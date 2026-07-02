# Basis — agents-skill-loading-rule

## Decision basis

Today's daily 1% cron recommended a small `AGENTS.md` simplification: make skill loading selective so Nuclear-grade does not feel like a giant checklist. The recommendation was based on external AGENTS.md/context-file research and the current target repo state.

## Relevant facts

- `AGENTS.md` currently has a flat 17-item recommended-skills list.
- The repo's sharpness goal is minimum discipline that lets agents do serious work without turning every change into vibes.
- Skill loading is part of context engineering: more context is not automatically better.
- The existing default behavior and authority boundaries already contain important escalation safeguards.

## Alternatives considered

| Alternative | Decision | Reason |
|---|---|---|
| Do nothing | Rejected | Leaves the flat list open to checklist interpretation. |
| Group skills under trigger headings | Rejected after review | Could create new mini-checklists or imply groups are exclusive modes. |
| Add one short skill-loading rule and keep the list flat | Accepted | Smallest change that addresses the issue while preserving all links. |
| Add eval README or Copilot instructions too | Deferred | Valuable candidates, but would expand this PR beyond one 1% move. |

## Independent review inputs

- Codex CLI: supported a short trigger-based rule and warned not to load whole groups.
- Claude CLI: warned grouping and skip-reason requirements could add bloat; recommended one sentence/short section above the flat list.
- AGY CLI: unavailable due account `PERMISSION_DENIED`; fallback red-team review emphasized trigger screening before minimization and safeguards for ambiguous triggers.

## Decision

Add a concise `## Skill loading rule` section to `AGENTS.md`, keep all recommended skills present, and do not add grouping or new artifacts beyond this packet.

## Open gaps

- No behavioral eval proves agents will load fewer or better skills after this wording change.
- The PR relies on reviewer judgment and future agent behavior observation.

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
