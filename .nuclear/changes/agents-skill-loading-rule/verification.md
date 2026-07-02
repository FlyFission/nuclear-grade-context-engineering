# Verification — agents-skill-loading-rule

## Claims to verify

| Claim | Status | Evidence |
|---|---|---|
| Diff is limited to `AGENTS.md` and this packet | planned | `git diff --stat` |
| No whitespace errors | planned | `git diff --check` |
| Packet validates | planned | `python tools/ng.py validate .nuclear/changes/agents-skill-loading-rule` |
| Repo wiring remains healthy | planned | `python tools/ng.py doctor .` |

## Commands

```bash
git diff --stat
git diff --check
python tools/ng.py validate .nuclear/changes/agents-skill-loading-rule
python tools/ng.py doctor .
```

## Results

- `git diff --stat`: `AGENTS.md | 4 ++++` plus this change packet.
- `git diff --check`: passed with no whitespace errors.
- `python tools/ng.py validate .nuclear/changes/agents-skill-loading-rule`: `OK: .nuclear/changes/agents-skill-loading-rule`.
- `python tools/ng.py doctor .`: `OK: Nuclear-grade doctor`.

## Known gaps

- No automated behavioral eval measures whether future agents load fewer or better skills.
- Reviewer judgment is required to decide whether the wording is sharp enough and not too permissive.

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
