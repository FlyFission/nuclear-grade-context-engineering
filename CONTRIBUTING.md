# Contributing

Thank you for thinking about helping with Nuclear-grade.

Nuclear-grade is an original way to do software engineering, drawn from public sources. Your changes should make evidence easier to produce, review, and keep current, without faking compliance.

By taking part, you agree to follow the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Ground rules

- Do not claim this repo meets DOE, NRC, NASA, NIST, CISA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other outside standard.
- For direct source lineage, use only public, open sources you can link to.
- Do not build templates from paywalled, proprietary, or controlled standards or manuals.
- Prefer small, focused evidence packets over large generic templates.
- Use clear evidence statuses: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Keep AI-assisted work tightly scoped and checked by someone else.

## Before opening a PR

Run:

```bash
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

Also scan new public docs for overclaiming. Lean on phrases like:

- public-source-inspired;
- evidence-oriented;
- original software workflow;
- non-compliance-claiming.

Avoid phrases like:

- compliant;
- certified;
- approved;
- formal QA program;
- regulatory submittal;
- production sandbox, unless separately proven and scoped.

## Change packets

For anything more than a trivial change, create or update a packet under:

```text
.nuclear/changes/<slug>/
```

For Standard changes, use:

```text
risk.md
basis.md
plan.md
trace.md
verification.md
ship.md
```

Keep each file to the smallest useful version a reviewer needs.

If your change touches something that must stay under control, such as prompts, models, tools, dependencies, public claims, templates, skills, commands, checkers, or release artifacts, also add the CM record (keeping the approved version under control) from `templates/cm/`.
