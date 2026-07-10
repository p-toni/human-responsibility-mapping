"""Adversarial tests for scripts/validate_map.py.

Each test seeds a violation the validator must catch (or a malformed input it
must reject without crashing). Run with:

    uv run --with pyyaml --with jsonschema --with pytest pytest -q tests/
"""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
EXAMPLE = REPO / "schemas" / "agent-context-pack.example.yaml"

spec = importlib.util.spec_from_file_location("validate_map", REPO / "scripts" / "validate_map.py")
validate_map = importlib.util.module_from_spec(spec)
sys.modules["validate_map"] = validate_map
spec.loader.exec_module(validate_map)


def load_example() -> dict:
    return yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))


def findings_for(data: dict) -> list[str]:
    structural = validate_map.structural_findings(data, "test")
    if structural:
        return structural
    return validate_map.semantic_findings(data, "test")


def passing_gate(gate: dict) -> dict:
    gate = copy.deepcopy(gate)
    for section in ("capability", "trust_and_evidence", "accountability",
                    "oversight_viability", "evals", "telemetry"):
        for check in gate[section]:
            if check["status"] == "fail":
                check["status"] = "pass"
                check["evidence"] = "test-evidence"
    return gate


def signed_record(decision: str) -> dict:
    return {
        "date": "2026-07-10",
        "responsibility": "draft_response",
        "decision": decision,
        "accountable_owner_signoff": "support_lead",
    }


def test_example_passes():
    assert findings_for(load_example()) == []


def test_example_via_file_api():
    assert validate_map.validate_file(EXAMPLE) == []


def test_unknown_schema_version_fails_closed():
    data = load_example()
    data["schema_version"] = "not-a-version"
    findings = findings_for(data)
    assert findings and "unsupported schema_version" in findings[0]


def test_missing_schema_version_fails_closed():
    data = load_example()
    del data["schema_version"]
    findings = findings_for(data)
    assert findings and "unsupported schema_version" in findings[0]


def test_move_with_failing_check_rejected():
    data = load_example()
    data["release_gate"]["decision"] = "move"
    data["decision_records"] = [signed_record("move")]
    findings = findings_for(data)
    assert any("status is fail but decision is move" in f for f in findings)


def test_move_without_decision_record_rejected():
    data = load_example()
    data["release_gate"] = passing_gate(data["release_gate"])
    data["release_gate"]["decision"] = "move"
    findings = findings_for(data)
    assert any("no decision record" in f for f in findings)


def test_move_with_passing_gate_and_signed_record_accepted():
    data = load_example()
    data["release_gate"] = passing_gate(data["release_gate"])
    data["release_gate"]["decision"] = "move"
    data["decision_records"] = [signed_record("move")]
    assert findings_for(data) == []


def test_not_applicable_without_evidence_rejected_on_move():
    data = load_example()
    data["release_gate"] = passing_gate(data["release_gate"])
    data["release_gate"]["decision"] = "move"
    data["release_gate"]["oversight_viability"][2]["evidence"] = None
    data["decision_records"] = [signed_record("move")]
    findings = findings_for(data)
    assert any("not_applicable requires evidence" in f for f in findings)


def test_do_not_move_requires_signed_record():
    data = load_example()
    data["release_gate"]["decision"] = "do_not_move"
    findings = findings_for(data)
    assert any("no decision record" in f for f in findings)


def test_record_without_signoff_rejected_structurally():
    data = load_example()
    data["decision_records"] = [
        {"date": "2026-07-10", "responsibility": "draft_response", "decision": "do_not_move"}
    ]
    findings = findings_for(data)
    assert any("accountable_owner_signoff" in f for f in findings)


def test_gate_string_checks_rejected():
    data = load_example()
    data["release_gate"]["capability"] = ["capability_demonstrated"]
    findings = findings_for(data)
    assert any("capability" in f for f in findings)


def test_current_executed_without_current_controls_rejected():
    data = load_example()
    boundary = data["responsibilities"][0]["boundary"]
    boundary["current_state"] = "AI-executed"
    findings = findings_for(data)
    assert any("current_controls is empty" in f for f in findings)


def test_target_executed_without_target_controls_rejected():
    data = load_example()
    data["system_dependencies"] = data.get("system_dependencies") or {}
    boundary = data["responsibilities"][0]["boundary"]
    boundary["target_state"] = "AI-executed"
    findings = findings_for(data)
    assert any("target_controls is empty" in f for f in findings)


