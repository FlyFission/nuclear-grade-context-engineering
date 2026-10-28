---
description: "States what an agent intends to do and why before a critical or irreversible action, so a reviewer can challenge the thinking and not just the result."
disable-model-invocation: true
---

# ng-intent

Portable command prompt generated from `skills/declaring-intent/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- Before a deploy, migration, data change, public claim, dependency or model swap, or release.
- When an action is hard to reverse, or its blast radius is more than the immediate file.
- When you want a reviewer's eyes on the reasoning and the abort criteria before execution.
- When standing authority lets an agent proceed unless told no, and the team needs the "no" window.

## Do not use when

- The action is a routine, reversible edit with obvious proof and no trust boundary.
- An incident is live and the next move is stabilization, not a fresh proposal.
- Someone wants the declaration treated as a guarantee or certification.

## Inputs

- The intended action and the exact target.
- The reasoning and the evidence that says the preconditions are met.
- The expected result, and the signals that would mean it went wrong.
- The abort and rollback criteria, the decision rights, and who is backing up the action.

## Prompt text

```text
Declare intent before this action the Nuclear-grade way.

Inputs:
- intended action and target:
- reasoning / evidence preconditions are met:
- expected result:
- abort criteria (numbers where possible):
- rollback (and is it verified?):
- who may stop it, by when / backup watcher:

Return:
- "I intend to <action> on <target> because <evidence/reasoning>"
- the expected result and the precise signals that would falsify it
- the abort criteria and the verified rollback
- the decision rights and the backup
- after acting: the actual result compared to the expected result, and any gap

State what would prove this wrong, not just what success looks like. Treat the stated intent as a proposal to review, not proof the agent understood. Do not imply certification or formal assurance.
```

## Verification

- The declaration names what would prove it wrong, not just what success looks like.
- Abort and rollback criteria are concrete and the rollback has been checked.
- The actual result is compared to the expected result and the gap is recorded.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/declaring-intent/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
