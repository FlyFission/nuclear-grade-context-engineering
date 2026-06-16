# Standard Basis Record

**Purpose:** State what must stay true for the change to be safe, reliable, secure, useful, and easy to review.

**Activation threshold:** Use for Standard changes where the requirements, architecture, interfaces, dependencies, AI power, protected outcomes, or outcomes to prevent need a clear basis.

**Minimum useful version:** the mission, the protected outcomes, the outcomes to prevent, the assumptions, the constraints, the trust decisions about intended use, and the evidence needs.

**Overhead trap:** Do not invent requirements by writing a long design essay. Link to the real needs and capture only the basis this change needs.

---

## Change context

- Slug: integrations-cross-tool-install
- Related risk record: `risk.md`
- Owner: FlyFission (Ben Huffer)
- Date: 2026-06-16
- Decision this basis supports: ship cross-tool skill distribution plus an opt-in MCP server.

## Mission / need

Users want to install the skill catalog once and have it auto-surface in Codex, Claude Code, Cursor, Windsurf, and VS Code, without per-tool manual wiring and without inflating always-on context.

## Protected outcomes

What must the system keep safe?

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Base install stays zero-dependency | leanness is a core value; many users never want MCP | `pyproject` keeps `mcp` under optional extras; the suite runs without it |
| Existing CLI behavior unchanged | an additive feature must not regress current users | full suite green; existing tests untouched |

## Unacceptable outcomes

What must not happen?

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Skills written to a wrong, undocumented path | user confusion; orphaned files | doc-confirmed paths, `--dry-run`, runtime verify note, `--dest` override |
| A version bump that leaves a mirror stale | inconsistent metadata; possible overclaim | sync test across `pyproject`, plugin manifests, `nuclear-grade.yaml`, `CITATION.cff` |
| MCP dependency forced on the base install | breaks the zero-dependency promise | `mcp` is an optional extra; importorskip-guarded tests |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Each tool auto-loads `SKILL.md` by description | fact | official docs for each tool | a tool drops the Agent Skills standard | FlyFission |
| Each tool's skills directory is as documented | fact (except VS Code user path) | official docs; VS Code user path is best-known | a tool relocates its skills directory | FlyFission |
| `mcp>=1.0` is installable and exposes FastMCP | fact | PyPI shows 1.0.0..1.27.2; verified in a clean venv | `mcp` removes FastMCP or changes the API | FlyFission |

## Grounding status

Keep confidence apart from evidence before any derived claim is accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Codex plugin manifest uses name/version/description/skills | source claim | developers.openai.com/codex/plugins/build | shape of `.codex-plugin/plugin.json` |
| VS Code project skills live in `.github/skills` | source claim | code.visualstudio.com agent-skills docs | the `vscode` project path in `install_dest` |
| VS Code user-scope skills path | unknown | best-known default only | kept unverified; flagged plus `--dest` |

## Interfaces and trust boundaries

- Internal interfaces affected: the `ng` CLI subcommand surface (`install`, `mcp-config`) and the new `nuclear_grade.mcp_server` module.
- External services/APIs affected: none; all operations are local filesystem.
- Data classes affected: none.
- Human approval boundaries: human PR review on PR #42 before merge.
- AI/model/tool authority boundaries: MCP tools set up and report on records on explicit call; no autonomous or networked authority.

## Dependency / model / supplier intended use

Use this section only when activated.

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| `mcp` (Python SDK) | run the optional MCP server | only MCP users affected; the base install is unaffected | optional extra; pinned `mcp>=1.0`; the `mcp-smoke` CI job | a new major of `mcp` or a FastMCP API change |

## Derived requirements or claims

Include only the important claims that need evidence.

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN a user runs `ng install <tool>` THE SYSTEM SHALL copy the skill catalog into that tool's documented skills directory. | mission / need | `install_dest` plus `handle_install` | install tests plus dry-run |
| REQ-002 | THE SYSTEM SHALL keep the base install dependency-free, and the MCP server SHALL be an optional extra. | protected outcome | `[project.optional-dependencies] mcp` | suite runs without the extra |
| REQ-003 | WHERE a tool's skills path is not doc-confirmed THE SYSTEM SHALL print a verify note and accept `--dest`. | unacceptable outcome | `VERIFIED_TOOLS` plus the note plus `--dest` | unverified-tool test |
| REQ-004 | THE SYSTEM SHALL keep every version mirror in sync with `pyproject`. | unacceptable outcome | version-sync test | `test_all_version_mirrors_track_pyproject` |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` summary plus `INTEGRATIONS.md` |
| Architecture — shape and major parts | yes | `nuclear_grade/cli.py`, `nuclear_grade/mcp_server.py` |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data model change |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: PR #42
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
