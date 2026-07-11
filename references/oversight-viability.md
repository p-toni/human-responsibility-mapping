# Oversight Viability

The release rule asks whether evidence supports a boundary move and whether someone owns the consequence. This file covers the question most AI deployments skip: **can the humans actually do the part the map says they retain?**

A boundary move changes the human role it leaves behind. Review replaces production. Exception handling replaces routine handling. Monitoring replaces doing. Each retained role has failure modes of its own. A map that assigns "human still owns X" without checking that X is performable documents an intention, not a control.

This is also what regulators now require: EU AI Act Article 14 demands oversight that is *effective* — the overseer must be able to understand, monitor, intervene, and interrupt — not oversight that exists on paper. Empirically, paper-only oversight is the norm, not the exception (Green 2022).

---

## Check 1: Review capacity is a budget, not a vibe

`approve-before-action` and `sampling-review` consume human attention. That attention is finite, measurable, and — critically — has to be sufficient at the worst moment, not on the average week. Four rules make the budget real:

1. **Size the sample from a detection target.** "We review 10%" is meaningless without the volume behind it. Decide what failure rate must not go undetected, then size the sample: bounding an undetected failure rate at θ with ~95% confidence takes about `3 / θ` clean reviews in that stratum (the rule of three — Hanley & Lippman-Hand 1983). Bounding at 2.5% needs ~120 reviews; whether that is 10% or 40% of volume is a consequence, not a choice.
2. **Stratify by risk.** A uniform sample mostly re-measures the easy majority. Rare, high-harm strata need their own sample and their own detection target.
3. **Budget at peak, not steady state.** Volume spikes, incident surges, and staffing gaps arrive together; human-factors practice assesses workload under peaks and process upsets, not averages (UK HSE workload guidance). Keep planned reviewer utilization under ~80% — vigilance degrades with fatigue, and zero headroom means the first incident consumes the sampling budget.
4. **Check the intervention SLA, not just the sample rate.** Detection that arrives after the harm window closes is bookkeeping, not oversight. The review cadence must beat the harm's timeline.

If needed exceeds available, the control does not fail loudly — the sample rate decays silently toward what capacity allows, and the boundary moves without anyone deciding. The override-collapse watch-out in `SKILL.md` (override rate below ~5% means the boundary has moved de facto) detects this failure after the fact. The capacity budget prevents scheduling it in the first place.

Use the Oversight capacity check template in `references/templates.md` before approving any move that adds review load. If the budget doesn't fit, the honest options are: narrower scope, different controls, more reviewers, or no move — not a quietly decaying sample rate.

**Attention budget for AI-initiated work.** When AI initiates contact — alerts, suggestions, drafts, pings — every interrupt spends human attention whether or not it is useful. Alarm fatigue in clinical settings is the documented extreme (see the ICU example); notification fatigue in knowledge work is the common case. An AI that surfaces work faster than humans can absorb it degrades the very oversight it is supposed to enable. Budget interrupts like review load.

## Check 2: Skill retention (the ironies of automation)

Bainbridge (1983): automating routine work removes the practice that kept humans able to handle exceptions — while routing exactly the hardest cases to them. The more successful the automation, the less practiced the human fallback, and the more critical the moments that reach them.

If the retained human role is "handle what AI can't," ask what keeps that ability alive:

- rotation through un-automated work
- periodic drills or manual-handling days
- deliberately human-owned slices of routine volume
- shadowing AI-executed work with active prediction, not passive watching

If nothing does, either add a skill-retention plan to the movement condition or stop claiming humans as fallback in the map.

The same erosion applies to reviewers: people who no longer do the work lose the context needed to review it. Code review by people who no longer write code, QA by people who no longer handle tickets. Review quality decays on the same curve as production skill.

## Check 3: Accountability with authority (moral crumple zones)

