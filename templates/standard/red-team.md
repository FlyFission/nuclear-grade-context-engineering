# Red-Team Findings Record

**Purpose:** Record adversarial probe results, residual risks, and compensating controls for agent authority, tool grants, or release scope that requires adversarial evidence.

**Activation threshold:** Use when a release packet has agent tool authority, model inputs, or data access that warrants adversarial review beyond functional testing.

**Minimum useful version:** Agent role, selected adversarial classes, per-class probe intent, expected safe behavior, outcome, residual risk, and posture note.

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

Select the classes relevant to this configuration. Mark inapplicable classes `N/A` with a brief reason.

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

For each `uncertain` or `exposed` finding:

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

- Every selected class has a recorded probe intent, expected behavior, and outcome status.
- All `uncertain` or `exposed` findings have named residual risk and compensating controls.
- Posture note is referenced in `ship.md`.
- No public wording claims "secure," "safe," or "hardened" beyond the scope of these probes.

## Source-lineage note

Original Nuclear-grade template influenced by public adversarial probe taxonomy (Garak LLM vulnerability scanner, NVIDIA Safety for Agentic AI blueprint), NeMo Guardrails rail-type vocabulary, and NIST AI RMF framing, all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. No compliance, penetration-test, or security certification claim is made.
