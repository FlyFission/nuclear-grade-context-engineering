"""Deterministic scoring for catalog-level skill-routing observations.

The scorer measures recorded selections against required and allowed skill sets. It
is intentionally separate from the model runner: a manifest can be validated in CI,
while provider/host runs are captured as JSONL and scored without pretending that a
structural check proves live routing efficacy.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from nuclear_grade.skill_catalog import SkillCatalog


class RoutingEvalError(ValueError):
    """Raised when a scenario or observed run cannot be scored honestly."""


@dataclass(frozen=True)
class RoutingScenario:
    id: str
    prompt: str
    required_skills: frozenset[str]
    allowed_skills: frozenset[str]


@dataclass(frozen=True)
class RoutingScore:
    true_positive: int
    false_positive: int
    false_negative: int
    acceptable_cases: int
    total_cases: int
    failures: tuple[str, ...]

    @property
    def precision(self) -> float:
        denominator = self.true_positive + self.false_positive
        return self.true_positive / denominator if denominator else 1.0

    @property
    def recall(self) -> float:
        denominator = self.true_positive + self.false_negative
        return self.true_positive / denominator if denominator else 1.0

    @property
    def acceptable_rate(self) -> float:
        """Share of routes satisfying required-subset and allowed-superset constraints."""

        return self.acceptable_cases / self.total_cases


def _jsonl(path: Path) -> list[tuple[int, object]]:
    rows: list[tuple[int, object]] = []
    errors: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append((line_number, json.loads(line)))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid JSON: {exc.msg}")
    if errors:
        raise RoutingEvalError("\n".join(errors))
    return rows


def _string_set(value: object, *, path: Path, line_number: int, field: str, errors: list[str]) -> frozenset[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        errors.append(f"{path}:{line_number}: {field} must be a list of non-empty skill ids")
        return frozenset()
    if len(value) != len(set(value)):
        errors.append(f"{path}:{line_number}: {field} contains duplicates")
    return frozenset(value)


def load_scenarios(path: Path, catalog: SkillCatalog) -> tuple[RoutingScenario, ...]:
    """Load exact/composable routing scenarios and validate them against the live catalog."""

    routable = {entry.id for entry in catalog.model_routable}
    errors: list[str] = []
    scenarios: list[RoutingScenario] = []
    seen: set[str] = set()

    for line_number, raw in _jsonl(path):
        if not isinstance(raw, dict):
            errors.append(f"{path}:{line_number}: scenario must be an object")
            continue
        case_id = raw.get("id")
        prompt = raw.get("prompt")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{path}:{line_number}: id must be a non-empty string")
            continue
        if case_id in seen:
            errors.append(f"{path}:{line_number}: duplicate scenario id {case_id!r}")
        seen.add(case_id)
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{path}:{line_number}: prompt must be non-empty")
            prompt = ""

        required = _string_set(
            raw.get("required_skills"),
            path=path,
            line_number=line_number,
            field="required_skills",
            errors=errors,
        )
        allowed_raw = raw.get("allowed_skills", list(required))
        allowed = _string_set(
            allowed_raw,
            path=path,
            line_number=line_number,
            field="allowed_skills",
            errors=errors,
        )
        if not required:
            errors.append(f"{path}:{line_number}: required_skills must not be empty")
        if not required <= allowed:
            errors.append(f"{path}:{line_number}: required_skills must be a subset of allowed_skills")
        unknown = sorted((required | allowed) - routable)
        if unknown:
            errors.append(
                f"{path}:{line_number}: non-model-routable or unknown skill(s): {', '.join(unknown)}"
            )
        scenarios.append(
            RoutingScenario(
                id=case_id,
                prompt=prompt,
                required_skills=required,
                allowed_skills=allowed,
            )
        )

    if not scenarios:
        errors.append(f"{path}: at least one routing scenario is required")
    if errors:
        raise RoutingEvalError("invalid routing scenarios:\n- " + "\n- ".join(errors))
    return tuple(scenarios)


def load_observed(
    path: Path,
    scenarios: tuple[RoutingScenario, ...],
    catalog: SkillCatalog,
) -> dict[str, frozenset[str]]:
    """Load recorded routes and reject unknown IDs/skills or duplicate evidence rows."""

    scenario_ids = {scenario.id for scenario in scenarios}
    known = {entry.id for entry in catalog.entries}
    observed: dict[str, frozenset[str]] = {}
    errors: list[str] = []

    for line_number, raw in _jsonl(path):
        if not isinstance(raw, dict):
            errors.append(f"{path}:{line_number}: observed row must be an object")
            continue
        case_id = raw.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{path}:{line_number}: id must be a non-empty string")
            continue
        loaded = _string_set(
            raw.get("loaded_skills", []),
            path=path,
            line_number=line_number,
            field="loaded_skills",
            errors=errors,
        )
        if case_id in observed:
            errors.append(f"{path}:{line_number}: duplicate observed id {case_id!r}")
        else:
            observed[case_id] = loaded
        if case_id not in scenario_ids:
            errors.append(f"{path}:{line_number}: observed id {case_id!r} has no matching scenario")
        unknown = sorted(loaded - known)
        if unknown:
            errors.append(f"{path}:{line_number}: unknown skill(s): {', '.join(unknown)}")

    missing_ids = sorted(scenario_ids - set(observed))
    if not observed:
        errors.append(f"{path}: at least one observed route is required")
    if missing_ids:
        errors.append(f"{path}: missing observed route(s): {', '.join(missing_ids)}")
    if errors:
        raise RoutingEvalError("invalid observed routes:\n- " + "\n- ".join(errors))
    return observed


def score_routes(
    scenarios: tuple[RoutingScenario, ...],
    observed: dict[str, frozenset[str]],
) -> RoutingScore:
    """Score required recall and unnecessary selection, case by case."""

    if not scenarios:
        raise RoutingEvalError("at least one routing scenario is required")

    true_positive = 0
    false_positive = 0
    false_negative = 0
    acceptable_cases = 0
    failures: list[str] = []

    for scenario in scenarios:
        loaded = observed.get(scenario.id)
        if loaded is None:
            false_negative += len(scenario.required_skills)
            failures.append(f"{scenario.id}: missing observed route")
            continue
        present = scenario.required_skills & loaded
        missing = scenario.required_skills - loaded
        unnecessary = loaded - scenario.allowed_skills
        true_positive += len(present)
        false_negative += len(missing)
        false_positive += len(unnecessary)
        if not missing and not unnecessary:
            acceptable_cases += 1
        if missing:
            failures.append(
                f"{scenario.id}: missing required skill(s): {', '.join(sorted(missing))}"
            )
        if unnecessary:
            failures.append(
                f"{scenario.id}: unnecessary skill(s): {', '.join(sorted(unnecessary))}"
            )

    return RoutingScore(
        true_positive=true_positive,
        false_positive=false_positive,
        false_negative=false_negative,
        acceptable_cases=acceptable_cases,
        total_cases=len(scenarios),
        failures=tuple(failures),
    )
