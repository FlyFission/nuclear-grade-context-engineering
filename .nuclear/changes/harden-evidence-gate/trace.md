# Trace

## Trace summary

| ID | Claim | Basis link | Control / design feature | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|
| C-001 | Validator rejects packets that still carry the marker. | `basis.md` | `PLACEHOLDER_MARKER` constant and per-file check in `validate_packet`. | `verification.md` C-001 row. | ship | pass |
| C-002 | Each template under quick/standard/cm/golden-path carries exactly one marker. | `basis.md` | Manual injection plus grep. | `verification.md` C-002 row. | ship | pass |
| C-003 | Marker is absent from real packets, the flagship example, and fixtures. | `basis.md` | Repo grep. | `verification.md` C-003 row. | ship | pass |
| C-004 | Doctor requires the four added public files. | `basis.md` | `REQUIRED_PUBLIC_FILES` update in `cli.py`. | `verification.md` C-004 row. | ship | pass |
| C-005 | SWOT report is removed from version control and from public docs. | `basis.md` | `git mv` plus README bullet removal. | `verification.md` C-005 row. | ship | pass |

## Evidence chain

```text
Risk: scaffold validates green
  -> Basis: load-bearing marker + doctor coverage + clean public tree
  -> Control: marker constant + per-file validator check + template injection + REQUIRED_PUBLIC_FILES + .research/ move
  -> Verification: pytest, doctor, all packet validations, repo greps
  -> Release decision: ship; baseline trigger = the validator and templates files are now controlled items.
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| `docs/00-standards-foundation/flyfission-ops-knowledge-graph-usage.md` keeps FlyFission-specific framing. | Vendor-neutral framing is a public-positioning goal. | defer | maintainer | Next public-positioning pass. |
| Defense-in-depth table-row status check. | A stricter status rule would resist prose collisions even better. | defer | maintainer | Recorded as deferred in `verification.md`; revisited when the minimal_standard_packet fixture is reviewed. |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Each claim has a status.
- Open gaps have explicit dispositions.

## Source-lineage note

Original Nuclear-grade trace record grounded in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
