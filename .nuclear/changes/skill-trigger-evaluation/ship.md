# Skill Trigger Evaluation Ship Decision

## Release identity

- Change slug: skill-trigger-evaluation
- Version / release / baseline: public main follow-up
- PR / commit / artifact: pending local commit
- Owner: FlyFission
- Date: 2026-05-25
- Intended release window: after local validation passes

## Scope and exclusions

- Included: Skill frontmatter descriptions, skill-evaluation prompt bank, authoring contract, reference index, contract tests, and packet record.
- Excluded: Runtime CLI behavior, lifecycle vocabulary, package publishing, and formal benchmark viewer output.
- Known non-goals: No formal assurance, compliance, certification, safety, security, or regulatory adequacy claim.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode selected for public skill-surface change |
| Basis / requirements / claims | pass | `basis.md` | Three bounded requirements captured |
| Questioning attitude | not applicable | `risk.md` | Summary captured in risk record |
| Verification | pass | `verification.md` | Commands passed locally |
| Dependency / supply-chain evidence | not applicable | none | No dependency changes |
| AI-assisted work checks | pass | `verification.md` | Local tool-assisted edits validated |
| Review / approval | pass | local review | User requested updates after adversarial review |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Prompt bank is not a full benchmark | Trigger quality still needs future measured evals | accept | FlyFission | Major skill rewrite or packaging |
| Descriptions may over-trigger adjacent skills | Some prompts could select a related skill first | mitigate | FlyFission | Real use shows repeated wrong trigger |

## Rollback / restore plan

- Rollback method: Revert the commit for this packet and associated files.
- Data migration reversal or restore notes: No data migration.
- Feature flag / kill switch: not applicable.
- Owner on call: FlyFission
- Time to restore estimate: less than 15 minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Skill trigger complaints | Repeated reports of missed or wrong skill activation | FlyFission | Issues, PR comments, user feedback | Update prompt bank and descriptions |
| Contract tests | Must pass on public main | FlyFission | GitHub Actions or local pytest | Block release until fixed |
| Public boundary language | No formal assurance overclaims | FlyFission | Public docs review | Run legal/source boundary skills |

## Handoff

- Operator/customer/support notes: Future skill edits should start from `docs/05-reference/skill-evaluation.md`.
- Docs/runbook updated: yes, reference index and authoring contract updated.
- Communication needed: mention eval prompt bank in release notes if this becomes a tagged release.
- Follow-up date: next material skill rewrite.

## Release decision

- Decision: ship
- Decision maker: FlyFission
- Rationale: The change is useful, scoped, and passed local contract, doctor, and packet validation.
- Conditions attached: Re-run skill evaluation prompts before any major skill rewrite or packaging change.

## Baseline trigger

- Baseline required? yes
- Baseline record: repository main after commit and push
- Revalidation trigger: Skill descriptions, skill folders, or evaluation prompt bank change.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: pending local commit
- Monitoring/dashboard/log query: GitHub issues and CI
- Rollback/runbook: git revert of this change

## Exit criteria

- Release decision is explicit.
- Baseline trigger is explicit when controlled state changes.
- Evidence status and gaps are visible.
- Rollback/restore path exists or the lack is consciously accepted.
- Monitoring/handoff covers the claims most likely to fail in operation.
- Any accepted residual risk has an owner and recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public configuration-management, release-readiness, secure-development, software-assurance, supply-chain, lifecycle, and operating-learning concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
