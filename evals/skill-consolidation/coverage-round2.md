# Skill-merge coverage audit (round 2)

Round 2 re-audits the revised drafts against the same 15 originals. Round-1 copies are in `drafts-round1/`, and the round-1 report is in `coverage-round1.md`. Each merge opens with the status of every round-1 item. Capability rows changed in round 2 are tagged R2; all other rows were re-checked against the current drafts and are unchanged.

New lens in round 2: `nuclear_grade/gen_commands.py` projects only When to Use, When Not, Inputs, Prompt, and Verification into each `commands/ng-*.md` card. A fix that lands only in Process, Outputs, or Escalation reaches the skill but not the portable card. Where the original carried the rule in a projected section and the draft does not, this report flags a low card residual.

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

### Round-2 status of round-1 findings

| # | Round-1 item | Round-2 status |
|---|---|---|
| L1 | Credential/network/data/release/public-trust escalation | RESOLVED: "Escalate when the action affects credentials, network effects, data, releases, public trust, or anything that cannot be undone." |
| L2 | Depth-2 gate narrowed to "irreversible" | RESOLVED for hard-to-reverse and blast radius ("hard to reverse, its blast radius reaches past the immediate file"). Residual: "public claim" was left out of the new depth-2 list (still LOSS-MATTERS, minor) |
| L3 | Read-only exemption qualifier | RESOLVED: "only reads data and affects no later decision" |
| O1 | Depth-2 steps numbered after "act" | RESOLVED: step 3 "Decide the depth", step 4 "At depth 2, before acting", step 5 "Act only inside the authority" |

Numbering note: unchanged rows below use round-1 step numbers. Current mapping: Process old 3→5, 4→6, 5→7, and old 6–9 are now the bullets of step 4. Escalation old 2→3, old 3→4; new Escalation 2 is the credential/data trigger. The content of every unchanged row was re-checked against the current draft.

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
| DCBA | When Not: read-only action **that has no effect on any later decision** | "or an action that only reads data and affects no later decision" | COVERED (R2 RESOLVED) |
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
| DCBA | Escalation: **escalate when action affects credentials, network effects, data, releases, public trust, or anything irreversible** | Escalation 2: "Escalate when the action affects credentials, network effects, data, releases, public trust, or anything that cannot be undone." | COVERED (R2 RESOLVED) |
| DCBA | Rationalization "one command" | kept | COVERED |
| DCBA | Rationalization "target is obvious" | dropped | ACCEPTABLE-TRIM (Red flag "action starts before the target is named") |
| DCBA | Rationalization "check after" | kept | COVERED |
| DCBA | Red flags: target unnamed / vague result / retry on mismatch | Red flags 1–2 | COVERED |
| DCBA | Red flag: public wording claims safe/secure/approved/compliant without scoped evidence | MISSING | ACCEPTABLE-TRIM (owned by `checking-public-claims`; recommend a one-line pointer since public claims are a When-to-Use trigger) |
| DI | Contract claim: falsifying signal, concrete abort criteria, checked rollback, preconditions proven | Contract + steps 7–9 ("Prove the preconditions rather than assert them") | COVERED |
| DI | Failure class unfalsifiable-intent | Contract | COVERED |
| DI | Output `intent.md` (action, reasoning, expected, abort, rollback, decision rights, backup) | Outputs: "At depth 2, an `intent.md`" | COVERED |
| DI | Trigger: before deploy, migration, data change, **public claim**, dependency/model swap, release | Step 3: "it is a deploy, migration, data change, dependency or model swap, or release" — public claim left out of the depth-2 list | **LOSS-MATTERS (R2 residual, minor)**: publishing a README or release-note claim can be reverted with git, so it is not "hard to reverse", and it is no longer named. It gets a depth-1 self-check, and nobody declares intent or a falsifying signal before the claim goes public. `declaring-intent` named it as a trigger. (`checking-public-claims` checks the wording, not the intent.) |
| DI | Trigger: **hard to reverse, or blast radius beyond the immediate file** | Step 3: "applies when the action is hard to reverse, its blast radius reaches past the immediate file, ... or a reviewer must be able to stop it" | COVERED (R2 RESOLVED) |
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

