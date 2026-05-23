# Variance and Drift

**Purpose:** Distinguish accepted deviation from uncontrolled divergence.

## Definitions

- **Variance:** A known deviation from baseline that is recorded, owned, and accepted or time-limited.
- **Drift:** An unrecorded or unreviewed divergence from the accepted baseline.

## Use when

- public docs no longer match validator behavior;
- source links move or source status changes;
- prompts, models, tools, dependencies, or CI change outside a packet;
- operation reveals behavior not covered by verification evidence.

## Exit criteria

Variance must have owner, reason, impact, expiration or recheck trigger, and disposition. Drift should become a packet, incident/OPEX record, or re-baseline action.

## Source-lineage note

This variance/drift model is an original workflow inspired by public configuration-management and operating-experience concepts mapped in `../00-standards-foundation/source-map.md`.
