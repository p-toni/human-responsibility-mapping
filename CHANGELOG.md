# Changelog

## Unreleased

### Fixed

- Made `SKILL.md` frontmatter valid YAML by converting the long description to a folded scalar.
- Shortened the `SKILL.md` description to satisfy skill validator length limits.
- Fixed `schemas/agent-context-pack.example.yaml` so `control_mode` is only populated for AI-executed boundaries.
- Added a repo-local trigger eval runner and replaced the invalid eval reproduction command.

### Changed

- Clarified that the skill is portable across Claude Code, Codex, and other systems that can load `SKILL.md`-style skills.

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
