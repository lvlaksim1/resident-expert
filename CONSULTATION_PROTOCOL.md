# Consultation protocol

## Required inputs

A consultation should identify:

- target repository;
- question;
- optional scope or files;
- optional target revision;
- optional constraints.

If the repository contains Context Capsule, start from its `.context/ENTRYPOINT.md`.

## Evidence order

Prefer:

1. target Context Capsule semantic state;
2. live target repository evidence at the relevant revision;
3. CI/runtime evidence when needed;
4. authoritative external references when the question requires them.

A stored Capsule may be stale. Reconcile it against newer repository evidence before relying on it.

## Report discipline

A useful report states:

- expert identity/version;
- target repository and revision;
- Capsule revision/provenance when available;
- skills used;
- question and scope;
- verified facts;
- analysis;
- uncertainty or missing evidence;
- recommendations or alternatives;
- whether any durable expert lesson was promoted.

Do not expose private chain-of-thought. Give concise reasoning summaries and evidence sufficient to audit the conclusion.

## Write boundary

Consultation mode is read-only for the target repository. Recommendations are returned to the user or the target project's primary agent for execution.
