# Illustrative Synthetic Example — Not Research Output

This example is synthetic. It shows the shape of a Human Responsibility Snapshot for a customer-support workflow. **It is not based on validated research.** Do not quote rows from this file in a real PRD or strategy memo.

Per the framework's evidence policy, every claim below carries an explicit evidence label. All labels in this file are `ai_generated_hypothesis` because the example was generated, not researched. A real map for your team would replace these with `observed`, `interview_derived`, `telemetry_derived`, or `artifact_derived` claims grounded in your actual research.

For the complete synthetic deliverable (stakeholder coverage, evidence ledger, oversight capacity, AI-only paths, full release gate, decision record), see [`customer-support-full-map.md`](customer-support-full-map.md).

| Responsibility | Human owner today | AI role now/next | Boundary state now | Target state | Movement condition | Human still owns | Evidence label |
|---|---|---|---|---|---|---|---|
| Gather context | Support agent | Build source-linked context pack | AI-assisted | AI-assisted | Source fidelity ≥ 90% on held-out tickets; agent can edit context inline | Final interpretation | `ai_generated_hypothesis` |
| Draft response | Support agent | Draft policy-checked response | AI-assisted | AI-assisted | Response correctness eval and human approval gate | Customer send | `ai_generated_hypothesis` |
| Execute bounded fix (e.g., reset session) | Support agent / engineer | Apply reversible fix within policy | Human-owned | AI-executed (`approve-before-action` + `rollback-required`) | Approval gate, tested rollback path, audit log, eval of policy adherence | Accountability for action | `ai_generated_hypothesis` |
| Escalate | Support lead | Route with evidence packet | AI-assisted | AI-executed (`policy-governed`) | Escalation-quality eval and confidence threshold | Override and exception handling | `ai_generated_hypothesis` |

Release gate (illustrative): do not allow AI to send customer responses without human approval until response correctness, source fidelity, and policy-compliance evals pass; post-launch telemetry (override rate, reopen rate, escalation rate, customer-satisfaction delta) is in place; and the full SKILL.md release rule holds — including **oversight viability** (peak review capacity, owner authority test, skill retention, AI-only path controls) and durable-ambiguity refresh triggers (behavioral and system-change).
