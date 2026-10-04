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
export ANTHROPIC_API_KEY=sk-ant-...

uv run deliberate --request-id cold-relationship     # one request from config/requests.yaml
uv run deliberate --all                              # all five
uv run deliberate --request "Executives want a dashboard of relationship health."
```

No API key? Every committed run can be replayed from its recorded model outputs, with no API calls:

```bash
uv run deliberate --replay runs/cold-relationship/events.jsonl
```

Tests need no key either: `uv run pytest`.

### Options

| Flag | Default | |
|---|---|---|
| `--request` / `--request-file` / `--request-id` / `--all` | `$DELIBERATION_REQUEST` | Where the request comes from |
| `--policy` | `gated` | `naive` runs the baseline termination policy (Critic's word + round cap) |
| `--provider`, `--model` | `anthropic`, `claude-haiku-4-5-20251001` | `--provider openai` uses `gpt-4o-mini` and `OPENAI_API_KEY` |
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

- The Proposer answers every open challenge with **DEFEND**, **REVISE** or **CONCEDE**, and returns its
  full proposal: core commitments (V), in-scope (S), out-of-scope (X), assumptions (A), definitions of every
  vague term (D) and success criteria (K), all with stable IDs.
- The Critic rules on every answered challenge (**ACCEPT**, **MAINTAIN**, **ESCALATE**), then may raise new
  ones. A challenge must name the IDs it targets, a lens, a severity, a concrete failure scenario and a
  resolution test. Generic pushback cannot be expressed in the schema.
- An illegal move (a missing ruling, an over-budget challenge, a dropped core commitment) gets one repair
  request; if that also fails, the orchestrator coerces it safely and records a warning.

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
