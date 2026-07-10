#!/usr/bin/env python3
"""Structural linter for machine-readable Human Responsibility Maps.

Checks the cross-field rules that SKILL.md states in prose, so maps kept in a
repo can be linted in CI:

- boundary states, control modes, evidence labels, and release-gate decisions
  come from the fixed vocabularies
- control_mode is set when a boundary's target state is AI-executed, and unset
  when neither state is AI-executed
- every responsibility names an accountability owner
- any map with an AI-executed boundary pins system_dependencies and declares
  ai_only_paths (an empty list is a claim; a missing key is a gap)

Usage:
    uv run --with pyyaml scripts/validate_map.py schemas/agent-context-pack.example.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

BOUNDARY_STATES = {"Human-owned", "AI-assisted", "AI-executed"}
CONTROL_MODES = {
    "approve-before-action",
    "policy-governed",
    "sampling-review",
    "rollback-required",
}
EVIDENCE_LABELS = {
    "observed",
    "interview_derived",
    "telemetry_derived",
    "artifact_derived",
    "inferred",
    "ai_generated_hypothesis",
    "unvalidated",
}
GATE_DECISIONS = {"move", "do_not_move", "validate_further"}
RELEASE_GATE_SECTIONS = {
    "capability",
    "trust_and_evidence",
    "accountability",
    "oversight_viability",
    "evals",
    "telemetry",
}


def check_responsibility(unit: dict, where: str) -> list[str]:
    """Validate one responsibility unit and return finding strings."""
    findings: list[str] = []
    boundary = unit.get("boundary")
    if not isinstance(boundary, dict):
        return [f"{where}: missing boundary block"]

    states = {}
    for field in ("current_state", "target_state"):
        state = boundary.get(field)
        states[field] = state
        if state not in BOUNDARY_STATES:
            findings.append(
                f"{where}: boundary.{field} {state!r} is not one of {sorted(BOUNDARY_STATES)}"
            )

    control_mode = boundary.get("control_mode")
    executed = "AI-executed" in (states["current_state"], states["target_state"])
    if states["target_state"] == "AI-executed" and control_mode is None:
        findings.append(f"{where}: target state is AI-executed but control_mode is null")
    if not executed and control_mode is not None:
        findings.append(
            f"{where}: control_mode {control_mode!r} set but neither state is AI-executed"
        )
    if control_mode is not None and control_mode not in CONTROL_MODES:
        findings.append(
            f"{where}: control_mode {control_mode!r} is not one of {sorted(CONTROL_MODES)}"
        )

    if not boundary.get("accountability_owner"):
        findings.append(f"{where}: boundary.accountability_owner is missing or empty")

    for index, claim in enumerate(unit.get("claims") or []):
        label = claim.get("evidence_label")
        if label not in EVIDENCE_LABELS:
            findings.append(
                f"{where}.claims[{index}]: evidence_label {label!r} "
                f"is not one of {sorted(EVIDENCE_LABELS)}"
            )
    return findings


def check_map(data: dict, path: Path) -> list[str]:
    """Validate one parsed map and return finding strings."""
    findings: list[str] = []
    responsibilities = data.get("responsibilities")
    if not responsibilities:
        findings.append(f"{path}: no responsibilities defined")
        responsibilities = []

    any_executed = False
    for index, unit in enumerate(responsibilities):
        name = unit.get("name") or f"[{index}]"
        where = f"{path}: responsibilities.{name}"
        findings.extend(check_responsibility(unit, where))
        boundary = unit.get("boundary") or {}
        if "AI-executed" in (boundary.get("current_state"), boundary.get("target_state")):
            any_executed = True

    gate = data.get("release_gate")
    if isinstance(gate, dict):
        decision = gate.get("decision")
        if decision not in GATE_DECISIONS:
            findings.append(
                f"{path}: release_gate.decision {decision!r} is not one of {sorted(GATE_DECISIONS)}"
            )
        for section in sorted(RELEASE_GATE_SECTIONS - set(gate)):
            findings.append(f"{path}: release_gate is missing the {section!r} section")
    else:
        findings.append(f"{path}: missing release_gate block")

    if any_executed:
        if not data.get("system_dependencies"):
            findings.append(
                f"{path}: AI-executed boundary present but system_dependencies is missing "
                "(pin model/prompt/tool/corpus versions)"
            )
        if data.get("ai_only_paths") is None:
            findings.append(
                f"{path}: AI-executed boundary present but ai_only_paths is missing "
                "(declare [] only after tracing the work architecture)"
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("maps", nargs="+", type=Path, help="map YAML files to validate")
    args = parser.parse_args()

    failures = 0
    for path in args.maps:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as error:
            print(f"{path}: cannot parse: {error}", file=sys.stderr)
            failures += 1
            continue
        if not isinstance(data, dict):
            print(f"{path}: top level is not a mapping", file=sys.stderr)
            failures += 1
            continue

        findings = check_map(data, path)
        if findings:
            failures += 1
            for finding in findings:
                print(finding, file=sys.stderr)
        else:
            print(f"{path}: ok")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
