# Trace — Add Agent Tool Permissions

**Purpose:** Keep the worked example honest by linking claims to basis, controls, evidence, and release posture.

---

## Trace summary

| ID | Claim | Basis link | Control / design feature | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|
| C-001 | Agent writes only under the configured workspace root. | `basis.md#derived-requirements-or-claims` | `WorkspaceGuard.write_text()` resolves requested path and requires containment under workspace root. | `verification.md`, `../../tests/test_workspace_guard.py` | Shippable for educational v0 with scope warnings. | pass |
| C-004a | Denied C-001 writes emit visible audit events. | `basis.md#protected-outcomes` | `WorkspaceGuard._audit()` appends structured `write_denied` records. | `verification.md`, denied-path test assertions. | Shippable as in-memory example evidence only. | pass |
| C-002 | External API calls require approved tool IDs and scoped credentials. | `basis.md#derived-requirements-or-claims` | Future tool registry and credential binding. | Not implemented in v0. | Do not claim. | deferred |
| C-003 | Human approval is required for high-impact actions. | `basis.md#derived-requirements-or-claims` | Future policy engine and approval record. | Not implemented in v0. | Do not claim. | deferred |

## Evidence chain for C-001

```text
Risk: AI agent receives file-write authority.
  → Basis: writes must remain inside approved workspace; escapes are unacceptable.
  → Control: canonical path resolution + workspace containment check + denial audit.
  → Verification: allowed write passes; traversal/absolute/symlink escapes fail safely.
  → Ship: example v0 can launch with explicit educational scope and residual risks.
```

## Open trace gaps

| Gap | Why it matters | Disposition |
|---|---|---|
| Windows path semantics not separately tested. | Path behavior can differ across platforms. | Residual risk accepted for WSL/Linux example; add Windows CI before claiming cross-platform guard. |
| Race conditions / TOCTOU not tested. | Production attackers may exploit filesystem timing. | Explicitly out of v0 scope; production sandboxing requires stronger controls. |
| Persistent audit log not implemented. | Real operations need durable evidence. | Deferred; in-memory log proves concept only. |
| C-002/C-003/C-004 full scope not implemented. | Tool/API/approval/audit system is larger than C-001. | Mark deferred/gap and do not claim broader safety. |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- `../../reference/workspace_guard.py`
- `../../tests/test_workspace_guard.py`

## Exit criteria

- Each claim has status: `pass`, `gap`, `deferred`, or `not applicable`.
- C-001 can be followed without reading the whole repo.
- Deferred claims are not used as release evidence.

## Source-lineage note

This trace record is an original Nuclear-grade artifact based on public-source-inspired traceability, verification, configuration, and release-readiness concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
