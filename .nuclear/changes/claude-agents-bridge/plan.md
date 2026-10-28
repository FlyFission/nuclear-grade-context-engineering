# Plan — claude-agents-bridge

## Change context

- **Slug:** `claude-agents-bridge`
- **Owner:** FlyFission
- **Date:** 2026-08-06
- **Lifecycle phase:** Execute / Verify

## Build sequence

| Step | Task | Requirement | Output | Proof |
|---|---|---|---|---|
| 1 | Add the documented import shim | REQ-001 | `CLAUDE.md` | Exact-content inspection |
| 2 | Record and run bounded verification | REQ-001 | `verification.md` | Packet validation, public-doc tests, doctor, diff check |
| 3 | Open a review-only PR | REQ-001 | GitHub PR | CI and human merge verdict |

## Affected files and non-goals

- Add `CLAUDE.md`.
- Add this Standard change record.
- Do not duplicate `AGENTS.md`, add Claude-specific rules, configure hooks/settings, or alter permissions.

## Review checkpoints

- Requirement/design/tasks: pass — bounded to one import line.
- Build complete: pass — diff is limited to the import shim and this packet.
- Verification complete: pass — all listed commands succeeded.
- Release decision: human reviewer after PR.

## Rollback

Revert the focused commit. There is no migration, stored state, dependency, or external side effect.

## Proof commands

```bash
git diff --check
python -m pytest tests/test_public_docs.py -q
python tools/ng.py validate .nuclear/changes/claude-agents-bridge --strict-custody
python tools/ng.py doctor .
python tools/ng.py tokens .
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- The diff contains one import-only compatibility file and this packet.
- All bounded proof commands pass.
- The PR leaves the merge verdict to a human.

## Source-lineage note

The implementation uses Anthropic's documented `CLAUDE.md` import syntax at <https://code.claude.com/docs/en/memory> and adds no broader workflow claim.
