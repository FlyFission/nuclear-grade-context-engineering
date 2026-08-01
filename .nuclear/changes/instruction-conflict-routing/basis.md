# Basis — instruction conflict routing

## Mission

Prevent an agent from silently choosing among contradictory instructions and presenting the resulting action as if its authority were clear.

## Requirement

**REQ-001:** When loaded instructions conflict on an affected action, the agent shall identify the conflicting sources, apply the host's documented precedence, and stop before that action if precedence does not resolve the conflict.

Codex currently collects project instructions from repository root to working directory and preserves that source order; it also supports a preferred local override file. Those mechanics make instruction provenance operational, but this repository did not tell an agent what to do when the resulting instructions disagree. The rule stays host-neutral rather than asserting that every tool resolves scope identically.

## Primary records

- [Codex `agents_md.rs`](https://github.com/openai/codex/blob/c4ce0493dc94923493ca5b1e7e8695c289febad0/codex-rs/core/src/agents_md.rs) — discovery order, source retention, and `AGENTS.override.md` preference; repository Apache-2.0.
- [Codex commit c4ce049 (2026-07-16)](https://github.com/openai/codex/commit/c4ce0493dc94923493ca5b1e7e8695c289febad0) — latest change on that source path reviewed for this packet.
- [AGENTS.md format repository](https://github.com/agentsmd/agents.md) — a minimal, MIT-licensed instruction-file format; it does not supply a universal cross-host precedence rule.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

The requirement names the failure, the resolution path, and the stop condition without inventing portable precedence semantics.

## Source-lineage note

Host behavior is treated as implementation evidence, not proof that the proposed wording improves outcomes.