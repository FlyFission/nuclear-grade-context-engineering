# Challenge results

Run coding agents on the [15-minute challenge](../challenge/README.md) many times, score every
run the same way, and publish everything. Read [`METHOD.md`](METHOD.md) first: it explains the
two tracks, the outcomes, and the limits.

## Run it

Use a throwaway container or VM. The agent commands in `agents.json` let the agent act without
asking, and the scorer runs code the agent wrote. You need Python 3.11+, `git`, `pytest`, and
the agent's own CLI, signed in. Set `NG_CONTAINER_IMAGE` to the image you run in, so each
result records it.

```bash
python challenge-results/run.py --agent claude-code --model <model-id> --track rules --trials 5
python challenge-results/run.py --agent claude-code --model <model-id> --track plain --trials 5
python challenge-results/build.py
```

Or run every agent CLI you have installed on both tracks in one go, then rebuild:

```bash
python challenge-results/run-all.py --trials 5 --model claude-code=<model-id>
```

`run.py` writes one JSON file, one transcript, and one diff per run into `results/`.
`build.py` turns them into `RESULTS.md`, `results.json`, the one-page scoreboard at
[`docs/scoreboard/index.html`](../docs/scoreboard/index.html) (each agent's task-only runs
beside its house-rules runs, plus what each silent run changed, with links to its transcript
and diff), and the `badge.json` endpoint badge. With GitHub Pages serving `docs/` from `main`,
the page is at `https://flyfission.github.io/nuclear-grade-context-engineering/scoreboard/`.

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
| `run-all.py` | Runs every installed agent on both tracks, then `build.py` |
| `disclosure.py` | A keyword read of the agent's final words |
| `build.py` | Builds `RESULTS.md`, the scoreboard page and the badge from the run files |
| `adjudications.json` | Human rulings that replace an automatic outcome |
| `CORRECTIONS.md` | Every change to a published result |
| `tracks/plain/` | The task-only `AGENTS.md` |
