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
- `## Decision contract`
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

## Decision contract

Charter Article 11 says to name the decision the evidence must support before the work starts. A skill is a control in that loop, so each one states, in a short scannable block right after `## Overview`, the one decision it can move and the class of signal it leaves. A skill that cannot name a decision it changes is documentation, not a skill; move it to `docs/`.

The block is four labelled bullets:

```markdown
## Decision contract

- **Claim verified:** <stated so evidence could prove it right or wrong>
- **Observed artifact:** <file/section read, and the file/section left behind, e.g. `verification.md` claim-to-evidence table>
- **Decision it can change:** <the one named downstream decision or file this can flip, e.g. `ship.md` ship/block/defer, the Quick/Standard mode choice, the authority line>
- **Class:** <hard gate | soft note>
```

- **hard gate** -- a failing observation blocks the named decision (do not ship, resume, or start).
- **soft note** -- a passing observation that still records a residual risk the decider must weigh, attached to a named decision.
- **deletion signal** -- *not declared here.* A check that almost never moves its named decision is a relocation candidate, surfaced by measurement (the `tokens-per-decision-signal` join in `ng tokens`/`ng eval`), not by a self-assigned label. A guard inside the writable set is a suggestion the author can edit, so deletability is earned from the numbers over time, not claimed up front.

Keep the block tight: it is the distilled pointer to the decision, not a re-listing of everything in `## Outputs`. The point is that a reviewer reads one block, not the whole skill, to learn whether running it could change an outcome. `ng doctor` lints that the block is present and the class is valid; whether the named decision is the *honest* one is human judgment, like every other structural check here.

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
- Name the exact artifacts or decisions the skill produces. State the one decision it can move in the `## Decision contract` block; if you cannot, the skill is docs, not a skill.
- Include stop conditions and escalation triggers.
- Include boundary language when public trust or assurance terms show up.
- For each skill, keep at least three should-trigger prompts and two near-miss should-not-trigger prompts in `skill-evaluation.md`.

## Tests

`tests/test_skill_contracts.py` checks that the public contract is met.

## Source-lineage note

This contract is an original writing standard for Nuclear-grade skills. It does not create formal assurance or compliance.
