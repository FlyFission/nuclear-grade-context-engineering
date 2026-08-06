# Controlled items

## Change

- Slug: `matt-skill-lifecycle-and-flow`
- Owner: FlyFission maintainer
- Date: 2026-08-05

## Controlled-item register

| Item family | Approved state | Candidate state | Why controlled | Evidence / baseline trigger |
|---|---|---|---|---|
| Skill catalog and invocation semantics | flat 29-skill catalog at `3ade94e` | structured lifecycle registry plus checked compatibility projections | determines what may auto-route or ship | lifecycle tests; merged commit if accepted |
| Skill bodies and command prompts | inline prompts and universal section shape | bounded progressive-disclosure pilot | changes agent runtime instructions | command parity, output fixtures, token report |
| Installer and plugin exports | current core/full skills | promoted-only lifecycle filtering | controls distributed behavior | package tests and install dry runs |
| Routing evaluation | per-skill manifest and observed scorer | exact catalog scenarios and over-trigger metrics | supports retrieval claims | scorer tests and recorded runs |
| Token budgets | per-file maxima | per-file plus aggregate/profile budgets | limits standing and selected context | token tests/report |
| Workflow doctrine/templates | current eight/eleven-beat guidance | crosswalk and conditional build adapters | shapes consequential work | public-doc tests and review |
| Change packet | none | this packet | preserves basis, evidence, and decision boundary | strict validation |

## Required links

- `risk.md`
- `change-impact.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every changed controlled family appears above.
- Candidate state is not called approved until merge/release authority acts.

## Source-lineage note

This register follows the public configuration-state disciplines mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal configuration-management compliance or assurance.
