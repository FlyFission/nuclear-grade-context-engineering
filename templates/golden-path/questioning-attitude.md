# Questioning Attitude Screen

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Challenge the assumptions before an agent builds, merges, or releases.

**Activation threshold:** Use when a request, diff, dependency, tool permission, prompt/model change, release decision, or public claim carries uncertainty or real stakes.

**Minimum useful version:** the decision question, the assumptions, the facts to check, the warning signs, the stop conditions, and the next artifact.

---

## Change context

- Slug:
- Owner:
- Date:
- Request / issue / PR:
- Work type (all that apply): greenfield / brownfield / defect-fix / refactor-migration
- Current golden-path phase: Question

## Decision question

What decision must this change record make?

## Work-type questions

For each work type marked in the change context, answer the questions it forces; overlapping types stack, so cover the union (brownfield/migration → blast radius + rollback-of-state; defect-fix → reproduction + regression; greenfield → interfaces + acceptance). See `docs/02-operating-system/work-type-lens.md`.

- Forced questions and answers (per marked type):

## Assumptions to validate

| Assumption | Why it matters | Validation source | Status |
|---|---|---|---|
| | | | planned |

## Knowns, unknowns, and danger words

| Item | Type: fact / assumption / unknown | Source quality | Action |
|---|---|---|---|
| | | repo / source / test / owner / model claim | |

Danger words to challenge: probably, should, seems, obvious, just docs, safe, secure, compliant, approved, we can classify later.

## Warning signs and uncertainty

| Warning sign / uncertainty | Possible consequence | Resolve before |
|---|---|---|
| | | execute / verify / review / decide |

## Agent error precursors

| Precursor | Present? | Control |
|---|---|---|
| Heavy task: many files, mixed goals, hidden links between parts, a long context | yes/no | |
| Capability gap: missing source, stale memory, an unfamiliar tool or domain | yes/no | |
| Work environment: a messy tree, failing tests, an unclear branch, flaky CI | yes/no | |
| Human or model nature: overconfidence, anchoring on the first idea, pressure to be done | yes/no | |

## Hidden escalation triggers

- User-visible behavior:
- Data, auth, permission, or network effect:
- Dependency, model, API, or tool trust change:
- AI authority change:
- Release, rollback, monitoring, or public-claim effect:

## Stop or hold conditions

| Condition | Stop / hold action | Owner |
|---|---|---|
| | | |

## Next artifact

- Quick proof:
- Standard spec / design basis:
- Context pack:
- Turnover record:
- Self-check record:
- CM record:
- Release decision:

## Required links

- Packet: `.nuclear/changes/<slug>/`
- Related `risk.md` or `basis.md`:
- Evidence source:
- Source lineage if invoked:

## Exit criteria

- Assumptions are checked, marked as a gap, or assigned to someone.
- For each work type marked, the questions it forces are answered or marked not applicable.
- The triggers to escalate are not hidden.
- The next artifact and the evidence it owes are named.

## Source-lineage note

Original Nuclear-grade template inspired by the questioning-attitude, validate-your-assumptions, pause-when-unsure, and review habits in DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md` and used as public source lineage. No compliance claim is made.
