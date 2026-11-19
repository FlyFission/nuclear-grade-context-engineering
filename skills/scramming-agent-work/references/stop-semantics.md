# SCRAM semantics and graduated implementation

## Five essential states

- **STOP REQUESTED** — operator command received; no further voluntary work starts.
- **STOPPING** — host/orchestrator cancellation requests sent; outstanding acknowledgements tracked.
- **HELD** — all **enumerated in-scope** actors and queues have acknowledged a stop, and an independent status check verifies the hold.
- **PARTIAL HOLD** — at least one job remains running, requested-but-unconfirmed, or unobservable.
- **RESUME PENDING** — operator authorizes a specific restart, pending authority, state and risk checks.

A skill-only invocation **cannot** establish HELD across external runtimes, so prefer PARTIAL HOLD if the scope was "all agents" and external worker enumeration is incomplete.

## Independent execution-plane upgrade (future, not shipped by this skill)

A real all-agent hold needs a trusted supervisor outside agent-write control with authenticated operator access, registered worker IDs and leases, a monotonically versioned stop epoch, atomic latch, tool-dispatch deny gate, cancellation/ack deadlines, queue drain/inhibition, and read-only reconciliation of in-flight external side effects. Its resume should be an operator-only, recorded transition. Workers that miss the heartbeat are UNKNOWN, not STOPPED. Review isolation across workspaces and avoid affecting unrelated actors.

## Debrief template

**State:** HELD / PARTIAL HOLD / IN-SESSION HOLD, as actually evidenced.

**Stop coverage:** X confirmed, Y requested, Z still running, N unknown. Scope and observed time.

**Where we are:** plain-language progress in 1–2 sentences.

**Completed:** last concrete accepted step and evidence reference.

**In flight:** unfinished work and unconfirmed side effects.

**Reversibility:** easy local undo / requires approval or compensating action / likely irreversible.

**Risk:** biggest current unknown and what can still change externally.

**Owner's options:** keep held; authorize read-only investigation; authorize a targeted cancellation/recovery; begin a controlled resume.

Do not create files or use mutating tools to prepare the debrief under a hold.
