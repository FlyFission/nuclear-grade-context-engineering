# Trace - CM Public Readiness

**Purpose:** Tie the CM (keeping the approved version under control) public-readiness claims to their controls, evidence, and release stance.

## Change context

- Slug: `cm-public-readiness`
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: Maintainer
- Date: 2026-05-23

## Trace summary

| ID | Claim | Basis link | Control / design feature | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|
| CM-001 | Public thesis is configuration management for AI-assisted work. | `basis.md` | README/workflows/CM docs. | Public docs and boundary scans. | Required before public launch. | pass |
| CM-002 | Activated CM records exist without making Standard too heavy. | `basis.md` | `templates/cm/` separate from Standard. | Template presence and docs. | Required before public launch. | pass |
| CM-003 | Skills and command prompts expose CM actions. | `basis.md` | New CM skill/command cards and indexes. | Contract tests and doctor. | Required before public launch. | pass |
| CM-004 | Installed console entry point avoids `tools` package collision. | `basis.md` | Namespaced `nuclear_grade` package and explicit setuptools discovery. | Packaging tests and editable install. | Required before public launch. | pass |
| CM-005 | Public-readiness evidence remains navigable. | `basis.md` | CM packet, controlled items, impact, baseline. | Packet validation. | Required before public launch. | pass |

## Evidence chain

```text
Risk: public repo promises Nuclear-grade discipline.
  -> Basis: CM must be real and usable, not branding.
  -> Control: CM docs/templates/skills/commands plus package fix and boundary language.
  -> Verification: tests, doctor, packet validation, install check, scans.
  -> Baseline: accepted public-ready controlled state.
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| CM validator does not deeply validate CM records yet. | Public v0 should not overclaim deterministic CM assurance. | accept for v0; document Quick/Standard validator scope. | Maintainer | Validator roadmap work. |
| Additional worked examples not implemented. | Adoption improves with examples. | defer; do not claim complete coverage. | Maintainer | v0.1/v0.2 planning. |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- `controlled-items.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Each claim has a status label.
- Every shipped claim has evidence or accepted residual risk.
- Deferred/gap claims are not used as release evidence.

## Source-lineage note

Original Nuclear-grade trace record based on public-source-inspired traceability, verification, configuration, and release-readiness concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
