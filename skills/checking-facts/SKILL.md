---
name: checking-facts
description: Checks factual assertions (numbers, quotes, dates, versions, API or tool behavior, what a source actually says) against primary sources read this pass, confirming each load-bearing fact by a second independent means. Use before a packet, doc, review, or release note relies on a fact. Do not use for citation-lineage wording (checking-source-claims) or mapping claims to local test evidence (proving-claims).
---

# Checking Facts

## Overview

A fluent sentence carrying a wrong number reads exactly like one carrying a right number. Agents state facts from memory, search snippets, a secondary summary, or their own earlier output, and all of those are leads, not sources. This skill traces each load-bearing fact to its primary source, reads that source now, and confirms the fact by a second means that cannot share the first's common cause, the alternate-method rung in [`verification-methods-and-depth.md`](../../docs/02-operating-system/verification-methods-and-depth.md). A fact that survives is stated with its scope and locator. One that does not is corrected, labeled, or removed.

Boundary: `checking-source-claims` asks whether a citation is *worded* honestly (influence, not compliance). `proving-claims` maps claims about *this change* to local evidence. This skill asks whether an assertion about the world is *true*.

## Decision contract

- **Claim checked:** every load-bearing factual assertion traces to a primary source read this pass and is confirmed by a second independent means, and no unconfirmed fact is stated as settled.
- **Artifact observed:** the asserting text, each primary source at a locator, and the second means -> a fact ledger and corrected wording.
- **Decision affected:** block -- whether the text may rely on the fact as stated.
- **Failure class:** unverified-fact (asserted from memory, a summary, the actor's own output, or one source standing in for two).
- **Next action:** correct to what the source supports, label as unverified, or remove; a disputed fact under a trust-bearing decision escalates.

## When to Use

- A packet, doc, review, release note, or answer states a number, quote, date, version, limit, price, or availability.
- Text describes how an API, library, CLI, model, or service behaves.
- Text says what a statute, standard, paper, issue, or vendor page says.
- A reviewer would act differently if the fact were wrong.

## When Not to Use

- The question is whether citation wording overclaims; use `checking-source-claims`.
- The claim is about this change's behavior and a local test settles it; use `proving-claims`.
- The fact is not load-bearing and is already labeled as approximate or unverified.

## Inputs

- The text and the decision that depends on it.
- Access to primary sources: official docs at the pinned version, source code, statute text, the paper itself, raw data, or the live system.
- The mode: Quick, Standard, or Nuclear.

## Process

1. Extract each assertion. Type it: quantity, quote, date or version, behavior, attribution, or current state.
2. Mark the load-bearing ones: a decision, claim, or public statement fails if they are wrong.
3. Find the primary source, the origin rather than a page about it. Record a locator: URL or path, section or line, version, and date accessed.
4. Read it this pass. Memory, training data, a snippet, an LLM summary (including your own earlier turn), and the citing doc's paraphrase are leads.
5. Confirm by a second means that cannot share the first's common cause: an independent authoritative copy; running the code or calling the API against the docs; recomputing a number from raw data another way; an exact-string match for a quote against a second, independently published copy; a minimal reproduction at the pinned version. Re-reading the same copy is a check, not a second means. Two pages repeating one upstream are one source. Two model answers are one source.
6. Record a verdict: confirmed, confirmed with qualification, contradicted, or unverifiable. Note the version or date the fact holds for.
7. Rewrite to exactly what the sources support, with scope and locator. Present a conflict as a conflict. Label or remove what you could not verify.
8. Grade by who does the second means. Quick: the author may do both. Standard: someone other than the author does or re-runs the second means. Nuclear: that person is also briefed without the author's answer.

## Outputs

- A fact ledger in `verification.md` or beside the doc: fact | type | primary source and locator | second means | verdict | as-of.
- Corrected wording.
- Unverified or disputed facts carried as named gaps.

## Verification

- Every load-bearing fact has a primary locator, a second means, and a verdict.
- No fact is cited to memory, a snippet, or a model summary.
- Quoted text matches the source exactly; volatile facts carry an as-of date.

## Escalation

- Stop when a load-bearing fact cannot be verified and the text still asserts it.
- Escalate when sources conflict and the decision depends on which is right, or when the fact bears on public trust, safety, security, legal, or procurement.
- Return unverifiable, not a guess, when the primary source is unreachable here. Name the gap.

## Common Rationalizations

- "I know this." Memory is a lead; read the source.
- "Two sources agree." Check they do not share one upstream.
- "It is in our own docs." Your docs can carry a propagated error.
- "The docs say so." Docs drift from behavior; for behavior, run it.
- "It is a minor number." Then label it; do not assert it.

## Red Flags

- A fact with no locator, or a locator to a summary rather than the origin.
- Paraphrase inside quotation marks.
- Version-dependent behavior with no version; a price, limit, or availability with no as-of date.
- The only confirmation is the actor's own earlier output.

## Prompt

```text
Run a Nuclear-grade fact check.

Inputs:
- text and the decision that relies on it: <paste/link>
- mode: Quick / Standard / Nuclear
- primary sources available: <docs at version / code / statute / paper / data / live system>

Do this:
- Extract each assertion; type it; mark the load-bearing ones.
- Trace each to its primary source and read it this pass; record a locator.
- Confirm each load-bearing fact by a second means that cannot share the first's common cause.
- Rewrite to what the sources support, with scope and as-of date.

Return:
- a fact ledger: fact | type | primary source and locator | second means | verdict | as-of
- corrected wording
- unverified or disputed facts as named gaps, and any escalation

Do not treat memory, a snippet, or a model summary as a source. Do not imply formal verification, compliance, certification, safety, security, or regulatory adequacy.
```

## Source-lineage note

An original fact-checking workflow, not a claim to have invented source verification. Concept lineage: alternate or simplified calculational methods as one way of verifying or checking a design, by someone other than the originator (10 CFR 50 Appendix B, Criterion III), and independent verification as "freedom of thought from the performer" plus validating assumptions (DOE-HDBK-1028-2009), both mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal verification and validation, compliance, certification, or any safety, security, or regulatory guarantee.
