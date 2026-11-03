# Skill-merge coverage audit

Reviewer: read-only audit of 15 original skills (`skills/<name>/SKILL.md`) against 7 merged drafts
(`scratchpad/consolidation/drafts/<new-name>/SKILL.md`). Every capability of every original is listed,
including the two whose names survive (`double-checking-before-acting`, `learning-from-experience`).

Verdict key:
- **COVERED** — the draft keeps the rule (quoted phrase shows where).
- **PARTIAL** — kept but weakened; verdict says whether the weakening matters.
- **MISSING / LOSS-MATTERS** — an agent following the draft would now do the job worse or skip a needed step (example given).
- **MISSING / ACCEPTABLE-TRIM** — redundant, generic, or covered elsewhere in the repo (location named).

Method notes: every repo path the drafts cite was checked on disk (all exist; packet file names such as
`intent.md`, `deficiency.md`, `baseline.md`, `turnover.md` exist under `templates/golden-path/` or `templates/cm/`).
Every skill name the drafts cite was checked against the surviving set of 23
(31 − 15 originals + 7 drafts).

---

## Merge 1: double-checking-before-acting + declaring-intent -> drafts/double-checking-before-acting

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| DCBA | Contract claim: target, expected result, stop condition named before; real vs expected compared before claiming success | Contract: "target, expected result, and stop condition were named before the action and compared after it" | COVERED |
| DCBA | Failure class wrong-target-or-unverified-action | "wrong-target-or-unverified-action, or unfalsifiable-intent" | COVERED |
| DCBA | Output `self-check.md` (action, target, expected/real, stop, evidence, mismatch) | Outputs: "A self-check note or `self-check.md`: action, target, expected and real result, stop condition, evidence" | COVERED |
| DCBA | Next action: mismatch halts, not retry | "a mismatch halts the action rather than triggering a retry" | COVERED |
| DCBA | Trigger: delete/move/publish/release/migrate/outside-repo commands | When to Use 1 | COVERED |
| DCBA | Trigger: edits touching public claims, idea lineage, permissions, credentials, deps, models, APIs, release | When to Use 2 ("public claims, permissions, credentials, dependencies, models, APIs, or the release") — "where ideas came from" dropped | PARTIAL / ACCEPTABLE-TRIM (lineage covered by `checking-public-claims`) |
| DCBA | Trigger: wide or repeated change | When to Use 3 | COVERED |
| DCBA | Trigger: quick candidate becoming public claim, accepted version, or release action | MISSING (public claim/release in bullet 2; "accepted version" promotion moment gone) | ACCEPTABLE-TRIM (baseline promotion handled by `controlling-approved-versions` acceptance stage) |
| DCBA | When Not: tiny local edit | "A tiny local edit with obvious proof" | COVERED |
| DCBA | When Not: read-only action **that has no effect on any later decision** | "or an action that only reads data" — qualifier dropped | **LOSS-MATTERS** — a read-only prod query whose result selects the migration target is now exempted from naming/verifying the target |
| DCBA | When Not: record already requires stronger human check | "use `deciding-who-decides` to place it" | COVERED |
| DCBA | Inputs: current phase, packet | Prompt inputs drop "packet:" and "current phase:" | ACCEPTABLE-TRIM (authority source covers phase legitimacy; self-check.md lives in the packet) |
| DCBA | Process 1: stop at key moment, name action and target | Step 1 | COVERED |
| DCBA | Process 2: expected result, likely error | Step 2 | COVERED |
| DCBA | Process 3: act inside authority | Step 3 | COVERED |
| DCBA | Process 4: compare real vs expected before claim | Step 4 | COVERED |
| DCBA | Process 5: forceful independent backup for trust-bearing actions; same-context second pass not independent | Step 5 "A second pass by the same agent in the same context is not independent" | COVERED |
| DCBA | Process 6: record mismatch, no blind retry | Step 4 "Record any mismatch and pause; do not retry blindly" | COVERED |
| DCBA | Verification: target exact enough to rule out wrong file/env | Verification 1 | COVERED |
| DCBA | Escalation: pause if authority/target/result/evidence unclear | Escalation 1 | COVERED |
| DCBA | Escalation: halt regardless of seniority; surfacing protected | "Halting unsafe work is protected." ("regardless of seniority" dropped) | ACCEPTABLE-TRIM (AGENTS.md "Halt unsafe or unclear work") |
| DCBA | Escalation: **escalate when action affects credentials, network effects, data, releases, public trust, or anything irreversible** | MISSING — draft escalation only has unclear-pause, no-rollback stop, and second reviewer for irreversible | **LOSS-MATTERS** — a reversible staging deploy that uses a new API credential or touches user data gets a depth-1 self-check and proceeds with no human escalation. AGENTS.md authority boundaries partly cover this repo, but the skill ships to `starter-kit/` consumers without that file |
| DCBA | Rationalization "one command" | kept | COVERED |
| DCBA | Rationalization "target is obvious" | dropped | ACCEPTABLE-TRIM (Red flag "action starts before the target is named") |
| DCBA | Rationalization "check after" | kept | COVERED |
| DCBA | Red flags: target unnamed / vague result / retry on mismatch | Red flags 1–2 | COVERED |
| DCBA | Red flag: public wording claims safe/secure/approved/compliant without scoped evidence | MISSING | ACCEPTABLE-TRIM (owned by `checking-public-claims`; recommend a one-line pointer since public claims are a When-to-Use trigger) |
| DI | Contract claim: falsifying signal, concrete abort criteria, checked rollback, preconditions proven | Contract + steps 7–9 ("Prove the preconditions rather than assert them") | COVERED |
| DI | Failure class unfalsifiable-intent | Contract | COVERED |
| DI | Output `intent.md` (action, reasoning, expected, abort, rollback, decision rights, backup) | Outputs: "At depth 2, an `intent.md`" | COVERED |
| DI | Trigger: before deploy, migration, data change, public claim, dependency/model swap, release | Depth-2 gate is only "Irreversible, or a reviewer must be able to stop it" | **LOSS-MATTERS** (see next row) |
| DI | Trigger: **hard to reverse, or blast radius beyond the immediate file** | Narrowed to "Irreversible" | **LOSS-MATTERS** — a model swap or deploy that is technically rollback-able but has fleet-wide blast radius no longer gets a declared intent, falsifying signal, or numeric abort criteria |
| DI | Trigger: want reviewer eyes on reasoning before execution | "a reviewer must be able to stop it" | COVERED |
| DI | Trigger: standing authority "no" window | When to Use 4 | COVERED |
| DI | When Not: routine reversible edit | When Not 1 / description | COVERED |
| DI | When Not: live incident -> stabilization | "use `responding-to-incidents`" | COVERED |
| DI | When Not: declaration treated as guarantee | Overview "never evidence that the agent understood"; prompt "not proof of understanding" | COVERED |
| DI | Process 1: "I intend to <action> on <target> because <evidence>" | Step 6 | COVERED |
| DI | Process 2: falsifying signals | Step 7 | COVERED |
| DI | Process 3: abort criteria in numbers, verified rollback | Step 8 | COVERED |
| DI | Process 4: who may stop, by when, backup watcher | Step 9 | COVERED |
| DI | Process 5: preconditions proven not assumed | Step 9 | COVERED |
| DI | Process 6: act after review window; record actual vs expected | Step 9 + Step 4 | COVERED |
| DI | Output: mismatch routed to pause/incident/deficiency | Outputs 3 (`responding-to-incidents`, `learning-from-experience`) | COVERED |
| DI | Escalation: preconditions cannot be shown | Escalation 1 ("evidence is unclear") | COVERED |
| DI | Escalation: stop when no rollback / unmeasurable abort | Escalation 2 | COVERED |
| DI | Escalation: second reviewer when irreversible and one person saw reasoning | Escalation 3 | COVERED |
| DI | Rationalization: declared = cleared | kept | COVERED |
| DI | Rationalization: confident intent ≠ understanding | Overview + prompt | COVERED |
| DI | Rationalization: rollback probably fine | kept | COVERED |
| DI | Rationalization: abort criteria obvious | Verification "concrete" | COVERED |
| DI | Red flags: no falsifying signal, asserted preconditions, zero review window, reviewer never saw reasoning | Red flags 3–4 | COVERED |

