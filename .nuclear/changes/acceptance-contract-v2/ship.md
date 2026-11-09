# Ship: typed acceptance contract and adversarial fixtures

## Release identity

- Slug: acceptance-contract-v2
- Change: receipt schema version 2 with a typed acceptance block, a receipt binding check, three CLI flags, one added output line, a 32-test fixture suite, and a consequence-policy edit; no release version change.
- Owner: FlyFission (maintainer)

## Scope and exclusions

- In scope: the paths named in `risk.md`.
- Excluded: any change to `validate_packet`; the scope interlock; the dependency model; signed attestations; decision custody; the published challenge results; the external evidence adapter contract; a default flip of any strict flag or of the exit code.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Typed acceptance and consumers REQ-001..005 | pass | [`verification.md`](verification.md) |
| Propagation kept advisory REQ-006 | pass | [`verification.md`](verification.md) |
| Fixtures can fail (7 of 7 controls) | pass | [`verification.md`](verification.md) |
| Ground truth for the eligibility split | gap | owner labels not yet supplied |
| Independence of evidence | gap | all decisive evidence is self-check |
| Approval replay and out-of-packet swaps | gap | strict expected failures; decision custody not built |

## Residual risks and gaps

- **Self-check evidence.** The agent wrote the contract, the fixtures, and the weakening run. CI re-runs the suite. Maintainer review is the independent check, and it is required: this change edits the consequence policy, which needs an approving review from someone other than the PR author.
- **The fixtures are the author's attacks.** They cover the named properties. They do not show the acceptance path survives an adversary who did not write them. An independent attack on the contract is the useful next evidence.
- **Eligibility is structural.** It reads declared statuses and declared claim ids. It cannot see whether a `pass` is true, whether evidence is independent, or whether a citation is real. The fixtures pin this for external citations.
- **Fail-closed cost.** 6 of 82 earlier records read `undetermined` because their claim tables have no claim-id rows. If owners judge those a format problem, either the records or the parser should change, not the meaning of `undetermined`.
- **Propagation is advisory, with a crude model.** It has no dependency edges and treats evidence-id rows as claims. It does not gate until a typed dependency model exists.
- **Default exit codes did not change.** A record with a `gap` still exits 0 from `ng validate` unless `--require-eligible` is passed. A team that wants the stricter default must choose it; that is a breaking change for the next validator release.
- **Receipts are still not signatures.** Anyone who can edit the packet and the receipt can regenerate both. `verify_receipt` shows a stored receipt matches current bytes and that its block was not hand-edited. It does not show who issued it.

## Rollback / restore plan

- Revert the commit. Receipts return to schema version 1; the extra keys are ignored by readers that do not know them.

## Monitoring and post-release checks

- Read the `Acceptance:` line on real PRs for a few weeks. Count how often `undetermined` is a format problem and not an evidence problem.
- When decision custody is built, the two expected failures should flip; the strict marker will fail the suite and force the update.

## Handoff

- Next owner: the agent continuing the roadmap, or the maintainer.
- Next steps, in order: run and publish the existing challenge results as a frozen run; a typed claim-to-evidence dependency model with invalidation; approval binding and replay resistance; a versioned external evidence contract; the scope check against the final diff.

## Release decision

- **Decision:** ship with named residual risk, pending maintainer review.
- **Decider:** maintainer (FlyFission).

## Apply clearance

- Applied by merging the PR; the maintainer merges. The agent has no merge authority for this change.

## Baseline trigger

- A baseline is recorded when the contract is made the default exit code.

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`plan.md`](plan.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`decision-authority.md`](decision-authority.md)

## Exit criteria

- The release decision, rollback, and monitoring are stated.
- Residual risks are named, not hidden.

## Source-lineage note

Original Nuclear-grade ship record; release-readiness lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
