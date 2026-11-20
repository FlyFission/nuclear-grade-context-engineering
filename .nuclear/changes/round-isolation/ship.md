# Ship: round isolation: one container per run, results out of agents' reach

## Release identity

- Slug: round-isolation
- Change: `round.sh` runs one container per trial with results, sign-ins and home folders kept apart. No release version change.
- Owner: FlyFission (maintainer)

## Scope and exclusions

- In scope: the paths named in `risk.md`.
- Excluded: outcome logic, rulings, the scorer, the challenge, and any published result.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| REQ-001..006 | pass | [`verification.md`](verification.md) |
| Independence of evidence | gap | the new tests are self-check |
| macOS run | deferred | the first round runs on the Mac Studio |

## Residual risks and gaps

- The agent can still read the scorer and harness. That is by design: the challenge is open-book (`challenge/README.md`).
- On macOS, the container runs as the host user. If a CLI cannot read its copied sign-in there, the round prompt's sign-in check catches it before any scored run.
- The new tests were written by the agent that made the change; maintainer review is the independent check.

## Rollback / restore plan

- Revert the commit.

## Monitoring and post-release checks

- Read the first round's transcripts for permission errors before publishing.

## Handoff

- Next owner: the maintainer, for round 1.
- Next step: the one-prompt round on the Mac Studio.

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
