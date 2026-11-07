# Ship: move the required-mode command into the engine module

## Release identity

- Slug: ws1-required-mode-handler
- Change: `ng required-mode` now runs from `nuclear_grade/consequence.py`; the failure hint matches the failure. No release version change.
- Owner: FlyFission (maintainer)

## Scope and exclusions

- In scope: the three paths named in `risk.md`.
- Excluded: any change to classification, coverage, approvals, exit codes, the receipt schema, or the policy.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| REQ-001..003 | pass | [`verification.md`](verification.md) |
| Independence of evidence | gap | the new tests are self-check; the pre-existing tests predate the move |

## Residual risks and gaps

- The new tests were written by the agent that made the change. The unmodified tests from #123 give a check the change could not shape. Maintainer review is the independent check.
- The coverage gain depends on #128 merging with `nuclear_grade/consequence.py` under the `validators` rule. Until then, this repository's gate has only the built-in policy.

## Rollback / restore plan

- Revert the commit.

## Monitoring and post-release checks

- When the advisory CI job lands, its receipts print these hints on real PRs.

## Handoff

- Next owner: the agent continuing WS1, or the maintainer.
- Next step: once #128 merges, this change closes the `gate-cli` residual recorded in the `ws1-repo-policy` record.

## Release decision

- **Decision:** ship with named residual risk (self-check evidence), pending maintainer review.
- **Decider:** maintainer (FlyFission).

## Apply clearance

- Applied by merging the PR; the maintainer merges.

## Baseline trigger

- None; no release.

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`plan.md`](plan.md), [`trace.md`](trace.md), [`verification.md`](verification.md)

## Exit criteria

- The release decision, rollback, and monitoring are stated.
- Residual risks are named, not hidden.

## Source-lineage note

Original Nuclear-grade ship record; release-readiness lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
