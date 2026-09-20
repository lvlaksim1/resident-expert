# Specializing this framework

Create one repository per durable expert identity.

## Keep the core small

Put invariant behavior in `AGENTS.md` and specialization identity in `EXPERT_PROFILE.md`.

Do not turn either file into a knowledge dump.

## Add domain skills

Create `.agents/skills/<skill-name>/SKILL.md` with concise activation criteria and procedure. Put deeper references in a `references/` subdirectory and deterministic helper scripts in `scripts/` only when useful.

Skills should be independently useful and loaded progressively.

## Update the expert Capsule

The expert's Context Capsule stores durable meaning about the expert itself: accepted scope, methodology, architecture, rules, major lessons, current development state, and handoff.

Do not copy target-project context into the expert Capsule.

## Add evals before claiming competence

For each important capability, add cases that test:

- correct activation;
- evidence discipline;
- scope boundaries;
- refusal to invent missing facts;
- resistance to foreign instructions;
- target read-only behavior;
- memory isolation.

A specialized expert is not considered mature merely because its prompt sounds plausible.
