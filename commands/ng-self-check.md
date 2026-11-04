---
description: "Checks a critical agent action against its exact target, expected result, and stop condition before and after execution."
disable-model-invocation: true
---

# ng-self-check

Portable command prompt generated from `skills/double-checking-before-acting/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- A command can delete, move, publish, release, migrate, or change something outside the repo.
- An edit touches public claims, where ideas came from, permissions, credentials, dependencies, models, APIs, or the release.
- An agent is about to make a wide or repeated change, where hitting the wrong target is easy.
- A quick candidate is about to become a public claim, an accepted version, or a release action.

## Do not use when

- The task is a tiny local edit with obvious proof.
- The action only reads data and has no effect on any later decision.
- The change record already requires a stronger human check before the action.

## Inputs

- The action you mean to take, the exact target, the current phase, and where your authority comes from.
- The result you expect, the most likely wrong-target mistake, and when to stop.
- The proof command, review check, or evidence link you will need after the action.

## Prompt text

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

## Verification

- The target is exact enough to rule out work on the wrong file or the wrong environment.
- The expected result is named before the action.
- The after-action check compares the evidence against what you expected.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/double-checking-before-acting/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
