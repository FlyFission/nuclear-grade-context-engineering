# Ship: Fix five gaps a code review found in the challenge harness

## Release decision

**Decision: defer to human review.** The change goes up as a draft pull request, and merge authority stays with the maintainer. No run is made or published.

Residual risk:

- E-001 to E-006 are self-checks by the AI agent that wrote the change. CI on a clean runner is still to come.
- On Windows the timeout still stops only the agent's CLI.
- `container_image` is only as good as the value the person running the round sets.

## Rollback

Revert the commit. No results exist yet, so nothing else holds state.

## Monitoring

On the first real round, check that each result's `environment` block is filled in and that no run file was replaced.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

A human reviews the diff, CI passes on a clean runner, and the maintainer makes the merge decision.

## Source-lineage note

This is a repository change decision. It makes no compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
