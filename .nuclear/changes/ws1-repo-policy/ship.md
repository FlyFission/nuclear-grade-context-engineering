# Ship: WS1 repository consequence policy

## Release identity

- Slug: ws1-repo-policy
- Change: new `.nuclear/consequence-policy.json`, its test, a CLI reference sentence, and a correction to the engine record; no release version change.
- Owner: FlyFission (maintainer)

## Scope and exclusions

- In scope: the four paths named in `risk.md`.
- Excluded: the CI job that reads the policy, enforcement, the hook change, the bot identity, and owner-labelled tuning.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Rule mapping REQ-001..005 | pass | [`verification.md`](verification.md) |
| Backtest BT-001 | pass | [`verification.md`](verification.md) |
| Ground truth for enforcement | gap | owner labels not yet supplied |
| Independence of evidence | gap | all decisive evidence is self-check |

## Residual risks and gaps

- **Self-check evidence.** The agent wrote the policy and the test that pins it. CI re-runs the test; maintainer review is the independent check.
- **No ground truth yet.** The policy would have failed 12 of 49 merged commits. Before enforcement, the owner labels about 20 commits with the mode they should have needed, and the policy is tuned against those labels.
- **`gate-cli` is partial.** It fires when changed lines in `nuclear_grade/cli.py` name gate-wiring identifiers. A change to `handle_required_mode` that names none of them stays at the floor. The durable fix is to move the handler into `nuclear_grade/consequence.py`, which the `validators` rule covers by path.
- **`bot_identities` is empty.** The engine still excludes any `[bot]` login and the PR author, but agent pushes under the owner's account cannot be told apart from the owner until the bot identity exists (owner decision 4).
- **The policy cannot gate itself.** Any change to it needs `standard+authority`, which needs an approving review from someone other than the PR author. While the agent pushes as the owner, the owner's merge is the only approval available.

## Rollback / restore plan

- Revert the commit. The engine falls back to its built-in policy (CI and gate files only).

## Monitoring and post-release checks

- When the advisory CI job lands, compare its receipts on real PRs against this backtest before enforcing.

## Handoff

- Next owner: the agent continuing WS1, or the maintainer.
- Next steps: the owner labels about 20 commits; the advisory `consequence-gate` CI job (a `standard+authority` change); the bot identity.

## Release decision

- **Decision:** ship as policy only, with named residual risk, pending maintainer review.
- **Decider:** maintainer (FlyFission).

## Apply clearance

- Applied by merging the PR; the maintainer merges. The agent has no merge authority for this change.

## Baseline trigger

- A baseline is recorded when the gate becomes enforcing.

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`plan.md`](plan.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`decision-authority.md`](decision-authority.md)

## Exit criteria

- The release decision, rollback, and monitoring are stated.
- Residual risks are named, not hidden.

## Source-lineage note

Original Nuclear-grade ship record; release-readiness lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
