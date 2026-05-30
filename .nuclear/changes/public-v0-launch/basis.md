# Basis — Public v0 Launch

**Purpose:** State what must stay true before Nuclear-grade is made public.

---

## Change context

- **Slug:** `public-v0-launch`
- **Related risk record:** `risk.md`
- **Owner:** Maintainer
- **Date:** 2026-05-19
- **Decision this basis supports:** Whether the repository is ready to become public as an honest v0.

## Mission / need

Make the repository public only after its docs, examples, source map, validator, tests, and launch workflow support the stated promise: bounded evidence for AI-assisted software work without compliance or production assurance overclaims.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Public docs contain no internal launch residue. | Private paths or names weaken credibility and can expose local process details. | Residue scans. |
| Source-lineage claims are status-labeled. | Readers must know what is verified public lineage versus context. | Source-map status labels and source scans. |
| Validator behavior matches Quick/Standard docs. | Public users should not hit documented commands that fail for Quick packets. | Validator tests and packet validation commands. |
| Worked-example status matches reality. | The flagship example must not contain stale planned/gap records for completed checks. | Worked-example packet validation and residue scans. |
| GitHub visibility changes only after merge/CI/review. | Visibility is the public release side effect. | PR/CI/visibility evidence in `ship.md`. |
| License/use boundaries are explicit. | MIT reuse should not be mistaken for regulated verification, NQA-1, QA, safety, procurement, regulator, or fitness assurance. | README, DISCLAIMER, compliance-boundaries, validator seed list, and overclaim scans. |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Public files mention internal local paths or launch residue. | Credibility and privacy risk. | `rg` residue scan blocks launch. |
| Unverified sources are presented as direct lineage. | Source credibility risk. | Status labels and source-gap scan. |
| Quick packet validation fails under documented command. | Onboarding failure. | Quick-mode tests. |
| Public language implies compliance or production sandboxing. | Overtrust and misuse risk. | Prohibited-phrase scan and boundary language. |
| Repository is made public before PR/CI pass. | Broken launch state becomes public. | Visibility flip remains in `ship.md` as conditional. |

## Assumptions and constraints

| Assumption / constraint | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|
| Public v0 is enough; v1 polish is not required. | Launch plan. | Request to add more examples or broader validator modes before launch. | Maintainer |
| Validator v0 covers Quick and Standard only. | `tools/README.md`, `QUICKSTART.md`. | Public docs claim Nuclear/Incident/Release validator support. | Maintainer |
| Source gaps can remain only when downgraded. | `source-map.md`. | Any `public-url-needed` row is cited as direct lineage. | Maintainer |
| No formal compliance/certification claim is made. | Boundary docs and disclaimer. | Any public claim that Nuclear-grade satisfies a standard or regulator. | Maintainer |
| MIT license is permissive but not an assurance statement. | `LICENSE`, OSI/SPDX MIT license references, and boundary docs. | Readers or contributors treat reuse permission as project-specific approval or fitness. | Maintainer |

## Interfaces and trust boundaries

- **Internal interfaces affected:** `validate_packet(packet)` in `tools/ng_validate.py`.
- **External services/APIs affected:** GitHub CLI and GitHub repository visibility after PR merge.
- **Data classes affected:** Public Markdown docs and educational example code only.
- **Human approval boundaries:** Maintainer approval before PR ready/merge/visibility flip.
- **AI/model/tool authority boundaries:** AI-assisted edits require deterministic tests/scans before public release.

## Dependency / model / supplier intended use

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| Python standard library | Validator implementation. | Incorrect validation could miss launch blockers. | Focused pytest coverage. | Validator scope changes. |
| `pytest` | Validator and example test execution. | Test evidence unavailable. | CI installs pytest. | CI dependency failure. |
| GitHub CLI | PR, CI, and visibility operations. | Public visibility cannot be verified. | Stop before visibility flip if unavailable. | GitHub API/network failure. |

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| L-001 | Public docs contain no internal launch residue. | Protect public credibility and privacy. | Residue scan over tracked public files. | `verification.md` scan result. |
| L-002 | Source-map entries are verified-public or explicitly downgraded. | Prevent unverified citation claims. | `Status` column and source-gap scan. | `verification.md` scan result. |
| L-003 | Validator supports documented Quick and Standard packet modes. | Keep onboarding command honest. | Mode detection, required-file checks, tests. | pytest and packet validation. |
| L-004 | Worked-example packet status matches current repo state. | Avoid stale launch contradictions. | Packet edits and validation. | validator/scans. |
| L-005 | GitHub visibility changes only after merged PR and CI pass. | Control public release side effect. | `ship.md` release decision gate. | PR/CI/`gh repo view` evidence. |
| L-006 | License/use boundaries make MIT reuse distinct from formal assurance. | Prevent misuse or overtrust. | README/DISCLAIMER/compliance-boundaries updates and validator seed expansion. | Legal/license scans and validator tests. |

## Required links

- Risk record: `risk.md`
- Plan record: `plan.md`
- Trace record: `trace.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Source lineage: `../../../docs/00-standards-foundation/source-map.md`

## Exit criteria

- Launch claims are explicit.
- Non-claims are preserved.
- Evidence needs flow into `verification.md`.
- Release decision remains gated in `ship.md`.

## Source-lineage note

Original Nuclear-grade launch basis inspired by public design-basis, configuration-management, verification, and release-readiness concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
