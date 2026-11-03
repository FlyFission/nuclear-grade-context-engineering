---
name: double-checking-before-acting
description: Checks a critical action against its exact target, expected result, and stop condition before and after it runs, and, when the action is irreversible or needs a reviewer's clearance, declares intent first with a falsifying signal, abort criteria, and a verified rollback. Use before a risky command, migration, deploy, credential or dependency change, public claim, or release. Do not use for low-stakes reversible edits.
---

# Double-Checking Before Acting

## Overview

A self-check turns a high-stakes action into a careful one. Before you act, name the target, the result you expect, and when to stop. After you act, compare. When the action cannot be undone, or someone else must be able to stop it, go one step further: declare your intent and reasoning first, so a reviewer can challenge the thinking before the action, not the wreckage after. A stated intent is a proposal to review. It is never evidence that the agent understood.

## Decision contract

- **Claim checked:** target, expected result, and stop condition were named before the action and compared after it; for an irreversible or reviewer-gated action, a declared intent also named a falsifying signal, abort criteria, and a verified rollback.
- **Artifact observed:** the action, target, and authority -> a `self-check.md` note, plus an `intent.md` declaration when the second depth applies.
- **Decision affected:** block -- whether the critical action proceeds, pauses, or aborts.
- **Failure class:** wrong-target-or-unverified-action, or unfalsifiable-intent (no falsifying signal, abort threshold, or verified rollback).
- **Next action:** pause and escalate when authority, target, evidence, or rollback is unclear; a mismatch halts the action rather than triggering a retry.

## When to Use

- A command can delete, move, publish, release, migrate, deploy, or change something outside the repo.
- An edit touches public claims, permissions, credentials, dependencies, models, APIs, or the release.
- An agent is about to make a wide or repeated change where hitting the wrong target is easy.
- Standing authority lets an agent proceed unless told no, and the team needs the "no" window.

## When Not to Use

- A tiny local edit with obvious proof, or an action that only reads data.
- An incident is live and the next move is stabilization (use `responding-to-incidents`).
- The record already requires a stronger human gate before this action (use `deciding-who-decides` to place it).

## Inputs

- The action, the exact target, and where your authority comes from.
- The expected result, the most likely wrong-target mistake, and the stop condition.
- For the second depth: the reasoning and precondition evidence, abort criteria, rollback, and who may stop the action.

## Process

Every critical action (depth 1, self-check):

1. Stop after choosing the action and before committing it. Name the exact action and target.
2. State the expected result, the likely error, and what would make the action wrong.
3. Act only inside the authority you were given.
4. Compare the real result with the expected one before claiming success. Record any mismatch and pause; do not retry blindly.
5. For a trust-bearing action, get a forceful backup from someone who can fail differently: a person, a different mechanism, or a fresh context. A second pass by the same agent in the same context is not independent.

Irreversible, or a reviewer must be able to stop it (depth 2, declared intent), before step 3:

6. Write "I intend to <action> on <target> because <evidence>."
7. Name the signals that would prove the expected result wrong, not just what success looks like.
8. State abort criteria in numbers where possible, and confirm the rollback has actually been tested.
9. Name who may stop the action, by when, and the backup watcher. Prove the preconditions rather than assert them. Act only after the review window.

## Outputs

- A self-check note or `self-check.md`: action, target, expected and real result, stop condition, evidence.
- At depth 2, an `intent.md`: intent sentence, falsifying signals, abort criteria, verified rollback, decision rights, backup.
- A mismatch routed to a pause, `responding-to-incidents`, or a deficiency entry (`learning-from-experience`).

## Verification

- The target was exact enough to rule out the wrong file or environment, and the expected result was named before the action.
- The after-action check compared evidence against expectation.
- At depth 2, the falsifying signal and abort criteria are concrete and the rollback was checked.

## Escalation

- Pause if the authority, target, expected result, or evidence is unclear. Halting unsafe work is protected.
- Stop when no rollback exists or the abort criteria cannot be measured.
- Get a second reviewer when the action is irreversible and only one person has seen the reasoning.

## Common Rationalizations

- "It is only one command." A single command can do wide damage.
- "I can check after." Checking after only helps if you named the expected result first.
- "I declared intent, so I am cleared." A declaration invites challenge; it is not its own approval.
- "Rollback is probably fine." An unverified rollback is a gap, not a plan.

## Red Flags

- The action starts before the target is named, or the expected result is vague.
- A mismatch is treated as a reason to retry instead of to pause.
- An intent with no falsifying signal, preconditions asserted with no link, or a zero review window.
- A reviewer approves the result without having seen the reasoning.

## Prompt

```text
Double-check this action the Nuclear-grade way.

Inputs:
- intended action and exact target:
- authority source:
- expected result and likely wrong-target error:
- stop condition and after-action check:
- irreversible, or must a reviewer be able to stop it? (yes/no)
- if yes: reasoning and precondition evidence, abort criteria, rollback (verified?), who may stop it and by when

Return:
- the action, target, expected result, stop condition, and after-action evidence
- if irreversible or reviewer-gated: "I intend to <action> on <target> because <evidence>", the falsifying signals, abort criteria, verified rollback, and decision rights
- go ahead, pause, or ask for help; after acting, actual vs expected and any gap

Treat a stated intent as a proposal to review, not proof of understanding. Do not imply certification or formal assurance.
```

## Source-lineage note

An original software-workflow translation of self-checking, pause when unsure, deliberate action, and three-way communication from DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md`. The "I intend to" construct is concept inspiration from intent-based leadership only, paraphrased and not template lineage (see `docs/00-standards-foundation/do-not-cite-directly.md`). It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
