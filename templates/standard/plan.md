# Standard Plan Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Bound the work so the build, the review, the verification, and the rollback are planned before the change grows.

**Activation threshold:** Use for Standard changes where the build has several steps, affected controlled items, dependency/model/tool decisions, rollback concerns, or a review order to plan.

**Minimum useful version:** the build sequence, the affected files and assets, the non-goals, the review checkpoints, the rollback approach, and the proof commands.

**Overhead trap:** Do not write a project plan for a small change. Capture only the decisions you need to build and review the change without losing the intent.

---

## Change context

- Slug:
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner:
- Date:
- Current lifecycle phase: Plan / Execute / Verify / Review / Decide

## Charter and anchor check

A gate you check more than once, not a one-time note. Confirm it before Plan, and check it again before Verify. See `staying-on-mission`.

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no:
- Re-checked before Verify? yes/no/not yet:
- Charter articles in play:

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| | | | |

## Build sequence

Number the fewest steps needed to finish the change. Stamp each step with the
requirement IDs it delivers (`REQ-NNN` from `basis.md` or `spec.md`) so the chain
requirement → task → code → evidence stays unbroken. Every requirement should
appear against at least one step; a step with no requirement is either scaffolding
or scope creep — say which.

For work that will be handed to another agent or session, make each step a delegable
slice written as a **stage contract**: name its prerequisites, its **Inputs by exact
`file#section`** (and a context budget, so the runner is not handed the whole plan), the
**Outputs** and where they land, the proof that closes it, and the stop or done condition.
This is a handoff contract, not a schedule — see `briefing-an-agent`, `handing-off-work`,
the full form in `templates/standard/stage-contract.md`, and the doctrine in
`docs/02-operating-system/agentic-workflow-architecture.md`. Writing the inputs here is what
lets a human review what each fan-out slice will and will not load before build authority opens.

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | | REQ-001 | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

For any slice whose work is model-mediated, record its **determinism posture** (model id,
prompt reference, and which steps are replayable vs human judgment) — a disclosure of what can
be reproduced, not a guarantee. See `docs/02-operating-system/agentic-workflow-architecture.md`.

## Two-speed work plan

Keep fast trial work apart from the slower gates where work is accepted.

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | | |
| candidate | | |
| audit | | |
| accept | | |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| | | | | |

## Agent briefing

- Role:
- Authority source:
- Active procedure/template:
- Last completed action if resumed:
- Handoff or turnover needed? yes/no:
- Pause when unsure condition:

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| | | REQ-001 | | |

## Non-goals

List what this change does not do, on purpose.

-
-

## Dependency / model / tool decisions

Use only if activated.

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| | | | | |

## Review checkpoints

Approve the work in stages, not all at once. Each gate is approved by a human (or
an out-of-band check the agent cannot rewrite) before the next phase opens — an
agent that drafts and self-approves its own spec is the "ships green by editing its
own test" trap. See the agent-drafts-spec workflow in `CORE.md`.

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each requirement is one clear trigger→response statement with a `REQ-NNN` ID, reviewed by a human. | planned / pass / gap |
| Design approved | The design outline in `basis.md` is complete enough for this change and reviewed. | planned / pass / gap |
| Tasks approved | Every build step carries the requirement IDs it delivers, and the sequence is reviewed. | planned / pass / gap |
| Specification reviewed | The protected outcomes, the outcomes to prevent, and the assumptions are stated plainly. | planned / pass / gap |
| Tests/evals defined | Each piece of evidence maps to a claim. | planned / pass / gap |
| Build complete | The affected files match the plan. | planned / pass / gap |
| Verification complete | The evidence is linked in `verification.md`. | planned / pass / gap |
| Release decision ready | The leftover risks and the rollback are recorded. | planned / pass / gap |
| Turnover complete if activated | The next owner has the state, the authority, the stop rules, and the work left to do. | planned / pass / gap |

## Rollback approach

- Rollback method:
- State/data reversal notes:
- Feature flag / kill switch:
- Owner:
- Time to restore estimate:

## Proof commands

```bash
# command(s) or manual checks needed before ship
```

## Required links

- `risk.md`
- `basis.md` or `spec.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc:

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software lifecycle, keeping the approved version under control (CM), software assurance, secure development, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