### Over-application risks

- None found where a gated step now reads as mandatory. Depth 2 is clearly gated.
- **Sequencing risk (under-application):** depth-2 steps are numbered 6–9 *after* step 3 ("Act only inside the authority") and step 4 (compare after acting), with only the heading text "before step 3" placing them earlier. An agent reading numbered steps in order would act at step 3 and then write the intent. Renumber or move the depth-2 block above step 3.

### Broken references

None. `responding-to-incidents`, `deciding-who-decides`, `learning-from-experience` all survive; `docs/00-standards-foundation/source-map.md` and `do-not-cite-directly.md` exist.

**Summary: COVERAGE FAIL (3 LOSS-MATTERS: credential/data/release escalation trigger; depth-2 gate narrowed from "hard to reverse or wide blast radius" to "irreversible"; read-only exemption lost its "no effect on a later decision" qualifier).**

---

## Merge 2: learning-from-experience + tracking-deficiencies + reporting-shared-defects -> drafts/learning-from-experience

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| LFE | Contract: actual-vs-standard, root cause, weak control, owned verified fix or deliberate waiver | Contract "a lesson with an owned, verified control fix or a reasoned waiver"; steps 1, 3–5 | COVERED |
| LFE | Failure class unlearned-lesson | Contract | COVERED |
| LFE | No-blame for honest error, not willful violation; bypassable gate is its own weak control | Overview "Surface that as a finding and fix the gate that allowed it" | COVERED ("keep an owner for closure" dropped — ACCEPTABLE-TRIM, owners required on every path) |
| LFE | Trigger list: bad handoff, wrong-file edit, made-up claim, overreach, escaped bug, review surprise | When to Use 1 | COVERED |
| LFE | Trigger: users/operators misread a release, public claim, runbook, template, approved version | "or misread release" only | ACCEPTABLE-TRIM (covered by "something went wrong" in description) |
| LFE | Trigger: a change record, skill, command, test, checker, monitor, or template failed to steer behavior | MISSING as explicit trigger | ACCEPTABLE-TRIM (description "something went wrong", Overview "operating signal") |
| LFE | Trigger: rules/sources change produced new text but no control change | MISSING | ACCEPTABLE-TRIM (`checking-what-a-change-affects` When to Use: "Public claims, where ideas came from, checkers ... may need updates") |
| LFE | When Not: no repeatable lesson | When Not 2 | COVERED |
| LFE | When Not: live incident | When Not 1 | COVERED |
| LFE | When Not: blame request | When Not 3 | COVERED |
| LFE | Inputs: chance it happens again | dropped | ACCEPTABLE-TRIM |
| LFE | Process 1: actual vs standard, honest vs willful | Step 1 | COVERED |
| LFE | Process 2: root cause, weak control, which approved version/file | Step 3 | COVERED |
| LFE | Process 3: pick lasting fix type | Step 4 | COVERED |
| LFE | Process 4: regret is not a fix | Step 4 | COVERED |
| LFE | Process 5: owner + verify or deliberate close | Step 5 | COVERED |
| LFE | Process 6: feed lesson into questioning/planning/verification/handoffs | "feed the lesson into future questioning, planning, and handoffs" | COVERED |
| LFE | Output: OPEX record or issue entry | Outputs 1 | COVERED |
| LFE | Output: **trigger to re-verify or re-record the approved version when a controlled item changed** | MISSING | **LOSS-MATTERS** — an OPEX fix tightens a checker/template that is in a recorded baseline; the draft closes the lesson with "owner and verify" and the baseline silently goes stale. `controlling-approved-versions` step 7 lists re-check triggers only for "a dependency, model, prompt, tool, or public-claim change" (not checker/template), and `docs/02-operating-system/rebaseline.md` names OPEX as a trigger but the draft never routes there |
| LFE | Verification: future agents can find the lesson | Red flag "a lesson stuck in chat" | COVERED |
| LFE | Escalation: users, data, security, credentials, releases, public claims, repeated agent power | Escalation 1 | COVERED |
| LFE | Escalation: outward duty for shared artifacts | Shared-defect path | COVERED |
| LFE | Escalation: second independent reviewer on repeated weak control | Escalation 2 | COVERED |
| LFE | Rationalizations: "just a mistake", "we fixed the bug", "no-blame ≠ accountability" | kept | COVERED |
| LFE | Rationalization: "No one was harmed" — near miss is a cheaper warning | dropped | ACCEPTABLE-TRIM (near miss named in description/Overview/prompt) |
| LFE | Red flags: no fix/reason; stuck in chat; blames one person/model; willful bypass filed as mistake; no owner/trigger | Red flags 1, 4; contract "assign owners and recheck triggers" | COVERED |
| TD | Contract: first-seen age, owner, fix-by date or formal risk-acceptance with owner + revisit trigger | Contract + steps 6–7 | COVERED |
| TD | Failure class normalized-deviation | Contract | COVERED |
| TD | Output `deficiency.md` row (description, age, owner, disposition, trigger), linked | Outputs 2 | COVERED |
| TD | Trigger: known problem outlives change (flaky test, noisy alert, unowned service, dead dashboard, recurring incident, deferred hardening) | When to Use 2 (recurring incident folded into escalation) | COVERED |
| TD | Trigger: review/incident surfaced something not being fixed now | Prompt "is a problem being left in place for now?" | COVERED |
| TD | When Not: lesson already closed in packet | Step 2 "only those" | COVERED |
| TD | When Not: brand-new work — rate as normal change | dropped | ACCEPTABLE-TRIM (description is post-event; `rating-change-risk` owns new work) |
| TD | When Not: active incident | When Not 1 | COVERED |
| TD | Process 1–5: one line + link, first seen, owner (unowned is finding), disposition, review trigger | Steps 6–7 | COVERED |
| TD | Process 6: link related incident/OPEX/controlled items | "Then link the records to each other" | COVERED |
| TD | Verification: age visible so old accepted risks resurface | Outputs "age"; step 7 revisit trigger | COVERED |
| TD | Escalation: **safety, security, data integrity, or a protected outcome** | Draft list: users, data, security, credentials, releases, public claims, agent power — "safety" and "protected outcome" gone | **LOSS-MATTERS** — a flaky latency test guarding a protected outcome named in `basis.md` can be risk-accepted by the agent with an owner and date but no escalation |
| TD | Escalation: shared-artifact deficiency outward duty | Shared-defect path | COVERED |
| TD | Escalation: stop normalizing on repeat incidents | Escalation 3 | COVERED |
| TD | Escalation: decision owner when no one accepts or funds | "Report upward when no one will own a fix, an acceptance, or a notice" | COVERED |
| TD | Rationalizations: everyone knows | kept | COVERED |
| TD | Rationalizations: "been like that for ages" (age argues for action); "fix eventually"; "just a flaky test" (noise trains people to ignore signal) | dropped | ACCEPTABLE-TRIM (owner/date/trigger rules enforce the same; overview "must not quietly become normal") |
| TD | Red flags: chat/memory; no owner/date/trigger; repeat incidents; standards lowered to match | Red flag 2; escalation 3 | COVERED ("standards lowered" ACCEPTABLE-TRIM — `deficiency-register.md`) |
| RSD | Contract: evaluated for downstream impact; notified with owner + tracking link, or not-reportable with reason | Contract + steps 8–9 | COVERED |
| RSD | Failure class silent-local-fix | Contract | COVERED |
| RSD | Output shared-defect report (description, consumers, severity, notice to whom/when, owner, link) | Outputs 3 | COVERED |
| RSD | Trigger: defect in shared prompt/skill/command/template/dep pin/model/eval/config | When to Use 3 ("command" dropped) | COVERED |
| RSD | Trigger: local fix leaves others exposed | Step 9 | COVERED |
| RSD | Trigger: incident/OPEX traced to shared artifact | Triage step 2 | COVERED |
| RSD | When Not: local defect; live incident; no consumers foreseeable | When Not 1–2; step 9 "record why it is not reportable" | COVERED |
| RSD | Process 1–2: confirm shared; evaluate who consumes and how it fails | Step 8 | COVERED |
| RSD | Process 3: local fix and outward notice are separate obligations | Step 9 "Fix your copy and, separately, notify" | COVERED |
| RSD | Process 4: notify with severity and fix/workaround; owner + tracking link | Step 9 | COVERED |
| RSD | Process 5: tie report to OPEX record and deficiency register | "link the records to each other" — but triage "only those" paths means a notice can exist with no OPEX/deficiency record | ACCEPTABLE-TRIM (notice carries owner + tracking link, so it does not vanish) |
| RSD | Process 6: not-reportable recorded with reason | Step 9 | COVERED |
| RSD | Verification: not-reportable records reason **and who decided** | "or record why it is not reportable" — decider dropped | **LOSS-MATTERS** — the agent can self-decide "consumers override this pin, not reportable" with no named decider for anyone to challenge |
| RSD | Escalation: security, credentials, data integrity, privacy, public release | Escalation 1 (privacy → "users, data") | COVERED |
| RSD | Escalation: qualified/independent reviewer when consumers external **or defect could cause a substantial downstream failure** | "or a shared defect reaches external consumers" — substantial-failure clause gone | **LOSS-MATTERS** — a shared eval harness that silently passes every internal team's tests is internal-only, so no independent reviewer is required |
| RSD | Escalation: stop and report upward when no one owns notice | Escalation 3 | COVERED |
| RSD | Rationalizations: "fixed in my repo"; "they'll pull eventually"; "probably fine for others" | "your fix does not reach other consumers"; record not-reportable reason | COVERED |
| RSD | Red flags: no notice; no named consumers/owner/link; known issue in chat | Red flags 3; Verification 3 | COVERED |

