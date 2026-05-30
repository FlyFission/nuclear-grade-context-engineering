# Red-Team Review

**Purpose:** This file turns on adversarial review at the right points in the lifecycle. It closes the gap between what normal tests cover and the risk that comes with an agent's authority.

## Why this exists

Standard change packets prove claims with normal evidence: tests pass, diffs get reviewed, behavior is correct. But an agent with tool grants, network access, or release scope opens an attack surface that normal evidence never probes. Red-team review is where you turn on the check for that gap.

## When to activate

Red-team review is an HPI overlay for agent authority. Turn it on when any of these apply to the current release:

- The agent gets a new tool grant (write a file, run a command, call an API, use credentials, reach the outside network).
- Its authority grows: more files, broader commands, a larger data set, or a higher-trust system.
- A dependency or model update may change how the agent handles untrusted user input.
- A past OPEX record flagged the agent's defenses against attack as a gap.

## How it fits in the lifecycle

```text
Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline
                                ↑
                      Red-team overlay activates here
                      when agent authority is in scope
```

Red-team evidence feeds `verification.md` just like normal test evidence. It is one more kind of verification, not a separate layer of assurance.

## Minimum useful version

- Name the agent's role, its tool grants, and how far its authority reaches.
- Pick the attack types from the list (prompt injection, jailbreak, authority escalation, tool misuse, unsafe output, retrieval poisoning, data exfiltration, multi-turn manipulation).
- For each type, state what you will probe and what safe behavior you expect, before you probe.
- Record the outcome: `contained`, `uncertain`, or `exposed`.
- Link leftover risks to `ship.md`.

Use `skills/stress-testing-agent-changes/SKILL.md` for the full process.
Use `commands/ng-red-team.md` as a portable agent prompt.
Use `templates/standard/red-team.md` when findings warrant a separate record.

## Relationship to self-check and agent authority model

Red-team review adds to, and does not replace, `double-checking-before-acting` and the agent authority model in `docs/04-adoption/agent-authority-model.md`. The authority model says what the agent is allowed to do. The self-check applies before each critical action. Red-team review tests whether someone outside can break through the permission boundary. You need all three for a full picture.

## Boundaries

This review is not:

- a formal penetration test;
- a security audit or certification;
- a complete check for every vulnerability;
- a stand-in for qualified security engineering on high-risk systems.

The attack types are a starting list, not a full count of every vulnerability. Unknown ways in still exist.

## Source-lineage note

Influenced by public lists of attack probes (the Garak open-source LLM vulnerability scanner, the NVIDIA Safety for Agentic AI blueprint), the NeMo Guardrails set of guardrail types, and the framing in the NIST AI RMF, all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. Not a compliance or certification artifact.