"Accountable owner is explicit" can be satisfied while creating a **moral crumple zone**: a human who absorbs blame for a system they cannot meaningfully control (Elish 2019). Naming an owner is not the control; the owner's actual capacity to control is.

Meaningful control requires all four (cf. Santoni de Sio & van den Hoven 2018):

| Requirement | Test |
|---|---|
| Authority | Can they stop or constrain the system without escalating for permission? |
| Information | Can they see what the system did and why, in time to act? |
| Time | Is the intervention window longer than their realistic reaction time? |
| Capability | Do they have the skill to judge the output (see Check 2)? |

Field test: ask the named accountable owner to describe the last time they overrode or stopped the system, and what it cost them. If the honest answer is "never, and trying would be career noise," the accountability facet is decorated, not satisfied.

Two additions the owner test alone does not cover:

- **Automation bias is a design input, not a character flaw.** EU AI Act Article 14 requires overseers to remain aware of the tendency to over-rely on system output. Design against it: show uncertainty where it exists, force occasional blind review (the reviewer judges before seeing the AI's answer), and track agreement rates — a reviewer who never disagrees is either overseeing a perfect system or not overseeing.
- **High-impact moves need institutional oversight, not just an owner.** Green (2022)'s central remedy is institutional: an individual overseer can legitimate an unsafe system while being structurally unable to challenge it. For moves with large blast radius, add organizational risk acceptance (someone above the team formally accepts the residual risk), independent challenge (a party outside the deploying team who can block or escalate), and affected-party recourse (a working channel for the people the decisions land on to contest them).

## Check 4: The map's own telemetry will be gamed (Goodhart)

Movement conditions in this framework run on telemetry: override rate, edit distance, escalation rate, sampled QA pass rate. The moment those numbers decide boundary moves — or worse, individual performance reviews — they stop being neutral measurements (Goodhart's law; Strathern 1997). Operators who understand that low override rates justify automation that threatens their role will bend the number in whichever direction protects them. The instrument is load-bearing, so protect it:

- **Never use boundary telemetry for individual performance management.** State this in policy where operators can read it.
- **Watch denominators.** A falling override *rate* during rising volume can hide constant override *effort*.
- **Triangulate.** No single signal moves a boundary: override rate + reopen rate + sampled QA together, minimum.
- **Expect instrument decay.** Once AI drafts everything, edit distance measures anchoring, not quality; once AI triages everything, escalation rate measures the AI's policy, not case difficulty. Re-validate what each instrument means after every boundary move.

## The residue problem (worker impact)

Boundary moves are chosen per responsibility, but a job is the sum of its rows. Moving the satisfying rows to AI — the diagnosis, the writing, the solve — while leaving the residue — the reviewing, the exception-mopping, the accountability — produces a job nobody wants, staffed by people whose expertise is decaying (Check 2) and whose metrics are load-bearing (Check 4).

The stakeholder coverage template treats operators as a research source. Treat them also as parties whose role the map is redesigning. A map that redesigns someone's job without their input will meet resistance that shows up in telemetry as "adoption failure" and is actually rational self-defense. When reviewing a full map, read the "Human still owns" column top to bottom *as a job description* and ask whether you would take that job.

---

## Release-rule hookup

These checks appear in the `SKILL.md` release rule as the **Oversight viability** group:

```text
[ ] Review capacity is budgeted at peak load, with sample sizes derived from a stated detection target.
[ ] The accountable owner has the authority, information, time, and skill to intervene — not accountability in name only.
[ ] High-impact moves have independent challenge and affected-party recourse, not only a named owner.
[ ] Retained human skills have a retention plan where this move erodes their practice.
[ ] AI-only paths created or extended by this move are enumerated, with controls commensurate with their worst outcome (see references/agentic-work.md).
```

If a move passes capability and evidence checks but fails oversight viability, the correct decision is *do not move* or *change the design of the human role*, not "move and monitor." Monitoring is itself an oversight activity that just failed the viability test.
