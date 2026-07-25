# Skill Benchmark Findings and Amendment Implementation Plan

> **Implementation note:** If this plan is executed after the current benchmark-readiness PR, work it task-by-task, validating each amendment against the repo's tests and `python tools/ng.py validate` before moving to the next.

**Goal:** Incorporate the all-28 skill efficacy findings into the Nuclear-grade repo as explicit benchmark gates, skill-boundary amendments, SkillsBench live-evaluation tasks, and PR-ready evidence.

**Architecture:** Keep repo-native deterministic checks as Gate 1, use SkillsBench/BenchFlow-compatible task packages as Gate 2 live A/B execution, then feed measured outcomes back into skill amendments and keep/compress/refactor decisions. The current PR should ship the Gate 1 instrumentation, initial boundary fixes, and executable plan for remaining P0/P1/P2 amendments without claiming live efficacy.

**Tech Stack:** Markdown skill files, JSONL benchmark manifests, Python deterministic scorers, pytest, `tools/ng.py`, optional BenchFlow/SkillsBench task packages.

---

## Change context

- Slug: `skill-benchmark-findings-and-amendments`
- Branch: `alfred/skill-audit-efficacy-20260704`
- Scope: all 28 `skills/*/SKILL.md` files, benchmark manifests under `evals/`, scorer tools under `tools/`, tests under `tests/`, reference docs under `docs/05-reference/`
- Non-claim: this work proves structural readiness and benchmarkability; it does **not** prove live skill efficacy until recorded with-skill/no-skill trials are run and scored.

## Findings to incorporate

### P0 before expensive live A/B

| Finding | Repo amendment | Acceptance evidence |
|---|---|---|
| `using-nuclear-grade` can over-trigger or act before enough context exists. | Add provisional read-only discovery rule and deterministic downstream routing table. | Skill body contains a provisional mode rule and route table; route/output cases cover provisional behavior. |
| `rating-change-risk` can choose mode inconsistently. | Add ordered tripwire table and clarify administrative floor / Quick / Standard-plus boundary. | Skill body contains ordered tripwires; output case checks tripwire-driven mode. |
| `briefing-an-agent` and `handing-off-work` overlap. | Keep `briefing-an-agent` for pre-action context packaging; keep `handing-off-work` for unfinished-work responsibility transfer and hard incoming-owner confirmation. | Both skill descriptions and decision contracts include reciprocal discriminator; command cards stay regenerated. |
| Claim/release/source/legal skills overlap. | Encode sequence: source status and legal/safety wording checks feed `proving-claims`; `proving-claims` builds trace; `checking-release-readiness` makes ship/block/defer decision. | Required columns for source status and independence exist in trace/output cases; release skill explicitly consumes proof status rather than building it. |
| `organizing-project-folders` has high token cost. | Run compressed-skill ablation before deciding whether to keep full body, compress, or split references. | Benchmark matrix includes full skill vs concise checklist vs prompt-only; report records decision. |

### P1 after first all-28 live run if measured weak

| Skill | Amendment hypothesis | Measurement trigger |
|---|---|---|
| `choosing-what-to-control` | Narrow to approved-state tracking, not downstream impact decisions. | Compress/refactor if it ties checklist baseline. |
| `recording-a-known-good-version` | Require exact rebuild identity and accepted-version evidence. | Amend if output cases omit invalidation triggers. |
| `reviewing-code-quality` | Require delete/simplify/justify-keep classification. | Amend if findings are generic style comments. |
| `questioning-attitude` | Compress around decision question, assumptions, decision-changing fact, and routing step. | Amend if broad skepticism does not change outcome. |
| `breaking-down-the-work` | Separate WBS-only structure from delegated stage contracts. | Amend if prompt-only WBS checklist ties full skill. |

### P2 keep mostly as-is, test with fixture-backed cases

