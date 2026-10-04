# Design decisions

The brief's central risk is two agents that either agree at once or never stop. My answer takes both outcomes away
from them: each turn is a typed move (a revision, a defense, a ruling) that a ledger validates and applies, and the
ledger decides what is settled, what goes to humans and when to stop. Seven live batches showed where the leverage is:
asking gpt-4o-mini to behave did little; making a bad move impossible to express, or checkable by code, fixed every
failure I measured.

## 1. The prompts

**Opposed stakes, not opposed personalities.** The Proposer is the product owner, judged on delivered value; the
Critic is the architect who owns the data-protection sign-off. The burden of proof sits with the Critic: a challenge
earns a change only if its failure scenario is plausible and material. I tested this by removing the stakes (the
`generic` runs). The Critic accepted 84% of revisions either way; what changed was the Proposer. With the stakes it
defended on the merits 15 times, without them once (28 of its 29 defenses were "a human must decide"). Arguing isn't
winning: the Critic accepted 4 of the 15, all minor; most of these disputes are about risk appetite and go to a named
human.

**Classify, then derive.** Neither agent picks its move directly: the Proposer names the kind of challenge it faces
(missing decision, design detail, acceptable risk, needs a human) and the move follows; the Critic quotes the words
closest to answering its test, names the fact they commit to and judges whether it is settled, and the ruling follows.
Models classify honestly but don't push back when merely asked: prose about when to defend (v2) produced 0 defenses in
46 moves; a grounds field (v3) produced 65%.

**Specific pushback by construction.** A challenge must name its target items, a lens, a severity, a failure scenario
and a resolution test answerable with a role, a number or a rule, so "have you considered security?" cannot be
expressed. A pre-mortem points the Critic's first challenges at the real risk.

**Where prompts stopped working, the ledger took over.** Rubber-stamped ACCEPTs (v1), revisions described but never
written (v4), promises such as "a process will be established" accepted as answers (v5) and decisions parked in
assumptions (v6) each became a rule the ledger checks (one repair, then a safe coercion); in the 15 final gated runs it
sent back 31 moves. That is why the code is about 1,150 lines rather than 300: the loop and stop rules are about 115,
and the rest are those rules, each traceable in `tasks/iteration-log.md`. A stronger model would need fewer.

## 2. Termination

**The Critic proposes, the ledger disposes.** Round 1's schema has no signal field. From round 2, CONCLUDE is accepted
only if no BLOCKER or MAJOR is open and every mandatory lens (confidentiality, definitions, ownership) has been
examined; otherwise the Critic is told why. A CONTINUE with nothing open and nothing new ends the run as `converged`:
an objection the Critic can't state as a challenge isn't one. The end is certain because the new-challenge budget
shrinks each round (6, 3, 2, 1, 0) and an issue maintained twice goes to humans. The 8-round cap is a circuit breaker
that never fired.

**Alternatives.** I measured the common pattern, the Critic's word plus a round cap (`naive`). In 7 of 15 runs it
closed with a BLOCKER or MAJOR open; three times the Critic concluded in the same turn it maintained a MAJOR
objection. Without convergence pressure it re-asked old questions in new words, took twice as many rounds, cost 1.9
times as much, and in 44 settlements a later edit removed the agreed wording. A fixed round count ends on the clock,
not the content. A confidence threshold fails because self-reported confidence doesn't track open risk (one record
shows the Proposer at 80/100 with a blocker open). A judge model adds another unreliable opinion; the ledger's rule is
deterministic and testable.

**What I accept.** The gate never had to reject a CONCLUDE in the final runs: the budget and the two-strike rule
emptied the ledger first, and in 13 of 15 runs the Critic still said CONTINUE with nothing left. So "done" means every
challenge is agreed or owned by a named human, not that the Critic is satisfied. Two strikes can escalate what one
more round would have settled, and from round 5 a late concern survives only as the Critic's remaining worry.

## 3. One thing I would do differently

I would add a semantic check where the lexical ones run out. The ledger catches missing quotes, assumptions used as
answers and listed weak phrases, but not paraphrased repeats (right-contact C4 and C7 are one question), real text
that doesn't answer the question, or invented roles: the Critic marked 32 of 192 gated answers unconfirmed, never one it had
judged settled. A small verifier model would ask one narrow question per ACCEPT, "does this quote answer this test?",
measured against the 43 hand-labelled ACCEPTs from v5 and v6 as the weak-phrase rule was (17 of 28 vague answers
refused, 0 of 15 concrete).

## Interpretations and other choices

- "The Critic must be capable of signaling completion": it signals; the ledger decides whether that holds.
- "Open questions requiring human input": what needs authority neither agent has (law, policy, budgets, existing
  teams). Who sees what, and what happens when people change roles, are product rules for the agents.
- No framework: the core is a typed loop around a ledger, and orchestration frameworks optimize for the free-form
  conversation this design avoids.
- gpt-4o-mini in every role, at about $0.009 per run.
- I built this with Claude as a pair programmer: it wrote most of the code and prompt drafts and ran the analyses; I
  chose the architecture, ran every live batch and decided what to keep. The commits carry a co-author line.
