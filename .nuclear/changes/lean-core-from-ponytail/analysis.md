# Ponytail, read closely

What Ponytail is, why it works on a model, where it stops, and what the same reading says about Nuclear-grade. Facts are from the Ponytail repository as read on 2026-11-07 (`README.md`, `skills/ponytail/SKILL.md`, `AGENTS.md`, `commands/*.toml`, `benchmarks/results/2026-10-07-agentic.md`). Its numbers are its author's self-report, not ours.

## 1. What it is

- One prompt. `skills/ponytail/SKILL.md` is 592 words. `AGENTS.md` is 473 words and is the same body without the frontmatter and level table. The README says: "Everything else in this repo loads that prompt into different agents." Twenty hosts, one text.
- Six commands: `/ponytail [lite|full|ultra|off]`, `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help`. Each is one paragraph.
- Three levels. `lite` builds what was asked and names the smaller option. `full` is the rules. `ultra` also questions the request. Levels are user-chosen intensity, kept across a session by two small hooks.
- A benchmark: 39 tasks, 3 arms (Ponytail 5, Ponytail 4.13, no skill), 5 runs each, one model, headless Claude Code. Reported: 53% fewer lines, 26% lower cost, a test left behind on 98% of risky logic against 68% without. It also reports a loss: where a test existed, the no-skill tests caught more injected bugs (77% against 69%).

## 2. Anatomy: the eight parts and why each works on a model

| Part | The text | Mechanism |
|---|---|---|
| Persona | "You are a lazy senior developer. The best code is the code never written." | One image carries a whole value system. The model already knows this person. No doctrine needed. |
| Read first | "Read the task and the code it touches. List every place your change must reach ... That is scope. Extra features are not." | Puts the only non-lazy step first and names what counts as scope, so "lazy" cannot be read as "skip the reading". |
| The ladder | Six rungs, "Take the first option that fully works." | An ordered search with a stopping rule. Models follow a numbered first-hit procedure far better than a value ("prefer simplicity"). |
| Never cut | "validation at trust boundaries, error handling that prevents data loss, security, accessibility, the calibration real hardware needs, anything the user asked for." | A vague value (safety) becomes an enumerated floor. The list is short enough to check against every edit. |
| Test trigger | "a branch, a loop, a parser, money or security, or a whole new script or app" leaves "one small test or an assert-based self-check." | A concrete trigger list and a bounded cost ("one small test"). The 98% figure is this line working. |
| Debt marker | `shortcut: <the limit>, <when to upgrade>` plus `/ponytail-debt` which greps them into a ledger. | Deferred work becomes a controlled item for the cost of one comment. The harvester flags markers with no trigger, "those rot silently". |
| Receipt | "End your reply with one or two lines: what you skipped or did not check, and any risk the user must know." | Every turn ends with the gap statement. Two lines, always, so the human's trust recalibrates every turn. |
| Review | Reads callers, not the diff. Findings as Must / Should / Nice, each with What this is, Problem, Fix, If we skip it. Ends "Verdict:", "Not checked:". "Change no code." A marked shortcut "is a decision, not a finding." | Consequence stated per finding; the reviewer separated from the fixer; accepted debt not re-litigated. |

Two sentences carry the whole balance: "Lazy about the solution, never about reading." and "Lazy, not negligent."

## 3. Why the whole is small and still holds

1. It is always on and fits the attention budget. Our own `context-window-discipline.md` says recall decays with length and that always-loaded files should hold "exact commands, constraints, and non-obvious gotchas that change action". Ponytail is only that.
2. Every line is an action at the moment of action: read, list, grep, take the first option, leave a test, end with two lines. There is no "consider", "ensure", or doctrine.
3. The ladder and the floor replace judgment with procedure where procedure is enough, and leave judgment only where it is needed (rung 1 and `ultra`).
4. The record is cheap and durable where it matters: `shortcut:` comments live in the code, so `git grep` is the register.
5. It measures the claim it makes (less code, tests present) and prints the number that went the wrong way.
6. One source, rendered. The compact and full forms are the same words, so they cannot drift.

## 4. Where it stops

This is the ground Nuclear-grade stands on. Ponytail has:

- No consequence grading. A typo and an auth change get the same rules. The floor is the only escalation.
- No human gate. Nothing in the prompt routes a decision to a person.
- No evidence custody. The receipt is the agent's own report of what it skipped. `/ponytail-review` is the same model reviewing its own diff, and it ends with "Ship."
- No record outside the transcript except the `shortcut:` marker and, in Claude Code, the cost band.
- Levels chosen by mood, not stakes.

Its benchmark is author-run, on author-written tasks, with one model; the author says so.

## 5. The mirror: Nuclear-grade measured the same way

Reproducible with `python tools/ng.py tokens .` and `wc -w skills/*/SKILL.md` at commit `06e762e`.

