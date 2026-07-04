# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** Additive documentation only — three new pages, one new source-map tier,
  cross-links, a skill-routing convention with four worked pointers, and one reframed table in
  the comparison study. No code, validator logic, dependencies, permissions, gates, or public
  assurance claims change. The command cards that changed are a mechanical projection of the
  edited skills (`ng gen-commands`), not authored logic. This mirrors the accepted
  `context-window-discipline` Quick packet, an additive docs + source-map-tier change of the
  same shape.

**Purpose:** Decide whether extracting the useful, mission-fit value from five public
context-engineering repositories into repo doctrine can safely stay in Quick mode, and name the
proof required.

---

## Change

- Slug: context-engineering-external-review
- PR / issue: Extract useful value from five external context-engineering repositories
- Owner: FlyFission
- Date: 2026-07-03
- Summary: Add three docs — `docs/02-operating-system/evaluation-integrity.md` (LLM-judge bias
  taxonomy, process-reward grading, panel/meta-judge escalation),
  `docs/05-reference/reasoning-techniques.md` (zero/few-shot, CoT, self-consistency, ReAct, PAL,
  reflexion mapped to PROVE with evidence caveats), and
  `docs/01-field-guide/context-engineering-landscape.md` (formal field framing, adjacent-territory
  map as landscape-only, and an explicit rejection of speculative "field-physics" framing). Add a
  Tier 11 (Practitioner Context-Engineering Collections) to `source-map.md` crediting the five
  reviewed repos as secondary/aggregator sources. Add a surface-classification section
  (locked/editable/append-only/human-controlled) to `agent-authority-model.md`; a judge-bias guard
  block to `agents/judge.md`; a PAL rationalization line to `proving-claims`; a routing
  (anti-overlap) convention to the skill-authoring contract with four reciprocal pointers across
  `briefing-an-agent`↔`handing-off-work` and `rating-change-risk`↔`creating-change-records`; a
  rigor-tier-vs-payoff table to the comparison study's `results-summary.md`; two index rows and
  cross-links in `docs/README.md` and `actor-evidence-independence.md`. Regenerate the four
  affected command cards from their skills.
- Provenance discipline: the five repos are **secondary/aggregator** sources. No template or
  wording is derived from them; every adopted idea is mapped onto existing Nuclear-grade controls.
  Deliberately **not** adopted: jasontang-ai's neural-field / attractor / quantum-semantics framing
  (declined on the record as unfalsifiable and off-mission), any framework-specific dependency
  (Mem0/Zep/Letta/LangGraph stay landscape-only), and other projects' benchmark numbers (cited as
  illustrative external evidence, never restated as Nuclear-grade results).

## Scope

- Affected files/configs/docs: three new docs (above); `docs/00-standards-foundation/source-map.md`
  (one additive tier); `docs/04-adoption/agent-authority-model.md` (one section);
  `docs/02-operating-system/actor-evidence-independence.md` (cross-links);
  `agents/judge.md` (one body block); `skills/proving-claims/SKILL.md` (one line);
  `docs/05-reference/skill-authoring-contract.md` (one section);
  `skills/{briefing-an-agent,handing-off-work,rating-change-risk,creating-change-records}/SKILL.md`
  (one routing line each); `docs/03-worked-examples/skill-workflow-comparison/results-summary.md`
  (one additive section); `docs/README.md` (two index rows); `commands/{ng-classify,ng-context-pack,ng-new,ng-turnover}.md`
  (regenerated projection).
- User-visible behavior changed? no (documentation only).
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A citation or cross-link reads poorly or rots; reversible by edit. No runtime, evidence-gate, or trust-boundary effect. |
| Reversibility | Fully reversible; all edits are additive or mechanical regeneration. |
| Detectability | High; `pytest`, `ruff`, `doctor`, `tokens`, command parity, and packet validation run green (see `proof.md`). |
| Exposure | Public docs, but additive, hedged, secondary-source-framed, and within existing boundary wording. |
| Uncertainty | Low; each adopted idea maps onto an existing control; the declined material is named, not silently dropped. |
| Why Quick is enough | No new trust boundary, dependency, permission, gate, or release effect. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`; `python -m ruff check .`;
  `python tools/ng.py doctor .`; `python tools/ng.py tokens .`;
  `python tools/ng.py validate .nuclear/changes/context-engineering-external-review`;
  explicit resolution check of every internal link in the three new pages.
- Expected result: full suite green; ruff clean; doctor OK; token budget OK; this packet
  validates; every internal link resolves.
- Evidence link/location: `proof.md`.

## Critical-action self-check

- Exact target: the three new pages, the new source-map tier, the surface-classification section,
  and the small additive edits and regenerated cards.
- Expected result: no heading asserted by `tests/test_public_docs.py` is disturbed; command parity
  holds (`test_command_parity.py`); every new internal link resolves; every source row carries a
  real public URL; no benchmark number is stated as a Nuclear-grade result; no compliance claim.
- Stop condition: if any edit would remove an asserted heading, break a link, an unverified
  citation, or introduce a compliance/field-physics claim, stop and revert.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected — no;
- a trust decision about a dependency, model, or API changed — no;
- a failure could be silent, delayed, costly, or hard to undo — no;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just
  drafting under review — no (the agent drafted documentation, ran read-only verification and the
  deterministic `gen-commands` projection, and used web review only to read the five public repos;
  it changed no product code, held no credentials, and the merge decision stays with a human via
  PR review, matching the accepted `context-window-discipline` Quick packet);
- the proof will not fit in one small `proof.md` — false.

None apply. Quick stands. (If a follow-up adds validator code or a new gate, re-classify to Standard.)

## Required links

- Packet: `.nuclear/changes/context-engineering-external-review/`
- Related PR/issue: Extract useful value from five external context-engineering repositories
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md` (Tier 11)

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public graded-rigor and software-assurance concepts
mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
