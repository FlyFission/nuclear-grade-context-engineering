# AI-Assisted PR Review Loop: Plan

## Change context

- Slug: ai-assisted-pr-review-loop
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-07-24
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: minimum sufficient context, evidence before acceptance, human decision authority, no silent standards drift

No non-goal or charter crossing is authorized.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Add a failing public-doc contract for role labels, exact-candidate closure, and correction budget | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005 | Current-main inspection | `tests/test_public_docs.py`; 1 file | Failing focused test | Focused pytest fails because controls are absent | Expected failure observed |
| 2 | Update existing role diagram and text fallback in both canonical copies | REQ-001, REQ-002, REQ-005 | Step 1 | `README.md#Who does what`, `docs/diagrams.md#6`; 2 sections | Mirrored four-role sequence with one controlled candidate artifact | Focused test plus source comparison | Diagram is role-based, candidate-bound, and readable |
| 3 | Add bounded correction planning and exact-candidate ship closure | REQ-003, REQ-004 | Step 1 | Standard plan and ship templates; 2 sections | Operational fields | Focused test and template review | Required fields present with stale-verdict rule |
| 4 | Add compact Standard-loop explanation and change history | REQ-001, REQ-002, REQ-005 | Steps 2-3 | `WORKFLOWS.md`, `CHANGELOG.md`; 2 sections | Public explanation | Public-doc tests and diff review | No new mode or overclaim |
| 5 | Complete packet, full verification, frozen review, commit, push, and PR | REQ-001 through REQ-005 | Steps 1-4 | Candidate tree and packet; bounded to staged diff | Verified PR candidate | Full gates, exact-candidate review, remote checks | PR open with current head verified |

Model-mediated determinism posture: Hermes GPT-5.6 Sol authors the candidate; deterministic checks are replayable; semantic review is judgment and must not be described as deterministic or independent merely because a different provider is used.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | Inspect current main, open PR overlap, and external diagram | Scope selected without duplicate workflow |
| candidate | Edit tests, docs, templates, and packet in isolated worktree | Focused test green and packet coherent |
| audit | Freeze diff; run full gates and reviewer challenge | No unresolved P0/P1 and current candidate identity recorded |
| accept | Commit, push, open PR | GitHub head, mergeability, and checks verified; merge held for human |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Amend public diagram | Overload the simple view | Adoption surface becomes harder to understand | Keep one existing diagram, use role labels, retain text fallback | Reviewer finding and source inspection |
| Record candidate identity | Ask an in-tree record to contain its own commit SHA | Self-referential identity never closes | Use a scoped payload identity plus provenance, with attestation outside the payload | `ship.md` fields and contract test |
| Correction loop | Review forever or lower criteria | Cost and false pass | Fixed budget plus human escalation | Plan fields and review record |
| Open PR | Build on stale or dirty checkout | Conflicts or user-work damage | Isolated worktree from fetched `origin/main` | Git branch and remote OID |

## Agent briefing

- Role: Builder and chair of deterministic verification; not independent semantic verifier.
- Authority source: Direct user request to push the feedback as a PR.
- Active procedure/template: Repository AGENTS guidance, Standard packet, PR release gate.
- Last completed action if resumed: Focused RED and GREEN test cycle completed after docs/template implementation.
- Handoff or turnover needed? no
- Pause when unsure condition: Stop before scope expansion, merge, release, or any claim of independent validation.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `README.md` | Replace the base sequence with four roles plus one candidate artifact | REQ-001, REQ-002, REQ-005 | Public front door | FlyFission |
| `docs/diagrams.md` | Mirror canonical sequence and text fallback | REQ-001, REQ-002, REQ-005 | Controlled diagram source | FlyFission |
| `WORKFLOWS.md` | Add compact Standard-mode PR interpretation | REQ-001, REQ-002 | Prevents new-mode ambiguity | FlyFission |
| `templates/standard/plan.md` | Add review/correction budget fields | REQ-003 | Operationalizes bounded remediation | FlyFission |
| `templates/standard/ship.md` | Add reviewed/current candidate identity gate | REQ-002, REQ-004 | Prevents stale verdict use | FlyFission |
| `tests/test_public_docs.py` | Add contract test | REQ-001 through REQ-005 | Prevents drift | FlyFission |
| `CHANGELOG.md` | Record public change | REQ-005 | Public trace | FlyFission |
| Packet files | Dogfood the change | REQ-001 through REQ-005 | Preserves basis and evidence | FlyFission |

