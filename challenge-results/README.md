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

## Run a round in containers

`container/round.sh` does the whole round with Docker. Each agent gets its own fresh
container with only its own sign-in passed in, the repo mounted read-only so no agent can
reach the scorer, and the image digest saved with every run. Sign-ins stay outside the repo:
variables in `~/.ng-challenge/agents.env` (one `KEY=value` per line, for example
`CLAUDE_CODE_OAUTH_TOKEN`, `OPENAI_API_KEY`, `GEMINI_API_KEY`), and, for CLIs that keep their
sign-in in a file, a home folder per agent at `~/.ng-challenge/home/<agent>/` (for example
`~/.ng-challenge/home/codex/.codex/auth.json`). Each agent sees only its own. Then name the
agents you signed in for:

```bash
challenge-results/container/round.sh --agents claude-code,codex,gemini-cli --trials 5
```

Tool versions are pinned in `container/Dockerfile`. Changing one starts a new row.

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
| `container/` | The pinned image and `round.sh`, which runs a round one container per agent |
| `disclosure.py` | A keyword read of the agent's final words |
| `build.py` | Builds `RESULTS.md`, the scoreboard page and the badge from the run files |
| `adjudications.json` | Human rulings that replace an automatic outcome |
| `CORRECTIONS.md` | Every change to a published result |
| `tracks/plain/` | The task-only `AGENTS.md` |
