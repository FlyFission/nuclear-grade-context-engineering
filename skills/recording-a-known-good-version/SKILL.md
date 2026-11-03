---
name: recording-a-known-good-version
description: Records the version everyone agreed is correct, the evidence behind it, and what would make that record out of date. Use when a standard change ships, when prompts, models, tools, dependencies, docs, or release items are accepted, or when a lesson forces a re-record. Do not use for a tiny local edit with nothing to release or trust, or while the work is still under review.
---

# Recording a Known-Good Version

## Overview

A baseline is simply the version everyone agreed is correct and wants to protect. This skill writes down that version, the evidence that backs it, and the things that would make it out of date.

## Decision contract

- **Claim checked:** the accepted version can be rebuilt exactly from its named commit/PR/release, everything under control is either included or deliberately left out, the accepted residual risks have owners, and the triggers that force a new known-good version are recorded.
- **Artifact observed:** `controlled-items.md`, `change-impact.md`, `verification.md`, the `ship.md` decision, and the identifying commit/PR/release -> a `baseline.md` with included/excluded scope, accepted gaps, and re-record triggers.
- **Decision affected:** warn -- the accepted baseline the ship decision produced, and the triggers that invalidate it.
- **Failure class:** unrebuildable-baseline (a version recorded as accepted with missing evidence or silently dropped scope).
- **Next action:** record the missing link or excluded scope as a named gap; escalate when the version affects customers, regulated work, or outside trust.

## When to Use

- A standard change ships, or the public-facing state of the workflow changes.
- Controlled prompts, models, tools, dependencies, docs, templates, skills, commands, checkers, or release items are accepted.
- A lesson from operation or a piece of review feedback means you need to re-record the known-good version.
- A near miss or operating lesson changes the accepted state or the trigger for re-checking it.

## When Not to Use

- The change is a tiny local edit with nothing to release and no trust on the line.
- The work is still under review and the evidence is not ready.

## Inputs

- The records for what is under control, the ripple effects, the verification, and the ship decision (`controlled-items.md`, `change-impact.md`, `verification.md`, and `ship.md`).
- The pull request, commit, or release that identifies the exact version.
- The gaps you accepted and the triggers for re-checking.

## Process

1. Name the known-good version and the decision it came from.
2. Write down what is included and what is left out.
3. Link the basis, ripple effects, run record, verification, ship decision, and any operating lessons.
4. Name the leftover risks you accepted and what would trigger a re-check.
5. Record what would force you to write a new known-good version.

## Outputs

- A `baseline.md` file, or a known-good section inside `ship.md`.
- The triggers that would force a new known-good version.
- The accepted gaps, each with an owner.
- A link to the lesson, if a lesson is what changed the version.

## Verification

- The version can be rebuilt exactly from the commit, pull request, release, or artifact.
- Everything under control is either included or clearly left out on purpose.
- The re-check triggers are easy to find.

## Escalation

- Stop if the record claims a version is accepted but the evidence is missing.
- Escalate when the version affects customers, regulated work, safety, security, procurement, or any outside-trust claim.

## Common Rationalizations

- "The merge commit is the baseline." The commit names the version; the record explains why it was accepted and what would change it.
- "We'll record the version later." Waiting lets things drift at the exact moment that matters.
- "Only release teams need this." Agent prompts, skills, and public claims drift too.

## Red Flags

- The record has no links to evidence.
- Things were quietly left out.
- There are no re-check triggers for dependencies, models, prompts, tools, or public claims.

## Prompt

Create or update the Nuclear-grade baseline record for this change.

Inputs:
- packet:
- baseline identity:
- included controlled items:
- excluded items/claims:
- verification evidence:
- OPEX / near-miss links:
- accepted gaps:

Return a baseline record. Include the version that is saved, the items it covers, the items it leaves out, links to the evidence, the gaps you have accepted, and what should trigger a re-check or a new baseline. Do not imply formal assurance or compliance.

## Source-lineage note

This skill is an original known-good-version workflow influenced by public configuration-management, lifecycle, release-readiness, and operating-lesson sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
