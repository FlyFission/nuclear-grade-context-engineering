# ng-context-pack

## Purpose

Prepare focused context for a human or AI agent working from a packet. This is a portable command prompt.

## Use when

- An agent will edit files, run tools, or prepare evidence.
- A reviewer needs a short operational summary.
- A long thread needs distillation before work continues.
- Work is resumed, delegated, or transferred and needs state, authority, proof, and stop criteria preserved.

## Do not use when

- The packet itself already contains all needed Quick-mode context.
- The task is only to explain one file.

## Inputs

- Packet path.
- Role, decision question, objective, work phase, affected files, allowed commands, forbidden actions, approvals, and required evidence.
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

Return a concise context pack with mode, decision question, objective, work phase, risk summary, basis summary, required evidence, authority boundaries, forbidden claims, open gaps, last completed action, changed conditions, critical next action, and next action. If responsibility transfers, add incoming-owner confirmation.
```

## Files created or modified

- Packet note or context-pack section chosen by the maintainer.
- No implementation files unless separately authorized.

## Expected outputs

- Focused context pack.
- Clear authority boundaries.
- Decision question and work phase.
- Next action.
- Resume point and incoming-owner confirmation when activated.

## Verification command

```bash
python tools/ng.py status .
```

## Failure modes

- Loading the whole repo without an activated reason.
- Omitting the decision question and forcing the agent to infer what evidence must support.
- Leaving file, command, network, credential, or release authority unstated.
- Omitting forbidden claims.
- Omitting last completed action for resumed or delegated work.

## Legal/assurance boundary note

A context pack constrains work. It does not approve side effects, certify adequacy, or create formal assurance.
