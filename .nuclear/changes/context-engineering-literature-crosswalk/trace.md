# Standard Trace Template

**Purpose:** Tie each important claim to its basis, its design and control features, its verification evidence, its release stance, and its gaps.

**Activation threshold:** Use for Standard changes where reviewers need to see how the requirements, claims, controls, tests/evals, and release decisions connect.

**Minimum useful version:** the claim IDs, the basis links, the control and design features, the evidence links, the ship stance, and the status labels.

**Overhead trap:** Do not build a giant trace table. Trace only the claims that matter for the stakes, trust, security, release, or behavior users can see.

---

## Change context

- Slug: context-engineering-literature-crosswalk
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-07-03

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Both projects framed as public peers; no endorsement/affiliation/superiority claim | `basis.md` | `plan.md` steps 1,4,5,6 / `docs/01-field-guide/context-engineering-literature-crosswalk.md` | Boundary status line + "what not to claim" section | local proof | `verification.md` overclaim scan | ship | pass |
| REQ-002 | No claim of implementing/conforming to the taxonomy or PRP as a standard | `basis.md` | `plan.md` steps 1,3,4 / crosswalk + `context-packs.md` + `WORKFLOWS.md` | "Not a compliance claim" status; conceptual mappings only | local proof | `verification.md` doc inspection | ship | pass |
| REQ-003 | Skill descriptions + command cards unchanged | `basis.md` | `plan.md` step 3 / docs-only change | No `skills/` or `commands/` edits | local proof | `verification.md` git status + gen-commands | ship | pass |
| REQ-004 | Both repos recorded as verified-public Tier 9 sources | `basis.md` | `plan.md` step 2 / `source-map.md` | Two Tier 9 rows with role + boundary notes | local proof | `verification.md` source-map inspection | ship | pass |

## Evidence chain

```text
Risk / need (adopter orientation across the context-engineering conversation, no overclaim)
  → Basis / requirement (REQ-001..004)
  → Control / design feature (boundary notes; verified-public sourcing; docs-only edits; conceptual mappings)
  → Verification evidence (ng doctor; ng validate; overclaim scan; gen-commands diff; git status)
  → Release decision (ship) / rollback (git revert) / monitoring (PR review) / baseline trigger (n/a)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| First-class emulation `examples/` convention not built | Named in the crosswalk §4 as an open gap, not delivered here | deferred | Ben Huffer | Roadmap grooming |
| Simpler on-ramp not built | Named in the crosswalk §4 as an open gap, not delivered here | deferred | Ben Huffer | Roadmap grooming |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `docs/01-field-guide/context-engineering-literature-crosswalk.md`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → specification/basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on requirements tracing, verification, keeping the approved version under control (CM), software assurance, secure development, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
