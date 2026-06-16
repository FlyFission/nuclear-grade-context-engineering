---
name: checking-what-a-change-affects
description: Screens what a controlled change might leave out of date across docs, tests, skills, commands, templates, checkers, prompts, releases, saved versions, and evidence, and names the triggers to re-check. Use when a change touches a controlled item. Do not use for a single edit that nothing else depends on.
---

# Checking What a Change Affects

## Overview

An impact screen asks a simple question. When a controlled item changes, what else does that change leave out of date? You look downstream for ripple effects before they surprise you.

## Decision contract

- **Claim checked:** every artifact a controlled change could leave stale -- docs, tests, checkers, skills, commands, templates, prompts, releases, saved versions, and runtime blast radius (schema/state migration, API consumers, backward-compatibility, rollback-of-state) -- has one named action with evidence, and no stale surface is quietly accepted.
- **Artifact observed:** the controlled-item list, `risk.md`, `basis.md`, `plan.md`, the diff, and `change-impact.md` -> `change-impact.md` with per-item actions, re-check triggers, and required follow-ups.
- **Decision affected:** block -- per affected item, update / leave alone / defer / block; blockers carry into `ship.md`.
- **Failure class:** missed-ripple (a stale doc, test, checker, or runtime contract quietly accepted).
- **Next action:** assign each stale surface an action with an owner and trigger; escalate when it touches outside trust, security, or the release.

## When to Use

- A change affects more than one kind of artifact.
- A change touches a running system, a schema, stored data, or an API other code depends on (brownfield or migration work).
- Public claims, where ideas came from, checkers, tests, templates, skills, commands, dependencies, prompts, or the release may need updates.
- A saved version or a re-check trigger may change.
- A near miss, a weak control, or a lesson from real operation (OPEX) hints at hidden ripple effects.

## When Not to Use

- The change is clearly Quick. It affects one local item and needs one proof step.
- A current `change-impact.md` already covers the exact scope.

## Inputs

- The controlled-item list.
- `risk.md`, `basis.md`, `plan.md`, and the diff.
- `docs/02-operating-system/change-impact.md`.

## Process

1. Name the kinds of artifacts the change might affect. When the change touches a running system or stored data, screen the runtime blast radius too — schema and state migration, API consumers that depend on the contract, backward-compatibility, and rollback-of-state — not just repo artifacts. See `docs/02-operating-system/change-impact.md`.
2. For each kind, pick one action: update it, leave it alone, defer it, or block on it.
3. Name the stale links, evidence, examples, claims, handoffs, or controls.
4. Link evidence for each choice.
5. Record the triggers to re-check.
6. Carry any blockers or accepted gaps into `ship.md`.

## Outputs

- `change-impact.md`, or a short impact screen.
- Triggers to re-check.
- The follow-up updates that are required.

## Verification

- No stale public claim, test, checker, skill, command, template, or release record is quietly accepted.
- Deferred ripple effects have owners and triggers.
- Blocking ripple effects show up in the release posture.

## Escalation

- Escalate when a change affects outside trust, security, data, the release, or public assurance wording.
- Stop if you cannot tell the impact from the context you have.

## Common Rationalizations

- "The diff is small." Small changes can break docs, tests, or public claims.
- "The README can lag." Public docs are controlled surfaces that carry trust.
- "Checker updates can wait." If docs claim a behavior, drift in the check matters now.
- "The near miss is fixed." The control that let it happen may still be stale.

## Red Flags

- Lifecycle wording changed, but skills, commands, and templates did not.
- A template's shape changed, but the checker or tests did not.
- Evidence was deleted while change records still link to it.

## Prompt

Run a Nuclear-grade ripple-effect check.

Inputs:
- packet:
- controlled items:
- planned or actual diff:

For each family of files, decide one of: update, leave as is, defer, or block. Name the updates needed, the controls now stale, the evidence links, the owners, and what should trigger a re-check. Pay close attention to public claims, validator behavior, source-lineage notes, handoffs, trust checks, lessons from operation (OPEX), and the release. When the change touches a running system or stored data, also screen the runtime blast radius: schema and state migration, API consumers that depend on the contract, backward-compatibility, and rollback-of-state.

## Source-lineage note

This skill is an original impact-screen workflow. It draws on public configuration-management, lifecycle, secure-development, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
