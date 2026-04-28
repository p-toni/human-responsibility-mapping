# Illustrative Synthetic Example — Not Research Output

This example is synthetic. It shows the shape of a Human Responsibility Snapshot for a security/red-team workflow. **It is not based on validated research.** Do not quote rows from this file in a real PRD or threat model.

Per the framework's evidence policy, every claim below carries an explicit evidence label. All labels in this file are `ai_generated_hypothesis` because the example was generated, not researched. A real map for your team would replace these with grounded claims (`observed`, `interview_derived`, `artifact_derived` from incidents/postmortems, `telemetry_derived` from your tooling).

| Responsibility | Human owner today | AI role now/next | Boundary state now | Target state | Movement condition | Human still owns | Evidence label |
|---|---|---|---|---|---|---|---|
| Gather context for finding | Security engineer | Build evidence packet from logs/configs | AI-assisted | AI-assisted | Source traceability and reproducible artifact links | Context acceptance | `ai_generated_hypothesis` |
| Explore attack path | Red teamer | Suggest or run bounded exploration | AI-assisted | AI-executed (`policy-governed` + `rollback-required`) | Sandbox enforcement, policy gate on action types, full action trace | Objective framing and authorization | `ai_generated_hypothesis` |
| Validate finding | Security engineer | Reproduce with trace | AI-assisted | AI-assisted | Reproducibility eval; false-positive rate measured | Final validation judgment | `ai_generated_hypothesis` |
| Prioritize remediation | Vulnerability manager | Rank with policy and business context | AI-assisted | AI-assisted | Ranking eval and transparent rationale; SLA fit measured | Risk tradeoff | `ai_generated_hypothesis` |
| Accept residual risk | Product/security owner | Inform decision with evidence packet | Human-owned | Human-owned | Not movable — accountability constraint | Decision and accountability | `ai_generated_hypothesis` |

Release gate (illustrative): do not move attack-path exploration to AI-executed until sandboxing, policy gates, action traceability, evals (sensitivity for known attack patterns, false-positive bound), and human stop controls are in place and tested. Apply the SKILL.md release rule before any boundary move.
