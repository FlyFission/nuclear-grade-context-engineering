# Trace — Public v0 Launch

**Purpose:** Tie each launch claim to its controls, evidence, and release stance.

---

## Trace summary

| ID | Claim | Basis link | Control / design feature | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|
| L-001 | Public docs contain no internal launch residue. | `basis.md#derived-requirements-or-claims` | Public residue scans and targeted doc edits. | `verification.md` | Required before PR ready. | planned |
| L-002 | Source-map entries are verified-public or explicitly downgraded. | `basis.md#derived-requirements-or-claims` | `Status` column and source-gap scans. | `verification.md` | Required before PR ready. | planned |
| L-003 | Validator supports documented Quick and Standard packet modes. | `basis.md#derived-requirements-or-claims` | Mode detection, required-file checks, local link checks. | `tests/test_ng_validate.py` | Required before PR ready. | planned |
| L-004 | Worked-example packet status matches current repo state. | `basis.md#derived-requirements-or-claims` | Packet cleanup and validation. | `verification.md` | Required before PR ready. | planned |
| L-005 | GitHub visibility changes only after merged PR and CI pass. | `basis.md#derived-requirements-or-claims` | Release gate in `ship.md`. | PR/CI/`gh repo view` evidence. | Required before public visibility. | planned |
| L-006 | License/use boundaries make MIT reuse distinct from formal assurance. | `basis.md#derived-requirements-or-claims` | License boundary docs and expanded overclaim validator seeds. | `verification.md` | Required before public visibility. | pass |

## Evidence chain

```text
Risk: public repo visibility can expose stale state or overclaims.
  -> Basis: public v0 must be honest, bounded, and source-safe.
  -> Control: residue scans, source status labels, Quick/Standard validator tests, license/use boundary docs.
  -> Verification: pytest, packet validation, diff check, scan results.
  -> Ship: PR/CI/review first, GitHub visibility flip last.
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| GitHub visibility not yet flipped. | Public release is intentionally last. | block until PR merge and CI pass. | Maintainer | PR merged. |
| C-002/C-003 not implemented. | Broader agent-permission claims remain future work. | defer and do not claim. | Maintainer | Worked-example expansion. |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- `../cm-public-readiness/`

## Exit criteria

- Each launch claim has a status label.
- Every public-v0 claim has evidence or an explicit gate.
- Deferred claims are not used as release evidence.

## Source-lineage note

This trace record is an original Nuclear-grade artifact based on public-source-inspired traceability, verification, configuration, and release-readiness concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
