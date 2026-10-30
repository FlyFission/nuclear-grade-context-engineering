# Ship: WS1 consequence engine

## Release identity

- Slug: ws1-consequence-engine
- Change: new `ng required-mode` engine, CLI, backtest tool, and tests; no release version change.
- Owner: FlyFission (maintainer)

## Scope and exclusions

- In scope: `nuclear_grade/consequence.py`, `nuclear_grade/globmatch.py`, the `required-mode` subcommand, `tools/ng_policy_backtest.py`, tests, and the CLI reference entry.
- Excluded: the repository policy file, the CI job, the hook change, and enforcement. Each is a later WS1 change with its own record.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Engine requirements REQ-001..004, REQ-006 | pass | [`verification.md`](verification.md) |
| Claim detection REQ-005 | pass | [`verification.md`](verification.md) |
| Independence of evidence | gap | all decisive evidence is self-check (see below) |

## Residual risks and gaps

- Decisive evidence is self-check: the agent wrote the engine and its tests; CI re-runs them, and maintainer review is the independent check. Accepted because nothing enforces on this output yet; the change that turns the gate on must carry separated evidence.
- Claim detection is heuristic. Paraphrase can evade it and ordinary wording can trip it. The policy is the control surface: the next change tunes it against owner-labelled commits, and human review stays the real check on public wording.

## Rollback / restore plan

- Revert the commit. Nothing depends on the engine until the CI change lands.

## Monitoring and post-release checks

- When the CI job lands in advisory mode, watch its receipts on real PRs for false positives and misses before enforcing.

## Handoff

- Next owner: the agent continuing WS1, or the maintainer.
- Next steps: add `.nuclear/consequence-policy.json` (a `standard+authority` change by its own rule), label about 20 past commits for the backtest, then the advisory CI job.

## Release decision

- **Decision:** ship with named residual risk (self-check evidence; heuristic claim detection), pending maintainer review.
- **Decider:** maintainer (FlyFission).

## Apply clearance

- Applied by merging the PR; the maintainer merges. The agent has no merge authority.

## Baseline trigger

- A baseline is recorded when the gate becomes enforcing, not at this step.

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`plan.md`](plan.md), [`trace.md`](trace.md), [`verification.md`](verification.md)

## Exit criteria

- The release decision, rollback, and monitoring are stated.
- Residual risks are named, not hidden.

## Source-lineage note

Original Nuclear-grade ship record; release-readiness lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
