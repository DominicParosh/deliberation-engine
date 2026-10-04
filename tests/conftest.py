"""Test doubles. `Fake` answers from the rendered prompt it receives, so tests drive the real
prompt rendering, validation, ledger and termination code, with no API calls."""

import json
import re

import pytest

from deliberation.llm import Completion


class Fake:
    def __init__(self, respond, model="fake"):
        self.respond, self.model, self.prompts = respond, model, []

    def complete(self, system, messages, schema):
        self.prompts.append(messages)
        return Completion(self.respond(messages[0]["content"], messages), 0, 0, self.model)


def open_ids(prompt: str) -> list[str]:
    return re.findall(r"^\*\*(C\d+)\*\* · ", prompt, flags=re.M)


def round_of(prompt: str) -> int:
    return int(re.search(r"# Round (\d+)", prompt).group(1))


def budget_of(prompt: str) -> int:
    return int(re.search(r"(?:at most|and) (\d+) (?:new )?challenge", prompt).group(1))


def proposal(drop_core=False, scope=("S1", "S2")) -> dict:
    return {
        "summary": "A first release.",
        "core_commitments": [] if drop_core else [{"id": "V1", "text": "Know who to call."}],
        "in_scope": [{"id": s, "text": f"Scope item {s}."} for s in scope],
        "out_of_scope": [{"id": "X1", "text": "No mobile app."}],
        "assumptions": [{"id": "A1", "text": "Contacts have one country.", "why_implicit": "'each country' implies it."}],
        "definitions": [{"id": "D1", "term": "right person", "definition": "Most recently assigned focal point."}],
        "success_criteria": [{"id": "K1", "metric": "Lookup time", "target": "< 1 min", "measurement": "Survey"}],
    }


def proposer_json(prompt: str, _messages=None, *, grounds="ACCEPTABLE_RISK", **kw) -> str:
    responses = [{"challenge_id": c, "grounds": grounds, "rationale": "Because.", "changed_ids": []} for c in open_ids(prompt)]
    return json.dumps({"responses": responses, "proposal": proposal(**kw), "confidence": 70, "biggest_worry": "Adoption."})


def challenge(severity="MAJOR", lens="CONFIDENTIALITY", targets=("S1",)) -> dict:
    return {"targets": list(targets), "lens": lens, "severity": severity, "challenge": "What breaks?",
            "failure_scenario": "A coordinator sees a confidential note.", "resolution_test": "Restrict it."}


def opening_json(*challenges) -> str:
    return json.dumps({"gaps": ["Who decides who the right person is?"], "new_challenges": list(challenges),
                       "confidence": 30, "biggest_worry": "Leaks."})


EVIDENCE = "Know who to call."  # appears in every fake proposal, so an ACCEPT quoting it is supported


def critic_json(rulings: dict[str, str] | str, new=(), signal="CONTINUE", coverage=(), confidence=60, evidence=EVIDENCE) -> str:
    return json.dumps({
        "verdicts": [{"challenge_id": c, "answered": r == "ACCEPT", "evidence": evidence if r == "ACCEPT" else "",
                      "needs_human_decision": r == "ESCALATE", "rationale": "Considered."} for c, r in rulings.items()],
        "new_challenges": list(new), "signal": signal, "confidence": confidence, "biggest_worry": "Leaks.",
        "lens_coverage": [{"lens": lens, "note": "No material risk."} for lens in coverage]})


def summarizer_json(prompt: str, _messages=None) -> str:
    needing = re.search(r"## Issues that need an open question\n(.*)", prompt).group(1)
    dropped = re.findall(r"^- ([A-Z]\d+): ", prompt.split("## Items dropped")[1].split("##")[0], flags=re.M)
    return json.dumps({
        "executive_summary": "We build a contact register.",
        "item_notes": [{"id": "S1", "note": "Kept.", "refs": []}],
        "rejected": [{"what": f"Item {d}", "why": "Descoped.", "refs": [d]} for d in dropped],
        "open_questions": [{"issue_id": c, "question": "Who decides?", "why_it_matters": "Risk.", "decision_owner": "DPO",
                            "options": ["A", "B"], "blocks_build": True} for c in re.findall(r"C\d+", needing)],
        "tension_summary": "They disagreed about access."})


@pytest.fixture
def context() -> str:
    return "A Government CRM with sensitive diplomatic contact records."
