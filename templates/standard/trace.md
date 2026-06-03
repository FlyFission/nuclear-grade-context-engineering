# Standard Trace Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Tie each important claim to its basis, its design and control features, its verification evidence, its release stance, and its gaps.

**Activation threshold:** Use for Standard changes where reviewers need to see how the requirements, claims, controls, tests/evals, and release decisions connect.

**Minimum useful version:** the claim IDs, the basis links, the control and design features, the evidence links, the ship stance, and the status labels.

**Overhead trap:** Do not build a giant trace table. Trace only the claims that matter for the stakes, trust, security, release, or behavior users can see.

---

## Change context

- Slug:
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner:
- Date:

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

Use the same `REQ-NNN` IDs the requirement carries in `basis.md` / `spec.md` so the
chain reads end to end (`C-NNN` is an accepted alias for an older record). The
`Task / code ref` column reaches the `plan.md` build step and the code path that
delivers the claim, closing requirement → task → code → evidence.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | | `basis.md` | `plan.md` step 1 / `path/to/file` | | fact / assumption / unknown / source claim / local proof / decision authority | `verification.md` | | planned |

## Evidence chain

Sum up the most important chain in one compact flow.

```text
Risk / need
  → Basis / requirement
  → Control / design feature
  → Verification evidence
  → Release decision / rollback / monitoring / baseline trigger
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| | | accept / mitigate / defer / block | | |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals:

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → specification/basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on requirements tracing, verification, keeping the approved version under control (CM), software assurance, secure development, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
