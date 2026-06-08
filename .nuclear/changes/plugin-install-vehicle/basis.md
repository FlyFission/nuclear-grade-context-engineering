# Standard Basis

**Purpose:** State what must stay true for the one-line plugin install to be safe, honest, and reviewable.

---

## Change context

- Slug: plugin-install-vehicle
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-06-08
- Decision this basis supports: ship a no-hooks plugin install vehicle.

## Mission / need

Adopters currently copy Markdown by hand or run the `ng` CLI. The repo should install as a Claude Code plugin in two commands, packaging the existing skills and command prompts, without auto-running any code or overclaiming.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The documented install works as written | A broken manifest blocks every adopter | Manifests match the current official schema; parse clean; packaging test green |
| No hooks are configured, so nothing auto-runs | Avoids any new auto-executed / supply-chain surface | no `hooks/hooks.json`; the bundled `ng` CLI runs only when invoked |
| Version stays single-sourced | Plugin/package version drift misleads adopters | `test_plugin_version_tracks_pyproject` passes |
| No enforcement/assurance overclaim | The repo's whole brand is anti-overclaiming | Install docs reviewed; `test_public_docs` boundary check green |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Manifest fails to install | Adopters bounce at the front door | Schema verified against official docs; parse + structure tests |
| Executable hooks ship unnoticed | New trust surface, against doctrine | No-hooks tier; structure test asserts only manifests in `.claude-plugin/` |
| plugin.json / pyproject version drift | Confusing or silent updates | Version-sync test |
| Docs imply the plugin "enforces" | Overclaim the repo condemns | Honest wording; boundary note; public-docs test |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Skills (`skills/*/SKILL.md`) and commands (`commands/*.md`) auto-discover from the plugin root | fact | Official Claude Code plugin docs | Docs/schema change | FlyFission |
| `source: "./"` resolves for a repo-as-marketplace added via GitHub | fact | Official marketplace docs | A live install fails on a Claude Code surface | FlyFission |
| Live `/plugin install` cannot be run in this container | fact | No Claude Code CLI in CI | n/a | FlyFission |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Manifests match the current schema | source claim + local proof | Official docs + JSON parse + packaging test | Supports ship |
| Install works end-to-end | unknown (deferred) | Needs a live Claude Code surface | Ship with residual risk; maintainer smoke-test |

## Interfaces and trust boundaries

- Internal interfaces affected: none (additive manifests).
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: maintainer reviews public wording and runs the live install.
- AI/model/tool authority boundaries: unchanged — no executable hooks in this tier.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN a user runs the documented marketplace-add + install commands THE SYSTEM SHALL expose the existing skills and commands as the `nuclear-grade` plugin with no hooks configured | two-command install need | schema-correct manifests; auto-discovery; no `hooks/hooks.json` | schema check + parse + packaging test + deferred live install |
| REQ-002 | THE plugin manifest version SHALL equal the `pyproject` package version | avoid drift | single-source guard | `test_plugin_version_tracks_pyproject` |
| REQ-003 | THE plugin SHALL configure no auto-run hooks (no `hooks/hooks.json`) in this tier | no auto-executed trust surface | components at root; no `hooks/hooks.json` | structure + no-auto-activation tests |
| REQ-004 | Public install docs SHALL lead with the plugin and SHALL NOT claim the project "does not package as a plug-in" | honest, current docs | INSTALL.md / README edits | `test_public_docs` + review |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | this basis + `risk.md` |
| Architecture — shape and major parts | yes | two manifests + auto-discovered skills/commands |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data models |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: the approved plugin-packaging plan.
- Source lineage, if cited: not cited.

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on design basis, configuration management, and release readiness, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
