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

A skill carries two separate decisions; keep them apart.

**Decision 1 -- does this skill deserve to exist?** Made on evidence, not taste. A skill that has run and never changed a real decision -- merge, rollback, escalation, or review scope -- is noise, and a relocation or deletion candidate. This is earned from the numbers over time (see `docs/05-reference/skill-evaluation.md`), never from a self-assigned label, because a guard inside the writable set is a suggestion the author can edit. No skill is deleted automatically; the signal is raised for a human to decide.

**Decision 2 -- what receipt must it emit?** Not every skill needs a long artifact, but every skill must name the decision it can change, in a compact receipt right after `## Overview`:

```markdown
## Decision contract

- **Claim checked:** <stated so evidence could prove it right or wrong>
- **Artifact observed:** <file/section read, and the file/section left behind>
- **Decision affected:** <block | warn | observe> -- <the one decision this moves, e.g. `ship.md` ship/block/defer, the Quick/Standard mode choice, the authority line>
- **Failure class:** <the kind of failure if the claim fails, e.g. missing-evidence, scope-overrun, boundary-overreach>
- **Next action:** <what the agent or human does next>
```

The **Decision affected** tier is what keeps the control loop from becoming audit-the-audit:

- **block** -- a failure stops the named decision (do not ship, resume, or start); promoted into the operator receipt.
- **warn** -- the decision proceeds, but a named residual risk is recorded for the decider; promoted into the operator receipt.
- **observe** -- the skill rarely moves its decision; it stays in telemetry, not promoted into the operator receipt. An honest resting place for a low-value-but-not-yet-removed check, and the step before relocation or deletion.

Only **block** and **warn** are promoted into the operator receipt (`ng decisions`); **observe** stays in telemetry (`ng decisions --all`). If a skill changes decisions but emits vague prose, amend it until the receipt is machine-checkable rather than dropping it.

Keep the receipt compact -- one short clause per field, not a re-listing of `## Outputs`. `ng doctor` lints that the receipt is present, has all five fields, and carries a valid tier; whether the named decision is the *honest* one is human judgment, like every other structural check here.

## Progressive disclosure

Keep `SKILL.md` under 500 lines. When the detail grows, move it into optional sibling files the agent can load when it needs them:

```text
skills/<skill-name>/
  SKILL.md
  references/   long reference material, one topic per file
  scripts/      runnable helpers the skill can call
  assets/       templates or fixtures the skill emits
```

Treat the frontmatter as a routing index, not guaranteed context. Hosts may shorten descriptions or
omit entries when their catalog budget is tight; Codex, for example, now [drops descriptions before
entries](https://github.com/openai/codex/pull/34738) and [warns when the visible catalog is
reduced](https://github.com/openai/codex/pull/34997). Make the name useful without its description,
front-load the description's discriminating trigger, and do not assume every enabled skill is visible
to the model. The `SKILL.md` body and optional folders load only after selection. Packaged wheels
bundle the whole skill directory, so these subfolders travel with the skill.

## Writing rules

- One skill, one job.
- Write the description so it triggers well. Lead with what it does. Name concrete trigger conditions. Add a negative clause so the skill does not over-trigger.
- Explain why. Prefer the reason over ALL-CAPS MUST or NEVER.
- Put the process in the body, not in the frontmatter.
- Name the exact artifacts or decisions the skill produces. State the one decision it can move in the `## Decision contract` block; if you cannot, the skill is docs, not a skill.
- Include stop conditions and escalation triggers.
- Include boundary language when public trust or assurance terms show up.
- For each skill, keep at least three should-trigger prompts and two near-miss should-not-trigger prompts in `skill-evaluation.md`.
- Declare the skill's assumptions of use when they matter: the context it was validated for -- the trust level of its inputs, whether a human gate is present, the model tier, the granted tools. A reusable skill is only safe in that context, and the consumer should confirm the assumptions hold before relying on it. A skill written assuming a human approves each action is unsafe when dropped into an unattended agent run.

## Routing (anti-overlap)

With a large skill set, the expensive failure is not a missing skill — it is two skills that both
look right, so an agent fires the wrong one or fires both. A negative clause that only says *when
not* to use a skill leaves the agent to guess *what instead*. Close that gap: where a skill has a
close neighbor, the `## When Not to Use` entry names the sibling to use instead.

- Prefer `Do not use for X — use \`<sibling-skill>\` instead` over a bare `Do not use for X`.
- Only add the pointer where a real near-miss exists (e.g. `briefing-an-agent` ↔ `handing-off-work`;
  `creating-change-records` ↔ `rating-change-risk`). Do not manufacture cross-links for distant skills.
- This turns the skill set into a navigable graph: each near-miss edge routes to the more specific
  skill, which is what keeps 29 skills from collapsing into "read them all and decide."

Source: the explicit activation-boundary pattern in Agent-Skills-for-Context-Engineering
(source-map Tier 11), adapted to this repo's existing `## When Not to Use` section.

## Tests

`tests/test_skill_contracts.py` checks that the public contract is met.

## Source-lineage note

This contract is an original writing standard for Nuclear-grade skills. It does not create formal assurance or compliance.
