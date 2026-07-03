# Quick Risk Template

## Selected mode

- **Mode:** Quick
- **Why this mode:** Additive doctrine refinements to existing pages; reversible, no code, dependency, charter, or behavior change. Escalate to Standard if a reviewer judges the adoption consequence warrants a full basis/trace.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: glean-agent-control-flow
- PR / issue: the working branch for this change
- Owner: FlyFission
- Date: 2026-07-03
- Summary: A review of public agent-engineering practice was screened for value-adds against the existing method. Only two items survived as genuinely additive; both are folded into existing doctrine and map to already-cited sources. (1) Name the **decision→action hold point** — the interval between an agent selecting an action and committing it — as the canonical location for an out-of-band gate. (2) Add **pre-fetch as the bounded complement to just-in-time retrieval**. Everything else reviewed was already covered by existing controls (see Review scope).

## Scope

- Affected files/configs/docs: `docs/02-operating-system/runtime-enforcement.md`, `docs/02-operating-system/context-window-discipline.md`, `skills/double-checking-before-acting/SKILL.md`
- User-visible behavior changed? no
- Dependency/model/API/prompt/tool permission changed? no
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A doctrine paragraph misleads a reader; caught in review, reverted in one diff |
| Reversibility | Full — additive prose; a single revert restores prior text |
| Detectability | High — visible in the diff and rendered docs; link and contract tests run in CI |
| Exposure | Public repo; adopters read the doctrine, but no interface or behavior changes |
| Uncertainty | Low — both additions refine existing prose and map to already-mapped sources |
| Why Quick is enough | Additive, reversible, no code/dependency/charter/behavior change; no Standard trigger tripped |

## Required proof

- Command/check/eval to run: `python -m pytest tests/`; `python tools/ng.py doctor`; `python tools/ng.py tokens`; `python tools/ng.py validate .nuclear/changes/glean-agent-control-flow`; and a diff grep confirming no external source is named.
- Expected result: full suite passes; doctor and token budget green; packet validates; new internal links resolve; grep returns nothing.
- Evidence link/location: `proof.md`

## Review scope

Screened against the existing method; each item below was found **already covered**, so it was
deliberately not re-added (the same "skip what's covered" discipline as the
`glean-nuclear-leadership` packet):

| Reviewed idea | Already lives in |
|---|---|
| Own your prompts | `owning-prompts` skill; configuration management of prompts |
| Own your context window | `context-window-discipline.md`, `context-packs.md` |
| Tools as structured outputs / decouple decision from execution | tool and skill design; `validators.md` |
| Unify execution and business state / stateless append-only thread | packet-as-source-of-truth; `agent-trace-evidence.md`; append-only-deltas rule |
| Launch / pause / resume; trigger from anywhere | `handing-off-work`, turnover, outer-loop triggers |
| Contact humans as a structured request | `declaring-intent`, `deciding-who-decides` |
| Bounded self-correction on error / stop the retry loop | `staying-on-mission` / `ng-drift-check` (counted 3-attempt loop → stop) |
| Small, focused agents | small-mission-work; `modes.md`; work-breakdown |

## Critical-action self-check

- Exact target: the three files named under Scope.
- Expected result: additive-only diffs; all gates green.
- Stop condition: any test, link, or validation failure halts the change rather than triggering a retry.

## Escalation check

None of the Standard triggers are tripped: no users, data, security, permissions, operations, or architecture are affected; no dependency/model/API trust decision changed; no failure path is silent, delayed, costly, or hard to undo; the AI only drafted doctrine prose; the proof fits in one `proof.md`.

## Required links

- Packet: `.nuclear/changes/glean-agent-control-flow/`
- Related PR/issue: the working branch for this change
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md` (DOE-HDBK-1028, Tier 1; Anthropic context-engineering, Tier 9)

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade change record. The two applied refinements draw on public human-performance hold-point and self-checking practice (DOE-HDBK-1028-2009) and public context-engineering guidance, both mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
