# Trace — agents-skill-loading-rule

## Change trace

| Requirement / risk | Implementation | Evidence |
|---|---|---|
| Make skills trigger-based, not inventory-based | Added `## Skill loading rule` to `AGENTS.md` | `AGENTS.md` diff |
| Prevent under-loading safeguards | Rule says to screen for risk, evidence, decision-rights, public-claim, trust-boundary, handoff, release, incident, or hard-to-reverse triggers before minimizing | `AGENTS.md` diff |
| Avoid a new checklist | Rule says the list is a routing aid, not a checklist; existing list remains flat | `AGENTS.md` diff |
| Keep existing skill links | No recommended skill links removed | `git diff` review |
| Keep the PR small | No new skills, commands, runtime features, eval README, or Copilot instructions added | `git diff --stat` |

## Review trace

| Reviewer | Input incorporated |
|---|---|
| Codex CLI | Added “trigger, not inventory” / “routing aid, not checklist” framing. |
| Claude CLI | Dropped the grouping idea and avoided requiring documentation of every skipped skill. |
| AGY CLI | Attempted, but unavailable with account permission error. |
| Fallback red-team review | Added trigger screening before minimization and ambiguity guardrail. |

## Files changed

- `AGENTS.md`
- `.nuclear/changes/agents-skill-loading-rule/risk.md`
- `.nuclear/changes/agents-skill-loading-rule/basis.md`
- `.nuclear/changes/agents-skill-loading-rule/plan.md`
- `.nuclear/changes/agents-skill-loading-rule/trace.md`
- `.nuclear/changes/agents-skill-loading-rule/verification.md`
- `.nuclear/changes/agents-skill-loading-rule/ship.md`

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
