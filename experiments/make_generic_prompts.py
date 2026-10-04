"""Derive the `generic` prompt variant from prompts/: same rules and mechanics, but without the role
stakes and the burden-of-proof clauses. Rerun after editing prompts/ so the comparison stays controlled.

  uv run python experiments/make_generic_prompts.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/prompts-generic"


def between(text: str, start: str, end: str, replacement: str) -> str:
    i, j = text.index(start), text.index(end)
    return text[:i] + replacement + text[j:]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    proposer = (ROOT / "prompts/proposer.system.md").read_text()
    proposer = between(proposer, "# Your role", "# The system", "# Your role\nYou turn feature requests into clear proposals. "
                       "Work with the **Critic**, who reviews your proposal, to produce the best possible specification.\n\n")
    proposer = between(proposer, "**The burden of proof is on the Critic.**", "# IDs",
                       "If a challenge attacks a core commitment (V), defend it or revise how it is delivered; never concede it away.\n\n")
    critic = (ROOT / "prompts/critic.system.md").read_text()
    critic = between(critic, "# Your role", "# The system", "# Your role\nYou review proposals written by the **Proposer** "
                     "and point out problems so the proposal can be improved.\n\n")
    critic = between(critic, "A defense can be right", "Don't re-raise", "")
    (OUT / "proposer.system.md").write_text(proposer)
    (OUT / "critic.system.md").write_text(critic)
    print(f"wrote {OUT.relative_to(ROOT)}/proposer.system.md and critic.system.md")


if __name__ == "__main__":
    main()