## Non-goals

- No new skill, command, validator flag, packet mode, model router, or CI policy.
- No copying of the external diagram or tying workflow authority to Claude, Grok, Codex, or another vendor.
- No merge, release, or compliance claim.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| Host surface | Existing Standard workflow and role diagram | New standalone workflow or skill | Current repo already owns the full lifecycle | Existing surfaces cannot express the control cleanly |
| Candidate identity | Scoped payload/content identity plus provenance ID and out-of-payload attestation | PR number alone; self-referential in-tree commit SHA | Stable payload closure without asking a commit to contain its own SHA | Target tool lacks a stable payload identity |
| Review loop | Declared correction budget plus human escalation | Fixed one-round rule; unlimited loop | Preserves boundedness without premature stop | Empirical use shows different default needed |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001 through REQ-005 are bounded and testable | pass |
| Design approved | Amend existing surfaces; no parallel workflow | pass |
| Tasks approved | Every step maps to requirements and proof | pass |
| Specification reviewed | Protected and unacceptable outcomes explicit | pass |
| Tests/evals defined | Focused contract plus full repo gates | pass |
| Build complete | Intended files match plan | pass |
| Verification complete | Full local evidence linked in `verification.md`; remote checks are a PR-time gate | pass |
| Release decision ready | Residual risks, identity, and rollback recorded | pass |
| Turnover complete if activated | Not activated | not applicable |

## Review candidate and correction budget

- Acceptance-criteria revision: `basis.md` dated 2026-07-24, REQ-001 through REQ-005
- Human decision owner: Ben/FlyFission
- Builder: Hermes GPT-5.6 Sol
- Criteria challenger function, if activated, and custody note: External friend's diagram prompted the critique; Hermes translated it into criteria; Ben approved PR implementation. This is not independent evidence.
- Verifier and separation rationale: Blind first-round Claude, Codex, and Grok reviews inspected frozen commit `2bc9c00`; OpenCode/Kimi attempts produced no substantive verdict and are not counted. Codex then completed a read-only corrected-candidate delta review of `6cc462a`; Claude and Grok delta attempts did not return reliable final verdicts and are excluded. Model review remains advisory defect discovery.
- Candidate identity method and attestation location: SHA-256 manifest over the changed public/template/test payload; provenance commit recorded separately; final attestation in this packet and PR review, outside the payload scope.
- Identity scope and exclusions: Include `CHANGELOG.md`, `README.md`, `WORKFLOWS.md`, `docs/diagrams.md`, both changed Standard templates, and `tests/test_public_docs.py`; exclude this mutable `.nuclear` decision packet.
- Maximum correction rounds before human escalation: 2
- Current correction round: 1
- Material change that invalidates the current verdict: Any change to README/diagram semantics, Standard plan/ship fields, contract test, or packet claim boundary; any rebase/conflict resolution affecting those surfaces.
- What consumes a correction round: A material payload change followed by a renewed review request. Round 1 addresses accepted role, agency, recursion, re-verification, mirror-test, and delta-review findings from frozen commit `2bc9c00`.
- Escalation action when the budget is exhausted: Hold the PR and present unresolved blockers and options to Ben; do not relax criteria.

## Rollback approach

- Rollback method: Revert the candidate commit or close the unmerged PR.
- State/data reversal notes: No data or runtime state changes.
- Feature flag / kill switch: Not applicable.
- Owner: FlyFission.
- Time to restore estimate: Minutes.

## Proof commands

```bash
python -m pytest tests/test_public_docs.py::test_ai_assisted_pr_loop_closes_the_exact_review_candidate -q
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py eval .
python tools/ng.py gen-commands . --check
python tools/ng.py validate .nuclear/changes/ai-assisted-pr-review-loop --strict-custody
git diff --check
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: direct user instruction; PR URL after creation

## Exit criteria

- Work remains inside the seven intended public/template/test surfaces plus packet.
- Review candidate and correction budget are explicit.
- Exact-candidate identity is checked before a verdict can support merge/apply.
- Full verification and closure review are complete before push.

## Source-lineage note

This plan applies existing Nuclear-grade lifecycle, role-separation, configuration-management, and release-readiness controls whose public lineage is mapped in `docs/00-standards-foundation/source-map.md`. The external diagram is a design prompt, not copied content or formal assurance evidence.
