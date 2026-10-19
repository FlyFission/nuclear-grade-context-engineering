# Risk: initial tool runner

## Selected mode

- **Mode:** Standard
- **Why:** This change creates the agent's authority: which tools exist, whether it may use the network, and which folder it may write to.

## Decision

Give the file agent two tools, `read_file` and `write_file`, with `network: false` and writes limited to `workspace/`.

Main failure modes and controls:

- **A write escapes the workspace.** Control: `ToolRunner.resolve` denies paths outside `workspace/`; tested.
- **A tool runs without being configured.** Control: `run` checks `allowed_tools` and the `TOOLS` registry; tested.
- **A network tool runs while network is off.** Control: tools flagged `needs_network` are denied unless `network` is true; tested.

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Each authority limit has a control and a test.

## Source-lineage note

Record shape from Nuclear-grade, https://github.com/FlyFission/nuclear-grade-context-engineering. No compliance claim is made.
