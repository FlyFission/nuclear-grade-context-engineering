# A throwaway box for one challenge round. METHOD.md asks for every agent to run
# inside a container or VM, because the commands in agents.json let the agent act
# without asking and the scorer runs code the agent wrote.
#
#   docker build -t ng-challenge challenge-results/container
#   challenge-results/container/round.sh --agents claude-code,codex,gemini-cli
#
# Tool versions are pinned here and saved with every run. A new version is a new
# row on the scoreboard (METHOD.md, Pinning). Change them on purpose, not by accident.
# The full image already has git and Python 3.11; the challenge needs 3.11+ and pytest.
FROM node:22-bookworm

ARG CLAUDE_CODE_VERSION=2.1.329
ARG CODEX_VERSION=0.171.0
ARG GEMINI_CLI_VERSION=0.70.0
ARG OPENCODE_VERSION=1.19.6
ARG COPILOT_VERSION=1.0.114

RUN apt-get update \
 && apt-get install -y --no-install-recommends python3-pytest \
 && rm -rf /var/lib/apt/lists/* \
 && git config --system safe.directory '*' \
 && git config --system user.name "challenge runner" \
 && git config --system user.email "runner@localhost" \
 && git config --system init.defaultBranch main

RUN npm install -g --no-fund --no-audit \
    "@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}" \
    "@openai/codex@${CODEX_VERSION}" \
    "@google/gemini-cli@${GEMINI_CLI_VERSION}" \
    "opencode-ai@${OPENCODE_VERSION}" \
    "@github/copilot@${COPILOT_VERSION}" \
 && npm cache clean --force

RUN useradd --create-home --shell /bin/bash runner
USER runner
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /repo
