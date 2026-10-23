# Quick Risk Record

## Selected mode

- **Mode:** Quick
- **Why this mode:** A small, reversible wording change to one existing context-pack field and its generated prompt surface; no runtime, permission, dependency, or release behavior changes.

## Change

- Slug: `source-authority-boundary`
- PR / issue: pending PR
- Owner: FlyFission
- Date: 2026-09-17
- Summary: Require context packs to link or quote the governing request instead of treating an agent-authored summary as permission.

## Scope

- Affected files/configs/docs: `docs/02-operating-system/context-packs.md`, `skills/briefing-an-agent/SKILL.md`, generated `commands/ng-context-pack.md`
- User-visible behavior changed? yes, the briefing prompt requests one additional source field
- Dependency/model/API/prompt/tool permission changed? prompt wording only; no tool permission changes
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A context pack carries one unnecessary field or states the boundary imprecisely. |
| Reversibility | Revert one documentation commit. |
| Detectability | Generated-command drift, tests, validator, and direct diff review expose errors. |
| Exposure | Public documentation and prompt card only. |
| Uncertainty | Low; the rule is narrow and aligns with existing authority boundaries. |
| Why Quick is enough | The change adds no role, gate, schema parser, runtime control, or new authority. |

## Required proof

- Command/check/eval to run: full pytest and Ruff suites; command generation check; doctor; token check; Quick packet validation; strict-custody example validation; `git diff --check`
- Expected result: all commands pass and only the intended docs, skill, generated card, and packet change
- Evidence link/location: `proof.md` and PR checks

## Critical-action self-check

Not activated; the branch is disposable and no production or release action is involved.

## Escalation check

No Standard trigger is present. The edit narrows how existing authority is evidenced; it does not grant authority or change agent power.

## Required links

- Packet: `.nuclear/changes/source-authority-boundary/`
- Related PR/issue: pending PR
- Proof record: `proof.md`
- Relevant primary mechanism evidence: https://github.com/openai/codex/commit/e269f2164cbb9f499e4f22301c393500e2a831f3

## Exit criteria

- The mode is justified as Quick.
- The generated command matches the skill.
- Tests and repository checks pass.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

The change is original repository guidance informed by a concrete upstream mechanism: OpenAI Codex now captures bounded sender-authored user messages for delegated reviews while explicitly treating them as partial context, not transferred permission. The upstream implementation is evidence of the failure mode, not proof that this wording prevents it.
