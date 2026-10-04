"""The three roles. All prompt wording lives in prompts/*.md; this module fills in the blanks
and enforces the contract on every reply: validate -> one repair attempt -> coerce."""

import re
from collections.abc import Callable
from pathlib import Path

from pydantic import BaseModel, ValidationError

from .ledger import Ledger
from .llm import LLM
from .render import issue_md, proposal_md
from .schemas import MANDATORY_LENSES, SECTIONS, CriticOpening, CriticTurn, ProposerOpening, ProposerTurn, Synthesis, section_of
from .termination import Policy

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "prompts"


def fill(template: str, **values: str) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    if leftover := re.findall(r"{{\s*\w+\s*}}", template):
        raise ValueError(f"Unfilled prompt placeholders: {leftover}")
    return template


class Agents:
    def __init__(self, context: str, llms: dict[str, LLM], log: Callable[[dict], None], prompt_dirs: list[Path] = ()):
        self.dirs = [*prompt_dirs, PROMPTS]  # a variant directory may override any prompt file
        self.llms, self.log = llms, log
        self.system = {role: fill(self._load(f"{role}.system.md"), system_context=context) for role in llms}

    def _load(self, name: str) -> str:
        return next(d / name for d in self.dirs if (d / name).exists()).read_text()

    # ---------------------------------------------------------------- roles

    def propose(self, ledger: Ledger, rnd: int) -> ProposerOpening | ProposerTurn:
        if rnd == 1:
            schema, state, task = ProposerOpening, "No proposal yet.", "Write your initial proposal."
        else:
            schema = ProposerTurn
            ids = ", ".join(ledger.next_id(s) for s in SECTIONS)
            state = f"## Your current proposal\n{proposal_md(ledger.proposal)}\n\nIDs for new items start at: {ids}.\n\n" \
                    "## Open challenges\n" + "\n\n".join(issue_md(i) for i in ledger.open_issues()) + settled_view(ledger)
            task = ("Answer every open challenge exactly once and name its `grounds`, which decide your move. For a revision "
                    "or concession, `edits` holds the complete new wording of each item you change (empty text removes an "
                    "item); for a defense it is empty. Items you don't edit stay exactly as they are.")
        turn, ok = self._turn("proposer", rnd, ledger, schema, ledger.check_proposer, state, task)
        return turn if ok else ledger.coerce_proposer(turn, rnd)

    def critique(self, ledger: Ledger, rnd: int, policy: Policy, feedback: str) -> CriticOpening | CriticTurn:
        budget = policy.budget(rnd)
        proposal = f"## Current proposal (version {rnd})\n{proposal_md(ledger.proposal)}"
        if rnd == 1:
            schema, state = CriticOpening, proposal
            task = ("Write your pre-mortem, then list the questions the request leaves open (`gaps`). Then raise one "
                    f"challenge for each gap the proposal leaves unanswered or answers badly, up to {budget}, most material "
                    "first and covering at least 2 lenses: if the proposal doesn't prevent your pre-mortem, start there. "
                    "You cannot conclude in round 1.")
        else:
            schema = CriticTurn
            changes = "; ".join(f"{k}: {', '.join(v)}" for k, v in ledger.changes().items() if v) or "none"
            state = (f"{proposal}\n\nChanges since last round: {changes}\n\n## Challenges the Proposer just answered\n"
                     + "\n\n".join(answered_view(ledger, i) for i in ledger.open_issues()) + settled_view(ledger))
            if ledger.pre_mortem:
                state += f"\n\n## Your pre-mortem from round 1\n{ledger.pre_mortem}"
            if feedback:
                state += f"\n\n## Note from the moderator\n{feedback}"
            uncovered = [lens for lens in MANDATORY_LENSES if lens not in ledger.lenses_examined([])]
            task = (f"Rule on every answered challenge exactly once: quote the words that come closest to answering your test, "
                    f"name the fact they commit to, and judge whether that answers your test and stops your failure scenario. "
                    f"Then raise at most {budget} new challenge(s), only for material problems (none is fine). "
                    f"Then signal CONCLUDE if no BLOCKER or MAJOR challenge stays open after your rulings and you raise no "
                    f"new one (escalated challenges are with humans now and don't keep the deliberation open); otherwise "
                    f"CONTINUE. Mandatory lenses with no challenge so far: {', '.join(uncovered) or 'none'}; if you conclude, "
                    f"add a lens_coverage note for each of them.")
        turn, ok = self._turn("critic", rnd, ledger, schema, lambda t: ledger.check_critic(t, rnd, budget), state, task)
        return turn if ok else ledger.coerce_critic(turn, rnd, budget)

    def synthesize(self, ledger: Ledger) -> Synthesis:
        user = fill(self._load("summarizer.turn.md"), request=ledger.request, record=record_view(ledger))
        synthesis, ok = self._call("summarizer", 0, user, Synthesis, lambda s: check_synthesis(s, ledger))
        return synthesis if ok else coerce_synthesis(synthesis, ledger)

    # ---------------------------------------------------------------- plumbing

    def _turn(self, role, rnd, ledger, schema, check, state, task):
        user = fill(self._load(f"{role}.turn.md"), request=ledger.request, round=str(rnd), state=state, task=task)
        return self._call(role, rnd, user, schema, check)

    def _call(self, role: str, rnd: int, user: str, schema: type[BaseModel], check) -> tuple[BaseModel, bool]:
        """Returns (value, ok). ok=False means the repair attempt also broke a rule and the caller must coerce."""
        messages = [{"role": "user", "content": user}]
        for attempt in (1, 2):
            out = self.llms[role].complete(self.system[role], messages, schema)
            self.log({"kind": "llm", "role": role, "round": rnd, "attempt": attempt, "model": out.model,
                      "input_tokens": out.input_tokens, "output_tokens": out.output_tokens, "raw": out.raw})
            try:
                value = schema.model_validate_json(out.raw)
                problems = check(value)
            except ValidationError as e:
                value, problems = None, [f"The JSON did not match the schema: {e.errors()[0]['msg']} at {e.errors()[0]['loc']}"]
            if not problems:
                return value, True
            self.log({"kind": "violation", "role": role, "round": rnd, "attempt": attempt, "problems": problems})
            if attempt == 1:
                messages += [{"role": "assistant", "content": out.raw},
                             {"role": "user", "content": fill(self._load("repair.md"), problems="\n".join(f"- {p}" for p in problems))}]
        if value is None:
            raise RuntimeError(f"{role} returned invalid JSON twice in round {rnd}: {problems}")
        return value, False


