import importlib.util
import json
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODEX_PLUGIN_DIR = ROOT / ".codex-plugin"
MANIFEST_PATH = CODEX_PLUGIN_DIR / "plugin.json"
INSTALL_HELPER = ROOT / "tools" / "install-codex.py"

# Skills are the only surface Codex install exports. The repo also ships
# agents/, commands/, templates/, .nuclear/, and the ng CLI, but those are NOT
# packaged as Codex-native capabilities -- the manifest must not imply they are.
UNSUPPORTED_KEYS = ("agents", "commands", "hooks", "mcpServers", "apps")


def _manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def _pyproject() -> dict:
    return tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))


def _load_install_helper():
    spec = importlib.util.spec_from_file_location("install_codex", INSTALL_HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_codex_manifest_parses_and_names_the_plugin():
    manifest = _manifest()

    assert manifest["name"] == "nuclear-grade"
    assert manifest["description"], "codex plugin needs a description"


def test_codex_manifest_has_required_fields_with_correct_types():
    manifest = _manifest()

    expected_types = {
        "name": str,
        "version": str,
        "description": str,
        "author": dict,
        "homepage": str,
        "repository": str,
        "license": str,
        "keywords": list,
        "skills": str,
        "interface": dict,
    }
    for field, field_type in expected_types.items():
        assert field in manifest, f"codex manifest missing required field: {field}"
        assert isinstance(manifest[field], field_type), (
            f"codex manifest field {field} must be {field_type.__name__}"
        )

    # The two fields Codex plugin validation rejected before this change.
    assert manifest["author"].get("name"), "author object must carry a name"
    assert isinstance(manifest["author"]["name"], str)


def test_codex_interface_carries_display_metadata():
    interface = _manifest()["interface"]

    expected_types = {
        "displayName": str,
        "developerName": str,
        "category": str,
        "capabilities": list,
        "defaultPrompt": list,
    }
    for field, field_type in expected_types.items():
        assert field in interface, f"codex interface missing {field}"
        assert isinstance(interface[field], field_type), (
            f"codex interface field {field} must be {field_type.__name__}"
        )

    assert interface["capabilities"], "interface should list at least one capability"
    assert 1 <= len(interface["defaultPrompt"]) <= 3, (
        "interface.defaultPrompt should hold 1-3 short prompts"
    )


def test_default_prompts_stay_under_the_codex_128_char_limit():
    # Verified constraint: the Codex manifest loader ignores any
    # interface.defaultPrompt entry longer than 128 characters
    # ("prompt must be at most 128 characters"). Keep every prompt under it so
    # none is silently dropped on install.
    for index, prompt in enumerate(_manifest()["interface"]["defaultPrompt"]):
        assert isinstance(prompt, str)
        assert len(prompt) <= 128, (
            f"defaultPrompt[{index}] is {len(prompt)} chars; Codex caps prompts at 128"
        )


def test_codex_plugin_version_tracks_pyproject():
    # One source of truth for the version; guard the mirror against drift.
    assert _manifest()["version"] == _pyproject()["project"]["version"]


def test_codex_plugin_points_at_an_existing_skill_catalog():
    skills = _manifest()["skills"]
    assert skills, "codex plugin must reference the shipped skills"

    skills_dir = (ROOT / skills).resolve()
    assert skills_dir.is_dir(), f"skills must point at an existing directory, got {skills}"
    assert skills_dir == (ROOT / "skills").resolve()


def test_every_exported_skill_folder_has_a_skill_md():
    skills_dir = (ROOT / _manifest()["skills"]).resolve()

    skill_dirs = [child for child in skills_dir.iterdir() if child.is_dir()]
    assert skill_dirs, "expected skill folders under the exported skills directory"
    for child in skill_dirs:
        assert (child / "SKILL.md").is_file(), (
            f"exported skill folder {child.name} is missing SKILL.md"
        )


def test_codex_manifest_does_not_imply_native_agents_or_commands():
    # Codex install exports skills only. Advertising agents/commands/hooks/etc.
    # as top-level manifest keys would imply Codex installs them natively -- it
    # does not. Keep the export boundary honest.
    manifest = _manifest()
    for key in UNSUPPORTED_KEYS:
        assert key not in manifest, (
            f"manifest must not declare '{key}': Codex install does not package it as a native capability"
        )


def test_codex_manifest_has_no_placeholder_text():
    assert "[TODO:" not in MANIFEST_PATH.read_text(encoding="utf-8"), (
        "codex manifest still contains a [TODO: placeholder"
    )


def test_install_helper_validates_the_shipped_manifest():
    helper = _load_install_helper()
    assert helper.validate_manifest(_manifest()) == []


def test_install_helper_flags_a_broken_manifest():
    helper = _load_install_helper()

    broken = _manifest()
    broken["author"] = "FlyFission"  # string, not an object
    broken["interface"] = "rich"  # string, not an object
    broken["agents"] = "./agents/"  # implies a native capability that is not shipped

    errors = helper.validate_manifest(broken)
    assert any("author" in error for error in errors)
    assert any("interface" in error for error in errors)
    assert any("agents" in error for error in errors)


def test_install_helper_flags_an_overlong_default_prompt():
    helper = _load_install_helper()

    over_limit = _manifest()
    over_limit["interface"]["defaultPrompt"] = ["x" * 129]

    errors = helper.validate_manifest(over_limit)
    assert any("128" in error and "defaultPrompt" in error for error in errors)


def test_install_helper_check_mode_passes_for_the_repo():
    result = subprocess.run(
        [sys.executable, str(INSTALL_HELPER), "--check"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "valid Codex plugin manifest" in result.stdout
