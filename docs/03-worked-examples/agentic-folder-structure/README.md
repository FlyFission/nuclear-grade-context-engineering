# Worked Example: Agentic Folder Structure (Model Workspace Protocol)

This example shows a sequential agent workflow expressed as **folder structure** instead of framework
code, following the Model Workspace Protocol (MWP) pattern that `structuring-agentic-folders` teaches.
A single agent reads the right context file at each stage; numbered folders encode order; persistent
reference material is separated from per-run output; a human reviews each stage's output before the
next runs.

## The layout

```text
example-workspace/
├── CONTEXT.md            # routing: what this workspace is, how to run the stages in order
├── references/           # persistent reference material (set once; constraints, not input)
│   └── voice.md
├── 01_research/
│   ├── CONTEXT.md        # stage contract: Inputs / Process / Outputs
│   └── output/           # per-run working artifacts (changes each run)
└── 02_draft/
    ├── CONTEXT.md        # stage contract: consumes 01_research/output/
    └── output/
```

## Why it is structured this way

- **Numbered folders encode execution order.** `01_` runs before `02_`; the number is the sequence.
- **Each stage is a contract.** Its `CONTEXT.md` states Inputs, Process, and Outputs — nothing hidden.
- **Reference vs working are separated.** `references/` holds durable constraints; `output/` holds the
  per-run artifacts that feed the next stage's input.
- **Every output is an edit surface with a review gate.** A human can inspect and edit `01_research/output/`
  before `02_draft` runs.
- **Names are platform-safe and sortable.** Lowercase and zero-padded. The numbered stage prefix `NN_` (number then underscore, as in `01_research`) marks the sequence — the one accepted exception to the hyphen word-separator convention used elsewhere. `references/` sits at the workspace root, and each stage reaches it via `../references/`. The `CONTEXT.md` marker files are capitalized by Model Workspace Protocol convention (like `README.md`) — an accepted exception to the lowercase rule.

This is one paradigm `structuring-agentic-folders` supports (the *agent-workflow-workspace* branch);
the other is product-oriented codebase decomposition, where the folder tree is the WBS projected to disk.

## Boundary note

This is an illustrative example, not a runnable harness or a mandated layout. It does not create
compliance, formal assurance, or certification. Lineage: the Model Workspace Protocol
(Van Clief and McDermott, arXiv:2603.16021), mapped as supporting context in
`docs/00-standards-foundation/source-map.md`.
