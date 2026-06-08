# Standard Risk

**Purpose:** Sort the PROVE-pipeline change by risk, justify Standard mode, and name the records turned on.

---

## Change identity

- Slug: prove-pipeline
- PR / issue: Add the PROVE subagent pipeline (planner/runner/observer/judge/educator)
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide
- Current work phase: accept
- Summary: Add five plugin subagent definitions under `agents/` — `planner`, `runner`, `observer`, `judge`, `educator` — mapping the PROVE beats onto dedicated subagents whose `tools` frontmatter **encodes the authority split** the doctrine demands (read-only planner that writes only the packet; gated runner with build authority that may fan out; observer that gathers evidence but writes no product code; read-only judge independent of the runner; educator that writes baseline/lessons into `.nuclear/`). Each carries the baton-pass contract (Context Pack + closed-loop confirm + data-fence). `agents/README.md` carries the honesty caveat; `tests/test_agents.py` guards the roster, the frontmatter, and the authority split. These are markdown definitions — **no executable code** — opt-in and Standard+-only.

## Mission anchor

- Objective: encode the PROVE authority split as five subagents with a disciplined baton pass, without overclaiming confinement.
- Success criteria: five valid agent defs whose tools match the authority table; the baton-pass contract present in each; the honesty caveat documented; tests green.
- Non-goals / forbidden directions: no executable hooks; no claim of real `permissionMode` confinement from the plugin; no always-on fan-out (Standard+ only).
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: the approved plan (Phase 4); the baton-pass design; findings A7/F6.

## Questioning-attitude summary

- Decision question: can the authority split be encoded as subagents honestly, given the plugin cannot pin `permissionMode`?
- Evidence that would change the decision: an agent def whose tools contradict its stage's authority, or a README that overclaims confinement.
- Assumptions that changed the mode: subagent definitions shape how agents act on changes (an AI-behavior surface), so Standard.
- Facts still needing validation: a live multi-agent orchestration run (verified here by the defs + tests, not a live run).
- Stop or hold conditions: stop if a def would claim a perimeter the packaging cannot deliver.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `agents/planner.md` … `educator.md` | Subagent defs | Encode the PROVE authority split | `agents/` |
| `agents/README.md` | Doc | The baton pass + the honesty caveat | `agents/README.md` |
| `tests/test_agents.py` | Test | Guards roster, frontmatter, authority split | `tests/test_agents.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Shapes multi-agent behavior on changes; but markdown defs, opt-in, reversible. |
| Reversibility | high | Delete `agents/` + the test; no state, no executable code. |
| Detectability | high | Contract test on roster/frontmatter/authority; `pytest`. |
| Exposure | medium | Public, agent-facing definitions. |
| Uncertainty | low | Deterministic defs; the only unproven step is a live orchestration run. |
| Dependency trust | low | No new dependency; no code. |
| AI authority | medium | Defines what each subagent may do — but encodes *limits*, and cannot pin `permissionMode` (F6). |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check / proof |
| Known procedure where following the steps matters | yes | packet path / deviation note |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | yes | turnover / context pack (the baton pass is the subject) |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: subagent definitions shape how agents act on changes (an AI-behavior surface) and encode an authority model.
- Why lighter mode is not enough: Quick fits local reversible docs; an authority-encoding pipeline warrants a basis, plan, trace, and release decision.
- Why heavier mode is not yet required: markdown defs, no executable code, reversible, opt-in, Standard+-only.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline in this risk record. | FlyFission |
| `basis.md` | yes | The authority split + baton-pass contract that must hold. | FlyFission |
| `verification.md` | yes | Evidence for the roster + authority encoding. | FlyFission |
| `ship.md` | yes | Release decision; carries the A7/F6 honesty. | FlyFission |
| `turnover.md` | no | Same agent continues; no handoff. | FlyFission |
| `self-check.md` | no | No irreversible critical action. | FlyFission |
| `supplier-trust.md` | no | No external dependency/model/API trust decision. | FlyFission |
| Nuclear subset record | no | Stakes below Nuclear. | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: the subagent frontmatter schema + the F6 `permissionMode` limit.
- Minimum evidence before merge/release: roster + frontmatter + authority-split tests green; `pytest`/`ruff`/`doctor`/`tokens`/`validate` green.
- Independent review needed? yes; why: a maintainer should review the authority model and run a live orchestration once.

## Required links

- Packet: `.nuclear/changes/prove-pipeline/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: not invoked.

## Exit criteria

- The mode is justified.
- The artifacts turned on are named.
- Important risks, assumptions, and evidence due are recorded here, not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on configuration management, graded rigor, and human performance improvement, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
