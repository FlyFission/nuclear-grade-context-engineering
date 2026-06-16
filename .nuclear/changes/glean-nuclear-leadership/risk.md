# Standard Risk Record

**Purpose:** Sort the "glean nuclear-leadership value-adds" update by risk, and name the controls needed before the changes to charter, public docs, a skill, a command, and a template are accepted.

**Activation threshold:** Standard mode is required because the change amends the charter and edits public operating docs, a skill, a command prompt, and a CM template that downstream agents and users rely on.

**Minimum useful version:** Decision question, mission anchor, affected controlled items, threshold screen, selected mode, and evidence obligations.

**Overhead trap:** Do not turn two deep-research reports into inspirational copy. Pull over only items that close a loop the repo already opened, and skip everything already covered or deliberately out of scope.

---

## Change identity

- Slug: glean-nuclear-leadership
- PR / issue: branch `claude/inspiring-ride-hix4tl`
- Owner: FlyFission
- Date: 2026-06-16
- Current lifecycle phase: Execute
- Current work phase: audit
- Summary: Transfer four adversarially-filtered nuclear-leadership value-adds (just-culture line, independent-layers principle, temporary-modification discipline, competence-to-act qualification) plus one durable-memory doctrine into existing Nuclear-grade surfaces, anchored to sources already in the source map.

## Mission anchor

- Objective: Add only the highest-confidence nuclear-leadership practices the repo does not already cover, each sharpening existing material rather than inventing new machinery.
- Success criteria: Charter Art. 19 distinguishes honest error from willful violation; the control stack states layer independence; variance discipline covers deliberate temporary modifications; authority-and-intent defines competence-to-act; a durable-memory doctrine exists as the persistent counterpart to context-window discipline; tests, token budget, doctor, and packet validation pass.
- Non-goals / forbidden directions: No new skills or commands; no IAEA/WANO/INSAG citations or accident case studies; no leading-indicators metrics doc; no drill template; no charter article beyond the Art. 19 refinement; no compliance, safety, security, certification, formal-assurance, or legal claim; no validator or CLI behavior change.
- Drift check: re-anchor if an edit duplicates content already covered deeply, expands the repo into an HR/certification program, or adds a source outside the existing DOE/NRC/NIST/NASA map.
- Traces to: `.nuclear/charter.md`, the two source reports, and the user-approved plan.

## Questioning-attitude summary

- Decision question: Which nuclear-leadership practices from the two reports are genuine gaps in this repo, and how are they added without fluff or scope creep?
- Evidence that would change the decision: a proposed item is already covered deeply elsewhere in the repo; an item contradicts a stated repo boundary; tests, token budget, or boundary checks fail; an item needs a paywalled or non-mapped source.
- Assumptions that changed the mode: charter, public operating docs, a skill, a command, and a CM template are controlled items; a shallow or duplicative edit would mislead; the change amends a charter article.
- Facts still needing validation: full test suite stays green; token budget stays green; packet validates; no prohibited compliance wording is introduced.
- Stop or hold conditions: stop if an edit requires a new external source, a new skill/command (with its index wiring), a charter article rewrite, or a claim the repo forbids.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `.nuclear/charter.md` | Charter | Art. 19 refinement changes the durable backbone all work holds to | `controlled-items.md` |
| Operating-system + field-guide docs | Public doctrine | Define how changes are run; downstream agents read them | `controlled-items.md` |
| `learning-from-experience` skill, `ng-learn` command | Agent-operable instructions | Carry the just-culture distinction into agent behavior | `controlled-items.md` |
| `templates/cm/variance.md` | Packet interface | Users record temporary modifications through this template | `controlled-items.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Public doctrine, charter, and agent-facing surfaces change. |
| Reversibility | medium | Text changes revert cleanly, but doctrine drift reaches users and agents. |
| Detectability | medium | A weak or duplicative edit may surface later as confusion or shallow agent behavior. |
| Exposure | medium | Charter, public docs, a skill, a command, and a template are end-user surfaces. |
| Uncertainty | low | Each item maps to an existing internal loop and an already-mapped source. |
| Dependency trust | low | No dependency, model, API, or vendor trust change. |
| AI authority | medium | Agent-facing instructions (skill, command, qualification doctrine) change. |

## Selected mode

- Mode: Standard
- Why this mode: The change amends the charter and durable public doctrine plus agent-operable artifacts.
- Why lighter mode is not enough: Quick proof cannot show charter, multi-doc, skill, command, and template impact together.
- Why heavier mode is not yet required: No code behavior, release automation, dependency/model trust, credentials, data, or production state changes.

## Immediate evidence obligations

- Minimum evidence before build: confirm each item is a real gap and maps to an already-mapped source; record controlled items and change impact.
- Minimum evidence before merge: full pytest suite, token-budget audit, doctor, packet validation, and a manual boundary read of the new and edited docs.
- Independent review needed? yes; PR review is requested because charter and public agent-facing doctrine change.

## Required links

- Packet: `.nuclear/changes/glean-nuclear-leadership/`
- `basis.md`
- `plan.md`
- `controlled-items.md`
- `change-impact.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Mode is justified.
- Affected controlled items are explicit.
- Important risks, assumptions, and evidence obligations are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade packet record inspired by public human-performance, configuration-management, systems-security-engineering, and context-engineering sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
