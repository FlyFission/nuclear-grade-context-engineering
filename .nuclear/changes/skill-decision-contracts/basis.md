# Basis -- skill decision contracts

**Purpose:** State what must stay true for the decision-contract change to be correct and reviewable.

---

## Change context

- Slug: skill-decision-contracts
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-06-16
- Decision this basis supports: whether to require and enforce a `## Decision contract` block on every skill.

## Mission / need

A reviewer cannot tell, without reading 27 prose skills, which ones could change an outcome. Charter Art. 11 already requires naming the decision the evidence must support; this change makes each skill declare it structurally.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Every skill names one decision it can change | removes the audit-the-audit prose problem | `ng decisions` lists 27 skills, each with a named decision |
| The token budget gate stays green | the block must not bloat the always-loaded cost | `ng tokens` passes; descriptions stay flat |
| Existing skill behavior is untouched | this is additive, not a rewrite | the full test suite passes |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Blocks become generic boilerplate | reintroduces the audit-the-audit problem | `ng decisions` surfaces generic rows; the redundancy gate fails copy-paste |
| A self-declared deletion of a skill | a guard inside the writable set the author can edit | only the `block`/`warn`/`observe` tier is declarable; the existence (delete) decision is measured |
| A skill body exceeds the token budget | CI regression | the `ng tokens` budget gate |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| The block fits the on-invocation body, not the description | fact | `ng tokens` shows descriptions flat at 2,814 | descriptions grow with the block | FlyFission |
| Six of seven prose-heavy skills already feed a decision | assumption | the per-skill audit | a skill cannot name a non-generic decision | FlyFission |

## Grounding status

Keep confidence apart from evidence before any derived claim is accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| All 27 skills carry a valid block | local proof | `ng doctor` and `test_every_skill_declares_a_decision_contract` pass | clears the ship gate |
| The heaviest body stays under budget | local proof | `ng tokens`: 2,875 of 3,000 | clears the ship gate |

## Interfaces and trust boundaries

- Internal interfaces affected: the skill authoring contract and `check_skill_contracts` in `nuclear_grade/cli.py`.
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: a human approves the contract change before merge.
- AI/model/tool authority boundaries: unchanged; no runtime authority is added.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN a skill is validated THE SYSTEM SHALL require a `## Decision contract` receipt with all five fields and a `Decision affected` tier of `block`, `warn`, or `observe`. | removes audit-the-audit | `REQUIRED_SKILL_SECTIONS` and `check_skill_contracts` | `pytest`, `ng doctor` |
| REQ-002 | THE SYSTEM SHALL roll up every skill's decision contract into one generated view. | single-source reviewer scan | `ng decisions` | `ng decisions` output and a smoke test |
| REQ-003 | THE SYSTEM SHALL keep the per-skill block out of the always-loaded description. | bounded routing cost | the block sits in the body | `ng tokens` descriptions flat |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview -- what changes and why | yes | `risk.md` and this file |
| Architecture -- shape and major parts | yes | contract doc, validator, CLI |
| Components and interfaces -- boundaries above | yes | `Interfaces and trust boundaries` |
| Data models -- shapes, classes, ownership | n/a | no data models |
| Error handling -- failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy -- how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: reviewer feedback on decision artifacts
- Source lineage, if cited: `docs/05-reference/skill-authoring-contract.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade change record, influenced by public design-basis and requirements-discipline ideas mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
