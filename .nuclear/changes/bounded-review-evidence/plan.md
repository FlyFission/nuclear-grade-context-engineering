# Plan — bounded review evidence

1. Add opt-in `review-run.v1.json` and separately pinned authorization templates; validate records on the existing packet-checking path.
2. Require `validate PACKET --before-review` in new bounded-panel workflows. Reject malformed, overspent, infeasible, unsupported or stopped attempts before dispatch; no reset/amendment engine.
3. Keep existing doctrine refinements for native ingress, stable proof hashes, parity and exact-state follow-up; regenerate cards and deliberately update the panel prompt fixture.
4. Run behavioral CLI regressions and full repository pytest, lint, doctor, tokens, release identity, strict packet validation, compile and generated badge parity.
5. Commit and update the draft PR around the actual gate. Do not merge or refresh installed skills.

Non-goals: application runtime code, provider interception/calls, authenticated authority, external append-only storage, automatic budget amendment or new review councils.

## Required links

- [Risk](risk.md), [basis](basis.md), [plan](plan.md), [trace](trace.md), [verification](verification.md), [ship](ship.md).
- [Controlled items](controlled-items.md), [operating lesson](opex.md).

## Exit criteria

The scoped wording passes the recorded checks and remains pending human PR review.

## Source-lineage note

An original operational refinement of existing evidence custody and evaluation discipline; see the repository [source map](../../../docs/00-standards-foundation/source-map.md). No compliance, independence, efficacy, or formal assurance claim.
