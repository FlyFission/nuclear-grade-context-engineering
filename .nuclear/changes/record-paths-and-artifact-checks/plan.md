# Record Paths and Artifact Checks Implementation Plan

> **For agentic workers:** Execute scoped tasks with test-first verification; the root agent integrates and a fresh reviewer checks the branch.

**Goal:** Address the verified public-release defects and deliver a reviewable PR.

**Architecture:** Keep existing stdlib interfaces. Share path validation across CLI/MCP, bound subprocess cleanup, strip copied abstracts while preserving metadata, and strengthen artifact checks.

**Tech Stack:** Python 3.11+, pytest, Git, existing CI/build tools.

**Spec:** [basis.md](basis.md), authorized by the user's explicit remediation request.

## Global constraints

No new runtime dependency; no Git history rewrite, remote deletion, credential disclosure, or release publication. No assurance claims. Existing checkout is already isolated.

## Review focus

Absolute and Windows path forms; symlinked packet/files; descendants retaining output pipes; non-consumer-domain mailboxes in transcripts; bibliographic records losing identifiers during abstract removal.

## Build sequence

- [x] REQ-001: add failing CLI/MCP traversal, absolute, separator, and symlink tests; run RED; add shared validation; run GREEN.
- [x] REQ-002: delegate harness and its tests only; reproduce retained-pipe timeout; implement bounded cleanup; run targeted tests. Do not silently import unrelated draft PR #130 changes.
- [x] REQ-003/005: delegate research JSON, release inventory and metadata regression only; remove abstract/summary fields, refresh provenance and historical cleanup guidance; retain metadata and annotations.
- [x] REQ-004: add failing artifact-coverage fixtures; expand tree/suffix and mailbox classification without treating intentional fixtures as leaks; prove rejection and safe examples.
- [x] Integrate delegated results, run complete pre-PR checks, record raw outcomes and coupled custody, regenerate badge, and perform fresh-context whole-branch review.
- [ ] Push feature branch, create PR, resolve CI/review failures and conflicts; do not claim merge or historical erasure without evidence.

## Handoff and rollback

Root agent owns CLI/MCP, artifact review, packet, integration and PR. Timeout implementer owns harness/tests. Public-content implementer owns research JSON, provenance docs and metadata tests. Same model family: these roles do not establish independence. Maintainer owns merge, history cleanup and release. Revert scoped commits if needed; never erase raw adverse results from the review evidence.

## Required links

[risk.md](risk.md), [basis.md](basis.md), [plan.md](plan.md), [trace.md](trace.md), [verification.md](verification.md), [ship.md](ship.md).

## Exit criteria

The scoped regressions pass, remaining gaps are explicit, and maintainer review precedes merge.

## Source-lineage note

Original project remediation record using the public-source workflow mapped in [source-map.md](../../../docs/00-standards-foundation/source-map.md). No certification, legal opinion, or assurance claim.
