# Follow-up to Skills Token Audit (post-rename): Basis

**Purpose:** State what must stay true for the change to be safe, reliable, secure, useful, and easy to review.

**Activation threshold:** Use for Standard changes where the requirements, architecture, interfaces, dependencies, AI power, protected outcomes, or outcomes to prevent need a clear basis.

**Minimum useful version:** the mission, the protected outcomes, the outcomes to prevent, the assumptions, the constraints, the trust decisions about intended use, and the evidence needs.

**Overhead trap:** Do not invent requirements by writing a long design essay. Link to the real needs and capture only the basis this change needs.

---

## Change context

- Slug: `follow-up-token-audit`
- Related risk record: `risk.md`
- Owner: `@codex[agent]`
- Date: 2026-05-31
- Decision this basis supports: Keep the flagged overlap clusters as separate skills for now; defer optional skill-body prose cuts; keep the per-file boundary disclaimer approach and the current `docs/` corpus layout.

## Mission / need

The token audit doc (`docs/05-reference/skills-token-audit.md`) was written as a “measurement + gate” deliverable and explicitly deferred post-rename body edits and overlap decisions. The rename sweep has landed, so the follow-up need is:

- keep the audit reference page aligned with the current measured baseline; and
- make explicit, reviewable decisions about the flagged overlap clusters and optional prose cuts so later PRs don’t drift by assumption.

## Protected outcomes

What must the system keep safe?

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Audit doc accuracy | Other work will use the baseline numbers and cluster names; drift undermines “measure, don’t assume” | `python tools/ng.py tokens .` output matches the doc |
| Skill routing and contracts remain stable | Merging skills is a structural change with contract/routing implications | No `skills/*/SKILL.md` body changes; tests stay green |
| Gate remains deterministic and honest | Token-budget regression should still be caught reproducibly | `python tools/ng.py tokens .` stays `OK: token budget` |

## Unacceptable outcomes

What must not happen?

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Skill merges or deletions “as a cleanup” | Breaks routing expectations and contract tests | Explicit non-goal + keep change scoped to docs/packet |
| Large skill-body rewrites justified only by token numbers | Risks losing decision signals and quality | Defer to a separate, scoped proposal if ever pursued |
| Misleading claims about runtime/package cost | Wrong decision framing for relocation of docs | Verify packaging boundaries from `pyproject.toml` and `ng tokens` design notes |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Overlap clusters are adjacent but distinct | assumption | Skill catalog and token-audit findings | recurring routing confusion or duplication evidence | maintainers |
| Always-loaded cost stays small | fact | `ng tokens` skill description total | description totals materially rise or budgets fail | maintainers |
| Per-file boundary notes are worth the repetition | decision | current doctrine favors self-containment | maintainers decide compactness outweighs self-containment | maintainers |

## Grounding status

Keep confidence apart from evidence before any derived claim is accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Current baseline numbers for skills/commands/templates/docs | local proof | `python tools/ng.py tokens .` | updates the audit doc tables |
| Overlap cluster skill IDs (post-rename) | local proof | `skills/*/SKILL.md` names + `SKILLS.md` | updates the audit doc overlap section |
| Docs are not shipped in the wheel runtime | local proof | `pyproject.toml` wheel config | informs the “core-source-rationale relocation” discussion |

## Interfaces and trust boundaries

- Internal interfaces affected: not applicable.
- External services/APIs affected: not applicable.
- Data classes affected: not applicable.
- Human approval boundaries: not applicable.
- AI/model/tool authority boundaries: none (docs + change-record only).

## Dependency / model / supplier intended use

Use this section only when activated.

Not applicable: no dependency, model, API, SaaS, or supplier is introduced or changed in this follow-up.

## Derived requirements or claims

Include only the important claims that need evidence.

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | `docs/05-reference/skills-token-audit.md` matches current measured baseline numbers | “measure, don’t assume”; deterministic counter | Update doc from `ng tokens` output + derived per-surface totals | `python tools/ng.py tokens .` |
| REQ-002 | Overlap clusters are recorded using current (post-rename) skill IDs | Avoid confusion after rename sweep | Update overlap section to current IDs and record keep/merge decision | `SKILLS.md` skill list + audit doc review |
| REQ-003 | Decisions are explicit: no merges; no optional prose cuts; no disclaimer collapse; no doc relocation | Avoid “silent doctrine change” | Record decisions in audit doc and this packet | Packet validation + doc review |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Token audit reference page: `docs/05-reference/skills-token-audit.md`
- Skill catalog: `SKILLS.md`
- Packaging boundary evidence: `pyproject.toml`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
