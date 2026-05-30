# Plan — Add Agent Tool Permissions

**Purpose:** Keep the worked-example build small, so the first proof chain stays easy to review.

---

## Build sequence

1. Write failing tests for C-001:
   - an allowed relative write inside the workspace;
   - a denied parent `../` path;
   - a denied absolute path outside the workspace;
   - a denied symlink escape.
2. Build the smallest sample guard that passes those tests.
3. Save the test output in `verification.md`.
4. Mark C-002 and C-003 as deferred or gap. Do not pretend they are proven.
5. Run an attack review against overclaiming, missing evidence, tricky path cases, and release-readiness gaps.
6. Update the launch docs only after C-001 is proven.

## Non-goals

- Do not build a full agent runtime.
- Do not build a production sandbox.
- Do not build external API approval, credential binding, or human approval gates in v0.
- Do not claim the sample guard is enough for regulated, production, multi-tenant, container, Windows, or hostile filesystem setups.

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
| Failing tests seen before the build | The import fails because the package is missing, which shows the RED (failing) state. | pass |
| C-001 tests pass | `4 passed` from pytest. | pass |
| Packet records updated | `risk.md`, `basis.md`, `trace.md`, `verification.md`, `ship.md`. | pass |
| Attack review done | `adversarial-review.md`. | pass |
| Validator accepts the packet | `tools/ng_validate.py` accepts the finished packet. | pass |

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

- A reviewer can repeat the C-001 evidence from the command in `verification.md`.
- Every shipped claim has a status label.
- Deferred claims are visible and do not block example v0.
- The launch docs link to the packet and keep the no-compliance boundary.

## Source-lineage note

This plan is an original Nuclear-grade worked-example artifact. It applies the repo operating model and public-source lineage summed up in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
