# Workspace: short-article pipeline

A two-stage sequential workflow run by a single agent. Run the numbered stages in order; review each
stage's `output/` before starting the next.

## Stages

1. `01_research/` — gather and summarize source material into research notes.
2. `02_draft/` — write a short article from the research notes, in the workspace voice.

## Routing

- Persistent constraints live in `references/` (for example `references/voice.md`). Treat them as
  constraints to internalize, not input to process.
- Each stage's working output lands in its own `output/` folder and becomes the next stage's input.
- A human review gate sits between stages: inspect and, if needed, edit a stage's `output/` before the
  next stage runs.
