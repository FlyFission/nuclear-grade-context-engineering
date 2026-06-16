# Variance and Drift

**Purpose:** This file tells apart a gap you accepted from a gap that nobody controlled.

## Definitions

- **Variance:** A known gap from the baseline that is recorded, owned, and either accepted or set to expire.
- **Drift:** A gap from the accepted baseline that nobody recorded or reviewed.

## Temporary modifications (deliberate, time-boxed)

A variance is usually a gap you *discover*. A temporary modification is a gap you *introduce on purpose* and intend to remove: a feature flag, an emergency bypass or hotfix override, a loosened tool permission, a disabled test or eval, a raised alert threshold, an autonomy downgrade, a skip-CI flag. It is still a variance from the baseline, so it is recorded the same way — with three disciplines that keep a deliberate exception from becoming permanent by accident:

- **Visible to whoever operates the system.** The people and agents running the system can see the active exceptions; a bypass nobody can see is indistinguishable from drift. Keep a short active-exceptions list, not just a buried record.
- **A named back-out, not just a re-check.** Record how the modification is removed and what restores the baseline, so removal is a decision someone can execute — not an open question.
- **An expiry or revisit trigger.** Every temporary modification carries a date or condition that forces removal or a conscious re-decision (reuses the variance recheck trigger).

Watch the high-blast-radius ones especially: disabled safety checks, loosened permissions, and emergency bypasses *accumulating* is itself a signal worth surfacing, even when each one was reasonable on its own.

## Use when

- public docs no longer match how the checker behaves;
- source links move, or a source's status changes;
- prompts, models, tools, dependencies, or CI change outside a packet;
- real use turns up behavior that the verification evidence does not cover.

## Exit criteria

A variance must have an owner, a reason, the impact, an expiration or re-check trigger, and how it was handled. A deliberate temporary modification additionally carries a named back-out and stays visible to whoever operates the system. Drift should turn into a packet, an incident or OPEX record, or a re-baseline action.

## Source-lineage note

This variance and drift model is an original workflow. It draws on public ideas about keeping the approved version of everything under control and learning from operation, mapped in `../00-standards-foundation/source-map.md`.
