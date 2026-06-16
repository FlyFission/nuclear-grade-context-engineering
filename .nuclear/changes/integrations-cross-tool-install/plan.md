# Standard Plan Record

**Purpose:** Bound the work so the build, the review, the verification, and the rollback are planned before the change grows.

**Activation threshold:** Use for Standard changes where the build has several steps, affected controlled items, dependency/model/tool decisions, rollback concerns, or a review order to plan.

**Minimum useful version:** the build sequence, the affected files and assets, the non-goals, the review checkpoints, the rollback approach, and the proof commands.

**Overhead trap:** Do not write a project plan for a small change. Capture only the decisions you need to build and review the change without losing the intent.

---

## Change context

- Slug: integrations-cross-tool-install
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission (Ben Huffer)
- Current lifecycle phase: Verify

## Charter and anchor check

A gate you check more than once, not a one-time note. Confirm it before Plan, and check it again before Verify. See `staying-on-mission`.

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: evidence over persuasion; graded rigor; baseline discipline.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | no non-goal or charter article was crossed | n/a | FlyFission |

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Add `ng install` with per-tool `install_dest`, profiles, `--dest`, `--dry-run` | REQ-001, REQ-003 | none | install + dest-resolution tests | tests green |
| 2 | Confirm each tool's skills path against official docs; correct VS Code and Windsurf | REQ-001, REQ-003 | step 1 | first-party doc check | paths confirmed or flagged |
| 3 | Add `.codex-plugin/plugin.json` and bump + mirror the version | REQ-004 | none | manifest + version-sync tests | mirrors in sync |
| 4 | Add the opt-in MCP server and `ng mcp-config`; keep base zero-dep | REQ-002 | none | `mcp-smoke` job; importorskip tests | server lists 4 tools |

## Two-speed work plan

Keep fast trial work apart from the slower gates where work is accepted.

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | research tool paths; prototype `install_dest` | none |
| candidate | implement subcommands, server, tests | local suite green |
| audit | adversarial self-review; first-party path verification | this packet plus PR review |
| accept | merge PR #42 | human approval plus green CI |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Hardcoding tool paths | wrong/guessed path | skills land in the wrong dir | doc-confirm; `VERIFIED_TOOLS`; `--dest`; runtime note | `verification.md` REQ-003 |
| Version bump | a stale mirror | inconsistent metadata | version-sync test across all mirrors | `verification.md` REQ-004 |

## Agent briefing

- Role: implementing agent on branch `claude/loving-ride-sgg6ww`.
- Authority source: the approved plan and the user's "accomplish everything" instruction.
- Active procedure/template: this Standard packet.
- Last completed action if resumed: Phase 2 and Phase 3 pushed to PR #42.
- Handoff or turnover needed? no.
- Pause when unsure condition: stop and ask if a fix is ambiguous or architecturally significant.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `nuclear_grade/cli.py` | new subcommands and path logic | REQ-001, REQ-003 | the install + config surface | FlyFission |
| `nuclear_grade/mcp_server.py` | new optional server | REQ-002 | the MCP tool surface | FlyFission |
| `pyproject.toml` | optional extra, script, version | REQ-002, REQ-004 | packaging and version | FlyFission |
| `tests/` | install, mcp, version-sync, codex-plugin tests | REQ-001..004 | proof | FlyFission |

## Non-goals

List what this change does not do, on purpose.

- It does not add always-on hooks on install.
- It does not add any runtime dependency to the base install.
- It does not change existing CLI commands, templates, or methodology.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| How to expose the checks as tools | FastMCP optional extra | always-on MCP; a bespoke daemon | leanest; base stays zero-dep | a FastMCP API change |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each requirement is one clear trigger→response statement with a `REQ-NNN` ID, reviewed by a human. | pass |
| Design approved | The design outline in `basis.md` is complete enough for this change and reviewed. | pass |
| Tasks approved | Every build step carries the requirement IDs it delivers, and the sequence is reviewed. | pass |
| Specification reviewed | The protected outcomes, the outcomes to prevent, and the assumptions are stated plainly. | pass |
| Tests/evals defined | Each piece of evidence maps to a claim. | pass |
| Build complete | The affected files match the plan. | pass |
| Verification complete | The evidence is linked in `verification.md`. | pass |
| Release decision ready | The leftover risks and the rollback are recorded. | pass |
| Turnover complete if activated | The next owner has the state, the authority, the stop rules, and the work left to do. | not applicable |

## Rollback approach

- Rollback method: revert the PR #42 commits; the change is purely additive.
- State/data reversal notes: none; no data or state is created.
- Feature flag / kill switch: the MCP server is gated behind the optional `mcp` extra.
- Owner: FlyFission.
- Time to restore estimate: minutes (a single revert).

## Proof commands

```bash
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/integrations-cross-tool-install
pip install -e ".[mcp]" && python -m pytest tests/test_mcp_server.py -q
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: PR #42

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on software lifecycle, keeping the approved version under control (CM), software assurance, secure development, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
