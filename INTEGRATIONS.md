# Integrations

Install Nuclear-grade once and let your agent reach for its skills the way it
already reaches for any other installed skill — in Codex, Claude Code, Cursor,
Windsurf, and VS Code.

## How it works

A Nuclear-grade skill is a plain `SKILL.md` file with a `name` and a
`description` in its frontmatter. Every modern agent tool reads the
`description` of each installed skill and the model itself pulls the full skill
in when a request matches — no dispatcher, no daemon, no per-prompt wiring. The
**`description` is the integration**. The same files work unmodified across
tools; "installing" just means placing them where each tool looks.

That is also why this is lean: only the short descriptions are ever
always-loaded; a skill's body is read **only when that skill fires**.

## Install per tool

`ng install <tool>` copies the skills into the right place. Run it from a
checkout (`python tools/ng.py install …`) or via the installed console script
(`nuclear-grade install …`).

| Tool | Command | Skills land in | Scope |
|---|---|---|---|
| Codex CLI | `python tools/ng.py install codex` | `~/.codex/skills/` (honors `$CODEX_HOME`) | user — every project |
| Claude Code | plugin (below) **or** `python tools/ng.py install claude` | `~/.claude/skills/` | user or `--scope project` |
| Cursor | `python tools/ng.py install cursor` | `~/.cursor/skills/` | user or project |
| Windsurf | `python tools/ng.py install windsurf --scope project --repo .` | `.windsurf/skills/` | project only |
| VS Code + Copilot | `python tools/ng.py install vscode` | `~/.vscode/skills/` | user or project |

Or fan out to every detected tool in one step:

```bash
./install.sh            # Core set into each detected tool
./install.sh --full     # all skills
```

> Codex and Claude Code paths are confirmed against current docs. Cursor,
> Windsurf, and VS Code paths are best-known defaults — the command says so when
> you run it. If your install differs, point it anywhere with
> `--dest <path>`.

### Claude Code: the native plugin

Claude Code users can also install the repository as a plugin marketplace, which
surfaces the skills **and** the command prompts with no copying:

```bash
/plugin marketplace add FlyFission/nuclear-grade-context-engineering
/plugin install nuclear-grade@nuclear-grade
/reload-plugins
```

The plugin configures **no hooks**, so nothing runs automatically. The optional
always-on routing hooks remain opt-in — see [`HOOKS.md`](HOOKS.md).

## Profiles and token cost

- `--core` (default): the always-first `using-nuclear-grade` router plus the
  Core 7 from [`CORE.md`](CORE.md) — 8 skills.
- `--full`: every skill.

Each run prints the **always-on description cost** of what it installed (≈100
tokens per skill), so you can keep context lean. Re-running updates in place.

### CLI vs skills vs MCP — what costs context

| Surface | Always-on cost | When you pay |
|---|---|---|
| **CLI** (`ng …` run via the shell) | ~0 | only the command + its output, on demand |
| **Skills** (`SKILL.md`) | each skill's short `description` | full body only when the skill fires |
| **MCP server** | every tool's name + description + JSON schema | loaded for the whole session whether used or not |

Ranking, lean to heavy: **CLI ≈ Skills ≪ MCP**. Nuclear-grade therefore ships
skills (auto-surfaced) and keeps the `ng` checks as an on-demand CLI; an MCP
server is deferred until its standing cost is worth paying.

## Verify it worked

1. `python tools/ng.py install codex --core --dry-run --dest /tmp/ng-skills`
   prints the file list and the always-on cost without writing.
2. After a real install, ask the agent something that should route — e.g.
   *"I'm about to change auth"* — and confirm it reaches for
   `using-nuclear-grade` / `questioning-attitude` on its own.
3. If a skill does not appear, restart the tool so it re-scans its skills
   directory.

## Boundary note

These integrations install workflow guidance. Adopting them does not create
formal verification and validation, compliance, certification, safety, security,
or regulatory adequacy. See [`DISCLAIMER.md`](DISCLAIMER.md).
