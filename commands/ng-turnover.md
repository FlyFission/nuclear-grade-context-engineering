# ng-turnover

## Purpose

Create a handoff record when work passes from one AI agent, reviewer, verifier, releaser, support person, or thread to the next. This is a portable command prompt.

## Use when

- Work is moving from one agent, person, role, or thread to another.
- A subagent or reviewer needs the current state, the authority, the open evidence, and the stop conditions.
- Release, incident, or lessons-from-operation (OPEX) work has an unfinished handoff.

## Do not use when

- The change record already holds the finished work, the evidence, and the decision.
- A tiny Quick change only needs a proof note.

## Inputs

- The path to the change record (the packet), the current phase, the work done, the work left, what has changed, the limits on authority, and the next owner.

## Prompt text

```text
Create a Nuclear-grade turnover record.

Inputs:
- packet:
- current phase:
- outgoing owner / role:
- incoming owner / role:
- last completed action:
- completed artifacts:
- changed conditions:
- remaining work:
- allowed files/commands/tools:
- forbidden files/commands/tools:
- proof still needed:
- stop or hold conditions:

Produce a short turnover record. Include the critical next action, the likely error, the control, the evidence, and a prompt for the incoming owner to confirm they have it and understand it before they act.
```

## Files created or modified

- `turnover.md`, or a turnover section inside a context pack.
- Related packet records, if what has changed affects the risk, the verification, the decision, or the baseline.

## Expected outputs

- The current state, the point to resume from, what has changed, the work left, the authority, and the stop conditions.
- A prompt for the incoming owner to confirm.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- The handoff leaves out what has changed or the last action completed.
- The incoming owner acts before restating the scope and the stop rules.
- The turnover mixes new build work into the handoff.

## Legal/assurance boundary note

Turnover records keep the work continuous. They do not create formal V&V, compliance, certification, safety, security, procurement, or regulatory records, unless you separately adopt them under an external program.
