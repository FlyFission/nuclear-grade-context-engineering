# Trace

## Claim-to-evidence map

| Claim | Basis | Control / design feature | Evidence | Status |
|---|---|---|---|---|
| E-001 action-first WBS exists | `basis.md` | Top-level docs plus adoption/reference docs | `README.md`, `WORKFLOWS.md`, `docs/README.md` | pass |
| E-002 skills and commands are contract-tested | `basis.md` | Required contract tests | `tests/test_skill_contracts.py`, `tests/test_command_contracts.py` | pass |
| E-003 CLI supports product surface | `basis.md` | `tools/ng.py` command parser | `tests/test_ng_cli.py` | pass |
| E-004 boundary wording is propagated | `basis.md` | Public docs test and scans | `tests/test_public_docs.py` | pass |

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Every status is pass, gap, deferred, or blocked before release.

## Source-lineage note

This trace record is part of the original Nuclear-grade packet workflow and references `docs/00-standards-foundation/source-map.md`.
