# Risk: move the required-mode command into the engine module

## Change identity

- Slug: ws1-required-mode-handler
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-04
- Summary: move the body of `ng required-mode` from `nuclear_grade/cli.py` into `nuclear_grade/consequence.py` (`run_cli`, `default_base`), leaving a one-line delegate in the CLI, and make the failure hint match the failure: a record hint only when a path is uncovered, an approval hint when only an approval is missing.

## Mission anchor

- **Objective:** close the residual gap recorded in `ws1-repo-policy`: the `gate-cli` content rule covers `cli.py` only partly, so an edit to the handler that names no gate identifier needed no record.
- **Success criterion:** every line that decides the command's exit code lives in `consequence.py`, which the policy's `validators` rule covers by path; a test pins the delegate; the hint is correct for uncovered and approval-only failures.
- **Non-goals:** no change to classification, coverage, approval logic, exit codes, the receipt schema, or the policy file.

## Questioning-attitude summary

- The fact that would change the decision: if any caller relied on `cli._default_base` or on the old hint text. A search found no other caller, and only the hint wording changes.

## Affected configuration items

| Item | Change |
|---|---|
| `nuclear_grade/consequence.py` | gains `run_cli`, `default_base`, `fix_hints` (moved and extended) |
| `nuclear_grade/cli.py` | `handle_required_mode` becomes a delegate; `_default_base` and the unused `subprocess` import removed |
| `tests/test_consequence.py` | two tests: hints match the failure; the CLI handler only delegates |

## Threshold screen

| Dimension | Rating | Why |
|---|---|---|
| Consequence | medium | the command a later CI gate will run |
| Reversibility | high | revert the commit; not wired into CI |
| Detectability | high | the existing CLI exit-code tests plus two new ones |
| Trust boundary | yes | gate checker code |
| Uncertainty | low | a move with no logic change, plus hint selection |

## Selected mode

- **Mode:** Standard
- **Why this mode:** it edits checker code (`validators`) and a trust-guarding test (`trust-tests`) under `.nuclear/consequence-policy.json` (#128).

## Activated artifacts

- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Not activated: decision-authority record (no gate, CI or policy change).

## Immediate evidence obligations

- The two new tests fail on the previous commit and pass after.
- The full suite, ruff, doctor, token budgets, and `validate --strict-custody` on this record pass.

## Scope

- Paths covered by this record: `nuclear_grade/consequence.py`, `nuclear_grade/cli.py`, `tests/test_consequence.py`.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship: [`ship.md`](ship.md)
- Residual gap this closes: the `gate-cli` entry in the `ws1-repo-policy` record's `ship.md` (PR #128)

## Exit criteria

- The mode is justified and every path this change touches is named above.
- Evidence obligations are met or carried into `ship.md` as gaps.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
