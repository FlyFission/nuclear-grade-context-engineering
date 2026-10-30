# Plan: WS1 consequence engine

## Change context

- Slug: ws1-consequence-engine
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-10-30
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: yes; the non-goals held (no CI, policy file, or hook change).
- Charter articles in play: evidence before claims; the actor is not the only witness.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Copy the gate's glob matcher into the package with a parity test | REQ-006 | none | `hooks/pre_tool_use.py#_glob_regex` | `nuclear_grade/globmatch.py` | `tests/test_globmatch.py` | parity test passes |
| 2 | Policy parsing, diff reading, per-path classification | REQ-001, REQ-004 | step 1 | `challenge/score.py#changed_paths` | `nuclear_grade/consequence.py` | tests | classification tests pass |
| 3 | Coverage by new records and human approval | REQ-002, REQ-003 | step 2 | `challenge/score.py#find_record`, `ng_validate.validate_packet` | `_cover` | tests | approval and coverage tests pass |
| 4 | Claim detection; backtest and fix false positives | REQ-005 | step 2 | validator claim lists | `_claims_in`, `tools/ng_policy_backtest.py` | backtest plus regression tests | no known false positive left unexplained |
| 5 | CLI subcommand and reference entry | REQ-001..005 | steps 2-4 | `nuclear_grade/cli.py#build_parser` | `required-mode` | CLI tests | exit codes 0, 1, 2 verified |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `nuclear_grade/consequence.py` | new | REQ-001..005 | the engine | maintainer |
| `nuclear_grade/globmatch.py` | new | REQ-006 | shared globs | maintainer |
| `nuclear_grade/cli.py` | new subcommand | REQ-001..005 | entry point | maintainer |
| `tools/ng_policy_backtest.py` | new | REQ-005 | calibration before enforcement | maintainer |

## Non-goals

- No `.nuclear/consequence-policy.json` for this repository (next change, `standard+authority` by its own rule).
- No CI job and no hook change.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..006 reviewed by the maintainer | planned |
| Tests/evals defined | each requirement maps to evidence | pass |
| Build complete | affected files match the plan | pass |
| Verification complete | evidence linked in `verification.md` | pass |
| Release decision ready | residual risks recorded in `ship.md` | pass |

## Rollback approach

- Rollback method: revert the commit; nothing else depends on it yet.
- State/data reversal notes: none; the engine writes nothing.
- Feature flag / kill switch: not wired into CI.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q tests/test_consequence.py tests/test_globmatch.py
python -m pytest -q && python -m ruff check . && python tools/ng.py doctor . && python tools/ng.py tokens .
python tools/ng.py required-mode --base main
python tools/ng_policy_backtest.py --policy <candidate-policy.json> --last 49
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade plan; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
