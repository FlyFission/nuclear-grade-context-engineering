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
| Codex CLI | `… install codex` | user `~/.agents/skills/`; project `.agents/skills/` | user or project |
| Claude Code | plugin (below) **or** `… install claude` | user `~/.claude/skills/`; project `.claude/skills/` | user or project |
| Cursor | `… install cursor` | user `~/.cursor/skills/`; project `.cursor/skills/` | user or project |
| Windsurf | `… install windsurf` | user `~/.codeium/windsurf/skills/`; project `.windsurf/skills/` | user or project |
| VS Code + Copilot | `… install vscode` | project `.github/skills/`; user `~/.config/github-copilot/skills/` | user or project |

Default scope is `user` (available in every project); pass `--scope project --repo .`
for a single repo. Or fan out to every detected tool in one step:

```bash
./install.sh            # Core set into each detected tool
./install.sh --full     # all skills
```

> Codex, Claude Code, Cursor, and Windsurf paths are confirmed against current
> docs. VS Code's project path (`.github/skills`) is confirmed; its user-scope
> path is a best-known default — the command flags it. If your install differs,
> point it anywhere with `--dest <path>`.

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

### Codex: the plugin package and skill installer

The repo ships a `.codex-plugin/plugin.json` manifest, so it is a publishable
Codex plugin that bundles the **skills**. Besides `ng install codex`, Codex users
can pull the skills with the built-in installer from a Codex session:

```text
$skill-installer install nuclear-grade from https://github.com/FlyFission/nuclear-grade-context-engineering
```

(Codex's self-serve plugin directory is still rolling out; verify the exact
installer syntax against <https://developers.openai.com/codex/plugins>.)

To validate the manifest and print the exact install + restart steps from a
checkout, run the repo-side helper:

```bash
python tools/install-codex.py            # validate, then print Codex install guidance
python tools/install-codex.py --check    # validate the manifest only (used in tests/CI)
```

**What the Codex plugin install gives you, and what it does not.** The plugin
exports `skills/` only — the `SKILL.md` files Codex auto-surfaces by their
`description`. It deliberately does **not** package the rest of the repo as
Codex-native capabilities:

| Repo asset | In the Codex plugin? | Why |
|---|---|---|
| `skills/` | **Yes** | Exported via `plugin.json` `skills`; Codex routes to them by `description`. |
| `agents/` | No | These are **Claude** PROVE subagent definitions. Codex subagent packaging is not supported here; treat them as Claude-only until converted (see [`agents/README.md`](agents/README.md)). |
| `commands/` | No | Paste-ready prompt cards, not Codex slash commands. Open them from a checkout and paste. |
| `templates/`, `.nuclear/` | No | Repo assets the skills and `ng` CLI use. The `ng init`/`ng new` commands copy them into a target repo; the Codex plugin does not. |
| `tools/ng.py` | No | A repo-side CLI you run from a checkout. The plugin adds no `ng` command to your `PATH`. |

Because the flagship `using-nuclear-grade` skill is a **router** whose body
points at repo-local files (`.nuclear/charter.md`, `WORKFLOWS.md`/`CORE.md`, the
`ng` CLI), skills installed *without* the repository will route you toward files
that are not there. For the full workflow, **clone the repo** as well — the
plugin install is a discovery pointer, not a self-contained package. See
[`docs/04-adoption/listing-and-discovery.md`](docs/04-adoption/listing-and-discovery.md).

**After installing, start a new Codex thread** (or restart Codex) so it re-scans
its skills directory and loads the new descriptions. Then describe your task and
Codex pulls in the matching skill on its own — no slash command needed.

**How this differs from the Claude Code plugin.** The Claude Code marketplace
plugin surfaces both the skills **and** the `commands/` prompt cards as native
slash commands with no copying, and it ships the PROVE subagents in `agents/`.
The Codex plugin exports skills only; commands and agents stay repo-side. Both
tiers configure **no hooks**, so nothing runs automatically on install.

**Verified manifest constraints.** Codex's manifest loader caps each
`interface.defaultPrompt` entry at **128 characters** — an over-long prompt is
logged (`prompt must be at most 128 characters`) and **dropped**, not fatal. Our
prompts are all well under that, and `tools/install-codex.py` plus the packaging
tests enforce the limit so a future edit cannot reintroduce one. The minimally
required top-level fields are `name`, `version`, `description`, and `skills`;
this manifest also ships `author` and `interface` as objects (Codex plugin
validation rejects them as anything else). The full, authoritative field list
lives in the Codex docs at <https://developers.openai.com/codex/plugins/build>;
re-confirm it there before adding fields, since the schema is still evolving.

### Windsurf / Cursor: the community skills CLI

The cross-tool `skills` CLI also installs into these tools:

```bash
npx skills add FlyFission/nuclear-grade-context-engineering
```

## Get listed in official directories

Beyond installing from this repo, you can submit to official directories so others discover
the skills. See [`docs/04-adoption/listing-and-discovery.md`](docs/04-adoption/listing-and-discovery.md)
for the verified, step-by-step process. The two worth pursuing today are the **Claude Code
community directory** (`claude plugin validate` already passes, so the repo is
submission-ready) and the **`openai/skills`** catalog; the MCP Registry is deferred and VS
Code/Copilot need full extension repackaging.

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
skills (auto-surfaced) and keeps the `ng` checks as an on-demand CLI; the MCP
server below is **opt-in** for when a tool must *call* the checks.

## Calling the checks as tools (optional MCP server)

Skills let the model *read* Nuclear-grade's guidance; the MCP server lets a tool
*call* its checks as tools. It is opt-in and carries a real standing cost, so
reach for it only when a tool must run the checks itself.

```bash
pip install "nuclear-grade[mcp]"        # optional extra; the base install stays zero-dependency
python tools/ng.py mcp-config codex     # prints the config to paste for your tool
```

The server (`python -m nuclear_grade.mcp_server`) exposes `validate_change_record`,
`doctor`, `status`, and `new_change_record`, wrapping the same logic the CLI uses
(it does not shell out). `ng mcp-config <tool>` prints the exact server entry for:

| Tool | Config file | Top-level key |
|---|---|---|
| Codex CLI | `~/.codex/config.toml` | `[mcp_servers.nuclear_grade]` |
| Claude Code | `.mcp.json` (or `claude mcp add`) | `mcpServers` |
| Cursor | `.cursor/mcp.json` | `mcpServers` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` | `mcpServers` |
| VS Code + Copilot | `.vscode/mcp.json` | `servers` (note: not `mcpServers`) |

**Why opt-in:** an MCP server's tool schemas load into the model's context every
session whether used or not (~1k tokens per tool); skills load only short
descriptions until they fire. Prefer `ng install` for everyday use; add the MCP
server when an agent needs to execute the checks.

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
