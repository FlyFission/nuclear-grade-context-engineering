# Session Summary — Repo Review Enhancements (2026-05-30)

A holistic record of the work done in this session, for review/memory in another window.

## TL;DR

Three bodies of work, all driven through review and CI to clean merges:

1. **PR #7 (merged)** — Reproducible efficacy harness (`ng eval`), `ng status` health tags, and workflow visuals.
2. **PR #9 (merged, authored by owner)** — Doctrine spine controls; I drove the merge order and rebased #7 over it.
3. **PR #11 (in review)** — `closing-stale-packets` skill + `ng-close-packet` command + `ng status` `closed` terminal state.

Repo-wide gate after all work: **94 tests pass, ruff clean, `doctor` OK, `ng eval` 15/15.**

---

## PR #7 — Efficacy harness, status health, visuals (MERGED as `407ac14`)

### What shipped
- **`ng eval`** (`nuclear_grade/efficacy.py`): a stdlib-only, reproducible harness that reads each worked-example trial record, isolates the `## Nuclear-Grade Trial` section, and checks it still surfaces the decision signals the methodology claims. Exits non-zero if a worked example drops a required signal — a regression guard against silent drift.
  - Eval cases are plain JSON in `evals/cases/` (U02 agent boundary, U04 assurance wording, U07 payment idempotency).
  - **No new runtime dependency** (verified by clean-venv wheel install).
  - **Honesty boundary:** the simple-prompt-vs-Nuclear-grade score table is deliberately NOT mechanized — those author-written meta-sections use the same vocabulary as the signals, so substring scoring would inflate the result. The harness measures *presence of named decision elements*, not correctness/safety/compliance.
- **`ng status` health tags**: each packet tagged `ok` / `scaffold` / `invalid`, with a "needs attention" reminder, so abandoned half-filled drafts are visible. Health derives from the existing `validate_packet`.
- **Docs/visuals**: 4 render-checked Mermaid diagrams (`docs/diagrams.md`), `docs/glossary.md`, `docs/02-operating-system/agent-threat-model.md`, skill-graph router fix.

### Review dispositioned (Codex + Copilot)
All threads fixed, replied, and resolved:
- **Signal matching was too weak.** Originally `any`-matching let a multi-part signal pass when only one part was present (e.g. U07 release gates: `rollback path` alone passed even if monitoring + risk owner were dropped). Fix: added conjunctive **`all`** matching alongside `any`, and converted the genuinely-complementary signals (U07 release gates; U02 allowed-AND-forbidden authority) to `all`. Audited all 15 signals under one rule: `all` when the signal name enumerates distinct required elements; `any` only for interchangeable phrasings.
- **`packet_health` brittleness.** It classified `scaffold` by substring-matching the validator's *message text*. Fix: import `PLACEHOLDER_MARKER` and check the packet files directly, so health tracks behavior not wording.
- **`handle_eval` crash on bad input.** Fix: catch `OSError`/`ValueError`/`KeyError`/`TypeError`, print one clear line, exit 1 (no traceback).
- **Teeth test stability.** Selected case by id (`U02`) instead of `[0]`.

### Key decision recorded
- **Dropped the "progressive disclosure" token refactor** after verifying the premise was wrong: the always-loaded cost is the skill *descriptions* (~1.6k tokens for all 20, already lean), not the bodies. Moving `Common Rationalizations`/`Red Flags` out would save ~450 tokens only on a skill that just triggered — exactly when those sections matter — while touching 6 contract sites. Negative trade.

---

## PR #9 — Doctrine spine controls (MERGED as `9f3146e`, owner-authored)

