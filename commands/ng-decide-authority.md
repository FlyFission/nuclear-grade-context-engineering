# ng-decide-authority

## Purpose

Decide who holds authority for a specific action — the agent at the edge or a human gate — by matching decision rights to reversibility, evidence, and consequence. Push the decision to where the information is without removing a required human gate. This is a portable command prompt.

## Use when

- An agent is about to act and it is unclear whether it may decide alone or must ask first.
- The action is irreversible, trust-bearing, or rests on thin evidence.
- You are setting an agent's standing authority and need explicit escalation thresholds.

## Do not use when

- The edit is trivial and reversible with obvious proof and no new trust boundary.
- A required human approval already exists; this prompt never talks past it.
- An incident is live and stabilization comes first.

## Inputs

- The proposed action, its exact target, and whether it can be undone.
- The evidence on hand and how good it is (fact, local proof, source claim, or confidence).
- The consequence if it is wrong, and who is affected.
- The agent's granted authority and any standing human gate.

## Prompt text

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

## Files created or modified

- A decision-rights line inside `risk.md`, `basis.md`, or a context pack.
- `.nuclear/changes/<slug>/intent.md` when the action also needs a stated intent.

## Expected outputs

- The action, who decides, and the escalation trigger.
- The evidence the decider must hold before acting.
- Any mandatory human gate that the gradient does not dissolve.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Arguing authority from how confident the agent sounds.
- Citing "push authority to information" to skip a human approval.
- Vague escalation triggers like "if it seems risky."
- Placing an irreversible action at the edge because the diff looked small.

## Legal/assurance boundary note

Deciding who decides helps you place authority and escalation with intent. It does not create formal verification and validation, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
