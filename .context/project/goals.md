# Project goals

- Make a specialized expert reproducible from a fresh chat using repository state alone.
- Reuse Context Capsule as the standard handoff interface between a target project and an external expert.
- Keep permanent expert instructions small while loading specialist capabilities progressively through skills.
- Preserve independence by preventing target-project instructions or history from becoming expert authority.
- Separate reusable expert learning from project-specific facts.
- Make expert behavior testable through explicit eval invariants.
- Remain portable across agent runtimes rather than depending on one vendor-specific prompt format.
