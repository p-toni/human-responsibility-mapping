# Prior Art

Human Responsibility Mapping is an integration framework. It does not introduce new theory. It packages established ideas from automation research, trust research, service design, decision-rights frameworks, evidence grading, and product practice into one operating artifact for AI product teams.

This file lists the prior art the framework draws on, names the specific works, and states what is and isn't original.

## How to read this file

Each section names a body of work, the closest prior art with proper citations, what Human Responsibility Mapping borrows, and what it doesn't claim.

---

## Levels of automation and supervisory control

The Boundary states (Human-owned / AI-assisted / AI-executed) and the control modes for AI-executed work are a compressed restatement of work in supervisory control.

- Sheridan, T. B., & Verplank, W. L. (1978). *Human and computer control of undersea teleoperators.* MIT Man-Machine Systems Laboratory. The original 10-level supervisory control taxonomy.
- Sheridan, T. B. (1992). *Telerobotics, automation, and human supervisory control.* MIT Press. The refined 10-level scale most often cited.
- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics — Part A*, 30(3), 286–297. The four-stage information-processing model (acquisition / analysis / decision / action) crossed with levels of automation.
- Endsley, M. R., & Kaber, D. B. (1999). Level of automation effects on performance, situation awareness and workload in a dynamic control task. *Ergonomics*, 42(3), 462–492.
- SAE International (2021). *J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles.* The 0–5 driving-automation level framework.

What this framework borrows: the gradient idea, the principle that higher automation isn't automatically better, and the recognition that level boundaries are policy choices, not capability ceilings. What it doesn't claim: a new automation taxonomy. The three-state simplification is a deliberate compression — for AI product teams the practical decision is "does AI take action or not, and under what control mode," not which of ten rungs you're on.

## Trust in automation and calibrated reliance

Trust requirements and movement conditions are a practitioner restatement of the trust-in-automation literature.

- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50–80. The canonical purpose / process / performance trust model and the calibrated-reliance frame.
- Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors*, 57(3), 407–434. Three-layer model: dispositional, situational, learned trust.
- Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230–253. The use/misuse/disuse/abuse failure modes framework.

What this framework borrows: the idea that trust must be calibrated to evidence, not maximized; the questions used in capability-confrontation conversations; the warning that automation bias and disuse are both real. What it doesn't claim: a new trust theory.

## Service blueprinting and work-architecture redesign

Work architecture mapping draws on service design and lean process redesign.

- Shostack, G. L. (1984). Designing services that deliver. *Harvard Business Review*, 62(1), 133–139. Original service blueprint, including the line of visibility.
- Bitner, M. J., Ostrom, A. L., & Morgan, F. N. (2008). Service blueprinting: A practical technique for service innovation. *California Management Review*, 50(3), 66–94.
- Rother, M., & Shook, J. (1998). *Learning to See: Value Stream Mapping to Add Value and Eliminate Muda.* Lean Enterprise Institute. The current-state / future-state value stream method.
- SIPOC (Suppliers, Inputs, Process, Outputs, Customers): a standard Six Sigma / Lean Six Sigma scoping diagram, widely attributed to Motorola Six Sigma practice in the 1980s; no canonical academic origin.

What this framework borrows: current-state / future-state mapping, the discipline of representing handoffs and review points, and the lean instinct against "paving the cowpath." The "old layout trap" warning — that AI inserted into existing workflows often only makes old work faster — is the framework's restatement of Hammer & Champy's BPR principle. What it doesn't claim: a new service-design method.

## Responsibility and decision-rights frameworks

Roles and accountability draw on standard decision-rights frameworks.

- RACI (Responsible, Accountable, Consulted, Informed) and its variants (RASCI, CAIRO, RACI-VS, ARCI in ITIL): no single canonical citation; widely used in project management since at least the 1970s. Common reference: Project Management Institute, *PMBOK Guide*.
- Rogers, P., & Blenko, M. W. (2006). Who has the D? How clear decision roles enhance organizational performance. *Harvard Business Review*, 84(1), 52–61. The RAPID (Recommend / Agree / Perform / Input / Decide) framework.

