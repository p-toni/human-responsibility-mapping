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

## Oversight viability
[ ] Review capacity is budgeted at peak load, with sample sizes derived from a stated detection target.
[ ] Accountable owner passes the authority / information / time / skill test.
[ ] Independent challenge and affected-party recourse exist for high-impact moves.
[ ] Skill-retention plan exists where the move erodes practice.
[ ] AI-only paths are enumerated with controls commensurate with their worst outcome.

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

## Durable ambiguity

Append the Ambiguity-aware release checks (below) — the gate is incomplete without them.

Decision: Move / do not move / validate further — record it as a Boundary decision record (below).
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

Run before any move that adds `approve-before-action` or `sampling-review` load. If needed exceeds available, the control will silently degrade into rubber-stamping — change scope, controls, or staffing instead.

Size the sample from a detection target, not from feel: to bound an undetected failure rate at θ with ~95% confidence you need about `3 / θ` clean reviews in that stratum (rule of three). Budget at peak, not mean — volume spikes, incidents, and staffing gaps arrive together (see `references/oversight-viability.md`).

```markdown
| AI-executed responsibility | Risk stratum | Volume/week (mean / peak) | Detection target (max undetected failure rate) | Reviews/week needed (≈ 3 / target) | Minutes per adequate review | Review hours needed at peak | Review hours available (worst shift) | Headroom ≥ 20%? |
|---|---|---|---|---:|---:|---:|---:|---|
```

Rules that keep the numbers honest:

- Stratify by risk: a uniform sample mostly re-measures the easy majority; rare high-harm strata need their own sample and target.
- Count AI-initiated interrupts (alerts, suggestions, pings) in the same budget: attention spent absorbing them is attention unavailable for review.
- Detection without intervention time is not oversight: check that the review cadence beats the harm's timeline (intervention SLA), not just its rate.
- Keep planned reviewer utilization under ~80%: vigilance degrades with fatigue, and zero headroom means the first incident consumes the sampling budget.

## AI-only path table

After any boundary move, trace the work architecture for sequences of AI-executed steps a work item can traverse with no human contact. Row-level controls do not cover chains; each path needs path-level controls **commensurate with its worst outcome** (see `references/agentic-work.md` for control types).

```markdown
| Path (AI-executed steps in sequence) | Entry condition | Volume (mean / peak) | Worst plausible outcome | Hazard class (reversible / irreversible; detection latency) | Controls (type: control) | Owner |
|---|---|---|---|---|---|---|
```

Hazard rule: if the worst outcome is irreversible, or detection latency exceeds the intervention window, detective controls (sampling, audit) are not sufficient — add preventive or containment controls (entry constraints, action budgets, runtime invariants, kill switch), or prohibit the path by inserting a human gate.

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
