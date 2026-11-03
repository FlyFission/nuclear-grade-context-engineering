---
name: controlling-approved-versions
description: Keeps the approved version of what matters under control at both ends of a change - when scoping, names which code, prompts, models, tools, dependencies, docs, evals, or claims have an approved state worth tracking; when the change is accepted, records that known-good version, its evidence, and what would make it out of date. Do not use for scratch work nothing depends on, or while work is still under review.
---

# Controlling Approved Versions

## Overview

Some parts of a system have an approved version that matters: to trust, to review, to repeating a result, to what an agent may do, or to a release. Engineers call keeping that version under control configuration management (CM). It happens at two moments. At the start of a change, name which items are controlled, so drift in them is noticed. When the change is accepted, record the known-good version (the baseline), the evidence behind it, and what would make that record stale. Do the part that matches where you are.

## Decision contract

- **Claim checked:** every item whose approved state affects trust, agent power, the release, repeatability, or public understanding is named with owner, state, evidence or gap, and re-check trigger; and an accepted version can be rebuilt exactly, with scope included or deliberately excluded and its invalidation triggers recorded.
- **Artifact observed:** the request, diff, or record -> `controlled-items.md` at scoping; `controlled-items.md`, `change-impact.md`, `verification.md`, `ship.md`, and the identifying commit or release -> `baseline.md` at acceptance.
- **Decision affected:** warn -- which items become controlled, and the accepted baseline plus the triggers that invalidate it.
- **Failure class:** uncontrolled-item, or unrebuildable-baseline (missing evidence or silently dropped scope).
- **Next action:** name the missing item, owner, link, or excluded scope as a gap; escalate when drift or the version affects users, security, releases, regulated work, or agent power.

## When to Use

- **Scoping:** a change touches prompts, models, tools, dependencies, public docs, checkers, templates, skills, commands, release files, or agent power, and a reviewer needs to know which state is approved.
- **Accepting:** a Standard change ships, a controlled item is accepted, or a lesson forces a re-record of the known-good version.

## When Not to Use

- A local, easy-to-undo change with no state that carries trust and nothing to release.
- The item is already listed in a fresh `controlled-items.md` and the scope has not changed.
- The work is still under review and the evidence is not ready to record a baseline.
- Several kinds of artifacts could go stale and you need per-item update decisions (use `checking-what-a-change-affects`).

## Inputs

- The request, issue, diff, or change record, and `docs/02-operating-system/controlled-items.md`.
- At acceptance: the verification, ship decision, identifying commit, PR, or release, and the accepted gaps.

## Process

**At scoping (what is controlled):**

1. List the files, prompts, models, dependencies, tools, data sources, docs, tests, evals, release files, and claims the change affects.
2. Keep only items whose state affects trust, agent power, the release, repeatability, or what the public understands. Do not inventory the whole repo.
3. For each: current state, intended state, owner, evidence link or gap, re-check trigger, and do-not-touch boundaries when the target must be exact.

**At acceptance (the known-good version):**

4. Name the known-good version and the decision it came from, by commit, PR, release, or artifact.
5. Write what is included and what is deliberately left out; nothing in scope drops silently.
6. Link the basis, impact, verification, ship decision, and any lessons. Name the accepted residual risks with owners.
7. Record what would force a re-check or a new baseline: a dependency, model, prompt, tool, or public-claim change.

## Outputs

- At scoping: a controlled-item table or `controlled-items.md`, with named gaps for items that need a saved version later.
- At acceptance: `baseline.md` (or a known-good section in `ship.md`) with scope, evidence links, accepted gaps and owners, and re-record triggers.

## Verification

- Each controlled item has a reason, an owner, and an evidence link or stated gap.
- The accepted version can be rebuilt exactly from its identifier; excluded scope is visible.
- Re-check triggers are easy to find.

## Escalation

- Stop if a record claims a version is accepted but the evidence is missing, or the list grows into a whole-repo inventory.
- Escalate when drift or the version affects users, data, security, releases, regulated work, procurement, or agent power.

## Common Rationalizations

- "Git tracks everything." Git tracks bytes; CM records which state is approved and when to re-check it.
- "It is only a prompt or a doc." Prompts and docs change how agents behave and how the public trusts you.
- "The merge commit is the baseline." The commit names the version; the record says why it was accepted and what would change it.

## Red Flags

- A controlled item with no owner or no re-check trigger; agent tool power changed but no item records it.
- A baseline with no evidence links, or scope quietly left out.
- No re-check triggers for dependencies, models, prompts, tools, or public claims.

## Prompt

```text
Keep the approved version under control for this change.

Inputs:
- change and packet:
- stage: scoping / acceptance
- affected files and items (scoping):
- baseline identity, verification, ship decision, accepted gaps (acceptance):

Return, for scoping: a table of controlled items with type, current and intended state, why controlled, evidence or gap, owner, and re-check trigger. Do not list unrelated files.
Return, for acceptance: the known-good version, included and excluded items, evidence links, accepted gaps with owners, and the triggers for a re-check or new baseline.

Do not imply formal assurance or compliance.
```

## Source-lineage note

An original workflow for keeping approved versions under control and recording known-good versions, influenced by public configuration-management, lifecycle, release-readiness, and operating-lesson sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
