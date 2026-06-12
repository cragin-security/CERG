#!/usr/bin/env python3
"""CERG Corpus Integrity Checker
Checks document metadata, cross-references, and consistency across the CERG corpus.
Run: python3 tools/cerg-integrity-check.py
"""

import os
import re
import sys
import hashlib
from datetime import datetime, timedelta
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Helpers ──────────────────────────────────────────────

def find_md_files():
    """Find all .md files in the CERG repository."""
    files = []
    for root, dirs, filenames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('machine-readable', 'flows')]
        for f in filenames:
            if f.endswith('.md') and not f.startswith('.') and not os.path.basename(f) in ('README.md',):
                files.append(os.path.join(root, f))
    return files


def parse_metadata(filepath):
    """Extract metadata from the first ~30 lines of a CERG document."""
    meta = {'document_id': None, 'version': None, 'status': None, 
            'classification': None, 'owner': None, 'next_review_date': None}
    
    with open(filepath) as f:
        lines = f.readlines()
    
    content = ''.join(lines)
    
    for line in lines[:30]:
        m_id = re.match(r'\|\s*\*\*Document ID\*\*\s*\|\s*(CERG-[A-Z]+-[A-Z]+(?:-[A-Z]+)?-\d+)\s*\|', line)
        m_ver = re.match(r'\|\s*\*\*Version\*\*\s*\|\s*(.+?)\s*\|', line)
        m_status = re.match(r'\|\s*\*\*Status\*\*\s*\|\s*(.+?)\s*\|', line)
        m_class = re.match(r'\|\s*\*\*Classification\*\*\s*\|\s*(.+?)\s*\|', line)
        m_owner = re.match(r'\|\s*\*\*Owner\*\*\s*\|\s*(.+?)\s*\|', line)
        
        if m_id: meta['document_id'] = m_id.group(1)
        if m_ver: meta['version'] = m_ver.group(1).strip()
        if m_status: meta['status'] = m_status.group(1).strip()
        if m_class: meta['classification'] = m_class.group(1).strip()
        if m_owner: meta['owner'] = m_owner.group(1).strip()
    
    # Check for next review date in Document Control section
    m_review = re.search(r'\|\s*\*\*Next Scheduled Review\*\*\s*\|\s*(.+?)\s*\|', content)
    if m_review:
        meta['next_review_date'] = m_review.group(1).strip()
    
    return meta, content


def find_markdown_links(content):
    """Find all markdown links pointing to .md files."""
    return re.findall(r'\]\(([^)]+\.md)\)', content)


def find_cross_refs(content):
    """Find Document ID references like CERG-XXX-XXX-XXX."""
    return set(re.findall(r'CERG-[A-Z]+-[A-Z]+-\d+', content))


def load_catalog():
    """Parse CAT-001 to get the authoritative catalog entries."""
    cat_path = os.path.join(BASE, 'CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md')
    if not os.path.exists(cat_path):
        return {}
    
    with open(cat_path) as f:
        cat_content = f.read()
    
    catalog = {}
    for line in cat_content.split('\n'):
        # Try linked format: | [`ID`](file.md) | Title | Owner | Status |
        m = re.match(r'\|\s*\[?`?(CERG-[A-Z]+-[A-Z]+-\d+)`?\]?\(.+?\.md\)?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|', line)
        if not m:
            # Try unlinked format: | `ID` | Title | Owner | Status |
            m = re.match(r'\|\s*`?(CERG-[A-Z]+-[A-Z]+-\d+)`?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|', line)
        if m:
            doc_id = m.group(1)
            catalog[doc_id] = {
                'title': m.group(2).strip(),
                'owner': m.group(3).strip(),
                'status': m.group(4).strip()
            }
    return catalog


# ── Checks ───────────────────────────────────────────────

