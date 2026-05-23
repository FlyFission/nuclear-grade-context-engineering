# Adversarial Review — Add Agent Tool Permissions Packet

**Review date:** 2026-05-17
**Reviewer stance:** hostile reviewer looking for overclaiming, missing evidence, broken traceability, and hidden release risk.
**Packet:** `.nuclear/changes/add-agent-tool-permissions/`

---

## Executive finding

The packet is strong enough for a **worked-example v0** if it stays tightly scoped to C-001: workspace-only file writes plus denied-write audit visibility. It should not be presented as a production sandbox, a complete agent-permission framework, or evidence for API/approval controls.

The biggest risk is not the code; it is **reader over-inference**. The launch docs must say that Nuclear-grade proves bounded claims, not general safety.

---

## Review checklist

| Area | Adversarial question | Finding | Disposition |
|---|---|---|---|
| Scope | Does the packet imply more than it proves? | C-001/C-004a are proven; C-002/C-003 are deferred. Ship record warns against broad claims. | acceptable with README wording |
| Evidence | Is there actual evidence, not prose? | Yes: pytest tests were written first and pass after implementation. | pass |
| Negative tests | Did we test ways this can fail? | Traversal, absolute path, symlink escape, and silent denial are tested. | pass for v0 |
| Path edge cases | Are all filesystem attacks covered? | No. TOCTOU, permissions/ACLs, hard links, mounts, Windows semantics, and concurrent mutation are not covered. | residual risk; block production claim |
| Auditability | Are denied actions observable? | In-memory audit events are asserted in tests. | pass for educational v0; gap for production |
| Release readiness | Is ship/no-ship decision explicit? | Yes, ship with residual risk only after review and validator. | acceptable |
| Compliance boundary | Any formal compliance claim? | Packet repeatedly says no compliance claim. | pass |
| Source lineage | Does it cite proprietary/paywalled standards as direct template lineage? | It references public-source family docs through source map/crosswalk and avoids direct proprietary template lineage. | pass |
| AI-assisted work | Is AI contribution disclosed? | Verification records AI-assisted drafting/editing scope and no direct release side effects. | pass |

---

## Required corrections before launch

1. README must link to the completed packet, not only the blueprint.
2. Quickstart must use actual `cp` commands, not `copy` pseudocode.
3. Validator must check the packet’s required files/sections and status labels before we claim the launch docs are ready.
4. The worked-example README should change “Blueprint only” to “Worked example v0 includes a completed Standard-mode packet.”

---

## Explicit non-claims to preserve

Do **not** claim:

- this is a production sandbox;
- this makes agent file writes secure in all environments;
- this covers Windows, containers, ACLs, hard links, race conditions, or hostile multi-user filesystems;
- C-002 external API controls are implemented;
- C-003 human approval controls are implemented;
- the repo satisfies any DOE/NRC/NASA/NIST/CISA/ASME/EPRI/IEEE/IEC/ISO/ANSI/ANS/NEI requirement;
- the packet is a formal dedication package, QA program, or certification artifact.

---

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `../../reference/workspace_guard.py`
- `../../tests/test_workspace_guard.py`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Scope remains limited to C-001/C-004a.
- Launch docs preserve the non-compliance and non-production-sandbox boundary.
- Validator passes before commit/push.

## Source-lineage note

This adversarial review is an original Nuclear-grade review artifact using the repo operating model and public-source lineage summarized in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.

## Decision

**Adversarial review result:** pass for educational worked-example v0, conditional on validator pass and launch-doc wording updates.

**Residual risk owner:** Nuclear-grade maintainer.

**Recheck trigger:** Any public language that expands the example from “C-001 evidence chain” to “secure agent permissions” or “compliance-grade agent controls.”