- **NEW: every deploy or data change is now depth 2, review window included.** Step 3 reads: "Depth 2 (declared intent) applies when ... it is a deploy, migration, data change, dependency or model swap, or release". `declaring-intent` covered deploys "that deserve a stated intent" and excluded routine reversible ones. Under the draft, redeploying a throwaway preview environment, or a reversible seed-data change in a dev database, requires an `intent.md`, a backup watcher, and "act only after the review window". Qualify the list, for example with "to a shared or production environment".
- The round-1 sequencing risk is resolved.

### Broken references

None. `responding-to-incidents`, `deciding-who-decides`, `learning-from-experience` all survive; `docs/00-standards-foundation/source-map.md` and `do-not-cite-directly.md` exist.

**Summary: COVERAGE FAIL (1 LOSS-MATTERS: public claim left out of the depth-2 trigger list). Also 1 NEW over-application risk (every deploy or data change at depth 2).**

---

## Merge 2: learning-from-experience + tracking-deficiencies + reporting-shared-defects -> drafts/learning-from-experience

### Round-2 status of round-1 findings

| # | Round-1 item | Round-2 status |
|---|---|---|
| L4 | Re-baseline trigger output | RESOLVED: "plus a trigger to re-verify or re-record the approved version when a controlled item changed" |
| L5 | Deficiency escalation for safety/protected outcome | RESOLVED: "Deficiency: escalate when it touches safety, security, data integrity, or a protected outcome named in `basis.md`" |
| L6 | Not-reportable "who decided" | RESOLVED in Process step 9: "record why it is not reportable and who decided" (low residual: absent from Verification/Prompt, the sections the command card projects) |
| L7 | Independent reviewer for substantial downstream failure | RESOLVED: "require a qualified or independent reviewer when consumers are external or the defect could cause a substantial downstream failure" |
| O2 | Lesson escalation list applied to deficiencies | RESOLVED: escalation split into "Lesson:", "Deficiency:", "Shared defect:" bullets |
| (soft) | Description frames deficiencies as post-event | NOT CHANGED: still "After something went wrong or nearly did". Low; not counted |

Numbering note: Escalation is now three path bullets. In unchanged rows, old "Escalation 1" and "Escalation 2" (repeated weak control) map to the Lesson bullet, and old "Escalation 3" (stop normalizing / report upward) maps to the Deficiency and Shared-defect bullets. Content was re-checked.

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
| LFE | Output: **trigger to re-verify or re-record the approved version when a controlled item changed** | Outputs 1: "plus a trigger to re-verify or re-record the approved version when a controlled item changed" | COVERED (R2 RESOLVED) |
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
| TD | Escalation: **safety, security, data integrity, or a protected outcome** | Escalation "Deficiency: escalate when it touches safety, security, data integrity, or a protected outcome named in `basis.md`" | COVERED (R2 RESOLVED) |
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
| RSD | Verification: not-reportable records reason **and who decided** | Step 9: "or record why it is not reportable and who decided" | COVERED in body (R2 RESOLVED). Low-severity residual: the original carried it in `## Verification`, which the generated `commands/ng-report-defect.md` card shows. The draft's Verification and Prompt still omit "who decided", so the card loses it |
| RSD | Escalation: security, credentials, data integrity, privacy, public release | Escalation 1 (privacy → "users, data") | COVERED |
| RSD | Escalation: qualified/independent reviewer when consumers external **or defect could cause a substantial downstream failure** | Escalation "Shared defect: ... require a qualified or independent reviewer when consumers are external or the defect could cause a substantial downstream failure" | COVERED (R2 RESOLVED) |
| RSD | Escalation: stop and report upward when no one owns notice | Escalation 3 | COVERED |
| RSD | Rationalizations: "fixed in my repo"; "they'll pull eventually"; "probably fine for others" | "your fix does not reach other consumers"; record not-reportable reason | COVERED |
| RSD | Red flags: no notice; no named consumers/owner/link; known issue in chat | Red flags 3; Verification 3 | COVERED |

### Over-application risks

- The round-1 risk is resolved (escalation is now split per path).
- Soft, unchanged: the description opens "After something went wrong or nearly did", while `docs/02-operating-system/deficiency-register.md` treats the register as standing rather than event-driven. Not counted.
- New: none found. The per-path escalation bullets match each original's list.

### Broken references

None in the draft (`responding-to-incidents` survives; `source-map.md` exists).

**Summary: COVERAGE PASS (0 LOSS-MATTERS). Low residual: "who decided" is absent from Verification and Prompt, so the command card loses it.**

---

## Merge 3: checking-legal-and-safety-wording + checking-source-claims -> drafts/checking-public-claims