### Over-application risks

- **Escalation list from LFE now governs deficiencies:** "Escalate when the event touched users, data, security, credentials, releases, public claims, or repeated agent power." Under the original `tracking-deficiencies`, a flaky test in release CI or a noisy alert on a user-facing service was logged and dispositioned locally. Under the draft every such deficiency "touched releases/users" and escalates.
- **Discoverability narrowing (soft):** the description opens "After something went wrong or nearly did", but deficiencies are often found with no triggering event (`docs/02-operating-system/deficiency-register.md` explicitly calls OPEX event-driven and the register standing). The examples in the description ("flaky test, noisy alert, unowned service") reduce but do not remove the risk that a trigger-based loader skips it.

### Broken references

None in the draft (`responding-to-incidents` survives; `source-map.md` exists).

**Summary: COVERAGE FAIL (4 LOSS-MATTERS: re-baseline trigger output; deficiency escalation for safety/protected outcomes; not-reportable "who decided"; independent reviewer for substantial internal downstream failure).**

---

## Merge 3: checking-legal-and-safety-wording + checking-source-claims -> drafts/checking-public-claims

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| CLSW | Contract: "may use" vs "proven fit"; banned phrases only in negative/disclaimer; `doctor` passes | Contract + step 7 | COVERED |
| CLSW | Failure class assurance-overreach | Contract | COVERED |
| CLSW | Artifacts: LICENSE, DISCLAIMER, SECURITY, compliance-boundaries | Inputs | COVERED |
| CLSW | Trigger: README, install/public docs, templates, skills, commands, examples, release notes | When to Use 1 | COVERED |
| CLSW | Trigger: source families, assurance wording, enterprise rollout wording | When to Use 2–4 | COVERED |
| CLSW | Trigger: getting repo ready to be public | When to Use 4 | COVERED |
| CLSW | Trigger: public claim needs self-check, or a line pointing hard claims to qualified outside review | Step 3 checks claims vs evidence; escalation to qualified professionals | COVERED |
| CLSW | When Not: private detail; legal advice -> lawyer | When Not 1, 3 | COVERED |
| CLSW | Inputs: checker's starting list of banned phrases | dropped | ACCEPTABLE-TRIM (`python tools/ng.py doctor .` in step 7 carries the list) |
| CLSW | Process 1–2: MIT still; may-use vs proven-fit | Step 2 | COVERED |
| CLSW | Process 3: self-check claim vs evidence **and a qualified authority** | Step 3 (evidence only) | ACCEPTABLE-TRIM (Escalation 2 sends project-specific claims to qualified professionals) |
| CLSW | Process 4: "this does not create..." near onboarding, templates, commands, CLI help | Step 4 | COVERED |
| CLSW | Process 5: evidence-tied wording | Step 4 | COVERED |
| CLSW | Process 6: scan for banned phrases and leftover internal text | Step 7 | COVERED |
| CLSW | Outputs: bounded wording, updated docs, scan results/gaps | Outputs | COVERED |
| CLSW | Verification 1–3 | Verification 1–2, step 7 | COVERED |
| CLSW | Escalation: stop on legal advice / regulated use / purchasing fitness / customer assurance beyond repo | Escalation 1 ("customer assurance beyond the repo" dropped) | ACCEPTABLE-TRIM (Escalation 2 "customer ... trust") |
| CLSW | Escalation: qualified legal/compliance/security/safety for project-specific claims | Escalation 2 | COVERED |
| CLSW | Rationalizations: MIT; disclaimers in one file | kept | COVERED |
| CLSW | Rationalization: **"Enterprise-grade means certified." Here it means testable, easy to navigate, and reviewable** | MISSING (draft lists "enterprise-grade" as an assurance word but gives no in-repo meaning) | **LOSS-MATTERS** — this is the only place in the repo defining the term (`docs/00-standards-foundation/core-source-rationale.md:189` uses it undefined); an agent editing rollout copy will strip or negate "enterprise-grade" instead of rewording it to the repo's defined meaning |
| CLSW | Red flags: promises safe/secure/compliant; CLI help lacks boundary wording; examples imply more proof | Red flags 1, 4; step 4 "command help" | COVERED |
| CSC | Contract: every source public, mapped or "public URL needed", influence not compliance | Contract | COVERED |
| CSC | Failure class overstated-lineage | Contract | COVERED |
| CSC | Decision tier **warn** | Draft tier **block** | See over-application |
| CSC | Trigger: doc, template, skill, command, **or change record** cites a source family | When to Use 1/3 and description list public docs, READMEs, templates, release copy; change records dropped | **LOSS-MATTERS** — a Standard packet's `basis.md` saying "meets DOE-HDBK-1028" is committed to the public repo, but the loader-facing description no longer covers change records, and When-Not "Private code or notes" invites skipping it |
| CSC | Trigger: new standards/frameworks/agencies/assurance terms | When to Use 2–3 | COVERED |
| CSC | Trigger: public claim might sound like compliance/certification | When to Use 2 | COVERED |
| CSC | Trigger: dependency/model/API/vendor claim confused with local proof | Step 6 "vendor claim" classification | COVERED |
| CSC | When Not: private code | When Not 1 | COVERED |
| CSC | When Not: non-public source -> private project-specific controls outside the repo | Escalation 1 stop on private source; alternative route dropped | ACCEPTABLE-TRIM |
| CSC | When Not: truth of a fact -> `checking-facts` | When Not 2, Overview, prompt | COVERED |
| CSC | Inputs: source-map, crosswalk, compliance-boundaries | Inputs | COVERED |
| CSC | Process 1–6 (find, confirm public, classify, downgrade, reword, remove/negate) | Steps 1, 5, 6 | COVERED |
| CSC | Outputs: source-map/crosswalk rows; narrowed wording | Outputs 1–2 | COVERED |
| CSC | Output: a clear source-lineage note | MISSING | ACCEPTABLE-TRIM (`nuclear_grade/ng_validate.py` `_check_source_lineage` and `tools/ng_skill_audit.py` enforce it for packets and skills) |
| CSC | Verification: points to source-map; no unconfirmed direct lineage; boundary phrases only negative | Verification 2–3 | COVERED |
| CSC | Escalation: stop on non-public/proprietary/unverified source | Escalation 1 | COVERED |
| CSC | Escalation: regulated/purchasing/customer/investor trust | Escalation 2 | COVERED |
| CSC | Rationalizations: hostile reader; only an influence; source probably exists | Overview; kept | COVERED |
| CSC | Red flags: no URL/status; "compliant" outside negative; repeated source details | Red flags 2–3; step 6 "Link to the source map" | COVERED |
| CSC | Prompt statuses verified-public / supporting-context / public-url-needed / excluded-direct | Prompt | COVERED |

