# ng-code-review

## Purpose

Review a diff or module for standards drift (oversized files, needless abstraction, leaked feature logic, clever indirection) and issue one honest verdict. This is a portable command prompt.

## Use when

- A diff or module is up for review and you want a standards check, not just a correctness check.
- A file or function has grown large, or an abstraction layer is being added.
- A refactor is proposed and you need to judge whether it removes complexity or just moves it.
- An agent produced code quickly and the question is whether it stays maintainable.

## Do not use when

- The change is a trivial, obvious edit with no structural impact.
- The task is only about functional correctness (use ng-prove instead).
- A hotfix must ship for incident containment before a quality pass is reasonable.

## Inputs

- The diff or module under review and its surrounding files.
- The change's mission anchor or objective.
- Project conventions and any agreed countable limits.
- The layering map: what is shared/canonical versus feature-specific.

## Prompt text

```text
Run a Nuclear-grade code-quality review on this change.

Inputs:
- diff or module:
- objective / mission anchor:
- agreed limits or conventions:
- shared vs feature-specific layers:

Do this:
- Read the change against its objective; flag scope drift first.
- Look for deletion before rearrangement; ask what can be removed entirely.
- Apply countable tripwires as prompts, not laws (file ~1000 lines, function ~50 lines, deep nesting, duplicated branches).
- Test each abstraction: it must remove more complexity than it adds; flag thin pass-throughs.
- Check layering: flag feature logic leaking into shared/canonical/framework code.
- Prefer boring direct code over clever indirection.

Return:
- a prioritized findings list (location, standard at risk, concrete fix, often a deletion)
- one verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE
- a short rationale tying the verdict to the findings

Do not soften every finding into "looks good." Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Files created or modified

- Review notes in the PR, or a section in `verification.md` when the review is packet evidence.

## Expected outputs

- A prioritized findings list with concrete fixes.
- A single verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE.
- A rationale that matches the verdict.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Rearranging complexity instead of asking what deletes the need for it.
- Treating countable tripwires as hard laws rather than investigation prompts.
- Passing speculative abstraction because it "might be useful later."
- Ending with no verdict, or a verdict that does not match the findings.

## Legal/assurance boundary note

This command supports maintainability review and evidence visibility. It does not create formal V&V, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
