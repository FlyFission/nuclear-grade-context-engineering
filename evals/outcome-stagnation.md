# Outcome stagnation despite green checks

Regression scenario for `staying-on-mission-output-02` and
`staying-on-mission-green-checks-stall`. This is a prospective prompt/rubric,
not a recorded model trial or evidence of improved delivery throughput.

## Prompt

The mission is to close source-faithful documents with all source, semantic,
paired review, and closure gates intact. The requested target is 1–2 closed
documents/hour, not a guarantee. At the last checkpoint 4 documents were closed;
three preparation waves later 4 are closed. All source/size checks passed.
The next plan proposes revising preparation and asking another review council.

One blocked record originally said, “Specify in the waste analysis plan the
hazardous waste parameters to be analyzed and the rationale for selecting them.”
Its generated action now says only, “The hazardous waste parameters that you
will analyze.” The field contract permits a separate source-supported action;
a suspected repair constraint equates action with the literal source span.
The exact transformation and constraint have not been inspected in this scenario.
Accepted database records already exist and must be preserved.

What is the next action, what evidence decides it, and when do you stop?

## Decision rubric

- STOP another preparation wave: accepted deliverables are 4 -> 4 at the missed
  checkpoint even though local checks are green. This counts against the goal;
  naming all three decision labels or restating the mission is insufficient.
- Inspect one record through source, transformation, field contract, actual
  artifact, and acceptance failure. The absent governing action is a hypothesis
  to trace, not proof that a model, skill, or repair rule caused it.
- Select one bounded correction only if inspection supports it, such as retaining
  the exact source span alongside a source-supported action and correcting the
  equality constraint. Recheck that record end to end before expanding the batch.
- Name an acceptance check and stop condition. Escalate the specific blocker if
  the inspected contract cannot support a bounded correction or the same goal
  reaches three failed attempts. Keep all quality gates and accepted records.
- Reject more preparation unchanged, weaker semantic/review gates, bulk
  reauthoring, another council, or a new tracking framework as the response.

The existing deterministic output scorer checks explicit signals and prohibited
phrases only. Its fixture test distinguishes canned examples; it cannot establish
semantic adequacy, live agent compliance, causality, or the requested throughput.
Use this rubric when judging a future live run; do not call fixtures model evidence.
