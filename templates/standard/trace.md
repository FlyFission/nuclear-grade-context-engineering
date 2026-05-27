# Standard Trace Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Link important claims to basis, design/control features, verification evidence, release posture, and gaps.

**Activation threshold:** Use for Standard changes where reviewers need to see how requirements, claims, controls, tests/evals, and release decisions connect.

**Minimum useful version:** Claim IDs, basis links, control/design features, evidence links, ship posture, and status labels.

**Overhead trap:** Do not build a giant trace matrix. Trace only the claims that matter for consequence, trust, security, release, or user-visible behavior.

---

## Change context

- Slug:
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner:
- Date:

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Control / design feature | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|
| C-001 | | `basis.md` | | `verification.md` | | planned |

## Evidence chain

Summarize the most important chain in one compact flow.

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
- Every shipped claim has evidence or an accepted residual risk.
- Deferred/gap claims are not used as release evidence.
- Reviewer can navigate claim → specification/basis → evidence → release decision quickly.

## Source-lineage note

Original Nuclear-grade template inspired by public requirements traceability, verification, configuration-management, software assurance, secure-development, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
