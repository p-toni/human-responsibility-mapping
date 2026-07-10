# Core Concepts

## Boundary

Use one concept: **Boundary**.

| Facet | Question |
|---|---|
| Current line | What does the human own today, and what does AI do today? |
| Movement condition | What evidence, control, eval, telemetry, or policy would allow the line to move? |
| Accountability | Who remains responsible if the AI is wrong, incomplete, unsafe, or misused? |

## Boundary states

| State | AI role | Human role |
|---|---|---|
| Human-owned | AI absent or peripheral | Human performs and decides |
| AI-assisted | AI summarizes, suggests, ranks, drafts, or explains | Human chooses, edits, approves, decides |
| AI-executed | AI takes bounded action, routes, updates, or triggers work | Human gates, monitors, audits, or governs |

For `AI-executed`, specify a control stack — one or more of `approve-before-action`, `policy-governed` (AI acts within bounded policy; humans review only exceptions or anomalies), `sampling-review`, and `rollback-required`. The modes cover different categories (authorization, runtime constraint, review, recoverability) and compose. Record the current stack and the target stack separately: a boundary that is AI-executed today needs its current controls in the map even mid-move. See `SKILL.md` for full definitions and the watch-out about implicit boundary movement when override rates collapse.

## Granularity rule

A responsibility unit is too broad if it hides different boundary states.

Bad: `handle incident`.

Better: detect signal, classify severity, gather context, propose hypothesis, execute containment, notify stakeholders, validate recovery, write postmortem.

A useful responsibility unit has one primary owner, one primary output, one boundary state, one trust/accountability question, and one eval or telemetry implication.

## Prioritization heuristic

Prioritize boundary work by high user pain, high volume, clear evidence requirement, reversible/controllable failure mode, measurable eval, available telemetry, accountable owner, and meaningful work-architecture improvement.

Avoid first moves where failure is irreversible, evidence is weak, or accountability is unclear.

## Closure criterion

A map is good enough when it changes what to build, what not to automate, what eval to run, what telemetry to add, what human control to preserve, what work architecture to redesign, or what assumption to validate next.

## Map maintenance

A map with no owner is a workshop artifact, not an operating one. Every map names:

- **An owner** — one person accountable for the map staying true, usually the product owner of the AI capability.
- **A home** — where the current version lives (repo, wiki page, planning doc). Machine-readable maps (`schemas/`) can live in the repo and be linted in CI with `scripts/validate_map.py`.
- **Refresh triggers** — behavioral contradictions (see `references/durable-ambiguity.md`) and system changes: model, prompt, tool, or corpus version changes invalidate the evidence behind affected boundaries until evals re-run (see `references/agentic-work.md`).
- **Decision history** — one Boundary Decision Record per move / do-not-move decision (`references/templates.md`), so accountability has an audit trail instead of a recollection.

## Durable ambiguity

For full guidance on ambiguity-aware mapping, optionality, multiple-hypothesis tables, and contradiction handling, see `references/durable-ambiguity.md`.

In short: a map is not a prediction. It is an option-preserving instrument. Keep claims evidence-labeled, prefer reversible boundary moves, define contradiction signals, and refresh when reality disagrees.