def test_controls_on_non_executed_state_rejected():
    data = load_example()
    boundary = data["responsibilities"][0]["boundary"]
    boundary["target_controls"] = ["sampling-review"]
    findings = findings_for(data)
    assert any("controls only apply to AI-executed states" in f for f in findings)


def test_composed_control_stack_accepted():
    data = load_example()
    boundary = data["responsibilities"][0]["boundary"]
    boundary["target_state"] = "AI-executed"
    boundary["target_controls"] = ["policy-governed", "rollback-required"]
    data["ai_only_paths"] = []
    findings = findings_for(data)
    assert findings == []


def test_invalid_control_mode_rejected():
    data = load_example()
    boundary = data["responsibilities"][0]["boundary"]
    boundary["target_state"] = "AI-executed"
    boundary["target_controls"] = ["vibes-based"]
    findings = findings_for(data)
    assert any("vibes-based" in f for f in findings)


def test_executed_requires_system_dependencies():
    data = load_example()
    del data["system_dependencies"]
    boundary = data["responsibilities"][0]["boundary"]
    boundary["target_state"] = "AI-executed"
    boundary["target_controls"] = ["sampling-review"]
    findings = findings_for(data)
    assert any("system_dependencies is missing" in f for f in findings)


def test_executed_requires_ai_only_paths_key():
    data = load_example()
    del data["ai_only_paths"]
    boundary = data["responsibilities"][0]["boundary"]
    boundary["target_state"] = "AI-executed"
    boundary["target_controls"] = ["sampling-review"]
    findings = findings_for(data)
    assert any("ai_only_paths is missing" in f for f in findings)


def test_ai_only_paths_as_string_rejected():
    data = load_example()
    data["ai_only_paths"] = "not actually traced"
    findings = findings_for(data)
    assert any("ai_only_paths" in f for f in findings)


def irreversible_path(controls: list[dict]) -> dict:
    return {
        "path": ["classify_ticket", "issue_refund"],
        "entry_condition": "low-risk classification",
        "worst_plausible_outcome": "unrecoverable refund to wrong account",
        "hazard_class": "irreversible",
        "controls": controls,
        "owner": "support_lead",
    }


def test_irreversible_path_with_detective_only_controls_rejected():
    data = load_example()
    data["ai_only_paths"] = [
        irreversible_path([{"type": "detective", "control": "end-to-end sampling"}])
    ]
    findings = findings_for(data)
    assert any("preventive or containment" in f for f in findings)


def test_irreversible_path_with_preventive_control_accepted():
    data = load_example()
    data["ai_only_paths"] = [
        irreversible_path(
            [
                {"type": "preventive", "control": "refund amount cap and allowlist"},
                {"type": "detective", "control": "end-to-end sampling"},
            ]
        )
    ]
    assert findings_for(data) == []


def test_fake_system_dependencies_shape_rejected():
    data = load_example()
    data["system_dependencies"] = {"note": "we use the latest model"}
    findings = findings_for(data)
    assert any("system_dependencies" in f for f in findings)


def test_non_mapping_responsibility_rejected_without_crash():
    data = load_example()
    data["responsibilities"] = ["just a string"]
    findings = findings_for(data)
    assert findings


def test_malformed_claim_rejected_without_crash():
    data = load_example()
    data["responsibilities"][0]["claims"] = [{"claim": 42, "evidence_label": ["nested"]}]
    findings = findings_for(data)
    assert findings


def test_invalid_evidence_label_rejected():
    data = load_example()
    data["responsibilities"][0]["claims"][0]["evidence_label"] = "trust_me"
    findings = findings_for(data)
    assert any("trust_me" in f for f in findings)


def test_invalid_boundary_state_rejected():
    data = load_example()
    data["responsibilities"][0]["boundary"]["current_state"] = "AI-Assisted"
    findings = findings_for(data)
    assert any("AI-Assisted" in f for f in findings)


def test_invalid_gate_decision_rejected():
    data = load_example()
    data["release_gate"]["decision"] = "ship_it"
    findings = findings_for(data)
    assert any("ship_it" in f for f in findings)


def test_missing_oversight_viability_section_rejected():
    data = load_example()
    del data["release_gate"]["oversight_viability"]
    findings = findings_for(data)
    assert any("oversight_viability" in f for f in findings)


def test_non_mapping_top_level_rejected_without_crash(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text("- just\n- a\n- list\n", encoding="utf-8")
    findings = validate_map.validate_file(bad)
    assert any("not a mapping" in f for f in findings)


def test_unparseable_yaml_rejected_without_crash(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text("key: [unclosed\n", encoding="utf-8")
    findings = validate_map.validate_file(bad)
    assert any("cannot parse" in f for f in findings)
