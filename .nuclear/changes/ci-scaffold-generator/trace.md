# Standard Trace

**Purpose:** Tie each claim to its basis, control, evidence, and ship stance.

---

## Change context

- Slug: ci-scaffold-generator
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-06-08

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | `ng scaffold-ci` writes a valid workflow that validates change records | `basis.md` | `plan.md` step 1 / `nuclear_grade/cli.py` | subcommand + template | local proof | `verification.md` | ship | pass |
| REQ-002 | Generated workflow is least-privilege, `pull_request`-triggered, secret-free | `basis.md` | `plan.md` step 1 / cli.py template | hardened template | local proof | `verification.md` | ship | pass |
| REQ-003 | This repo's `ci.yml` declares least-privilege permissions | `basis.md` | `plan.md` step 2 / `.github/workflows/ci.yml` | `permissions: contents: read` | local proof | CI run | ship | pass |
| REQ-004 | Generator behavior guarded by tests | `basis.md` | `plan.md` step 3 / `tests/test_ng_cli.py` | generator tests | local proof | `verification.md` | ship | pass |
| (live run) | The workflow runs green on a real adopter PR | `basis.md` | a live GitHub Actions run | n/a | unknown | deferred | ship with residual risk | deferred |

## Evidence chain

```text
Need: a rung-4 gate the authoring agent cannot defeat
  -> Basis: REQ-001..004 (valid + hardened generated workflow; repo practices it; guarded)
  -> Control: ng scaffold-ci + hardened template + ci.yml permissions + tests
  -> Verification: YAML parse, generator tests, pytest, ruff, doctor, tokens, validate
  -> Release: ship with residual risk (a live Actions run is deferred to the maintainer)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No live GitHub Actions run | End-to-end gate behavior unproven here | defer | FlyFission | Maintainer runs the generated workflow on a real PR |
| Actions pinned to tags, not SHAs | Mutable-tag supply-chain risk (F5) | accept | FlyFission | Adopters SHA-pin for production (recommended in-file) |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `nuclear_grade/cli.py`, `.github/workflows/ci.yml`, `tests/test_ng_cli.py`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim to basis to evidence to release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on requirements tracing, release readiness, and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
