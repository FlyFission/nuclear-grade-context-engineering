# Ship -- skill decision contracts

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

---

## Release identity

- Change slug: skill-decision-contracts
- Version / release / baseline: branch `claude/practical-faraday-dwcv5b`
- PR / commit / artifact: PR to follow
- Owner: FlyFission
- Date: 2026-06-16
- Intended release window: on review approval.

## Scope and exclusions

- Included: the `## Decision contract` block on 27 skills, its enforcement, `ng decisions`, and the doc updates.
- Excluded: command cards, agent role files, and any prose trim of skill bodies.
- Known non-goals: cutting or merging skills, and self-declaring a skill as deletable.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard; a controlled-item change |
| Basis / requirements / claims | pass | `basis.md` | REQ-001 through REQ-003 stated |
| Questioning attitude | pass | `risk.md` | summarized inline |
| Verification | pass | `verification.md` | pytest, doctor, tokens, decisions green |
| Dependency / supply-chain evidence | not applicable | `verification.md` | no dependencies added |
| AI-assisted work checks | pass | `verification.md` | human-approved and reversible |
| Review / approval | planned | the PR | human review before merge |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Some blocks are wordier than the ideal one-scan line | a mild scannability cost | accept | FlyFission | trim if a block is shown to mislead |
| The heaviest body is now 2,875 of 3,000 tokens | less budget headroom | accept | FlyFission | `ng tokens` fails on the next addition |

## Rollback / restore plan

- Rollback method: revert the branch commit.
- Data migration reversal or restore notes: none; no data is touched.
- Feature flag / kill switch: not applicable.
- Owner on call: FlyFission
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI skill-contract test | stays green | FlyFission | CI on PRs | fix the offending skill block |
| `ng tokens` budget gate | stays green | FlyFission | CI on PRs | trim the heaviest body |

## Handoff

- Operator/customer/support notes: skill authors must add the block; the contract doc explains it.
- Docs/runbook updated: `skill-authoring-contract.md`, `skill-evaluation.md`, `cli-reference.md`, `skills-token-audit.md`, `SKILLS.md`.
- Communication needed: note the new required section in the PR description.
- Turnover record if activated: not activated.
- Follow-up date: the next skill change.

## Release decision

- Decision: ship with residual risk
- Decision maker: FlyFission
- Rationale: the change is additive, reversible, and passes the contract, doctor, token, and test gates; the only residual risks (block verbosity, reduced token headroom) are minor and owned.
- Decision question answered by evidence? yes
- Conditions attached: human PR review before merge, and tighten any block later shown to mislead.
- Decision posture: conservative enough
- Abort or rollback trigger: a CI gate fails, or a reviewer rejects the contract change.
- OPEX or post-release learning trigger: a skill that cannot name a non-generic decision, which signals a relocation candidate.

## Baseline trigger

- Baseline required? yes
- Baseline record: the merged commit becomes the accepted skill-contract baseline.
- Revalidation trigger: a future change to the skill authoring contract or the validator.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: branch `claude/practical-faraday-dwcv5b`
- Monitoring/dashboard/log query: CI on the PR
- Rollback/runbook: revert the branch commit

## Exit criteria

- The release decision is stated plainly.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade change record, influenced by public release-readiness and configuration-management ideas mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
