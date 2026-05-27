# ng-turnover

## Purpose

Create a turnover record for AI-agent, reviewer, verifier, releaser, support, or resumed-thread work. This is a portable command prompt.

## Use when

- Work is moving from one agent, human, role, or thread to another.
- A subagent or reviewer needs current state, authority, open evidence, and stop conditions.
- Release, incident, or OPEX work has unfinished handoff obligations.

## Do not use when

- The packet already records completed work, evidence, and decision.
- A tiny Quick change only needs a proof note.

## Inputs

- Packet path, current phase, completed work, remaining work, changed conditions, authority limits, and next owner.

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

Produce a concise turnover record. Include the critical next action, likely error, control, evidence, and closed-loop acceptance prompt for the incoming owner.
```

## Files created or modified

- `turnover.md` or a turnover section inside a context pack.
- Related packet records if changed conditions affect risk, verification, decision, or baseline.

## Expected outputs

- Current state, resume point, changed conditions, remaining work, authority, and stop conditions.
- Incoming-owner confirmation prompt.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Handoff omits changed conditions or last completed action.
- Incoming owner acts before restating scope and stop criteria.
- Turnover summary mixes new implementation work into the handoff.

## Legal/assurance boundary note

Turnover records support workflow continuity. They do not create formal V&V, compliance, certification, safety, security, procurement, or regulatory records unless separately adopted under an external program.
