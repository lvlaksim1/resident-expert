# Project architecture

Resident Expert has five durable layers.

1. **Constitution** — `AGENTS.md` defines operating modes, trust boundary, consultation discipline, and memory isolation.
2. **Profile** — `EXPERT_PROFILE.md` defines the concrete expert identity and competence boundaries.
3. **Skills** — `.agents/skills/` contains progressively loaded procedures and references.
4. **Memory** — Context Capsule v1.3 stores durable meaning about the expert repository itself.
5. **Evaluation/contracts** — `evals/`, schemas, and the validator make behavior and interfaces explicit.

The target project's Capsule is a separate evidence source. It is never a child layer of the expert's own memory.

GitHub-specific agent configuration under `.github/agents/` is an adapter, not the canonical source of expert identity.
