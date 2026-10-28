import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from nuclear_grade.ng_validate import CLOSURE_MARKER
from nuclear_grade.skill_catalog import load_catalog
from tests.test_ng_validate import (
    COMMON_TAIL,
    add_decision_authority,
    minimal_quick_packet,
    minimal_standard_packet,
)
from tools import ng as ng_cli

ROOT = Path(__file__).resolve().parents[1]
NG = ROOT / "tools" / "ng.py"


def run_ng(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(NG), *args],
        cwd=cwd,
        check=False,
        text=True,
        capture_output=True,
    )


def scaffold_repo(
    repo: Path,
    *,
    missing_public_files: tuple[str, ...] = (),
    missing_templates: tuple[tuple[str, str], ...] = (),
    include_catalog: bool = True,
    skill_sections: tuple[str, ...] = ng_cli.REQUIRED_SKILL_SECTIONS,
    command_sections: tuple[str, ...] = ng_cli.REQUIRED_COMMAND_SECTIONS,
) -> Path:
    for public_file in ng_cli.REQUIRED_PUBLIC_FILES:
        if public_file not in missing_public_files:
            (repo / public_file).write_text(f"# {public_file}\n", encoding="utf-8")

    for mode, files in (("quick", ng_cli.QUICK_FILES), ("standard", ng_cli.STANDARD_FILES)):
        for name in files:
            if (mode, name) in missing_templates:
                continue
            path = repo / "templates" / mode / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# {mode} {name} from repo\n", encoding="utf-8")

    for name in ng_cli.CM_FILES:
        if ("cm", name) in missing_templates:
            continue
        path = repo / "templates" / "cm" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# cm {name} from repo\n", encoding="utf-8")

    for name in ng_cli.GOLDEN_PATH_FILES:
        if ("golden-path", name) in missing_templates:
            continue
        path = repo / "templates" / "golden-path" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# golden-path {name} from repo\n", encoding="utf-8")

    for name in ng_cli.OPTIONAL_FILES:
        if ("optional", name) in missing_templates:
            continue
        path = repo / "templates" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# optional {name} from repo\n", encoding="utf-8")

    if include_catalog:
        (repo / "nuclear-grade.yaml").write_text("name: test-catalog\n", encoding="utf-8")

    skill = repo / "skills" / "sample" / "SKILL.md"
    skill.parent.mkdir(parents=True, exist_ok=True)
    skill.write_text(build_skill_contract(skill_sections), encoding="utf-8")

    command = repo / "commands" / "sample.md"
    command.parent.mkdir(parents=True, exist_ok=True)
    command.write_text(build_command_contract(command_sections), encoding="utf-8")
    return repo


def build_skill_contract(sections: tuple[str, ...]) -> str:
    body = "\n\n".join(f"{section}\n\nplaceholder" for section in sections)
    return "---\nname: sample\ndescription: sample\n---\n\n# Sample Skill\n\n" + body + "\n"


def build_command_contract(sections: tuple[str, ...]) -> str:
    return "# Sample Command\n\n" + "\n\n".join(f"{section}\n\nplaceholder" for section in sections) + "\n"


def test_init_dry_run_is_non_mutating(tmp_path):
    result = run_ng("init", str(tmp_path), "--dry-run")

    assert result.returncode == 0
    assert "would create" in result.stdout
    assert not (tmp_path / ".nuclear").exists()


