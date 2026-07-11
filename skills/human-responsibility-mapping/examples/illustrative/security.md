# Illustrative Synthetic Example — Not Research Output

This example is synthetic. It shows the shape of a Human Responsibility Snapshot for a security/red-team workflow. **It is not based on validated research.** Do not quote rows from this file in a real PRD or threat model.

Per the framework's evidence policy, every claim below carries an explicit evidence label. All labels in this file are `ai_generated_hypothesis` because the example was generated, not researched. A real map for your team would replace these with grounded claims (`observed`, `interview_derived`, `artifact_derived` from incidents/postmortems, `telemetry_derived` from your tooling).

This domain is **exploratory + agentic**: AI may propose and run multi-step exploration. Per `SKILL.md` / `references/agentic-work.md`, planning is its own responsibility row — usually the most consequential boundary and the least examined. Control stacks compose (`policy-governed` + `rollback-required`); movement conditions for orchestration above Human-owned must specify control-transfer mechanics (takeover, consultation triggers, approval triggers, emergency stop).

| Responsibility | Human owner today | AI role now/next | Boundary state now | Target state | Movement condition | Human still owns | Evidence label |
|---|---|---|---|---|---|---|---|
| Plan and sequence the work | Red teamer | Propose exploration plan and step order | Human-owned | AI-assisted | Human approves plan before execution; consultation triggers on novel asset class or out-of-sandbox action; emergency stop tested; step/time budget | Objective framing, plan approval, stop authority | `ai_generated_hypothesis` |
| Gather context for finding | Security engineer | Build evidence packet from logs/configs | AI-assisted | AI-assisted | Source traceability and reproducible artifact links | Context acceptance | `ai_generated_hypothesis` |
| Explore attack path | Red teamer | Suggest or run bounded exploration steps | AI-assisted | AI-executed (`policy-governed` + `rollback-required`) | Sandbox enforcement, policy gate on action types, full action trace, tested rollback of environment changes | Authorization of objective and exception handling | `ai_generated_hypothesis` |
| Validate finding | Security engineer | Reproduce with trace | AI-assisted | AI-assisted | Reproducibility eval; false-positive rate measured | Final validation judgment | `ai_generated_hypothesis` |
| Prioritize remediation | Vulnerability manager | Rank with policy and business context | AI-assisted | AI-assisted | Ranking eval and transparent rationale; SLA fit measured | Risk tradeoff | `ai_generated_hypothesis` |
| Accept residual risk | Product/security owner | Inform decision with evidence packet | Human-owned | Human-owned | Not movable — accountability constraint | Decision and accountability | `ai_generated_hypothesis` |

Release gate (illustrative): do not move attack-path exploration to AI-executed until sandboxing, policy gates, action traceability, evals (sensitivity for known attack patterns, false-positive bound), human stop controls, and **oversight viability** (review capacity for policy exceptions, owner authority/information/time/skill, AI-only path analysis if plan + explore both execute without a human) are in place and tested. Keep `plan and sequence the work` at AI-assisted until control-transfer mechanics are demonstrated. Apply the full SKILL.md release rule before any boundary move.
