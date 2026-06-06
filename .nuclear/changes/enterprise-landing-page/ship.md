# Ship — Enterprise Landing Page

**Purpose:** State the release decision for the landing-page overhaul plainly.

---

## Release identity

- **Change slug:** `enterprise-landing-page`
- **Version / release / baseline:** Landing-page README on `claude/enterprise-landing-page-uSnWo`
- **PR / commit / artifact:** Landing-page draft PR
- **Owner:** Maintainer
- **Date:** 2026-06-06
- **Intended release window:** After maintainer review and CI pass on the branch.

## Scope and exclusions

- **Included:** README rewrite, two canonical diagrams, the SVG hero banner, and this Standard packet.
- **Excluded:** Any GitHub Pages site, HTML, build step, or changes to skills, commands, templates, the CLI, or the charter.
- **Known non-goals:** Marketing claims, compliance language, or assurance the project does not provide.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified. |
| Basis / requirements / claims | pass | `basis.md` | REQ-001 through REQ-006 defined. |
| Trace | pass | `trace.md` | Claims mapped to evidence and release posture. |
| Verification | pass | `verification.md` | Doc tests, validator, doctor, token gate, and Mermaid validation passed. |
| Diagram fallbacks | pass | `README.md` | Each embedded diagram carries an "In words" fallback. |
| Boundary / disclaimer wording | pass | `tests/test_public_docs.py` | Boundary phrases stay negative; disclaimers stay expanded. |
| AI-assisted work checks | pass | `verification.md` | Independent deterministic checks performed locally. |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| PyPI may strip the SVG banner from the long description. | The hero image may not show on PyPI. | accept; the plain H1 title and text carry the page. | Maintainer | Next PyPI release renders without the banner. |
| External shields.io badges depend on a third-party service. | A badge image could fail to load. | accept; badges are decorative, not load-bearing. | Maintainer | A badge image breaks. |
| Component counts are a v0.5.0 snapshot. | A count could age as the catalog grows. | accept; counts are version-qualified and point to the live source. | Maintainer | `nuclear-grade.yaml` changes. |

## Rollback / restore plan

- **Rollback method:** `git revert` the landing-page commit; the previous README and `docs/diagrams.md` return unchanged.
- **Data migration reversal or restore notes:** Not applicable; documentation-only change.
- **Feature flag / kill switch:** Not applicable; the PR is the gate.
- **Owner on call:** Maintainer.
- **Time to restore estimate:** Under ten minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI status | Doc tests, validator, doctor, and token gate pass. | Maintainer | Branch CI checks. | Fix before merge. |
| Reader confusion / overclaim risk | No issue suggesting the page implies compliance or assurance. | Maintainer | GitHub issues and reviews. | Narrow the wording. |
| Rendering | Banner and diagrams render on GitHub; fallbacks read on PyPI. | Maintainer | Rendered README on the branch and the next PyPI page. | Adjust the asset or fallback. |

## Handoff

- **Operator/customer/support notes:** This is a public educational v0 under MIT, not a compliance, regulated-verification, or assurance product.
- **Docs/runbook updated:** README, `docs/diagrams.md`, and the new banner asset.
- **Communication needed:** The PR description explains the before/after, the new diagrams, the banner, and this packet.
- **Follow-up date:** First post-merge issue triage.

## Release decision

- **Decision:** ship with named residual risk.
- **Decision maker:** Maintainer.
- **Rationale:** The change is documentation-only, reversible, and verified; the residual risks are bounded, owned, and have recheck triggers.
- **Conditions attached:** Do not merge if CI or maintainer review fails.
- **Abort or rollback trigger:** Any failing doc test, a broken fallback, or an overclaim found in review.

## Baseline trigger

- **Baseline required?** yes; the public landing page is a controlled item.
- **Baseline record:** The merged commit on the default branch becomes the README baseline.
- **Revalidation trigger:** A change to the component counts, the lifecycle, or the boundary wording.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: landing-page draft PR
- Monitoring: branch CI checks
- Rollback: `git revert` of the landing-page commit

## Exit criteria

- The release decision is stated plainly.
- The baseline trigger is named because a controlled item changed.
- The evidence status and the gaps are visible.
- A rollback path exists.
- Any accepted residual risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public ideas on configuration management, release readiness, and software assurance mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
