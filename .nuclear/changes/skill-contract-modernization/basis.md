# Basis

## Change context

- Slug: skill-contract-modernization
- Scope: Skill-authoring contract relaxation plus rewrite of all 18 descriptions, name-format rule, optional frontmatter, progressive-disclosure docs, version sync.
- Outcome to protect: Skills trigger reliably without breaking existing skills or downstream authors.

## Need and scope

The prior contract forced descriptions to start with `Use when` and capped them at 90-180 characters. Anthropic skill-authoring guidance is the opposite: descriptions should be richer (what the skill does, when to trigger it, and an explicit "Do not use for ..." near-miss) to reduce under-triggering. The repo's own rule was likely wrong. This change relaxes the rule, rewrites all descriptions, and adds supporting affordances, all non-breaking.

## Derived requirements or claims

| ID | Requirement / claim | Evidence planned |
|---|---|---|
| C-001 | The contract test no longer mandates a `Use when` prefix or a 90-180 cap; it requires 80-500 characters, a negative clause, and no colon-space. | `tests/test_skill_contracts.py`; suite green. |
| C-002 | All 18 skill descriptions are rewritten to the what-plus-when-plus-negative form, within band and colon-free. | Per-file frontmatter; the contract test iterates all skills. |
| C-003 | `name` must be lowercase, hyphen-separated, start with a letter, with no consecutive or trailing dashes, and no length cap (existing names exceed 32 characters). | `SKILL_NAME_PATTERN` check; all 18 pass. |
| C-004 | `license` and `compatibility` are optional supported frontmatter fields. | `ALLOWED_FRONTMATTER_KEYS`; test passes with current files. |
| C-005 | Progressive disclosure (optional `references/`, `scripts/`, `assets/`) is documented in the authoring contract and SKILLS.md. | Diffs of those files. |
| C-006 | Version is synced to 0.3.0 across `pyproject.toml`, `nuclear-grade.yaml`, and `CITATION.cff`, and `test_packaging.py` asserts 0.3.0. | Diffs; `tests/test_packaging.py`. |
| C-007 | The change is non-breaking: it loosens the repo's own contract test and does not constrain externally authored skills. | Reasoning recorded; no required field added. |

## Assumptions, constraints, and invalidation triggers

- Assumption: relaxing the contract cannot break downstream authors because it only loosens our own test. Invalidation trigger: a real YAML loader rejects a rewritten description (mitigated by the colon-space ban).
- Constraint: no skill renames (a 32-char name cap would force them; the rule omits a length cap).
- Constraint: description enforcement stays in the contract test, not the CLI doctor, because the doctor's stub fixtures use short descriptions.

## Acceptance scenarios

- An author writes a skill whose description says what it does, when to use it, and what not to use it for, in 80-500 characters with no colon-space; the contract test passes.
- A strict YAML loader in an agent harness parses every shipped description as a single scalar (no colon-space).
- A reviewer reads SKILLS.md and the authoring contract and sees the new rule and the progressive-disclosure layout.

## Required links

- Packet: `.nuclear/changes/skill-contract-modernization/`
- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- Claims C-001 through C-007 are mapped to plan steps and have evidence rows.

## Source-lineage note

Original Nuclear-grade packet influenced by public skill-authoring practice and the concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
