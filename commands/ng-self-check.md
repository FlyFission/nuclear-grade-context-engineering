# ng-self-check

## Purpose

Run a short self-check just before and just after a risky agent action — the kind that is hard to take back. This is a portable command prompt.

## Use when

- An edit, command, tool call, credential use, public claim, change to a dependency/model/API, migration, or release action could affect a version you keep under control.
- It is plausible the agent could hit the wrong target, the wrong scope, or mismatch the evidence.
- A fast draft is about to become a public claim, an accepted baseline, or a release action.

## Do not use when

- The task is read-only, or a tiny local Quick edit with obvious proof.
- A stronger human approval gate must happen before the action.

## Inputs

- The action you intend, the exact target, where the authority comes from, the result you expect, the likely error, the stop condition, and the proof check.

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

## Files created or modified

- `self-check.md` if started.
- `verification.md`, `ship.md`, or `decision.md` if the self-check changes the evidence or the release.

## Expected outputs

- A go-ahead / pause / ask-for-help decision.
- The risky point, the action, the target, the expected result, the stop condition, and the evidence required.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- The action starts before the target and the expected result are named.
- A mismatch leads to a blind retry instead of a pause.
- A public claim is treated as proven with no scoped evidence behind it.

## Legal/assurance boundary note

Self-check records support careful engineering review. They do not create formal V&V, compliance, certification, safety, security, procurement, or regulatory approval.
