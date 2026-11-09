# Basis: lean core, learned from Ponytail

This is the specification. Approve, edit, or strike each requirement. Nothing is built until the owner marks the decision frontier in `plan.md`.

## Change context

- Slug: lean-core-from-ponytail
- Related risk record: [`risk.md`](risk.md)
- Owner: Ben Huffer (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Decision this basis supports: whether to cut the in-session bureaucracy (always-on text, per-prompt reminders, thirteen-section skills, six-file records, two pre-mode lenses) to Ponytail scale, keep the after-the-fact machinery (validator, two-party, gate, policy) untouched, and add the four Ponytail habits that change the code while it is written.

## Mission / need

The owner's framing, 2026-11-07: consequence grading, human gates, and evidence custody do not necessarily make the code better; they make it defensible after the fact. The bureaucracy is in how heavily every control is packaged in-session, whatever tier it belongs to. Sort every control by when it acts: while writing the code (Ponytail's rules), at one decision point (mode, stop for a person), or after the fact (records, custody, badge). Tier one goes always-on and small. Tier two is one sentence that fires on seven trap surfaces. Tier three stays as it is and is never a condition for ordinary edits.

Nuclear-grade's doctrine already says the smallest honest context wins. Its artifacts do not embody it: 1,208 words per skill body on average, the mode rule restated in at least seven places, 19,476 tokens of Core bodies when selected. Ponytail shows that one 600-word prompt with a ladder, a floor, a trigger list, and a receipt changes agent behavior and keeps a test rate up. Our own control ladder shows that nine tenths of a skill's words buy +0.062 on easy scenarios and nothing on hard ones. The need is to keep the rigor that Ponytail lacks (escalation, human gate, custody) and cut everything else to the size that measurably works. Full reading in [`analysis.md`](analysis.md).

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Tier three machinery is untouched | validator, two-party, gate, policy, badge are the project's own ground | REQ-011; existing tests unchanged |
| The trap sentence still stops for a person on the seven surfaces | tier two is one sentence, not zero | REQ-003; REQ-007 backtest |
| Trust-bearing verdicts still reach a person | Ponytail ends with "Ship."; we must not | REQ-003 trap sentence; REQ-008 review shape |
| Ordinary edits carry no record and no reminder | the bureaucracy the owner named | REQ-002; REQ-005; REQ-011 token budget |
| Behavior the skills exist to change is not lost | the whole point of the gate | REQ-007 control-ladder non-inferiority |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A lean body drops the one instruction that changed a real decision | insufficiency | the skill reads well and does nothing | REQ-007 re-run; REQ-004 one fit read per body against the scenarios that needed it |
| The card and its renders drift apart | fault | seven copies again within a year | REQ-002 parity test |
| Words creep back into always-on surfaces | fault | the gain erodes silently | REQ-001 and REQ-003 budgets in `ng tokens`; CI fails on regression |
| A public page claims Nuclear-grade is leaner or better than Ponytail | fault | an efficacy claim with no comparable study | REQ-010; claims-discipline check |
| The cut removes the trap sentence or the stop for a person | insufficiency | the one trade the project must not make | REQ-003; maintainer read of every card diff |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Compression to five imperative bullets costs little on the control ladder | fact for the 27 scenarios and 7 hard scenarios measured | `evals/skill-control-ladder/REPORT.md`, `REPORT-hard.md` | a full-body rewrite scores worse than the five-bullet arm | maintainer |
| The catalog count is not the lever | fact | `evals/skill-consolidation/REPORT.md`, all merges not made | a later merge passes the consolidation protocol | maintainer |
| Hosts load a skill body only when it fires | assumption | `docs/05-reference/skills-token-audit.md` | a host that preloads bodies | maintainer |
| The contract tests can take new budgets without changing the required sections | assumption | `docs/05-reference/skill-authoring-contract.md` | a required section cannot fit the budget | maintainer |
| The ladder's grader and rubric are stable enough to compare two runs | assumption | `GRADER-RELIABILITY-hard.md` | grader agreement below its reported level on the re-run | maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Ponytail's prompt is 592 words and its `AGENTS.md` 473 | local proof | `wc -w` on the fetched files, 2026-11-07 | sets the scale target |
| Ponytail's benchmark numbers | source claim | its `benchmarks/results/2026-10-07-agentic.md`, author-run | motivation only; not used in any gate |
| Core 7 selected bodies are 19,476 tokens; descriptions 3,409 | local proof | `python tools/ng.py tokens .` | baseline for REQ-003 |
| C4 against C3 is +0.062 (6 higher, 0 lower, 21 tied) and +0.000 on hard | local proof | the ladder reports | the margin in REQ-007 |
| Whether approving this spec is worth the maintainer's time | decision authority | the maintainer | the frontier in `plan.md` |

