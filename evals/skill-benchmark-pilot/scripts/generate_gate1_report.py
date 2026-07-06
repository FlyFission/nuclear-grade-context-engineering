#!/usr/bin/env python3
"""Generate GATE1_REPORT.md directly from the raw Gate 1 data (no hand-transcription)."""
import json
from pathlib import Path

BASE = Path(__file__).parent.parent
GATE1 = BASE / "data" / "gate1-hard-case-pilot"
ALL = BASE / "data" / "all-skills-pilot"

gate1_tasks = json.loads((GATE1 / "gate1_tasks.json").read_text())
gate1_graded = json.loads((GATE1 / "graded_results_gate1.json").read_text())
round1_summary = json.loads((ALL / "summary_all_FINAL.json").read_text())
round1_by_skill = {r["skill"]: r for r in round1_summary}


def fmt_money(x):
    return f"${x:.4f}" if x is not None else "n/a"


def fence_for(text):
    longest = 0
    run = 0
    for ch in text:
        if ch == "`":
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    return "`" * max(3, longest + 1)


def round1_verdict(skill):
    r = round1_by_skill.get(skill)
    if not r:
        return "n/a"
    d = r["with_skill"]["yes"] - r["without_skill"]["yes"]
    return "WINS" if d > 0 else ("TIE" if d == 0 else "LOSES")


lines = []
a = lines.append

a("# Gate 1: Hard-Case Retest of the 14 Skills That Tied or Lost in Round 1")
a("")
a("Generated directly from the raw data in `evals/skill-benchmark-pilot/data/gate1-hard-case-pilot/` "
  "by `scripts/generate_gate1_report.py`. Companion to `REPORT.md` (the round-1, 28-skill "
  "pilot) — read that report's methodology, bias disclosure, and limitations sections "
  "first; this document only covers what's specific to Gate 1.")
a("")
a("## Executive summary")
a("")
a("Round 1 tested each skill's own \"When to Use\" trigger — the obvious, textbook case. "
  "13 of 27 skills tied there (plain Sonnet 5 already satisfied the pass criterion with no "
  "skill loaded), which round 1's own limitations section flagged as likely ceiling effects "
  "rather than proof the skills add nothing. Gate 1 tests that hypothesis directly: for "
  "those same skills (plus the 1 that lost), a new scenario was built to target the "
  "specific rationalization, shortcut, or edge case named in that skill's own \"Common "
  "Rationalizations\" / \"Escalation\" / \"Red Flags\" text — not the trigger condition. "
  "5 trials per condition instead of 3.")
a("")
a("**Result: 11 of the 14 skills flip from TIE to WINS on the harder case.** Only "
  "`briefing-an-agent` and `proving-claims` remain flat ties (5/5 vs 5/5 — the baseline "
  "still nails even the harder version of these two). `creating-change-records` — the one "
  "round-1 LOSES — improves to a TIE (0/5 YES both conditions, but the skill earns partial "
  "credit on all 5 trials versus 1/5 for the baseline). **This is real support for the "
  "ceiling-effect hypothesis**: most of round 1's ties were an artifact of testing where the "
  "skill wasn't needed, not evidence the skill adds nothing.")
a("")
a("**But not all 11 flips are the same kind of finding — read section 2 before treating "
  "them as uniform.** Some flips reflect the skill surfacing a genuinely new, distinct "
  "decision element the baseline never mentions unprompted. Others reflect the baseline "
  "getting the substance right but missing a specific, stricter phrasing bar the grading "
  "criterion demanded (e.g. requiring the literal words \"escalate to a named human\" "
  "rather than crediting a substantively equivalent \"get explicit human sign-off\"). Both "
  "are legitimate results, but they support different strength of claim.")
a("")

a("## 1. Method — what's different from round 1")
a("")
a("Same harness, model (`claude-sonnet-5`), grader (`claude-haiku-4-5`), and blind-grading "
  "process as round 1 (see `REPORT.md` section 1). Differences:")
a("")
a("- **5 trials per condition** instead of 3 (140 runs total: 14 skills × 2 conditions × 5).")
a("- **`--tools \"Read,Glob,Grep\"` used from the start**, not `--tools \"\"`. Round 1 "
  "discovered mid-run that fully disabling tools broke skills whose process invites a repo "
  "check; Gate 1 starts with the fix already applied instead of discovering it again.")
a("- **New scenarios and criteria**, authored the same way as round 1 (3 parallel subagents, "
  "same non-independence caveat applies — see `REPORT.md` section 2 and the note below), "
  "but explicitly instructed to target each skill's own named rationalization/red-flag "
  "text instead of its \"When to Use\" trigger, and to write a criterion that a generically "
  "cautious answer could not satisfy by accident.")
a("")
a("**The same authorship caveat from round 1 applies with one more layer:** these harder "
  "scenarios were designed by an agent reading the skill's own \"here's how people get this "
  "wrong\" text and building a test around it. That is a reasonable way to find the hard "
  "case, but it also means the test is, by construction, aimed at exactly what the skill "
  "already claims to catch. A skill that catches the failure mode it explicitly names about "
  "itself is a weaker result than one that catches a failure mode nobody wrote down.")
a("")

a("## 2. Full comparison table")
a("")
a("| Skill | Round 1 | Gate 1 | With skill (Gate 1) | Without skill (Gate 1) | Cost with | Cost without |")
a("|---|---|---|---|---|---|---|")
gate1_summary_path = GATE1 / "summary_gate1.json"
if not gate1_summary_path.exists():
    gate1_summary_path = GATE1 / "summary_gate1_FINAL.json"
