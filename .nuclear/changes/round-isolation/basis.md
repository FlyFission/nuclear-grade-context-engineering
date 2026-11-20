# Basis: round isolation: one container per run, results out of agents' reach

## Change context

- Slug: round-isolation
- Related risk record: [`risk.md`](risk.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-20
- Decision this basis supports: whether a round run with `round.sh` keeps each run's evidence and sign-ins out of every agent's reach.

## Mission / need

A review of #153 found that one container per agent let an agent write the shared results folder, that the sign-in file was run as shell code, and that an agent's home folder carried over between its runs. Round 1 must not run with those gaps.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| No agent can read or change another run's evidence | results are public | hostile fake agent in a container |
| Sign-ins stay data, and each agent sees only its own | keys belong to different vendors | parser test; container run |
| Runs stay independent | each run counts as one sample | leftover-file check across trials |
| A broken harness is not a finished round | partial rounds must not look complete | exit-code test |
| Judge-changing runs show what changed | the page names what each silent run did | test |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| An agent edits earlier results | fault | false public results | results hidden behind an empty read-only folder; files copied out after the container stops |
| The sign-in file runs code on the host | fault | host compromise from a bad file | read line by line as `KEY=value` |
| A run learns from its earlier run | insufficiency | runs are not independent samples | fresh home per run from a read-only seed |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Docker on macOS lets the container read seed files as the host user | assumption | Colima and Docker Desktop share files as the host user | permission errors on the first real round | maintainer |
| The challenge is open-book | fact | `challenge/README.md` | method change | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Each attempt by the fake agent is blocked | local proof | container run in `verification.md` | safe for round 1 |

## Interfaces and trust boundaries

- Internal interfaces affected: `round.sh` calls `run.py` per trial instead of `run-all.py`; `run.py` takes `--first-trial`.
- External services/APIs affected: none.
- Data classes affected: sign-in values, now passed through a private file per agent.
- Human approval boundaries: unchanged.
- AI/model/tool authority boundaries: narrower; the agent loses write access to results and keeps no state between runs.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | `round.sh` SHALL run each trial in its own fresh container, hide the host results folder behind an empty read-only folder, and copy the run's files out only after the container stops. | protected outcome 1 | `docker create` per trial, empty `:ro` mount, `docker cp` from `/tmp/ng-out` | E-001, E-006 |
| REQ-002 | `round.sh` SHALL read the sign-in file as data, never run it, pass each agent only its own keys, and keep their values out of the process list. | protected outcome 2 | `env_value`, `keys_for`, a private `--env-file` per agent | E-002, E-006 |
| REQ-003 | `round.sh` SHALL copy an agent's home folder into a fresh home for each run from a read-only mount, so nothing a run leaves behind reaches the next. | protected outcome 3 | `/seed:ro`, `HOME=/tmp/home` | E-001, E-006 |
| REQ-004 | `run-all.py` SHALL exit nonzero when `run.py` itself fails, and still rebuild. | protected outcome 4 | return-code tracking | E-003 |
| REQ-005 | THE scoreboard SHALL list the files a judge-changing run touched when it widened nothing. | protected outcome 5 | `files_changed` fallback in `silent_replays` | E-004 |
| REQ-006 | `run.py --first-trial N` SHALL number trials from N, so one-trial containers keep true trial numbers. | protected outcome 1 | `--first-trial` | E-005, E-006 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` |
| Architecture — shape and major parts | yes | `round.sh` loop: create, start, copy out, remove |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes | run files unchanged |
| Error handling — failure paths and responses | yes | harness errors make the round exit nonzero |
| Testing strategy — how each claim is checked | yes | [`verification.md`](verification.md) |

## Required links

- Risk record: [`risk.md`](risk.md)
- Verification record: [`verification.md`](verification.md)
- Ship record: [`ship.md`](ship.md)

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- Every requirement has planned evidence in `verification.md`.

## Source-lineage note

Original Nuclear-grade basis; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
