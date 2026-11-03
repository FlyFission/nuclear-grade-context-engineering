# Basis: Guard plugin, deny-rule comparison, and `init` add-ons

## Mission

Make the strongest opt-in control, the `PreToolUse` gate, reachable in one step without changing the default no-hooks install, explain honestly when Claude Code's built-in permission rules are enough, and let `init` set up a repo's agent guidance, gate, and CI in one opt-in command. Success means each requirement below has a passing test or a recorded check.

## Requirements

- **REQ-001:** The marketplace shall list a separate `nuclear-grade-guard` plugin whose only component is a `hooks/hooks.json` that registers the gate for `PreToolUse` in exec form with `${CLAUDE_PLUGIN_ROOT}`, `onFailure: block`, and a timeout.
- **REQ-002:** The main `nuclear-grade` plugin shall still register no hooks.
- **REQ-003:** The plugin's copy of the gate shall stay byte-identical to `hooks/pre_tool_use.py`, and its version shall track `pyproject.toml`.
- **REQ-004:** HOOKS.md, the guard plugin, and `init --hook` shall register the same matcher, command, timeout, and failure handling.
- **REQ-005:** The gate shall deny writes to `~/.claude/plugins/**` and ask before shell commands that disable or remove a plugin or name `.claude/plugins`, without gating `claude plugin install` or `list`.
- **REQ-006:** `init --agents`, `--hook`, `--ci`, and `--all` shall be opt-in. Plain `init` shall behave as before. `--dry-run` shall write nothing and list each change. Existing files shall be kept unless `--yes`, and `.nuclear/` files shall never be overwritten by an add-on run.
- **REQ-007:** `init --hook` shall merge into an existing `.claude/settings.json`, keep every other key and hook, add nothing when the gate is already registered, and refuse an unmergeable file before writing anything.
- **REQ-008:** `init --hook` and `init --agents` shall work from an installed wheel, so their sources ship in the wheel.
- **REQ-009:** HOOKS.md, INSTALL.md, INTEGRATIONS.md, the CLI reference, and QUICKSTART.md shall document the install, what the gate blocks or asks, how to remove it, and the new flags, with each claim checked.

## Non-goals

Out of scope: hooks in the main plugin, a sandbox, MCP-tool coverage, the advisory session hooks in the guard plugin, any change to README.md, CHANGELOG.md, `docs/diagrams.md`, `challenge/`, or `leaderboard/` (another change owns them), and any release.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)
- Doctrine: [`HOOKS.md`](../../../HOOKS.md)

## Exit criteria

Each requirement is testable and maps to evidence in [`trace.md`](trace.md).

## Source-lineage note

Original Nuclear-grade synthesis, drawing on [`agent-authority-model.md`](../../../docs/04-adoption/agent-authority-model.md) and the sources in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
