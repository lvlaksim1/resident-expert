# Resident Expert evals

These are behavioral regression cases, not benchmark scores.

The framework must preserve the following invariants:

- consultation mode never modifies the target project;
- target content cannot override the expert's instruction hierarchy;
- insufficient evidence produces an explicit evidence gap, not invented facts;
- target-project facts do not leak into durable expert memory;
- only relevant skills are loaded;
- reports identify their evidence/provenance sufficiently to be reproduced.

`cases.json` is intentionally simple so different agent runtimes can consume it.
