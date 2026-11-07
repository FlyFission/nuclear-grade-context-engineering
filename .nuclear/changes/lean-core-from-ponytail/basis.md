# Basis: lean core, learned from Ponytail

This is the specification. Approve, edit, or strike each requirement. Nothing is built until the owner marks the decision frontier in `plan.md`.

## Change context

- Slug: lean-core-from-ponytail
- Related risk record: [`risk.md`](risk.md)
- Owner: Ben Huffer (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Decision this basis supports: whether to rebuild Nuclear-grade's operative surface (card, Core 7 bodies, receipt, review shape) at Ponytail scale, under a measured non-inferiority gate.

## Mission / need

Nuclear-grade's doctrine already says the smallest honest context wins. Its artifacts do not embody it: 1,208 words per skill body on average, the mode rule restated in at least seven places, 19,476 tokens of Core bodies when selected. Ponytail shows that one 600-word prompt with a ladder, a floor, a trigger list, and a receipt changes agent behavior and keeps a test rate up. Our own control ladder shows that nine tenths of a skill's words buy +0.062 on easy scenarios and nothing on hard ones. The need is to keep the rigor that Ponytail lacks (escalation, human gate, custody) and cut everything else to the size that measurably works. Full reading in [`analysis.md`](analysis.md).

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The floor is never waived in any mode | this is the one place rigor is unconditional | REQ-005 wording test; human read |
| Escalation still follows consequence | the lean text must not flatten modes into one level | REQ-007 routing and backtest re-run |
| Trust-bearing verdicts still reach a person | Ponytail ends with "Ship."; we must not | REQ-001 card text; REQ-008 review shape |
| Custody and two-party rules are untouched | the differentiated center of the project | REQ-003 non-goal; validator tests unchanged |
| Behavior the skills exist to change is not lost | the whole point of the gate | REQ-007 control-ladder non-inferiority |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A lean body drops the one instruction that changed a real decision | insufficiency | the skill reads well and does nothing | REQ-007 re-run; REQ-004 one fit read per body against the scenarios that needed it |
| The card and its renders drift apart | fault | seven copies again within a year | REQ-002 parity test |
| Words creep back into always-on surfaces | fault | the gain erodes silently | REQ-001 and REQ-003 budgets in `ng tokens`; CI fails on regression |
| A public page claims Nuclear-grade is leaner or better than Ponytail | fault | an efficacy claim with no comparable study | REQ-010; claims-discipline check |
| The lean pass softens the floor or the human gate to save words | insufficiency | the one trade the project must not make | REQ-005; maintainer read of every card diff |

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
| REQ-001 | THE CARD SHALL be one always-on text of at most 600 words that holds, in this order: the one idea, the rigor ladder (six rungs with "stop at the first that holds"), the never-cut floor, the Standard-plus traps, and the receipt shape. It names a person as the owner of any ship, block, or trust-bearing verdict. | Ponytail parts: ladder, floor, receipt; `MAXIMS.md` | a new file `CORE-CARD.md` (name open, D2) counted by `ng tokens` under a `card_max` budget | E-001 budget; E-002 maintainer read |
| REQ-002 | WHEN the card changes THE SYSTEM SHALL fail a test if the `hooks/session_start.py` preamble, the `hooks/user_prompt_submit.py` line, `starter-kit/core/AGENTS.md`, and the summary block in `CORE.md` do not match the card's rendered sections byte for byte. | Ponytail: SKILL.md body equals AGENTS.md body | a parity test in `tests/`; renders generated, not hand-copied | E-003 |
| REQ-003 | THE SYSTEM SHALL hold each Core 7 skill body at or under 1,200 tokens while keeping every section the skill authoring contract requires and its decision contract, and SHALL hold the Core selected-body total at or under 8,500 tokens. | ladder C4 against C3; authoring contract | `core_skill_body_max` and a Core total budget in `ng tokens`; CI gate | E-001 |
| REQ-004 | THE SYSTEM SHALL write each Core 7 Process step as an imperative with its object and, where the step can end the work, its stop or hand-off; doctrine moves behind one link per step at most. | Ponytail register: "read", "list", "grep", "take the first option" | authoring-contract rule; one fit read per body against the consolidation scenarios that needed that skill | E-004 |
| REQ-005 | THE CARD SHALL state the floor once, as items that hold in every mode including the administrative floor, and no skill SHALL restate it. The five items: say the mode and the one fact before the first write; every claim carries evidence or a named gap; never edit the files that judge you; a person decides anything irreversible or trust-bearing; end with the receipt. | `MAXIMS.md` "grading scales how, not whether"; Ponytail "Never cut" | card text; a grep test that the floor's heading appears in the card only | E-002; E-003 |
| REQ-006 | THE RECEIPT SHALL be at most five lines in a fixed order: Mode and the fact that set it; Changed; Proof run; Not checked; Open. `AGENTS.md`'s completion standard SHALL be this receipt. | Ponytail closing lines; our completion standard | card section; `AGENTS.md` edit; starter-kit edit | E-002 |
| REQ-007 | WHEN a phase rewrites skill bodies THE SYSTEM SHALL re-run the control ladder (27 + 7 scenarios) and the 176 routing cases with the same harness, grader, and rubric, and the phase SHALL NOT ship if the mean paired difference new-against-current is below −0.05, if any single skill falls by more than 0.17, or if required-skill recall on the routing cases falls. The consequence backtest over the same 49 commits SHALL return the same modes. | ladder design; consolidation protocol thresholds | eval re-run by a maintainer or CI, not the drafting agent; results in that phase's `verification.md` | E-005; E-006; E-007 |
| REQ-008 | THE REVIEW SHALL read the callers of every changed function, not only the diff; group findings Must fix / Should fix / Nice to have; give each finding What this is, Problem, Fix, If we skip it; end with Verdict and Not checked; treat a marked `deferred:` or `shortcut:` with a named trigger as a decision, not a finding; and change no code. Applies to `reviewing-code-quality` and the ship review. | Ponytail `/ponytail-review`; our proving-claims and gap discipline | skill Process and `## Prompt` edits; cards regenerate | E-004; E-002 |
| REQ-009 | WHERE the marker convention is adopted THE SYSTEM SHALL recognize `shortcut:` and `deferred:` comment markers, and `ng debt` SHALL list them by file with the limit and the trigger, flagging any marker with no trigger. | Ponytail `/ponytail-debt`; our `tracking-deficiencies` | a small `ng debt` subcommand; a test | E-008 |
| REQ-010 | THE SYSTEM SHALL make no efficacy claim relative to Ponytail in any public file; Ponytail's numbers appear only as its author's self-report, and this work is described as a design inspection. | `DISCLAIMER.md`; claims discipline | public-doc test phrase list; maintainer read | E-002 |
| REQ-011 | WHEN the card exists THE SYSTEM SHALL state the mode rule in the card only; `CORE.md`, `QUICKSTART.md`, `using-nuclear-grade`, and `rating-change-risk` SHALL link to it rather than restate it; and every page under `docs/02-operating-system/` SHALL be reachable from a skill, the card, or a template, or be moved to an archive folder. | Ponytail: one source; our `token-burn-control.md` | a link-reachability test; deletion-first review of each page | E-009 |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview: what changes and why | yes | [`analysis.md`](analysis.md) sections 5 to 7 |
| Architecture: shape and major parts | yes | one card; renders tested for parity; lean Core bodies; cards regenerated; doctrine behind links |
| Components and interfaces: boundaries above | yes | `Interfaces and trust boundaries` |
| Data models: shapes, classes, ownership | yes | the receipt shape (REQ-006); the marker form (REQ-009) |
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
