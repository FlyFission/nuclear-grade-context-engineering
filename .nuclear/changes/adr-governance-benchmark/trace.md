# Trace — ADR governance lessons and landscape benchmark

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `nuclear_grade/mcp_server.py`, `pyproject.toml`, `ci.yml` `mcp-smoke` | E-001 | pass |
| REQ-002 | `nuclear_grade/receipt.py`, `nuclear_grade/cli.py` | E-002 | pass |
| REQ-003 | `ci.yml` `CI gate` | E-003 | deferred |
| REQ-004 | `.github/dependabot.yml` | E-003 | deferred |

REQ-003 and REQ-004 only run on GitHub. Local evidence is limited to YAML parsing, so final status waits on the PR run.

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability is an internal review aid, not formal verification and validation. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
