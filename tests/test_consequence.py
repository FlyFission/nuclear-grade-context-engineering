"""`ng required-mode`: diff -> required mode -> covering record -> human approval."""

from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from nuclear_grade import consequence

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("ng_validate_fixtures", ROOT / "tests" / "test_ng_validate.py")
fixtures = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fixtures)

pytestmark = pytest.mark.skipif(shutil.which("git") is None, reason="required-mode reads git diffs")

POLICY = {
    "version": 1,
    "default": "none",
    "bot_identities": ["agent-bot"],
    "dependency_lane": {"authors": ["dependabot[bot]"], "paths": ["pyproject.toml", ".github/workflows/**"]},
    "rules": [
        {"id": "claims", "mode": "quick", "paths": ["*.md", "docs/**.md"], "claims": "general"},
        {"id": "assurance", "mode": "standard", "paths": ["*.md", "docs/**.md"], "claims": "assurance"},
        {"id": "efficacy", "mode": "standard", "paths": ["*.md", "docs/**.md"], "claims": "efficacy"},
        {"id": "deps", "mode": "standard", "paths": ["pyproject.toml"], "skills": ["vetting-outside-code-and-models"]},
        {"id": "model-id", "mode": "standard", "paths": ["src/**"], "content": r"\bclaude-[a-z0-9.-]+\b"},
        {"id": "checker", "mode": "standard", "paths": ["src/checker.py"], "overridable": True},
        {"id": "ci", "mode": "standard+authority", "paths": [".github/**"], "overridable": False},
        {"id": "gate", "mode": "standard+authority", "paths": ["hooks/**"], "overridable": False},
    ],
}
APPROVED_BY_OWNER = [{"user": {"login": "owner"}, "state": "APPROVED"}]


