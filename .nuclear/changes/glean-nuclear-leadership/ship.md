# Standard Ship Record

**Purpose:** State the acceptance decision for the gleaned nuclear-leadership value-adds.

**Activation threshold:** Standard mode: the change amends the charter and durable public doctrine plus agent-operable artifacts.

**Minimum useful version:** Evidence status, residual risk, rollback, monitoring, release decision, and baseline trigger.

**Overhead trap:** Do not treat a green suite as acceptance. Ship only when the doctrine reads cleanly and the boundary wording is reviewed.

---

## Release identity

- Change slug: glean-nuclear-leadership
- Version / baseline: branch `claude/inspiring-ride-hix4tl`
- PR / commit / artifact: forthcoming draft PR
- Owner: FlyFission
- Date: 2026-06-16
- Intended release window: after PR review

## Scope and exclusions

- Included: charter Art. 19 refinement, the just-culture distinction in a skill and a command, the control-stack independence principle, the temporary-modification discipline and template column, the competence-to-act qualification, the durable-memory doctrine, a boundary amendment, two crosswalk rows, and a nav row.
- Excluded: a leading-indicators metrics doc, a drill template, any new skill or command, any new external source, and any charter article beyond the Art. 19 refinement.
- Known non-goals: no compliance, safety, security, certification, formal-assurance, regulatory-adequacy, or legal-advice claim.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard with CM/baseline activated |
| Basis / requirements | pass | `basis.md` | One requirement per workstream, each mapped to a source |
| Trace | pass | `trace.md` | Every requirement traced to an edit and evidence |
| Verification | pass | `verification.md` | Suite, token audit, doctor, and packet validation run |
| Boundary wording | pass | `verification.md` | No prohibited compliance phrase; source-lineage notes intact |
| Review / approval | planned | PR | PR review requested by user |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Doctrine quality is partly review-based | Tests prove structure, not best wording | mitigate | FlyFission | PR review or future OPEX |
| A reader could still treat no-blame as no-accountability | The Art. 19 refinement mitigates but does not eliminate the misread | mitigate | FlyFission | OPEX if a record excuses a willful violation |

## Rollback / restore plan

- Rollback method: revert the branch commit; all changes are text in version control.
- Data migration reversal: none; no data, schema, or production state touched.
- Feature flag / kill switch: not applicable.
- Owner on call: FlyFission.
- Time to restore: one revert.

## Monitoring and post-release checks

| Signal | Expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Reader confusion | Readers treat the additions as duplicative or as ceremony | FlyFission | Issues / PR comments | OPEX and targeted trim |
| Boundary drift | A new doc implies compliance or assurance | FlyFission | Doctor, manual scan, review | Block / revert and re-word |
| Misread of just culture | An OPEX record files a willful violation as an honest mistake | FlyFission | OPEX records | Reinforce the Art. 19 distinction |

## Handoff

- Operator / support notes: not applicable; documentation and agent-instruction change only.
- Docs / runbook updated: navigation row added in `docs/README.md`.
- Communication needed: PR summary should state which report items were pulled in and which were deliberately deferred or rejected.
- Turnover record: not activated; same owner continues.
- Follow-up date: after PR review.

## Release decision

- Decision: defer until PR review passes
- Decision maker: FlyFission
- Rationale: Controlled charter and public doctrine require slow acceptance after fast candidate edits.
- Decision question answered by evidence? yes
- Conditions attached: PR review and any remote CI checks.
- Decision posture: conservative enough
- Abort or rollback trigger: prohibited compliance wording, a contract-test failure, or an actionable review left unaddressed.
- OPEX trigger: reader or agent confusion about the just-culture distinction or the memory provenance guard.

## Baseline trigger

- Baseline required? yes
- Baseline record: `baseline.md`
- Revalidation trigger: future changes to the charter, the control-stack doctrine, variance discipline, the qualification section, or the durable-memory doctrine.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `baseline.md`

## Exit criteria

- The release decision is explicit.
- The baseline trigger is explicit because controlled state changed.
- Evidence status and gaps are visible.
- A rollback path exists.
- Monitoring covers the claims most likely to fail in operation.
- Any accepted residual risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public configuration-management, release-readiness, and operating-learning concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
