# Templates

## Human Responsibility Snapshot

```markdown
# Human Responsibility Snapshot

## Work domain
## Current work architecture
## Old constraints
## Main roles

| Responsibility | Human owner today | AI role now/next | Boundary state now | Target state | Movement condition | Human still owns |
|---|---|---|---|---|---|---|

## Trust / accountability requirements
## Work architecture shift
## Product implications
## Eval implications
## Telemetry signals
## Open assumptions and contradictions
```

## Evidence ledger

```markdown
| Claim | Evidence label | Source | Confidence | Decision impact | Validation plan |
|---|---|---|---:|---|---|
```

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
