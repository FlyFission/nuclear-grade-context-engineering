---
name: checking-public-claims
description: Checks public text for claims that go too far - license, warranty, safety, security, compliance, certification, or fitness wording, and how outside sources, standards, and agencies are cited - then rewrites it to stay inside what the repo proves and what each source supports. Use when editing public docs, READMEs, templates, release copy, or the public text of a change record. Do not use to check whether a fact is true (checking-facts) or for legal advice.
---

# Checking Public Claims

## Overview

Public text has to survive a hostile reader. Two kinds of overreach slip into it. The first is an assurance claim: "you may use it" quietly turning into "it is proven safe, secure, compliant, or certified." The second is a lineage claim: a cited standard or agency quietly turning from "an influence on this idea" into "a requirement this repo meets." This skill checks the wording of both and narrows it to what is actually backed. Whether a cited number or quote is *true* is a different question, for `checking-facts`.

## Decision contract

- **Claim checked:** public text keeps permission to use apart from proof of fitness; banned assurance phrases appear only in negative or disclaimer sentences; every cited source is public, mapped or marked "public URL needed", and worded as influence rather than compliance.
- **Artifact observed:** the changed public text against `LICENSE`, `DISCLAIMER.md`, `compliance-boundaries.md`, `source-map.md`, and the crosswalk -> narrowed wording, source-map rows, and scan results.
- **Decision affected:** block -- whether the public text ships; an assurance overreach blocks until reworded, while a lineage gap is a warn resolved by narrowing to influence wording or marking the source "public URL needed".
- **Failure class:** assurance-overreach or overstated-lineage.
- **Next action:** reword or downgrade before release; legal advice, regulated-use approval, or wording that affects customer, investor, or procurement trust escalates.

## When to Use

- Editing the README, install or public docs, templates, skills, commands, examples, release notes, or the public text of a change record (for example a `basis.md` that cites a standard).
- Text says safe, secure, compliant, certified, approved, enterprise-grade, or fit for regulated use.
- Text cites a standard, agency, framework, vendor, or borrowed idea.
- Getting the repo ready to be public, or writing rollout copy.

## When Not to Use

- Private code or notes with no public claim and no citation.
- Checking whether a cited fact, number, or quote is accurate (use `checking-facts`).
- Someone needs legal advice or approval for regulated use; point them to a qualified professional.

## Inputs

- The changed public text and the sources it cites.
- `LICENSE`, `DISCLAIMER.md`, `SECURITY.md`, `docs/00-standards-foundation/compliance-boundaries.md`.
- `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`.

## Process

1. List every assurance-sounding word and every cited source in the text. Work only the parts that are present.

**Assurance wording:**

2. Confirm the license is still MIT, and keep "you may use it" separate from "it is proven fit."
3. Check each trust claim against the evidence the repo actually has. Support it, narrow it, or remove it.
4. Replace broad assurance words with wording tied to evidence anyone can review, and put "this does not create..." wording where readers form expectations (onboarding, templates, command help).

**Source lineage:**

5. Confirm each cited source is public, linkable, and listed in the source map. Otherwise mark it "public URL needed" or downgrade it to supporting context.
6. Classify each reference: influence, analogy, evidence, requirement, authority, or vendor claim. Reword it as influence or idea lineage, never as compliance. Link to the source map rather than repeating source details in every file.

Then:

7. Scan the text for banned phrases and leftover internal text, and run `python tools/ng.py doctor .`.

## Outputs

- Narrowed public wording and any updated docs or templates.
- Source-map or crosswalk rows with a status per source.
- Scan and `doctor` results, or the list of gaps.

## Verification

- Public text says the repo does not create formal assurance, compliance, certification, safety, security, or regulated-use fitness.
- Banned phrases appear only in negative or disclaimer sentences.
- Every cited source points to the source map or a public URL; none is presented as direct lineage unconfirmed.

## Escalation

- Stop when asked to give legal advice, approve regulated use, confirm purchasing fitness, or cite a private, proprietary, or unverified source as public lineage.
- Escalate to qualified legal, compliance, security, or safety professionals for project-specific claims, or when wording could affect regulated, customer, procurement, or investor trust.

## Common Rationalizations

- "MIT means people can use it for anything." MIT grants permission and disclaims warranty; it does not prove fitness.
- "Disclaimers in one file are enough." Boundary wording belongs where users form expectations.
- "It is only an influence." Then call it an influence, not something you meet.
- "The source probably exists." Verify it or downgrade it.
- "Enterprise-grade means certified." Here it means testable, easy to navigate, and reviewable; say that instead.

## Red Flags

- Public copy promises safe, secure, compliant, approved, or certified results.
- A doc says "compliant", "certified", or "formal" outside a negative sentence.
- A source row has no public URL and no status.
- Examples imply more proof than they show.

## Prompt

```text
Run a Nuclear-grade public-claims check.

Inputs:
- changed public text: <paste/link>
- cited sources, standards, agencies, or vendors: <list>
- public trust claims to check: <list>
- audience: <user/team/enterprise>

Return:
- for each trust claim: supported, narrowed, or removed, with replacement wording
- for each source: verified-public, supporting-context, public-url-needed, or excluded-direct, and influence-not-compliance wording
- whether MIT permission stays separate from any fitness claim
- source-map or crosswalk updates
- the scan and doctor commands, and the final limits note

Do not judge whether a cited fact is true here; route that to checking-facts. Not legal advice.
```

## Source-lineage note

An original public-claims workflow informed by the repo license, disclaimer, compliance-boundaries, and source-foundation docs, and an original citation-safety workflow for public-source-inspired methodology. It does not turn cited sources into requirements this repo satisfies, and it is not legal advice. Sources are mapped in `docs/00-standards-foundation/source-map.md`.
