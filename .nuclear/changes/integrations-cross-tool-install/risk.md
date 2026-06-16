# Standard Risk Record

**Purpose:** Sort a real change by risk after questioning the assumptions, justify Standard mode, and name any extra records you turn on.

**Activation threshold:** Use for behavior users can see, lasting design decisions, important dependency/model/API/prompt/tool changes, security/privacy/data handling, operational stance, or anything where the stakes, the uncertainty, or the review value are more than trivial.

**Minimum useful version:** the scope, the affected controlled items, the threshold ratings, the chosen mode, the artifacts you turn on, and the evidence due right away.

**Overhead trap:** Do not score risk with fake precision. Use the screen to surface the stakes and the evidence you need.

---

## Change identity

- Slug: integrations-cross-tool-install
- PR / issue: PR #42
- Owner: FlyFission (Ben Huffer)
- Date: 2026-06-16
- Current lifecycle phase: Verify
- Current work phase: audit
- Summary: Add cross-tool skill distribution (`ng install` for Codex, Claude Code, Cursor, Windsurf, VS Code), a publishable `.codex-plugin` package, a one-command `install.sh`, and an opt-in MCP server (`nuclear-grade[mcp]` plus `ng mcp-config`). Additive and reversible; bumps the version 0.5.0 -> 0.6.0.

## Mission anchor

State what this change is for, so a long session can be checked against it. See `staying-on-mission`.

- Objective: let a user install the skill catalog once and have it auto-surface across every supported agent tool, the way Superpowers does, without bloating context.
- Success criteria: `ng install <tool>` places the skills in each tool's documented location; the base install stays zero-dependency; the full test suite, `doctor`, and the token budget stay green.
- Non-goals / forbidden directions: no always-on hooks added on install; no MCP dependency forced on the base install; no change to existing CLI commands or methodology.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: workspace `.nuclear/mission.md` and the prior `.nuclear/changes/plugin-install-vehicle/` record.

## Questioning-attitude summary

- Decision question: how do we distribute the existing skills across tools so they auto-integrate, leanly, without inventing new machinery?
- Evidence that would change the decision: a tool not supporting the `SKILL.md` standard, or its skills directory differing from the documented path.
- Assumptions that changed the mode: introducing a new optional dependency (`mcp`) is a supply-chain/architecture decision, which lifts this above Quick.
- Facts still needing validation: the VS Code user-scope skills path (`~/.config/github-copilot/skills`) is a best-known default, flagged at runtime.
- Stop or hold conditions: stop and use `--dest` if a tool's path is uncertain; escalate if any change would force a dependency on the base install.

## Affected configuration items

List the affected code, docs, infrastructure, dependencies, prompts, models, data, evals, releases, dashboards, or runbooks.

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `nuclear_grade/cli.py` | code | adds `ng install` and `ng mcp-config` | `nuclear_grade/cli.py` |
| `nuclear_grade/mcp_server.py` | code | optional MCP server wrapping existing checks | `nuclear_grade/mcp_server.py` |
| `.codex-plugin/plugin.json` | config | makes the repo a publishable Codex plugin | `.codex-plugin/plugin.json` |
| `pyproject.toml` | dependency | adds the optional `mcp` extra and a second script | `pyproject.toml` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | low | a wrong path writes files to the wrong dir; no data loss |
| Reversibility | high | delete copied skills / uninstall the extra; no state changed |
| Detectability | high | `--dry-run`, printed target path, tests, and `doctor` surface problems |
| Exposure | low | local filesystem only; no network, secrets, or production |
| Uncertainty | low | paths doc-confirmed except the VS Code user path (flagged) |
| Dependency trust | medium | introduces an optional `mcp` dependency; base stays zero-dep |
| AI authority | low | tools set up and report on records; no autonomous authority |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check |
| Known procedure where following the steps matters | yes | packet path |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | no | turnover |
| A high-stakes critical action | no | independent verification |

## Selected mode

- Mode: Standard
- Why this mode: it adds a new optional dependency and a new module (the MCP server), and touches packaging across several tools.
- Why lighter mode is not enough: Quick explicitly excludes dependency-trust and architecture decisions, both present here.
- Why heavier mode is not yet required: the change is additive, reversible, local, and makes no safety, security, or production claim.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | summary captured inline above | FlyFission |
| `basis.md` | yes | requirements and the dependency decision need a basis | FlyFission |
| `verification.md` | yes | claims need evidence | FlyFission |
| `ship.md` | yes | a release decision and version bump are involved | FlyFission |
| `turnover.md` | no | single-session change, no handoff | FlyFission |
| `self-check.md` | no | no irreversible critical action | FlyFission |
| `supplier-trust.md` | no | the optional dep is opt-in; trust noted in `basis.md` | FlyFission |
| Nuclear subset record | no | not safety or regulated work | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: confirmed each tool's documented skills path before writing `install_dest`.
- Minimum evidence before merge/release: full test suite, `ruff`, `doctor`, and token budget green; MCP server verified with the extra installed.
- Independent review needed? yes; human PR review on PR #42.

## Required links

- Packet: `.nuclear/changes/integrations-cross-tool-install/`
- `questioning-attitude.md` if activated: not activated; the summary is in this `risk.md`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
