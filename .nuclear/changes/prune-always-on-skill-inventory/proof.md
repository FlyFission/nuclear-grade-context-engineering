# Quick Proof Record

**Purpose:** Capture the smallest believable evidence record for a Quick change.

**Activation threshold:** Use with `risk.md` when a change is low-stakes, easy to undo, easy to check, and does not trip Standard mode.

**Minimum useful version:** one proof command, check, or eval; the result; an evidence link; and a reviewer note.

**Overhead trap:** Do not paste long logs. Link to the evidence and quote only the result that matters.

---

## Proof summary

- Change slug: prune-always-on-skill-inventory
- Proof owner: FlyFission
- Date/time: 2026-07-20
- Risk record: `risk.md`

## Claim proven

> Removing the `## Recommended skills` inventory from `AGENTS.md` removes no skill access: every skill remains reachable through `CORE.md` routing and the `SKILLS.md` catalog, and the public-doc/agent guards still pass.

Claim: The inventory removal is a safe, capability-preserving documentation edit.

## Method

- Command/check/eval/review: `python -m pytest tests/test_public_docs.py tests/test_agents.py -q`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `git diff --check`; confirm `CORE.md` and `SKILLS.md` exist.
- Environment: Python 3.11, repo checkout.
- Inputs/fixtures: current `AGENTS.md`, `CORE.md`, `SKILLS.md`.
- Expected result: all commands pass; `CORE.md` and `SKILLS.md` present; `AGENTS.md` retains `## Skill loading rule` and drops only `## Recommended skills`.
- Self-check used? yes; target: the `## Recommended skills` section of `AGENTS.md`.
- Reproducible by the reviewer (command/artifact), not just the author's narration? yes; the reviewer can rerun the commands above and `grep -n "Recommended skills" AGENTS.md` (expected: no match).

## Result

- Status: pass
- Actual result: `pytest tests/test_public_docs.py tests/test_agents.py` green; `ng doctor` OK; `ng tokens` OK (token budget, and lower than before by the removed lines); `git diff --check` clean; `CORE.md` and `SKILLS.md` present.
- Evidence link or artifact path: PR #71 CI run; local run recorded in this record.
- If failed/gap: n/a.

## Reviewer note

- Reviewer: maintainer (independent decider on merge)
- Review note: Change is docs-only and reversible; skill access preserved via existing routing. AI-assisted; independent maintainer review is the merge gate.
- Is Quick mode still valid after proof? yes.

## Required links

- Related PR/issue: #71
- Relevant changed files: `AGENTS.md`
- CI run / test output / eval report / screenshot / log: PR #71 checks (validate 3.11/3.12, wheel-smoke, mcp-smoke).
- If AI-assisted: link to AI scope or independent check note: AI authored the edit and this record; the maintainer's merge review is the independent check.

## Exit criteria

- The evidence matches the claim in `risk.md` directly.
- The actual result is compared to the expected result you named before the proof.
- The result status is stated plainly.
- Any failure or gap has a next action or an escalation.
- The reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on software test documentation, verification, work records, and keeping the approved version under control, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
