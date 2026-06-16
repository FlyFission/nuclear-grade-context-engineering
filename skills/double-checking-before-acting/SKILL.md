---
name: double-checking-before-acting
description: Checks a critical agent action against its exact target, expected result, and stop condition before and after execution. Use when an agent is about to make a critical edit, run a command or migration, use a credential or tool, change a dependency or model, make a public claim, or affect a release. Do not use for low-stakes reversible edits.
---

# Double-Checking Before Acting

## Overview

A self-check turns a high-stakes action into a careful one. Before you claim success, name the target, the result you expect, when to stop, the action itself, and the check you will run afterward.

## Decision contract

- **Claim checked:** the target, expected result, and stop condition were named before the action, and the real result was compared against the expected one before claiming success.
- **Artifact observed:** the proposed action, target, and authority -> a `self-check.md` note of action, target, expected/real result, stop condition, evidence, and any mismatch.
- **Decision affected:** block -- whether to proceed with or abort the critical action: a big edit, command, public claim, trust change, or release.
- **Failure class:** wrong-target-or-unverified-action (acting on an assumed target, or claiming success without comparing the result).
- **Next action:** pause and escalate when authority, target, or evidence is unclear; a mismatch halts the action rather than triggering a retry.

## When to Use

- A command can delete, move, publish, release, migrate, or change something outside the repo.
- An edit touches public claims, where ideas came from, permissions, credentials, dependencies, models, APIs, or the release.
- An agent is about to make a wide or repeated change, where hitting the wrong target is easy.
- A quick candidate is about to become a public claim, an accepted version, or a release action.

## When Not to Use

- The task is a tiny local edit with obvious proof.
- The action only reads data and has no effect on any later decision.
- The change record already requires a stronger human check before the action.

## Inputs

- The action you mean to take, the exact target, the current phase, and where your authority comes from.
- The result you expect, the most likely wrong-target mistake, and when to stop.
- The proof command, review check, or evidence link you will need after the action.

## Process

1. Stop at the key moment and name the exact action and target.
2. Think through the result you expect, the likely error, and what would make the action wrong.
3. Act only inside the authority you were given.
4. Compare the real result against the result you expected, before you make any claim.
5. For trust-bearing actions, get a forceful backup — an independent person, or a different model or context — to check the action. A second pass by the same agent in the same context inherits the same blind spots and is not independent.
6. Record any mismatch, gap, or escalation. Do not just retry blindly.

## Outputs

- A short self-check note, or a `self-check.md` file.
- The action, target, expected result, stop condition, real result, and evidence.
- An escalation note when the result does not match.

## Verification

- The target is exact enough to rule out work on the wrong file or the wrong environment.
- The expected result is named before the action.
- The after-action check compares the evidence against what you expected.

## Escalation

- Pause if the authority, the target, the expected result, or the evidence is unclear.
- Halt the action if it is unsafe or unclear, regardless of seniority; surfacing the concern is protected, not punished.
- Escalate when the action affects credentials, network effects, data, releases, public trust, or anything that cannot be undone.

## Common Rationalizations

- "It is only one command." A single command can do wide damage.
- "The target is obvious." Wrong-target mistakes come from assumed targets.
- "I can check after." Checking after only helps if you named the expected result first.

## Red Flags

- The action starts before the target is named.
- The expected result is missing or vague.
- A mismatch is treated as a reason to retry instead of a reason to pause.
- Public wording claims safe, secure, approved, or compliant with no scoped evidence behind it.

## Prompt

```text
Self-check this Nuclear-grade agent action before it happens.

Inputs:
- packet:
- current phase:
- intended action:
- exact target:
- authority source:
- expected result:
- likely wrong-target or wrong-state error:
- stop condition:
- proof or after-action check:

Return:
- the risky point being checked;
- the action and the target;
- the expected result;
- the stop condition;
- the evidence to collect after the action;
- whether to go ahead, pause, or ask for help.
```

## Source-lineage note

This skill is an original software-workflow translation of self-checking, pause when unsure, flagging, procedure adherence, and verification practices from DOE-HDBK-1028-2009 as public source lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
