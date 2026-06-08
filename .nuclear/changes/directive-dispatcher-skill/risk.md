# Standard Risk

**Purpose:** Sort the dispatcher-skill change by risk, justify Standard mode, and name the records turned on.

---

## Change identity

- Slug: directive-dispatcher-skill
- PR / issue: Make `using-nuclear-grade` a directive dispatcher (advisory, no hooks)
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide
- Current work phase: accept
- Summary: Rewrite the `using-nuclear-grade` router skill to be directive: a mandatory "classify first, out loud" step (a declaration of intent, not a request for permission), an imperative MUST-promote trip-wire on the high-consequence "it's only small" traps (auth, data/migration, dependencies, model ids, `.github/`, public wording), and the classification rationalizations — all in imperative voice. It stays an advisory **skill** — no executable hooks, no SessionStart/PreToolUse. Adds a guard test so the directive behavior cannot silently regress.

## Mission anchor

- Objective: make the always-first router force a spoken risk classification before acting, and MUST-promote the cheap traps, without shipping executable code or overclaiming.
- Success criteria: the directive content is present and guarded by a test; the skill stays within its contract and token budget; the full suite is green.
- Non-goals / forbidden directions: no executable hooks; no SessionStart/PreToolUse; no edits to other skills; no enforcement claim; no claim that the wording *measurably* lifts behavior (that is the deferred A3 measurement).
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: the approved plan (revised dispatcher = forced spoken classification as intent declaration; Lens 1 + Lens 5 convergence; R3 imperative voice).

## Questioning-attitude summary

- Decision question: can the router be made directive (force the classification) safely and advisorily, before the A3 measurement?
- Evidence that would change the decision: A3 showing a directive preamble does not lift classification rate (then revisit directiveness or go to hooks), or the edit breaking the skill contract / token budget.
- Assumptions that changed the mode: imperative "MUST" voice raises adherence (Anthropic guidance, plan Lens 5 R3), but the *magnitude* is unmeasured here.
- Facts still needing validation: the behavioral lift itself — the A3 classification-rate measurement (needs a model-in-the-loop run; cannot run in this container).
- Stop or hold conditions: stop if the edit would add executable hooks, claim enforcement, or exceed the skill body / description budget.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/using-nuclear-grade/SKILL.md` | Always-on router skill (prompt) | Guides every session's classification | `skills/using-nuclear-grade/SKILL.md` |
| `tests/test_skill_contracts.py` | Test | Guards the directive behavior + the contract | `tests/test_skill_contracts.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Edits an always-on router that ripples to every adopter/session; but advisory and reversible. |
| Reversibility | high | Revert the SKILL.md and test edits; no state, no code. |
| Detectability | high | Guard test + skill-contract test + token budget + `pytest` cover it. |
| Exposure | medium | Public, agent-facing skill prose. |
| Uncertainty | medium | The behavioral lift is unmeasured (the A3 go/no-go). |
| Dependency trust | low | No new dependency. |
| AI authority | low | Advisory guidance only; grants no new agent authority; no hooks. |

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
- Why this mode: it changes the guidance an always-on router gives every session (an AI-behavior / prompt change) and ripples to every adopter.
- Why lighter mode is not enough: Quick fits local reversible docs; this reshapes how the router classifies every change, which warrants a basis, a plan, a trace, and a release decision.
- Why heavier mode is not yet required: advisory prose edit to one skill, reversible, no executable code/permission/data; matches the `incorporate-planning-lessons` precedent (Core-skill edits → Standard).

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline in this risk record. | FlyFission |
| `basis.md` | yes | What must stay true about the directive router. | FlyFission |
| `verification.md` | yes | Evidence for the directive content + the contract. | FlyFission |
| `ship.md` | yes | Release decision; carries the deferred A3 residual. | FlyFission |
| `turnover.md` | no | Same agent continues; no handoff. | FlyFission |
| `self-check.md` | no | No irreversible critical action. | FlyFission |
| `supplier-trust.md` | no | No external dependency/model/API trust decision. | FlyFission |
| Nuclear subset record | no | Stakes below Nuclear. | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: the skill contract + token budget rules (so the edit stays valid).
- Minimum evidence before merge/release: directive content present + guarded; `pytest`/`ruff`/`doctor`/`tokens`/`validate` green.
- Independent review needed? yes; why: a maintainer should review the always-on wording, and run the A3 measurement to confirm the lift before going more forceful (hooks).

## Required links

- Packet: `.nuclear/changes/directive-dispatcher-skill/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: not invoked.

## Exit criteria

- The mode is justified.
- The artifacts turned on are named.
- Important risks, assumptions, and evidence due are recorded here, not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on human performance improvement, graded rigor, and configuration management, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
