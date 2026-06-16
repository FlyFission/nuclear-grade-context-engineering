# Nuclear-grade Charter

**Version:** 1.3.0
**Ratified:** 2026-05-27
**Last amended:** 2026-06-16

The charter is the lasting backbone: the principles for how work is done here that do not bend for any single change. A mission anchor says what a given change is for; the charter says how all changes must be carried out. The tools treat the charter as advice for now (the validator does not block on it), but it is the standard a reviewer and an agent are expected to hold to.

The principles scale with the mode. Quick changes honor the spirit; Standard and activated records are where the charter earns its keep. To amend the charter, raise the version (major for a removed or redefined principle, minor for an added one, patch for wording) and note the change below.

## Articles

1. **Ownership.** A named person owns each change and its evidence. If no one owns it, no one is accountable for whether it still serves its mission.
2. **Face facts.** Report the actual state, not the hoped-for state. Wishful thinking is not evidence.
3. **Rising standards.** Never normalize a deviation. A small erosion of rigor is a finding, not a rounding error.
4. **Formality.** Follow the procedure. Deviations are documented and decided, never silent.
5. **Technical depth.** The owner understands the details, not just the summary.
6. **Integrity in reporting.** Bad news travels up immediately and intact. A softened report is itself a drift.
7. **Questioning attitude.** Challenge assumptions before acting; prefer facts over confidence.
8. **Evidence over persuasion.** Claims carry reproducible evidence or a labeled gap, not prose that convinces.
9. **Graded rigor.** Match controls to consequence. Quick for low-consequence reversible work; Standard and activated records as consequence rises.
10. **Baseline discipline.** The accepted configuration is recorded, and changes to it are controlled and traceable.
11. **Decision-question discipline.** Before meaningful work starts, name the decision the evidence must support. A well-run change spends enough effort on the question that the later proof is pointed at the right decision.
12. **Operational unambiguity.** Write skills, commands, templates, and handoffs so they are hard to misuse under pressure, not merely possible to understand with care.
13. **Mission-aligned small work.** Local edits, checks, and reviews must serve the mission anchor. Winning a small task while drifting from the objective is a control failure.
14. **Grounded truth.** Separate fact, assumption, unknown, source claim, local proof, and decision authority. Confidence, fluency, preference, and vendor language are not proof.
15. **Two-speed control.** Move quickly while exploring and building reversible candidates; slow down at acceptance gates for claims, baselines, public wording, releases, and other trust-bearing decisions.
16. **Cut-point self-checking.** Measure critical targets before the cut: commands, public claims, dependency/model/API changes, release actions, and other wrong-target or hard-to-reverse steps.
17. **Authority to information.** Decision authority belongs where the evidence and competence are, not automatically at the top, and it stays bounded. Reversible, well-evidenced work may be decided at the edge; irreversible, trust-bearing, or thinly evidenced decisions are escalated to a named person. Authority is earned by demonstrated competence and shared clarity of intent, and the gradient never removes a required human gate. An agent's confidence is not competence, and its stated intent is not proof it understood.
18. **Intent before action.** Before a critical action, state the intent and the reasoning behind it so a reviewer can challenge the thinking, not just the result. Hand off so the next owner is more capable, not more dependent.
19. **Stop-work and standing deficiencies.** Anyone may halt unsafe or unclear work regardless of seniority, and surfacing bad news is protected, never punished. That protection covers honest error and good-faith concern; it does not shield a willful violation — knowingly disabling a control, fabricating evidence, or routing around a required gate — which is itself a finding to surface and correct, never normalize (Art. 3). Known deficiencies are logged, owned, and fixed or explicitly risk-accepted with an owner and a revisit date — never silently normalized.

## Amendment log

- 1.3.0 (2026-06-16): Refined Art. 19 to distinguish protected honest error and good-faith concern from an accountable willful violation (a knowingly bypassed gate, a disabled control, a fabricated result), reconciling no-blame learning with the no-normalization rule (Art. 3).
- 1.2.0 (2026-05-31): Added leadership and high-reliability articles for authority to information, intent before action, and stop-work and standing deficiencies.
- 1.1.0 (2026-05-30): Added doctrine-spine articles for decision-question discipline, operational unambiguity, mission-aligned small work, grounded truth, two-speed control, and cut-point self-checking.
- 1.0.0 (2026-05-27): Initial charter.

## Source-lineage note

The charter is an original software-workflow statement influenced by nuclear-industry safety and quality culture (Rickover and Navy nuclear practice, and the human-performance practices in DOE-HDBK-1028-2009), and by intent-based-leadership and naval mission-command ideas (authority to information, intent before action, leader-leader), as concept lineage mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
