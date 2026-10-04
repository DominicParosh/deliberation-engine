"""Everything a person or a model reads as text. One Markdown renderer serves the agents'
prompts, the live console (through rich.markdown) and trace.md, so what the agents saw, what
was printed and what was saved cannot drift apart. The decision document's structure comes
from the ledger; the summarizer only supplies the prose around it."""

from rich.console import Console
from rich.markdown import Markdown

from .ledger import Issue, Ledger
from .schemas import WEIGHT, Proposal


def proposal_md(p: Proposal) -> str:
    out = [f"_{p.summary}_"]
    for title, items in (("Core commitments", p.core_commitments), ("In scope", p.in_scope), ("Out of scope", p.out_of_scope)):
        out += ["", f"**{title}**"] + [f"- {i.id}: {i.text}" for i in items]
    out += ["", "**Assumptions**"] + [f"- {a.id}: {a.text} _(implicit because: {a.why_implicit})_" for a in p.assumptions]
    out += ["", "**Definitions**"] + [f'- {d.id}: "{d.term}" = {d.definition}' for d in p.definitions]
    out += ["", "**Success criteria**"] + [f"- {k.id}: {k.metric}; target {k.target}; measured by {k.measurement}"
                                           for k in p.success_criteria]
    return "\n".join(out)


def issue_md(i: Issue, history: bool = True) -> str:
    out = [f"**{i.id}** · {i.severity} · {i.lens} · targets {', '.join(i.targets)}",
           f"- Challenge: {i.challenge}", f"- Failure scenario: {i.failure_scenario}", f"- Resolution test: {i.resolution_test}"]
    if history:
        out += [f"- R{e.round} {e.actor} {e.move}: {e.text}" for e in i.history if e.move != "RAISE"]
        if i.strikes and i.status == "OPEN":
            out.append(f"- Maintained {i.strikes} time(s) so far; a second MAINTAIN hands it to humans.")
    return "\n".join(out)


def _moves(ledger: Ledger, rnd: int, *actors: str) -> list[str]:
    return [f"- **{i.id}** {e.move}: {e.text}" for i in ledger.issues.values() for e in i.history
            if e.round == rnd and e.actor in actors and e.move != "RAISE"]


def round_md(ledger: Ledger, rnd: int) -> str:
    s, p = ledger.rounds[rnd - 1], ledger.proposals[rnd - 1]
    out = [f"## Round {rnd}", "", f"### Proposer · confidence {s.proposer_confidence}", ""]
    if rnd == 1:
        out.append(proposal_md(p))
    else:
        changes, items = ledger.changes(rnd - 1), p.items()
        out += _moves(ledger, rnd, "proposer")
        out += ["", "Proposal changes: " + ("; ".join(f"{k} {', '.join(v)}" for k, v in changes.items() if v) or "none")]
        out += [f"- {k} now reads: {items[k]}" for k in changes.get("added", []) + changes.get("edited", [])]
    signal = f" · {s.signal}" if s.signal != "-" else ""
    out += ["", f"Biggest worry: {s.proposer_worry}", "", f"### Critic · confidence {s.critic_confidence}{signal}", ""]
    if rnd == 1 and ledger.gaps:
        out += ["Questions the request leaves open:", *[f"- {g}" for g in ledger.gaps], ""]
    if rulings := _moves(ledger, rnd, "critic", "orchestrator"):
        out += ["Rulings:", *rulings, ""]
    if new := [i for i in ledger.issues.values() if i.round_raised == rnd]:
        out += ["New challenges:", ""] + [issue_md(i, history=False) + "\n" for i in new]
    out += [f"Biggest worry: {s.critic_worry}", "",
            f"**Ledger:** raised {s.raised} · open {s.open} · resolved {s.resolved} · escalated {s.escalated} · "
            f"disagreement {s.disagreement:.2f} → **{s.decision}**"]
    if s.feedback:
        out += ["", f"> Moderator: {s.feedback}"]
    return "\n".join(out) + "\n"


def console_round(console: Console, ledger: Ledger, rnd: int) -> None:
    console.print(Markdown(round_md(ledger, rnd)))


def trace_md(run) -> str:
    L, m = run.ledger, run.meta
    out = [f"# Deliberation trace: {m['request_id']}", "", f"> {L.request}", "",
           f"Policy `{m['policy']}` · models: {', '.join(f'{r} {v}' for r, v in m['models'].items())} · "
           f"ended **{m['termination']}** after {m['rounds']} rounds · {m['llm_calls']} model calls ({m['repairs']} repairs)", ""]
    out += [round_md(L, s.round) for s in L.rounds]
    out += ["## Final proposal", "", proposal_md(L.proposal), ""]
    if L.warnings:
        out += ["## Orchestrator warnings", ""] + [f"- {w}" for w in L.warnings] + [""]
    return "\n".join(out)


# ------------------------------------------------------------------------ decision document


