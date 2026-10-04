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

## v6 → sixth live batch (2026-10-04 ~13:00, code cebe2dc)

| Request | Rounds | Exit | Proposer moves | Critic rulings | Escalated | Open questions | Repairs |
|---|---|---|---|---|---|---|---|
| right-contact | 5 | converged | 8 REVISE, 1 CONCEDE | 5 ACCEPT, 4 MAINTAIN (2 auto-escalated) | 2/7 | 2 | 3 |
| engagement-history | 2 | converged | 3 REVISE | 2 ACCEPT, 1 ESCALATE | 1/3 | 1 | 1 |
| cold-relationship | 3 | consensus | 8 REVISE | 7 ACCEPT, 1 MAINTAIN | 0/7 | 0 | 2 |
| auto-logging | 3 | converged | 8 REVISE | 5 ACCEPT, 1 MAINTAIN, 2 ESCALATE | 2/7 | 2 | 2 |
| influence-ranking | 6 | converged | 14 REVISE, 2 DEFEND | 1 ACCEPT, 8 MAINTAIN, 7 ESCALATE (3 auto) | 10/11 | 10 | 8 |

What improved: round 1 now raises 6 challenges in 4/5 runs (it was always 3); MAINTAIN is back (14, v5: 0); the
Critic's attempts to accept answers parked in assumptions were refused 11 times, and from round 3 on it maintained
them itself ("based on an assumption rather than a decision").

What didn't:
1. **The Proposer writes its decisions into assumptions.** In influence-ranking every revision from round 2 to 6 edited
   only A1–A4 (authority, criteria, governance, retention); right-contact C5/C7 edited only A1 for three rounds. The
   Critic was right not to accept, but the Proposer never moved the decision into an S or D item, so those issues
   were maintained twice and auto-escalated: 10 of 11 influence-ranking issues ended with humans.
2. **The Critic still accepts promises and unnamed roles**, now with a paraphrase as the "fact": "A process will be
   established to reassign alert notifications" (fact: "A process exists to reassign notifications"), "with clearly
   defined roles for who is authorized to edit ... and a conflict resolution protocol", "periodic audits", "a
   designated oversight committee", "appropriate security clearance as defined in organizational policy". Labelling
   the 43 ACCEPTs of v5–v6 by hand, 28 rest on a promise, an unnamed role, an invented fact or an untestable condition.
3. **Same-turn duplicates.** When it maintains or escalates an issue, the Critic also re-raises it as a new challenge:
   cold-relationship C7 and auto-logging C7 repeat C1 and C4 word for word; influence C7/C8 restate C4/C5.
4. **Defenses can't win any more**: 2 DEFEND in 44 moves (v4: 15/45). The v6 test ("does the fact answer your test and
   stop your failure scenario?") has no path for a defense that is right because the test asked for design detail or
   the risk is acceptable, and the Proposer revises even MINOR challenges.
5. engagement-history raised only 3 challenges (with 6 gaps listed) and ended after round 2 with nothing new: without
   the gaps list in round 2, nothing prompted the rest. "Full history" (how far back) was never bound or challenged.
6. Still no "should this exist?" (influence ranking) and no challenge to auto-logging being manual entry.

## v7 changes

Each rule below comes from a v6 failure and is a check in the ledger: a move that breaks it gets one repair request
and is then coerced.
- **A revision can't consist only of assumption edits** (v6 #1). The Proposer is told at once to write the decision
  into a V, S, X, D or K item (or to choose NEEDS_HUMAN_DECISION if only the organisation can decide), instead of
  learning it from two MAINTAINs and an auto-escalation. If the repair fails too, the answer is recorded as "no usable
  answer". The prompt adds: a challenge that targets an assumption is still answered with a decision.
