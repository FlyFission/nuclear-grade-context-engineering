# Risk — agents-skill-loading-rule

## Selected mode

- **Mode:** Standard
- **Why this mode:** This is a small Markdown change, but it changes `AGENTS.md`, a controlled agent-guidance file that can affect how agents select safeguards. Standard mode is warranted because the change touches AI behavior and evidence discipline.

## Change

- Slug: `agents-skill-loading-rule`
- Owner: Hermes Agent
- Date: 2026-07-01
- Summary: Add a short rule telling agents to load skills by trigger, not by inventory, and to minimize only after screening for risk/evidence/escalation triggers.

## Risk statement

The current flat recommended-skills list may be read as a checklist to load wholesale. That can increase context, cost, and process feel. The opposite failure is also possible: a “smallest skill set” rule could become a license to skip safeguards before understanding the work.

## Scope

- Affected files: `AGENTS.md` and this change packet.
- Controlled item changed: repo-level agent guidance.
- Runtime/code behavior changed: no.
- Public claim/compliance posture changed: no.
- Dependency/model/API/tool permission changed: no.
- Release posture changed: no.

## Must not break

- Agents must still screen for trust boundaries, public claims, release decisions, incidents, hard-to-reverse steps, and evidence needs.
- Existing recommended skill links must remain present.
- The change must not add a new workflow, new artifact family, or new runtime surface.
- The wording must not imply that confidence or familiarity is a reason to skip evidence.

## Main failure modes

| Failure mode | Control |
|---|---|
| Agents load the whole skill list by default | State that the list is a routing aid, not a checklist. |
| Agents under-load safeguards | Require trigger screening before minimizing. |
| Agents use “smallest useful” to skip escalation | If a trigger is present or ambiguous, load the matching skill or state specific evidence showing why it is not needed. |
| Change becomes process-heavy | Keep the AGENTS.md edit to one short section and keep the skill list flat. |

## Escalation check

No code, dependency, credential, network, production-facing, release, or compliance claim changes are included. The reason this remains Standard rather than Quick is the controlled agent-guidance impact.

## Exit criteria

- Diff is limited to `AGENTS.md` and the packet.
- `git diff --check` passes.
- Packet validation passes.
- `python tools/ng.py doctor .` passes.

## Required links

- Packet: `.nuclear/changes/agents-skill-loading-rule/`
- Changed guidance: `AGENTS.md`
- Daily cron source: job `35dfea877788`, 2026-07-01 output
- Source map: `docs/00-standards-foundation/source-map.md`

## Source-lineage note

This change is informed by the daily repo-scouting output and external AGENTS.md/context-file research cited there. It stays within the repo's public source-lineage boundaries in `docs/00-standards-foundation/source-map.md` and makes no compliance, certification, safety, security, regulatory, or formal QA claim.
