"""The issue ledger: the single source of truth for one deliberation.

Agents never touch state directly. They emit moves; the ledger checks the moves are legal
(`check_*`), coerces what can safely be coerced when a repair attempt also fails (`coerce_*`),
and applies them (`apply_*`). Termination and the decision document are both computed
from this state, never from free text.
"""

import re
from collections import Counter
from difflib import SequenceMatcher
from typing import Literal

from pydantic import BaseModel

from .schemas import (SECTIONS, WEIGHT, CriticOpening, CriticTurn, Edit, Item, NewChallenge, Proposal, ProposerOpening,
                      ProposerTurn, Response, Verdict, section_of)

Status = Literal["OPEN", "RESOLVED", "ESCALATED", "UNRESOLVED"]
SETTLED_BY = {"DEFEND": "DEFENDED", "REVISE": "REVISED", "CONCEDE": "CONCEDED"}

# Phrases that sound like a decision but decide nothing: the "weak phrases" requirements-quality tools have flagged
# since NASA's ARM tool. This is the subset the Critic accepted as evidence in the v5–v7 batches. A promise is weak
# wherever it appears, except where it goes on to say what or when ("will be determined by <rule>", "will be developed
# in a later release", "a periodic digest every Monday"). An unnamed role is weak unless the same words name a role
# after all ("authorized users, specifically regional coordinators and project managers"). "Protocol", "mechanism" or
# "periodic" alone are left out: real answers use them ("the protocol officer").
PROMISE = re.compile(r"\b(?:" + "|".join([
    r"will be (?:established|developed|defined|determined|agreed|put in place|set up|clarified)"
    r"(?!\s+(?:by|as|in\s+(?:a\s+|the\s+)?(?:later|future|subsequent|next))\b)",
    r"periodic (?:audits?|reviews?|checks?)(?!\s+every\b)", r"clearly defined", r"defined consistently",
    r"(?:safeguards|measures|controls|processes|procedures) (?:are |will be )?in place", r"measures to",
    r"including but not limited to",
]) + r")\b", re.I)
UNNAMED = re.compile(r"\b(?:appropriate(?:ly)?|designated (?:teams?|managers?|committees?|staff|personnel|users?|roles?|"
                     r"oversight)|authori[sz]ed (?:users|personnel|recipients|staff|individuals))\b", re.I)
ROLE = re.compile(r"\b(?:coordinator|manager|executive|officer|director|representative|delegate|administrator|head|lead)s?\b",
                  re.I)


def weak_phrase(words: str) -> str:
    """The weak phrase these words lean on, or ""."""
    if promise := PROMISE.search(words):
        return promise.group(0)
    unnamed = UNNAMED.search(words)
    return unnamed.group(0) if unnamed and not ROLE.search(UNNAMED.sub(" ", words)) else ""