| Surface | Nuclear-grade | Ponytail |
|---|---|---|
| Always-on skill descriptions | 3,409 tokens (31) | one description |
| Core 7 bodies when selected | 19,476 tokens | the whole prompt is ~800 tokens |
| Mean skill body | 1,208 words; p95 3,212 tokens | 592 words total |
| Command cards | 30 cards, 29,842 tokens, largest 1,700 | 6 paragraphs |
| Places the mode rule is restated | at least 7: `hooks/session_start.py`, `hooks/user_prompt_submit.py`, `skills/using-nuclear-grade`, `skills/rating-change-risk`, `CORE.md`, `QUICKSTART.md`, `AGENTS.md` | 2, and they are the same words |
| Assurance disclaimer | 170 occurrences in 155 files | none needed |
| Measured prose | 481,847 tokens | one README |

Two results from our own evals decide what to do about it:

- `evals/skill-control-ladder/REPORT.md`: the full skill (C4, mean 1,100 appended words) against the same skill compressed to five imperative bullets (C3, 127 words) scores +0.062, 6 higher, 0 lower, 21 tied. On the seven hard scenarios (`REPORT-hard.md`) the difference is +0.000. Nine tenths of the words buy a small effect on easy cases and nothing measured on hard ones.
- `evals/skill-consolidation/REPORT.md`: merging 31 skills into 23 failed on fit; every merge was reverted or not made. The catalog count is not the lever. Body length and register are.

So the tension the maintainer feels is real and is measured: the doctrine is deep, the operative surface is heavy, and our own pages (`token-burn-control.md`, `MAXIMS.md` "minimum sufficient context", `CORE.md` "Core 7") already say what Ponytail does. We preach the smallest honest context and ship 1,200-word skills.

## 6. The balance, stated once

Ponytail is lazy about the solution and never about reading.
Nuclear-grade must be lazy about the ceremony and never about the evidence.

Rigor lives in three places and only three: the floor that is never cut, the graded escalation when stakes appear, and who controlled the evidence. Everything else should be Ponytail-sized.

Where rigor wins and Ponytail's pattern is not adopted:

- Same-agent review as the verdict. The verdict on anything trust-bearing stays with a named person, or a panel that can fail differently.
- The receipt as the only record. For Standard-plus work the receipt is necessary and not sufficient; the record stays.
- "Ship." from the reviewer. The ship decision is a separate step with a name on it.
- Intensity by mood. Mode is set by consequence, and the one fact that sets it is said before the first write.
- "Never cut anything the user asked for." Here the agent may stop and escalate unsafe or unclear work; that stays.

## 7. What to port, and what not

| Principle | Ponytail form | Nuclear-grade form |
|---|---|---|
| One ladder with a stopping rule | six rungs for code | six rungs for rigor: floor, existing proof, one-command proof, Quick record, Standard record, human gate |
| An enumerated floor | "Never cut: ..." | five things never waived in any mode |
| A receipt every turn | two lines | one fixed receipt of at most five lines, replacing the prose completion standard |
| Read first, then act | callers, tests, fixtures, config | the bounded read-only preflight we already require, said in one line |
| Concrete trigger lists | branch, loop, parser, money, security | the Standard-plus traps we already have, kept to one line each |
| Debt made greppable | `shortcut:` plus a harvester | recognize `shortcut:` and `deferred:`; `ng debt` harvests; no-trigger markers flagged |
| Review that states consequence and changes no code | What / Problem / Fix / If we skip it; Verdict; Not checked | the same shape in `reviewing-code-quality` and the ship review; an accepted gap is a decision, not a finding |
| One source rendered to every host | SKILL.md body equals AGENTS.md body | one card; the hook preamble, the starter `AGENTS.md`, and `CORE.md` are tested for parity with it |
| Measure the claim you make and print the loss | benchmark with the 77% against 69% line | the control ladder and the routing cases re-run after every lean pass; a drop is reported, not explained away |
| Persona compression | the lazy senior dev | an open decision for the maintainer; see `plan.md` D1 |
| Levels | lite / full / ultra | not ported; mode by consequence stays |

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`plan.md`](plan.md)
- Ponytail: https://github.com/DietrichGebert/ponytail (MIT)
- [`evals/skill-control-ladder/REPORT.md`](../../../evals/skill-control-ladder/REPORT.md)
- [`evals/skill-consolidation/REPORT.md`](../../../evals/skill-consolidation/REPORT.md)
- [`docs/05-reference/skills-token-audit.md`](../../../docs/05-reference/skills-token-audit.md)

## Exit criteria

- Every quoted Ponytail line is in the fetched files named at the top.
- Every Nuclear-grade number has a command or a report path.
- The table in section 7 is the list `basis.md` turns into requirements.

## Source-lineage note

Original design inspection by this repository's maintainer with AI assistance. Ponytail is MIT-licensed and quoted under that license; its results are its author's. Lineage for the Nuclear-grade side is mapped in `docs/00-standards-foundation/source-map.md`. This note makes no efficacy claim about either project and creates no assurance or compliance.