`checking-release-readiness`, `closing-stale-packets`, `deciding-who-decides`, `double-checking-before-acting`, `proving-claims`, `recording-what-an-agent-did`, `reporting-shared-defects`, `responding-to-incidents`, `staying-on-mission`, `stress-testing-agent-changes`, `tracking-deficiencies`, and `vetting-outside-code-and-models` are most likely to show value when benchmark tasks contain realistic traps and artifact obligations.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-001 | Every one of the 28 skills must have routing and output benchmark coverage before live A/B starts. | `pytest tests/test_skill_efficacy_coverage.py -q` and scorer manifest validation. |
| REQ-002 | Static readiness must be described as structural completeness only, never as efficacy proof. | Audit markdown/report wording contains the explicit caveat. |
| REQ-003 | P0 boundary fixes already implemented in this branch must be reflected in skills and generated command cards. | `git diff` shows updated skill files and regenerated command cards; `python tools/ng.py eval .` passes. |
| REQ-004 | SkillsBench adoption must be documented as Gate 2, not as a replacement for repo-native Gate 1. | `docs/05-reference/skillsbench-adoption-plan.md`. |
| REQ-005 | Deterministic scorer tools must reject bad manifests and duplicate observations. | `pytest tests/test_skill_route_score.py tests/test_skill_output_score.py -q`. |
| REQ-006 | The PR must include clear next-step decisions for P0/P1/P2 amendments and live A/B execution. | PR body checklist and this implementation plan. |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters |
|---|---|---|---|
| `tools/ng_skill_audit.py` | Static skill readiness audit; caveats that score is structural only. | REQ-001, REQ-002 | Prevents structural completeness from being mistaken for measured efficacy. |
| `tools/ng_skill_route_score.py` | Deterministic route-case validator/scorer. | REQ-001, REQ-005 | Measures trigger coverage and over-triggering. |
| `tools/ng_skill_output_score.py` | Deterministic required/forbidden signal scorer. | REQ-001, REQ-005 | Measures concrete output obligations. |
| `evals/skill-routing-cases.jsonl` | 158 routing cases covering all skills with positives and near-miss negatives. | REQ-001 | Ensures full-corpus trigger coverage. |
| `evals/skill-output-cases.jsonl` | 29 output cases with required/forbidden signals. | REQ-001 | Ensures each skill has a measurable output contract. |
| `docs/05-reference/independent-skill-benchmark-protocol.md` | Gate protocol for prompt-only vs skill-loaded comparisons. | REQ-002, REQ-006 | Defines fair comparison and avoids vibe scoring. |
| `docs/05-reference/skillsbench-adoption-plan.md` | Gate 2 SkillsBench/BenchFlow adoption plan. | REQ-004, REQ-006 | Provides live-execution architecture. |
| `docs/05-reference/skill-evaluation.md` | Reframe as minimum prompt bank and point to stricter protocol. | REQ-002 | Aligns existing docs with new benchmark standard. |
| `skills/briefing-an-agent/SKILL.md` | Boundary narrowed to pre-action context packaging. | REQ-003 | Reduces overlap with handoff. |
| `skills/handing-off-work/SKILL.md` | Should retain/strengthen incoming-owner restatement in later P0 pass. | REQ-006 | Distinguishes transfer of responsibility from context pack. |
| `skills/proving-claims/SKILL.md` | Boundary narrowed to claim-to-evidence trace, not release/legal/source verdict. | REQ-003 | Reduces false release decisions from proof-building skill. |
| `skills/creating-change-records/SKILL.md` | Boundary narrowed to packet shell/file/link operations. | REQ-003 | Prevents clerical setup skill from choosing mode/proof/release. |
| `commands/ng-context-pack.md`, `commands/ng-new.md`, `commands/ng-prove.md` | Regenerated command-card wording matching changed skills. | REQ-003 | Keeps user-facing commands consistent with skill bodies. |
| `evals/skill-static-audit/2026-07-04/*.md/json/jsonl` | Static audit results, all-28 findings, recommendations. | REQ-002, REQ-006 | Gives reviewers evidence and next-step queue. |
| `tests/test_*.py` | Unit tests for prompt bank quality, efficacy signal mutation, coverage, and scorer behavior. | REQ-001, REQ-005 | Makes benchmark infrastructure regression-tested. |

## Implementation tasks

### Task 1: Ship Gate 1 benchmark infrastructure

**Objective:** Land deterministic readiness and scoring infrastructure that covers all 28 skills.

**Files:**
- Create: `tools/ng_skill_audit.py`
- Create: `tools/ng_skill_route_score.py`
- Create: `tools/ng_skill_output_score.py`
- Create: `evals/skill-routing-cases.jsonl`
- Create: `evals/skill-output-cases.jsonl`
- Create/modify: `tests/test_skill_*.py`, `tests/test_efficacy_signal_mutations.py`

**Steps:**
1. Validate manifests:
   ```bash
   python tools/ng_skill_route_score.py --cases evals/skill-routing-cases.jsonl --skills-dir skills
   python - <<'PY'
   from pathlib import Path
   from tools.ng_skill_output_score import load_cases, validate_case_skills
   cases = load_cases(Path('evals/skill-output-cases.jsonl'))
   validate_case_skills(cases, Path('skills'))
   print(len(cases))
   PY
   ```
2. Run scorer tests:
   ```bash
   pytest tests/test_skill_route_score.py tests/test_skill_output_score.py tests/test_skill_efficacy_coverage.py -q
   ```
3. Acceptance: all 28 skills covered, no unknown skill references, duplicate observations rejected.

### Task 2: Land P0 boundary amendments already proven safe

**Objective:** Reduce overlap in the areas most likely to distort A/B results.

**Files:**
- Modify: `skills/briefing-an-agent/SKILL.md`
- Modify: `skills/proving-claims/SKILL.md`
- Modify: `skills/creating-change-records/SKILL.md`
- Regenerate: `commands/ng-context-pack.md`, `commands/ng-new.md`, `commands/ng-prove.md`

