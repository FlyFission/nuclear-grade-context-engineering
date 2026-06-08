# Standard Trace

**Purpose:** Tie each claim to its basis, control, evidence, and ship stance.

---

## Change context

- Slug: plugin-install-vehicle
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-06-08

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | One-line install exposes existing skills/commands as the `nuclear-grade` plugin, no hooks | `basis.md` | `plan.md` step 2 / `.claude-plugin/plugin.json` | schema-correct manifests; auto-discovery | source claim / local proof | `verification.md` | ship with residual risk | pass for schema+parse; live install deferred |
| REQ-002 | plugin.json version equals pyproject version | `basis.md` | `plan.md` step 3 / `tests/test_plugin_packaging.py` | version-sync test | local proof | `verification.md` | ship | pass |
| REQ-003 | No auto-run hooks configured (no `hooks/hooks.json`) | `basis.md` | `plan.md` step 2 / `.claude-plugin/` | no `hooks/hooks.json`; bundled CLI runs only on invocation | local proof | `verification.md` | ship | pass |
| REQ-004 | Install docs lead with the plugin; no "does not package" claim | `basis.md` | `plan.md` step 4 / `INSTALL.md` | honest wording; boundary note | local proof | `verification.md` | ship | pass |

## Evidence chain

```text
Need: one-line install without an executable surface or an overclaim
  -> Basis: REQ-001..004 (schema-correct, version-synced, no hooks, honest docs)
  -> Control: two manifests + packaging test + honest install docs
  -> Verification: schema check, parse, pytest, ruff, doctor, tokens, validate
  -> Release: ship with residual risk (live /plugin install deferred to maintainer)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Live `/plugin install` not run in CI | End-to-end install is unproven here | defer | FlyFission | Maintainer runs it on a Claude Code surface |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `.claude-plugin/`, `tests/test_plugin_packaging.py`, `INSTALL.md`, `README.md`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim to basis to evidence to release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on requirements tracing, verification, and release readiness, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
