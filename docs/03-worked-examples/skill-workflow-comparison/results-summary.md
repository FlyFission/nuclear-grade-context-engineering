# Results Summary

> *Author-judged qualitative 1-5 scores. See `methodology.md` for limits. No independent reviewer panel. No timing, defect-rate, or A/B measurement. The "overhead" column is judgment, not minutes. For the reproducible, mechanical layer that checks each artifact still surfaces its claimed decision signals, see [`efficacy-harness.md`](efficacy-harness.md) (`python tools/ng.py eval .`). Replication from the public trial records is invited.*

## Aggregate Score Table

| Use case | Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---|:---:|:---:|:---:|:---:|:---:|
| U01 Tiny README fix | Simple prompt | 4 | 2 | 3 | 3 | 1 |
| U01 Tiny README fix | Nuclear-grade | 4 | 3 | 4 | 3 | 2 |
| U02 Agent workspace boundary | Simple prompt | 3 | 2 | 2 | 2 | 1 |
| U02 Agent workspace boundary | Nuclear-grade | 5 | 5 | 5 | 4 | 4 |
| U03 Dependency security update | Simple prompt | 3 | 2 | 2 | 2 | 1 |
| U03 Dependency security update | Nuclear-grade | 5 | 4 | 4 | 5 | 4 |
| U04 Public assurance wording | Simple prompt | 3 | 1 | 2 | 2 | 1 |
| U04 Public assurance wording | Nuclear-grade | 5 | 5 | 4 | 4 | 3 |
| U05 Prompt/model baseline | Simple prompt | 2 | 2 | 2 | 2 | 1 |
| U05 Prompt/model baseline | Nuclear-grade | 5 | 5 | 4 | 5 | 4 |
| U06 Validator agent handoff | Simple prompt | 3 | 2 | 3 | 3 | 1 |
| U06 Validator agent handoff | Nuclear-grade | 4 | 4 | 4 | 4 | 3 |
| U07 Payment webhook idempotency | Simple prompt | 3 | 2 | 3 | 2 | 1 |
| U07 Payment webhook idempotency | Nuclear-grade | 5 | 5 | 5 | 5 | 4 |
| U08 Data retention migration | Simple prompt | 2 | 2 | 2 | 1 | 1 |
| U08 Data retention migration | Nuclear-grade | 5 | 5 | 4 | 5 | 5 |
| U09 Release readiness cut | Simple prompt | 3 | 2 | 3 | 2 | 1 |
| U09 Release readiness cut | Nuclear-grade | 5 | 4 | 4 | 5 | 3 |
| U10 Incident regression fix | Simple prompt | 3 | 2 | 3 | 2 | 1 |
| U10 Incident regression fix | Nuclear-grade | 4 | 4 | 4 | 4 | 3 |
| U11 External API tool permission | Simple prompt | 2 | 2 | 2 | 1 | 1 |
| U11 External API tool permission | Nuclear-grade | 5 | 5 | 5 | 5 | 4 |
| U12 Source citation adoption doc | Simple prompt | 3 | 1 | 2 | 2 | 1 |
| U12 Source citation adoption doc | Nuclear-grade | 5 | 5 | 4 | 4 | 3 |

## Skill Coverage

*This table maps each skill to the use cases it applies to. Skills added after the original U01-U12 trials (for example `staying-on-mission` and `reviewing-code-quality`) are mapped retroactively to the use cases where they apply; they were not run as separate trials.*

| Skill | Trial records |
|---|---|
| `questioning-attitude` | U02, U03, U04, U05, U06, U07, U08, U09, U10, U11, U12 |
| `using-nuclear-grade` | U01, U02, U03, U04, U05, U06, U07, U08, U09, U10, U11, U12 |
| `choosing-what-to-control` | U02, U03, U05, U07, U08, U09, U11 |
| `checking-what-a-change-affects` | U02, U03, U04, U05, U07, U08, U09, U10, U12 |
| `recording-a-known-good-version` | U03, U05, U08, U09, U11 |
| `rating-change-risk` | U01, U02, U03, U04, U05, U06, U07, U08, U09, U10, U11, U12 |
| `creating-change-records` | U01, U02, U03, U04, U06, U07, U08, U09, U10, U11, U12 |
| `briefing-an-agent` | U02, U06, U07, U10, U11 |
| `handing-off-work` | U06, U09, U10, U11 |
| `double-checking-before-acting` | U04, U07, U08, U11 |
| `proving-claims` | U01, U02, U03, U05, U06, U07, U08, U09, U10, U11 |
| `checking-release-readiness` | U02, U03, U05, U07, U08, U09, U11 |
| `learning-from-experience` | U06, U09, U10, U12 |
| `vetting-outside-code-and-models` | U03, U05, U07, U11 |
| `checking-source-claims` | U04, U05, U12 |
| `checking-legal-and-safety-wording` | U04, U05, U12 |
| `staying-on-mission` | U05, U08, U09, U11 |
| `reviewing-code-quality` | U02, U07, U08 |
| `stress-testing-agent-changes` | (new skill; applies conceptually to U02, U11; formal trial records pending) |
| `recording-what-an-agent-did` | (new skill; applies conceptually to U02, U06, U11; formal trial records pending) |
| `breaking-down-the-work` | (new skill; applies conceptually to U02, U08; formal trial records pending) |
| `organizing-project-folders` | (new skill; applies conceptually to U02, U06; formal trial records pending) |
| `closing-stale-packets` | (new skill; applies conceptually to U09, U10; formal trial records pending) |
| `deciding-who-decides` | (new skill; applies conceptually to U02, U06, U11; formal trial records pending) |
| `declaring-intent` | (new skill; applies conceptually to U07, U09, U11; formal trial records pending) |
| `responding-to-incidents` | (new skill; applies conceptually to U07, U10; formal trial records pending) |
| `tracking-deficiencies` | (new skill; applies conceptually to U03, U10; formal trial records pending) |
| `reporting-shared-defects` | (new skill; applies conceptually to U03, U10; formal trial records pending) |

