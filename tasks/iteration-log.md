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

## v4 → fourth live batch (2026-10-04 ~11:30, code dc9e895)

| Request | Rounds | Exit | Proposer moves | Critic rulings | Escalated | Open questions | Repairs |
|---|---|---|---|---|---|---|---|
| right-contact | 5 | converged | 7 REVISE, 2 DEFEND | 5 ACCEPT, 3 ESCALATE, 1 MAINTAIN | 3/8 | 3 | 1 |
| engagement-history | 5 | converged | 6 REVISE, 2 DEFEND | 2 ACCEPT, 4 ESCALATE, 2 MAINTAIN | 4/6 | 4 | 2 |
| cold-relationship | 5 | converged | 12 REVISE, 2 DEFEND | 5 ACCEPT, 1 ESCALATE, 8 MAINTAIN | 4/9 | 4 | 9 |
| auto-logging | 5 | converged | 2 REVISE, 7 DEFEND | 4 ACCEPT, 5 ESCALATE | 5/9 | 5 | 2 |
| influence-ranking | 3 | consensus | 3 REVISE, 2 DEFEND | 5 ACCEPT | 0/5 | 0 | 1 |

First balanced batch: 30 REVISE / 15 DEFEND; the Critic accepts (21), escalates directly (13) and maintains (11);
0–5 open questions per document.

Remaining problems:
1. **The Proposer still describes edits it doesn't write**, even with the proposal first. cold-relationship round 3:
   five revisions claimed, one item (S6) actually changed; after the repair, two. The integrity checks did their job
   (the Critic's quotes of the rationale were refused; the one real edit, S3, was accepted), but the gap costs
   repairs and turns fixable issues into escalations. Regenerating a long document with targeted changes is
   exactly what a small model is bad at.
2. **Defenses that edit.** influence-ranking C4/C5 were labelled NEEDS_HUMAN_DECISION but added S7/S8.
3. **No "should this exist?"** influence-ranking kept 1–5 ratings of named officials; no challenge questioned
   holding them at all, and nothing was conceded in any run.
4. **The Critic rarely concludes.** 4/5 runs ended `converged` (nothing open, Critic still saying CONTINUE):
   it seems to treat escalated issues as unfinished business.
5. Evidence can be real text that doesn't answer the question (C3 asked who may *view* scores; the quoted S5 is
   about who may *assign* them). A lexical check can't catch that; it's a stated limitation.

## v5 changes (code: see the commit after dc9e895)

- **The Proposer emits edits, the engine applies them.** Round 1 returns the full proposal (`ProposerOpening`);
  afterwards each response carries `edits` (item ID + complete new wording; empty text removes the item) and the
  turn restates the two-sentence summary. `Proposal.edited()` applies them in order, so claimed and actual changes
  are the same by construction. The ledger refuses, with one repair: a defense with edits, a revision or concession
  without them, an ID that isn't an item ID, removing a core commitment, removing an item that doesn't exist, an edit
  that changes nothing, reusing the ID of an item removed earlier, two answers giving one item different wordings
  (1 of 15 revising rounds in v4 had two answers touching one item, so repeating the same wording costs little), two
  new items with the same ID, and a turn that would leave a section empty. The Proposer is shown the next unused ID
  per section. After a failed repair the illegal edits are dropped, and an answer whose claimed change is then empty
  is recorded as a defense, so the ledger never shows a revision or concession that changed nothing.
- **Every proposal item is `{id, text}`.** Definitions read '"right person" means...', assumptions end with what in
  the request depends on them, success criteria state metric, target and measurement in one sentence. Edits, diffs,
  quoting and rendering now work the same way for every section; the per-section models and the quote-stripping
  validator are gone.
- **Pre-mortem.** The Critic's opening starts with `pre_mortem`: a year after launch this feature caused a serious
  incident; what happened? If the proposal doesn't prevent it, that is the first challenge. Later rounds show the
  Critic its pre-mortem next to its round-1 gaps.
- **Concluding.** The prompt and the task line now say escalated challenges are closed for this deliberation (humans
  decide them, the record lists them as open questions), and spell out when to conclude: no BLOCKER or MAJOR still
  open after the rulings and nothing new raised.
- Found by an independent review of the v5 diff and fixed before the batch: the cases above about new-item IDs, emptied
  sections (checked on the result, not edit by edit) and coerced revisions; dropped assumptions now show as dropped in
  the decision record, linked to the challenge whose answer removed them; test doubles now record each call's
  messages separately, so repair tests read the repair that was really sent.

## v5 → fifth live batch (2026-10-04 ~12:08, code 9d30d63)

| Request | Rounds | Exit | Proposer moves | Critic rulings | Escalated | Open questions | Repairs |
|---|---|---|---|---|---|---|---|
| right-contact | 4 | converged | 4 REVISE, 2 DEFEND | 3 ACCEPT, 3 ESCALATE | 3/6 | 3 | 3 |
| engagement-history | 3 | converged | 3 REVISE, 3 DEFEND | 3 ACCEPT, 3 ESCALATE | 3/6 | 3 | 0 |
| cold-relationship | 3 | consensus | 5 REVISE, 1 CONCEDE | 6 ACCEPT | 0/6 | 0 | 1 |
| auto-logging | 3 | consensus | 5 REVISE, 1 DEFEND | 5 ACCEPT, 1 ESCALATE | 1/6 | 1 | 0 |
| influence-ranking | 4 | converged | 6 REVISE, 1 DEFEND | 6 ACCEPT, 1 ESCALATE | 1/7 | 1 | 2 |

