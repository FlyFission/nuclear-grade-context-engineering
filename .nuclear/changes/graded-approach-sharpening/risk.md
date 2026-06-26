# Standard Risk Record

**Purpose:** Sort the "graded-approach sharpening" change by risk, justify Standard mode, and name the controls due before the edits to public docs, a skill, the maxims, and the source map are accepted.

**Activation threshold:** Standard mode is required because the change edits durable public operating docs, a skill (and its generated command card), `MAXIMS.md`, `AGENTS.md`, and the source map — surfaces downstream agents and users rely on.

**Minimum useful version:** the scope, the affected controlled items, the threshold ratings, the chosen mode, the artifacts turned on, and the evidence due right away.

**Overhead trap:** Do not turn a deep-research report into inspirational copy. Pull over only what closes a loop the repo already opened, and skip everything already covered or deliberately out of scope.

---

## Change identity

- Slug: graded-approach-sharpening
- PR / issue: branch `claude/zealous-sagan-g9sfn0`
- Owner: FlyFission
- Date: 2026-06-17
- Current lifecycle phase: Verify
- Current work phase: audit
- Summary: Sharpen the repo's existing graded approach after an adversarial review — name the administrative floor below Quick (no packet; the commit message is the record), add a non-waiver maxim, grade the change independently of the standing item, add performance history as an oversight modulator, and consolidate the graded-approach lineage in the crosswalk — folded into existing surfaces, anchored to already-mapped DOE/NASA sources.

## Mission anchor

State what this change is for, so a long session can be checked against it. See `staying-on-mission`.

- Objective: Make the graded approach the repo already runs sharper at both ends — a named, near-zero-oversight floor for administrative changes, and an honest link from consequence to rigor — without inventing a parallel taxonomy or new machinery.
- Success criteria: the administrative floor is named with dominant tripwires; the non-waiver maxim is stated; `rating-change-risk` screens the floor first, grades change-vs-item, and reads performance history; one consolidated graded-approach lineage row exists; tests, token budget, doctor, and packet validation pass.
- Non-goals / forbidden directions: no A/B/C/D taxonomy; no new mode token, template mode, `--mode` choice, or validator/CLI behavior change; no new standalone doctrine page; no reproduced regulator text; no compliance, safety, security, certification, formal-assurance, or legal claim.
- Drift check: re-anchor / escalate / stop when an edit duplicates content already covered deeply, names a competing taxonomy, or claims compliance with any cited regulator.
- Traces to: `.nuclear/charter.md` (Art. 9 graded rigor, Art. 15 two-speed control), the uploaded deep-research report, and the user-approved plan.

## Questioning-attitude summary

- Decision question: Which graded-approach ideas from the report are genuine gaps in this repo, and how are they added without fluff, a competing taxonomy, or a new oversight loophole?
- Evidence that would change the decision: an item is already covered deeply (the review confirmed several were); an item contradicts a stated boundary (the new page + IAEA-as-primary did); an item creates a rationalization loophole ("no artifact" did); tests, token budget, or boundary checks fail.
- Assumptions that changed the mode: public operating docs, a skill, the generated command card, `MAXIMS.md`, `AGENTS.md`, and the source map are controlled items; a shallow or duplicative edit would mislead.
- Facts still needing validation: full suite stays green; token budget stays green; packet validates; no prohibited compliance wording is introduced.
- Stop or hold conditions: stop if an edit requires a new skill/command, a new template mode or validator change, or a claim the repo forbids.

## Affected configuration items

List the affected code, docs, infrastructure, dependencies, prompts, models, data, evals, releases, dashboards, or runbooks.

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `rating-change-risk` skill + `ng-classify` card | skill / generated command | Agents load it to choose rigor; the card is single-sourced from it | `skills/rating-change-risk/SKILL.md` |
| `activation-thresholds.md` | operating doc | The threshold reference | `docs/02-operating-system/activation-thresholds.md` |
| `modes.md`, `risk-tiers-and-modes.md`, `change-control-packets.md` | operating docs | Mode/tier/packet doctrine | `docs/02-operating-system/` |
| `MAXIMS.md`, `AGENTS.md`, `CORE.md` | doctrine / agent guidance | Quotable principles + completion standard | repo root |
| `README.md`, `WORKFLOWS.md`, `QUICKSTART.md`, `glossary.md`, `templates/README.md` | public surfaces | Reader-facing consistency | repo root / docs |
| `source-map.md`, `source-to-concept-crosswalk.md` | source foundation | Lineage discipline | `docs/00-standards-foundation/`, `docs/01-field-guide/` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Mis-stated doctrine could misroute future changes |
| Reversibility | low | All edits are text in version control; revert is one commit |
| Detectability | low | Contract tests + doctor + review catch structural breaks |
| Exposure | medium | Public docs and an agent-loaded skill |
| Uncertainty | low | The concept already lives in the repo; this sharpens it |
| Dependency trust | low | No new runtime dependency |
| AI authority | low | No change to what any agent may do |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check / proof |
| Known procedure where following the steps matters | yes | packet path / deviation note |
| New or uncertain work where the assumptions may be wrong | no | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | no | turnover / context pack |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: the change edits controlled public doctrine and an agent-loaded skill, so it needs a basis, a trace, and a stated release decision.
- Why lighter mode is not enough: a commit message alone (the administrative floor) cannot hold the basis or the claim-to-evidence trace for doctrine many agents read.
- Why heavier mode is not yet required: text-only, reversible, no runtime/security/data state, no new agent authority.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | The questioning-attitude summary in this record suffices | FlyFission |
| `basis.md` | yes | Protected outcomes and per-item requirements | FlyFission |
| `verification.md` | yes | Suite, token, doctor, validate evidence | FlyFission |
| `ship.md` | yes | Acceptance decision and baseline trigger | FlyFission |
| `turnover.md` | no | Same owner continues | FlyFission |
| `self-check.md` | no | Covered by the promise-boundary check in `plan.md` | FlyFission |
| `supplier-trust.md` | no | No dependency/model/supplier trust change | FlyFission |
| Nuclear subset record | no | Reversible text-only doctrine change | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: the adversarial review confirming each item is a true value-add (recorded in `basis.md`).
- Minimum evidence before merge/release: `gen-commands --check`, `tokens`, `doctor`, `pytest`, `ruff`, and packet `validate` all green.
- Independent review needed? yes; why: the change edits the charter-adjacent maxims and public doctrine — a PR reviewer should confirm the wording and the boundary discipline.

## Required links

- Packet: `.nuclear/changes/graded-approach-sharpening/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `docs/00-standards-foundation/source-map.md`, `docs/01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- The mode is justified.
- The artifacts turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade risk record inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
