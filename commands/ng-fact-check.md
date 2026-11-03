---
description: "Checks factual assertions (numbers, quotes, dates, versions, API or tool behavior, what a source actually says) against primary sources read this pass, confirming each load-bearing fact by a second independent means."
disable-model-invocation: true
---

# ng-fact-check

Portable command prompt generated from `skills/checking-facts/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- A packet, doc, review, release note, or answer states a number, quote, date, version, limit, price, or availability.
- Text describes how an API, library, CLI, model, or service behaves.
- Text says what a statute, standard, paper, issue, or vendor page says.
- A reviewer would act differently if the fact were wrong.

## Do not use when

- The question is whether citation wording overclaims; use `checking-source-claims`.
- The claim is about this change's behavior and a local test settles it; use `proving-claims`.
- The fact is not load-bearing and is already labeled as approximate or unverified.

## Inputs

- The text and the decision that depends on it.
- Access to primary sources: official docs at the pinned version, source code, statute text, the paper itself, raw data, or the live system.
- The mode: Quick, Standard, or Nuclear.

## Prompt text

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

## Verification

- Every load-bearing fact has a primary locator, a second means, and a verdict.
- No fact is cited to memory, a snippet, or a model summary.
- Quoted text matches the source exactly; volatile facts carry an as-of date.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/checking-facts/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
