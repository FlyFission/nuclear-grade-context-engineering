---
name: baselining-configuration
description: Records the accepted controlled state of items and the evidence behind it, and names what would make the baseline stale. Use when a Standard packet ships, when prompts, models, tools, dependencies, docs, or release artifacts are accepted, or when OPEX requires re-baselining. Do not use for a Quick local edit with no release or trust-bearing state, or while work is still under review.
---

# Baselining Configuration

## Overview

A baseline records the accepted state of controlled items and the evidence that supports that state. It names what would make the baseline stale.

## When to Use

- A Standard packet ships or public-facing workflow state changes.
- Controlled prompts, models, tools, dependencies, docs, templates, skills, commands, validators, or release artifacts are accepted.
- OPEX or review feedback requires re-baselining.
- A near miss or operating lesson changes the accepted state or revalidation trigger.

## When Not to Use

- The change is a Quick local edit with no release or trust-bearing state.
- The work is still under review and evidence is not ready.

## Inputs

- `controlled-items.md`, `change-impact.md`, `verification.md`, and `ship.md`.
- PR/commit/release identity.
- Accepted gaps and revalidation triggers.

## Process

1. Name the baseline and decision point.
2. Record included and excluded controlled items.
3. Link basis, impact, trace, verification, ship, and OPEX records.
4. Name accepted residual risks and revalidation triggers.
5. Record what would require re-baseline.

## Outputs

- `baseline.md` or baseline section in `ship.md`.
- Re-baseline triggers.
- Accepted gaps with owners.
- OPEX link when learning changed the baseline.

## Verification

- Baseline identity is reproducible from commit, PR, release, or artifact.
- Controlled items are included or explicitly excluded.
- Revalidation triggers are visible.

## Escalation

- Stop if evidence is missing but the baseline claims acceptance.
- Escalate when baseline affects customer, regulated, safety, security, procurement, or external-trust claims.

## Common Rationalizations

- "The merge commit is the baseline." The commit identifies state; the record explains accepted basis and triggers.
- "We will update baseline later." That creates drift at the decision point.
- "Only release teams need baselines." Agent prompts, skills, and public claims also drift.

## Red Flags

- Baseline lacks evidence links.
- Exclusions are hidden.
- Revalidation triggers are absent for dependencies, models, prompts, tools, or public claims.

## Source-lineage note

This skill is an original baseline workflow influenced by public configuration-management, lifecycle, release-readiness, and operating-learning sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
