# Prompt iteration log

Raw material for DECISIONS.md. Every live batch, what it showed, and what changed because of it.
Model for all live runs: gpt-4o-mini (OpenAI), run by Domi locally. Policy: gated unless stated.

## v1 → first live batch (2026-10-04, code 957cd64)

Inputs: the brief's three requests, one run each. Evidence kept in `experiments/prompt-iterations/v1/`.

| Request | Rounds | Exit | Proposer moves | Critic rulings | Escalated |
|---|---|---|---|---|---|
| right-contact | 2 | consensus | 5 REVISE | 5 ACCEPT | 0 |
| engagement-history | 2 | consensus | 4 REVISE | 4 ACCEPT | 0 |
| cold-relationship | 5 | consensus | 11 REVISE | 7 ACCEPT, 4 MAINTAIN | 2 |

What went wrong:
1. **The Proposer never defended.** 20 of 20 moves were REVISE, despite the burden-of-proof clause.
   The revisions were promises ("I will clarify the ownership responsibilities...") with token edits to the item text.
2. **The Critic rubber-stamped.** It accepted promise-only revisions whose text did not meet its own
   resolution test (right-contact C2 asked "who is responsible"; the revised A2 still names nobody).
   Two of three runs reached consensus in round 2 at 85–90 confidence: the trivial agreement the brief warns about.
3. **Assumption laundering.** right-contact A2/A3 were rewritten from assumptions into claims that the problem
   was already solved ("There is a defined ownership process..."), which then counted as a fix.
4. **The Critic asked for detail, not decisions.** Most challenges were "specify the process/method".
   That invites cheap "will specify" answers and, in cold-relationship, a loop on validation methodology (C4, C6).
5. **It missed the gaps the brief itself names**: how far back the history goes and what one project team
   may see of another's (engagement-history); what happens when contacts change roles or leave (right-contact).
6. **Duplicate challenge.** cold-relationship C6 restated C4 while C4 was still open, so one point was escalated twice.
7. engagement-history's decision document listed **no open questions**, for a request whose confidentiality
   rules are explicitly unstated in the brief. Output quality follows from 1–5.
8. Noise: definition terms sometimes came back wrapped in quotes, producing spurious "edited" diffs;
   the Summarizer wanted to annotate definitions and was refused (1 wasted repair call).

What the gate did right: it rejected nothing here because the Critic never concluded against the evidence.
The problem was upstream, in what counted as evidence. That is the lesson: the gate can only be as good as
the rulings it is fed.

## v2 changes

Mechanics:
- **ACCEPT needs evidence.** Each ruling now carries `evidence`: words copied from the current proposal or the
  Proposer's answer that meet the resolution test. The ledger checks the quote really is there. An ACCEPT
  without it gets one repair, then counts as MAINTAIN. Rubber-stamping becomes as hard to express as generic pushback.
- **Gaps first.** The Critic's round-1 output starts with `gaps`: the questions the request leaves open
  (who, how far back, which data, who must not see it, what happens when people change roles). Its challenges
  should come from those. Later rounds are reminded of them.
- Definition terms are stripped of quotes; the Summarizer may annotate definitions and success criteria.

Prompts:
- Proposer: the proposal is a **scope agreement, not a design document**, which gives DEFEND legitimate grounds
  (implementation detail, already handled by another item, accepted risk with mitigation, needs a human decision).
  REVISE must write the actual decision into the item; promises and assumption rewrites don't count.
- Critic: ask for the missing **decision**, not more detail; don't duplicate an open challenge; ACCEPT only with
  quoted evidence.

## v2 → second live batch (2026-10-04 ~10:50, code 0bed078)

All five requests, one run each.

| Request | Rounds | Exit | Proposer moves | Critic rulings | Escalated | Open questions |
|---|---|---|---|---|---|---|
| right-contact | 5 | consensus | 10 REVISE | 9 ACCEPT, 1 MAINTAIN | 0 | 0 |
| engagement-history | 4 | consensus | 8 REVISE | 8 ACCEPT | 0 | 0 |
| cold-relationship | 5 | converged | 9 REVISE | 9 ACCEPT | 0 | 0 |
| auto-logging | 5 | consensus | 12 REVISE | 8 ACCEPT, 4 MAINTAIN | 1 | 1 |
| influence-ranking | 3 | consensus | 7 REVISE | 6 ACCEPT, 1 MAINTAIN | 0 | 0 |

What improved: no more round-2 rubber stamps; every ACCEPT now quotes text; deliberations run 3–5 rounds.

What didn't:
1. **Still zero DEFENDs (46/46 REVISE).** Listing DEFEND grounds in prose did nothing for gpt-4o-mini.
2. **Evidence loophole.** The Critic quoted the Proposer's *answer*, so a revision that existed only in the answer
   counted (influence-ranking C5: "access is revoked on role change" never reached the proposal).
