# Workspace: short-article pipeline

A two-stage workflow run by a single agent, one stage after the other. Run the numbered stages in order.
Check each stage's `output/` before you start the next one.

## Stages

1. `01_research/` — gather and summarize source material into research notes.
2. `02_draft/` — write a short article from the research notes, in the workspace voice.

## Routing

- Lasting rules live in `references/` (for example `references/voice.md`). Treat them as rules to follow,
  not as input to work on.
- Each stage's working output lands in its own `output/` folder and becomes the next stage's input.
- A person checks the work between stages. Read a stage's `output/`, edit it if needed, then run the
  next stage.
