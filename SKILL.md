---
name: human-responsibility-mapping
description: >-
  Produces a **Human Responsibility Snapshot** — a structured Markdown
  artifact mapping each responsibility in a workflow, who owns it today, what
  AI takes on next, the boundary state (human-owned / AI-assisted /
  AI-executed), the movement condition (evidence, eval, telemetry, or control
  needed to move it), and what stays human-owned. Use whenever a user asks
  how AI changes a workflow, role, RACI, service blueprint, journey,
  operating model, or strategy — including "what should AI do vs humans?",
  "what should we automate?", "who's accountable when the AI is wrong?", or
  "what evals, telemetry, or release gates do we need before launch?".
  Triggers on AI-assisted or agentic incident response, customer support,
  legal review, security/SOC triage, sales, ops, AI-era persona views, and
  operating-model memos about AI changing a team's work. Default output is
  the filled Snapshot table — not prose advice.
---

# Human Responsibility Mapping

Use this skill to **produce a Human Responsibility Snapshot or Map** — structured Markdown artifacts that show which responsibilities AI takes on, what humans retain, the evidence/control/accountability conditions required to move each boundary, and the product/eval/telemetry implications. The Snapshot (lightweight) is the default deliverable; the Map (Standard/Full mode) is the longer version.

This skill targets the Markdown + YAML-frontmatter convention used by Claude Code and Anthropic's Skills system. Other agent runtimes that load the same convention (e.g. Codex when configured to read `SKILL.md`) should apply the same workflow and guardrails. Triggering reliability varies across runtimes — see `evals/README.md`.

This is not a synthetic-persona generator. It is an integration framework for AI product teams. It produces AI-era persona views as one output, but the source artifact is a **Human Responsibility Map**.

## Core instruction

When a user asks how AI changes a workflow, role, journey, operating model, or strategy:

1. Start from the work, not from demographic personas.
2. Map the current work architecture.
3. Break the work into responsibility units.
4. Identify the human/AI boundary for each responsibility.
5. State the evidence, control, and accountability conditions required to move that boundary.
6. Translate the map into product requirements, evals, telemetry, and release gates.
7. Label evidence. Link sources where possible. Do not invent evidence.

**Default output: a filled Snapshot using the Minimum snapshot template below, populated from your responses to steps 1–7. Switch to prose discussion only if the user explicitly asks to discuss tradeoffs instead of producing the artifact.**

## Core model

```text
Work domain -> Current work architecture -> Responsibility units -> Boundary conditions -> Product/eval/telemetry decisions -> Observed behavior -> Map refresh
```

## Choose the smallest useful artifact

| Mode | Use when | Output |
|---|---|---|
| Lightweight | Early exploration, unclear fit, low-stakes work, creative/strategy work | Human Responsibility Snapshot |
| Standard | AI changes responsibility, trust, delegation, or workflow shape | Human Responsibility Map |
| Full | High-stakes, multi-role, agentic, regulated, safety-critical, or accountability-heavy systems | Full map + evidence ledger + eval plan + telemetry plan + release gate |

Default to lightweight unless the user asks for a full framework, PRD, eval plan, operating model, or high-stakes launch decision.

## Boundary model

Use one concept: **Boundary**.

A boundary has three facets:

| Facet | Question |
|---|---|
| Current line | What does the human own today, and what does AI do today? |
| Movement condition | What evidence, control, eval, telemetry, or policy would allow the line to move? |
| Accountability | Who remains responsible if the AI is wrong, incomplete, unsafe, or misused? |

Treat AI exposure, delegation, trust, and accountability as facets of the same boundary decision.

## Three boundary states

| State | AI role | Human role |
|---|---|---|
| Human-owned | AI absent or peripheral | Human performs and decides |
| AI-assisted | AI summarizes, suggests, ranks, drafts, or explains | Human chooses, edits, approves, decides |
| AI-executed | AI takes bounded action, routes, updates, or triggers work | Human gates, monitors, audits, or governs |

For AI-executed work, specify one control mode:

| Control mode | Meaning |
|---|---|
| `approve-before-action` | Human approves each action before it executes |
| `policy-governed` | AI acts within bounded policy; humans review only policy exceptions or anomalies |
| `sampling-review` | AI acts; humans review a sample post-hoc for QA and drift |
| `rollback-required` | AI acts; system must support fast rollback if outcomes are wrong |

These compress a longer literature on supervisory control and levels of automation (Sheridan 1992; Parasuraman, Sheridan & Wickens 2000). The watch-out is the soft edge between AI-assisted and AI-executed: a "draft humans always accept" is operationally executed under `approve-before-action`. If override rates fall below ~5%, treat the boundary as having moved whether the design says so or not.

Do not imply that more automation is better. The right boundary depends on risk, reversibility, evidence quality, regulation, user trust, accountability, and failure blast radius.

For prior-art context on these states and modes, see `references/prior-art.md`.

## Durable ambiguity

Treat uncertainty as a durable operating condition, not a temporary gap to eliminate.

When model capability, user behavior, workflow shape, or accountability is unclear:

1. Preserve multiple plausible work-architecture hypotheses.
2. Prefer reversible boundary moves.
3. Add human override or escalation.
4. Add telemetry before broad rollout.
5. Define contradiction signals.
6. Refresh the map when reality disagrees.

Use this rule:

