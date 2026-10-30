# Risk: WS1 consequence engine (`ng required-mode`)

## Change identity

- Slug: ws1-consequence-engine
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-10-30
- Summary: add a deterministic engine that reads a git diff and a consequence policy, reports the minimum change-record mode each changed path requires, and checks whether a new record and (where required) a human approval cover it. Adds `nuclear_grade/consequence.py`, `nuclear_grade/globmatch.py`, the `ng required-mode` command, `tools/ng_policy_backtest.py`, tests, and a CLI reference entry. Nothing is wired into CI in this change.

## Mission anchor

- **Objective:** make the graded approach executable, so the mode a change needs comes from what it touches rather than from the agent's own declaration.
- **Success criterion:** `ng required-mode` classifies diffs, rejects uncovered or self-approved trust-surface changes in tests, and a backtest over the last 49 merged commits runs with a candidate policy.
- **Non-goals:** no policy file for this repository yet, no CI job, no hook change, no change to the validator's rules. Those are later WS1 changes, each with its own record.

## Questioning-attitude summary

- The one fact that would change the decision: if the claim detectors flooded ordinary docs with requirements, the gate would recreate the always-on cost the 352-run study measured. The backtest was run for that reason and three false-positive patterns were fixed (see `verification.md`).
- Assumption: CI will later supply PR reviews from the GitHub API and run the engine from the base commit, outside the candidate tree.

## Affected configuration items

| Item | Change |
|---|---|
| `nuclear_grade/consequence.py` | new checker module |
| `nuclear_grade/globmatch.py` | new; copy of the gate's glob matcher, pinned by a parity test |
| `nuclear_grade/cli.py` | new `required-mode` subcommand |
| `tools/ng_policy_backtest.py` | new read-only backtest tool |
| `tests/test_consequence.py`, `tests/test_globmatch.py` | new tests |
| `docs/05-reference/cli-reference.md` | command reference entry |

## Threshold screen

| Dimension | Rating | Why |
|---|---|---|
| Consequence | medium | a future gate will rely on this classification |
| Reversibility | high | not wired into CI; revert the commit |
| Detectability | high | deterministic, covered by 63 tests and a backtest |
| Trust boundary | yes | it is a checker; its output will decide merges later |
| Uncertainty | medium | claim detection is heuristic; tuned against 49 real commits |

## HPI work-mode screen

- Work mode: rule-based build against a written plan (`MASTER_PLAN` WS1), with known failure modes from two independent reviews.
- Error-likely situation: heuristic claim matching. Control: negation, quote, and lead-in handling plus regression tests drawn from real false positives.

## Selected mode

- **Mode:** Standard
- **Why this mode:** checker code whose output a later CI gate will use to decide merges; a trust-bearing component, though not yet wired in.

## Activated artifacts

- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Not activated: CM baseline (no release), decision-authority record (no gate or CI change in this diff).

## Immediate evidence obligations

- Tests for each requirement in `basis.md` (`tests/test_consequence.py`, `tests/test_globmatch.py`).
- The full repository suite, ruff, doctor, and token budgets pass.
- A backtest over merged history with a candidate policy, with false positives inspected.

## Scope

- Paths covered by this record: `nuclear_grade/consequence.py`, `nuclear_grade/globmatch.py`, `nuclear_grade/cli.py`, `tools/ng_policy_backtest.py`, `tests/test_consequence.py`, `tests/test_globmatch.py`, `docs/05-reference/cli-reference.md`.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship: [`ship.md`](ship.md)
- Source doctrine: [`activation-thresholds.md`](../../../docs/02-operating-system/activation-thresholds.md)

## Exit criteria

- The mode is justified and every path this change touches is named above.
- Evidence obligations are met or carried into `ship.md` as gaps.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
