# Basis: CI job timeouts

## Change context

- Slug: ci-job-timeouts
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-06
- Related risk record: [`risk.md`](risk.md)
- Decision this basis supports: whether bounded job timeouts belong in this repository's CI and in the CI that `ng scaffold-ci` ships.

## Mission / need

None of the 9 jobs in this repository's two workflows declared `timeout-minutes` (counted 2026-11-06), so each inherited GitHub's 360-minute default. `ng scaffold-ci` writes a required-gate workflow into other repositories with the same gap. A hung step in a required gate blocks merges for hours.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| A hung job ends within minutes | the required CI gate must give a verdict | REQ-001, REQ-002 |
| The bound cannot silently regress | a new job added without a timeout would reopen the gap | REQ-003 |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A cap shorter than a real run fails CI or a release | fault | blocked merge or release; rerun fixes it | generous caps; measured CI runtime; release caps flagged unmeasured |
| The checker passes a workflow it did not understand | insufficiency | false assurance | the checker fails when it sees no jobs; unit tests cover each defect |
| A downstream scaffold user loses a long validation | fault | their gate times out at 10 minutes | the scaffold job only validates packets (seconds in this repository's CI); documented in `ship.md` |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| `ci.yml` jobs finish far inside their caps | fact for the sampled run | run 42293941938: slowest job 76 s, whole run under 2 minutes | a job nearing 50% of its cap | maintainer |
| `release.yml` jobs finish inside their caps | fact for one run | the v0.7.0 release run (42122799962) took 3 min 18 s end to end by created and updated time; per-job times not read | a job nearing 50% of its cap | maintainer |
| An environment approval wait does not count toward `timeout-minutes` | unknown | not checked in this change | the first `pypi` job that waits for approval | maintainer |
| PyYAML is installed wherever the test must run | fact for CI | `ci.yml` installs `pyyaml`; the test skips without it, like `test_scaffold_ci_emits_parseable_yaml` | removing `pyyaml` from the CI install step | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The unchanged files fail the new test and the changed files pass it | local proof | `verification.md` E-001 | the test checks the defect |
| CI job runtimes are far below the caps | local proof | `verification.md` E-002 | cap sizing |
| A hung job in a serialized CI group held a slot for six hours at XERJ | source claim | XERJ `.github/scripts/workflow-timeout-guard.py` header; not independently verified | motivation only; no decision rests on it |

## Interfaces and trust boundaries

- Internal interfaces affected: the workflow text written by `ng scaffold-ci`; the CI jobs listed in `risk.md`.
- External services/APIs affected: GitHub Actions job scheduling only.
- Data classes affected: none.
- Human approval boundaries: `.github/**` is `standard+authority`; the maintainer's review and merge is the approval.
- AI/model/tool authority boundaries: the agent edited the workflows on a branch; it has no merge authority.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | EVERY JOB in `.github/workflows/*.yml` SHALL declare an integer `timeout-minutes` from 1 to 60, unless it calls a reusable workflow. | protected outcome 1 | job-level `timeout-minutes` | E-001, E-002 |
| REQ-002 | THE WORKFLOW written by `ng scaffold-ci` SHALL declare the same. | protected outcome 1 | `timeout-minutes: 10` in `nuclear_grade/cli.py` | E-001 |
| REQ-003 | A TEST SHALL fail when a job has no timeout, a zero, an over-large, a boolean or a non-integer one, or when the checker sees no jobs. | protected outcome 2 | `tests/test_workflow_timeouts.py` | E-001 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` |
| Architecture — shape and major parts | yes | job-level key plus one pytest module |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | not applicable | no data |
| Error handling — failure paths and responses | yes | the test names the job and the problem |
| Testing strategy — how each claim is checked | yes | [`verification.md`](verification.md) |

## Required links

- Risk record: [`risk.md`](risk.md)
- Verification record: [`verification.md`](verification.md)
- Ship record: [`ship.md`](ship.md)
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- Every requirement has planned evidence in `verification.md`.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
