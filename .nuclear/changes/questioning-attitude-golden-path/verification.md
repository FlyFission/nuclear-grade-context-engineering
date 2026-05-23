# Verification

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| QA-001 | Public-doc tests and `rg` scan. | No canonical `Frame -> ...` lifecycle remains; baseline appears late. | pass | `python -m pytest -q`; public-surface `rg` scan. | None known. |
| QA-002 | Skill and command contract tests. | New skill/command exists, indexed, cataloged, and contract-valid. | pass | `python -m pytest -q`. | None known. |
| QA-003 | CLI tests and doctor. | Golden-path templates checked and listed. | pass | `python -m pytest -q`; `python tools/ng.py doctor .`. | None known. |
| QA-004 | Boundary and residue scan. | DOE-HDBK-1028 wording is lineage only; local paths removed. | pass | Public-surface `rg` scan. | None known. |

## Required links

- `risk.md`
- `basis.md`
- `ship.md`

## Exit criteria

- Verification status is pass before release decision.
- Evidence is linked or summarized from reproducible local commands.

## Source-lineage note

Original verification record mapped to public source lineage in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
