# Follow-up to Skills Token Audit (post-rename): Risk

**Purpose:** Sort a real change by risk after questioning the assumptions, justify Standard mode, and name any extra records you turn on.

**Activation threshold:** Use for behavior users can see, lasting design decisions, important dependency/model/API/prompt/tool changes, security/privacy/data handling, operational stance, or anything where the stakes, the uncertainty, or the review value are more than trivial.

**Minimum useful version:** the scope, the affected controlled items, the threshold ratings, the chosen mode, the artifacts you turn on, and the evidence due right away.

**Overhead trap:** Do not score risk with fake precision. Use the screen to surface the stakes and the evidence you need.

---

## Change identity

- Slug: `follow-up-token-audit`
- PR / issue: follow-up tracking issue for post-token-audit decisions (post-rename sweep)
- Owner: `@codex[agent]`
- Date: 2026-05-31
- Current lifecycle phase: Verify / Decide
- Current work phase: audit / accept
- Summary: Update `docs/05-reference/skills-token-audit.md` to match current `ng tokens` output and record the keep/merge + prose-cut decisions for the flagged overlap clusters.

## Mission anchor

State what this change is for, so a long session can be checked against it. See `staying-on-mission`.

- Objective: Close the deferred follow-up items from the skills token audit by recording explicit decisions and aligning the audit doc with the post-rename corpus.
- Success criteria: `ng tokens` baseline numbers and overlap-skill IDs in `docs/05-reference/skills-token-audit.md` match the current repo; a Standard change record exists and validates.
- Non-goals / forbidden directions: listed below.
  - Merge or delete skills.
  - Do broad skill-body “token cuts” without a separate, scoped proposal and review.
  - Collapse the per-file boundary disclaimer family to a shared link (doctrine trade) as part of this follow-up.
  - Move `docs/00-standards-foundation/core-source-rationale.md` out of `docs/` as part of this follow-up.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: audit baseline in `docs/05-reference/skills-token-audit.md` and the `ng tokens` gate described there.

## Questioning-attitude summary

- Decision question: Should any of the flagged overlap clusters be merged, and should any optional token-driven prose cuts happen now that the rename sweep has landed?
- Evidence that would change the decision: recurring routing confusion, duplicated maintenance burden across skills, or token-budget pressure that blocks new work.
- Assumptions that changed the mode: a “decision record” change is still a controlled artifact; reviewers benefit from a Standard packet even though the implementation is mostly doc updates.
- Facts still needing validation: the current measured baseline numbers and overlap-skill IDs (from `python tools/ng.py tokens .`) and that packaging/runtime is unaffected.
- Stop or hold conditions: if any decision implies a skill merge or skill-body rewrite, stop and open a separate change record scoped to that structural work.

## Affected configuration items

List the affected code, docs, infrastructure, dependencies, prompts, models, data, evals, releases, dashboards, or runbooks.

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Skills token audit reference | doc | Records measured baseline and gate intent; must match reproducible numbers | `docs/05-reference/skills-token-audit.md` |
| Decision record | change record | Captures the overlap/prose-cut decisions and evidence | `.nuclear/changes/follow-up-token-audit/` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | low | Doc-only changes; no runtime behavior change intended |
| Reversibility | high | Revertable via git |
| Detectability | high | `ng tokens` output + tests make drift visible |
| Exposure | low | Public docs only |
| Uncertainty | low | Measurements are deterministic and reproducible |
| Dependency trust | low | No new dependencies; no version changes |
| AI authority | low | No authority boundary changes |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | n/a |
| Known procedure where following the steps matters | yes | follow the audit doc + `ng tokens` output exactly |
| New or uncertain work where the assumptions may be wrong | yes | keep decisions explicit; stop if scope expands to merges |
| Work that was interrupted, resumed, or handed off | no | n/a |
| A high-stakes critical action | no | n/a |

## Selected mode

- **Mode:** Standard
- Why this mode: This change records decisions that affect how the skill catalog is maintained, and it updates a measured baseline reference page that other work depends on.
- Why lighter mode is not enough: A Quick record would not capture the trace and ship posture for “no merge/no cuts” decisions; the follow-up is intentionally decision-heavy.
- Why heavier mode is not yet required: No release stance change, no authority change, no new trust boundary, no dependency/model/API change.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Decisions are narrow and evidence-driven; summary captured here | `@codex[agent]` |
| `basis.md` | yes | States what must stay true (no merges, doc accuracy) | `@codex[agent]` |
| `verification.md` | yes | Records the exact evidence run (`ruff`, `pytest`, `ng doctor/eval/tokens/validate`) | `@codex[agent]` |
| `ship.md` | yes | Captures merge posture and residual risk (doc drift only) | `@codex[agent]` |
| `turnover.md` | no | No handoff planned | n/a |
| `self-check.md` | no | No critical irreversible action | n/a |
| `supplier-trust.md` | no | No supplier change | n/a |
| Nuclear subset record | no | Not activated | n/a |

## Immediate evidence obligations

- Minimum evidence before build: confirm current `ng tokens` output and relevant audit doc sections before editing.
- Minimum evidence before merge/release: `python -m ruff check .`, `python -m pytest -q`, `python tools/ng.py doctor .`, `python tools/ng.py eval .`, `python tools/ng.py tokens .`, `python tools/ng.py validate .nuclear/changes/follow-up-token-audit`.
- Independent review needed? no; why: doc-only, reversible, and bounded by deterministic gates/tests.

## Required links

- Packet: `.nuclear/changes/follow-up-token-audit/`
- `basis.md`
- `verification.md`
- `ship.md`
- Skills token audit page: `docs/05-reference/skills-token-audit.md`

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
