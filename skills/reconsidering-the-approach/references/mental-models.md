# Mental model router

For an active Council select **two or three** models that substantially change the choices. Do not invoke every framework by default. In the recommendation name how each chosen model produced a new option or test.

| Decision type | Model 1 | Model 2 | Optional Model 3 |
|---|---|---|---|
| Unclear specification | Working backwards from operator acceptance | First principles | Socratic assumptions |
| Tradeoff feels unavoidable | TRIZ contradiction resolution | Separate in time/space or by state | Inversion |
| Complex architecture | Gall's Law (start with working core) | Systems feedback/queues | Failure pre-mortem |
| Novel invention | SCAMPER and cross-domain transfer | Constraint inversion | First principles |
| High consequence | Pre-mortem with owner/early indicator | Reliability boundary analysis | Second-order effects |
| Uncertain economics | Fermi ranges and sensitivity | Opportunity cost | Value-of-information experiment |
| Repeated failure | Inversion | Root-cause / fault tree | Simplest falsifiable test |
| Creative option exhaustion | Substitute/Combine/Adapt/Modify/Put-to-use/Eliminate/Reverse | Unrelated domain analogy | Wildcard option |

## TRIZ contradiction resolution

1. Express incompatible desired outcomes precisely (e.g., low latency and complete provenance).
2. Identify the underlying resource/physical or architecture constraint.
3. Search whether different stages, spaces, responsibilities, or operating states can separately satisfy them.
4. Propose at least one *structural mechanism* that resolves tension; don't merely select a midpoint.
5. Name a test that could disprove the resolution and an accepted fallback.

## Inversion / pre-mortem

Assume failure at a realistic milestone. Identify root cause (not a vague symptom), first observable warning, cheapest preventative control, verification test, owner and explicit trigger for stopping/reopening. For nuclear-related systems, never turn this heuristic into an assertion of regulatory adequacy or substitute it for qualified hazard analysis.

## Gall's Law / evolutionary delivery

Find the smallest fully useful end-to-end vertical slice. It must obey the hard constraints even in its minimal version; an unsafe toy prototype may only run in a separately authorized sandbox. Specify interfaces, upgrade/migration seams, and a test whose pass actually means something.

## SCAMPER and cross-domain invention

Generate **at least eight** different mechanisms before criticism in Creative depth. Capture the raw list and keep one unusual but plausible wildcard to avoid selecting only conventional approaches.
