---
name: declaring-intent
description: States what an agent intends to do and why before a critical or irreversible action, so a reviewer can challenge the thinking and not just the result. Use before deploys, migrations, public claims, or trust changes that deserve a stated intent, expected result, abort criteria, and backup. Do not use for routine reversible edits, and never treat the stated intent as proof the agent understood.
---

# Declaring Intent

## Overview

Before a critical action, say what you intend to do and the reasoning behind it, then act unless someone stops you. The value is that a reviewer can challenge the thinking before the action happens, not the wreckage after. The declaration also forces the actor to make the "why" and the "how will I know" explicit. For an agent, the stated intent is a proposal to be reviewed, never evidence that the agent actually understood.

## Decision contract

- **Claim checked:** the declared intent names a falsifying signal (not just success), carries concrete abort criteria and a checked rollback, and the preconditions are proven rather than assumed before the action runs.
- **Artifact observed:** the intended action and target, the reasoning and precondition evidence, the expected result, and the abort/rollback criteria -> an intent declaration or `intent.md` (action, reasoning, expected result, abort, rollback, decision rights, backup) and the actual-vs-expected result.
- **Decision affected:** block -- whether a reviewer clears the critical or irreversible action before it runs, given expected result, abort criteria, and rollback.
- **Failure class:** unfalsifiable-intent (a stated goal with no falsifying signal, abort threshold, or verified rollback).
- **Next action:** stop when no rollback exists or abort criteria are unmeasurable; get a second reviewer when only one has seen the reasoning.

## When to Use

- Before a deploy, migration, data change, public claim, dependency or model swap, or release.
- When an action is hard to reverse, or its blast radius is more than the immediate file.
- When you want a reviewer's eyes on the reasoning and the abort criteria before execution.
- When standing authority lets an agent proceed unless told no, and the team needs the "no" window.

## When Not to Use

- The action is a routine, reversible edit with obvious proof and no trust boundary.
- An incident is live and the next move is stabilization, not a fresh proposal.
- Someone wants the declaration treated as a guarantee or certification.

## Inputs

- The intended action and the exact target.
- The reasoning and the evidence that says the preconditions are met.
- The expected result, and the signals that would mean it went wrong.
- The abort and rollback criteria, the decision rights, and who is backing up the action.

## Process

1. Write the intent as "I intend to <action> on <target> because <evidence/reasoning>."
2. State the expected result and the precise signals that would falsify it.
3. State the abort criteria and the verified rollback, in numbers where possible.
4. Name who may stop the action, by when, and who is the backup watcher.
5. Confirm the preconditions are actually proven, not assumed, before you proceed.
6. Act only after the review window; then record the actual result against the expected one.

## Outputs

- An intent declaration, or an `intent.md` record, with action, reasoning, expected result, abort criteria, rollback, decision rights, and backup.
- The actual result compared to the expected result after the action.
- Any mismatch routed to a pause, an incident, or a deficiency entry.

## Verification

- The declaration names what would prove it wrong, not just what success looks like.
- Abort and rollback criteria are concrete and the rollback has been checked.
- The actual result is compared to the expected result and the gap is recorded.

## Escalation

- Escalate when the preconditions cannot be shown to be true before acting.
- Stop when no rollback exists or the abort criteria cannot be measured.
- Get a second reviewer when the action is irreversible and only one person has seen the reasoning.

## Common Rationalizations

- "I said what I intend, so I am cleared to go." Declaration invites a challenge; it is not its own approval.
- "The agent's intent reads confidently." Confident wording is not understanding or evidence.
- "Rollback is probably fine." An unverified rollback is a gap, not a plan.
- "Abort criteria are obvious." If they are not written and measurable, they will not be obeyed under pressure.

## Red Flags

- The intent states the goal but no falsifying signal or abort threshold.
- Preconditions are asserted ("checks passed") with no link to the evidence.
- The review window is zero because the work felt urgent.
- A reviewer approves the result without ever seeing the reasoning.

## Prompt

```text
Declare intent before this action the Nuclear-grade way.

Inputs:
- intended action and target:
- reasoning / evidence preconditions are met:
- expected result:
- abort criteria (numbers where possible):
- rollback (and is it verified?):
- who may stop it, by when / backup watcher:

Return:
- "I intend to <action> on <target> because <evidence/reasoning>"
- the expected result and the precise signals that would falsify it
- the abort criteria and the verified rollback
- the decision rights and the backup
- after acting: the actual result compared to the expected result, and any gap

State what would prove this wrong, not just what success looks like. Treat the stated intent as a proposal to review, not proof the agent understood. Do not imply certification or formal assurance.
```

## Source-lineage note

This skill is an original software-workflow translation of stating intent before acting. The "I intend to" construct and leader-leader idea are concept inspiration from intent-based leadership only — paraphrased, not template lineage (a copyrighted source; see `docs/00-standards-foundation/do-not-cite-directly.md`). Its public idea lineage is the deliberate-action, self-checking, and three-way-communication habits in DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
