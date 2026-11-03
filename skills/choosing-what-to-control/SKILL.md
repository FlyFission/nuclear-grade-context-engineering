---
name: choosing-what-to-control
description: Decides which code, prompts, models, tools, dependencies, docs, tests, evals, releases, or claims need their approved state tracked. Use when scoping what a change puts at risk or what must stay reviewable. Do not use for scratch work that nothing else depends on.
---

# Choosing What to Control

## Overview

Controlled items are the parts of a system whose approved version matters. They matter to trust, to review, to being able to repeat a result, to what an agent may do, or to a release. This skill keeps the approved version of those items under control. Engineers call that keeping the approved version under control, or configuration management (CM).

## Decision contract

- **Claim checked:** every item whose approved state affects trust, agent power, the release, repeatability, or public understanding is named -- with owner, current and intended state, an evidence link or stated gap, and a re-check trigger -- and nothing in scope is silently left uncontrolled.
- **Artifact observed:** the request/diff/record and `controlled-items.md` (plus any `risk.md`, `basis.md`, `plan.md`) -> the controlled-item list with owners, states, triggers, and named gaps.
- **Decision affected:** warn -- which code, prompts, models, dependencies, docs, and releases become controlled items (feeds `change-impact.md` and the baseline).
- **Failure class:** uncontrolled-item (drift in an unlisted prompt, doc, or agent-power state left untracked).
- **Next action:** name the item, owner, and re-check trigger; escalate when drift could hit users, security, releases, or agent power.

## When to Use

- A change touches prompts, models, tools, dependencies, public docs, checkers, templates, skills, commands, release files, or runbooks.
- A reviewer needs to know which state is approved and which kind of drift would matter.
- Agent power or wording about where ideas came from changes.
- Work could hit the wrong target, so the exact item needs to be named before anyone acts.

## When Not to Use

- The change is local, easy to undo, and holds no state that carries trust.
- The item is already listed in a fresh `controlled-items.md` and the scope has not changed.

## Inputs

- The user request, issue, pull request, diff, or change record.
- `docs/02-operating-system/controlled-items.md`.
- Any existing `risk.md`, `basis.md`, and `plan.md`.

## Process

1. List the files, prompts, models, dependencies, tools, data sources, docs, tests, evals, release files, and claims the change affects.
2. Keep only the items whose state affects trust, agent power, the release, repeatability, or what the public understands.
3. Flag the exact item, its owner, and the boundaries that must not be touched.
4. For each item, record its current state, its intended state, its owner, a link to evidence, and the trigger to re-check it.
5. Move up to `change-impact.md` when several kinds of artifacts could go stale.

## Outputs

- A controlled-item list, or `controlled-items.md`.
- The exact target and the do-not-touch boundaries, when needed.
- Triggers to re-check each item.
- Named gaps for items that need a saved-version step later.

## Verification

- Each controlled item has a reason it is controlled.
- Each item links to evidence or to a stated gap.
- A reviewer can tell which items are in and which are out.

## Escalation

- Escalate when drift in an uncontrolled item could affect users, data, security, releases, where ideas came from, or what an agent may do.
- Stop if the list turns into a whole-repo inventory instead of a list tied to this change.

## Common Rationalizations

- "Git tracks everything." Git tracks the bytes. Keeping the approved version under control records which state is approved and when to re-check it.
- "It is only a prompt or a doc." Prompts and docs can change how an agent behaves and how the public trusts you.
- "We can work out the affected items from the diff." Future reviewers need the intent, not just the changed paths.

## Red Flags

- No owner, or no trigger to re-check.
- Public claims change but stay uncontrolled.
- Agent tool power changes, but no controlled item records the new permission state.

## Prompt

List the items this change must keep under control (CM).

Inputs:
- change:
- packet:
- affected files/items:

Return a short table. For each item, give: the item, its type, its current state, its intended state, why it is controlled, a link to its evidence (or the gap), its owner, and what should trigger a re-check. Do not list unrelated repo files. Do not imply formal assurance or compliance.

## Source-lineage note

This skill is an original workflow for keeping approved versions under control. It draws on public configuration-management and software-assurance sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
