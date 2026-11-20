#!/usr/bin/env bash
# Run one challenge round in throwaway containers, then rebuild the scoreboard.
#
#   challenge-results/container/round.sh --agents claude-code,codex,gemini-cli [--trials 5] [--model codex=<id>]
#
# Works with the bash that ships with macOS. Each agent gets its own fresh container, with only its own sign-in passed in, so
# no agent can read another vendor's key. The repo is mounted read-only, so an agent
# cannot reach the scorer; only challenge-results/results/ is writable. Everything
# except --agents goes to run-all.py unchanged.
#
# Sign-ins are read from the file in NG_AGENTS_ENV (default ~/.ng-challenge.env),
# kept outside the repo so it is never copied, mounted or committed. One KEY=value per
# line. An agent with no sign-in still runs, and its failed runs are published like
# any other (METHOD.md, How many runs), so name only agents you have signed in for.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo="$(cd "$here/../.." && pwd)"
image="${NG_IMAGE:-ng-challenge}"
env_file="${NG_AGENTS_ENV:-$HOME/.ng-challenge.env}"

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

agents=""
rest=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agents) agents="$2"; shift 2 ;;
    --agents=*) agents="${1#--agents=}"; shift ;;
    *) rest+=("$1"); shift ;;
  esac
done
if [[ -z "$agents" ]]; then
  echo "name the agents you have signed in for: --agents claude-code,codex,..." >&2
  exit 2
fi

if [[ -f "$env_file" ]]; then
  set -a
  # shellcheck disable=SC1090
  . "$env_file"
  set +a
fi

if [[ -z "${NG_SKIP_BUILD:-}" ]]; then
  docker build -q -t "$image" "$here" >/dev/null
fi
digest="$(docker image inspect --format '{{.Id}}' "$image")"
mkdir -p "$repo/challenge-results/results"

IFS=',' read -r -a names <<< "$agents"
for name in "${names[@]}"; do
  env_args=()
  for key in $(keys_for "$name"); do
    if [[ -n "${!key:-}" ]]; then
      env_args+=(-e "$key")
    fi
  done
  echo "== $name ($(( ${#env_args[@]} / 2 )) sign-in variable(s) passed)"
  docker run --rm \
    ${env_args[@]+"${env_args[@]}"} \
    -e NG_CONTAINER_IMAGE="$image@$digest" \
    -v "$repo:/repo:ro" \
    -v "$repo/challenge-results/results:/repo/challenge-results/results" \
    "$image" \
    python3 challenge-results/run-all.py --no-build --agents "$name" ${rest[@]+"${rest[@]}"}
done

# build.py only reads the run files, so it runs on the host.
python3 "$repo/challenge-results/build.py"
