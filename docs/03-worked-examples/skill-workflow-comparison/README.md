# Skill and Workflow Comparison

**Purpose:** Test whether Nuclear-grade skills and workflows produce better records for review than simple prompting, and find where the extra work is not worth it.

**Status:** A judgment-based look at the records. This is not a benchmark, a user study, a safety claim, a security claim, a compliance claim, a certification claim, a production-suitability claim, or a formal assurance result.

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

Nuclear-grade does not beat simple prompting on every task. For tiny, local changes you can undo, where the proof is obvious, the extra work is barely worth it. It is well worth it when the work touches agent power, trust in dependencies, public assurance wording, prompt and model drift, data you cannot undo, side effects that move money, release stance, or evidence gaps that must turn into ship, defer, or block decisions.

## Boundary Note

This comparison judges how useful the workflow records are for review. It does not prove safety, security, compliance, certification, formal verification, formal validation, production suitability, or regulatory adequacy.

## Source-Lineage Note

This evaluation is an original Nuclear-grade adoption artifact. It uses the repo operating model and the public-source lineage summed up in `docs/00-standards-foundation/source-map.md`.