What worked: claimed and actual edits now match by construction (no "described but not written" revisions); repairs
fell from 15 to 6; runs are shorter (3–4 rounds, $0.005–0.009 each); the first CONCEDE appeared.

What didn't:
1. **The Critic accepts any related text: 23 ACCEPT, 9 ESCALATE, 0 MAINTAIN** (v4: 11 MAINTAIN). Accepted answers
   include invented organisation facts ("a 'Data Governance Team'", "security clearance level 3", "retention policies
   dictate 5 years"), answers written into assumptions (influence A1, auto-logging A4), promises ("a process will be
   established to transfer or archive"), unnamed roles ("authorized users with appropriate clearance", "a designated
   manager"), a circular definition ("'High' indicates a significant influence") and an untestable condition (alerts
   only "when there are no ongoing diplomatic negotiations", which the system can't know). In v4 most revisions were
   never written, so MAINTAIN was easy to justify; now every revision has a real edit under the challenge, and the
   Critic reads "related text exists" as "answered".
2. **Duplicate challenges.** Later rounds walk the round-1 gaps list in order, including gaps already settled
   (influence C6 = C1 and C7 = C3, engagement C5 = C3, right-contact C4 = C3). In all 15 runs of v3–v5 the Critic
   raised exactly 3 challenges in round 1, the stated minimum ("between 3 and 6"), leaving the rest for later rounds.
3. **The one-wording rule lost a decision.** right-contact C1 and C3 both edited S1; C3's wording built on C1's (what
   we want) but differed, failed twice, was coerced to "no usable answer", escalated, and came back as C4.
4. Edit texts often repeat their ID ("S3: S3: ..."), 7 items.
5. Product rules punted to humans and escalated (engagement C6: access when a project manager changes role or leaves,
   which the Proposer prompt names as ours to decide).
6. An out-of-scope item rewritten as an inclusion (influence X3: "This release will include role-based access...").
7. Still no "should this exist?": the influence ranking keeps subjective ratings of named officials; auto-logging
   defined "automatically" as manual form entry and nobody challenged it.
8. 3/5 runs end `converged`: the Critic says CONTINUE with nothing open and nothing new.

## v6 changes

- **The Critic quotes, names the fact, then judges.** Each verdict runs in fixed steps: `evidence` (the words that come
  closest to answering the test), `fact` (what they commit to: a role, number, rule or yes/no; "no fact" for a promise,
  an unnamed role, a circular definition or something the system can't know), `answered` (does the fact answer the test
  *and stop the failure scenario as described*), `unconfirmed` (does the answer rest on a team, policy, clearance, law
  or system the system description doesn't mention), `needs_human_decision` (does answering the test need authority
  neither agent has). The ruling is derived: answered and confirmed → ACCEPT; otherwise the *question* decides where
  it goes: needs humans → ESCALATE, a rule the agents can decide → MAINTAIN. So an invented retention policy is
  escalated, while "access on role change follows existing policy" goes back to the Proposer, because role changes
  are ours to decide. An ACCEPT without a named fact is refused like one without evidence.
- **Assumptions can't settle a challenge.** Evidence quoted from an A item is refused, including through a defense that
  merely repeats the assumption: assumptions are what the release depends on, not what it decides. Quotes are credited
  to the text they match best, in order (an order-aware match replaced the bag-of-words one; all 44 accepted quotes
  from v4–v5 still match).
- **Product rules are never for humans** (`needs_human_decision` says so explicitly).
- **Round 1 isn't anchored on a minimum.** The task asks for one challenge per gap the proposal leaves unanswered (up
  to the budget) instead of "between 3 and 6"; the ≥3 rule still applies through the check. The gaps list is no longer
  shown again after round 1 (re-showing it produced the duplicates); the pre-mortem still is, and now asks about
  something the feature created (a record, list, score or alert) that reached the wrong person, was wrong, or should
  never have existed.
- **Edits.** Several answers may edit one item; edits apply in order, so the later wording replaces the earlier (the
  prompt says to write it to include both changes) and the Critic judges the result. A new item may be refined that
  way, but a later wording that drops the earlier one's words is a different item and needs its own ID. An item can't
  be removed by one answer and rewritten by another. A concession must drop or descope something, and a revision that
  only removes items is a concession; mislabelled moves are sent back, and corrected if the repair fails. A repeated
  "S3:" at the start of an item's text is stripped (colon form only, so "S1-S3 apply" survives).
- Proposer prompt: an out-of-scope item never describes something the release includes; edits must name the role,
  number or rule.
- An independent review of the diff found, and these changes fix: Critic coercion crashed when a ruling was missing
  (the filler verdict lacked the new fields); removing then rewriting an item in one turn resurrected it while the
  concession still counted; the first ruling design sent "follows existing policy" punts on role changes to humans;
  "none" was both the no-fact marker and a legitimate answer ("which roles can export? none"); the ID stripper could
  eat "S1-S3".
