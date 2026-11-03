# Basis: WS1 consequence engine

## Change context

- Slug: ws1-consequence-engine
- Related risk record: [`risk.md`](risk.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-10-30
- Decision this basis supports: whether the engine is correct and conservative enough to become the input to a CI gate in a later change.

## Mission / need

Mode selection is self-declared today: no code maps a diff to a required mode, and CI validates only the records a PR already has. A 352-run study on this repository found that always-loaded prose raised cost without changing outcomes, while instructions were followed. The engine moves the grading decision into a deterministic check.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Trust-surface changes cannot pass without a new, valid record of high enough mode | the gate's whole purpose | REQ-002 tests |
| A change cannot approve itself | the agent must not be the only witness | REQ-003 tests |
| A change cannot loosen the policy that judges it | policy read from base; policy edits need the top mode | REQ-004 tests |
| Ordinary work stays cheap | measured cost of always-on rigor | floor tests; backtest counts |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| An old record is touched to "cover" new work | fault | gate bypassed | only records added in the diff count; test |
| Self-approval, bot approval, or a stale approval counts | fault | human gate bypassed | author, bot identities, and `[bot]` logins excluded; latest review state wins; tests |
| Negated or quoted wording is read as a claim | insufficiency | needless records on docs PRs | sentence, lead-in, quote, and emphasis handling; regression tests from real false positives |
| A malformed policy silently passes everything | fault | gate disabled | parse errors exit 2 (fail closed); tests |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| The head is checked out in the repository being evaluated | assumption | CLI refuses a head that is not checked out | a CI layout that evaluates a different tree | maintainer |
| CI supplies reviews from the GitHub API | assumption | later WS1 change | reviews supplied from an agent-writable source | maintainer |
| Agents act under a separate bot identity | assumption | owner decision 4 | agents push as the owner's account | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Diff classification matches the policy | local proof | `tests/test_consequence.py` | gate correctness |
| Claim detection is not noisy on this repo's history | local proof (partial) | backtest in `verification.md` | policy tuning in the next change |

## Interfaces and trust boundaries

- Internal interfaces affected: new `required-mode` subcommand; reuses `validate_packet`, the validator's claim lists, and `has_closure_note`.
- External services/APIs affected: none directly; it reads review JSON that CI will fetch.
- Data classes affected: none.
- Human approval boundaries: `standard+authority`, overrides, and the dependency lane require an APPROVED review from a non-author, non-bot account.
- AI/model/tool authority boundaries: the engine executes no candidate code; it reads git and files.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN a diff changes a path, THE SYSTEM SHALL require the highest mode among the policy rules that match it, and the policy default otherwise. | graded approach | `classify`, `_rule_fires`, `_max_mode` | E-001 |
| REQ-002 | THE SYSTEM SHALL count a requirement as covered only by a record added in the diff that is open, declares a high enough mode, names the path in `risk.md`, and passes validation with that mode's flags. | protected outcome 1 | `_cover`, `_names_path`, `validate_packet` | E-002 |
| REQ-003 | IF the required mode is `standard+authority`, an override is used, or the dependency lane applies, THEN THE SYSTEM SHALL fail unless an APPROVED review exists from an account other than the PR author and bot identities. | protected outcome 2 | `_human_approvers` | E-003 |
| REQ-004 | THE SYSTEM SHALL read the policy from the base by default, require `standard+authority` for any policy change, and exit 2 on a malformed policy. | protected outcome 3 | `load_policy`, `_evaluate_policy_self`, `parse_policy` | E-004 |
| REQ-005 | THE SYSTEM SHALL count claim rules only on net-new claim wording that is not negated, quoted, or under a negated lead-in. | protected outcome 4 | `_claims_in`, `net_new_claims` | E-005 |
| REQ-006 | THE SYSTEM SHALL match globs exactly as the PreToolUse gate does. | consistency | `globmatch.glob_regex` | E-006 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | module docstring in `nuclear_grade/consequence.py` |
| Architecture — shape and major parts | yes | `classify` (per-path requirement) then `_cover` (records and approvals) |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes | `Policy`, `Rule`, `Diff`, receipt schema v1 |
| Error handling — failure paths and responses | yes | `PolicyError` and `GitError` exit 2 |
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

Original Nuclear-grade basis; graded-rigor and independence lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
