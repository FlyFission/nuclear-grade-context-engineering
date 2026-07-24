---
name: deciding-who-decides
description: Decides who holds authority for a change — the agent at the edge or a human gate — by matching decision rights to reversibility, evidence, and consequence, and names the escalation trigger. Use when an agent could act on something irreversible, trust-bearing, or thinly evidenced. Do not use for trivial reversible edits, or to justify skipping a required human approval.
---

# Deciding Who Decides

## Overview

Authority should sit where the policy, evidence, competence, and effective ability to intervene support it, not automatically at the top or with the actor holding the tool. This skill creates an evidence-conditioned authority record for one bounded decision episode. It separates prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close rights; links each right to exact evidence IDs; preserves unknown and disputed states; and names transfer or blocking triggers. It does not infer authorization from technical capability, repository activity, fluency, or nominal human presence.

## Decision contract

- **Claim checked:** each decision right is assigned under an explicit local policy to a named actor, the exact admitted evidence IDs and custody profile are visible, unresolved evidence cannot silently clear agent application, and transfer/reopen/close triggers are concrete.
- **Artifact observed:** the bounded action; `verification.md` evidence IDs, raw states, intended-use/V&V status, and coupling profile; standing authority policy; effective intervention capability; and any existing human gate -> `decision-authority.md` plus a policy-relative derived result.
- **Decision affected:** block -- may the proposed actor exercise the evaluated decision right, must authority transfer, is separate or dual control required, or is the action blocked/prohibited/indeterminate.
- **Failure class:** misplaced-authority or unsupported-basis (capability treated as authorization, unresolved/self-check evidence clearing agent action, prohibited role overlap, stale basis, or skipped gate).
- **Next action:** record raw observations, derive the policy-relative result, and transfer or block before side effects when the basis or authority is unresolved.

## When to Use

- An agent is about to act and it is unclear whether it may decide alone or must ask first.
- A change is irreversible, touches users, data, credentials, dependencies, agent authority, or a release.
- The evidence behind a decision is thin, contested, or rests only on the agent's own confidence.
- You are setting up an agent's standing authority and want explicit decision rights and escalation thresholds.

## When Not to Use

- The edit is trivial and reversible with obvious proof and no new trust boundary.
- A required human approval already exists; this skill never exists to talk past it.
- An incident is live and you must stabilize first (use `responding-to-incidents`).

## Inputs

- The proposed action, its target, and whether it can be undone.
- The exact evidence IDs in `verification.md`, their raw states, intended use, and custody/coupling profile.
- The consequence if it is wrong, and who is affected.
- The agent's granted authority, effective stop/reversal capability, and any standing rule or human gate that already applies.
- The actors proposed for prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close.

## Process

1. Bound the decision episode: identify the exact candidate/action, controlling policy version, and whether the action is reversible.
2. Copy source-linked raw evidence states from the record: `observed`, `bounded_absence`, `unknown`, or `disputed`. Never convert missing telemetry into absence.
3. Link the intended-use/V&V status and evidence-custody/coupling profile from `verification.md`. Do not infer substantive truth or independence from structure alone.
4. Allocate every decision right: prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close. Name the proposed actor, evidence IDs, policy gate, required authority, and transfer trigger.
5. Derive the evaluated result under the declared policy: `agent_authorized`, `human_required`, `separate_control_required`, `dual_authority_required`, `blocked_pending_evidence`, `prohibited_for_agent`, or `indeterminate`.
6. Block agent application when decisive evidence is unknown, disputed, or classified as self-check. A nominal human approval does not cure absent evidence, absent authority, or absent intervention capability.
7. Record reopen, supersession, interim-expiry, and closure controls. A materially changed action or evidence basis requires a new or successor episode; do not silently reuse prior acceptance.
8. Run `ng validate <packet> --strict-authority`; use `--strict-custody` as well when the packet must require both activated records.

## Outputs

- A completed `decision-authority.md` for the bounded episode.
- Explicit allocations for all nine decision rights and their evidence IDs.
- A policy-relative result and concrete transfer/blocking trigger.
- Reopen, supersession, expiry, and closure controls.

## Verification

- `ng validate <packet> --strict-authority` passes; for strict evidence custody use both strict flags.
- Every Evidence ID exists in `verification.md`; `bounded_absence` has finite scope and a time boundary.
- Unknown, disputed, or decisive self-check evidence does not clear `agent_authorized` apply.
- Every decision right appears once, and the derived result is consistent with the recorded apply allocation or a blocking override.
- Passing proves structural consistency only, not identity, evidence quality, independence, authorization, safety, security, or compliance.

## Escalation

- Transfer or block when the policy requires a human, separate control, or dual authority.
- Stop when the exact evidence basis, action identity, authority holder, or intervention capability is unknown or disputed.
- Stop when only the action-producing agent's self-check clears a decisive acceptance condition.
- Reopen when admitted evidence expires, is invalidated, becomes disputed, or no longer matches the action.

## Common Rationalizations

- "The agent has the most context, so it should decide." Local context is not judgment on an irreversible action.
- "It is faster if it just acts." Speed at the edge is the goal only while the work is reversible.
- "We delegated this already." Delegation sets a boundary; it does not dissolve the gate above the boundary.
- "It is probably fine." "Probably" is the trigger to escalate, not to proceed.

## Red Flags

- Authority is argued from how confident or fluent the agent sounds.
- "Push authority to the information" is cited as a reason to skip a human approval.
- The escalation trigger is vague ("if it seems risky") rather than a named condition.
- An irreversible action is placed at the edge because the diff looked small.

## Prompt

```text
Decide who decides for this action the Nuclear-grade way.

Inputs:
- exact action, target, and stable identity:
- controlling local policy/version:
- reversible? (yes/no):
- `verification.md` Evidence IDs, raw states, V&V status, and custody/coupling profile:
- consequence if wrong and effective stop/reversal capability:
- granted agent authority / existing human gates:

Create or update `decision-authority.md` using the repository template. Allocate prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close. Derive one policy-relative result, name every transfer trigger, preserve unknown/disputed states, and record reopen/closure controls.

Run `ng validate <packet> --strict-authority`. Do not let confidence, technical capability, repository activity, or nominal human presence stand in for evidence or authorization.
```

## Source-lineage note

This skill is an original software-workflow integration, not a claim to have invented authority transfer, mixed initiative, provenance, V&V, human oversight, or meaningful human control. Relevant prior mechanisms include Parasuraman, Sheridan, and Wickens' levels-of-automation model (https://doi.org/10.1109/3468.844354), Scerri, Pynadath, and Tambe's adjustable-autonomy transfer-of-control strategies (https://doi.org/10.1613/jair.1037), Decision Provenance (https://doi.org/10.1109/ACCESS.2018.2887201), and meaningful-human-control tracking/tracing (https://doi.org/10.3389/frobt.2018.00015). The repository contribution is the record-supported join between exact software evidence IDs, custody/coupling, explicit decision rights, and a policy-relative result. It does not create DOE compliance, formal assurance, safety, security, certification, regulatory adequacy, or proof of effective human control.