def git(repo: Path, *args: str) -> str:
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.invalid")
    return subprocess.run(["git", "-c", "commit.gpgsign=false", *args], cwd=repo, check=True,
                          capture_output=True, text=True, env=env).stdout.strip()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    write(root / consequence.POLICY_PATH, json.dumps(POLICY, indent=1))
    write(root / "README.md", "# Demo\n\nA small tool. It does not claim compliance with anything.\n")
    write(root / "hooks" / "gate.py", "print('gate')\n")
    write(root / "src" / "app.py", "MODEL = 'none'\n")
    write(root / "src" / "checker.py", "def check():\n    return True\n")
    write(root / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["requests==2.31.0"]\n')
    write(root / ".github" / "workflows" / "ci.yml", "steps:\n  - uses: actions/checkout@" + "a" * 40 + "\n")
    old = fixtures.minimal_quick_packet(root)
    old.rename(old.parent / "old-record")
    git(root, "init", "-q", "-b", "main")
    git(root, "add", "-A")
    git(root, "commit", "-qm", "base")
    return root


def base(repo: Path) -> str:
    return git(repo, "rev-parse", "main")


def run(repo: Path, head: str | None = None, **kwargs) -> dict:
    policy = consequence.load_policy(repo, base(repo))
    return consequence.evaluate(
        repo, base(repo), head, policy,
        base_policy_text=consequence.policy_text(repo, base(repo)),
        head_policy_text=consequence.policy_text(repo, head or consequence.WORKTREE),
        **kwargs,
    )


def quick_record(repo: Path, slug: str, names: str) -> Path:
    packet = fixtures.minimal_quick_packet(repo / "tmp-build")
    target = repo / ".nuclear" / "changes" / slug
    target.parent.mkdir(parents=True, exist_ok=True)
    packet.rename(target)
    shutil.rmtree(repo / "tmp-build")
    risk = target / "risk.md"
    risk.write_text(risk.read_text().replace("## Required links", f"## Scope\n\n- Paths: {names}\n\n## Required links"))
    return target


def standard_record(repo: Path, slug: str, names: str, *, authority: bool = False) -> Path:
    packet = fixtures.minimal_standard_packet(repo / "tmp-build")
    if authority:
        fixtures.add_decision_authority(packet)
    target = repo / ".nuclear" / "changes" / slug
    target.parent.mkdir(parents=True, exist_ok=True)
    packet.rename(target)
    shutil.rmtree(repo / "tmp-build")
    risk = target / "risk.md"
    risk.write_text(risk.read_text().replace("## Required links", f"## Scope\n\n- Paths: {names}\n\n## Required links"))
    return target


def path_entry(receipt: dict, path: str) -> dict:
    return next(entry for entry in receipt["paths"] if entry["path"] == path)


# ------------------------------------------------------------------ floor and modes


def test_docs_only_change_passes_at_the_floor(repo):
    write(repo / "docs" / "guide.md", "# Guide\n\nHow to run the tool.\n")
    receipt = run(repo)
    assert receipt["verdict"] == "pass-floor"
    assert receipt["required_mode"] == "none"
    assert receipt["failures"] == []


def test_ordinary_code_needs_no_record(repo):
    write(repo / "src" / "app.py", "MODEL = 'none'\nVALUE = 2\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_gate_edit_without_a_record_fails_and_names_the_rule(repo):
    write(repo / "hooks" / "gate.py", "print('loosened')\n")
    receipt = run(repo, approvals=APPROVED_BY_OWNER)
    entry = path_entry(receipt, "hooks/gate.py")
    assert receipt["verdict"] == "fail"
    assert entry["required"] == "standard+authority"
    assert entry["rules"] == ["gate"]


def test_a_quick_record_cannot_cover_a_standard_requirement(repo):
    write(repo / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["requests==2.32.0", "rich"]\n')
    quick_record(repo, "bump-deps", "`pyproject.toml`")
    receipt = run(repo)
    assert receipt["verdict"] == "fail"
    assert path_entry(receipt, "pyproject.toml")["covered_by"] == []


def test_a_new_standard_record_naming_the_path_covers_it(repo):
    write(repo / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["requests==2.32.0", "rich"]\n')
    standard_record(repo, "add-rich", "`pyproject.toml`")
    receipt = run(repo)
    assert receipt["verdict"] == "pass", receipt["failures"]
    assert path_entry(receipt, "pyproject.toml")["covered_by"] == [".nuclear/changes/add-rich"]
    assert receipt["skills"] == ["vetting-outside-code-and-models"]


def test_a_record_that_does_not_name_the_path_does_not_cover_it(repo):
    write(repo / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["rich"]\n')
    standard_record(repo, "unrelated", "`src/other.py`")
    assert run(repo)["verdict"] == "fail"


def test_a_parent_directory_or_glob_in_risk_md_names_the_path(repo):
    write(repo / "src" / "app.py", "MODEL = 'claude-opus-5-5'\n")
    standard_record(repo, "swap-model", "`src/**`")
    assert run(repo)["verdict"] == "pass"


# ------------------------------------------------------------------ records as evidence


def test_editing_an_existing_record_never_covers_new_work(repo):
    write(repo / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["rich"]\n')
    risk = repo / ".nuclear" / "changes" / "old-record" / "risk.md"
    risk.write_text(risk.read_text().replace("- **Mode:** Quick", "- **Mode:** Standard\n\n`pyproject.toml`"))
    receipt = run(repo)
    assert receipt["verdict"] == "fail"
    assert path_entry(receipt, ".nuclear/changes/old-record/risk.md")["rules"] == ["record-edit"]


def test_record_edit_needs_quick_and_record_delete_needs_standard(repo):
    proof = repo / ".nuclear" / "changes" / "old-record" / "proof.md"
    proof.write_text(proof.read_text() + "\nUpdated.\n")
    assert path_entry(run(repo), ".nuclear/changes/old-record/proof.md")["required"] == "quick"
    git(repo, "rm", "-q", "-r", "-f", ".nuclear/changes/old-record")
    receipt = run(repo)
    assert path_entry(receipt, ".nuclear/changes/old-record/risk.md")["required"] == "standard"


def test_a_closed_record_does_not_cover(repo):
    write(repo / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["rich"]\n')
    packet = standard_record(repo, "closed-one", "`pyproject.toml`")
    (packet / "ship.md").write_text((packet / "ship.md").read_text() + "\nNUCLEAR-GRADE-CLOSED: superseded\n")
    assert run(repo)["verdict"] == "fail"


def test_new_record_files_themselves_are_at_the_floor(repo):
    quick_record(repo, "notes", "`docs/`")
    receipt = run(repo)
    assert receipt["verdict"] == "pass-floor"


# ------------------------------------------------------------------ content and claim rules


def test_model_id_in_code_fires_but_the_same_string_in_docs_does_not(repo):
    write(repo / "src" / "app.py", "MODEL = 'claude-opus-5-5'\n")
    assert path_entry(run(repo), "src/app.py")["rules"] == ["model-id"]
    git(repo, "checkout", "-q", "--", "src/app.py")
    write(repo / "docs" / "models.md", "We tested with claude-opus-5-5.\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_net_new_assurance_claim_requires_standard(repo):
    write(repo / "README.md", "# Demo\n\nA small tool. It is SOC 2 compliant.\n")
    entry = path_entry(run(repo), "README.md")
    assert entry["required"] == "standard"
    assert "assurance" in entry["rules"]


def test_negated_claim_lines_stay_at_the_floor(repo):
    write(repo / "README.md", "# Demo\n\nA small tool. It is not SOC 2 compliant and is not certified.\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_general_claim_wording_requires_quick(repo):
    write(repo / "README.md", "# Demo\n\nA small tool with proven results.\n")
    entry = path_entry(run(repo), "README.md")
    assert entry["required"] == "quick"
    assert entry["rules"] == ["claims"]


def test_efficacy_number_requires_standard(repo):
    write(repo / "README.md", "# Demo\n\nSkills improve agent performance by 40% on average.\n")
    assert path_entry(run(repo), "README.md")["required"] == "standard"


def test_rewording_a_line_that_already_carried_the_claim_adds_nothing(repo):
    write(repo / "README.md", "# Demo\n\nThe tool is guaranteed to finish.\n")
    git(repo, "commit", "-qam", "claim already present")  # moves main: the claim is now in the base
    write(repo / "README.md", "# Demo\n\nThe tool is guaranteed to finish quickly.\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_a_typo_fix_stays_at_the_floor(repo):
    write(repo / "README.md", "# Demo\n\nA smal tool. It does not claim compliance with anything.\n")
    assert run(repo)["verdict"] == "pass-floor"


# ------------------------------------------------------------------ renames and the policy itself


def test_moving_a_gate_file_counts_both_paths(repo):
    git(repo, "mv", "hooks/gate.py", "src/gate.py")
    receipt = run(repo)
    assert path_entry(receipt, "hooks/gate.py")["status"] == "D"
    assert path_entry(receipt, "hooks/gate.py")["rules"] == ["gate"]
    assert any(entry["path"] == "src/gate.py" for entry in receipt["paths"])


def test_changing_the_policy_requires_the_top_mode_and_the_base_policy_still_applies(repo):
    loosened = dict(POLICY, rules=[r for r in POLICY["rules"] if r["id"] != "gate"])
    write(repo / consequence.POLICY_PATH, json.dumps(loosened))
    write(repo / "hooks" / "gate.py", "print('loosened')\n")
    receipt = run(repo)
    assert path_entry(receipt, consequence.POLICY_PATH)["rules"] == ["policy-self"]
    assert path_entry(receipt, consequence.POLICY_PATH)["required"] == "standard+authority"
    assert path_entry(receipt, "hooks/gate.py")["rules"] == ["gate"]  # read from base, not head


# ------------------------------------------------------------------ human approval


def test_standard_authority_passes_only_with_a_human_approval_from_another_account(repo):
    write(repo / "hooks" / "gate.py", "print('narrowed')\n")
    standard_record(repo, "narrow-gate", "`hooks/gate.py`", authority=True)
    assert run(repo, pr_author="owner")["verdict"] == "fail"  # no review
    assert run(repo, pr_author="owner", approvals=APPROVED_BY_OWNER)["verdict"] == "fail"  # self-approval
    bot = [{"user": {"login": "agent-bot"}, "state": "APPROVED"}]
    assert run(repo, pr_author="owner", approvals=bot)["verdict"] == "fail"  # bot identity
    app = [{"user": {"login": "some-app[bot]"}, "state": "APPROVED"}]
    assert run(repo, pr_author="owner", approvals=app)["verdict"] == "fail"  # any bot
    human = [{"user": {"login": "reviewer"}, "state": "APPROVED"}]
    receipt = run(repo, pr_author="agent-bot", approvals=human)
    assert receipt["verdict"] == "pass", receipt["failures"]
    assert receipt["approvals"]["human_approvers"] == ["reviewer"]


def test_a_later_changes_requested_review_withdraws_the_approval(repo):
    write(repo / "hooks" / "gate.py", "print('narrowed')\n")
    standard_record(repo, "narrow-gate", "`hooks/gate.py`", authority=True)
    reviews = [{"user": {"login": "reviewer"}, "state": "APPROVED"},
               {"user": {"login": "reviewer"}, "state": "CHANGES_REQUESTED"}]
    assert run(repo, pr_author="agent-bot", approvals=reviews)["verdict"] == "fail"


def test_standard_authority_needs_the_authority_record(repo):
    write(repo / "hooks" / "gate.py", "print('narrowed')\n")
    standard_record(repo, "narrow-gate", "`hooks/gate.py`", authority=False)
    human = [{"user": {"login": "reviewer"}, "state": "APPROVED"}]
    assert run(repo, pr_author="agent-bot", approvals=human)["verdict"] == "fail"


# ------------------------------------------------------------------ overrides and the dependency lane


def _override(packet: Path, rule: str) -> None:
    risk = packet / "risk.md"
    risk.write_text(risk.read_text() + f"\n## Policy override\n\n- **Rule:** `{rule}`\n- **Why the rule does not fit:** comment-only edit\n")


def test_an_approved_override_lowers_an_overridable_rule_to_quick(repo):
    write(repo / "src" / "checker.py", "def check():\n    # clarify\n    return True\n")
    packet = quick_record(repo, "checker-comment", "`src/checker.py`")
    _override(packet, "checker")
    assert run(repo, pr_author="agent-bot")["verdict"] == "fail"  # override without approval
    receipt = run(repo, pr_author="agent-bot", approvals=[{"user": {"login": "reviewer"}, "state": "APPROVED"}])
    assert receipt["verdict"] == "pass", receipt["failures"]
    assert receipt["overrides"][0]["to"] == "quick"


def test_a_non_overridable_rule_cannot_be_overridden(repo):
    write(repo / "hooks" / "gate.py", "print('x')\n")
    packet = quick_record(repo, "gate-x", "`hooks/gate.py`")
    _override(packet, "gate")
    receipt = run(repo, pr_author="agent-bot", approvals=[{"user": {"login": "reviewer"}, "state": "APPROVED"}])
    assert receipt["verdict"] == "fail"
    assert any("not overridable" in failure for failure in receipt["failures"])


def test_dependency_lane_covers_pin_bumps_with_a_human_approval(repo):
    write(repo / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["requests==2.32.3"]\n')
    assert run(repo, pr_author="dependabot[bot]")["verdict"] == "fail"  # lane still needs a human
    receipt = run(repo, pr_author="dependabot[bot]", approvals=[{"user": {"login": "reviewer"}, "state": "APPROVED"}])
    assert receipt["verdict"] == "pass", receipt["failures"]
    assert receipt["approvals"]["dependency_lane"] is True


def test_dependency_lane_rejects_non_pin_changes(repo):
    write(repo / "pyproject.toml", '[project]\nname = "demo"\ndependencies = ["requests==2.32.3", "evil"]\n')
    receipt = run(repo, pr_author="dependabot[bot]", approvals=[{"user": {"login": "reviewer"}, "state": "APPROVED"}])
    assert receipt["approvals"]["dependency_lane"] is False
    assert receipt["verdict"] == "fail"


# ------------------------------------------------------------------ git modes, policy errors, CLI


def test_untracked_files_count_in_working_tree_mode(repo):
    write(repo / "hooks" / "new_hook.py", "print('new')\n")
    assert path_entry(run(repo), "hooks/new_hook.py")["status"] == "A"


def test_committed_head_is_evaluated_between_refs(repo):
    git(repo, "checkout", "-q", "-b", "feature")
    write(repo / "hooks" / "gate.py", "print('x')\n")
    git(repo, "commit", "-qam", "edit gate")
    receipt = run(repo, head=git(repo, "rev-parse", "HEAD"))
    assert path_entry(receipt, "hooks/gate.py")["status"] == "M"


def test_missing_policy_falls_back_to_the_builtin_trust_surfaces(tmp_path):
    root = tmp_path / "bare"
    write(root / "hooks" / "x.py", "a\n")
    git(root, "init", "-q", "-b", "main")
    git(root, "add", "-A")
    git(root, "commit", "-qm", "base")
    write(root / "hooks" / "x.py", "b\n")
    policy = consequence.load_policy(root, "main")
    assert policy.source.startswith("built-in")
    receipt = consequence.evaluate(root, "main", None, policy)
    assert path_entry(receipt, "hooks/x.py")["required"] == "standard+authority"


@pytest.mark.parametrize("bad, message", [
    ({"rules": [{"id": "a", "mode": "extreme", "paths": ["x"]}]}, "unknown mode"),
    ({"rules": [{"id": "a", "mode": "quick", "paths": ["x"]}, {"id": "a", "mode": "quick", "paths": ["y"]}]},
     "duplicate rule id"),
    ({"rules": [{"id": "a", "mode": "quick", "paths": ["x"], "content": "("}]}, "bad 'content' regex"),
    ({"rules": [{"id": "a", "mode": "quick", "paths": []}]}, "non-empty list"),
    ({"default": "maybe"}, "unknown default"),
    ({"rules": [{"id": "a", "mode": "quick", "paths": ["x"], "claims": "vibes"}]}, "'claims' must be"),
])
def test_malformed_policy_fails_closed(bad, message):
    with pytest.raises(consequence.PolicyError, match=message):
        consequence.parse_policy(bad)


def _cli(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(ROOT / "tools" / "ng.py"), "required-mode", "--repo", str(repo), *args],
                          capture_output=True, text=True)


def test_cli_exit_codes_and_receipt_schema(repo):
    assert _cli(repo, "--base", "main").returncode == 0
    write(repo / "hooks" / "gate.py", "print('x')\n")
    failing = _cli(repo, "--base", "main", "--json")
    assert failing.returncode == 1
    receipt = json.loads(failing.stdout)
    assert receipt["schema"] == consequence.SCHEMA and receipt["schema_version"] == 1
    assert {"base", "head", "policy", "required_mode", "verdict", "paths", "packets", "approvals",
            "overrides", "skills", "failures", "boundary"} <= set(receipt)
    assert _cli(repo, "--base", "main", "--advisory").returncode == 0
    assert _cli(repo, "--base", "no-such-ref").returncode == 2
    write(repo / "bad.json", "{not json")
    assert _cli(repo, "--base", "main", "--policy-file", str(repo / "bad.json")).returncode == 2


def test_cli_rejects_a_head_that_is_not_checked_out(repo):
    git(repo, "checkout", "-q", "-b", "feature")
    write(repo / "src" / "app.py", "X = 1\n")
    git(repo, "commit", "-qam", "feature")
    git(repo, "checkout", "-q", "main")
    assert _cli(repo, "--base", "main", "--head", "feature").returncode == 2


def test_cli_print_table_lists_every_rule(repo):
    out = _cli(repo, "--base", "main", "--print-table").stdout
    for rule in POLICY["rules"]:
        assert f"`{rule['id']}`" in out


# ------------------------------------------------------------------ false positives found by the backtest


def test_negation_earlier_in_the_sentence_spans_lines(repo):
    write(repo / "README.md", "# Demo\n\nA small tool. It does not create:\n"
                               "compliance, certified quality assurance program status,\n"
                               "or SOC 2 coverage.\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_quoted_examples_of_forbidden_wording_are_not_claims(repo):
    write(repo / "docs" / "style.md", "Avoid phrases like “nuclear-compliant” or \"SOC 2 certified\".\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_citation_titles_with_bare_nouns_are_not_claims(repo):
    write(repo / "docs" / "refs.md", "9. NASA handbook, *SWE-136: Software Tool Accreditation*.\n"
                                      "10. Compliance-by-Construction Argument Graphs (preprint).\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_a_claim_after_an_unrelated_negated_sentence_still_counts(repo):
    write(repo / "README.md", "# Demo\n\nThis is not slow. It is SOC 2 compliant.\n")
    assert path_entry(run(repo), "README.md")["required"] == "standard"


def test_a_list_continues_its_negated_lead_in(repo):
    write(repo / "docs" / "claims.md", "## What not to claim\n\nDo not state or imply that the tool:\n\n"
                                        "- is endorsed by any regulator;\n- is certified against any standard.\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_emphasis_does_not_hide_a_negation(repo):
    write(repo / "docs" / "style.md", "Do **not** say *is endorsed by* either project.\n")
    assert run(repo)["verdict"] == "pass-floor"


def test_a_list_after_a_positive_lead_in_still_counts(repo):
    write(repo / "README.md", "# Demo\n\nThe tool is:\n\n- endorsed by the regulator;\n- fast.\n")
    assert path_entry(run(repo), "README.md")["required"] == "standard"
