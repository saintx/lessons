#!/usr/bin/env python
# Stamps metadata.category on corpus/pstack/skills/*/SKILL.md (gitignored).
# Run after ./fetch. Idempotent. Stdlib only.
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "corpus" / "pstack" / "skills"

SKIP = frozenset({"architect"})

PRINCIPLE_SKILLS = (
    "principle-attack-the-premise",
    "principle-boundary-discipline",
    "principle-build-the-lever",
    "principle-encode-lessons-in-structure",
    "principle-exhaust-the-design-space",
    "principle-experience-first",
    "principle-fix-root-causes",
    "principle-foundational-thinking",
    "principle-guard-the-context-window",
    "principle-laziness-protocol",
    "principle-make-operations-idempotent",
    "principle-migrate-callers-then-delete-legacy-apis",
    "principle-minimize-reader-load",
    "principle-model-the-domain",
    "principle-never-block-on-the-human",
    "principle-outcome-oriented-execution",
    "principle-prove-it-works",
    "principle-redesign-from-first-principles",
    "principle-separate-before-serializing-shared-state",
    "principle-sequence-verifiable-units",
    "principle-subtract-before-you-add",
    "principle-test-behavior-not-implementation",
    "principle-type-system-discipline",
)

PRINCIPLES_PROVE = frozenset(
    {
        "principle-prove-it-works",
        "principle-test-behavior-not-implementation",
        "principle-sequence-verifiable-units",
    }
)

CATEGORIES: dict[str, tuple[str, ...]] = {
    "arena": ("fan-out",),
    "automate-me": ("write",),
    "blast-radius": ("prove",),
    "bro": ("constrain",),
    "create-verification-skill": ("write", "prove"),
    "figure-it-out": ("trail",),
    "how": ("explain",),
    "interrogate": ("fan-out",),
    "maintain-verification-skill": ("write", "prove"),
    "make-bot-ui": ("setup",),
    "no-comments": ("constrain",),
    "poteto-mode": ("constrain",),
    "recall": ("explain",),
    "reflect": ("write", "fan-out"),
    "setup-pstack": ("setup",),
    "show-me-your-work": ("trail",),
    "swarm": ("fan-out",),
    "tdd": ("prove",),
    "teach": ("explain",),
    "technical-writing": ("constrain",),
    "typescript-best-practices": ("constrain",),
    "unslop": ("constrain",),
    "why": ("fan-out", "explain"),
}

for _name in PRINCIPLE_SKILLS:
    CATEGORIES[_name] = (
        ("constrain", "prove") if _name in PRINCIPLES_PROVE else ("constrain",)
    )


def die(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def is_top_level(line: str) -> bool:
    return bool(line) and not line[0].isspace()


def split_skill(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        die("no opening frontmatter fence")
    rest = text[4:]
    idx = rest.find("\n---")
    if idx < 0:
        die("unclosed frontmatter")
    yaml_text = rest[:idx]
    after = rest[idx + len("\n---") :]
    body = after[1:] if after.startswith("\n") else after
    return yaml_text, body


def join_skill(yaml_text: str, body: str) -> str:
    yaml_text = yaml_text.strip("\n")
    if not body.endswith("\n"):
        body += "\n"
    return f"---\n{yaml_text}\n---\n{body}"


def format_metadata(tags: tuple[str, ...]) -> list[str]:
    if len(tags) == 1:
        return ["metadata:", f"  category: {tags[0]}"]
    return ["metadata:", "  category:"] + [f"    - {tag}" for tag in tags]


def apply_category(yaml_text: str, tags: tuple[str, ...]) -> str:
    lines = yaml_text.splitlines()
    meta_block = format_metadata(tags)
    start = next(
        (
            i
            for i, line in enumerate(lines)
            if is_top_level(line) and line.startswith("metadata:")
        ),
        None,
    )
    if start is not None:
        end = start + 1
        while end < len(lines) and not is_top_level(lines[end]):
            end += 1
        others: list[str] = []
        if lines[start] == "metadata:":
            i = start + 1
            while i < end:
                line = lines[i]
                if line.startswith("  category:"):
                    i += 1
                    while i < end and (
                        lines[i].startswith("    - ") or lines[i].startswith("      ")
                    ):
                        i += 1
                    continue
                others.append(line)
                i += 1
        lines = lines[:start] + meta_block + others + lines[end:]
        return "\n".join(lines)

    name_idx = next(
        (
            i
            for i, line in enumerate(lines)
            if is_top_level(line) and line.startswith("name:")
        ),
        None,
    )
    insert_at = 0 if name_idx is None else name_idx + 1
    return "\n".join(lines[:insert_at] + meta_block + lines[insert_at:])


def tag_file(path: Path, tags: tuple[str, ...]) -> str:
    original = path.read_text(encoding="utf-8")
    yaml_text, body = split_skill(original)
    updated = join_skill(apply_category(yaml_text, tags), body)
    if updated == original:
        return "unchanged"
    path.write_text(updated, encoding="utf-8")
    return "tagged"


def main() -> None:
    if not SKILLS.is_dir():
        die(f"missing {SKILLS}\nRun ./fetch first.")
    found = sorted(
        path.parent.name for path in SKILLS.glob("*/SKILL.md") if path.is_file()
    )
    if not found:
        die(f"no SKILL.md files under {SKILLS}")
    mapped = set(CATEGORIES) | SKIP
    extra = [name for name in found if name not in mapped]
    missing = sorted(name for name in mapped if name not in found)
    if extra:
        die(f"unmapped skills: {', '.join(extra)}")
    if missing:
        die(f"mapped skills missing from corpus: {', '.join(missing)}")

    tagged = 0
    unchanged = 0
    skipped = 0
    for name in found:
        if name in SKIP:
            print(f"skipped {name} (no category)")
            skipped += 1
            continue
        path = SKILLS / name / "SKILL.md"
        result = tag_file(path, CATEGORIES[name])
        label = ", ".join(CATEGORIES[name])
        print(f"{result} {name} -> {label}")
        if result == "tagged":
            tagged += 1
        else:
            unchanged += 1
    print(f"{tagged} tagged, {unchanged} unchanged, {skipped} skipped")


if __name__ == "__main__":
    main()
