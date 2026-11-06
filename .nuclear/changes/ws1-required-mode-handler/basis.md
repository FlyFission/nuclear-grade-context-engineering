# Basis: move the required-mode command into the engine module

## Change context

- Slug: ws1-required-mode-handler
- Related risk record: [`risk.md`](risk.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-04
- Decision this basis supports: whether the move keeps the command's behavior and closes the `gate-cli` coverage gap.

## Mission / need

`.nuclear/consequence-policy.json` protects `nuclear_grade/consequence.py` by path, but `nuclear_grade/cli.py` only through a content rule on gate identifiers. The `required-mode` handler, including the line that turns a failing verdict into exit 1, lived in `cli.py`. The hint it printed on failure always asked for a new change record, even when every path was covered and only an approval was missing.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The command's exit codes and receipts are unchanged | CI will rely on them | existing CLI tests in `tests/test_consequence.py` |
| Gate-deciding code sits under a path rule | an edit to it needs a record | delegate test |
| The hint names the actual fix | a wrong hint sends people to create needless records | hint test |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| Logic changes during the move | fault | gate behaves differently | the body is moved verbatim apart from the hint; existing exit-code and error tests run unchanged |
| Logic drifts back into `cli.py` | insufficiency | coverage gap returns | `test_the_cli_handler_only_delegates_to_the_engine` |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Nothing else calls `cli._default_base` | fact | repository search on this branch | a new caller | maintainer |
| #128 merges with `consequence.py` under `validators` | assumption | PR #128 | the rule changes | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Behavior is unchanged except the hint | local proof | existing CLI tests pass unmodified | safe to merge |

## Interfaces and trust boundaries

- Internal interfaces affected: `cli.handle_required_mode` now calls `consequence.run_cli`; `consequence.default_base` and `consequence.fix_hints` are new.
- External services/APIs affected: none.
- Data classes affected: none; the receipt schema is unchanged.
- Human approval boundaries: unchanged.
- AI/model/tool authority boundaries: unchanged.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE CLI handler SHALL contain only a call to `consequence.run_cli`. | protected outcome 2 | delegate | E-001 |
| REQ-002 | WHEN the verdict fails, THE SYSTEM SHALL print the record hint only if a path is uncovered, and the approval hint when a required approval is missing. | protected outcome 3 | `fix_hints` reads receipt fields, not messages | E-002 |
| REQ-003 | THE command's exit codes and receipt SHALL be unchanged. | protected outcome 1 | verbatim move | E-003 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` |
| Architecture — shape and major parts | yes | `consequence.run_cli` owns the command |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes | receipt schema v1, unchanged |
| Error handling — failure paths and responses | yes | unchanged: exit 2 on bad input |
| Testing strategy — how each claim is checked | yes | [`verification.md`](verification.md) |

## Required links

- Risk record: [`risk.md`](risk.md)
- Verification record: [`verification.md`](verification.md)
- Ship record: [`ship.md`](ship.md)

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- Every requirement has planned evidence in `verification.md`.

## Source-lineage note

Original Nuclear-grade basis; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
