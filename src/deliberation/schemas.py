"""Typed contracts between the agents and the orchestrator.

With structured outputs the JSON schema is sent to the model, so the field descriptions
below do prompt work. They are kept short and deliberate, like the files in prompts/.
Every field is required (no defaults) to stay inside both providers' strict-schema rules.
"""

from typing import Annotated, Literal

from pydantic import BaseModel, BeforeValidator, Field


def _upper(value: object) -> object:
    # Structured outputs don't guarantee enum casing, so normalise before validating.
    return value.strip().upper().replace(" ", "_") if isinstance(value, str) else value


def Choice(*values: str):  # noqa: N802 - used like a type
    return Annotated[Literal[values], BeforeValidator(_upper)]


Lens = Choice("CONFIDENTIALITY", "DEFINITIONS", "OWNERSHIP", "DATA_QUALITY", "OPERATIONS", "COMPLIANCE", "FEASIBILITY")
Severity = Choice("BLOCKER", "MAJOR", "MINOR")
Action = Choice("DEFEND", "REVISE", "CONCEDE")
Ruling = Choice("ACCEPT", "MAINTAIN", "ESCALATE")
Signal = Choice("CONTINUE", "CONCLUDE")

MANDATORY_LENSES = ("CONFIDENTIALITY", "DEFINITIONS", "OWNERSHIP")
BLOCKING = ("BLOCKER", "MAJOR")
WEIGHT = {"BLOCKER": 3, "MAJOR": 2, "MINOR": 1}

# ---------------------------------------------------------------- Proposer output


class Item(BaseModel):
    id: str = Field(description="Stable ID with the section prefix, e.g. S1. Keep it when the item is edited.")
    text: str


class Assumption(BaseModel):
    id: str = Field(description="A1, A2, ...")
    text: str
    why_implicit: str = Field(description="What in the request silently depends on this assumption.")


class Definition(BaseModel):
    id: str = Field(description="D1, D2, ...")
    term: str = Field(description="The vague phrase, quoted from the request.")
    definition: str = Field(description="An operational definition an engineer can build and a tester can check.")


class Criterion(BaseModel):
    id: str = Field(description="K1, K2, ...")
    metric: str
    target: str
    measurement: str = Field(description="How and when it is measured.")


class Proposal(BaseModel):
    summary: str = Field(description="Two sentences: what this release delivers and for whom.")
    core_commitments: list[Item] = Field(description="V-items: the 1-2 outcomes the stakeholder actually needs.")
    in_scope: list[Item] = Field(description="S-items: concrete, testable things this release does.")
    out_of_scope: list[Item] = Field(description="X-items: what this release deliberately does not do.")
    assumptions: list[Assumption]
    definitions: list[Definition]
    success_criteria: list[Criterion]

    def items(self) -> dict[str, str]:
        """Every item ID mapped to a one-line text, across all sections."""
        out = {i.id: i.text for i in self.core_commitments + self.in_scope + self.out_of_scope}
        out |= {a.id: a.text for a in self.assumptions}
        out |= {d.id: f'"{d.term}": {d.definition}' for d in self.definitions}
        out |= {k.id: f"{k.metric} — target {k.target} ({k.measurement})" for k in self.success_criteria}
        return out


class Response(BaseModel):
    challenge_id: str
    action: Action
    rationale: str = Field(description="1-3 sentences. For CONCEDE, name the argument that changed your mind.")
    changed_ids: list[str] = Field(description="IDs you added, edited or removed for this response; empty for DEFEND.")


class ProposerTurn(BaseModel):
    responses: list[Response] = Field(description="Exactly one per open challenge. Empty in round 1.")
    proposal: Proposal = Field(description="The full current proposal, including unchanged items.")
    confidence: int = Field(description="0-100: how ready this proposal is to build as written.")
    biggest_worry: str = Field(description="One sentence.")


# ---------------------------------------------------------------- Critic output


class NewChallenge(BaseModel):
    targets: list[str] = Field(description='Item IDs you challenge, e.g. ["S2", "D1"], or ["GAP"] if something essential is missing.')
    lens: Lens
    severity: Severity
    challenge: str = Field(description="The objection or question, in one or two sentences.")
    failure_scenario: str = Field(description="A concrete story of how this goes wrong, using the CRM's real actors and data.")
    resolution_test: str = Field(description="What the Proposer must show or change for you to accept.")


class Verdict(BaseModel):
    challenge_id: str
    ruling: Ruling
    rationale: str = Field(description="1-2 sentences. For MAINTAIN, give a new argument, not a repeat.")


class LensNote(BaseModel):
    lens: Lens
    note: str = Field(description="Why this lens carries no material risk in the current proposal.")


class CriticOpening(BaseModel):
    """Round 1. There is deliberately no signal field: concluding in round 1 is impossible, not just forbidden."""

    new_challenges: list[NewChallenge]
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
    id: str = Field(description="A final item ID (V, S, X or A).")
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
    blocks_build: bool


class Synthesis(BaseModel):
    executive_summary: str = Field(description="3-4 sentences: what will be built, what won't, what humans must decide.")
    item_notes: list[ItemNote]
    rejected: list[Rejected]
    open_questions: list[OpenQuestion] = Field(description="Exactly one per escalated or unresolved issue.")
    tension_summary: str = Field(description="2-3 sentences on where the real disagreement was and how it moved.")
