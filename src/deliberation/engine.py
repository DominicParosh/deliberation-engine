"""The round loop. Deliberately small: the rules live in ledger.py and termination.py,
the wording in prompts/, and everything human-readable in render.py."""

import json
import time
from collections.abc import Callable
from dataclasses import dataclass, replace
from pathlib import Path

from . import render
from .agents import Agents
from .ledger import Ledger
from .llm import LLM, ScriptedLLM, cost
from .schemas import Synthesis
from .termination import POLICIES, Policy


@dataclass
class Run:
    ledger: Ledger
    synthesis: Synthesis
    meta: dict
    events: list[dict]

    def save(self, out_dir: Path) -> None:
        out_dir.mkdir(parents=True, exist_ok=True)
        doc = render.decision(self)
        (out_dir / "events.jsonl").write_text("".join(json.dumps(e) + "\n" for e in self.events))
        (out_dir / "ledger.json").write_text(self.ledger.model_dump_json(indent=2))
        (out_dir / "decision.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False))
        (out_dir / "decision.md").write_text(render.decision_md(doc))
        (out_dir / "trace.md").write_text(render.trace_md(self))


def deliberate(request: str, context: str, llms: dict[str, LLM], policy: Policy, *, request_id: str = "adhoc",
               prompt_dirs: tuple[Path, ...] = (), on_round: Callable[[Ledger, int], None] | None = None) -> Run:
    events = [{"kind": "run", "request_id": request_id, "request": request, "context": context, "policy": policy.name,
               "max_rounds": policy.max_rounds, "prompt_dirs": [str(d) for d in prompt_dirs]}]
    agents = Agents(context, llms, events.append, list(prompt_dirs))
    ledger, feedback, started = Ledger(request=request), "", time.time()

    for rnd in range(1, policy.max_rounds + 1):
        proposal = agents.propose(ledger, rnd)
        ledger.apply_proposer(rnd, proposal)
        critique = agents.critique(ledger, rnd, policy, feedback)
        ledger.apply_critic(rnd, critique, policy.strike_limit)
        decision = policy.decide(ledger, rnd, critique)
        ledger.record(rnd, proposal, critique, decision.reason, decision.feedback)
        if on_round:
            on_round(ledger, rnd)
        if decision.stop:
            break
        feedback = decision.feedback

    ledger.close(decision.reason)
    synthesis = agents.synthesize(ledger)
    calls = [e for e in events if e["kind"] == "llm"]
    costs = [cost(e["model"], e["input_tokens"], e["output_tokens"]) for e in calls]
    meta = {"request_id": request_id, "policy": policy.name, "rounds": len(ledger.rounds), "termination": ledger.termination,
            "models": {role: llm.model for role, llm in llms.items()}, "llm_calls": len(calls),
            "repairs": sum(e["kind"] == "violation" for e in events),
            "input_tokens": sum(e["input_tokens"] for e in calls), "output_tokens": sum(e["output_tokens"] for e in calls),
            "cost_usd": round(sum(costs), 4) if None not in costs else None,
            "seconds": round(time.time() - started, 1), "warnings": ledger.warnings}
    return Run(ledger, synthesis, meta, events)


def replay(events_path: Path, on_round=None) -> Run:
    """Re-run a recorded deliberation from its events.jsonl, with no API calls."""
    events = [json.loads(line) for line in events_path.read_text().splitlines() if line.strip()]
    head = events[0]
    llms = {role: ScriptedLLM([e for e in events if e["kind"] == "llm" and e["role"] == role])
            for role in ("proposer", "critic", "summarizer")}
    policy = replace(POLICIES[head["policy"]], max_rounds=head["max_rounds"])
    run = deliberate(head["request"], head["context"], llms, policy, request_id=head["request_id"],
                     prompt_dirs=tuple(Path(d) for d in head["prompt_dirs"]), on_round=on_round)
    run.meta["replayed_from"] = str(events_path)
    return run
