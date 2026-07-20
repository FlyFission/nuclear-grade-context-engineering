# Skill and Workflow Comparison

**Purpose:** Formatively inspect which decision signals appear in author-constructed Nuclear-grade records versus simple-prompt records, and find where the added structure appears unnecessary.

**Status:** Formative, author-produced artifact inspection. The scores are design feedback, not efficacy evidence. This is not a benchmark, controlled experiment, user study, safety claim, security claim, compliance claim, certification claim, production-suitability claim, or formal assurance result. For the mechanized, per-skill complement to this comparison — headless with/without-skill runs, blind grading, real cost/token data, and every raw response public — see [`evals/skill-benchmark-pilot/`](../../../evals/skill-benchmark-pilot/).

## Read This First

We replaced the earlier version of this comparison on purpose, because it was too thin: it summed up outcomes without keeping enough trial evidence. This version keeps the comparison open to inspection.

| Artifact | Use |
|---|---|
| [`methodology.md`](methodology.md) | The rules, the scoring guide, the limits, and the steps that guard against bias. |
| [`results-summary.md`](results-summary.md) | The combined findings, the score table, and the advice. |
| [`trial-records/`](trial-records/) | One record per use case, with the simple-prompt output, the Nuclear-grade output, the scoring reasons, and the leftover concerns. |
| [`efficacy-harness.md`](efficacy-harness.md) | A repeatable `python tools/ng.py eval .` check that each worked example still surfaces the decision signals it claims. It runs on its own, unlike the author-judged scores. |

## Trial Set

| ID | Trial | Main question |
|---|---|---|
| U01 | [`tiny-readme-fix.md`](trial-records/tiny-readme-fix.md) | Does Quick mode add anything over a direct docs prompt? |
| U02 | [`agent-workspace-boundary.md`](trial-records/agent-workspace-boundary.md) | Does the workflow surface the boundary and the gaps in what is claimed for agent writes? |
| U03 | [`dependency-security-update.md`](trial-records/dependency-security-update.md) | Does the workflow keep proof of behavior apart from proof of the advisory? |
| U04 | [`public-assurance-wording.md`](trial-records/public-assurance-wording.md) | Does checking the source and the legal wording stop public overclaiming? |
| U05 | [`prompt-model-baseline.md`](trial-records/prompt-model-baseline.md) | Does keeping the approved version under control help with prompt and model drift? |
| U06 | [`validator-agent-handoff.md`](trial-records/validator-agent-handoff.md) | Does a context pack improve the agent's power limits and stop rules? |
| U07 | [`payment-webhook-idempotency.md`](trial-records/payment-webhook-idempotency.md) | Does Standard mode help with side effects that move money? |
| U08 | [`data-retention-migration.md`](trial-records/data-retention-migration.md) | Does the impact check expose data you cannot undo and gaps in rollback? |
| U09 | [`release-readiness-cut.md`](trial-records/release-readiness-cut.md) | Does a ship-readiness check beat "CI is green" for a release? |
| U10 | [`incident-regression-fix.md`](trial-records/incident-regression-fix.md) | Does the workflow keep the incident's lessons from being hidden after a quick fix? |
| U11 | [`external-api-tool-permission.md`](trial-records/external-api-tool-permission.md) | Does the agent-power workflow control the API, the credentials, and the network scope? |
| U12 | [`source-citation-adoption-doc.md`](trial-records/source-citation-adoption-doc.md) | Does checking source lineage improve adoption docs that cite assurance sources? |

## Coverage

Every published skill shows up in more than one trial record, and so does every published workflow. Tests make sure the comparison mentions every listed skill and workflow, and that enough trial records exist.

## Bottom Line

In the constructed artifacts, the added structure exposed few additional decision signals for tiny, local, reversible changes. It exposed more of the seeded authority, dependency, public-claim, model-drift, irreversible-data, payment, release, and evidence-gap signals in the consequential scenarios. Because the same author designed and scored both paths, this supports repository iteration only; it does not establish that Nuclear-grade improves real reviewer decisions.

## Boundary Note

This comparison judges how useful the workflow records are for review. It does not prove safety, security, compliance, certification, formal verification, formal validation, production suitability, or regulatory adequacy.

## Source-Lineage Note

This evaluation is an authored Nuclear-grade adoption artifact. It uses the repo operating model and the public-source lineage summed up in `docs/00-standards-foundation/source-map.md`.
