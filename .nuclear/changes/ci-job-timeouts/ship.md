# Ship: CI job timeouts

## Release identity

- Slug: ci-job-timeouts
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-06
- Change: `timeout-minutes` on 9 workflow jobs, the same key in the workflow `ng scaffold-ci` writes, and a test that keeps both bounded. No release version change.

## Scope and exclusions

- In scope: the four paths named in `risk.md`.
- Excluded: tuning caps from more than one run, path filtering, any change to steps, triggers, permissions or pins.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| REQ-001..003 | pass | [`verification.md`](verification.md) |
| Independent review | pass, findings dispositioned | [`verification.md`](verification.md) |
| `release.yml` runtimes | pass for one run | v0.7.0 took 3 min 18 s end to end |
| Approval wait vs timeout | gap | not checked |
| Independence of evidence | gap | all decisive evidence is self-check |

## Residual risks and gaps

- **Release caps rest on one run.** The v0.7.0 release took 3 min 18 s end to end against caps of 10 to 15 minutes per job. A tag that times out is fixed by rerunning with a larger cap.
- **Approval wait.** The `pypi` job uses `environment: pypi`. Whether time spent waiting for a required reviewer counts toward `timeout-minutes` is not confirmed. The reviewer believed it does not but could not read the documentation section, and the v0.7.0 timing does not show whether an approval was needed. If it does count, a slow approval could cancel the publish job. Confirm before the next tag, or raise the `pypi` cap; it is the one cap with a possible false failure.
- **Production-facing file.** `release.yml` publishes to PyPI. AGENTS.md asks for permission before editing such material; this record routes it through the maintainer's review and merge.
- **Downstream scaffold users.** Repositories that already ran `ng scaffold-ci` keep their old file. New runs get a 10-minute cap on the validation job, which only validates packets.
- **Self-check evidence.** The agent wrote the fix and the test. CI re-runs the test; maintainer review is the independent check.
- **The test skips without PyYAML.** CI installs it. A local run without it skips the repository checks.

## Rollback / restore plan

- Revert the commit. No state, schema or published artifact depends on it.

## Monitoring and post-release checks

- After merge, confirm the next CI run's jobs complete well inside their caps.
- After the next tag, confirm the release jobs complete and note their durations here.

## Handoff

- Next owner: the maintainer.
- Next steps: confirm the approval-wait behavior before the next tag; decide whether to add a "Not run, and why" line to the PR template (a further `standard+authority` path). Control Rod's matching proposal is a separate record there.

## Release decision

- **Decision:** ship with named residual risk, pending maintainer review.
- **Decider:** maintainer (FlyFission).

## Apply clearance

- Applied by merging the PR; the maintainer merges. The agent has no merge authority for this change.

## Baseline trigger

- Not applicable: no release in this change.

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`plan.md`](plan.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`decision-authority.md`](decision-authority.md)

## Exit criteria

- The release decision, rollback, and monitoring are stated.
- Residual risks are named, not hidden.

## Source-lineage note

Original Nuclear-grade record; lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
