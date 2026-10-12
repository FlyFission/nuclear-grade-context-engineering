# Risk — Blocking PreToolUse gate (opt-in)

## Selected mode

- **Mode:** Standard
- **Why:** The brief asked for a Quick packet and to check whether Standard is warranted. It is. The hook is executable code that changes what an agent may do (it can deny and ask), and it guards the trust surfaces of the gate itself. CORE.md routes "what a tool or agent may do" to Standard+. The [`dispatcher-hooks`](../dispatcher-hooks/risk.md) precedent already rated two advisory, opt-in hooks Standard, and a blocking hook carries more consequence. Quick would understate it.

## Decision

Ship follow-up F-01 from [`../adr-governance-benchmark/basis.md`](../adr-governance-benchmark/basis.md): an opt-in `PreToolUse` gate that decides on structured facts only, fails closed, and never auto-allows. It stays opt-in. No `hooks/hooks.json` ships, so installing the plugin does not turn it on.

Main failure modes and controls:

- **The gate auto-allows and widens authority.** Control: there is no `allow` code path, and an AST test bans an `allow` literal. A sweep test over 960 inputs sees only `deny`, `ask`, or no output.
- **Bad input passes silently.** Control: malformed JSON, missing fields, a missing path, a relative-only cwd, an invalid policy file, or an internal exception each return `ask` (tested).
- **An editable policy weakens the gate.** Control: the policy file has additive keys only, the defaults are constants, and agent writes to the policy file are denied (tested).
- **The hook becomes an exfiltration or execution surface.** Control: an AST test limits imports to `json`/`os`/`re`/`sys`, limits `os` to read-only path helpers, requires a read-only `open`, and bans `exec`/`eval`/`compile`/`__import__`. The existing banned-substring network scan also covers the new file.
- **Readers mistake it for a sandbox.** Control: HOOKS.md says shell matching is defeatable, calls the gate rung 2/3, and keeps out-of-band CI as the real gate.
- **False positives annoy adopters.** Accepted. `ask` only routes the call to the human prompt, and the gate is opt-in.

The release stance does not change. There is no version bump and no tag.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Each failure mode above has a named test, the full suite passes, and the gate stays opt-in.

## Source-lineage note

Original Nuclear-grade control. It applies the enforcement-rung and hold-point ideas in [`runtime-enforcement.md`](../../../docs/02-operating-system/runtime-enforcement.md), mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No security, compliance, or efficacy claim is made.