### Round-2 status of round-1 findings

| # | Round-1 item | Round-2 status |
|---|---|---|
| L8 | "Enterprise-grade" in-repo meaning | RESOLVED: "Here it means testable, easy to navigate, and reviewable; say that instead." |
| L9 | Change records dropped from lineage scope | RESOLVED in When to Use: "or the public text of a change record (for example a `basis.md` that cites a standard)". Low residual: the frontmatter description is unchanged |
| O3 | Lineage warn promoted to block | RESOLVED: "an assurance overreach blocks until reworded, while a lineage gap is a warn" |

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
| CLSW | Rationalization: **"Enterprise-grade means certified." Here it means testable, easy to navigate, and reviewable** | Rationalization 5: "Here it means testable, easy to navigate, and reviewable; say that instead." | COVERED (R2 RESOLVED) |
| CLSW | Red flags: promises safe/secure/compliant; CLI help lacks boundary wording; examples imply more proof | Red flags 1, 4; step 4 "command help" | COVERED |
| CSC | Contract: every source public, mapped or "public URL needed", influence not compliance | Contract | COVERED |
| CSC | Failure class overstated-lineage | Contract | COVERED |
| CSC | Decision tier **warn** | Draft tier **block** | See over-application |
| CSC | Trigger: doc, template, skill, command, **or change record** cites a source family | When to Use 1: "or the public text of a change record (for example a `basis.md` that cites a standard)" | COVERED in body (R2 RESOLVED). Low residual: the frontmatter description, which loaders read, still says only "public docs, READMEs, templates, or release copy" |
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

- The round-1 risk is resolved: "an assurance overreach blocks until reworded, while a lineage gap is a warn".
- New: none found. The tier regex in `tools/ng_skill_audit.py` still reads the first tier word ("block").

### Broken references

None. `checking-facts` survives; all doc paths exist.

**Summary: COVERAGE PASS (0 LOSS-MATTERS). Low residual: the frontmatter description does not mention change records.**

---

## Merge 4: recording-a-known-good-version + choosing-what-to-control -> drafts/controlling-approved-versions

### Round-2 status of round-1 findings

| # | Round-1 item | Round-2 status |
|---|---|---|
| L10 | "Move up" to change-impact became "instead" | RESOLVED: step 3a "carry this list into `change-impact.md` with `checking-what-a-change-affects`, which takes it as its first input"; the When-Not redirect was removed |
| O4 | Description excluded scoping during review | RESOLVED: "or to record a baseline before the evidence is ready" |

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
| CWTC | Process 5: **move up to `change-impact.md` when several artifact kinds could go stale** (do both) | Step 3a: "carry this list into `change-impact.md` with `checking-what-a-change-affects`, which takes it as its first input"; the When-Not redirect was removed | COVERED (R2 RESOLVED) |
| CWTC | Verification: reason, evidence/gap; reviewer can tell in vs out | Verification 1–2 | COVERED |
| CWTC | Escalation: drift could affect users, data, security, releases, **lineage**, agent power | Escalation 2 (lineage dropped) | ACCEPTABLE-TRIM (as above) |
| CWTC | Escalation: stop on whole-repo inventory | Escalation 1; step 2 | COVERED |
| CWTC | Rationalizations: git tracks bytes; only a prompt/doc; "work it out from the diff" (reviewers need intent) | 1–2 kept; 3 covered by "why controlled" in prompt | COVERED |
| CWTC | Red flags: no owner/trigger; **public claims change but stay uncontrolled**; agent tool power unrecorded | Red flag 1; public-claims flag partly via step 1 "claims" | ACCEPTABLE-TRIM |

### Over-application risks

- The round-1 description risk is resolved: "or to record a baseline before the evidence is ready".
- New: none found. Step "3a." renders as a continuation of list item 3, which is cosmetic.

### Broken references

None. `checking-what-a-change-affects` survives; `docs/02-operating-system/controlled-items.md` and `source-map.md` exist.

**Summary: COVERAGE PASS (0 LOSS-MATTERS).**

---

## Merge 5: creating-change-records + closing-stale-packets -> drafts/managing-change-records

### Round-2 status of round-1 findings

