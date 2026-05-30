# Adversarial Review — Add Agent Tool Permissions Packet

**Review date:** 2026-05-17
**Reviewer stance:** a hostile reviewer hunting for overclaiming, missing evidence, broken claim-to-evidence links, and hidden release risk.
**Packet:** `.nuclear/changes/add-agent-tool-permissions/`

---

## Executive finding

The packet is strong enough for a **worked-example v0** if it stays tightly scoped to C-001: workspace-only file writes, plus making denied writes visible in the audit log. It should not be shown as a production sandbox, a complete agent-permission framework, or evidence for API or approval controls.

The biggest risk is not the code. It is **the reader reading in more than is there**. The launch docs must say that Nuclear-grade proves narrow, bounded claims, not general safety.

---

## Review checklist

| Area | Adversarial question | Finding | Disposition |
|---|---|---|---|
| Scope | Does the packet imply more than it proves? | C-001 and C-004a are proven; C-002 and C-003 are deferred. The ship record warns against broad claims. | acceptable with README wording |
| Evidence | Is there real evidence, not just prose? | Yes: the pytest tests were written first and pass after the build. | pass |
| Negative tests | Did we test ways this can fail? | The `../` path, absolute path, symlink escape, and silent denial are all tested. | pass for v0 |
| Path edge cases | Are all filesystem attacks covered? | No. TOCTOU, permissions and ACLs, hard links, mounts, Windows rules, and concurrent changes are not covered. | leftover risk; block any production claim |
| Auditability | Can you see denied actions? | The tests check in-memory audit events. | pass for teaching v0; gap for production |
| Release readiness | Is the ship/no-ship decision plain? | Yes: ship with leftover risk only after review and the validator. | acceptable |
| Compliance boundary | Any formal compliance claim? | The packet says again and again that it makes no compliance claim. | pass |
| Source lineage | Does it cite private or paywalled standards as direct template lineage? | It points to public-source family docs through the source map and crosswalk, and avoids direct private template lineage. | pass |
| AI-assisted work | Is the AI's part disclosed? | Verification records the AI's drafting and editing scope and shows no direct release side effects. | pass |

---

## Required corrections before launch

1. The README must link to the finished packet, not just the blueprint.
2. The Quickstart must use real `cp` commands, not `copy` pseudocode.
3. The validator must check the packet's required files, sections, and status labels before we say the launch docs are ready.
4. The worked-example README should change "Blueprint only" to "Worked example v0 includes a completed Standard-mode packet."

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

- The scope stays limited to C-001 and C-004a.
- The launch docs keep the no-compliance and no-production-sandbox boundary.
- The validator passes before commit or push.

## Source-lineage note

This adversarial review is an original Nuclear-grade review artifact. It uses the repo operating model and the public-source lineage summed up in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.

## Decision

**Adversarial review result:** pass for the teaching worked-example v0, on the condition that the validator passes and the launch-doc wording is updated.

**Residual risk owner:** the Nuclear-grade maintainer.

**Recheck trigger:** any public wording that grows the example from "C-001 evidence chain" into "secure agent permissions" or "compliance-grade agent controls."
