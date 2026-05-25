# Skill Trigger Evaluation Trace

## Change context

- Slug: skill-trigger-evaluation
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-05-25

## Trace summary

| ID | Claim | Basis link | Control / design feature | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|
| REQ-001 | All skills have concrete trigger descriptions within repo limits | `basis.md` | Frontmatter edits and length assertions | `verification.md` | Required before ship | pass |
| REQ-002 | Every skill has minimum eval prompt coverage | `basis.md` | `skill-evaluation.md` and coverage test | `verification.md` | Required before ship | pass |
| REQ-003 | Skill folders stay lean without premature resources | `basis.md` | No per-skill resource directories added | `verification.md` | Acceptable for ship | pass |

## Evidence chain

```text
Skill-trigger risk
  -> Basis requirements
  -> Description and prompt-bank controls
  -> Pytest, doctor, packet validator
  -> Release decision and future eval obligation
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No full subagent benchmark in this change | A prompt bank is not the same as measured behavioral lift | accept | FlyFission | Before any major skill rewrite |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: repo diff for this change

## Exit criteria

- Each important claim has a status label.
- Every shipped claim has evidence or an accepted residual risk.
- Deferred/gap claims are not used as release evidence.
- Reviewer can navigate claim to basis to evidence to release decision quickly.

## Source-lineage note

Original Nuclear-grade trace inspired by public requirements traceability, verification, configuration-management, software assurance, secure-development, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
