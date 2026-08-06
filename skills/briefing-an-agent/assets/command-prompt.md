```text
Build a Nuclear-grade context pack for this work.

Inputs:
- packet: .nuclear/changes/<slug>/
- role: <builder|reviewer|verifier|releaser|researcher>
- decision question: <one sentence>
- objective: <one paragraph>
- work phase: <explore|candidate|audit|accept>
- targeted improvement cycle active: <yes|no>
- task / intended outcome: <required when active>
- build method and ownership: <independent slices, coupled sequential owner, integration owner>
- frozen inspectable bar: <requirements/reference/benchmark/test and threshold>
- bar custodian / change authority: <who may approve a variance>
- current largest consequential gap: <required when active>
- fresh artifact: <candidate digest and artifact the critic must inspect>
- critic coupling basis: <actor/context/mechanism/authority/resource>
- iteration bound: <rounds/time/tokens and terminal state>
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

Return a short context pack. Include the mode, the decision question, the goal, the work phase, the archetype the brief places the agent in and its characteristic drift, a risk summary, a basis summary, the evidence required, the loaded instruction files in force and which one wins on conflict, the limits on what the agent may do, the claims it must not make, the open gaps, the last action completed, what has changed, the critical next action, and the next action. When the targeted improvement cycle is active, include the Task, Build Method, frozen Bar, bar custodian, current largest gap, fresh artifact, five-axis critic coupling basis, integration owner, and bounded non-pass terminal state; a fresh critic is not automatically independent and supplies no release authority. If responsibility is changing hands rather than starting fresh, use the `handing-off-work` prompt instead.
```
