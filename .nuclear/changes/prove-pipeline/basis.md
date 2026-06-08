# Standard Basis

**Purpose:** State what must stay true for the PROVE subagent pipeline to be safe, honest, and reviewable.

---

## Change context

- Slug: prove-pipeline
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-06-08
- Decision this basis supports: ship five PROVE subagent definitions with an honest authority split.

## Mission / need

The doctrine demands a plan/build/verify/decide/learn authority split. Encoding it as five subagents with tool boundaries makes the split *visible and tool-enforced* — provided we do not claim a confinement the plugin cannot deliver.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Each stage's tools match its authority | The split is the whole value | authority-split test |
| The judge is read-only and independent of the runner | The verdict is not self-review | judge tools = read-only |
| The observer cannot write product code | It cannot fix code to pass its own evidence | observer has no Edit/Write |
| The pipeline does not overclaim confinement | The repo's brand is anti-overclaiming | README documents the F6/A7 limit |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| An agent's tools contradict its stage | The authority split is a fiction | authority-split test |
| README advertises a perimeter | Overclaim the doctrine condemns | README states "not a perimeter"; F6 caveat |
| Always-on fan-out on trivial work | Busywork the lifecycle rejects | Standard+-only; documented |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Subagent frontmatter (`name`/`description`/`tools`) defines authority | fact | official Claude Code subagent docs | schema change | FlyFission |
| Plugin subagents cannot pin `permissionMode` | fact | official docs / finding F6 | platform adds plugin permissionMode | FlyFission |
| A live multi-agent run is not exercised here | fact | no live orchestration in CI | n/a | FlyFission |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The five defs encode the authority split | local proof | the defs + the authority-split test | Supports ship |
| The split confines a real agent at runtime | unknown (limited) | plugin cannot pin permissionMode (F6) | Ship as advisory; document the limit |

## Interfaces and trust boundaries

- Internal interfaces affected: none (new agent defs).
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: the planner→runner human gate is documented in the defs.
- AI/model/tool authority boundaries: each def declares its `tools`; real `permissionMode` confinement is out of plugin reach (F6).

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE pipeline SHALL define exactly the five PROVE subagents with valid frontmatter | the PROVE map | `agents/*.md` | roster + frontmatter test |
| REQ-002 | EACH stage's `tools` SHALL encode its authority (read-only judge/planner-over-code; no observer writes; runner build authority) | the authority split | per-stage `tools` lists | authority-split test |
| REQ-003 | EACH def SHALL carry the baton-pass contract (Context Pack + closed-loop confirm + data-fence + halt-on-failure) | safe handoffs | the agent bodies | review + read |
| REQ-004 | THE README SHALL document the honesty limit (not a perimeter; plugin cannot pin permissionMode; trust-bearing work needs rung-4/5) | anti-overclaim | `agents/README.md` | README caveat test |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | this basis + `risk.md` |
| Architecture — shape and major parts | yes | five subagent defs + README |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data models |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes`; halt-on-failed-handshake in the defs |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: the approved plan (Phase 4) + A7/F6.
- Source lineage, if cited: not cited.

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on configuration management and human performance improvement, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
