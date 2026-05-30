"""Reproducible efficacy harness for Nuclear-grade worked examples.

What this measures
------------------
Whether each worked-example artifact actually surfaces the decision signals the
methodology claims it demonstrates. It is a transparent presence check over the
real artifacts already in the repository, runnable by anyone, that guards the
worked examples against silent drift.

What this does NOT measure
--------------------------
Whether the underlying engineering is correct, safe, secure, compliant, or
production-ready. Signals are authored from each scenario's stated risks. A
present signal means the artifact *names* the decision element; it is not proof
that the element is adequately handled in the real world. This harness is a
reproducibility and regression aid, not an assurance, benchmark, or A/B proof.

The qualitative simple-prompt-versus-Nuclear-grade comparison lives in
``docs/03-worked-examples/skill-workflow-comparison/results-summary.md`` and is
deliberately not mechanized here, because those author-written meta-sections
describe gaps using the same vocabulary as the signals and cannot be scored by
substring presence without inflating the result.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Signal:
    """A decision element, scored by phrase presence in a section.

    ``any_of`` passes when at least one phrasing appears: use it for genuine
    alternatives (several ways to name the same element). ``all_of`` passes only
    when every phrasing appears: use it for distinct conjunctive gates that must
    all be present, for example a release decision that requires a rollback path
    *and* a monitoring query *and* a named risk owner. When both are given, both
    must hold.
    """

    name: str
    any_of: tuple[str, ...] = ()
    all_of: tuple[str, ...] = ()

    def present_in(self, text: str) -> bool:
        lowered = text.lower()
        any_ok = (not self.any_of) or any(needle.lower() in lowered for needle in self.any_of)
        all_ok = all(needle.lower() in lowered for needle in self.all_of)
        return any_ok and all_ok


@dataclass(frozen=True)
class EvalCase:
    id: str
    title: str
    artifact: str  # repo-relative path to the artifact being scored
    section: str  # exact heading whose body is scored, e.g. "## Nuclear-Grade Trial"
    signals: tuple[Signal, ...]


@dataclass(frozen=True)
class SignalResult:
    name: str
    present: bool


@dataclass(frozen=True)
class CaseResult:
    case: EvalCase
    artifact_found: bool
    section_found: bool
    signals: tuple[SignalResult, ...]

    @property
    def present_count(self) -> int:
        return sum(1 for signal in self.signals if signal.present)

    @property
    def total(self) -> int:
        return len(self.signals)

    @property
    def status(self) -> str:
        if not self.artifact_found:
            return "artifact-missing"
        if not self.section_found:
            return "section-missing"
        if self.present_count == self.total:
            return "ok"
        return "incomplete"

    @property
    def ok(self) -> bool:
        return self.status == "ok"


def load_cases(cases_dir: Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for path in sorted(cases_dir.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        signals = tuple(
            Signal(
                name=signal["name"],
                any_of=tuple(signal.get("any", ())),
                all_of=tuple(signal.get("all", ())),
            )
            for signal in data["signals"]
        )
        cases.append(
            EvalCase(
                id=data["id"],
                title=data["title"],
                artifact=data["artifact"],
                section=data["section"],
                signals=signals,
            )
        )
    return cases


def extract_section(text: str, heading: str) -> str | None:
    """Return the body under an exact ``## Heading`` up to the next ``## `` heading."""

    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index + 1
            break
    if start is None:
        return None
    body: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        body.append(line)
    return "\n".join(body)


def run_case(case: EvalCase, repo: Path) -> CaseResult:
    artifact_path = repo / case.artifact
    empty = tuple(SignalResult(signal.name, False) for signal in case.signals)
    if not artifact_path.exists():
        return CaseResult(case, artifact_found=False, section_found=False, signals=empty)
    section = extract_section(artifact_path.read_text(encoding="utf-8"), case.section)
    if section is None:
        return CaseResult(case, artifact_found=True, section_found=False, signals=empty)
    results = tuple(
        SignalResult(signal.name, signal.present_in(section)) for signal in case.signals
    )
    return CaseResult(case, artifact_found=True, section_found=True, signals=results)


def run_all(repo: Path, cases_dir: Path | None = None) -> list[CaseResult]:
    cases_dir = cases_dir or (repo / "evals" / "cases")
    if not cases_dir.exists():
        return []
    return [run_case(case, repo) for case in load_cases(cases_dir)]
