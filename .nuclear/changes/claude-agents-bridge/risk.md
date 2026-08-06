# Risk — claude-agents-bridge

## Change identity

- **Slug:** `claude-agents-bridge`
- **Owner:** FlyFission
- **Date:** 2026-08-06
- **Summary:** Add the documented Claude Code import shim so cloned-repository sessions receive the existing `AGENTS.md` guidance without duplicating it.

## Mission and scope

The objective is to make the repository's existing agent brief effective in Claude Code while preserving one source of truth. Success is one import-only `CLAUDE.md`; non-goals are Claude-specific policy, hooks, settings, or copied guidance.

## Risk screen

| Dimension | Rating | Basis |
|---|---|---|
| Consequence | medium | The file changes the instructions Claude Code loads. |
| Reversibility | low | One file and one commit can be reverted. |
| Detectability | high | The file content and import target are directly inspectable. |
| Exposure | medium | Every Claude Code session in the checkout can receive the guidance. |
| Uncertainty | low | Anthropic documents this exact import pattern. |
| AI authority | medium | The imported brief bounds agent behavior but grants no new tool permission. |

## Selected mode

- **Mode:** Standard
- **Why:** This changes model-visible repository instructions, a controlled AI-behavior surface.
- **Why not lighter:** The operational edit is tiny, but its consequence is not merely administrative.
- **Why not heavier:** It adds no permission, hook, runtime, secret, dependency, or release action.

## Evidence obligations and holds

Before review, prove the import target exists, the packet validates, repository checks pass, and the diff contains no duplicated instruction body. Hold if Claude's documented syntax differs or an open PR already adds this bridge.

## Exit criteria

- `CLAUDE.md` contains only `@AGENTS.md`.
- The Standard packet and repository checks pass.
- A human retains the merge verdict.

## Required links

- Packet: `.nuclear/changes/claude-agents-bridge/`
- Changed instruction surface: `CLAUDE.md`
- Primary host documentation: <https://code.claude.com/docs/en/memory>

## Source-lineage note

This change follows Anthropic's documented compatibility import and the repository's existing agent guidance. It makes no compliance, safety, security, or formal V&V claim.
