"""When does deliberation end? Two policies, both pure functions of (ledger, round, critic turn).

GATED (default)  The Critic proposes, the ledger disposes. CONCLUDE is accepted only when
                 the evidence agrees with it. Convergence pressure (shrinking challenge budget,
                 two-strike escalation) bounds every issue's lifetime, so deliberation ends by
                 construction; the round cap is a circuit breaker that should never fire.
NAIVE            The pattern most frameworks ship: the Critic's word plus a round cap. Kept
                 only as the baseline for experiments/ablate.py.
"""

from collections.abc import Callable
from dataclasses import dataclass

from .ledger import Ledger
from .schemas import BLOCKING, MANDATORY_LENSES, CriticOpening, CriticTurn


@dataclass(frozen=True)
class Decision:
    stop: bool
    reason: str = ""    # consensus | converged | cap
    feedback: str = ""  # shown to the Critic next round when its CONCLUDE was rejected


def gated(policy: "Policy", ledger: Ledger, rnd: int, turn: CriticOpening | CriticTurn) -> Decision:
    if rnd < policy.min_rounds:  # round 1's schema has no signal at all; this is belt and braces
        return Decision(False)
    signal = getattr(turn, "signal", "CONTINUE")
    if signal == "CONCLUDE":
        problems = []
        if blocking := [i.id for i in ledger.open_issues() if i.severity in BLOCKING]:
            problems.append(f"still open at BLOCKER/MAJOR: {', '.join(blocking)}")
        if missing := [lens for lens in MANDATORY_LENSES if lens not in ledger.lenses_examined(turn.lens_coverage)]:
            problems.append(f"no challenge raised and no coverage note for: {', '.join(missing)}")
        if not problems:
            return Decision(True, "consensus")
        feedback = "Your CONCLUDE was rejected: " + "; ".join(problems) + "."
        return Decision(True, "cap", feedback) if rnd >= policy.max_rounds else Decision(False, feedback=feedback)
    if not ledger.open_issues():  # CONTINUE with nothing open and nothing new: nothing left to deliberate
        return Decision(True, "converged")
    return Decision(True, "cap") if rnd >= policy.max_rounds else Decision(False)


def naive(policy: "Policy", ledger: Ledger, rnd: int, turn: CriticOpening | CriticTurn) -> Decision:
    if rnd >= policy.min_rounds and getattr(turn, "signal", "CONTINUE") == "CONCLUDE":
        return Decision(True, "consensus")
    return Decision(True, "cap") if rnd >= policy.max_rounds else Decision(False)


@dataclass(frozen=True)
class Policy:
    name: str
    rule: Callable[["Policy", Ledger, int, CriticOpening | CriticTurn], Decision]
    budgets: tuple[int, ...]   # new-challenge budget per round; the last value repeats
    strike_limit: int | None   # MAINTAIN rulings before an issue is escalated to humans; None = never
    min_rounds: int = 2        # the brief: no satisfaction in round 1
    max_rounds: int = 8        # backstop

    def budget(self, rnd: int) -> int:
        return self.budgets[min(rnd, len(self.budgets)) - 1]

    def decide(self, ledger: Ledger, rnd: int, turn: CriticOpening | CriticTurn) -> Decision:
        return self.rule(self, ledger, rnd, turn)


GATED = Policy("gated", gated, budgets=(6, 3, 2, 1, 0), strike_limit=2)
NAIVE = Policy("naive", naive, budgets=(6,), strike_limit=None)
POLICIES = {p.name: p for p in (GATED, NAIVE)}
