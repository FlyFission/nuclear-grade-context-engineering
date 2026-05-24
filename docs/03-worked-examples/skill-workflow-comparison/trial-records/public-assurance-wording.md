# U04 - Public Assurance Wording

## Scenario Facts

- A public README should sound credible to engineering teams.
- The repo uses high-consequence engineering source lineage.
- The wording must not imply compliance, certification, formal verification, safety, security, or regulatory adequacy.

## Simple Prompt Trial

Prompt:

```text
Make the README sound more enterprise-ready and credible.
```

Expected simple output:

- Stronger marketing language.
- More confident claims about rigor.
- Possibly words like "certified", "compliant", "safe", "secure", or "production-grade".

Simple path strengths:

- Better polish.
- Clearer value proposition.

Simple path gaps:

- High risk of overclaiming.
- Source influence may be phrased as satisfaction of requirements.
- License permission may be confused with assurance.
- No source-map or boundary review.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `screening-change-impact`
- `classifying-change-risk`
- `creating-change-packets`
- `checking-source-lineage`
- `checking-license-and-assurance-boundaries`

Workflows exercised:

- Questioning attitude
- Standard change
- Source/legal check

Nuclear-grade output:

- Decision question: can public copy be stronger without implying assurance the repo does not provide?
- Mode: Standard because public trust and source-lineage claims change.
- Source-lineage result: cite sources as public inspiration and concept lineage, not satisfied requirements.
- Legal/assurance boundary result: MIT permission remains separate from fitness, compliance, safety, security, and production suitability.
- Impact screen: README, DISCLAIMER, source-map, templates, skills, commands, and validator wording may need alignment.
- Ship decision: ship only with boundary-safe wording and prohibited-claim scan.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 1 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 4 | 3 |

Nuclear-grade is substantially better for public methodology copy because hostile reading matters.

## Decision

Use Nuclear-grade source/legal checks for public assurance wording. Do not rely on generic marketing prompts.

## Boundary Note

This trial is not legal advice and does not establish compliance or assurance.
