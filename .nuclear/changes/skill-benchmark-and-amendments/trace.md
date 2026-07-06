# Standard Trace

**Purpose:** Tie each important claim to its basis, its design and control features, its verification evidence, its release stance, and its gaps.

---

## Change context

- Slug: skill-benchmark-and-amendments
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-07-06

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Both skill amendments were adversarially critiqued before being applied | `basis.md` | `plan.md` steps 5, 10 | Draft → critique → apply loop | local proof | `AMENDMENT_VALIDATION.md`, `MULTI_MODEL_CHECK.md` addendum — both critiques found real issues (a house-style violation; two wording gaps) and both were fixed before validating | shipped, both amendments kept | pass |
| REQ-002 | Every skill Prompt-section change has a regenerated command card and a deliberately updated golden fixture | `basis.md` | `plan.md` steps 5, 10 | `tools/ng.py gen-commands`; `tests/fixtures/command_prompts.json` | deterministic test | `test_command_parity.py` green after both amendments and after the `main` merge | shipped | pass |
| REQ-003 | A validation result that contradicts an amendment's justification is reported as open, not fixed | `basis.md` | `plan.md` step 10 | Status table wording discipline | local proof | `evals/skill-benchmark-pilot/README.md` status table: `creating-change-records` marked "WINS on Sonnet; unresolved on Haiku," not WINS | shipped as an honest open item | pass |
| REQ-004 | Conflicts with `main` or a parallel open PR touching the same files are reconciled explicitly, not silently overwritten | `basis.md` | `plan.md` steps 9, 11 | PR comments on #63; explicit `git merge` against `origin/main` | local proof | Two PR #63 comments (overlap flagged; `creating-change-records` resolution reported back); merge commit `eb3b016` with one real conflict resolved and reasoning stated | `briefing-an-agent` conflict with PR #63 remains a maintainer decision — flagged, not resolved | gap (owned, see Open trace gaps) |
| REQ-005 | Statistical significance is disclosed even when unflattering | `basis.md` | `plan.md` step 8 | Benjamini-Hochberg correction across all 47 tests (corrected from 44 after Codex found 3 closeout rechecks missing from the family) | local proof | `STATISTICAL_ANALYSIS.md`: 0 of 47 tests survive correction, stated as the document's headline finding, not softened | shipped, stated prominently | pass |

## Evidence chain

```text
Risk / need
  → No objective evidence existed for whether skills change model behavior (basis.md: Mission/need)
  → Basis / requirement: REQ-001..REQ-005 (adversarial review, artifact sync, honest disconfirmation,
    cross-branch reconciliation, disclosed statistics)
  → Control / design feature: draft->critique->apply->validate loop; gen-commands sync; status-table
    wording discipline; explicit git merge; Benjamini-Hochberg correction
  → Verification evidence: evals/skill-benchmark-pilot/*.md, raw transcripts in data/, statistical_summary.json
  → Release decision / rollback / monitoring / baseline trigger: ship.md
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| `briefing-an-agent` has an unreconciled conflict with PR #63's independent version | Two different fixes for the same diagnosed problem exist on two open PRs; only one has live validation behind it | defer | Whoever merges #62/#63 (FlyFission) | Either PR is merged, or the other is updated/closed |
| `creating-change-records` does not work reliably on `claude-haiku-4-5` even after an amendment attempt | The skill's benefit is Sonnet-specific for at least this one scenario; the amendment shipped is a small improvement, not a fix | accept (as a stated, open limitation) | FlyFission | A future amendment attempt with a different approach, or evidence the gap doesn't matter in practice |
| Oracle-based verification and full 28-skill multi-model coverage are unbuilt | Both were part of the original self-audit's gap list; both were correctly re-scoped down after an adversarial critique found the original cost/feasibility premises wrong | defer | FlyFission | Budget/scope explicitly allocated for either |
| No third-party/independent replication has occurred | Every scenario, criterion, and amendment in this packet was authored or reviewed by the same overall effort | defer | FlyFission | An outside reviewer re-runs or re-scores any part of this work |
| This packet was written retroactively, at Review phase, not before Plan | The repo's own process expects a packet before or during build, not after; this is itself a process gap being named rather than hidden | accept (named here) | FlyFission | Future work of this scale should scaffold a packet before starting, not after |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `evals/skill-benchmark-pilot/`, `skills/briefing-an-agent/SKILL.md`, `skills/creating-change-records/SKILL.md`, PR #62, PR #63

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → specification/basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on requirements tracing, verification, keeping the approved version under control (CM), software assurance, secure development, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
