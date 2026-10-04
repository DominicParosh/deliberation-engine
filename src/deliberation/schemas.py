"""Typed contracts between the agents and the orchestrator.

With structured outputs the JSON schema is sent to the model, so the field descriptions
below do prompt work. They are kept short and deliberate, like the files in prompts/.
Every field is required (no defaults) to stay inside both providers' strict-schema rules.
"""

import re
from typing import Annotated, Literal

from pydantic import BaseModel, BeforeValidator, Field, model_validator


def _upper(value: object) -> object:
    # Structured outputs don't guarantee enum casing, so normalise before validating.
    return value.strip().upper().replace(" ", "_") if isinstance(value, str) else value


def Choice(*values: str):  # noqa: N802 - used like a type
    return Annotated[Literal[values], BeforeValidator(_upper)]


Lens = Choice("CONFIDENTIALITY", "DEFINITIONS", "OWNERSHIP", "DATA_QUALITY", "OPERATIONS", "COMPLIANCE", "FEASIBILITY")
Severity = Choice("BLOCKER", "MAJOR", "MINOR")
Grounds = Choice("MISSING_DECISION", "SHOULD_NOT_BUILD", "ALREADY_COVERED", "DESIGN_DETAIL", "ACCEPTABLE_RISK",
                 "NEEDS_HUMAN_DECISION")
MOVE_FOR = {"MISSING_DECISION": "REVISE", "SHOULD_NOT_BUILD": "CONCEDE"}  # every other ground is a DEFEND
Signal = Choice("CONTINUE", "CONCLUDE")

MANDATORY_LENSES = ("CONFIDENTIALITY", "DEFINITIONS", "OWNERSHIP")
BLOCKING = ("BLOCKER", "MAJOR")
WEIGHT = {"BLOCKER": 3, "MAJOR": 2, "MINOR": 1}
SECTIONS = {"core_commitments": "V", "in_scope": "S", "out_of_scope": "X",
            "assumptions": "A", "definitions": "D", "success_criteria": "K"}


def section_of(item_id: str) -> str | None:
    """The proposal section an item ID belongs to (S3 -> in_scope), or None if it is not an item ID."""
    return next((s for s, prefix in SECTIONS.items() if re.fullmatch(prefix + r"[1-9]\d*", item_id)), None)


# ---------------------------------------------------------------- Proposer output


class Item(BaseModel):
    id: str = Field(description="Stable ID with the section prefix, e.g. S1.")
    text: str

    @model_validator(mode="after")
    def _drop_repeated_id(self) -> "Item":
        # Models often start the text with "S3:" as well, which renders as "S3: S3: ...". Only the colon form is
        # stripped ("S1-S3 apply" and "K1.5 hours" are real text), all repeats at once so re-validation changes
        # nothing, and never down to an empty text, which would turn an edit into a removal.
        self.text = re.sub(rf"^(\s*{re.escape(self.id)}\s*:\s*)+", "", self.text) or self.text
        return self


class Edit(Item):
    id: str = Field(description="The item to change, e.g. S3. A new item takes the next number its section has never used.")
    text: str = Field(description="The item's complete new wording, exactly as it should read in the proposal, naming the "
                                  "specific role, number or rule ('authorized users' or 'a process will be established' "
                                  "decide nothing). Empty removes the item.")


