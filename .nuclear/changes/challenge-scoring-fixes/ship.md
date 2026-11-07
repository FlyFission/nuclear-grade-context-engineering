# Ship: Three challenge scoring fixes found in trial runs

## Release decision

**Decision: defer to human review.** The change goes up as a draft pull request, and merge authority stays with the maintainer. The release stance does not change: no version bump and no tag.

Residual risk:

- E-001 to E-003 are self-checks by the AI agent that wrote the change. CI on a clean runner and a human reading the scorer diff are the less-coupled checks still to come.
- A test in a new file can still change shared state for the tests that run after it. That was true before this change and is not made wider by it.
- The trial run itself is not published and does not count toward any result.

## Rollback

Revert the commit and regenerate the manifest. Nothing else holds state.

## Monitoring

Read every scored run where "Original tests kept" fails, and every run with the new outcome, before results are published.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

A human reviews the diff, CI passes on a clean runner, and the maintainer makes the merge decision.

## Source-lineage note

This is a repository change decision. It makes no compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
