# Ship — Blocking PreToolUse gate (opt-in)

## Release decision

**Decision: defer to PR review.** The change is opt-in and reversible, and merge authority stays with the owner. The release stance does not change: no version bump and no tag.

Residual risk: E-001 to E-003 are self-checks by the change actor. The CI rerun on a clean runner is the less-coupled signal, and a reviewer reading the deny/ask table is the independent check. E-007 is still a gap because no live Claude Code session has run the gate. Shell matching is defeatable by design, and HOOKS.md says so. A regex an adopter adds to the policy file could backtrack badly. The adopter owns that risk, because the agent cannot edit the file.

## Rollback

Revert the commit. Adopters who enabled the gate remove the `PreToolUse` entry from `.claude/settings.json`. Nothing else holds state.

## Monitoring

Watch for false-positive `ask` reports and for host protocol changes to the `PreToolUse` output fields. If the protocol changes, update the hook and its CLI test together.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

The PR's CI is green, and the owner makes the merge decision.

## Source-lineage note

This is a repository change decision, not a compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
