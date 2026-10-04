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
        new = [challenge("MINOR", "OPERATIONS") for _ in range(4)] + [challenge("BLOCKER", "COMPLIANCE", ("GAP",))]
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
    assert any("ACCEPT of C1 was refused" in w and "is not there" in w for w in result.ledger.warnings)


def test_evidence_must_be_quoted_but_may_carry_an_id_or_elide_words():
    p = proposal()
    p["in_scope"][0]["text"] = "Only the regional coordinator for a country can mark a contact as its focal point."
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(p)])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    check = lambda quote: ledger.evidence_source(verdict(evidence=quote))  # noqa: E731
    assert check("only the regional coordinator for a country can mark a contact") == "S1"
    assert check("S1: Only the regional coordinator ... can mark a contact as its focal point") == "S1"
    assert check("Regional coordinators own focal-point assignments") == ""  # a paraphrase is not evidence
    assert check("Only the ... focal") == ""                                  # fragments too short to check


def verdict(**kw) -> Verdict:
    return Verdict(**{"challenge_id": "C1", "evidence": "", "fact": "regional coordinators", "settled": True,
                      "unconfirmed": False, "needs_human_decision": False, "rationale": "r", **kw})


def test_an_accept_needs_a_concrete_fact_and_evidence_from_a_decided_item():
    p = proposal()
    p["assumptions"][0]["text"] = "A data steward reviews every contact record each quarter."
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(p)])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    steward = "A data steward reviews every contact record each quarter"
    assert "comes from assumption A1" in ledger.verdict_problem(verdict(evidence=steward))
    ledger.issues["C1"].history.append(Event(round=2, actor="proposer", move="DEFEND", text=f"A1 covers it: {steward}."))
    assert "comes from assumption A1" in ledger.verdict_problem(verdict(evidence=steward))  # not through a defense either
    for empty in ("no fact", "`no fact`", "No fact - it only promises a process", "", "n/a"):
        assert "`fact` is" in ledger.verdict_problem(verdict(evidence="Know who to call.", fact=empty)), empty
    assert ledger.verdict_problem(verdict(evidence="Know who to call.", fact="none: no role can export")) == ""
    assert "at least four consecutive words" in ledger.verdict_problem(verdict(evidence="Know who"))
    assert ledger.verdict_problem(verdict(evidence="Know who to call.")) == ""
    assert ledger.verdict_problem(verdict(settled=False, evidence="anything")) == ""  # only an ACCEPT needs support


def test_an_accept_cannot_rest_on_a_weak_phrase_or_on_a_question_sent_to_humans():
    p = proposal()
    p["in_scope"][0]["text"] = "A process will be established to reassign alerts when a coordinator leaves."
    p["in_scope"][1]["text"] = "Alerts move to the regional coordinator's successor within 5 working days."
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(p)])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    weak = ledger.verdict_problem(verdict(evidence="A process will be established to reassign alerts"))
    assert "leans on 'will be established'" in weak
    assert ledger.verdict_problem(verdict(evidence="Alerts move to the regional coordinator's successor")) == ""
    trimmed = ledger.verdict_problem(verdict(evidence="to reassign alerts when a coordinator leaves"))
    assert "leans on 'will be established'" in trimmed  # quoting around the weak phrase doesn't hide it
    ledger.issues["C1"].history.append(Event(round=2, actor="proposer", move="DEFEND", grounds="DESIGN_DETAIL",
                                             text="Alert wording will be defined in design; this release fixes who gets them."))
    assert ledger.verdict_problem(verdict(evidence="Alert wording will be defined in design")) == ""  # deferring is the point
    ledger.issues["C1"].history.append(Event(round=2, actor="proposer", move="DEFEND", grounds="ACCEPTABLE_RISK",
                                             text="Acceptable for a first release: appropriate staff will review alerts."))
    assert "leans on 'appropriate'" in ledger.verdict_problem(verdict(evidence="appropriate staff will review alerts"))
    ledger.issues["C1"].history.append(Event(round=3, actor="proposer", move="DEFEND", grounds="NEEDS_HUMAN_DECISION",
                                             text="How long alerts are kept is for the records office to decide."))
    assert "needs a human decision, so it can't be settled here" in \
        ledger.verdict_problem(verdict(evidence="How long alerts are kept is for the records office"))


def test_an_accepted_question_for_humans_is_refused_and_the_critics_own_routing_decides():
    def proposer(prompt, _):
        return proposer_json(prompt, moves={"C1": ("NEEDS_HUMAN_DECISION", [])})

    llms = agents(proposer=proposer)  # the Critic accepts everything and never says C1 needs humans
    result = deliberate("Request.", "ctx", llms, GATED)
    assert "needs a human decision, so it can't be settled here" in llms["critic"].prompts[2][-1]["content"]
    c1 = result.ledger.issues["C1"]
    assert [e.move for e in c1.history if e.actor == "critic"][1] == "MAINTAIN"  # ours to decide, says the Critic
    assert c1.status == "ESCALATED" and c1.strikes == 2                          # until the strike limit hands it over


