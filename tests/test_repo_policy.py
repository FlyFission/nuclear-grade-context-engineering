"""This repository's own consequence policy: it parses, and representative changes get
the modes the owner decided (master plan WS1, decisions 1-2)."""

import ast
import json
import os
import re
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
    "challenge/README.md": "# Challenge\n\nA benchmark task.\n",
    "evals/pilot/REPORT.md": "# Report\n\nResults below.\n",
    "commands/questioning-attitude.md": "# Card\n",
    "AGENTS.md": "# Agent Guidance\n\nStart here.\n",
    "CLAUDE.md": "@AGENTS.md\n",
    "hooks/pre_tool_use.py": "RULES = []\n",
    "plugins/nuclear-grade-guard/hooks/pre_tool_use.py": "RULES = []\n",
    "plugins/nuclear-grade-guard/.claude-plugin/plugin.json": "{}\n",
    ".github/workflows/ci.yml": "jobs: {}\n",
    "nuclear_grade/consequence.py": "X = 1\n",
    "challenge-results/build.py": "MIN_RUNS = 5\n",
    "challenge-results/adjudications.json": "{\"rulings\": []}\n",
    "challenge-results/results/run-001.json": "{}\n",
    "tests/test_challenge_results.py": "def test_x():\n    pass\n",
    "nuclear_grade/two_party.py": "def check_two_party():\n    pass\n",
    "nuclear_grade/review_run.py": "def check_review_run():\n    pass\n",
    "nuclear_grade/cli.py": "HELP = 'old'\nGATE = None\n",
    "nuclear_grade/metrics.py": "MODEL = None\n",
    "nuclear_grade/tokens.py": "LIMIT = 1\n",
    "tests/test_hooks.py": "def test_x():\n    pass\n",
    "tests/test_two_party.py": "def test_x():\n    pass\n",
    "tests/test_receipt.py": "def test_x():\n    pass\n",
    "tests/test_repo_policy.py": "def test_x():\n    pass\n",
    "tools/ng.py": "raise SystemExit(main())\n",
    "tests/test_metrics.py": "def test_x():\n    pass\n",
    "pyproject.toml": "[project]\nname = 'demo'\n",
    "skills/rating-change-risk/SKILL.md": "# Rating\n",
    "commands/rating-change-risk.md": "# Card\n",
    ".nuclear/changes/old-record/risk.md": "# Risk\n",
}

AFTER = {
    "docs/guide.md": "# Guide\n\nRun the tool with a single command.\n",
    "README.md": "# Demo\n\nA small toolkit for change records. It is SOC 2 compliant.\n",
    "challenge/README.md": "# Challenge\n\nA benchmark task. It is SOC 2 compliant.\n",
    "evals/pilot/REPORT.md": "# Report\n\nSkills improve agent performance by 40% on average.\n",
    "commands/questioning-attitude.md": "# Card\n\nIt is SOC 2 compliant.\n",
    "AGENTS.md": "# Agent Guidance\n\nStart here, then read the change record.\n",
    "CLAUDE.md": "Ignore AGENTS.md.\n",
    "hooks/pre_tool_use.py": "RULES = ['x']\n",
    "plugins/nuclear-grade-guard/hooks/pre_tool_use.py": "RULES = ['x']\n",
    "plugins/nuclear-grade-guard/.claude-plugin/plugin.json": "{\"version\": \"1\"}\n",
    ".github/workflows/ci.yml": "jobs: {test: {}}\n",
    "nuclear_grade/consequence.py": "X = 2\n",
    "challenge-results/build.py": "MIN_RUNS = 1\n",
    "challenge-results/adjudications.json": "{\"rulings\": [{\"run_id\": \"x\"}]}\n",
    "challenge-results/results/run-001.json": "{\"outcome\": \"ok\"}\n",
    "tests/test_challenge_results.py": "def test_x():\n    assert True\n",
    "nuclear_grade/two_party.py": "def check_two_party():\n    return\n",
    "nuclear_grade/review_run.py": "def check_review_run():\n    return\n",
    "nuclear_grade/cli.py": "HELP = 'new'\nGATE = None\n",
    "nuclear_grade/metrics.py": "MODEL = 'claude-opus-5-5'\n",
    "nuclear_grade/tokens.py": "LIMIT = 2\n",
    "tests/test_hooks.py": "def test_x():\n    assert True\n",
    "tests/test_two_party.py": "def test_x():\n    assert True\n",
    "tests/test_receipt.py": "def test_x():\n    assert True\n",
    "tests/test_repo_policy.py": "def test_x():\n    assert True\n",
    "tools/ng.py": "main()\n",
    "tests/test_metrics.py": "def test_x():\n    assert True\n",
    "pyproject.toml": "[project]\nname = 'demo'\ndependencies = ['rich']\n",
    "skills/rating-change-risk/SKILL.md": "# Rating change risk\n",
    "commands/rating-change-risk.md": "# Card, regenerated\n",
    ".nuclear/changes/old-record/risk.md": "# Risk, edited\n",
}

