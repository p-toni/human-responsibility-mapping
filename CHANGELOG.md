# Changelog

## v0.3.8

### Added

- `examples/illustrative/customer-support-boundary-map.svg`, a deterministic visual summary of the full customer-support map.
- Embedded the visual map from `examples/illustrative/customer-support-full-map.md` and linked it from README / examples index.

## v0.3.7

### Added

- `examples/illustrative/customer-support-full-map.md`, a complete synthetic deliverable showing the finished artifact shape across work architecture, responsibility boundaries, stakeholder coverage, evidence, trust/accountability, evals, telemetry, release gate, and contradiction signals.
- README "What you produce" section linking the framework to the concrete deliverables a team should expect.

### Changed

- Reframed `SKILL.md` and the description as **deliverable-first**. Description opens with "Produces a **Human Responsibility Snapshot** — a structured Markdown artifact..." rather than "Use this skill whenever a user asks…". The hypothesis: skill loaders weight artifact-producing skills higher for triggering than advisory skills, because Claude can answer advisory questions by reasoning but can't fabricate a structured template. Concrete trigger phrases preserved in the description (folded scalar, under 1024 chars).
- SKILL.md opening line now leads with "**produce a Human Responsibility Snapshot or Map**" rather than "map how AI changes work".
- Added explicit "Default output: a filled Snapshot using the Minimum snapshot template" instruction at the end of Core instruction.
- Expanded `references/workshop.md` into a 60-minute, deliverable-first workshop with inputs, first three deliverables, and a "done means" checklist.
- All conceptual content (Boundary model, control modes, evidence labels, release rule, references, templates) unchanged. The framework's substance is the same; only the default mode of output shifted from "discuss" to "produce".

### Validation

- `SKILL.md` frontmatter remains valid YAML and the description remains under the 1024-character loader limit after the deliverable-first rewrite.
- Canonical trigger evals should be rerun before publishing a release that changes the description. The committed `evals/trigger-eval-results-*.json` files remain the existing baseline unless updated in the same release.

## v0.3.5

### Added

- `Stakeholder coverage` template in `references/templates.md` to track sampled roles with `unsampled` / `initial` / `theme-stable` / `n/a` status.
- `Stakeholder coverage` heading in the SKILL.md Minimum Snapshot template.
- Multi-domain guidance in `references/application-modes.md` that keeps one map per domain, avoids adding a new Program Mode, and calls out vocabulary consistency plus coverage rollup as the framework-shaped cross-domain concerns.
- Glaser & Strauss 1967 citation in `references/prior-art.md` for the saturation framing used by the coverage template.

### Changed

- SKILL.md evidence guidance now asks agents to link claims to source artifacts where possible so evidence labels remain auditable.

## v0.3.4

### Fixed

- Kept the `SKILL.md` description as a YAML folded scalar (`>-`) for valid frontmatter, but restored the concrete trigger phrases ("what should AI do vs humans?", "what should we automate?", "who's accountable when the AI is wrong?", "what evals/telemetry/release gates do we need before launch?") that the v0.3.3 trigger eval showed were load-bearing for recall. v0.3.4 description is ~960 chars — within typical loader limits, with the recall signal intact.
- `schemas/agent-context-pack.example.yaml` — kept the `control_mode: null` correction for the AI-assisted boundary (control modes are only meaningful for AI-executed work, per SKILL.md).
- Renamed `scripts/run_eval.py` → `scripts/description_self_report.py` and clarified in its docstring + `evals/README.md` that it measures self-report (Claude-judges-its-own-description), which is a different methodology from the skill-creator harness that produced the committed result files. Both reproduction commands are now documented separately.

### Changed

- Hedged the portability framing in `README.md` and `SKILL.md`: the `SKILL.md` Markdown + YAML-frontmatter convention is from Claude Code / Anthropic Skills; other runtimes (e.g. Codex) can use it when configured to load that convention, but triggering reliability varies. Pointer to `evals/` added.

## v0.3.3

### Added

- `evals/` directory with trigger evaluation artifacts: 12-query test set (6 should-trigger bullseye, 6 should-not-trigger near-miss) plus per-query results for Haiku 4.5 and Sonnet 4.6.
- README "Triggering and explicit invocation" section documenting the eval result and the explicit-invocation pattern for advisory questions.

### Changed

- Rewrote the SKILL.md `description` to be more imperative ("Use this skill whenever ...") with concrete trigger phrases, after the first eval pass showed the original was undertriggering. Specificity is perfect (no false positives on adjacent topics); recall on advisory questions is structurally limited regardless of phrasing — some agents handle "how should we think about X" questions by reasoning rather than consulting a framework file.

