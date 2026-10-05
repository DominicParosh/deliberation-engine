# Prompts

Every instruction the agents read lives in this folder, plus the field descriptions in
`src/deliberation/schemas.py`, which structured outputs send to the model as part of the JSON schema, and the
repair sentences in `src/deliberation/ledger.py` described below.

| File | Sent as | Placeholders filled by code |
|---|---|---|
| `proposer.system.md` | Proposer system prompt | `{{system_context}}` from `config/system_context.md` |
| `proposer.turn.md` | Proposer user turn, every round | `{{request}}`, `{{round}}`, `{{state}}`, `{{task}}` |
| `proposer.task.round1.md`, `proposer.task.md` | The `{{task}}` in round 1 and in later rounds | none |
| `critic.system.md` | Critic system prompt | `{{system_context}}` |
| `critic.turn.md` | Critic user turn, every round | `{{request}}`, `{{round}}`, `{{state}}`, `{{task}}` |
| `critic.task.round1.md`, `critic.task.md` | The `{{task}}` in round 1 and in later rounds | `{{budget}}` (new challenges allowed this round), `{{uncovered}}` (mandatory lenses not yet examined) |
| `summarizer.system.md` | Rapporteur system prompt | `{{system_context}}` |
| `summarizer.turn.md` | Rapporteur user turn, once | `{{request}}`, `{{record}}` |
| `repair.md` | Follow-up when a reply breaks a rule | `{{problems}}` |

Two kinds of text are written by code, because each depends on the ledger's state: the `{{problems}}` in a
repair, one sentence per rule the reply broke saying how to fix it (`src/deliberation/ledger.py`), and the
moderator's note to the Critic when the termination policy keeps a deliberation going
(`src/deliberation/termination.py`).

Round 1 and later rounds use different output schemas. In round 1 the Proposer returns the full proposal and the
Critic adds a pre-mortem and the request's open questions (`ProposerOpening`, `CriticOpening`). From round 2 the
Proposer returns answers with edits, which the engine applies, and the Critic returns rulings and a signal
(`ProposerTurn`, `CriticTurn`).

`{{state}}` is rendered from the ledger by the view functions at the bottom of `src/deliberation/agents.py`:
the current proposal, the open challenges with their history, and the settled ones. Each agent sees the
original request and the current ledger every turn, not the whole transcript, which keeps them anchored to
the task and keeps the prompt size flat as rounds go by.

A directory passed with `--prompts` overrides files here by name. `experiments/prompts-generic/` uses that
to swap in neutral role prompts for the comparison in `experiments/results.md`.
