---
name: screening-change-impact
description: Use when a controlled change may stale docs, tests, skills, commands, templates, validators, prompts, releases, baselines, or evidence.
---

# Screening Change Impact

## Overview

Impact screening asks what downstream artifacts become stale when controlled configuration changes.

## When to Use

- A change affects more than one artifact family.
- Public claims, source lineage, validators, tests, templates, skills, commands, dependencies, prompts, or release posture may need updates.
- A baseline or revalidation trigger may change.

## When Not to Use

- The change is clearly Quick and affects one local item with one proof step.
- A current `change-impact.md` already covers the exact scope.

## Inputs

- Controlled item list.
- `risk.md`, `basis.md`, `plan.md`, and diff.
- `docs/02-operating-system/change-impact.md`.

## Process

1. Identify artifact families that may be affected.
2. For each family, choose update, no-op, defer, or block.
3. Link evidence for each disposition.
4. Record revalidation triggers.
5. Reflect blockers or accepted gaps in `ship.md`.

## Outputs

- `change-impact.md` or compact impact screen.
- Revalidation triggers.
- Required follow-up updates.

## Verification

- No stale public claim, test, validator, skill, command, template, or release record is silently accepted.
- Deferred impacts have owners and triggers.
- Blocking impacts appear in release posture.

## Escalation

- Escalate when a change affects external trust, security, data, release posture, or public assurance language.
- Stop if impact cannot be determined from current context.

## Common Rationalizations

- "The diff is small." Small changes can invalidate docs, tests, or public claims.
- "The README can lag." Public docs are controlled trust surfaces.
- "Validator updates can come later." If docs claim behavior, validation drift matters now.

## Red Flags

- Changed lifecycle language without updating skills/commands/templates.
- Changed template shape without updating validator or tests.
- Deleted evidence while packets still link to it.

## Source-lineage note

This skill is an original impact-screen workflow influenced by public configuration-management, lifecycle, secure-development, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
