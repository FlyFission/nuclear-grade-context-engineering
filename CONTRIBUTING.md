# Contributing

Thank you for considering a contribution to Nuclear-grade.

Nuclear-grade is an original, public-source-inspired software engineering methodology. Contributions should make evidence easier to produce, review, and maintain without creating fake compliance theater.

By participating, you agree to uphold the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Ground rules

- Do not claim this repo satisfies DOE, NRC, NASA, NIST, CISA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other external standard.
- Use only public, open, linkable sources for direct source lineage.
- Do not derive templates from paywalled, proprietary, or controlled standards/manuals.
- Prefer bounded evidence packets over large generic templates.
- Use explicit evidence statuses: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Keep AI-assisted work scoped and independently checked.

## Before opening a PR

Run:

```bash
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

Also scan new public docs for overclaiming. Prefer phrases like:

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

For non-trivial contributions, create or update a packet under:

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

Keep each file to the minimum useful version needed for review.

If the contribution changes controlled configuration such as prompts, models, tools, dependencies, public claims, templates, skills, commands, validators, or release artifacts, also add the activated CM record from `templates/cm/`.
