# Plan — agents-skill-loading-rule

## Goal

Sharpen `AGENTS.md` so agents treat the recommended skills as a routing aid, not a checklist, and load the smallest useful skill set only after screening for real triggers.

## Value check

Today's daily 1% cron found that repository-level agent instruction files can add cost and confusion when they carry unnecessary requirements. In this repo, the flat 17-item recommended-skills list can be misread as “load everything.” The valuable update is not a new workflow; it is a short rule that keeps skill loading evidence-driven.

## Non-goals

- Do not add new skills.
- Do not add a new agent runtime, command, hook, or template family.
- Do not add `.github/copilot-instructions.md` or `evals/README.md` in this PR.
- Do not rewrite the whole agent policy.
- Do not overclaim based on one research paper or one cron run.

## Initial proposal

The first proposal was to add a skill-loading rule and group the existing skills under three trigger headings.

## Independent review input received

- **Codex CLI independent review:** keep the short skill-loading rule; make it trigger-based; add “not a checklist”; avoid extra scope.
- **Claude CLI adversarial review:** avoid grouping because it may create new mini-checklists; do not require agents to document every skipped skill; keep the flat list and add one sharp rule.
- **AGY CLI red-team attempt:** `agy models` returned `PERMISSION_DENIED (code 403)`, and print mode returned no review text. Because the requested CLI was unavailable, a fallback red-team subagent reviewed the plan and warned against letting “smallest useful” become a reason to skip escalation or evidence.

## Incorporated approach

Use the simpler version:

1. Add one `## Skill loading rule` section before `## Recommended skills`.
2. Keep the current skill list flat.
3. Say skills are loaded by trigger, not inventory.
4. Require trigger screening before minimizing.
5. State that the list is a routing aid, not a checklist.
6. Preserve a hard guardrail: if a trigger is present or ambiguous, load the matching skill or state the specific evidence showing why it is not needed.

## Files expected to change

- `AGENTS.md`
- `.nuclear/changes/agents-skill-loading-rule/risk.md`
- `.nuclear/changes/agents-skill-loading-rule/basis.md`
- `.nuclear/changes/agents-skill-loading-rule/plan.md`
- `.nuclear/changes/agents-skill-loading-rule/trace.md`
- `.nuclear/changes/agents-skill-loading-rule/verification.md`
- `.nuclear/changes/agents-skill-loading-rule/ship.md`

## Validation plan

- Inspect `git diff` to confirm the change is limited to `AGENTS.md` and this packet.
- Run `git diff --check`.
- Run `python tools/ng.py validate .nuclear/changes/agents-skill-loading-rule`.
- Run `python tools/ng.py doctor .`.

## Acceptance criteria

- `AGENTS.md` makes trigger-based skill loading explicit.
- Existing skill links remain present.
- The change reduces checklist behavior without weakening escalation, evidence, or trust-boundary safeguards.
- Packet validation passes.
- PR body names the cron source, review inputs, and validation commands.

## Required links

- Packet: `.nuclear/changes/agents-skill-loading-rule/`
- Changed guidance: `AGENTS.md`
- Daily cron source: job `35dfea877788`, 2026-07-01 output
- Independent review notes: local CLI output files under `/tmp/nuclear-grade-*-review.out` during implementation

## Exit criteria

- The guidance update is limited to the skill-loading rule.
- Existing skill links remain present.
- Validation commands pass locally.
- The PR body states residual gaps and the human maintainer owns the merge decision.

## Source-lineage note

This change is informed by the daily repo-scouting output and external AGENTS.md/context-file research cited there. It stays within the repo's public source-lineage boundaries in `docs/00-standards-foundation/source-map.md` and makes no compliance, certification, safety, security, regulatory, or formal QA claim.
