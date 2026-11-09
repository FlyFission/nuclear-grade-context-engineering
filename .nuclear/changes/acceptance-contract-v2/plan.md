# Plan: typed acceptance contract and adversarial fixtures

## Change context

- Slug: acceptance-contract-v2
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: yes; no hook, CI, or `validate_packet` change was made.
- Charter articles in play: evidence before claims; honest reporting; accountability stays with people.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Measure the propagation rule over every existing record before using it | REQ-006 | none | 82 records | counts in E-003 | reproducible script | done |
| 2 | Add `build_acceptance`, `read_acceptance`, schema version 2 | REQ-001, REQ-002, REQ-004 | step 1 | `receipt.py` | acceptance block | fixtures | done |
| 3 | Add `verify_receipt` and recompute the block | REQ-003 | step 2 | `receipt.py` | bound/stale/invalid | fixtures | done |
| 4 | Wire flags and the Acceptance line into CLI and MCP | REQ-005 | steps 2, 3 | `cli.py`, `mcp_server.py` | three flags, one line | consumer fixtures | done |
| 5 | Write the fixture suite by property | all | steps 2, 3 | `tests/test_acceptance_adversarial.py` | 32 tests | suite passes | done |
| 6 | Weaken each control and rerun | REQ-003, REQ-004 | step 5 | scratch script | 7 of 7 caught | E-002 | done |
| 7 | Fix the policy-test findings: `propagation.py` and two suites into the policy | none | step 2 | `.nuclear/consequence-policy.json` | policy edit | `tests/test_repo_policy.py` | done |
| 8 | Docs, changelog, badge | none | steps 2-4 | docs | text | public-doc tests | done |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `nuclear_grade/receipt.py` | edit | REQ-001..004 | the receipt contract | maintainer |
| `nuclear_grade/propagation.py` | edit | REQ-006 | advisory input | maintainer |
| `nuclear_grade/cli.py` | edit | REQ-005 | flags and output | maintainer |
| `nuclear_grade/mcp_server.py` | edit | REQ-005 | client output | maintainer |
| `.nuclear/consequence-policy.json` | edit | none | policy consistency tests | maintainer |
| `tests/test_acceptance_adversarial.py` | new | all | the attack | maintainer |
| docs, `CHANGELOG.md`, `.nuclear/badge.json` | edit | none | discoverability | maintainer |

## Non-goals

- No change to `validate_packet`, hooks, CI, or default exit codes.
- No dependency model, scope interlock, attestations, decision custody, or published challenge results.
- No default flip of `--strict-custody`, `--strict-authority`, or `--two-party`.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | maintainer confirms the eligibility split | planned |
| Tests/evals defined | each requirement maps to evidence | pass |
| Build complete | affected files match the plan | pass |
| Verification complete | evidence linked in `verification.md` | pass |
| Release decision ready | residual risks recorded in `ship.md` | pass |

## Rollback approach

- Rollback method: revert the commit. Receipts return to schema version 1; stored version 2 receipts then read as unknown to old readers, which ignore the extra key.
- State/data reversal notes: none.
- Feature flag / kill switch: none needed; additions are inert unless a client reads `acceptance`.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python -m nuclear_grade.release
python tools/ng.py validate .nuclear/changes/acceptance-contract-v2 --strict-authority
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md), [`decision-authority.md`](decision-authority.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade plan; lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
