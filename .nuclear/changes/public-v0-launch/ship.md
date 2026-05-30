# Ship — Public v0 Launch

**Purpose:** State the decision to go public plainly.

---

## Release identity

- **Change slug:** `public-v0-launch`
- **Version / release / baseline:** Public v0 launch-ready main branch
- **PR / commit / artifact:** Launch-readiness PR plus final README workflow-selling PR
- **Owner:** Maintainer
- **Date:** 2026-05-19
- **Intended release window:** After final README workflow-selling PR review, CI pass, and maintainer visibility toggle.

## Scope and exclusions

- **Included:** Public residue cleanup, source-map status labels, Quick/Standard validator support, tests, launch packet, PR/visibility gate.
- **Excluded:** C-002/C-003 implementation, all-mode validator support, marketing site, formal compliance package, production sandbox claims.
- **Known non-goals:** Certification, regulator-facing submittal, formal QA program, or production security product.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified. |
| Basis / requirements / claims | pass | `basis.md` | Launch claims L-001 through L-005 defined. |
| Trace | pass | `trace.md` | Claims mapped to evidence and release posture. |
| Verification | pass | `verification.md` | Local commands and scans passed. |
| Source-lineage evidence | pass | `source-map.md` | Status labels added; source-gap scan passed. |
| License/use boundary | pass | `verification.md` | MIT reuse separated from formal assurance, V&V, QA, regulatory, procurement, and fitness claims. |
| AI-assisted work checks | pass | `verification.md` | Independent checks performed locally. |
| Review / approval | pass | launch and README workflow-selling PRs | Copilot review and CI required before merge. |
| GitHub visibility | planned | `gh repo view` | Maintainer toggle remains the only remaining side effect. |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Public sources can move or change. | Links may age. | accept with source status labels and future maintenance. | Maintainer | Broken link or source update. |
| Validator covers Quick/Standard only. | Broader modes require human review or future tooling. | accept for public v0; document scope. | Maintainer | Public docs claim broader validator support. |
| C-002/C-003 remain unimplemented. | Agent permission example covers only C-001/C-004a. | defer and do not claim. | Maintainer | Worked-example expansion. |
| Legal review is not formal counsel review. | License/use boundary docs may not satisfy every jurisdiction, contract, or customer requirement. | accept for public v0; recommend qualified review for regulated/customer-facing reliance. | Maintainer | Commercial, regulated, procurement, or customer assurance use. |
| GitHub visibility toggle remains manual. | Repo stays private until maintainer completes the final action. | accept; intentional final control point. | Maintainer | `gh repo view` still reports private. |

## Rollback / restore plan

- **Rollback method:** Revert the launch PR before visibility flip; after visibility flip, make repo private again and revert if a blocker is discovered.
- **Data migration reversal or restore notes:** Not applicable.
- **Feature flag / kill switch:** GitHub repository visibility remains private until all gates pass.
- **Owner on call:** Maintainer.
- **Time to restore estimate:** Less than 30 minutes for visibility rollback if GitHub access is available.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| GitHub visibility | Repository reports public after final flip. | Maintainer | `gh repo view FlyFission/nuclear-grade-context-engineering --json visibility,url` | Retry or stop and report blocker. |
| CI status | Launch and README workflow-selling PR checks pass. | Maintainer | GitHub PR checks. | Fix before merge. |
| Reader confusion / overclaim risk | Any issue/comment suggesting compliance, regulated verification, NQA-1, QA records, production sandboxing, or regulated-use fitness. | Maintainer | GitHub issues/reviews. | Narrow README/disclaimer/example language. |
| Validator behavior | Quick and Standard packets validate as documented. | Maintainer | Local/CI pytest and validator output. | Patch validator or docs. |

## Handoff

- **Operator/customer/support notes:** This is a public educational v0 under MIT, not a compliance, regulated verification, QA, regulatory, procurement, or production security product.
- **Docs/runbook updated:** README, Quickstart, source map, tools docs, worked example, launch packet, and onboarding path.
- **Communication needed:** Public announcement should emphasize bounded evidence and non-claims.
- **Follow-up date:** First post-public issue triage after visibility flip.

## Release decision

- **Decision:** ready for maintainer visibility toggle after final README workflow-selling PR merge.
- **Decision maker:** Maintainer.
- **Rationale:** Launch changes are merged and verified; public visibility is intentionally the final maintainer-controlled side effect.
- **Conditions attached:** Do not flip visibility if final PR CI or review fails, or if `gh repo view` does not identify the expected repository.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- PR/commit/release artifact: launch-readiness PR and final README workflow-selling PR
- Monitoring/dashboard/log query: GitHub PR checks and `gh repo view`
- Rollback/runbook: visibility rollback and PR revert if needed

## Exit criteria

- Release decision is explicit.
- Evidence status and gaps are visible.
- Rollback/restore path exists.
- Monitoring/handoff covers the public visibility claim.
- Any accepted residual risk has an owner and recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public configuration-management, release-readiness, software-assurance, lifecycle, and operating-learning concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
