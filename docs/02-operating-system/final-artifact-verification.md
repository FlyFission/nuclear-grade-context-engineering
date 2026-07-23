# Final-Artifact Verification

**Purpose:** Name a failure the control loop makes routinely — verifying the *source* that produces a deliverable instead of the deliverable itself — and state the defense: observe the freshly regenerated artifact the consumer actually receives, and loop until it is right. This is the artifact-facing complement to [actor-evidence independence](actor-evidence-independence.md): that page keeps the evidence honest about *who authored it*; this one keeps it honest about *what was actually observed*.

**Status:** Doctrine for the PROVE **Observe** stage, realized as the [`verifying-final-artifacts`](../../skills/verifying-final-artifacts/SKILL.md) skill. Not a compliance, certification, or formal-V&V workflow.

---

## The hole

Most agent work produces something a consumer receives at one remove from the source that made it: a plotting script emits a figure, a LaTeX or Markdown source compiles to a PDF, a component renders to a screen, a config deploys to a live endpoint, a query exports to a dataset. The **artifact of consequence** is the figure, the PDF, the screen, the response, the file — not the code.

When an agent is asked to verify such a deliverable, it reaches for what it can read most easily: the source. It reads the plotting code, confirms the axes are set and the labels assigned, and reports the figure correct. But the source being correct is *necessary, not sufficient*. A whole class of defects exists only in the rendered output and is invisible to a source read:

- overlapping or clipped labels, legends off the page, misaligned elements
- a substituted font because the intended one did not resolve at render time
- a table or figure that breaks across a page boundary
- a component that is correct in JSX and still renders broken
- a valid deploy config whose live endpoint returns the wrong body
- an export step that corrupts what the query returned correctly

The loop's Observe stage quietly substitutes the generator for the thing it generates. Call this the **source-proxy error**. Its close cousin is the **stale-artifact error**: reviewing a cached or previous export instead of one regenerated from the current source, so the review reflects neither the old state nor the change.

## Why it is worth a named control

This is the failure a book author hit iterating on figures: an agent "reviewed" each figure by reading its generating code and kept declaring success, while the exported images still carried the visible defect. Only an explicit instruction to *look at the rendered figure* and *loop* — regenerate, observe, fix the source, regenerate, observe again — surfaced and corrected the real issues. Left implicit, the source read wins every time because it is cheaper; the discipline has to be a standing control, not a thing re-typed by hand.

## The defense

At the Observe stage, when the deliverable is a produced artifact, **observation means looking at the freshly regenerated artifact itself**, at the granularity a consumer sees it, before judging the source. The loop is:

```text
regenerate fresh  ->  observe the real output  ->  compare to spec  ->
trace each observed defect to its source line  ->  fix  ->  regenerate  ->  observe again
```

...repeated until the observed artifact matches the spec or a named iteration budget is spent. Three rules make it real:

1. **The generator is not the artifact.** A build log, a "0 errors" line, or the source diff is metadata *about* the artifact, not an observation *of* it. See [`references/observation-recipes.md`](../../skills/verifying-final-artifacts/references/observation-recipes.md) for how to make each artifact type observable.
2. **Observe before you judge the source.** Look at the output first and log concrete defects; only then trace each defect to the source line responsible. Jumping from a source read to a verdict is the failure.
3. **No pass without a fresh render this pass.** The re-render-and-re-look *is* the validation. A fix verified against the source diff, not the re-rendered artifact, is unverified.

If the real output cannot be observed in the current environment — no renderer, no viewer, no network — the honest result is **INCONCLUSIVE** naming the tooling gap, routed to whoever can run the toolchain. A source read is never a substitute for the observation.

## Where it sits

- **Stage:** PROVE **Observe** (Verify · Review). The [observer](../../agents/observer.md) gathers evidence; for produced artifacts that evidence is a direct observation of the regenerated output.
- **Skill:** [`verifying-final-artifacts`](../../skills/verifying-final-artifacts/SKILL.md) carries the loop, the stop condition, and the verdict (VERIFIED / NOT VERIFIED / INCONCLUSIVE).
- **Near neighbors:** [`reviewing-code-quality`](../../skills/reviewing-code-quality/SKILL.md) reviews source structure with no separate produced output; [`proving-claims`](../../skills/proving-claims/SKILL.md) maps claims to evidence, and a claim about a produced artifact routes here for its evidence.

## Boundary

This doctrine buys a visible, repeatable discipline of observing the delivered output. It does not manufacture formal verification and validation, compliance, certification, or any safety, security, or regulatory guarantee.
