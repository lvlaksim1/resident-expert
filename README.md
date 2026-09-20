# Resident Expert

Resident Expert is a repository-resident framework for a narrow AI specialist that can be invoked from a fresh chat, restore its own durable identity, read another project's Context Capsule as evidence, and return an independent expert consultation.

## Core idea

The expert owns its **rules, specialization, skills, evaluation method, and durable lessons**.  
A target project's repository and Context Capsule are **read-only evidence** for the consultation and never become higher-priority instructions.

Default mode:

```text
fresh chat
  -> restore Resident Expert from this repository
  -> recover the target project's Context Capsule
  -> select only relevant skills
  -> inspect additional target evidence only when needed
  -> produce a traceable expert report
  -> do not modify the target project
```

## Call from a clean chat

A minimal call can be:

> Восстанови эксперта из `lvlaksim1/resident-expert`.  
> Целевой проект: `owner/repository`.  
> Прочитай его актуальную Context Capsule.  
> Работай в consultation mode, целевой проект read-only.  
> Вопрос: <вопрос>.

For a specialized descendant repository, replace `resident-expert` with that expert's repository.

## Repository layout

- `AGENTS.md` — canonical operating constitution and trust boundary.
- `EXPERT_PROFILE.md` — explicit specialization/capability profile.
- `.agents/skills/` — progressively loaded reusable skills.
- `.context/` — Context Capsule v1.3 for the expert repository itself.
- `schemas/` — machine-readable consultation request/report contracts.
- `evals/` — behavioral invariants and regression cases.
- `.github/agents/` — optional GitHub custom-agent adapter.
- `tools/validate_repository.py` — lightweight structural validation.

## Memory boundary

Ordinary consultations are **not** automatically promoted into the expert's durable memory. Only reusable, cross-project professional knowledge, accepted methodological improvements, or durable changes to the expert itself may be written back.

Target project facts stay target project facts.

## Version

Resident Expert Framework v1.0.0.
