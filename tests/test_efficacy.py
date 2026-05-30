from pathlib import Path

from nuclear_grade import efficacy
from tests.test_ng_cli import run_ng

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "evals" / "cases"


def test_real_worked_examples_surface_every_claimed_signal():
    """Each shipped worked example must contain all the decision signals it claims."""

    results = efficacy.run_all(ROOT)

    assert results, "expected eval cases under evals/cases/"
    for result in results:
        assert result.artifact_found, f"{result.case.id} artifact missing: {result.case.artifact}"
        assert result.section_found, f"{result.case.id} missing section {result.case.section!r}"
        missing = [signal.name for signal in result.signals if not signal.present]
        assert not missing, f"{result.case.id} dropped decision signals: {missing}"


def test_cases_are_loadable_and_well_formed():
    cases = efficacy.load_cases(CASES_DIR)

    assert len(cases) >= 3
    for case in cases:
        assert case.id and case.title and case.artifact
        assert case.section.startswith("## ")
        assert len(case.signals) >= 3
        for signal in case.signals:
            assert signal.any_of, f"{case.id} signal {signal.name!r} has no phrasings"


def test_extract_section_returns_body_until_next_heading():
    text = "# Title\n\n## A\n\nalpha\n\n## B\n\nbeta\n"

    assert "alpha" in efficacy.extract_section(text, "## A")
    assert "beta" not in efficacy.extract_section(text, "## A")
    assert efficacy.extract_section(text, "## Missing") is None


def test_harness_has_teeth_when_a_signal_is_dropped(tmp_path):
    """A tampered artifact that drops a signal must fail the case (exit 1)."""

    case = efficacy.load_cases(CASES_DIR)[0]
    artifact = ROOT / case.artifact
    section = efficacy.extract_section(artifact.read_text(encoding="utf-8"), case.section)
    assert section is not None

    # Reproduce the repo layout under tmp_path, but strip the scored section body
    # so every signal goes missing.
    target = tmp_path / case.artifact
    target.parent.mkdir(parents=True, exist_ok=True)
    tampered = artifact.read_text(encoding="utf-8").replace(section, "\n(content removed)\n")
    target.write_text(tampered, encoding="utf-8")
    (tmp_path / "evals" / "cases").mkdir(parents=True)
    for json_path in CASES_DIR.glob("*.json"):
        (tmp_path / "evals" / "cases" / json_path.name).write_text(
            json_path.read_text(encoding="utf-8"), encoding="utf-8"
        )

    result = next(r for r in efficacy.run_all(tmp_path) if r.case.id == case.id)

    assert not result.ok
    assert result.status == "incomplete"
    assert result.present_count == 0


def test_run_all_is_empty_outside_a_repo_with_cases(tmp_path):
    assert efficacy.run_all(tmp_path) == []


def test_eval_command_reports_full_coverage():
    result = run_ng("eval", str(ROOT))

    assert result.returncode == 0, result.stderr
    assert "Decision-signal coverage: 15/15" in result.stdout
    assert "[ok]" in result.stdout


def test_eval_command_is_graceful_without_cases(tmp_path):
    result = run_ng("eval", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "No eval cases found" in result.stdout