def decision(run) -> dict:
    L, S, final = run.ledger, run.synthesis, run.ledger.proposal
    notes = {n.id: n for n in S.item_notes}

    def item(i) -> dict:
        n = notes.get(i.id)
        return {"id": i.id, "text": i.text, "note": n.note if n else "", "refs": n.refs if n else []}

    def challenges(item_id: str) -> list[dict]:
        return [{"id": i.id, "outcome": i.outcome} for i in L.issues.values() if item_id in i.targets]

    assumptions = [{**item(a), "why_implicit": a.why_implicit, "challenges": challenges(a.id)} for a in final.assumptions]
    assumptions += [{"id": k, "text": text, "note": "Dropped during deliberation.", "refs": [], "why_implicit": "",
                     "challenges": challenges(k)} for k, text in L.dropped().items() if k.startswith("A")]
    questions = sorted(
        ({**q.model_dump(), "severity": L.issues[q.issue_id].severity, "status": L.issues[q.issue_id].status}
         for q in S.open_questions if q.issue_id in L.issues),
        key=lambda q: (not q["blocks_build"], -WEIGHT[q["severity"]]))
    last = L.rounds[-1]
    unsettled = [i.id for i in L.issues.values() if i.severity == "BLOCKER" and i.status in ("ESCALATED", "UNRESOLVED")]
    flags = [f"{role.title()} reported {conf}/100 confidence while blocker(s) {', '.join(unsettled)} remain unsettled."
             for role, conf in (("proposer", last.proposer_confidence), ("critic", last.critic_confidence))
             if conf >= 80 and unsettled]
    return {
        "request": L.request,
        "meta": run.meta,
        "executive_summary": S.executive_summary,
        "core_commitments": [item(v) for v in final.core_commitments],
        "in_scope": [item(s) for s in final.in_scope],
        "out_of_scope": [item(x) for x in final.out_of_scope],
        "rejected": [r.model_dump() for r in S.rejected],
        "assumptions": assumptions,
        "definitions": [{**d.model_dump(), "note": notes[d.id].note if d.id in notes else ""} for d in final.definitions],
        "success_criteria": [{**k.model_dump(), "note": notes[k.id].note if k.id in notes else ""} for k in final.success_criteria],
        "open_questions": questions,
        "tension": {
            "summary": S.tension_summary,
            "by_round": [s.model_dump(exclude={"proposer_worry", "critic_worry"}) for s in L.rounds],
            "final_positions": {"proposer": {"confidence": last.proposer_confidence, "worry": last.proposer_worry},
                                "critic": {"confidence": last.critic_confidence, "worry": last.critic_worry}},
            "flags": flags,
        },
        "issues": [{**i.model_dump(), "outcome": i.outcome} for i in L.issues.values()],
    }


def decision_md(doc: dict) -> str:
    m, t = doc["meta"], doc["tension"]
    cost = f" · ${m['cost_usd']:.3f}" if m.get("cost_usd") is not None else ""

    def items(entries) -> list[str]:
        cite = lambda refs: f" _({', '.join(refs)})_" if refs else ""  # noqa: E731
        return [f"- **{e['id']}** {e['text']}" + (f"  \n  {e['note']}{cite(e['refs'])}" if e["note"] else "") for e in entries]

    def challenged(cs) -> str:
        return "; ".join(f"{c['id']} → {c['outcome'].lower()}" for c in cs) or "Accepted (never challenged)"

    out = [f"# Decision record: {m['request_id']}", "", f"> {doc['request']}", "",
           f"Deliberation ended **{m['termination']}** after {m['rounds']} rounds (policy `{m['policy']}`){cost}.", "",
           "## Summary", "", doc["executive_summary"], "", "## What this release will do", "",
           "**Core commitments** (only the stakeholder can drop these)", "", *items(doc["core_commitments"]), "",
           "**In scope**", "", *items(doc["in_scope"]), "", "## What it will not do", "",
           "**Out of scope for this release**", "", *items(doc["out_of_scope"]), "", "**Rejected during deliberation**", ""]
    out += [f"- {r['what']}: {r['why']}" + (f" _({', '.join(r['refs'])})_" if r["refs"] else "") for r in doc["rejected"]] \
        or ["- Nothing was dropped."]
    out += ["", "## Assumptions", "", "| ID | Assumption | Why it was implicit | Challenged? |", "|---|---|---|---|"]
    out += [f"| {a['id']} | {a['text']} | {a['why_implicit'] or '—'} | {challenged(a['challenges'])} |" for a in doc["assumptions"]]
    note = lambda e: f"  \n  {e['note']}" if e.get("note") else ""  # noqa: E731
    out += ["", "## Definitions", ""] + [f'- **{d["id"]}** "{d["term"]}": {d["definition"]}{note(d)}' for d in doc["definitions"]]
    out += ["", "## Success criteria", ""] + [f"- **{k['id']}** {k['metric']}: target {k['target']} ({k['measurement']}){note(k)}"
                                             for k in doc["success_criteria"]]
    out += ["", "## Open questions for humans", ""]
    if not doc["open_questions"]:
        out += ["None: every challenge was settled between the agents.", ""]
    for q in doc["open_questions"]:
        block = "blocks the build" if q["blocks_build"] else "does not block the build"
        out += [f"### {q['issue_id']} · {q['severity']} · {block}", "", f"**{q['question']}**", "",
                f"- Why it matters: {q['why_it_matters']}", f"- Decision owner: {q['decision_owner']}",
                "- Options: " + " / ".join(q["options"]), ""]
    out += ["## Tension report", "", t["summary"], "",
            "| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    out += [f"| {r['round']} | {r['raised']} | {r['open']} | {r['resolved']} | {r['escalated']} | {r['disagreement']:.2f} | "
            f"{r['proposer_confidence']} | {r['critic_confidence']} | {r['signal']} | {r['decision']} |" for r in t["by_round"]]
    fp = t["final_positions"]
    out += ["", f"- Proposer's remaining worry ({fp['proposer']['confidence']}/100): {fp['proposer']['worry']}",
            f"- Critic's remaining worry ({fp['critic']['confidence']}/100): {fp['critic']['worry']}"]
    out += [f"- ⚠ {f}" for f in t["flags"]]
    out += ["", "## Appendix: issue ledger", "", "| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |",
            "|---|---|---|---|---|---|---|---|"]
    out += [f"| {i['id']} | {i['severity']} | {i['lens']} | {', '.join(i['targets'])} | R{i['round_raised']} | {i['outcome']} | "
            f"{i['strikes']} | {i['challenge']} |" for i in doc["issues"]]
    return "\n".join(out) + "\n"
