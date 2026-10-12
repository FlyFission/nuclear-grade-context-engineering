# Quick Proof Record

**Purpose:** Capture the smallest believable evidence record for a Quick change.

**Activation threshold:** Use with `risk.md` when a change is low-stakes, easy to undo, easy to check, and does not trip Standard mode.

**Minimum useful version:** one proof command, check, or eval; the result; an evidence link; and a reviewer note.

**Overhead trap:** Do not paste long logs. Link to the evidence and quote only the result that matters.

---

## Proof summary

- Change slug: threat-map-and-decision-metadata
- Proof owner: FlyFission
- Date/time: 2026-10-12
- Risk record: [`risk.md`](risk.md)

## Claim proven

> The optional decision-metadata block does not change what `ng validate` reports. The OWASP map and the release-review page state only what was checked, and they mark gaps.

Claim: Adding the front matter leaves validator output the same for fresh scaffolds and for valid packets. The new pages make no claim to coverage, compliance, or verification.

## Method

- Command/check/eval/review: `python -m pytest -q`; `python -m ruff check .`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `python tools/ng.py validate .nuclear/changes/threat-map-and-decision-metadata`; `git diff --check`. Run `ng new demo --mode standard` and `ng new demoq --mode quick` in two temp repos, one with the new templates and one with the `HEAD` templates, then diff the `ng validate` messages. Check sources with WebSearch, WebFetch, and curl.
- Environment: Python 3, worktree checkout, network through the agent proxy.
- Inputs/fixtures: the two `risk.md` templates; the new test `test_template_decision_metadata_is_tolerated_by_validator`; the MADR template and CHANGELOG from the GitHub raw files.
- Expected result: everything passes; the scaffold message lists are identical; this packet validates with front matter present.
- Self-check used? yes. Target: the template front matter and each "Does NOT cover" cell in the threat map.
- Reproducible by the reviewer (command/artifact), not just the author's narration? yes; rerun the commands.

## Result

- Status: pass
- Actual result: pytest passed 329 tests, 0 failures. ruff reported `All checks passed!`. doctor, the token budget, and validation of this packet (with and without `--strict-custody`) all returned OK. `git diff --check` was clean. Scaffold diff: standard gave 28 messages before and after with no difference; quick gave 4 and 4 with no difference. Those messages are the expected placeholder failures and were already there.
- Evidence link or artifact path: `tests/test_ng_validate.py::test_template_decision_metadata_is_tolerated_by_validator`.
- If failed/gap: gap. The official OWASP page (genai.owasp.org) and adr.github.io were blocked by the proxy. OWASP names come from secondary sources, and the source-map row stays `public-url-needed`; the next step is for the maintainer to verify it from a networked browser. MADR was checked through its GitHub repository files instead.

## Reviewer note

- Reviewer: maintainer (merge gate)
- Review note: An AI wrote the edits and this record, so the maintainer's review is the independent check. Things to check: the threat-map wording, the MADR field rename (`deciders` became `decision-makers` in MADR 4), and the personal-data open item on the release-review page.
- Is Quick mode still valid after proof? yes, subject to the agent-authority note in `risk.md`.

## Required links

- Related PR/issue: follow-ups F-06, F-08, F-09 in `../adr-governance-benchmark/basis.md`
- Relevant changed files: see `risk.md` Scope.
- CI run / test output / eval report / screenshot / log: local runs only; CI is pending a PR.
- If AI-assisted: link to AI scope or independent check note: AI-authored; maintainer merge review is the independent check.

## Exit criteria

- The evidence matches the claim in `risk.md` directly.
- The actual result is compared to the expected result you named before the proof.
- The result status is stated plainly.
- Any failure or gap has a next action or an escalation.
- The reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade record; sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
