# ng-ship-review

## Purpose

Review whether a change is ready to release. Treat this as the careful, final gate, and record the call: ship, block, defer, or ship with known risk. This is a portable command prompt.

## Use when

- A Standard change record (the packet) is near merge or release.
- Gaps in the evidence, the rollback plan, the monitoring plan, or the leftover risks need a decision.
- A PR changes who or what is trusted.
- A fast draft is about to become a baseline, a public claim, a release, or an accepted version under control.
- The handoff, the support handoff, the lessons-from-operation (OPEX) trigger, or how cautious to be is unclear.

## Do not use when

- The work is not headed for release.
- You are still containing an incident.

## Inputs

- `ship.md`, `verification.md`, `trace.md`, the PR status, the test-run (CI) status, the rollback plan, the monitoring plan, and the leftover risks.

## Prompt text

```text
Perform a Nuclear-grade ship-readiness review.

Inputs:
- packet: .nuclear/changes/<slug>/
- baseline: <commit/PR/release>
- evidence status: <summary>
- unresolved gaps: <list>
- rollback/restore path: <summary>
- monitoring/post-release checks: <summary>
- turnover/support handoff:
- OPEX trigger:

Return:
- the release decision: ship, block, defer, or ship with a named leftover risk
- whether the evidence actually answers the decision question
- an evidence summary
- the leftover risks and who owns them
- the rollback and monitoring notes
- why this is the cautious call, the abort trigger, the handoff, and the lessons-from-operation (OPEX) trigger
- the exact packet updates needed
```

## Files created or modified

- `.nuclear/changes/<slug>/ship.md`
- `.nuclear/changes/<slug>/verification.md` if the evidence status changed.

## Expected outputs

- A clear release decision.
- An answer to the decision question, backed by evidence.
- A statement of the leftover risk.
- A record of the rollback and monitoring plans.
- The cautious posture, the handoff, and the trigger for capturing a lesson.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating a green test run (CI) as proof it is ready to ship.
- Promoting a draft to an accepted version before the audit gates clear.
- Deferring evidence with no owner and no read on the impact.
- Missing the rollback or monitoring plan.
- Missing the handoff to operations or the lessons-from-operation (OPEX) trigger.

## Legal/assurance boundary note

A ship review supports the release call. It does not create fitness for production, compliance, certification, safety, security, or regulatory adequacy.
