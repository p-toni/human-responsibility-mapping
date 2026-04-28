# Illustrative Synthetic Example — Not Research Output

This example applies Human Responsibility Mapping to **ICU bedside nursing during a multi-patient deterioration event**. It is included as a deliberate stress test: the framework's defaults assume decomposable knowledge work, AI as assistant, and an identifiable single role per responsibility. ICU bedside nursing breaks all three. The example shows what the framework looks like when the default assumptions invert.

**This example is synthetic.** It is not based on validated nursing research, real ICU shadowing, or interviews with clinicians. Do not quote rows from this file in a clinical workflow design or vendor RFP. Per the framework's evidence policy, every claim carries the label `ai_generated_hypothesis`.

## Why this example breaks the defaults

- **Embodied, not knowledge work.** Many responsibilities are physical (titrate a drip, reposition a patient, suction an airway). Decomposing them into "responsibility units" loses the embodied judgment.
- **Non-linear, multi-patient.** Attention is allocated across simultaneous patients; the workflow is a continuous prioritization loop, not a ticket pipeline.
- **No single role per responsibility.** Charge nurse, bedside RN, respiratory therapist, intensivist, pharmacist, family — overlapping, fluid, and partly determined by who is physically present.
- **AI is rarely "assistant" — at best monitor, at worst harm.** Alarm fatigue is a documented patient-safety harm; every additional alert without corresponding human capacity-to-act *worsens* outcomes.
- **Accountability is legally codified.** The accountable-owner facet is fixed by state nursing practice acts and hospital licensing, not negotiable as a UX surface.
- **Reversibility is often zero.** Many actions cannot be rolled back.

## Snapshot

| Responsibility | Human owner today | AI role now/next | Boundary state now | Target state | Movement condition | Human still owns | Evidence label |
|---|---|---|---|---|---|---|---|
| Continuous monitoring of vitals across patients | Bedside RN + monitors | AI surfaces deterioration patterns earlier | AI-assisted (existing alarm systems) | AI-assisted with reduced alarm volume | Demonstrated reduction in alarm fatigue without missed events; per-population calibration | Trend interpretation and acting | `ai_generated_hypothesis` |
| Prioritize attention across patients | Charge nurse + bedside RN | AI suggests acuity-weighted priority | Human-owned | AI-assisted | Suggestions match expert ranking on retrospective shifts; do not replace charge nurse role | Final allocation decision | `ai_generated_hypothesis` |
| Detect early sepsis, ARDS, hemodynamic deterioration | Bedside RN clinical assessment | AI scoring (e.g., MEWS-like) | AI-assisted | AI-assisted | Local sensitivity/specificity on this ICU's population; subgroup parity (age, comorbidity) | Clinical assessment and escalation | `ai_generated_hypothesis` |
| Titrate continuous infusions (vasopressors, sedation) | Bedside RN per protocol | AI suggests dose changes per protocol | Human-owned | Human-owned | Not movable — physiologic blast radius is high; reversibility low | Dose, route, and timing | `ai_generated_hypothesis` |
| Communicate change in patient status | Bedside RN | AI drafts handoff/SBAR text | Human-owned | AI-assisted | Drafts pass clinician review without semantic loss; no auto-send | Verbal handoff and clinical interpretation | `ai_generated_hypothesis` |
| Document care | Bedside RN | AI drafts notes from observed actions | Human-owned | AI-assisted | Auto-draft accuracy ≥ baseline; nurse edits before sign | Sign-off (legal record) | `ai_generated_hypothesis` |
| Decide to call rapid response / code | Bedside RN + intensivist | AI surfaces risk score | Human-owned | Human-owned | Not movable — accountability is legally fixed | The call | `ai_generated_hypothesis` |

## What's different from the knowledge-work examples

1. **More boundaries stay Human-owned.** The accountability facet alone (legal, regulatory) prevents many movements that the movement-condition facet would otherwise allow. This is the right outcome — the framework correctly resists automation pressure here.
2. **The movement-condition facet is dominated by harm avoidance, not capability.** "Could AI do this?" is the wrong question; "would AI doing this create alarm fatigue, automation bias, or moral distress?" is the right one.
3. **Optionality is asymmetric.** Reversing a workflow change in an ICU is much harder than reversing a customer-support change — clinical staff retrain slowly, muscle memory matters, and the wrong tool can become embedded in safety routines. `prefer boundary moves that preserve optionality` becomes "prefer not moving, then move only with extensive piloting."
4. **The work-architecture lens matters more than usual.** The biggest AI value is probably *flow* changes (continuous monitoring instead of batched rounding observations; risk-weighted attention instead of FIFO patient lists), not *atom* changes (replacing what nurses do).

## Release gate notes

For any AI tool in this domain, the release rule from `SKILL.md` should be augmented with: alarm-fatigue impact study, subgroup parity across patient populations the unit actually treats (not vendor's training set), regulatory pathway (FDA SaMD class), and a kill-switch that frontline staff can pull without escalation. Several boundary moves in this snapshot should remain Human-owned indefinitely — this is the correct application of the framework, not a bug.
