# Standard Plan Record

**Purpose:** Bound the doctrine-spine update so the build, review, verification, and rollback stay linked.

**Activation threshold:** Use because this change touches multiple controlled artifact families and public agent-facing behavior.

**Minimum useful version:** Build sequence, affected files/assets, non-goals, review checkpoints, rollback approach, and proof commands.

**Overhead trap:** Do not turn the plan into a source essay. Keep it tied to controls and evidence.

---

## Change context

- Slug: doctrine-spine-influence
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-05-30
- Current lifecycle phase: Execute

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? planned
- Charter articles in play: questioning attitude, evidence over persuasion, graded rigor, baseline discipline, plus new doctrine-spine articles.

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | not applicable | not applicable | not applicable |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | Read current docs, skills, commands, templates, and tests | No file acceptance; use findings to shape the packet |
| candidate | Edit controlled docs, skills, commands, templates, and packet records | Keep scope tied to control stack and non-goals |
| audit | Run validation, tests, doctor, boundary scans, and PR review | Address actionable findings before acceptance |
| accept | Commit, push, and request PR/Copilot review | Do not merge until CI and actionable review feedback are clean |

## Build sequence

1. Fill the Standard packet and activated CM/OPEX/baseline records.
2. Update charter and operating docs.
3. Update end-user adoption surfaces.
4. Update downstream-agent skills and command cards.
5. Update Standard templates and skill-evaluation prompts.
6. Run validation, contract tests, public-doc tests, doctor, and boundary scans.
7. Update verification, ship, and baseline records with results.
8. Commit, push, open PR, request/inspect Copilot review, and address actionable feedback.

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Public wording update | Accidental quote, attribution, or assurance claim | Source/legal boundary drift | Quote-exclusion and prohibited-claim scan | `verification.md` |
| Skill/command description change | Contract violation | Downstream agent trigger breakage | Run skill/command contract tests | `verification.md` |
| Template update | New prompt bloat slows users | Adoption friction | Manual Quickstart/template review | `ship.md` |
| PR publication | Unverified public claim | Review trust loss | Validate before commit/push | `verification.md` |

## Agent briefing

- Role: builder/verifier for public workflow-control update
- Authority source: user-approved implementation plan
- Active procedure/template: Standard packet plus CM/OPEX records
- Last completed action if resumed: packet scaffolded
- Handoff or turnover needed? no
- Pause when unsure condition: any need for quotes, new source lineage, validator behavior, dependency/model trust, or broader release posture.

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| `.nuclear/charter.md` and packet files | Doctrine and evidence record | Controlled workflow state | FlyFission |
| README, WORKFLOWS, QUICKSTART, operating docs | User-facing doctrine | Adoption and expectations | FlyFission |
| Selected skills and commands | Agent-facing controls | Downstream execution behavior | FlyFission |
| Standard templates and evaluation prompts | Packet interface and trigger tests | Future user/agent behavior | FlyFission |

## Non-goals

- Add public quotes or named attributions.
- Add a new public doctrine page.
- Change CLI behavior or validator rules.
- Add dependencies, models, API integrations, or release automation.

## Dependency / model / tool decisions

Not activated. No dependency/model/tool change.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Specification reviewed | Protected/unacceptable outcomes and assumptions are explicit. | pass |
| Tests/evals defined | Evidence maps to claims. | pass |
| Build complete | Affected files match plan. | planned |
| Verification complete | Evidence is linked in `verification.md`. | planned |
| Release decision ready | Residual risks and rollback are recorded. | planned |
| PR review complete | Copilot/actionable review feedback is addressed or recorded. | planned |

## Rollback approach

- Rollback method: revert the PR/commit.
- State/data reversal notes: no data or external state changes.
- Feature flag / kill switch: not applicable.
- Owner: FlyFission.
- Time to restore estimate: one revert.

## Proof commands

```bash
python3 tools/ng.py validate .nuclear/changes/doctrine-spine-influence
python3 -m pytest tests/test_public_docs.py tests/test_skill_contracts.py tests/test_command_contracts.py tests/test_ng_validate.py -q
python3 tools/ng.py doctor .
rg -n "quote|quotation|formal|certified|approval|compliant|regulatory adequacy|safe|secure" README.md QUICKSTART.md WORKFLOWS.md docs skills commands templates .nuclear/changes/doctrine-spine-influence
# Also run a local attribution-name scan for the owner-supplied names without adding those names to tracked artifacts.
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: forthcoming PR

## Exit criteria

- Work is bounded enough to prevent scope creep.
- Review checkpoints are explicit.
- Rollback/restore thinking exists before release.
- Proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade plan record inspired by public lifecycle, configuration-management, software assurance, secure-development, release-readiness, and operating-learning sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
