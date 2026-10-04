"""The contract around the agents: repair-then-coerce, summarizer validation, replay, adapters."""

import json
from types import SimpleNamespace

from conftest import (Fake, answer, challenge, critic_json, open_ids, opening_json, proposal, proposer_json, round_of,
                      summarizer_json)

from deliberation.engine import deliberate, replay
from deliberation.ledger import Event, Issue, Ledger
from deliberation.llm import AnthropicLLM, OpenAILLM
from deliberation.schemas import Edit, Proposal, ProposerTurn, Response, Verdict
from deliberation.termination import GATED

THREE = (challenge("BLOCKER", "CONFIDENTIALITY"), challenge("MAJOR", "DEFINITIONS"), challenge("MINOR", "OWNERSHIP"))


def accept_then_conclude(prompt, _):
    if round_of(prompt) == 1:
        return opening_json(*THREE)
    return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, signal="CONCLUDE")


def agents(proposer=proposer_json, critic=accept_then_conclude, summarizer=summarizer_json):
    return {"proposer": Fake(proposer), "critic": Fake(critic), "summarizer": Fake(summarizer)}


def test_enum_casing_is_normalised():
    turn = json.loads(proposer_json("# Round 2\n**C1** · MAJOR · OPERATIONS · targets S1"))
    turn["responses"][0]["grounds"] = "needs human decision"
    assert ProposerTurn.model_validate(turn).responses[0].grounds == "NEEDS_HUMAN_DECISION"


def test_over_budget_critic_gets_one_repair_then_keeps_the_most_severe():
    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        new = [challenge("MINOR", "OPERATIONS")] * 4 + [challenge("BLOCKER", "COMPLIANCE", ("GAP",))]
        return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, new=new)  # 5 new, budget 3

    llms = agents(critic=critic)
    result = deliberate("Request.", "ctx", llms, GATED)
    r2_new = [i for i in result.ledger.issues.values() if i.round_raised == 2]
    assert len(r2_new) == 3 and r2_new[0].severity == "BLOCKER"
    assert "budget this round is 3" in llms["critic"].prompts[2][-1]["content"]  # the repair request
    assert any("budget" in w for w in result.ledger.warnings)


def test_core_commitments_survive_an_attempt_to_drop_them():
    def proposer(prompt, _):
        return proposer_json(prompt, moves={"C1": ("SHOULD_NOT_BUILD", [("V1", "")])})

    result = deliberate("Request.", "ctx", agents(proposer=proposer), GATED)
    assert [v.id for v in result.ledger.proposal.core_commitments] == ["V1"]
    assert any("core commitments can't be removed" in w for w in result.ledger.warnings)
    assert [e.move for e in result.ledger.issues["C1"].history if e.actor == "proposer"] == ["DEFEND"]  # not a concession


def test_summarizer_cannot_drop_open_questions_or_cite_unknown_ids():
    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        return critic_json({c: ("ESCALATE" if c == "C1" else "ACCEPT") for c in open_ids(prompt)}, signal="CONCLUDE")

    def careless(prompt, _):
        doc = json.loads(summarizer_json(prompt))
        doc["open_questions"] = []
        doc["item_notes"][0]["refs"] = ["C99"]
        return json.dumps(doc)

    llms = agents(critic=critic, summarizer=careless)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert [q.issue_id for q in result.synthesis.open_questions] == ["C1"]
    assert result.synthesis.item_notes[0].refs == []
    assert len(llms["summarizer"].prompts) == 2  # one repair attempt before coercion


def test_dropped_items_must_be_explained():
    def proposer(prompt, _):
        return proposer_json(prompt, moves={"C1": ("SHOULD_NOT_BUILD", [("S2", "")])})

    def forgetful(prompt, _):  # never mentions what was dropped
        return json.dumps({**json.loads(summarizer_json(prompt)), "rejected": []})

    llms = agents(proposer=proposer, summarizer=forgetful)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert "Explain the dropped items in `rejected`: S2" in llms["summarizer"].prompts[1][-1]["content"]
    assert {"S2"} <= {r for x in result.synthesis.rejected for r in x.refs}  # added by coercion


def test_replay_reproduces_the_run_without_any_model(tmp_path):
    original = deliberate("Request.", "ctx", agents(), GATED, request_id="demo")
    original.save(tmp_path)
    again = replay(tmp_path / "events.jsonl")
    assert again.ledger == original.ledger
    assert again.synthesis == original.synthesis


def test_disagreement_index_weights_by_severity():
    ledger = Ledger(request="r")
    for cid, severity, status in (("C1", "BLOCKER", "ESCALATED"), ("C2", "MAJOR", "RESOLVED"), ("C3", "MINOR", "OPEN")):
        ledger.issues[cid] = Issue(id=cid, round_raised=1, status=status, **challenge(severity))
    assert ledger.disagreement() == round((3 + 1) / (3 + 2 + 1), 2)


