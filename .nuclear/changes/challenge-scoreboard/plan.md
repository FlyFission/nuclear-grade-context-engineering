# Plan: a scoreboard page, a badge and a run-everything script for the challenge

## Change context

- Slug: challenge-scoreboard
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-18
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: yes; outcome logic is untouched.
- Charter articles in play: evidence before claims.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Pair rows and count silent widenings | REQ-001, REQ-002 | none | `challenge-results/build.py#summarize` | `scoreboard_pairs`, `silent_widenings` | tests | pass |
| 2 | Render the page and badge | REQ-002, REQ-003 | step 1 | the rows | `render_scoreboard`, `render_badge` | tests | pass |
| 3 | Run every installed agent on both tracks | REQ-004 | none | `challenge-results/run.py#TRACKS` | `run-all.py` | test and `--dry-run` | pass |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `challenge-results/build.py` | renderers and flags | REQ-001..003 | results tooling | maintainer |
| `challenge-results/run-all.py` | new | REQ-004 | round orchestration | maintainer |
| `tests/test_challenge_results.py` | five tests | REQ-001..004 | evidence | maintainer |

## Non-goals

- No change to outcomes, rulings, `run.py`, the scorer, or `METHOD.md`.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | maintainer review | planned |
| Tests/evals defined | each requirement maps to evidence | pass |
| Build complete | affected files match the plan | pass |
| Verification complete | evidence linked in `verification.md` | pass |
| Release decision ready | residual risks recorded in `ship.md` | pass |

## Rollback approach

- Rollback method: revert the commit.
- State/data reversal notes: delete the two generated files.
- Feature flag / kill switch: nothing links the page or badge yet.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q tests/test_challenge_results.py
python challenge-results/run-all.py --dry-run --trials 1
python -m pytest -q && python -m ruff check . && python tools/ng.py doctor . && python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/challenge-scoreboard
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade plan; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
