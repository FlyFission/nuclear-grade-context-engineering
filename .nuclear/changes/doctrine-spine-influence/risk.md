# Standard Risk Record

**Purpose:** Sort the doctrine-spine influence update by risk, and name the controls needed before the public workflow artifacts are accepted.

**Activation threshold:** Standard mode is required because the change affects public docs, skills, command prompts, templates, and baseline expectations for downstream agents.

**Minimum useful version:** Decision question, mission anchor, affected controlled items, threshold screen, activated artifacts, and evidence obligations.

**Overhead trap:** Do not turn the influence into inspirational copy. Only add controls that improve decisions, evidence, or agent operation.

---

## Change identity

- Slug: doctrine-spine-influence
- PR / issue: branch `add-quotes-and-influence`
- Owner: FlyFission
- Date: 2026-05-30
- Current lifecycle phase: Execute
- Current work phase: audit
- Summary: Convert owner-supplied operating influences into existing Nuclear-grade control surfaces without adding quotes, attribution, or a new doctrine page.

## Mission anchor

- Objective: Make Nuclear-grade harder to misuse by end users and downstream agents while preserving fast candidate work and slow acceptance gates.
- Success criteria: Existing docs, skills, command prompts, and Standard templates express the control stack; Quickstart remains usable; public wording does not add quotes or new assurance claims; validation and contract tests pass.
- Non-goals / forbidden directions: No verbatim quotes, named quote attributions, new manifesto page, compliance claim, safety claim, security claim, certification claim, formal assurance claim, legal advice, CLI behavior change, or validator rule change.
- Drift check: re-anchor when an edit does not improve a decision, evidence path, agent trigger, or acceptance gate; escalate before broadening to unrelated docs.
- Traces to: `.nuclear/charter.md`, `WORKFLOWS.md`, and the user-approved implementation plan.

## Questioning-attitude summary

- Decision question: How should these influences change Nuclear-grade's controls so users and downstream agents make better decisions without adding ceremony?
- Evidence that would change the decision: tests fail, public wording inserts quotes or named attributions, agent-facing contracts break, reviewers find that fast exploration is slowed without acceptance value, or Copilot/human review finds unaddressed template drift.
- Assumptions that changed the mode: Public workflow wording, skill triggers, command prompts, and templates are controlled items; a shallow doctrine update would be misleading; the prior review surprise warrants OPEX.
- Facts still needing validation: Contract tests continue to pass after description and prompt changes; public boundary scans find no quote insertion or unsafe claims.
- Stop or hold conditions: Stop if a change requires quote attribution, new public source lineage, validator behavior, dependency/model trust review, or a new public doctrine page.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Charter and operating docs | Public doctrine | Define how all changes should be carried out | `controlled-items.md` |
| Skills and command prompts | Agent-operable instructions | Downstream agents discover behavior through triggers and prompt cards | `controlled-items.md` |
| Standard templates | Packet interface | Users encode the control stack through these fields | `controlled-items.md` |
| Adoption and evaluation docs | User/agent adoption | Shape end-user rollout and future skill assessment | `controlled-items.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Public methodology and agent behavior surfaces change. |
| Reversibility | medium | Text changes can be reverted, but public workflow drift affects users. |
| Detectability | medium | Misuse may appear later as bad packets or shallow agent behavior. |
| Exposure | medium | Public docs, skills, and command prompts are end-user surfaces. |
| Uncertainty | medium | The influence must be translated into controls without overfitting. |
| Dependency trust | low | No dependency, model, API, SaaS, or vendor trust change. |
| AI authority | medium | Agent-facing instructions and command prompts change. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine/repetitive action where inattention is plausible | yes | self-check for public claims and exact target files |
| Known procedure where workflow adherence matters | yes | Standard packet plus CM records |
| Novel or uncertain work where assumptions may be wrong | yes | questioning attitude and adversarial review |
| Interrupted, resumed, or handed-off work | yes | packet state and PR evidence |
| High-consequence critical action | no | no release or external-state action before PR review |

## Selected mode

- Mode: Standard
- Why this mode: The change affects durable public workflow controls and agent-operable artifacts.
- Why lighter mode is not enough: Quick proof cannot show downstream skill, command, template, adoption, OPEX, and boundary impacts.
- Why heavier mode is not yet required: No code behavior, release automation, dependency/model trust, credentials, data, or production state changes.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Compact summary in this risk record is enough. | FlyFission |
| `basis.md` | yes | Needs protected outcomes and grounded influence mapping. | FlyFission |
| `plan.md` | yes | Multi-surface public and agent-facing changes need sequenced work, checkpoints, and rollback. | FlyFission |
| `trace.md` | yes | Doctrine-spine claims need links from basis to controls, verification, and ship posture. | FlyFission |
| `verification.md` | yes | Public/contract tests and boundary scans must be recorded. | FlyFission |
| `ship.md` | yes | Acceptance and baseline posture must be explicit. | FlyFission |
| `turnover.md` | no | Same owner/agent continues in-thread. | FlyFission |
| `self-check.md` | no | Critical claim checks are embedded in verification and ship records. | FlyFission |
| `supplier-trust.md` | no | No external dependency, model, API, or vendor trust decision. | FlyFission |
| CM records | yes | Controlled items, change impact, OPEX, and baseline are activated. | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: confirm affected files and non-goals; record OPEX and controlled items.
- Minimum evidence before merge/release: packet validation, public-doc tests, skill/command contract tests, validator tests, doctor output, quote-exclusion and boundary scan.
- Independent review needed? yes; PR review/Copilot review is requested because the change affects public agent behavior.

## Required links

- Packet: `.nuclear/changes/doctrine-spine-influence/`
- `basis.md`
- `controlled-items.md`
- `change-impact.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: existing source-lineage notes only; no new direct source lineage added.

## Exit criteria

- Mode is justified.
- Activated artifacts are explicit.
- Important risks, assumptions, and evidence obligations are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade packet record inspired by public graded quality, configuration management, lifecycle, software assurance, secure development, AI risk, and supply-chain sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
