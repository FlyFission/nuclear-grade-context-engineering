# U05 - Prompt/Model Baseline

## Scenario Facts

- An internal coding agent changes from one model/prompt combination to another.
- The agent can edit files and run tests.
- The team wants to know when the accepted prompt/model state becomes stale.

## Simple Prompt Trial

Prompt:

```text
Update the agent prompt and model to the new version and release it.
```

Expected simple output:

- Prompt text updated.
- Model name changed.
- Maybe a short note that tests pass.

Simple path strengths:

- Fast.
- Works if the change is experimental and reversible.

Simple path gaps:

- Treats prompt/model as content, not controlled behavior.
- Does not name eval evidence.
- Does not record previous accepted state.
- Does not name revalidation triggers when tools, model, prompt, or evals drift.
- May miss source/legal wording if public docs mention model behavior.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `choosing-what-to-control`
- `checking-what-a-change-affects`
- `recording-a-known-good-version`
- `rating-change-risk`
- `vetting-outside-code-and-models`
- `proving-claims`
- `checking-release-readiness`
- `checking-source-claims`
- `checking-legal-and-safety-wording`

Workflows exercised:

- Questioning attitude
- Controlled configuration
- Agent authority change
- Trust check
- Release readiness
- Source/legal check

Nuclear-grade output:

- Controlled items: model identifier, prompt version, tool authority, eval set, release docs.
- Impact screen: tests, evals, docs, context packs, and authority records may need updates.
- Baseline: accepted prompt/model/tool state, evidence links, excluded claims, revalidation triggers.
- Trust check: model/provider claims are separated from local eval evidence and intended-use limits.
- Evidence: eval pass/fail/gap statuses linked to behavior claims.
- Release decision: release only if behavior evidence supports the new baseline or defer with named gaps.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 2 | 2 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 5 | 4 |

Nuclear-grade is much better because prompt/model changes are configuration changes with behavioral drift risk.

## Decision

Use Controlled configuration and Release readiness workflows for prompt/model baselines.

## Boundary Note

This trial does not prove model safety, security, or suitability.
