# Prompts

Every word the agents read lives in this folder, plus the field descriptions in
`src/deliberation/schemas.py`, which structured outputs send to the model as part of the JSON schema.

| File | Sent as | Placeholders filled by code |
|---|---|---|
| `proposer.system.md` | Proposer system prompt | `{{system_context}}` from `config/system_context.md` |
| `proposer.turn.md` | Proposer user turn, every round | `{{request}}`, `{{round}}`, `{{state}}`, `{{task}}` |
| `critic.system.md` | Critic system prompt | `{{system_context}}` |
| `critic.turn.md` | Critic user turn, every round | `{{request}}`, `{{round}}`, `{{state}}`, `{{task}}` |
| `summarizer.system.md` | Rapporteur system prompt | `{{system_context}}` |
| `summarizer.turn.md` | Rapporteur user turn, once | `{{request}}`, `{{record}}` |
| `repair.md` | Follow-up when a reply breaks a rule | `{{problems}}` |

`{{state}}` is rendered from the ledger by the view functions at the bottom of `src/deliberation/agents.py`:
the current proposal, the open challenges with their history, and the settled ones. Each agent sees the
original request and the current ledger every turn, not the whole transcript, which keeps them anchored to
the task and keeps the prompt size flat as rounds go by.

A directory passed with `--prompts` overrides files here by name. `experiments/prompts-generic/` uses that
to swap in neutral role prompts for the comparison in `experiments/results.md`.
