"""The issue ledger: the single source of truth for one deliberation.

Agents never touch state directly. They emit moves; the ledger checks the moves are legal
(`check_*`), coerces what can safely be coerced when a repair attempt also fails (`coerce_*`),
and applies them (`apply_*`). Termination and the decision document are both computed
from this state, never from free text.
"""

import re
from collections import Counter
from typing import Literal

from pydantic import BaseModel

from .schemas import WEIGHT, CriticOpening, CriticTurn, NewChallenge, Proposal, ProposerTurn, Response, Verdict

Status = Literal["OPEN", "RESOLVED", "ESCALATED", "UNRESOLVED"]
SECTIONS = {"core_commitments": "V", "in_scope": "S", "out_of_scope": "X",
            "assumptions": "A", "definitions": "D", "success_criteria": "K"}
SETTLED_BY = {"DEFEND": "DEFENDED", "REVISE": "REVISED", "CONCEDE": "CONCEDED"}


class Event(BaseModel):
    round: int
    actor: Literal["proposer", "critic", "orchestrator"]
    move: str
    text: str
    grounds: str = ""          # the Proposer's triage of the challenge, for its moves
    changed: list[str] = []    # item IDs the Proposer changed with this move


class Issue(NewChallenge):
    id: str
    round_raised: int
    status: Status = "OPEN"
    strikes: int = 0
    history: list[Event] = []

    @property
    def outcome(self) -> str:
        """For a resolved issue, how it was settled: the Proposer's last move before the Critic accepted."""
        if self.status != "RESOLVED":
            return self.status
        moves = [e.move for e in self.history if e.actor == "proposer"]
        return SETTLED_BY.get(moves[-1], "RESOLVED") if moves else "RESOLVED"


class RoundStats(BaseModel):
    round: int
    raised: int
    open: int
    resolved: int
    escalated: int
    disagreement: float
    proposer_confidence: int
    critic_confidence: int
    proposer_worry: str
    critic_worry: str
    signal: str
    decision: str
    feedback: str