def test_anthropic_adapter_sends_a_json_schema_and_returns_raw_text():
    sent = {}

    def create(**kwargs):
        sent.update(kwargs)
        return SimpleNamespace(stop_reason="end_turn", content=[SimpleNamespace(type="text", text='{"ok": 1}')],
                               usage=SimpleNamespace(input_tokens=11, output_tokens=7))

    llm = AnthropicLLM("claude-haiku-4-5-20251001", client=SimpleNamespace(messages=SimpleNamespace(create=create)))
    out = llm.complete("system", [{"role": "user", "content": "hi"}], ProposerTurn)
    assert sent["output_config"]["format"]["type"] == "json_schema" and sent["system"] == "system"
    assert (out.raw, out.input_tokens, out.output_tokens) == ('{"ok": 1}', 11, 7)


def test_openai_adapter_prepends_the_system_prompt_and_returns_raw_text():
    sent = {}

    def parse(**kwargs):
        sent.update(kwargs)
        message = SimpleNamespace(content='{"ok": 1}', refusal=None)
        return SimpleNamespace(choices=[SimpleNamespace(message=message)], usage=SimpleNamespace(prompt_tokens=5, completion_tokens=3))

    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(parse=parse)))
    out = OpenAILLM("gpt-4o-mini", client=client).complete("system", [{"role": "user", "content": "hi"}], ProposerTurn)
    assert sent["messages"][0] == {"role": "system", "content": "system"} and sent["response_format"] is ProposerTurn
    assert (out.raw, out.input_tokens, out.output_tokens) == ('{"ok": 1}', 5, 3)


def test_an_accept_must_quote_text_that_is_really_there():
    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, signal="CONCLUDE", evidence="We will clarify everything later.")

    llms = agents(critic=critic)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert "is not there" in llms["critic"].prompts[2][-1]["content"]  # one repair request first
    assert result.ledger.issues["C1"].strikes >= 1                      # then the unsupported ACCEPTs count as MAINTAIN
    assert any("without evidence" in w for w in result.ledger.warnings)


def test_evidence_must_be_quoted_but_may_carry_an_id_or_elide_words():
    p = proposal()
    p["in_scope"][0]["text"] = "Only the regional coordinator for a country can mark a contact as its focal point."
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(p)])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    check = lambda quote: ledger.supported(Verdict(challenge_id="C1", answered=True, evidence=quote,  # noqa: E731
                                                   needs_human_decision=False, rationale="r"))
    assert check("only the regional coordinator for a country can mark a contact")
    assert check("S1: Only the regional coordinator ... can mark a contact as its focal point")
    assert not check("Regional coordinators own focal-point assignments")  # a paraphrase is not evidence
    assert not check("Only the ... focal")                                  # fragments too short to check


def test_the_critics_pre_mortem_and_gaps_are_kept_and_shown_again():
    critic_fake = Fake(accept_then_conclude)
    deliberate("Request.", "ctx", {"proposer": Fake(proposer_json), "critic": critic_fake, "summarizer": Fake(summarizer_json)}, GATED)
    round2 = critic_fake.prompts[1][0]["content"]
    assert "A coordinator exported a confidential note." in round2 and "Who decides who the right person is?" in round2


def test_the_move_follows_from_the_grounds():
    move = lambda grounds: Response(challenge_id="C1", grounds=grounds, edits=[], rationale="r").action  # noqa: E731
    assert move("MISSING_DECISION") == "REVISE" and move("SHOULD_NOT_BUILD") == "CONCEDE"
    assert {move(g) for g in ("ALREADY_COVERED", "DESIGN_DETAIL", "ACCEPTABLE_RISK", "NEEDS_HUMAN_DECISION")} == {"DEFEND"}


def test_a_revision_must_show_in_the_proposal_but_a_defense_may_be_quoted_from_the_answer():
    claim = "Exports are limited to regional coordinators for their own region."
    for move, expected in (("REVISE", False), ("DEFEND", True)):
        ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
        ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
        ledger.issues["C1"].history.append(Event(round=2, actor="proposer", move=move, text=claim))
        verdict = Verdict(challenge_id="C1", answered=True, evidence=claim, needs_human_decision=False, rationale="r")
        assert ledger.supported(verdict) is expected, move


def test_the_ruling_follows_from_the_critics_two_judgements():
    rule = lambda answered, humans: Verdict(challenge_id="C1", answered=answered, evidence="",  # noqa: E731
                                            needs_human_decision=humans, rationale="r").ruling
    assert (rule(True, False), rule(True, True), rule(False, True), rule(False, False)) == ("ACCEPT", "ACCEPT", "ESCALATE", "MAINTAIN")


