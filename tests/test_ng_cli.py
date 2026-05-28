import shutil
import subprocess
import sys
from pathlib import Path

from tests.test_ng_validate import minimal_quick_packet
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


def test_validate_delegates_to_packet_validator(tmp_path):
    packet = minimal_quick_packet(tmp_path)

    result = run_ng("validate", str(packet))

    assert result.returncode == 0, result.stderr
    assert "OK:" in result.stdout


def test_doctor_passes_on_this_repo():
    result = run_ng("doctor", str(ROOT))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK:" in result.stdout


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
    assert "missing ## Legal/assurance boundary note" in result.stdout


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
