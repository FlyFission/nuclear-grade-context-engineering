# Basis

## Change context

- Slug: review-findings-2026-05
- Scope: Address the twelve findings from the 2026-05 adversarial review.
- Outcome to protect: Repo claims (rigor, questioning attitude, controlled change) remain credible after upgrade to 0.2.0.

## Need and scope

The 2026-05 adversarial review surfaced twelve actionable findings against `nuclear-grade-context-engineering`. Six are critical-to-high (F1, F2, F3, F4, F8, F9). The repo's positioning depends on rigor and a questioning attitude; the front-door demo failing red without framing, the installed wheel being functionally broken, and the prohibited-claims detector being trivially evaded all undermine the thesis the repo sells. This packet records the coordinated fix.

## Protected and unacceptable outcomes

| Concern | Protected outcome | Unacceptable outcome |
|---|---|---|
| Front-door credibility | A new reader runs the 60-second demo and reads framing that explains why `FAILED` is expected. | A reader assumes the project is broken and bounces. |
| Installed wheel | `pip install` followed by `nuclear-grade new` works in a clean environment. | The wheel is functionally inert outside the repo. |
| Overclaiming detector | Paraphrased compliance claims (see code-block corpus below) fail validation. | Paraphrases evade the rule and ship in downstream packets. |
| Mode discipline | Every packet declares Quick or Standard explicitly. | Mode is inferred silently from file presence, masking authorial intent. |

## Derived requirements or claims

| ID | Requirement / claim | Evidence planned |
|---|---|---|
| C-001 | The README and QUICKSTART frame the 60-second demo so the expected `FAILED` is read as intended, not as breakage. | Diff of `README.md` and `QUICKSTART.md`; manual readthrough. |
| C-002 | A wheel built from this repo, installed into a clean venv, can run `nuclear-grade init`, `new --mode quick`, `new --mode standard`, `new --mode cm`, `new --mode golden-path`, `list`, and `validate` end to end. | New `wheel-smoke` CI job; `tests/test_packaging.py` archive-content assertion. |
| C-003 | The validator rejects paraphrased compliance claims (see code block below) while still allowing legitimate "inspired by" / "does not claim" prose. | New paraphrase-battery tests in `tests/test_ng_validate.py`. |
| C-004 | The validator requires every packet's `risk.md` to declare `- **Mode:** Quick` or `- **Mode:** Standard` under a `## Selected mode` heading. A `nuclear-grade migrate` helper inserts that line for legacy packets. | New `tests/test_ng_validate.py` missing-mode case; new `tests/test_ng_cli.py` migrate case. |
| C-005 | `nuclear-grade new` supports `--mode cm` and `--mode golden-path`, scaffolding all five files for each mode. | New `tests/test_ng_cli.py` scaffolding tests. |
| C-006 | CI runs on Python 3.11 and 3.12 and includes a `ruff` lint step. | Diff of `.github/workflows/ci.yml`; CI green on both legs. |
| C-007 | The unfilled-prompt detector matches labels longer than 80 characters. | New `tests/test_ng_validate.py` long-label case. |
| C-008 | The README and `results-summary.md` describe the worked-example evidence as "tested" and the comparison as "author-judged," not as "validated" without qualification. | Diff of `README.md:19`, `README.md:151`, and `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` banner. |
| C-009 | `CHANGELOG.md` has one Unreleased section above a stamped `[0.2.0] - 2026-05-27` entry with Breaking / Added / Fixed / Changed subsections. | Diff of `CHANGELOG.md`. |
| C-010 | The repo carries a `CITATION.cff` (CFF 1.2) and a `.github/CODEOWNERS` (placeholder for maintainer handle). | Files exist; doctor passes. |
| C-011 | `docs/04-adoption/report-swot-gap-remediation.md` marks the proposed-but-not-present files as such so a reader cannot mistake them for current refs. | Diff of the file. |
| C-012 | `pyproject.toml` uses the `hatchling` build backend with `force-include` mapping top-level `templates/`, `skills/`, and `commands/` into `nuclear_grade/_bundled/` at wheel-build time. Version is `0.2.0`. | Diff of `pyproject.toml`; built wheel archive contains the expected paths. |

## Paraphrase test corpus (examples that must fail validation)

```
meets NQA-1 requirements
fully ASME qualified
conforms to IEEE 829
satisfies 10 CFR 50 Appendix B
implements quality assurance per NQA-1
audited to NRC standards
regulator-approved
```

Allowed-by-boundary corpus:

```
inspired by NQA-1 concepts
influenced by ASME structure, not aligned with it
we do not claim IEEE conformance
this repo is not NRC compliant
no formal V&V is implied
```

## Assumptions, constraints, and invalidation triggers

- Assumption: `hatchling` `force-include` produces files reachable from a `pip install`-ed package via `importlib.resources` or direct `__file__`-relative path. Invalidation trigger: wheel-smoke job cannot find `_bundled/templates/quick/risk.md`.
- Assumption: All seven existing repo packets already declare `## Selected mode` (confirmed during pre-flight). Invalidation trigger: a packet without it is found mid-build.
- Constraint: No em dashes or en dashes in any new written content (style preference).
- Constraint: 0.2.0 version bump because the validator's new Mode requirement breaks downstream packets that did not previously declare a mode.

## Acceptance scenarios

- A maintainer runs `pip install dist/nuclear_grade-0.2.0-py3-none-any.whl` in a fresh venv outside the source tree, then `nuclear-grade init .` followed by `nuclear-grade new demo --mode cm`. Five CM files appear in `.nuclear/changes/demo/`.
- A downstream user upgrading from 0.1.0 runs `nuclear-grade migrate .nuclear/changes/old-packet`. The packet's `risk.md` gains a `## Selected mode` section. Subsequent `validate` passes that rule.
- A reviewer pastes one of the corpus phrases above into a packet basis. `validate` reports a prohibited compliance claim with the offending phrase named in the message.

## Required links

- Packet: `.nuclear/changes/review-findings-2026-05/`
- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- Twelve claims C-001 through C-012 are mapped to plan steps in `plan.md`.
- Each claim has an evidence row in `verification.md`.
- `trace.md` is populated end to end.
- Ship decision is recorded in `ship.md`.

## Source-lineage note

Original Nuclear-grade packet inspired by the public graded-rigor, configuration-management, and software-assurance concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
