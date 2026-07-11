# Human Responsibility Mapping

*A practical framework for mapping AI-era work, responsibility, boundaries, trust, evals, telemetry, and persona views.*

Human Responsibility Mapping helps teams decide what AI should do, what humans should retain, what evidence is required, and how the surrounding work architecture should change.

This is an **integration framework**, not a claim of new theory. It combines established ideas from automation levels, trust in automation, responsibility/accountability mapping, service blueprinting, technology probes, Lean UX, and product eval practice into one practical operating artifact for AI product teams.

The skill is packaged for OpenAI Codex with `SKILL.md` trigger metadata and `agents/openai.yaml` UI metadata. Its Markdown workflow is runtime-neutral and can also be loaded by other agents that support `SKILL.md`. Implicit triggering varies by runtime and model; explicit `$human-responsibility-mapping` invocation is the portable, reliable path.

## What you produce

A Human Responsibility Map usually includes:

- Current work architecture
- Responsibility boundaries
- Evidence ledger
- Stakeholder coverage
- Trust / accountability requirements
- Eval plan
- Telemetry plan
- Release gate
- AI-only path analysis
- Boundary decision records

For a complete synthetic example, see [`examples/illustrative/customer-support-full-map.md`](examples/illustrative/customer-support-full-map.md), including its deterministic visual summary [`customer-support-boundary-map.svg`](examples/illustrative/customer-support-boundary-map.svg).

## What changed in v0.4

v0.4 answers the strongest critique of v0.3: the release rule checked the AI side of every boundary and the paperwork side of accountability, but never whether the humans could actually do the part the map said they retained.

- Added the **Oversight viability** group to the release rule: review capacity budgeted at peak with a stated detection target (rule-of-three sample sizing, not "we review 10%"), accountable owners need authority/information/time/skill (not accountability in name only), high-impact moves need independent challenge and affected-party recourse, retained skills need retention plans (ironies of automation), and AI-only paths need hazard-commensurate controls — detective-only is insufficient where harm is irreversible.
- Added `references/oversight-viability.md` — capacity math, skill retention, moral crumple zones, Goodhart-proofing the map's own telemetry, and the residue problem (read the "Human still owns" column as a job description).
- Added `references/agentic-work.md` — orchestration as a responsibility row (agent autonomy levels expressed in the existing three-state vocabulary), AI reviewers get their own row and eval, accountability chains terminate in humans, AI-to-AI handoffs, and system-change revalidation (a boundary validated on model N is unvalidated on model N+1).
- Added **Boundary Decision Records** (ADRs for boundary moves), an **oversight capacity check**, and an **AI-only path table** to the templates — plus a worked decision record where a move passes every v0.3 check and is rejected on oversight viability.
- Made `schemas/` real: a formal JSON Schema (`schemas/human-responsibility-map.schema.json`, versioned, fail-closed on unknown versions) plus `scripts/validate_map.py`, which validates structure and then enforces the semantic rules — control stacks must match boundary states, gate decision `move` requires every check to pass with a signed decision record, and irreversible AI-only paths cannot rely on detective-only controls. Adversarial tests in `tests/`.
- Added `agents/openai.yaml` so Codex can display and explicitly invoke the skill through `$human-responsibility-mapping`; validated the package with OpenAI's `skill-creator` tooling and forward-tested it in Codex.
- Extended prior art with the oversight-limits literature (Bainbridge 1983, Elish 2019, Green 2022, Santoni de Sio & van den Hoven 2018), systems safety (Leveson 2011), agent-autonomy frameworks (Feng, McDonald & Zhang 2025; Shavit et al. 2023; Mitchell et al. 2025), and the regulatory bar (EU AI Act Article 14, NIST AI RMF).
- Subgroup parity joined the capability checks; the minimum snapshot now carries the evidence-label column it always should have had.

## What changed in v0.3

- Added portable Skill YAML frontmatter and explicit resources so bundled files are not orphaned.
- Rewrote `SKILL.md` as operational instructions.
- Collapsed overlapping concepts (delegation, AI exposure, trust requirement, accountability) into one **Boundary** model with three facets.
- Simplified delegation into three boundary states with four control modes for AI-executed work.
- Repositioned the framework as integration, not new theory.
- Added `references/prior-art.md` with proper citations for the 16 works the framework draws on.
- Marked examples as **illustrative synthetic examples** with per-claim evidence labels and a directory README.
- Added a deliberate stress-test example (ICU bedside nursing) outside knowledge-work defaults.
- Added missing operational templates: evidence ledger, trust profile, eval plan, telemetry plan, and system release gate (with sectional structure mirrored in the schema).
- Reorganized the release rule by Boundary facet, removing leftover v0.2 vocabulary leaks.

