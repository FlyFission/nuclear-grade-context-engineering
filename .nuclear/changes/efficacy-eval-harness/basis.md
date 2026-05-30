# Basis

## Change context

- Slug: efficacy-eval-harness
- Scope: A reproducible presence-check harness over worked-example artifacts, with three eval cases, a CLI subcommand, a bounded doc, and tests.
- Outcome to protect: The repo's efficacy claims become falsifiable and drift-resistant without overclaiming.

## Need and scope

Before this change, every efficacy claim in the skill-workflow comparison was author-judged on a 1-5 scale with no runnable artifact. A skeptic had to trust the author. This harness adds a small mechanical layer: it reads each real trial-record artifact, isolates the `## Nuclear-Grade Trial` section, and checks that each declared decision signal is present. It does not mechanize the simple-versus-Nuclear-grade comparison, because those author-written meta-sections describe gaps using the same vocabulary as the signals and cannot be scored by substring presence without inflating the result.

## Derived requirements or claims

| ID | Requirement / claim | Evidence planned |
|---|---|---|
| C-001 | `ng eval` scores the three real trial-record artifacts and reports per-case and total decision-signal coverage. | Live run; `tests/test_efficacy.py`. |
| C-002 | The harness fails (exit non-zero) when a worked example drops a required signal. | Teeth test that strips a section and asserts the case fails. |
| C-003 | The harness adds no runtime dependency (stdlib only: json, dataclasses, pathlib). | Clean-venv wheel install; import review. |
| C-004 | The published doc states what the harness does and does not measure, with an explicit non-assurance boundary. | `efficacy-harness.md`. |
| C-005 | Eval cases are plain JSON with signals authored from each scenario's stated risks, easy to review and extend. | `evals/cases/*.json`. |
| C-006 | The command degrades gracefully (exit 0, clear message) when run outside a repo that has `evals/cases/`. | Wheel smoke run from a temp dir; `tests/test_efficacy.py`. |
| C-007 | The comparison's qualitative scope is preserved and cross-linked, not replaced or overstated. | Links added to README and results-summary; boundary note retained. |

## Assumptions, constraints, and invalidation triggers

- Assumption: signal presence is a meaningful, honest proxy for "the artifact surfaces this decision element." Invalidation trigger: a signal phrase appears in unrelated prose; mitigated by scoping to the `## Nuclear-Grade Trial` section and authoring multiple specific phrasings.
- Constraint: zero runtime dependencies, because the package ships as a dependency-free wheel and wheel-smoke installs into a clean venv.
- Constraint: do not present signal presence as proof of correctness, safety, or assurance.

## Acceptance scenarios

- A skeptic clones the repo, runs `python tools/ng.py eval .`, and sees 15/15 coverage across three worked examples with a printed non-assurance caveat.
- A maintainer edits a trial record and removes a decision element; CI fails on the efficacy test until the example or the case is corrected.
- A user installs the wheel and runs `nuclear-grade eval` outside the repo; it reports no cases found and exits 0.

## Required links

- Packet: `.nuclear/changes/efficacy-eval-harness/`
- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- Claims C-001 through C-007 are mapped to plan steps and have evidence rows.

## Source-lineage note

Original Nuclear-grade packet influenced by public software verification and evidence concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
