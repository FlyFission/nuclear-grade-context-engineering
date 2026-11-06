# Trace: move the required-mode command into the engine module

## Change context

- Slug: ws1-required-mode-handler
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-04

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | the CLI handler only delegates | `basis.md` | `plan.md` step 1 / `nuclear_grade/cli.py#handle_required_mode` | delegate test | local proof | `verification.md` E-001 | ship | pass |
| REQ-002 | the hint matches the failure | `basis.md` | `plan.md` step 2 / `nuclear_grade/consequence.py#fix_hints` | field-based selection | local proof | `verification.md` E-002 | ship | pass |
| REQ-003 | behavior unchanged | `basis.md` | `plan.md` step 1 / `nuclear_grade/consequence.py#run_cli` | verbatim move | local proof | `verification.md` E-003 | ship | pass |

## Evidence chain

```text
gate-cli covers cli.py only partly (ws1-repo-policy residual)
  -> REQ-001..003 (basis)
  -> run_cli in consequence.py; delegate in cli.py (design)
  -> delegate, hint, and existing CLI tests (verification)
  -> agent-generated evidence, re-run by CI; maintainer review (custody)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| not applicable | not applicable | not applicable | not applicable | not applicable |

## Required links

- [`basis.md`](basis.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- Every requirement traces to code and evidence with a status.

## Source-lineage note

Original Nuclear-grade trace; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
