# Basis — claude-agents-bridge

## Mission / need

The repository tells agent users to start from `AGENTS.md`, but Anthropic's current Claude Code documentation states that Claude Code reads `CLAUDE.md`, not `AGENTS.md`, and recommends a `CLAUDE.md` import when another agent format is already in use. A one-line bridge closes that discovery gap without creating a second instruction source.

Primary source: <https://code.claude.com/docs/en/memory>

## Protected and unacceptable outcomes

| Outcome | Type | Control / evidence |
|---|---|---|
| `AGENTS.md` remains the single maintained brief | protected | Import it rather than copy its body. |
| Claude Code automatically receives the shared brief in a checkout | protected | Root `CLAUDE.md` uses Anthropic's documented `@AGENTS.md` form. |
| Host-specific policy grows in the shim | unacceptable / insufficiency | Keep the file import-only. |
| A broken import silently points nowhere | unacceptable / fault | Public-doc/local-link test plus direct file inspection. |

## Assumptions and boundaries

- **Fact:** `AGENTS.md` exists at repository root.
- **Source claim:** Anthropic documents `CLAUDE.md` as Claude Code's persistent project-instruction file and the `@AGENTS.md` compatibility import.
- **Boundary:** Imported instructions remain context, not deterministic enforcement; no hook or permission control is claimed.
- **Invalidation trigger:** Anthropic changes import syntax or begins natively loading `AGENTS.md` in a way that makes the shim redundant.

## Derived requirement

**REQ-001:** WHEN Claude Code loads repository instructions, THE REPOSITORY SHALL route it to the existing root `AGENTS.md` without duplicating that guidance.

## Design outline

Add a root `CLAUDE.md` containing only `@AGENTS.md`. No other repository or host configuration changes.

## Required links

- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- The reviewer can identify the single requirement and its source.
- The shim does not duplicate or expand the agent brief.
- Verification covers the import target and repository integrity.

## Source-lineage note

The host-loading claim is bounded to Anthropic's current Claude Code documentation. No cross-host or enforcement claim is made.