What this framework borrows: the discipline of separating who performs from who decides from who is accountable. What it adds, for autonomous systems: explicit *Exception handler* and *Governance owner* roles, because AI systems generate more exceptions and policy questions than human-only systems.

## Capability confrontation and concept testing

The "show users a plausible AI capability and observe trust/resistance" method is a long-standing user-research technique.

- Hutchinson, H., et al. (2003). Technology probes: Inspiring design for and with families. *Proceedings of CHI 2003*, 17–24.
- Kelley, J. F. (1984). An iterative design methodology for user-friendly natural language office information applications. *ACM Transactions on Information Systems*, 2(1), 26–41. The original Wizard of Oz study.

What this framework borrows: the idea of using concrete capability demos to discover delegation boundaries. What it doesn't claim: a new research method. "Capability confrontation" was deprecated as a term in earlier drafts because it added nothing to existing technology probe / Wizard of Oz practice.

## Oversight viability and the limits of human-in-the-loop

The Oversight viability checks in the release rule restate a literature on why nominal human oversight fails structurally.

- Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775–779. Automating routine work removes the practice that kept humans able to handle the exceptions routed to them.
- Elish, M. C. (2019). Moral crumple zones: Cautionary tales in human-robot interaction. *Engaging Science, Technology, and Society*, 5, 40–60. Humans positioned to absorb liability for systems they cannot meaningfully control.
- Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. *Computer Law & Security Review*, 45, 105681. Empirical case that oversight-on-paper is the norm and functions as legitimation; the central remedy is institutional oversight, which the independent-challenge and affected-party-recourse checks follow.
- Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems: A philosophical account. *Frontiers in Robotics and AI*, 5, 15. The tracking/tracing conditions behind the authority–information–time–capability test.
- Strathern, M. (1997). 'Improving ratings': Audit in the British university system. *European Review*, 5(3), 305–321. The standard formulation of Goodhart's law, applied here to the map's own telemetry.
- Hanley, J. A., & Lippman-Hand, A. (1983). If nothing goes wrong, is everything all right? Interpreting zero numerators. *JAMA*, 249(13), 1743–1745. The rule of three used to size review samples from a detection target.
- UK Health and Safety Executive. *Human factors: workload* guidance. Staffing and workload assessed under peaks, emergencies, and process upsets — not steady-state averages; the basis for budgeting review capacity at peak.
- Shneiderman, B. (2022). *Human-Centered AI.* Oxford University Press. High automation and high human control as a two-dimensional space, not a slider.
- Regulation (EU) 2024/1689 (EU AI Act), Article 14. Human oversight for high-risk systems must be *effective* — the overseer must be able to understand, monitor, intervene, and interrupt — and designed with automation bias in mind.
- NIST (2023). *AI Risk Management Framework 1.0*; NIST (2024). *Generative AI Profile* (NIST-AI-600-1). Govern/map/measure/manage risk vocabulary that release gates and telemetry plans should be legible to. NIST stresses its actions are not a checklist; this framework's gates are decision points inside continuous risk management, not a substitute for it.

What this framework borrows: oversight is a resource-constrained activity that fails structurally, not just occasionally; naming an accountable owner is not the same as giving them control. What it doesn't claim: a new oversight theory or a compliance mapping to Article 14.

## Systems safety and composition

The AI-only path check restates a systems-safety principle.

- Leveson, N. G. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety.* MIT Press. STAMP/STPA: accidents emerge from unsafe interactions between components that are each locally correct, so hazards must be analyzed on the control structure, not per component.

What this framework borrows: gate paths, not just rows. What it doesn't claim: to substitute for STPA — safety-critical systems should run the real analysis on the future-state work architecture.

## Agent autonomy and agentic governance

The guidance in `references/agentic-work.md` aligns the framework with the agent-autonomy literature.

- Feng, K. K., McDonald, D. W., & Zhang, A. X. (2025). Levels of autonomy for AI agents. arXiv:2506.12469; Knight First Amendment Institute. Five user roles (operator, collaborator, consultant, approver, observer); autonomy as a designable property separate from capability.
- Shavit, Y., et al. (2023). *Practices for governing agentic AI systems.* OpenAI. Practical governance measures for agentic deployments, including human approval points and incident readiness.
- Mitchell, M., Ghosh, A., Luccioni, A. S., & Pistilli, G. (2025). Fully autonomous AI agents should not be developed. arXiv:2502.02649. Autonomy-level scale and the argument for retaining human control points.

