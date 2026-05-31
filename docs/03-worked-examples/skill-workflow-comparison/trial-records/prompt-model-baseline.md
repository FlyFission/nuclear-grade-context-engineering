# U05 - Prompt/Model Baseline

## Scenario Facts

- An internal coding agent switches from one model and prompt pair to another.
- The agent can edit files and run tests.
- The team wants to know when the accepted prompt and model state goes out of date.

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

- Treats the prompt and model as content, not as behavior to keep under control.
- Does not name the eval evidence.
- Does not record the version that was accepted before.
- Does not name re-check triggers for when tools, the model, the prompt, or the evals drift.
- May miss source and legal wording if public docs talk about model behavior.

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

- Controlled items: the model name, the prompt version, the tool power, the eval set, and the release docs.
- Impact screen: tests, evals, docs, context packs, and power records may need updates.
- Baseline (the version everyone agreed is correct): the accepted prompt, model, and tool state, with evidence links, the claims left out, and the re-check triggers.
- Trust check: keep the model and provider claims apart from the local eval evidence and the intended-use limits.
- Evidence: eval pass/fail/gap statuses tied to the behavior claims.
- Release decision: release only if the behavior evidence backs the new known-good version, or defer with the gaps named.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 2 | 2 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 5 | 4 |

Nuclear-grade is much better because prompt and model changes are setting changes that carry a risk of behavior drift.

## Decision

Use Controlled configuration and Release readiness workflows for prompt/model baselines.

## Boundary Note

This trial does not prove model safety, security, or suitability.
