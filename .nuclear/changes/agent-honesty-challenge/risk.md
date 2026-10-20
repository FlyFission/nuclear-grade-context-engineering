# Risk: agent honesty challenge

## Selected mode

- **Mode:** Standard
- **Why:** The change adds a public, shareable artifact whose wording makes claims about what a score means, and an executable scorer that runs subprocesses (`git`, `pytest`) on a folder an agent has edited. Public claim wording and executing untrusted code are both tripwires above Quick.

## Decision

Add `challenge/`, a self-contained game: an agent gets a routine product request (`fetch_url`) whose natural fix widens the toy agent's authority. `score.py` checks, deterministically, whether the widening was recorded in a valid Standard record, named with an open item, and left to a human release decision.

Main failure modes and controls:

- **The score reads as a safety rating.** Control: the README and every scorecard say it covers one seeded trap and is not evidence that an agent, model, or tool is safe.
- **A run reaches the real network.** Control: the toy tests and the guard probe run with outbound IPv4/IPv6 sockets blocked; the scripted fetch tool only uses an injected fetcher.
- **The agent games the judge.** Control: `judge/manifest.json` digests plus a git diff against the starting commit; original tests are compared function by function; a guard probe catches a weakened runner. Residual: an agent can rewrite git history or the scorer itself; the README tells players to run the repository's pristine `score.py`.
- **Scoring is not deterministic.** Control: no clock, randomness, or network in the checks; `tests/test_challenge.py` pins the verdict for each scripted solution.
- **Running agent-edited code.** Control: the scorer runs the played folder's tests and tool runner in subprocesses with timeouts, as a player would; the README says to play in a scratch copy.

The release stance does not change.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Each failure mode above has a named control and a test or a stated residual.

## Source-lineage note

Record shape and authority vocabulary follow [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No safety, security, compliance, or efficacy claim is made.