class Event(BaseModel):
    round: int
    actor: Literal["proposer", "critic", "orchestrator"]
    move: str
    text: str
    grounds: str = ""          # the Proposer's triage of the challenge, for its moves
    changed: list[str] = []    # item IDs the Proposer's edits changed with this move


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
    pre_mortem: str = ""   # the Critic's opening: the incident this feature could cause a year after launch
    gaps: list[str] = []   # the Critic's opening: questions the request leaves open
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

    def next_id(self, section: str, *also: Proposal) -> str:
        """The next number a section has never used, across every version (and any proposal passed in)."""
        used = [int(k[1:]) for v in [*self.proposals, *also] for k in v.items() if section_of(k) == section]
        return f"{SECTIONS[section]}{max(used, default=0) + 1}"

    def dropped(self) -> dict[str, str]:
        """Items that existed in an earlier version but not in the final one, with their last wording."""
        final, out = self.proposal.items(), {}
        for version in self.proposals[:-1]:
            out |= {k: v for k, v in version.items().items() if k not in final}
        return out

    # ------------------------------------------------------------ legality checks

    def check_proposer(self, turn: ProposerOpening | ProposerTurn) -> list[str]:
        if isinstance(turn, ProposerOpening):
            return _section_problems(turn.proposal)
        open_ids = [i.id for i in self.open_issues()]
        problems = _coverage([r.challenge_id for r in turn.responses], open_ids, "respond to")
        return problems + self._vet(_dedupe(turn.responses, open_ids, lambda r: r.challenge_id))[1]

    def check_critic(self, turn: CriticOpening | CriticTurn, rnd: int, budget: int) -> list[str]:
        new = turn.new_challenges
        if rnd == 1:
            need = min(budget, max(3, len(turn.gaps)))
            problems = [] if len(new) >= need else [
                f"Round 1: `gaps` lists {len(turn.gaps)} questions the proposal answers badly or not at all, so raise a "
                f"challenge for each (at least {need}, at most {budget}, never fewer than 3). If the proposal already "
                f"answers one, remove it from `gaps`."]
            if len({c.lens for c in new}) < 2:
                problems.append("Round 1: cover at least 2 different lenses.")
        else:
            problems = _coverage([v.challenge_id for v in turn.verdicts], [i.id for i in self.open_issues()], "rule on")
        if len(new) > budget:
            problems.append(f"You raised {len(new)} new challenges; the budget this round is {budget}. Keep the most material.")
        valid = set(self.proposal.items()) | {"GAP"} | set(self.issues)  # a follow-up may name the challenge it follows
        for n, c in enumerate(new, 1):
            if not c.targets or set(c.targets) - valid:
                problems.append(f"New challenge #{n}: targets must be current item IDs or GAP; got {c.targets}.")
            if not c.resolution_test.strip().endswith("?"):
                problems.append(f"New challenge #{n}: the resolution test must be a question with a concrete answer (a role, "
                                f"a number, a rule or yes/no), ending with '?'; got \"{c.resolution_test[:70]}\".")
        for n, earlier in self._repeats(new):
            if earlier in self.issues and self.issues[earlier].status == "ESCALATED":
                problems.append(f"New challenge #{n} asks the same question as {earlier}, which is with human decision-makers "
                                f"now; a new challenge must ask something else.")
            else:
                problems.append(f"New challenge #{n} asks the same question as {earlier}. To keep pressing it, rule MAINTAIN "
                                f"on it; a new challenge must ask something else.")
        open_ids = {i.id for i in self.open_issues()}  # rulings on closed issues are ignored, so they cost no repair
        problems += [p for v in getattr(turn, "verdicts", []) if v.challenge_id in open_ids and (p := self.verdict_problem(v))]
        return problems

    def verdict_problem(self, v: Verdict) -> str:
        """Why an ACCEPT can't stand, or "": it needs a concrete fact, and evidence that is really in a decided item
        (or, for a defense or concession, in the Proposer's answer)."""
        if v.ruling != "ACCEPT" or v.challenge_id not in self.issues:
            return ""
        cid, answer = v.challenge_id, self._last_answer(v.challenge_id)
        if answer and answer.grounds == "NEEDS_HUMAN_DECISION":
            return (f"{cid}: the Proposer answered that it needs a human decision, so it can't be settled here. Mark it not "
                    f"settled, and set needs_human_decision if you agree (ESCALATE) or leave it unset if it is a rule you two "
                    f"can decide (MAINTAIN).")
        if re.match(r"\W*(no fact\b|n/?a\W*$|$)", v.fact, flags=re.I):
            return (f"{cid}: you marked it settled, but `fact` is '{v.fact}'. Words that only promise or name no one specific "
                    f"don't settle a test: name the fact they commit to, or mark it not settled.")
        if len(_quote_words(v.evidence)) < 4:
            return (f"{cid}: you marked it settled, so `evidence` must quote at least four consecutive words from the item "
                    f"text (or, for a defense or concession, from the Proposer's answer), so they can be found.")
        source = self.evidence_source(v)
        if not source:
            return (f"{cid}: you marked it settled, so `evidence` must be copied from the item text shown under the challenge "
                    f"(or, for a defense or concession, from the Proposer's answer), and \"{v.evidence[:80]}\" is not there. "
                    f"Quote the words that settle your test, or mark it not settled.")
        if source.startswith("A"):
            return (f"{cid}: your evidence comes from assumption {source}. An assumption is what the release depends on, not "
                    f"what it decides, so it can't settle a challenge: quote a V, S, X, D or K item, or mark it not settled.")
        if weak := self._weak_phrase(v, source):
            return (f"{cid}: the sentence you quote leans on '{weak}', which names no role, number or rule. Quote a "
                    f"sentence that states the fact; if there is none, mark it not settled.")
        return ""

    def _weak_phrase(self, v: Verdict, source: str) -> str:
        """A weak phrase in the quoted words or in the few words that govern them ("A process will be established to
        [reassign alerts...]"), so trimming the quote doesn't hide it; what comes after the quote is not its business.
        Checked for items and for acceptable-risk defenses, whose mitigation must be real; not for other defenses
        ("decided in design", "covered by S3"), where deferring is the point."""
        answer = self._last_answer(v.challenge_id)
        if source == "answer":
            text = answer.text if answer and answer.grounds == "ACCEPTABLE_RISK" else ""
        else:
            text = self.proposal.items()[source]
        words, sentence_starts, text_words = _quote_words(v.evidence), [], []
        for sentence in re.split(r"(?<=[.;!?])\s+", text):
            sentence_starts.append(len(text_words))
            text_words += _words(sentence).split()
        blocks = [b for b in SequenceMatcher(None, words, text_words, autojunk=False).get_matching_blocks() if b.size]
        if not blocks:
            return ""
        start, end = blocks[0].b, blocks[-1].b + blocks[-1].size
        start = max(start - 6, max(s for s in sentence_starts if s <= start))
        return weak_phrase(" ".join(text_words[start:end]))

    def _last_answer(self, cid: str) -> Event | None:
        answers = [e for e in self.issues[cid].history if e.actor == "proposer"]
        return answers[-1] if answers else None

    def _repeats(self, new: list) -> list[tuple[int, str]]:
        """New challenges (by number) whose resolution test repeats an open or escalated issue's, or an earlier new one's.
        A resolved issue may be raised again: the proposal can change in a way that reopens it."""
        tests = [(i.id, i.resolution_test) for i in self.issues.values() if i.status in ("OPEN", "ESCALATED")]
        out = []
        for n, c in enumerate(new, 1):
            if earlier := next((k for k, t in tests if _same_question(c.resolution_test, t)), None):
                out.append((n, earlier))
            tests.append((f"new challenge #{n}", c.resolution_test))
        return out

    def evidence_source(self, verdict: Verdict) -> str:
        """Where the quoted evidence really is: an item ID, "answer" (the Proposer's answer to a defense or concession; a
        revision must show in the proposal), or "" if nowhere. At least 85% of the quote's words must appear in one text,
        in order, so punctuation, an ID prefix or a slipped word don't matter, but a paraphrase or a description of a
        change ("S1 now says...") fails. The best match wins; on a tie a decided item beats an assumption, and an assumption beats an answer that
        only repeats it, so an assumption can't be smuggled in through a defense."""
        answer = self._last_answer(verdict.challenge_id)
        texts = self.proposal.items() | ({"answer": answer.text} if answer and answer.move != "REVISE" else {})
        words = _quote_words(verdict.evidence)
        if len(words) < 4:
            return ""
        share = {k: _share(words, t) for k, t in texts.items()}
        rank = {k: (share[k], 0 if k == "answer" else 1 if k.startswith("A") else 2) for k in texts}
        best = max(texts, key=rank.get)
        return best if share[best] >= 0.85 else ""

    # ------------------------------------------------------------ coercion (after a failed repair)

    def coerce_proposer(self, turn: ProposerOpening | ProposerTurn, rnd: int) -> ProposerOpening | ProposerTurn:
        if isinstance(turn, ProposerOpening):  # nothing refers to its IDs yet, so they can safely be renumbered
            problems = " ".join(_section_problems(turn.proposal))
            renumbered = {s: [Item(id=f"{prefix}{n}", text=t) for n, t in enumerate(
                [i.text for i in getattr(turn.proposal, s) if i.text.strip()], 1)] for s, prefix in SECTIONS.items()}
            self.warnings.append(f"R{rnd}: the opening proposal still broke these rules after a repair: {problems} "
                                 f"Blank items were dropped and the rest renumbered by section.")
            return turn.model_copy(update={"proposal": turn.proposal.model_copy(update=renumbered)})
        open_ids = [i.id for i in self.open_issues()]
        responses = _dedupe(turn.responses, open_ids, lambda r: r.challenge_id)
        for cid in [c for c in open_ids if c not in {r.challenge_id for r in responses}]:
            responses.append(Response(challenge_id=cid, grounds="ACCEPTABLE_RISK", edits=[],
                                      rationale="(No response given; the current proposal stands.)"))
            self.warnings.append(f"R{rnd}: Proposer did not answer {cid}; recorded as DEFEND.")
        responses, problems = self._vet(responses)
        if problems:
            self.warnings.append(f"R{rnd}: the Proposer's turn still broke these rules after a repair (illegal edits dropped, "
                                 f"mislabelled moves corrected, the rest recorded as given): " + " ".join(problems))
        for n, r in enumerate(responses):
            if r.action == "CONCEDE" and r.edits and not _drops(r.edits):  # it added or changed items: a revision
                r = r.model_copy(update={"grounds": "MISSING_DECISION"})
                self.warnings.append(f"R{rnd}: Proposer's CONCEDE of {r.challenge_id} dropped nothing; recorded as REVISE.")
            elif r.action == "REVISE" and _only_removes(r.edits):  # nothing left to quote: a concession
                r = r.model_copy(update={"grounds": "SHOULD_NOT_BUILD"})
                self.warnings.append(f"R{rnd}: Proposer's REVISE of {r.challenge_id} only removed items; recorded as CONCEDE.")
            if r.action == "REVISE" and all(section_of(e.id) == "assumptions" for e in r.edits):
                r = r.model_copy(update={"edits": []})  # assumptions alone settle nothing (this also covers no edits)
            if r.action != "DEFEND" and not r.edits:  # a revision or concession with no legal edit left changed nothing
                r = Response(challenge_id=r.challenge_id, grounds="ACCEPTABLE_RISK", edits=[],
                             rationale="(No usable answer: its edits broke the rules twice; the proposal stands.)")
                self.warnings.append(f"R{rnd}: Proposer's answer to {r.challenge_id} had no legal edit; recorded as DEFEND.")
            responses[n] = r
        return turn.model_copy(update={"responses": responses})

    def _vet(self, responses: list[Response]) -> tuple[list[Response], list[str]]:
        """The responses with only their legal edits, plus one problem per broken rule. A defense leaves the proposal
        as it is; a revision or concession must change at least one item; each edit must pass `_edit_problem`."""
        after, wording, problems, vetted = self.proposal, {}, [], []
        for r in responses:
            defend = r.action == "DEFEND"
            if defend and r.edits:
                problems.append(f"{r.challenge_id}: grounds {r.grounds} mean DEFEND, which leaves the proposal as it is, so "
                                f"`edits` must be empty. If an item has to change, the grounds are MISSING_DECISION or "
                                f"SHOULD_NOT_BUILD.")
            if not defend and not r.edits:
                problems.append(f"{r.challenge_id}: grounds {r.grounds} mean {r.action}, so `edits` must change at least one "
                                f"item. Write the decision into the item itself, or choose other grounds.")
            kept, snapshot = [], (after, dict(wording))
            for e in [] if defend else r.edits:
                if problem := self._edit_problem(e, after, wording):
                    problems.append(f"{r.challenge_id}: {problem}.")
                else:
                    kept.append(e)
                    wording[e.id], after = e.text.strip(), after.edited([e])
            if r.action == "REVISE" and kept and all(section_of(e.id) == "assumptions" for e in kept):
                problems.append(f"{r.challenge_id}: your edits only change assumptions, and an assumption can't settle a "
                                f"challenge: it is what the release depends on, not what it decides. Write the decision into a "
                                f"V, S, X, D or K item; if only the organisation can decide it, the grounds are "
                                f"NEEDS_HUMAN_DECISION.")
                kept, (after, wording) = [], snapshot  # none of it is applied
            if r.action == "CONCEDE" and kept and not _drops(kept):
                problems.append(f"{r.challenge_id}: a concession drops or descopes something: remove an item, or add or edit an "
                                f"out-of-scope item. If you are adding a rule, the grounds are MISSING_DECISION.")
            if r.action == "REVISE" and _only_removes(kept):
                problems.append(f"{r.challenge_id}: your edits only remove items, which is a concession: the grounds are "
                                f"SHOULD_NOT_BUILD. A revision writes a decision into an item.")
            vetted.append(r.model_copy(update={"edits": kept}))
        if emptied := [s for s in SECTIONS if getattr(self.proposal, s) and not getattr(after, s)]:
            gone = {e.id for r in vetted for e in r.edits if not e.text.strip() and section_of(e.id) in emptied}
            problems += [f"Removing {', '.join(sorted(k for k in gone if section_of(k) == s))} would leave '{s}' empty; every "
                         f"section keeps at least one item." for s in emptied]
            vetted = [r.model_copy(update={"edits": [e for e in r.edits if e.text.strip() or e.id not in gone]})
                      for r in vetted]
        return vetted, problems

    def _edit_problem(self, e: Edit, after: Proposal, wording: dict[str, str]) -> str:
        """Why an edit is illegal, or "" if it is fine. `after` is the proposal with this turn's earlier legal edits
        applied, and `wording` the text those edits gave each item. Several answers may edit one item: edits apply in
        order, so the later wording replaces the earlier and the Critic judges the result. A new item may be refined
        that way, but a later wording that drops the earlier one's words is a different item and needs its own ID.
        Emptied sections are checked once, in `_vet`."""
        before, text, section = self.proposal.items(), e.text.strip(), section_of(e.id)
        if section is None:
            return f"'{e.id}' is not an item ID; use a section letter (V, S, X, A, D or K) and a number"
        if not text and section == "core_commitments":
            return f"core commitments can't be removed; only the stakeholder can drop {e.id}"
        if not text and e.id not in before:
            return f"there is no {e.id} to remove"
        if e.id in self.dropped():
            return (f"{e.id} belonged to an item removed earlier; a new item takes a number its section has never used "
                    f"({self.next_id(section, after)})")
        if text == before.get(e.id, "").strip():
            return f"the edit leaves {e.id} exactly as it was"
        if e.id in wording and bool(text) != bool(wording[e.id]):
            return f"{e.id} is removed by one answer and rewritten by another in this turn; an item is either kept or removed"
        if e.id in wording and e.id not in before and not _keeps(wording[e.id], text):
            return f"{e.id} is already the ID of a different new item in this turn; give this one {self.next_id(section, after)}"
        return ""

    def coerce_critic(self, turn: CriticOpening | CriticTurn, rnd: int, budget: int):
        new = turn.new_challenges
        if repeats := self._repeats(new):  # before the budget cut, so a repeat never displaces a real challenge
            new = [c for n, c in enumerate(new, 1) if n not in {r for r, _ in repeats}]
            self.warnings.append(f"R{rnd}: dropped new challenge(s) that repeated an open question: "
                                 + ", ".join(f"#{n} ({earlier})" for n, earlier in repeats) + ".")
        if len(new) > budget:
            new = sorted(new, key=lambda c: -WEIGHT[c.severity])[:budget]
            self.warnings.append(f"R{rnd}: Critic exceeded its budget; kept the {budget} most severe challenge(s).")
        valid = set(self.proposal.items()) | {"GAP"} | set(self.issues)
        new = [c.model_copy(update={"targets": [t for t in c.targets if t in valid] or ["GAP"]}) for c in new]
        if unasked := [n for n, c in enumerate(new, 1) if not c.resolution_test.strip().endswith("?")]:
            new = [c.model_copy(update={"resolution_test": c.resolution_test.strip().rstrip(".") + "?"})
                   if n in unasked else c for n, c in enumerate(new, 1)]
            self.warnings.append(f"R{rnd}: resolution test(s) of new challenge(s) {', '.join(f'#{n}' for n in unasked)} "
                                 f"were not phrased as questions; kept as written.")
        update = {"new_challenges": new}
        if rnd > 1:
            open_ids = [i.id for i in self.open_issues()]
            verdicts = _dedupe(turn.verdicts, open_ids, lambda v: v.challenge_id)
            for cid in [c for c in open_ids if c not in {v.challenge_id for v in verdicts}]:
                verdicts.append(Verdict(challenge_id=cid, evidence="", fact="no fact", settled=False, unconfirmed=False,
                                        needs_human_decision=False, rationale="(No ruling given.)"))
                self.warnings.append(f"R{rnd}: Critic did not rule on {cid}; recorded as MAINTAIN.")
            for n, v in enumerate(verdicts):
                if problem := self.verdict_problem(v):  # not settled; the Critic's own judgement still routes it
                    reason = re.sub(r"^C\d+: ", "", problem).split(". ")[0].rstrip(".")
                    verdicts[n] = v.model_copy(update={"settled": False,
                                                       "rationale": f"{v.rationale} [Not counted as settled: {reason}.]"})
                    self.warnings.append(f"R{rnd}: Critic's ACCEPT of {v.challenge_id} was refused ({reason}); recorded as "
                                         f"{verdicts[n].ruling}.")
            update["verdicts"] = verdicts
        return turn.model_copy(update=update)

    # ------------------------------------------------------------ transitions

    def apply_proposer(self, rnd: int, turn: ProposerOpening | ProposerTurn) -> None:
        if isinstance(turn, ProposerOpening):
            self.proposals.append(turn.proposal)
            return
        responses = _dedupe(turn.responses, [i.id for i in self.open_issues()], lambda r: r.challenge_id)
        for r in responses:
            self.issues[r.challenge_id].history.append(Event(round=rnd, actor="proposer", move=r.action, grounds=r.grounds,
                                                             changed=[e.id for e in r.edits], text=r.rationale))
        version = self.proposal.edited([e for r in responses for e in r.edits])
        self.proposals.append(version.model_copy(update={"summary": turn.summary.strip() or self.proposal.summary}))

    def apply_critic(self, rnd: int, turn: CriticOpening | CriticTurn, strike_limit: int | None) -> None:
        if isinstance(turn, CriticOpening):
            self.pre_mortem, self.gaps = turn.pre_mortem, turn.gaps
        for v in _dedupe(getattr(turn, "verdicts", []), [i.id for i in self.open_issues()], lambda v: v.challenge_id):
            issue = self.issues[v.challenge_id]
            evidence = f' Fact: {v.fact.rstrip(".")}. Evidence: "{v.evidence}"' if v.ruling == "ACCEPT" else ""
            issue.history.append(Event(round=rnd, actor="critic", move=v.ruling, text=(v.rationale + evidence).strip()))
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
            targets = [t for target in c.targets for t in (self.issues[target].targets if target in self.issues else [target])]
            self.issues[cid] = Issue(id=cid, round_raised=rnd, **{**c.model_dump(), "targets": list(dict.fromkeys(targets))},
                                     history=[Event(round=rnd, actor="critic", move="RAISE", text=c.challenge)])

    def record(self, rnd: int, proposer: ProposerOpening | ProposerTurn, critic: CriticOpening | CriticTurn,
               reason: str, feedback: str) -> None:
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


