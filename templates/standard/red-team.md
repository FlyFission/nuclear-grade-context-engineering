# Red-Team Findings Record

**Purpose:** Record what your attack probes found, the leftover risks, and the controls that make up for them, for agent power, tool grants, or a release scope that needs attack evidence.

**Activation threshold:** Use when a release packet has agent tool power, model inputs, or data access that calls for an attack review beyond normal testing.

**Minimum useful version:** the agent role, the attack types you chose, the goal of each probe, the expected safe behavior, the outcome, the leftover risk, and a stance note.

---

## Change context

- Slug:
- Agent role and tool grants:
- Release context:
- Owner:
- Date:
- Related risk record: `risk.md`
- Related basis record: `basis.md`

## Adversarial class selection

Pick the attack types that fit this setup. Mark the ones that do not fit `N/A` with a short reason.

| Class | Applicable? | Reason if N/A |
|---|---|---|
| Prompt injection | | |
| Jailbreak | | |
| Authority escalation | | |
| Tool misuse | | |
| Unsafe or harmful output | | |
| Retrieval poisoning | | |
| Data exfiltration | | |
| Multi-turn manipulation | | |

## Adversarial probe table

| Class | Probe intent | Expected safe behavior | Probe run or simulated | Outcome | Evidence or gap |
|---|---|---|---|---|---|
| | | | yes / simulated / no | contained / uncertain / exposed | |

## Residual risk and compensating controls

For each finding marked `uncertain` or `exposed`:

| Class | Residual risk | Compensating control | Control evidence | Ship impact |
|---|---|---|---|---|
| | | | | |

## Before/after posture note

- Classes checked:
- Outcomes summary (contained / uncertain / exposed counts):
- Guardrails or authority controls in place:
- Residual adversarial risk accepted for this release:
- Decision authority:

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every chosen attack type has a recorded probe goal, expected behavior, and outcome status.
- Every `uncertain` or `exposed` finding has a named leftover risk and controls that make up for it.
- The stance note is linked from `ship.md`.
- No public wording claims "secure," "safe," or "hardened" beyond what these probes actually covered.

## Source-lineage note

Original Nuclear-grade template influenced by a public list of attack types (the Garak LLM vulnerability scanner, the NVIDIA Safety for Agentic AI blueprint), the NeMo Guardrails rail-type vocabulary, and NIST AI RMF framing, all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. No compliance, penetration-test, or security certification claim is made.
