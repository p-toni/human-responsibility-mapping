# Illustrative Synthetic Examples

The files in this directory are **synthetic worked examples**, not research outputs. They exist to show the shape of a Human Responsibility Snapshot in different domains — they do not document real teams, tools, tickets, or interviews.

Per the framework's evidence policy, every claim in every file here carries the evidence label `ai_generated_hypothesis`. A real map for your team replaces these with `observed`, `interview_derived`, `telemetry_derived`, or `artifact_derived` claims grounded in your actual research.

## What's here

| File | Domain | Why it's included |
|---|---|---|
| `customer-support.md` | Knowledge-work IC, mostly linear ticket pipeline | Common starting case for AI-assisted draft + bounded action |
| `customer-support-full-map.md` | Knowledge-work team, full support workflow | Complete synthetic deliverable showing boundaries, evidence, stakeholder coverage, evals, telemetry, and release gate |
| `security.md` | Knowledge-work IC, exploratory + agentic | Demonstrates `policy-governed` + `rollback-required` control modes for an AI-executed boundary |
| `icu-bedside-nursing.md` | Embodied, multi-patient, safety-critical | Stress-tests the framework on non-knowledge work where naive automation harms (alarm fatigue) and accountability is legally fixed |

The ICU example is included to show where the framework's default assumptions (decomposable knowledge work, AI as assistant, identifiable single role per responsibility) break or invert. If your domain looks more like the ICU example than like customer-support, expect to spend more time on the durable-ambiguity and accountability facets and less on the movement-condition facet.

## Read with caution

Anyone reading or quoting these files should treat them as the framework's *own dogfooding* — illustrative scaffolding for a method, not evidence about the domains. If you find rows you want to use in a real document, run the framework against your own team and replace the labels with real evidence.
