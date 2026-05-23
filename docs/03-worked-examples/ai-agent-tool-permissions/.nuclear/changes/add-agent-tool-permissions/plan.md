# Plan — Add Agent Tool Permissions

**Purpose:** Bound the worked-example implementation so the first proof chain stays small and reviewable.

---

## Build sequence

1. Write failing tests for C-001:
   - allowed relative write inside workspace;
   - parent traversal denied;
   - absolute path outside workspace denied;
   - symlink escape denied.
2. Implement the smallest reference guard that passes those tests.
3. Capture test output in `verification.md`.
4. Mark C-002/C-003 as deferred/gap rather than pretending they are proven.
5. Run adversarial review against overclaiming, missing evidence, path-edge cases, and release-readiness gaps.
6. Update launch docs only after C-001 is proven.

## Non-goals

- Do not build a full agent runtime.
- Do not build a production sandbox.
- Do not implement external API approval, credential binding, or human approval gates in v0.
- Do not claim the reference guard is sufficient for regulated, production, multi-tenant, container, Windows, or adversarial filesystem environments.

## Design sketch for C-001

```text
requested path
  → combine with workspace root if relative
  → resolve/canonicalize final destination
  → require destination.relative_to(workspace_root)
  → write + audit allow OR deny + audit denial
```

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Failing tests observed before implementation | Import failure for missing reference package demonstrates RED state. | pass |
| C-001 tests pass | `4 passed` from pytest. | pass |
| Packet records updated | `risk.md`, `basis.md`, `trace.md`, `verification.md`, `ship.md`. | pass |
| Adversarial review completed | `adversarial-review.md`. | pass |
| Validator accepts packet | `tools/ng_validate.py` accepts the completed packet. | pass |

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `adversarial-review.md`
- `../../reference/workspace_guard.py`
- `../../tests/test_workspace_guard.py`

## Exit criteria

- A reviewer can reproduce C-001 evidence from the command in `verification.md`.
- Every shipped claim has a status label.
- Deferred claims are visible and do not block example v0.
- Launch docs link to the packet and keep the no-compliance boundary.

## Source-lineage note

This plan is an original Nuclear-grade worked-example artifact. It applies the repo operating model and public-source lineage summarized in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
