import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "ng_skill_route_score.py"
CASES = ROOT / "evals" / "skill-routing-cases.jsonl"


def test_skill_routing_cases_manifest_is_valid():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--cases", str(CASES)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "manifest is well-formed" in result.stdout


def test_skill_route_score_fails_wrong_observed_route(tmp_path):
    observed = tmp_path / "observed.jsonl"
    observed.write_text(
        "\n".join(
            [
                json.dumps({"id": "breaking-down-the-work-trigger-01", "loaded_skills": []}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--cases",
            str(CASES),
            "--observed",
            str(observed),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "breaking-down-the-work-trigger-01" in result.stdout
    assert "Skill-routing accuracy:" in result.stdout


def test_skill_route_score_rejects_unknown_skill_in_manifest(tmp_path):
    cases = tmp_path / "cases.jsonl"
    cases.write_text(
        json.dumps(
            {
                "id": "routing-bad",
                "skill": "not-a-real-skill",
                "prompt": "Should fail manifest validation.",
                "expected": "trigger",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--cases", str(cases), "--skills-dir", str(ROOT / "skills")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "unknown skill" in (result.stdout + result.stderr)
