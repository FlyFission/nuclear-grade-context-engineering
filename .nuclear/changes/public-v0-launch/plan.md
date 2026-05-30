# Plan — Public v0 Launch

**Purpose:** Bound the launch-readiness work so public v0 ships cleanly, without growing the method.

---

## Build sequence

1. Create launch branch and launch packet.
2. Remove public residue and stale worked-example state.
3. Add explicit source-map status labels and downgrade unresolved sources.
4. Align validator with documented Quick and Standard packet behavior.
5. Run tests, packet validation, diff check, and residue/source/overclaim scans.
6. Open PR, request review, merge after CI, then flip GitHub visibility.

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| `README.md`, `QUICKSTART.md`, `tools/README.md` | Public status and validator scope updates. | First-run user experience. | Maintainer |
| `docs/00-standards-foundation/source-map.md` | Status-labeled public source map. | Citation safety. | Maintainer |
| Worked-example packet | Stale status/residue cleanup. | Flagship example credibility. | Maintainer |
| `tools/ng_validate.py` and `tests/test_ng_validate.py` | Quick/Standard mode support and tests. | Deterministic launch gate. | Maintainer |
| `.nuclear/changes/public-v0-launch/` | Launch evidence packet. | Release-readiness record. | Maintainer |

## Non-goals

- Do not implement C-002/C-003 before public v0.
- Do not add Nuclear/Incident/Release validator support before public v0.
- Do not add marketing pages, branding work, or new methodology layers.
- Do not claim compliance, certification, production sandboxing, or regulator readiness.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| Validator scope | Quick and Standard only. | All modes in v0. | Matches public onboarding needs without overbuilding. | Public docs claim broader validation. |
| Source gaps | Verify or downgrade. | Delete context or pretend verification. | Preserves useful context without unsafe lineage claims. | New official URLs found. |
| Release workflow | Branch + PR + CI before visibility. | Direct main/public flip. | Visibility is a public side effect. | Emergency rollback. |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Public residue cleanup | Internal local paths and stale launch wording removed. | pass |
| Source status cleanup | Source-map entries status-labeled. | pass |
| Validator tests updated | Quick/Standard behavior covered. | pass |
| Packet validation complete | Worked-example and launch packets validate. | planned |
| Release decision ready | PR/CI/visibility gates recorded. | planned |

## Rollback approach

- **Rollback method:** Revert the launch branch or PR before merge; after merge, revert the launch commit(s).
- **State/data reversal notes:** No production service state exists.
- **Feature flag / kill switch:** GitHub visibility can remain private until all gates pass.
- **Owner:** Maintainer.
- **Time to restore estimate:** Less than 30 minutes before visibility flip.

## Proof commands

```bash
python -m pytest tests/test_ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q
python -m py_compile tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/reference/workspace_guard.py
python tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
python tools/ng_validate.py .nuclear/changes/public-v0-launch
git diff --check
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Superseding public-readiness packet: `../cm-public-readiness/`

## Exit criteria

- Public v0 work is bounded.
- Review checkpoints are explicit.
- Rollback/visibility gate exists.
- Proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade launch plan inspired by public lifecycle, configuration-management, release-readiness, and verification concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
