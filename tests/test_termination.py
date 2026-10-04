"""Every way a deliberation can end (or must not end), driven by scripted agents."""

from conftest import Fake, budget_of, challenge, critic_json, open_ids, opening_json, proposer_json, round_of, summarizer_json

from deliberation.engine import deliberate
from deliberation.schemas import CriticOpening
from deliberation.termination import GATED, NAIVE

THREE = (challenge("BLOCKER", "CONFIDENTIALITY"), challenge("MAJOR", "DEFINITIONS"), challenge("MINOR", "OWNERSHIP"))


def run(critic, policy=GATED, proposer=proposer_json, context="ctx"):
    llms = {"proposer": Fake(proposer), "critic": Fake(critic), "summarizer": Fake(summarizer_json)}
    return deliberate("We need a better way to track contacts.", context, llms, policy)


def test_round_one_has_no_way_to_conclude():
    assert "signal" not in CriticOpening.model_fields


def test_conclude_is_rejected_while_a_blocker_is_open_then_accepted_once_resolved():
    def critic(prompt, _):
        rnd = round_of(prompt)
        if rnd == 1:
            return opening_json(*THREE)
        if rnd == 2:  # concedes the minor points but keeps the blocker, and tries to conclude anyway
            return critic_json({"C1": "MAINTAIN", "C2": "ACCEPT", "C3": "ACCEPT"}, signal="CONCLUDE")
        return critic_json({"C1": "ACCEPT"}, signal="CONCLUDE")

    result = run(critic)
    rounds = result.ledger.rounds
    assert rounds[1].decision == "continue" and "C1" in rounds[1].feedback
    assert result.ledger.termination == "consensus" and len(rounds) == 3


def test_moderator_feedback_reaches_the_critic():
    def critic(prompt, _):
        rnd = round_of(prompt)
        if rnd == 1:
            return opening_json(*THREE)
        if rnd == 2:
            return critic_json({"C1": "MAINTAIN", "C2": "ACCEPT", "C3": "ACCEPT"}, signal="CONCLUDE")
        return critic_json({"C1": "ACCEPT"}, signal="CONCLUDE")

    fake = Fake(critic)
    deliberate("Request.", "ctx", {"proposer": Fake(proposer_json), "critic": fake, "summarizer": Fake(summarizer_json)}, GATED)
    round3 = fake.prompts[2][0]["content"]
    assert "Note from the moderator" in round3 and "C1" in round3


def test_a_critic_that_is_never_satisfied_still_terminates_without_hitting_the_cap():
    def critic(prompt, _):  # maintains everything and always spends its full budget
        new = [challenge("MAJOR", "OPERATIONS")] * budget_of(prompt)
        if round_of(prompt) == 1:
            return opening_json(*THREE, *new[3:])
        return critic_json({c: "MAINTAIN" for c in open_ids(prompt)}, new=new)

    result = run(critic)
    assert result.ledger.termination == "converged"
    assert len(result.ledger.rounds) < GATED.max_rounds
    assert all(i.status == "ESCALATED" for i in result.ledger.issues.values())


def test_continue_with_nothing_open_converges():
    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, signal="CONTINUE")

    result = run(critic)
    assert result.ledger.termination == "converged" and len(result.ledger.rounds) == 2


def test_conclude_without_mandatory_lens_coverage_is_rejected():
    ops = [challenge("MAJOR", lens) for lens in ("OPERATIONS", "DATA_QUALITY", "FEASIBILITY")]

    def critic(prompt, _):
        rnd = round_of(prompt)
        if rnd == 1:
            return opening_json(*ops)
        if rnd == 2:
            return critic_json({c: "ACCEPT" for c in open_ids(prompt)}, signal="CONCLUDE")
        return critic_json({}, signal="CONCLUDE", coverage=("CONFIDENTIALITY", "DEFINITIONS", "OWNERSHIP"))

    result = run(critic)
    assert "no challenge raised and no coverage note" in result.ledger.rounds[1].feedback
    assert result.ledger.termination == "consensus" and len(result.ledger.rounds) == 3


def test_naive_policy_takes_the_critics_word_even_with_a_blocker_open():
    def critic(prompt, _):
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        return critic_json({"C1": "MAINTAIN", "C2": "ACCEPT", "C3": "ACCEPT"}, signal="CONCLUDE", confidence=90)

    result = run(critic, policy=NAIVE)
    assert result.ledger.termination == "consensus" and len(result.ledger.rounds) == 2
    assert result.ledger.issues["C1"].status == "UNRESOLVED"  # closed over an open blocker


def test_two_strikes_escalate_an_issue_to_humans():
    def critic(prompt, _):
        rnd = round_of(prompt)
        if rnd == 1:
            return opening_json(*THREE)
        rulings = {c: ("MAINTAIN" if c == "C1" else "ACCEPT") for c in open_ids(prompt)}
        return critic_json(rulings, signal="CONCLUDE" if rnd == 3 else "CONTINUE")

    result = run(critic)
    c1 = result.ledger.issues["C1"]
    assert c1.status == "ESCALATED" and c1.strikes == 2
    assert result.ledger.termination == "consensus"
    assert [q.issue_id for q in result.synthesis.open_questions] == ["C1"]


def test_cap_is_a_backstop_for_a_critic_that_keeps_concluding_against_the_evidence():
    from dataclasses import replace

    def critic(prompt, _):  # maintains the blocker and concludes every round, with no strike limit
        if round_of(prompt) == 1:
            return opening_json(*THREE)
        return critic_json({c: "MAINTAIN" for c in open_ids(prompt)}, signal="CONCLUDE")

    result = run(critic, policy=replace(GATED, strike_limit=None, max_rounds=4))
    assert result.ledger.termination == "cap" and len(result.ledger.rounds) == 4
    assert all(i.status == "UNRESOLVED" for i in result.ledger.issues.values())
