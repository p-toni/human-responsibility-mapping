#!/usr/bin/env python3
"""Run the trigger eval set against the skill description with Claude CLI."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import sys
from pathlib import Path


def load_metadata(skill_path: Path) -> tuple[str, str]:
    skill_md = skill_path / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_md} does not start with YAML frontmatter")

    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{skill_md} has no closing YAML frontmatter marker")

    lines = text[4:end].splitlines()
    name = ""
    description = ""
    for index, line in enumerate(lines):
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
        if line.startswith("description: >"):
            chunks: list[str] = []
            for next_line in lines[index + 1 :]:
                if next_line and not next_line.startswith((" ", "\t")):
                    break
                stripped = next_line.strip()
                if stripped:
                    chunks.append(stripped)
            description = " ".join(chunks)
            break
        if line.startswith("description:"):
            value = line.split(":", 1)[1].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]
            description = value
            break

    if not name:
        raise ValueError(f"{skill_md} frontmatter has no name")
    if not description:
        raise ValueError(f"{skill_md} frontmatter has no description")
    return name, description


def build_prompt(description: str, query: str) -> str:
    return f"""You are evaluating whether an AI coding assistant should load a skill.

Skill description:
{description}

User query:
{query}

Return exactly one token:
TRIGGER if the assistant should load this skill.
NO_TRIGGER if the assistant should not load this skill.
"""


def run_one(description: str, query: str, model: str, timeout: int) -> bool:
    cmd = [
        "claude",
        "-p",
        build_prompt(description, query),
        "--model",
        model,
        "--disable-slash-commands",
        "--no-session-persistence",
        "--tools",
        "",
    ]
    completed = subprocess.run(
        cmd,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout,
    )
    output = completed.stdout.strip().upper()
    if output == "TRIGGER":
        return True
    if output == "NO_TRIGGER":
        return False
    raise ValueError(f"Unexpected model output: {completed.stdout!r}")


def evaluate_case(case: dict, description: str, model: str, runs: int, timeout: int) -> dict:
    triggers = 0
    for _ in range(runs):
        if run_one(description, case["query"], model, timeout):
            triggers += 1

    should_trigger = bool(case["should_trigger"])
    trigger_rate = triggers / runs
    passed = triggers == runs if should_trigger else triggers == 0
    return {
        "query": case["query"],
        "should_trigger": should_trigger,
        "trigger_rate": trigger_rate,
        "triggers": triggers,
        "runs": runs,
        "pass": passed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--eval-set", required=True, type=Path)
    parser.add_argument("--skill-path", required=True, type=Path)
    parser.add_argument("--runs-per-query", type=int, default=3)
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--model", default="claude-sonnet-4-6")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    skill_name, description = load_metadata(args.skill_path)
    cases = json.loads(args.eval_set.read_text(encoding="utf-8"))

    results: list[dict | None] = [None] * len(cases)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.num_workers) as executor:
        future_to_index = {
            executor.submit(
                evaluate_case,
                case,
                description,
                args.model,
                args.runs_per_query,
                args.timeout,
            ): index
            for index, case in enumerate(cases)
        }
        for future in concurrent.futures.as_completed(future_to_index):
            index = future_to_index[future]
            result = future.result()
            results[index] = result
            if args.verbose:
                status = "PASS" if result["pass"] else "FAIL"
                print(f"{status}: {result['triggers']}/{result['runs']} {result['query'][:80]}", file=sys.stderr)

    final_results = [result for result in results if result is not None]
    summary = {
        "total": len(final_results),
        "passed": sum(1 for result in final_results if result["pass"]),
        "failed": sum(1 for result in final_results if not result["pass"]),
    }
    payload = {
        "skill_name": skill_name,
        "description": description,
        "results": final_results,
        "summary": summary,
    }

    rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
