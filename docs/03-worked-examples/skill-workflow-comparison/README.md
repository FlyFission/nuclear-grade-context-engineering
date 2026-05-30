# Skill and Workflow Comparison

**Purpose:** Evaluate whether Nuclear-grade skills and workflows produce better review artifacts than simple prompting, and where the overhead is not justified.

**Status:** Qualitative artifact evaluation. This is not a benchmark, user study, safety claim, security claim, compliance claim, certification claim, production-suitability claim, or formal assurance result.

## Read This First

The earlier version of this comparison was intentionally replaced because it was too shallow: it summarized outcomes without preserving enough trial evidence. This version keeps the comparison inspectable.

| Artifact | Use |
|---|---|
| [`methodology.md`](methodology.md) | Evaluation rules, scoring rubric, limits, and bias controls. |
| [`results-summary.md`](results-summary.md) | Aggregate findings, score table, and recommendations. |
| [`trial-records/`](trial-records/) | Per-use-case records with simple prompt output, Nuclear-grade output, scoring rationale, and residual concerns. |
| [`efficacy-harness.md`](efficacy-harness.md) | A reproducible `python tools/ng.py eval .` check that each worked example still surfaces the decision signals it claims. Mechanical and runnable, unlike the author-judged scores. |

## Trial Set

| ID | Trial | Main question |
|---|---|---|
| U01 | [`tiny-readme-fix.md`](trial-records/tiny-readme-fix.md) | Does Quick mode add anything over a direct docs prompt? |
| U02 | [`agent-workspace-boundary.md`](trial-records/agent-workspace-boundary.md) | Does the workflow reveal boundary and non-claim gaps for agent writes? |
| U03 | [`dependency-security-update.md`](trial-records/dependency-security-update.md) | Does the workflow separate behavior proof from advisory proof? |
| U04 | [`public-assurance-wording.md`](trial-records/public-assurance-wording.md) | Does source/legal checking prevent public overclaiming? |
| U05 | [`prompt-model-baseline.md`](trial-records/prompt-model-baseline.md) | Does configuration management help with prompt/model drift? |
| U06 | [`validator-agent-handoff.md`](trial-records/validator-agent-handoff.md) | Does a context pack improve agent authority and stopping rules? |
| U07 | [`payment-webhook-idempotency.md`](trial-records/payment-webhook-idempotency.md) | Does Standard mode help with money-moving side effects? |
| U08 | [`data-retention-migration.md`](trial-records/data-retention-migration.md) | Does impact screening expose irreversible data and rollback gaps? |
| U09 | [`release-readiness-cut.md`](trial-records/release-readiness-cut.md) | Does ship readiness beat "CI is green" for a release cut? |
| U10 | [`incident-regression-fix.md`](trial-records/incident-regression-fix.md) | Does the workflow avoid hiding incident learning after a quick fix? |
| U11 | [`external-api-tool-permission.md`](trial-records/external-api-tool-permission.md) | Does agent-authority workflow control API, credential, and network scope? |
| U12 | [`source-citation-adoption-doc.md`](trial-records/source-citation-adoption-doc.md) | Does source-lineage checking improve adoption docs that cite assurance sources? |

## Coverage

Every published skill appears in multiple trial records, and every published workflow appears in multiple trial records. Tests enforce that the comparison mentions every cataloged skill and workflow and that enough trial records exist.

## Bottom Line

Nuclear-grade does not beat simple prompting on every task. It is weakly justified for tiny, local, reversible changes where the proof is obvious. It is strongly justified when work touches agent authority, dependency trust, public assurance wording, prompt/model drift, irreversible data, money-moving side effects, release posture, or evidence gaps that must become ship/defer/block decisions.

## Boundary Note

This comparison evaluates review usefulness of workflow artifacts. It does not prove safety, security, compliance, certification, formal verification, formal validation, production suitability, or regulatory adequacy.

## Source-Lineage Note

This evaluation is an original Nuclear-grade adoption artifact using the repo operating model and public-source lineage summarized in `docs/00-standards-foundation/source-map.md`.
