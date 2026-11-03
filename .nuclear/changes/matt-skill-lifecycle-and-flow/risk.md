# Risk: Matt skill lifecycle and flow adaptation

## Selected mode

- **Mode:** Standard
- **Reason:** This changes skill routing, lifecycle metadata, generated command inputs, token gates, public workflow doctrine, templates, tests, packaging behavior, and the evidence used to review future skills.

## Change identity

- Slug: `matt-skill-lifecycle-and-flow`
- PR / issue: PR to be opened
- Owner: FlyFission maintainer
- Date: 2026-08-05
- Current lifecycle phase: Plan
- Current work phase: candidate
- Summary: Adapt Matt Pocock's high-value skill-product patterns without weakening Nuclear-grade evidence, authority, custody, or release controls.

## Mission anchor

- Objective: Make Nuclear-grade easier to route and operate while preserving its stronger assurance spine.
- Success criteria: read-only preflight precedes classification; lifecycle and invocation semantics are machine-verifiable; routing scenarios are executable; aggregate context budgets fail closed; compact-skill pilot preserves command parity; engineering build on-ramps and one lifecycle crosswalk are public and testable; full checks and independent reviews close without P0/P1 blockers.
- Non-goals / forbidden directions: no wholesale import of Matt's skills, no auto-commit or merge authority, no compliance/efficacy claim, no live production change, no mass rewrite of all 29 skills, and no merge without human review.
- Drift check: stop or split the PR if the compact pilot grows into a full-catalog rewrite or if lifecycle changes require a breaking installer migration.

## Questioning-attitude summary

- Decision question: Which Matt patterns improve routing, context economy, and build execution without weakening Nuclear-grade controls?
- Evidence that would change the decision: a failing parity/package gate, routing cases that cannot distinguish neighboring skills, or compact bodies that lose required decision signals.
- Assumptions that changed the mode: the work changes public skills, commands, templates, checkers, and plugin behavior.
- Facts still needing validation: final token deltas, exact package parity, and provider-diverse review of the frozen diff.
- Stop or hold conditions: any beta/deprecated skill leaks into a promoted install, any generated command changes unintentionally, any control is deleted without replacement, or any public claim outruns evidence.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skill-catalog.json` and `nuclear-grade.yaml` | lifecycle/config | Single semantic owner plus compatibility projections | repository root |
| `nuclear_grade/skill_catalog.py`, CLI, generator, token tooling | executable controls | Installer, command, routing, and budget behavior | `nuclear_grade/` |
| `skills/` and `commands/` | agent runtime | Invocation and progressive-disclosure pilot | `skills/`, `commands/` |
| `WORKFLOWS.md`, `CORE.md`, doctrine and templates | public workflow | Build on-ramps, frontiers, reviews, context boundaries, crosswalk | repository docs/templates |
| tests and eval manifests | verification | Lifecycle, routing, projection, and budget gates | `tests/`, `evals/` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Changes public agent-routing and review behavior. |
| Reversibility | high | Branch can be reverted; no external runtime state changes. |
| Detectability | high | Contract, parity, package, routing, token, and full-suite checks. |
| Exposure | medium | Public repo and installed skills. |
| Uncertainty | medium | Invocation/lifecycle schema and compact-body behavior are new. |
| Dependency trust | low | Standard-library implementation; no dependency added. |
| AI authority | medium | Skills influence autonomous routing but grant no credentials or release authority. |
| Controllability | high | PR review and CI precede merge. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Repetitive edits | yes | generated projections, tests, token report |
| Procedure-sensitive work | yes | Standard packet and staged verification |
| New or uncertain work | yes | small pilot, explicit non-goals, independent review |
| Interrupted or handed-off work | possible | branch, packet, and PR preserve state |
| High-stakes critical action | no | no deployment or merge in scope |

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `basis.md` | yes | Requirements and non-goals | maintainer |
| `plan.md` | yes | Bounded build sequence | maintainer |
| `trace.md` | yes | Requirement-to-evidence chain | maintainer |
| `verification.md` | yes | Tests, reviews, and custody | maintainer |
| `ship.md` | yes | PR readiness, not merge authority | maintainer |
| CM records | yes | Skills, templates, checkers, and generated cards are controlled items | maintainer |

## Immediate evidence obligations

- Minimum evidence before build: current main frozen at `3ade94ee994f727098a90ee7c5b69c157b107ddf`; baseline tests, Ruff, doctor, and tokens passed; open PRs #85 and #97 inspected.
- Minimum evidence before merge/release: focused and full tests, Ruff, doctor, tokens, command parity, Codex manifest, strict packet validation, diff check, secret scan, and provider-diverse review with no unresolved P0/P1.
- Candidate decisive claims: lifecycle excludes non-promoted skills from default distribution; routing scoring penalizes misses and over-triggering; aggregate token gates have mutation-tested teeth; compact pilot preserves generated commands.
- Evidence custody: builder writes code and local evidence; external reviewers inspect a frozen diff; GitHub CI supplies remote structural evidence; maintainer retains merge authority.

## Required links

- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `controlled-items.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Scope and mode remain honest.
- Every requirement is traced to implementation and evidence.
- Residual gaps are explicit and do not become release claims.

## Source-lineage note

This packet records a selective adaptation of public skill-workflow patterns mapped in `docs/00-standards-foundation/source-map.md`. It preserves Nuclear-grade's evidence and authority controls and makes no compliance, certification, formal V&V, safety, security, or efficacy claim.
