#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "VERSION",
    "AGENTS.md",
    "AI_CONTEXT.md",
    "EXPERT_PROFILE.md",
    "CONSULTATION_PROTOCOL.md",
    "agent-card.json",
    ".context/ENTRYPOINT.md",
    ".context/capsule.json",
    ".context/manifest.json",
    ".context/protocol.md",
    "schemas/consultation-request.schema.json",
    "schemas/expert-report.schema.json",
    "evals/cases.json",
]

SKILLS = [
    ".agents/skills/target-context-recovery/SKILL.md",
    ".agents/skills/evidence-first-analysis/SKILL.md",
    ".agents/skills/expert-consultation/SKILL.md",
    ".agents/skills/memory-promotion/SKILL.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


for rel in REQUIRED + SKILLS:
    if not (ROOT / rel).is_file():
        fail(f"missing {rel}")

for rel in [
    "agent-card.json",
    ".context/capsule.json",
    ".context/manifest.json",
    "schemas/consultation-request.schema.json",
    "schemas/expert-report.schema.json",
    "evals/cases.json",
]:
    try:
        json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON in {rel}: {exc}")

manifest = json.loads((ROOT / ".context/manifest.json").read_text(encoding="utf-8"))
if manifest.get("schema") != "context-capsule-manifest":
    fail("unexpected Context Capsule manifest schema")
if manifest.get("schema_version") != 3:
    fail("unexpected Context Capsule manifest version")

capsule = json.loads((ROOT / ".context/capsule.json").read_text(encoding="utf-8"))
if capsule.get("version") != "1.3.0":
    fail("Context Capsule Core must be v1.3.0")

agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
for phrase in [
    "consultation",
    "read-only",
    "trust boundary",
    "Do not wait for the user to ask to save context",
]:
    if phrase not in agents:
        fail(f"AGENTS.md missing invariant: {phrase}")

for rel in SKILLS:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
        fail(f"invalid skill frontmatter: {rel}")

cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
ids = [case.get("id") for case in cases]
if len(ids) != len(set(ids)):
    fail("duplicate eval IDs")

print(f"VALID: Resident Expert repository structure ({len(REQUIRED)} required files, {len(SKILLS)} skills, {len(cases)} evals)")
