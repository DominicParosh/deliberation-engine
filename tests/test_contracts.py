"""The contract around the agents: repair-then-coerce, summarizer validation, replay, adapters."""

import json
from types import SimpleNamespace

from conftest import Fake, challenge, critic_json, open_ids, opening_json, proposer_json, round_of, summarizer_json

from deliberation.engine import deliberate, replay
from deliberation.ledger import Issue, Ledger
from deliberation.llm import AnthropicLLM, OpenAILLM
from deliberation.schemas import ProposerTurn
from deliberation.termination import GATED

THREE = (challenge("BLOCKER", "CONFIDENTIALITY"), challenge("MAJOR", "DEFINITIONS"), challenge("MINOR", "OWNERSHIP"))


def accept_then_conclude(prompt, _):
    if round_of(prompt) == 1:
        return opening_json(*THREE)
    return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, signal="CONCLUDE")


def agents(proposer=proposer_json, critic=accept_then_conclude, summarizer=summarizer_json):
    return {"proposer": Fake(proposer), "critic": Fake(critic), "summarizer": Fake(summarizer)}


def test_enum_casing_is_normalised():
    turn = json.loads(proposer_json("**C1** · MAJOR · OPERATIONS · targets S1"))
    turn["responses"][0]["action"] = "Defend"
    assert ProposerTurn.model_validate(turn).responses[0].action == "DEFEND"


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
    assert "budget this round is 3" in llms["critic"].prompts[1][-1]["content"]  # the repair request
    assert any("budget" in w for w in result.ledger.warnings)


def test_core_commitments_survive_an_attempt_to_drop_them():
    def proposer(prompt, _):
        return proposer_json(prompt, drop_core=round_of(prompt) > 1)

    result = deliberate("Request.", "ctx", agents(proposer=proposer), GATED)
    assert [v.id for v in result.ledger.proposal.core_commitments] == ["V1"]
    assert any("core commitments" in w for w in result.ledger.warnings)


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
        return proposer_json(prompt, scope=("S1",) if round_of(prompt) > 1 else ("S1", "S2"))

    result = deliberate("Request.", "ctx", agents(proposer=proposer), GATED)
    assert {"S2"} <= {r for x in result.synthesis.rejected for r in x.refs}


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
    assert "is not there" in llms["critic"].prompts[1][-1]["content"]  # one repair request first
    assert result.ledger.issues["C1"].strikes >= 1                      # then the unsupported ACCEPTs count as MAINTAIN
    assert any("without evidence" in w for w in result.ledger.warnings)


def test_evidence_must_be_quoted_but_may_carry_an_id_or_elide_words():
    from conftest import proposal

    from deliberation.schemas import Proposal, Verdict

    p = proposal()
    p["in_scope"][0]["text"] = "Only the regional coordinator for a country can mark a contact as its focal point."
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(p)])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    check = lambda quote: ledger.supported(Verdict(challenge_id="C1", evidence=quote, ruling="ACCEPT", rationale="r"))  # noqa: E731
    assert check("only the regional coordinator for a country can mark a contact")
    assert check("S1: Only the regional coordinator ... can mark a contact as its focal point")
    assert not check("Regional coordinators own focal-point assignments")  # a paraphrase is not evidence
    assert not check("Only the ... focal")                                  # fragments too short to check


def test_definition_terms_lose_their_quotes():
    from deliberation.schemas import Definition

    assert Definition(id="D1", term='"goes cold"', definition="d").term == "goes cold"


def test_the_critics_opening_gaps_are_kept_and_shown_again():
    critic_fake = Fake(accept_then_conclude)
    deliberate("Request.", "ctx", {"proposer": Fake(proposer_json), "critic": critic_fake, "summarizer": Fake(summarizer_json)}, GATED)
    assert "Who decides who the right person is?" in critic_fake.prompts[1][0]["content"]
