# Risk: round isolation: one container per run, results out of agents' reach

## Change identity

- Slug: round-isolation
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-20
- Summary: fixes from the review of #153, before any scored round. `container/round.sh` now runs every trial in its own container, hides the results folder from the agent, reads the sign-in file as data, and gives each run a fresh home. `run-all.py` reports harness failures. The scoreboard lists the files a judge-changing run touched. `run.py` gains `--first-trial`.

## Mission anchor

- **Objective:** make sure no agent in a round can read or change another run's evidence, or carry anything into its own next run, before round 1 is published.
- **Success criterion:** a fake agent that tries each of those things inside `round.sh` is stopped every time, and the round still records every run.
- **Non-goals:** no change to outcomes, the scorer, the challenge, or the published method beyond what `challenge-scoreboard` logged. No results are published.

## Questioning-attitude summary

- The fact that would change the decision: if an agent could still reach the host results folder or another agent's keys. The container test checks both from inside the agent's own process.

## Affected configuration items

| Item | Change |
|---|---|
| `challenge-results/container/round.sh` | one container per trial; results hidden; env file parsed; fresh home per run |
| `challenge-results/run-all.py` | nonzero exit on harness failure |
| `challenge-results/run.py` | `--first-trial` |
| `challenge-results/build.py` | judge runs list touched files |
| `tests/test_challenge_results.py` | four new or changed tests |
| `.nuclear/changes/challenge-scoreboard/risk.md` | non-goal corrected: it did add one dated `METHOD.md` entry |

## Threshold screen

| Dimension | Rating | Why |
|---|---|---|
| Consequence | medium | round 1 results will be public and quoted |
| Reversibility | high | revert the commit; no round has run |
| Detectability | medium | unit tests plus a manual container run with a hostile fake agent |
| Trust boundary | yes | results tooling is under the `validators` rule |
| Uncertainty | medium | Docker on macOS maps file ownership differently from Linux |

## Selected mode

- **Mode:** Standard
- **Why this mode:** it edits results tooling (`validators`) and a trust-guarding test (`trust-tests`) under `.nuclear/consequence-policy.json`.

## Activated artifacts

- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Not activated: decision-authority record (no gate, CI or policy change).

## Immediate evidence obligations

- New tests fail on the previous commit and pass after.
- A container run with a fake agent shows each attempt blocked.

## Scope

- Paths covered by this record: `challenge-results/container/round.sh`, `challenge-results/run-all.py`, `challenge-results/run.py`, `challenge-results/build.py`, `challenge-results/README.md`, `tests/test_challenge_results.py`, `.nuclear/changes/challenge-scoreboard/risk.md`.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship: [`ship.md`](ship.md)

## Exit criteria

- The mode is justified and every path this change touches is named above.
- Evidence obligations are met or carried into `ship.md` as gaps.

## Source-lineage note

Original Nuclear-grade record; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
