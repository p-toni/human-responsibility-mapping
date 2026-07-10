# Changelog

## v0.4.0

Theme: the v0.3 release rule gated the AI side of every boundary and the paperwork side of accountability; it never checked whether the retained human role was performable, whether boundaries compose safely, or whether the evidence survives a model upgrade. v0.4 closes those gaps.

### Added

- **Oversight viability** group in the SKILL.md release rule: review capacity budgeted at peak load with a stated detection target, accountable owner passes an authority/information/time/skill test, independent challenge and affected-party recourse for high-impact moves, skill-retention plan where the move erodes practice, AI-only paths enumerated with hazard-commensurate controls.
- `references/oversight-viability.md`: detection-target sample sizing (rule of three, Hanley & Lippman-Hand 1983), risk stratification, peak-not-average capacity budgeting (UK HSE workload guidance), intervention SLAs, utilization headroom, attention budgets for AI-initiated work, skill retention (Bainbridge's ironies of automation), moral-crumple-zone test plus automation-bias countermeasures and institutional oversight for high-impact moves (Green 2022's remedy), Goodhart-proofing rules for boundary telemetry (never use it for individual performance management; triangulate; watch denominators; expect instrument decay), and the residue problem (read "Human still owns" as a job description).
- `references/agentic-work.md`: orchestration mapped as its own responsibility row instead of a fourth boundary state (published agent-autonomy levels decompose into the orchestration row's state plus execution-row control stacks), control-transfer mechanics as movement conditions (takeover, consultation triggers, approval triggers, emergency stop — preserving Feng et al.'s dynamic distinctions), AI-as-reviewer rules (own row, judge-validation eval, accountability chains terminate in humans), AI-to-AI handoff seams, AI-only path composition analysis with typed controls (preventive / containment / corrective / detective) proportionate to hazard class, and system-change revalidation with pinned model/prompt/tool/corpus versions.
- Templates: **Boundary decision record** (ADR for boundary moves, with a dissent field), **Oversight capacity check** (risk-stratified, detection-target sample sizing, peak-load budgeting, utilization headroom), and **AI-only path table** (hazard class, typed controls, and the rule that irreversible outcomes forbid detective-only controls) in `references/templates.md`. The **System release gate** template gains the Oversight viability section it was missing and now points to the ambiguity-aware checks and the decision record.
- Control modes became **control stacks**: composable (e.g. `policy-governed` + `rollback-required`), categorized (authorization / runtime constraint / review / recoverability), and recorded for the *current* state as well as the target — a currently AI-executed boundary keeps its controls in the map even mid-move.
- `examples/illustrative/customer-support-boundary-decision-record.md`: a worked decision record where the acknowledgement boundary move passes every v0.3 check and is rejected on oversight viability (review capacity 3 h/week against an 8 h/week sampling load, no skill-retention plan, uncontrolled AI-only path).
- `schemas/human-responsibility-map.schema.json`: formal JSON Schema (draft 2020-12) for `schema_version` 0.4 — typed responsibilities, claims, gate checks (`check` / `status` / `evidence` / `owner`), typed path controls, and decision records.
- `scripts/validate_map.py`: fail-closed validator — version dispatch (unknown `schema_version` rejected, never guessed), JSON Schema structural validation (malformed input rejected without crashes), then semantic cross-field rules: control stacks must be non-empty exactly when a state is AI-executed (current *and* target), gate decision `move` requires every check `pass`/`not_applicable`-with-evidence plus a signed decision record (`do_not_move` also requires the record), irreversible AI-only paths are rejected with detective-only controls, and AI-executed boundaries require pinned `system_dependencies` and a declared `ai_only_paths` list.
- `tests/test_validate_map.py`: 30 adversarial tests — gamed gates (empty sections + `decision: move`), fake `system_dependencies`, `ai_only_paths` as prose, missing current controls on a currently-executed boundary, garbage schema versions, and malformed structures that previously crashed.
- `schemas/agent-context-pack.example.yaml`: `system_dependencies` version pinning, gate checks with per-check status and evidence, `current_controls`/`target_controls` stacks, `ai_only_paths`, `decision_records`; `schema_version` 0.4; gate decision normalized to the move / do_not_move / validate_further enum.
- Prior art: Bainbridge 1983, Elish 2019, Green 2022, Santoni de Sio & van den Hoven 2018, Strathern 1997, Shneiderman 2022, EU AI Act Article 14, NIST AI RMF, Leveson 2011, Feng/McDonald/Zhang 2025, Shavit et al. 2023, Mitchell et al. 2025. Additive-contributions list extended with the oversight-viability gate packaging and the orchestration-row move.
- `Map maintenance` section in `references/core-concepts.md`: every map names an owner, a home, refresh triggers (behavioral and system-change), and a decision history.
- Trigger-eval queries 13–14 (agent-autonomy should-trigger, agent-engineering should-not-trigger).

### Changed

- SKILL.md release rule: capability check now requires subgroup coverage; durable-ambiguity checks now include system-change refresh triggers; failing oversight viability means "redesign the human role," not "move and monitor"; every decision produces a Boundary Decision Record.
- SKILL.md control-mode watch-out extended: override rate is Goodhart-vulnerable, and human-review control modes must be capacity-budgeted up front, not just monitored for override collapse after the fact.
- SKILL.md special work shapes: agentic systems map `plan and sequence the work` as its own row; AI reviewers get their own row and eval.
- SKILL.md description: added "how much autonomy should our agent have?" and human-in-the-loop/oversight-design trigger phrases (dropped "sales" to stay under the 1024-char loader limit; 982 chars). **Committed eval baselines predate this description — rerun the canonical harness before citing trigger numbers.** `evals/README.md` and the README now label the committed results and their interpretation as a v0.3.7 baseline; no v0.4 trigger numbers exist yet.
- Minimum snapshot template (SKILL.md and `references/templates.md`) gains the evidence-label column the evidence policy always implied; templates.md snapshot gains the missing Stakeholder coverage heading, aligning it with SKILL.md.
- `examples/illustrative/customer-support-full-map.md`: added AI-only path analysis and an Oversight Viability section to the release gate; linked the new decision record.
- `examples/illustrative/icu-bedside-nursing.md`: alarm fatigue cross-linked as the clinical extreme of the general attention-budget rule.

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
