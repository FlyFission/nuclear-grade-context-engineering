---
name: self-checking-agent-actions
description: Checks a critical agent action against its exact target, expected result, and stop condition before and after execution. Use when an agent is about to make a critical edit, run a command or migration, use a credential or tool, change a dependency or model, make a public claim, or affect a release. Do not use for low-stakes reversible edits.
---

# Self-Checking Agent Actions

## Overview

Self-checking makes a cut-point action deliberate: identify the target, expected result, stop condition, action, and after-action check before claiming success.

## When to Use

- A command can delete, move, publish, release, migrate, or affect external state.
- An edit touches public claims, source lineage, permissions, credentials, dependencies, models, APIs, or release posture.
- An agent is about to make a broad or repetitive change where wrong-target work is plausible.
- A fast candidate is about to become a public claim, accepted baseline, or release action.

## When Not to Use

- The task is a tiny local edit with obvious proof.
- The action is read-only and has no downstream decision impact.
- The packet already requires a stronger human gate before action.

## Inputs

- Intended action, exact target, current phase, and authority source.
- Expected result, likely wrong-target failure, and stop condition.
- Proof command, review check, or evidence link needed after action.

## Process

1. Stop at the cut point and name the exact action and target.
2. Think through expected result, likely error, and what would make the action invalid.
3. Act only inside the named authority boundary.
4. Review actual result against expected result before making claims.
5. Record mismatch, gap, or escalation instead of retrying blindly.

## Outputs

- Compact self-check note or `self-check.md`.
- Action, target, expected result, stop condition, actual result, and evidence.
- Escalation note when the result does not match.

## Verification

- The action target is exact enough to prevent wrong-file or wrong-environment work.
- The expected result is named before the action.
- The after-action check compares evidence with expectation.

## Escalation

- Pause if authority, target, expected result, or evidence is unclear.
- Escalate when the action affects credentials, network effects, data, releases, public trust, or irreversible state.

## Common Rationalizations

- "It is only one command." Single commands can do broad damage.
- "The target is obvious." Wrong-target errors come from assumed targets.
- "I can inspect after." Inspection only helps if expected result was named first.

## Red Flags

- Action starts before target is named.
- Expected result is missing or vague.
- A mismatch is treated as a reason to retry instead of pause.
- Public wording claims safe, secure, approved, or compliant without scoped evidence.

## Source-lineage note

This skill is an original software-workflow translation of self-checking, pause when unsure, flagging, procedure adherence, and verification practices from DOE-HDBK-1028-2009 as public source lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
