# ng-classify

## Purpose

Sort a change into the lightest mode that is still honest. First name the decision the change must settle. Then pick the mode. Then name the proof needed before work goes on. This is a portable command prompt.

## Use when

- A new change request arrives.
- A pull request (PR) has grown or shrunk in scope.
- Reviewers are unsure whether Quick proof is enough.
- The work is routine, by-the-book, new, interrupted, resumed, handed off, or important enough to need a safety habit. We call these safety habits HPI (Human Performance Improvement) — the habits borrowed from high-reliability work.

## Do not use when

- An incident is live and you must contain it first.
- The mode is already set and the scope has not changed.

## Inputs

- The user request, issue, PR, or code change (the diff).
- The files, dependencies, prompts, data, tools, credentials, and release items the change touches.
- The questioning-attitude screen or known assumptions, if you have them.
- `docs/02-operating-system/activation-thresholds.md`.

## Prompt text

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

## Files created or modified

- `.nuclear/changes/<slug>/risk.md`

## Expected outputs

- The chosen mode.
- The decision question and the proof gate.
- Why that mode was chosen.
- What the change must prove.
- Which safety habit (HPI) to use, when one applies.
- The conditions that should make you ask for help.

## Verification command

```bash
python tools/ng.py status .
```

## Failure modes

- Picking a mode by how much work it is, instead of how bad a mistake would be.
- Picking a mode before the decision question is clear.
- Ignoring how much power the AI has, whether a dependency can be trusted, how exposed the data is, or what the release touches.
- Picking Quick while reasons to go Standard are still unresolved.

## Legal/assurance boundary note

This prompt only helps you see the evidence. It does not create compliance, formal verification and validation, certification, safety, security, or regulatory adequacy.