What this framework borrows: autonomy is a design decision, not a capability consequence; and the ladder's dynamic distinctions — control transfer, consultation triggers, customizable approval triggers, takeover, emergency stop — which the orchestration row must carry as movement conditions, not lose in a static state label. What it adds: the observation that an agent's resting autonomy level decomposes into this framework's existing vocabulary — the boundary state of the orchestration row plus the control stacks of the execution rows — so no separate autonomy taxonomy is needed inside a map.

## Personas as versioned hypotheses

The "treat personas as hypotheses with invalidation conditions" framing is from Lean UX.

- Gothelf, J. (2013). *Lean UX: Applying Lean Principles to Improve User Experience.* O'Reilly. Proto-personas and assumption-driven persona work.
- Ries, E. (2011). *The Lean Startup.* Crown Business. Hypothesis-driven product development.
- Torres, T. (2021). *Continuous Discovery Habits.* Product Talk LLC. Assumption mapping in product discovery.

What this framework borrows: proto-persona discipline. What it doesn't claim: novelty for treating personas as falsifiable.

## Evidence grading and provenance

The seven evidence labels (`observed`, `interview_derived`, `telemetry_derived`, `artifact_derived`, `inferred`, `ai_generated_hypothesis`, `unvalidated`) draw on standard research provenance practice.

- Guyatt, G., et al. (2008). GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. *BMJ*, 336(7650), 924–926. Standard evidence-grading framework in medicine.
- Miles, M. B., & Huberman, A. M. (1994). *Qualitative Data Analysis* (2nd ed.). Sage. Source typing in qualitative research.
- Glaser, B. G., & Strauss, A. L. (1967). *The Discovery of Grounded Theory: Strategies for Qualitative Research.* Aldine. Origin of theoretical saturation: new interviews stop yielding new themes. Referenced by the Stakeholder Coverage template.

What this framework borrows: the discipline of attaching provenance to every claim. What it adds, for AI-assisted research: the explicit `ai_generated_hypothesis` label, because synthetic outputs are easy to mistake for findings if not labeled. This label is the only genuinely additive item in the evidence taxonomy.

## What is genuinely additive

The framework integrates the above. It does not invent anything large. The narrowly additive contributions are:

1. The **`ai_generated_hypothesis` evidence label** as a first-class category, useful when AI is part of the research pipeline.
2. The **"old layout trap" articulation** — sharper than generic service blueprinting for AI contexts because it names the specific failure mode of inserting AI into preserved human-era workflows.
3. The **Exception handler** and **Governance owner** roles in the role taxonomy, which extend RACI/RAPID for systems that generate exceptions and policy questions at scale.
4. The **integration packaging itself** — one map that connects boundary decisions, trust requirements, work-architecture redesign, evals, telemetry, release gates, and persona views, scoped for AI product teams.
5. The **durable ambiguity stance** — applying option-preserving / real-options reasoning to AI-product boundary decisions specifically.
6. The **Oversight viability gate** — packaging the ironies-of-automation, crumple-zone, and review-capacity findings as release-blocking checks rather than background reading.
7. The **orchestration-row move** — expressing agent autonomy levels inside the existing three-state vocabulary by mapping planning as a responsibility unit, instead of adding an autonomy taxonomy.

Items 1–3 are small extensions of existing frameworks. Items 4–5 are operational glue and stance, not new theory. Items 6–7 are compressions of existing literature into gate checks and mapping moves.

## What this framework does not claim

- It does not replace personas, JTBD, journey mapping, service design, or any existing user-research method.
- It does not introduce a new automation taxonomy or trust theory.
- It does not propose a new research method.
- It does not justify higher automation; the goal is calibrated, evidence-backed, accountable boundary movement.
- It does not generate or substitute for evidence; synthetic outputs are hypotheses until validated.
