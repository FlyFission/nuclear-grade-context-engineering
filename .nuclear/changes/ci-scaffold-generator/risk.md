# Standard Risk

**Purpose:** Sort the CI-scaffold generator change by risk, justify Standard mode, and name the records turned on.

---

## Change identity

- Slug: ci-scaffold-generator
- PR / issue: Add `ng scaffold-ci` (the hardened rung-4 out-of-band gate generator)
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide
- Current work phase: accept
- Summary: Add `ng scaffold-ci`, a CLI-only subcommand that writes a hardened GitHub Actions workflow into an adopter repo. The workflow is the **rung-4 out-of-band gate** — it runs the change-record validator over `.nuclear/changes/*` on `pull_request`, where the authoring agent cannot edit the check to pass. Hardened per the security review: read-only token, `pull_request` trigger (not the privileged fork-runnable trigger), no secrets, a rung-4 honesty banner, and a SHA-pin recommendation. Also adds `permissions: contents: read` to this repo's own `.github/workflows/ci.yml` so the repo practices what the generator preaches. Tests guard the generator and its hardening.

## Mission anchor

- Objective: give adopters a one-command, hardened CI gate that validates change records, and make this repo's own CI consistent with it.
- Success criteria: the generated workflow is valid YAML, least-privilege, safely triggered, secret-free, and runs the validator; tests guard it; the suite is green.
- Non-goals / forbidden directions: no in-session hooks; no claim the workflow decides engineering adequacy/safety/security; no guessed action SHAs.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: the approved plan (Phase 3 CI scaffolding; the honest rung-4 enforcement) and security finding F5.

## Questioning-attitude summary

- Decision question: can adopters get the real (rung-4) gate with one command, hardened by default?
- Evidence that would change the decision: the generated workflow failing on a real adopter repo, or a hardening property missing.
- Assumptions that changed the mode: it adds a CI/automation surface adopters depend on and edits this repo's `.github/`, so Standard.
- Facts still needing validation: an actual GitHub Actions run on a real adopter repo (verified here by structure + local generation, not a live Actions run).
- Stop or hold conditions: stop if hardening would be dropped, or if the generator would emit unverified action SHAs.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `nuclear_grade/cli.py` | CLI generator | New `scaffold-ci` subcommand + workflow template | `nuclear_grade/cli.py` |
| `.github/workflows/ci.yml` | This repo's CI | Gains a least-privilege `permissions` block | `.github/workflows/ci.yml` |
| `tests/test_ng_cli.py` | Test | Guards the generator + the hardening | `tests/test_ng_cli.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Creates adopter CI + edits this repo's CI; but additive and reversible. |
| Reversibility | high | Revert the cli.py + ci.yml + test edits; generated files live in adopter repos and are deletable. |
| Detectability | high | Generator tests + YAML parse + `pytest` + `doctor` cover it. |
| Exposure | medium | Public CLI; the generated workflow is adopter-facing. |
| Uncertainty | low | Deterministic generator; the only unproven step is a live Actions run. |
| Dependency trust | low | No new dependency; the generated workflow installs the validator from PyPI/git (adopter's choice). |
| AI authority | low | No in-session hooks; no new agent authority. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check / proof |
| Known procedure where following the steps matters | yes | packet path / deviation note |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | no | turnover / context pack |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: it adds an automation/CI surface adopters depend on and edits this repo's `.github/` workflow (a high-consequence area).
- Why lighter mode is not enough: Quick fits local reversible docs; a CI generator + a CI edit warrant a basis, plan, trace, and release decision.
- Why heavier mode is not yet required: deterministic, additive, reversible, no executable in-session code, no new dependency/permission/data.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline in this risk record. | FlyFission |
| `basis.md` | yes | The gate contract and hardening that must hold. | FlyFission |
| `verification.md` | yes | Evidence for the generator + hardening. | FlyFission |
| `ship.md` | yes | Release decision for a new automation surface. | FlyFission |
| `turnover.md` | no | Same agent continues; no handoff. | FlyFission |
| `self-check.md` | no | No irreversible critical action. | FlyFission |
| `supplier-trust.md` | no | No external dependency/model/API trust decision. | FlyFission |
| Nuclear subset record | no | Stakes below Nuclear. | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: the F5 hardening requirements (permissions, trigger, secrets) and the existing CI loop pattern.
- Minimum evidence before merge/release: the generated workflow is valid + hardened; `pytest`/`ruff`/`doctor`/`tokens`/`validate` green.
- Independent review needed? yes; why: a maintainer should run the generated workflow on a real adopter PR once, and confirm the action-SHA-pin posture.

## Required links

- Packet: `.nuclear/changes/ci-scaffold-generator/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: not invoked.

## Exit criteria

- The mode is justified.
- The artifacts turned on are named.
- Important risks, assumptions, and evidence due are recorded here, not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on configuration management, release readiness, and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
