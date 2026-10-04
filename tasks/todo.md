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

Environment (updated 2026-10-04 06:55):
- Live runs use OpenAI gpt-4o-mini, run by Domi in his own terminal (his choice; no Anthropic key).
- api.openai.com is blocked both in the cloud workspace and in the desktop VM, so Claude can't run live calls.
- Project lives at ~/code/assessments/deliberation-engine on Domi's Mac (new folder; government_crm_deliberation untouched).
  Source of truth stays in the cloud repo; changed files are synced over with device_commit_files, and run outputs
  are read back from runs/ in that folder.
- Synced copy verified: 18/18 tests pass on the Mac workspace.

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
- [x] First live runs on the 3 brief inputs (Domi runs; gpt-4o-mini); iterate prompts; log every change in `tasks/iteration-log.md`
  (v1–v4 done; evidence in `experiments/prompt-iterations/`)

## Prompt iteration v5 (2026-10-04)
- [x] Engine-applied edits: `ProposerOpening` in round 1, `ProposerTurn` with per-answer `edits` after; ledger vets every edit
- [x] Uniform `{id, text}` items for all six sections
- [x] Critic pre-mortem in round 1, shown again later; clearer concluding rule (escalated = closed for the deliberation)
- [x] Tests for every edit rule; strict-schema check for both providers; replay round-trip; rendered trace + decision read
- [x] Independent review of the diff; fixed: new-item ID clashes, coerced revisions that changed nothing, next unused IDs
      shown to the Proposer, section emptiness checked on the result, dropped assumptions rendered as dropped
- [x] v5 live batch run and analysed (`tasks/iteration-log.md`): edits fixed; the Critic became too lenient (0 MAINTAIN)

## Prompt iteration v6 (2026-10-04)
- [x] Critic verdict in steps: evidence → fact → answered (test + failure scenario) → unconfirmed → needs humans;
      ruling derived, routed by the question (humans vs. ours); ACCEPT needs a named fact and non-assumption evidence
- [x] Order-aware evidence matching, best match wins (all 44 accepted v4–v5 quotes still match)
- [x] Round 1 without the "between 3 and" anchor; gaps list not re-shown; pre-mortem about what the feature creates
- [x] Edits: sequential for one item, distinct new IDs, no remove-and-rewrite, concession/revision labels checked,
      repeated "S3:" stripped
- [x] Independent review of the diff; all findings fixed or deliberately kept (revert check), fuzzed coercion clean
- [x] v6 live batch run and analysed: assumptions as answers, vague accepts, same-turn repeats, no defenses

## Prompt iteration v7 (2026-10-04)
- [x] Ledger rules from the v6 batch: assumption-only revisions, weak-phrase evidence, repeated questions,
      `settled` with a defense path, NEEDS_HUMAN answers never accepted, round 1 covers its gaps
- [x] Replayed the 43 v5–v6 ACCEPTs through the new checks (18/28 vague refused, 1/15 concrete)
- [x] Independent review; fixed ordering, routing, weak-phrase precision and trim-resistance; fuzzed coercion clean
- [x] v7 live batch run and analysed: most balanced so far; one weak-phrase false positive, re-raised escalations
- [x] v7.1: role-aware weak phrases, follow-up targets, question-form tests, no re-asking escalated questions
- [x] Prompts frozen. Comparison batch (Domi): `uv run python experiments/ablate.py run --runs 3`

## Day 2 — evidence and polish
- [x] Inputs A + B
- [x] Generic-prompt variant for the prompt comparison
- [x] `experiments/ablate.py` — 5 inputs × 3 runs per arm → metrics table
- [x] Run comparisons: policy (naive vs gated), prompts (generic vs opposed): 45 runs, `experiments/results.md`
- [x] Final traces for all 5 inputs under `runs/` (one gated run each, picked by a read-through audit)
- [x] README (setup, run, replay, results table, traces, iteration story, limitations)
- [x] DECISIONS.md outline + data pack (Domi writes the final text; pack delivered outside the repo)
- [x] Fresh-agent review against the brief's rubric; fix findings (see the iteration log)
- [x] Clean-checkout check: `uv sync` → tests → replay (live run: Domi, after the sync)

## Comparison batch and evidence (2026-10-04)
- [x] Imported the 45 runs from the Mac (md5 of all 225 files identical); `ablate.py report` reproduces Domi's table
- [x] Deep-dive: naive concludes over its own MAINTAINs (3 runs) and re-asks escalated questions; gated's gate never had
      to fire (convergence pressure emptied the ledger); opposed prompts change the Proposer (15 vs 1 merit defenses),
      not the Critic (84% of revisions accepted in both)
- [x] Audited all 15 gated decision documents; red flags recorded as README limitations
- [x] Fix found in the audit: "blocks the build" now follows the Critic's severity (the Rapporteur had marked 14 of 16
      MINOR questions as blocking); field removed from the Rapporteur's schema and prompt; counts line in the header
- [x] Replayed all 45 runs through the new code: ledgers, traces, events and meta byte-identical; decision documents
      changed only as intended; the five published runs replay identically through the CLI
- [x] Fixed `ablate.py`'s claim that each configuration differs in one thing (naive swaps the whole policy)

## Review
- Delivered: the 45-run comparison analysed (`experiments/results.md`), one published trace per request (`runs/`),
  the README's evidence section with limitations, and a DECISIONS.md data pack for Domi (kept outside the repo).
- Independent review (rubric grader and README fact-check) led to: the lens check on `converged`, every instruction
  in `prompts/`, a decision record that shows both sides' last word, declined challenges and undone settlements,
  twelve README corrections, and 54 tests. Replaying all 45 recorded runs through the final code reproduces every
  ledger, trace and model call.
- Open: DECISIONS.md (Domi writes it), one live smoke run of the final code (Domi), and the sync to the Mac.
