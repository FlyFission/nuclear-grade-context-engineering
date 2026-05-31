# Follow-up to Skills Token Audit (post-rename): Trace

**Purpose:** Tie each important claim to its basis, its design and control features, its verification evidence, its release stance, and its gaps.

**Activation threshold:** Use for Standard changes where reviewers need to see how the requirements, claims, controls, tests/evals, and release decisions connect.

**Minimum useful version:** the claim IDs, the basis links, the control and design features, the evidence links, the ship stance, and the status labels.

**Overhead trap:** Do not build a giant trace table. Trace only the claims that matter for the stakes, trust, security, release, or behavior users can see.

---

## Change context

- Slug: `follow-up-token-audit`
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: `@codex[agent]`
- Date: 2026-05-31

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|
| C-001 | `docs/05-reference/skills-token-audit.md` baseline tables reflect the current measured corpus | `basis.md` | Update doc from current measurement output | local proof | `verification.md` | ship | planned |
| C-002 | Overlap cluster skill IDs are post-rename and the decision is explicit: keep separate (no merges) | `basis.md` | Update overlap section + record decision | decision authority | `verification.md` | ship | planned |
| C-003 | Optional prose cuts are explicitly deferred; no disclaimer collapse or doc relocation in this follow-up | `basis.md` | Decision recorded in audit doc + ship posture | decision authority | `verification.md` | ship | planned |

## Evidence chain

Sum up the most important chain in one compact flow.

```text
Deferred follow-up items (need)
  → Explicit decisions (basis)
  → Update audit doc to match measured baseline (control)
  → `ruff` / `pytest` / `ng doctor|eval|tokens|validate` (evidence)
  → Merge doc-only change (ship posture)
```

## Open trace gaps

None (doc-only change bounded by deterministic checks).

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: listed below.
  - `docs/05-reference/skills-token-audit.md`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → specification/basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on requirements tracing, verification, keeping the approved version under control (CM), software assurance, secure development, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
