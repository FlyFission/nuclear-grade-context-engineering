---
status: proposed
date: 2026-11-07
decision-makers: Ben Huffer (maintainer)
consulted: AI agent (drafter)
informed: contributors via the draft pull request
---

# Risk: lean core, learned from Ponytail

## Change identity

- Slug: lean-core-from-ponytail
- PR / issue: draft pull request on `claude/bold-hamilton-w8qymj`
- Owner: Ben Huffer (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Current lifecycle phase: Specify
- Current work phase: candidate
- Summary: an umbrella specification and phased plan for cutting the in-session bureaucracy to Ponytail scale: one 400-word always-on card, no per-prompt reminder, two agent-facing states on seven trap surfaces, four-section skills, one-file Quick and three-file Standard records, lenses demoted to reference, plus the four Ponytail habits that change code while it is written. The after-the-fact machinery (validator, two-party, gate, policy, badge) is left as it is. This record changes no code. Each phase runs as its own record and pull request.

## Mission anchor

- Objective: an ordinary edit under Nuclear-grade costs the agent one 400-word card and three closing lines, no record and no reminder; a change on one of seven trap surfaces still stops for a person; the after-the-fact checks still run unchanged.
- Success criteria: always-on tokens for an ordinary edit under 1,500; a filled Quick record under 30 lines in one file; Core 7 bodies at four sections and under 600 words; control-ladder and routing scores not past the margin; the mode rule in the card only.
- Non-goals / forbidden directions: no merge of skills; no change to what the validator, two-party check, gate, or policy decide beyond accepting the smaller record shapes; no efficacy claim relative to Ponytail; no new always-on text; the trap sentence and the stop for a person are never cut to save words.
- Drift check: if a phase adds words to an always-on surface, or softens the floor, stop and re-anchor.
- Traces to: `.nuclear/charter.md` articles 9 (graded rigor), 12 (operational unambiguity), 15 (two-speed control); `MAXIMS.md` "minimum sufficient context".

## Questioning-attitude summary

- Decision question: can the operative text shrink to Ponytail scale without a measured loss on the behaviors the skills exist to change?
- Evidence that would change the decision: a control-ladder re-run where the lean bodies score lower than the current ones past the margin in `basis.md` REQ-007, or a routing re-run with lower required-skill recall.
- Assumptions that changed the mode: the change touches always-loaded agent instructions, the two mode-owning skills, and the hook preamble, so it is Standard by this repository's consequence policy and the hook phase is `standard+authority`.
- Facts still needing validation: the control-ladder C4 against C3 result (+0.062, 0 lower of 27; +0.000 on 7 hard) was measured with one model family and author-written rubrics; whether it holds for a full rewrite rather than a five-bullet compression is the question the gate answers.
- Stop or hold conditions: any phase that cannot meet its gate stops at that phase; the earlier phases stay; the loss is reported in that phase's record.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `AGENTS.md`, `CLAUDE.md`, `starter-kit/core/AGENTS.md` | always-loaded agent instructions | the card lands here; policy mode Quick (`agent-instructions`) | `../../consequence-policy.json` |
| `hooks/session_start.py`, `hooks/user_prompt_submit.py` | gate hooks | the preamble is one render of the card; policy mode `standard+authority`, human merge | `../../consequence-policy.json` |
| `skills/using-nuclear-grade/`, `skills/rating-change-risk/` | mode-owning skills | first bodies to rewrite; policy mode Standard (`mode-owners`) | `../../consequence-policy.json` |
| the other five Core 7 skills | skills | rewrite to the operative register and budget | `../../../CORE.md` |
| `commands/*.md` | generated command cards | regenerate from the lean skills | `../../../COMMANDS.md` |
| `CORE.md`, `QUICKSTART.md` | public docs | restatements of the mode rule collapse to the card plus links | `../../../CORE.md` |
| `nuclear_grade/tokens.py` budgets, `tests/test_skill_contracts.py` | budget gate and contract tests | new ceilings, four-section contract, parity test | `../../../docs/05-reference/skills-token-audit.md` |
| `templates/quick/`, `templates/standard/`, `nuclear_grade/ng_validate.py` | record templates and validator | one-file Quick, three-file Standard; validator accepts both shapes; policy mode Standard (`validators`) | `../../consequence-policy.json` |
| `docs/02-operating-system/work-type-lens.md`, `archetype-lens.md`, `hpi-overlays.md` | doctrine | demoted from steps to reference | `../../../CORE.md` |
| `evals/skill-control-ladder/`, `evals/skill-routing-cases.jsonl` | evidence | the non-inferiority gate | `../../../evals/skill-control-ladder/README.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | high | these texts decide how every agent run classifies and proves its work |
| Reversibility | high | prose and budgets; revert the phase commit; the gate hook is opt-in |
| Detectability | medium | token and parity gates are deterministic; behavior loss shows only in the eval re-run |
| Exposure | high | every adopter who vendors the Core 7 or the starter kit |
| Uncertainty | medium | compression was measured at five bullets, not at a full rewrite |
| Dependency trust | low | no new dependency |
| AI authority | medium | an agent drafts the lean text that will steer agents; the maintainer approves each phase |
| Controllability (human gate can catch/reverse in time?) | high | each phase is its own pull request with its own record |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | yes | rewriting seven skill bodies in a row invites drift; the parity and budget tests, and one fit read per body |
| Known procedure where following the steps matters | yes | the skill authoring contract and `ng doctor` |
| New or uncertain work where the assumptions may be wrong | yes | the control-ladder re-run before any phase is called done |
| Work that was interrupted, resumed, or handed off | yes | phases hand off through their own records |
| A high-stakes critical action | yes | the hook preamble edit; human merge under `standard+authority` |

## Selected mode

- **Mode:** Standard
- Why this mode: always-loaded agent instructions, the mode-owning skills, and public wording are all in scope; the consequence policy sets Standard for the skills and `standard+authority` for the hooks.
- Why lighter mode is not enough: this text steers every classification an agent makes.
- Why heavier mode is not yet required: this record changes nothing; the hook phase carries its own `decision-authority.md` and validates with `--strict-authority`.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | the summary above is enough for a specification record | maintainer |
| `basis.md` | yes | the specification lives there | maintainer |
| `verification.md` | yes | baseline numbers and the gates, all `planned` | maintainer |
| `ship.md` | yes | the decision this record asks for is approval of the specification | maintainer |
| `turnover.md` | no | handoff is per phase | maintainer |
| `self-check.md` | no | no critical action in this record | maintainer |
| `supplier-trust.md` | no | no dependency change | maintainer |
| Nuclear subset record | no | not regulated work | maintainer |

## Immediate evidence obligations

- Minimum evidence before build: the maintainer approves `basis.md` and the decision frontier in `plan.md`.
- Minimum evidence before merge/release: this record validates; the badge is regenerated; no code or prose outside `.nuclear/changes/` changes in this pull request.
- Candidate load-bearing / decisive claim IDs: REQ-007 (non-inferiority) decides whether any phase ships.
- Minimum actor/context/mechanism/authority/resource profile for those claims: the eval re-run is executed by a maintainer or CI, not by the agent that wrote the lean text; the rubric is unchanged from the baseline run.
- Prohibited coupling paths (for example actor may not control threshold, retention, and verdict): the agent that drafts a lean body may not edit the control-ladder rubric, the routing cases, or the margin in REQ-007 in the same change.
- Who owns evidence admissibility and residual-risk disposition: the maintainer.
- Independent reproduction, diverse verification, or direct witnessing needed? yes; the eval must be re-run by someone other than the drafting agent before a phase is called done.

## Required links

- Packet: `.nuclear/changes/lean-core-from-ponytail/`
- Analysis: [`analysis.md`](analysis.md)
- [`basis.md`](basis.md)
- [`plan.md`](plan.md)
- [`trace.md`](trace.md)
- [`verification.md`](verification.md)
- [`ship.md`](ship.md)
- Source-map/crosswalk references if source lineage is invoked: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade record. Graded-rigor and human-performance lineage is mapped in `docs/00-standards-foundation/source-map.md`. Ponytail is cited as a design influence under its MIT license. No compliance claim is made.
