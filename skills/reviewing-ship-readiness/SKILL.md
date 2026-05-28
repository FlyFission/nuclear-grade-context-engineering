---
name: reviewing-ship-readiness
description: Use when deciding ship, block, defer, or ship-with-risk for packets, PRs, releases, dependency changes, or agent-authority changes.
---

# Reviewing Ship Readiness

## Overview

Ship readiness is a decision record, not a mood. It ties baseline, evidence status, residual risk, rollback, monitoring, handoff, and release decision together.

## When to Use

- A Standard packet is approaching merge or release.
- A PR changes user behavior, security posture, dependencies, agent authority, or operational state.
- Evidence gaps must be accepted or made blocking.
- Turnover, support handoff, OPEX trigger, or conservative decision posture needs to be explicit.

## When Not to Use

- The work is a local Quick packet with no release effect.
- Incident containment or rollback is still in progress.

## Inputs

- `ship.md`, `verification.md`, `trace.md`, PR status, CI status, rollback plan, monitoring plan, and open risks.
- `docs/02-operating-system/change-control-packets.md`.

## Process

1. Confirm baseline and affected artifacts.
2. Review each evidence status and unresolved gap, and check for accumulated drift: does the shipped change still serve the mission anchor, with non-goals uncrossed? See `controlling-mission-drift`.
3. Confirm rollback or restore path.
4. Confirm monitoring and post-release checks.
5. State why the decision is conservative enough for remaining uncertainty.
6. Record one decision: ship, block, defer, or ship with named residual risk.
7. Name owner, abort trigger, turnover need, OPEX trigger, and baseline trigger.

## Outputs

- Updated `ship.md`.
- Release decision and rationale.
- Residual risks, owner, monitoring, and rollback notes.
- Conservative decision posture, turnover, and OPEX trigger.

## Verification

- `ship.md` mentions release decision, rollback, and monitoring.
- CI and packet validation results are linked or explicitly unavailable.
- A reviewer can see why release is accepted or blocked.

## Escalation

- Stop if release readiness depends on unreviewed compliance, safety, security, or approval claims.
- Escalate if rollback is impossible, monitoring is missing, or external trust impact is unclear.

## Common Rationalizations

- "Green CI means ship." Release readiness includes residual risk and rollback.
- "The gap is probably fine." Accepted residual risk must be named.
- "Monitoring is overkill." Monitoring should scale by consequence, not habit.
- "Support will figure it out." Operational handoff is part of release readiness.

## Red Flags

- No release decision.
- Rollback is vague or missing.
- Deferred evidence has no owner or consequence.

## Source-lineage note

This skill is an original release-readiness workflow influenced by public lifecycle, configuration, software assurance, and secure development sources mapped in `docs/00-standards-foundation/source-map.md`. It does not grant production suitability.
