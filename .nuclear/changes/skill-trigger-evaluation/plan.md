# Skill Trigger Evaluation Plan

## Change context

- Slug: skill-trigger-evaluation
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-05-25
- Current lifecycle phase: Verify / Review / Decide

## Build sequence

1. Review current skill-creator guidance and local skill contracts.
2. Update all skill frontmatter descriptions for concrete trigger contexts.
3. Add the shared skill-evaluation prompt bank and link it from reference docs.
4. Extend contract tests for description substance and eval-prompt coverage.
5. Run tests, doctor, and packet validation before release.

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| `skills/*/SKILL.md` | description updates only | Improves trigger accuracy while preserving concise bodies | FlyFission |
| `docs/05-reference/skill-evaluation.md` | new prompt bank | Makes future skill evaluation repeatable | FlyFission |
| `docs/05-reference/skill-authoring-contract.md` | contract wording update | States evaluation coverage expectation | FlyFission |
| `docs/05-reference/README.md` | index update | Makes the prompt bank discoverable | FlyFission |
| `tests/test_skill_contracts.py` | coverage assertions | Keeps skill descriptions and prompt bank from drifting | FlyFission |

## Non-goals

- Do not add per-skill `references`, `scripts`, `assets`, or `agents/openai.yaml` in this change.
- Do not claim the prompt bank proves skill effectiveness.
- Do not change lifecycle vocabulary, command behavior, or packet templates.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| Eval artifact location | Shared reference doc | Per-skill docs | Keeps skill folders lean | Repeated skill-specific eval failures |
| Description length | 90 to 180 chars | Very short or unlimited descriptions | Balances trigger context with compact metadata | Contract test failures or tool guidance changes |
| Resource additions | None | Add resources now | No repeated deterministic work observed | Real eval runs show repeated manual work |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Specification reviewed | Protected/unacceptable outcomes and assumptions are explicit. | pass |
| Tests/evals defined | Evidence maps to claims. | pass |
| Build complete | Affected files match plan. | pass |
| Verification complete | Evidence is linked in `verification.md`. | pass |
| Release decision ready | Residual risks and rollback are recorded. | pass |

## Rollback approach

- Rollback method: Revert the commit that updates descriptions, prompt bank, tests, and this packet.
- State/data reversal notes: No stateful data migration.
- Feature flag / kill switch: not applicable.
- Owner: FlyFission
- Time to restore estimate: less than 15 minutes.

## Proof commands

```bash
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/skill-trigger-evaluation
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: public-readiness follow-up

## Exit criteria

- Work is bounded enough to prevent scope creep.
- Review checkpoints are explicit.
- Rollback/restore thinking exists before release.
- Proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade plan inspired by public lifecycle, configuration-management, software assurance, secure-development, release-readiness, and operating-learning sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
