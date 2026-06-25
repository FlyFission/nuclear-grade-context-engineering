# Standard Trace Template

**Purpose:** Tie each important claim to its basis, its design and control features, its verification evidence, its release stance, and its gaps.

**Activation threshold:** Use for Standard changes where reviewers need to see how the requirements, claims, controls, tests/evals, and release decisions connect.

**Minimum useful version:** the claim IDs, the basis links, the control and design features, the evidence links, the ship stance, and the status labels.

**Overhead trap:** Do not build a giant trace table. Trace only the claims that matter for the stakes, trust, security, release, or behavior users can see.

---

## Change context

- Slug: pmbok-pmi-ai-crosswalk
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-06-21

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | PMI/PMBOK framed as named background, no compliance claim | `basis.md` | `plan.md` steps 1,2,4 / `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md` | Boundary note + "what not to claim" + compliance-boundaries entry | local proof | `verification.md` overclaim scan | ship | pass |
| REQ-002 | No PMI text reproduced; structure not derived from PMI works | `basis.md` | `plan.md` steps 1,2 / `source-map.md`, `do-not-cite-directly.md` | PMBOK 8 described structurally; PMI excluded-direct | local proof | `verification.md` doc inspection | ship | pass |
| REQ-003 | Skill descriptions + command cards unchanged | `basis.md` | `plan.md` step 3 / 5 `SKILL.md` bodies | Body-only edits, avoid `## Prompt` | local proof | `verification.md` diff + gen-commands | ship | pass |

## Evidence chain

```text
Risk / need (adopter vocabulary bridge, no overclaim)
  → Basis / requirement (REQ-001..003)
  → Control / design feature (boundary notes; excluded-direct sourcing; body-only edits)
  → Verification evidence (ng doctor; overclaim scan; gen-commands diff; link checks)
  → Release decision (ship) / rollback (git revert) / monitoring (PR review) / baseline trigger (n/a)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| PMBOK 8 per-item names withheld | Keeps detail at "structural" level by design | accept | Ben Huffer | If PMI publishes an open edition |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → specification/basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on requirements tracing, verification, keeping the approved version under control (CM), software assurance, secure development, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
