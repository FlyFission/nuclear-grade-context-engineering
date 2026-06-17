# Standard Ship Record

**Purpose:** State the acceptance decision for the graded-approach sharpening.

**Activation threshold:** Standard mode: the change edits durable public doctrine, an agent-loaded skill, and the maxims.

**Minimum useful version:** the evidence status, the leftover risks, the rollback plan, the monitoring, the handoff, the release decision, and the baseline trigger.

**Overhead trap:** Do not treat a green suite as acceptance. Ship only when the doctrine reads cleanly and the boundary wording is reviewed.

---

## Release identity

- Change slug: graded-approach-sharpening
- Version / release / baseline: branch `claude/zealous-sagan-g9sfn0`
- PR / commit / artifact: forthcoming draft PR
- Owner: FlyFission
- Date: 2026-06-17
- Intended release window: after PR review

## Scope and exclusions

- Included: the administrative floor (no packet; commit message is the record) with dominant tripwires; the non-waiver maxim; the change-vs-item rule; the performance-history modulator; the consolidated DOE-anchored lineage row + Tier 1b concept-only references; consistency lines across the public surfaces; the regenerated `ng-classify` card; a CHANGELOG entry.
- Excluded: a new standalone field-guide page; IAEA/CNSC/ONR as primary/direct lineage; any A/B/C/D taxonomy; any new skill, command, template mode, or validator/CLI change.
- Known non-goals: no compliance, safety, security, certification, formal-assurance, regulatory-adequacy, or legal-advice claim.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard; CM/baseline not activated as separate files (merge commit is the baseline) |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..006, each mapped to an existing loop and a mapped source |
| Questioning attitude | pass | `risk.md` | Questioning-attitude summary in the risk record |
| Verification | pass | `verification.md` | Suite (190 passed, 1 skipped), tokens, doctor, ruff, validate, card parity |
| Dependency / supply-chain evidence | not applicable | `verification.md` | No dependency/build/security change |
| AI-assisted work checks | pass | `verification.md` | Agent drafted; contract tests + PR review are the independent checks |
| Review / approval | planned | PR | PR review requested |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Foreign-source URLs unverified | Marked `public-url-needed`; not usable as direct lineage yet | accept | FlyFission | A current public URL confirmed in-repo |
| A reader treats the floor as a license to skip rigor | A trust-bearing change could be mislabeled administrative | mitigate | FlyFission | OPEX if a record uses the floor to skip a tripwire |
| Doctrine quality is partly review-based | Tests prove structure, not best wording | mitigate | FlyFission | PR review or future OPEX |

## Rollback / restore plan

- Rollback method: revert the branch commit; all changes are text in version control.
- Data migration reversal or restore notes: none; no data, schema, or production state touched.
- Feature flag / kill switch: not applicable.
- Owner on call: FlyFission.
- Time to restore estimate: one revert.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Floor misuse | A change crossing a tripwire is labeled administrative | FlyFission | PR diffs / commit history | OPEX; tighten tripwire wording |
| Boundary drift | A doc implies compliance with IAEA/CNSC/ONR | FlyFission | doctor, manual scan, review | Block / reword |
| Reader confusion | Floor read as a competing taxonomy | FlyFission | Issues / PR comments | Trim and reconcile to the one axis |

## Handoff

- Operator/customer/support notes: not applicable; documentation and agent-instruction change only.
- Docs/runbook updated: floor reconciled across README, WORKFLOWS, QUICKSTART, glossary, templates/README; CHANGELOG entry added.
- Communication needed: PR summary should state which report items were adopted, reframed, or rejected, and why.
- Turnover record if activated: not activated; same owner continues.
- Follow-up date: after PR review.

## Release decision

- Decision: defer until PR review passes
- Decision maker: FlyFission
- Rationale: controlled public doctrine and the maxims require slow acceptance after fast candidate edits; the change is reversible and fully evidenced locally.
- Decision question answered by evidence? yes
- Conditions attached: PR review and remote CI checks.
- Decision posture: conservative enough
- Abort or rollback trigger: prohibited compliance wording, a contract/parity/token/doctor failure, or an actionable review left unaddressed.
- OPEX or post-release learning trigger: a record uses the administrative floor to skip a tripwire, or a reader treats the floor as a separate taxonomy.

## Baseline trigger

- Baseline required? yes
- Baseline record: the squash-merge commit on the default branch is the baseline; no separate `baseline.md` because no controlled runtime state changed.
- Revalidation trigger: future changes to the modes/tiers/thresholds doctrine, the administrative-floor definition, or the non-waiver maxim.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: forthcoming draft PR on `claude/zealous-sagan-g9sfn0`
- Monitoring/dashboard/log query: not applicable (doctrine change)
- Rollback/runbook: revert the branch commit

## Exit criteria

- The release decision is stated plainly.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public ideas on configuration management, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
