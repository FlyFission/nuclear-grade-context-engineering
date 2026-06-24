# Actor-Evidence Independence — Verification

## Purpose

Show the evidence behind the amendment's claims, and disclose who authored that evidence relative to the actor.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim | Verification method | Result | Status |
|---|---|---|---|
| REQ-001 | Read the doctrine page and the Self-authorship boundary section | Present, consistent, framed as the dual | pass |
| REQ-002 | `rg -n "actor-evidence-independence" README.md WORKFLOWS.md CORE.md docs skills templates` | The concept is reachable from every trust-bearing gate | pass |
| REQ-003 | Read the `## Evidence independence` template section and the deferred-check note | Fields present; check kept as a disclosure, not a verdict | pass |
| REQ-004 | `python -m pytest`; `ruff check .`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .` | 190 passed, 1 skipped; lint clean; doctor OK; budget OK | pass |

## Evidence independence

Who authored the evidence for each load-bearing claim, relative to the actor (the AI agent that made this change)? This packet is itself the subject of its change, so it discloses its own independence posture honestly. See `../../../docs/02-operating-system/actor-evidence-independence.md`.

| Load-bearing claim | Who authored the evidence | Reproducible by an independent party? | Independence rung | Gap / residual risk if below the stakes |
|---|---|---|---|---|
| REQ-002 (the seam is wired in) | The actor, but as a reproducible grep | Yes — the reviewer reruns the grep and reads the result | 3 | None; the check is mechanical |
| REQ-004 (nothing breaks) | The pre-existing test suite and validators, re-run out-of-band by CI | Yes — the reviewer and CI re-run them; the actor did not author these checks for this change | 4 | None; CI re-runs where the actor cannot tamper |
| REQ-001/003 (the doctrine is correct and sufficient) | The actor — this is a judgment, not a mechanical check | No — correctness of the framing cannot be self-certified | 1 | Open: a human reviewer owns this call. Carried to `ship.md` |

- Decider independent of the actor for the ship decision? no — pending human review; the actor does not self-certify the merge.
- Evidence authored only by the actor is labeled a self-check and carried as residual risk in `ship.md`? yes — the REQ-001/003 correctness judgment is the open gap.

## AI-assisted work checks

- AI scope: authored the documentation and template changes on this branch.
- Model/tool used: an AI coding agent operating on the repo.
- Permissions/actions allowed: edit docs, skills, templates, and this packet; run the test suite and validators.
- Independent checks performed: the pre-existing contract tests, ruff, `ng doctor`, `ng tokens`, and the packet validators — none authored by the actor for this change.
- Self-check / turnover records: this packet.
- Hallucination/slop screening: claims about test results are reproducible commands, not narration; the doctrine's correctness is explicitly left to human review.
- Human approval gates exercised: pending — the merge decision is the reviewer's.

## Required links

- Basis: `basis.md`
- Ship: `ship.md`
- Doctrine: `../../../docs/02-operating-system/actor-evidence-independence.md`

## Exit criteria

- Each claim has a status.
- Evidence the actor authored alone is labeled a self-check and carried as residual risk.
- The reviewer can reproduce the mechanical evidence without trusting the actor's narration.

## Source-lineage note

Original Nuclear-grade packet inspired by public verification, independent-review, and software-assurance ideas mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
