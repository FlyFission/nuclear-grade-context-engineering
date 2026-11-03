# Quick Risk: Effective Instruction State

## Selected mode

- **Mode:** Quick
- **Why this mode:** This is a small, reversible wording correction to an existing context-pack field; it adds no permission, runtime behavior, dependency, or release claim.

## Change

- Slug: `effective-instruction-state`
- PR / issue: PR to be opened
- Owner: FlyFission
- Date: 2026-09-11
- Summary: Replace a configuration-shaped list of instruction files with evidence-shaped effective instruction state.

## Scope

- Affected files/configs/docs: `docs/02-operating-system/context-packs.md`, `skills/briefing-an-agent/SKILL.md`, generated `commands/ng-context-pack.md`, and its golden prompt fixture.
- User-visible behavior changed? yes, the context-pack prompt now distinguishes observed instruction state from file presence.
- Dependency/model/API/prompt/tool permission changed? prompt wording only; no model, API, dependency, or permission change.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A context pack may report instruction state as unknown more often; no action authority changes. |
| Reversibility | One documentation commit. |
| Detectability | Command parity, repository tests, and direct diff review expose drift or overreach. |
| Exposure | Existing public context-pack guidance only. |
| Uncertainty | Low: the change requires evidence when available and preserves an explicit fallback when it is not. |
| Why Quick is enough | The diff narrows one existing field and is mechanically checked; it adds no control layer. |

## Required proof

- Command/check/eval to run: full pytest and Ruff checks; command-card parity; doctor; token check; strict-custody worked-example validation; `git diff --check`.
- Expected result: all checks pass and only the intended context-pack surfaces change.
- Evidence link/location: `proof.md` and CI on the PR.

## Critical-action self-check

Not activated; the branch is isolated and the change is reversible.

## Escalation check

No Standard trigger found: no user/data/security/permission/operation/architecture effect, no trust decision, and proof fits this packet.

## Required links

- Packet: `.nuclear/changes/effective-instruction-state/`
- Related PR/issue: PR to be opened
- Proof record: `proof.md`
- Relevant source: [OpenAI Codex commit 935ac771, 2026-09-10](https://github.com/openai/codex/commit/935ac7710da6d33cf700b3fd953a878f9e1c4535)

## Exit criteria

- Quick mode remains justified.
- The generated command and golden prompt fixture match the skill.
- The wording does not claim every host exposes instruction-load evidence.

## Source-lineage note

This change uses the upstream commit as implementation evidence that applied instruction state can change at request boundaries. It does not claim Codex proves this documentation effective, and it creates no formal assurance or compliance claim.
