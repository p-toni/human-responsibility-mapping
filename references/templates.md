# Templates

## Human Responsibility Snapshot

```markdown
# Human Responsibility Snapshot

## Work domain
## Current work architecture
## Old constraints
## Main roles

| Responsibility | Human owner today | AI role now/next | Boundary state now | Target state | Movement condition | Human still owns | Evidence label |
|---|---|---|---|---|---|---|---|

## Trust / accountability requirements
## Work architecture shift
## Product implications
## Eval implications
## Telemetry signals
## Open assumptions and contradictions
## Stakeholder coverage
```

## Evidence ledger

```markdown
| Claim | Evidence label | Source | Confidence | Decision impact | Validation plan |
|---|---|---|---:|---|---|
```

## Stakeholder coverage

Track which roles have been sampled and whether the sample is stable enough to support downstream claims. A claim labeled `interview_derived` from one conversation is not the same kind of evidence as one from repeated conversations across role types.

```markdown
| Role | Sampled count | Saturation status | Evidence types collected | Gaps |
|---|---:|---|---|---|
| Operator |  |  |  |  |
| Reviewer |  |  |  |  |
| Decision owner |  |  |  |  |
| Accountable owner |  |  |  |  |
| Beneficiary |  |  |  |  |
| Governance owner |  |  |  |  |
| Exception handler |  |  |  |  |
```

Saturation status values:

- `unsampled` — no contact made with this role.
- `initial` — fewer than 3 conversations; do not generalize.
- `theme-stable` — 3+ conversations and new sessions stop yielding new themes (Glaser & Strauss 1967).
- `n/a` — role is not relevant to this domain.

If any load-bearing role is `unsampled` or `initial`, label downstream claims about that role `inferred` or `unvalidated` and treat them as hypotheses pending research.

## Trust profile

```markdown
| Role | Responsibility | Trust requirement | Trust breaker | Evidence/control needed | Boundary implication |
|---|---|---|---|---|---|
```

## Eval plan

```markdown
| Boundary movement or work shift | Eval scenario | Success criteria | Failure criteria | Required evidence | Owner |
|---|---|---|---|---|---|
```

## Telemetry plan

```markdown
| Assumption | Telemetry signal | Expected pattern | Contradiction signal | Refresh action |
|---|---|---|---|---|
```

## System release gate

```markdown
# System Release Gate

Boundary or work-architecture shift:

## Capability
[ ] Capability demonstrated in realistic scenarios.
[ ] Known limitations documented.
[ ] Failure modes understood.

## Trust and evidence
[ ] Evidence is inspectable.
[ ] Calibration / uncertainty is visible where relevant.
[ ] Human control is appropriate.

## Accountability
[ ] Accountable owner is explicit.
[ ] Human-only decisions are preserved.
[ ] Escalation path exists.

## Evals
[ ] Required evals are defined.
[ ] Required evals pass.
[ ] Regression coverage exists.

## Telemetry
[ ] Adoption is measurable.
[ ] Overrides are measurable.
[ ] Misuse is measurable.
[ ] Rejection or abandonment is measurable.
[ ] Drift or degradation can be detected.

Decision: Move / do not move / validate further
```

## Boundary decision record

One per move / do-not-move decision. This is the audit trail the accountability facet depends on — an ADR for boundaries.

```markdown
# Boundary Decision Record: [responsibility]

- Date / map version:
- System versions (model, prompts, tools, corpus):
- Boundary: [current state] -> [proposed state] ([control mode if AI-executed])
- Decision: move / do not move / validate further
- Release rule result: [which checks passed and failed, with evidence links]
- Oversight viability: [capacity math, skill-retention plan, owner authority test]
- Dissent and unresolved objections: [who disagreed and why — record it, do not erase it]
- Rollback plan and trigger:
- Revisit date or trigger:
- Accountable owner sign-off:
```

## Oversight capacity check

Run before any move that adds `approve-before-action` or `sampling-review` load. If needed exceeds available, the control will silently degrade into rubber-stamping — change scope, control mode, or staffing instead.

```markdown
| AI-executed responsibility | Control mode | Expected items/week | Minutes per adequate review | Review hours needed | Review hours available | Fits? |
|---|---|---:|---:|---:|---:|---|
```

Count AI-initiated interrupts (alerts, suggestions, pings) in the same budget: attention spent absorbing them is attention unavailable for review.

## AI-only path table

After any boundary move, trace the work architecture for sequences of AI-executed steps a work item can traverse with no human contact. Row-level controls do not cover chains; each path needs a path-level control (end-to-end sampling of completed cases, or periodic whole-case audit).

```markdown
| Path (AI-executed steps in sequence) | Entry condition | Expected volume | Worst plausible outcome | Path-level control | Owner |
|---|---|---:|---|---|---|
```

## Contradiction log

```markdown
| Date | Assumption challenged | Signal | What we learned | Map update | Product/eval impact |
|---|---|---|---|---|---|
```

## Multiple work-architecture hypotheses

```markdown
| Hypothesis | What changes | Evidence needed | Risk | Option-preserving next step |
|---|---|---|---|---|
| H1 |  |  |  |  |
| H2 |  |  |  |  |
| H3 |  |  |  |  |
```

Use this when the future workflow is unclear or stakeholders disagree.

## Ambiguity-aware release checks

```markdown
## Durable ambiguity

[ ] We have identified what remains uncertain.
[ ] We have not collapsed multiple plausible futures into one assumed path.
[ ] The proposed change preserves reversibility where possible.
[ ] The proposed change has clear override or escalation.
[ ] The proposed change has telemetry to detect contradiction.
[ ] The map has a scheduled or trigger-based refresh.
```
