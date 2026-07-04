#!/usr/bin/env python3
"""Blind-grade each run's review text against the pre-registered answer key.

Grading is done by a separate, cheap model (Haiku) that never sees which
condition (with_skill / without_skill) produced the text, forced into a
strict JSON schema so the verdict is mechanical, not a free-form judgment.
"""
import json
import re
import statistics as stats
import subprocess
from pathlib import Path

BASE = Path(__file__).parent
RUNS_DIR = BASE / "runs"
ANSWER_KEYS = json.loads((BASE / "answer_keys.json").read_text())
GRADER_MODEL = "claude-haiku-4-5-20251001"

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})

VERDICT_RE = re.compile(r"\b(NOT VERIFIED|INCONCLUSIVE|VERIFIED)\b")


def grade_review(task: str, review_text: str) -> dict:
    criteria = ANSWER_KEYS[task]["pass_criteria"]
    prompt = (
        "You are grading a code review against ONE specific pass criterion. "
        "Do not reward general competence or thoroughness — check ONLY whether "
        "this exact criterion is explicitly satisfied.\n\n"
        f"Pass criterion:\n{criteria}\n\n"
        f"Code review to grade:\n---\n{review_text}\n---\n\n"
        "Answer YES only if the criterion is clearly and explicitly met, "
        "PARTIAL if it is hinted at but not explicit or is materially incomplete, "
        "NO if it is absent."
    )
    cmd = [
        "claude", "-p", prompt,
        "--output-format", "json",
        "--model", GRADER_MODEL,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", "0.20",
        "--json-schema", SCHEMA,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    try:
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
        return verdict
    except Exception as e:
        return {"meets_criteria": "ERROR", "quote": f"{e}: {proc.stdout[:300]}"}


def main():
    rows = []
    for path in sorted(RUNS_DIR.glob("*.json")):
        d = json.loads(path.read_text())
        task = d.get("_task")
        condition = d.get("_condition")
        trial = d.get("_trial")
        if d.get("type") == "error" or d.get("is_error"):
            rows.append({"task": task, "condition": condition, "trial": trial, "error": True})
            continue

        result_text = d.get("result", "")
        usage = d.get("usage", {})
        grade = grade_review(task, result_text)
        verdict_format_present = bool(VERDICT_RE.search(result_text))

        rows.append({
            "task": task,
            "condition": condition,
            "trial": trial,
            "error": False,
            "meets_criteria": grade.get("meets_criteria"),
            "grader_quote": grade.get("quote"),
            "verdict_format_present": verdict_format_present,
            "cost_usd": d.get("total_cost_usd"),
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "cache_read_tokens": usage.get("cache_read_input_tokens"),
            "cache_creation_tokens": usage.get("cache_creation_input_tokens"),
            "num_turns": d.get("num_turns"),
            "duration_ms": d.get("duration_ms"),
        })
        print(f"{task:28s} {condition:15s} trial{trial}  meets_criteria={grade.get('meets_criteria')}  cost=${d.get('total_cost_usd'):.4f}")

    (BASE / "graded_results.json").write_text(json.dumps(rows, indent=2))

    print("\n\n=== SUMMARY ===")
    tasks = sorted(set(r["task"] for r in rows))
    for task in tasks:
        print(f"\n--- {task} ---")
        for condition in ["with_skill", "without_skill"]:
            sub = [r for r in rows if r["task"] == task and r["condition"] == condition and not r["error"]]
            if not sub:
                print(f"  {condition}: no successful runs")
                continue
            catch = sum(1 for r in sub if r["meets_criteria"] == "YES")
            partial = sum(1 for r in sub if r["meets_criteria"] == "PARTIAL")
            n = len(sub)
            verdict_fmt = sum(1 for r in sub if r["verdict_format_present"])
            costs = [r["cost_usd"] for r in sub if r["cost_usd"] is not None]
            out_tok = [r["output_tokens"] for r in sub if r["output_tokens"] is not None]
            in_tok = [(r["input_tokens"] or 0) + (r["cache_creation_tokens"] or 0) + (r["cache_read_tokens"] or 0) for r in sub]
            turns = [r["num_turns"] for r in sub if r["num_turns"] is not None]
            dur = [r["duration_ms"] for r in sub if r["duration_ms"] is not None]
            print(f"  {condition}: caught {catch}/{n} (+{partial} partial), verdict-format {verdict_fmt}/{n}")
            print(f"    cost: mean=${stats.mean(costs):.4f} (n={n})  | output_tok: mean={stats.mean(out_tok):.0f} | input+cache_tok: mean={stats.mean(in_tok):.0f} | turns: mean={stats.mean(turns):.1f} | duration_ms: mean={stats.mean(dur):.0f}")


if __name__ == "__main__":
    main()