- Translated owner-supplied operating influences into existing charter/skills/commands/templates without adding quotes or attributions; charter → 1.1.0 with six new articles; Standard templates gained decision-question, grounding-status, two-speed, support-type, and cut-point fields.
- All 9 Codex/Copilot threads were already resolved by the owner.
- **My role:** chose merge order (#9 first), merged it, then **rebased #7 onto the new main** and resolved two conflicts as true semantic merges:
  - `QUICKSTART.md`: kept #9's two-speed line + my improved validator note.
  - `templates/standard/verification.md`: kept #9's `Support type` exit criterion AND my `planned` evidence status.

---

## PR #11 — closing-stale-packets (IN REVIEW, branch `claude/closing-stale-packets-skill`)

### What it is
The skill half of the packet-lifecycle work. #7 made `ng status` *detect* abandoned packets; this tells an agent what to *do* about them.

### What shipped
- **`skills/closing-stale-packets/SKILL.md`** — full agent-operable contract. Every stale packet must reach one honest terminal state:
  - **Completed** — filled, `validate` passes (`ok`).
  - **Closed** — deliberately abandoned with a recorded rationale (`closed`).
  - **Deleted** — never a real change (empty scaffold).
  - Forbidden state: half-done and silent. Two integrity guards: faking a pass by deleting the placeholder marker is a named red flag; deletion (irreversible) needs owner sign-off when the change can't be confirmed dead.
- **`commands/ng-close-packet.md`** — portable command card.
- Wired into all registration points: catalog (skills+commands), `SKILLS.md` table + router diagram (`LFO -. stale packet sweep .-> CSP`), `COMMANDS.md`, `skill-evaluation.md` (3 should-trigger + 2 should-not), `results-summary.md` coverage, both contract-test EXPECTED sets, CHANGELOG.

### Review dispositioned (Codex P2) — led to a code change
- **Finding:** the CLOSE path promised `ng status` would stop flagging a closed packet, but `packet_health()` had no concept of "closed" — so a closed-with-rationale packet kept showing as `scaffold`/`invalid` and kept incrementing the "needs attention" nag, pressuring agents toward delete or fake-validation (the two behaviors the skill forbids).
- **Fix (chosen convention: `NUCLEAR-GRADE-CLOSED` marker, mirroring `PLACEHOLDER_MARKER`):**
  - Added `CLOSURE_MARKER = "NUCLEAR-GRADE-CLOSED"` in `nuclear_grade/ng_validate.py`, next to `PLACEHOLDER_MARKER`.
  - `packet_health()` now returns a `closed` state (checked *before* scaffold, since an abandoned packet may still hold the placeholder marker).
  - `ng status` treats `ok` and `closed` as terminal; only `scaffold`/`invalid` count toward "needs attention".
  - Updated CLI reference, the skill (Process/Outputs/Verification), the command card, and CHANGELOG to describe the convention.
  - Added `test_status_marks_closed_packet_as_terminal`; verified live end-to-end.

---

## Conventions / facts worth remembering

- **Branch discipline:** session work was on `claude/repo-review-enhancements-xszED` (#7) and `claude/closing-stale-packets-skill` (#11).
- **The gate** (run before every push): `python -m pytest -q` · `python -m ruff check .` · `python tools/ng.py doctor .` · `python tools/ng.py eval .`.
- **Marker conventions:** `NUCLEAR-GRADE-PLACEHOLDER` (unfilled scaffold) and `NUCLEAR-GRADE-CLOSED:` (deliberately closed, with rationale) — both live in `nuclear_grade/ng_validate.py`.
- **`ng status` states:** `ok` / `closed` (terminal) vs `scaffold` / `invalid` (needs attention).
- **Efficacy signal rule:** JSON cases support `any` (interchangeable phrasings) and `all` (distinct complementary elements that must all appear).
- **Zero runtime dependencies** for the `nuclear_grade` package is a hard constraint (wheel-smoke installs into a clean venv).
- **Honesty posture:** nothing in this repo claims formal assurance/compliance/certification; new public claims (e.g. the efficacy harness) trigger Standard-mode treatment and carry explicit boundary notes.

## Outstanding / possible next steps
- Merge #11 once review is green (CI green at last check; one Codex P2 dispositioned with the `closed`-state code change).
- Optional future: more eval cases; a worked-example trial record formally exercising `closing-stale-packets` (currently mapped conceptually to U09/U10).