def test_the_engine_applies_the_edits_so_claimed_and_actual_changes_match():
    def proposer(prompt, _):
        return proposer_json(prompt, moves={"C1": ("MISSING_DECISION", [("S1", "Only regional coordinators see notes."),
                                                                        ("S3", "Notes are kept for 2 years.")]),
                                            "C2": ("SHOULD_NOT_BUILD", [("S2", "")])})

    result = deliberate("Request.", "ctx", agents(proposer=proposer), GATED)
    L = result.ledger
    items = L.proposal.items()
    assert items["S1"] == "Only regional coordinators see notes." and items["S3"] == "Notes are kept for 2 years."
    assert "S2" not in L.proposal.items() and [i.id for i in L.proposal.in_scope] == ["S1", "S3"]
    assert L.changes(1) == {"added": ["S3"], "edited": ["S1"], "removed": ["S2"]}
    assert [e.changed for e in L.issues["C1"].history if e.actor == "proposer"] == [["S1", "S3"]]
    assert [e.move for e in L.issues["C2"].history if e.actor == "proposer"] == ["CONCEDE"]
    assert L.next_id("in_scope") == "S4" and L.next_id("out_of_scope") == "X2"


def test_a_defense_may_not_edit_and_a_revision_must():
    def proposer(prompt, _):
        return proposer_json(prompt, moves={"C1": ("ALREADY_COVERED", [("S1", "Changed anyway.")]),
                                            "C2": ("MISSING_DECISION", [])})

    llms = agents(proposer=proposer)
    result = deliberate("Request.", "ctx", llms, GATED)
    repair = llms["proposer"].prompts[2][-1]["content"]
    assert "C1: grounds ALREADY_COVERED mean DEFEND" in repair and "C2: grounds MISSING_DECISION mean REVISE" in repair
    assert result.ledger.proposals[1].items() == result.ledger.proposals[0].items()  # second failure: nothing changed
    assert any("edits breaking these rules were dropped" in w for w in result.ledger.warnings)
    c2 = [e for e in result.ledger.issues["C2"].history if e.actor == "proposer"][0]
    assert c2.move == "DEFEND" and "No usable answer" in c2.text  # a claimed revision that changed nothing isn't one


def test_each_illegal_edit_is_named():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    cases = {("Q1", "x"): "not an item ID", ("V1", ""): "core commitments can't be removed", ("S9", ""): "no S9 to remove",
             ("S1", "Scope item S1."): "exactly as it was", ("X1", ""): "would leave 'out_of_scope' empty",
             ("S01", "x"): "not an item ID"}
    for (item, text), expected in cases.items():
        response = Response(challenge_id="C1", grounds="MISSING_DECISION", edits=[Edit(id=item, text=text)], rationale="r")
        problems = ledger.check_proposer(ProposerTurn(responses=[response], summary="s", confidence=50, biggest_worry="w"))
        assert len(problems) == 1 and expected in problems[0], (item, problems)
    for order in ([Edit(id="X1", text=""), Edit(id="X2", text="No offline mode.")], [Edit(id="X2", text="No offline mode."),
                                                                                    Edit(id="X1", text="")]):
        response = Response(challenge_id="C1", grounds="MISSING_DECISION", edits=order, rationale="r")
        assert ledger.check_proposer(ProposerTurn(responses=[response], summary="s", confidence=50, biggest_worry="w")) == []
    ledger.proposals.append(ledger.proposal.edited([Edit(id="S2", text="")]))  # S2 is retired, so it can't come back
    response = Response(challenge_id="C1", grounds="MISSING_DECISION", edits=[Edit(id="S2", text="New.")], rationale="r")
    problems = ledger.check_proposer(ProposerTurn(responses=[response], summary="s", confidence=50, biggest_worry="w"))
    assert "S2 belonged to an item removed earlier" in problems[0] and "(S3)" in problems[0]


def test_an_item_has_one_wording_per_turn():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    for cid in ("C1", "C2"):
        ledger.issues[cid] = Issue(id=cid, round_raised=1, **challenge())

    def problems(item: str, first: str, second: str) -> list[str]:
        responses = [Response(challenge_id=c, grounds="MISSING_DECISION", edits=[Edit(id=item, text=t)], rationale="r")
                     for c, t in (("C1", first), ("C2", second))]
        return ledger.check_proposer(ProposerTurn(responses=responses, summary="s", confidence=50, biggest_worry="w"))

    assert problems("S1", "Rule A and rule B.", "Rule A and rule B.") == []
    assert "S1 is given two different wordings" in problems("S1", "Rule A.", "Rule A and rule B.")[0]
    assert "S3 is already the ID of a different new item in this turn; give this one S4" in \
        problems("S3", "Notes are kept 2 years.", "Exports are disabled.")[0]


def test_answers_to_closed_issues_are_ignored_without_a_repair():
    def proposer(prompt, _):  # also answers C1 after it was escalated
        doc = json.loads(proposer_json(prompt))
        if round_of(prompt) == 3:  # twice, with an edit that would be illegal, to show it isn't even checked
            doc["responses"] += [answer("C1", "MISSING_DECISION", [("S9", "")])] * 2
        return json.dumps(doc)

    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        rulings = {c: ("ESCALATE" if c == "C1" else "MAINTAIN") for c in open_ids(prompt)}
        return critic_json(rulings, signal="CONTINUE")

    result = deliberate("Request.", "ctx", agents(proposer=proposer, critic=critic), GATED)
    assert result.meta["repairs"] == 0
    assert [e.move for e in result.ledger.issues["C1"].history] == ["RAISE", "DEFEND", "ESCALATE"]
