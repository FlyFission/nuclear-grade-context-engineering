# Plan

## Build sequence

1. Add failing contract and public-doc tests for the new skill, command, golden-path templates, and lifecycle wording.
2. Add the `questioning-attitude` skill, `ng-question` command, and golden-path templates.
3. Wire CLI doctor/list, manifest, indexes, and docs.
4. Update lifecycle, CM, quickstart, workflow, reviewer, source-map, and crosswalk language.
5. Run tests, doctor, packet validation, and public scans.

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| `README.md`, `WORKFLOWS.md`, `QUICKSTART.md` | Questioning Attitude public hook and golden path. | First-reader comprehension. | Codex |
| `skills/`, `commands/`, `templates/golden-path/` | New portable workflow surfaces. | Agent usability. | Codex |
| `nuclear_grade/cli.py`, tests, manifest | Doctor/list and contracts. | Machine-checkable consistency. | Codex |
| `docs/00-standards-foundation/`, `docs/01-field-guide/` | DOE-HDBK-1028 source lineage. | Public citation hygiene. | Codex |

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Work is bounded to the approved plan.
- Tests and scans identify stale vocabulary or missing artifacts.

## Source-lineage note

Original implementation plan mapped to public source lineage in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
