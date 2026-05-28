---
name: packing-agent-context
description: Use when preparing focused context for an AI agent, human reviewer, verifier, or releaser with explicit authority, evidence, and stop conditions.
---

# Packing Agent Context

## Overview

Context packs give agents and reviewers the right focused information: role, mode, objective, affected files, evidence obligations, approvals, forbidden actions, source lineage, critical next action, and turnover state.

## When to Use

- An AI agent will edit files, run commands, call tools, or prepare release evidence.
- A reviewer needs a one-screen summary of a Standard packet.
- A long research or implementation thread must be distilled into operational context.
- Work is resumed, delegated, or transferred and the next owner needs a closed-loop briefing.

## When Not to Use

- The task is a small Quick change with all context already in `risk.md` and `proof.md`.
- The agent has no authority to act and only needs a file explanation.

## Inputs

- Packet path and selected mode.
- Role: builder, reviewer, verifier, releaser, incident lead, or researcher.
- Affected files, allowed commands, forbidden actions, approval gates, and required evidence.
- `docs/02-operating-system/context-packs.md`.

## Process

1. Name the role and objective, and carry the mission anchor (objective, success criteria, non-goals) so it survives context resets. See `controlling-mission-drift`.
2. Include only the packet files, affected files, source rows, and evidence commands needed for the next decision.
3. State last completed action, changed conditions, critical next action, likely error, and control.
4. State file, command, network, credential, approval, and release authority.
5. State forbidden claims, do-not-touch targets, stop conditions, and turnover need.
6. Link the context pack back to the packet and relevant mode rules.
7. Require incoming confirmation when responsibility transfers.

## Outputs

- A context pack section or file.
- Clear authority boundaries.
- Next action and evidence requirement.
- Last completed action, changed conditions, and closed-loop handoff prompt when activated.

## Verification

- A reader can answer what they may do, what must remain true, what evidence is required, and when to stop.
- A resumed or delegated agent can identify where to continue and what changed.
- The context pack does not ask for whole-repo or full-standards loading without an activated reason.

## Escalation

- Stop if requested actions exceed the context pack authority.
- Escalate when credentials, network effects, production data, release authority, or external trust claims appear.
- Escalate to `turning-over-agent-work` when responsibility transfers with open work or changed conditions.

## Common Rationalizations

- "More context is safer." Excess context hides the actual decision and increases token burn.
- "The agent can infer permissions." Tool authority must be explicit.
- "Approval can happen later." Approval gates belong before the side effect.

## Red Flags

- No forbidden actions.
- No allowed file or command scope.
- No last completed action for resumed or delegated work.
- Source lineage is pasted wholesale instead of linked.

## Source-lineage note

This skill is an original context-discipline pattern influenced by public configuration management, secure development, AI risk, and systems engineering sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance.
