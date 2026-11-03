# Proof: explicit execution consent

## Proof summary

- **Change slug:** `explicit-execution-consent`
- **Proof owner:** automated scheduled maintenance run
- **Date:** 2026-09-05
- **Risk record:** [`risk.md`](risk.md)

## Claim proven

The shipped planner and runner prompts require explicit execution authorization and do not treat acceptance of plan contents alone as permission to act.

## Method and expected result

Run the targeted agent contract test, Ruff on that test, and `git diff --check`. The contract must find both required statements in both executable agent prompts, and all checks must pass.

The change actor wrote the test and will run and summarize the deterministic checks. PR CI can reproduce them. That coupling is visible and accepted for this small, reversible wording guard; reviewer judgment remains required.

## Result

- **Status:** pass.
- **Actual result:** `tests/test_agents.py` passed (5 tests); the full suite passed after removing an internal-name residue caught by the public-doc guard; Ruff, doctor, tokens, packet validation, flagship strict-custody validation, and `git diff --check` passed.
- **Evidence:** reproducible from the commands in this packet and `CONTRIBUTING.md`; PR CI remains the remote check.

## Reviewer note

Review whether the wording preserves the intended low-friction flow: one human signal may both accept the plan and authorize execution, but it must explicitly grant both.

## Required links

- Risk: [`risk.md`](risk.md)
- Test: [`tests/test_agents.py`](../../../tests/test_agents.py)
- Agent prompts: [`agents/planner.md`](../../../agents/planner.md) and [`agents/runner.md`](../../../agents/runner.md)

## Exit criteria

The targeted checks pass, the diff stays focused, and the reviewer can reject the distinction by reverting one commit.

## Source-lineage note

This proof records deterministic repository checks within the public boundaries mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). It makes no compliance, security, or efficacy claim.