def test_a_new_challenge_may_not_repeat_an_existing_question():
    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        again = {**challenge("BLOCKER", "CONFIDENTIALITY"), "resolution_test": " which RULE settles case " + first + "?!"}
        return critic_json({c: ("MAINTAIN" if c == "C1" else "ACCEPT") for c in open_ids(prompt)}, new=[again])

    first = THREE[0]["resolution_test"].removeprefix("Which rule settles case ").rstrip("?")
    llms = agents(critic=critic)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert "asks the same question as C1" in llms["critic"].prompts[2][-1]["content"]
    assert any("repeated an open question" in w for w in result.ledger.warnings)
    assert len(result.ledger.issues) == 3  # nothing new was added


def test_round_one_raises_a_challenge_per_open_question():
    def critic(prompt, _):
        doc = json.loads(accept_then_conclude(prompt, _))
        if round_of(prompt) == 1:
            doc["gaps"] = [f"Question {n}?" for n in range(1, 6)]  # five gaps, three challenges
        return json.dumps(doc)

    llms = agents(critic=critic)
    deliberate("Request.", "ctx", llms, GATED)
    assert "at least 5, at most 6" in llms["critic"].prompts[1][-1]["content"]


def test_weak_phrases_are_only_the_ones_that_never_name_anything():
    p = proposal()
    concrete = ["The mission's protocol officer is the primary contact for each country.",
                "A deputy acts in place of the focal point during leave.",
                "Cold means inactive as defined in D1, checked by a periodic digest every Monday.",
                "Inactivity will be determined by the date of the last logged meeting.",
                "Only authorized users including regional coordinators and project managers see scores."]
    p["in_scope"] = [{"id": f"S{n}", "text": t} for n, t in enumerate(concrete, 1)]
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(p)])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    for text in concrete:
        assert ledger.verdict_problem(verdict(evidence=text)) == "", text


def test_an_unnamed_role_is_weak_only_when_no_role_is_named():
    from deliberation.ledger import weak_phrase

    # v7 auto-logging C8: a concrete answer that a role-blind check refused twice, auto-escalating it
    assert weak_phrase("access controls limited to authorized users based on their role, specifically the roles of "
                       "regional coordinators and project managers") == ""
    assert weak_phrase("a designated manager will be assigned to maintain the records") == "designated manager"
    assert weak_phrase("only authorized users can access sensitive information") == "authorized users"
    assert weak_phrase("project managers with appropriate clearance will be established later") == "will be established"


def test_a_follow_up_challenge_may_name_the_challenge_it_follows():
    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        if round_of(prompt) == 2:
            follow_up = {**challenge("MAJOR", "OWNERSHIP", ("C1",)), "resolution_test": "Who revokes access when a coordinator leaves?"}
            return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, new=[follow_up])
        return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, signal="CONCLUDE")

    llms = agents(critic=critic)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert result.meta["repairs"] == 0 and result.ledger.issues["C4"].targets == THREE[0]["targets"]


def test_a_resolution_test_must_be_a_question_and_an_escalated_one_cannot_be_asked_again():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, status="ESCALATED", **{**challenge(), "resolution_test":
                                "How long are logged meetings kept?"})
    opening = lambda *tests: ledger.check_critic(CriticTurnStub(tests), 2, budget=3)  # noqa: E731
    assert any("ending with '?'" in p for p in opening("Outline the retention process."))
    assert any("with human decision-makers now" in p for p in opening("How long are logged meetings kept?"))


def CriticTurnStub(tests):  # noqa: N802 - a CriticTurn with no rulings and the given new questions
    from deliberation.schemas import CriticTurn, NewChallenge

    return CriticTurn(verdicts=[], signal="CONTINUE", lens_coverage=[], confidence=50, biggest_worry="w",
                      new_challenges=[NewChallenge(**{**challenge(), "resolution_test": t}) for t in tests])


def test_repeated_questions_are_caught_but_different_ones_are_not():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **{**challenge(), "resolution_test":
                                "What guidelines decide which meetings are logged?"})
    ledger.issues["C2"] = Issue(id="C2", round_raised=1, status="RESOLVED", **{**challenge(), "resolution_test":
                                "Which roles can view other teams' history?"})
    from deliberation.schemas import NewChallenge

    ask = lambda *tests: ledger._repeats([NewChallenge(**{**challenge(), "resolution_test": t}) for t in tests])  # noqa: E731
    assert ask("What specific guidelines decide which meetings are logged?") == [(1, "C1")]  # one word inserted
    assert ask("Which roles can view other teams' history?") == []   # C2 is closed: re-raising it is allowed
    assert ask("Which roles can edit other teams' history?", "Which roles can edit other teams' history?") == \
        [(2, "new challenge #1")]                                    # a repeat within one turn
    assert ask("What guidelines decide which calls are logged?") == []  # a changed word is a different question


