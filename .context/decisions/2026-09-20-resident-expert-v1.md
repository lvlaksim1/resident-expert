# Resident Expert v1 architecture

Date: 2026-09-20  
Status: accepted

## Decision

Resident Expert v1 uses:

- one small canonical constitution in `AGENTS.md`;
- a separate explicit specialization profile;
- progressive Agent Skills instead of one monolithic expertise prompt;
- Context Capsule v1.3 for durable expert state;
- a strict trust boundary that treats target-project content as read-only evidence;
- no automatic promotion of ordinary consultations into durable expert memory;
- explicit schemas and eval invariants;
- optional runtime/vendor adapters that are subordinate to the canonical repository rules.

## Rationale

The design keeps the expert independent from the projects it reviews, reduces context load, supports fresh-chat recovery, and makes changes to expert behavior auditable and testable.