### Over-application risks

- **Lineage findings promoted from warn to block:** the original `checking-source-claims` tier was "warn"; the draft says "**Decision affected:** block -- whether the public text ships; an overreaching assurance or lineage claim blocks until reworded." A source row marked "public URL needed", which the original accepted as an honest interim status, now reads as ship-blocking.
- Step 7 (`doctor`) now runs on lineage-only checks. Harmless, since CSC already asked for validation and scan commands.

### Broken references

None. `checking-facts` survives; all doc paths exist.

**Summary: COVERAGE FAIL (2 LOSS-MATTERS: in-repo meaning of "enterprise-grade"; change records dropped from lineage-check scope).**

---

## Merge 4: recording-a-known-good-version + choosing-what-to-control -> drafts/controlling-approved-versions

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| RKGV | Contract: rebuildable from commit/PR/release; scope included/excluded; residual risks owned; re-record triggers | Contract 2nd clause; steps 4–7 | COVERED |
| RKGV | Failure class unrebuildable-baseline | Contract | COVERED |
| RKGV | Output `baseline.md` or known-good section in `ship.md` | Outputs 2 | COVERED |
| RKGV | Trigger: Standard change ships | When to Use "Accepting" | COVERED |
| RKGV | Trigger: public-facing workflow state changes | dropped | ACCEPTABLE-TRIM (covered by "a controlled item is accepted") |
| RKGV | Trigger: controlled prompts/models/tools/deps/docs/... accepted | "a controlled item is accepted" | COVERED |
| RKGV | Trigger: lesson or review feedback forces re-record; near miss changes accepted state **or its re-check trigger** | "a lesson forces a re-record" | COVERED (re-check-trigger nuance ACCEPTABLE-TRIM) |
| RKGV | When Not: tiny local edit; still under review | When Not 1, 3 | COVERED |
| RKGV | Process 1: name version + decision | Step 4 | COVERED |
| RKGV | Process 2: included/excluded | Step 5 | COVERED |
| RKGV | Process 3: link basis, impact, **run record**, verification, ship, lessons | Step 6 (run record dropped) | ACCEPTABLE-TRIM (verification.md carries the run evidence) |
| RKGV | Process 4: residual risks + re-check triggers | Step 6–7 | COVERED |
| RKGV | Process 5: what forces new baseline | Step 7 | COVERED |
| RKGV | Outputs: accepted gaps with owner; link to lesson | Outputs 2; step 6 | COVERED |
| RKGV | Verification: rebuildable; in/out on purpose; triggers findable | Verification 2–3 | COVERED |
| RKGV | Escalation: stop if accepted without evidence | Escalation 1 | COVERED |
| RKGV | Escalation: customers, regulated, safety, security, procurement, outside-trust claim | Escalation 2 (safety and outside-trust claim dropped; customers → users) | ACCEPTABLE-TRIM (public claims routed through `checking-public-claims`; AGENTS.md authority boundaries) |
| RKGV | Rationalizations: merge commit ≠ baseline; record later; only release teams | 1 kept; "only release teams" ≈ "only a prompt or doc"; "record later" dropped | ACCEPTABLE-TRIM |
| RKGV | Red flags: no evidence links; quiet exclusions; no triggers for deps/models/prompts/tools/claims | Red flags 2–3 | COVERED |
| CWTC | Contract: every trust/agent-power/release/repeatability/public item named with owner, states, evidence/gap, trigger | Contract 1st clause; step 3 | COVERED |
| CWTC | Failure class uncontrolled-item | Contract | COVERED |
| CWTC | Output controlled-item list with do-not-touch boundaries, triggers, named gaps | Outputs 1; step 3 | COVERED |
| CWTC | Trigger: change touches prompts/models/tools/deps/docs/checkers/templates/skills/commands/release/runbooks | When to Use "Scoping" (runbooks dropped) | COVERED |
| CWTC | Trigger: reviewer needs approved state | When to Use "Scoping" | COVERED |
| CWTC | Trigger: agent power **or idea-lineage wording** changes | agent power kept; lineage dropped | ACCEPTABLE-TRIM (`checking-public-claims`; AGENTS.md "make bigger claims about where the ideas come from") |
| CWTC | Trigger: wrong-target risk -> name exact item first | Step 3 "do-not-touch boundaries when the target must be exact" | COVERED |
| CWTC | When Not: local/reversible; fresh controlled-items.md | When Not 1–2 | COVERED |
| CWTC | Inputs: risk.md, basis.md, plan.md | dropped | ACCEPTABLE-TRIM |
| CWTC | Process 1–4 | Steps 1–3 | COVERED |
| CWTC | Process 5: **move up to `change-impact.md` when several artifact kinds could go stale** (do both) | Turned into When Not: "Several kinds of artifacts could go stale ... (use `checking-what-a-change-affects`)" (do the other instead) | **LOSS-MATTERS** — for a prompt + checker + docs change the agent is told not to use this skill, so it skips `controlled-items.md`; but `checking-what-a-change-affects` lists "The controlled-item list" as its first input, so the impact screen starts without it |
| CWTC | Verification: reason, evidence/gap; reviewer can tell in vs out | Verification 1–2 | COVERED |
| CWTC | Escalation: drift could affect users, data, security, releases, **lineage**, agent power | Escalation 2 (lineage dropped) | ACCEPTABLE-TRIM (as above) |
| CWTC | Escalation: stop on whole-repo inventory | Escalation 1; step 2 | COVERED |
| CWTC | Rationalizations: git tracks bytes; only a prompt/doc; "work it out from the diff" (reviewers need intent) | 1–2 kept; 3 covered by "why controlled" in prompt | COVERED |
| CWTC | Red flags: no owner/trigger; **public claims change but stay uncontrolled**; agent tool power unrecorded | Red flag 1; public-claims flag partly via step 1 "claims" | ACCEPTABLE-TRIM |

### Over-application risks

- **The baseline gate now blocks scoping (description level):** "Do not use for scratch work nothing depends on, **or while work is still under review**." In the original, only `recording-a-known-good-version` carried this exclusion. Scoping controlled items happens precisely while work is in progress or under review, so a trigger-based loader reading the description will skip the scoping half. The body's When Not correctly scopes it ("not ready to record a baseline"); the description does not.
- Escalation 2 now applies "regulated work, procurement" to scoping. Low impact.

### Broken references

None. `checking-what-a-change-affects` survives; `docs/02-operating-system/controlled-items.md` and `source-map.md` exist.

**Summary: COVERAGE FAIL (1 LOSS-MATTERS: "move up to change-impact" became "use the other skill instead", which drops the controlled-item list the impact screen needs as input). Also fix the description-level over-application.**

---

