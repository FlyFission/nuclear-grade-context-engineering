# Standard Risk Template

**Purpose:** Sort a real change by risk after questioning the assumptions, justify Standard mode, and name any extra records you turn on.

**Activation threshold:** Use for behavior users can see, lasting design decisions, important dependency/model/API/prompt/tool changes, security/privacy/data handling, operational stance, or anything where the stakes, the uncertainty, or the review value are more than trivial.

**Minimum useful version:** the scope, the affected controlled items, the threshold ratings, the chosen mode, the artifacts you turn on, and the evidence due right away.

**Overhead trap:** Do not score risk with fake precision. Use the screen to surface the stakes and the evidence you need.

---

## Change identity

- Slug: context-engineering-literature-crosswalk
- PR / issue: this PR
- Owner: Ben Huffer (FlyFission)
- Date: 2026-07-03
- Current lifecycle phase: Decide
- Current work phase: audit
- Summary: Add a public peer-project crosswalk doc mapping Nuclear-grade to two public "context engineering" repositories (Meirtz/Awesome-Context-Engineering survey and coleam00/context-engineering-intro PRP template); name the survey's payload-component taxonomy in `context-packs.md`; add a "Blueprint and execute" workflow-catalog entry crediting PRP; point `durable-memory.md` and the roadmap MCP entry at the survey's production-memory literature; log both repos as verified-public Tier 9 sources. No endorsement or compliance claim.

## Mission anchor

State what this change is for, so a long session can be checked against it. See `staying-on-mission`.

- Objective: Help adopters arriving from the broader context-engineering conversation orient on where Nuclear-grade sits, borrowing the survey's vocabulary and the template's ergonomics without diluting the evidence/CM spine.
- Success criteria: One crosswalk doc; one taxonomy lens folded into `context-packs.md`; one workflow-catalog entry; two lineage pointers (durable-memory + roadmap); two Tier 9 source rows; all repo gates pass; skill descriptions and command cards unchanged.
- Non-goals / forbidden directions: No new skills/clusters/templates/commands; no claim of endorsement, affiliation, or superiority over either project; no claim that we implement/conform to the taxonomy or PRP as a standard.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: originating user request ("what can we learn from these two repos based on our repo"); charter boundary discipline.

## Questioning-attitude summary

- Decision question: Can these two public projects enhance the repo as *named peers and cited concept lineage* without implying endorsement, affiliation, or a standard we conform to?
- Evidence that would change the decision: If either repo were paywalled/proprietary it would be excluded-direct; both are public (GitHub + arXiv) and coleam00 is MIT-licensed, so direct citation is allowed under the source-map use rule.
- Assumptions that changed the mode: Touches public wording about external projects + source governance + several docs → Standard, not Quick.
- Facts still needing validation: None blocking; external repo summaries taken from live READMEs this session and framed conceptually so a repo revision does not falsify them.
- Stop or hold conditions: Stop if any wording implies endorsement/affiliation/superiority, or that we implement/conform to the taxonomy or PRP, or if a skill `description:` or command card would change.

## Affected configuration items

List the affected code, docs, infrastructure, dependencies, prompts, models, data, evals, releases, dashboards, or runbooks.

| Item | Type | Why it matters | Link |
|---|---|---|---|
| context-engineering-literature-crosswalk.md | public doc | New external-project bridge; boundary-sensitive wording | `docs/01-field-guide/context-engineering-literature-crosswalk.md` |
| source-map.md | governance doc | Adds two verified-public Tier 9 rows | `docs/00-standards-foundation/source-map.md` |
| context-packs.md | operating doc | Adds the payload-component taxonomy lens | `docs/02-operating-system/context-packs.md` |
| WORKFLOWS.md | public doc | Adds "Blueprint and execute" catalog entry + section | `WORKFLOWS.md` |
| durable-memory.md / ROADMAP.md | docs | Point at the survey's production-memory literature | (repo paths) |
| docs/README.md | index | Discoverability link to the new doc | `docs/README.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Public wording about others' projects; brand/boundary risk if it reads as endorsement or a conformance claim |
| Reversibility | high | Docs-only additions; trivially revertible |
| Detectability | high | `ng doctor` + overclaim scan + review catch boundary slips |
| Exposure | medium | Public README link; adopters comparing frameworks |
| Uncertainty | low | Both repos public and well understood; sourcing policy explicit |
| Dependency trust | low | No code or dependency change |
| AI authority | low | No change to agent authority |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check / proof |
| Known procedure where following the steps matters | yes | packet path + boundary self-check |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude / review |
| Work that was interrupted, resumed, or handed off | no | turnover / context pack |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: Public wording about external projects plus a source-governance change across several doc surfaces.
- Why lighter mode is not enough: Quick cannot carry the boundary-wording and multi-surface review this needs.
- Why heavier mode is not yet required: No code, dependency, data, credential, or agent-authority change; fully reversible; sources are public, not paywalled (lower boundary risk than the PMI crosswalk).

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline above | Ben Huffer |
| `basis.md` | yes | State what must stay true (boundary) | Ben Huffer |
| `verification.md` | yes | Record the gate results | Ben Huffer |
| `ship.md` | yes | Release decision | Ben Huffer |
| `turnover.md` | no | No handoff | — |
| `self-check.md` | no | Folded into verification | — |
| `supplier-trust.md` | no | No dependency/model change | — |
| Nuclear subset record | no | Not Tier 0/1 | — |

## Immediate evidence obligations

- Minimum evidence before build: Confirm both repos are public and citable under the source-map use rule (they are: public GitHub + arXiv; coleam00 MIT-licensed).
- Minimum evidence before merge/release: `ng doctor` OK; overclaim scan clean; `gen-commands` leaves command cards unchanged; skill descriptions unchanged; new doc's links resolve.
- Independent review needed? yes — human review of boundary wording before merge (PR review).

## Required links

- Packet: `.nuclear/changes/context-engineering-literature-crosswalk/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `docs/00-standards-foundation/source-map.md`, `docs/01-field-guide/context-engineering-literature-crosswalk.md`

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