class Proposal(BaseModel):
    """Every item is an ID and a sentence, so edits, diffs, quotes and rendering work the same way for all sections."""

    summary: str = Field(description="Two sentences: what this release delivers and for whom.")
    core_commitments: list[Item] = Field(description="V: the 1-2 outcomes the stakeholder actually needs.")
    in_scope: list[Item] = Field(description="S: concrete, testable things this release does, naming the roles, rules, "
                                             "limits and data.")
    out_of_scope: list[Item] = Field(description="X: what this release deliberately does not do.")
    assumptions: list[Item] = Field(description="A: what the request silently depends on; each ends with what in the "
                                                "request depends on it.")
    definitions: list[Item] = Field(description='D: one per vague term, worded "<term>" means <a definition an engineer '
                                                'can build and a tester can check>.')
    success_criteria: list[Item] = Field(description="K: a metric, a target and how it is measured.")

    def items(self) -> dict[str, str]:
        """Every item's ID mapped to its wording, across all sections."""
        return {i.id: i.text for section in SECTIONS for i in getattr(self, section)}

    def edited(self, edits: list[Edit]) -> "Proposal":
        """The next version. Each edit, in order, rewrites an item in place, appends a new ID to its section,
        or (with empty text) removes the item. IDs that aren't item IDs are ignored; the ledger refuses them first."""
        sections = {s: list(getattr(self, s)) for s in SECTIONS}
        for e in edits:
            if (section := section_of(e.id)) is None:
                continue
            items, text = sections[section], e.text.strip()
            at = next((n for n, i in enumerate(items) if i.id == e.id), len(items))
            items[at:at + 1] = [Item(id=e.id, text=text)] if text else []
        return self.model_copy(update=sections)


class Response(BaseModel):
    challenge_id: str
    grounds: Grounds = Field(description="What kind of challenge this is. It decides your move: MISSING_DECISION means "
                                         "REVISE, SHOULD_NOT_BUILD means CONCEDE, anything else means DEFEND.")
    edits: list[Edit] = Field(description="REVISE or CONCEDE: each item you rewrite, add or remove to settle the challenge, "
                                           "with its complete new wording. DEFEND: empty, the proposal stays as it is.")
    rationale: str = Field(description="1-3 sentences. For a revision, what your edits decide. For a defense, why the item "
                                       "stands. For a concession, the argument that convinced you.")

    @property
    def action(self) -> str:
        return MOVE_FOR.get(self.grounds, "DEFEND")


class ProposerOpening(BaseModel):
    """Round 1: the full proposal."""

    proposal: Proposal
    confidence: int = Field(description="0-100: how ready this proposal is to build as written.")
    biggest_worry: str = Field(description="One sentence.")


class ProposerTurn(BaseModel):
    """Round 2 onwards. The Proposer never rewrites the whole proposal: the engine applies its edits, so what it
    says it changed and what changed are the same thing."""

    responses: list[Response] = Field(description="Exactly one per open challenge.")
    summary: str = Field(description="The proposal's two-sentence summary, updated if your edits changed what the "
                                     "release delivers.")
    confidence: int = Field(description="0-100: how ready the proposal is to build as written, with your edits.")
    biggest_worry: str = Field(description="One sentence.")


# ---------------------------------------------------------------- Critic output


class NewChallenge(BaseModel):
    targets: list[str] = Field(description='Item IDs you challenge, e.g. ["S2", "D1"], or ["GAP"] if something essential is missing.')
    lens: Lens
    severity: Severity
    challenge: str = Field(description="The objection or question, in one or two sentences.")
    failure_scenario: str = Field(description="A concrete story of how this goes wrong, using the CRM's real actors and data.")
    resolution_test: str = Field(description="The question the proposal must answer for you to accept, answerable with a "
                                             "concrete fact: a role, a number, a rule or yes/no.")


