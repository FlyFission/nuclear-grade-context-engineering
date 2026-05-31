# U08 - Data Retention Migration

## Scenario Facts

- A product adds a 30-day keep-then-delete policy for short-lived user logs.
- The change includes a migration, a scheduled deletion job, docs, and a rollback question.
- The deletion may be impossible to undo.

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

- May not tell a recoverable delete apart from one you cannot undo.
- May skip backup and restore, and skip legal or product sign-off on the policy.
- May miss the effects on dashboards, runbooks, support docs, and messages to customers.
- May ship before there is any dry-run evidence.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `choosing-what-to-control`
- `checking-what-a-change-affects`
- `recording-a-known-good-version`
- `rating-change-risk`
- `creating-change-records`
- `double-checking-before-acting`
- `proving-claims`
- `checking-release-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Critical action self-check
- Release readiness

Nuclear-grade output:

- Mode: Standard, with human review if it is unclear who owns the policy or the legal side.
- Controlled items: the retention policy, the migration and job, the backup and restore plan, the dashboards, the support docs, and the runbook.
- Impact screen: the data model, the scheduler, the retention docs, the monitoring, the promises to customers, and the rollback path.
- Self-check: name the exact migration and deletion target, the expected dry-run result, and the stop condition before any action you cannot undo.
- Proof claims: the old logs that qualify are selected; new logs are kept; the dry-run count is reviewed; a restore path exists, or an unrecoverable deletion is blocked on purpose.
- Release decision: block if the restore or dry-run evidence is missing.
- Baseline trigger: the accepted retention policy and job settings.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 2 | 2 | 2 | 1 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 5 | 5 |

Nuclear-grade is heavy, but right here, because a deletion you cannot undo is a release and operations decision, not just a code change.

## Decision

Use Standard mode, or a stronger human-reviewed mode. Do not ship without dry-run, restore, monitoring, and policy-owner evidence.

## Boundary Note

This trial is not legal advice and does not prove privacy, compliance, or data governance adequacy.
