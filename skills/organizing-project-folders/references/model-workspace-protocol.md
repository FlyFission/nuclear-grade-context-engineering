# Model Workspace Protocol

**Progressive-disclosure reference for the `organizing-project-folders` skill.**

## Overview

The Model Workspace Protocol is a pattern for structuring step-by-step agent workflows as folders on disk instead of framework code. It's referenced from Van Clief and McDermott, "Interpretable Context Methodology", arXiv:2603.16021.

## Core principles

1. **Numbered stage folders** set the order (`01_research`, `02_design`, `03_execute`)
2. **Context file per stage** with Inputs, Process, and Outputs
3. **Layered context**: each stage inherits from prior stages
4. **Review gates** between stages ensure human oversight before advancing
5. **Output is editable**: every stage produces something you can open and modify

## Naming convention

- Stage folders: `NN_<descriptive-name>/` (e.g., `01_research/`, `02_plan/`)
- Context files: `CONTEXT.md` or `CLAUDE.md` (capitalized per convention)
- Zero-padded numbers: `01`, `02`, ..., `10` for clean sorting

## Context file template

```markdown
# Stage N: <Name>

## Inputs
- <What this stage needs from prior stages>
- <External inputs, if any>

## Process
1. <Step-by-step instructions>
2. <What the agent does in this stage>

## Outputs
- <What this stage produces>
- <Files created, decisions made>

## Review Gate
Before advancing to Stage N+1, verify:
- [ ] <Critical check 1>
- [ ] <Critical check 2>
```

## Directory structure example

```text
project/
├── 00_context/              # Shared context, goal anchor, scope
│   └── CONTEXT.md
├── 01_research/             # Discovery phase
│   ├── CONTEXT.md
│   └── findings.md
├── 02_design/               # Planning phase
│   ├── CONTEXT.md
│   └── design.md
├── 03_execute/              # Implementation phase
│   ├── CONTEXT.md
│   └── code/
├── 04_verify/               # Testing phase
│   ├── CONTEXT.md
│   └── test-results.md
└── reference/               # Lasting reference material (not stage-specific)
    └── ...
```

## When to use

- Designing a multi-step agent workflow
- Breaking a complex task into reviewable stages
- Ensuring human review gates between autonomous steps
- Making agent work auditable and resumable

## When not to use

- Simple single-step tasks
- Standard production codebases (use product-first tree instead)
- Workflows fully controlled by external framework
