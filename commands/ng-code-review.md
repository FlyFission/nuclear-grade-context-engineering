# ng-code-review

## Purpose

Review a diff or a module for slipping standards — oversized files, needless layers of abstraction, feature logic leaking where it should not, and clever indirection — and give one honest verdict. This is a portable command prompt.

## Use when

- A diff or a module is up for review and you want a standards check, not just a correctness check.
- A file or function has grown large, or someone is adding a new layer of abstraction.
- A refactor is proposed and you must judge whether it removes complexity or just moves it.
- An agent wrote code fast and the question is whether it stays maintainable.

## Do not use when

- The change is a trivial, obvious edit with no effect on structure.
- The task is only about whether the code works (use ng-prove instead).
- A hotfix must ship to contain an incident before a quality pass makes sense.

## Inputs

- The diff or module under review, and the files around it.
- The change's stated goal (its mission anchor).
- The project's conventions, and any countable limits you agreed on.
- The layering map: what is shared and canonical versus what is feature-specific.

## Prompt text

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

## Files created or modified

- Review notes in the PR, or a section in `verification.md` when the review is packet evidence.

## Expected outputs

- A ranked list of findings, each with a concrete fix.
- A single verdict: VERIFIED, NOT VERIFIED, or INCONCLUSIVE.
- A reason that matches the verdict.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Rearranging complexity instead of asking what removes the need for it.
- Treating the countable tripwires as hard laws rather than prompts to investigate.
- Passing a speculative abstraction because it "might be useful later."
- Ending with no verdict, or a verdict that does not match the findings.

## Legal/assurance boundary note

This command supports a maintainability review and makes the evidence visible. It does not create formal V&V, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
