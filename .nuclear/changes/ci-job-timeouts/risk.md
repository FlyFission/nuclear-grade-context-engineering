# Risk: CI job timeouts

## Change identity

- Slug: ci-job-timeouts
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-06
- Summary: every job in `.github/workflows/ci.yml` and `release.yml` now declares `timeout-minutes`, the workflow that `ng scaffold-ci` writes into other repositories declares one too, and `tests/test_workflow_timeouts.py` fails if any job loses its timeout or sets an unbounded one. Prompted by a study of the XERJ project (Apache-2.0), whose CI guard records a six-hour hang; the guard here is written independently.

## Mission anchor

- **Objective:** a hung step can hold a runner for minutes, not for GitHub's 360-minute default.
- **Success criterion:** all 9 repository jobs and the scaffold job declare an integer `timeout-minutes` between 1 and 60; the new test fails on the old files and passes on the new.
- **Non-goals:** no change to any step, trigger, permission, action pin or job order; no timeout tuning beyond sizing from one measured run; no CI path filtering; no change to the policy file.

## Questioning-attitude summary

- The fact that would change the decision: a job that legitimately runs longer than its cap. The slowest job in the measured run took 76 s against a 20-minute cap, so the margin is large for `ci.yml`. `release.yml` runs only on tags; its one run (v0.7.0) took 3 min 18 s end to end by workflow timestamps, against caps of 10 to 15 minutes per job.
- The fact still unknown: whether the `pypi` job's `environment: pypi` approval wait counts toward `timeout-minutes`. Not confirmed: the reviewer believed it does not but could not read the relevant documentation section, and I did not check. See `ship.md`.

## Affected configuration items

| Item | Change |
|---|---|
| `.github/workflows/ci.yml` | `timeout-minutes` on 4 jobs (validate 20, wheel-smoke 15, mcp-smoke 15, ci-gate 5) |
| `.github/workflows/release.yml` | `timeout-minutes` on 5 jobs (build 15, mcp-smoke 15, wheel-smoke 15, github-release 10, pypi 10) |
| `nuclear_grade/cli.py` | the workflow text `ng scaffold-ci` writes gains `timeout-minutes: 10` and a comment (shipped output) |
| `tests/test_workflow_timeouts.py` | new |
| `CHANGELOG.md` | `[Unreleased]` entry for the user-visible scaffold change and the CI timeouts |

## Threshold screen

| Dimension | Rating | Why |
|---|---|---|
| Consequence | medium | a cap set too low fails a release or CI run; a cap too high changes nothing |
| Reversibility | high | revert the commit; no state, no published artifact |
| Detectability | high | a too-low cap fails loudly and visibly in the run |
| Trust boundary | yes | `.github/**` is gate infrastructure; the repository policy rule `ci` is `standard+authority` and not overridable |
| Uncertainty | medium | one release run and one CI run measured; approval-wait behavior unconfirmed |

## HPI work-mode screen

- Work mode: rule-based edit of 9 job headers plus one new test.
- Error-likely situation: a cap that is tighter than a real run. Control: caps are at least 10x above the measured CI job times and 3x above the whole measured release run per job; the approval-wait question is carried as a gap.

## Selected mode

- **Mode:** Standard
- **Strict authority:** yes. `ng required-mode` returns `standard+authority` for `.github/**` (rule `ci`, not overridable), so this record carries `decision-authority.md` and validates with `--strict-authority`.
- **Why this mode:** the change touches CI, which is the out-of-band gate. The size of the edit does not lower the required mode.

## Activated artifacts

- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Decision-authority record: `decision-authority.md` (strict authority).
- Not activated: CM baseline (no release).

## Immediate evidence obligations

- `tests/test_workflow_timeouts.py` fails on the unchanged files and passes on the changed ones.
- The full suite, ruff, doctor, token budget, release identity and `validate --strict-authority` on this record pass.
- An independent review of the diff by a reviewer that did not write it.

## Scope

- Paths covered by this record: `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `nuclear_grade/cli.py`, `tests/test_workflow_timeouts.py`, `CHANGELOG.md`.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Decision authority: [`decision-authority.md`](decision-authority.md)
- Ship: [`ship.md`](ship.md)
- Source doctrine: [`activation-thresholds.md`](../../../docs/02-operating-system/activation-thresholds.md)

## Exit criteria

- The mode is justified and every path this change touches is named above.
- Evidence obligations are met or carried into `ship.md` as gaps.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
