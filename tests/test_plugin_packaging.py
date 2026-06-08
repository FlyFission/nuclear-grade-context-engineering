import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / ".claude-plugin"


def _manifest(name: str) -> dict:
    return json.loads((PLUGIN_DIR / name).read_text(encoding="utf-8"))


def _pyproject() -> dict:
    return tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))


def test_manifests_parse_and_name_the_plugin():
    plugin = _manifest("plugin.json")
    marketplace = _manifest("marketplace.json")

    assert plugin["name"] == "nuclear-grade"
    assert marketplace["name"], "marketplace needs a name"
    assert marketplace["owner"]["name"], "marketplace needs an owner name"


def test_plugin_version_tracks_pyproject():
    # One source of truth for the version; guard the mirror against drift.
    assert _manifest("plugin.json")["version"] == _pyproject()["project"]["version"]


def test_marketplace_lists_the_plugin_at_repo_root():
    entries = {p["name"]: p for p in _manifest("marketplace.json")["plugins"]}

    assert "nuclear-grade" in entries, "marketplace must list the nuclear-grade plugin"
    assert entries["nuclear-grade"]["source"] == "./", (
        "repo-as-marketplace: the plugin source is the repository root"
    )


def test_components_live_at_plugin_root_not_inside_claude_plugin():
    # Claude Code discovers skills/commands/agents/hooks at the plugin ROOT;
    # only the manifests belong in .claude-plugin/.
    assert (ROOT / "skills").is_dir()
    assert (ROOT / "commands").is_dir()
    assert not (PLUGIN_DIR / "skills").exists()
    assert not (PLUGIN_DIR / "commands").exists()

    names = {p.name for p in PLUGIN_DIR.iterdir()}
    assert names == {"plugin.json", "marketplace.json"}, (
        f"unexpected files in .claude-plugin/: {sorted(names)}"
    )


def test_skills_are_discoverable():
    # Auto-discovery needs SKILL.md files under skills/*/.
    skill_files = list((ROOT / "skills").glob("*/SKILL.md"))
    assert len(skill_files) >= 20, f"expected the skill catalog, found {len(skill_files)}"


def test_no_auto_activated_hooks_config():
    # The no-hooks tier rests on Claude Code auto-discovering hooks ONLY from
    # hooks/hooks.json at the plugin root; its absence is what keeps installing the
    # plugin from running any hook. Hook *scripts* may ship for explicit opt-in
    # (see HOOKS.md) -- only hooks/hooks.json auto-activates, so that is what we guard.
    assert not (ROOT / "hooks" / "hooks.json").exists(), (
        "shipping hooks/hooks.json auto-activates hooks on install -- it would break the no-hooks tier"
    )
