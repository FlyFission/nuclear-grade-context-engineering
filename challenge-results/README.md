# Challenge results

Run coding agents on the [15-minute challenge](../challenge/README.md) many times, score every
run the same way, and publish everything. Read [`METHOD.md`](METHOD.md) first: it explains the
two tracks, the outcomes, and the limits.

## Run it

Use a throwaway container or VM. The agent commands in `agents.json` let the agent act without
asking, and the scorer runs code the agent wrote. You need Python 3.11+, `git`, `pytest`, and
the agent's own CLI, signed in.

```bash
python challenge-results/run.py --agent claude-code --model <model-id> --track rules --trials 5
python challenge-results/run.py --agent claude-code --model <model-id> --track plain --trials 5
python challenge-results/build.py
```

`run.py` writes one JSON file, one transcript, and one diff per run into `results/`.
`build.py` turns them into `RESULTS.md` and `results.json`.

Check each CLI's flags with `--help` before a scored run. They change between releases, and
the version you used is saved with every run.

## Post your own result

Ran it on your agent? Share the JSON file and transcript with the
[challenge result form](../.github/ISSUE_TEMPLATE/challenge_result.yml). We add outside runs to
the results with your name on them, after a quick check that they match the method.

## Files

| File | What it is |
|---|---|
| `METHOD.md` | The rules, written before any run |
| `agents.json` | Agent CLIs and the flags used to run them |
| `run.py` | Runs one agent on fresh copies of the challenge and scores each run |
| `disclosure.py` | A keyword read of the agent's final words |
| `build.py` | Builds `RESULTS.md` from the run files |
| `adjudications.json` | Human rulings that replace an automatic outcome |
| `CORRECTIONS.md` | Every change to a published result |
| `tracks/plain/` | The task-only `AGENTS.md` |
