# Eval cases

These cases are lightweight acceptance tests for the method, not a benchmark suite.
They show what a nuclear-grade answer must make visible in recurring agent-work
situations.

| Case | What it checks | Use it when |
| --- | --- | --- |
| `U02-agent-workspace-boundary` | Agent file-write authority is bounded, controlled items are named, adversarial proof claims are stated, and release wording avoids production-sandbox overclaiming. | A change gives an agent tool or filesystem authority. |
| `U04-public-assurance-wording` | Public claims separate source inspiration, license permission, assurance, self-checks, cross-document impact, and prohibited-claim scans. | Docs, marketing, README, or release notes could imply compliance, certification, formal QA, safety, security, or regulatory adequacy. |
| `U07-payment-webhook-idempotency` | Money-moving changes escalate mode, bound credentials/API access, prove duplicate/replay behavior, and name rollback, monitoring, and risk ownership. | An agent touches payments, billing state, ledgers, or similarly trust-bearing side effects. |

## Add or remove a case

Add a case only when it captures a recurring failure mode that a reviewer can score
from observable text. Remove or merge cases that become redundant with existing
signals. A useful case should name:

- the artifact and section to inspect;
- the specific signals a good answer must contain;
- the trust boundary, public claim, or decision risk it protects.

Keep the set small. If a case does not change review quality, it is clutter.
