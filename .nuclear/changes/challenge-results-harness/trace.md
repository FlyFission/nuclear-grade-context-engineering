# Trace: challenge results harness

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `challenge/score.py` `to_json`, `main` | E-001 | pass |
| REQ-002 | `challenge/judge/manifest.json` | E-001 | pass |
| REQ-003 | `challenge-results/run.py` | E-002 | pass |
| REQ-004 | `challenge-results/run.py` `fresh_copy`, `tracks/plain/AGENTS.md` | E-002 | pass |
| REQ-005 | `challenge-results/build.py` | E-002 | pass |
| REQ-006 | `challenge-results/agents.json` | E-003 | deferred |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Original Nuclear-grade record inspired by public configuration-management and operating-experience concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
