---
name: checking-release-readiness
description: Records a ship, block, defer, or ship-with-risk decision that ties baseline, evidence status, residual risk, rollback, monitoring, and handoff together. Use when a packet, PR, release, dependency change, or agent-authority change approaches merge. Do not use early in development before evidence exists.
---

# Checking Release Readiness

## Overview

Release readiness is a careful, audited decision you write down. It is not a mood. It ties seven things together before a candidate becomes the accepted version: the baseline (the version everyone agreed is correct), the evidence status, the leftover risk, the rollback plan, the monitoring plan, the handoff, and the release decision itself.

## Decision contract

- **Claim checked:** the candidate has evidence, rollback, monitoring, and residual risk that is accepted or made a blocker.
- **Artifact observed:** `verification.md`/`trace.md` statuses and CI status -> the decision recorded in `ship.md`.
- **Decision affected:** block -- the `ship.md` ship/block/defer/ship-with-risk release decision.
- **Failure class:** unevidenced-or-unsafe-release (a gap or missing rollback treated as shippable).
- **Next action:** block the release; record the gap, its owner, and a recheck trigger.

## When to Use

- A Standard change record is getting close to merge or release.
- A pull request changes how users see the system, its security, its dependencies, what an agent may do, or how it runs in production.
- Evidence gaps have to be accepted or made into blockers.
- A quick candidate is being promoted into a baseline, a public claim, a release, or any other state that carries trust.
- A handoff, a support handoff, a lesson from real operation (OPEX), or a cautious decision stance needs to be stated plainly.

## When Not to Use

- The work is a local Quick change record with no effect on a release.
- An incident is still being contained or rolled back.

## Inputs

- `ship.md`, `verification.md`, `trace.md`, the pull request status, the CI status, the rollback plan, the monitoring plan, and the open risks.
- `docs/02-operating-system/change-control-packets.md`.

## Process

1. Confirm the baseline and the artifacts the change affects.
2. Confirm the question to decide has been answered by evidence, not by confidence.
3. Review each evidence status and each open gap. Check for drift building up: does the shipped change still serve the goal anchor, with the non-goals (the things ruled out of scope) still uncrossed? See `staying-on-mission`.
4. Confirm a rollback or restore path.
5. Confirm the monitoring and the checks you will run after release.
6. State why the decision is cautious enough given what is still uncertain.
7. Record one decision: ship, block, defer, or ship with named leftover risk.
8. Name the owner, the trigger to abort, whether a handoff is needed, the trigger for an operating lesson (OPEX), and the trigger to record a new baseline.

## Outputs

- An updated `ship.md`.
- The release decision and the reason for it.
- The leftover risks, the owner, the monitoring, and the rollback notes.
- The cautious decision stance, the handoff, and the OPEX trigger.

## Verification

- `ship.md` states the release decision, the rollback, and the monitoring.
- The CI and change-record validation results are linked, or it says plainly that they are not available.
- A reviewer can see why the release is accepted or blocked.

## Escalation

- Stop if release readiness rests on unreviewed compliance, safety, security, or approval claims.
- Escalate if rollback is impossible, monitoring is missing, or the effect on outside trust is unclear.

## Common Rationalizations

- "Green CI means ship." Release readiness also covers leftover risk and rollback.
- "The gap is probably fine." Any leftover risk you accept must be named.
- "Monitoring is overkill." Monitoring should scale with the stakes, not with habit.
- "Support will figure it out." The handoff to operations is part of release readiness.

## Red Flags

- No release decision.
- A rollback plan that is vague or missing.
- Deferred evidence with no owner and no stated consequence.

## Prompt

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

## Source-lineage note

This skill is an original release-readiness workflow influenced by public lifecycle, configuration, software assurance, and secure development sources mapped in `docs/00-standards-foundation/source-map.md`. It does not grant production suitability.