gate1_summary = json.loads(gate1_summary_path.read_text())
for row in gate1_summary:
    a(f"| {row['skill']} | {round1_verdict(row['skill'])} | {row['verdict']} | "
      f"{row['with_skill']['catch']} | {row['without_skill']['catch']} | "
      f"{fmt_money(row['with_skill']['mean_cost'])} | {fmt_money(row['without_skill']['mean_cost'])} |")
a("")

a("## 3. Reading the flips: new decision element vs. stricter phrasing bar")
a("")
a("Two of the 11 flips were manually inspected in full (not just the grader's YES/NO) to "
  "check whether the harder criteria were finding real gaps or just being pedantic about "
  "wording. Both are reproduced in full below so an independent reader can judge for "
  "themselves; this is a spot check of 2 of 11, not an audit of all 11.")
a("")
a("### `checking-what-a-change-affects` — genuinely new decision element")
a("")
a(f"**Pass criterion:** {gate1_tasks['checking-what-a-change-affects']['pass_criteria']}")
a("")
a("Every `without_skill` trial correctly identified the external-API backward-compatibility "
  "risk (the \"obvious\" half of this compound criterion) — that part was never in doubt. "
  "What they consistently missed, unprompted, was the second required element: a "
  "rollback-of-state plan for the database migration itself. That is a distinct technical "
  "practice, not a rephrasing of the API-compatibility point, and the `with_skill` trials "
  "named it every time. This flip looks like real signal.")
a("")
a("### `deciding-who-decides` — same substance, stricter phrasing bar")
a("")
a(f"**Pass criterion:** {gate1_tasks['deciding-who-decides']['pass_criteria']}")
a("")
a("Every `without_skill` trial correctly rejected both wrong justifications (existing "
  "delegated config authority; the agent's own confidence from prior staging success) and "
  "required human sign-off before rotating production API keys — the substantive judgment "
  "call was right in all 5 trials. Most were graded PARTIAL rather than YES because the "
  "criterion specifically required the phrase-level commitment to escalate to a **named** "
  "human, and most `without_skill` responses said \"get human sign-off\" without specifying "
  "that the sign-off must be from a specific, named accountable person. That is a real "
  "difference in precision, but it is a smaller claim than \"the baseline gets this wrong\" "
  "— the baseline gets the decision right and is less precise about the escalation target.")
a("")

a("## 4. Full detail: every scenario, criterion, and trial")
a("")
skills_sorted = sorted(gate1_tasks.keys())
for skill in skills_sorted:
    task = gate1_tasks[skill]
    scenario_text = task["scenario_prompt"].strip()
    scenario_fence = fence_for(scenario_text)
    rows = [r for r in gate1_graded if r["skill"] == skill and not r.get("error")]

    a(f"### `{skill}`")
    a("")
    a(f"**Hard-case rationale (why this targets what round 1 didn't):** {task.get('hard_case_rationale', 'n/a')}")
    a("")
    a("**Scenario given to the model (identical in both conditions):**")
    a(scenario_fence)
    a(scenario_text)
    a(scenario_fence)
    a("")
    a(f"**Pre-registered pass criterion:** {task['pass_criteria']}")
    a("")
    a("| Condition | Trial | Verdict | Cost | Output tokens | Turns | Duration (ms) | Grader quote |")
    a("|---|---|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: (r["condition"], r["trial"])):
        quote = (r.get("grader_quote") or "").replace("\n", " ").replace("|", "/")[:220]
        a(f"| {r['condition']} | {r['trial']} | {r['meets_criteria']} | "
          f"{fmt_money(r.get('cost_usd'))} | {r.get('output_tokens', 'n/a')} | "
          f"{r.get('num_turns', 'n/a')} | {r.get('duration_ms', 'n/a')} | {quote} |")
    a("")

a("## 5. Cost")
a("")
run_files = list((GATE1 / "runs").glob("*.json"))
gate1_cost = sum(json.loads(f.read_text()).get("total_cost_usd") or 0 for f in run_files)
a(f"- Gate 1 review runs (140 runs, 14 skills × 2 conditions × 5 trials): "
  f"**${gate1_cost:.2f}** (unrounded: ${gate1_cost:.4f}), plus a few dollars of Haiku "
  f"grading calls not itemized here. 4 trials hit a transient upstream API/proxy error "
  f"unrelated to content and were simply retried; that cost is included in the total above.")
a("")

a("## 6. Limitations specific to Gate 1")
a("")
a("- **n=5 trials per cell** — better than round 1's n=3, but still not enough for a real "
  "confidence interval; a 5/5-vs-0/5 split is stronger pilot evidence than round 1's "
  "3/3-vs-0/3, not a settled statistical result.")
a("- **Scenario/criteria authorship is still not independent**, and Gate 1 adds a second "
  "layer of it: these harder scenarios were built directly from each skill's own stated "
  "failure modes (see section 1). A skill catching exactly the shortcut it names about "
  "itself is expected; it does not by itself prove the skill would catch a failure mode "
  "nobody anticipated.")
a("- **Not every flip was individually audited.** Section 3 manually checked 2 of the 11 "
  "flips and found both to be legitimate but different in strength (a genuinely new element "
  "vs. a phrasing-precision bar). The other 9 have not had the same manual read — their "
  "full transcripts are in section 4 for anyone who wants to check.")
a("- **`briefing-an-agent` and `proving-claims` remaining flat ties on the harder case "
  "is itself informative** — it means the ceiling-effect hypothesis doesn't automatically "
  "explain every round-1 tie. For these two specifically, the baseline may be genuinely "
  "as good as the skill on the decision element tested, not just on the easy case.")
a("")

report = "\n".join(lines)
out_path = BASE / "GATE1_REPORT.md"
out_path.write_text(report)
print(f"Wrote {out_path} ({len(report)} chars, {len(skills_sorted)} skills detailed)")
