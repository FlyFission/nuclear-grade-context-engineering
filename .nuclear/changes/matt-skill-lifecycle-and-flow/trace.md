# Trace: Matt skill lifecycle and flow adaptation

## Trace summary

| ID | Source | Planned implementation | Verification | Status |
|---|---|---|---|---|
| REQ-001 | `basis.md` | router skill, contract tests, related docs | `verification.md` E-001 | pass |
| REQ-002 | `basis.md` | lifecycle registry/module | `verification.md` E-002 | pass |
| REQ-003 | `basis.md` | installer/package filtering and negative fixtures | `verification.md` E-003 | pass |
| REQ-004 | `basis.md` | catalog-level route scenarios and acceptable-route scorer | `verification.md` E-004 | pass; live run deferred |
| REQ-005 | `basis.md` | aggregate token/profile budgets | `verification.md` E-005 | pass |
| REQ-006 | `basis.md` | compact skill assets/references and generator fallback | `verification.md` E-006 | pass |
| REQ-007 | `basis.md` | workflow/doctrine/template adapters | `verification.md` E-007 | pass |
| REQ-008 | `basis.md` | lifecycle crosswalk | `verification.md` E-008 | pass |
| REQ-009 | `basis.md` | generated/docs/package parity | `verification.md` E-009 | local pass; CI pending |

## Evidence chain

```text
Audited routing/context/workflow gaps
  -> REQ-001 through REQ-009
  -> lifecycle, scorer, budgets, compact pilot, and workflow adapters
  -> focused tests + full suite + project checks + independent reviews
  -> PR readiness decision held separately from merge/release
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Cross-host live routing remains nondeterministic/manual | Static cases and scorers do not prove deployed host behavior | defer to release-candidate evaluation, do not overclaim | maintainer | promotion or cross-host claim |
| PR #85 evidence is draft and based on limited pools | It supports a pilot, not broad compression efficacy | constrain to pilot | maintainer | broader rollout request |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every requirement has a concrete implementation location and evidence ID.
- Deferred evidence is not used as release support.

## Source-lineage note

This trace records a selective public-pattern adaptation mapped in `docs/00-standards-foundation/source-map.md`. It makes no compliance or formal assurance claim.
