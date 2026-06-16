# Trace -- skill decision contracts

**Purpose:** Tie each important claim to its basis, its control, its evidence, and its ship stance.

---

## Change context

- Slug: skill-decision-contracts
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-06-16

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Every skill declares a valid decision-contract receipt | `basis.md` | `nuclear_grade/cli.py` `check_skill_contracts` | required section plus tier lint | local proof | `verification.md` | ship | pass |
| REQ-002 | The blocks roll up into one generated view | `basis.md` | `nuclear_grade/cli.py` `handle_decisions` | `ng decisions` | local proof | `verification.md` | ship | pass |
| REQ-003 | The block stays out of the always-loaded description | `basis.md` | `skills/*/SKILL.md` body placement | body-only block | local proof | `verification.md` | ship | pass |

## Evidence chain

Sum up the most important chain in one compact flow.

```text
Reviewer feedback / Charter Art. 11
  -> Basis: every skill must name its one decision
  -> Control: required `## Decision contract` block, lint, and `ng decisions`
  -> Verification: pytest, ng doctor, ng tokens, ng decisions all green
  -> Release decision: ship with one named residual risk (block tightness)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Some blocks are wordier than the ideal one-scan line | scannability is the point of the change | accept | FlyFission | trim if a block is later shown to mislead |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `nuclear_grade/cli.py`, `tests/test_skill_contracts.py`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim -> specification/basis -> evidence -> release decision.

## Source-lineage note

Original Nuclear-grade change record, influenced by public requirements-tracing and verification ideas mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
