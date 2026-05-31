# Trace — Add Agent Tool Permissions

**Purpose:** Keep the worked example honest by tying each claim to its basis, controls, evidence, and release stance.

---

## Trace summary

| ID | Claim | Basis link | Control / design feature | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|
| C-001 | The agent writes only under the set workspace root. | `basis.md#derived-requirements-or-claims` | `WorkspaceGuard.write_text()` resolves the requested path and requires it to stay under the workspace root. | `verification.md`, `../../tests/test_workspace_guard.py` | Can ship for teaching v0 with scope warnings. | pass |
| C-004a | Denied C-001 writes produce visible audit events. | `basis.md#protected-outcomes` | `WorkspaceGuard._audit()` adds structured `write_denied` records. | `verification.md`, denied-path test checks. | Can ship as in-memory example evidence only. | pass |
| C-002 | External API calls need approved tool IDs and scoped credentials. | `basis.md#derived-requirements-or-claims` | A future tool list and credential binding. | Not built in v0. | Do not claim. | deferred |
| C-003 | Human approval is required for high-impact actions. | `basis.md#derived-requirements-or-claims` | A future policy engine and approval record. | Not built in v0. | Do not claim. | deferred |

## Evidence chain for C-001

```text
Risk: the AI agent is given the power to write files.
  → Basis: writes must stay inside the approved workspace; escapes are not allowed.
  → Control: resolve the real path + check it stays in the workspace + log denials.
  → Verification: the allowed write passes; `../`, absolute, and symlink escapes fail safely.
  → Ship: example v0 can launch with a clear teaching scope and leftover risks.
```

## Open trace gaps

| Gap | Why it matters | Disposition |
|---|---|---|
| Windows path rules not tested on their own. | Path behavior can differ across platforms. | Leftover risk accepted for the WSL/Linux example; add Windows CI before claiming a cross-platform guard. |
| Race conditions (TOCTOU, time-of-check to time-of-use) not tested. | Production attackers may abuse filesystem timing. | Clearly out of v0 scope; a production sandbox needs stronger controls. |
| No lasting audit log yet. | Real operations need durable evidence. | Deferred; the in-memory log only proves the idea. |
| C-002, C-003, and C-004 not built in full. | The tool, API, approval, and audit system is bigger than C-001. | Mark them deferred or gap, and do not claim broader safety. |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- `../../reference/workspace_guard.py`
- `../../tests/test_workspace_guard.py`

## Exit criteria

- Each claim has a status: `pass`, `gap`, `deferred`, or `not applicable`.
- C-001 can be followed without reading the whole repo.
- Deferred claims are not used as release evidence.

## Source-lineage note

This trace record is an original Nuclear-grade artifact. It is based on public-source-inspired ideas for claim-to-evidence tracing, verification, keeping the approved version under control, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