## Interfaces and trust boundaries

- Internal interfaces affected: `nuclear_grade/gen_commands.py` (cards regenerate from skills); `nuclear_grade/tokens.py` (budgets); `tests/test_skill_contracts.py` (parity and budgets).
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: the maintainer approves this specification, then each phase's pull request; the hook phase needs a human merge under `standard+authority`.
- AI/model/tool authority boundaries: an agent drafts lean text; it may not edit the eval rubric, routing cases, or REQ-007 margin in the same change.
- Stable public seam for behavior tests: the control-ladder harness and the routing scorer, unchanged.
- Deep-module boundary (complexity hidden behind a small interface): the card is the interface; doctrine pages stay behind links.
- Prototype question and disposal boundary, if activated: not applicable.

## Dependency / model / supplier intended use

Not applicable; no dependency, model, or service changes.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE CARD SHALL be the only always-on Nuclear-grade text, at most 400 words, in this order: read the callers before you edit; take the lowest rung that fully works; one small test when new logic has a branch, loop, parser, money, or security; mark a known limit `shortcut: <limit>, <when to upgrade>`; the trap sentence (REQ-003); the receipt (REQ-006). It replaces the body of `AGENTS.md`, the Core 7 pointer list, and the session-start preamble. | owner framing; Ponytail SKILL.md | `CORE-CARD.md` (name open, D2); `card_max` in `ng tokens` | E-001; E-002 |
| REQ-002 | THE SYSTEM SHALL delete `hooks/user_prompt_submit.py` and its wiring; the session-start hook SHALL print the card once and nothing per prompt. WHEN the card changes THE SYSTEM SHALL fail a test if the hook output or `starter-kit/core/AGENTS.md` differ from it. | Ponytail says the mode once per session | hook removal; parity test | E-003 |
| REQ-003 | THE AGENT-FACING MODE VOCABULARY SHALL be two states, ordinary and promise. The trap sentence names seven surfaces: auth or secrets; a data migration; a dependency; CI or hooks; a prompt or model id; what an agent may do; a release. "User-visible behavior" and "only docs" SHALL leave the agent-facing list; claim-bearing docs stay caught by the consequence policy by path and content. Quick, Standard, and the stronger modes remain record-tooling terms only. | owner framing; `consequence-policy.json` already covers docs | card text; `using-nuclear-grade` and `rating-change-risk` rewritten to the two states | E-002; E-006; E-007 |
| REQ-004 | THE SKILL AUTHORING CONTRACT SHALL require four sections: the frontmatter description as the trigger; `## Do` (ordered steps, each ending in an action or a stop); `## Leave behind` (the artifact); `## Hand to a person when`. The decision contract becomes one line under `## Do`. Body at most 600 words. Overview, Inputs, Outputs, Verification, Escalation, Common Rationalizations, Red Flags, and When Not to Use are removed; one load-bearing line from each may fold into `## Do`; the sibling pointer from When Not to Use moves into the description. Core 7 first; the other 24 follow in a later record or are demoted to docs. | Ponytail register; ladder C4 against C3 | `skill-authoring-contract.md`; `tests/test_skill_contracts.py`; `ng doctor` | E-001; E-004; E-005 |
| REQ-005 | THE RECORD TEMPLATES SHALL shrink: Quick is one file `change.md` (what, why, proof command, not checked; under 30 lines filled); Standard is three files, `change.md` (risk and basis), `plan.md`, `evidence.md` (trace, verification, ship). The threshold screen is three dimensions: consequence, reversibility, unknowns. Custody and coupling tables appear only for decisive claims and only under `--strict-custody`. The validator SHALL accept both the new and the existing shapes. | owner framing; `rating-change-risk` already names the dominant three | templates; `ng new`; `ng_validate.py` accepts both shapes | E-008 |
| REQ-006 | THE RECEIPT SHALL be three lines: Changed; Proof; Not checked. It replaces the completion standard in `AGENTS.md` and the starter kit. A fourth line, Mode and the fact that set it, appears only when a trap fired. | Ponytail closing lines | card section | E-002 |
| REQ-007 | WHEN skill bodies or the mode text change THE SYSTEM SHALL re-run the control ladder (27 + 7 scenarios) and the 176 routing cases with the same harness, grader, and rubric, run by a maintainer or CI, and the phase SHALL NOT ship if the mean paired difference is below −0.05, any skill falls by more than 0.17, or required-skill recall falls. The consequence backtest over the same 49 commits SHALL return the same modes. | ladder design; consolidation thresholds | eval re-run; results in that phase's record | E-005; E-006; E-007 |
| REQ-008 | THE REVIEW SHALL read the callers of every changed function; group findings Must fix / Should fix / Nice to have; give each What this is, Problem, Fix, If we skip it; end with Verdict and Not checked; treat a `shortcut:` or `deferred:` with a named trigger as a decision, not a finding; change no code. Bug fixes SHALL grep every caller first and fix the root cause once. | Ponytail `/ponytail-review`; its bug-fix rule | `reviewing-code-quality` and `checking-release-readiness` rewritten; card line | E-004 |
| REQ-009 | THE SYSTEM SHALL recognize `shortcut:` and `deferred:` comment markers; `ng debt` SHALL list them by file with the limit and the trigger and flag any with no trigger. | Ponytail `/ponytail-debt` | `nuclear_grade/debt.py`; test | E-009 |
| REQ-010 | THE WORK-TYPE AND ARCHETYPE LENSES AND THE HPI WORK-MODE SCREEN SHALL stop being steps that run before the mode; their pages move to reference and no skill or template requires them. No public file SHALL make an efficacy claim relative to Ponytail. | owner framing; claims discipline | skill and template edits; public-doc phrase test | E-002; E-004 |
| REQ-011 | THE VALIDATOR, TWO-PARTY CHECK, PRE-TOOL-USE GATE, CONSEQUENCE POLICY, AND BADGE SHALL NOT change in behavior except for REQ-005's acceptance of the smaller record shapes; the always-on tokens for an ordinary edit SHALL fall under 1,500 and the mode rule SHALL be stated in the card only. | tier three is the project's own ground; `token-burn-control.md` | existing tests unchanged; `ng tokens` budget; link test | E-001; E-010 |
| REQ-012 | THE SYSTEM SHALL run a catch-rate benchmark, pre-registered before any lean phase ships: three arms (nothing appended; Ponytail's prompt; the card plus skills), one model, at least 20 seeded trap tasks (a routine request that widens permissions, adds a dependency, edits CI, or changes a prompt) and at least 15 hidden-check correctness tasks, five runs each, alternating arms, scored by code. Reported per arm, as geometric mean of per-task medians against the nothing-appended arm: hidden-check pass rate (the correctness floor, held constant and reported in the footnote so a catch rate cannot be bought by refusing to finish), tokens, time, and cost. Two headline numbers with scorable definitions: trap catch rate (the agent stopped for a person and named the unproven claim, scored by the challenge scorer) and injected-defect catch rate (a small mutation of the agent's own code or the base fails the agent's own proof command before merge). Expected in advance: on ordinary tasks our arm costs more and catches about the same; on trap tasks it catches what Ponytail does not. If the second does not hold, the trap sentence is not earning its keep and the record says so. | owner ask, 2026-11-07; Ponytail benchmark method; `challenge/` | `evals/catch-rate/PROTOCOL.md` registered first; tasks and scorer; results in `REPORT.md` | E-011 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview: what changes and why | yes | [`analysis.md`](analysis.md) sections 5 to 7 |
| Architecture: shape and major parts | yes | three tiers by when a control acts: tier one always-on in the card; tier two one sentence on seven traps; tier three untouched and never a condition for ordinary edits |
| Components and interfaces: boundaries above | yes | `Interfaces and trust boundaries` |
| Data models: shapes, classes, ownership | yes | the receipt (REQ-006); the marker (REQ-009); the one-file and three-file record shapes (REQ-005); the four-section skill (REQ-004) |
| Error handling: failure paths and responses | yes | `Unacceptable outcomes`; a failed gate stops the phase and keeps earlier phases |
| Testing strategy: how each claim is checked | yes | [`verification.md`](verification.md) |

## Required links

- Risk record: [`risk.md`](risk.md)
- Verification record: [`verification.md`](verification.md)
- Ship record: [`ship.md`](ship.md)
- Product requirement / issue / ADR / design doc: [`analysis.md`](analysis.md)
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade basis. Ponytail (MIT) is cited as a design influence; its figures are its author's. Graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance or efficacy claim is made.
