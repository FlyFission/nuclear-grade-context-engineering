# ng-context-pack

## Purpose

Prepare focused context for a person or AI agent working from a change record (the packet). This is a portable command prompt.

## Use when

- An agent will edit files, run tools, or prepare evidence.
- A reviewer needs a short summary of where the work stands.
- A long thread needs to be boiled down before work continues.
- Work is resumed, handed off, or transferred, and you must keep its state, its authority, its proof, and its stop rules intact.

## Do not use when

- The change record already holds all the context a Quick change needs.
- The task is only to explain one file.

## Inputs

- The path to the change record (the packet).
- The role, the decision question, the goal, the work phase, the files it touches, the commands allowed, the actions forbidden, the approvals needed, and the evidence required.
- `docs/02-operating-system/context-packs.md`.

## Prompt text

```text
Build a Nuclear-grade context pack for this work.

Inputs:
- packet: .nuclear/changes/<slug>/
- role: <builder|reviewer|verifier|releaser|researcher>
- decision question: <one sentence>
- objective: <one paragraph>
- work phase: <explore|candidate|audit|accept>
- affected files: <list>
- last completed action:
- changed conditions:
- critical next action and likely error:
- allowed commands/tools: <list>
- forbidden actions: <list>
- do-not-touch targets: <list>
- approval gates: <list>
- required evidence: <commands/links/reviews>

Return a short context pack. Include the mode, the decision question, the goal, the work phase, a risk summary, a basis summary, the evidence required, the limits on what the agent may do, the claims it must not make, the open gaps, the last action completed, what has changed, the critical next action, and the next action. If responsibility is changing hands, add a step where the incoming owner confirms they understand.
```

## Files created or modified

- A packet note, or a context-pack section, as the maintainer chooses.
- No code files, unless that is separately authorized.

## Expected outputs

- A focused context pack.
- Clear limits on what the agent may do.
- The decision question and the work phase.
- The next action.
- The point to resume from, and the incoming owner's confirmation, when those apply.

## Verification command

```bash
python tools/ng.py status .
```

## Failure modes

- Loading the whole repo with no reason to.
- Leaving out the decision question, which forces the agent to guess what the evidence must support.
- Leaving the limits on files, commands, the network, credentials, or releases unstated.
- Leaving out the claims the agent must not make.
- Leaving out the last action completed, for resumed or handed-off work.

## Legal/assurance boundary note

A context pack sets limits on the work. It does not approve side effects, certify that anything is adequate, or create formal assurance.
