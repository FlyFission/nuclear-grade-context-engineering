# Basis: WS1 repository consequence policy

## Change context

- Slug: ws1-repo-policy
- Related risk record: [`risk.md`](risk.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-03
- Decision this basis supports: whether this policy is the right rule set for CI to read, in advisory mode first, in this repository.

## Mission / need

The engine merged in #123 has only a built-in policy covering CI and the gate files. The owner decisions recorded in the master plan (WS1) set the rest: ordinary code needs tests only; claim-bearing wording needs Quick and efficacy or assurance wording needs Standard; gate files need Standard plus a human merge; Dependabot pin bumps take a lane with a human review.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Trust surfaces need a record: CI, the gate, validators, trust-guarding tests, mode-owning skills, dependencies, model IDs in code | the gate's purpose | REQ-001 test |
| Ordinary work stays at the floor | measured cost of always-on rigor | REQ-002 test; backtest counts |
| Wording carries only the mode the owner set | owner decision 2 | REQ-003 test |
| CI and gate rules cannot be overridden | owner decision 3 | REQ-004 test |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A glob typo leaves a trust surface at the floor | fault | silent gap | every pattern checked against tracked files; representative-path test |
| The policy floods ordinary commits with requirements | insufficiency | cost without benefit; people route around it | backtest on 49 commits; advisory before enforcing |
| A CLI edit weakens the gate without a record | fault | gate weakened | `gate-cli` content rule on gate-wiring identifiers (partial; see `ship.md`) |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| CI will read the policy from the base commit | assumption | engine default `--policy-ref base` | a CI job that reads the candidate's policy | maintainer |
| Agents will act under a separate bot identity listed in `bot_identities` | assumption | owner decision 4 | the list stays empty after the bot account exists | maintainer |
| The owner decisions in the master plan are current | assumption | recorded in this session's plan | the owner revises a decision | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Each owner decision maps to a rule | local proof | `tests/test_repo_policy.py` | correctness of the mapping |
| The policy would have failed 13 of 49 merged commits | local proof | backtest in `verification.md` | the enforcement decision |
| Those 13 are real misses rather than over-classification | unknown | needs owner labels | tuning before enforcement |

## Interfaces and trust boundaries

- Internal interfaces affected: none at runtime; the file is read only by `ng required-mode` and `tools/ng_policy_backtest.py`.
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: `ci` and `gate` rules are `standard+authority` and not overridable; the policy file itself is `standard+authority` by the engine's built-in rule.
- AI/model/tool authority boundaries: the agent drafted the policy; the maintainer decides whether it merges.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE POLICY SHALL require at least Standard for validators, trust-guarding tests, mode-owning skills, dependency and release files, and model IDs in executable code, and `standard+authority` for `.github/**`, `hooks/**`, `.claude/**`, the gate policy and the charter. | protected outcome 1 | rules `validators`, `trust-tests`, `mode-owners`, `deps-release`, `model-id`, `ci`, `gate` | E-001 |
| REQ-002 | THE POLICY SHALL leave ordinary code, ordinary tests, prose edits and generated command cards at `none`. | owner decision 1 | `default: none`; no rule names them | E-001 |
| REQ-003 | THE POLICY SHALL require Quick for net-new general claims and always-loaded agent instructions, and Standard for net-new assurance or efficacy claims. | owner decision 2 | rules `claims`, `agent-instructions`, `assurance-claims`, `efficacy-claims` | E-001 |
| REQ-004 | THE POLICY SHALL mark `ci` and `gate` not overridable. | owner decision 3 | `overridable: false` | E-001 |
| REQ-005 | THE POLICY SHALL route `dependabot[bot]` pin bumps on workflows and `pyproject.toml` to the dependency lane. | owner decision 6 | `dependency_lane` | E-002 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` |
| Architecture — shape and major parts | yes | one JSON file read from the base by the engine |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes | policy schema v1 (`nuclear_grade/consequence.py#parse_policy`) |
| Error handling — failure paths and responses | yes | malformed policy exits 2 (engine) |
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