def test_init_creates_nuclear_workspace(tmp_path):
    result = run_ng("init", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert (tmp_path / ".nuclear" / "README.md").exists()
    assert (tmp_path / ".nuclear" / "changes").is_dir()


def test_init_creates_charter_and_mission_anchor(tmp_path):
    result = run_ng("init", str(tmp_path))

    assert result.returncode == 0, result.stderr
    charter = tmp_path / ".nuclear" / "charter.md"
    mission = tmp_path / ".nuclear" / "mission.md"
    assert charter.exists()
    assert mission.exists()
    assert "Ownership" in charter.read_text(encoding="utf-8")
    assert "Non-goals" in mission.read_text(encoding="utf-8")


def test_new_quick_packet_copies_templates(tmp_path):
    scaffold_repo(tmp_path)
    result = run_ng("new", "demo", "--mode", "quick", "--repo", str(tmp_path))

    assert result.returncode == 0, result.stderr
    packet = tmp_path / ".nuclear" / "changes" / "demo"
    assert (packet / "risk.md").exists()
    assert (packet / "proof.md").exists()
    assert (packet / "risk.md").read_text(encoding="utf-8") == "# quick risk.md from repo\n"
    assert (packet / "proof.md").read_text(encoding="utf-8") == "# quick proof.md from repo\n"


def test_new_standard_packet_copies_templates(tmp_path):
    scaffold_repo(tmp_path)
    result = run_ng("new", "demo", "--mode", "standard", "--repo", str(tmp_path))

    assert result.returncode == 0, result.stderr
    packet = tmp_path / ".nuclear" / "changes" / "demo"
    assert {path.name for path in packet.glob("*.md")} == {
        "risk.md",
        "basis.md",
        "plan.md",
        "trace.md",
        "verification.md",
        "ship.md",
    }
    assert (packet / "risk.md").read_text(encoding="utf-8") == "# standard risk.md from repo\n"
    assert (packet / "ship.md").read_text(encoding="utf-8") == "# standard ship.md from repo\n"


def test_new_refuses_overwrite_without_force(tmp_path):
    scaffold_repo(tmp_path)
    assert run_ng("new", "demo", "--mode", "quick", "--repo", str(tmp_path)).returncode == 0

    result = run_ng("new", "demo", "--mode", "quick", "--repo", str(tmp_path))

    assert result.returncode != 0
    assert "already exists" in result.stderr


def test_new_falls_back_to_bundled_templates_for_initialized_workspace(tmp_path):
    scaffold_repo(tmp_path, missing_templates=(("quick", "proof.md"),))

    result = run_ng("new", "demo", "--mode", "quick", "--repo", str(tmp_path))

    assert result.returncode == 0, result.stderr
    packet = tmp_path / ".nuclear" / "changes" / "demo"
    assert (packet / "risk.md").exists()
    assert (packet / "proof.md").exists()
    assert "# Quick Risk Template" in (packet / "risk.md").read_text(encoding="utf-8")


def test_doctor_checks_cm_templates(tmp_path):
    scaffold_repo(tmp_path, missing_templates=(("cm", "baseline.md"),))

    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 1
    assert "missing template: templates/cm/baseline.md" in result.stdout


def test_doctor_checks_golden_path_templates(tmp_path):
    scaffold_repo(tmp_path, missing_templates=(("golden-path", "questioning-attitude.md"),))

    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 1
    assert "missing template: templates/golden-path/questioning-attitude.md" in result.stdout


def test_doctor_checks_optional_templates(tmp_path):
    scaffold_repo(tmp_path, missing_templates=(("optional", "standard/supplier-trust.md"),))

    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 1
    assert "missing template: templates/standard/supplier-trust.md" in result.stdout


def test_list_includes_golden_path_templates():
    result = run_ng("list")

    assert result.returncode == 0, result.stderr
    assert "Golden path files:" in result.stdout
    assert "questioning-attitude.md" in result.stdout
    assert "turnover.md" in result.stdout
    assert "self-check.md" in result.stdout
    assert "Optional files:" in result.stdout
    assert "standard/supplier-trust.md" in result.stdout
    assert "standard/decision-authority.md" in result.stdout


def test_validate_delegates_to_packet_validator(tmp_path):
    packet = minimal_quick_packet(tmp_path)

    result = run_ng("validate", str(packet))

    assert result.returncode == 0, result.stderr
    assert "OK:" in result.stdout


def test_validate_strict_custody_flag_changes_legacy_packet_exit(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    (packet / "verification.md").write_text(
        "# Verification\n\n## Result\n\n- Status: pass\n- Evidence: test\n" + COMMON_TAIL,
        encoding="utf-8",
    )

    compatible = run_ng("validate", str(packet))
    strict = run_ng("validate", str(packet), "--strict-custody")

    assert compatible.returncode == 0, compatible.stdout
    assert strict.returncode != 0
    assert "missing required section: Evidence custody and coupling" in strict.stdout


def test_validate_strict_authority_flag_requires_authority_record(tmp_path):
    packet = minimal_standard_packet(tmp_path)

    result = run_ng("validate", str(packet), "--strict-authority")

    assert result.returncode != 0
    assert "missing required file: decision-authority.md" in result.stdout


def test_validate_strict_authority_flag_accepts_complete_record(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    add_decision_authority(packet)

    result = run_ng("validate", str(packet), "--strict-authority")

    assert result.returncode == 0, result.stdout + result.stderr


def test_doctor_passes_on_this_repo():
    result = run_ng("doctor", str(ROOT))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK:" in result.stdout


def test_decisions_rolls_up_every_skill_contract():
    result = run_ng("decisions", str(ROOT))

    assert result.returncode == 0, result.stdout + result.stderr
    # The operator receipt promotes block/warn; the summary accounts for every skill.
    assert "Operator receipt" in result.stdout
    assert "30 skills:" in result.stdout
    assert "block" in result.stdout and "warn" in result.stdout
    assert "checking-release-readiness" in result.stdout
    assert "ship.md" in result.stdout
    # No skill should be missing a tier (that line only prints on a gap).
    assert "Missing a declarable tier" not in result.stdout


def test_doctor_passes_on_initialized_workspace(tmp_path):
    assert run_ng("init", str(tmp_path)).returncode == 0

    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK:" in result.stdout


def test_doctor_reports_uninitialized_workspace(tmp_path):
    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 1
    assert "missing initialized workspace: .nuclear" in result.stdout


def test_doctor_requires_repo_local_catalog(tmp_path):
    scaffold_repo(tmp_path, include_catalog=False)

    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 1
    assert "missing nuclear-grade.yaml" in result.stdout


def test_doctor_uses_repo_relative_skill_and_command_contracts(tmp_path):
    scaffold_repo(
        tmp_path,
        skill_sections=ng_cli.REQUIRED_SKILL_SECTIONS[:-1],
        command_sections=ng_cli.REQUIRED_COMMAND_SECTIONS[:-1],
    )

    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 1
    assert str(tmp_path / "skills" / "sample" / "SKILL.md") in result.stdout
    assert "missing ## Source-lineage note" in result.stdout
    assert str(tmp_path / "commands" / "sample.md") in result.stdout
    assert "missing ## Verification" in result.stdout


def test_doctor_checks_additional_public_docs(tmp_path):
    scaffold_repo(tmp_path, missing_public_files=("ROADMAP.md",))

    result = run_ng("doctor", str(tmp_path))

    assert result.returncode == 1
    assert "missing public file: ROADMAP.md" in result.stdout


def test_new_packet_from_real_templates_fails_validation_until_marker_removed(tmp_path):
    shutil.copytree(ROOT / "templates", tmp_path / "templates")
    (tmp_path / "nuclear-grade.yaml").write_text("name: test-catalog\n", encoding="utf-8")

    assert run_ng("new", "demo", "--mode", "quick", "--repo", str(tmp_path)).returncode == 0

    packet = tmp_path / ".nuclear" / "changes" / "demo"
    result = run_ng("validate", str(packet))

    assert result.returncode != 0, result.stdout
    assert "still contains the placeholder marker" in result.stdout


def test_status_detects_active_packets(tmp_path):
    scaffold_repo(tmp_path)
    assert run_ng("new", "demo", "--mode", "standard", "--repo", str(tmp_path)).returncode == 0

    result = run_ng("status", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "demo: standard" in result.stdout


def test_status_flags_unfilled_scaffold_packet(tmp_path):
    shutil.copytree(ROOT / "templates", tmp_path / "templates")
    (tmp_path / "nuclear-grade.yaml").write_text("name: test-catalog\n", encoding="utf-8")
    assert run_ng("new", "draft", "--mode", "quick", "--repo", str(tmp_path)).returncode == 0

    result = run_ng("status", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "draft: quick  [scaffold]" in result.stdout
    assert "need attention" in result.stdout


def _closing_quick_packet(tmp_path, slug):
    shutil.copytree(ROOT / "templates", tmp_path / "templates")
    (tmp_path / "nuclear-grade.yaml").write_text("name: test-catalog\n", encoding="utf-8")
    assert run_ng("new", slug, "--mode", "quick", "--repo", str(tmp_path)).returncode == 0
    return tmp_path / ".nuclear" / "changes" / slug / "risk.md"


def test_status_marks_closed_packet_as_terminal(tmp_path):
    # An abandoned packet kept as a record still carries the placeholder marker,
    # but a NUCLEAR-GRADE-CLOSED: line with a rationale makes it a terminal state.
    risk = _closing_quick_packet(tmp_path, "dropped")
    risk.write_text(
        f"{CLOSURE_MARKER}: feature cut in planning; superseded by demo. Closed by maintainer.\n"
        + risk.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    result = run_ng("status", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "dropped: quick  [closed]" in result.stdout
    assert "need attention" not in result.stdout


def test_status_does_not_treat_bare_or_prose_marker_as_closed(tmp_path):
    # A bare marker with no rationale, or the marker merely mentioned in prose,
    # must NOT suppress an otherwise-scaffold packet from needing attention.
    risk = _closing_quick_packet(tmp_path, "fake")
    risk.write_text(
        f"We should document the {CLOSURE_MARKER} marker someday.\n"
        f"{CLOSURE_MARKER}:\n"
        + risk.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    result = run_ng("status", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "fake: quick  [scaffold]" in result.stdout
    assert "need attention" in result.stdout


def test_status_marks_filled_packet_ok(tmp_path):
    minimal_quick_packet(tmp_path)

    result = run_ng("status", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "quick-demo: quick  [ok]" in result.stdout
    assert "need attention" not in result.stdout


def test_new_cm_packet_scaffolds_all_cm_files(tmp_path):
    scaffold_repo(tmp_path)

    result = run_ng("new", "cm-demo", "--mode", "cm", "--repo", str(tmp_path))

    assert result.returncode == 0, result.stderr
    packet = tmp_path / ".nuclear" / "changes" / "cm-demo"
    assert {path.name for path in packet.glob("*.md")} == set(ng_cli.CM_FILES)


def test_new_golden_path_packet_scaffolds_all_files(tmp_path):
    scaffold_repo(tmp_path)

    result = run_ng("new", "gp-demo", "--mode", "golden-path", "--repo", str(tmp_path))

    assert result.returncode == 0, result.stderr
    packet = tmp_path / ".nuclear" / "changes" / "gp-demo"
    assert {path.name for path in packet.glob("*.md")} == set(ng_cli.GOLDEN_PATH_FILES)


def test_migrate_inserts_standard_mode_block_when_standard_files_present(tmp_path):
    packet = tmp_path / ".nuclear" / "changes" / "legacy"
    packet.mkdir(parents=True)
    (packet / "risk.md").write_text("# Risk\n\nLegacy content with no mode declaration.\n", encoding="utf-8")
    (packet / "plan.md").write_text("# Plan\n", encoding="utf-8")

    result = run_ng("migrate", str(packet))

    assert result.returncode == 0, result.stderr
    text = (packet / "risk.md").read_text(encoding="utf-8")
    assert "## Selected mode" in text
    assert "**Mode:** Standard" in text


def test_migrate_inserts_quick_mode_block_when_only_quick_files_present(tmp_path):
    packet = tmp_path / ".nuclear" / "changes" / "legacy-quick"
    packet.mkdir(parents=True)
    (packet / "risk.md").write_text("# Risk\n\nLegacy quick packet.\n", encoding="utf-8")
    (packet / "proof.md").write_text("# Proof\n", encoding="utf-8")

    result = run_ng("migrate", str(packet))

    assert result.returncode == 0, result.stderr
    text = (packet / "risk.md").read_text(encoding="utf-8")
    assert "**Mode:** Quick" in text


def test_migrate_is_idempotent_when_mode_already_declared(tmp_path):
    packet = tmp_path / ".nuclear" / "changes" / "already-declared"
    packet.mkdir(parents=True)
    (packet / "risk.md").write_text(
        "# Risk\n\n## Selected mode\n\n- **Mode:** Standard\n", encoding="utf-8"
    )

    result = run_ng("migrate", str(packet))

    assert result.returncode == 0, result.stderr
    assert "already declares mode" in result.stdout
    text = (packet / "risk.md").read_text(encoding="utf-8")
    assert text.count("## Selected mode") == 1


def test_scaffold_ci_writes_hardened_workflow(tmp_path):
    result = run_ng("scaffold-ci", str(tmp_path))

    assert result.returncode == 0, result.stderr
    workflow = tmp_path / ".github" / "workflows" / "nuclear-grade.yml"
    assert workflow.exists()
    text = workflow.read_text(encoding="utf-8")
    # F5 hardening: least privilege, safe trigger, no secrets, and it runs the validator.
    assert "permissions:\n  contents: read\n" in text
    assert "on:\n  pull_request:\n" in text
    # `pull_request_target` is *named* in the explanatory banner (why it is avoided), but
    # must never be an actual `on:` trigger key -- check the indented key, not a substring.
    assert "\n  pull_request_target:" not in text
    assert "secrets." not in text
    assert "nuclear-grade validate" in text
    assert "OUT-OF-BAND gate" in text
    assert "actor-controlled" in text
    assert "branch protection" in text  # honest that the gate requires external enforcement
    assert "nuclear-grade==" in text  # the validator is version-pinned for a reproducible gate (Codex P2)


def test_scaffold_ci_emits_parseable_yaml(tmp_path):
    # A deterministic guard that the generated workflow is valid YAML, not merely that
    # the right substrings are present -- a stray indent or quote could satisfy the
    # string asserts above while leaving the file unparseable. Skips locally when PyYAML
    # is absent; CI installs it, so the parse always runs there.
    yaml = pytest.importorskip("yaml")
    assert run_ng("scaffold-ci", str(tmp_path)).returncode == 0
    workflow = tmp_path / ".github" / "workflows" / "nuclear-grade.yml"
    doc = yaml.safe_load(workflow.read_text(encoding="utf-8"))
    assert isinstance(doc, dict)
    # PyYAML (YAML 1.1) parses the bare key `on:` as boolean True; accept either form.
    trigger = doc.get("on", doc.get(True))
    # Exactly `pull_request` -- this also proves `pull_request_target` is not a trigger.
    assert isinstance(trigger, dict) and set(trigger) == {"pull_request"}
    assert doc.get("permissions") == {"contents": "read"}
    assert "validate-change-records" in doc.get("jobs", {})


def test_scaffold_ci_skips_closed_packets(tmp_path):
    # A packet closed via the documented closure path (NUCLEAR-GRADE-CLOSED) is kept
    # for audit history; the validator still rejects its unfilled fields, so the gate
    # must skip closed records rather than block CI forever (Codex). The marker comes
    # from the validator constant, so the workflow can't drift from the closure contract.
    from nuclear_grade.ng_validate import CLOSURE_MARKER

    assert run_ng("scaffold-ci", str(tmp_path)).returncode == 0
    text = (tmp_path / ".github" / "workflows" / "nuclear-grade.yml").read_text(encoding="utf-8")
    assert CLOSURE_MARKER in text
    assert "Skipping closed record" in text


def test_scaffold_ci_dry_run_is_non_mutating(tmp_path):
    result = run_ng("scaffold-ci", str(tmp_path), "--dry-run")

    assert result.returncode == 0, result.stderr
    assert "would create" in result.stdout
    assert not (tmp_path / ".github").exists()


def test_scaffold_ci_refuses_overwrite_without_force(tmp_path):
    assert run_ng("scaffold-ci", str(tmp_path)).returncode == 0

    result = run_ng("scaffold-ci", str(tmp_path))
    assert result.returncode != 0
    assert "already exists" in result.stderr

    assert run_ng("scaffold-ci", str(tmp_path), "--force").returncode == 0


# --- ng init add-ons: --agents, --hook, --ci, --all --------------------------------


def _tree(root: Path) -> dict[str, bytes]:
    return {str(p.relative_to(root)): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


def test_plain_init_still_refuses_existing_files(tmp_path):
    assert run_ng("init", str(tmp_path)).returncode == 0

    result = run_ng("init", str(tmp_path))
    assert result.returncode == 2
    assert "already exists" in result.stderr
    assert not (tmp_path / "AGENTS.md").exists()
    assert not (tmp_path / ".claude").exists()


def test_init_all_dry_run_lists_every_change_and_writes_nothing(tmp_path):
    result = run_ng("init", str(tmp_path), "--all", "--dry-run")

    assert result.returncode == 0, result.stderr
    for rel in ("AGENTS.md", ".claude/hooks/pre_tool_use.py", ".github/workflows/nuclear-grade.yml",
                ".claude/settings.json", ".nuclear/charter.md"):
        assert str(tmp_path / rel) in result.stdout, rel
    assert list(tmp_path.iterdir()) == []


def test_init_all_writes_agents_hook_and_ci(tmp_path):
    result = run_ng("init", str(tmp_path), "--all")

    assert result.returncode == 0, result.stderr
    assert (tmp_path / "AGENTS.md").read_bytes() == (ROOT / "starter-kit" / "core" / "AGENTS.md").read_bytes()
    assert (tmp_path / ".claude" / "hooks" / "pre_tool_use.py").read_bytes() == (
        ROOT / "hooks" / "pre_tool_use.py"
    ).read_bytes()
    assert (tmp_path / ".github" / "workflows" / "nuclear-grade.yml").is_file()
    assert (tmp_path / ".nuclear" / "charter.md").is_file()
    settings = json.loads((tmp_path / ".claude" / "settings.json").read_text(encoding="utf-8"))
    assert settings == {"hooks": {"PreToolUse": [ng_cli.gate_hook_entry(ng_cli.PROJECT_GATE_SCRIPT)]}}


def test_init_ci_matches_scaffold_ci(tmp_path):
    assert run_ng("init", str(tmp_path / "a"), "--ci").returncode == 0
    assert run_ng("scaffold-ci", str(tmp_path / "b")).returncode == 0

    rel = Path(".github") / "workflows" / "nuclear-grade.yml"
    assert (tmp_path / "a" / rel).read_bytes() == (tmp_path / "b" / rel).read_bytes()


def test_init_addon_keeps_existing_files_and_workspace(tmp_path):
    assert run_ng("init", str(tmp_path)).returncode == 0
    (tmp_path / ".nuclear" / "charter.md").write_text("my charter\n", encoding="utf-8")
    (tmp_path / "AGENTS.md").write_text("my agents\n", encoding="utf-8")

    result = run_ng("init", str(tmp_path), "--agents", "--yes")
    assert result.returncode == 0, result.stderr
    # --yes overwrites add-on files only; the workspace records are never replaced by an add-on run.
    assert (tmp_path / ".nuclear" / "charter.md").read_text(encoding="utf-8") == "my charter\n"
    assert "kept existing" in result.stdout
    assert "Agent guidance" in (tmp_path / "AGENTS.md").read_text(encoding="utf-8")

    (tmp_path / "AGENTS.md").write_text("my agents\n", encoding="utf-8")
    result = run_ng("init", str(tmp_path), "--agents")
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "AGENTS.md").read_text(encoding="utf-8") == "my agents\n"
    assert "pass --yes to overwrite" in result.stdout


def test_init_hook_merges_into_existing_settings(tmp_path):
    settings_path = tmp_path / ".claude" / "settings.json"
    settings_path.parent.mkdir()
    other_hook = {"matcher": "Bash", "hooks": [{"type": "command", "command": "echo hi"}]}
    existing = {"model": "x", "permissions": {"deny": ["Read(./.env)"]},
                "hooks": {"PreToolUse": [other_hook], "Stop": []}}
    settings_path.write_text(json.dumps(existing), encoding="utf-8")

    assert run_ng("init", str(tmp_path), "--hook").returncode == 0
    merged = json.loads(settings_path.read_text(encoding="utf-8"))
    assert merged["model"] == "x" and merged["permissions"] == existing["permissions"]
    assert merged["hooks"]["Stop"] == []
    assert merged["hooks"]["PreToolUse"] == [other_hook, ng_cli.gate_hook_entry(ng_cli.PROJECT_GATE_SCRIPT)]

    # Re-running is idempotent: the gate is registered once.
    result = run_ng("init", str(tmp_path), "--hook", "--yes")
    assert result.returncode == 0, result.stderr
    assert "already registered" in result.stdout
    assert json.loads(settings_path.read_text(encoding="utf-8")) == merged


@pytest.mark.parametrize("content", ["{not json", "[]", '{"hooks": []}', '{"hooks": {"PreToolUse": {}}}'])
def test_init_hook_refuses_settings_it_cannot_merge(tmp_path, content):
    settings_path = tmp_path / ".claude" / "settings.json"
    settings_path.parent.mkdir()
    settings_path.write_text(content, encoding="utf-8")

    result = run_ng("init", str(tmp_path), "--hook", "--yes")
    assert result.returncode == 2
    assert "cannot merge" in result.stderr
    assert settings_path.read_text(encoding="utf-8") == content
    assert not (tmp_path / ".nuclear").exists(), "nothing is written when the settings file cannot be merged"


def test_init_hook_dry_run_leaves_settings_untouched(tmp_path):
    settings_path = tmp_path / ".claude" / "settings.json"
    settings_path.parent.mkdir()
    settings_path.write_text('{"model": "x"}', encoding="utf-8")
    before = _tree(tmp_path)

    result = run_ng("init", str(tmp_path), "--hook", "--dry-run")
    assert result.returncode == 0, result.stderr
    assert f"would update: {settings_path}" in result.stdout
    assert _tree(tmp_path) == before
    assert not (tmp_path / ".nuclear").exists()


def test_installed_gate_denies_agent_edits_to_its_own_settings(tmp_path):
    assert run_ng("init", str(tmp_path), "--hook").returncode == 0
    payload = json.dumps({"tool_name": "Edit", "tool_input": {"file_path": ".claude/settings.json"},
                          "cwd": str(tmp_path)})
    proc = subprocess.run([sys.executable, str(tmp_path / ".claude" / "hooks" / "pre_tool_use.py")],
                          input=payload, text=True, capture_output=True, check=False, cwd=tmp_path)
    assert json.loads(proc.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny"


# --- ng install -----------------------------------------------------------------


def test_cli_help_builds_without_loading_lifecycle_catalog(monkeypatch):
    def fail_if_loaded(_root):
        raise AssertionError("catalog loaded during parser construction")

    monkeypatch.setattr(ng_cli, "load_catalog", fail_if_loaded)
    parser = ng_cli.build_parser()

    assert parser.parse_args(["list"]).command == "list"


ALL_SKILLS = sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md"))


def test_install_dry_run_is_non_mutating(tmp_path):
    dest = tmp_path / "skills"
    result = run_ng("install", "codex", "--dry-run", "--dest", str(dest))

    assert result.returncode == 0, result.stderr
    assert "would install" in result.stdout
    assert not dest.exists()


def test_install_core_installs_router_plus_core_seven(tmp_path):
    dest = tmp_path / "skills"
    result = run_ng("install", "codex", "--dest", str(dest))

    assert result.returncode == 0, result.stderr
    installed = sorted(path.name for path in dest.iterdir() if path.is_dir())
    expected_core = [entry.id for entry in load_catalog(ROOT).profile("core")]
    assert installed == sorted(expected_core)
    assert len(installed) == 8
    assert (dest / "using-nuclear-grade" / "SKILL.md").exists()


def test_install_full_installs_every_skill(tmp_path):
    dest = tmp_path / "skills"
    result = run_ng("install", "codex", "--full", "--dest", str(dest))

    assert result.returncode == 0, result.stderr
    installed = sorted(path.name for path in dest.iterdir() if path.is_dir())
    assert installed == ALL_SKILLS
    assert len(installed) >= 20


def test_install_reports_always_on_cost(tmp_path):
    result = run_ng("install", "codex", "--dest", str(tmp_path / "skills"))

    assert result.returncode == 0, result.stderr
    assert "catalog-metadata description cost" in result.stdout


def test_install_is_idempotent_update(tmp_path):
    dest = tmp_path / "skills"
    assert run_ng("install", "codex", "--dest", str(dest)).returncode == 0

    # Re-running refreshes in place rather than refusing like `new` does.
    second = run_ng("install", "codex", "--dest", str(dest))

    assert second.returncode == 0, second.stderr
    assert len([path for path in dest.iterdir() if path.is_dir()]) == 8


def test_install_blocks_premanifest_profile_shrink_with_known_skill_dirs(tmp_path):
    dest = tmp_path / "skills"
    core_ids = {entry.id for entry in load_catalog(ROOT).profile("core")}
    extra = next(name for name in ALL_SKILLS if name not in core_ids)
    (dest / "using-nuclear-grade").mkdir(parents=True)
    (dest / "using-nuclear-grade" / "SKILL.md").write_text("legacy\n", encoding="utf-8")
    (dest / extra).mkdir()
    (dest / extra / "SKILL.md").write_text("legacy\n", encoding="utf-8")

    result = run_ng("install", "codex", "--dest", str(dest))

    assert result.returncode == 2
    assert "pre-manifest Nuclear-grade skill(s) are outside the selected profile" in result.stderr
    assert extra in result.stderr
    assert not (dest / ".nuclear-grade-install.json").exists()


def test_install_blocks_when_previously_owned_skill_becomes_stale(tmp_path):
    dest = tmp_path / "skills"
    assert run_ng("install", "codex", "--dest", str(dest)).returncode == 0

    manifest = json.loads((dest / ".nuclear-grade-install.json").read_text(encoding="utf-8"))
    manifest["skills"].append("obsolete-skill")
    (dest / ".nuclear-grade-install.json").write_text(json.dumps(manifest), encoding="utf-8")
    (dest / "obsolete-skill").mkdir()
    (dest / "obsolete-skill" / "SKILL.md").write_text("stale\n", encoding="utf-8")

    result = run_ng("install", "codex", "--dest", str(dest))

    assert result.returncode == 2
    assert "previously installed skill(s) are no longer in the selected profile" in result.stderr
    assert "obsolete-skill" in result.stderr
    assert (dest / "obsolete-skill" / "SKILL.md").exists()


def test_install_unverified_tool_warns_to_verify_path(tmp_path):
    # VS Code's user path is a best-known default; without --dest the install must flag it.
    result = run_ng("install", "vscode", "--scope", "project", "--repo", str(tmp_path))

    assert result.returncode == 0, result.stderr
    assert "best-known default" in result.stdout
    assert (tmp_path / ".github" / "skills" / "using-nuclear-grade" / "SKILL.md").exists()


def test_install_verified_tool_has_no_verify_note(tmp_path):
    result = run_ng("install", "codex", "--dest", str(tmp_path / "skills"))

    assert "best-known default" not in result.stdout


def test_install_rejects_unknown_tool(tmp_path):
    result = run_ng("install", "emacs", "--dest", str(tmp_path / "skills"))

    assert result.returncode != 0
    assert "invalid choice" in result.stderr


def test_install_dest_resolution_per_tool(tmp_path, monkeypatch):
    monkeypatch.delenv("APPDATA", raising=False)  # force the POSIX VS Code-user path
    repo = tmp_path / "repo"
    home = Path.home()

    assert ng_cli.install_dest("codex", "user", repo) == home / ".agents" / "skills"
    assert ng_cli.install_dest("codex", "project", repo) == repo / ".agents" / "skills"
    assert ng_cli.install_dest("claude", "user", repo) == home / ".claude" / "skills"
    assert ng_cli.install_dest("claude", "project", repo) == repo / ".claude" / "skills"
    assert ng_cli.install_dest("cursor", "project", repo) == repo / ".cursor" / "skills"
    # Windsurf: user scope lives under ~/.codeium; project under .windsurf.
    assert ng_cli.install_dest("windsurf", "user", repo) == home / ".codeium" / "windsurf" / "skills"
    assert ng_cli.install_dest("windsurf", "project", repo) == repo / ".windsurf" / "skills"
    # VS Code + Copilot: project is .github/skills (NOT .vscode); user is ~/.config/github-copilot.
    assert ng_cli.install_dest("vscode", "project", repo) == repo / ".github" / "skills"
    assert ng_cli.install_dest("vscode", "user", repo) == home / ".config" / "github-copilot" / "skills"


# --- ng mcp-config --------------------------------------------------------------


def test_mcp_config_codex_prints_toml(tmp_path):
    result = run_ng("mcp-config", "codex")

    assert result.returncode == 0, result.stderr
    assert "[mcp_servers.nuclear_grade]" in result.stdout
    assert "nuclear_grade.mcp_server" in result.stdout


def test_mcp_config_vscode_uses_servers_key_not_mcpservers(tmp_path):
    result = run_ng("mcp-config", "vscode")

    assert result.returncode == 0, result.stderr
    assert '"servers"' in result.stdout
    assert "mcpServers" not in result.stdout


def test_mcp_config_claude_uses_mcpservers_key(tmp_path):
    result = run_ng("mcp-config", "claude")

    assert result.returncode == 0, result.stderr
    assert "mcpServers" in result.stdout
    assert "claude mcp add" in result.stdout


def test_mcp_config_rejects_unknown_tool(tmp_path):
    result = run_ng("mcp-config", "emacs")

    assert result.returncode != 0
    assert "invalid choice" in result.stderr
