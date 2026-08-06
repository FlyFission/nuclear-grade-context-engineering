```text
Build a Nuclear-grade context pack for this work.

Inputs:
- packet: .nuclear/changes/<slug>/
- role: <builder|reviewer|verifier|releaser|researcher>
- decision question: <one sentence>
- objective: <one paragraph>
- work phase: <explore|candidate|audit|accept>
- affected files: <list>
- last completed action:
- changed conditions:
- critical next action and likely error:
- allowed commands/tools: <list>
- forbidden actions: <list>
- do-not-touch targets: <list>
- approval gates: <list>
- required evidence: <commands/links/reviews>
- loaded instruction files: <AGENTS.md / CLAUDE.md / .github/copilot-instructions.md / tool rules in force, with precedence or "none known">

Return a short context pack. Include the mode, the decision question, the goal, the work phase, the archetype the brief places the agent in and its characteristic drift, a risk summary, a basis summary, the evidence required, the loaded instruction files in force and which one wins on conflict, the limits on what the agent may do, the claims it must not make, the open gaps, the last action completed, what has changed, the critical next action, and the next action. If responsibility is changing hands rather than starting fresh, use the `handing-off-work` prompt instead.
```
