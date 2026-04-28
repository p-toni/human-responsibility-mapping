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

For `AI-executed`, specify one `control_mode`: `approve-before-action`, `policy-governed` (AI acts within bounded policy; humans review only exceptions or anomalies), `sampling-review`, or `rollback-required`. See `SKILL.md` for full definitions and the watch-out about implicit boundary movement when override rates collapse.

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

## Durable ambiguity

For full guidance on ambiguity-aware mapping, optionality, multiple-hypothesis tables, and contradiction handling, see `references/durable-ambiguity.md`.

In short: a map is not a prediction. It is an option-preserving instrument. Keep claims evidence-labeled, prefer reversible boundary moves, define contradiction signals, and refresh when reality disagrees.
