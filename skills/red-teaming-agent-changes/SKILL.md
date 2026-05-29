---
name: red-teaming-agent-changes
description: Adversarially probes an agent change, tool grant, dependency, model, or release across risk classes such as prompt injection, authority escalation, unsafe output, and tool misuse, recording probe intent, outcome, and residual risk. Use when a change expands agent authority, data access, or network scope before release. Do not use for a typo fix with no agent-authority component, or to produce a certified penetration test or formal security audit.
---

# Red-Teaming Agent Changes

## Overview

Agents with tool authority, data access, or release scope create adversarial surface that standard functional testing does not probe. This skill applies a structured adversarial review: enumerate relevant risk classes, state expected safe behavior, probe or simulate attacks, record outcomes, and link findings into the packet's evidence record.

## When to Use

- An agent is gaining new tool grants, network access, credential scope, or file-write authority.
- A change expands what an agent may read, execute, call, or release.
- A dependency or model update may shift how the agent processes untrusted input.
- The release packet needs adversarial evidence, not just functional test coverage.
- A prior OPEX record identified a gap in adversarial posture.

## When Not to Use

- The change has no agent authority component (pure data, formatting, or documentation work).
- A formal penetration test, certified security audit, or regulatory red-team exercise is already scoped.
- The packet mode is Quick and the risk screen confirms no new trust or permission boundary.

## Inputs

- Agent role description, tool grants, authority scope, data access, and release context.
- `basis.md` (protected outcomes, unacceptable outcomes, assumptions).
- `risk.md` (consequence level, failure modes).
- Prior OPEX records related to agent authority or adversarial incidents.

## Process

1. From `basis.md` and `risk.md`, name the agent role, each tool grant, and data access scope.
2. Select the adversarial classes relevant to this configuration:
   - **Prompt injection** — untrusted input attempts to overwrite agent instructions.
   - **Jailbreak** — adversarial framing to bypass content or behavior constraints.
   - **Authority escalation** — agent encouraged to exceed granted scope.
   - **Tool misuse** — allowed tools invoked for unauthorized purposes.
   - **Unsafe or harmful output** — eliciting content that violates policy or harms users.
   - **Retrieval poisoning** — malicious content injected through search, RAG, or context.
   - **Data exfiltration** — sensitive data leaked through output channels.
   - **Multi-turn manipulation** — iterative context-building to shift agent behavior.
3. For each selected class: state the probe intent, describe expected safe agent behavior, and run or simulate an adversarial probe.
4. Record the outcome for each class: `contained`, `uncertain`, or `exposed`.
5. For each `uncertain` or `exposed` finding: describe the residual risk and any compensating control (authority limit, input rail, output check, human gate).
6. Produce a before/after posture note: classes checked, results, guardrails in place, residual risks.
7. Link findings into `verification.md` and `ship.md`.

## Outputs

- Red-team findings record (inline in `verification.md`, or an optional `red-team.md`).
- Per-class probe intent, expected behavior, outcome status, and evidence or gap.
- Residual risk and compensating controls for any uncertain or exposed finding.
- Before/after posture note linked to the release decision in `ship.md`.

## Verification

- Every selected adversarial class has a recorded outcome: `contained`, `uncertain`, or `exposed`.
- No finding is silently dropped; residual risks are named in `ship.md`.
- A reviewer can see what was probed, what behavior was expected, and what was observed.
- `python tools/ng.py validate <packet>` passes.

## Escalation

- Pause if authority scope or data access is not clearly defined before probing.
- Escalate when an `exposed` finding affects credentials, production data, external users, or release posture.
- Escalate when the change requires a formal security audit beyond this skill's scope.
- Stop if adversarial probing reveals unexpected tool behavior that could affect other users or systems.

## Common Rationalizations

- "We have guardrails." Guardrails are controls, not evidence; probe them.
- "The agent only uses approved tools." Tool misuse and authority escalation use approved tools in unauthorized ways.
- "Testing covers this." Functional tests do not enumerate adversarial intent.
- "It has not been attacked yet." Adversarial surface exists at grant time, not at incident time.

## Red Flags

- The adversarial class list is empty or unchecked on a release with new agent authority.
- `uncertain` or `exposed` findings reach `ship.md` without named residual risk.
- The probe intent and expected behavior are not stated before the outcome is recorded.
- Public wording claims the agent is "safe," "secure," or "hardened" without linked adversarial evidence.

## Source-lineage note

This skill is an original adversarial-review workflow for AI-agent authority, influenced by public adversarial probe taxonomy (including the Garak open-source LLM vulnerability scanner and the NVIDIA Safety for Agentic AI blueprint), NeMo Guardrails rail-type vocabulary (input, output, retrieval, dialog, topic rails), and the NIST AI RMF govern-map-measure-manage framing, all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. It does not create formal security assurance, penetration-test certification, safety proof, compliance, or regulatory adequacy. The adversarial classes listed are a conceptual starting taxonomy, not a complete vulnerability enumeration.
