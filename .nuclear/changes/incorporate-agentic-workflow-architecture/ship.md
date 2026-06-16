# Ship — Incorporate Agentic Workflow Architecture

**Purpose:** State the release decision plainly for this methodology change.

---

## Release identity

- Change slug: `incorporate-agentic-workflow-architecture`
- Version / release / baseline: repository docs/methodology, branch `claude/loving-dijkstra-kd8q14`
- PR / commit / artifact: draft PR to follow
- Owner: Maintainer
- Date: 2026-06-16
- Intended release window: on human review and merge of the draft PR.

## Scope and exclusions

- Included: the stage-contract template, the workflow-architecture doctrine doc, the planner + plan-template wiring, the vocabulary reconciliation, the external-trace bridge, the discoverability surface (workflow row, matrix trigger, and the doctrine's design-pass section), the coupled CI edits, the preventive boundary test, and this packet.
- Excluded: a new skill, a standalone command card (its design pass was rehomed to the doctrine §8 to fit the generated-commands model from the single-sourcing change), validator code for stage contracts, a worked example, and an eval case.
- Known non-goals: any claim that folders replace durable runtimes, and any compliance, certification, or formal-assurance claim.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified. |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..007 stated and testable. |
| Questioning attitude | pass | `risk.md` | Captured in the risk record, not a separate file. |
| Verification | pass | `verification.md` | All deterministic gates pass. |
| Dependency / supply-chain evidence | not applicable | `basis.md` | No new dependency or service. |
| AI-assisted work checks | pass | `verification.md` | Scope, model, and actions recorded; human review pending. |
| Review / approval | planned | this PR | Human review of boundary wording before merge. |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| The stage-contract shape is not machine-enforced yet | A malformed contract could pass | defer | Maintainer | When the opt-in validator/semantic layer lands (v0.2) |
| No worked example for the new path | Less hands-on illustration | defer | Maintainer | If adopters ask for a runnable example |
| Adopters could still over-read "folders as a whole runtime" | Misapplied pattern | mitigate | Maintainer | Any issue reading the doctrine as a framework replacement |

## Rollback / restore plan

- Rollback method: `git revert` the branch commits; all edits are additive markdown plus a few registry/test lines.
- Data migration reversal or restore notes: not applicable.
- Feature flag / kill switch: not applicable for documentation.
- Owner on call: Maintainer.
- Time to restore estimate: under 10 minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI on the PR | All jobs green (tests, ruff, doctor, tokens, packet validation) | Maintainer | GitHub Actions | Fix before merge |
| Reader over-claim | No issue reads the doctrine as compliance or a framework replacement | Maintainer | GitHub issues / discussions | Patch the boundary wording |
| Packet validation | This packet keeps passing `ng validate` | Maintainer | CI "Validate change packets" step | Repair the packet |

## Handoff

- Operator/customer/support notes: this is a methodology/doc change; no runtime behavior changes.
- Docs/runbook updated: the doctrine doc, glossary, WORKFLOWS, CORE, and COMMANDS reflect the new path.
- Communication needed: the PR body points reviewers at this packet as the single place to follow the change.
- Turnover record if activated: not activated.
- Follow-up date: the next repo pass after review.

## Release decision

- Decision: ship with residual risk
- Decision maker: Maintainer (human review of the draft PR)
- Rationale: the change adds value at the planning seam, keeps CI green, and stays inside the boundary; the deferred items are named and reversible.
- Decision question answered by evidence? yes
- Conditions attached: do not add a new skill, validator code, or any compliance claim under this packet.
- Decision posture: conservative enough — reversible documentation behind a human merge gate.
- Abort or rollback trigger: a reviewer finds unbounded wording or a broken gate.
- OPEX or post-release learning trigger: an adopter misreads the pattern, or a coupled-edit class repeats.

## Baseline trigger

- Baseline required? no
- Baseline record: not applicable — no controlled runtime state changes; the merge commit is the record.
- Revalidation trigger: a future change to the planner authority model or the validator.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this branch's draft PR
- Monitoring/dashboard/log query: the CI run on the PR
- Rollback/runbook: `git revert` of the branch commits

## Exit criteria

- The release decision is stated plainly.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade change record. The stage-contract pattern adapts the Model Workspace Protocol (arXiv:2603.16021); the rung and determinism framing are original. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
