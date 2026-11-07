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
| REQ-001 | one 400-word always-on card replaces `AGENTS.md` body and the preamble | `basis.md` | `plan.md` phase 1 / `CORE-CARD.md` | `card_max` budget | local proof | `verification.md` E-001, E-002 | defer | planned |
| REQ-002 | per-prompt hook deleted; session hook prints the card; parity test | `basis.md` | `plan.md` phase 1h / `hooks/` | parity test | local proof | E-003 | defer | planned |
| REQ-003 | two agent-facing states; seven trap surfaces | `basis.md` | `plan.md` phases 1, 2 / card and mode skills | card text; backtest | local proof | E-002, E-006, E-007 | defer | planned |
| REQ-004 | four-section skills under 600 words | `basis.md` | `plan.md` phase 2 / contract and seven `SKILL.md` | contract tests; fit read | local proof | E-001, E-004, E-005 | defer | planned |
| REQ-005 | one-file Quick, three-file Standard; validator accepts both | `basis.md` | `plan.md` phase 3 / templates, `ng_validate.py` | validator tests; every existing record still validates | local proof | E-008 | defer | planned |
| REQ-006 | three-line receipt replaces the completion standard | `basis.md` | `plan.md` phase 1 / `AGENTS.md` | card section | peer review | E-002 | defer | planned |
| REQ-007 | no measured loss past the margin | `basis.md` | `plan.md` phase 2 / eval harness | ladder, routing, backtest re-run | independent verification | E-005, E-006, E-007 | defer | planned |
| REQ-008 | review reads callers, states consequence, changes no code; bug fixes grep callers | `basis.md` | `plan.md` phase 4 / two `SKILL.md`, card | skill text | peer review | E-004 | defer | planned |
| REQ-009 | markers harvested by `ng debt` | `basis.md` | `plan.md` phase 4 / `nuclear_grade/debt.py` | CLI and test | local proof | E-009 | defer | planned |
| REQ-010 | lenses and HPI screen demoted to reference; no efficacy claim | `basis.md` | `plan.md` phases 3, 5 / docs, skills, templates | edits; phrase test | peer review | E-002, E-004 | defer | planned |
| REQ-011 | tier three unchanged; always-on under 1,500 tokens; mode rule in the card only | `basis.md` | `plan.md` phases 3, 5 / existing tests, `tokens.py` | existing tests; budget; link test | local proof | E-001, E-010 | defer | planned |

## Evidence chain

```text
Need: in-session bureaucracy on every edit, whatever tier the control belongs to
  → Basis: REQ-001 to REQ-011
  → Controls: the card, one hook, two states, four-section skills, smaller records, receipt, review shape, markers; tier three untouched
  → Evidence: budget and parity tests; a fit read per body; the control-ladder, routing, and backtest re-runs
  → Custody: the drafting agent may not touch the rubric, cases, or margin; re-runs by a maintainer or CI
  → Decision: per phase, ship or stop; a failed gate keeps the earlier phases and reports the loss
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Compression was measured at five bullets, not at a four-section rewrite | the gate may behave differently | mitigate: REQ-007 re-run before any phase 2 body ships | maintainer | phase 2 results |
| The validator accepting two record shapes adds code to a trust surface | more branches in the checker | mitigate: existing tests unchanged plus new tests; every existing record re-validated in phase 3 | maintainer | phase 3 |
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
