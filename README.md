# Deliberation Engine

Two agents deliberate over a vague feature request for a Government CRM and produce a decision
document: what will be built, what won't, what was assumed, and what humans still have to decide.

- The **Proposer** is the product owner. It represents the stakeholder and is judged on delivered value.
- The **Critic** is the principal architect who also owns data-protection sign-off. It is judged on what breaks.
- A **Rapporteur** writes the prose of the decision record afterwards. It cannot change any decision.

Why it is built this way, what else was considered, and what I'd change: [DECISIONS.md](DECISIONS.md).

## Run it

Needs Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env        # then fill in OPENAI_API_KEY or ANTHROPIC_API_KEY (either works)

uv run deliberate --request-id cold-relationship     # one request from config/requests.yaml
uv run deliberate --all                              # all five
uv run deliberate --request "Executives want a dashboard of relationship health."
```

Exported environment variables work too and take precedence over `.env`.

No API key? Every committed run can be replayed from its recorded model outputs, with no API calls:

```bash
uv run deliberate --replay runs/cold-relationship/events.jsonl
```

Tests need no key either: `uv run pytest`.

### Options

| Flag | Default | |
|---|---|---|
| `--request` / `--request-file` / `--request-id ID...` / `--all` | `$DELIBERATION_REQUEST` | Where the request comes from |
| `--policy` | `gated` | `naive` runs the baseline termination policy (Critic's word + round cap) |
| `--provider`, `--model` | whichever key is set | `anthropic` → `claude-haiku-4-5-20251001`, `openai` → `gpt-4o-mini` |
| `--critic-provider`, `--critic-model` | same as Proposer | Run the Critic on a different model family |
| `--context` | `config/system_context.md` | The system description both agents reason about |
| `--prompts DIR` | — | Override prompt files by name |
| `--max-rounds` | 8 | Circuit breaker only; see below |

## What a run produces

Each run writes `out/<request-id>/` (`--out` changes that; the recorded runs this repo ships are in `runs/`, see
[Evidence](#evidence)):

| File | What it is |
|---|---|
| `decision.md` | The decision document (rendered from `decision.json`) |
| `decision.json` | The same, machine-readable |
| `trace.md` | Every round: proposals, responses, rulings, new challenges, ledger state, termination decision |
| `ledger.json` | The full deliberation state |
| `events.jsonl` | Every model call's raw output, which is what `--replay` plays back |

The console prints the same round-by-round view as `trace.md` while the deliberation runs. A replay runs the
recorded model outputs through the current code, so a run recorded before a change to the output schemas only
replays on the commit that recorded it.

## How it works

```
request + system context
  → PROPOSER ⇄ CRITIC                        rounds of typed, validated moves
  → ISSUE LEDGER                             single source of truth
  → termination gate                         pure function of the ledger
  → RAPPORTEUR → decision.json → decision.md
