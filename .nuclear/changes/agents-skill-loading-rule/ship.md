# Ship — agents-skill-loading-rule

## Decision

Planned for PR review.

## Release decision

Defer to human maintainer. This PR is ready to be considered after local validation and CI pass, but merge is not approved by the agent.

## Evidence status

- Local validation: planned in `verification.md`.
- Independent review: Codex and Claude CLI input received; AGY CLI unavailable; fallback red-team review completed.
- CI: to be run by GitHub after PR is opened.

## Residual risk

- The wording may still be interpreted too permissively or too broadly; reviewer should inspect whether it preserves escalation safeguards without becoming another checklist.
- There is no behavioral eval for skill-loading quality in this PR.

## Rollback

Revert the `AGENTS.md` section and this packet if the wording increases confusion or causes agents to under-load safeguards.

## Monitoring / follow-up

Watch future agent PRs and cron outputs for either failure mode:

- agents loading all skills by default;
- agents skipping needed safeguards under the “smallest useful” rationale.

If either appears, update `AGENTS.md` with a tighter trigger table or add a small eval case.

## Apply clearance

This PR changes documentation and agent guidance only. Merge decision belongs to the human maintainer after PR review and CI.

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