| # | Round-1 item | Round-2 status |
|---|---|---|
| L11 | Record granularity | RESOLVED: When Not "Work that belongs in an existing record rather than a new one; keep one change per record" + rationalization "One change per record keeps the review small enough to do well." (but see NEW over-application) |
| L12 | "Name only the set for the mode in play" | RESOLVED in step 2: "Name in your reply only the file set for the mode in play." (low residual: Prompt still "name the required files for the mode") |
| O5 | Repo-wide clean status gating every create | RESOLVED: "whether this record is structurally complete (`ng validate`), or, for a stale record, whether it reached `ok` or `closed`"; step 8 "confirm the records you touched" |

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| CCR | Contract: required files, links, exit criteria, lineage notes, plain labels, resolving links | Contract 1st clause | COVERED |
| CCR | Failure class incomplete-record | Contract | COVERED |
| CCR | Outputs: Quick/Standard file sets, habit records, validator result | Outputs 1 | COVERED |
| CCR | Trigger: start real change; update after scope/proof/risk/posture change; PR needing evidence | When to Use 1–2 | COVERED |
| CCR | Trigger: preview/self-check/handoff/OPEX/supplier trust needs a record | Step 3 habit records | COVERED |
| CCR | When Not: no lasting artifact; browse/explain docs | When Not 1 | COVERED |
| CCR | When Not / description: **work belongs in an existing record rather than a new one**; Rationalization **"One big record is easier" → one change per record** | When Not 4: "Work that belongs in an existing record rather than a new one; keep one change per record"; description: "work that belongs in an existing record"; Rationalization 4 restored | COVERED (R2 RESOLVED). See the NEW over-application risk: as worded, it can exclude the update path |
| CCR | When Not: mode only -> `rating-change-risk` | When Not 2 | COVERED |
| CCR | Inputs: questioning-attitude screen when uncertainty/AI power/dependency trust/release stakes real; prompt "questioned assumptions" | MISSING | ACCEPTABLE-TRIM (`templates/standard/risk.md` "## Questioning-attitude summary", `templates/standard/basis.md` assumptions table, `templates/quick/risk.md` question table) |
| CCR | Process 1: `ng new` | Step 1 | COVERED |
| CCR | Process 2: name required files in reply (reader without tool access) — **name only the set for the mode in play** | Step 2: "Name in your reply only the file set for the mode in play." | COVERED (R2 RESOLVED). Low residual: the original rule was in the Prompt Return, which the `commands/ng-new.md` card projects. The draft prompt still says only "name the required files for the mode" |
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

- The round-1 contract risk is resolved.
- **NEW: the granularity rule now reads as excluding the skill's own update path.** The description says "Do not use for a throwaway script, **work that belongs in an existing record**, or to silence the validator", and When Not 4 says "Work that belongs in an existing record rather than a new one". But the skill "Creates, updates, and closes" records, and revising an existing record is exactly work that belongs in an existing record. A trigger-based loader can skip the skill on an update, so no `validate` run happens. Under "Create or update", step 1 still runs `ng new` unconditionally, so even when loaded the update path opens a new packet. Reword as a process rule: "If the work belongs in an existing record, update that record instead of running `ng new`; keep one change per record."

### Broken references

None. `rating-change-risk` survives.

**Summary: COVERAGE PASS (0 LOSS-MATTERS). Also 1 NEW over-application risk (the granularity rule excludes the update path; step 1 always runs `ng new`). Low residual: "only" is absent from the Prompt.**

---

## Merge 6: handing-off-work + briefing-an-agent -> drafts/briefing-and-handing-off

### Round-2 status of round-1 findings

| # | Round-1 item | Round-2 status |
|---|---|---|
| L13 | `context-packs.md` pointer | RESOLVED: "The context-pack schema in `docs/02-operating-system/context-packs.md`, including its memory slot" |
| L14 | Risk/basis/open-gaps in the brief | **NOT RESOLVED** in the Prompt (where the loss was): added to Process step 5 and Outputs only; the Prompt Return line is unchanged, and the Prompt is what the `ng-context-pack` card projects |
| O6 | Mid-task subagent brief pulled into full turnover | PARTIALLY RESOLVED: Process now has a middle tier ("When the brief follows earlier work in the same task: add the last finished action and the conditions that changed. That is enough for a subagent the same owner is directing."). But the contract ("for open work ... the owner confirmed them before acting"; Next action "require the restatement") and the Prompt (binary "open work changing hands or resuming? (yes/no)") were not updated |

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
| BAA | Inputs: **`docs/02-operating-system/context-packs.md`** (pack schema, six-component completeness check) | Inputs 3: "The context-pack schema in `docs/02-operating-system/context-packs.md`, including its memory slot (baselines, OPEX, open deficiencies)" | COVERED (R2 RESOLVED) |
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
| BAA | Prompt return: **risk summary, basis summary, open gaps** | Added to Process step 5 ("a one-line risk summary (mode and tier), a basis summary, and the open gaps") and Outputs. **The `## Prompt` Return line is unchanged** ("role, decision question, goal anchor, phase and archetype ..., critical next action and likely error") | **LOSS-MATTERS (R2 NOT RESOLVED)**: the loss was in the prompt return, and the prompt is still missing it. The prompt is the paste-ready block and is projected verbatim into the generated `commands/ng-context-pack.md` card (`nuclear_grade/gen_commands.py` projects When to Use, When Not, Inputs, Prompt, and Verification, but not Process or Outputs). A reviewer briefed from the prompt or card still gets no risk tier, basis, or open gaps |

