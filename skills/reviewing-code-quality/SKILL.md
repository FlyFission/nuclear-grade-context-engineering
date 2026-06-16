---
name: reviewing-code-quality
description: Reviews a diff or module for slipping standards, favoring deletion over rearranging, and ends in one honest verdict. Use when a change risks oversized files, needless layers, feature logic leaking into shared code, or clever indirection. Do not use for a trivial obvious edit, or for a check that is only about whether the code works.
---

# Reviewing Code Quality

## Overview

Standards drift in code is the slow buildup of complexity. Files grow until no one can hold them in their head. Layers get added that do not pull their weight. Logic for one feature leaks into shared code. Clever, hard-to-follow code replaces plain, direct code. Each step looks fine on its own. Added up, they make a system no one can maintain. This review holds the line and keeps standards rising. Its strongest move is deletion: prefer removing structure over moving it around. It ends in one honest verdict, not a softened summary. A review that always says "looks good" is not a control.

## Decision contract

- **Claim checked:** the diff was read against its goal, deletion was considered before rearranging for each complexity finding, and the verdict matches the findings -- an INCONCLUSIVE verdict naming the missing evidence.
- **Artifact observed:** the diff or module, its mission anchor or goal, and the shared-versus-feature layering map -> a ranked findings list (each with location, standard at risk, concrete fix) and one verdict with a reason.
- **Decision affected:** block -- one verdict on the diff or module: VERIFIED, NOT VERIFIED, or INCONCLUSIVE.
- **Failure class:** standards-drift (oversized files, thin pass-through layers, feature logic in shared code, or clever indirection accepted as fine).
- **Next action:** return NOT VERIFIED for the owner to decide, or INCONCLUSIVE naming the missing context; standards drift that recurs escalates to a control.

## When to Use

- A diff or module is up for review and you want a standards check, not just a "does it work" check.
- A file or function has grown large, or a new layer is being added.
- Logic for one feature may be leaking into shared, core, or framework code.
- A rewrite is proposed and you need to judge whether it removes complexity or just moves it.
- An agent wrote code fast and the question is whether anyone can maintain it.

## When Not to Use

- The change is a trivial, obvious edit with no effect on structure.
- The task is only about whether the code works (use proving-claims and verification instead).
- A quick fix has to ship to contain a live incident before a quality pass makes sense.

## Inputs

- The diff or module under review and the files around it.
- The change's mission anchor or goal, so you can judge scope.
- Project conventions and any countable limits the team agreed on.
- The map of dependencies and layers: what is shared or core versus tied to one feature.

## Process

1. Read the change against its goal. Code that does not serve the stated goal is scope drift. Flag that before you judge style.
2. Look for deletion first. Ask what could be removed entirely, not just reorganized. Prefer cutting structure over moving it.
3. Use countable warning lines as prompts, not hard laws. A file past roughly 1000 lines, a function past roughly 50 lines, deep nesting, or repeated branches are signals to look closer. Give a reason each time.
4. Test every layer for its worth. A wrapper, helper, or layer must remove more complexity than it adds. Flag thin pass-throughs and code that only renames something.
5. Check the layering. Logic for one feature must not leak into shared, core, or framework code. Flag special cases that mess up a general path.
6. Prefer boring over clever. Flag magic, hidden links between parts, and indirection where plain, direct code would read clearly.
7. Give one verdict, with no hedging.

## Outputs

- A ranked list of findings. Each one names the location, the standard at risk, and the concrete fix (often a deletion).
- One verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE.
- A short reason tying the verdict to the findings.

## Verification

- Each finding points to a specific spot and a specific standard, not a general feeling.
- For each complexity finding, deletion was considered before rearranging.
- The verdict matches the findings. An INCONCLUSIVE verdict names what evidence is missing and routes to escalation.

## Escalation

- Return NOT VERIFIED when a finding would hurt maintainability and the author disagrees. Let the owner decide with the finding on record.
- Return INCONCLUSIVE when you cannot judge the diff without context the review does not have. Name the missing context.
- Escalate when slipping standards keep coming back across changes. A repeated exception is a pattern. The fix is a control, not another one-off review.

## Common Rationalizations

- "It works, so the structure is fine." Working is correctness. This review is about whether the next change stays cheap.
- "The layer might be useful later." A layer built for a maybe-someday need is complexity now for a benefit that may never come.
- "It is only a little over the limit." Limits exist because little overages are how files become unreadable.
- "Rewriting it would touch a lot." Moving complexity is not removing it. Ask what would delete the need.
- "The author is experienced." The review checks the code, not the author.

## Red Flags

- A file or function well past the agreed size with no breaking-up.
- A wrapper or helper that only forwards calls or renames a thing.
- Feature-specific branches inside shared or core code.
- Clever indirection where plain, direct code would read clearly.
- A review summary that softens every finding into "looks good" with no verdict.

## Prompt

```text
Run a Nuclear-grade code-quality review on this change.

Inputs:
- diff or module:
- objective / mission anchor:
- agreed limits or conventions:
- shared vs feature-specific layers:

Do this:
- Read the change against its goal; flag scope drift first.
- Look to delete before you rearrange; ask what can be removed entirely.
- Use the countable tripwires as prompts, not laws (file around 1000 lines, function around 50 lines, deep nesting, duplicated branches).
- Test each abstraction: it must remove more complexity than it adds; flag thin pass-throughs.
- Check the layering: flag feature logic leaking into shared, canonical, or framework code.
- Prefer plain, direct code over clever indirection.

Return:
- a ranked list of findings (location, the standard at risk, a concrete fix, often a deletion)
- one verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE
- a short reason tying the verdict to the findings

Do not soften every finding into "looks good." Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Source-lineage note

This skill is an original software workflow influenced by nuclear-industry rising-standards and questioning-attitude culture (Rickover and Navy nuclear practice as concept lineage, not an implemented program) and by the self-checking and verification practices in DOE-HDBK-1028-2009 mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
