"""Targeted regression contracts for optional reconsideration."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills/reconsidering-the-approach/SKILL.md").read_text(encoding="utf-8")
ROUTER = (ROOT / "skills/using-nuclear-grade/SKILL.md").read_text(encoding="utf-8")


def test_depths_and_dispositions_are_explicit():
    for term in ("Quick", "Standard", "Deep", "Creative", "CONTINUE", "REFINE", "REOPEN", "ESCALATE"):
        assert term in SKILL


def test_dissent_and_limits_of_model_independence():
    for term in ("strongest dissent", "not independent reviewers", "decision owner", "accepted basis"):
        assert term in SKILL.lower()


def test_council_cannot_approve_its_own_changes():
    assert "never approve a controlled revision or release" in SKILL.lower()
    assert "never silently alter accepted requirements" in SKILL.lower()


def test_router_remains_optional_and_mode_preserved():
    assert "reconsidering-the-approach" in ROUTER
    assert "without bypassing classification" in ROUTER


def test_near_miss_skills_are_named():
    for term in ("questioning-attitude", "running-a-review-panel", "staying-on-mission", "deciding-who-decides", "responding-to-incidents"):
        assert term in SKILL
