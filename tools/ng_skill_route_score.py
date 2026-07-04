#!/usr/bin/env python3
"""Score recorded skill-routing decisions against deterministic expected routes.

Input:
  --cases evals/skill-routing-cases.jsonl

Optional observed routes:
  --observed path/to/observed.jsonl

Observed JSONL schema:
  {"id": "routing-001", "loaded_skills": ["rating-change-risk", "..."]}

If --observed is omitted, the script only validates the case manifest. This lets CI
enforce that routing cases stay well-formed while real model-run results can be
scored in a separate job.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RoutingCase:
    id: str
    skill: str
    prompt: str
    expected: str

    @property
    def should_trigger(self) -> bool:
        return self.expected == "trigger"


def load_cases(path: Path) -> list[RoutingCase]:
    cases = []
    seen_ids = set()

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue

        data = json.loads(line)
        case = RoutingCase(
            id=data["id"],
            skill=data["skill"],
            prompt=data["prompt"],
            expected=data["expected"],
        )

        if case.id in seen_ids:
            raise ValueError(f"{path}:{line_number}: duplicate id {case.id!r}")
        seen_ids.add(case.id)

        if case.expected not in {"trigger", "not-trigger"}:
            raise ValueError(f"{path}:{line_number}: expected must be trigger or not-trigger")

        if not case.prompt.strip():
            raise ValueError(f"{path}:{line_number}: empty prompt")

        cases.append(case)

    return cases


def known_skills(skills_dir: Path) -> set[str]:
    return {path.parent.name for path in skills_dir.glob("*/SKILL.md")}


def validate_case_skills(cases: list[RoutingCase], skills_dir: Path) -> None:
    known = known_skills(skills_dir)
    unknown = sorted({case.skill for case in cases if case.skill not in known})
    if unknown:
        raise ValueError(f"unknown skill(s) in routing manifest: {unknown}")


def load_observed(path: Path) -> dict[str, set[str]]:
    observed: dict[str, set[str]] = {}

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue

        data = json.loads(line)
        case_id = data["id"]
        loaded = set(data.get("loaded_skills", []))

        if case_id in observed:
            raise ValueError(f"{path}:{line_number}: duplicate observed id {case_id!r}")

        observed[case_id] = loaded

    return observed


def score(cases: list[RoutingCase], observed: dict[str, set[str]]) -> tuple[int, int, list[str]]:
    passed = 0
    failures: list[str] = []

    for case in cases:
        if case.id not in observed:
            failures.append(f"{case.id}: missing observed route")
            continue

        fired = case.skill in observed[case.id]
        if fired == case.should_trigger:
            passed += 1
            continue

        expectation = "to fire" if case.should_trigger else "not to fire"
        failures.append(
            f"{case.id}: expected {case.skill} {expectation}; loaded={sorted(observed[case.id])}"
        )

    return passed, len(cases), failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=Path("evals/skill-routing-cases.jsonl"))
    parser.add_argument("--observed", type=Path)
    parser.add_argument("--skills-dir", type=Path, default=Path("skills"))
    args = parser.parse_args()

    cases = load_cases(args.cases)
    validate_case_skills(cases, args.skills_dir)
    print(f"Loaded {len(cases)} routing case(s) from {args.cases}")

    if args.observed is None:
        print("No observed routes supplied; manifest is well-formed.")
        return 0

    observed = load_observed(args.observed)
    passed, total, failures = score(cases, observed)

    for failure in failures:
        print(f"- {failure}")

    print(f"\nSkill-routing accuracy: {passed}/{total}")

    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
