"""Contracts for the opt-in Council and nonblocking router offer.

These are static regression gates, not proof of better decision quality.
"""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "reconsidering-the-approach"
SKILL = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
ROUTER = (ROOT / "skills/using-nuclear-grade/SKILL.md").read_text(encoding="utf-8")
QUESTION = (ROOT / "skills/questioning-attitude/SKILL.md").read_text(encoding="utf-8")
PROTO = (SKILL_DIR / "references/decision-and-prototypes.md").read_text(encoding="utf-8")
DELIB = (SKILL_DIR / "references/deliberation.md").read_text(encoding="utf-8")
HANDOFF = (SKILL_DIR / "references/engineering-handoff.md").read_text(encoding="utf-8")

spec = importlib.util.spec_from_file_location("ng_prototypes", SKILL_DIR / "scripts/compare_prototypes.py")
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_depths_modes_and_governed_dispositions():
    for mode in ("imagine", "decide", "challenge", "design", "build", "audit"):
        assert mode in SKILL
    for depth in ("Quick", "Standard", "Deep", "Creative"):
        assert depth in SKILL
    for state in ("CONTINUE", "REFINE", "REOPEN", "ESCALATE", "NO_DECISION"):
        assert state in SKILL


def test_three_rounds_and_independence_are_explicit():
    for term in ("Round 1", "Round 2", "Round 3", "SIMULATED_LENSES", "three mandatory"):
        assert term.lower() in DELIB.lower()
    assert "not independent" in SKILL.lower()
    assert "strongest dissent" in SKILL.lower()


def test_creative_and_prototype_evidence_requirements():
    assert "eight" in SKILL.lower()
    assert "before any critique" in SKILL.lower()
    for term in ("freeze", "hard gate", "UNKNOWN", "sensitivity"):
        assert term.lower() in PROTO.lower()


def test_governance_authority_and_spec_handoff():
    assert "never approve a controlled revision" in SKILL.lower()
    assert "do not update accepted" in SKILL.lower()
    for term in ("PROPOSED", "rollback", "re-entry", "verification", "interfaces"):
        assert term.lower() in HANDOFF.lower()


def test_router_offers_once_never_auto_invokes():
    for text in ("one concise, non-blocking offer", "Do **not** load or execute", "do not repeat", "specific unresolved issue"):
        assert text.lower() in ROUTER.lower()
    assert "do not invoke the council automatically" in QUESTION.lower()
    assert "if declined" in ROUTER.lower()


def test_near_miss_skill_boundaries():
    for name in ("questioning-attitude", "running-a-review-panel", "staying-on-mission", "deciding-who-decides", "responding-to-incidents"):
        assert name in SKILL


@pytest.fixture
def baseline():
    return json.loads((SKILL_DIR / "references/prototype-input-example.json").read_text(encoding="utf-8"))


def test_prototype_runner_disqualifies_failed_gates_and_unknown(baseline):
    result = module.evaluate(baseline)
    states = {c["name"]: c["status"] for c in result["candidates"]}
    assert states == {"simple_core": "ELIGIBLE", "agent_orchestrated": "UNKNOWN", "fast_unsafe": "INELIGIBLE"}
    assert result["provisional_winner"] == "simple_core"
    assert "unverified" in result["warning"].lower()


def test_all_missing_data_means_no_winner(baseline):
    for c in baseline["candidates"]:
        c["gates"]["acceptance_tests"] = None
    result = module.evaluate(baseline)
    assert result["provisional_winner"] is None


def test_invalid_and_duplicate_metrics_rejected(baseline):
    baseline["candidates"][0]["results"]["p95_latency_ms"] = True
    with pytest.raises(ValueError):
        module.evaluate(baseline)
    baseline["candidates"][0]["results"]["p95_latency_ms"] = 120
    baseline["candidates"][1]["name"] = "simple_core"
    with pytest.raises(ValueError):
        module.evaluate(baseline)
