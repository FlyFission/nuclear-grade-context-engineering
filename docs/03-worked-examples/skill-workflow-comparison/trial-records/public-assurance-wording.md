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
- A source that merely inspired the work may be written up as if its requirements were met.
- License permission may be confused with assurance.
- No review of the source map or the boundaries.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `checking-what-a-change-affects`
- `rating-change-risk`
- `creating-change-records`
- `double-checking-before-acting`
- `checking-source-claims`
- `checking-legal-and-safety-wording`

Workflows exercised:

- Questioning attitude
- Standard change
- Critical action self-check
- Source/legal check

Nuclear-grade output:

- Decision question: can the public copy be stronger without implying assurance the repo does not provide?
- Mode: Standard, because public trust and source-lineage claims change.
- Source-lineage result: cite sources as public inspiration and idea lineage, not as requirements that were met.
- Self-check: name the exact public claim, the evidence behind it, the lack of a qualified outside authority, and the stop condition before the release wording is accepted.
- Legal/assurance boundary result: MIT permission stays separate from fitness, compliance, safety, security, and production suitability.
- Impact screen: the README, DISCLAIMER, source map, templates, skills, commands, and validator wording may need to be brought in line.
- Release decision: ship only with boundary-safe wording and a scan for banned claims.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 1 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 4 | 3 |

Nuclear-grade is clearly better for public method copy, because how a hostile reader reads it matters.

## Decision

Use the Nuclear-grade source and legal checks for public assurance wording. Do not rely on generic marketing prompts.

## Boundary Note

This trial is not legal advice and does not establish compliance or assurance.
