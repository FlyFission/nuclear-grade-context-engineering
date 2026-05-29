---
name: checking-source-lineage
description: Checks that citations of source families, agencies, standards, or borrowed concepts are source-safe and non-overclaiming. Use when public docs, templates, skills, packets, or adoption copy reference outside sources. Do not use for private notes, or for verifying the functional correctness of code.
---

# Checking Source Lineage

## Overview

Source lineage keeps public claims honest. It links concepts to public sources while preventing the repo from implying formal compliance with those sources.

## When to Use

- A doc, template, skill, command, or packet cites a source family.
- New standards, frameworks, agencies, or assurance terms appear.
- A public-facing claim may sound like compliance, certification, approval, or formal verification.
- Dependency, model, API, or vendor source claims may be confused with local proof.

## When Not to Use

- The change is private implementation code with no methodology or source claim.
- A source cannot be public; use project-specific private controls outside this public repo.

## Inputs

- Changed public text.
- `docs/00-standards-foundation/source-map.md`.
- `docs/01-field-guide/source-to-concept-crosswalk.md`.
- `docs/00-standards-foundation/compliance-boundaries.md`.

## Process

1. Identify every cited source family and assurance-sounding term.
2. Confirm each direct lineage source is public, linkable, and listed in the source map.
3. Separate influence, analogy, evidence, requirement, authority, and vendor/source claim.
4. Downgrade unresolved sources to supporting context or public URL needed.
5. Rewrite claims as influence, concept lineage, or workflow inspiration.
6. Remove or negate language that implies compliance, approval, or formal assurance.

## Outputs

- Updated source-map or crosswalk rows.
- Narrowed public wording.
- Explicit source-lineage note.

## Verification

- Source claims point to `source-map.md` or public URLs.
- Public docs do not present unresolved sources as direct lineage.
- Boundary scans find only negative or disclaimer contexts for prohibited phrases.

## Escalation

- Stop when asked to cite inaccessible, proprietary, or unverified sources as public lineage.
- Escalate when wording could affect regulated, procurement, customer, or investor trust.

## Common Rationalizations

- "Everyone knows what we mean." Public text must survive hostile reading.
- "It is only an influence." Name it as influence, not satisfaction.
- "The source probably exists." Verify or downgrade.

## Red Flags

- A source row has no public URL or status.
- A doc says "compliant", "approved", "certified", or "formal" outside a negative boundary.
- Every artifact repeats source details instead of linking to the source map.

## Source-lineage note

This skill is an original citation-safety workflow for public-source-inspired software methodology. It does not turn cited sources into requirements this repo satisfies.
