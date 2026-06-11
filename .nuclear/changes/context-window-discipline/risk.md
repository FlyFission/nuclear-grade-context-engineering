# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** Additive documentation only — one new operating-system page, one new
  source-map tier, three one-line cross-links, and seven glossary rows. No code, validator
  logic, dependencies, permissions, or public assurance claims change. The page indexes and
  grounds controls that already exist (context packs, token-burn control, lessons learned);
  it adds no gate.

**Purpose:** Decide whether extracting the verified content of an external
"context engineering blueprint" research report into repo doctrine can safely stay in Quick
mode, and name the proof required.

---

## Change

- Slug: context-window-discipline
- PR / issue: Extract verified context-engineering mechanics from external research report
- Owner: FlyFission
- Date: 2026-06-10
- Summary: Add `docs/02-operating-system/context-window-discipline.md`, the mechanics behind
  the existing context-pack and token-burn doctrine: why small ordered context outperforms
  big context (attention budget, context rot, lost-in-the-middle), the named context failure
  modes (poisoning, distraction, confusion, clash, rot, collapse, brevity bias) each mapped
  to an existing Nuclear-grade control, placement/ordering rules, compression caveats,
  structure-aware code retrieval, and multi-agent state hygiene. Add a Tier 9
  (Context-Engineering Mechanics Sources) section to `source-map.md` with ten verified
  public sources. Add one index row to `docs/README.md`, one grounding link each to
  `context-packs.md` and `token-burn-control.md`, and seven plain-language glossary rows.
- Provenance discipline: the triggering report cited only two distinct public pages and
  carried several unverifiable numbers. Every source in the new Tier 9 was independently
  re-verified against its public URL before citation. Deliberately **not** adopted from the
  report: per-tool "context waste" percentages (no traceable public source), the
  "Forward-Deployed Context Engineer" framing (marketing, not engineering), garbled formula
  fragments, and vendor-specific middleware patterns.

## Scope

- Affected files/configs/docs: `docs/02-operating-system/context-window-discipline.md` (new),
  `docs/00-standards-foundation/source-map.md` (one additive tier),
  `docs/README.md` (one index row), `docs/02-operating-system/context-packs.md` (one
  sentence), `docs/02-operating-system/token-burn-control.md` (one sentence),
  `docs/glossary.md` (seven additive rows).
- User-visible behavior changed? no (documentation only).
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A citation or benchmark caveat reads poorly or a link rots; reversible by edit. No runtime, evidence-gate, or trust-boundary effect. |
| Reversibility | Fully reversible; all edits are additive. |
| Detectability | High; the test suite, `doctor`, `tokens`, and packet validation run green, and link resolution for the new page is recorded in `proof.md`. |
| Exposure | Public docs, but additive, hedged ("their benchmarks, not promises"), and within the existing boundary wording. |
| Uncertainty | Low; every cited source was re-verified public before inclusion; doctrine maps onto existing controls rather than inventing new ones. |
| Why Quick is enough | No new trust boundary, dependency, permission, gate, or release effect. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`; `python tools/ng.py doctor .`;
  `python tools/ng.py tokens .`;
  `python tools/ng.py validate .nuclear/changes/context-window-discipline`;
  explicit resolution check of every internal link in the new page.
- Expected result: full suite green; doctor OK; token budget OK; this packet validates;
  every internal link resolves.
- Evidence link/location: `proof.md`.

## Critical-action self-check

- Exact target: the new page, the new source-map tier, and the five small additive edits.
- Expected result: no existing heading asserted by `tests/test_public_docs.py` is disturbed;
  every new internal link resolves; every external source row carries a real, re-verified
  public URL; no benchmark number is stated as a promise.
- Stop condition: if any edit would remove an asserted heading, introduce a broken link, an
  unverified citation, or a compliance claim, stop and revert.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected — no;
- a trust decision about a dependency, model, or API changed — no;
- a failure could be silent, delayed, costly, or hard to undo — no;
- the AI had the power to write, run commands, use the network, or approve actions, beyond
  just drafting under review — no (the agent drafted documentation, ran read-only
  verification commands, and used web search only to verify public citations; it changed no
  product code, held no credentials, and the merge decision stays with a human via PR
  review, matching the accepted `runtime-enforcement-doctrine` Quick packet, also an
  AI-prepared docs change);
- the proof will not fit in one small `proof.md` — false.

None apply. Quick stands. (If a follow-up adds validator code or a new gate, re-classify to
Standard.)

## Required links

- Packet: `.nuclear/changes/context-window-discipline/`
- Related PR/issue: Extract verified context-engineering mechanics from external research report
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md` (Tier 9)

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public graded-rigor and software-assurance concepts
mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
