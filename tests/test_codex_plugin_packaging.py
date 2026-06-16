import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODEX_PLUGIN_DIR = ROOT / ".codex-plugin"


def _manifest() -> dict:
    return json.loads((CODEX_PLUGIN_DIR / "plugin.json").read_text(encoding="utf-8"))


def _pyproject() -> dict:
    return tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))


def test_codex_manifest_parses_and_names_the_plugin():
    manifest = _manifest()

    assert manifest["name"] == "nuclear-grade"
    assert manifest["description"], "codex plugin needs a description"


def test_codex_plugin_version_tracks_pyproject():
    # One source of truth for the version; guard the mirror against drift.
    assert _manifest()["version"] == _pyproject()["project"]["version"]


def test_codex_plugin_points_at_the_skill_catalog():
    assert _manifest()["skills"], "codex plugin must reference the shipped skills"
    assert (ROOT / "skills").is_dir()
