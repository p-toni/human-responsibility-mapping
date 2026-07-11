#!/usr/bin/env python3
"""Fail-closed validator for machine-readable Human Responsibility Maps.

Two layers:

1. Structural: the map must declare a supported schema_version and validate
   against the matching JSON Schema in schemas/ (types, enums, required
   fields). Unknown versions and malformed structures are rejected, never
   guessed at.
2. Semantic: cross-field rules that SKILL.md states in prose:
   - an AI-executed state (current or target) requires a non-empty control
     stack for that state; non-AI-executed states must not carry controls
   - any AI-executed boundary requires pinned system_dependencies and a
     declared ai_only_paths list (empty is a claim; missing is a gap)
   - ai_only_paths with irreversible worst outcomes need at least one
     preventive or containment control — detective-only is insufficient
   - release_gate.decision "move" requires every gate check to be pass or
     not_applicable (with evidence for not_applicable)
   - decisions "move" and "do_not_move" require a matching decision record
     with an accountable-owner sign-off

Usage:
    uv run --with pyyaml --with jsonschema scripts/validate_map.py \
        schemas/agent-context-pack.example.yaml

Tests (adversarial cases included):
    uv run --with pyyaml --with jsonschema --with pytest pytest -q tests/
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import jsonschema
import yaml

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schemas"
SUPPORTED_VERSIONS = {"0.4": SCHEMA_DIR / "human-responsibility-map.schema.json"}
EXECUTED = "AI-executed"


def structural_findings(data: dict, where: str) -> list[str]:
    """Dispatch on schema_version and validate against the JSON Schema."""
    version = data.get("schema_version")
    schema_path = SUPPORTED_VERSIONS.get(version)
    if schema_path is None:
        supported = ", ".join(sorted(SUPPORTED_VERSIONS))
        return [f"{where}: unsupported schema_version {version!r} (supported: {supported})"]

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    findings = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        location = "/".join(str(part) for part in error.absolute_path) or "(root)"
        findings.append(f"{where}: {location}: {error.message}")
    return findings


def control_findings(unit: dict, where: str) -> list[str]:
    """Check that control stacks match boundary states for one responsibility."""
    findings = []
    boundary = unit["boundary"]
    for state_field, controls_field in (
        ("current_state", "current_controls"),
        ("target_state", "target_controls"),
    ):
        state = boundary[state_field]
        controls = boundary.get(controls_field) or []
        if state == EXECUTED and not controls:
            findings.append(
                f"{where}: {state_field} is AI-executed but {controls_field} is empty "
                "(specify the control stack governing execution)"
            )
        if state != EXECUTED and controls:
            findings.append(
                f"{where}: {controls_field} set but {state_field} is {state!r} "
                "(controls only apply to AI-executed states)"
            )
    return findings


def path_findings(paths: list, where: str) -> list[str]:
    """Check that path controls are commensurate with the declared hazard."""
    findings = []
    for index, path in enumerate(paths):
        control_types = {control["type"] for control in path["controls"]}
        if path["hazard_class"] == "irreversible" and not control_types & {
            "preventive",
            "containment",
        }:
            findings.append(
                f"{where}: ai_only_paths[{index}]: irreversible worst outcome with only "
                f"{sorted(control_types)} controls — add a preventive or containment "
                "control, or prohibit the path with a human gate"
            )
    return findings


def gate_findings(data: dict, where: str) -> list[str]:
    """Enforce fail-closed release-gate semantics for the declared decision."""
    findings = []
    gate = data["release_gate"]
    decision = gate["decision"]
    sections = ("capability", "trust_and_evidence", "accountability", "oversight_viability",
                "evals", "telemetry")

    if decision == "move":
        for section in sections:
            for index, check in enumerate(gate[section]):
                spot = f"{where}: release_gate.{section}[{index}] ({check['check']})"
                if check["status"] == "fail":
                    findings.append(f"{spot}: status is fail but decision is move")
                if check["status"] == "not_applicable" and not check.get("evidence"):
                    findings.append(
                        f"{spot}: not_applicable requires evidence explaining why"
                    )

    if decision in ("move", "do_not_move"):
        records = data.get("decision_records") or []
        if not any(record["decision"] == decision for record in records):
            findings.append(
                f"{where}: release_gate.decision is {decision!r} but no decision record "
                "with that decision and an accountable-owner sign-off exists"
            )
    return findings


def semantic_findings(data: dict, where: str) -> list[str]:
    """Run cross-field rules; assumes structural validation already passed."""
    findings = []
    any_executed = False
    for unit in data["responsibilities"]:
        unit_where = f"{where}: responsibilities.{unit['name']}"
        findings.extend(control_findings(unit, unit_where))
        boundary = unit["boundary"]
        if EXECUTED in (boundary["current_state"], boundary["target_state"]):
            any_executed = True

    if any_executed:
        if not data.get("system_dependencies"):
            findings.append(
                f"{where}: AI-executed boundary present but system_dependencies is missing "
                "(pin model/prompt/tool/corpus versions)"
            )
        if data.get("ai_only_paths") is None:
            findings.append(
                f"{where}: AI-executed boundary present but ai_only_paths is missing "
                "(declare [] only after tracing the work architecture)"
            )

    findings.extend(path_findings(data.get("ai_only_paths") or [], where))
    findings.extend(gate_findings(data, where))
    return findings


def validate_file(path: Path) -> list[str]:
    """Validate one map file and return finding strings (empty means valid)."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [f"{path}: cannot parse: {error}"]
    if not isinstance(data, dict):
        return [f"{path}: top level is not a mapping"]

    findings = structural_findings(data, str(path))
    if findings:
        return findings
    return semantic_findings(data, str(path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("maps", nargs="+", type=Path, help="map YAML files to validate")
    args = parser.parse_args()

    failed = False
    for path in args.maps:
        findings = validate_file(path)
        if findings:
            failed = True
            for finding in findings:
                print(finding, file=sys.stderr)
        else:
            print(f"{path}: ok")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
