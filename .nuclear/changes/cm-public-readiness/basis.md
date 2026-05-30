# Basis - CM Public Readiness

**Purpose:** State what must stay true while we reframe Nuclear-grade around keeping the approved version under control (configuration management, CM).

## Change context

- Slug: `cm-public-readiness`
- Related risk record: `risk.md`
- Owner: Maintainer
- Date: 2026-05-23
- Decision this basis supports: Whether this repo is ready to present Nuclear-grade publicly as configuration management for AI-assisted software work.

## Mission / need

Make the repo immediately legible to AI-agent users while preserving the deeper promise: controlled configuration, bounded authority, claim-to-evidence traceability, baseline discipline, and operating learning.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Public hook is simple and differentiated. | Skill repos go viral when value is obvious. | README and workflow docs. |
| CM is real, not branding. | The repo name creates high expectations. | CM docs, templates, skills, commands, packet records. |
| Existing Quick/Standard onboarding still works. | Public users need immediate utility. | CLI tests and validator commands. |
| Packaging entry point works. | Public install attempts should not fail. | Editable install and console command check. |
| Boundary language remains explicit. | Avoids compliance, certification, safety, security, or regulatory overclaims. | Public-doc tests and scans. |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| README sells virality but not substance. | Short-term attention, weak trust. | CM thesis and concrete artifacts. |
| CM docs become a process binder. | Users bounce before trying it. | Activated records only. |
| Packaging fix introduces top-level package collision. | Install path fails or imports wrong `tools`. | Namespaced package and explicit discovery. |
| Deleted internal plan remains linked. | Broken evidence chain. | Impact screen and link scans. |
| Public claims imply formal assurance. | Overtrust and legal risk. | Boundary wording and validator seed list. |

## Assumptions and constraints

| Assumption / constraint | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|
| Public v0 remains educational and workflow-oriented. | README and disclaimer. | Any regulated or production assurance claim. | Maintainer |
| Quick/Standard validator remains the deterministic v0 scope. | Validator docs. | Claims of CM/Nuclear full validation. | Maintainer |
| CM records are activated by consequence. | `configuration-management.md`. | Users asked to fill every CM record by default. | Maintainer |
| Skills and commands stay portable Markdown. | Public v0 integration scope. | Packaged marketplace integration claim. | Maintainer |

## Interfaces and trust boundaries

- Internal interfaces affected: `nuclear_grade.cli`, `nuclear_grade.ng_validate`, `tools/ng.py`, `tools/ng_validate.py`.
- External services/APIs affected: GitHub CI badge and future repository visibility only.
- Human approval boundaries: Maintainer approval before public visibility or PR merge.
- AI/model/tool authority boundaries: Agent workflows must record allowed actions, forbidden actions, evidence, and stop conditions.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| CM-001 | Nuclear-grade public thesis is configuration management for AI-assisted work. | Public differentiation and source foundation. | README, workflows, CM docs. | Public doc review. |
| CM-002 | Activated CM records exist without making Standard mode too heavy. | Proportional rigor. | `templates/cm/`. | Template/catalog tests. |
| CM-003 | Skills and command prompts expose CM actions. | Viral skill-pack utility. | New skills and command cards. | Contract tests and doctor. |
| CM-004 | Installed console entry point avoids `tools` package collision. | PR #8 blocker. | `nuclear_grade/` package and setuptools find scope. | Packaging test and editable install. |
| CM-005 | Public-readiness evidence remains navigable. | CM claim requires traceability. | This packet and baseline record. | Packet validation. |

## Required links

- `risk.md`
- `trace.md`
- `verification.md`
- `controlled-items.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Claims are narrow and evidence-backed.
- Non-claims remain explicit.
- Evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade basis inspired by public design-basis, configuration-management, software assurance, secure-development, and release-readiness concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