3. **Invented organisation.** The Proposer resolved policy questions by inventing them ("the CRM data governance team",
   "scores are deleted whenever a contact is modified"), and the Critic accepted. Exactly the questions that should
   have become open questions for humans were settled by fiat, so 4/5 documents had none.
4. **Vague tests admit vague fixes.** Resolution tests read "the proposal outlines X", so "Implement checks and
   validations to manage duplicates" passes with a perfectly real quote.
5. **No "should this exist?"** influence-ranking kept subjective 1–5 ratings of named officials *and* a CSV export of them.
6. Duplicates again (engagement-history C7 = C1 after C1 was settled).
7. The quote matcher was too strict about punctuation (`D3: "term" = ...`, `S6: "..."`): 3 avoidable repairs.

## v3 changes

- **Triage before move.** Each Proposer response now states its `grounds`, and the move follows from it:
  MISSING_DECISION → REVISE; SHOULD_NOT_BUILD → CONCEDE; ALREADY_COVERED, DESIGN_DETAIL, ACCEPTABLE_RISK,
  NEEDS_HUMAN_DECISION → DEFEND. Naming the kind of challenge is a classification the model does honestly;
  choosing to push back is not. NEEDS_HUMAN_DECISION is the legitimate exit for policy, law and org structure.
- **Resolution tests become questions with concrete answers** (a role, a number, a rule, yes/no), not "outline a process".
- **Evidence for a REVISE must be in the proposal**; only a DEFEND or CONCEDE may be evidenced from the answer.
  Matching compares word sequences, ignoring punctuation and quotes.
- Critic: escalate NEEDS_HUMAN_DECISION defenses it agrees with; treat invented teams/policies/laws as non-evidence;
  ask whether risky items should exist at all; check the open and settled lists before raising anything.

## v3 → third live batch (2026-10-04 ~11:05, code 556d603)

| Request | Rounds | Exit | Proposer moves | Critic rulings | Escalated | Open questions |
|---|---|---|---|---|---|---|
| right-contact | 6 | converged | 6 REVISE, 11 DEFEND | 16 MAINTAIN, 1 ESCALATE | 9/9 | 9 |
| engagement-history | 6 | converged | 10 REVISE, 4 DEFEND | 10 MAINTAIN, 2 ESCALATE, 2 ACCEPT | 7/9 | 7 |
| cold-relationship | 6 | converged | 6 REVISE, 14 DEFEND | 20 MAINTAIN | 10/10 | 10 |
| auto-logging | 6 | converged | 4 REVISE, 10 DEFEND | 14 MAINTAIN | 7/7 | 7 |
| influence-ranking | 6 | consensus | 2 REVISE, 14 DEFEND | 15 MAINTAIN, 1 ACCEPT | 7/8 | 7 |

Triage worked on the Proposer, too well: DEFEND went from 0% to 65% of moves, but 51 of 53 defenses were
NEEDS_HUMAN_DECISION. The Critic accepted 3 times in 81 rulings; 40 of 43 issues ended escalated; every run used
the full 6 rounds the design allows (the cap never fired, so termination behaved; the rulings feeding it did not).

Reading the traces:
1. **The Proposer claims edits it doesn't make.** cold-relationship C1: the rationale says S1 now restricts alerts
   to "regional coordinators and project managers"; S1's text never says so (v3 S1 only adds "visible only to
   authorized users"). The evidence rule correctly refused the ACCEPT. Cause: responses are generated before the
   full proposal is regenerated, and the regenerated proposal drops the change.
2. **The Critic moves the goalposts.** C3's test asked *who* maintains records; the answer named roles; the Critic
   then maintained because it was "unclear how this responsibility will be enforced".
3. **NEEDS_HUMAN_DECISION is read too broadly.** "What happens to alerts when a user changes role?" is a product rule
   we can decide, not organisational policy.
4. Repairs for answering already-closed issues (the Proposer answered escalated C3–C6 in round 6).

## v4 changes

- **The Critic classifies too.** Each verdict states `answered` (is the question in my resolution test, as written,
  answered?) and `needs_human_decision`; the ruling is derived: answered → ACCEPT, else needs humans → ESCALATE,
  else MAINTAIN. A new concern can't block an answered question; it has to be a new challenge.
- **A REVISE or CONCEDE must actually change the items it lists** (checked against the previous version), and the
  Proposer now writes its updated proposal *before* its responses, so it describes what it wrote, not what it intends.
- The Critic sees each changed item's current text right under the challenge it answers, so it can quote it.
  Evidence matching tolerates small wording slips (85% of the quote's words found in one item), still rejecting
  descriptions like "S1 has been revised to specify...".
- Proposer prompt: NEEDS_HUMAN_DECISION is for organisational facts (law, policy, budgets, existing teams), not for
  rules of this feature, which are ours to propose (who sees what, thresholds as defaults, what happens on role change).
- Answers or rulings for issues that are no longer open are dropped silently instead of costing a repair.
