---
name: deciding-who-decides
description: Decides who holds authority for a change — the agent at the edge or a human gate — by matching decision rights to reversibility, evidence, and consequence, and names the escalation trigger. Use when an agent could act on something irreversible, trust-bearing, or thinly evidenced. Do not use for trivial reversible edits, or to justify skipping a required human approval.
---

# Deciding Who Decides

## Overview

Authority should sit where the policy, evidence, competence, and effective ability to intervene support it, not automatically at the top or with the actor holding the tool. This skill creates an evidence-conditioned authority record for one bounded decision episode. It separates prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close rights; links evidentiary rights to exact Evidence IDs; names the authority that may assemble each right's basis; preserves unknown and disputed states; and names transfer or blocking triggers. It does not infer authorization from technical capability, repository activity, fluency, or nominal human presence.

## Decision contract

- **Claim checked:** each decision right is assigned under an explicit local policy to a named actor; each right's declared basis and basis authority are visible; required Evidence IDs and their custody profile are visible; unresolved evidence cannot silently clear agent application; and transfer/reopen/close triggers are concrete.
- **Artifact observed:** the bounded action; `verification.md` Evidence IDs, coded source states, intended-use/V&V status, and coupling profile; declared policy identity, authority, custody, digest, and validity; effective intervention capability; and any existing human gate -> `decision-authority.md` plus a declaration-relative structural result.
- **Decision affected:** block -- does the declared record structurally permit agent application, require authority transfer or separate/dual control, or remain blocked/prohibited/indeterminate?
- **Failure class:** misplaced-authority or unsupported-basis (capability treated as authorization, unresolved/self-check evidence clearing agent action, prohibited role overlap, stale basis, or skipped gate).
- **Next action:** record raw observations, derive the declaration-relative result, and transfer or block before side effects when the basis or authority is unresolved.

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
- The exact Evidence IDs in `verification.md`, their coded source states, intended use, and custody/coupling profile.
- The controlling policy ID/version, policy authority, policy custodian, policy digest, and validity or non-expiry basis.
- The consequence if it is wrong, and who is affected.
- The agent's granted authority, effective stop/reversal capability, and any standing rule or human gate that already applies.
- The actors proposed for prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close.

## Process

1. Bound the decision episode: identify the exact candidate/action, controlling policy version, policy authority, policy custodian, policy digest, a non-expired UTC validity or concrete non-expiry basis, and whether the action is reversible. Validator-host time is not a trusted clock.
2. Code source-linked evidence states from the record: `observed`, `bounded_absence`, `unknown`, or `disputed`. These are interpreted record states, not sensor-raw facts. Never convert missing telemetry into absence.
3. Link the intended-use/V&V status and evidence-custody/coupling profile from `verification.md`. Do not infer substantive truth or independence from structure alone.
4. Allocate every decision right: prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close. Name the proposed actor, evidence-basis authority, policy gate, required authority, and transfer trigger. Evidence-basis authority is mandatory and cannot be `not applicable`. Recommend, verify, validate, verdict, accept, and close require decisive Evidence IDs. Prepare, apply, and reopen may use `not applicable` only for the Evidence IDs when the policy/trigger basis is explicit; a structurally clearable agent apply still requires decisive evidence.
5. Allocate `agent_permitted`, `human_required`, `separate_control_required`, `dual_authority_required`, `blocked_pending_evidence`, or `prohibited_for_agent`. Derive one declaration-relative result: `agent_apply_structurally_clearable`, one of the five non-agent paths, or `policy_result_indeterminate`. Indeterminate never clears application.
6. Block agent application when decisive evidence is unknown, disputed, or classified as self-check. A nominal human approval does not cure absent evidence, absent authority, or absent intervention capability.
7. Record reopen, supersession, interim-expiry, and closure controls. A materially changed action or evidence basis requires a new or successor episode; do not silently reuse prior acceptance.
8. Run `ng validate <packet> --strict-authority`; use `--strict-custody` as well when the packet must require both activated records.

## Outputs

- A completed `decision-authority.md` for the bounded episode.
- Explicit allocations for all nine decision rights, their basis authority, and their Evidence IDs or explicit non-evidentiary basis.
- A declaration-relative structural result and concrete transfer/blocking trigger.
- Reopen, supersession, expiry, and closure controls.

## Verification

- `ng validate <packet> --strict-authority` passes; for strict evidence custody use both strict flags.
- Every required Evidence ID exists in `verification.md`; `bounded_absence` has finite scope and a time boundary; each right names evidence-basis authority.
- Unknown, disputed, absent, or decisive self-check evidence does not produce `agent_apply_structurally_clearable`; `policy_result_indeterminate` is non-clearing.
- Each required table occurs once inside its named section; supported Markdown-equivalent H2, unordered-list, comment, and fenced-example forms cannot hide duplicates or satisfy required structure from examples; every required episode, result, and lifecycle scalar occurs once; every decision right appears once; and the derived result evaluates `apply` and is consistent with the recorded apply allocation or a blocking override.
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
- controlling policy ID/version, authority, custodian, digest, and validity:
- reversible? (yes/no):
- `verification.md` Evidence IDs, coded source states, V&V status, and custody/coupling profile:
- consequence if wrong and effective stop/reversal capability:
- granted agent authority / existing human gates:

Create or update `decision-authority.md` using the repository template. Allocate prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close. Name each right's evidence-basis authority. Derive one declaration-relative structural result, name every transfer trigger, preserve unknown/disputed states, and record reopen/closure controls.

Run `ng validate <packet> --strict-authority`. Do not let confidence, technical capability, repository activity, or nominal human presence stand in for evidence or authorization.
```

## Source-lineage note

This skill is an original software-workflow integration, not a claim to have invented authority transfer, provenance-based access control, workflow authorization, proof-carrying authorization, usage control, supply-chain attestations, assurance cases, V&V, human oversight, or meaningful human control. Relevant mechanisms include PBAC (https://doi.org/10.1109/PST.2012.6297930), dynamic separation of duties in PBAC (https://doi.org/10.1109/PST.2013.6596060), Proof-Carrying Authentication (https://doi.org/10.1145/319709.319718), workflow authorization constraints (https://doi.org/10.1145/300830.300837), UCON (https://doi.org/10.1145/507711.507722), in-toto (https://doi.org/10.5555/3230833.3230851), Decision Provenance (https://doi.org/10.1109/ACCESS.2018.2887201), and meaningful-human-control tracking/tracing (https://doi.org/10.3389/frobt.2018.00015). The repository contribution is the bounded record-supported join between explicit decision rights, each right's declared basis and basis authority, required software Evidence IDs and custody/coupling, and a declaration-relative structural result. It does not create actual authorization, formal assurance, safety, security, certification, regulatory adequacy, or proof of effective human control.
