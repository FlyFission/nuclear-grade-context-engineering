# AI-Assisted PR Review Loop: Trace

## Change context

- Slug: ai-assisted-pr-review-loop
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-07-24

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Public loop uses roles rather than model brands and retains human authority | `basis.md#derived-requirements-or-claims` | `plan.md` steps 2 and 4; `README.md`; `docs/diagrams.md`; `WORKFLOWS.md` | Five-role sequence plus text fallback | local proof | `verification.md` E-001 | Candidate may proceed only if mirrored and readable | pass |
| REQ-002 | Verdict is bound to exact candidate and becomes stale after material change | `basis.md#derived-requirements-or-claims` | `plan.md` steps 2-3; diagrams and `ship.md` | Candidate ID messages and stale-verdict rule | local proof | `verification.md` E-001 | Required before merge/apply | pass |
| REQ-003 | Correction loop has a maximum round count and human escalation | `basis.md#derived-requirements-or-claims` | `plan.md` step 3; Standard plan template | Review candidate and correction budget section | local proof | `verification.md` E-001 | Required when review loop is activated | pass |
| REQ-004 | Ship record compares reviewed and current candidate identities | `basis.md#derived-requirements-or-claims` | `plan.md` step 3; Standard ship template | Reviewed candidate identity section | local proof | `verification.md` E-001 | Blocks stale verdict use | pass |
| REQ-005 | Diagram copies remain mirrored and repo gates pass | `basis.md#derived-requirements-or-claims` | `plan.md` steps 2 and 5; public-doc test | Contract test and final gate | local proof | `verification.md` E-001 and E-002 | Local gate complete; remote checks remain required | pass |

## Evidence chain

```text
External diagram and current-main gap inspection
  → REQ-001 through REQ-005
  → existing role diagram plus Standard plan/ship controls
  → focused contract and full repository verification
  → custody disclosure and exact-candidate review
  → human PR decision; merge remains held
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Semantic readability and proportionality not independently reviewed | Builder cannot self-certify the communication improvement | block until closure review and human PR review | FlyFission | Frozen candidate available |
| Mermaid not visually rendered in this worktree | Source syntax and GitHub rendering may diverge | mitigate through source review and GitHub PR render; block if malformed | FlyFission | PR opened |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: repository diff and final command records

## Exit criteria

- Every important claim has a status and evidence ID.
- No planned or gap claim is used as release evidence.
- Decisive evidence resolves to custody and coupling disclosure.
- Reviewer can move from requirement to changed surface, evidence, and ship posture.

## Source-lineage note

This trace records an original Nuclear-grade workflow refinement using public source families mapped in `docs/00-standards-foundation/source-map.md`. It does not claim formal verification, validation, compliance, safety, security, or regulatory adequacy.
