# Basis: a scoreboard page, a badge and a run-everything script for the challenge

## Change context

- Slug: challenge-scoreboard
- Related risk record: [`risk.md`](risk.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-18
- Decision this basis supports: whether the new outputs report only what the existing rows support, and whether `run-all.py` runs the same harness the method describes.

## Mission / need

The challenge has two tracks (task only, house rules given) and a tested harness, but its results exist only as a Markdown table, and running a round means one command per agent per track. A head-to-head reads best as one page with both tracks side by side, and a round should take one command on a machine that has the agent CLIs.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The page reports only what the rows say | people will quote it | pairing and count tests |
| An empty page says there are no runs | no implied result before a round | empty-state test |
| Agent and model names cannot inject markup | names come from run files anyone can submit | escaping test |
| `run-all.py` uses `run.py` unchanged on both tracks | the method stays the same | plan test and dry run |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| Headline overstates failures | fault | an unfair public claim about an agent | counts only `UNFLAGGED` and `JUDGE`, the two outcomes that mean a silent widening or a changed judge; test pins the count |
| Page ranks agents | insufficiency | reads as a safety rating | rows stay alphabetical; the page repeats the method's limits |
| Script hides a missing agent | insufficiency | a round looks complete when it is not | skipped agents are printed by name |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| A CLI on PATH is the one agents.json names | assumption | agents.json command[0] | a wrapper with the same name | maintainer |
| shields.io endpoint schema v1 | source claim | shields.io endpoint docs | schema change | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Outcome logic is untouched | local proof | existing harness tests pass unmodified | safe to merge |

## Interfaces and trust boundaries

- Internal interfaces affected: `build.main` writes two more files; `run-all.py` calls `run.py` and `build.py` as subprocesses.
- External services/APIs affected: none; the badge is read by shields.io only if someone links it.
- Data classes affected: none; the run-file schema is unchanged.
- Human approval boundaries: unchanged; rulings still override outcomes.
- AI/model/tool authority boundaries: `run-all.py` launches the same agent commands `run.py` already launches, in the container the method requires.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE scoreboard SHALL pair each agent and model's task-only and house-rules rows, and say "not run yet" for a missing track. | protected outcome 1 | `scoreboard_pairs` | E-001 |
| REQ-002 | THE headline and badge SHALL count only silent widenings and changed judges, over all scored runs, and SHALL say so plainly when there are no runs. | protected outcomes 1, 2 | `silent_widenings`, empty-state text | E-001, E-002, E-003 |
| REQ-003 | THE page SHALL escape agent and model names. | protected outcome 3 | `html.escape` | E-004 |
| REQ-004 | `run-all.py` SHALL skip and name agents whose CLI is missing, and run `run.py` on both tracks for the rest. | protected outcome 4 | `plan`, `TRACKS` | E-005 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` |
| Architecture — shape and major parts | yes | renderers in `build.py`; orchestration in `run-all.py` |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes | the existing summary rows; badge schema v1 |
| Error handling — failure paths and responses | yes | unknown agents and bad `--model` values exit with a message |
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
