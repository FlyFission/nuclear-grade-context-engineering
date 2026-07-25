---
name: verifying-final-artifacts
description: Verifies the delivered artifact a consumer actually receives (a figure, chart, PDF, SVG, screenshot, compiled build, or deployed response) by regenerating it fresh and directly observing the output, not the source that produces it, and ends in one honest verdict. Use when the deliverable is a produced artifact and correctness lives in the rendered result. Do not use for a pure source or code diff with no separate produced output; use reviewing-code-quality instead.
---

# Verifying Final Artifacts

## Overview

Reviewing the code, config, or markup that *produces* a figure, chart, PDF, or interface -- and calling it done without opening the actual output -- is validating the recipe, not the meal. The generator is not the artifact. A plotting script can be correct line by line and still emit a figure with overlapping labels, a substituted font, a clipped axis, or a legend off the page. A LaTeX source can compile "cleanly" into a PDF whose table breaks across a page boundary. A UI component can look right in source and render broken. A deploy config can be valid and the live endpoint still return the wrong body.

The delivered artifact is the only thing the consumer ever sees, and the only place these defects appear. None of them is reliably predictable from a source read. This skill holds that line: it regenerates the artifact fresh, observes the real output the way a consumer would, compares it to the spec, and loops -- fix the source, regenerate, look again -- until the observed artifact is right or a stop condition is hit. It ends in one honest verdict, not a verdict inferred from "the diff looks correct."

## Decision contract

- **Claim checked:** the final delivered artifact, freshly regenerated this pass and directly observed, meets its spec or acceptance criteria -- the source that generates it was not accepted as a stand-in for the output.
- **Artifact observed:** the regenerated output itself (the image opened, every PDF page rasterized and read, the UI screenshotted, the endpoint response fetched) compared against the spec or reference -> a findings list, each defect tied to a location in the *output* and the source line responsible, plus one verdict.
- **Decision affected:** block -- whether the artifact ships as-is, or the source must change and the artifact be regenerated and re-observed before it can ship.
- **Failure class:** source-proxy error (approving the generator in place of the thing it generates) or stale-artifact error (reviewing a cached or old export instead of a freshly regenerated one).
- **Next action:** NOT VERIFIED routes the fix back to the source and then back into the same regenerate-and-observe loop; it does not exit on "the diff looks right."

## When to Use

- The deliverable is a produced artifact a consumer receives directly -- a book or document figure, a generated chart or diagram, a PDF, DOCX, or slide export, a built-UI screen, a compiled binary or app, an exported dataset, or a deployed endpoint's real response.
- An agent has "reviewed" the artifact by reading the source that makes it, and has not itself looked at the output.
- A figure or export keeps getting declared fixed, but the visible defect is still there.
- Correctness of this change lives in how the result renders, paginates, or responds -- not in whether the source is tidy.

## When Not to Use

- The change is a pure source or code diff with no separate produced output -- use `reviewing-code-quality` instead.
- The claim is textual or non-produced and needs claim-to-evidence mapping rather than a rendered observation -- use `proving-claims` instead.
- A one-line fix where the same freshly regenerated artifact was already observed this pass and nothing downstream of it changed.

## Inputs

- The spec or acceptance criteria for the artifact: a reference image, a style guide, the required elements, the expected page count, the expected response shape.
- The current source or generator, and the exact command or tool that produces the artifact.
- A way to actually observe the output at consumer granularity. See `references/observation-recipes.md` for how to make each artifact type observable.

## Process

1. Name the artifact's true final form and exactly how you will observe it directly -- open the image, rasterize every PDF page and read the pages, screenshot the built UI, fetch the deployed response. Observing metadata *about* the artifact (a build log, a "0 errors" line, the source diff) is not observing the artifact.
2. Regenerate the artifact fresh from the current source. Never review a cached or stale export; a stale artifact hides both old defects and the effect of the latest change.
3. Look at the actual output at the granularity a consumer sees it -- the full image, every page, every affected screen or response -- *before* forming any opinion about whether the source is correct.
4. Compare against the spec criterion by criterion. Log concrete defects: overlapping labels, cut-off text, wrong font or color, broken pagination, misaligned elements, a corrupted embed, a wrong response. "Looks fine" is not an observation.
5. Only now trace each *observed* defect to the specific source location responsible. Do not jump from reading the source to a verdict; the observation comes first, the source explains it second.
6. Fix the source, then regenerate and re-observe the new artifact from scratch. Do not assume the fix worked because the source diff looks right -- the re-render-and-re-look is the actual validation. Repeat until the observed artifact matches the spec or the iteration budget is spent.
7. Give one verdict, with no hedging.

## Outputs

- The freshly regenerated artifact that the verdict is about.
- A findings list: each defect, its location in the observed output, the source line responsible, and the fix applied.
- The iteration count -- how many regenerate-and-observe loops it took.
- One verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE, with a short reason tying it to what was observed.

## Verification

- The artifact the verdict is about was regenerated this pass, not reused from a prior run.
- Every finding cites a location in the observed output, not only a source line.
- The verdict followed a direct look at the final artifact -- not an inference from the source diff or a build log.

## Escalation

- After a small named budget of loops without converging (default three), stop and return NOT VERIFIED or INCONCLUSIVE naming the remaining defects, rather than looping indefinitely.
- Return INCONCLUSIVE when the real output cannot be observed in this environment -- no renderer, viewer, or network to reach the artifact. A tooling gap is a named gap, not a pass; route it to whoever can run the toolchain.
- Escalate when the artifact is public-facing or trust-bearing and the observed defect would reach a consumer.

## Common Rationalizations

- "The code looks right, so the output must be right." Correct source is necessary, not sufficient; the defects this skill catches live only in the render.
- "I already checked this figure last iteration." A prior look is not a look at the artifact you just regenerated. Re-observe or you are trusting a stale artifact.
- "Close enough, a human will eyeball it at the end." Deferring the look is how the defect ships; the point is to look now, in the loop.
- "The build reported no errors." A clean build is a claim about the process, not an observation of the product.

## Red Flags

- A verdict given with no fresh render this pass.
- Findings that cite source lines but no location in the actual output.
- The same defect surviving two loops because the fix was checked against the source, not the re-rendered artifact.
- Public wording that calls the artifact correct, safe, or approved with no observed evidence behind it.

## Prompt

```text
Run a Nuclear-grade final-artifact verification on this deliverable.

Inputs:
- artifact and its true final form (figure / PDF / SVG / screenshot / build / deployed response):
- spec or acceptance criteria (reference image, style guide, required elements, page count, expected response):
- command or tool that produces the artifact:
- how the output will be observed directly (see references/observation-recipes.md):

Do this:
- Regenerate the artifact fresh; never review a cached or stale export.
- Look at the actual output at consumer granularity (full image, every page, every screen or response) before judging the source.
- Compare against the spec criterion by criterion; log concrete defects, not "looks fine."
- Trace each observed defect to the source line responsible, then fix, regenerate, and re-observe the new artifact.
- Repeat until the observed artifact matches the spec or the loop budget (default three) is spent.

Return:
- a findings list (defect, location in the output, source line responsible, fix applied)
- the iteration count
- one verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE
- a short reason tying the verdict to what was observed

Do not give a verdict without a fresh render this pass. Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Source-lineage note

This skill is an original software-workflow control influenced by the verification-versus-source-review discipline in the self-checking and independent-verification practices of DOE-HDBK-1028-2009 mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal verification and validation, safety, security, certification, or regulatory adequacy.
