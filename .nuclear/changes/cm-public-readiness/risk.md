# Risk - CM Public Readiness

**Purpose:** Sort by risk the repo-wide shift from an evidence-workflow framing to keeping the approved version under control (configuration management, CM) for AI-assisted software work.

## Change identity

- Slug: `cm-public-readiness`
- PR / issue: local public-readiness pass
- Owner: Maintainer
- Date: 2026-05-23
- Current lifecycle phase: Verify
- Summary: Reposition Nuclear-grade around controlled configuration, add activated CM docs/templates/skills/commands, fix package entry point, and preserve public boundary language.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Public README/workflows/quickstart | Public docs | First public framing and onboarding. | `../../../README.md` |
| CM operating docs | Doctrine | Defines controlled items, impact, baselines, variance, OPEX, and re-baseline. | `../../../docs/02-operating-system/configuration-management.md` |
| Skills and commands | Agent surface | Makes the repo useful as a portable skill/workflow pack. | `../../../SKILLS.md`, `../../../COMMANDS.md` |
| Templates | Evidence records | Gives reviewers concrete CM artifacts without activating a full binder. | `../../../templates/cm/` |
| CLI/package entry point | Tooling | Prevents install-time package discovery failure and top-level `tools` collision. | `../../../pyproject.toml`, `../../../nuclear_grade/` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | High | Public thesis, tooling, skills, and docs all change. |
| Reversibility | Medium | Docs are reversible, but public launch impressions and forks persist. |
| Detectability | Medium | Stale links and overclaims require scans and tests. |
| Exposure | High | Repo is being prepared for public visibility. |
| Uncertainty | Medium | CM architecture must stay useful without becoming compliance theater. |
| Dependency trust | Low | Tooling remains standard library plus pytest for tests. |
| AI authority | Medium | Repo teaches agent workflows and must bound authority clearly. |

## Selected mode

- Mode: Standard with activated CM records.
- Why this mode: Repo-wide public claims, package behavior, docs, templates, skills, commands, and baseline posture are controlled configuration.
- Why lighter mode is not enough: Quick mode would hide impact across public docs, tests, package entry point, catalog, and launch packets.
- Why heavier mode is not yet required: This remains a public educational workflow repo, not a regulated quality program.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `basis.md` | yes | Defines public promise and non-claims. | Maintainer |
| `plan.md` | yes | Bounds repo-wide update sequence. | Maintainer |
| `trace.md` | yes | Links launch claims to evidence. | Maintainer |
| `verification.md` | yes | Records tests, install check, validator, scans. | Maintainer |
| `ship.md` | yes | Controls public-readiness decision. | Maintainer |
| `controlled-items.md` | yes | Public thesis changes controlled repo state. | Maintainer |
| `change-impact.md` | yes | Many artifact families are affected. | Maintainer |
| `baseline.md` | yes | Records accepted public-ready baseline. | Maintainer |

## Immediate proof obligations

- Full pytest suite passes.
- Doctor and packet validations pass.
- Editable install and console entry point work.
- Public docs avoid compliance, certification, formal assurance, production-sandbox, or regulatory adequacy claims.
- Stale links to deleted internal scaffolding are removed.

## Required links

- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `controlled-items.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Mode and activated artifacts are justified.
- Public CM thesis is supported by docs, templates, skills, commands, and tests.
- Release posture remains bounded and non-compliance-claiming.

## Source-lineage note

Original Nuclear-grade packet inspired by public configuration-management, lifecycle, software assurance, secure development, release-readiness, and operating-learning sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
