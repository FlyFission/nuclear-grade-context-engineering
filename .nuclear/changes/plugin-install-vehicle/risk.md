# Standard Risk

**Purpose:** Sort the plugin-packaging change by risk, justify Standard mode, and name the records turned on.

---

## Change identity

- Slug: plugin-install-vehicle
- PR / issue: Package the repo as a one-line-install Claude Code plugin (no-hooks tier)
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide
- Current work phase: accept
- Summary: Add `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` so the repo installs as a Claude Code plugin (two commands) that exposes the existing skills and command prompts. This is the no-hooks tier — no hooks are configured, so nothing auto-runs; the repo-as-marketplace source also copies the bundled `ng` CLI, which runs only when invoked. Adds `tests/test_plugin_packaging.py` (manifest validity, version-sync with `pyproject.toml`, structure gotchas) and updates the public install docs to lead with the plugin and drop the now-false "does not package as a plug-in" statements.

## Mission anchor

- Objective: a one-line install that exposes the existing Markdown skills/commands as a plugin, without shipping auto-run code or overclaiming.
- Success criteria: schema-correct manifests (per official Claude Code docs); version single-sourced with `pyproject`; honest install docs; full suite + doctor + tokens + validate green.
- Non-goals / forbidden directions: no executable hooks; no SessionStart/PreToolUse behavior; no enforcement claims; no change to the `ng` CLI; no edits to command/skill bodies.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: the approved plugin-packaging plan and the originating session.

## Questioning-attitude summary

- Decision question: can the repo be made one-line installable without adding an executable trust surface or an overclaim?
- Evidence that would change the decision: a live `/plugin install` failing on a Claude Code surface, or the manifest schema differing from current docs.
- Assumptions that changed the mode: the no-hooks tier adds no auto-run code, but it does add a public distribution surface — a promise to adopters — so Standard, not Quick.
- Facts still needing validation: the live `/plugin install` smoke-test on an actual Claude Code surface (cannot run in this CI container).
- Stop or hold conditions: stop if the install would require executable hooks, or if any doc would imply the in-session plugin "enforces" anything.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `.claude-plugin/plugin.json` | Plugin manifest | Defines the installable plugin | `.claude-plugin/plugin.json` |
| `.claude-plugin/marketplace.json` | Marketplace manifest | Repo as its own marketplace | `.claude-plugin/marketplace.json` |
| `tests/test_plugin_packaging.py` | Test | Guards manifest validity + version-sync | `tests/test_plugin_packaging.py` |
| `INSTALL.md` | Public doc | Leads with the plugin install | `INSTALL.md` |
| `README.md` | Public doc | Adds the one-line install to Quick start | `README.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | New public install surface adopters rely on; but additive and reversible. |
| Reversibility | high | Delete `.claude-plugin/` and revert the doc edits; no state, no migration. |
| Detectability | high | Manifests parse + match the documented schema; packaging test + `pytest` + `doctor` cover it. |
| Exposure | medium | Public repo; manifests + install docs are adopter-facing. |
| Uncertainty | medium | Live `/plugin install` cannot be exercised in this container; deferred to a Claude Code surface. |
| Dependency trust | low | No new dependency; pure-stdlib test; inert JSON. |
| AI authority | low | No executable hooks; the plugin grants no new agent authority in this tier. |

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
- Why this mode: it adds a public distribution surface adopters will depend on (a "release consequence" trigger) and edits public install docs.
- Why lighter mode is not enough: Quick fits local reversible docs; this introduces a new install contract worth a basis, a plan, a trace, and a release decision.
- Why heavier mode is not yet required: no auto-run code, no new dependency/permission/data/auth, fully reversible; Nuclear/Incident triggers do not apply. The later hooks tier will warrant Standard+ with a security review.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline in this risk record. | FlyFission |
| `basis.md` | yes | The install contract and what must stay true. | FlyFission |
| `verification.md` | yes | Evidence for the manifest + version-sync claims. | FlyFission |
| `ship.md` | yes | Release decision for a new install surface. | FlyFission |
| `turnover.md` | no | Same agent continues; no handoff. | FlyFission |
| `self-check.md` | no | No irreversible critical action. | FlyFission |
| `supplier-trust.md` | no | No external dependency/model/API trust decision. | FlyFission |
| Nuclear subset record | no | Stakes below Nuclear. | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: the official plugin/marketplace schema, confirmed against current Claude Code docs.
- Minimum evidence before merge/release: manifests parse + match schema; `pytest`/`ruff`/`doctor`/`tokens`/`validate` green; honest install docs.
- Independent review needed? yes; why: a maintainer must run the live `/plugin install` on a Claude Code surface (this container cannot) and review the public wording.

## Required links

- Packet: `.nuclear/changes/plugin-install-vehicle/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: not invoked (packaging change).

## Exit criteria

- The mode is justified.
- The artifacts turned on are named.
- Important risks, assumptions, and evidence due are recorded here, not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on graded quality, configuration management, software lifecycle, and release readiness, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
