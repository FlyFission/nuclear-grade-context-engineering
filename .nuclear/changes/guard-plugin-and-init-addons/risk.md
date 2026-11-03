# Risk: Guard plugin, deny-rule comparison, and `init` add-ons

## Selected mode

- **Mode:** Standard
- **Why:** The change gives adopters a one-line way to register an executable hook that can deny and ask, extends the gate's own rules, and adds a CLI path that writes Claude Code settings into a target repo. Each of these changes what a tool or agent may do, which CORE.md routes to Standard or higher. The precedents [`blocking-pretooluse-gate`](../blocking-pretooluse-gate/risk.md) and [`plugin-install-vehicle`](../plugin-install-vehicle/risk.md) were rated Standard for smaller steps.

## Decision

Ship three opt-in improvements in one reviewable change:

1. A second plugin, `nuclear-grade-guard`, in the same marketplace. It registers only the existing `PreToolUse` gate. The main `nuclear-grade` plugin keeps shipping no hooks.
2. A short HOOKS.md section that compares the gate with Claude Code's own permission rules and offers deny and ask rules as a lighter option.
3. `init --agents`, `--hook`, `--ci`, and `--all`, with plain `init` unchanged.

Main failure modes and controls:

- **The main plugin starts running hooks on install.** Control: the guard lives under `plugins/nuclear-grade-guard/`, and only `hooks/hooks.json` at a plugin root (or a manifest `hooks` key) registers hooks. Tests assert the root has no `hooks/hooks.json`, the main manifest and its marketplace entry have no `hooks` key, and `claude plugin details` reports `Hooks (0)` for the main plugin.
- **The plugin copy of the gate drifts from the tested original.** Control: a test fails unless the copy is byte-identical to `hooks/pre_tool_use.py` after line-ending normalization. The guard manifest version is added to the release identity check.
- **An agent switches the plugin gate off.** The plugin puts a live copy of the gate under `~/.claude/plugins/`, and `claude plugin disable` or `uninstall` can turn it off from the shell. Control: the gate now denies file-tool writes to `~/.claude/plugins/**`, asks on shell commands that name `.claude/plugins`, and asks on `claude plugin disable`, `uninstall`, `remove`, and `marketplace remove`. Shell matching stays defeatable, and HOOKS.md keeps saying so.
- **The gate fails open when it cannot run.** Control: every registration (HOOKS.md snippet, plugin `hooks.json`, `init --hook`) sets `onFailure: block` and a 10 second timeout, and one test fails if the three drift apart.
- **`init --hook` damages an adopter's settings or records.** Control: the settings file is parsed and merged in memory first; unreadable JSON or an unexpected shape stops the run with exit 2 before any file is written. Other keys and hooks are kept, a second run adds nothing, add-on runs never overwrite `.nuclear/` files, and `--dry-run` writes nothing (all tested).
- **The comparison section overclaims.** Control: each claim about Claude Code's permission rules was checked against the current Claude Code docs, and each claim about the gate maps to code and a test. The section states the gate is built for Claude Code and untested elsewhere.

The release stance does not change. There is no version bump and no tag.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Each failure mode above has a named test or a recorded check, the full suite passes, and both the main plugin's no-hooks posture and plain `init` behavior are unchanged.

## Source-lineage note

Original Nuclear-grade change. It applies the enforcement-rung ideas in [`runtime-enforcement.md`](../../../docs/02-operating-system/runtime-enforcement.md), mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). Claude Code behavior is cited from its public docs at https://code.claude.com/docs/en/hooks, https://code.claude.com/docs/en/plugins-reference, and https://code.claude.com/docs/en/permissions. No security, compliance, or efficacy claim is made.
