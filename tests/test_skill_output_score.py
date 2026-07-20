import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "ng_skill_output_score.py"
CASES = ROOT / "evals" / "skill-output-cases.jsonl"


def test_skill_output_score_detects_skill_win(tmp_path):
    runs = tmp_path / "runs.jsonl"
    runs.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "case_id": "choosing-what-to-control-output-01",
                        "variant": "baseline",
                        "output": "Track the files that matter and update the release notes.",
                    }
                ),
                json.dumps(
                    {
                        "case_id": "choosing-what-to-control-output-01",
                        "variant": "skill",
                        "output": (
                            "Controlled item rows must name the approved state, current state, "
                            "intended state, reason controlled, evidence gap, and re-check trigger. "
                            "Do not turn this into an entire repository inventory, update decision, "
                            "or ship decision."
                        ),
                    }
                ),
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
            "--runs",
            str(runs),
            "--require-skill-win",
            "--allow-partial",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "choosing-what-to-control-output-01 baseline:" in result.stdout
    assert "choosing-what-to-control-output-01 skill:" in result.stdout


def test_skill_output_score_fails_when_skill_does_not_beat_baseline(tmp_path):
    runs = tmp_path / "runs.jsonl"
    weak = "Add a path check and tests."

    runs.write_text(
        "\n".join(
            [
                json.dumps({"case_id": "choosing-what-to-control-output-01", "variant": "baseline", "output": weak}),
                json.dumps({"case_id": "choosing-what-to-control-output-01", "variant": "skill", "output": weak}),
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
            "--runs",
            str(runs),
            "--require-skill-win",
            "--allow-partial",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "did not beat baseline" in result.stdout


def test_skill_output_score_rejects_duplicate_case_variant_rows(tmp_path):
    runs = tmp_path / "runs.jsonl"
    runs.write_text(
        "\n".join(
            [
                json.dumps({"case_id": "choosing-what-to-control-output-01", "variant": "skill", "output": "first"}),
                json.dumps({"case_id": "choosing-what-to-control-output-01", "variant": "skill", "output": "second"}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--cases", str(CASES), "--runs", str(runs)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "duplicate run row" in (result.stdout + result.stderr)


def test_skill_output_score_rejects_invalid_variant(tmp_path):
    runs = tmp_path / "runs.jsonl"
    runs.write_text(
        json.dumps(
            {
                "case_id": "choosing-what-to-control-output-01",
                "variant": "skil",
                "output": "approved state",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--cases", str(CASES), "--runs", str(runs)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "invalid variant" in (result.stdout + result.stderr)


def test_skill_output_score_requires_baseline_and_skill_pair_for_observed_case(tmp_path):
    runs = tmp_path / "runs.jsonl"
    runs.write_text(
        json.dumps(
            {
                "case_id": "choosing-what-to-control-output-01",
                "variant": "skill",
                "output": "approved state current state intended state reason controlled evidence gap re-check trigger",
            }
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
            "--runs",
            str(runs),
            "--require-skill-win",
            "--allow-partial",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "missing required variant(s): baseline" in result.stdout


def test_skill_output_score_requires_complete_manifest_without_allow_partial(tmp_path):
    cases = tmp_path / "cases.jsonl"
    cases.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "id": "CASE-A",
                        "title": "Case A",
                        "skill_set": ["choosing-what-to-control"],
                        "required": ["approved state"],
                        "forbidden": [],
                    }
                ),
                json.dumps(
                    {
                        "id": "CASE-B",
                        "title": "Case B",
                        "skill_set": ["choosing-what-to-control"],
                        "required": ["approved state"],
                        "forbidden": [],
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    runs = tmp_path / "runs.jsonl"
    runs.write_text(
        "\n".join(
            [
                json.dumps({"case_id": "CASE-A", "variant": "baseline", "output": ""}),
                json.dumps({"case_id": "CASE-A", "variant": "skill", "output": "approved state"}),
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
            str(cases),
            "--runs",
            str(runs),
            "--skills-dir",
            str(ROOT / "skills"),
            "--require-skill-win",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "CASE-B: missing required variant(s): baseline, skill" in result.stdout


def test_skill_output_score_rejects_unknown_skill_in_manifest(tmp_path):
    cases = tmp_path / "cases.jsonl"
    cases.write_text(
        json.dumps(
            {
                "id": "BAD",
                "title": "Bad case",
                "skill_set": ["not-a-real-skill"],
                "required": ["x"],
                "forbidden": [],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    runs = tmp_path / "runs.jsonl"
    runs.write_text(json.dumps({"case_id": "BAD", "variant": "skill", "output": "x"}) + "\n")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--cases",
            str(cases),
            "--runs",
            str(runs),
            "--skills-dir",
            str(ROOT / "skills"),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "unknown skill" in (result.stdout + result.stderr)
