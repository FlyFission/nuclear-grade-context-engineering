# Ship: a scoreboard page, a badge and a run-everything script for the challenge

## Release identity

- Slug: challenge-scoreboard
- Change: `build.py` writes a scoreboard page and a badge; `run-all.py` runs a full round. No release version change.
- Owner: FlyFission (maintainer)

## Scope and exclusions

- In scope: the paths named in `risk.md`.
- Excluded: outcome logic, rulings, `run.py`, the scorer, `METHOD.md`, and any published result.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| REQ-001..004 | pass | [`verification.md`](verification.md) |
| Independence of evidence | gap | the new tests are self-check |
| Real results | deferred | the page shows the empty state until the first scored round |

## Residual risks and gaps

- The new tests were written by the agent that made the change. The unmodified harness tests give a check the change could not shape. Maintainer review is the independent check.
- The headline counts two outcomes as silent. A run a person later rules differently moves with its ruling, because the page reads the same rows `RESULTS.md` does.
- GitHub Pages is not switched on by this change; the page can be viewed from the repository until it is.

## Rollback / restore plan

- Revert the commit and delete the two generated files.

## Monitoring and post-release checks

- After the first scored round, read the page against `RESULTS.md` row by row before anyone shares it.

## Handoff

- Next owner: the maintainer, for the first scored round.
- Next step: run `python challenge-results/run-all.py --trials 5` in a throwaway container or VM with the agent CLIs signed in.

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