# -------------------------------------------------------------------- views (what each agent sees)


def answered_view(ledger: Ledger, issue) -> str:
    """An answered challenge plus the current text of the items it touches, so the Critic can check and quote them."""
    items = ledger.proposal.items()
    last = [e for e in issue.history if e.actor == "proposer"][-1:]
    ids = [k for k in dict.fromkeys([*(last[0].changed if last else []), *issue.targets]) if section_of(k)]
    shown = [f"  - {k}: {items.get(k, '(removed)')}" for k in ids]
    return issue_md(issue) + ("\n- Items as they now read:\n" + "\n".join(shown) if shown else "")


def settled_view(ledger: Ledger) -> str:
    settled = [i for i in ledger.issues.values() if i.status != "OPEN"]
    if not settled:
        return ""
    return "\n\n## Settled (do not re-raise unless the proposal changed)\n" + \
        "\n".join(f"- {i.id} {i.outcome} · {i.severity} · {i.challenge}" for i in settled)


def record_view(ledger: Ledger) -> str:
    stats = ledger.rounds[-1]
    dropped = "\n".join(f"- {k}: {v}" for k, v in ledger.dropped().items()) or "none"
    needing = [i.id for i in ledger.issues.values() if i.status in ("ESCALATED", "UNRESOLVED")]
    return "\n\n".join([
        f"Ended after {stats.round} rounds ({ledger.termination}).",
        f"## Final proposal\n{proposal_md(ledger.proposal)}",
        f"## Items dropped during deliberation (last wording)\n{dropped}",
        "## Issues (final status and full history)\n" + "\n\n".join(f"[{i.status}] {issue_md(i)}" for i in ledger.issues.values()),
        f"## Issues that need an open question\n{', '.join(needing) or 'none'}",
        f"## Final positions\nProposer: {stats.proposer_confidence}/100 confident; worry: {stats.proposer_worry}\n"
        f"Critic: {stats.critic_confidence}/100 confident; worry: {stats.critic_worry}",
    ])


# -------------------------------------------------------------------- summarizer contract


def _known_ids(ledger: Ledger) -> set[str]:
    return set(ledger.issues) | {k for p in ledger.proposals for k in p.items()}


def check_synthesis(s: Synthesis, ledger: Ledger) -> list[str]:
    known, final = _known_ids(ledger), set(ledger.proposal.items())
    needing = {i.id for i in ledger.issues.values() if i.status in ("ESCALATED", "UNRESOLVED")}
    problems = []
    if bad := sorted({n.id for n in s.item_notes} - final):
        problems.append(f"item_notes may only use IDs of items in the final proposal (explain dropped items under "
                        f"`rejected` instead); not in the final proposal: {', '.join(bad)}.")
    refs = [r for n in s.item_notes for r in n.refs] + [r for x in s.rejected for r in x.refs]
    if bad := sorted(set(refs) - known):
        problems.append(f"These refs are not in the record: {', '.join(bad)}.")
    asked = [q.issue_id for q in s.open_questions]
    if missing := sorted(needing - set(asked)):
        problems.append(f"Write one open question for each of: {', '.join(missing)}.")
    if extra := sorted(set(asked) - needing):
        problems.append(f"Only escalated or unresolved issues get open questions; remove: {', '.join(extra)}.")
    if uncovered := sorted(set(ledger.dropped()) - set(refs)):
        problems.append(f"Explain the dropped items in `rejected`: {', '.join(uncovered)}.")
    return problems


def coerce_synthesis(s: Synthesis, ledger: Ledger) -> Synthesis:
    from .schemas import OpenQuestion, Rejected

    known, final = _known_ids(ledger), set(ledger.proposal.items())
    notes = [n.model_copy(update={"refs": [r for r in n.refs if r in known]}) for n in s.item_notes if n.id in final]
    rejected = [x.model_copy(update={"refs": [r for r in x.refs if r in known]}) for x in s.rejected]
    covered = {r for x in rejected for r in x.refs}
    rejected += [Rejected(what=text, why="Dropped during deliberation; see the issue history.", refs=[k])
                 for k, text in ledger.dropped().items() if k not in covered]
    questions = [q for q in s.open_questions if ledger.issues.get(q.issue_id) and ledger.issues[q.issue_id].status in ("ESCALATED", "UNRESOLVED")]
    asked = {q.issue_id for q in questions}
    questions += [OpenQuestion(issue_id=i.id, question=i.challenge, why_it_matters=i.failure_scenario,
                               decision_owner="To be assigned", options=[i.resolution_test], blocks_build=i.severity == "BLOCKER")
                  for i in ledger.issues.values() if i.status in ("ESCALATED", "UNRESOLVED") and i.id not in asked]
    ledger.warnings.append("Summarizer output needed coercion after a failed repair; see events.jsonl.")
    return s.model_copy(update={"item_notes": notes, "rejected": rejected, "open_questions": questions})