- **Weak phrases can't carry an ACCEPT** (v6 #2). An ACCEPT is refused when the quoted words, or the few words that
  govern them ("A process will be established to [reassign alerts...]"), lean on a phrase that names no role, number
  or rule: "will be established/developed/defined...", "appropriate", "a designated team/manager...", "authorized
  personnel", "clearly defined", "safeguards in place", "measures to", "periodic audits", "including but not limited
  to". Requirements-quality tools have flagged such weak phrases since NASA's ARM tool; this list is the subset seen in
  v5–v6, kept to phrases that are vague wherever they appear ("protocol officer", "a periodic digest every Monday",
  "will be determined by the date of the last meeting", "will be developed in a later release" and "authorized users
  including regional coordinators" all pass). Replaying the 43 ACCEPTs of v5–v6 against the proposals the Critic saw,
  v7 refuses 18 of the 28 hand-labelled vague or invented answers (15 weak phrases, 3 assumptions) and 1 of the 15
  concrete ones (a quote that included a vague second clause; the repair asks for the sentence that states the fact).
  The rest need judgement a pattern can't give: untestable conditions and invented teams. It also applies to an
  acceptable-risk defense's mitigation, but not to "decided in design" or "covered by S3" defenses.
- **A new challenge can't repeat an open question** (v6 #3): the same words in the same order, give or take two
  inserted words ("What specific guidelines..." repeats "What guidelines..."), while a changed word ("view" vs "edit")
  is a different question. Closed issues may be raised again, since a later edit can reopen them. The repair says to
  MAINTAIN instead; coercion drops repeats before cutting to the budget.
- **Defenses can win again** (v6 #4). The verdict's `answered` became `settled`: the fact answers the test and stops the
  failure scenario, *or* a defense's argument holds (design detail, already covered, acceptable risk), with `fact`
  naming what the argument establishes. A challenge the Proposer sent to humans is never settled here; a refused ACCEPT
  of one is routed by the Critic's own `needs_human_decision`, so a product rule punted to humans comes back to the
  Proposer. Proposer prompt: a MINOR challenge usually deserves an acceptable-risk defense; spend revisions on BLOCKERs
  and MAJORs.
- **Round 1 covers every gap it lists** (v6 #5). `gaps` now lists only the questions the proposal answers badly or not
  at all, and each gets a challenge: at least min(budget, max(3, number of gaps)).
- An independent review of the diff found, and these changes fix: the budget cut ran before repeats were dropped (so a
  repeat could displace a real challenge); the repair for an accepted NEEDS_HUMAN answer asked for a change that didn't
  alter the ruling; the first weak-phrase list refused real roles ("protocol officer") and was dodged by trimming the
  quote; repeats were checked against closed issues; and coercion left assumption-only revisions failing the check.
  Coerced rulings now carry the real refusal reason, so the Proposer and the record see which phrase failed.

## v7 → seventh live batch (2026-10-04 ~13:45, code 8be7379)

| Request | Rounds | Exit | Proposer moves | Critic rulings | Escalated | Open questions | Repairs |
|---|---|---|---|---|---|---|---|
| right-contact | 4 | consensus | 6 REVISE, 3 DEFEND | 6 ACCEPT, 3 ESCALATE | 3/9 | 3 | 6 |
| engagement-history | 4 | converged | 7 REVISE, 3 DEFEND | 6 ACCEPT, 4 ESCALATE | 4/10 | 4 | 4 |
| cold-relationship | 2 | converged | 5 REVISE, 1 DEFEND | 4 ACCEPT, 2 ESCALATE | 2/6 | 2 | 1 |
| auto-logging | 4 | converged | 7 REVISE, 2 DEFEND | 5 ACCEPT, 2 ESCALATE, 2 MAINTAIN (1 auto) | 3/8 | 3 | 5 |
| influence-ranking | 5 | consensus | 8 REVISE, 3 DEFEND | 8 ACCEPT, 2 ESCALATE, 1 MAINTAIN | 2/10 | 2 | 7 |

The most balanced batch so far: 33 REVISE / 12 DEFEND (v6: 2 DEFEND), every run 2–5 rounds, 2–4 open questions per
document, no assumption loops (the assumption-only rule fired 9 times and the repair worked in all but one). The
influence ranking moved from subjective High/Medium/Low to auditable thresholds (seniority, at least three engagements
for High). Remaining problems:
1. **A weak-phrase false positive cost a real decision.** auto-logging C8: the Proposer wrote "access controls limited
   to authorized users based on their role, specifically the roles of regional coordinators and project managers";
   the Critic accepted it, the check refused "authorized users", the Critic then reversed itself, and C8 was
   auto-escalated. A list can't tell an unnamed role from one that is named a few words later.
2. **The Critic re-raises what it just escalated**, in other words (engagement C7/C9 restate escalated C2; auto-logging
   C7/C8 restate escalated C2/C6), and the Proposer then answers it again.
3. **New challenges target earlier challenges** ("targets: C2"): 6 repairs across 4 runs.
4. Resolution tests that aren't questions still appear ("Specify...", "Define...", "Detail..."): 3 in auto-logging.
5. Known limits, unchanged: invented facts are sometimes accepted ("the CRM Data Steward", "retains data for five years
   complying with GDPR"); vague answers that avoid the listed phrases pass ("implement a process for identifying and
   managing duplicates"); no "should this exist?" challenge, and auto-logging still never asks how logging is automatic.

## v7.1 changes (small; prompts frozen after this)

- **Unnamed roles are weak only when no role is named.** Weak phrases split into promises ("will be established",
  "safeguards in place", ...), weak wherever they appear, and unnamed roles ("authorized users", "a designated manager",
  "appropriate"), weak unless the quoted words name a role after all. Replayed on v5–v6, this refuses 17 of the 28
  vague accepts and none of the 15 concrete ones; it would have kept auto-logging C8.
- **A new challenge may name the challenge it follows up**; it takes over that challenge's targets.
- **A resolution test must be a question** (ends with "?"); the repair asks for one with a concrete answer.
- **A question that is with humans can't be asked again** (word for word, give or take two words); the task line says
  not to re-raise what was just escalated.

## Comparison batch (2026-10-04 ~14:20, code 9545bcc)

Five requests × three runs × three configurations, gpt-4o-mini throughout, ~$0.50 in total. Full table in
`experiments/results.md`; runs in `experiments/runs/`. `naive` swaps the termination policy (stop rule, constant
budget of 6, no two-strike escalation); `generic` swaps the prompts (no role stakes, no burden-of-proof guidance).

| | gated | naive | generic |
|---|---|---|---|
| Runs closed with a BLOCKER/MAJOR open | 0/15 | 7/15 | 0/15 |
| Ended consensus / converged / cap | 2 / 13 / 0 | 12 / 0 / 3 | 8 / 7 / 0 |
| Rounds, median (range) | 3 (2–5) | 6 (2–8) | 3 (2–6) |
| Challenges raised per run | 7.4 | 15.1 | 7.9 |
| Defenses on merit (accepted) | 15 (4) | 7 (2) | 1 (0) |
| Revisions accepted by the Critic | 84% | 76% | 84% |
| Repair requests per run | 2.1 | 5.1 | 2.7 |

What it shows:
1. **naive concludes over its own objections.** In 3 of its 12 CONCLUDEs the Critic maintained a MAJOR in the same
   turn (auto-logging/3 C16, engagement-history/1 C10, right-contact/3 C14 and C16); a fourth left a question the
   Proposer had sent to humans open (engagement-history/3 C18); 3 runs hit the cap. The ledger-built record still
   lists those questions, under a "consensus" header.
2. **naive's extra challenges are mostly re-asks.** right-contact/1 asked the data-protection-compliance question four
   times (C10, C11, C20, C22) and ended with 7 BLOCKERs open, 6 raised in round 8; influence-ranking/3 maintained C16
   three rounds running while S11 grew. Proposals grew 77% in words (gated 35%).
3. **gated's gate never fired.** The Critic concluded twice, both with nothing open; 13 runs ended `converged`. The
   shrinking budget and the two-strike rule emptied the ledger before the Critic could conclude over an open issue.
4. **The opposed prompts change the Proposer, not the Critic.** Same accept rate for revisions; 15 merit defenses vs 1;
   runs with no defense 1/15 vs 4/15; the Critic declared itself satisfied 2/15 vs 8/15. Of the 4 accepted merit
   defenses (all MINOR), one is clean (engagement-history/2 C6); MINOR risk disputes usually deadlock and are
   auto-escalated (cold-relationship/3 C5, right-contact/1 C6, influence-ranking/1 C6).
5. **What the ledger sent back** (gated, 31 repair requests, 46 problems): 16 assumption-only revisions, 10 resolution
   tests that weren't questions, 7 ACCEPTs quoting outside a decided item, 5 weak phrases, 4 round-1 openings short of
   their gaps, 2 repeats, 1 defense with edits, 1 missing answer.

Audit of the 15 gated decision documents (red flags kept as README limitations): invented roles and teams accepted
("data privacy officer", "compliance team", "data management team"); the Critic's `fact` often describes the quote
instead of stating it; the same question escalated twice in different words (right-contact C4/C7, auto-logging
C2/C7 and C5/C8, influence-ranking C3/C8, cold-relationship/2 C6/C7); role-change rules escalated although they are
the agents' to decide; scope never shrinks (no "should this exist?"); a self-contradicting scope in right-contact/2
(X3 excludes the notifications S1 includes); an unchallenged PDF export in engagement-history/3.

### Fix after the batch (rendering only; prompts for the deliberation unchanged)

- **Whether an open question blocks the build now follows from the Critic's severity.** The Rapporteur had been
  asked to judge it and marked 14 of 16 MINOR questions as blocking (and 1 BLOCKER as not). Severity already defines
  it ("MINOR: won't sink the release"), and decisions belong to the ledger, so the field left the Rapporteur's
  schema and prompt. The decision header also counts challenges settled, handed to humans and still open, so a
  "consensus" with open questions is visible at a glance.
- All 45 runs replayed through the new code: ledgers, traces, events and run metadata byte-identical; decision
  documents changed only by the new line, 25 corrected labels and 4 reorderings. The re-rendered documents replaced
  the originals in `experiments/runs/`.
- Published `runs/` (one gated run per request): right-contact/1, engagement-history/2, cold-relationship/3,
  auto-logging/1, influence-ranking/1, chosen for the fewest red flags in the audit; each replays identically.
