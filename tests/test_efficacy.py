from pathlib import Path

import pytest

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
            assert signal.any_of or signal.all_of, (
                f"{case.id} signal {signal.name!r} has no phrasings"
            )


def test_extract_section_returns_body_until_next_heading():
    text = "# Title\n\n## A\n\nalpha\n\n## B\n\nbeta\n"

    assert "alpha" in efficacy.extract_section(text, "## A")
    assert "beta" not in efficacy.extract_section(text, "## A")
    assert efficacy.extract_section(text, "## Missing") is None


def test_harness_has_teeth_when_a_signal_is_dropped(tmp_path):
    """A tampered artifact that drops a signal must fail the case (exit 1)."""

    case = next(c for c in efficacy.load_cases(CASES_DIR) if c.id == "U02")
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


def test_all_of_requires_every_phrase_unlike_any_of():
    text = "names a rollback path and a monitoring query"
    conjunctive = efficacy.Signal(
        name="release gates",
        all_of=("rollback path", "monitoring query", "residual risk owner"),
    )
    alternative = efficacy.Signal(
        name="release gates",
        any_of=("rollback path", "monitoring query", "residual risk owner"),
    )

    # all_of fails because "residual risk owner" is missing; any_of still passes.
    assert not conjunctive.present_in(text)
    assert alternative.present_in(text)
    assert conjunctive.present_in(text + " with a residual risk owner")


# Signals whose phrases name complementary halves the methodology requires
# together: dropping either half loses a distinct decision element, so these
# must be conjunctive (`all`). A signal is identified by (case id, substring of
# its name). When a new case adds a complementary signal, list it here so the
# regression guard catches drift instead of leaving it to an external reviewer.
# Signals whose phrases are redundant indicators of one element -- including the
# by-design adversarial-claim signals where one denial proves "not just a happy
# path" -- correctly stay `any` and are not listed.
COMPLEMENTARY_SIGNALS = (
    ("U07", "rollback"),  # rollback path AND monitoring query AND risk owner
    ("U02", "authority"),  # allowed (may edit ... only) AND forbidden (may not broaden)
    ("U02", "bounded release decision"),  # internal residual risk AND public non-claim
    ("U04", "source inspiration"),  # what sources are for AND what they do not satisfy
    ("U04", "self-check"),  # the self-check ran AND it named a stop condition
)


@pytest.mark.parametrize("case_id, name_substring", COMPLEMENTARY_SIGNALS)
def test_complementary_signals_are_conjunctive(case_id, name_substring):
    """Each complementary signal must require all its halves, so dropping one
    half cannot still score as covered (the teeth-weakness Codex flagged)."""

    case = next(c for c in efficacy.load_cases(CASES_DIR) if c.id == case_id)
    signal = next(s for s in case.signals if name_substring in s.name.lower())

    assert signal.all_of, (
        f"{case_id} signal {signal.name!r} names complementary halves and must use "
        f"`all`, not `any`, or dropping one half still reports full coverage"
    )
    assert not signal.any_of, (
        f"{case_id} signal {signal.name!r} mixes `any` with `all`; a loose `any` "
        f"alternative would let the signal pass without every required half"
    )


def test_u02_authority_signal_has_no_leaky_generic_fallback():
    case = next(c for c in efficacy.load_cases(CASES_DIR) if c.id == "U02")
    authority = next(s for s in case.signals if "authority" in s.name.lower())

    assert "write authority" not in authority.all_of + authority.any_of, (
        "generic 'write authority' fallback leaks: it also appears in the controlled-items line"
    )


def test_run_all_is_empty_outside_a_repo_with_cases(tmp_path):
    assert efficacy.run_all(tmp_path) == []


def test_eval_command_reports_malformed_case_clearly(tmp_path):
    cases_dir = tmp_path / "evals" / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / "broken.json").write_text("{ not valid json", encoding="utf-8")

    result = run_ng("eval", str(tmp_path))

    assert result.returncode == 1
    assert "could not load eval cases" in result.stdout
    assert "Traceback" not in (result.stdout + result.stderr)


def test_eval_command_reports_full_coverage():
    result = run_ng("eval", str(ROOT))

    assert result.returncode == 0, result.stderr
    assert "Decision-signal coverage: 15/15" in result.stdout
    assert "[ok]" in result.stdout


def test_eval_command_is_graceful_without_cases(tmp_path):
    result = run_ng("eval", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "No eval cases found" in result.stdout
