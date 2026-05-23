# Controlled Items

**Purpose:** Help teams decide what must be controlled before AI-assisted work changes it.

## Rule

Control the item when its state affects trust, reviewability, reproducibility, authority, release posture, or public claims.

## Common item types

| Type | Examples | Why control it |
|---|---|---|
| Code/tests | source files, fixtures, evals | Behavior and proof can drift. |
| Agent context | prompts, skills, command cards, context packs | Agent authority and behavior depend on them. |
| Dependencies | packages, APIs, SaaS, models, data sources | Trust decisions need revalidation triggers. |
| Release state | changelog, tags, CI, artifacts, runbooks | Users receive this state. |
| Public claims | README, docs, source-map rows, disclaimers | Overclaims create trust and legal risk. |

## Exit criteria

Each controlled item has an owner, current state link, basis link, verification link or gap, and revalidation trigger.

## Source-lineage note

This controlled-item guide is an original workflow artifact inspired by public configuration-management and software assurance sources mapped in `../00-standards-foundation/source-map.md`.
