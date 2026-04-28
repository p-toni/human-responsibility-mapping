# Human Responsibility Mapping

*A practical framework for mapping AI-era work, responsibility, boundaries, trust, evals, telemetry, and persona views.*

Human Responsibility Mapping helps teams decide what AI should do, what humans should retain, what evidence is required, and how the surrounding work architecture should change.

This is an **integration framework**, not a claim of new theory. It combines established ideas from automation levels, trust in automation, responsibility/accountability mapping, service blueprinting, technology probes, Lean UX, and product eval practice into one practical operating artifact for AI product teams.

The skill is not Claude-only. `SKILL.md` is plain YAML frontmatter plus Markdown instructions, so Claude Code, Codex, and any other agent or runtime that can load `SKILL.md`-style skills should be able to use the same workflow. If a system does not auto-trigger the skill, invoke it explicitly by name.

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
  LICENSE
  CONTRIBUTING.md
  CHANGELOG.md
  references/
    core-concepts.md
    prior-art.md
    application-modes.md
    durable-ambiguity.md
    templates.md
    workshop.md
  examples/
    illustrative/
      README.md
      customer-support.md
      security.md
      icu-bedside-nursing.md
  schemas/
    agent-context-pack.example.yaml
  scripts/
    run_eval.py
  evals/
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

This skill auto-triggers reliably when you ask for a **deliverable** ("write a strategy memo about how AI changes our CSM org", "build me a release gate for our AI feature", "produce a Human Responsibility Snapshot for ..."). It can trigger less reliably on pure advisory questions ("how should we think about what AI does vs humans?") because some agents answer those directly without consulting a framework file.

If you want the skill's structured output on an advisory question, invoke it explicitly:

```text
Use the human-responsibility-mapping skill to think through [WORK DOMAIN].
```

See `evals/` for the trigger evaluation artifacts across Haiku 4.5 and Sonnet 4.6, including the 12-query test set and the per-query trigger rates. Specificity is perfect (no false positives on adjacent topics like marketing personas, plain RACI, or no-AI journey maps); recall is partial and structural.

## License

MIT. See `LICENSE`.
