# Ship: CI job timeouts

## Release identity

- Slug: ci-job-timeouts
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-06
- Change: `timeout-minutes` on 9 workflow jobs, the same key in the workflow `ng scaffold-ci` writes, and a test that keeps both bounded. No release version change.

## Scope and exclusions

- In scope: the four paths named in `risk.md`.
- Excluded: tuning caps beyond the margins in `evidence/job-times.txt`, path filtering, any change to steps, triggers, permissions or pins.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| REQ-001..003 | pass | [`verification.md`](verification.md) |
| Independent review | pass, findings dispositioned | [`verification.md`](verification.md) |
| `release.yml` runtimes | pass for one run | v0.7.0 per-job times in `evidence/job-times.txt`: `build` 71 s is the slowest |
| Approval wait vs timeout | gap | not checked |
| Independence of evidence | gap | all decisive evidence is self-check |

## Residual risks and gaps

- **Release caps rest on one run.** In the v0.7.0 release `build` took 71 s and `pypi` 21 s against caps of 15 and 10 minutes. A tag that times out is fixed by re-running with a larger cap.
- **Approval wait.** The `pypi` job uses `environment: pypi`. GitHub's documentation does not say whether time waiting for approval counts toward `timeout-minutes`. In v0.7.0 the `pypi` job waited 71 s before starting and ran 21 s, so that wait did not show in its run time. A long wait is untested. If it did count, a slow approval could cancel the publish job; `pypi` is the one cap with that possible false failure. Options for the signer: keep 10 minutes, or raise `pypi`; confirm before relying on either.
- **Production-facing file.** `release.yml` publishes to PyPI. AGENTS.md asks for permission before editing such material; this record routes it through the maintainer's review and merge.
- **Downstream scaffold users.** Repositories that already ran `ng scaffold-ci` keep their old file. New runs get a 10-minute cap on the validation job, which only validates packets.
- **Self-check evidence.** The agent wrote the fix and the test. CI re-runs the test; maintainer review is the independent check.
- **The test skips without PyYAML.** CI installs it. A local run without it skips the repository checks.

## Signature

This record is an unsigned draft. It approves nothing.

| Field | Entry |
|---|---|
| Decision | not yet signed: approve, approve with changes, or reject |
| Signed by | not yet signed: a maintainer other than the person who prompted the agent |
| Date | not yet signed |
| Basis | not yet signed: the PR review that approves this change as it stands |
| Caps accepted or changed | not yet signed |

Open decisions for the signer:

1. **Who signs.** The agent drafted this at Ben Huffer's request, so he cannot be the independent signer. This PR is opened from the `FlyFission` account, and `ng required-mode` reports it cannot confirm an approver other than the PR author (it needs `--pr-author`). A second maintainer must review, or the owner records an exception. The agent does not choose.
2. **The caps.** `validate` 20, `wheel-smoke` 15, `mcp-smoke` 15, `ci-gate` 5; release `build` 15, `mcp-smoke` 15, `wheel-smoke` 15, `github-release` 10, `pypi` 10 minutes. These are policy choices; the checker's ceiling is 60 minutes.
3. **`pypi`.** Keep 10 minutes or raise it, given the approval-wait question above.
4. **`release.yml` publishes to PyPI.** AGENTS.md asks for permission before editing production-facing material; the signer's review is that permission.

## Rollback / restore plan

- Revert the commit. No state, schema or published artifact depends on it.

## Monitoring and post-release checks

- After merge, confirm the next CI run's jobs complete well inside their caps.
- After the next tag, confirm the release jobs complete and note their durations here.

## Handoff

- Next owner: the maintainer.
- Next steps: settle the `pypi` approval-wait question or accept the risk before the next tag; decide whether to add a "Not run, and why" line to the PR template (a further `standard+authority` path). Control Rod's matching record is Control-Rod#92.

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