class Ledger(BaseModel):
    request: str
    gaps: list[str] = []  # the Critic's opening list of questions the request leaves open
    proposals: list[Proposal] = []
    issues: dict[str, Issue] = {}
    rounds: list[RoundStats] = []
    termination: str = ""
    warnings: list[str] = []

    # ------------------------------------------------------------ views

    @property
    def proposal(self) -> Proposal:
        return self.proposals[-1]

    def open_issues(self) -> list[Issue]:
        return [i for i in self.issues.values() if i.status == "OPEN"]

    def disagreement(self) -> float:
        """Severity-weighted share of raised issues not settled by agreement (open, escalated or unresolved)."""
        raised = sum(WEIGHT[i.severity] for i in self.issues.values())
        unsettled = sum(WEIGHT[i.severity] for i in self.issues.values() if i.status != "RESOLVED")
        return round(unsettled / raised, 2) if raised else 0.0

    def lenses_examined(self, coverage: list) -> set[str]:
        return {i.lens for i in self.issues.values()} | {note.lens for note in coverage}

    def changes(self, version: int = -1) -> dict[str, list[str]]:
        """Item IDs added, edited and removed by a proposal version (default: the latest)."""
        index = version % len(self.proposals)
        if index == 0:
            return {}
        before, after = self.proposals[index - 1].items(), self.proposals[index].items()
        return {"added": [k for k in after if k not in before],
                "edited": [k for k in after if k in before and after[k] != before[k]],
                "removed": [k for k in before if k not in after]}

    def dropped(self) -> dict[str, str]:
        """Items that existed in an earlier version but not in the final one, with their last wording."""
        final, out = self.proposal.items(), {}
        for version in self.proposals[:-1]:
            out |= {k: v for k, v in version.items().items() if k not in final}
        return out

    # ------------------------------------------------------------ legality checks

    def check_proposer(self, turn: ProposerTurn) -> list[str]:
        problems = _coverage([r.challenge_id for r in turn.responses], [i.id for i in self.open_issues()], "respond to")
        ids = []
        for section, prefix in SECTIONS.items():
            items = getattr(turn.proposal, section)
            ids += [i.id for i in items]
            if not items:
                problems.append(f"'{section}' is empty; every section needs at least one item.")
            if bad := [i.id for i in items if not re.fullmatch(prefix + r"\d+", i.id)]:
                problems.append(f"IDs in '{section}' must look like {prefix}1, {prefix}2; got {', '.join(bad)}.")
        if dupes := sorted({i for i in ids if ids.count(i) > 1}):
            problems.append(f"Duplicate IDs: {', '.join(dupes)}.")
        if self.proposals and (lost := self._lost_commitments(turn.proposal)):
            problems.append(f"Core commitments can't be dropped, only the stakeholder can do that: {', '.join(lost)}.")
        if self.proposals:
            before, after = self.proposal.items(), turn.proposal.items()
            edited = {k for k in after if before.get(k) != after[k]} | {k for k in before if k not in after}
            for r in turn.responses:
                if r.action != "DEFEND" and not set(r.changed_ids) & edited:
                    problems.append(f"{r.challenge_id}: grounds {r.grounds} mean the proposal must change, but none of the items "
                                    f"you listed ({', '.join(r.changed_ids) or 'none'}) changed. Write the decision into the item "
                                    f"itself, or choose other grounds.")
        return problems

    def check_critic(self, turn: CriticOpening | CriticTurn, rnd: int, budget: int) -> list[str]:
        new = turn.new_challenges
        if rnd == 1:
            problems = [] if len(new) >= 3 else ["Round 1: raise at least 3 challenges."]
            if len({c.lens for c in new}) < 2:
                problems.append("Round 1: cover at least 2 different lenses.")
        else:
            problems = _coverage([v.challenge_id for v in turn.verdicts], [i.id for i in self.open_issues()], "rule on")
        if len(new) > budget:
            problems.append(f"You raised {len(new)} new challenges; the budget this round is {budget}. Keep the most material.")
        valid = set(self.proposal.items()) | {"GAP"}
        for n, c in enumerate(new, 1):
            if not c.targets or set(c.targets) - valid:
                problems.append(f"New challenge #{n}: targets must be current item IDs or GAP; got {c.targets}.")
        for v in getattr(turn, "verdicts", []):
            if v.answered and v.challenge_id in self.issues and not self.supported(v):
                problems.append(f"{v.challenge_id}: you marked it answered, so `evidence` must be copied from the item text shown "
                                f"under the challenge (or, for a defense or concession, from the Proposer's answer), and "
                                f"\"{v.evidence[:80]}\" is not there. Quote the words that answer your question, or mark it "
                                f"not answered.")
        return problems

    def supported(self, verdict: Verdict) -> bool:
        """Is the evidence really there? A revision must show in a proposal item; a defense or concession may be
        evidenced by the Proposer's answer. At least 85% of the quote's words must appear in one of those texts, so
        punctuation, an ID prefix or a slipped word don't matter but a description of a change ("S1 now says...") fails."""
        answer = [e for e in self.issues[verdict.challenge_id].history if e.actor == "proposer"][-1:]
        texts = list(self.proposal.items().values()) + [e.text for e in answer if e.move != "REVISE"]
        words = _words(verdict.evidence).split()
        words = words[1:] if words and re.fullmatch(r"[a-z]\d+", words[0]) else words
        if len(words) < 4:
            return False
        return max(sum(w in set(_words(t).split()) for w in words) / len(words) for t in texts) >= 0.85

    # ------------------------------------------------------------ coercion (after a failed repair)

    def coerce_proposer(self, turn: ProposerTurn, rnd: int) -> ProposerTurn:
        responses = _dedupe(turn.responses, [i.id for i in self.open_issues()], lambda r: r.challenge_id)
        for cid in [i.id for i in self.open_issues() if i.id not in {r.challenge_id for r in responses}]:
            responses.append(Response(challenge_id=cid, grounds="ACCEPTABLE_RISK", changed_ids=[],
                                      rationale="(No response given; the current proposal stands.)"))
            self.warnings.append(f"R{rnd}: Proposer did not answer {cid}; recorded as DEFEND.")
        proposal = turn.proposal
        if self.proposals and (lost := self._lost_commitments(proposal)):
            restored = [v for v in self.proposal.core_commitments if v.id in lost]
            proposal = proposal.model_copy(update={"core_commitments": proposal.core_commitments + restored})
            self.warnings.append(f"R{rnd}: Proposer dropped core commitments {', '.join(lost)}; restored.")
        return turn.model_copy(update={"responses": responses, "proposal": proposal})

    def coerce_critic(self, turn: CriticOpening | CriticTurn, rnd: int, budget: int):
        new = turn.new_challenges
        if len(new) > budget:
            new = sorted(new, key=lambda c: -WEIGHT[c.severity])[:budget]
            self.warnings.append(f"R{rnd}: Critic exceeded its budget; kept the {budget} most severe challenge(s).")
        valid = set(self.proposal.items()) | {"GAP"}
        new = [c.model_copy(update={"targets": [t for t in c.targets if t in valid] or ["GAP"]}) for c in new]
        update = {"new_challenges": new}
        if rnd > 1:
            open_ids = [i.id for i in self.open_issues()]
            verdicts = _dedupe(turn.verdicts, open_ids, lambda v: v.challenge_id)
            for cid in [c for c in open_ids if c not in {v.challenge_id for v in verdicts}]:
                verdicts.append(Verdict(challenge_id=cid, answered=False, evidence="", needs_human_decision=False,
                                        rationale="(No ruling given.)"))
                self.warnings.append(f"R{rnd}: Critic did not rule on {cid}; recorded as MAINTAIN.")
            for n, v in enumerate(verdicts):
                if v.answered and not self.supported(v):
                    verdicts[n] = v.model_copy(update={"answered": False, "rationale": v.rationale +
                                                       " [Not counted as answered: the quoted evidence is not in the proposal.]"})
                    self.warnings.append(f"R{rnd}: Critic accepted {v.challenge_id} without evidence; recorded as not answered.")
            update["verdicts"] = verdicts
        return turn.model_copy(update=update)

    # ------------------------------------------------------------ transitions

    def apply_proposer(self, rnd: int, turn: ProposerTurn) -> None:
        for r in _dedupe(turn.responses, [i.id for i in self.open_issues()], lambda r: r.challenge_id):
            self.issues[r.challenge_id].history.append(Event(round=rnd, actor="proposer", move=r.action, grounds=r.grounds,
                                                             changed=r.changed_ids, text=r.rationale))
        self.proposals.append(turn.proposal)

    def apply_critic(self, rnd: int, turn: CriticOpening | CriticTurn, strike_limit: int | None) -> None:
        self.gaps += getattr(turn, "gaps", [])
        for v in _dedupe(getattr(turn, "verdicts", []), [i.id for i in self.open_issues()], lambda v: v.challenge_id):
            issue = self.issues[v.challenge_id]
            evidence = f' Evidence: "{v.evidence}"' if v.ruling == "ACCEPT" else ""
            issue.history.append(Event(round=rnd, actor="critic", move=v.ruling, text=v.rationale + evidence))
            if v.ruling == "ACCEPT":
                issue.status = "RESOLVED"
            elif v.ruling == "ESCALATE":
                issue.status = "ESCALATED"
            else:
                issue.strikes += 1
                if strike_limit and issue.strikes >= strike_limit:
                    issue.status = "ESCALATED"
                    issue.history.append(Event(round=rnd, actor="orchestrator", move="AUTO_ESCALATE",
                                               text=f"Maintained {issue.strikes} times without agreement; handed to human decision-makers."))
        for c in turn.new_challenges:
            cid = f"C{len(self.issues) + 1}"
            self.issues[cid] = Issue(id=cid, round_raised=rnd, **c.model_dump(),
                                     history=[Event(round=rnd, actor="critic", move="RAISE", text=c.challenge)])

    def record(self, rnd: int, proposer: ProposerTurn, critic: CriticOpening | CriticTurn, reason: str, feedback: str) -> None:
        count = Counter(i.status for i in self.issues.values())
        self.rounds.append(RoundStats(
            round=rnd, raised=len(self.issues), open=count["OPEN"], resolved=count["RESOLVED"], escalated=count["ESCALATED"],
            disagreement=self.disagreement(), proposer_confidence=proposer.confidence, critic_confidence=critic.confidence,
            proposer_worry=proposer.biggest_worry, critic_worry=critic.biggest_worry,
            signal=getattr(critic, "signal", "-"), decision=reason or "continue", feedback=feedback))

    def close(self, reason: str) -> None:
        self.termination = reason
        last = self.rounds[-1].round if self.rounds else 0
        for issue in self.open_issues():
            issue.status = "UNRESOLVED"
            issue.history.append(Event(round=last, actor="orchestrator", move="OPEN_AT_CLOSE",
                                       text=f"Still open when deliberation ended ({reason})."))

    def _lost_commitments(self, proposal: Proposal) -> list[str]:
        kept = {v.id for v in proposal.core_commitments}
        return [v.id for v in self.proposal.core_commitments if v.id not in kept]


def _coverage(got: list[str], expected: list[str], verb: str) -> list[str]:
    problems = []
    if missing := [e for e in expected if e not in got]:
        problems.append(f"You must {verb} every open challenge exactly once; missing: {', '.join(missing)}.")
    if dupes := sorted({g for g in got if got.count(g) > 1}):
        problems.append(f"Answered more than once: {', '.join(dupes)}.")
    return problems


def _words(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _dedupe(moves: list, allowed: list[str], key) -> list:
    seen, out = set(), []
    for m in moves:
        if key(m) in allowed and key(m) not in seen:
            seen.add(key(m))
            out.append(m)
    return out