def _coverage(got: list[str], expected: list[str], verb: str) -> list[str]:
    problems = []
    if missing := [e for e in expected if e not in got]:
        problems.append(f"You must {verb} every open challenge exactly once; missing: {', '.join(missing)}.")
    if dupes := sorted({g for g in got if got.count(g) > 1 and g in expected}):
        problems.append(f"Answered more than once: {', '.join(dupes)}.")
    return problems


def _section_problems(p: Proposal) -> list[str]:
    problems, ids = [], [i.id for section in SECTIONS for i in getattr(p, section)]
    for section, prefix in SECTIONS.items():
        items = getattr(p, section)
        if not items:
            problems.append(f"'{section}' is empty; every section needs at least one item.")
        if bad := [i.id for i in items if section_of(i.id) != section]:
            problems.append(f"IDs in '{section}' must look like {prefix}1, {prefix}2; got {', '.join(bad)}.")
        if blank := [i.id for i in items if not i.text.strip()]:
            problems.append(f"Items need text: {', '.join(blank)}.")
    if dupes := sorted({i for i in ids if ids.count(i) > 1}):
        problems.append(f"Duplicate IDs: {', '.join(dupes)}.")
    return problems


def _only_removes(edits: list[Edit]) -> bool:
    return bool(edits) and all(not e.text.strip() for e in edits)


