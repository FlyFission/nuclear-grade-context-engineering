# Controlled Items - CM Public Readiness

**Purpose:** Name the controlled items the public-readiness pass affects.

## Change context

- Slug: `cm-public-readiness`
- Related packet: `.nuclear/changes/cm-public-readiness/`
- Owner: Maintainer
- Date: 2026-05-23

## Controlled item table

| Item | Type | Current state | Intended state | Why controlled | Owner | Evidence / link | Revalidation trigger |
|---|---|---|---|---|---|---|---|
| Public README/workflow docs | Public docs | Evidence-workflow first | CM-first public thesis | First public trust surface. | Maintainer | `README.md`, `WORKFLOWS.md` | Public confusion or claim expansion |
| CM operating docs | Doctrine | Missing as first-class docs | Controlled items, impact, baseline, variance, OPEX, re-baseline docs | Core product promise. | Maintainer | `docs/02-operating-system/` | CM templates or lifecycle changes |
| CM templates | Templates | Not present | Activated CM records | Turns thesis into usable artifacts. | Maintainer | `templates/cm/` | Validator or workflow expansion |
| CM skills/commands | Agent surface | Not present | Portable CM actions | Skill-pack utility. | Maintainer | `skills/`, `commands/` | Skill/command contract changes |
| CLI package entry point | Tooling | `tools.ng:main` | `nuclear_grade.cli:main` | Avoids install collision. | Maintainer | `pyproject.toml`, `nuclear_grade/` | Packaging metadata changes |
| Public boundary language | Trust boundary | Evidence-oriented wording | CM wording without assurance overclaims | Prevents misuse. | Maintainer | README, DISCLAIMER, docs | New assurance terms |

## Required links

- `risk.md`
- `basis.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Each item has a reason for control.
- Each item has evidence or explicit verification path.
- Revalidation triggers are named for trust-bearing items.

## Source-lineage note

Original Nuclear-grade CM record inspired by public configuration-management and software assurance sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