**Steps:**
1. Ensure each amended skill has a boundary paragraph and decision contract matching its narrower role.
2. Regenerate command cards:
   ```bash
   python tools/ng.py gen-commands
   ```
3. Verify repo-native contract checks:
   ```bash
   python tools/ng.py eval .
   python tools/ng.py tokens .
   ```
4. Acceptance: command cards match skill boundaries and validator/token checks pass.

### Task 3: Record findings and next amendments

**Objective:** Put independent findings, risks, and recommended updates in durable repo docs.

**Files:**
- Create: `evals/skill-static-audit/2026-07-04/all-28-efficacy-evaluation.md`
- Create: `evals/skill-static-audit/2026-07-04/recommendations.md`
- Create: `docs/05-reference/independent-skill-benchmark-protocol.md`
- Create: `docs/05-reference/skillsbench-adoption-plan.md`
- Create: `docs/05-reference/skill-benchmark-amendment-plan.md`

**Steps:**
1. State clearly that static scores are structural readiness, not live efficacy.
2. Record P0/P1/P2 amendment queue.
3. Record SkillsBench as Gate 2 live execution layer.
4. Acceptance: docs provide enough information for a reviewer to reproduce the next benchmark phase.

### Task 4: Draft and open the PR

**Objective:** Package the branch as a draft PR for review without overstating the claim.

**PR title:** `test: add all-28 skill benchmark readiness gates`

**PR body must include:**
- Summary of Gate 1 infrastructure.
- P0 boundary amendments included in the branch.
- Explicit caveat: no live efficacy claim yet.
- Test plan with exact commands run.
- Reviewer focus areas.
- Next-step checklist for SkillsBench Gate 2 and remaining amendments.

**Commands:**
```bash
git diff --check
pytest -q
python tools/ng.py eval .
python tools/ng.py tokens .
git add <intended files>
git commit -m "test: add all-28 skill benchmark readiness gates"
git push -u origin HEAD
gh pr create --draft --title "test: add all-28 skill benchmark readiness gates" --body-file /tmp/nuclear-grade-skill-benchmark-pr.md
```

**Acceptance:** draft PR exists, branch pushed, tests listed in PR body.

## Gate 2 SkillsBench execution spec

### Package layout

```text
evals/skillsbench/tasks/<task-id>/
  task.md
  environment/
    Dockerfile
    fixtures...
    skills/<skill-name>/SKILL.md
  oracle/
    solve.sh
  verifier/
    test.sh
    test_outputs.py
```

### Minimum pilot tasks

| Task family | Primary skills | Verifier target |
|---|---|---|
| Public claim hardening | `checking-source-claims`, `checking-legal-and-safety-wording`, `proving-claims`, `checking-release-readiness` | Public copy contains no unsupported compliance/safety claims; trace has source-status and independence columns; release decision is ship/block/defer. |
| Packet repair and closure | `creating-change-records`, `closing-stale-packets`, `checking-what-a-change-affects`, `recording-a-known-good-version` | Packet files, terminal marker, controlled-item impact actions, accepted baseline record. |
| Agent authority incident | `deciding-who-decides`, `declaring-intent`, `double-checking-before-acting`, `responding-to-incidents` | Protected action escalated; target/state verified; incident log separates fact/hypothesis/action. |
| Project decomposition and handoff | `breaking-down-the-work`, `organizing-project-folders`, `briefing-an-agent`, `handing-off-work` | WBS, folder map, context pack, incoming-owner confirmation. |

### Benchmark variants

For each task, run:

1. naive prompt-only
2. best-practice prompt-only
3. equal-token generic checklist
4. skill description only
5. full skill
6. compressed-skill ablation for high-token skills
7. irrelevant-skill control

### Scoring

- Deterministic verifier reward first.
- Required/forbidden signal score second.
- Decision-movement bit third: mode, escalation, ship/block/defer, evidence bar, owner, downstream notification, terminal state, or artifact completeness.
- Blind pairwise review only for ties.

## Verification checklist for this PR

```bash
git diff --check
pytest -q
python tools/ng_skill_route_score.py --cases evals/skill-routing-cases.jsonl --skills-dir skills
python - <<'PY'
from pathlib import Path
from tools.ng_skill_output_score import load_cases, validate_case_skills
cases = load_cases(Path('evals/skill-output-cases.jsonl'))
validate_case_skills(cases, Path('skills'))
print(f'Loaded {len(cases)} output case(s); all references valid')
PY
python tools/ng_skill_audit.py --root . \
  --jsonl evals/skill-static-audit/2026-07-04/skill-audit.jsonl \
  --markdown evals/skill-static-audit/2026-07-04/skill-audit.md
python tools/ng.py eval .
python tools/ng.py tokens .
```

## Exit criteria

- All 28 skills have deterministic route/output coverage.
- Static audit and docs clearly avoid claiming live efficacy.
- P0 boundary amendments included in this PR are reflected in command cards.
- SkillsBench adoption is documented as the live A/B layer.
- Draft PR body identifies remaining P0/P1/P2 work and reviewer focus areas.