## Merge 5: creating-change-records + closing-stale-packets -> drafts/managing-change-records

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| CCR | Contract: required files, links, exit criteria, lineage notes, plain labels, resolving links | Contract 1st clause | COVERED |
| CCR | Failure class incomplete-record | Contract | COVERED |
| CCR | Outputs: Quick/Standard file sets, habit records, validator result | Outputs 1 | COVERED |
| CCR | Trigger: start real change; update after scope/proof/risk/posture change; PR needing evidence | When to Use 1–2 | COVERED |
| CCR | Trigger: preview/self-check/handoff/OPEX/supplier trust needs a record | Step 3 habit records | COVERED |
| CCR | When Not: no lasting artifact; browse/explain docs | When Not 1 | COVERED |
| CCR | When Not / description: **work belongs in an existing record rather than a new one**; Rationalization **"One big record is easier" → one change per record** | MISSING (no other repo file states either rule) | **LOSS-MATTERS** — a follow-up fix opens a second packet for the same change (feeding the stale-packet problem the other half cleans up), or three changes get lumped into one record too big to review. Draft step 1 runs `ng new` even on the "update" path |
| CCR | When Not: mode only -> `rating-change-risk` | When Not 2 | COVERED |
| CCR | Inputs: questioning-attitude screen when uncertainty/AI power/dependency trust/release stakes real; prompt "questioned assumptions" | MISSING | ACCEPTABLE-TRIM (`templates/standard/risk.md` "## Questioning-attitude summary", `templates/standard/basis.md` assumptions table, `templates/quick/risk.md` question table) |
| CCR | Process 1: `ng new` | Step 1 | COVERED |
| CCR | Process 2: name required files in reply (reader without tool access) — **name only the set for the mode in play** | Step 2 "Name the required files in your reply. Quick: ... Standard: ..." — "only the set for the mode in play" dropped from the step; prompt says "for the mode" | **LOSS-MATTERS** (minor) — this was an eval-driven amendment for the one skill that scored LOSES (`evals/skill-benchmark-pilot/REPORT.md`; the rule is still in `commands/ng-new.md:45`); the draft step lists both sets with no "only", inviting answers that list both |
| CCR | Process 3–4: fill only what helps decide; habit records only when they change a decision | Step 3 | COVERED |
| CCR | Process 5–6: links; plain status labels | Step 4 | COVERED |
| CCR | Process 7: validate | Step 5 | COVERED |
| CCR | Verification 1–4 | Verification 1 | COVERED |
| CCR | Escalation: Quick→Standard; human review | Escalation 1 | COVERED |
| CCR | Escalation: stop if record becomes long story without claim→evidence links | dropped | ACCEPTABLE-TRIM (Overview "smallest record"; red flag "missing ... evidence link") |
| CCR | Rationalizations: fill after PR | kept | COVERED |
| CCR | Rationalization: "everything is obvious" — save assumption and evidence path | dropped | ACCEPTABLE-TRIM (templates' assumptions sections) |
| CCR | Red flags: missing proof command; claims past evidence; repeating files | Red flags 1–2 | COVERED |
| CSP | Contract: one honest terminal state (completed, closed with reason + decider, deleted empty scaffold) | Contract 2nd clause | COVERED |
| CSP | Failure class silent-stale-packet incl. faked pass | Contract | COVERED |
| CSP | Output `NUCLEAR-GRADE-CLOSED:` line; status ok/closed | Outputs 2; step 7–8 | COVERED |
| CSP | Trigger: ng status scaffold/invalid; interrupted session; dropped/superseded change | When to Use 3 | COVERED |
| CSP | Trigger: periodic cleanup or release-readiness sweep | dropped | ACCEPTABLE-TRIM (falls under "ng status flags") |
| CSP | Trigger: exploration scaffold abandoned | Step 7 Delete | COVERED |
| CSP | When Not: actively worked | When Not 3 | COVERED |
| CSP | When Not: intend to ship — don't close to silence validator | Description "or to silence the validator on work you mean to ship" | COVERED |
| CSP | When Not: incident first; formal assurance | dropped / prompt disclaimer | ACCEPTABLE-TRIM |
| CSP | Process 1: list non-ok packets | Inputs (status output); step 8 | COVERED |
| CSP | Process 2: ownership + intent from issue/PR/anchor | Step 6 | COVERED |
| CSP | Process 3: complete / close (why, replacement, who decided, same line) / delete | Step 7 | COVERED |
| CSP | Process 4: prefer close over delete; delete only empty scaffolds | Step 7 | COVERED |
| CSP | Process 5: OPEX note when abandonment is a near miss worth learning | Step 8 "when abandonment keeps recurring" (single near miss dropped) | ACCEPTABLE-TRIM |
| CSP | Process 6: re-run status | Step 8 | COVERED |
| CSP | Verification: closed names why + who; completed passes not by marker deletion; deleted were empty | Verification 2; step 7 | COVERED |
| CSP | Escalation: owner before deleting unconfirmed-dead | Escalation 2 | COVERED |
| CSP | Escalation: accumulation is an LFE signal | Step 8 OPEX note | COVERED |
| CSP | Escalation: shipped without proof — closing ≠ closing risk | Escalation 3 | COVERED |
| CSP | Rationalizations: marker deletion; closing = failure | kept | COVERED |
| CSP | Rationalizations: "finish later"; "leaving open harmless"; "empty scaffold, close formally" | Overview ("misleads the next reader") | ACCEPTABLE-TRIM |
| CSP | Red flags: stale marker; unexplained scaffold; faked pass; deleted to tidy; repeat abandonment w/o OPEX | Red flag 3; verification; step 8 | COVERED |

### Over-application risks

- **Repo-wide clean status now gates every create/update:** "**Decision affected:** block -- whether the record is structurally complete, **and whether `ng status` reports every record `ok` or `closed`**." In the original, only the stale-packet cleanup was blocked on a clean `ng status`. Under the draft an agent creating a new record is blocked until every other packet in the repo is clean, and its own in-progress record (scaffold) blocks itself, which contradicts When Not 3.
- Step 1 `ng new` on the "Create or update" path. (Inherited from the original, but the original's description exclusion that limited it is gone.)

### Broken references

None. `rating-change-risk` survives.

**Summary: COVERAGE FAIL (2 LOSS-MATTERS: record-granularity rules (existing record vs new; one change per record); "name only the set for the mode in play").**

---

## Merge 6: handing-off-work + briefing-an-agent -> drafts/briefing-and-handing-off

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| HOW | Contract: resume without chat; last action, changes, scope, authority, evidence, stop; owner restates before acting | Contract 2nd clause; step 7 | COVERED |
| HOW | Failure class open-loop-handoff | Contract | COVERED |
| HOW | Output `turnover.md` (resume point, changes, remaining, next gate, confirmation) | Outputs 2 | COVERED |
| HOW | Output variants: turnover section in context pack; release or support handoff note | dropped | ACCEPTABLE-TRIM |
| HOW | Trigger: agent/reviewer/verifier/releaser/support owner continues | When to Use 3 | COVERED |
| HOW | Trigger: long thread resumed after context change | When to Use 3 | COVERED |
| HOW | Trigger: open evidence/decisions/limits; release/incident/OPEX transfer | When to Use 3 | COVERED |
| HOW | When Not: done; tiny Quick; summarize-only; brief-only | When Not 1–3 | COVERED |
| HOW | Inputs: record path, phase, mode; done/changed/assumptions/gaps; allowed/forbidden; next owner + role | Inputs 1–3 | COVERED |
| HOW | Process 1: last action, done artifacts, evidence | Step 6 | COVERED |
| HOW | Process 2: changed conditions, oddities, failed attempts, unchecked assumptions | Step 6 ("anything odd" dropped) | COVERED |
| HOW | Process 3: controlled items, no-touch targets, hold points, approval gates | Steps 4, 6 | COVERED |
| HOW | Process 4: next decision/action, critical action, likely error, guard | Step 5 | COVERED |
| HOW | Process 5: incoming owner restates scope/authority/proof/stop | Step 7 | COVERED |
| HOW | Verification: no chat history; done/left/changed/must-not; limits obeyable | Verification 1, 3 | COVERED |
| HOW | Escalation: stop if owner cannot restate; credentials/prod data/release/public claims/evidence gaps | Escalation 1–2 | COVERED |
| HOW | Rationalizations: figure it out; chat not controlled; "just continue" | Rationalization 3; contract | COVERED |
| HOW | Red flags: no last action; no changed conditions; build work mixed in; act before confirm | Red flags 2–3; step 7 | COVERED |
| BAA | Contract: what may do / stay true / evidence / when stop; authority ≤ clarity; goal anchor + forbidden actions | Contract 1st clause | COVERED |
| BAA | Failure class boundary-overreach | Contract | COVERED |
| BAA | Decision rights: what it may decide at the edge vs escalate | Overview | COVERED |
| BAA | Trigger: agent about to edit/run/call/prepare release evidence | When to Use 1 | COVERED |
| BAA | Trigger: reviewer one-screen summary of Standard record | When to Use 2 | COVERED (but see risk/basis summary row) |
| BAA | Trigger: boil long thread into context to act | When to Use 3 ("long thread resumes") | COVERED |
| BAA | When Not: small Quick; no power, only explain | When Not 2 | COVERED |
| BAA | Inputs: role list | Inputs 1 | COVERED |
| BAA | Inputs: **`docs/02-operating-system/context-packs.md`** (the pack schema and six-component completeness check: instructions, knowledge, tools, memory, state, query) | MISSING — the draft never cites it | **LOSS-MATTERS** — without the schema an agent builds a pack with no memory slot (baselines, OPEX, open deficiencies pulled in through `durable-memory.md`), so a subagent starts unaware of an open deficiency on the file it is about to edit |
| BAA | Process 1: role, question, goal anchor (goal/success/non-goals), affected parties; see `staying-on-mission` | Step 1 (pointer dropped) | COVERED (pointer ACCEPTABLE-TRIM) |
| BAA | Process 2: only needed files/rows/commands | Step 2 | COVERED |
| BAA | Process 3: last action, changed conditions, critical action, likely mistake, guard | Steps 5–6 | COVERED |
| BAA | Process 4: phase + archetype and its drift (`archetype-lens.md`) | Step 3 | COVERED |
| BAA | Process 5–6: power over files/commands/network/creds/approvals/release; off-limits claims, no-touch targets, stop | Step 4 | COVERED |
| BAA | Process 7: link pack back to record **and mode rules** | dropped | ACCEPTABLE-TRIM (Inputs carry the record and mode) |
| BAA | Outputs: pack; power limits; archetype + drift; next action + evidence; last action when mid-task | Outputs 1; red flag 2 | COVERED |
| BAA | Verification: answerable four questions; no chat; no whole-repo load | Verification 1–2 | COVERED |
| BAA | Escalation: stop on actions past pack power; credentials/network/prod/release/outside trust | Escalation 1–2 | COVERED |
| BAA | Escalation: move to handoff when responsibility transfers | Merged path step 6–7 | COVERED |
| BAA | Rationalizations: more context; work out permissions | kept | COVERED |
| BAA | Rationalization: "Approval can happen later" — approval before side-effect action | dropped | ACCEPTABLE-TRIM (`deciding-who-decides` Next action: "transfer or block before side effects") |
| BAA | Red flags: no off-limits list; no allowed files; no last action mid-task; lineage pasted | Red flags 1, 2, 4 | COVERED |
| BAA | Prompt input: loaded instruction files with precedence | Prompt "instruction files in force and which wins on conflict" | COVERED |
| BAA | Prompt return: **risk summary, basis summary, open gaps** | MISSING from the draft's return list | **LOSS-MATTERS** — the "one-screen summary of a Standard change record" for a reviewer now returns authority limits and archetype but no risk grade, basis, or open gaps, so the reviewer starts without knowing the risk tier |

### Over-application risks

- **Mid-task subagent briefs now pull in the full turnover path:** "**When open work changes hands or resumes, add:** ... 7. Have the new owner restate scope, authority, proof owed, and stop conditions before acting." In the original, a brief that followed earlier work in the same task only added the last action and changed conditions (BAA Outputs 5) and did not require `turnover.md` or a restatement. In the draft, any delegation mid-task is "open work changing hands", so every subagent spawn reads as needing a turnover record plus a confirmation round-trip.

### Broken references

None. `docs/02-operating-system/archetype-lens.md` and `source-map.md` exist.

**Summary: COVERAGE FAIL (2 LOSS-MATTERS: `context-packs.md` schema pointer; risk/basis/open-gaps summary in the brief).**

---

## Merge 7: organizing-project-folders + breaking-down-the-work -> drafts/structuring-the-work

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| OPF | Contract: folder maps to one piece/rule, one reason to change, naming/depth checks | Contract | COVERED |
| OPF | Failure class junk-drawer-layout | Contract | COVERED |
| OPF | Outputs: folder map w/ disposition; README stubs; stage layout; naming/depth/single-source check; flagged conflicts | Outputs 2–3 | COVERED |
| OPF | Overview pointer: **`docs/02-operating-system/agentic-workflow-architecture.md` — when folders are enough and when a durable runtime is needed** (also cited by BDW step 9) | MISSING — neither the doc nor the folders-vs-runtime boundary appears | **LOSS-MATTERS** — an agent designing a retry-heavy, multi-user agent pipeline as numbered folders gets no warning; the doc (line 178) flags "Selling the folder system as a durable runtime when state, retries, or scale are real" |
| OPF | Triggers: new tree; where file belongs; junk drawer; WBS→folders; workflow as folders | When to Use 2–3 | COVERED |
| OPF | When Not: obvious file / clean rename; framework-fixed layout | When Not 1–2 | COVERED |
| OPF | When Not: live incident | dropped | ACCEPTABLE-TRIM |
| OPF | When Not: ownership/CI/supply-chain enforcement → other skills | dropped | ACCEPTABLE-TRIM (those skills trigger on their own descriptions) |
| OPF | Inputs: WBS + dictionary; tree/conventions; mission anchor; platform/tooling limits; disposition | Inputs (platform limits dropped) | COVERED |
| OPF | Process 1: pick pattern | Step 6 | COVERED |
| OPF | Process 2: WBS as source of truth; dictionary → folder notes; reverse-engineer if none | Overview "Do only the half you need"; prompt "derive folders from outline numbers" (dictionary→notes dropped) | COVERED |
| OPF | Process 3: folder-decision checklist | Step 7 | COVERED |
| OPF | Process 4: MWP — numbered stages, context file I/P/O, reference vs run output, **scripts do mechanical work, every output openable/editable, human review gate at each boundary** | Step 6 "a review gate per stage" ("human", scripts, editable outputs dropped; the original prompt also said "human review gate") | **LOSS-MATTERS** — an LLM-judge gate between stage 2 and stage 3 now satisfies "a review gate per stage", removing the human checkpoint the MWP pattern requires |
| OPF | Process 5: naming rules incl. zero-padded sequences, `NN_` exception, **"files normally capitalized by convention" exception (README.md, LICENSE, CONTEXT.md, CLAUDE.md)**, banned names | Step 8: closed list "`README.md`, `LICENSE`, `CONTEXT.md` and the `NN_` stage prefix are accepted exceptions" (general convention clause and `CLAUDE.md` dropped) | **LOSS-MATTERS** — the naming check now flags `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`; an agent applying it to this repo could propose `SKILL.md` → `skill.md` and break skill loading |
| OPF | Process 6: depth/path caps; **do not blindly nest one folder per WBS level** (+ rationalization) | Step 8 caps kept; the anti-1:1-nesting rule dropped while the prompt says "derive folders from outline numbers" | **LOSS-MATTERS** — WBS `1.2.3` becomes three nested directories for a five-file feature; the 8-level cap does not prevent it |
| OPF | Process 7: README per **non-trivial** folder (purpose, belongs, not, owner) + disposition | Outputs "per-folder README stubs"; prompt "add a README and disposition per folder" | see over-application |
| OPF | Process 8: respect conventions, least structure, flag conflicts | Step 9 | COVERED |
| OPF | Process 9: output map + check | Outputs 2 | COVERED |
| OPF | Verification: naming; depth; mapping/one home; cohesion/coupling; docs; workflow stages | Verification 3 (documentation check dropped from verification; still in outputs) | COVERED |
| OPF | Escalation: conflict with saved known-good convention | Escalation 2 (`controlling-approved-versions`) | COVERED |
| OPF | Escalation: **cannot reach one source of truth without an architecture decision** | MISSING | **LOSS-MATTERS** — two services both own a shared schema; the agent picks a "single home" itself instead of escalating an architecture decision |
| OPF | Escalation: to breakdown when none exists | Internal (Breakdown half) | COVERED |
| OPF | Rationalizations: utils "for now"; copy to two places | kept | COVERED |
| OPF | Rationalizations: deeper is organized; spaces fine; name explains itself; one folder per WBS level | dropped (rules kept except 1:1 nesting, above) | ACCEPTABLE-TRIM except the nesting rule |
| OPF | Red flags: junk names; bad chars; deep nesting; coupling; stage w/o context/gate; undocumented top-level | Red flags 2–3 (coupling/undocumented dropped) | ACCEPTABLE-TRIM |
| BDW | Contract: 100% rule, no overlap, dictionary per outline number | Contract | COVERED |
| BDW | Failure class non-mece-breakdown | Contract | COVERED |
| BDW | Decision tier block (plan-ready) | "block for the breakdown" | COVERED |
| BDW | Triggers: epic/feature/subsystem; tree design needs scope basis; scope growth; shared map for several agents | When to Use 1 | COVERED |
| BDW | Trigger: packet inside structure decided on principle | dropped | ACCEPTABLE-TRIM |
| BDW | When Not: one-file edit; already broken down; schedule/cost/cert | When Not 1–3 | COVERED |
| BDW | Inputs: deliverable; mission anchor path; charter; non-goals; tree; `wbs.md` | Inputs; contract cites `wbs.md` | COVERED |
| BDW | Process 1: one top deliverable or stop | Step 1 | COVERED |
| BDW | Process 2: product-first nouns; verbs in activity layer | Step 2 | COVERED |
| BDW | Process 3: 100% rule + gap lines | Step 3 | COVERED |
| BDW | Process 4: no overlap, one home, lift common work, never copy | Step 3 | COVERED |
| BDW | Process 5: stop at work package (8/80); **match depth to mode** | Step 4 (mode-depth dropped; mode is an input but unused) | ACCEPTABLE-TRIM (8/80 cap bounds it) |
| BDW | Process 6: outline numbering as lasting ID | Step 4 | COVERED |
| BDW | Process 7: dictionary fields | Step 5 | COVERED |
| BDW | Process 8: same taxonomy for ownership, folders, CI grouping, risk labels | dropped | ACCEPTABLE-TRIM (Overview "the spine that estimates, ownership, delegation, and folders hang from") |
| BDW | Process 9: self-check; hand to folders; delegated leaf → `plan.md` stage contract (prereqs, `file#section` inputs + context budget, outputs, proof, stop) | Step 5 "point each leaf to its `plan.md` slice written as a stage contract (`templates/standard/stage-contract.md`)" | COVERED (field list lives in the template) |
| BDW | Outputs: table, dictionary, common pieces, gap lines, handoff note, leaf→plan pointer | Outputs 1; step 5 | COVERED |
| BDW | Verification: 100%; one home; nouns; dictionary; leveling; reviewer test | Verification 1–2 | COVERED |
| BDW | Escalation: stop no deliverable; overlap; unestimable/**not understood** work; official cost/schedule; conflict with known-good structure | Escalation 1–2; When Not 3 | COVERED ("not understood" ACCEPTABLE-TRIM) |
| BDW | Rationalizations: task list; close enough; two owners; dictionary obvious; deeper rigorous | 1–2 kept; rest enforced by steps | COVERED |
| BDW | Rationalization: "breakdown grew so mission grew" is drift → `staying-on-mission` | dropped | ACCEPTABLE-TRIM (`staying-on-mission` triggers on scope drift; contract "nothing invented") |
| BDW | Red flags: missing coverage; two branches; verbs; no dictionary/owner; misc bucket; outline gaps/duplicates; unestimable leaf | Red flags 1–2 (outline gaps/duplicates dropped) | ACCEPTABLE-TRIM |

### Over-application risks

- **README for every folder:** the prompt says "add a README and disposition per folder". The original said "each non-trivial folder". Under the draft, trivial leaf folders such as `fixtures/` or `assets/icons/` get README stubs, which conflicts with the draft's own "propose the least new structure".
- **Closed capitalization exception list (also counted as LOSS-MATTERS):** "`README.md`, `LICENSE`, `CONTEXT.md` and the `NN_` stage prefix are accepted exceptions." Applied literally, the lowercase rule now covers `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, and `CORE.md`.

### Broken references

None. `controlling-approved-versions` is a draft name; `templates/standard/wbs.md`, `templates/standard/stage-contract.md`, and `source-map.md` exist.

**Summary: COVERAGE FAIL (5 LOSS-MATTERS: folders-vs-durable-runtime doctrine pointer; human review gate between stages; convention-capitalized-file exception; no 1:1 WBS-level nesting; architecture-decision escalation for single source of truth).**

---

## Repo references to the 15 original names (would mislead after the merge)

Scope as requested: `skills/` (excluding the 15 original dirs themselves), `docs/`, `templates/`, `agents/`, `hooks/`, `nuclear_grade/`, `tools/`, `starter-kit/`, `CORE.md`, `SKILLS.md`, `README.md`; `evals/` and `.nuclear/changes/` excluded. Counts are matching lines. `agents/` and `hooks/` had no hits. Names marked (survives) remain valid, but references may describe the old, narrower scope.

| Old name | Files | Lines | Per-file (file:lines) |
|---|---|---|---|
| double-checking-before-acting (survives) | 26 | 33 | runtime-enforcement.md:3, SKILLS.md:3, starter-kit/core/README.md:2, skill-benchmark-amendment-plan.md:2, agent-threat-model.md:2, tools/build_diagrams.py:1, starter-kit/core/AGENTS.md:1, nuclear_grade/cli.py:1, docs/diagrams.md:1, skill-map.svg:1, skill-map-core.svg:1, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, independent-skill-benchmark-protocol.md:1, trial-records/{public-assurance-wording, payment-webhook-idempotency, external-api-tool-permission, data-retention-migration}.md:1 each, results-summary.md:1, red-team-review.md:1, independence-architecture.md:1, authority-and-intent.md:1, pmbok-pmi-ai-crosswalk.md:1, leadership-and-high-reliability.md:1, CORE.md:1 |
| declaring-intent | 18 | 23 | SKILLS.md:3, starter-kit/agent-authority/README.md:2, pmbok-pmi-ai-crosswalk.md:2, leadership-and-high-reliability.md:2, tools/build_diagrams.py:1, skill-map.svg:1, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, skill-benchmark-amendment-plan.md:1, independent-skill-benchmark-protocol.md:1, results-summary.md:1, runtime-enforcement.md:1, authority-and-intent.md:1, archetype-lens.md:1, agent-threat-model.md:1, source-to-concept-crosswalk.md:1, CORE.md:1 |
| learning-from-experience (survives) | 26 | 34 | SKILLS.md:3, tools/build_diagrams.py:2, starter-kit/core/README.md:2, skill-map.svg:2, skill-map-core.svg:2, source-to-concept-crosswalk.md:2, pmbok-pmi-ai-crosswalk.md:2, starter-kit/core/AGENTS.md:1, skills/responding-to-incidents/SKILL.md:1, nuclear_grade/cli.py:1, docs/diagrams.md:1, skillsbench-adoption-plan.md:1, skill-evaluation.md:1, trial-records/{source-citation-adoption-doc, release-readiness-cut, incident-regression-fix}.md:1 each, results-summary.md:1, program-self-assessment.md:1, incident-response.md:1, durable-memory.md:1, deficiency-register.md:1, archetype-lens.md:1, leadership-and-high-reliability.md:1, for-high-consequence-builders.md:1, source-map.md:1, CORE.md:1 |
| tracking-deficiencies | 15 | 17 | source-to-concept-crosswalk.md:2, leadership-and-high-reliability.md:2, skills/responding-to-incidents/SKILL.md:1, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, skill-benchmark-amendment-plan.md:1, independent-skill-benchmark-protocol.md:1, results-summary.md:1, program-self-assessment.md:1, deficiency-register.md:1, archetype-lens.md:1, pmbok-pmi-ai-crosswalk.md:1, SKILLS.md:1, CORE.md:1 |
| reporting-shared-defects | 8 | 8 | skillsbench-adoption-plan.md:1, skill-evaluation.md:1, skill-benchmark-amendment-plan.md:1, independent-skill-benchmark-protocol.md:1, results-summary.md:1, agent-threat-model.md:1, SKILLS.md:1, CORE.md:1 |
| checking-legal-and-safety-wording | 14 | 18 | starter-kit/public-claims/README.md:2, skills/proving-claims/SKILL.md:2, skillsbench-adoption-plan.md:2, skills-token-audit.md:2, skill-evaluation.md:1, skill-benchmark-amendment-plan.md:1, independent-skill-benchmark-protocol.md:1, trial-records/{source-citation-adoption-doc, public-assurance-wording, prompt-model-baseline}.md:1 each, results-summary.md:1, pmbok-pmi-ai-crosswalk.md:1, SKILLS.md:1, CORE.md:1 |
| checking-source-claims | 15 | 21 | skills/checking-facts/SKILL.md:3, starter-kit/public-claims/README.md:2, skills/proving-claims/SKILL.md:2, skillsbench-adoption-plan.md:2, skills-token-audit.md:2, skill-evaluation.md:1, skill-benchmark-amendment-plan.md:1, independent-skill-benchmark-protocol.md:1, trial-records/{source-citation-adoption-doc, public-assurance-wording, prompt-model-baseline}.md:1 each, results-summary.md:1, pmbok-pmi-ai-crosswalk.md:1, SKILLS.md:1, CORE.md:1 |
| recording-a-known-good-version | 19 | 25 | tools/build_diagrams.py:2, skill-map.svg:2, skill-map-core.svg:2, skill-benchmark-amendment-plan.md:2, archetype-lens.md:2, SKILLS.md:2, docs/diagrams.md:1, skillsbench-adoption-plan.md:1, skill-evaluation.md:1, independent-skill-benchmark-protocol.md:1, trial-records/{release-readiness-cut, prompt-model-baseline, external-api-tool-permission, dependency-security-update, data-retention-migration}.md:1 each, results-summary.md:1, work-breakdown-and-folders.md:1, pmbok-pmi-ai-crosswalk.md:1, CORE.md:1 |
| choosing-what-to-control | 21 | 25 | tools/build_diagrams.py:2, skill-map.svg:2, skill-map-core.svg:2, SKILLS.md:2, docs/diagrams.md:1, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, skill-benchmark-amendment-plan.md:1, independent-skill-benchmark-protocol.md:1, trial-records/{release-readiness-cut, prompt-model-baseline, payment-webhook-idempotency, external-api-tool-permission, dependency-security-update, data-retention-migration, agent-workspace-boundary}.md:1 each, results-summary.md:1, work-breakdown-and-folders.md:1, pmbok-pmi-ai-crosswalk.md:1, CORE.md:1 |
| creating-change-records | 27 | 33 | skill-benchmark-amendment-plan.md:3, tools/build_diagrams.py:2, skill-map.svg:2, skill-map-core.svg:2, SKILLS.md:2, skills/rating-change-risk/SKILL.md:1, skills/proving-claims/SKILL.md:1, docs/diagrams.md:1, skillsbench-adoption-plan.md:1, skill-evaluation.md:1, skill-authoring-contract.md:1, independent-skill-benchmark-protocol.md:1, trial-records (11 files):1 each, results-summary.md:1, archetype-lens.md:1, README.md:1, CORE.md:1 |
| closing-stale-packets | 13 | 15 | skill-benchmark-amendment-plan.md:2, SKILLS.md:2, tools/build_diagrams.py:1, nuclear_grade/ng_validate.py:1, docs/diagrams.md:1, skill-map.svg:1, skill-map-core.svg:1, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, docs/05-reference/cli-reference.md:1, results-summary.md:1, CORE.md:1 |
| handing-off-work | 23 | 29 | skill-benchmark-amendment-plan.md:3, SKILLS.md:3, starter-kit/agent-authority/README.md:2, pmbok-pmi-ai-crosswalk.md:2, tools/build_diagrams.py:1, templates/standard/plan.md:1, docs/diagrams.md:1, skill-map.svg:1, skill-map-core.svg:1, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, skill-authoring-contract.md:1, independent-skill-benchmark-protocol.md:1, trial-records/{validator-agent-handoff, release-readiness-cut, incident-regression-fix, external-api-tool-permission}.md:1 each, results-summary.md:1, runtime-enforcement.md:1, incident-response.md:1, agent-threat-model.md:1, CORE.md:1 |
| briefing-an-agent | 27 | 39 | pmbok-pmi-ai-crosswalk.md:6, skill-benchmark-amendment-plan.md:4, SKILLS.md:3, starter-kit/agent-authority/README.md:2, CORE.md:2, tools/build_diagrams.py:1, templates/standard/plan.md:1, docs/diagrams.md:1, skill-map.svg:1, skill-map-core.svg:1, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, skill-authoring-contract.md:1, independent-skill-benchmark-protocol.md:1, trial-records/{validator-agent-handoff, payment-webhook-idempotency, incident-regression-fix, external-api-tool-permission, dependency-security-update, agent-workspace-boundary}.md:1 each, results-summary.md:1, runtime-enforcement.md:1, archetype-lens.md:1, agent-threat-model.md:1, source-to-concept-crosswalk.md:1, context-engineering-literature-crosswalk.md:1 |
| organizing-project-folders | 13 | 21 | skills-token-audit.md:4, source-map.md:3, skill-benchmark-amendment-plan.md:2, docs/03-worked-examples/agentic-folder-structure/README.md:2, CORE.md:2, nuclear_grade/tokens.py:1, skillsbench-adoption-plan.md:1, skill-evaluation.md:1, results-summary.md:1, work-breakdown-and-folders.md:1, agentic-workflow-architecture.md:1, source-to-concept-crosswalk.md:1, SKILLS.md:1 |
| breaking-down-the-work | 11 | 15 | skill-benchmark-amendment-plan.md:2, pmbok-pmi-ai-crosswalk.md:2, source-map.md:2, CORE.md:2, skillsbench-adoption-plan.md:1, skills-token-audit.md:1, skill-evaluation.md:1, results-summary.md:1, work-breakdown-and-folders.md:1, source-to-concept-crosswalk.md:1, SKILLS.md:1 |

Surviving skills (outside the 15) that cite removed names: `skills/checking-facts/SKILL.md` (checking-source-claims ×3), `skills/proving-claims/SKILL.md` (checking-legal-and-safety-wording ×2, checking-source-claims ×2, creating-change-records ×1), `skills/rating-change-risk/SKILL.md` (creating-change-records ×1), `skills/responding-to-incidents/SKILL.md` (tracking-deficiencies ×1). Code that will break or mislead: `nuclear_grade/cli.py`, `nuclear_grade/ng_validate.py`, `nuclear_grade/tokens.py`, `tools/build_diagrams.py`.

Outside the requested scope but load-bearing (every one of the 15 names hits these): `nuclear-grade.yaml` (skill list and skill→command map), `tests/test_skill_contracts.py`, `tests/fixtures/command_prompts.json`, `commands/ng-*.md` (ng-self-check, ng-intent, ng-learn, ng-incident, ng-deficiency, ng-report-defect, ng-legal-check, ng-source-check, ng-fact-check, ng-prove, ng-baseline, ng-what-to-control, ng-folders, ng-new, ng-classify, ng-close-packet, ng-turnover, ng-context-pack, ng-breakdown), `WORKFLOWS.md`, `COMMANDS.md`, `MAXIMS.md`, `CHANGELOG.md`.

## Structural blocker beyond capability coverage

`tests/test_command_parity.py` asserts that (a) the skill→command map in `nuclear-grade.yaml` is a bijection ("two skills map to one command") and (b) each skill's `## Prompt` equals the frozen prompt in `tests/fixtures/command_prompts.json` byte for byte. All 7 drafts rewrote their prompts, and 8 commands lose their source skill (one of each pair: ng-intent, ng-deficiency, ng-report-defect, ng-legal-check/ng-source-check, ng-baseline/ng-what-to-control, ng-new/ng-close-packet, ng-turnover/ng-context-pack, ng-folders/ng-breakdown). The merge needs a deliberate fixture and command-map update in the same diff, plus a decision on whether those 8 user-facing slash commands are retired or re-pointed. The originals of `recording-a-known-good-version` and `choosing-what-to-control` had unfenced prompts; the draft fences its prompt, which also changes the bytes.

## Per-merge summary

1. double-checking-before-acting: COVERAGE FAIL (3 LOSS-MATTERS)
2. learning-from-experience: COVERAGE FAIL (4 LOSS-MATTERS)
3. checking-public-claims: COVERAGE FAIL (2 LOSS-MATTERS)
4. controlling-approved-versions: COVERAGE FAIL (1 LOSS-MATTERS)
5. managing-change-records: COVERAGE FAIL (2 LOSS-MATTERS)
6. briefing-and-handing-off: COVERAGE FAIL (2 LOSS-MATTERS)
7. structuring-the-work: COVERAGE FAIL (5 LOSS-MATTERS)
