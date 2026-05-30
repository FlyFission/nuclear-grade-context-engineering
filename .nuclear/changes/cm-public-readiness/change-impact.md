# Change Impact - CM Public Readiness

**Purpose:** Check which downstream files the CM (keeping the approved version under control) public-readiness pass affects.

## Change context

- Slug: `cm-public-readiness`
- Related packet: `.nuclear/changes/cm-public-readiness/`
- Owner: Maintainer
- Date: 2026-05-23

## Impact screen

| Artifact family | Impact | Required action | Evidence / link | Disposition | Owner |
|---|---|---|---|---|---|
| Docs/public claims | Public thesis changes from evidence workflow to CM for AI-assisted work. | Update README, workflows, quickstart, docs map, roadmap. | `README.md`, `WORKFLOWS.md`, `QUICKSTART.md` | update | Maintainer |
| Tests/evals/validator | Package entry point changes; catalog grows. | Add packaging test, update skill/command tests. | `tests/test_packaging.py`, contract tests | update | Maintainer |
| Skills/commands/templates | CM actions become first-class. | Add CM skills, commands, templates, indexes, manifest. | `skills/`, `commands/`, `templates/cm/` | update | Maintainer |
| Dependencies/models/tools | No new runtime dependency. | Keep standard-library CLI/validator. | `pyproject.toml` | no-op | Maintainer |
| Release/operate/support | Public baseline changes. | Add baseline record and ship decision. | `baseline.md`, `ship.md` | update | Maintainer |

## Revalidation triggers

| Trigger | What must be rerun or reviewed | Owner |
|---|---|---|
| Skill/command/template catalog changes | Contract tests, doctor, manifest review | Maintainer |
| Public CM claim changes | Public-doc scan and boundary review | Maintainer |
| Packaging metadata changes | Packaging test and editable install | Maintainer |
| Validator mode expansion | Validator tests and docs update | Maintainer |

## Required links

- `risk.md`
- `basis.md`
- `controlled-items.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Impacted artifact families are updated or explicitly no-op.
- Revalidation triggers are visible.
- No stale public claim or validator behavior is silently accepted.

## Source-lineage note

Original Nuclear-grade impact record inspired by public configuration-management, secure-development, lifecycle, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
