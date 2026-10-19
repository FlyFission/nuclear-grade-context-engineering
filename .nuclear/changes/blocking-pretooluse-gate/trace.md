# Trace — Blocking PreToolUse gate (opt-in)

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `hooks/pre_tool_use.py` `DENY_PATHS`, `_match_paths` | E-001 | pass |
| REQ-002 | `ASK_COMMANDS`, `_rm_outside_cwd`, `SHELL_TRUST_TOKENS` | E-001 | pass |
| REQ-003 | `decide` (no `allow` branch) | E-002 | pass |
| REQ-004 | `decide` / `_decide` fail-closed returns | E-002 | pass |
| REQ-005 | `_load_policy` (additive keys only); policy file in `DENY_PATHS` | E-003 | pass |
| REQ-006 | imports and calls in `hooks/pre_tool_use.py` | E-004 | pass |
| REQ-007 | `HOOKS.md`; `tests/test_plugin_packaging.py::test_no_auto_activated_hooks_config` | E-005 | pass |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability is an internal review aid, not formal verification and validation. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
