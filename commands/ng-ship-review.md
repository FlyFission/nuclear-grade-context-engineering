# ng-ship-review

## Purpose

Review release readiness and record ship, block, defer, or ship-with-risk decisions. This is a portable command prompt.

## Use when

- A Standard packet is approaching merge or release.
- Evidence gaps, rollback, monitoring, or residual risks need a decision.
- A PR changes trust posture.
- Turnover, support handoff, OPEX trigger, or conservative decision posture is unclear.

## Do not use when

- The work is not release-facing.
- Incident containment is still underway.

## Inputs

- `ship.md`, `verification.md`, `trace.md`, PR status, CI status, rollback plan, monitoring plan, and residual risks.

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
- release decision: ship, block, defer, or ship with named residual risk
- evidence summary
- residual risks and owner
- rollback and monitoring notes
- conservative decision rationale, abort trigger, handoff, and OPEX trigger
- exact packet updates needed
```

## Files created or modified

- `.nuclear/changes/<slug>/ship.md`
- `.nuclear/changes/<slug>/verification.md` if evidence status changed.

## Expected outputs

- Explicit release decision.
- Residual risk statement.
- Rollback and monitoring record.
- Conservative posture, turnover, and learning trigger.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Equating green CI with ship readiness.
- Deferring evidence without owner or impact.
- Missing rollback or monitoring.
- Missing operational handoff or OPEX trigger.

## Legal/assurance boundary note

Ship review supports release judgment. It does not create production suitability, compliance, certification, safety, security, or regulatory adequacy.
