# Workshop Guide

Use this when a team needs a first Human Responsibility Snapshot in one session. Keep the goal narrow: one work domain, one workflow, one AI capability or capability hypothesis.

## Inputs

- Workflow or service-blueprint sketch, even if rough.
- Current policy, escalation, QA, or approval rules.
- Example tickets, cases, traces, or artifacts.
- Any known eval, telemetry, incident, or customer-feedback data.
- Participants who can speak for operation, decision, accountability, and governance. If a role is missing, mark the coverage gap instead of filling it with guesses.

## 60-minute workshop

```text
0-5 min: Define the work domain, workflow boundary, and decision the map must support.
5-15 min: Map current work architecture: sequence, queues, handoffs, reviews, approvals, artifacts, feedback loops, control surfaces, metrics.
15-25 min: Break the workflow into responsibility units. Split any unit that hides different boundary states.
25-38 min: Assign current and target boundary states for each responsibility. Use control modes only for AI-executed work.
38-48 min: Define movement conditions: evidence, controls, evals, telemetry, rollback, escalation, accountable owner.
48-55 min: Identify stakeholder coverage gaps, old-layout traps, and contradiction signals.
55-60 min: Choose the first three deliverables and owners.
```

## First three deliverables

1. A filled Human Responsibility Snapshot.
2. The top 3 boundary moves or "do not move yet" decisions.
3. A validation plan covering evals, telemetry, stakeholder gaps, and release-gate blockers.

## Done means

- Every responsibility has one current boundary state and one target state.
- Every AI-executed target has exactly one control mode.
- Every load-bearing claim has an evidence label and source reference where possible.
- Missing evidence is labeled `unvalidated`; synthetic assumptions are labeled `ai_generated_hypothesis`.
- Stakeholder coverage gaps are visible.
- The team knows what to build, what not to automate, what to measure, or what to validate next.

## Facilitation rules

Do not start with demographic personas. Do not debate automation level before defining accountability. Do not let "AI can do this" become "AI should do this." Capture disagreements as assumptions or contradictions. Preserve evidence labels. End with decisions or validation tasks.
