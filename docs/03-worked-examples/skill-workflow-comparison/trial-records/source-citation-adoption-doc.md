# U12 - Source Citation Adoption Doc

## Scenario Facts

- A new adoption doc explains why Nuclear-grade borrows ideas from DOE-HDBK-1028, configuration management, secure development, and software assurance sources.
- The doc should be believable without implying those sources are requirements the repo meets.

## Simple Prompt Trial

Prompt:

```text
Write an adoption doc explaining that this workflow is based on nuclear-grade and secure-development standards.
```

Expected simple output:

- Persuasive adoption text.
- Several standards or agencies named.
- Possibly broad claims about "standards-based" or "compliance-grade" practice.

Simple path strengths:

- Produces readable narrative quickly.
- Helps users understand inspiration.

Simple path gaps:

- May cite the sources too directly.
- May imply compliance or formal assurance.
- May leave out the public URL and source-map status.
- May confuse "influenced by" with "meets."

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `checking-what-a-change-affects`
- `rating-change-risk`
- `creating-change-records`
- `learning-from-experience`
- `checking-source-claims`
- `checking-legal-and-safety-wording`

Workflows exercised:

- Questioning attitude
- Standard change
- OPEX learning
- Source/legal check

Nuclear-grade output:

- Mode: Standard, because public source-lineage wording affects trust.
- Source-lineage check: every source family must be public, linkable, and mapped.
- Boundary wording: "inspired by" and "translated from public concepts," not "meets" or "implements" requirements.
- Impact screen: bring the source map, crosswalk, README, skill notes, command notes, and disclaimer in line.
- OPEX (lessons from real operation): if readers read the source lineage as compliance, update the source-map wording, templates, skills, commands, or where the disclaimer sits.
- Proof: scan for banned overclaiming phrases; check the source-map links.
- Decision: ship only if unsettled sources are downgraded or removed.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 1 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 4 | 3 |

Nuclear-grade is better because public citation wording must hold up to a hostile reading.

## Decision

Use the Source/legal check workflow for adoption docs that cite assurance, agency, or high-consequence engineering sources.

## Boundary Note

This trial does not provide legal advice, compliance determination, or formal assurance.