## v0.3.2

### Fixed

- Removed duplicated "Durable ambiguity" sections from `SKILL.md`, `README.md`, `references/core-concepts.md`, and `references/prior-art.md`; canonical content lives in `references/durable-ambiguity.md`.
- Removed duplicated "Multiple Hypotheses" and "Ambiguity-Aware Release Checks" blocks in `references/templates.md`.
- Removed duplicated `references/durable-ambiguity.md` lines in `SKILL.md` resources list and in `README.md` repository-structure tree.
- Removed duplicated `## v0.3.1` block in this changelog.
- Fixed YAML duplicate-key bug for `durable_ambiguity` in `schemas/agent-context-pack.example.yaml`.

### Changed

- Rewrote `references/prior-art.md` with proper citations (author, year, title) for all 16 referenced works including Sheridan & Verplank 1978, Sheridan 1992, Parasuraman/Sheridan/Wickens 2000, Endsley & Kaber 1999, SAE J3016, Lee & See 2004, Hoff & Bashir 2015, Parasuraman & Riley 1997, Shostack 1984, Bitner/Ostrom/Morgan 2008, Rother & Shook 1998, SIPOC, Hutchinson et al. 2003, Kelley 1984, Gothelf 2013, Rogers & Blenko 2006, and GRADE (Guyatt et al. 2008). Named the four genuinely additive contributions explicitly.
- Added inline prior-art pointers in `SKILL.md` for boundary states, work architecture, and evidence labels.
- Rewrote the Release Rule to organize checks by Boundary facet (movement condition / accountability / durable ambiguity), removing the surviving v0.2 vocabulary leaks ("trust requirements", "human control") that the Boundary collapse was supposed to absorb.
- Compressed the six control modes to four: dropped `human-only` (contradicted "AI-executed"), folded `exception-review` into `policy-governed` (the policy defines exceptions). Added a watch-out for implicit boundary movement when override rates collapse.
- Reframed Work Architecture as a distinct lens (workflow flow) from Responsibility Units (workflow atoms), so they no longer appear redundant.
- Updated the schema's `release_gate` to use sectional structure (capability / trust_and_evidence / accountability / evals / telemetry / decision) matching the templates, instead of a flattened `required[]` array.
- Added the `what_changes` field to the schema's multiple-hypothesis structure to match `references/templates.md`.

### Added

- Per-claim `evidence_label` columns in both existing illustrative examples (`customer-support.md`, `security.md`) instead of a header-only disclaimer.
- `examples/illustrative/README.md` explaining what these files are and aren't.
- `examples/illustrative/icu-bedside-nursing.md` — a stress-test example outside white-collar IC knowledge work, deliberately chosen to break the framework's default assumptions (decomposable knowledge work, AI as assistant, identifiable single role per responsibility).

## v0.3.1

### Added

- `references/durable-ambiguity.md`.
- Durable Ambiguity principle: treat uncertainty as a durable operating condition, not a temporary gap.
- Option-preserving boundary movement rule.
- Multiple work-architecture hypotheses template.
- Ambiguity-aware release checks.
- Schema fields for durable ambiguity, multiple hypotheses, option-preserving rules, and contradiction signals.

### Changed

- README and SKILL now frame maps as option-preserving instruments, not prediction engines.
- Release rule now requires uncertainty identification, optionality preservation, contradiction signals, and refresh triggers.


## v0.3.0

### Added

- Portable Skill YAML frontmatter.
- Runtime resource pointers in `SKILL.md`.
- `references/` folder for progressive disclosure.
- Prior-art positioning.
- Boundary model with three facets: current line, movement condition, accountability.
- Three boundary states: Human-owned, AI-assisted, AI-executed.
- Control modes for AI-executed work.
- Evidence ledger, trust profile, eval plan, telemetry plan, system release gate templates.
- Granularity rule for responsibility units.
- Prioritization heuristic and closure criterion.
- Illustrative synthetic examples with explicit banners.
- Updated schema with evidence policy, control surfaces, and complete contradiction fields.

### Changed

- Rewrote `SKILL.md` as agent instructions rather than doctrine.
- Repositioned the framework as integration, not new theory.
- Collapsed overlapping concepts around AI exposure, delegation, trust, and accountability into Boundary.
- Moved long explanations into references.
- Simplified delegation/autonomy ladder.
- Tightened persona positioning: personas are derived views, not source artifacts.
