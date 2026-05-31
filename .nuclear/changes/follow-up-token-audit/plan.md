# Follow-up to Skills Token Audit (post-rename): Plan

**Purpose:** Bound the work so the build, the review, the verification, and the rollback are planned before the change grows.

**Activation threshold:** Use for Standard changes where the build has several steps, affected controlled items, dependency/model/tool decisions, rollback concerns, or a review order to plan.

**Minimum useful version:** the build sequence, the affected files and assets, the non-goals, the review checkpoints, the rollback approach, and the proof commands.

**Overhead trap:** Do not write a project plan for a small change. Capture only the decisions you need to build and review the change without losing the intent.

---

## Change context

- Slug: `follow-up-token-audit`
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: `@codex[agent]`
- Date: 2026-05-31
- Current lifecycle phase: Execute / Verify / Decide

## Charter and anchor check

A gate you check more than once, not a one-time note. Confirm it before Plan, and check it again before Verify. See `staying-on-mission`.

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes.
- Re-checked before Verify? yes.
- Charter articles in play: listed below.
  - Keep changes minimal and reversible.
  - Tie claims to evidence.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | not applicable | not applicable | not crossed |

## Build sequence

Number the fewest steps needed to finish the change.

1. Generate a Standard change record for this follow-up and fill it with decisions + evidence plan.
2. Update `docs/05-reference/skills-token-audit.md` to match current `ng tokens` numbers and post-rename skill IDs.
3. Run verification commands and update `verification.md` + `ship.md`.

## Two-speed work plan

Keep fast trial work apart from the slower gates where work is accepted.

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | read-only inspection of docs + `ng tokens` output | stop if scope expands to skill merges |
| candidate | edit the change record and the audit doc | `ng validate` passes |
| audit | run `ruff`, `pytest`, `ng doctor/eval/tokens` | all checks green |
| accept | finalize decisions in `ship.md` and update the audit doc narrative | `git diff` matches intended scope |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Copying stale token counts into the audit doc | out-of-date baseline | undermines “measure, don’t assume” | derive numbers from current `ng tokens` output | `verification.md` command output |
| Treating “overlap flagged” as “merge now” | unreviewed structural change | contract/routing churn | explicit stop condition; no skill edits in this follow-up | `git diff` scope review |

## Agent briefing

- Role: update audit docs and record decisions; do not change skill content beyond references/IDs in docs.
- Authority source: this Standard change record + repo instructions.
- Active procedure/template: Standard packet (`risk/basis/plan/trace/verification/ship`).
- Last completed action if resumed: baseline checks ran green (`ruff`, `pytest`, `ng doctor/eval/tokens`).
- Handoff or turnover needed? no.
- Pause when unsure condition: any change implies merging skills or altering skill-body guidance.

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| `.nuclear/changes/follow-up-token-audit/*` | New Standard change record filled | Records decisions and evidence | `@codex[agent]` |
| `docs/05-reference/skills-token-audit.md` | Update baseline numbers + overlap cluster IDs + decisions | Reference used by future work | `@codex[agent]` |

## Non-goals

List what this change does not do, on purpose.

- Merge or delete any skills.
- Rewrite skill bodies to chase token reductions.

## Dependency / model / tool decisions

Use only if activated.

Not applicable: no dependency, model, or tool decisions are part of this doc-only follow-up.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Specification reviewed | The protected outcomes, the outcomes to prevent, and the assumptions are stated plainly. | planned / pass / gap |
| Tests/evals defined | Each piece of evidence maps to a claim. | planned / pass / gap |
| Build complete | The affected files match the plan. | planned / pass / gap |
| Verification complete | The evidence is linked in `verification.md`. | planned / pass / gap |
| Release decision ready | The leftover risks and the rollback are recorded. | planned / pass / gap |
| Turnover complete if activated | The next owner has the state, the authority, the stop rules, and the work left to do. | planned / pass / gap |

## Rollback approach

- Rollback method: revert the commit(s) that touched `docs/05-reference/skills-token-audit.md` and `.nuclear/changes/follow-up-token-audit/`.
- State/data reversal notes: not applicable (no data/state change).
- Feature flag / kill switch: not applicable.
- Owner: maintainers.
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m ruff check .
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py eval .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/follow-up-token-audit
```

## Required links

- `risk.md`
- `basis.md` or `spec.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Skill audit doc: `docs/05-reference/skills-token-audit.md`

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software lifecycle, keeping the approved version under control (CM), software assurance, secure development, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
