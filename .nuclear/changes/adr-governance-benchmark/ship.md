# Ship — ADR governance lessons and landscape benchmark

## Release decision

**Decision: defer to PR review.** This is a reversible tooling and CI change. Merge authority stays with the owner, and the release stance does not change: no version bump, no tag. B-4 (version drift) and the follow-ups F-01 to F-09 in [`basis.md`](basis.md) are owner decisions.

Residual risk: E-001 and E-002 are self-checks by the change actor. The CI rerun on a clean runner is the less-coupled signal. After merge, the owner should make `CI gate` the required check in branch protection; until then REQ-003 is built but not enforced.

## Rollback

Revert the commit. The receipt is opt-in output, and the `mcp` range narrows back to `<2` with no data migration.

## Monitoring

Watch the first Dependabot Actions PRs and the `mcp-smoke` matrix. If the 2.x leg fails on an SDK minor release, narrow the range rather than skipping the leg.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

The PR's CI is green, including `CI gate` and both `mcp-smoke` legs, and the owner makes the merge decision.

## Source-lineage note

This is a repository change decision, not a compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
