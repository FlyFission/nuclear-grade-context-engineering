# Standard Basis

**Purpose:** State what must stay true for the directive router to be safe, honest, and reviewable.

---

## Change context

- Slug: directive-dispatcher-skill
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-06-08
- Decision this basis supports: ship a directive, advisory `using-nuclear-grade` router.

## Mission / need

Skill auto-invocation is unreliable, and classification is the step most prone to motivated error under pressure. The router should force a spoken risk classification before acting and MUST-promote the cheap "it's only small" traps — as advisory guidance, ahead of (and to be tuned by) the A3 measurement.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The router instructs a mandatory classification before acting | The classification is the load-bearing control | Directive content present; guard test passes |
| The MUST-promote trip-wire names the high-consequence traps | Stops "it's small" downgrades on auth/deps/etc. | Guard test asserts the traps |
| The skill stays within contract + token budget | A broken skill fails CI / loads badly | `test_skill_contracts` + `test_tokens` pass |
| No enforcement/assurance overclaim | It is advisory (rung 1), not a hard gate | Wording review; no "enforce" claim about itself |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| The classification step is silently removed later | The dispatcher reverts to a coin-flip | Guard test (`test_using_nuclear_grade_forces_classification_and_trip_wire`) |
| The skill exceeds its token/contract budget | CI fails; the always-on cost balloons | `test_tokens` + `test_skill_contracts` |
| The skill claims it "enforces" or that the lift is proven | Overclaim the repo condemns | Advisory wording; this packet defers the lift to A3 |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Imperative "MUST" voice raises adherence | assumption | Anthropic skill guidance; plan Lens 5 R3 | A3 shows no lift over a gentler version | FlyFission |
| The directive lift in classification rate is measurable | unknown | Needs a model-in-the-loop A3 run | A3 result | FlyFission |
| The skill auto-loads via its description | fact | Claude Code skill mechanics | Skill loading mechanics change | FlyFission |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The router now instructs a mandatory classification + trip-wire | local proof | the SKILL.md text + guard test | Supports ship |
| The wording measurably lifts classification behavior | unknown (deferred) | A3 measurement | Ship with residual risk; do not claim the lift |

## Interfaces and trust boundaries

- Internal interfaces affected: none (one skill's prose).
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: maintainer reviews the always-on wording.
- AI/model/tool authority boundaries: unchanged — advisory guidance, no hooks, no new authority.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE router SHALL instruct the agent to state the mode + the one fact before acting (classify first, as a declaration of intent) | classification is the control | "Classify first — out loud" step | guard test + read |
| REQ-002 | WHEN a change touches a high-consequence trap THE router SHALL instruct a MUST-promote to Standard-plus | stop motivated downgrades | imperative trip-wire list | guard test |
| REQ-003 | THE directive behavior SHALL be guarded against silent regression | mirrors the mirror-drift discipline | new contract test | the test runs in CI |
| REQ-004 | THE edit SHALL stay within the skill contract and token budget | a broken skill fails / bloats | required sections; <=200 desc / <=3000 body | `test_skill_contracts` + `test_tokens` |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | this basis + `risk.md` |
| Architecture — shape and major parts | yes | one skill's Process / Overview / rationalizations |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data models |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: the approved dispatcher design (revised core).
- Source lineage, if cited: not cited.

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on human performance improvement and graded rigor, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
