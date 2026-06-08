# Standard Basis

**Purpose:** State what must stay true for the CI-scaffold generator to be safe, honest, and reviewable.

---

## Change context

- Slug: ci-scaffold-generator
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-06-08
- Decision this basis supports: ship `ng scaffold-ci` and harden this repo's CI.

## Mission / need

The in-session controls (skills, and any later hooks) are rungs 1-3 — defeatable by the agent that authors a change. The real gate is rung 4: an out-of-band CI check the agent cannot edit to pass. Adopters should get that gate with one command, hardened by default.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The generated workflow is valid and runs the validator | A broken gate protects nothing | YAML parses; the validate loop runs `nuclear-grade validate` |
| The workflow is least-privilege and safely triggered | Avoid the fork-PR write-token/secret-exfil class | `permissions: contents: read`; `pull_request` trigger; no secrets |
| This repo practices what it preaches | Credibility of the generated gate | `ci.yml` gains a `permissions` block |
| Honest about what the gate checks | The check is structural, not adequacy | banner says "structurally complete -- does not decide adequacy" |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Generated workflow uses the privileged fork trigger | Fork PRs run with a write token + secrets | Trigger is `pull_request`; test asserts no `pull_request_target` |
| Generated workflow references secrets | Exfiltration surface | No secrets in the template; test asserts none |
| Unverified action SHAs shipped | A wrong SHA breaks every adopter's CI | Tag-pin + a SHA-pin recommendation comment; do not guess SHAs |
| Overclaiming the gate decides adequacy | Overclaim the repo condemns | Honesty banner; structural-only wording |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| `nuclear-grade` is installable in adopter CI (PyPI or git) | assumption | the package's `pyproject` console script | PyPI not published and git pin stale | FlyFission |
| `pull_request` + read-only token is the safe default | fact | security finding F5; GitHub docs | GitHub Actions security model changes | FlyFission |
| A live GitHub Actions run is not exercised here | fact | no Actions runner in this container | n/a | FlyFission |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The generated workflow is valid + hardened | local proof | YAML parse + generator tests | Supports ship |
| The workflow runs green on a real adopter PR | unknown (deferred) | needs a live Actions run | Ship with residual risk; maintainer smoke-test |

## Interfaces and trust boundaries

- Internal interfaces affected: the `ng` CLI gains a subcommand.
- External services/APIs affected: GitHub Actions (the generated workflow runs there) and PyPI/git (validator install).
- Data classes affected: none.
- Human approval boundaries: maintainer reviews the generated workflow and runs it once.
- AI/model/tool authority boundaries: unchanged in-session; the generated workflow runs with a read-only token.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN a user runs `ng scaffold-ci <repo>` THE SYSTEM SHALL write a valid GitHub Actions workflow that validates `.nuclear/changes/*` | one-command rung-4 gate | the `scaffold-ci` subcommand + template | generator test + YAML parse |
| REQ-002 | THE generated workflow SHALL be least-privilege, `pull_request`-triggered, and secret-free | F5 hardening | the template + a guard test | generator test asserts the properties |
| REQ-003 | THIS repo's `ci.yml` SHALL declare a least-privilege `permissions` block | practice what is preached | the `permissions: contents: read` edit | CI run + read |
| REQ-004 | THE generator behavior SHALL be guarded by tests | regression discipline | new `test_ng_cli` cases | the tests run in CI |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | this basis + `risk.md` |
| Architecture — shape and major parts | yes | a CLI subcommand + a workflow template constant |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data models |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes`; `--force`/`--dry-run` semantics |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: the approved plan (Phase 3) + security finding F5.
- Source lineage, if cited: not cited.

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on configuration management, release readiness, and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
