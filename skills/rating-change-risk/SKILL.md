---
name: rating-change-risk
description: Picks Quick, Standard, or a stronger human-reviewed mode based on consequence, how easy it is to undo, and how much is unknown. Use when you start a change to code, docs, dependencies, AI power, releases, or public claims and the right level of care is unclear. Do not use for a tiny easy-to-undo edit with obvious proof, which is Quick by default, or for a purely administrative reversible edit crossing no trust boundary, which needs no packet at all.
---

# Rating Change Risk

## Overview

Sort the change before you build it. That way the care you take matches the stakes and the evidence the change needs. The result is a mode choice, tied to the decision question, what the change must prove, and the triggers to escalate. Choosing the mode is how Nuclear-grade *tailors* rigor to stakes — the same idea project-management practice calls tailoring; see `docs/02-operating-system/risk-tiers-and-modes.md`. Mode is about how much rigor; it is orthogonal to the work type (greenfield, brownfield, defect-fix, or refactor-migration), which is classified upstream in `questioning-attitude` and shapes which questions you ask. See `docs/02-operating-system/work-type-lens.md`.

## Decision contract

- **Claim checked:** the chosen mode matches the stakes -- Quick only for local, easy-to-undo, easy-to-prove work that adds no new trust boundary, and Standard or stronger once consequence, exposure, reversibility, detectability, unknowns, or agent power cross the line -- and the proof that mode owes is named.
- **Artifact observed:** the request/diff, the files/dependencies/credentials/APIs/users touched, `activation-thresholds.md`, and any prior `risk.md` -> the mode, decision question, evidence bar, required files, proof command or gap, and escalation triggers in `risk.md`.
- **Decision affected:** block -- the mode (Quick / Standard / stronger) and the evidence obligation that mode sets.
- **Failure class:** underrated-mode (a mode picked from effort, not stakes, weaker than the obvious consequence).
- **Next action:** raise the mode to fit the stakes; escalate when money, sensitive data, irreversible actions, autonomous tools, or release readiness are involved.

## When to Use

- A change request is new, vague, or has grown.
- You know the decision question, but the evidence bar is unclear.
- A pull request has AI-generated code, tests, docs, prompts, or release files.
- Reviewers disagree on whether Quick evidence is enough.
- The work is routine, by-the-book, new, interrupted, resumed, handed off, or high stakes, and you need the right habit to control it.

## When Not to Use

- A change record already has a fresh mode choice and the scope has not changed.
- The system is failing right now and needs incident handling first.
- The change is purely administrative, instantly reversible, and crosses no trust boundary -- that is the administrative floor (no packet; the commit message is the record), not a mode to rate.

## Inputs

- The user request, issue, pull request, or diff.
- The files, dependencies, prompts, data, credentials, APIs, release files, and users the change affects.
- `docs/02-operating-system/activation-thresholds.md`.
- The change record's `risk.md`, if one exists.

## Process

**Screen for the administrative floor first.** If the change is purely administrative, instantly reversible, and crosses no trust boundary -- a typo, a comment, formatting, a dead-link fix, a doc-only bump -- it needs no packet; the commit message is the record. Any tripwire (auth, data, a dependency, a model or prompt, agent authority, CI or `.github/`, a release, a baseline, or claim-bearing public wording -- a non-claim typo or dead-link fix in public docs does not by itself count), or a reviewer needing more than the commit, makes it at least Quick. When in doubt it is Quick, not the floor.

1. Restate the decision question and the evidence bar it needs. Grade the change itself, not the standing item it touches -- a routine file can receive a high-stakes change (auth, payments, an irreversible migration); take the higher of the two.
2. Judge the dominant three first -- consequence, how easy it is to undo, and how much is unknown -- then pull in who is exposed, how easily a failure would be caught, dependency trust, and how much power the agent has only if one of the three is unclear or a trap surface fires. Weigh them together: an easy-to-undo, known-pattern change is not high-rigor even at high consequence. Raise the mode when the affected component carries a live deficiency, a recent incident, or recurring escaped defects -- past performance is part of the stakes. Derive the grade in two directions so it is defensible, not asserted from effort: top-down (the worst credible outcome this could cause) and bottom-up (if this specific edit fails, what breaks).
3. Name the work mode: routine, known procedure, new or uncertain, interrupted or resumed, or a critical action.
4. Choose Quick only for local, easy-to-undo, easy-to-prove work that adds no new trust boundary.
5. Choose Standard when the change is user-visible or lasting, or touches dependencies, permissions, data, AI, operations, or a release.
6. Mark Nuclear, Incident, Research Board, or Release as human-reviewed patterns when they apply.
7. Record the triggers to escalate and the least proof required; when the tier is genuinely unclear, raise it -- over-grading costs minutes, under-grading can cost the release.

## Outputs

- The chosen mode.
- The decision question and the evidence bar.
- The reason for the mode.
- The change-record files required.
- The proof command, or the evidence gap.
- A suggested habit to control the work: self-check, handoff, briefing pack, a second independent check, lessons from operation (OPEX), or a trust check.
- The triggers to escalate.

## Verification

- `risk.md` names the mode, scope, consequence, how easy it is to undo, who is exposed, what is unknown, and the proof required.
- Quick and Standard records pass `python tools/ng.py validate .nuclear/changes/<slug>` after the required files are filled.

## Escalation

- Escalate when the change affects money, sensitive data, security, outside trust, actions that cannot be undone, autonomous tools, or release readiness.
- Stop when the requested mode is weaker than the obvious stakes.

## Common Rationalizations

- "It is small." Small code can change a large trust boundary.
- "The agent only changed docs." Docs can make public claims.
- "We can fix it later." Failures that are hard to catch or hard to undo need a stronger mode now.
- "It is administrative, so the floor covers it." The floor holds only when every inclusion test passes and no tripwire fires; a trust boundary, a dependency, or a public claim means it was never administrative.

## Red Flags

- The mode was picked from how much effort it takes, not from the stakes.
- No rollback or restore path is named for release-facing work.
- The agent's tool power is broader than the change record shows.

## Prompt

```text
Sort this change into a Nuclear-grade mode.

Inputs:
- Request or diff: <paste/link>
- Affected files/assets: <list>
- Impact on users, security, dependencies, data, AI behavior, or release: <known facts>

Return:
- the decision question and the proof that must clear before work goes on
- the chosen mode: Quick, Standard, or a stronger mode that a human reviews
- how bad it is if wrong, how easy to undo, how exposed, how easy to catch, how uncertain
- the work mode and which safety habit (HPI) to use: none, context pack, handoff, self-check, an independent check, a record of lessons from real operation (OPEX), or a trust check
- the assumptions or facts that drove the mode choice
- the record files this mode needs
- the least proof required
- the conditions that should make you ask for help
- a limits note: do not claim formal verification and validation, compliance, certification, safety, security, or regulatory adequacy
```

## Source-lineage note

This skill is an original risk-scaling workflow. It draws on public sources mapped in `docs/00-standards-foundation/source-map.md`. It does not set any regulatory class and does not create compliance.
