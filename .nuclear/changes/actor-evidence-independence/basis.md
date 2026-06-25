# Actor-Evidence Independence — Basis

## Purpose

State what the amendment must establish and the claims a reviewer must be able to check.

## Decision question

Does the framework now defend against the failure it already names — a confident hallucination clearing gates whose inputs the actor authored — rather than only describing it?

## Background

The repo named "persuasive documentation" as a failure pattern, but the control loop did not defend against it. In the default single-agent path the agent that acts at Execute also authors the Verify evidence, the Review narrative, and the Decide framing, so the actor and the evidence-author are one entity. The framework already had the self-modification boundary (the agent must not edit its gate); it lacked the dual (the agent must not be the sole author of the gate's input).

## Requirements / claims

| ID | Claim the change must support | How a reviewer checks it |
|---|---|---|
| REQ-001 | The failure pattern is named with a home doctrine page, framed as the dual of the self-modification boundary. | Read `actor-evidence-independence.md` and the new Self-authorship boundary in `agent-authority-model.md`. |
| REQ-002 | The independence seam is wired into the loop at Verify/Review/Decide, not only described in one page. | Grep the concept across `WORKFLOWS.md`, `lifecycle.md`, `README.md`, `CORE.md`, the two skills, and the templates. |
| REQ-003 | The amendment adds an operational hook and an honest validator/threat-model posture, without over-claiming enforcement. | Read the `## Evidence independence` template section and the deferred-check note in `validators.md`. |
| REQ-004 | The change breaks no existing contract test, token budget, or packet validator. | Run pytest, ruff, `ng doctor`, `ng tokens`, `ng validate`. |

## Outcomes to protect

- The validator principle (structure, not judgment) — the new check stays a disclosure, not a verdict.
- The boundary discipline — no formal-assurance claim is introduced.
- The token discipline — the doctrine body is gated by description cost, not pasted into always-on context.

## Assumptions

- Adopters read the loop docs and templates as the operative surface; naming the seam there is what changes behavior.
- The PROVE subagents already encode the seam in tool form; this change names them as such rather than inventing a new mechanism.

## Required links

- Risk: `risk.md`
- Plan: `plan.md`
- Verification: `verification.md`
- Doctrine: `../../../docs/02-operating-system/actor-evidence-independence.md`

## Exit criteria

- Each claim has a check a reviewer can run.
- The outcomes to protect are named.

## Source-lineage note

Original Nuclear-grade packet inspired by public ideas on independent verification, segregation of duties, software assurance, and AI risk mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
