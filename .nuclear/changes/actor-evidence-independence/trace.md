# Actor-Evidence Independence — Traceability

## Purpose

Tie each claim to where it is implemented and how it is verified.

## Claim-to-implementation-to-evidence

| Claim | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `actor-evidence-independence.md`; `agent-authority-model.md` Self-authorship boundary | The page and section exist with the independence rungs | pass |
| REQ-002 | `WORKFLOWS.md`, `lifecycle.md`, `README.md`, `CORE.md`, `proving-claims`, `checking-release-readiness` | The seam is named at Verify/Review/Decide; grep reaches it from each | pass |
| REQ-003 | `verification.md`, `ship.md`, `quick/proof.md`, `validators.md`, `agent-threat-model.md` | Template fields present; validator check kept as a deferred disclosure | pass |
| REQ-004 | The repo test suite and validators | pytest 190 passed / 1 skipped; ruff clean; doctor OK; tokens OK | pass |

## Required links

- Basis: `basis.md`
- Verification: `verification.md`
- Ship: `ship.md`

## Exit criteria

- Every claim maps to an implementation and an evidence row.
- No claim is left without a status.

## Source-lineage note

Original Nuclear-grade packet inspired by public software-assurance and traceability ideas mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
