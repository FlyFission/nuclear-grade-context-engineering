# Worked Example: Agentic Folder Structure (Model Workspace Protocol)

This example shows a step-by-step agent workflow built as a **folder structure** instead of framework
code. It follows the Model Workspace Protocol (MWP), a folder pattern that `organizing-project-folders`
teaches. One agent reads the right context file at each stage. Numbered folders set the order. Lasting
reference material is kept apart from the output of each run. A person checks each stage's output before
the next stage runs.

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

- **Numbered folders set the order.** `01_` runs before `02_`. The number is the sequence.
- **Each stage is a contract.** Its `CONTEXT.md` lists Inputs, Process, and Outputs. Nothing is hidden.
- **Reference and working files are kept apart.** `references/` holds lasting rules. `output/` holds the
  per-run files that feed the next stage's input.
- **Every output can be edited, and a person checks it.** A person can read and edit `01_research/output/`
  before `02_draft` runs.
- **Names are platform-safe and easy to sort.** Lowercase, with zeros padding the numbers. The numbered
  stage prefix `NN_` (a number, then an underscore, as in `01_research`) marks the order. It is the one
  allowed exception to the hyphen-between-words rule used elsewhere. `references/` sits at the workspace
  root, and each stage reaches it through `../references/`. The `CONTEXT.md` marker files are capitalized
  by Model Workspace Protocol custom (like `README.md`), which is an allowed exception to the lowercase rule.

This is one of two patterns `organizing-project-folders` supports (the *agent-workflow-workspace* branch).
The other is splitting a product codebase into folders, where the folder tree is the work breakdown (WBS)
laid out on disk.

## Boundary note

This is an illustrative example, not a runnable harness or a mandated layout. It does not create
compliance, formal assurance, or certification. Lineage: the Model Workspace Protocol
(Van Clief and McDermott, arXiv:2603.16021), mapped as supporting context in
`docs/00-standards-foundation/source-map.md`.
