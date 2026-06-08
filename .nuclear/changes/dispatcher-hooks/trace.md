# Standard Trace

**Purpose:** Tie each claim to its basis, control, evidence, and ship stance.

---

## Change context

- Slug: dispatcher-hooks
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-06-08

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | SessionStart injects a static routing preamble | `basis.md` | `plan.md` step 2 / `hooks/session_start.py` | PREAMBLE constant | local proof | `verification.md` | ship | pass |
| REQ-002 | UserPromptSubmit injects a static line, never the prompt | `basis.md` | `plan.md` step 2 / `hooks/user_prompt_submit.py` | static CLASSIFY_LINE | local proof | `verification.md` | ship | pass |
| REQ-003 | Hooks are pure stdlib, zero network | `basis.md` | `plan.md` step 2 / `hooks/*.py` | imports limited to json, sys | local proof | `verification.md` | ship | pass |
| REQ-004 | Hooks are opt-in (no auto-activation) | `basis.md` | `plan.md` step 3 / no `hooks/hooks.json` | absence + HOOKS.md enable step | local proof | `verification.md` | ship | pass |
| REQ-005 | Preamble in sync with CORE.md + within budget | `basis.md` | `plan.md` step 4 / `tests/test_hooks.py` | sync + length tests | local proof | `verification.md` | ship | pass |
| (live) | The hooks inject correctly in a live Claude Code session | `basis.md` | a live session | n/a | unknown | deferred | ship with residual risk | deferred |

## Evidence chain

```text
Need: the dispatcher always-on, without an exfiltration surface or auto-activation
  -> Basis: REQ-001..005 (static injection, no-echo, zero-network, opt-in, in-sync)
  -> Control: two static stdlib hooks + HOOKS.md + the security/behavior tests
  -> Verification: smoke-run, network-ban, no-echo, firewall, sync, budget, pytest, ruff, doctor
  -> Release: ship with residual risk (a live Claude Code session run is deferred)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No live Claude Code session run | Injection behavior unproven end-to-end | defer | FlyFission | Maintainer enables the hooks and starts a session |
| Enabling is manual (settings.json) | More friction than auto-on | accept | FlyFission | A future `ng scaffold-hooks` could automate the opt-in |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `hooks/session_start.py`, `hooks/user_prompt_submit.py`, `HOOKS.md`, `tests/test_hooks.py`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim to basis to evidence to release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on requirements tracing and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
