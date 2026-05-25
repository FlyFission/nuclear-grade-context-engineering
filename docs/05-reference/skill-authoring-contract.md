# Skill Authoring Contract

**Purpose:** Keep Nuclear-grade skills agent-operable and testable.

## Required structure

Every skill lives at:

```text
skills/<skill-name>/SKILL.md
```

The file must include:

- YAML frontmatter with `name` and `description`.
- `description` starts with `Use when`.
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

## Writing rules

- One skill, one job.
- Make trigger descriptions concrete enough to catch realistic use cases.
- Put process in the body, not in frontmatter.
- Name exact artifacts or decisions the skill produces.
- Include stop conditions and escalation triggers.
- Include boundary language when public trust or assurance terms appear.
- Maintain at least three should-trigger and two near-miss should-not-trigger prompts in `skill-evaluation.md` for each skill.

## Tests

`tests/test_skill_contracts.py` enforces the public contract.

## Source-lineage note

This contract is an original authoring standard for Nuclear-grade skills. It does not create formal assurance or compliance.
