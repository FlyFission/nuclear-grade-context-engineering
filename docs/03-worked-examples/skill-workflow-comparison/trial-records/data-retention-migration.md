# U08 - Data Retention Migration

## Scenario Facts

- A product adds a 30-day retention policy for transient user logs.
- The change includes a migration, scheduled deletion job, docs, and rollback question.
- Deletion may be irreversible.

## Simple Prompt Trial

Prompt:

```text
Implement 30-day log retention and add tests.
```

Expected simple output:

- Add deletion job.
- Add a unit test for old rows being deleted.
- Update docs.

Simple path strengths:

- Gets a first implementation quickly.
- Likely tests date filtering.

Simple path gaps:

- May not distinguish soft delete from irreversible delete.
- May omit backup/restore and legal/product retention approval.
- May not identify dashboards, runbooks, support docs, and customer communication impacts.
- May ship before dry-run evidence exists.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `identifying-controlled-items`
- `screening-change-impact`
- `baselining-configuration`
- `classifying-change-risk`
- `creating-change-packets`
- `proving-claims`
- `reviewing-ship-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Release readiness

Nuclear-grade output:

- Mode: Standard, with human review if policy/legal ownership is unclear.
- Controlled items: retention policy, migration/job, backup/restore plan, dashboards, support docs, runbook.
- Impact screen: data model, scheduler, retention docs, monitoring, customer promises, rollback path.
- Proof claims: old eligible logs are selected; new logs retained; dry run count reviewed; restore path exists or irreversible deletion is consciously blocked.
- Ship decision: block if restore/dry-run evidence is missing.
- Baseline trigger: accepted retention policy and job configuration.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 2 | 2 | 2 | 1 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 5 | 5 |

Nuclear-grade is heavy but appropriate because irreversible deletion is a release and operational decision, not just a code change.

## Decision

Use Standard mode or stronger human-reviewed mode. Do not ship without dry-run, restore, monitoring, and policy-owner evidence.

## Boundary Note

This trial is not legal advice and does not prove privacy, compliance, or data governance adequacy.
