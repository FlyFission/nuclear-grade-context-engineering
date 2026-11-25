#!/usr/bin/env bash
# Run one challenge round in throwaway containers, then rebuild the scoreboard.
#
#   challenge-results/container/round.sh --agents claude-code,codex,gemini-cli \
#       [--trials 5] [--timeout 1800] [--model codex=<id>]...
#
# Works with the bash that ships with macOS. Every run gets its own fresh container:
# - the repo is mounted read-only, so no agent can change the scorer or harness. The
#   challenge is open-book, so reading them is allowed, as it is in challenge/README.md;
# - the host's results folder is hidden behind an empty folder, and the run writes its
#   files inside the container, copied out only after the container stops. No agent can
#   read or change another run's evidence;
# - only that agent's own sign-in is passed in (a home folder read-only), copied into a fresh home
#   folder, so nothing an agent leaves behind reaches its next run;
# - the container runs as your own user, with the image digest saved in every run.
#
# Sign-ins live outside the repo, so they are never copied, mounted or committed:
# - ~/.ng-challenge/agents.env (or NG_AGENTS_ENV): one KEY=value per line. It is read as
#   data, never run as shell code, and each agent sees only its own keys (keys_for).
# - ~/.ng-challenge/home/<agent>/ (or NG_HOME_ROOT/<agent>/): copied into that agent's
#   home folder at the start of each run, for CLIs that keep their sign-in in a file
#   (for example .codex/auth.json or .gemini/).
# An agent with no sign-in still runs, and its failed runs are published like any
# other (METHOD.md, How many runs), so name only agents you have signed in for.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo="$(cd "$here/../.." && pwd)"
image="${NG_IMAGE:-ng-challenge}"
env_file="${NG_AGENTS_ENV:-$HOME/.ng-challenge/agents.env}"
home_root="${NG_HOME_ROOT:-$HOME/.ng-challenge/home}"
results="$repo/challenge-results/results"

# The sign-in variables each agent may see. Nothing else from the file is passed.
keys_for() {
  case "$1" in
    claude-code) echo "ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN" ;;
    codex) echo "OPENAI_API_KEY CODEX_API_KEY" ;;
    gemini-cli) echo "GEMINI_API_KEY GOOGLE_API_KEY" ;;
    copilot-cli) echo "COPILOT_GITHUB_TOKEN" ;;
    cursor-agent) echo "CURSOR_API_KEY" ;;
    opencode) echo "OPENCODE_API_KEY ANTHROPIC_API_KEY OPENAI_API_KEY" ;;
    aider) echo "ANTHROPIC_API_KEY OPENAI_API_KEY" ;;
    *) echo "" ;;
  esac
}

# Print the value of KEY from the env file, without running the file.
env_value() {
  [[ -f "$env_file" ]] || return 0
  local line key value
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line#"${line%%[![:space:]]*}"}"
    [[ -z "$line" || "$line" == \#* ]] && continue
    line="${line#export }"
    key="${line%%=*}"
    [[ "$key" == "$1" ]] || continue
    value="${line#*=}"
    if [[ "$value" == \"*\" || "$value" == \'*\' ]]; then
      value="${value:1:${#value}-2}"
    fi
    printf '%s' "$value"
  done < "$env_file"
}

agents=""
trials=5
timeout=1800
models=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agents) agents="$2"; shift 2 ;;
    --agents=*) agents="${1#--agents=}"; shift ;;
    --trials) trials="$2"; shift 2 ;;
    --trials=*) trials="${1#--trials=}"; shift ;;
    --timeout) timeout="$2"; shift 2 ;;
    --timeout=*) timeout="${1#--timeout=}"; shift ;;
    --model) models+=("$2"); shift 2 ;;
    --model=*) models+=("${1#--model=}"); shift ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done
if [[ -z "$agents" ]]; then
  echo "name the agents you have signed in for: --agents claude-code,codex,..." >&2
  exit 2
fi
[[ "$trials" =~ ^[1-9][0-9]*$ ]] || { echo "--trials takes a whole number" >&2; exit 2; }
[[ "$timeout" =~ ^[1-9][0-9]*$ ]] || { echo "--timeout takes seconds" >&2; exit 2; }

model_for() {
  local entry
  for entry in ${models[@]+"${models[@]}"}; do
    if [[ "${entry%%=*}" == "$1" ]]; then
      printf '%s' "${entry#*=}"
      return
    fi
  done
}

if [[ -z "${NG_SKIP_BUILD:-}" ]]; then
  docker build -q -t "$image" "$here" >/dev/null
fi
digest="$(docker image inspect --format '{{.Id}}' "$image")"
mkdir -p "$results"
empty="$(mktemp -d)"
private="$(mktemp -d)"
chmod 700 "$private"
trap 'rm -rf "$empty" "$private"' EXIT

# Your own user, so a CLI that refuses to run as root still runs. As root, use the
# image's own user instead.
run_as="$(id -u):$(id -g)"
if [[ "$(id -u)" == "0" ]]; then
  run_as="runner"
fi

failed=0
IFS=',' read -r -a names <<< "$agents"
for name in "${names[@]}"; do
  # Values go through a private file, so they never show up in the process list.
  agent_env="$private/$name.env"
  : > "$agent_env"
  passed=0
  for key in $(keys_for "$name"); do
    value="$(env_value "$key")"
    if [[ -n "$value" ]]; then
      printf '%s=%s\n' "$key" "$value" >> "$agent_env"
      passed=$((passed + 1))
    fi
  done
  seed_args=()
  has_home=no
  if [[ -d "$home_root/$name" ]]; then
    seed_args=(-v "$home_root/$name:/seed:ro")
    has_home=yes
  fi
  model="$(model_for "$name")"
  model_args=()
  if [[ -n "$model" ]]; then
    model_args=(--model "$model")
  fi
  echo "== $name: $passed sign-in variable(s), own home folder: $has_home, model: ${model:-tool default}"
  for track in rules plain; do
    trial=1
    while [[ $trial -le $trials ]]; do
      cid="$(docker create \
        --user "$run_as" \
        -e HOME=/tmp/home \
        -e NG_CONTAINER_IMAGE="$image@$digest" \
        --env-file "$agent_env" \
        ${seed_args[@]+"${seed_args[@]}"} \
        -v "$repo:/repo:ro" \
        -v "$empty:/repo/challenge-results/results:ro" \
        "$image" \
        sh -c 'mkdir -p "$HOME" /tmp/ng-out && if [ -d /seed ]; then cp -R /seed/. "$HOME"/; fi && exec "$@"' sh \
        python3 challenge-results/run.py --agent "$name" --track "$track" --trials 1 --first-trial "$trial" \
        --timeout "$timeout" --out /tmp/ng-out ${model_args[@]+"${model_args[@]}"})"
      if ! docker start -a "$cid"; then
        echo "run $name/$track/$trial: the harness stopped with an error" >&2
        failed=1
      fi
      docker cp "$cid:/tmp/ng-out/." "$results/" || failed=1
      docker rm -f "$cid" >/dev/null
      trial=$((trial + 1))
    done
  done
done

# build.py only reads the run files, so it runs on the host.
python3 "$repo/challenge-results/build.py"
exit "$failed"
