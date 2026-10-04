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
