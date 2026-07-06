#!/usr/bin/env python3
"""Routing validation: does the amended description fix the selection ambiguity?

Nothing else in this project tests skill SELECTION (description-matching) --
everything else force-loads a skill's content directly. This tests whether a
model, given only name+description for a small set of skills, picks the right
one for a handoff scenario -- before vs after the briefing-an-agent amendment.
"""
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).parent
RUNS_DIR = BASE / "routing_runs"
RUNS_DIR.mkdir(exist_ok=True)

MODEL = "claude-sonnet-5"
TOOLS = ""
MAX_BUDGET_USD = "0.30"
# Isolation/session flags that also shape what the subject model can do --
# named here (not inlined in cmd below) so the hash and the actual command
# are built from the exact same list and can never drift apart, the same
# fix already applied to TOOLS/MAX_BUDGET_USD.
HARNESS_FLAGS = ["--safe-mode", "--no-session-persistence"]

OLD_BRIEFING_DESC = (
    "briefing-an-agent: Prepares focused context for an AI agent, reviewer, verifier, or "
    "releaser, with a clear role, goal anchor, authority, evidence to produce, forbidden "
    "actions, and stop conditions. Use when handing off or resuming work that matters. Do "
    "not use for a tiny self-contained task that needs no handoff."
)
NEW_BRIEFING_DESC = (
    "briefing-an-agent: Prepares focused context for an AI agent, reviewer, verifier, or "
    "releaser at the start of a task, with a clear role, goal anchor, authority, evidence "
    "to produce, forbidden actions, and stop conditions. Use when an agent or reviewer is "
    "about to begin work and needs bounded context before it starts. Do not use for a tiny "
    "self-contained task that needs no briefing, or for transferring already-open work to "
    "a new owner, which is handing-off-work."
)
HANDING_OFF_DESC = (
    "handing-off-work: Hands off unfinished work with a closed-loop briefing of state, "
    "changed conditions, remaining scope, authority limits, and open evidence. Use when "
    "AI-agent, reviewer, verifier, releaser, or resumed-thread work transfers to a new "
    "owner. Do not use when the same owner continues uninterrupted with full context."
)
DECOY_1 = (
    "declaring-intent: States what an agent intends to do and why before a critical or "
    "irreversible action, so a reviewer can challenge the thinking and not just the "
    "result. Use before deploys, migrations, public claims, or trust changes that deserve "
    "a stated intent, expected result, abort criteria, and backup. Do not use for routine "
    "reversible edits, and never treat the stated intent as proof the agent understood."
)
DECOY_2 = (
    "checking-release-readiness: Records a ship, block, defer, or ship-with-risk decision "
    "that ties baseline, evidence status, residual risk, rollback, monitoring, and handoff "
    "together. Use when a packet, PR, release, dependency change, or agent-authority "
    "change approaches merge. Do not use early in development before evidence exists."
)

SCENARIO = (
    "My own coding session just got cut off mid-task and I need to hand this off to a "
    "fresh agent instance right now. The new agent needs to know what's done, what changed, "
    "what's left, and what it's allowed to do before it picks up the work."
)

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "chosen_skill": {"type": "string"},
        "reasoning": {"type": "string"},
    },
    "required": ["chosen_skill", "reasoning"],
})


def build_prompt(briefing_desc):
    skills_block = "\n\n".join([briefing_desc, HANDING_OFF_DESC, DECOY_1, DECOY_2])
    return (
        "You have access to the following skills. Each has a name and a description "
        "that states when to use it and when not to. Read only the descriptions below -- "
        "you do not have the skills' full content, only this routing information.\n\n"
        f"{skills_block}\n\n"
        f"Situation:\n{SCENARIO}\n\n"
        "Which ONE skill best applies to this situation? Answer with the exact skill name "
        "and a one-sentence reason."
    )


def input_spec_hash(prompt):
    """Fingerprint of everything that determines the subject-model call's
    output besides its own randomness: the fully-built prompt (which already
    captures SCENARIO, the variant's briefing description, and the fixed
    skill descriptions it's compared against) plus the harness settings
    (model, tools, budget, HARNESS_FLAGS). A persisted run file is only
    reused if this matches -- editing SCENARIO or any skill description
    must force a fresh call even if the old routing_runs/ file is still on
    disk from before the edit."""
    return hashlib.sha256(
        f"{prompt}::{MODEL}::{TOOLS}::{MAX_BUDGET_USD}::{'::'.join(HARNESS_FLAGS)}".encode()
    ).hexdigest()


def run_one(variant, briefing_desc, trial):
    prompt = build_prompt(briefing_desc)
    out_path = RUNS_DIR / f"{variant}__trial{trial}.json"
    spec_hash = input_spec_hash(prompt)
    if out_path.exists():
        existing = json.loads(out_path.read_text())
        # Never treat a cached ERROR record as a hit, even with a matching
        # hash -- a transient failure must always be retried on the next
        # invocation, not replayed forever until someone manually deletes
        # the file.
        if existing.get("_input_spec_sha256") == spec_hash and existing.get("type") != "error":
            return existing
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", MODEL,
           "--tools", TOOLS, "--max-budget-usd", MAX_BUDGET_USD, *HARNESS_FLAGS,
           "--json-schema", SCHEMA]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
        result = {"variant": variant, "trial": trial, "chosen_skill": verdict["chosen_skill"],
                  "reasoning": verdict["reasoning"]}
    except subprocess.TimeoutExpired:
        result = {"variant": variant, "trial": trial, "type": "error", "error": "timeout"}
    except (json.JSONDecodeError, KeyError) as e:
        result = {"variant": variant, "trial": trial, "type": "error",
                  "error": f"non-json or malformed output: {e}"}
    result["_input_spec_sha256"] = spec_hash
    out_path.write_text(json.dumps(result, indent=2))
    return result


def main():
    jobs = []
    for trial in range(1, 6):
        jobs.append(("old_description", OLD_BRIEFING_DESC, trial))
        jobs.append(("new_description", NEW_BRIEFING_DESC, trial))
    results = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(run_one, *j): j for j in jobs}
        for fut in as_completed(futs):
            results.append(fut.result())
    (BASE / "routing_results.json").write_text(json.dumps(results, indent=2))
    failures = sum(1 for r in results if r.get("type") == "error")
    for variant in ["old_description", "new_description"]:
        sub = [r for r in results if r["variant"] == variant and not r.get("type") == "error"]
        correct = sum(1 for r in sub if "handing-off-work" in r["chosen_skill"].lower())
        print(f"{variant}: chose handing-off-work {correct}/{len(sub)} times")
        for r in sorted(sub, key=lambda r: r["trial"]):
            print(" ", r["trial"], r["chosen_skill"], "|", r["reasoning"][:150])
    if failures:
        print(f"{failures}/{len(results)} job(s) recorded an error -- see the persisted "
              f"error rows in {RUNS_DIR}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
