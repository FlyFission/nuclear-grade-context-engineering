# Admit the next review attempt

Use these opt-in v1 records for a new bounded panel or model-review run. Existing packets without
them keep their old validation behavior. Copy both JSON files into the change packet; fill the
budget owner's identity and UTC authorization time, exact runtime SHA256 and bounds **before**
calls. Example numeric bounds are placeholders for the owner's decision, not granted authority.
Pin the exact authorization bytes in `review-run.v1.json` using `sha256sum`:

```bash
cp templates/review-run/*.json .nuclear/changes/your-packet/
# Edit review-authorization.v1.json, then copy this digest into authorization_sha256:
sha256sum .nuclear/changes/your-packet/review-authorization.v1.json
# Under the shared caller lock, re-read history and set the proposed next_attempt:
python tools/ng.py validate .nuclear/changes/your-packet --before-review
```

Previously, plain packet validation could pass while a declared run had no room to finish.
Now `--before-review` exits 1 for missing records, exhausted ordinary/reserve/total slots,
insufficient remaining slots to obtain required usable cases, changed authorization bytes,
a runtime mismatch, missing repair evidence, or a recorded stop. For example, 16 required usable
cases, 16 total slots and nine attempts with eight usable leave eight needed but seven available:
admission fails with `required usable cases infeasible within remaining attempt ceiling`.
Ordinary `validate` also checks any v1 history present, but does not admit `next_attempt`.

For serial or parallel callers, reserve **before launch**, using one shared lock covering every
dispatcher and settlement writer for this run (a separate stable lock file, not the JSON inode
replaced by atomic rename):

1. Acquire the caller lock and re-read current records; never admit from a cached snapshot.
2. Set the proposed `next_attempt` and require `validate PACKET --before-review` to pass. Retain its
   receipt. A pass alone reserves nothing; do not release the lock yet.
3. Atomically persist that same ID/case/runtime in `attempts` with `outcome: "in_flight"`, the full
   reservation, `coverage_credit: false`, and `opinion: null`. Use a durable atomic replace in the
   caller; require ordinary `validate PACKET` to pass on the written record before launch.
4. Launch only after the reservation is persisted, then release the caller lock. Other workers
   may now reserve their own slots while this request runs. If launch fails, keep the slot and
   settle its actual outcome; never remove it to regain capacity.
5. On completion, reacquire the same lock, re-read, and atomically settle **that ID in place** with
   its terminal outcome/opinion, retaining its full reservation and all other IDs. Retain prior
   receipts/snapshots externally; do not append another attempt for the same dispatch. A crash
   leaves the in-flight reservation occupied. Reconcile stopped processes and unknown results;
   never retry a pending ID or silently release its reservation.

All writers must honor this protocol. `--before-review` is read-only and supplies neither a lock
nor atomic reservation: four workers checking the same stale history can otherwise all pass.
The checker counts each recorded in-flight request against ordinary/reserve/total ceilings. Four
in flight under a four-attempt ceiling reject a fifth; three pending and one available slot can
still feasibly satisfy four required cases. Pending potential is **not usable coverage**.

A reserved record has these fields:

```json
{
  "id": "A001",
  "case_id": "case-001",
  "runtime_sha256": "<same authorized 64-character SHA256>",
  "started_at": "2026-11-04T12:00:00Z",
  "outcome": "in_flight",
  "reserved_units": 100,
  "coverage_credit": false,
  "opinion": null
}
```

Outcomes are `in_flight`, `usable`, `transport_failed`, `calibration_failed`, or `unknown`. Use `scope: "review"` for corpus review and `scope: "calibration"` for a seeded calibration.
`case_id` names an exact current state plus its review seat; changed states and separately required
views have different identities. Distinct case IDs prevent counting repeat views as new cases.
A complete source-grounded dissent is `outcome: "usable", opinion: "non_support"`: it earns coverage
credit without claiming approval. A supportive usable review has `opinion: "support"`; unusable
attempts have `opinion: null`. Only `usable` has
`coverage_credit: true`. Every attempt retains the full authorized `reservation_per_attempt`,
including pending/failed/unknown attempts. Report actual usage separately; reservations are not billing.
The ordinary pool is `attempt_ceiling - transport_reserve`; reserve slots cannot buy ordinary
views. `required_usable_cases` must fit the ordinary pool at authorization.

A transport replacement is a **new** ID with `recovery_of` naming one prior `transport_failed`
attempt with the same `case_id` and `repair_evidence: {"path": "repair.json", "sha256": "<digest>"}`. Pin a real repair
regression artifact inside the packet; the checker verifies its bytes, not the truth of its claim.
Both stored replacement records and `next_attempt` use those fields. One failed attempt gets at
most one replacement; a new transport failure consumes another reserve slot if replaced. Runtime
changes require explicit budget-owner disposition; a transport reserve does not authorize them.

`calibration_failed` means a missed seeded critical defect in calibration scope; it stops
continuation, preventing retry-to-agreement. Ordinary model findings and dissent do not use that
outcome and do not stop a corpus run. Consolidate source-demonstrated fixes, then use fresh exact-state
case identities for changed states within the same coverage and budget requirements. An unknown also stops
automatic continuation, retains its full reservation and supplies no support; it is distinct from
a demonstrated semantic failure. A budget owner may explicitly authorize a new case or amended
run after disposition. Already-launched peers may settle after a stop appears; retain them, but
any recorded stop blocks all new admissions even if another peer later settles usable. Preserve all original records, old authorization and receipt pins, and
carry prior counts/reservations into the combined ceiling. This v1 check deliberately has no
reset, amendment or waiver command: resolve that authority outside it; never overwrite history
to make this run pass.

This is a read-only pre-call admission check over declared records, not a provider interceptor,
append-only store, signature, clock witness, or authentication of human approval. Someone able
to rewrite both authorization and history can forge a consistent pair. Commit/freeze them and
retain `validate --before-review --json` receipts under custody outside the change actor where the
consequence warrants it. The checker catches inconsistent records; external custody and the
caller locking, persisting reservations before launch, and invoking it before dispatch remain required. No accuracy or cost improvement is claimed.