## Are we still talking about personas?

Yes, but personas are derived views, not the source artifact.

The source artifact is the **Human Responsibility Map**. Derived persona artifacts include persona snapshots, role evolution narratives, trust profiles, adoption narratives, boundary cards, design requirements, eval scenarios, and telemetry requirements.

Classic personas can and often do capture behavior, goals, context, and motivations. Human Responsibility Mapping extends persona work for situations where AI changes the work itself.

> Classic personas describe users. AI-era personas are role-responsibility views over changing work.

## Durable ambiguity

This framework assumes uncertainty does not disappear once a map is created.

In AI-native work, new capability often creates new uncertainty: new work architectures, new user expectations, new trust boundaries, and new accountability questions.

Use Human Responsibility Mapping as an **option-preserving instrument**, not a prediction engine.

Operational rule:

> Prefer boundary moves that preserve optionality.

That means favor reversible changes, human override, staged delegation, evals before autonomy, telemetry before broad rollout, multiple hypotheses, contradiction logs, and refresh triggers.

See `references/durable-ambiguity.md` for full guidance.

---

## Core model

```text
Work domain -> Current work architecture -> Responsibility units -> Boundary conditions -> Product/eval/telemetry decisions -> Observed behavior -> Map refresh
```

## When to use this

Use Human Responsibility Mapping when a team asks:

- What should AI do versus humans?
- How should responsibility change as AI improves?
- Where should humans stay in control?
- What evidence would make this safe or trustworthy?
- How should incident response/support/security/legal/ops workflows change with AI?
- What evals and telemetry are needed before launch?
- How should a journey map, service blueprint, or RACI change because of AI?
- How do we avoid using AI only to make old workflows faster?

Do not use it when you only need a marketing persona, a stable segmentation model, or a simple feature improvement.

## Repository structure

```text
human-responsibility-mapping/
  README.md
  SKILL.md
  agents/
    openai.yaml
  LICENSE
  CONTRIBUTING.md
  CHANGELOG.md
  references/
    core-concepts.md
    prior-art.md
    application-modes.md
    durable-ambiguity.md
    oversight-viability.md
    agentic-work.md
    templates.md
    workshop.md
  examples/
    illustrative/
      README.md
      customer-support.md
      customer-support-full-map.md
      customer-support-boundary-map.svg
      customer-support-boundary-decision-record.md
      security.md
      icu-bedside-nursing.md
  schemas/
    human-responsibility-map.schema.json
    agent-context-pack.example.yaml
  scripts/
    description_self_report.py
    validate_map.py
  tests/
    test_validate_map.py
  evals/
    openai-forward-test.json
    trigger-eval.json
    trigger-eval-results-haiku-4.5.json
    trigger-eval-results-sonnet-4.6.json
```

`SKILL.md` is the runtime skill. The `references/` files are loaded on demand.

## Prior-art stance

This framework is not presented as new theory. It integrates and operationalizes ideas adjacent to supervisory control, levels of automation, trust in automation, service blueprinting, RACI/RAPID-style responsibility mapping, technology probes, Lean UX, and AI eval/telemetry practice.

The intended contribution is practical glue:

> one map that connects boundary decisions → trust requirements → evals → telemetry → release gates for AI product teams.

## Quick start

Ask:

```text
Apply Human Responsibility Mapping to [WORK DOMAIN].
Start with a lightweight snapshot.
Label all unsupported claims as unvalidated.
Do not recommend higher automation unless the release rule is satisfied.
```

## Triggering and explicit invocation

In OpenAI Codex, invoke the skill explicitly when you need the structured workflow:

```text
Use $human-responsibility-mapping to map [WORK DOMAIN].
```

`agents/openai.yaml` permits implicit invocation, but the repository does not yet claim a Codex implicit-trigger rate. OpenAI compatibility is checked with `skill-creator` validation and fresh Codex forward tests. The committed Haiku 4.5 and Sonnet 4.6 trigger results are Anthropic-specific evidence and should not be extrapolated to OpenAI models. See `evals/README.md`.

## License

MIT. See `LICENSE`.
