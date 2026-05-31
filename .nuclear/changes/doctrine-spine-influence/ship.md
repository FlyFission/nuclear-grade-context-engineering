# Standard Ship Record

**Purpose:** State the acceptance decision plainly for the doctrine-spine influence update.

**Activation threshold:** Use because this Standard change affects public docs, skills, command prompts, templates, and baseline posture.

**Minimum useful version:** Evidence status, residual risks, rollback/restore, monitoring, handoff, release decision, and baseline trigger.

**Overhead trap:** Do not treat tests alone as acceptance. Ship only when evidence matches the claims and public boundary wording is reviewed.

---

## Release identity

- Change slug: doctrine-spine-influence
- Version / release / baseline: branch `add-quotes-and-influence`
- PR / commit / artifact: forthcoming PR
- Owner: FlyFission
- Date: 2026-05-30
- Intended release window: after PR review and requested Copilot review

## Scope and exclusions

- Included: public docs, selected skills, command cards, Standard templates, skill-evaluation prompts, packet, CM/OPEX/baseline records.
- Excluded: quotes, attributions, new doctrine page, CLI behavior, validator rules, dependencies, model/API/tool trust changes, release automation.
- Known non-goals: no compliance, safety, security, certification, formal assurance, regulatory adequacy, or legal advice claim.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard with CM/OPEX/baseline activated |
| Basis / requirements / claims | pass | `basis.md` | Control stack and non-goals explicit |
| Verification | pass | `verification.md` | Packet validation, tests, doctor, and scan run |
| Boundary wording | pass | `verification.md` | Scan reviewed for expected boundary-safe contexts |
| AI-assisted work checks | pass | `verification.md` | Local deterministic checks passed; PR review pending |
| Review / approval | planned | PR | Copilot/actionable review requested by user |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Semantic doctrine quality is partly review-based | Tests cannot prove the wording is the best possible translation | mitigate | FlyFission | PR review or future OPEX |
| Validator does not enforce doctrine-spine fields beyond current template checks | Future shallow updates could pass structure-only checks | defer | FlyFission | Repeated OPEX or reviewer finding |

## Rollback / restore plan

- Rollback method: revert the PR/commit.
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: not applicable.
- Owner on call: FlyFission.
- Time to restore estimate: one revert.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| User confusion | Users treat doctrine as extra ceremony or quotes are requested as public proof | FlyFission | Issues/PR comments | OPEX and targeted docs/templates adjustment |
| Agent misuse | Agents skip decision question, overclaim evidence, or blur build/audit phases | FlyFission | PR packets and reviews | Update skill/evaluation prompts |
| Boundary drift | Public wording implies assurance or source satisfaction | FlyFission | Doctor, scans, reviews | Block/revert and source/legal check |

## Handoff

- Operator/customer/support notes: not applicable.
- Docs/runbook updated: adoption docs and entrypoints updated in this change.
- Communication needed: PR summary should state no quotes/attributions or new assurance claims were added.
- Turnover record if activated: not activated.
- Follow-up date: after PR review.

## Release decision

- Decision: defer until PR review and requested Copilot review pass
- Decision maker: FlyFission
- Rationale: Controlled public workflow artifacts require slow acceptance after fast candidate edits.
- Decision question answered by evidence? yes
- Conditions attached: PR/Copilot review and any remote CI checks.
- Decision posture: conservative enough
- Abort or rollback trigger: quote insertion, unsafe assurance wording, contract test failure, or actionable review that is not addressed.
- OPEX or post-release learning trigger: user or agent confusion about decision question, evidence grounding, or build/audit phase separation.

## Baseline trigger

- Baseline required? yes
- Baseline record: `baseline.md`
- Revalidation trigger: future changes to charter, lifecycle, HPI overlays, activation thresholds, selected skills/commands, Standard templates, evaluation prompts, or public boundary wording.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: forthcoming PR
- Monitoring/dashboard/log query: GitHub issues/PR feedback
- Rollback/runbook: revert commit/PR

## Exit criteria

- Release decision is explicit.
- Baseline trigger is explicit when controlled state changes.
- Evidence status and gaps are visible.
- Residual uncertainty is bounded, owned, or blocks/defer the decision.
- Rollback/restore path exists or the lack is consciously accepted.
- Monitoring/handoff covers the claims most likely to fail in operation.
- Any accepted residual risk has an owner and recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public configuration-management, release-readiness, secure-development, software-assurance, supply-chain, lifecycle, and operating-learning concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
