# Actor-Evidence Independence — Risk

## Change identity

- Slug: actor-evidence-independence
- PR / issue: feedback follow-up on the control loop's persuasive-documentation gap
- Owner: FlyFission
- Date: 2026-06-24
- Current lifecycle phase: Verify / Review / Decide
- Summary: Name the actor-evidence-independence gap and wire the defense into the loop, the skills, the templates, the validator spec, and the threat model.

## Questioning-attitude summary

- Decision question: Does the framework now defend against the failure it already names — a confident hallucination clearing gates whose inputs the actor authored — rather than only describing it?
- Assumptions that set the mode: The control loop and its public framing are controlled items; a change to the method's core claim carries adoption and trust consequence.
- Facts still needing validation: That an independent reviewer agrees the doctrine closes the gap and stays internally consistent across the surfaces it touches.
- Stop or hold conditions: Hold if the change breaks the contract tests, the token budget, or the packet validators, or if it implies formal assurance.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `docs/02-operating-system/actor-evidence-independence.md` | doctrine | New home for the principle | repo |
| `docs/04-adoption/agent-authority-model.md` | doctrine | Adds the self-authorship boundary, dual of self-modification | repo |
| `WORKFLOWS.md`, `lifecycle.md`, `README.md`, `CORE.md` | loop docs | Name the seam at Verify/Review/Decide | repo |
| `proving-claims`, `checking-release-readiness` | skills | Carry the independence-of-evidence discipline | repo |
| `verification.md`, `ship.md`, `quick/proof.md` | templates | Operational independence fields | repo |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Changes the method's core claim and public framing; no production system |
| Reversibility | high | Documentation and templates revert with normal git history |
| Detectability | medium | Inconsistency across surfaces shows only on careful read or contract tests |
| Exposure | high | Public repo; adopters copy the loop and templates |
| Uncertainty | medium | Whether the framing fully closes the gap is a judgment call |
| Dependency trust | low | No runtime dependency changes |
| AI authority | medium | Authored by an AI agent acting on the repo |

## Selected mode

- **Mode:** Standard
- Why this mode: The change touches the loop docs, the public README, Core skills, and templates — controlled items with adoption consequence.
- Why lighter mode is not enough: A Quick record would not preserve the claim-to-evidence trace or the honest independence posture this very change is about.
- Why heavier mode is not yet required: No production system, dependency, credential, safety, or regulatory control changes.

## Immediate proof obligations

- Minimum evidence before build: The feedback's gap is reproduced against the current loop docs and confirmed real.
- Minimum evidence before merge/release: Pytest, ruff, `ng doctor`, `ng tokens`, and the packet validators pass; the concept is reachable at each trust-bearing gate.
- Independent review needed? yes — the authoring agent cannot self-certify that the doctrine is correct and sufficient; a human reviewer owns that call. This is the packet's own subject applied to itself.

## Required links

- Packet: `.nuclear/changes/actor-evidence-independence/`
- Basis: `basis.md`
- Verification: `verification.md`
- Doctrine: `../../../docs/02-operating-system/actor-evidence-independence.md`

## Exit criteria

- The mode is justified.
- The affected controlled items are explicit.
- The proof obligations and the independent-review need are visible.

## Source-lineage note

Original Nuclear-grade packet inspired by public ideas on independent verification, segregation of duties, configuration management, software assurance, and AI risk mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
