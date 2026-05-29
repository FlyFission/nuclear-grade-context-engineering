# Questioning Attitude Screen

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Challenge assumptions before an agent builds, merges, or releases.

**Activation threshold:** Use when a request, diff, dependency, tool permission, prompt/model change, release decision, or public claim has uncertainty or consequence.

**Minimum useful version:** Decision question, assumptions, facts to verify, warning signs, stop conditions, and next artifact.

---

## Change context

- Slug:
- Owner:
- Date:
- Request / issue / PR:
- Current golden-path phase: Question

## Decision question

What decision must this change record make?

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
| High task demand: many files, mixed objectives, hidden coupling, long context | yes/no | |
| Capability gap: missing source, stale memory, unfamiliar tool or domain | yes/no | |
| Work environment: dirty tree, failing tests, unclear branch, flaky CI | yes/no | |
| Human/model nature: overconfidence, anchoring, completion pressure | yes/no | |

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

- Assumptions are validated, gap-labeled, or assigned.
- Escalation triggers are not hidden.
- The next artifact and evidence obligation are named.

## Source-lineage note

Original Nuclear-grade template inspired by DOE-HDBK-1028-2009 questioning-attitude, validate-assumptions, pause-when-unsure, and review practices as public source lineage. No compliance claim is made.
