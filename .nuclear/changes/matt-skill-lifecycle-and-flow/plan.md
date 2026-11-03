# Plan: Matt skill lifecycle and flow adaptation

## Change context

- Slug: `matt-skill-lifecycle-and-flow`
- Mode: Standard
- Owner: FlyFission maintainer
- Current lifecycle phase: Plan

## Charter and anchor check

- Mission anchor confirmed before Plan: yes.
- Re-check before Verify: pending.
- Charter articles: questioning attitude, graded rigor, evidence over persuasion, baseline discipline, honest reporting.

## Build sequence

| # | Task | Reqs | Blocked by | Inputs | Outputs | Proof | Frontier / done |
|---|---|---|---|---|---|---|---|
| 1 | Add lifecycle registry and parser; validate paths, status, invocation, role, commands, successors, and projections | REQ-002, REQ-003, REQ-009 | none | catalog, CLI, generator, package tests | registry, module, RED/GREEN tests | focused pytest | active until lifecycle tests pass |
| 2 | Extend catalog routing scorer and add overlap scenarios | REQ-004 | 1 | existing route scorer/cases, lifecycle registry | exact-set scorer, scenarios, tests | focused pytest and scorer run | blocked by 1 |
| 3 | Add aggregate token/profile budgets | REQ-005 | 1 | token module, live report, registry | aggregate checks, tests, YAML budgets | focused pytest and `ng tokens` | blocked by 1 |
| 4 | Correct preflight and add workflow adapters/crosswalk | REQ-001, REQ-007, REQ-008 | none | router, CORE, WORKFLOWS, templates, doctrine | revised runtime/docs/templates/tests | focused pytest, doctor | unblocked |
| 5 | Pilot progressive disclosure on selected high-leverage skills | REQ-006, REQ-009 | 1 | skill bodies, prompts, generator | compact skills, assets/references | command parity, tokens, output fixtures | blocked by 1 |
| 6 | Reconcile generated cards, docs, packet, and package surfaces | REQ-009 | 1-5 | all changed canonical files | synchronized candidate | generator check, package tests | blocked by 1-5 |
| 7 | Freeze staged candidate, run full verification, provider-diverse review, and closure fixes | all | 1-6 | staged diff and packet | reviewed candidate | full gate and closure review | blocked by 1-6 |
| 8 | Commit, refresh base, push, open PR, and verify head/mergeability/checks | all | 7 | frozen candidate | reviewable PR | local/remote SHA and GitHub state | blocked by 7 |

## Decision frontier

No user decision is needed before implementation. The user explicitly authorized implementation and a PR. The maintainer retains decisions on merge, release, version bump, and any post-pilot full-catalog rollout.

## Engineering method

- Prototype only in tests or isolated fixtures; no prototype becomes production behavior without a traced requirement.
- Use vertical RED/GREEN slices at public seams: registry parsing, lifecycle filtering, routing scoring, aggregate budgets, generator assets.
- Keep Spec and Standards review findings separate.
- At each major boundary choose Continue, fresh context, handoff, subagent, or compact; record only when context actually changes.

## Non-goals

- Full rewrite of all skills.
- Live API benchmark in deterministic CI.
- Merge, release, deployment, or version publication.
- New dependencies.
- Claims that routing fixtures prove model behavior across hosts.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements and design approved | User authorized the audited recommendation; packet narrows it into REQ-001 through REQ-009 | pass |
| Implementation slices | Each RED/GREEN slice passes focused tests | pass |
| Compact pilot | Decision receipts and command semantics preserved; token delta measured | pass; 1,477 selected-body tokens removed, commands unchanged |
| Spec review | Every requirement has implementation and proof | local pass; provider review pending |
| Standards review | Maintainability, diagnostics, portability, and no unnecessary duplication | provider review pending |
| Full verification | Project pre-PR gate and strict packet validation pass | pass |
| Independent review | No unresolved P0/P1 on frozen candidate | planned |
| PR readiness | Base refreshed; remote head, mergeability, and checks inspected | planned |

## Rollback approach

- Revert the branch or individual commits before merge.
- No persistent data, deployment, credentials, or production state are changed.
- If registry adoption proves breaking, retain the previous YAML lists as compatibility projections and hold the new lifecycle behavior from release.

## Proof commands

```bash
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py eval .
python tools/ng.py gen-commands . --check
python tools/install-codex.py --check
python tools/ng.py validate .nuclear/changes/matt-skill-lifecycle-and-flow --strict-custody --strict-authority
git diff --check
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- All implementation slices and full checks pass.
- Review blockers are resolved or explicitly block PR creation.
- PR is opened for human review without implying merge or release approval.

## Source-lineage note

This plan adapts public skill-workflow methods mapped in `docs/00-standards-foundation/source-map.md` inside Nuclear-grade's existing control loop. It makes no compliance or formal assurance claim.
