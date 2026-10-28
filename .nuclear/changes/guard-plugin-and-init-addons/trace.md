# Trace: Guard plugin, deny-rule comparison, and `init` add-ons

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `plugins/nuclear-grade-guard/`, `.claude-plugin/marketplace.json` | E-001, E-005 | pass |
| REQ-002 | no root `hooks/hooks.json`; no `hooks` key in the main manifest or its entry | E-001, E-005 | pass |
| REQ-003 | `plugins/nuclear-grade-guard/hooks/pre_tool_use.py`; `MANIFESTS` in `nuclear_grade/release.py` | E-001 | pass |
| REQ-004 | `gate_hook_entry` in `nuclear_grade/cli.py`; HOOKS.md snippet; plugin `hooks.json` | E-001 | pass |
| REQ-005 | `DENY_PATHS`, `ASK_COMMANDS`, `SHELL_TRUST_TOKENS` in `hooks/pre_tool_use.py` | E-002 | pass |
| REQ-006 | `handle_init`, `apply_writes(keep_existing=...)`, `ci_writes` | E-003 | pass |
| REQ-007 | `plan_gate_settings` | E-003 | pass |
| REQ-008 | `pyproject.toml` force-include and sdist include | E-004 | pass |
| REQ-009 | HOOKS.md, INSTALL.md, INTEGRATIONS.md, `docs/05-reference/cli-reference.md`, QUICKSTART.md | E-006 | pass |
| REQ-001 live | A live Claude Code session runs the plugin gate and honors its decision | E-007 | gap |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability here is an internal review aid. It does not create formal verification and validation. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
