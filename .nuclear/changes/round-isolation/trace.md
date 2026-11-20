# Trace: round isolation: one container per run, results out of agents' reach

## Change context

- Slug: round-isolation
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-20

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | round.sh | `basis.md` | `plan.md` | `docker create` per trial, empty `:ro` mount, `docker cp` from `/tmp/ng-out` | local proof | `verification.md` E-001, E-006 | ship | pass |
| REQ-002 | round.sh | `basis.md` | `plan.md` | `env_value`, `keys_for`, a private `--env-file` per agent | local proof | `verification.md` E-002, E-006 | ship | pass |
| REQ-003 | round.sh | `basis.md` | `plan.md` | `/seed:ro`, `HOME=/tmp/home` | local proof | `verification.md` E-001, E-006 | ship | pass |
| REQ-004 | run-all.py | `basis.md` | `plan.md` | return-code tracking | local proof | `verification.md` E-003 | ship | pass |
| REQ-005 | THE scoreboard | `basis.md` | `plan.md` | `files_changed` fallback in `silent_replays` | local proof | `verification.md` E-004 | ship | pass |
| REQ-006 | run.py --first-trial N | `basis.md` | `plan.md` | `--first-trial` | local proof | `verification.md` E-005, E-006 | ship | pass |

## Evidence chain

```text
review of #153 found shared results, a sourced env file and a shared home
  -> REQ-001..006 (basis)
  -> per-trial containers, parser, fresh home, exit codes (design)
  -> tests and a hostile fake-agent container run (verification)
  -> agent-generated evidence, re-run by CI; maintainer review (custody)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Not yet run on macOS | file ownership differs there | first real round on the Mac Studio | maintainer | round 1 |

## Required links

- [`basis.md`](basis.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- Every requirement traces to code and evidence with a status.

## Source-lineage note

Original Nuclear-grade trace; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
