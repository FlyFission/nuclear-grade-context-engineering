---
name: checking-source-claims
description: Checks that the way you cite source families, agencies, standards, or borrowed ideas is honest and does not claim too much. Use when public docs, templates, skills, change records, or rollout copy point to outside sources. Do not use for private notes, or for checking whether code actually works.
---

# Checking Source Claims

## Overview

"Source lineage" means showing where an idea came from. Honest lineage keeps public claims clean. It links an idea to a real public source. At the same time, it keeps the repo from sounding like it formally meets that source's rules.

## When to Use

- A doc, template, skill, command, or change record cites a source family.
- New standards, frameworks, agencies, or assurance-sounding terms show up.
- A public claim might sound like compliance, certification, approval, or formal verification.
- A dependency, model, API, or vendor claim might get confused with proof from your own repo.

## When Not to Use

- The change is private code with no method claim and no source claim.
- A source cannot be made public; use private, project-specific controls outside this public repo.

## Inputs

- The changed public text.
- `docs/00-standards-foundation/source-map.md`.
- `docs/01-field-guide/source-to-concept-crosswalk.md`.
- `docs/00-standards-foundation/compliance-boundaries.md`.

## Process

1. Find every cited source family and every assurance-sounding term.
2. Confirm each direct source is public, can be linked, and is listed in the source map.
3. Sort each reference: is it an influence, an analogy, evidence, a requirement, an authority, or a vendor claim?
4. Downgrade any unconfirmed source to "supporting context" or mark it "public URL needed."
5. Reword claims as influence, idea lineage, or workflow inspiration.
6. Remove or negate any wording that implies compliance, approval, or formal assurance.

## Outputs

- Updated source-map or crosswalk rows.
- Narrowed public wording.
- A clear source-lineage note.

## Verification

- Source claims point to `source-map.md` or to public URLs.
- Public docs never present an unconfirmed source as direct lineage.
- Scans for the boundary phrases find them only in negative or disclaimer sentences.

## Escalation

- Stop when asked to cite a source that is not public, is proprietary, or is unverified as if it were public lineage.
- Escalate when the wording could affect regulated, purchasing, customer, or investor trust.

## Common Rationalizations

- "Everyone knows what we mean." Public text has to survive a hostile reader.
- "It is only an influence." Then call it an influence, not something you meet.
- "The source probably exists." Verify it or downgrade it.

## Red Flags

- A source row has no public URL and no status.
- A doc says "compliant", "approved", "certified", or "formal" outside a negative sentence.
- Every file repeats the source details instead of linking to the source map.

## Source-lineage note

This skill is an original citation-safety workflow for public-source-inspired software methodology. It does not turn cited sources into requirements this repo satisfies.
