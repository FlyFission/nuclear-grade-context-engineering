# Command Authoring Contract

**Purpose:** Keep portable command prompts clear, pasteable, and honest about integration status.

## Required structure

Every command card lives at:

```text
commands/<name>.md
```

The file must include:

- `## Purpose`
- `## Use when`
- `## Do not use when`
- `## Inputs`
- `## Prompt text`
- `## Files created or modified`
- `## Expected outputs`
- `## Verification command`
- `## Failure modes`
- `## Legal/assurance boundary note`

## Writing rules

- Call them portable command prompts in Public v0.
- Provide exact prompt text.
- Name expected files and outputs.
- Include a verification command.
- Include failure modes and boundary language.

## Tests

`tests/test_command_contracts.py` enforces the public contract.

## Source-lineage note

This contract is an original authoring standard for Nuclear-grade command prompts. It does not create formal assurance or compliance.
