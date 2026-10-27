#!/usr/bin/env python3
"""Synchronize source-document lifecycle statuses into CAT-001 §5.

The Document Catalog is authoritative for the inventory, titles, owners, order,
and roadmap.  This utility deliberately changes only the final Status cell of
existing §5 catalog rows.  It must not rebuild catalog tables from filenames.

Usage:
    python3 tools/cerg-catalog-sync.py --dry-run    # show status-only diff
    python3 tools/cerg-catalog-sync.py --write      # apply status-only updates
    python3 tools/cerg-catalog-sync.py --ci         # fail if statuses differ
"""

import argparse
import difflib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md"
EXCLUDE_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", "machine-readable", "tools", "policy-as-code", "scripts", "assets"}
DOC_ID_RE = re.compile(r"CERG-(?:[A-Z]+-)+\d{3}")
STATUS_RE = re.compile(r"\|\s*\*\*Status\*\*\s*\|\s*(\S[^|]*?)\s*\|")


def find_documents(root: Path) -> list[Path]:
    """Return governed Markdown sources with a CERG identifier in the name."""
    documents = []
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if any(part in EXCLUDE_DIRS for part in relative.parts):
            continue
        if path.name in {"README.md", "CONTRIBUTING.md", "AGENTS.md", "CHANGELOG.md"}:
            continue
        if DOC_ID_RE.search(path.name):
            documents.append(path)
    return sorted(documents)


def document_id(path: Path) -> str | None:
    match = DOC_ID_RE.search(path.name)
    return match.group(0) if match else None


def metadata_status(path: Path) -> str | None:
    match = STATUS_RE.search(path.read_text(encoding="utf-8"))
    return match.group(1).strip() if match else None


def section_five_bounds(text: str) -> tuple[int, int]:
    start = re.search(r"^## 5\. ", text, flags=re.MULTILINE)
    if not start:
        raise ValueError("Cannot find §5 catalog section in CAT-001")
    following = re.search(r"^## \d+\. ", text[start.end():], flags=re.MULTILINE)
    if not following:
        raise ValueError("Cannot find the end of CAT-001 §5")
    return start.start(), start.end() + following.start()


def sync_statuses(catalog_text: str, source_statuses: dict[str, str]) -> str:
    """Update only the Status cell of existing catalog rows in §5."""
    start, end = section_five_bounds(catalog_text)
    section_lines = catalog_text[start:end].splitlines(keepends=True)

    for index, line in enumerate(section_lines):
        match = DOC_ID_RE.search(line)
        if not match or match.group(0) not in source_statuses or not line.lstrip().startswith("|"):
            continue

        # Catalog §5 uses four columns: ID, title, owner, status.  Replace the
        # final non-empty cell so link/title/owner formatting and table layout
        # stay exactly as maintained by CAT-001.
        cells = line.rstrip("\n").split("|")
        populated = [position for position, cell in enumerate(cells) if cell.strip()]
        if len(populated) < 4:
            continue
        source_status = source_statuses[match.group(0)]
        catalog_status = cells[populated[-1]].strip()
        # CAT-001 may annotate its own row (for example, "Approved (this
        # doc)").  That annotation is not lifecycle-status drift.
        if catalog_status == source_status or catalog_status.startswith(f"{source_status} ("):
            continue
        cells[populated[-1]] = f" {source_status} "
        newline = "\n" if line.endswith("\n") else ""
        section_lines[index] = "|".join(cells) + newline

    return catalog_text[:start] + "".join(section_lines) + catalog_text[end:]


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync source Status metadata to CAT-001 §5")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Show status-only differences (default)")
    mode.add_argument("--write", action="store_true", help="Apply status-only updates")
    mode.add_argument("--ci", action="store_true", help="Exit 1 when statuses differ")
    args = parser.parse_args()

    documents = find_documents(REPO_ROOT)
    statuses = {
        doc_id: status
        for path in documents
        if (doc_id := document_id(path)) and (status := metadata_status(path))
    }
    print(f"Found {len(statuses)} CERG documents with Status metadata", file=sys.stderr)

    catalog_text = CATALOG_PATH.read_text(encoding="utf-8")
    try:
        updated_text = sync_statuses(catalog_text, statuses)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if updated_text == catalog_text:
        print("Catalog statuses are up to date.")
        return 0

    diff = difflib.unified_diff(
        catalog_text.splitlines(keepends=True),
        updated_text.splitlines(keepends=True),
        fromfile=str(CATALOG_PATH),
        tofile=str(CATALOG_PATH),
    )
    sys.stdout.writelines(diff)
    if args.write:
        CATALOG_PATH.write_text(updated_text, encoding="utf-8")
        print("Updated catalog statuses.")
        return 0

    print("Catalog status drift detected. Run with --write to apply.", file=sys.stderr)
    return 1 if args.ci else 0


if __name__ == "__main__":
    raise SystemExit(main())
