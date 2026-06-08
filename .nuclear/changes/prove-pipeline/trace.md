# Standard Trace

**Purpose:** Tie each claim to its basis, control, evidence, and ship stance.

---

## Change context

- Slug: prove-pipeline
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-06-08

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | The five PROVE subagents exist with valid frontmatter | `basis.md` | `plan.md` step 2 / `agents/*.md` | the five defs | local proof | `verification.md` | ship | pass |
| REQ-002 | Each stage's tools encode its authority | `basis.md` | `plan.md` step 2 / `agents/*.md` | per-stage `tools` | local proof | `verification.md` | ship | pass |
| REQ-003 | Each def carries the baton-pass contract | `basis.md` | `plan.md` step 2 / agent bodies | Context Pack + confirm + fence | local proof | `verification.md` | ship | pass |
| REQ-004 | The README documents the honesty limit | `basis.md` | `plan.md` step 3 / `agents/README.md` | the caveat | local proof | `verification.md` | ship | pass |
| (live) | The pipeline orchestrates correctly end-to-end | `basis.md` | a live multi-agent run | n/a | unknown | deferred | ship with residual risk | deferred |

## Evidence chain

```text
Need: encode the PROVE authority split visibly, without overclaiming confinement
  -> Basis: REQ-001..004 (roster, authority-tools, baton contract, honesty)
  -> Control: five tool-bounded subagent defs + README + the contract test
  -> Verification: roster/frontmatter/authority tests, pytest, ruff, doctor, tokens, validate
  -> Release: ship with residual risk (a live multi-agent run is deferred; confinement is advisory per F6)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No live multi-agent orchestration run | End-to-end behavior unproven here | defer | FlyFission | Maintainer runs the pipeline on a Standard+ change |
| Tool boundaries are advisory (F6) | Plugin cannot pin permissionMode | accept | FlyFission | For real confinement, move agents to `.claude/agents/` |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `agents/`, `tests/test_agents.py`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim to basis to evidence to release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on requirements tracing and human performance improvement, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
