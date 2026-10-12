# Basis — Blocking PreToolUse gate (opt-in)

## Mission

Close follow-up F-01 from [`../adr-governance-benchmark/basis.md`](../adr-governance-benchmark/basis.md). Today the hooks only advise. HOOKS.md deferred the blocking tier and set three conditions for it: decide on structured facts only, fail closed, and never auto-allow. This change ships that tier as an opt-in hook and honors each condition.

## Requirements

- **REQ-001:** `hooks/pre_tool_use.py` shall deny `Write`, `Edit`, `MultiEdit`, and `NotebookEdit` calls that target the gate's own trust surfaces, after normalizing the path, resolving symlinks, and folding case.
- **REQ-002:** It shall return `ask` for `Bash` commands that match the irreversible or release patterns listed in HOOKS.md.
- **REQ-003:** It shall never emit `allow`. When no rule matches, it shall print nothing and exit 0.
- **REQ-004:** It shall fail closed with `ask` on malformed input, a missing path or command, an invalid policy file, or an internal error.
- **REQ-005:** `.nuclear/gate-policy.json` shall be able to add deny and ask rules but never remove a default. The agent shall not be able to write the policy file.
- **REQ-006:** The hook shall use the standard library only, with no network, no subprocess, no dynamic execution, and read-only file access. An AST test shall enforce this.
- **REQ-007:** The hook shall stay opt-in, so no `hooks/hooks.json` ships. HOOKS.md shall document how to enable it, the default policy, and where it falls short.

## Non-goals

This change adds no sandbox, no MCP-tool coverage, no change to the advisory hooks' behavior, and no release.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)
- Doctrine: [`HOOKS.md`](../../../HOOKS.md)

## Exit criteria

Each requirement is testable, and each one maps to a test in [`trace.md`](trace.md).

## Source-lineage note

Original Nuclear-grade synthesis. It draws on the enforcement rungs in [`agent-authority-model.md`](../../../docs/04-adoption/agent-authority-model.md) and the sources in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
