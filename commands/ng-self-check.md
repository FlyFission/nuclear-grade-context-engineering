# ng-self-check

## Purpose

Run a compact self-check before and after a critical cut-point agent action. This is a portable command prompt.

## Use when

- An edit, command, tool call, credential use, public claim, dependency/model/API change, migration, or release action could affect controlled state.
- Wrong target, wrong scope, or mismatched evidence is plausible.
- A fast candidate is about to become a public claim, accepted baseline, or release action.

## Do not use when

- The task is read-only or a tiny local Quick edit with obvious proof.
- A stronger human approval gate must occur before the action.

## Inputs

- Intended action, exact target, authority source, expected result, likely error, stop condition, and proof check.

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
- cut point being checked;
- action and target;
- expected result;
- stop condition;
- after-action evidence to collect;
- whether to proceed, pause, or escalate.
```

## Files created or modified

- `self-check.md` if activated.
- `verification.md`, `ship.md`, or `decision.md` if the self-check changes evidence or release posture.

## Expected outputs

- Proceed / pause / escalate decision.
- Cut point, action, target, expected result, stop condition, and evidence requirement.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Action begins before target and expected result are named.
- Mismatch leads to blind retry instead of pause.
- Public claim is treated as proven without scoped evidence.

## Legal/assurance boundary note

Self-check records support engineering review discipline. They do not create formal V&V, compliance, certification, safety, security, procurement, or regulatory approval.
