# Skill Authoring Contract

**Purpose:** Keep Nuclear-grade skills easy for an agent to run and easy to test.

## Required structure

Every skill lives at:

```text
skills/<skill-name>/SKILL.md
```

The file must include:

- YAML frontmatter with `name` and `description` (required). `license` and `compatibility` are optional supported fields.
- A `name` that is lowercase, hyphen-separated, starts with a letter, and has no consecutive or trailing dashes.
- A `description` that says what the skill does, when to trigger it, and a clear negative clause (a "Do not use for ..." near-miss). Aim for one or two full sentences, 80 to 500 characters. Avoid a colon followed by a space, so strict YAML loaders read it as one value.
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

Keep `SKILL.md` under 500 lines. When the detail grows, move it into optional sibling files the agent can load when it needs them:

```text
skills/<skill-name>/
  SKILL.md
  references/   long reference material, one topic per file
  scripts/      runnable helpers the skill can call
  assets/       templates or fixtures the skill emits
```

The metadata (the frontmatter) is always loaded. The `SKILL.md` body loads when the skill triggers. The `references/`, `scripts/`, and `assets/` folders load only when the skill needs them. Packaged wheels bundle the whole skill directory, so these subfolders travel with the skill.

## Writing rules

- One skill, one job.
- Write the description so it triggers well. Lead with what it does. Name concrete trigger conditions. Add a negative clause so the skill does not over-trigger.
- Explain why. Prefer the reason over ALL-CAPS MUST or NEVER.
- Put the process in the body, not in the frontmatter.
- Name the exact artifacts or decisions the skill produces.
- Include stop conditions and escalation triggers.
- Include boundary language when public trust or assurance terms show up.
- For each skill, keep at least three should-trigger prompts and two near-miss should-not-trigger prompts in `skill-evaluation.md`.

## Tests

`tests/test_skill_contracts.py` checks that the public contract is met.

## Source-lineage note

This contract is an original writing standard for Nuclear-grade skills. It does not create formal assurance or compliance.
