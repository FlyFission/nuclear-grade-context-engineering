# Risk

## Change identity

- Slug: review-findings-2026-05
- PR / issue: (TBD on push)
- Owner: maintainer
- Date: 2026-05-27
- Current lifecycle phase: Execute
- Summary: Coordinated remediation of the twelve findings from the 2026-05 adversarial review of `nuclear-grade-context-engineering`. Closes a critical front-door framing gap (F1), a critical installed-wheel breakage (F2), and a high-leverage prohibited-claims evasion (F3); adds an enforced mode declaration (F4); raises CLI surface to cover all four template modes (F5); adds CI matrix and lint (F6); tightens validator detection (F7); softens evidence-overclaiming framing in worked-example and README (F8); cleans changelog state (F9); adds CITATION.cff and CODEOWNERS (F10); marks the SWOT remediation report as proposed (F11); and stamps 0.2.0.

## Questioning-attitude summary

- Decision question: Should the repo ship the twelve fixes as a single coordinated 0.2.0 release, or split them across smaller releases?
- Assumptions that changed the mode: The Mode declaration requirement (F4) is a breaking validator rule for downstream packets; the wheel rework (F2) changes the build backend. Both warrant Standard and a minor version bump.
- Facts still needing validation: That `hatchling` `force-include` produces a wheel where `nuclear_grade/_bundled/<dir>/...` is reachable from a clean `pip install`. That existing repo packets still validate after the validator change.
- Stop or hold conditions: If `hatchling` switch destabilizes the wheel, defer F2 to a follow-up release, ship the other eleven fixes as 0.2.0, mark F2 as Not Included.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `nuclear_grade/cli.py` | Code | Adds `--mode cm`, `--mode golden-path`, `migrate`, wheel resolver | `../../../nuclear_grade/cli.py` |
| `nuclear_grade/ng_validate.py` | Code | Tightens prohibited-claims regex, mode requirement, long-label detection | `../../../nuclear_grade/ng_validate.py` |
| `pyproject.toml` | Build | Switches to `hatchling`; bumps to 0.2.0 | `../../../pyproject.toml` |
| `.github/workflows/ci.yml` | CI | Adds matrix, ruff, wheel-smoke job | `../../../.github/workflows/ci.yml` |
| `README.md`, `QUICKSTART.md` | Docs | Frames the demo, lists new CLI modes | `../../../README.md`, `../../../QUICKSTART.md` |
| `templates/quick/risk.md`, `templates/standard/risk.md` | Templates | Pre-fills the Mode declaration | `../../../templates/quick/risk.md` |
| `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` | Docs | Adds methodology banner | (see file) |
| `docs/04-adoption/report-swot-gap-remediation.md` | Docs | Marks proposed-vs-existing | (see file) |
| `CHANGELOG.md`, `CITATION.cff`, `.github/CODEOWNERS` | Hygiene | Release-stamping and governance | `../../../CHANGELOG.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Affects public CLI behavior and validator rules for external users. |
| Reversibility | medium | Each layer is revertible; wheel rework reverts as one commit. |
| Detectability | high | CI matrix, wheel-smoke job, and pytest will fail loudly on regressions. |
| Exposure | medium | Public repo; external users may already pin to 0.1.0. |
| Uncertainty | medium | `hatchling` `force-include` behavior is well documented but not previously used here. |
| Dependency trust | low | Adds `hatchling`, `ruff`, `build`. All PyPA-or-Astral mainline. |
| AI authority | low | No new agent-write permissions. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine/repetitive action where inattention is plausible | no | n/a |
| Known procedure where workflow adherence matters | yes | packet path with explicit execution order in `plan.md` |
| Novel or uncertain work where assumptions may be wrong | yes | questioning attitude in this risk; wheel rework has a documented rollback |
| Interrupted, resumed, or handed-off work | no | n/a |
| High-consequence critical action | no | n/a |

## Selected mode

- **Mode:** Standard
- **Why this mode:** Twelve coordinated changes spanning code, build, CI, content, and templates; a breaking validator rule; a release stamp.
- **Why lighter mode is not enough:** Quick cannot record claim-to-evidence mapping for twelve findings or the basis for the breaking change.
- **Why heavier mode is not yet required:** No regulated-use deployment, no safety basis, no controlled-supplier dedication. Public repo update only.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline above for brevity. | maintainer |
| `basis.md` | yes | Twelve findings need claim-to-evidence mapping. | maintainer |
| `verification.md` | yes | Per-claim evidence status. | maintainer |
| `ship.md` | yes | Release decision for 0.2.0. | maintainer |
| `turnover.md` | no | No handoff; single-author packet. | maintainer |
| `self-check.md` | no | No high-consequence critical action present. | maintainer |
| `supplier-trust.md` | no | No new external supplier. | maintainer |
| Nuclear subset record | no | Not warranted. | maintainer |

## Immediate evidence obligations

- Minimum evidence before build: All seven existing repo packets already declare a `## Selected mode` section. Confirmed.
- Minimum evidence before merge/release: pytest green on 3.11 and 3.12; `doctor` OK; every existing packet validates; wheel-smoke job green; manual paraphrase battery passes; CHANGELOG stamped 0.2.0.
- Independent review needed? no for this PR; the review under remediation is itself the independent input.

## Required links

- Packet: `.nuclear/changes/review-findings-2026-05/`
- Related PR/issue: TBD on push
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- Mode is justified as Standard.
- Activated artifacts are explicit.
- Twelve findings are individually addressed in `basis.md` claims C-001 through C-012.
- No hidden activation trigger for a stronger mode.

## Source-lineage note

Original Nuclear-grade packet inspired by the public graded-rigor, configuration-management, software-assurance, and secure-development concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
