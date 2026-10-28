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
    # The main plugin's source is the repo root. Its no-hooks tier rests on Claude Code
    # auto-discovering hooks ONLY from hooks/hooks.json at the plugin root (or a manifest
    # `hooks` key); their absence is what keeps installing the
    # plugin from running any hook. Hook *scripts* may ship for explicit opt-in
    # (see HOOKS.md) -- only hooks/hooks.json auto-activates, so that is what we guard.
    # The opt-in gate lives in the separate nuclear-grade-guard plugin, whose hooks.json
    # sits under plugins/ where the main plugin never loads it.
    assert not (ROOT / "hooks" / "hooks.json").exists(), (
        "shipping hooks/hooks.json auto-activates hooks on install -- it would break the no-hooks tier"
    )
    assert "hooks" not in _manifest("plugin.json")
    main_entry = next(p for p in _manifest("marketplace.json")["plugins"] if p["name"] == "nuclear-grade")
    assert "hooks" not in main_entry


# --- nuclear-grade-guard: the separate, opt-in plugin that registers the PreToolUse gate ---

GUARD_DIR = ROOT / "plugins" / "nuclear-grade-guard"
GUARD_HOOKS = GUARD_DIR / "hooks" / "hooks.json"
GUARD_SCRIPT = GUARD_DIR / "hooks" / "pre_tool_use.py"


def _guard_manifest() -> dict:
    return json.loads((GUARD_DIR / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


def _guard_hooks() -> dict:
    return json.loads(GUARD_HOOKS.read_text(encoding="utf-8"))


def test_marketplace_lists_the_guard_plugin_in_its_own_directory():
    entries = {p["name"]: p for p in _manifest("marketplace.json")["plugins"]}

    assert set(entries) == {"nuclear-grade", "nuclear-grade-guard"}
    assert entries["nuclear-grade-guard"]["source"] == "./plugins/nuclear-grade-guard"
    assert _guard_manifest()["name"] == "nuclear-grade-guard"


def test_guard_version_tracks_pyproject():
    assert _guard_manifest()["version"] == _pyproject()["project"]["version"]


def test_guard_plugin_registers_only_the_pretooluse_gate():
    config = _guard_hooks()
    assert set(config["hooks"]) == {"PreToolUse"}, "the guard registers one event and nothing else"
    [group] = config["hooks"]["PreToolUse"]
    [hook] = group["hooks"]
    assert hook["type"] == "command"
    assert hook["args"] == ["${CLAUDE_PLUGIN_ROOT}/hooks/pre_tool_use.py"], "exec form keeps the path one argument"
    assert hook["onFailure"] == "block", "a crash, timeout, or missing python3 must block the call"
    assert GUARD_SCRIPT.is_file()


def test_guard_plugin_ships_no_other_components():
    # Hooks only: no skills, commands, agents, MCP or LSP servers, bin/ executables, or settings.
    names = {p.name for p in GUARD_DIR.iterdir()}
    assert names <= {".claude-plugin", "hooks", "README.md"}, sorted(names)
    assert {p.name for p in (GUARD_DIR / "hooks").iterdir()} == {"hooks.json", "pre_tool_use.py"}


def test_guard_script_is_an_exact_copy_of_the_gate():
    # A plugin is copied into Claude's cache on its own, so it carries its own copy of the
    # gate. Refresh it with: cp hooks/pre_tool_use.py plugins/nuclear-grade-guard/hooks/
    def normalized(path):
        return path.read_bytes().replace(b"\r\n", b"\n")

    assert normalized(GUARD_SCRIPT) == normalized(ROOT / "hooks" / "pre_tool_use.py"), (
        "plugins/nuclear-grade-guard/hooks/pre_tool_use.py drifted from hooks/pre_tool_use.py"
    )


def test_gate_config_agrees_everywhere_it_is_written():
    # HOOKS.md (copy-paste), the guard plugin, and `init --hook` must register the same gate.
    from nuclear_grade import cli

    [plugin_group] = _guard_hooks()["hooks"]["PreToolUse"]
    init_group = cli.gate_hook_entry(cli.PROJECT_GATE_SCRIPT)
    hooks_doc = (ROOT / "HOOKS.md").read_text(encoding="utf-8")
    doc_line = next(line for line in hooks_doc.splitlines() if "pre_tool_use.py" in line and '"matcher"' in line)
    doc_group = json.loads(doc_line.strip().rstrip(","))

    for group in (init_group, doc_group):
        assert group["matcher"] == plugin_group["matcher"]
        [hook], [plugin_hook] = group["hooks"], plugin_group["hooks"]
        for key in ("type", "command", "timeout", "onFailure"):
            assert hook[key] == plugin_hook[key], key
    assert doc_group["hooks"][0]["args"] == [cli.PROJECT_GATE_SCRIPT]
