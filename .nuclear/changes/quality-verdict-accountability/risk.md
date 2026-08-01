# Quality / Verdict / Accountability — Risk

## Change identity

- Slug: quality-verdict-accountability
- PR / issue: Embed the quality/verdict/accountability triad, the five work archetypes, and the AI-code evidence base
- Owner: FlyFission
- Date: 2026-07-31
- Current lifecycle phase: Verify / Review / Decide
- Summary: Name the three-way split the repo already practises but never defined (quality = the system of checks that produces evidence; verdict = the accountable decision made from it; accountability = the ability to explain that verdict later), add an archetype lens that names the posture work is done in and the drift it produces, and register three new external sources that supply evidence for claims the repo previously asserted unbacked.

## Questioning-attitude summary

- Decision question: Does the repo now define all three terms it depends on, and does the archetype lens change a decision rather than decorate the docs?
- Assumptions that set the mode: `CORE.md`, `MAXIMS.md`, `docs/glossary.md`, and the source map are controlled items; introducing external statistics into public doctrine is a provenance-bearing public claim.
- Facts still needing validation: that both statistical sources are accurately represented, that the pass-rate caveat travels with every citation of the token numbers, and that the vendor affiliation is disclosed at each citation point.
- Stop or hold conditions: hold if the contract tests, token budget, or packet validators fail, if any external link is unreachable, or if any figure is stated as a promise rather than as the source's own claim on its own benchmark.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `docs/02-operating-system/quality-verdict-accountability.md` | doctrine (new) | Canonical home for the triad | repo |
| `docs/02-operating-system/archetype-lens.md` | doctrine (new) | Front-door posture lens with mode floors | repo |
| `docs/00-standards-foundation/source-map.md` | citation registry | Three new source rows + a vendor-affiliation note | repo |
| `CORE.md`, `MAXIMS.md`, `docs/glossary.md`, `docs/README.md` | public headline docs | Carry the triad vocabulary and the front-door lenses | repo |
| `skills/reviewing-code-quality/SKILL.md` | skill | Sweeper trigger, two rationalizations, the agent-cost argument | repo |
| `docs/01-field-guide/leadership-and-high-reliability.md`, `docs/02-operating-system/token-burn-control.md`, `context-window-discipline.md`, `actor-evidence-independence.md`, `validators.md`, `work-type-lens.md`, `agents/judge.md`, `docs/01-field-guide/source-to-concept-crosswalk.md` | doctrine | Placement of the evidence and cross-wiring | repo |
| `pyproject.toml` (optional `mcp` extra) | dependency constraint | Unrelated CI repair folded in with owner approval — see the scope note below | repo |
| `skills/questioning-attitude`, `skills/rating-change-risk`, `skills/briefing-an-agent` | skills (distributed by `ng install`) | Implement the archetype lens at the front door it claims; added after review, owner-approved | repo |
| `commands/ng-question.md`, `commands/ng-context-pack.md`, `tests/fixtures/command_prompts.json` | generated + fixture | Regenerated projections and the golden prompt snapshot, following the two edited `## Prompt` blocks | repo |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Changes the repo's headline vocabulary and adds externally sourced public claims; no production system |
| Reversibility | high | Docs, skills and packet revert with normal git history. The `pyproject.toml` constraint is the one edit a plain revert would mishandle — reverting it re-opens the `mcp-smoke` break; see the rollback table in `ship.md` |
| Detectability | medium | A mis-stated statistic or a dropped caveat shows only on careful read |
| Exposure | high | Public repo; adopters quote `MAXIMS.md` and `CORE.md` directly |
| Uncertainty | medium | Two of three new sources are vendor-authored and unreplicated |
| Dependency trust | low | One optional-extra constraint **tightened** (`mcp>=1.0` to `mcp>=1.0,<2`), which narrows the accepted set rather than admitting anything new. No base-install dependency exists or changes |
| AI authority | medium | Drafted by an AI agent acting on the repo; merge decision stays with a human |

## Scope note — the folded-in CI repair

CI on this branch failed `mcp-smoke` for a reason this change did not cause. The optional extra was declared `mcp>=1.0` with no upper bound; `mcp` 2.0.0 removed `mcp.server.fastmcp`, which `nuclear_grade/mcp_server.py` imports. Verified in a clean environment: `mcp>=1.0` resolves to 2.0.0 and the import fails; `mcp>=1.0,<2` resolves to 1.29.0 and the job's 13 tests pass. `main` last went green on 2026-07-25, before 2.0.0 was picked up, and would fail identically if re-run today.

Mixing an unrelated repair into a doctrine change is normally the wrong shape. It is done here because the owner was asked and chose it over a separate PR: the break is repo-wide, the fix is one constraint, and leaving it would keep both this branch and `main` red. The 2.x port is **not** attempted here and is not a hidden part of this change.

## Selected mode

- **Mode:** Standard
- Why this mode: the change edits public headline docs and introduces external statistical claims a future maintainer or adopter could rely on. The activation screen's "will someone rely on the claim?" question answers yes.
- Why lighter mode is not enough: the near-identical `context-window-discipline` packet ran Quick, but that change added no headline-doc claims and no vendor-affiliated statistics. A Quick record would not preserve the claim-to-source trace this change specifically needs, and the change is itself about accountability.
- Why heavier mode is not yet required: no production system, credential, permission, safety, or regulatory control changes, and no new gate. The one dependency edit tightens an existing optional constraint rather than adding a supplier or widening trust — recorded in the affected items above and in `verification.md`'s dependency table.

## Immediate proof obligations

- Minimum evidence before build: every external figure independently re-verified against its public source, including authorship and affiliation.
- Minimum evidence before merge/release: pytest, ruff, `ng doctor`, `ng tokens`, and packet validation pass; the pass-rate caveat and the vendor disclosure are present at every citation point.
- Independent review needed? yes — the authoring agent selected and summarized the external evidence and then wrote the doctrine it supports. That is the actor–evidence coupling this repo asks others to disclose; a human reviewer owns the acceptance call.

## Required links

- Packet: `.nuclear/changes/quality-verdict-accountability/`
- Basis: `basis.md`
- Verification: `verification.md`
- Doctrine: `../../../docs/02-operating-system/quality-verdict-accountability.md`, `../../../docs/02-operating-system/archetype-lens.md`

## Exit criteria

- The mode is justified.
- The affected controlled items are explicit.
- The proof obligations and the independent-review need are visible.

## Source-lineage note

Original Nuclear-grade packet inspired by public ideas on graded rigor, independent verification, configuration management, and software assurance mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
