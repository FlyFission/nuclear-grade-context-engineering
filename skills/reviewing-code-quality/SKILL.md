---
name: reviewing-code-quality
description: Use when reviewing a diff or module for standards drift: oversized files, needless abstraction, leaked feature logic, or complexity that should be deleted.
---

# Reviewing Code Quality

## Overview

Standards drift in code is the slow accretion of complexity: files grow past the point of comprehension, abstractions get added that do not earn their keep, feature-specific logic leaks into shared layers, and clever indirection replaces boring direct code. Each step is locally defensible; the sum is an unmaintainable system. This review holds a rising-standards line. Its strongest move is deletion: prefer removing structure over rearranging it. It ends in a single honest verdict, not a softened summary, because a review that always says "looks good" is not a control.

## When to Use

- A diff or module is up for review and you want a standards check, not just a correctness check.
- A file or function has grown large, or an abstraction layer is being added.
- Feature logic may be leaking into shared, canonical, or framework layers.
- A refactor is proposed and you need to judge whether it removes complexity or just moves it.
- An agent produced code quickly and the question is whether it will be maintainable.

## When Not to Use

- The change is a trivial, obvious edit with no structural impact.
- The task is purely about whether the code is functionally correct (use proving-claims and verification instead).
- A hotfix must ship for incident containment before a quality pass is reasonable.

## Inputs

- The diff or module under review and its surrounding files.
- The change's mission anchor or objective, so scope can be judged.
- Project conventions and any countable limits the team has agreed.
- The dependency and layering map: what is shared/canonical versus feature-specific.

## Process

1. Read the change against its objective. Code that does not serve the stated objective is scope drift; flag it before judging style.
2. Look first for deletion. Ask what could be removed entirely rather than reorganized. Prefer cutting structure over moving it.
3. Apply countable tripwires as prompts, not laws: a file crossing roughly 1000 lines, a function past roughly 50 lines, deep nesting, or duplicated branches are signals to investigate, each with rationale.
4. Test every abstraction for its keep. A wrapper, helper, or layer must remove more complexity than it adds; flag thin pass-throughs and indirection that only renames.
5. Check layering. Feature-specific logic must not leak into shared, canonical, or framework code; flag special cases that pollute a general path.
6. Prefer boring over clever. Flag magic, implicit coupling, and indirection where direct code would read plainly.
7. Issue one verdict with no hedging.

## Outputs

- A prioritized findings list: each finding names the location, the standard at risk, and the concrete fix (often a deletion).
- A single verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE.
- A short rationale tying the verdict to the findings.

## Verification

- Each finding points to a specific location and a specific standard, not a general impression.
- Deletion was considered before rearrangement for each complexity finding.
- The verdict matches the findings; an INCONCLUSIVE verdict names what evidence is missing and routes to escalation.

## Escalation

- Return NOT VERIFIED when a finding would degrade maintainability and the author disagrees; let the owner decide with the finding on record.
- Return INCONCLUSIVE when the diff cannot be judged without context the review does not have; name the missing context.
- Escalate when standards drift recurs across changes; a repeated concession is a pattern, and the fix is a control, not another one-off review.

## Common Rationalizations

- "It works, so the structure is fine." Working is correctness; this review is about whether the next change stays cheap.
- "The abstraction might be useful later." Speculative abstraction is complexity now for a benefit that may never arrive.
- "It is only a little over the limit." Limits exist because the little overages are how files become unreadable.
- "Refactoring it would touch a lot." Moving complexity is not removing it; ask what deletes the need.
- "The author is experienced." The review checks the code, not the author.

## Red Flags

- A file or function well past the agreed size with no decomposition.
- A wrapper or helper that only forwards calls or renames a thing.
- Feature-specific branches inside shared or canonical code.
- Clever indirection where boring direct code would read plainly.
- A review summary that softens every finding into "looks good" with no verdict.

## Source-lineage note

This skill is an original software workflow influenced by nuclear-industry rising-standards and questioning-attitude culture (Rickover and Navy nuclear practice as concept lineage, not an implemented program) and by the self-checking and verification practices in DOE-HDBK-1028-2009 mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
