"""deliberate: run the Proposer/Critic deliberation from the command line.

  deliberate --request-id cold-relationship       requests by ID from config/requests.yaml
  deliberate --request "We need ..."              any request text (or --request-file, or $DELIBERATION_REQUEST)
  deliberate --all                                every request in config/requests.yaml
  deliberate --replay runs/<id>/events.jsonl      re-run a recorded deliberation with no API calls
"""

import argparse
import os
import re
import sys
from dataclasses import replace
from pathlib import Path

import yaml
from rich.console import Console

from .agents import ROOT
from .engine import deliberate, replay
from .llm import KEYS, default_provider, has_key, load_env, make_llm
from .render import console_round
from .termination import POLICIES


def parse_args(argv):
    ap = argparse.ArgumentParser(prog="deliberate", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    source = ap.add_mutually_exclusive_group()
    source.add_argument("--request", help="feature request text")
    source.add_argument("--request-file", type=Path, help="file containing the feature request")
    source.add_argument("--request-id", nargs="+", help="one or more request IDs from --requests")
    source.add_argument("--all", action="store_true", help="run every request in --requests")
    source.add_argument("--replay", type=Path, metavar="EVENTS", help="re-run a recorded events.jsonl without API calls")
    ap.add_argument("--policy", choices=sorted(POLICIES), default="gated", help="termination policy (default: gated)")
    ap.add_argument("--provider", choices=["anthropic", "openai"], help="default: whichever API key is set (Anthropic first)")
    ap.add_argument("--model", help="model for every role (default: the provider's small model)")
    ap.add_argument("--critic-provider", choices=["anthropic", "openai"], help="run the Critic on a different provider")
    ap.add_argument("--critic-model", help="run the Critic on a different model")
    ap.add_argument("--max-rounds", type=int, help="override the policy's backstop")
    ap.add_argument("--context", type=Path, default=ROOT / "config/system_context.md")
    ap.add_argument("--requests", type=Path, default=ROOT / "config/requests.yaml")
    ap.add_argument("--prompts", type=Path, action="append", default=[], help="prompt directory that overrides prompts/")
    ap.add_argument("--out", type=Path, default=ROOT / "runs", help="where run folders are written (default: runs/)")
    ap.add_argument("--quiet", action="store_true", help="only print the final summary")
    return ap.parse_args(argv)


def resolve_requests(args) -> list[tuple[str, str]]:
    catalog = {r["id"]: r["text"] for r in yaml.safe_load(args.requests.read_text())["requests"]}
    if args.all:
        return list(catalog.items())
    if args.request_id:
        if unknown := [r for r in args.request_id if r not in catalog]:
            sys.exit(f"Unknown request id(s) {', '.join(unknown)}. Known: {', '.join(catalog)}")
        return [(r, catalog[r]) for r in args.request_id]
    text = args.request or (args.request_file.read_text() if args.request_file else os.environ.get("DELIBERATION_REQUEST"))
    if not text or not text.strip():
        sys.exit("Give a request: --request, --request-file, --request-id, --all, or $DELIBERATION_REQUEST.")
    return [(re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48], text.strip())]


def main(argv=None) -> None:
    load_env(ROOT / ".env")
    args = parse_args(argv)
    console = Console()
    show = None if args.quiet else (lambda ledger, rnd: console_round(console, ledger, rnd))

    if args.replay:
        run = replay(args.replay, on_round=show)
        run.save(args.replay.parent / "replay")  # beside the original, so the two can be diffed
        runs = [(args.replay.parent / "replay", run)]
    else:
        args.provider = args.provider or default_provider()
        if not args.provider:
            sys.exit("No API key found: set ANTHROPIC_API_KEY or OPENAI_API_KEY (or put it in .env), "
                     "or view a recorded run with --replay.")
        critic_provider = args.critic_provider or args.provider
        for provider in {args.provider, critic_provider}:
            if not has_key(provider):
                sys.exit(f"No API key for {provider}: set {KEYS[provider]} (or put it in .env).")
        llms = {"proposer": make_llm(args.provider, args.model), "summarizer": make_llm(args.provider, args.model),
                "critic": make_llm(critic_provider, args.critic_model or (args.model if critic_provider == args.provider else None))}
        policy = POLICIES[args.policy] if args.max_rounds is None else replace(POLICIES[args.policy], max_rounds=args.max_rounds)
        context, runs = args.context.read_text(), []
        for request_id, text in resolve_requests(args):
            console.print(f"\n[bold]{request_id}[/] [dim]({policy.name} policy)[/]\n> {text}")
            run = deliberate(text, context, llms, policy, request_id=request_id, prompt_dirs=tuple(args.prompts), on_round=show)
            runs.append((args.out / request_id, run))
            run.save(args.out / request_id)

    for folder, run in runs:
        m = run.meta
        cost = f" · ${m['cost_usd']:.3f}" if m["cost_usd"] is not None else ""
        console.print(f"[bold green]✓[/] {m['request_id']}: {m['termination']} after {m['rounds']} rounds · "
                      f"{m['llm_calls']} calls{cost} → {folder}/decision.md")


if __name__ == "__main__":
    main()
