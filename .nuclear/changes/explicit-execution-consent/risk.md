# Risk: explicit execution consent

## Selected mode

- **Mode:** Quick
- **Why:** This is a small, fail-closed wording correction to two agent prompts and their authority documentation. It adds no tool, dependency, permission, or runtime mechanism and is removable in one commit.

## Change

- **Slug:** `explicit-execution-consent`
- **Owner:** automated scheduled maintenance run
- **Date:** 2026-09-05
- **Controlled items:** `agents/planner.md`, `agents/runner.md`, `agents/README.md`, and the plan/build boundary in `docs/04-adoption/agent-authority-model.md`

## Decision

Require a distinct human signal that explicitly authorizes execution. Accepting a plan's contents alone must not open the runner.

The main risk is adding ceremony to ordinary implementation. Keep the distinction binary and local: artifact acceptance and permission to act may arrive together, but the signal must say so.

## Required proof

- `python -m pytest tests/test_agents.py -q`
- `python -m ruff check tests/test_agents.py`
- `git diff --check`

Expected result: the agent contract test requires both explicit execution authorization and the statement that plan acceptance alone is insufficient; lint and whitespace checks pass.

## Required links

- Proof: [`proof.md`](proof.md)
- Primary operating model: [`docs/04-adoption/agent-authority-model.md`](../../../docs/04-adoption/agent-authority-model.md)
- Agent prompts: [`agents/planner.md`](../../../agents/planner.md) and [`agents/runner.md`](../../../agents/runner.md)

## Exit criteria

The distinction is consistent across the planner, runner, agent summary, and authority model; the targeted contract test passes; no new approval layer or role is introduced.

## Source-lineage note

This correction applies the repository's existing authority boundary. A public Claude Code issue reported a concrete interface that conflated plan acceptance with permission to implement: https://github.com/anthropics/claude-code/issues/92040. The report is treated as provisional incident evidence, not independent proof or a vendor-wide claim. No compliance claim is made.
