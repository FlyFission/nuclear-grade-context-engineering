# U06 - Validator Agent Handoff

## Scenario Facts

- A coding agent is asked to fix a validator false positive (a check that wrongly fails).
- The likely files are `nuclear_grade/ng_validate.py` and the validator tests.
- The agent should not rewrite docs, change public claims, or loosen how the validator checks things across the board.

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

- What the agent is allowed to do is never spelled out.
- The agent may change docs or templates just to make tests pass.
- The stop condition is unclear if the change affects how public packets are validated.
- The proof asked for may be only "tests pass," not "the original false positive is gone and blank templates still fail."

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `rating-change-risk`
- `creating-change-records`
- `briefing-an-agent`
- `handing-off-work`
- `proving-claims`

Workflows exercised:

- Questioning attitude
- Quick change
- Standard change
- Agent authority change
- Agent turnover

Nuclear-grade output:

- Role: builder/verifier.
- Allowed files: the validator and targeted tests.
- Allowed commands: focused pytest, then full pytest before finishing.
- Forbidden actions: weakening the public boundary checks, editing unrelated docs, deleting tests, or doing broad rewrites.
- Turnover: record the last reproduced result, the files touched, the proof still owed, and the stop rules before another agent picks it up.
- Mode: Quick if it is only a local false positive; Standard if the change alters how public packets are validated.
- Proof: the fixture fails before the fix, the fixture passes after the fix, and a blank template is still rejected.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 3 | 1 |
| Nuclear-grade | 4 | 4 | 4 | 4 | 3 |

Nuclear-grade is better when you hand off to an agent, because it narrows what the agent may do and protects how the validator works.

## Decision

Use a compact context pack for coding-agent handoffs that touch validators, commands, skills, or public docs.

## Boundary Note

This trial does not prove the validator is complete or formally correct.