def check_all():
    files = find_md_files()
    catalog = load_catalog()
    
    issues = defaultdict(list)  # severity -> list of messages
    known_files = {os.path.basename(f): f for f in files}
    id_to_file = {}
    
    print(f"CERG Integrity Check")
    print(f"{'='*60}")
    print(f"Files found: {len(files)}")
    print(f"Catalog entries: {len(catalog)}")
    print()
    
    # First pass: collect document IDs
    for filepath in sorted(files):
        relpath = os.path.relpath(filepath, BASE)
        meta, content = parse_metadata(filepath)
        doc_id = meta['document_id']
        
        if doc_id:
            id_to_file[doc_id] = relpath
    
    # Second pass: check each file
    for filepath in sorted(files):
        relpath = os.path.relpath(filepath, BASE)
        meta, content = parse_metadata(filepath)
        doc_id = meta['document_id']
        filename = os.path.basename(filepath)
        
        # P0: Missing Document ID
        if not doc_id:
            issues['P0'].append(f"[missing_document_id] {relpath}: No Document ID found in metadata")
            continue
        
        # P0: Duplicate Document ID
        if doc_id in id_to_file and id_to_file[doc_id] != relpath:
            issues['P0'].append(f"[duplicate_document_id] {relpath}: Document ID {doc_id} already used by {id_to_file[doc_id]}")
        
        # P1: Missing owner
        if not meta['owner']:
            issues['P1'].append(f"[missing_owner] {relpath} ({doc_id}): No Owner in metadata")
        
        # P0: Missing classification
        if not meta['classification']:
            issues['P0'].append(f"[missing_classification] {relpath} ({doc_id}): No Classification in metadata")
        
        # P1: Missing version
        if not meta['version']:
            issues['P1'].append(f"[missing_version] {relpath} ({doc_id}): No Version in metadata")
        
        # P0: Status mismatch between file and catalog
        if doc_id in catalog:
            cat_status = catalog[doc_id]['status']
            file_status = meta['status']
            # Normalize - treat Published and Approved as equivalent
            cat_norm = cat_status.lower().strip()
            file_norm = file_status.lower().strip() if file_status else ''
            # Published and Approved are equivalent in this corpus
            equivalent = {'approved', 'published', 'for review'}
            if file_norm and cat_norm and file_norm != cat_norm:
                if not (cat_norm in equivalent and file_norm in equivalent):
                    issues['P0'].append(f"[status_mismatch] {relpath} ({doc_id}): file='{file_status}' vs catalog='{cat_status}'")
        
        # P2: Stale review date
        review_date = meta.get('next_review_date')
        if review_date:
            try:
                rd = datetime.strptime(review_date, '%Y-%m-%d')
                if rd < datetime.now():
                    issues['P2'].append(f"[stale_review_date] {relpath} ({doc_id}): Next review {review_date} is in the past")
            except ValueError:
                issues['P2'].append(f"[stale_review_date] {relpath} ({doc_id}): Unparseable date '{review_date}'")
        
        # P1: Broken cross-references (markdown links)
        links = find_markdown_links(content)
        for link in links:
            clean_link = link.split('#')[0]  # strip anchor
            if clean_link not in known_files:
                issues['P1'].append(f"[broken_cross_reference] {relpath} ({doc_id}): links to non-existent file '{link}'")
        
        # P2: Cross-reference to non-catalog IDs
        refs = find_cross_refs(content)
        for ref in refs:
            if ref != doc_id and ref not in catalog:
                issues['P2'].append(f"[unknown_id_reference] {relpath} ({doc_id}): references {ref} which is not in the catalog")
    
    # P0: Check catalog entries that have no corresponding file
    for cat_id, cat_data in catalog.items():
        if cat_id not in id_to_file:
            issues['P0'].append(f"[file_not_found] catalog entry {cat_id} ({cat_data['title']}) has no corresponding .md file")
    
    # ── Report ──────────────────────────────────────────────
    
    print("RESULTS")
    print("="*60)
    
    total_issues = 0
    for severity in ['P0', 'P1', 'P2']:
        iss = issues.get(severity, [])
        total_issues += len(iss)
        tag = 'FAIL' if severity == 'P0' else ('WARN' if severity == 'P1' else 'INFO')
        print(f"\n[{severity}] {tag} — {len(iss)} issue(s)")
        for msg in sorted(iss)[:20]:  # limit output
            print(f"  {msg}")
        if len(iss) > 20:
            print(f"  ... and {len(iss) - 20} more")
    
    print(f"\n{'='*60}")
    print(f"Total issues: {total_issues}")
    
    p0_count = len(issues.get('P0', []))
    if p0_count > 0:
        print(f"P0 defects: {p0_count} — CORPUS BUILD SHOULD FAIL")
        return 1
    else:
        print("P0 defects: 0 — PASS")
        return 0


if __name__ == '__main__':
    sys.exit(check_all())