class Verdict(BaseModel):
    """The Critic quotes, names what the quote commits to, then judges. The ruling follows from its judgements, as the
    Proposer's move follows from its grounds."""

    challenge_id: str
    evidence: str = Field(description="The words that come closest to answering your test, copied exactly from the item text "
                                      "shown under the challenge (or from the Proposer's answer, for a defense or concession). "
                                      "Empty if nothing comes close.")
    fact: str = Field(description="What those words commit to, in a few words: the role, number, rule or yes/no your test asks "
                                  "for; for a defense, what its argument establishes ('design detail: alert wording', 'covered "
                                  "by S3'). Write 'no fact' if they only promise ('a process will be established'), name no "
                                  "one specific ('authorized users', 'appropriate clearance') or restate the question.")
    settled: bool = Field(description="Does `fact` answer your test and stop your failure scenario as you described it? For a "
                                      "defense, does its argument hold instead: your test asked how to build rather than what, "
                                      "another item already covers it, or the remaining risk is acceptable for a first release? "
                                      "Judge only your original scenario: a new concern is a new challenge, not a reason to say no. "
                                      "A challenge the Proposer says needs a human decision is never settled here.")
    unconfirmed: bool = Field(description="Does the answer rest on a team, policy, clearance level, law or system that the system "
                                          "description doesn't mention? Then it can't be accepted as it stands.")
    needs_human_decision: bool = Field(description="Does answering your test need authority neither of you has (what the law "
                                                   "requires, existing policy, budgets, which teams exist)? Who sees what, who is "
                                                   "alerted, thresholds, and what happens when people change roles or leave are "
                                                   "rules you two decide, never questions for humans.")
    rationale: str = Field(description="1-2 sentences. If you don't accept, say exactly what is still missing.")

    @property
    def ruling(self) -> str:
        """A settled, confirmed challenge is accepted. Otherwise the question decides where it goes: to humans if it
        needs authority neither agent has, back to the Proposer if it is a rule this deliberation can decide."""
        if self.settled and not self.unconfirmed:
            return "ACCEPT"
        return "ESCALATE" if self.needs_human_decision else "MAINTAIN"


class LensNote(BaseModel):
    lens: Lens
    note: str = Field(description="Why this lens carries no material risk in the current proposal.")


class CriticOpening(BaseModel):
    """Round 1. There is deliberately no signal field: concluding in round 1 is impossible, not just forbidden."""

    pre_mortem: str = Field(description="A year after launch, something this feature created (a record, a list, a score, an "
                                        "alert) caused a serious incident. In 2-3 sentences, what happened? Write this first.")
    gaps: list[str] = Field(description="Questions the original request leaves open that a buildable release must answer and "
                                        "the proposal answers badly or not at all, one short question each. Each gets a challenge.")
    new_challenges: list[NewChallenge] = Field(description="Most material first. If the proposal as written does not prevent "
                                                           "your pre-mortem, the first challenge is about that.")
    confidence: int = Field(description="0-100: how ready this proposal is to build as written.")
    biggest_worry: str = Field(description="One sentence.")


class CriticTurn(BaseModel):
    verdicts: list[Verdict] = Field(description="Exactly one per challenge the Proposer just answered.")
    new_challenges: list[NewChallenge]
    signal: Signal
    lens_coverage: list[LensNote] = Field(description="When concluding: one note per mandatory lens you never raised a challenge under. Otherwise empty.")
    confidence: int = Field(description="0-100: how ready this proposal is to build as written.")
    biggest_worry: str = Field(description="One sentence.")


# ---------------------------------------------------------------- Summarizer output


class ItemNote(BaseModel):
    id: str = Field(description="A final item ID (V, S, X, A, D or K).")
    note: str = Field(description="One or two sentences on why it ended up this way.")
    refs: list[str] = Field(description="Issue IDs (C...) that shaped it; empty if it was never challenged.")


class Rejected(BaseModel):
    what: str = Field(description="What was proposed and later dropped or descoped.")
    why: str
    refs: list[str] = Field(description="The item and issue IDs involved.")


class OpenQuestion(BaseModel):
    issue_id: str
    question: str = Field(description="Phrased so a human decision-maker can answer it.")
    why_it_matters: str
    decision_owner: str = Field(description="A role, e.g. 'Head of Data Protection'.")
    options: list[str]


class Synthesis(BaseModel):
    executive_summary: str = Field(description="3-4 sentences: what will be built, what won't, what humans must decide.")
    item_notes: list[ItemNote]
    rejected: list[Rejected]
    open_questions: list[OpenQuestion] = Field(description="Exactly one per escalated or unresolved issue.")
    tension_summary: str = Field(description="2-3 sentences on where the real disagreement was and how it moved.")
