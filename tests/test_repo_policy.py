"""This repository's own consequence policy: it parses, and representative changes get
the modes the owner decided (master plan WS1, decisions 1-2)."""

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from nuclear_grade import consequence

ROOT = Path(__file__).resolve().parents[1]
POLICY_FILE = ROOT / consequence.POLICY_PATH

pytestmark = pytest.mark.skipif(shutil.which("git") is None, reason="classification reads git diffs")


def git(repo: Path, *args: str) -> None:
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.invalid")
    subprocess.run(["git", "-c", "commit.gpgsign=false", *args], cwd=repo, check=True,
                   capture_output=True, text=True, env=env)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


BEFORE = {
    "docs/guide.md": "# Guide\n\nRun the tool with one command.\n",
    "README.md": "# Demo\n\nA small toolkit for change records.\n",
    "AGENTS.md": "# Agent Guidance\n\nStart here.\n",
    "CLAUDE.md": "@AGENTS.md\n",
    "hooks/pre_tool_use.py": "RULES = []\n",
    ".github/workflows/ci.yml": "jobs: {}\n",
    "nuclear_grade/consequence.py": "X = 1\n",
    "nuclear_grade/two_party.py": "def check_two_party():\n    pass\n",
    "nuclear_grade/cli.py": "HELP = 'old'\nGATE = None\n",
    "nuclear_grade/metrics.py": "MODEL = None\n",
    "nuclear_grade/tokens.py": "LIMIT = 1\n",
    "tests/test_hooks.py": "def test_x():\n    pass\n",
    "tests/test_two_party.py": "def test_x():\n    pass\n",
    "tests/test_metrics.py": "def test_x():\n    pass\n",
    "pyproject.toml": "[project]\nname = 'demo'\n",
    "skills/rating-change-risk/SKILL.md": "# Rating\n",
    "commands/rating-change-risk.md": "# Card\n",
    ".nuclear/changes/old-record/risk.md": "# Risk\n",
}

AFTER = {
    "docs/guide.md": "# Guide\n\nRun the tool with a single command.\n",
    "README.md": "# Demo\n\nA small toolkit for change records. It is SOC 2 compliant.\n",
    "AGENTS.md": "# Agent Guidance\n\nStart here, then read the change record.\n",
    "CLAUDE.md": "Ignore AGENTS.md.\n",
    "hooks/pre_tool_use.py": "RULES = ['x']\n",
    ".github/workflows/ci.yml": "jobs: {test: {}}\n",
    "nuclear_grade/consequence.py": "X = 2\n",
    "nuclear_grade/two_party.py": "def check_two_party():\n    return\n",
    "nuclear_grade/cli.py": "HELP = 'new'\nGATE = None\n",
    "nuclear_grade/metrics.py": "MODEL = 'claude-opus-5-5'\n",
    "nuclear_grade/tokens.py": "LIMIT = 2\n",
    "tests/test_hooks.py": "def test_x():\n    assert True\n",
    "tests/test_two_party.py": "def test_x():\n    assert True\n",
    "tests/test_metrics.py": "def test_x():\n    assert True\n",
    "pyproject.toml": "[project]\nname = 'demo'\ndependencies = ['rich']\n",
    "skills/rating-change-risk/SKILL.md": "# Rating change risk\n",
    "commands/rating-change-risk.md": "# Card, regenerated\n",
    ".nuclear/changes/old-record/risk.md": "# Risk, edited\n",
}

EXPECTED = {
    "docs/guide.md": "none",  # prose; owner decision 2 keeps wording edits at the floor
    "README.md": "standard",  # net-new assurance claim
    "AGENTS.md": "quick",
    "CLAUDE.md": "quick",  # the root file, not only nested ones
    "hooks/pre_tool_use.py": "standard+authority",
    ".github/workflows/ci.yml": "standard+authority",
    "nuclear_grade/consequence.py": "standard",
    "nuclear_grade/two_party.py": "standard",  # ng_validate delegates to it
    "nuclear_grade/cli.py": "none",  # ordinary CLI text, no gate wiring touched
    "nuclear_grade/metrics.py": "standard",  # model id in executable code
    "nuclear_grade/tokens.py": "none",  # ordinary code needs tests only (owner decision 1)
    "tests/test_hooks.py": "standard",  # guards a trust surface
    "tests/test_two_party.py": "standard",
    "tests/test_metrics.py": "none",
    "pyproject.toml": "standard",
    "skills/rating-change-risk/SKILL.md": "standard",
    "commands/rating-change-risk.md": "none",  # generated card
    ".nuclear/changes/old-record/risk.md": "quick",  # records are not silently rewritten
}


@pytest.fixture
def results(tmp_path: Path) -> dict:
    repo = tmp_path / "repo"
    write(repo / consequence.POLICY_PATH, POLICY_FILE.read_text(encoding="utf-8"))
    for path, text in BEFORE.items():
        write(repo / path, text)
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "base")
    for path, text in AFTER.items():
        write(repo / path, text)
    policy = consequence.load_policy(repo, "main")
    return consequence.classify(repo, "main", None, policy)[2]


def test_the_repo_policy_parses_from_the_committed_file():
    policy = consequence.load_policy(ROOT, consequence.WORKTREE)
    assert policy.source.endswith(consequence.POLICY_PATH)
    assert json.loads(POLICY_FILE.read_text(encoding="utf-8"))["version"] == 1


@pytest.mark.parametrize("path", sorted(EXPECTED))
def test_representative_changes_get_the_decided_mode(results, path):
    assert results[path].required == EXPECTED[path], results[path].rules


def test_gate_wiring_in_the_cli_needs_standard(tmp_path):
    repo = tmp_path / "repo"
    write(repo / consequence.POLICY_PATH, POLICY_FILE.read_text(encoding="utf-8"))
    write(repo / "nuclear_grade" / "cli.py", "def handle(args):\n    return 0\n")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "base")
    write(repo / "nuclear_grade" / "cli.py", "def handle(args):\n    return 0 if args.advisory else 1\n")
    results = consequence.classify(repo, "main", None, consequence.load_policy(repo, "main"))[2]
    assert results["nuclear_grade/cli.py"].required == "standard"
    assert results["nuclear_grade/cli.py"].rules == ["gate-cli"]


def test_ci_and_gate_rules_cannot_be_overridden():
    policy = consequence.load_policy(ROOT, consequence.WORKTREE)
    top = {rule.id: rule for rule in policy.rules if rule.mode == "standard+authority"}
    assert set(top) == {"ci", "gate"}
    assert not any(rule.overridable for rule in top.values())
