# Variance and Drift

**Purpose:** This file tells apart a gap you accepted from a gap that nobody controlled.

## Definitions

- **Variance:** A known gap from the baseline that is recorded, owned, and either accepted or set to expire.
- **Drift:** A gap from the accepted baseline that nobody recorded or reviewed.

## Use when

- public docs no longer match how the checker behaves;
- source links move, or a source's status changes;
- prompts, models, tools, dependencies, or CI change outside a packet;
- real use turns up behavior that the verification evidence does not cover.

## Exit criteria

A variance must have an owner, a reason, the impact, an expiration or re-check trigger, and how it was handled. Drift should turn into a packet, an incident or OPEX record, or a re-baseline action.

## Source-lineage note

This variance and drift model is an original workflow. It draws on public ideas about keeping the approved version of everything under control and learning from operation, mapped in `../00-standards-foundation/source-map.md`.
