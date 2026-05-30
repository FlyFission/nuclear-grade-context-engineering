# Plan - CM Public Readiness

**Purpose:** Bound the public-readiness pass so repo-wide CM (keeping the approved version under control) changes stay easy to review.

## Change context

- Slug: `cm-public-readiness`
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: Maintainer
- Date: 2026-05-23
- Current lifecycle phase: Verify

## Build sequence

1. Add packaging regression tests, watch them fail, then move CLI/validator into `nuclear_grade/`.
2. Rewrite public README/workflow/quickstart language around controlled configuration.
3. Add CM operating docs for controlled items, impact, baselines, variance, and re-baseline.
4. Add activated CM templates.
5. Add CM skills and portable command prompts.
6. Update catalog, tests, manifest, and tool docs.
7. Update public-readiness packet and baseline records.
8. Run full verification and fix blockers.

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| `README.md`, `WORKFLOWS.md`, `QUICKSTART.md` | Public CM positioning. | First-run clarity. | Maintainer |
| `docs/02-operating-system/` | CM doctrine. | True configuration-management backbone. | Maintainer |
| `templates/cm/` | Activated CM records. | Concrete workflow artifacts. | Maintainer |
| `skills/`, `commands/` | Portable agent surface. | Skill-repo utility and adoption. | Maintainer |
| `nuclear_grade/`, `tools/`, `pyproject.toml` | Namespaced package entry point. | Install path reliability. | Maintainer |
| Tests and manifest | Contract updates. | Prevent silent drift. | Maintainer |

## Non-goals

- Do not claim compliance, certification, regulated verification adequacy, safety, security, or regulatory adequacy.
- Do not implement full Nuclear/Incident/Release validators in this pass.
- Do not require all CM records for every Standard change.
- Do not create marketplace packaging in this pass.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| Package entry point | `nuclear_grade.cli:main` | `tools.ng:main` | Avoids top-level `tools` collision. | Packaging metadata changes. |
| CM scope | Activated records under `templates/cm/` | Add all records to Standard by default. | Preserves proportional rigor. | User confusion or validator expansion. |
| Public hook | Configuration management for AI-assisted software work. | Generic senior-agent workflow copy. | Differentiates from viral skills repos. | Public feedback shows confusion. |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Packaging red test observed | Packaging contract test fails before implementation. | pass |
| Packaging green | Focused tests pass. | pass |
| CM artifacts added | Docs/templates/skills/commands exist and are indexed. | pass |
| Public docs aligned | README/workflows/quickstart use CM thesis and boundary language. | pass |
| Verification complete | Tests, doctor, packet validation, install, compile, scans. | pass |

## Rollback approach

- Revert this packet and CM public-readiness changes before public launch if verification fails.
- Keep existing Quick/Standard packet path intact if CM docs need another pass.

## Proof commands

```bash
python -m pytest -q
python -m py_compile nuclear_grade/cli.py nuclear_grade/ng_validate.py tools/ng.py tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/reference/workspace_guard.py
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/cm-public-readiness
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
python -m pip install -e .
nuclear-grade doctor .
git diff --check
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `controlled-items.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Work is bounded enough to review.
- Verification commands pass or blockers are recorded.
- Public claims match implemented artifacts.

## Source-lineage note

Original Nuclear-grade plan inspired by public lifecycle, configuration-management, release-readiness, and verification concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
