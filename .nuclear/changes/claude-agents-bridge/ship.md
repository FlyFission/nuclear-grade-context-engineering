# Ship — claude-agents-bridge

## Release identity and scope

- **Change:** `claude-agents-bridge`
- **Owner:** FlyFission
- **Date:** 2026-08-06
- **Included:** Import-only root `CLAUDE.md` and its change record.
- **Excluded:** Hooks, settings, permissions, duplicated instructions, and Claude-specific workflow policy.

## Evidence status

| Area | Status | Link |
|---|---|---|
| Risk and basis | pass | `risk.md`, `basis.md` |
| Verification | pass | `verification.md` |
| Evidence custody | pass | `verification.md` |
| Human review | planned | PR review |

## Residual risk

| Gap | Impact | Disposition | Recheck trigger |
|---|---|---|---|
| CI does not launch Claude Code to prove import loading. | The shim could become stale if host behavior changes. | Accept for a one-line reversible compatibility file. | Import failure report or host-documentation change. |

## Rollback and monitoring

Revert the focused commit. Monitor only for Claude Code failing to load the imported brief or for Anthropic making the shim redundant.

## Release decision

- **Decision:** defer to human PR review
- **Decision maker:** FlyFission maintainer
- **Rationale:** Deterministic checks can establish repository integrity; the maintainer owns whether the host bridge belongs in the accepted baseline.
- **Abort trigger:** Verification failure, duplicate open work, or changed host documentation.

## Apply clearance and baseline

- **Clearance:** hold until PR approval; merge is the apply action.
- **Baseline required:** No separate baseline record; the accepted git commit is sufficient.
- **Revalidation trigger:** Claude Code instruction-discovery behavior changes.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `CLAUDE.md`
- Pull request: to be added after creation

## Exit criteria

- Verification is complete and gaps are visible.
- A human reviewer owns the merge verdict.
- Rollback remains a one-commit revert.

## Source-lineage note

The release posture is bounded to the reversible compatibility shim documented by Anthropic at <https://code.claude.com/docs/en/memory> and makes no compliance, safety, security, or formal assurance claim.
