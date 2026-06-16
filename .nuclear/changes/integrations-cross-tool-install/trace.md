# Standard Trace Record

**Purpose:** Tie each important claim to its basis, its design and control features, its verification evidence, its release stance, and its gaps.

**Activation threshold:** Use for Standard changes where reviewers need to see how the requirements, claims, controls, tests/evals, and release decisions connect.

**Minimum useful version:** the claim IDs, the basis links, the control and design features, the evidence links, the ship stance, and the status labels.

**Overhead trap:** Do not build a giant trace table. Trace only the claims that matter for the stakes, trust, security, release, or behavior users can see.

---

## Change context

- Slug: integrations-cross-tool-install
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission (Ben Huffer)
- Date: 2026-06-16

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | install copies skills to the tool's dir | `basis.md` | `plan.md` step 1 / `nuclear_grade/cli.py` | `install_dest` + `handle_install` | local proof | `verification.md` | ship | pass |
| REQ-002 | base stays zero-dep; MCP is optional | `basis.md` | `plan.md` step 4 / `pyproject.toml` | optional `mcp` extra | local proof | `verification.md` | ship | pass |
| REQ-003 | unverified path warns and accepts `--dest` | `basis.md` | `plan.md` step 2 / `nuclear_grade/cli.py` | `VERIFIED_TOOLS` + note | local proof | `verification.md` | ship | pass |
| REQ-004 | version mirrors stay in sync | `basis.md` | `plan.md` step 3 / `tests/test_packaging.py` | version-sync test | local proof | `verification.md` | ship | pass |

## Evidence chain

Sum up the most important chain in one compact flow.

```text
Need: install once, auto-surface everywhere, stay lean
  → Basis: REQ-001..004 (paths, zero-dep, verify-or-override, version sync)
  → Control: install_dest + VERIFIED_TOOLS + optional mcp extra + sync test
  → Verification: install/mcp/version-sync tests, ruff, doctor, tokens, mcp-smoke
  → Release: ship additive change on PR #42; revert is the rollback
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| VS Code user-scope skills path is best-known, not doc-confirmed | a wrong user path mislocates skills | accept | FlyFission | VS Code documents the user path |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: PR #42

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → specification/basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on requirements tracing, verification, keeping the approved version under control (CM), software assurance, secure development, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
