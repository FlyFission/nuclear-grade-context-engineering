# Risk: typed acceptance contract and adversarial fixtures

## Change identity

- Slug: acceptance-contract-v2
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Summary: replace the receipt's single structural `ok` as the only machine-readable verdict with a typed `acceptance` block (receipt schema version 2). Add `verify_receipt` (`bound`, `stale`, `invalid`), `--verify-receipt`, `--expect-commit`, and `--require-eligible`. Surface the same acceptance line in `ng validate` text output and the MCP tool. Read the evidence-trust propagation rule as an advisory input. Add `tests/test_acceptance_adversarial.py`. Add `propagation.py` and the two test suites to the consequence policy, because the policy's own tests require it.

## Mission anchor

- **Objective:** make it hard to read a structurally valid record as permission to ship, and test that claim by attacking the acceptance path.
- **Success criterion:** each attack in the fixture suite produces its own named result; each fixture fails when its control is weakened; the 82 earlier records still validate; default exit codes are unchanged.
- **Non-goals:** no change to what makes a record structurally valid; propagation is not added to `validate_packet`; no scope interlock or hook change; no signed attestations; no decision custody; no published challenge results; no dependency model; no default flip of any strict flag.

## Questioning-attitude summary

- The fact that would change the decision: whether a reader still takes `OK` as approval. The acceptance line sits directly under `OK`, but a reader who ignores it is not stopped. Only `--require-eligible` changes an exit code, and it is opt-in.
- The fact still unknown: whether `blocked` and `undetermined` are the right split on records in the wild. 6 of 82 existing records are `undetermined` because their claim tables have no claim-id rows, which may be a format problem and not an evidence problem.
- Direction check: the propagation rule treats evidence-id rows as claims. It was measured, not trusted, which is why it stays advisory.

## Affected configuration items

| Item | Change |
|---|---|
| `nuclear_grade/receipt.py` | acceptance block, `verify_receipt`, `read_acceptance`, schema version 2 |
| `nuclear_grade/propagation.py` | suffix-letter claim ids; public `claim_id`; docstring states advisory status |
| `nuclear_grade/cli.py` | `--require-eligible`, `--verify-receipt`, `--expect-commit`; `Acceptance:` line in text output |
| `nuclear_grade/mcp_server.py` | `validate_change_record` appends the `Acceptance:` line |
| `.nuclear/consequence-policy.json` | policy edit: `propagation.py` joins `validators`; two suites join `trust-tests` |
| `tests/test_acceptance_adversarial.py` | new, 32 tests including 2 strict expected failures |
| `docs/05-reference/cli-reference.md`, `docs/02-operating-system/validators.md`, `CHANGELOG.md` | document the contract |
| `.nuclear/badge.json` | regenerated |

## Threshold screen

| Dimension | Rating | Why |
|---|---|---|
| Consequence | high | the receipt is the artifact CI and reviewers read as the validator's verdict |
| Reversibility | high | additive fields and flags; revert the commit; default exit codes unchanged |
| Detectability | high | deterministic; 32 fixtures; mutation-checked |
| Trust boundary | yes | validator, receipt, and the consequence policy itself |
| Uncertainty | medium | the eligibility split has no owner-labelled ground truth |

## HPI work-mode screen

- Work mode: knowledge-based; the semantics of "eligible" were chosen, not looked up.
- Error-likely situation: a fixture that passes because it tests nothing. Control: each control was weakened on purpose and the suite was rerun (see `verification.md`, E-002).

## Selected mode

- **Mode:** Standard
- **Strict authority:** yes. The change edits `.nuclear/consequence-policy.json`, which the engine's policy-self rule puts at `standard+authority`, so this record carries `decision-authority.md` and validates with `--strict-authority`.
- **Why this mode:** the change edits the validator, the receipt, the MCP tool, and the gate policy. The consequence policy requires Standard for the first three and `standard+authority` for the last. A Quick record was considered and rejected on that basis.

## Activated artifacts

- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Decision-authority record: `decision-authority.md`.
- Not activated: CM baseline (no release).

## Immediate evidence obligations

- Full suite, ruff, doctor, token budget, release check, and `validate --strict-authority` on this record pass.
- Each fixture class fails when its control is weakened.
- The classification of every earlier record is recorded.

## Scope

- Paths covered by this record: `nuclear_grade/receipt.py`, `nuclear_grade/propagation.py`, `nuclear_grade/cli.py`, `nuclear_grade/mcp_server.py`, `.nuclear/consequence-policy.json`, `tests/test_acceptance_adversarial.py`, `docs/05-reference/cli-reference.md`, `docs/02-operating-system/validators.md`, `CHANGELOG.md`, `.nuclear/badge.json`.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Decision authority: [`decision-authority.md`](decision-authority.md)
- Ship: [`ship.md`](ship.md)
- Source doctrine: [`activation-thresholds.md`](../../../docs/02-operating-system/activation-thresholds.md)

## Exit criteria

- The mode is justified and every path this change touches is named above.
- Evidence obligations are met or carried into `ship.md` as gaps.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
