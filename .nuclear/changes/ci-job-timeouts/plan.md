# Plan: CI job timeouts

## Change context

- Slug: ci-job-timeouts
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-06
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: yes; no step, trigger, permission or pin changed.
- Charter articles in play: evidence before claims; accountability stays with people.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Read recent job durations | REQ-001 | none | GitHub Actions run 42293941938 | cap sizing | E-002 | done |
| 2 | Add `timeout-minutes` after `runs-on` in 9 jobs | REQ-001 | step 1 | `.github/workflows/*.yml` | 9 added lines | E-001 | done |
| 3 | Add the key and a comment to the scaffold workflow text | REQ-002 | none | `nuclear_grade/cli.py` | 2 added lines | E-001 | done |
| 4 | Write the test and watch it fail on the old files | REQ-003 | steps 2-3 | `tests/test_workflow_timeouts.py` | 3 failures before, 16 passes after | E-001 | done |
| 5 | Independent review of the diff | all | step 4 | the diff and sources | review findings | E-003 | done |
| 6 | Act on the review: reword the test docstring, add the changelog entry, record the release run time | all | step 5 | review report | `CHANGELOG.md`, this record | E-003 | done |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `.github/workflows/ci.yml` | 4 added lines | REQ-001 | required gate | maintainer |
| `.github/workflows/release.yml` | 5 added lines | REQ-001 | publishing path | maintainer |
| `nuclear_grade/cli.py` | 2 added lines | REQ-002 | shipped output | maintainer |
| `tests/test_workflow_timeouts.py` | new | REQ-001..003 | regression guard | maintainer |
| `CHANGELOG.md` | `[Unreleased]` entry | REQ-002 | user-visible scaffold change | maintainer |

## Non-goals

- No change to steps, triggers, permissions or action pins; no path filtering; no policy change.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | maintainer confirms the caps | planned |
| Tests/evals defined | each requirement maps to evidence | pass |
| Build complete | affected files match the plan | pass |
| Verification complete | evidence linked in `verification.md` | pass |
| Release decision ready | residual risks recorded in `ship.md` | pass |

## Rollback approach

- Rollback method: revert the commit.
- State/data reversal notes: none.
- Feature flag / kill switch: none needed.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q tests/test_workflow_timeouts.py
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/ci-job-timeouts --strict-authority
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md), [`decision-authority.md`](decision-authority.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
