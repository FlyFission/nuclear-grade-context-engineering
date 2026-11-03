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
