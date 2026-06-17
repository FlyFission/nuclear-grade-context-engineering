# Install Nuclear-grade

Nuclear-grade runs inside your repo and is Markdown-first. For Claude Code it also installs as a plugin — two commands, then a reload to activate it (see below). No package registry or hosted service is required either way.

> The `ng` CLI scaffolds and checks packets, but Nuclear-grade is markdown-first. Many adopters only need [`CORE.md`](CORE.md) (the seven habits + the decision matrix) plus one [`starter-kit/`](starter-kit/) directory copied into their repo. The steps below set up the optional CLI.

## Install as a Claude Code plugin

For Claude Code users, this repository is its own plugin marketplace. Add it, install the plugin, then reload to activate it in the current session:

```bash
/plugin marketplace add FlyFission/nuclear-grade-context-engineering
/plugin install nuclear-grade@nuclear-grade
/reload-plugins   # or restart Claude Code — loads the new skills/commands into this session
```

The plugin exposes the existing skills (`skills/`) and command prompts (`commands/`). It configures **no hooks**, so nothing runs automatically when you install it or start a session. Because the marketplace source is the repository root, the install also copies the repo's `ng` Python CLI into Claude's plugin cache — but the plugin adds no `ng` command to your `PATH` and runs nothing on its own. The CLI is a separate, repo-side tool: to use it, work from a checkout of this repo (the **Use in this repo** and **Add to another repo** steps below), not from the plugin install alone.

## Install into Codex, Cursor, Windsurf, or VS Code

Nuclear-grade's skills are plain `SKILL.md` files that every modern agent tool
auto-surfaces by their `description` — the same files work unmodified across
tools. `ng install` places them where each tool looks:

```bash
python tools/ng.py install codex          # ~/.agents/skills (Core set; install once)
python tools/ng.py install codex --full   # all 27 skills
python tools/ng.py install claude         # ~/.claude/skills
python tools/ng.py install cursor         # ~/.cursor/skills
python tools/ng.py install windsurf --scope project --repo .   # .windsurf/skills (project-scoped)
```

Or fan out to every detected tool in one step:

```bash
./install.sh          # Core set into each detected tool
./install.sh --full   # all skills
```

The Core set is the always-first router plus the Core 7 (the lean default);
`--full` adds the rest. The command prints the always-on token cost so you can
keep context lean, and re-running updates in place. See
[`INTEGRATIONS.md`](INTEGRATIONS.md) for per-tool paths, the `--scope`/`--dest`
options, the opt-in MCP server (`nuclear-grade[mcp]`), and how skills compare to
MCP on token cost.

### Codex plugin package

The repo also ships a `.codex-plugin/plugin.json` manifest, so it is a
publishable Codex plugin. The plugin exports the **skills** only — Codex surfaces
them by their `description`. It does **not** package `agents/` (Claude-only PROVE
subagents), `commands/` (paste-ready prompt cards), `templates/`, `.nuclear/`, or
`tools/ng.py` as Codex-native capabilities. Because the flagship skill routes to
repo-local files, **clone the repo too** for the full workflow. After installing,
start a new Codex thread (or restart Codex) so it picks up the new skills. To
validate the manifest and print exact install/restart steps from a checkout:

```bash
python tools/install-codex.py            # validate, then print Codex install guidance
python tools/install-codex.py --check    # validate the manifest only
```

See the Codex section of [`INTEGRATIONS.md`](INTEGRATIONS.md) for the full
export-boundary table and how this differs from the Claude Code plugin.

## Requirements

- Python 3.11 or newer (tested on 3.12).
- Git.
- `pytest` only if you want to run the test suite.

## Use in this repo

```bash
python tools/ng.py doctor .
python tools/ng.py list
python tools/ng.py status .
```

If your shell only has `python3`, use `python3` in the same commands.

## Add to another repo

From this checkout, set up the target repo:

```bash
python tools/ng.py init /path/to/your/repo --dry-run
python tools/ng.py init /path/to/your/repo
python tools/ng.py doctor /path/to/your/repo
```

Make a packet:

```bash
python tools/ng.py new add-boundary --mode standard --repo /path/to/your/repo
python tools/ng.py validate /path/to/your/repo/.nuclear/changes/add-boundary
```

`validate` is **supposed to fail** on the untouched packet. Each template ships with a `NUCLEAR-GRADE-PLACEHOLDER` marker line, and the checker refuses any packet that still has it. That is the gate doing its job. Fill in the fields, set at least one real status (`pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`), delete the marker line in every file, and validate again:

```bash
python tools/ng.py validate /path/to/your/repo/.nuclear/changes/add-boundary
# OK: /path/to/your/repo/.nuclear/changes/add-boundary
```

`new` uses templates in `/path/to/your/repo/templates/` when they exist. If they do not, it copies the bundled templates from this Nuclear-grade checkout, so a target repo only needs `.nuclear/` to get started.

## Tool and agent harness notes

Public v0 ships paste-ready command prompts in `commands/` and agent-ready skills in `skills/`. They are plain Markdown files you can paste into, or adapt for, an AI coding agent. For Claude Code they also install as a plugin (see the plugin install above); the plugin packages these same Markdown files, with no executable hooks in this tier.

## Optional editable install

To test the console script locally from this checkout:

```bash
python -m pip install -e .
nuclear-grade doctor .
```

The repo-local `python tools/ng.py ...` commands remain a primary way to work in Public v0, alongside the Claude Code plugin (above) for agent users. The console script is a convenience for local checkout work, not a standalone release.

## Boundary note

MIT license permission does not create formal V&V, compliance, certification, safety, security, regulatory adequacy, procurement adequacy, or a regulated quality program. For those claims, use qualified controls built for your own project.

## Source-lineage note

This install guide shows how to use the Nuclear-grade workflow files. The sources that shaped it are mapped in `docs/00-standards-foundation/source-map.md`.
