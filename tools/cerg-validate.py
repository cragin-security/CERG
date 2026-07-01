#!/usr/bin/env python3
"""Validate CERG Markdown links, catalog references, and file inventory."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

CATALOG_FILE = "governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md"
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

def _metadata_versions(path: Path) -> list[tuple[str, int]]:
    """Yield (version, line_no) for every Version row in every metadata table of the file.

    A metadata table is a contiguous block of pipe-delimited rows starting with a row
    that declares the Document ID. Each metadata block can contain at most one
    Version row. This function does NOT consider Document Control section tables
    as separate concerns; if the file declares CERG-XXX-YYY-ZZZ in two tables,
    both Version rows are reported and the validator compares them.
    """
    text = path.read_text(encoding="utf-8")
    blocks: list[tuple[str, int]] = []  # (doc_id_of_this_block, line_of_version)
    current_doc_id: str | None = None
    current_version: tuple[str, int] | None = None
    in_metadata = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        # Detect start of a table: line begins with | and contains a Document ID row
        doc_id_match = re.search(r"\|\s*\*\*Document ID\*\*\s*\|\s*([A-Z0-9-]+)\s*\|", line)
        if doc_id_match:
            current_doc_id = doc_id_match.group(1)
            in_metadata = True
            current_version = None
            continue
        # Detect end of table: blank line or non-pipe content
        if in_metadata and not stripped.startswith("|"):
            if current_version is not None:
                blocks.append(current_version)
            in_metadata = False
            current_doc_id = None
            current_version = None
            continue
        # Capture Version row
        if in_metadata:
            version_match = re.search(r"\|\s*\*\*Version\*\*\s*\|\s*([^|\s]+)\s*\|", line)
            if version_match:
                current_version = (version_match.group(1).strip(), line_no)
    # End of file: flush
    if in_metadata and current_version is not None:
        blocks.append(current_version)
    return blocks



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


ANCHOR_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]*#([^)\s]+))\)")
SECTION_NUM_REF_RE = re.compile(r"§(\d+(?:\.\d+)*)")


def heading_to_anchor_id(heading_text: str) -> str:
    """Convert a markdown heading line to its auto-generated anchor ID.

    GitHub-style anchors use visible link text, lowercase text, removed
    punctuation, spaces as hyphens, and collapsed consecutive hyphens.
    """
    anchor = strip_markdown_links(heading_text).lower().strip()
    anchor = re.sub(r"[^a-z0-9\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor)
    anchor = re.sub(r"-{2,}", "-", anchor)
    anchor = anchor.strip("-")
    return anchor


def normalize_anchor(anchor: str) -> str:
    """Normalize an anchor reference for comparison.

    Collapses consecutive hyphens and strips leading/trailing hyphens
    so that #1--know-what-you-own and #1-know-what-you-own are treated
    as equivalent.
    """
    a = anchor.lower().strip()
    a = re.sub(r"-{2,}", "-", a)
    a = a.strip("-")
    return a


def extract_file_headings(path: Path) -> dict[str, str]:
    """Extract all section headings from a markdown file.

    Returns dict mapping anchor_id -> original heading text.
    Also stores normalized versions of each anchor for fuzzy matching.
    Only top-level (##) and sub-section (###) headings.
    """
    headings: dict[str, str] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return headings
    for match in re.finditer(r"^(#{2,3})\s+(.+)", text, flags=re.MULTILINE):
        heading_text = match.group(2).strip()
        # Strip trailing {#custom-anchor} if present
        heading_text = re.sub(r"\s*\{#[^}]+\}\s*$", "", heading_text).strip()
        anchor_id = heading_to_anchor_id(heading_text)
        if anchor_id:
            headings[anchor_id] = heading_text
            # Also store a normalized version (collapsed hyphens)
            normalized = normalize_anchor(anchor_id)
            if normalized != anchor_id and normalized not in headings:
                headings[normalized] = heading_text
    return headings


def check_anchor_drift(root: Path) -> list[str]:
    """Validate section anchor references in markdown links and plain text.

    Returns a list of warning strings (not CI-blocking).
    Checks:
    1. Same-file anchors: [text](#anchor) -> anchor exists in this file's headings
    2. Cross-file anchors: [text](file.md#anchor) -> anchor exists in target file's headings
    3. Heading text drift: link text substantially differs from heading text
    """
    root = root.resolve()
    warnings: list[str] = []

    # Pre-load all file headings for cross-file lookups
    file_headings_cache: dict[str, dict[str, str]] = {}

    for md_file in sorted(root.rglob("*.md")):
        rel_parts = md_file.relative_to(root).parts
        if any(p in IGNORED_DIRS for p in rel_parts):
            continue
        try:
            text = strip_code_blocks(md_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        rel_path = str(md_file.relative_to(root))

        # Load this file's own headings
        own_headings = extract_file_headings(md_file)
        file_headings_cache[str(md_file)] = own_headings

        # ── 1. Same-file anchor checks ──
        for link_match in ANCHOR_LINK_RE.finditer(text):
            link_text = link_match.group(1).strip()
            link_url = link_match.group(2).strip()
            anchor_only = link_match.group(3)

            # Skip external URLs
            if re.match(r"^[a-z][a-z0-9+.-]*:", link_url, flags=re.IGNORECASE):
                continue

            # Same-file anchors: link has no .md file part before the #
            if link_url.startswith("#"):
                target_anchor = anchor_only
                normalized_target = normalize_anchor(target_anchor)
                if own_headings and normalized_target not in own_headings:
                    # Try matching without the initial number prefix
                    found = False
                    for aid, htext in own_headings.items():
                        aid_norm = normalize_anchor(aid)
                        if normalized_target == aid_norm:
                            found = True
                            break
                        stripped_aid = re.sub(r"^\d+-", "", aid_norm)
                        stripped_target = re.sub(r"^\d+-", "", normalized_target)
                        if stripped_target == stripped_aid:
                            found = True
                            break
                    if not found:
                        warnings.append(
                            f"[ANCHOR_MISSING] {rel_path}: Same-file anchor "
                            f"'{target_anchor}' (from link '[{link_text}]({link_url})') "
                            f"does not match any heading in this file"
                        )

        # ── 2. Cross-file anchor checks ──
        for link_match in ANCHOR_LINK_RE.finditer(text):
            link_url = link_match.group(2).strip()

            # Skip same-file and external URLs
            if link_url.startswith("#"):
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*:", link_url, flags=re.IGNORECASE):
                continue

            # Must be file.md#anchor format
            if "#" not in link_url:
                continue

            file_part, anchor_part = link_url.split("#", 1)
            if not file_part or not anchor_part:
                continue

            # Resolve the target file
            target_path = md_file.parent / unquote(file_part)
            if not target_path.exists():
                continue

            # Load target headings if not cached
            target_key = str(target_path)
            if target_key not in file_headings_cache:
                file_headings_cache[target_key] = extract_file_headings(target_path)

            target_headings = file_headings_cache.get(target_key, {})
            if target_headings and anchor_part not in target_headings:
                normalized_anchor = normalize_anchor(anchor_part)
                if normalized_anchor not in target_headings:
                    found = False
                    for aid in target_headings:
                        aid_norm = normalize_anchor(aid)
                        if normalized_anchor == aid_norm:
                            found = True
                            break
                        stripped_aid = re.sub(r"^\d+-", "", aid_norm)
                        stripped_target = re.sub(r"^\d+-", "", normalized_anchor)
                        if stripped_target == stripped_aid:
                            found = True
                            break
                    if not found:
                        warnings.append(
                            f"[ANCHOR_MISSING] {rel_path}: Cross-file anchor "
                            f"'{anchor_part}' not found in {target_path.name} "
                            f"(from link '[{link_match.group(1).strip()}]({link_url})')"
                        )

        # ── 3. Heading text drift check ──
        for link_match in ANCHOR_LINK_RE.finditer(text):
            link_text = link_match.group(1).strip()
            link_url = link_match.group(2).strip()

            if not link_url.startswith("#"):
                continue

            target_anchor = link_match.group(3)
            normalized_target = normalize_anchor(target_anchor)
            actual_heading = own_headings.get(target_anchor) or own_headings.get(normalized_target)
            if actual_heading:
                link_normalized = re.sub(r"[^a-z0-9]", "", link_text.lower())
                heading_normalized = re.sub(r"[^a-z0-9]", "", actual_heading.lower())
                if link_normalized and heading_normalized:
                    overlap = len(set(link_normalized) & set(heading_normalized))
                    union = len(set(link_normalized) | set(heading_normalized))
                    if union > 0 and (overlap / union) < 0.3:
                        if "table of contents" not in text[:100].lower():
                            warnings.append(
                                f"[HEADING_DRIFT] {rel_path}: Link text '{link_text}' differs "
                                f"significantly from heading '{actual_heading}' "
                                f"(anchor '{target_anchor}')"
                            )

    return warnings


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
            catalog_file_path_ = root / CATALOG_FILE
            target = catalog_file_path_.parent / entry.file_path
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

    # Check that metadata tables within the same file agree on Version.
    # CERG-GOV-CAT-001 has two metadata tables (front-matter and §8 Document Control).
    # Other governance documents may follow the same pattern. If the front-matter
    # version disagrees with the Document Control version, contributors may pick
    # one or the other and ship a document where the two metadata blocks diverge.
    for doc in docs:
        if doc.doc_id is None:
            continue
        metadata_versions = list(_metadata_versions(doc.path))
        if len(metadata_versions) >= 2:
            unique_versions = {v for v, _ in metadata_versions}
            if len(unique_versions) > 1:
                version_list = ", ".join(f"'{v}'" for v, _ in metadata_versions)
                findings.append(
                    Finding(
                        "METADATA_VERSION_MISMATCH",
                        str(doc.path.relative_to(root)),
                        f"{doc.doc_id} has multiple metadata tables with different Version values: {version_list}. Update all metadata tables to agree.",
                    )
                )

    return sorted(findings, key=lambda item: (item.path, item.code, item.message))





# ── P1 Checks: Quality gates (warnings only — do not block CI) ──

def quality_checks(root, catalog):
    """Run quality checks. Returns (errors, warnings) tuple.
    Errors block CI (exit code 1). Warnings are informational.
    """
    errors = []
    warnings = []
    
    # Track files seen (to avoid duplicate checks)
    for filepath in sorted(root.glob("**/*.md")):
        if any(p in str(filepath) for p in [".git", "machine-readable", "README.md"]):
            continue
        
        rel = str(filepath.relative_to(root))
        try:
            raw = filepath.read_bytes()
            text = raw.decode("utf-8")
        except Exception:
            continue

        # E0: basic Markdown structural sanity checks that link validation will not catch.
        if raw and not raw.endswith(b"\n"):
            errors.append(f"[MISSING_FINAL_NEWLINE] {rel}: file does not end with a newline")

        numeric_headings = []
        numeric_subsections = []
        in_code_block = False
        for line_no, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            if line.startswith("|") and not line.rstrip().endswith("|"):
                errors.append(f"[MALFORMED_TABLE_ROW] {rel}:{line_no}: table row starts with '|' but does not end with '|'")

            heading = re.match(r"^## (\d+)\.\s+", line)
            if heading:
                numeric_headings.append((line_no, int(heading.group(1))))

            subsection = re.match(r"^### (\d+)\.(\d+)\s+", line)
            if subsection:
                numeric_subsections.append((line_no, subsection.group(1), subsection.group(2)))

        if len(numeric_headings) >= 2:
            got = [number for _, number in numeric_headings]
            expected = list(range(1, len(got) + 1))
            if got != expected:
                detail = ", ".join(f"line {line}: {number}" for line, number in numeric_headings)
                errors.append(f"[SECTION_NUMBERING] {rel}: top-level numbered headings are {got}, expected {expected} ({detail})")

        seen_subsections = set()
        for line_no, parent, child in numeric_subsections:
            key = (parent, child)
            if key in seen_subsections:
                errors.append(f"[DUPLICATE_SUBSECTION] {rel}:{line_no}: duplicate subsection heading ### {parent}.{child}")
            seen_subsections.add(key)
        
        # Extract metadata
        doc_id = None
        status = None
        approver = None
        version = None
        classification = None
        owner = None
        review_cycle = None
        
        for line in text.split('\n')[:35]:
            m = re.match(r'\|\s*\*\*(Document ID|Status|Approved By|Version|Classification|Owner|Review Cycle)\*\*\s*\|\s*(.+?)\s*\|', line)
            if m:
                field = m.group(1)
                value = m.group(2).strip()
                if field == 'Document ID': doc_id = value
                elif field == 'Status': status = value
                elif field == 'Approved By': approver = value
                elif field == 'Version': version = value
                elif field == 'Classification': classification = value
                elif field == 'Owner': owner = value
                elif field == 'Review Cycle': review_cycle = value
        
        doc_type = doc_id.split('-')[1] if doc_id and '-' in doc_id else None
        
        # ── BLOCKING ERRORS ──
        
        # E1: DRAFT in Version field (contradicts Approved status)
        if version and 'draft' in version.lower():
            errors.append(f"[DRAFT_VERSION] {rel} ({doc_id}): Version contains 'DRAFT' — remove or change Status to Draft")
        
        # E2: Internal / Restricted classification in public reference corpus
        if classification:
            cl = classification.lower().strip()
            if 'internal' in cl or 'restricted' in cl:
                errors.append(f"[RESTRICTED_CLASSIFICATION] {rel} ({doc_id}): Classification '{classification}' not allowed in public reference corpus — use 'Public'")
        
        # E3: Approved status with Pending approver
        if status and status.lower().strip() == 'approved':
            if approver and 'pending' in approver.lower():
                errors.append(f"[APPROVED_PENDING] {rel} ({doc_id}): Status=Approved but Approved By='{approver}'")
        
        # E4: Missing mandatory metadata fields
        required_fields = {
            'POL': ['Document ID', 'Version', 'Status', 'Classification', 'Owner', 'Review Cycle'],
            'STD': ['Document ID', 'Version', 'Status', 'Classification', 'Owner', 'Parent Policy', 'Review Cycle'],
            'PRC': ['Document ID', 'Version', 'Status', 'Classification', 'Owner', 'Parent Policy', 'Review Cycle'],
            'PLN': ['Document ID', 'Version', 'Status', 'Classification', 'Owner', 'Parent Policy', 'Review Cycle'],
            'TMPL': ['Document ID', 'Version', 'Status', 'Classification', 'Owner'],
            'GOV': ['Document ID', 'Version', 'Status', 'Classification', 'Owner', 'Review Cycle'],
        }
        
        if doc_type in required_fields:
            for field in required_fields[doc_type]:
                found = False
                for line in text.split('\n')[:35]:
                    if f'**{field}**' in line:
                        found = True
                        break
                if not found:
                    errors.append(f"[MISSING_METADATA] {rel} ({doc_id}): missing required field '{field}' for type {doc_type}")
        
        # ── WARNINGS (do not block CI) ──
        
        # W1: TBD or placeholder in Approved doc
        if status and status.lower().strip() == 'approved':
            placeholders = ['TBD', 'TODO', 'placeholder', 'Placeholder', '[To be', '[TBD', 'N/A \u2014']
            for ph in placeholders:
                if ph in text:
                    count = text.count(ph)
                    if count > 0:
                        warnings.append(f"[PLACEHOLDER_IN_APPROVED] {rel}: contains '{ph}' ({count} occurrences)")
                        break
        
        # W2: Org-specific text — utility narrative outside /examples/
        if 'examples/' not in rel:
            org_patterns = [
                ('14,000 employee', 'utility-scale headcount'),
                ('major electrical utility', 'utility sector narrative'),
                ('electric utility', 'utility sector default'),
                ('60-person CERG team', 'utility team size'),
            ]
            for pattern, desc in org_patterns:
                if pattern in text:
                    warnings.append(f"[ORG_SPECIFIC_TEXT] {rel}: contains '{pattern}' ({desc}) — use generic language or move to /examples/")
                    break
        
        # W3: Stale website language — cerg.nexus as authoritative
        stale_web_patterns = [
            'The full corpus is available at [cerg.nexus]',
            'authoritative mirror',
        ]
        for pat in stale_web_patterns:
            if pat in text:
                warnings.append(f"[STALE_WEBSITE] {rel}: contains stale website reference — GitHub is authoritative, site is convenience mirror")
                break
    
    # ── ANCHOR DRIFT CHECKS (warnings) ──
    try:
        warnings.extend(check_anchor_drift(root))
    except Exception:
        pass
    
    return errors, warnings

def print_quality_report(errors, warnings, root):
    """Print a structured quality report."""
    from collections import Counter
    
    if errors:
        print(f"\nBLOCKING ERRORS: {len(errors)}")
        err_cats = Counter()
        for e in errors:
            cat = e.split(']')[0].replace('[', '')
            err_cats[cat] += 1
        for cat, count in err_cats.most_common():
            print(f"  [{cat}]: {count}")
        print()
        for e in errors[:30]:
            print(f"  {e}")
        if len(errors) > 30:
            print(f"  ... and {len(errors)-30} more")
    
    if warnings:
        print(f"\nWARNINGS: {len(warnings)}")
        warn_cats = Counter()
        for w in warnings:
            cat = w.split(']')[0].replace('[', '')
            warn_cats[cat] += 1
        for cat, count in warn_cats.most_common():
            print(f"  [{cat}]: {count}")
        print(f"\n  --- Detail ---")
        for w in warnings[:20]:
            print(f"  {w}")
        if len(warnings) > 20:
            print(f"  ... and {len(warnings)-20} more")
    
    if not errors and not warnings:
        print("\nQuality Checks: 0 issues — PASS")


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
    
    # Quality checks (errors block CI, warnings are informational)
    root_path = Path(args.root)
    catalog = parse_catalog(root_path)
    errors, warnings = quality_checks(root_path, catalog)
    print_quality_report(errors, warnings, root_path)
    
    if errors:
        print(f"\nCERG CI FAILED: {len(errors)} blocking error(s)")
        return 1
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
