# Plan: round isolation: one container per run, results out of agents' reach

## Change context

- Slug: round-isolation
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-20
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: yes; outcomes and scorer untouched.
- Charter articles in play: evidence before claims.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | One container per trial, results hidden, copied out after | REQ-001, REQ-006 | none | `challenge-results/container/round.sh` | new loop; `run.py --first-trial` | tests and container run | pass |
| 2 | Read sign-ins as data, per agent, out of argv | REQ-002 | none | `round.sh` | `env_value`, private env files | parser test and container run | pass |
| 3 | Fresh home per run | REQ-003 | step 1 | `round.sh` | `/seed:ro` copy | container run | pass |
| 4 | Report harness failures | REQ-004 | none | `run-all.py` | exit codes | test | pass |
| 5 | Name files for judge runs | REQ-005 | none | `build.py#silent_replays` | fallback | test | pass |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `challenge-results/container/round.sh` | rewritten loop | REQ-001..003 | round isolation | maintainer |
| `challenge-results/run.py` | `--first-trial` | REQ-006 | trial numbers | maintainer |
| `challenge-results/run-all.py` | exit codes | REQ-004 | honest rounds | maintainer |
| `challenge-results/build.py` | fallback | REQ-005 | page content | maintainer |
| `tests/test_challenge_results.py` | tests | REQ-001..006 | evidence | maintainer |

## Non-goals

- No change to outcomes, rulings, the scorer, or the challenge.

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
- State/data reversal notes: none; no round has run.
- Feature flag / kill switch: none needed.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q tests/test_challenge_results.py
python -m pytest -q && python -m ruff check . && python tools/ng.py doctor . && python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/round-isolation
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade plan; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
