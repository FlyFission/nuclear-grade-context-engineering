# Risk: WS1 repository consequence policy

## Change identity

- Slug: ws1-repo-policy
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-03
- Summary: add `.nuclear/consequence-policy.json`, the policy `ng required-mode` reads to decide the minimum change-record mode each changed path in this repository needs. Adds `tests/test_repo_policy.py` to pin representative paths to the modes the owner decided, one line in the CLI reference, and a disclosed correction to the backtest figures in the `ws1-consequence-engine` record. Nothing is wired into CI.

## Mission anchor

- **Objective:** give the engine merged in #123 this repository's real rules, so that the advisory CI job (next change) has a policy to read from the base.
- **Success criterion:** the policy parses; each owner decision maps to a rule; representative changes get the decided mode in a test; a backtest over the last 49 merged commits is recorded with the commits it would have failed.
- **Non-goals:** no CI job, no enforcement, no hook change, no bot identity. The policy does not change any behavior until a later change makes CI read it.

## Questioning-attitude summary

- The fact that would change the decision: if the policy asked for records on most ordinary commits, it would recreate the always-on cost that the 352-run study measured. The backtest says 21 of 49 commits need nothing and 10 need Quick only.
- The fact still unknown: whether the 13 commits the policy would have failed are real misses or over-classification. Owner labels on about 20 commits decide that before enforcement.

## Affected configuration items

| Item | Change |
|---|---|
| `.nuclear/consequence-policy.json` | new; this repository's consequence policy (12 rules) |
| `tests/test_repo_policy.py` | new; pins representative paths to their decided modes |
| `docs/05-reference/cli-reference.md` | one sentence naming the policy file |
| `.nuclear/changes/ws1-consequence-engine/verification.md` | backtest row corrected, with a correction note (an existing record; edit disclosed) |

## Threshold screen

| Dimension | Rating | Why |
|---|---|---|
| Consequence | high | once CI reads it, this file decides which changes need records and human approval |
| Reversibility | high | not read by CI yet; revert the commit |
| Detectability | high | deterministic; pinned by a test; backtest on real history |
| Trust boundary | yes | it is gate policy |
| Uncertainty | medium | the mapping reflects owner decisions, but not yet owner-labelled ground truth |

## HPI work-mode screen

- Work mode: rule-based, translating six recorded owner decisions into rules.
- Error-likely situation: a glob that silently matches nothing. Control: every pattern was checked against `git ls-files`; the three that match nothing today are deliberate (see `verification.md`).

## Selected mode

- **Mode:** Standard
- **Strict authority:** yes. The engine's built-in policy-self rule requires `standard+authority` for any change to the policy, so this record carries `decision-authority.md` and validates with `--strict-authority`.
- **Why this mode:** gate policy for this repository. The policy cannot be reviewed by the gate it defines, so the maintainer's review and merge is the approval.

## Activated artifacts

- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Decision-authority record: `decision-authority.md` (strict authority).
- Not activated: CM baseline (no release).

## Immediate evidence obligations

- `tests/test_repo_policy.py` passes.
- The full suite, ruff, doctor, token budgets, and `validate --strict-authority` on this record pass.
- A backtest over the last 49 merged commits with this exact policy file.

## Scope

- Paths covered by this record: `.nuclear/consequence-policy.json`, `tests/test_repo_policy.py`, `docs/05-reference/cli-reference.md`, `.nuclear/changes/ws1-consequence-engine/verification.md`.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Decision authority: [`decision-authority.md`](decision-authority.md)
- Ship: [`ship.md`](ship.md)
- Engine record: [`../ws1-consequence-engine/risk.md`](../ws1-consequence-engine/risk.md)
- Source doctrine: [`activation-thresholds.md`](../../../docs/02-operating-system/activation-thresholds.md)

## Exit criteria

- The mode is justified and every path this change touches is named above.
- Evidence obligations are met or carried into `ship.md` as gaps.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