def test_coercion_drops_repeats_before_cutting_to_the_budget():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge("BLOCKER"))
    from deliberation.schemas import CriticTurn, NewChallenge
    new = [NewChallenge(**{**challenge("BLOCKER"), "resolution_test": ledger.issues["C1"].resolution_test}),
           NewChallenge(**challenge("MAJOR")), NewChallenge(**challenge("MAJOR")), NewChallenge(**challenge("MINOR"))]
    turn = CriticTurn(verdicts=[verdict(settled=False)], new_challenges=new, signal="CONTINUE", lens_coverage=[],
                      confidence=50, biggest_worry="w")
    kept = ledger.coerce_critic(turn, 2, budget=3).new_challenges
    assert [c.severity for c in kept] == ["MAJOR", "MAJOR", "MINOR"]


def test_the_round_one_minimum_never_exceeds_the_budget():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    from deliberation.schemas import CriticOpening, NewChallenge
    opening = CriticOpening(pre_mortem="p", gaps=[f"Q{n}?" for n in range(8)], confidence=40, biggest_worry="w",
                            new_challenges=[NewChallenge(**challenge(lens=lens)) for lens in ("OWNERSHIP", "DEFINITIONS")
                                            for _ in range(3)])
    assert ledger.check_critic(opening, 1, budget=6) == []  # eight gaps, but six challenges is the most allowed


def test_an_assumption_only_revision_is_recorded_as_no_usable_answer_after_a_failed_repair():
    def proposer(prompt, _):
        return proposer_json(prompt, moves={"C1": ("MISSING_DECISION", [("A1", "Regional coordinators own each record.")])})

    llms = agents(proposer=proposer)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert "only change assumptions" in llms["proposer"].prompts[2][-1]["content"]
    c1 = [e for e in result.ledger.issues["C1"].history if e.actor == "proposer"][0]
    assert c1.move == "DEFEND" and "No usable answer" in c1.text
    assert result.ledger.proposals[1].items()["A1"] == result.ledger.proposals[0].items()["A1"]


def test_evidence_is_credited_to_the_text_it_matches_best():
    p = proposal()
    p["in_scope"][0]["text"] = "Regional coordinators can see the focal point for their countries; project managers maintain nothing."
    p["assumptions"][0]["text"] = "Regional coordinators maintain the focal point for their countries."
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(p)])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    assert ledger.evidence_source(verdict(evidence="Regional coordinators maintain the focal point for their countries")) == "A1"


def test_the_pre_mortem_is_shown_again_but_the_gaps_list_is_not():
    critic_fake = Fake(accept_then_conclude)
    result = deliberate("Request.", "ctx", {"proposer": Fake(proposer_json), "critic": critic_fake,
                                            "summarizer": Fake(summarizer_json)}, GATED)
    round2 = critic_fake.prompts[1][0]["content"]
    assert "A coordinator exported a confidential note." in round2
    assert "Who decides who the right person is?" not in round2  # re-showing it made the Critic re-raise settled points
    assert result.ledger.gaps == ["Who decides who the right person is?"]


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
        assert ledger.evidence_source(verdict(evidence=claim)) == ("answer" if expected else ""), move


def test_the_ruling_follows_from_the_critics_judgements():
    rule = lambda settled, unconfirmed, humans: verdict(settled=settled, unconfirmed=unconfirmed,  # noqa: E731
                                                        needs_human_decision=humans).ruling
    assert rule(True, False, False) == rule(True, False, True) == "ACCEPT"
    # an answer resting on a team or policy nobody mentioned can't be accepted; the question decides where it goes:
    assert rule(True, True, True) == "ESCALATE"    # to humans, if answering needs their authority (e.g. retention law)
    assert rule(True, True, False) == "MAINTAIN"   # back to the Proposer, if it is a rule we decide (e.g. role changes)
    assert rule(False, False, True) == rule(False, True, True) == "ESCALATE"
    assert rule(False, False, False) == rule(False, True, False) == "MAINTAIN"


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
    assert any("illegal edits dropped" in w for w in result.ledger.warnings)
    c2 = [e for e in result.ledger.issues["C2"].history if e.actor == "proposer"][0]
    assert c2.move == "DEFEND" and "No usable answer" in c2.text  # a claimed revision that changed nothing isn't one


