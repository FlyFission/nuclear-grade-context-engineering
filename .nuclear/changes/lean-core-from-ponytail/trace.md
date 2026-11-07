# Trace: lean core, learned from Ponytail

## Change context

- Slug: lean-core-from-ponytail
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)
- Owner: Ben Huffer (maintainer); drafted by an AI agent
- Date: 2026-11-07

## Trace summary

All rows are `planned`. This record specifies; the phases build and prove.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | one always-on card at or under 600 words | `basis.md` | `plan.md` phase 1 / `CORE-CARD.md` | `card_max` budget | local proof | `verification.md` E-001, E-002 | defer | planned |
| REQ-002 | renders match the card | `basis.md` | `plan.md` phases 1, 1h / `tests/test_card_parity.py` | parity test | local proof | E-003 | defer | planned |
| REQ-003 | Core bodies within budget | `basis.md` | `plan.md` phase 2 / `nuclear_grade/tokens.py` | `core_skill_body_max` | local proof | E-001 | defer | planned |
| REQ-004 | operative register, one fit read per body | `basis.md` | `plan.md` phase 2 / seven `SKILL.md` | authoring rule; fit read | peer review | E-004 | defer | planned |
| REQ-005 | the floor stated once, unconditional | `basis.md` | `plan.md` phase 1 / `CORE-CARD.md` | grep test; maintainer read | local proof | E-002, E-003 | defer | planned |
| REQ-006 | the receipt replaces the completion standard | `basis.md` | `plan.md` phase 1 / `AGENTS.md` | card section | peer review | E-002 | defer | planned |
| REQ-007 | no measured loss past the margin | `basis.md` | `plan.md` phase 2 / eval harness | ladder, routing, backtest re-run | independent verification | E-005, E-006, E-007 | defer | planned |
| REQ-008 | review reads callers, states consequence, changes no code | `basis.md` | `plan.md` phase 3 / two `SKILL.md` | skill Process and Prompt | peer review | E-004 | defer | planned |
| REQ-009 | markers harvested by `ng debt` | `basis.md` | `plan.md` phase 3 / `nuclear_grade/debt.py` | CLI and test | local proof | E-008 | defer | planned |
| REQ-010 | no efficacy claim against Ponytail | `basis.md` | `plan.md` phases 1, 4, 5 / public docs | phrase test; maintainer read | peer review | E-002 | defer | planned |
| REQ-011 | mode rule in one place; doctrine reachable | `basis.md` | `plan.md` phase 4 / `docs/02-operating-system/` | reachability test | local proof | E-009 | defer | planned |

## Evidence chain

```text
Need: the operative surface is heavy and the doctrine already says it should not be
  → Basis: REQ-001 to REQ-011
  → Controls: the card, parity test, budgets, operative register, receipt, review shape, markers
  → Evidence: budget and parity tests; a fit read per body; the control-ladder, routing, and backtest re-runs
  → Custody: the drafting agent may not touch the rubric, cases, or margin; re-runs by a maintainer or CI
  → Decision: per phase, ship or stop; a failed gate keeps the earlier phases and reports the loss
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Compression was measured at five bullets, not at a full rewrite that keeps thirteen sections | the gate may behave differently on longer, structured bodies | mitigate: REQ-007 re-run before any phase 2 body ships | maintainer | phase 2 results |
| The ladder's grader is the same model family as the drafter | correlated error; a structured check, not independent | accept for now; stated in each phase record | maintainer | an external reviewer runs the harness |
| D1 persona is unresolved | voice affects the card's compression and the project's tone | defer to after phase 1 text exists | maintainer | phase 1 review |

## Required links

- [`risk.md`](risk.md)
- [`basis.md`](basis.md)
- [`plan.md`](plan.md)
- [`verification.md`](verification.md)
- [`ship.md`](ship.md)

## Exit criteria

- Every requirement in `basis.md` has a row, a planned evidence ID, and an owner.
- Open gaps are named with a recheck trigger.

## Source-lineage note

Original Nuclear-grade trace. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
