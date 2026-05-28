# Red-Team Review

**Purpose:** Activate adversarial review at the right points in the lifecycle to close the gap between functional test coverage and agent authority risk.

## Why this exists

Standard change packets prove claims with functional evidence: tests pass, diffs are reviewed, behavior is correct. Agents with tool grants, network access, or release scope introduce adversarial surface that functional evidence does not probe. Red-team review is the activation point for that gap.

## When to activate

Red-team review is an HPI overlay for agent authority. Activate it when any of these apply to the current release:

- The agent gains a new tool grant (file write, command run, API call, credential access, external network).
- The authority scope expands: more files, broader commands, larger data set, or higher-trust system.
- A dependency or model update may shift how the agent processes untrusted user input.
- A prior OPEX record identified adversarial posture as a gap.

## How it fits in the lifecycle

```text
Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline
                                ↑
                      Red-team overlay activates here
                      when agent authority is in scope
```

Red-team evidence feeds `verification.md` exactly like functional test evidence. It is an additional verification class, not a separate assurance layer.

## Minimum useful version

- Agent role, tool grants, and authority scope named.
- Adversarial classes selected from the taxonomy (prompt injection, jailbreak, authority escalation, tool misuse, unsafe output, retrieval poisoning, data exfiltration, multi-turn manipulation).
- Per-class probe intent and expected safe behavior stated before probing.
- Outcome recorded: `contained`, `uncertain`, or `exposed`.
- Residual risks linked to `ship.md`.

Use `skills/red-teaming-agent-changes/SKILL.md` for the full process.
Use `commands/ng-red-team.md` as a portable agent prompt.
Use `templates/standard/red-team.md` when findings warrant a separate record.

## Relationship to self-check and agent authority model

Red-team review complements, not replaces, `self-checking-agent-actions` and the agent authority model in `docs/04-adoption/agent-authority-model.md`. The authority model defines what the agent is permitted to do; self-check applies before each critical action; red-team review probes whether the permission boundary can be violated from the outside. All three are needed for a complete picture.

## Boundaries

This review is not:

- a formal penetration test;
- a security audit or certification;
- a complete vulnerability assessment;
- a substitute for qualified security engineering on high-risk systems.

The adversarial classes are a conceptual starting taxonomy, not a complete vulnerability enumeration. Unknown vectors remain.

## Source-lineage note

Influenced by public adversarial probe taxonomy (Garak open-source LLM vulnerability scanner, NVIDIA Safety for Agentic AI blueprint), NeMo Guardrails rail-type vocabulary, and NIST AI RMF framing, all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. Not a compliance or certification artifact.
