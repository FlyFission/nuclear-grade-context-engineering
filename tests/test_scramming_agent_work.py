"""SCRAM contract tests: cooperative hold must never overstate global stop coverage."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills/scramming-agent-work/SKILL.md").read_text(encoding="utf-8")
ROUTER = (ROOT / "skills/using-nuclear-grade/SKILL.md").read_text(encoding="utf-8")


def test_stop_coverage_can_be_partial_or_unknown():
    for term in ("STOPPED (acknowledged)", "STOP REQUESTED (unconfirmed)", "STILL RUNNING", "UNKNOWN"):
        assert term in SKILL
    assert "cannot guarantee" in SKILL
    assert "PARTIAL HOLD" in SKILL


def test_scram_precedes_normal_work_and_does_not_resume_itself():
    assert "before ordinary preflight" in ROUTER
    assert "Maintain hold" in SKILL
    assert "explicit operator resume" in SKILL
    assert "No mutation" in SKILL


def test_reversibility_and_disclosure():
    for term in ("rollback", "compensating action", "irreversible", "read-only", "without executing it"):
        assert term in SKILL.lower()


def test_never_claims_hardware_scram_or_independent_cancel_without_host():
    assert "physical reactor SCRAM" in SKILL
    assert "out-of-band" in SKILL
    assert "external agents" in SKILL


def test_scram_is_not_a_thinking_or_incident_skill():
    for name in ("reconsidering-the-approach", "responding-to-incidents", "handing-off-work"):
        assert name in SKILL