## Workflow Coverage

| Workflow | Trial records |
|---|---|
| Questioning attitude | U02, U03, U04, U05, U06, U07, U08, U09, U10, U11, U12 |
| Quick change | U01, U06, U10 |
| Standard change | U02, U03, U04, U06, U07, U08, U09, U10, U11, U12 |
| Controlled configuration | U02, U03, U05, U07, U08, U09, U11 |
| Agent authority change | U02, U06, U07, U11 |
| Agent turnover | U06, U09, U10, U11 |
| Critical action self-check | U04, U07, U08, U11 |
| Release readiness | U02, U03, U05, U07, U08, U09, U11 |
| OPEX learning | U06, U09, U10, U12 |
| Trust check | U03, U05, U07, U11 |
| Source/legal check | U04, U05, U12 |

## Findings

1. **Simple prompting is enough for U01-like work.** If the change is local, reversible, easy to inspect, and has no trust-bearing claim, Quick mode adds only a light audit trail. Standard mode would be waste.
2. **The Nuclear-grade artifacts exposed more authority-boundary signals.** In U02, U06, U07, and U11, the structured path made allowed actions, forbidden actions, evidence obligations, and stop conditions visible where the simple-prompt artifact did not.
3. **The Nuclear-grade artifacts exposed more evidence-to-decision signals.** In U03, U07, U08, and U09, the structured path separated a passing test from the broader dependency, deletion, payment, and release decision. This is an author-scored artifact observation, not a measured reviewer benefit.
4. **Source/legal checks are launch-critical in the inspected artifacts.** In the author-constructed U04 and U12 pair, the simple-prompt artifacts used more confident public wording, while the Nuclear-grade artifacts narrowed claims to influence, lineage, and evidence. This does not establish a general tendency.
5. **Baselines matter most for drift-prone artifacts.** U05, U08, U09, and U11 show the value of naming accepted state and revalidation triggers for prompts, models, data policies, release artifacts, API permissions, and credentials.
6. **HPI microtools add value at transfer and critical action points.** U06, U09, U10, and U11 show that turnover prevents lost state; U04, U07, U08, and U11 show that self-checking is useful before public claims, irreversible data work, payment paths, and API permissions.
7. **The cost is real.** Nuclear-grade should be framed as consequence-scaled. It is not a universal replacement for good direct prompting.

## Formative score pattern by rigor tier

The per-trial scores record how the author judged the constructed artifacts. Read across the tiers,
they show where the design inspection found additional seeded signals and where it found added
ceremony. This table introduces no new measurement. It is author-judged, has no blinded A/B review,
and treats overhead as judgment rather than elapsed time.

| Rigor tier | Typical change | Hidden-risk discovery (simple → NG) | Defensible ship-call (simple → NG) | Overhead | Read the tier off |
|---|---|:---:|:---:|:---:|---|
| Administrative floor | typo, comment, dead link — no new trust boundary | n/a (no boundary to miss) | n/a | ~0 | (below Quick; commit message is the record) |
| Quick | local, reversible, obvious proof | 2 → 3 | 3 → 3 | 1–2 | U01 (the one pure-Quick trial) |
| Standard | touches users / deps / data / permissions / AI authority / release | 1–2 → 4–5 | 1–2 → 4–5 | 3–4 | U02, U03, U05, U07, U08, U11, U12 |
| Stronger (human-reviewed) | severe, silent, irreversible, external-trust | 1–2 → 5 + independent review | 1–2 → 5 | 4–5 | U04, U08 (upper band) |

The author-scored pattern suggests that the additional structure is concentrated where consequence
is, while also imposing more ceremony. On the Quick trial the two constructed paths scored similarly;
on Standard-and-above the structured artifacts exposed more seeded hidden-risk signals. Whether real
reviewers detect more defects or make better-calibrated decisions remains untested.

As **illustrative external evidence** for the same "reliability rises with rigor, and so does token
cost" shape, the NeoLabHQ context-engineering-kit publishes success-rate-by-scope tiers (basic
prompt vs. reflexion vs. plan-then-implement), reporting large reliability gains at 5–20× token cost
for its heaviest tier. Those are that project's numbers on its own tasks, cited here for the shape
of the trade-off — they are **not** restated as Nuclear-grade results. See
[`../../00-standards-foundation/source-map.md`](../../00-standards-foundation/source-map.md) (Tier 11).

## Repo Implications

- Keep Quick mode highly visible and legitimate.
- Add future worked examples for dependency upgrades, prompt/model baselines, API tool permissions, and release readiness.
- Keep "Questioning attitude" as the public hook, but immediately route to concrete artifacts.
- Improve examples that show `gap`, `deferred`, and `block` as successful workflow outcomes.
- Add one-screen context-pack, turnover, self-check, OPEX, and trust-check examples for agent handoff and critical-action scenarios.

## Boundary Note

These results summarize qualitative artifact trials. They do not prove safety, security, compliance, certification, production suitability, or formal assurance.

## Source-Lineage Note

This summary is an authored Nuclear-grade adoption artifact using the repo operating model and public-source lineage summarized in `docs/00-standards-foundation/source-map.md`.
