```text
Build a Nuclear-grade context pack for this work.

Inputs:
- packet: .nuclear/changes/<slug>/
- governing request: <direct source or exact quote>
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
- effective instruction state: <files/rules observed at the latest model or action boundary, with scope, precedence, and load result; otherwise "not observed">

Return a short context pack. Include the mode, the governing request's direct source or exact quote, the decision question, the goal, the work phase, the archetype the brief places the agent in and its characteristic drift, a risk summary, a basis summary, the evidence required, the effective instruction state and which source wins on conflict, the limits on what the agent may do, the claims it must not make, the open gaps, the last action completed, what has changed, the critical next action, and the next action. Treat summaries as context, not permission. Use a host load event or log when available; otherwise mark instruction state `not observed` rather than inferring it from file presence. If responsibility is changing hands rather than starting fresh, use the `handing-off-work` prompt instead.
```
