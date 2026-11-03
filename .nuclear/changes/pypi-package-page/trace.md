# Trace: Make the package page ready for PyPI

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `[project]` and `[project.urls]` in `pyproject.toml` | E-001 | pass |
| REQ-002 | `[tool.hatch.metadata.hooks.fancy-pypi-readme]` in `pyproject.toml` | E-002 | pass |
| REQ-003 | `.github/workflows/ci.yml`, `.github/workflows/release.yml` | E-003, E-005 | pass |
| REQ-004 | `docs/05-reference/releasing.md` | E-004 | pass |
| REQ-005 | no tag, no version change; wheel file list | E-006 | pass |
| REQ-001 live | The page renders as expected on PyPI | E-007 | gap |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability here is an internal review aid. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
