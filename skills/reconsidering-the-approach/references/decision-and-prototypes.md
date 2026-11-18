# Decision analysis and prototype comparison

The council compares *alternative ways to satisfy the same accepted objective*, not alternative success criteria.

## Decision screen

1. Freeze hard constraints (technical, regulatory, security, authority, data-handling, compatibility, safety-related interfaces, reversibility). A failed requirement disqualifies the design; an untested gate is `UNKNOWN`, not a pass.
2. Predeclare criteria before seeing results. Candidate dimensions typically include acceptance correctness, operator/user value, change cost, life-cycle cost, reliability, performance, coupling/maintainability, and time to first proof. Distinguish constraints from optimization objectives.
3. Prefer qualitative tradeoffs when no reliable scale or stakeholder weights exist. For weighted comparisons specify metrics, units, which direction wins, weights, source and error bands. Do not invent scores.
4. Sensitivity: vary plausible weights and measurement ranges and report whether preferred candidate changes. Unstable rank means `CONDITIONAL`, not precise winner. Keep minority objections with testable criteria.
5. Specify no-change baseline, buy/adapt baseline where practical, at least two different candidate mechanisms, and **value of information**: whether the decision impact justifies the cost/delay of prototyping.

## Fair prototype tournament

A proposed tournament is a test **plan**, not evidence that code ran. Run only when the user authorized code execution and spend, and Nuclear-grade has classified the operation; prototypes cannot alter a controlled baseline or deploy.

Before building, **freeze**:
- Candidate descriptions and mechanism difference, benchmark question and agreed acceptance gates.
- Same fixture/dataset and version/hash, environment/container/toolchain, machine resources, time/money limits, warm-up and repetition counts.
- Measurement procedure and units; allowable variance; correctness and security checks; quality threshold; how to handle failures and missing data.
- Independent or host-reproducible evidence source, custody and who has authority to compare or accept.

During competition, keep candidate implementations isolated; test identical workloads and edge cases. Repeat noisy measurements; record mean/distribution or range, not only the best run. Include all failures and timeouts. A candidate failing a hard gate is **INELIGIBLE** and cannot win on speed or cost. Missing gates or measured metrics are **UNKNOWN**, not zero or an assumed pass. If all eligible candidates are within measurement uncertainty, declare an unresolved tie and recommend the cheapest discriminating experiment.

**Machine-readable support:** `scripts/compare_prototypes.py` accepts a JSON file of pre-recorded candidate results, gates and metric definitions, validates missing/invalid metrics, applies hard gates, and reports normalized relative scores. It does **not** run the candidates, establish measurement integrity, rank unknowns as winners, or independently verify evidence. Treat scores as decision aids subject to human review. Use `references/prototype-input-example.json` as a demonstration, not empirical results.

## Reversal / kill criteria

For each recommendation record a measurable metric, direction, threshold, method/source, observation window or milestone, responsible owner and action (`pause`, `retest`, `reopen`, `escalate`). Use `TO_DEFINE` instead of invented numbers. A date without a measurement method is not a criterion.

## Evidence hygiene

Tag OBSERVED, SOURCE, INFERRED, ASSUMED, UNKNOWN, CONFLICTED. Direct file/test locators are stronger than model rhetoric. Keep `running-a-review-panel`, `proving-claims`, `checking-facts`, and `checking-release-readiness` as the authoritative review/evidence/ship paths. Do not transplant a second validation regime.