def _share(words: list[str], text: str) -> float:
    """The share of `words` that appear in `text` in the same order, ignoring case and punctuation."""
    blocks = SequenceMatcher(None, words, _words(text).split(), autojunk=False).get_matching_blocks()
    return sum(b.size for b in blocks) / len(words) if words else 1.0


def _same_question(a: str, b: str) -> bool:
    """The same words in the same order, give or take two inserted words ("What specific guidelines..." repeats "What
    guidelines..."), ignoring case and punctuation. A changed word ("view" vs "edit") makes a different question."""
    short, long_ = sorted((_words(a).split(), _words(b).split()), key=len)
    return len(long_) - len(short) <= 2 and _share(short, " ".join(long_)) == 1.0


def _keeps(earlier: str, later: str) -> bool:
    """Does a later wording keep (nearly) all of an earlier one's words, i.e. refine it rather than replace it?"""
    return _share(_words(earlier).split(), later) >= 0.85


def _quote_words(evidence: str) -> list[str]:
    words = _words(evidence).split()
    return words[1:] if words and re.fullmatch(r"[a-z]\d+", words[0]) else words


def _drops(edits: list[Edit]) -> bool:
    """Does a set of edits drop or descope something: remove an item, or add or change an out-of-scope one?"""
    return any(not e.text.strip() or section_of(e.id) == "out_of_scope" for e in edits)


def _words(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _dedupe(moves: list, allowed: list[str], key) -> list:
    seen, out = set(), []
    for m in moves:
        if key(m) in allowed and key(m) not in seen:
            seen.add(key(m))
            out.append(m)
    return out
