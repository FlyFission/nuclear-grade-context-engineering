# U01 - Tiny README Fix

## Scenario Facts

- A README sentence has awkward wording.
- No code, tests, dependencies, prompts, models, tools, public assurance claims, or release posture change.
- Desired outcome: make the sentence clearer and avoid touching unrelated files.

## Simple Prompt Trial

Prompt:

```text
Fix the README typo and make sure nothing else changes.
```

Expected simple output:

- One README diff.
- A short note that no tests are needed.
- Reviewer checks `git diff`.

Simple path strengths:

- Very low overhead.
- Directly matches the work.
- Easy to review by diff.

Simple path gaps:

- Does not preserve a durable reason why no test or stronger review was needed.
- Does not explicitly screen for public assurance wording drift.

## Nuclear-Grade Trial

Skills exercised:

- `using-nuclear-grade`
- `rating-change-risk`
- `creating-change-records`
- `proving-claims`

Workflows exercised:

- Quick change

Nuclear-grade output:

- Mode: Quick.
- Packet: `risk.md`, `proof.md`.
- Claim: README-only wording change does not alter runtime behavior or public assurance posture.
- Proof: `git diff -- README.md`.
- Decision: acceptable if diff is README-only and no source/legal language changes.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 4 | 2 | 3 | 3 | 1 |
| Nuclear-grade | 4 | 3 | 4 | 3 | 2 |

Nuclear-grade adds a useful record but only marginally improves the decision. Standard mode would be unjustified.

## Decision

Use simple prompting or Quick mode. Do not use Standard unless the README wording touches public assurance, source lineage, install behavior, or release claims.

## Boundary Note

This trial evaluates workflow usefulness only. It does not prove safety, security, compliance, certification, production suitability, or formal assurance.
