# Deliberation Engine — build plan

Strategy: **Option 3 (Ledger + Evidence) + OpenAI adapter**, chosen 2026-10-04.

Locked decisions:
- Issue ledger is the single source of truth; agents emit typed moves the orchestrator validates.
- Termination: ledger-gated Critic signal (round ≥ 2, no open BLOCKER/MAJOR, mandatory lenses covered);
  shrinking challenge budget 6→3→2→1→0; two-strike escalation; cap 8 as backstop only.
- Naive policy (Critic APPROVED + cap) ships beside it for the comparison.
- Prompts: opposed incentives (product owner vs architect/data-protection), DEFEND/REVISE/CONCEDE with burden of proof,
  core commitments, term binding, schema-enforced specific challenges, re-anchoring each turn.
- Claude Haiku 4.5 by default via structured outputs; OpenAI adapter; scripted/replay client for tests and `--replay`.
- Inputs: 3 from the brief + A (auto-logging) + B (influence ranking).
- Bonuses: summarizer as neutral clerk (ID-validated), Disagreement Index + self-reported confidence with overconfidence flag.

Environment constraints (found while scaffolding):
- No API key in this workspace yet → live runs blocked until one is provided.
- api.openai.com is blocked by the workspace egress policy → OpenAI adapter is tested against a fake client here;
  one live check has to run on Domi's machine.
- ANTHROPIC_BASE_URL is set by the workspace harness → run the project with `env -u ANTHROPIC_BASE_URL`.

## Day 1 — engine
- [x] Scaffold (uv project; anthropic, openai, pydantic, rich, pyyaml; pytest)
- [x] `schemas.py` — agent output models (all fields required; short `rationale` fields)
- [x] `ledger.py` — proposal versions, issues, strikes, Disagreement Index
- [x] `termination.py` — `gated` and `naive` policies as pure functions
- [x] `llm.py` — Anthropic + OpenAI structured-output clients, scripted/replay client
- [x] `agents.py` — prompt loading, turn rendering, validation + one repair retry
- [x] `engine.py` — round loop + events.jsonl
- [x] `render.py` — console, trace.md, decision.json, decision.md
- [x] `cli.py` — `--request` / `--request-id` / `--request-file` / env var / `--all` / `--replay` / `--policy` / `--provider`
- [x] Tests — every termination exit path with scripted agents (no API)
- [x] Prompts v1 — proposer, critic, summarizer (+ turn templates)
- [ ] First live runs on the 3 brief inputs; iterate prompts; log every change in `tasks/iteration-log.md`

## Day 2 — evidence and polish
- [x] Inputs A + B
- [x] Generic-prompt variant for the prompt comparison
- [x] `experiments/ablate.py` — 5 inputs × 3 runs per arm → metrics table
- [ ] Run comparisons: policy (naive vs gated), prompts (generic vs opposed)
- [ ] Final traces for all 5 inputs under `runs/`
- [ ] README (setup, run, replay, results table)
- [ ] DECISIONS.md outline + data pack (Domi writes the final text)
- [ ] Fresh-agent review against the brief's rubric; fix findings
- [ ] Clean-checkout check: `uv sync` → tests → one live run → replay

## Review
_(filled in at the end)_