### Over-application risks

- **Round-1 risk only partly resolved.** The Process middle tier is good. But the Decision contract still says "for open work, the last finished action, changed conditions, and remaining scope are stated **and the owner confirmed them before acting**" and "Next action: ... **require the restatement**", without condition. The Prompt still asks only "open work changing hands or resuming? (yes/no)", then "If yes: ... a prompt for the new owner to restate". A mid-task subagent brief is "open work", so from the contract or the prompt it still reads as needing a restatement round-trip.
- **NEW (same cause): the prompt lost the middle tier.** `briefing-an-agent`'s prompt always asked for "last completed action" and "changed conditions". The draft prompt asks for them only under "if yes". A same-owner subagent brief answered "no" now omits them, and one answered "yes" gets full turnover.

### Broken references

None. `docs/02-operating-system/archetype-lens.md` and `source-map.md` exist.

**Summary: COVERAGE FAIL (1 LOSS-MATTERS: the Prompt Return still lacks the risk summary, basis summary, and open gaps). The round-1 over-application is only partly resolved (contract and Prompt), with 1 NEW prompt-tier regression.**

---

## Merge 7: organizing-project-folders + breaking-down-the-work -> drafts/structuring-the-work

### Round-2 status of round-1 findings

| # | Round-1 item | Round-2 status |
|---|---|---|
| L15 | Folders-vs-durable-runtime doctrine pointer | RESOLVED: "`docs/02-operating-system/agentic-workflow-architecture.md` says when folders are enough and when a durable runtime is needed." |
| L16 | Human review gate | RESOLVED in step 6: "a human review gate at each stage boundary" (low residual: Prompt and Verification still lack "human", and the original prompt carried it into the `ng-folders` card) |
| L17 | Capitalized-by-convention exception | RESOLVED: "Files capitalized by convention (`README.md`, `LICENSE`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, and the like)" |
| L18 | No 1:1 WBS-level nesting | RESOLVED: "do not blindly nest one folder per breakdown level"; prompt "not one per level" |
| L19 | Architecture-decision escalation | RESOLVED: "Escalate when you cannot reach one source of truth without an architecture decision" |
| O7 | README for every folder | RESOLVED: prompt "add a README and disposition to each non-trivial folder" |
| O8 | Closed capitalization list | RESOLVED (same fix as L17) |

### Capability table

