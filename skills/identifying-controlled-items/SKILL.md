---
name: identifying-controlled-items
description: Use when deciding which code, prompts, models, tools, dependencies, docs, tests, evals, releases, or claims need controlled-state tracking.
---

# Identifying Controlled Items

## Overview

Controlled items are the parts of a software system whose approved state matters to trust, reviewability, reproducibility, agent authority, or release posture.

## When to Use

- A change touches prompts, models, tools, dependencies, public docs, validators, templates, skills, commands, release artifacts, or runbooks.
- A reviewer needs to know what state is approved and what drift would matter.
- Agent authority or source-lineage wording changes.
- Wrong-target work is plausible and exact item identity needs flagging before action.

## When Not to Use

- The change is a local, reversible Quick change with no trust-bearing state.
- The item is already listed in a fresh `controlled-items.md` and scope has not changed.

## Inputs

- User request, issue, PR, diff, or packet.
- `docs/02-operating-system/controlled-items.md`.
- Existing `risk.md`, `basis.md`, and `plan.md`.

## Process

1. List affected files, prompts, models, dependencies, tools, data sources, docs, tests, evals, release artifacts, and claims.
2. Keep only items whose state affects trust, authority, release posture, reproducibility, or public understanding.
3. Flag exact item identity, owner, and do-not-touch boundaries.
4. Record current state, intended state, owner, evidence link, and revalidation trigger.
5. Escalate to `change-impact.md` when multiple artifact families may become stale.

## Outputs

- Controlled item list or `controlled-items.md`.
- Exact target identity and do-not-touch boundaries when needed.
- Revalidation triggers.
- Named gaps for items that need later baseline work.

## Verification

- Each controlled item has a reason for control.
- Each item links to evidence or an explicit gap.
- Reviewers can tell which items are included and excluded.

## Escalation

- Escalate when uncontrolled drift could affect users, data, security, releases, source-lineage, or agent authority.
- Stop if the list becomes a whole-repo inventory instead of a change-specific control list.

## Common Rationalizations

- "Git tracks everything." Git tracks bytes; CM records approved state and revalidation triggers.
- "It is only a prompt/doc." Prompts and docs can change agent behavior and public trust.
- "We can infer affected items from the diff." Future reviewers need intent, not just changed paths.

## Red Flags

- No owner or revalidation trigger.
- Public claims change without being controlled.
- Agent tool authority changes but no controlled item records the permission state.

## Source-lineage note

This skill is an original controlled-configuration workflow influenced by public configuration-management and software assurance sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
