#!/usr/bin/env python3
"""Deterministically score recorded baseline-vs-skill outputs.

Case schema, JSONL:
  {"id": "U02", "required": ["controlled items"], "forbidden": ["complete sandbox"]}

Run output schema, JSONL:
  {"case_id": "U02", "variant": "baseline" | "skill", "output": "model output text..."}

This does not judge engineering adequacy. It counts explicit decision signals and
prohibited claims in recorded outputs so live A/B transcripts can be regression-
checked without turning the report into reviewer taste.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

VALID_VARIANTS = {"baseline", "skill"}


@dataclass(frozen=True)
class OutputCase:
    id: str
    title: str
    required: tuple[str, ...]
    forbidden: tuple[str, ...]
    skill_set: tuple[str, ...]


@dataclass(frozen=True)
class ScoredOutput:
    case_id: str
    variant: str
    required_present: int
    required_total: int
    forbidden_present: int

    @property
    def score(self) -> int:
        return self.required_present - self.forbidden_present


def load_cases(path: Path) -> dict[str, OutputCase]:
    cases = {}

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue

        data = json.loads(line)
        case = OutputCase(
            id=data["id"],
            title=data["title"],
            required=tuple(data.get("required", [])),
            forbidden=tuple(data.get("forbidden", [])),
            skill_set=tuple(data.get("skill_set", [])),
        )

        if case.id in cases:
            raise ValueError(f"{path}:{line_number}: duplicate case id {case.id!r}")
        if not case.required:
            raise ValueError(f"{path}:{line_number}: case has no required signals")

        cases[case.id] = case

    return cases


def known_skills(skills_dir: Path) -> set[str]:
    return {path.parent.name for path in skills_dir.glob("*/SKILL.md")}


def validate_case_skills(cases: dict[str, OutputCase], skills_dir: Path) -> None:
    known = known_skills(skills_dir)
    unknown = sorted({skill for case in cases.values() for skill in case.skill_set if skill not in known})
    if unknown:
        raise ValueError(f"unknown skill(s) in output manifest: {unknown}")


def score_output(case: OutputCase, variant: str, output: str) -> ScoredOutput:
    lowered = output.lower()

    required_present = sum(1 for phrase in case.required if phrase.lower() in lowered)
    forbidden_present = sum(1 for phrase in case.forbidden if phrase.lower() in lowered)

    return ScoredOutput(
        case_id=case.id,
        variant=variant,
        required_present=required_present,
        required_total=len(case.required),
        forbidden_present=forbidden_present,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=Path("evals/skill-output-cases.jsonl"))
    parser.add_argument("--runs", type=Path, required=True)
    parser.add_argument("--skills-dir", type=Path, default=Path("skills"))
    parser.add_argument(
        "--require-skill-win",
        action="store_true",
        help="Fail if the skill variant does not beat baseline, or if required baseline/skill pairs are missing.",
    )
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="When requiring skill wins, score only represented cases instead of requiring every manifest case.",
    )
    args = parser.parse_args()

    cases = load_cases(args.cases)
    validate_case_skills(cases, args.skills_dir)
    scores: dict[tuple[str, str], ScoredOutput] = {}

    for line_number, line in enumerate(args.runs.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue

        data = json.loads(line)
        case_id = data["case_id"]
        variant = data["variant"]
        output = data["output"]

        if case_id not in cases:
            raise ValueError(f"{args.runs}:{line_number}: unknown case_id {case_id!r}")
        if variant not in VALID_VARIANTS:
            raise ValueError(
                f"{args.runs}:{line_number}: invalid variant {variant!r}; "
                f"expected one of {sorted(VALID_VARIANTS)}"
            )

        scored = score_output(cases[case_id], variant, output)
        key = (case_id, variant)
        if key in scores:
            raise ValueError(f"{args.runs}:{line_number}: duplicate run row for {case_id!r}/{variant!r}")
        scores[key] = scored

    failures = []

    for scored in sorted(scores.values(), key=lambda item: (item.case_id, item.variant)):
        print(
            f"{scored.case_id} {scored.variant}: "
            f"{scored.required_present}/{scored.required_total} required, "
            f"{scored.forbidden_present} forbidden, score={scored.score}"
        )

    if args.require_skill_win:
        case_ids = sorted({case_id for case_id, _variant in scores}) if args.allow_partial else sorted(cases)

        for case_id in case_ids:
            baseline = scores.get((case_id, "baseline"))
            skill = scores.get((case_id, "skill"))
            if baseline is None or skill is None:
                missing = []
                if baseline is None:
                    missing.append("baseline")
                if skill is None:
                    missing.append("skill")
                failures.append(f"{case_id}: missing required variant(s): {', '.join(missing)}")
                continue
            if skill.score <= baseline.score:
                failures.append(
                    f"{case_id}: skill score {skill.score} did not beat baseline score {baseline.score}"
                )

    for failure in failures:
        print(f"- {failure}")

    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
