---
name: deciding-who-decides
description: Decides who holds authority for a change — the agent at the edge or a human gate — by matching decision rights to reversibility, evidence, and consequence, and names the escalation trigger. Use when an agent could act on something irreversible, trust-bearing, or thinly evidenced. Do not use for trivial reversible edits, or to justify skipping a required human approval.
---

# Deciding Who Decides

## Overview

Authority should sit where the evidence and competence are, not automatically at the top. But that gradient is bounded: an agent may decide reversible, well-evidenced work at the edge, and must escalate irreversible, trust-bearing, or thinly evidenced decisions to a human. This skill names, for a specific action, who decides and what makes it escalate. The point is to push decisions to the information, not to remove a human gate.

## Decision contract

- **Claim checked:** the action's reversibility, evidence grade, and consequence place it at the agent's edge or behind a named human gate, with an escalation trigger concrete enough to obey and no required approval skipped.
- **Artifact observed:** the proposed action and target, the evidence and its grade, the consequence, and the agent's authority and standing gates -> a decision-rights line (action, who decides, escalation trigger), the evidence the decider must hold, and any mandatory human gate.
- **Decision affected:** block -- may the agent act at the edge or must it escalate: the decision-rights line and its escalation trigger.
- **Failure class:** misplaced-authority (an irreversible or thinly-evidenced action placed at the edge, or a gate skipped).
- **Next action:** escalate to the named human when consequence is protected and evidence is short of proven; stop when only the agent's assurance authorizes it.

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
- The evidence on hand, and how good it is (fact, local proof, source claim, or just confidence).
- The consequence if it is wrong, and who is affected.
- The agent's granted authority, and any standing rule or human gate that already applies.

## Process

1. State the decision in one sentence and whether it is reversible.
2. Rate the evidence: proven, partially proven, or only asserted.
3. Rate the consequence: low, meaningful, or protected/irreversible.
4. Place the decision: reversible + well-evidenced + low consequence may be decided at the edge; anything irreversible, trust-bearing, or thinly evidenced escalates to a named human.
5. Name the escalation trigger in concrete terms an agent can actually obey.
6. Check that the placement raises rigor at the boundary; if it would let an agent skip a required gate, reject it.
7. Record who decides, who is informed, and what evidence the decider needs in hand.

## Outputs

- A decision-rights line: the action, who decides, and the escalation trigger.
- The evidence the decider must have before acting.
- Any human gate that stays mandatory regardless of the gradient.

## Verification

- Every escalation trigger is concrete enough for an agent or reviewer to obey without judgment calls.
- No placement removes a required human approval or lets confidence stand in for evidence.
- The decider named actually has the evidence and authority the decision needs.

## Escalation

- Escalate when consequence is protected or irreversible and the evidence is anything short of proven.
- Stop when the only thing authorizing the action is the agent's own assurance.
- Get an independent human when one agent's read is the sole basis for a trust-bearing decision.

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
- action and target:
- reversible? (yes/no):
- evidence and how good it is:
- consequence if wrong:
- agent authority / existing human gates:

Return:
- the decision in one sentence, and whether it is reversible
- evidence rating (proven / partial / asserted) and consequence rating (low / meaningful / protected)
- placement: who decides (agent at the edge, or a named human gate)
- the concrete escalation trigger an agent can obey
- any human approval that stays mandatory regardless of the gradient
- a check that the placement raises rigor at the boundary, not lowers it

Do not let confidence stand in for evidence. Do not use "authority to information" to skip a required gate.
```

## Source-lineage note

This skill is an original software-workflow translation of decentralized-decision and decision-rights ideas. Pushing authority to where the information is takes concept inspiration from intent-based leadership (paraphrased, not template lineage; see `docs/00-standards-foundation/do-not-cite-directly.md`) and from public naval mission-command doctrine, bounded by the conservative-decision-making and questioning-attitude habits in DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