| Original | Capability | Draft location | Verdict |
|---|---|---|---|
| OPF | Contract: folder maps to one piece/rule, one reason to change, naming/depth checks | Contract | COVERED |
| OPF | Failure class junk-drawer-layout | Contract | COVERED |
| OPF | Outputs: folder map w/ disposition; README stubs; stage layout; naming/depth/single-source check; flagged conflicts | Outputs 2–3 | COVERED |
| OPF | Overview pointer: **`docs/02-operating-system/agentic-workflow-architecture.md`** (folders vs durable runtime) | Step 6: "`docs/02-operating-system/agentic-workflow-architecture.md` says when folders are enough and when a durable runtime is needed." | COVERED (R2 RESOLVED) |
| OPF | Triggers: new tree; where file belongs; junk drawer; WBS→folders; workflow as folders | When to Use 2–3 | COVERED |
| OPF | When Not: obvious file / clean rename; framework-fixed layout | When Not 1–2 | COVERED |
| OPF | When Not: live incident | dropped | ACCEPTABLE-TRIM |
| OPF | When Not: ownership/CI/supply-chain enforcement → other skills | dropped | ACCEPTABLE-TRIM (those skills trigger on their own descriptions) |
| OPF | Inputs: WBS + dictionary; tree/conventions; mission anchor; platform/tooling limits; disposition | Inputs (platform limits dropped) | COVERED |
| OPF | Process 1: pick pattern | Step 6 | COVERED |
| OPF | Process 2: WBS as source of truth; dictionary → folder notes; reverse-engineer if none | Overview "Do only the half you need"; prompt "derive folders from outline numbers" (dictionary→notes dropped) | COVERED |
| OPF | Process 3: folder-decision checklist | Step 7 | COVERED |
| OPF | Process 4: MWP incl. **human review gate at each boundary** (scripts do mechanical work, outputs openable/editable) | Step 6: "a human review gate at each stage boundary" ("scripts do the mechanical work" and "every output ... open and edit" are still dropped) | COVERED (R2 RESOLVED). Low residual: the original prompt said "put a human review gate at each stage boundary", and the generated `commands/ng-folders.md` card projects the prompt. The draft prompt and Verification still say only "a review gate" or nothing. Scripts/editable outputs: ACCEPTABLE-TRIM |
| OPF | Process 5: naming rules incl. **"files normally capitalized by convention" exception** | Step 8: "Files capitalized by convention (`README.md`, `LICENSE`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, and the like) ... are accepted exceptions" | COVERED (R2 RESOLVED) |
| OPF | Process 6: depth/path caps; **do not blindly nest one folder per WBS level** | Step 8: "and do not blindly nest one folder per breakdown level"; prompt: "map folders to outline numbers deliberately, not one per level" | COVERED (R2 RESOLVED) |
| OPF | Process 7: README per **non-trivial** folder (purpose, belongs, not, owner) + disposition | Outputs "per-folder README stubs"; prompt "add a README and disposition per folder" | see over-application |
| OPF | Process 8: respect conventions, least structure, flag conflicts | Step 9 | COVERED |
| OPF | Process 9: output map + check | Outputs 2 | COVERED |
| OPF | Verification: naming; depth; mapping/one home; cohesion/coupling; docs; workflow stages | Verification 3 (documentation check dropped from verification; still in outputs) | COVERED |
| OPF | Escalation: conflict with saved known-good convention | Escalation 2 (`controlling-approved-versions`) | COVERED |
| OPF | Escalation: **cannot reach one source of truth without an architecture decision** | Escalation 2: "Escalate when you cannot reach one source of truth without an architecture decision" | COVERED (R2 RESOLVED) |
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

- Both round-1 risks are resolved ("each non-trivial folder"; the convention exception list is open-ended).
- New: none found.

### Broken references

None. `controlling-approved-versions` is a draft name; `templates/standard/wbs.md`, `templates/standard/stage-contract.md`, and `source-map.md` exist.

**Summary: COVERAGE PASS (0 LOSS-MATTERS). Low residual: "human" review gate is absent from Prompt and Verification, so the `ng-folders` card loses it.**

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

## Per-merge summary (round 2)

1. double-checking-before-acting: COVERAGE FAIL (1 LOSS-MATTERS: public claim left out of the depth-2 list) + 1 NEW over-application
2. learning-from-experience: COVERAGE PASS (0 LOSS-MATTERS)
3. checking-public-claims: COVERAGE PASS (0 LOSS-MATTERS)
4. controlling-approved-versions: COVERAGE PASS (0 LOSS-MATTERS)
5. managing-change-records: COVERAGE PASS (0 LOSS-MATTERS) + 1 NEW over-application
6. briefing-and-handing-off: COVERAGE FAIL (1 LOSS-MATTERS: Prompt Return still lacks risk/basis/open gaps) + over-application partly resolved, 1 NEW prompt-tier regression
7. structuring-the-work: COVERAGE PASS (0 LOSS-MATTERS)

Of the round-1 findings, 18 of 19 LOSS-MATTERS items are resolved (L14 is not; L2 is resolved but left a public-claim residual) and 7 of 8 over-application risks are resolved (O6 is partial). The revision introduced 3 new issues: the M1 unqualified deploy list, the M5 update-path exclusion, and the M6 prompt tier. There are 4 low card-projection residuals (M2, M3 description, M5, M7). The reference counts and the command-parity blocker are unchanged from round 1: the drafts did not touch other repo files, and all 7 prompts still differ from `tests/fixtures/command_prompts.json`.
