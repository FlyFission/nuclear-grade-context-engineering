# Skill Authoring Contract

**Purpose:** Keep Nuclear-grade skills agent-operable and testable.

## Required structure

Every skill lives at:

```text
skills/<skill-name>/SKILL.md
```

The file must include:

- YAML frontmatter with `name` and `description` (required). `license` and `compatibility` are optional supported fields.
- A `name` that is lowercase, hyphen-separated, starts with a letter, and has no consecutive or trailing dashes.
- A `description` that states what the skill does, when to trigger it, and an explicit negative clause (a "Do not use for ..." near-miss). Aim for one or two rich sentences, 80 to 500 characters. Avoid a colon followed by a space so strict YAML loaders read it as a single scalar.
- `## Overview`
- `## When to Use`
- `## When Not to Use`
- `## Inputs`
- `## Process`
- `## Outputs`
- `## Verification`
- `## Escalation`
- `## Common Rationalizations`
- `## Red Flags`
- `## Source-lineage note`

## Progressive disclosure

Keep `SKILL.md` under 500 lines. When detail grows, offload it to optional sibling files the agent can load on demand:

```text
skills/<skill-name>/
  SKILL.md
  references/   long reference material, one topic per file
  scripts/      runnable helpers the skill can call
  assets/       templates or fixtures the skill emits
```

The metadata (frontmatter) is always loaded, the `SKILL.md` body loads on trigger, and `references/`, `scripts/`, and `assets/` load only when the skill needs them. Packaged wheels bundle the whole skill directory, so these subfolders travel with the skill.

## Writing rules

- One skill, one job.
- Write the description for triggering: lead with what it does, name concrete trigger conditions, and add a negative clause so the skill does not over-trigger.
- Explain the why; prefer rationale over ALL-CAPS MUST or NEVER.
- Put process in the body, not in frontmatter.
- Name exact artifacts or decisions the skill produces.
- Include stop conditions and escalation triggers.
- Include boundary language when public trust or assurance terms appear.
- Maintain at least three should-trigger and two near-miss should-not-trigger prompts in `skill-evaluation.md` for each skill.

## Tests

`tests/test_skill_contracts.py` enforces the public contract.

## Source-lineage note

This contract is an original authoring standard for Nuclear-grade skills. It does not create formal assurance or compliance.
