# Trace — Enterprise Landing Page

**Purpose:** Tie each landing-page claim to its basis, its control feature, its verification evidence, and its release stance.

---

## Change context

- **Slug:** `enterprise-landing-page`
- **Related basis record:** `basis.md`
- **Related verification record:** `verification.md`
- **Owner:** Maintainer
- **Date:** 2026-06-06

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Project, one idea, and proof appear within the first screen. | `basis.md` | `plan.md` step 3 / `README.md` | Hero, "What this is", "The one idea", "See it work" at the top. | local proof | `verification.md` | ship | pass |
| REQ-002 | Every embedded diagram has an adjacent text fallback. | `basis.md` | `plan.md` step 3 / `README.md` | "In words" line under each Mermaid block. | local proof | `verification.md` | ship | pass |
| REQ-003 | Boundary and disclaimer language stays present, uncollapsed, and negative. | `basis.md` | `plan.md` step 3 / `README.md` | "What this is NOT" and license/limits kept expanded. | local proof | `verification.md` | ship | pass |
| REQ-004 | New diagrams are canonical in `docs/diagrams.md` and embedded, not forked. | `basis.md` | `plan.md` step 1 / `docs/diagrams.md` | Sections 6 and 7 are the source; README mirrors them. | local proof | `verification.md` | ship | pass |
| REQ-005 | Counts are qualified with the version and point to the live source. | `basis.md` | `plan.md` step 3 / `README.md` | "As of v0.5.0" with links to `nuclear-grade.yaml`. | fact | `verification.md` | ship | pass |
| REQ-006 | Relative links resolve and CI doc invariants are preserved. | `basis.md` | `plan.md` step 3 / `tests/test_public_docs.py` | Lifecycle line and HPI phrase kept verbatim; links verified. | local proof | `verification.md` | ship | pass |

## Evidence chain

```text
Risk / need: a dense README that newcomers cannot parse, with overclaim and rendering hazards
  → Basis / requirement: REQ-001..006 (clarity, fallbacks, no overclaim, canonical diagrams, honest counts, intact invariants)
  → Control / design feature: top-loaded pitch, per-diagram fallbacks, expanded disclaimers, single diagram source
  → Verification evidence: doc tests, Mermaid validation, count cross-check, link check, packet validation
  → Release decision: ship docs-only change; revert by git if a defect is found
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| PyPI may strip the SVG banner from the long description. | The hero image may not show on PyPI. | accept; the plain H1 title and text carry the page. | Maintainer | Next PyPI release renders without the banner. |
| External shields.io badges depend on a third-party service. | A badge image could fail to load. | accept; badges are decorative, not load-bearing. | Maintainer | A badge image breaks. |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation: `README.md`, `docs/diagrams.md`, `docs/assets/landing-banner.svg`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- A reviewer can move from claim to basis to evidence to decision quickly.

## Source-lineage note

Original Nuclear-grade trace record inspired by public sources on requirements tracing, verification, and configuration management mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
