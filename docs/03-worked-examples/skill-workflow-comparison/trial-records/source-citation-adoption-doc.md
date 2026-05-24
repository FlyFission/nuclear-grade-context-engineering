# U12 - Source Citation Adoption Doc

## Scenario Facts

- A new adoption doc explains why Nuclear-grade borrows ideas from DOE-HDBK-1028, configuration management, secure development, and software assurance sources.
- The doc should be credible without implying those sources are requirements the repo satisfies.

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

- May cite sources too directly.
- May imply compliance or formal assurance.
- May omit public URL/source-map status.
- May confuse "influenced by" with "satisfies."

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

- Mode: Standard because public source-lineage wording affects trust.
- Source-lineage check: every source family must be public, linkable, and mapped.
- Boundary wording: "inspired by" and "translated from public concepts," not "satisfies" or "implements" requirements.
- Impact screen: source-map, crosswalk, README, skill notes, command notes, and disclaimer alignment.
- Proof: scan for prohibited overclaiming phrases; verify source-map links.
- Decision: ship only if unresolved sources are downgraded or removed.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 1 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 4 | 4 | 3 |

Nuclear-grade is better because public citation language must survive hostile reading.

## Decision

Use Source/legal check workflow for adoption docs that cite assurance, agency, or high-consequence engineering sources.

## Boundary Note

This trial does not provide legal advice, compliance determination, or formal assurance.