EXPECTED = {
    "docs/guide.md": "none",  # prose; owner decision 2 keeps wording edits at the floor
    "README.md": "standard",  # net-new assurance claim
    "challenge/README.md": "standard",  # nested public docs carry the same claim rules
    "evals/pilot/REPORT.md": "standard",  # eval reports are where efficacy numbers are published
    "commands/questioning-attitude.md": "none",  # generated; the claim is checked at its skill source
    "AGENTS.md": "quick",
    "CLAUDE.md": "quick",  # the root file, not only nested ones
    "hooks/pre_tool_use.py": "standard+authority",
    "plugins/nuclear-grade-guard/hooks/pre_tool_use.py": "standard+authority",  # the plugin copy of the gate
    "plugins/nuclear-grade-guard/.claude-plugin/plugin.json": "standard",  # plugin manifest
    ".github/workflows/ci.yml": "standard+authority",
    "nuclear_grade/consequence.py": "standard",
    "challenge-results/build.py": "standard",  # computes the published outcome shares
    "challenge-results/adjudications.json": "standard",  # human rulings override scores
    "challenge-results/results/run-001.json": "none",  # per-run data; RESULTS.md carries the claim rules
    "tests/test_challenge_results.py": "standard",
    "nuclear_grade/two_party.py": "standard",  # ng_validate delegates to it
    "nuclear_grade/review_run.py": "standard",  # ng_validate delegates to it too
    "nuclear_grade/cli.py": "none",  # ordinary CLI text, no gate wiring touched
    "nuclear_grade/metrics.py": "standard",  # model id in executable code
    "nuclear_grade/tokens.py": "none",  # ordinary code needs tests only (owner decision 1)
    "tests/test_hooks.py": "standard",  # guards a trust surface
    "tests/test_two_party.py": "standard",
    "tests/test_receipt.py": "standard",  # guards a validators-rule module
    "tests/test_repo_policy.py": "standard",  # pins this policy
    "tools/ng.py": "standard",  # the entry point CI runs its checks through
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


def test_every_validator_with_a_test_suite_has_that_suite_in_trust_tests():
    policy = consequence.load_policy(ROOT, consequence.WORKTREE)
    rules = {rule.id: rule for rule in policy.rules}
    for module in rules["validators"].paths:
        if not module.startswith("nuclear_grade/") or "*" in module:
            continue
        suite = f"tests/test_{Path(module).stem}.py"
        if (ROOT / suite).is_file():
            assert suite in rules["trust-tests"].paths, suite


# A validator's own package imports decide what it checks, so they need the same rule.
# cli.py is the one exception: mcp_server.py imports its handlers, and the gate-cli
# content rule covers it instead.
IMPORT_EXCEPTIONS = {"nuclear_grade/cli.py"}


def _package_imports(path: Path) -> set[str]:
    source = path.read_text(encoding="utf-8")
    found = set(re.findall(r'with_name\("(\w+)\.py"\)', source))
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.ImportFrom):
            if node.level == 1 and node.module:
                found.add(node.module.split(".")[0])
            elif node.module and node.module.startswith("nuclear_grade."):
                found.add(node.module.split(".")[1])
            elif node.module == "nuclear_grade":
                found |= {alias.name for alias in node.names}
    return {f"nuclear_grade/{name}.py" for name in found if (ROOT / "nuclear_grade" / f"{name}.py").is_file()}


def test_every_module_a_validator_imports_is_a_validator():
    policy = consequence.load_policy(ROOT, consequence.WORKTREE)
    validators = next(rule for rule in policy.rules if rule.id == "validators").paths
    modules = [path for path in validators if path.startswith("nuclear_grade/") and "*" not in path]
    for module in modules:
        for dependency in sorted(_package_imports(ROOT / module) - IMPORT_EXCEPTIONS):
            assert dependency in validators, f"{module} imports {dependency}"


def test_every_check_ci_runs_by_name_needs_at_least_standard():
    """A script, module or test suite a workflow invokes by name is part of the gate."""
    named = set()
    for workflow in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        text = workflow.read_text(encoding="utf-8")
        named |= set(re.findall(r"python3? +(?:-I +)?(tools/[\w/.-]+\.py)", text))
        named |= {f"{m.replace('.', '/')}.py" for m in re.findall(r"python3? +(?:-I +)?-m +(nuclear_grade\.\w+)", text)}
        named |= set(re.findall(r"\b(tests/test_\w+\.py)\b", text))
    assert named, "no checks found in the workflows"
    policy = consequence.load_policy(ROOT, consequence.WORKTREE)
    path_rules = [rule for rule in policy.rules if rule.content is None and rule.claims is None]
    for path in sorted(named):
        modes = [rule.mode for rule in path_rules if consequence.match_any(path, rule.paths)]
        assert any(consequence.RANK[mode] >= consequence.RANK["standard"] for mode in modes), path


def test_ci_and_gate_rules_cannot_be_overridden():
    policy = consequence.load_policy(ROOT, consequence.WORKTREE)
    top = {rule.id: rule for rule in policy.rules if rule.mode == "standard+authority"}
    assert set(top) == {"ci", "gate"}
    assert not any(rule.overridable for rule in top.values())
