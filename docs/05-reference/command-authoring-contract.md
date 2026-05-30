# Command Authoring Contract

**Purpose:** Keep portable command prompts clear, easy to paste, and honest about how far they are wired in.

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

- In Public v0, call them portable command prompts.
- Give the exact prompt text.
- Name the files and outputs you expect.
- Include a verification command.
- Include the ways it can fail and the boundary language.

## Tests

`tests/test_command_contracts.py` checks that the public contract is met.

## Source-lineage note

This contract is an original writing standard for Nuclear-grade command prompts. It does not create formal assurance or compliance.
