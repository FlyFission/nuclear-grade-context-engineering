# Plan: move the required-mode command into the engine module

## Change context

- Slug: ws1-required-mode-handler
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-04
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: yes; no logic outside the hint changed.
- Charter articles in play: evidence before claims.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Move `handle_required_mode` and `_default_base` into `consequence.py` as `run_cli` and `default_base` | REQ-001, REQ-003 | none | `nuclear_grade/cli.py#handle_required_mode` | delegate in `cli.py` | existing CLI tests | pass unchanged |
| 2 | Select hints from receipt fields | REQ-002 | step 1 | receipt `paths`, `approvals`, `overrides` | `fix_hints` | hint test | pass |
| 3 | Pin the delegate | REQ-001 | step 1 | `inspect.getsource` | delegate test | test | pass |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `nuclear_grade/consequence.py` | gains the command | REQ-001..003 | gate checker | maintainer |
| `nuclear_grade/cli.py` | delegate only | REQ-001 | entry point | maintainer |
| `tests/test_consequence.py` | two tests | REQ-001, REQ-002 | evidence | maintainer |

## Non-goals

- No logic, schema, exit-code or policy change.

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
- State/data reversal notes: none.
- Feature flag / kill switch: not wired into CI.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q tests/test_consequence.py
python -m pytest -q && python -m ruff check . && python tools/ng.py doctor . && python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/ws1-required-mode-handler --strict-custody
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade plan; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
