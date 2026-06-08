# Verification — Enterprise Landing Page

**Purpose:** Show that the landing-page claims have evidence that fits the size of the change.

---

## Verification context

- **Slug:** `enterprise-landing-page`
- **Related basis:** `basis.md`
- **Owner:** Maintainer
- **Date:** 2026-06-06
- **Verification scope:** The README rewrite, the two canonical diagrams, the SVG banner, and this packet.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | peer review | Read the rendered README top to bottom. | Project, one idea, and a runnable proof are visible within the first screen. | pass | `README.md` | None. |
| REQ-002 | local proof | self-check | Confirm an "In words" fallback under each Mermaid block. | Every embedded diagram has adjacent text. | pass | `README.md` | None. |
| REQ-003 | local proof | deterministic test | `pytest tests/test_public_docs.py` plus diff review of disclaimers. | Boundary phrases stay negative; disclaimers stay expanded. | pass | `tests/test_public_docs.py` | None. |
| REQ-004 | local proof | deterministic test | Mermaid validation of both new diagrams; confirm they exist in both files. | Both diagrams valid and present in `docs/diagrams.md` and `README.md`. | pass | `docs/diagrams.md` | None. |
| REQ-005 | fact | self-check | Compare README counts to `nuclear-grade.yaml`. | Counts read 27 skills and 26 command prompts, qualified by version. | pass | `nuclear-grade.yaml` | None. |
| REQ-006 | local proof | deterministic test | `pytest tests/test_public_docs.py` plus `ng validate` link check. | Invariants preserved; links resolve. | pass | `tests/test_public_docs.py` | None. |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Doc invariant tests | `python -m pytest tests/test_public_docs.py -v` | Local CI image | pass | `tests/test_public_docs.py` |
| Packet validation | `python tools/ng.py validate .nuclear/changes/enterprise-landing-page` | Local | pass | `.nuclear/changes/enterprise-landing-page/` |
| Repo health | `python tools/ng.py doctor .` | Local | pass | `tools/ng.py` |
| Token budget | `python tools/ng.py tokens .` | Local | pass | `nuclear-grade.yaml` |
| Mermaid validation | Render both new diagrams in a Mermaid validator | External validator | pass | `docs/diagrams.md` |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| A boundary phrase used as a positive claim. | `test_boundary_phrases_are_only_used_in_negative_context`. | pass | `tests/test_public_docs.py` |
| Lifecycle string or HPI phrase dropped. | Assertions in `test_public_docs.py`. | pass | `tests/test_public_docs.py` |
| A diagram readable only in Mermaid. | Manual check for a text fallback under each block. | pass | `README.md` |
| Internal residue leaking into a public doc. | `test_public_docs_contain_no_internal_residue`. | pass | `tests/test_public_docs.py` |

## AI-assisted work checks

- **AI scope:** An AI agent drafted the README, the diagrams, the banner, and this packet.
- **Model/tool used:** Coding agent with repository file and shell access.
- **Permissions/actions allowed:** Edit files in this repository and run local checks only.
- **Independent checks performed:** Deterministic doc tests, the packet validator, doctor, and the token gate.
- **Self-check / turnover records:** This packet; no separate turnover needed for a single-session change.
- **Hallucination/slop screening:** Counts cross-checked against `nuclear-grade.yaml`; links verified to resolve.
- **Human approval gates exercised:** Maintainer review and CI before merge.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / test logs: branch CI on `claude/enterprise-landing-page-uSnWo`
- Implementation diff: `README.md`, `docs/diagrams.md`, `docs/assets/landing-banner.svg`

## Exit criteria

- Each important claim has a status.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.

## Source-lineage note

Original Nuclear-grade verification record inspired by public sources on verification and validation, software assurance, and application-security checks mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
