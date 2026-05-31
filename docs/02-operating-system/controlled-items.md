# Controlled Items

**Purpose:** This file helps teams decide what must stay under control before AI-assisted work changes it.

## Rule

Keep an item under control when its state affects trust, how easy it is to review, whether you can reproduce it, who is allowed to do what, release posture, or public claims.

## Common item types

| Type | Examples | Why control it |
|---|---|---|
| Code/tests | source files, fixtures, evals | Behavior and proof can drift. |
| Agent context | prompts, skills, command cards, context packs | Agent authority and behavior depend on them. |
| Dependencies | packages, APIs, SaaS, models, data sources | Trust decisions need re-check triggers. |
| Release state | changelog, tags, CI, artifacts, runbooks | Users receive this state. |
| Public claims | README, docs, source-map rows, disclaimers | Claiming too much creates trust and legal risk. |

## Exit criteria

Each controlled item has an owner, a link to its current state, a link to its basis, a verification link or a marked gap, and a trigger for when to check it again.

## Source-lineage note

This controlled-item guide is an original workflow piece. It draws on public sources about keeping the approved version of everything under control and software assurance, mapped in `../00-standards-foundation/source-map.md`.
