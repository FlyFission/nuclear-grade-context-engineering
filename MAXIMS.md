# Maxims

The principles people quote when they explain why this works. Most of these are stated in
longer form elsewhere in the repository; this page is the short, share-friendly version.

---

> **Go fast while you are exploring. Slow down the moment the work becomes a promise.**

Cheap iteration earns the right to spend time on careful evidence. Reverse the order and you
get neither speed nor confidence. *(See [`README.md`](README.md) — "The one idea.")*

---

> **The name is the standard, not the vocabulary.**

"Nuclear-grade" names the *standard of care*. When you adopt the discipline, you do not have
to adopt the word. If the branding would mis-calibrate your team, rename the local copy. The
habits travel; the label does not need to. *(See [`README.md`](README.md) and
[`DISCLAIMER.md`](DISCLAIMER.md).)*

---

> **A guard inside the agent's writable set is not enforcement — it is a suggestion the agent
> can edit.**

If an agent has write authority over the tests, prompts, CI scripts, or approval policy that
decide whether its work is acceptable, the agent can satisfy the check by changing the check.
Move the gate out of the agent's writable working set. *(See
[`docs/04-adoption/agent-authority-model.md`](docs/04-adoption/agent-authority-model.md) —
"Self-modification boundary.")*

---

> **Human judgment decides engineering adequacy; the validator checks whether the packet
> exposes the evidence needed for that judgment.**

The structural checker is a lint, not a verdict. It says the evidence is reachable; it does
not say the evidence is correct. The judgment is a human's, supported by
[`proving-claims`](skills/proving-claims/SKILL.md) and
[`checking-release-readiness`](skills/checking-release-readiness/SKILL.md). *(See
[`docs/02-operating-system/validators.md`](docs/02-operating-system/validators.md).)*

---

> **The agent drafts; the human approves.**

The intended loop is *user prompt → agent drafts the change record → human edits and approves
→ agent writes code → human reviews*. The human is editor and approver, not typist. Filling
empty templates by hand is what makes packets feel like a tax. *(See [`CORE.md`](CORE.md) —
"The agent-drafts-spec workflow.")*

---

> **For an unattended agent there is no one to ask. "Ask first" degrades to stop, record the
> needed approval, and halt.**

Prose that prompts for permission only works when someone is reading. In an unattended
subagent run, design the gate as block / escalate / record, not as a request for input that
nothing will answer. *(See
[`docs/04-adoption/agent-authority-model.md`](docs/04-adoption/agent-authority-model.md) —
"Denial rule.")*

---

> **CI passing is not a release decision.**

A green pipeline says the checks that exist did not fail. A release decision says ship, block,
defer, or ship-with-named-risk — and names the residual risk, the rollback, the monitoring,
and the baseline trigger. *(See
[`skills/checking-release-readiness/SKILL.md`](skills/checking-release-readiness/SKILL.md).)*

---

> **Every surprise updates a control.**

A near miss, an escaped bug, a bad handoff, an agent mistake — each should change a test, a
template, a prompt, a monitor, a checker, or a baseline. Lessons that do not change a control
disappear. *(See [`skills/learning-from-experience/SKILL.md`](skills/learning-from-experience/SKILL.md).)*

---

## Source-lineage note

These maxims summarize patterns from the wider Nuclear-grade repository. They do not create
assurance or certification — see [`DISCLAIMER.md`](DISCLAIMER.md) for the boundary discipline
they sit inside.