def test_each_illegal_edit_is_named():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    ledger.issues["C1"] = Issue(id="C1", round_raised=1, **challenge())
    revise, concede = "MISSING_DECISION", "SHOULD_NOT_BUILD"
    cases = [(revise, "Q1", "x", "not an item ID"), (revise, "S01", "x", "not an item ID"),
             (concede, "V1", "", "core commitments can't be removed"), (concede, "S9", "", "no S9 to remove"),
             (revise, "S1", "Scope item S1.", "exactly as it was"), (concede, "X1", "", "would leave 'out_of_scope' empty"),
             (revise, "S2", "", "only remove items, which is a concession"),
             (revise, "A1", "Regional coordinators own each country's record.", "only change assumptions"),
             (concede, "S1", "Alerts pause during negotiations.", "a concession drops or descopes")]
    for grounds, item, text, expected in cases:
        response = Response(challenge_id="C1", grounds=grounds, edits=[Edit(id=item, text=text)], rationale="r")
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


def test_later_edits_of_an_item_replace_earlier_ones_but_new_items_need_their_own_ids():
    ledger = Ledger(request="r", proposals=[Proposal.model_validate(proposal())])
    for cid in ("C1", "C2"):
        ledger.issues[cid] = Issue(id=cid, round_raised=1, **challenge())

    def problems(item: str, first: str, second: str) -> list[str]:
        responses = [Response(challenge_id=c, grounds="MISSING_DECISION", edits=[Edit(id=item, text=t)], rationale="r")
                     for c, t in (("C1", first), ("C2", second))]
        return ledger.check_proposer(ProposerTurn(responses=responses, summary="s", confidence=50, biggest_worry="w"))

    assert problems("S1", "Rule A.", "Rule A and rule B.") == []
    assert ledger.proposal.edited([Edit(id="S1", text="Rule A."), Edit(id="S1", text="Rule A and rule B.")]).items()["S1"] \
        == "Rule A and rule B."
    assert "S3 is already the ID of a different new item in this turn; give this one S4" in \
        problems("S3", "Notes are kept 2 years.", "Exports are disabled.")[0]
    assert problems("S3", "Notes are kept 2 years.", "Notes are kept 2 years and exports are disabled.") == []  # refined
    for first, second in (("", "Coordinators may export the list."), ("Coordinators may export the list.", "")):
        assert any("removed by one answer and rewritten by another" in p for p in problems("S2", first, second))


def test_a_concession_must_drop_or_descope_something():
    def proposer(prompt, _):  # labels as a concession what only adds a condition
        return proposer_json(prompt, moves={"C1": ("SHOULD_NOT_BUILD", [("S1", "Alerts pause during negotiations.")])})

    llms = agents(proposer=proposer)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert "a concession drops or descopes something" in llms["proposer"].prompts[2][-1]["content"]
    assert [e.move for e in result.ledger.issues["C1"].history if e.actor == "proposer"] == ["REVISE"]  # relabelled
    assert result.ledger.proposal.items()["S1"] == "Alerts pause during negotiations."


def test_items_lose_a_repeated_id_and_nothing_else():
    assert Edit(id="S3", text="S3: Only regional coordinators.").text == "Only regional coordinators."
    assert Edit(id="S3", text="S3: S3: Twice.").text == "Twice."
    assert Response(challenge_id="C1", grounds="MISSING_DECISION", rationale="r",  # validating again changes nothing
                    edits=[Edit(id="S3", text="S3: S3: Twice.")]).edits[0].text == "Twice."
    assert Edit(id="S1", text="S1-S3 apply to every region.").text == "S1-S3 apply to every region."
    assert Edit(id="K1", text="K1.5 hours is the median.").text == "K1.5 hours is the median."
    assert Edit(id="S1", text="S1:").text == "S1:"  # never turns an edit into a removal


def test_a_missing_ruling_is_recorded_as_maintain_after_a_failed_repair():
    def critic(prompt, _):  # forgets C3 every time
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        return critic_json({c: "ACCEPT" for c in open_ids(prompt) if c != "C3"}, signal="CONCLUDE")

    result = deliberate("Request.", "ctx", agents(critic=critic), GATED)
    assert any("did not rule on C3" in w for w in result.ledger.warnings)
    assert [e.move for e in result.ledger.issues["C3"].history if e.actor == "critic"][1] == "MAINTAIN"


def test_a_revision_that_only_removes_items_is_a_concession():
    def proposer(prompt, _):
        return proposer_json(prompt, moves={"C1": ("MISSING_DECISION", [("S2", "")])})

    llms = agents(proposer=proposer)
    result = deliberate("Request.", "ctx", llms, GATED)
    assert "which is a concession" in llms["proposer"].prompts[2][-1]["content"]
    assert [e.move for e in result.ledger.issues["C1"].history if e.actor == "proposer"] == ["CONCEDE"]


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
