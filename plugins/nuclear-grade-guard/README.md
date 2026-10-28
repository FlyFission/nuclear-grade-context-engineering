# nuclear-grade-guard

An opt-in Claude Code plugin with one job: it registers the Nuclear-grade blocking `PreToolUse`
gate. It adds no skills, commands, or agents.

```bash
/plugin marketplace add FlyFission/nuclear-grade-context-engineering
/plugin install nuclear-grade-guard@nuclear-grade
/reload-plugins
```

Turn it off with `/plugin disable nuclear-grade-guard@nuclear-grade`, or remove it with
`/plugin uninstall nuclear-grade-guard@nuclear-grade`.

What it denies, what it asks about, how it fails closed, and where it falls short are in
[`HOOKS.md`](../../HOOKS.md).

## Maintainer note

A plugin is copied into Claude's cache on its own, so `hooks/pre_tool_use.py` here is a copy of the
repo's [`hooks/pre_tool_use.py`](../../hooks/pre_tool_use.py). Edit the original, then refresh the
copy:

```bash
cp hooks/pre_tool_use.py plugins/nuclear-grade-guard/hooks/pre_tool_use.py
```

`tests/test_plugin_packaging.py` fails if the two files differ. The plugin's `version` tracks
`pyproject.toml`, and `python -m nuclear_grade.release` checks it, so a user with the plugin
installed gets a changed gate only after a version bump.

This plugin installs an in-session control. It does not create a sandbox, compliance, or
certification.
