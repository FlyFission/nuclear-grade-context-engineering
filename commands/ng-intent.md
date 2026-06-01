# ng-intent

## Purpose

State what you intend to do and why before a critical or irreversible action, so a reviewer can challenge the thinking before the action, not the wreckage after. Works as a release brief or a critical-action declaration. This is a portable command prompt.

## Use when

- Before a deploy, migration, data change, public claim, dependency or model swap, or release.
- The action is hard to reverse, or its blast radius is more than the immediate file.
- Standing authority lets an agent proceed unless told no, and the team needs the "no" window.

## Do not use when

- The action is a routine, reversible edit with obvious proof and no trust boundary.
- An incident is live and the next move is stabilization, not a fresh proposal.
- Someone wants the declaration treated as a guarantee or certification.

## Inputs

- The intended action and the exact target.
- The reasoning and the evidence that the preconditions are met.
- The expected result and the signals that would mean it went wrong.
- The abort criteria, the verified rollback, the decision rights, and the backup watcher.

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

## Files created or modified

- `.nuclear/changes/<slug>/intent.md` from `templates/golden-path/intent.md`.
- A release section in `ship.md`, or a self-check in `self-check.md`, when a short record is enough.

## Expected outputs

- The intent, the expected result, and the falsifying signals.
- The abort criteria and the verified rollback.
- The actual result compared to the expected result after the action.

## Verification command

The intent record is filed inside a change packet, so validate the packet it lives in. The packet's `risk.md` declares the mode (Quick or Standard) and carries that mode's base files; `intent.md` is checked alongside them.

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Stating the goal but no falsifying signal or abort threshold.
- Asserting "checks passed" with no link to the evidence.
- A zero-length review window because the work felt urgent.
- Approving the result without ever seeing the reasoning.

## Legal/assurance boundary note

Declaring intent helps a reviewer challenge the reasoning before the action. It does not create formal verification and validation, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
