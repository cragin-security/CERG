#!/usr/bin/env python3
"""Validate CERG Markdown links, catalog references, and file inventory."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

CATALOG_FILE = "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md"
DOC_ID_PATTERN = r"CERG-(?:POL-\d{3}|(?:STD|PRC|PLN|GL|TMPL|GOV)-[A-Z]{2,8}(?:-[A-Z]{2,8})?-\d{3})"
DOC_ID_RE = re.compile(rf"\b{DOC_ID_PATTERN}\b")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
METADATA_ROW_RE = re.compile(r"\|\s*\*\*(Document ID|Status)\*\*\s*\|\s*([^|]+?)\s*\|", re.IGNORECASE)
CATALOG_ROW_RE = re.compile(
    rf"^\|\s*(?:\[`(?P<linked_id>{DOC_ID_PATTERN})`\]\((?P<link>[^)]+)\)|`(?P<plain_id>{DOC_ID_PATTERN})`)\s*\|(?P<rest>.*)\|\s*$"
)
IGNORED_DIRS = {".git", ".github", ".pytest_cache", "__pycache__", "node_modules", "rendered"}
PLACEHOLDER_IDS = {"CERG-XXX-YYY-NNN"}
EMBEDDED_OR_RESERVED_IDS = {
    "CERG-PRC-AC-001",
    "CERG-GL-OT-001",
    "CERG-GOV-CIP-001",
    "CERG-TMPL-CIP-001",
}


@dataclass(frozen=True)
class CatalogEntry:
    doc_id: str
    file_path: str | None
    status: str


@dataclass(frozen=True)
class DocumentFile:
    path: Path
    doc_id: str | None
    status: str | None


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        rel_parts = path.relative_to(root).parts
        if any(part in IGNORED_DIRS for part in rel_parts):
            continue
        files.append(path)
    return sorted(files)


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def strip_markdown_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def normalize_status(value: str | None) -> str | None:
    if value is None:
        return None
    text = re.sub(r"<[^>]+>", "", value)
    text = re.sub(r"[`*_]", "", text).strip()
    text = re.sub(r"\s+", " ", text)
    if text.startswith("Approved (") or text == "Published":
        return "Approved"
    return text or None


def parse_document_metadata(path: Path) -> DocumentFile:
    text = path.read_text(encoding="utf-8")
    doc_id: str | None = None
    status: str | None = None
    for match in METADATA_ROW_RE.finditer(text[:3000]):
        field = match.group(1).lower()
        value = normalize_status(match.group(2))
        if field == "document id":
            cleaned_value = strip_markdown_links(value or "")
            id_match = DOC_ID_RE.search(cleaned_value)
            doc_id = id_match.group(0) if id_match else cleaned_value
        elif field == "status":
            status = value
    return DocumentFile(path=path, doc_id=doc_id, status=status)


def section_between(text: str, start_pattern: str, end_pattern: str) -> str:
    start = re.search(start_pattern, text, flags=re.MULTILINE)
    if not start:
        return ""
    end = re.search(end_pattern, text[start.end() :], flags=re.MULTILINE)
    if not end:
        return text[start.end() :]
    return text[start.end() : start.end() + end.start()]


def parse_catalog(root: Path) -> dict[str, CatalogEntry]:
    catalog_path = root / CATALOG_FILE
    text = catalog_path.read_text(encoding="utf-8")
    section = section_between(text, r"^## 5\. ", r"^## 6\. ")
    entries: dict[str, CatalogEntry] = {}
    for line in section.splitlines():
        match = CATALOG_ROW_RE.match(line.strip())
        if not match:
            continue
        doc_id = match.group("linked_id") or match.group("plain_id")
        link = match.group("link")
        cells = [cell.strip() for cell in match.group("rest").split("|")]
        status = normalize_status(cells[-1] if cells else "") or ""
        entries[doc_id] = CatalogEntry(doc_id=doc_id, file_path=unquote(link) if link else None, status=status)
    return entries


def find_markdown_links(text: str) -> list[str]:
    targets: list[str] = []
    for match in MARKDOWN_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith("#"):
            continue
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, flags=re.IGNORECASE):
            continue
        targets.append(target)
    return targets


def link_target_exists(source: Path, target: str) -> bool:
    target = target.split("#", 1)[0].strip()
    if not target:
        return True
    target = unquote(target)
    return (source.parent / target).exists()


def document_ids_in_text(text: str) -> set[str]:
    clean = strip_code_blocks(text)
    return {
        match.group(0)
        for match in DOC_ID_RE.finditer(clean)
        if match.group(0) not in PLACEHOLDER_IDS and match.group(0) not in EMBEDDED_OR_RESERVED_IDS
    }


def validate_repository(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    catalog = parse_catalog(root)
    catalog_ids = set(catalog)
    docs = [parse_document_metadata(path) for path in markdown_files(root)]
    docs_by_id = {doc.doc_id: doc for doc in docs if doc.doc_id}

    for doc in docs:
        rel_path = str(doc.path.relative_to(root))
        text = strip_code_blocks(doc.path.read_text(encoding="utf-8"))

        for target in find_markdown_links(text):
            if not link_target_exists(doc.path, target):
                findings.append(Finding("LINK_MISSING", rel_path, f"Markdown link target '{target}' does not resolve"))

        for cited_id in document_ids_in_text(text):
            if cited_id not in catalog_ids:
                findings.append(Finding("ID_NOT_IN_CATALOG", rel_path, f"{cited_id} is cited but not listed in catalog Section 5"))

        if doc.doc_id and doc.path.name != CATALOG_FILE:
            if doc.doc_id not in catalog_ids:
                findings.append(Finding("FILE_NOT_IN_CATALOG", rel_path, f"{doc.doc_id} has no Section 5 catalog entry"))
            else:
                expected = normalize_status(catalog[doc.doc_id].status)
                actual = normalize_status(doc.status)
                if expected and actual and expected != actual:
                    findings.append(
                        Finding(
                            "STATUS_MISMATCH",
                            rel_path,
                            f"{doc.doc_id} status mismatch: file has '{actual}', catalog has '{expected}'",
                        )
                    )

    for entry in catalog.values():
        if entry.file_path:
            target = root / entry.file_path
            if not target.exists():
                findings.append(
                    Finding(
                        "CATALOG_FILE_MISSING",
                        CATALOG_FILE,
                        f"{entry.doc_id} catalog entry points to missing file '{entry.file_path}'",
                    )
                )
            else:
                doc = parse_document_metadata(target)
                if doc.doc_id and doc.doc_id != entry.doc_id:
                    findings.append(
                        Finding(
                            "CATALOG_ID_MISMATCH",
                            CATALOG_FILE,
                            f"{entry.doc_id} catalog link points to file declaring {doc.doc_id}",
                        )
                    )
        elif entry.doc_id not in docs_by_id and entry.doc_id != "CERG-GOV-CAT-001":
            findings.append(
                Finding("CATALOG_FILE_MISSING", CATALOG_FILE, f"{entry.doc_id} catalog entry points to missing file")
            )

    return sorted(findings, key=lambda item: (item.path, item.code, item.message))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Repository root to validate")
    args = parser.parse_args(argv)

    findings = validate_repository(Path(args.root))
    if findings:
        print("CERG validation failed:")
        for finding in findings:
            print(f"- {finding.path}: [{finding.code}] {finding.message}")
        return 1
    print("CERG validation passed: links, catalog references, and file inventory are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
