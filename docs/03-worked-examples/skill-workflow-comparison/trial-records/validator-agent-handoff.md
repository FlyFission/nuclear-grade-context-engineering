# U06 - Validator Agent Handoff

## Scenario Facts

- A coding agent is asked to fix a validator false positive.
- The likely files are `nuclear_grade/ng_validate.py` and validator tests.
- The agent should not rewrite docs, alter public claims, or loosen validation semantics broadly.

## Simple Prompt Trial

Prompt:

```text
Fix the validator bug and run tests.
```

Expected simple output:

- Agent searches broadly.
- Edits validator.
- Runs tests.
- Reports pass.

Simple path strengths:

- Fast.
- Often enough for a local bug.

Simple path gaps:

- Authority is implicit.
- Agent may change docs or templates to make tests pass.
- Stop condition is unclear if semantics affect public validation.
- Proof obligation may be only "tests pass," not "the original false positive is gone and blank templates still fail."

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `classifying-change-risk`
- `creating-change-packets`
- `packing-agent-context`
- `proving-claims`

Workflows exercised:

- Questioning attitude
- Quick change
- Standard change
- Agent authority change

Nuclear-grade output:

- Role: builder/verifier.
- Allowed files: validator and targeted tests.
- Allowed commands: focused pytest and full pytest before completion.
- Forbidden actions: weakening public boundary checks, editing unrelated docs, deleting tests, broad refactors.
- Mode: Quick if local false positive only; Standard if validation semantics change public packet behavior.
- Proof: failing fixture before fix, passing fixture after fix, blank template still rejected.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 3 | 1 |
| Nuclear-grade | 4 | 4 | 4 | 4 | 3 |

Nuclear-grade is better when handing off to an agent because it narrows authority and protects validator semantics.

## Decision

Use a compact context pack for coding-agent handoffs that affect validators, commands, skills, or public docs.

## Boundary Note

This trial does not prove the validator is complete or formally correct.