```

**The agents don't chat; they make moves.** Each turn returns JSON (structured outputs, so it is
always schema-valid) that the orchestrator checks against the ledger before applying it:

- The Proposer writes the proposal once, in round 1: core commitments (V), in-scope (S), out-of-scope (X),
  assumptions (A), definitions of every vague term (D) and success criteria (K), each an ID and one sentence.
  From round 2 it answers every open challenge by naming its grounds (a missing decision, something that
  shouldn't be built, already covered, design detail, acceptable risk, needs a human decision). The move
  follows from the grounds (**REVISE**, **CONCEDE** or **DEFEND**), and a revision or concession carries
  **edits**: the new wording of each item it changes. The engine applies the edits, so what the Proposer
  says it changed is exactly what changed.
- The Critic opens with a pre-mortem (a year after launch, something this feature created caused an
  incident: what happened?) and the questions the request leaves open, then raises challenges. Each must name the IDs it targets, a
  lens, a severity, a concrete failure scenario and a resolution test phrased as a question with a concrete
  answer. Generic pushback cannot be expressed in the schema. From round 2 it rules on every answered
  challenge in fixed steps: it quotes the words that come closest to answering its test (from a decided item,
  or from the Proposer's answer to a defense or concession, never from an assumption), names the concrete fact
  they commit to, and judges whether the challenge is settled: the fact answers the test and stops the failure
  scenario, or a defense's argument holds. The ruling follows: settled with nothing unconfirmed → **ACCEPT**
  (the ledger checks the quote is really there, names a fact, and doesn't lean on a weak phrase such as "a
  process will be established"); otherwise a test that needs authority neither agent has (law, policy,
  budgets, existing teams) → **ESCALATE** to humans, and any other → **MAINTAIN**, back to the Proposer. An
  answer the Critic judges to rest on a team, policy or system nobody has confirmed is never accepted.
- An illegal move (a missing answer or ruling, an over-budget or repeated challenge, a resolution test that isn't a
  question, a defense that edits, a revision that doesn't or only touches assumptions, a concession that drops nothing, an attempt to remove a
  core commitment, an ACCEPT without a concrete fact or real evidence) gets one repair request; if that also
  fails, the orchestrator coerces it safely and records a warning.

**Termination: the Critic proposes, the ledger disposes.** The Critic signals CONCLUDE or CONTINUE every round
from round 2 (round 1's schema has no signal field at all), and the ledger decides what the signal is worth:

1. **CONCLUDE** is accepted only when no BLOCKER or MAJOR issue is open and each mandatory lens
   (confidentiality, definitions, ownership) has a challenge or a coverage note. Otherwise it is rejected and
   the reason goes back to the Critic as a moderator's note. Exit: `consensus`.
2. **CONTINUE** with nothing open and nothing new raised ends the run: an objection the Critic can't state as a
   challenge isn't one. If a mandatory lens was never examined, the Critic first gets one more round, once, to
   examine it or say why it carries no risk. Exit: `converged`.

Two mechanisms make deliberation end by construction: the Critic's new-challenge budget shrinks each round
(6 → 3 → 2 → 1 → 0), and an issue maintained twice is escalated to humans as an open question instead of
looping. So every issue lives at most two rounds after it is raised, and the round cap (8) is a circuit breaker
that should never fire (exit: `cap`). In practice `converged` is the usual exit: in 13 of the 15 recorded gated
runs the Critic was still saying CONTINUE when the ledger emptied (see [Evidence](#evidence)).

The policy is about 50 lines in [`src/deliberation/termination.py`](src/deliberation/termination.py); every exit
of both policies is covered in [`tests/test_termination.py`](tests/test_termination.py).

**The decision document is built from the ledger, not from a summary.** Scope, statuses and assumptions come
straight from the ledger, and so do which issues become open questions, whether each blocks the build (from the
Critic's severity) and where each side stood when the question left the agents. The Rapporteur writes the prose:
the summary, the notes on each item, and each question's wording, owner and options; every ID in its structured
fields is checked. The document also reports a **disagreement index** per round (severity-weighted share of
issues not settled by agreement), each agent's final confidence and remaining worry, and flags when an agent
claims high confidence while a blocker is unsettled, or when a later edit removed the wording that settled a
challenge.

## Where things are

| Path | |
|---|---|
| `DECISIONS.md` | Design decisions, the alternatives considered and their trade-offs |
| `prompts/` | Every prompt, as Markdown ([guide](prompts/README.md)) |
| `config/system_context.md`, `config/requests.yaml` | The CRM description and the five requests |
| `src/deliberation/termination.py` | Both termination policies |
| `src/deliberation/ledger.py` | Ledger state, move legality, transitions, metrics |
| `src/deliberation/agents.py` | Fills prompts, calls models, validate → repair → coerce |
| `src/deliberation/engine.py` | The round loop and replay |
| `src/deliberation/render.py` | Console, `trace.md`, decision document |
| `src/deliberation/schemas.py` | Every agent's output contract |
| `src/deliberation/llm.py` | Anthropic, OpenAI and scripted clients |
| `experiments/` | The comparison harness and its results |

## Evidence

Everything below comes from 45 recorded runs: the five requests, three times each, under three configurations,
with gpt-4o-mini in every role (about $0.50 in total). All of them are in [`experiments/runs/`](experiments/runs/)
and replay offline; [`experiments/results.md`](experiments/results.md) is regenerated from their ledgers by
`uv run python experiments/ablate.py report`.

### The traces

`runs/` holds one run per request: for each, the `gated` run whose decision document had the fewest problems when
all 15 were read through (all 15 are in `experiments/runs/gated/`). Start with cold-relationship.

| Request | | What to look at |
|---|---|---|
| cold-relationship (brief) | [trace](runs/cold-relationship/trace.md) · [decision](runs/cold-relationship/decision.md) | 3 rounds. C4 is maintained ("vagueness over the specific roles") and accepted once the revision names one. Two MINOR acceptable-risk defenses: C6 is accepted after a monthly accuracy review is added; C5 (alert fatigue) is maintained twice and handed to the product owner. |
| right-contact (brief) | [trace](runs/right-contact/trace.md) · [decision](runs/right-contact/decision.md) | 5 rounds. Access is limited to each project team's own countries (S4) and primary contacts are reviewed quarterly by regional coordinators (S1). A risk-acceptance dispute about the change log (C6) goes to humans after two strikes. The record flags that C9's edit to S4 removed the wording that had settled C8. |
| engagement-history (brief) | [trace](runs/engagement-history/trace.md) · [decision](runs/engagement-history/decision.md) | 2 rounds. "Full history" becomes the last five years, with diplomatic notes excluded (S3, S4). A defense wins on merit (C6: X1 already rules out editing), and the engine drops a re-asked question. |
| auto-logging | [trace](runs/auto-logging/trace.md) · [decision](runs/auto-logging/decision.md) | 3 rounds. Who counts as a government official (D4), who sees the logs (S4), who is notified (S2). Also shows two limitations: "automatic" is never pinned down, and two questions reach humans twice in different words. |
| influence-ranking | [trace](runs/influence-ranking/trace.md) · [decision](runs/influence-ranking/decision.md) | 5 rounds, ending in consensus (the Critic concluded and the ledger agreed): three challenges narrow "influence" to weights (50/30/20) and numeric thresholds (C1 → C7 → C10). Nobody asks whether ranking named officials should exist at all. |

### What the comparison shows

Same model, requests, ledger and checks in all three configurations. `gated` is the shipped engine. `naive` swaps
the termination policy for the one most frameworks ship: the Critic's word plus a round cap, with a constant
challenge budget and no two-strike escalation. `generic` keeps gated termination but drops the roles' stakes and
the burden-of-proof guidance from the prompts.

| | gated | naive | generic |
|---|---|---|---|
| Runs closed with a BLOCKER/MAJOR still open | **0/15** | 7/15 | 0/15 |
| Ended consensus / converged / cap | 2 / 13 / 0 | 12 / 0 / 3 | 8 / 7 / 0 |
| Rounds, median (range) | 3 (2–5) | 6 (2–8) | 3 (2–6) |
| Challenges raised per run | 7.4 | 15.1 | 7.9 |
| Questions escalated to humans per run | 2.7 | 2.7 | 2.3 |
| Proposer moves: defend / revise / concede | 37 / 62 / 1% | 15 / 84 / 1% | 22 / 77 / 1% |
| Defenses on merit (not "humans must decide"), of which accepted | 15 (4) | 7 (2) | 1 (0) |
| Revisions the Critic accepted | 84% | 76% | 84% |
| Repair requests per run | 2.1 | 5.1 | 2.7 |
| Cost per run | $0.009 | $0.016 | $0.009 |

**The Critic's word is not a stopping rule.** Under `naive`, 7 of 15 runs ended with a BLOCKER or MAJOR still
open. In three of them the Critic concluded in the same turn in which it maintained a MAJOR objection
([naive engagement-history/1](experiments/runs/naive/engagement-history/1/trace.md), round 5):

> Critic · confidence 70 · **CONCLUDE**
> - **C10** MAINTAIN: While quarterly audits are mentioned, the evidence does not specify how active monitoring and enforcement of role permissions will be managed.

A fourth concluded with a question the Proposer had sent to humans still open, and three ran into the round cap.
Because the record is built from the ledger, those questions still reach the decision document (4.0 open
questions per naive run, counting the ones left open), but under a header that says "consensus"
([naive right-contact/3](experiments/runs/naive/right-contact/3/decision.md) lists three MAJOR questions that block
the build). Under `gated` no run closed over an open BLOCKER or MAJOR. That is partly by construction, since only
the cap could end a gated run with one open and the cap never fired, and the gate itself never had to reject a
CONCLUDE: the shrinking budget and the two-strike rule emptied the ledger first. The Critic concluded twice, both
times with nothing open; the other 13 runs ended `converged`, with the Critic still saying CONTINUE. In these runs
the gate was a guarantee that never had to act; the naive runs show what it guards against.

**Convergence pressure is what ends a deliberation.** Without it the Critic keeps asking, mostly the same things
in new words. [naive right-contact/1](experiments/runs/naive/right-contact/1/trace.md) asked whether the feature
complies with data-protection law four times (C10, C11, C20, C22): the first two went to humans, the last two were
still open when the cap hit, with five other BLOCKERs, all but one raised in the final round.
[naive influence-ranking/3](experiments/runs/naive/influence-ranking/3/trace.md) maintained C16 three rounds
running while the Proposer rewrote S11 each time. Naive runs took twice as many rounds (median 6 against 3),
raised twice the challenges, grew the proposal by 77% (gated: 35%) and cost 1.9 times as much. Long runs also undo
their own decisions: in 44 naive settlements (in 9 of the 15 runs) the accepted wording was later edited away by
another answer (gated: 2, generic: 4), and the decision documents now flag each one.

**The opposed prompts change the Proposer, not the Critic.** The Critic accepted 84% of revisions under both
prompt sets. What changed is that the Proposer argued: 15 defenses on merit with the stakes and the burden of
proof, 1 without. With the generic prompts its only pushback was "a human must decide" (28 of 29 defenses), and in
4 of 15 runs it never defended at all. Arguing is not winning: the Critic accepted 4 of the 15, all on MINOR
challenges. The typical outcome is a disagreement about risk appetite (is user customization enough against alert
fatigue, in cold-relationship C5) that the two-strike rule hands to a named human owner instead of looping. The
stakes show in the Critic's signal too: it declared itself satisfied in 2 gated runs against 8 generic ones,
although both sets ended with nothing open.

**What reaches humans.** A gated decision document hands 2.7 questions per run to humans, each with an owner and
options: most often data-protection compliance, who owns ongoing processes (permissions, data quality, training),
and risk appetite.

Fifteen runs per configuration on one model: these are directions, not significance tests.

### How the prompts got here

Seven live batches, each kept in [`experiments/prompt-iterations/`](experiments/prompt-iterations/) and analyzed
in [`tasks/iteration-log.md`](tasks/iteration-log.md). The pattern: every failure was fixed by making the bad move
impossible to express or checkable by the ledger. Asking more nicely did nothing (v2 explained in prose when to
defend; 0 of 46 moves were defenses).

| Version | Change | What the next batch showed |
|---|---|---|
| v1 | Opposed roles, burden of proof on the Critic | 20 of 20 moves were revisions, mostly promises; two runs reached consensus in round 2 |
| v2 | An ACCEPT must quote the text that answers | No more round-2 rubber stamps, but 0 defenses in 46 moves, and invented teams accepted as answers |
| v3 | Grounds before the move; resolution tests must be questions with a concrete answer | 65% defenses, but 51 of 53 were "needs a human decision"; 3 ACCEPTs in 81 rulings |
| v4 | The Critic classifies, the ruling is derived | First balanced batch (30 revise, 15 defend), but the Proposer described edits it never wrote |
| v5 | The Proposer emits edits and the engine applies them | Claimed and actual changes match by construction; now the Critic accepted any related text (23 ACCEPT, 0 MAINTAIN) |
| v6 | Quote, then fact, then judge; assumptions can't settle a challenge | MAINTAIN is back, but decisions moved into assumptions and defenses could no longer win (2 in 44 moves) |
| v7 | A ledger rule for each v6 failure, and a path for a defense to win | 33 revise, 12 defend, 2–5 rounds, 2–4 open questions per document |
| v7.1 | Small fixes from the v7 batch; prompts frozen | The comparison batch above (gated: 77 revise, 46 defend) |

After the comparison batch, three things changed, and none of them alters a recorded deliberation: replaying all
45 runs through the final code reproduces every ledger, trace and model call byte for byte.
- Whether an open question blocks the build follows the Critic's severity instead of the Rapporteur's guess (it
  had marked 14 of 16 MINOR questions as blocking).
- The decision document shows each side's last word on every open question, the challenges declined on their
  merits, and any settlement a later edit undid.
- `converged` also requires every mandatory lens to have been examined. Every recorded run that converged
  already had each one covered by a challenge or a coverage note.

The decision documents in this repo were re-rendered from the recorded outputs accordingly.

### Limitations

- **The checks are lexical.** They catch a quote that isn't in the proposal, an assumption offered as an answer
  and listed weak phrases ("a process will be established", "authorized users" with no role named). They can't
  tell whether real text answers the question, or whether a team or policy it names exists. The Critic marked an
  answer unconfirmed 32 times in 192 gated rulings, but never one it also judged settled, so invented facts still
  get accepted ("managed by the data privacy officer" in right-contact S4; "data management processes currently
  in use" in influence-ranking C5). The Critic's `fact` often describes the quote ("Defines who can view sensitive
  information") instead of stating it, and a lens coverage note is taken at face value (right-contact's reads "No
  challenges were raised under this lens."); the ledger checks quotes, not paraphrases or notes.
- **Challenges still ask for processes.** About half the resolution tests (52 of 111 in gated runs) ask for a
  process, measure or safeguard, which the Critic's prompt tells it not to do, and such tests invite boilerplate.
- **Escalation is the easy exit.** 37% of gated challenges end with humans, and 31 of the Proposer's 46 defenses
  were "needs a human decision".
- **Paraphrased repeats get through.** The repeat check compares words in order, so the same question in new words
  is raised again. Under `gated` the budget bounds it, but some documents list one question twice (right-contact
  C4 and C7, auto-logging C2/C7 and C5/C8, influence-ranking C3 and C8).
- **Some product rules still go to humans.** The prompts say that what happens when someone changes role or leaves
  is for the agents to decide; they sometimes escalate it anyway (right-contact C4, C7).
- **Scope rarely shrinks.** 1% of moves were concessions, and under `gated` no out-of-scope list grew. No run asked
  whether a feature should exist, and core commitments can only be dropped by the stakeholder, so the influence
  ranking of named officials survives every run.
- **Contradictions the checks can't see.** In the published auto-logging run, S1 logs a meeting "whenever a meeting
  is scheduled or completed" while X2 rules out calendar integration; cold-relationship defines "cold" as 90 days
  (D1) but lets users choose 30–120 (S4) without calling 90 the default.
- **One model, small samples.** gpt-4o-mini in every role, 15 runs per configuration. `--critic-provider` runs the
  Critic on another model family; that was not measured.
- **Some runs are short.** 5 of the 15 gated runs ended after round 2, among them all three engagement-history runs.
