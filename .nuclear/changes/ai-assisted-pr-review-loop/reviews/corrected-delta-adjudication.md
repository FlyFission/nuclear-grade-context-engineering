# Corrected-Candidate Delta Adjudication

## Candidate closure

- Base: `77f1645e9205c45c754a567fc5e0a3fcede52f0e`
- First-round provenance: `2bc9c005b8a796afae1857500d1f27573f754c43`
- Corrected payload provenance: `6cc462a422a00907c836b256aaa0e3c6fd5428ea`
- First-round payload SHA-256: `5bdc1044d2be0ea061690a21ea744543359fd8b3ae93d3041b21aa80e543572d`
- Corrected payload SHA-256: `3d6270a98cafe28cc44fe90a88222c5a7c9a24eb90375bbd5ad38086bc655950`
- Payload scope: the seven public/template/test files listed in `payload-manifest-round-1.txt`; this packet is excluded from the payload.

## Review outcomes

| Reviewer path | Result | Counted? | Disposition |
|---|---|---|---|
| Codex CLI, read-only exact-commit delta review | ACCEPT, no unresolved P0/P1 | yes | Admitted as corrected-candidate defect-closure evidence |
| Claude Code, read-only exact-commit delta review | Reached max turns while attempting an independently recomputed digest; no final verdict | no | Excluded from verdict evidence |
| Grok CLI, read-only exact-commit delta review | Reached max turns and returned a cancelled/incoherent result despite inspecting the relevant source | no | Excluded from verdict evidence |
| OpenCode Go / Kimi K3 and K2.7 Code, first-round attempts | Three attempts produced no substantive result before timeout; the final background attempt was killed after nearly 15 minutes with no output | no | Recorded as failed review paths, not evidence |

## Codex closure findings

Codex independently recomputed the seven-file payload digest at exact corrected commit `6cc462a` and obtained `3d6270a98cafe28cc44fe90a88222c5a7c9a24eb90375bbd5ad38086bc655950`, matching the retained manifest. It found no unresolved P0/P1 and confirmed:

1. Payload identity, provenance, exclusions, and out-of-payload attestation are separated.
2. Material correction makes the verdict stale and returns the candidate to verification.
3. Correction-budget exhaustion stops and escalates to the human owner.
4. The committed contract test compares the Mermaid blocks exactly and checks the new operational fields.
5. Base, provenance, affected claims, rerun obligations, and stale-verdict disposition are coherent.

Codex noted one optional P2: this excluded ship packet retained pre-freeze chronology such as “corrected commit pending.” This attestation update closes that wording without changing the reviewed seven-file payload. GitHub rendering, remote checks, and human merge authorization remain intentionally open.

## Verdict

**Local corrected-payload verdict: current, with no unresolved P0/P1.**

This verdict is bound to corrected payload SHA-256 `3d6270a98cafe28cc44fe90a88222c5a7c9a24eb90375bbd5ad38086bc655950`, first introduced at provenance commit `6cc462a`. The packet-only attestation commit is outside the payload scope. Any scoped payload change makes this verdict stale and requires renewed review. Any base/provenance change with the same payload requires an impact check.

Remote CI, rendered Mermaid inspection, PR review, and merge authorization remain human-owned gates. This advisory review does not establish formal V&V, safety, security, compliance, or release authorization.
