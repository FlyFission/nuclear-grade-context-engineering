# Plan: WS1 repository consequence policy

## Change context

- Slug: ws1-repo-policy
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-03
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: yes; no CI, hook, or engine change was made.
- Charter articles in play: evidence before claims; accountability stays with people.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Start from the draft policy used for the #123 backtest; add `tests/test_hooks.py` to trust tests and a `gate-cli` content rule | REQ-001..005 | #123 merged | draft policy; master plan WS1 decisions | `.nuclear/consequence-policy.json` | parses; renders with `--print-table` | 12 rules |
| 2 | Check every path pattern against tracked files | REQ-001 | step 1 | `git ls-files` | list of non-matching patterns | each non-match explained | done |
| 3 | Pin representative paths to decided modes | REQ-001..004 | step 1 | owner decisions | `tests/test_repo_policy.py` | 35 tests pass | done |
| 4 | Backtest over the last 49 merged commits; list commits whose own record fell short | all | step 1 | `tools/ng_policy_backtest.py` | counts and list in `verification.md` | reproducible command | done |
| 5 | Correct the engine record's stale backtest row, with a note | none | step 4 | `.nuclear/changes/ws1-consequence-engine/verification.md` | corrected row | re-run matches | done |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `.nuclear/consequence-policy.json` | new | REQ-001..005 | gate policy | maintainer |
| `tests/test_repo_policy.py` | new | REQ-001..004 | pins the mapping | maintainer |
| `docs/05-reference/cli-reference.md` | one sentence | none | discoverability | maintainer |
| `.nuclear/changes/ws1-consequence-engine/verification.md` | correction | none | record accuracy | maintainer |

## Non-goals

- No CI job; no change to the engine, hooks, or validator.
- No owner-labelled tuning; that needs the owner's labels.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | maintainer confirms the rule set reflects the six decisions | planned |
| Tests/evals defined | each requirement maps to evidence | pass |
| Build complete | affected files match the plan | pass |
| Verification complete | evidence linked in `verification.md` | pass |
| Release decision ready | residual risks recorded in `ship.md` | pass |

## Rollback approach

- Rollback method: revert the commit. The engine then falls back to its built-in policy.
- State/data reversal notes: none.
- Feature flag / kill switch: CI does not read the file yet.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q tests/test_repo_policy.py
python tools/ng.py required-mode --policy-ref WORKTREE --print-table
python tools/ng_policy_backtest.py --policy .nuclear/consequence-policy.json --last 49   # from a checkout of 31e0a9e
python tools/ng.py validate .nuclear/changes/ws1-repo-policy --strict-authority
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md), [`decision-authority.md`](decision-authority.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade plan; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
