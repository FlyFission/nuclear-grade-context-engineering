# Ship: Inspectable builder-critic loop

## Scope and exclusions

- Included: existing workflow, briefing, prompt, plan, verification, source-map, test, and pilot-contract seams.
- Excluded: new mode/lifecycle/workflow catalog item; dedicated or promoted skill; live pilot; merge, release, deployment, or efficacy claim.
- Base: stacked on draft PR #98 until its lifecycle/catalog prerequisite merges.

## Evidence status summary

| Evidence area | Status | Notes |
|---|---|---|
| Risk/basis/requirements | pass | Standard packet complete |
| Adversarial transfer review | pass | P0/P1 controls incorporated |
| Focused RED/GREEN | pass | public and command parity behavior |
| Full local gates | pass | 346 pytest tests, Ruff, doctor, token budget, eval, command/Codex parity, strict packet, routing scenarios, and diff check |
| Independent final review | planned | exact diff, blockers resolved |
| Remote CI | planned | exact pushed head |
| Human approval | planned | maintainer merge decision |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Trigger |
|---|---|---|---|---|
| No live paired pilot observations | workflow may add cost without outcome gain | keep as optional technique; no dedicated skill or efficacy claim | maintainer | pilot proposal/promotion |
| Practitioner evidence is source-specific | generalization could overstate support | supporting-context source row and explicit boundary | maintainer | public claim change |
| Fresh model reviewers remain coupled on several axes | review may miss correlated failures | disclose profile; rely on deterministic checks and human PR review | maintainer | review disposition |
| Stacked PR depends on #98 | base diff is larger until prerequisite merges | open against #98 branch; retarget/rebase after merge | maintainer | #98 disposition |
| Template/prompt additions consume context | always-loaded cost may outweigh utility | token gate; optional section; no new skill/router | maintainer | token budget or routing proposal |

## Rollback / restore plan

- Revert the follow-up commit/branch before merge.
- No runtime, data, credentials, or deployment state changes.

## Monitoring and pilot triggers

- Measure external artifact outcomes, defects, cost, latency, and human burden under the pilot contract.
- Stop on authority/custody breach, omitted adverse evidence, hidden-case regression, coupled fan-out regression, or critic-score/external-outcome divergence.
- Require a fresh hidden confirmation set before any beta skill proposal.

## Release decision

- Decision: defer merge/release to maintainer after full evidence and PR review.
- Current authorization: draft stacked PR only.
- Conditions: full local gates, no P0/P1, exact remote head/CI, and #98 base disposition.
- Abort trigger: duplicate lifecycle/skill, weakened bar/custody, unsupported independence/efficacy claim, or unresolved serious review finding.

## Apply clearance

- Clearance: hold.
- Cleared by: not applicable.
- Re-clearance trigger: material diff, base rebase/retarget, or requirement change.

## Baseline trigger

- Baseline required if merged: merged commit, finalized packet, generated command parity, and pilot contract revision.
- Revalidation trigger: prompt/template change, dedicated skill proposal, pilot activation, or public efficacy claim.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `docs/00-standards-foundation/source-map.md`
- `docs/05-reference/inspectable-builder-critic-pilot.md`

## Exit criteria

- PR readiness remains separate from merge/release readiness.
- Residual risks and live-evidence gaps remain visible.
- Maintainer decision is requested rather than inferred.

## Source-lineage note

This ship record governs PR preparation only and uses the public source boundary in `docs/00-standards-foundation/source-map.md`. It creates no compliance, formal verification, efficacy, independence, safety, security, certification, or release claim.
