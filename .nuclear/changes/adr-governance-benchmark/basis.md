# Basis — ADR governance lessons and landscape benchmark

## Mission

The owner asked for a top-down and bottom-up comparison against similar repositories and a review of uber/ADR's governance. This packet records the findings and the requirements this change implements. Everything else is ranked as follow-up, not done.

## Uber ADR review (read 2026-10-12)

uber/ADR is **Agentic AI Detection and Response**, an agent-security system (endpoint discovery, normalized agent telemetry, a dual-agent detector, and a 304-task benchmark). It is not an Architecture Decision Record tool. Its governance patterns that fit this repository:

| ADR pattern | Where in ADR | Fit here |
|---|---|---|
| Partial coverage is a distinct state, so an incomplete scan never reads as clean | `Discovery/README.md` exit code 2 | Adopted as `open_evidence_items` in the receipt (REQ-002) |
| Run manifest: input hashes plus git commit | `Detection/run_manifest.py` | Adopted as receipt digests and git state (REQ-002) |
| Versioned, content-free health schema | `Sensor/README.md` `adr.sensor.health` | Adopted as `schema` and `schema_version` (REQ-002) |
| Aggregate CI gate with `if: always()` | `.github/workflows/ci.yml` | Adopted (REQ-003) |
| Dependabot with each freeze decision recorded inline | `.github/dependabot.yml` | Adopted (REQ-004) |
| OIDC trusted publishing, tag equals version, never move a tag | `docs/RELEASING.md` | Adopted with owner approval: identity check, `releasing.md`, and `release.yml` (PyPI job opt-in) |
| Open-source release review: fixtures, accepted risks, attributions | `docs/OPEN_SOURCE_REVIEW.md`, `NOTICE.md` | Docs half adopted: `docs/05-reference/release-review.md` |
| PR template asks for worst-case risk | `.github/pull_request_template.md` | Already covered by "Residual risks or gaps" |

## Bottom-up findings

- **B-1 (fixed here):** `mcp` 2.x renamed `FastMCP` to `MCPServer`. The extra was pinned `<2`, so the server ran only on a superseded SDK.
- **B-2 (fixed here):** the CI matrix had no aggregate gate, no concurrency control, and no Python 3.13 leg.
- **B-3 (fixed here):** Actions are SHA-pinned but nothing updates the pins. `actions/checkout` is at v4.4.0.
- **B-4 (addressed):** `CHANGELOG.md` now has `[0.6.0] - 2026-10-12`, `CITATION.cff` matches, and `python -m nuclear_grade.release` enforces agreement in CI. Tagging stays with the owner. Original finding: version drift. `pyproject.toml`, both plugin manifests, and `CITATION.cff` say `0.6.0` (CITATION dated 2026-06-04), but `CHANGELOG.md` has no 0.6.0 section. About two months of work sits under `[Unreleased]`, and the repository has no git tags.
- **B-5 (withdrawn):** the README limits its benchmark claim to the 28 skills in the July 2026 pilot and calls it a historical snapshot. The claim is accurate as written.

## Landscape benchmark (top down)

The research was delegated and cites public pages. Star counts were not cross-checked and are left out on purpose.

**Ahead of the field:** evidence custody and actor–evidence coupling as a structural check (`--strict-custody`, `--strict-authority`); graded rigor down to an administrative floor; release, baseline, deficiency, incident, and OPEX loops; hardened, test-enforced hooks; skill frontmatter clean against the Agent Skills spec; a stdlib-only validator.

**Behind the field, ranked follow-ups:**

| ID | Gap | Exemplar |
|---|---|---|
| F-01 | Blocking PreToolUse policy gate that fails closed (hooks are advisory today) **Done:** opt-in `hooks/pre_tool_use.py` (packet `blocking-pretooluse-gate`). | Claude Code / Codex hook policy kits |
| F-02 | Release workflow: tag equals version, trusted publishing, signed attestation over the receipt digest | uber/ADR `RELEASING.md`, SLSA, in-toto/Sigstore |
| F-03 | Import machine traces (OTel GenAI agent spans, Agent Trace, ADR Sensor schema) into `execution-trace.md` | uber/ADR Sensor, Agent Trace draft |
| F-04 | Fold accepted claims into a living baseline when a packet closes | OpenSpec archive |
| F-05 | Behavioral and pressure-scenario skill evals beyond routing cases | obra/superpowers evals, inspect_ai |
| F-06 | Skill and MCP security scan in CI, plus a release-review/NOTICE page | Snyk Agent Scan, uber/ADR |
| F-07 | Cross-tool distribution and directory listings (`npx skills`/skills.sh) | anthropics/skills, superpowers |
| F-08 | MADR-compatible front matter (status, deciders, supersedes) on decision records **Done:** optional front matter in `risk.md` templates (packet `threat-map-and-decision-metadata`). | MADR 4 |
| F-09 | Map the OWASP Top 10 for Agentic Applications (2026) in the threat model **Done:** `agent-threat-model.md`; source held at `public-url-needed`. | OWASP GenAI project |

## Requirements

- **REQ-001:** The optional MCP server shall run on `mcp` 1.x and 2.x, and CI shall test both.
- **REQ-002:** `ng validate --json` shall emit a versioned receipt with per-file and set digests, packet-scoped git state, validator and Python versions, and evidence-status counts. Exit codes stay the same.
- **REQ-003:** CI shall expose one required-check job that fails when any upstream job fails or is skipped.
- **REQ-004:** SHA-pinned Actions shall have an update channel, with the policy rationale recorded inline.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)
- Source map: [`source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

Each requirement is testable, and every unimplemented finding is named as a follow-up rather than implied done.

## Source-lineage note

uber/ADR is recorded in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md) Tier 6 as pattern lineage only. The landscape rows above are context for prioritizing work, not source lineage. No superiority, compliance, or efficacy claim is made.