> Prefer boundary moves that preserve optionality.

Do not present the map as a prediction. Present it as an option-preserving instrument for acting responsibly under uncertainty.

For deeper guidance — multiple-hypothesis tables, option-preserving checks, contradiction patterns — load `references/durable-ambiguity.md`.

---

## Work architecture

Work architecture and responsibility units are two different lenses on the same workflow. Responsibility units name what each atomic step *does* (observe, draft, decide). Work architecture names how the steps *flow*: the sequence, queues, handoffs, reviews, approvals, artifacts, feedback loops, control surfaces, and metrics that connect them. Map both — boundary moves often change the flow without changing the atoms, or change the atoms without changing the flow.

Before assigning tasks to AI, ask what old work layout is being preserved. Then ask what becomes continuous instead of batch, exception-based instead of universally reviewed, live instead of static, or evidence-backed instead of opinion-backed.

Old layout trap:

> If the workflow diagram looks the same after AI, the team may only be making old work faster.

This lens draws on service blueprinting (Shostack 1984; Bitner, Ostrom & Morgan 2008) and current-state / future-state value stream mapping (Rother & Shook 1998). The "old layout trap" is the framework's articulation of Hammer & Champy's BPR principle for AI contexts.

## Evidence labels

Attach an evidence label to every important claim.

| Label | Meaning |
|---|---|
| observed | Directly seen in behavior or workflow shadowing |
| interview_derived | Stated by users |
| telemetry_derived | Supported by usage/product data |
| artifact_derived | Supported by tickets, docs, logs, reports, traces, or decisions |
| inferred | Reasoned from evidence but not directly observed |
| ai_generated_hypothesis | Generated by AI and not validated |
| unvalidated | Important but unsupported |

If evidence is missing, label the claim `unvalidated`. Never upgrade confidence without evidence.

Where possible, link each claim to its source artifact: interview note URL, ticket ID, telemetry query, document anchor, trace, or decision record. A label without a source is a self-asserted provenance claim, not an auditable one.

This taxonomy is standard research provenance (cf. GRADE in medicine, Guyatt et al. 2008; qualitative source typing, Miles & Huberman 1994) plus the explicit `ai_generated_hypothesis` label, which is the only genuinely additive item — useful when AI is part of the research pipeline because synthetic outputs are easy to mistake for findings.

## Minimum snapshot

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
## Stakeholder coverage
```

## Special work shapes

- Dynamic objective work: map loops (`observe -> hypothesize -> act -> evaluate -> reframe -> continue/stop/escalate`) instead of linear steps.
- System-facing domains: if persona language feels forced, map operators, control surfaces, system states, failure modes, evidence, and accountability.
- Creative work: protect authorship, taste, and meaning boundaries; use lightweight mode.
- Strategy artifacts: use a lightweight strategy snapshot unless tied to real product, eval, telemetry, or operating-model changes.

## Release rule

Do not recommend moving a boundary unless these are true. The checks group by Boundary facet and one ambiguity stance.

```text
Movement condition (does the evidence support the move?)
[ ] Capability is demonstrated in realistic scenarios.
[ ] Failure modes are understood and documented.
[ ] Evidence is inspectable.
[ ] Required evals exist and pass.
[ ] Telemetry is in place to detect adoption, override, misuse, rejection, and drift.

Accountability (does someone own the consequence?)
[ ] Accountable owner is explicit.
[ ] Escalation path exists.
[ ] Human-only decisions inside the boundary are preserved.

Durable ambiguity (have we preserved optionality?)
[ ] We have identified what remains uncertain.
[ ] The proposed change preserves reversibility where possible.
[ ] Contradiction signals and refresh triggers are defined.
```

If not all true, keep the current boundary or recommend a validation plan.

## Resources

Load supporting files only when needed:

- `references/core-concepts.md` — definitions, boundary model, granularity, prioritization, closure.
- `references/prior-art.md` — prior-art positioning and honest contribution.
- `references/application-modes.md` — lightweight/standard/full modes and special work shapes.
- `references/durable-ambiguity.md` — ambiguity-aware mapping, optionality, multiple hypotheses, and contradiction handling.
- `references/templates.md` — evidence ledger, trust profile, eval plan, telemetry plan, release gates.
- `references/workshop.md` — workshop flow.
- `examples/illustrative/README.md` — what these examples are and aren't.
- `examples/illustrative/customer-support.md` — knowledge-work IC, linear pipeline.
- `examples/illustrative/customer-support-full-map.md` — complete synthetic map with boundaries, evidence, evals, telemetry, release gate.
- `examples/illustrative/customer-support-boundary-map.svg` — deterministic visual summary of the customer-support full map.
- `examples/illustrative/security.md` — knowledge-work IC, exploratory + agentic.
- `examples/illustrative/icu-bedside-nursing.md` — embodied, multi-patient, safety-critical (stress-tests the framework where its defaults break).
- `schemas/agent-context-pack.example.yaml` — machine-readable example.
- `evals/` — trigger evaluation artifacts (test set + per-model results).

## Guardrails

- Do not present synthetic examples as research.
- Do not strip evidence labels from downstream artifacts.
- Do not treat personas as the source of truth.
- Do not maximize automation by default.
- Do not hide accountability behind AI.
- Do not use the framework to profile private individual traits or manipulate adoption.
