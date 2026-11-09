# Basis: typed acceptance contract and adversarial fixtures

## Change context

- Slug: acceptance-contract-v2
- Related risk record: [`risk.md`](risk.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Decision this basis supports: whether the receipt's acceptance block is the right contract for CI and reviewers to read, and whether the fixture suite is a fair attack on it.

## Mission / need

`ng validate --json` prints `"ok": true` for a record that still carries open evidence, and the demo shows exactly that. External review of the roadmap asked for a verdict that cannot be mistaken for approval, tested by attacking it. Reviewers also asked that "implemented" not be counted as "effective": a control needs a test that fails when the control is weakened.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| A structurally valid record is never read as approval | the original misreading | REQ-001, REQ-002 |
| A receipt for other bytes or another commit is recognized as such | evidence swaps and stale receipts | REQ-003 |
| A hand-edited receipt cannot raise its own eligibility | the acceptance block sits outside the digest | REQ-003 |
| Old receipts never read as eligible | compatibility without silent upgrade | REQ-004 |
| Every consumer shows the same result | no path collapses it back to one boolean | REQ-005 |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A fixture suite that cannot fail | insufficiency | false confidence | weaken each control and rerun (E-002) |
| Eligibility reads "approved" or "trusted" | fault | the original misreading, now with a stamp | state set is closed and tested; no such key exists |
| Making propagation a pass/fail gate before its model exists | fault | 21 of 56 Standard-style records fail for format, not for evidence | keep it advisory; measured in E-003 |
| Breaking existing CI by changing default exit codes | fault | pipelines fail for a presentation change | exit codes unchanged; `--require-eligible` opt-in |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| `blocked` for `fail`, `gap`, `planned`; open-to-decision for `deferred` | assumption | a deferral is a recorded human choice; the others are unfinished work | owner labels disagree | maintainer |
| Claim rows keyed by claim id are the unit of claim support | assumption | existing `verification.md` tables | a record format that keys rows another way | maintainer |
| Eligibility needs no policy file | assumption | the rule is structural | per-claim-class minimums land (ROADMAP item 4) | maintainer |
| The receipt is not a signature | fact | module docstring; unchanged | signed attestations land | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Each attack class yields its own named result | local proof | E-001 | the contract is attackable |
| Each fixture fails when its control is weakened | local proof | E-002, 7 of 7 caught | the fixtures test something |
| 17 of 82 earlier records are `blocked` and 6 `undetermined` | local proof | E-003 | the split is usable on real records |
| Those 23 are right to withhold eligibility | unknown | needs owner review | tuning the split |
| Approval replay and out-of-packet artifact swaps are detected | not claimed | expected failures in E-001 | ROADMAP item 7 |

## Interfaces and trust boundaries

- Internal interfaces affected: the receipt JSON (additive; version 2), `ng validate` text output (one added line), the MCP tool's return string (one added line).
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: the policy edit is `standard+authority`; the maintainer's review and merge is the approval.
- AI/model/tool authority boundaries: the agent drafted the contract and the fixtures. It does not decide that the semantics are right.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE RECEIPT SHALL report structure, evidence status, claim support, declared-independence checks, release eligibility, authorized decision, and apply permission as separate fields, with no overall boolean and no eligibility value that reads as approval. | protected outcome 1 | `build_acceptance` | E-001 |
| REQ-002 | RELEASE ELIGIBILITY SHALL be `blocked` for invalid structure, a `fail`, `gap`, or `planned` item, or a declared claim with no verification row; `undetermined` when claim rows cannot be read; otherwise open to a decision. | protected outcome 1 | `_release_eligibility` | E-001, E-003 |
| REQ-003 | `verify_receipt` SHALL report `bound`, `stale`, or `invalid`, covering changed, added, and removed files, another commit, an edited digest, and an edited acceptance block. | protected outcomes 2, 3 | `verify_receipt` | E-001, E-002 |
| REQ-004 | A version 1, hand-built, or malformed receipt SHALL NOT read as eligible. | protected outcome 4 | `read_acceptance` | E-001 |
| REQ-005 | THE CLI text, CLI JSON, exit codes, and MCP tool SHALL agree, and default exit codes SHALL keep their old meaning. | protected outcome 5 | `handle_validate`, `validate_change_record` | E-001 |
| REQ-006 | THE PROPAGATION RULE SHALL be advisory input only and SHALL NOT be called by `validate_packet`. | unacceptable outcome 3 | receipt reads it; validator does not | E-001, E-003 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` |
| Architecture — shape and major parts | yes | one new block in an existing receipt; one new function; three flags |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes | `build_acceptance` in `nuclear_grade/receipt.py` |
| Error handling — failure paths and responses | yes | unreadable receipt file reads `invalid`; exit 1 |
| Testing strategy — how each claim is checked | yes | [`verification.md`](verification.md) |

## Required links

- Risk record: [`risk.md`](risk.md)
- Verification record: [`verification.md`](verification.md)
- Ship record: [`ship.md`](ship.md)
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- Every requirement has planned evidence in `verification.md`.

## Source-lineage note

Original Nuclear-grade basis; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
