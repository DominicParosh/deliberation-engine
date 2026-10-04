# Deliberation Engine

Two agents deliberate over a vague feature request for a Government CRM and produce a decision
document: what will be built, what won't, what was assumed, and what humans still have to decide.

- The **Proposer** is the product owner. It represents the stakeholder and is judged on delivered value.
- The **Critic** is the principal architect who also owns data-protection sign-off. It is judged on what breaks.
- A **Rapporteur** writes the prose of the decision record afterwards. It cannot change any decision.

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

Each run writes `runs/<request-id>/`:

| File | What it is |
|---|---|
| `decision.md` | The decision document (rendered from `decision.json`) |
| `decision.json` | The same, machine-readable |
| `trace.md` | Every round: proposals, responses, rulings, new challenges, ledger state, termination decision |
| `ledger.json` | The full deliberation state |
| `events.jsonl` | Every model call's raw output, which is what `--replay` plays back |

The console prints the same round-by-round view as `trace.md` while the deliberation runs.

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
  they commit to, and judges whether that answers the test and stops its failure scenario. The ruling follows:
  answered with nothing unconfirmed → **ACCEPT** (the ledger checks the quote is really there and a fact was
  named); otherwise a test that needs authority neither agent has (law, policy, budgets, existing teams) →
  **ESCALATE** to humans, and any other → **MAINTAIN**, back to the Proposer. An answer that rests on a team,
  policy or system nobody has confirmed is never accepted.
- An illegal move (a missing answer or ruling, an over-budget challenge, a defense that edits, a revision
  that doesn't, a concession that drops nothing, an attempt to remove a core commitment, an ACCEPT without a
  concrete fact or real evidence) gets one repair request; if that also fails, the orchestrator coerces it
  safely and records a warning.

**Termination: the Critic proposes, the ledger disposes.** The Critic signals CONCLUDE or CONTINUE, but
CONCLUDE is accepted only when the evidence agrees:

1. it is round 2 or later (round 1's schema has no signal field at all),
2. no BLOCKER or MAJOR issue is open, and
3. each mandatory lens (confidentiality, definitions, ownership) has a challenge or a coverage note.

A rejected CONCLUDE is fed back to the Critic. Two mechanisms make deliberation end by construction:
the Critic's new-challenge budget shrinks each round (6 → 3 → 2 → 1 → 0), and an issue maintained twice
is escalated to humans as an open question instead of looping. So every issue lives at most two rounds
after it is raised, and the round cap (8) is a circuit breaker that should never fire. Each run records
its exit: `consensus`, `converged` (nothing left open), or `cap`.

The policy is ~40 lines in [`src/deliberation/termination.py`](src/deliberation/termination.py); every
exit path is covered in [`tests/test_termination.py`](tests/test_termination.py).

**The decision document is built from the ledger, not from a summary.** Scope, statuses, assumptions and
open questions come straight from the ledger. The Rapporteur only writes prose around them, and every ID
it cites is checked. It also reports a **disagreement index** per round (severity-weighted share of
issues not settled by agreement), each agent's final confidence and remaining worry, and a flag when an
agent claims high confidence while a blocker is unsettled.

## Where things are

| Path | |
|---|---|
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

_Filled in from the experiment runs._
