# Illustrative Synthetic Example — Not Research Output

This is a synthetic Boundary Decision Record for one boundary from [`customer-support-full-map.md`](customer-support-full-map.md). It exists to show the artifact shape and, specifically, what a **rejection on oversight-viability grounds** looks like: a move whose capability and evidence checks pass but whose human side does not hold. All numbers are invented; every claim is `ai_generated_hypothesis`.

---

# Boundary Decision Record: Send low-risk acknowledgement

- **Date / map version:** 2026-07-01 / customer-support map v4
- **System versions:** `pinned-model-id`; `prompts@a1b2c3d`; `ticketing-api@2.3`; `kb-snapshot-2026-06-15`
- **Boundary:** Human-owned -> AI-executed (`sampling-review`)
- **Decision:** do not move — redesign the review role first
- **Release rule result:**
  - Movement condition: PASS. Shadow-mode replay on 2,400 historical tickets met the agreed correctness and eligibility bounds, including per-segment breakdown. Evals defined and passing. Telemetry live. (`ai_generated_hypothesis`)
  - Accountability: PASS. Support lead on call named as accountable owner; escalation path defined. (`ai_generated_hypothesis`)
  - Oversight viability: **FAIL.**
    - Review capacity: eligible volume ~1,200 tickets/week; agreed sample 10% at ~4 minutes per adequate review = **8.0 review hours/week. Current QA capacity: 3.0 hours/week.** The sample rate would decay silently toward what capacity allows (~4%), below the level the eligibility policy was justified on. (`ai_generated_hypothesis`)
    - Skill retention: acknowledgements are the training ground where new agents learn account context before harder tickets; removing 100% of them removes the on-ramp. No retention plan proposed. (`ai_generated_hypothesis`)
    - Owner authority test: the support lead on call can stop the system, has audit-log access, and reviewed a stop drill — this sub-check passes. (`ai_generated_hypothesis`)
    - AI-only paths: classify (`policy-governed`) -> acknowledge (`sampling-review`) would create the first end-to-end AI-only path for low-risk tickets. Path enumerated, but no path-level control proposed — row samples don't cover the chain. (`ai_generated_hypothesis`)
  - Durable ambiguity: PASS, except system-change revalidation depends on the model pin holding (vendor alias risk noted). (`ai_generated_hypothesis`)
- **Dissent and unresolved objections:** Support ops argued 5% sampling is adequate given shadow-mode results; QA lead disagreed because shadow-mode preceded the summer volume spike. Recorded, unresolved. (`ai_generated_hypothesis`)
- **Rollback plan and trigger:** feature-flag off; auto-revert if reopen rate for AI-acknowledged tickets exceeds baseline +2pp over any 7-day window. (`ai_generated_hypothesis`)
- **Revisit date or trigger:** revisit when QA capacity reaches 8 h/week or eligible volume drops; hard revisit 2026-09-01. (`ai_generated_hypothesis`)
- **Accountable owner sign-off:** support leadership signed the *do-not-move* decision and the capacity remediation owner. (`ai_generated_hypothesis`)

---

## Why this example matters

Under the v0.3 release rule this move passes: capability demonstrated, evals green, telemetry live, owner named, reversibility preserved. Every failed check above is on the human side of the boundary — attention, practice, and chain coverage — which is exactly the side most launch reviews never inspect. The decision is not "no automation"; it is "the retained human role, as designed, cannot do its job — redesign it, then move."
