# Trace: a scoreboard page, a badge and a run-everything script for the challenge

## Change context

- Slug: challenge-scoreboard
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-18

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | both tracks side by side | `basis.md` | `plan.md` step 1 / `challenge-results/build.py#scoreboard_pairs` | pairing | local proof | `verification.md` E-001 | ship | pass |
| REQ-002 | headline and badge count only silent widenings; empty state is plain | `basis.md` | `plan.md` steps 1-2 / `challenge-results/build.py#silent_widenings` | two named outcomes | local proof | `verification.md` E-001..E-003 | ship | pass |
| REQ-003 | names are escaped | `basis.md` | `plan.md` step 2 / `challenge-results/build.py#render_scoreboard` | `html.escape` | local proof | `verification.md` E-004 | ship | pass |
| REQ-004 | missing CLIs are skipped by name | `basis.md` | `plan.md` step 3 / `challenge-results/run-all.py#plan` | PATH check | local proof | `verification.md` E-005 | ship | pass |
| REQ-005 | one line per tool version; not-comparable reasons shown | `basis.md` | `plan.md` step 4 / `challenge-results/build.py#scoreboard_pairs` | version in the pair key | local proof | `verification.md` E-006 | ship | pass |
| REQ-006 | silent runs listed with what changed and links | `basis.md` | `plan.md` step 5 / `challenge-results/build.py#silent_replays` | outcome filter, `html.escape` | local proof | `verification.md` E-007 | ship | pass |

## Evidence chain

```text
results exist only as a Markdown table; a round takes one command per agent per track
  -> REQ-001..006 (basis)
  -> renderers in build.py; run-all.py (design)
  -> seven harness tests and a dry run (verification)
  -> agent-generated evidence, re-run by CI; maintainer review (custody)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No real runs yet | the page shows the empty state until a round is scored | deferred to the first scored round | maintainer | first round |

## Required links

- [`basis.md`](basis.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- Every requirement traces to code and evidence with a status.

## Source-lineage note

Original Nuclear-grade trace; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
