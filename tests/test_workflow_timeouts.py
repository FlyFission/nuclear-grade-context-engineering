"""Every GitHub Actions job here declares a bounded `timeout-minutes`.

Without one, GitHub allows a job 360 minutes. A stuck step then ties up a runner for hours,
and a required check that never reports blocks merging. This module covers the workflows
this repository runs and the one `ng scaffold-ci` writes into other repositories.

Idea source: the XERJ project (https://github.com/xerj-org/xerj, Apache-2.0) gates its CI the
same way after a hung job stalled its pipeline. Here the check reads the workflow with PyYAML
and the code and wording are our own.

It skips locally when PyYAML is absent; CI installs it, so the checks always run there.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.y*ml"))

# Largest cap accepted. Without a ceiling, a 300-minute value would pass the "declared" check
# while leaving the problem in place. Context: in the 2026-11-06 CI run the slowest job took
# 76 s and the whole run finished in under two minutes.
MAX_TIMEOUT_MINUTES = 60


def timeout_problems(doc: object) -> list[str]:
    """Return one message per job that breaks the rule. An empty list means the file is clean."""
    if not isinstance(doc, dict) or not isinstance(doc.get("jobs"), dict) or not doc["jobs"]:
        # Zero recognised jobs means the file shape is unknown; report it instead of passing.
        return ["no jobs found: the workflow shape is not what this check understands"]
    problems = []
    for name, job in doc["jobs"].items():
        if not isinstance(job, dict):
            problems.append(f"{name}: job is not a mapping")
            continue
        if "uses" in job:
            # GitHub rejects timeout-minutes on jobs that delegate through `uses`, so
            # they are exempt; the limit belongs to the jobs of the workflow they call.
            continue
        if "runs-on" not in job:
            problems.append(f"{name}: has neither runs-on nor uses")
            continue
        value = job.get("timeout-minutes")
        # bool is an int subclass in Python; `true` is not a duration.
        if isinstance(value, bool) or not isinstance(value, int):
            problems.append(f"{name}: timeout-minutes missing or not an integer ({value!r})")
        elif not 1 <= value <= MAX_TIMEOUT_MINUTES:
            problems.append(f"{name}: timeout-minutes {value} is outside 1..{MAX_TIMEOUT_MINUTES}")
    return problems


@pytest.fixture(scope="module")
def yaml():
    return pytest.importorskip("yaml")


def test_this_repository_has_workflows_to_check():
    # Guards the guard: an empty glob would make every parametrized check below vanish.
    assert WORKFLOWS, "no .github/workflows/*.yml found"


@pytest.mark.parametrize("workflow", WORKFLOWS, ids=lambda p: p.name)
def test_repository_workflow_jobs_declare_a_bounded_timeout(workflow, yaml):
    doc = yaml.safe_load(workflow.read_text(encoding="utf-8"))
    assert timeout_problems(doc) == []


def test_scaffold_ci_workflow_declares_a_bounded_timeout(tmp_path, yaml):
    ng = ROOT / "tools" / "ng.py"
    result = subprocess.run(
        [sys.executable, str(ng), "scaffold-ci", str(tmp_path)],
        check=False,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    workflow = tmp_path / ".github" / "workflows" / "nuclear-grade.yml"
    assert timeout_problems(yaml.safe_load(workflow.read_text(encoding="utf-8"))) == []


# The checker must fail for each defect it claims to catch.
@pytest.mark.parametrize(
    ("job", "fragment"),
    [
        ({"runs-on": "ubuntu-latest"}, "missing"),
        ({"runs-on": "ubuntu-latest", "timeout-minutes": 0}, "outside"),
        ({"runs-on": "ubuntu-latest", "timeout-minutes": 360}, "outside"),
        ({"runs-on": "ubuntu-latest", "timeout-minutes": True}, "not an integer"),
        ({"runs-on": "ubuntu-latest", "timeout-minutes": "${{ vars.T }}"}, "not an integer"),
        ({"steps": []}, "neither runs-on nor uses"),
    ],
)
def test_checker_flags_each_defect(job, fragment):
    problems = timeout_problems({"jobs": {"j": job}})
    assert len(problems) == 1 and fragment in problems[0]


def test_checker_accepts_bounded_and_reusable_jobs():
    doc = {"jobs": {"a": {"runs-on": "x", "timeout-minutes": 15}, "b": {"uses": "./w.yml"}}}
    assert timeout_problems(doc) == []


@pytest.mark.parametrize("doc", [None, {}, {"jobs": {}}, {"jobs": []}, "text"])
def test_checker_fails_loudly_when_it_sees_no_jobs(doc):
    assert "no jobs found" in timeout_problems(doc)[0]
