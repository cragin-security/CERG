#!/usr/bin/env python3
"""Regenerate machine-readable/cerg-llm-index.json from local Markdown.

The previous implementation depended on the public llms-full.txt mirror, which can
lag the repository. This script treats the local Markdown corpus as authoritative
and computes stable repo-relative paths for LLM/agent consumption.

Run from repo root: python3 tools/regenerate-llm-index.py
"""

from __future__ import annotations

import json
import os
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "machine-readable" / "cerg-llm-index.json"
EXCLUDED_DIRS = {".git", ".github", ".pytest_cache", "__pycache__", "node_modules", "rendered"}
DOC_ID_RE = re.compile(r"CERG-(?:POL-\d{3}|(?:STD|PRC|PLN|GL|TMPL|GOV)-[A-Z]{2,8}(?:-[A-Z]{2,8})?-\d{3})")
META_ROW_RE = re.compile(r"^\|\s*\*\*(?P<key>[^*]+)\*\*\s*\|\s*(?P<value>.*?)\s*\|\s*$")

PREFIXES = {
    "POL": {"type": "Policy", "pillar": "governance"},
    "GOV": {"type": "Governance Instrument", "pillar": "governance"},
    "STD": {"type": "Standard", "pillar": "engineering"},
    "PRC": {"type": "Procedure", "pillar": "risk"},
    "PLN": {"type": "Plan / Package", "pillar": "governance"},
    "GL": {"type": "Guideline", "pillar": "governance"},
    "TMPL": {"type": "Template", "pillar": "governance"},
    "JF": {"type": "Job Family", "pillar": "workforce"},
    "JD": {"type": "Job Description", "pillar": "workforce"},
    "META": {"type": "Repository Metadata", "pillar": "cross-cutting"},
}

FALLBACK_SUMMARY = {
    "README": "CERG repository root — project overview, adoption paths, architecture, reader guides.",
    "START-HERE": "First 48 hours adoption guide — Lite, Standard, and Regulated paths.",
    "CONTRIBUTING": "Contributing guide — validation requirements, conventions, PR workflow.",
    "ROADMAP": "CERG development roadmap and planned improvement workstreams.",
    "SECURITY": "Security policy and vulnerability disclosure.",
    "CODE_OF_CONDUCT": "Community code of conduct for CERG contributors.",
    "AGENTS": "Guide for AI agents working on CERG — conventions, pitfalls, tools, git workflow.",
}


def clean_value(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "")
    return " ".join(value.split())


def metadata(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    lines = text[:6000].splitlines()
    for idx, line in enumerate(lines):
        if line.strip() != "| | |":
            continue
        for row in lines[idx + 1 :]:
            if not row.startswith("|"):
                if data:
                    return data
                continue
            if row.strip() == "|---|---|":
                continue
            m = META_ROW_RE.match(row)
            if m:
                data[m.group("key").strip()] = clean_value(m.group("value").strip())
            elif data:
                return data
        break
    return data


def extract_id(path: Path, text: str, meta: dict[str, str]) -> str:
    if meta.get("Document ID"):
        return meta["Document ID"]
    m = DOC_ID_RE.search(path.name)
    if m:
        return m.group(0)
    if path.name == "README.md" and path.parent != ROOT:
        rel_parent = path.parent.relative_to(ROOT).as_posix().replace("/", "-")
        return f"README-{rel_parent}"
    return path.stem


def prefix_for(doc_id: str) -> str:
    if doc_id.startswith("CERG-GOV-JF-"):
        return "JF"
    if doc_id.startswith("CERG-GOV-JD-"):
        return "JD"
    if doc_id.startswith("CERG-"):
        return doc_id.split("-")[1]
    return "META"


def type_and_pillar(path: Path, doc_id: str) -> tuple[str, str, str]:
    rel = path.relative_to(ROOT)
    prefix = prefix_for(doc_id)
    if prefix == "POL":
        return "policy", "governance", prefix
    if prefix == "GOV":
        if doc_id.startswith("CERG-GOV-JF-"):
            return "job-family", "workforce", "JF"
        if doc_id.startswith("CERG-GOV-JD-"):
            return "job-description", "workforce", "JD"
        if doc_id in {"CERG-GOV-RMF-001", "CERG-GOV-TAX-001"}:
            return "governance-instrument", "risk", prefix
        if doc_id in {"CERG-GOV-CB-001", "CERG-GOV-TRC-001", "CERG-GOV-CEF-001"}:
            return "governance-instrument", "engineering", prefix
        return "governance-instrument", "governance", prefix
    if prefix == "STD":
        return "standard", "engineering", prefix
    if prefix == "PRC":
        return "procedure", "risk", prefix
    if prefix == "PLN":
        return "plan", "governance", prefix
    if prefix == "GL":
        return "guideline", "governance", prefix
    if prefix == "TMPL":
        return "template", "governance", prefix
    if rel.parts[0] == "roles":
        return ("job-family", "workforce", "JF") if "JF" in doc_id else ("job-description", "workforce", "JD")
    return ("readme" if path.name == "README.md" or path.parent == ROOT else "meta"), "cross-cutting", "META"


def title_for(path: Path, doc_id: str, meta: dict[str, str]) -> str:
    if doc_id.startswith("CERG-") and path.stem.startswith(doc_id + "_"):
        return path.stem[len(doc_id) + 1 :].replace("_", " ")
    return path.stem.replace("_", " ")


def cerg_version() -> str:
    cat = ROOT / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md"
    if cat.exists():
        m = re.search(r"\| \*\*Version\*\* \| ([^|]+) \|", cat.read_text(encoding="utf-8", errors="ignore"))
        if m:
            return m.group(1).strip()
    return "unknown"


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return not any(part in EXCLUDED_DIRS for part in rel.parts)


def sort_key(path: Path):
    rel = path.relative_to(ROOT).as_posix()
    order = ["README.md", "START-HERE.md", "AGENTS.md", "governance", "standards", "procedures", "plans", "templates", "roles", "machine-readable", "examples"]
    first = rel.split("/", 1)[0]
    rank = order.index(rel) if rel in order else (order.index(first) if first in order else 99)
    return (rank, rel)


def main():
    old_summaries = {}
    if OUT.exists():
        try:
            old = json.loads(OUT.read_text(encoding="utf-8"))
            old_summaries = {d.get("id"): d.get("summary", "") for d in old.get("documents", [])}
        except Exception:
            old_summaries = {}

    line_cursor = 1
    docs = []
    for path in sorted([p for p in ROOT.rglob("*.md") if should_include(p)], key=sort_key):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        meta = metadata(text)
        doc_id = extract_id(path, text, meta)
        if not doc_id.startswith("CERG-"):
            meta = {}
        doc_type, pillar, prefix = type_and_pillar(path, doc_id)
        chars = len(text)
        tokens = round(chars / 3.5)
        line_start = line_cursor
        line_end = line_cursor + len(lines)
        line_cursor = line_end + 2  # virtual boundary line
        summary = old_summaries.get(doc_id) or FALLBACK_SUMMARY.get(doc_id) or f"CERG {prefix} document: {title_for(path, doc_id, meta)}"
        docs.append({
            "id": doc_id,
            "prefix": prefix,
            "title": title_for(path, doc_id, meta),
            "type": doc_type,
            "pillar": pillar,
            "status": meta.get("Status"),
            "version": meta.get("Version"),
            "classification": meta.get("Classification"),
            "owner": meta.get("Owner") or meta.get("Document Owner"),
            "path": rel,
            "lines": [line_start, line_end],
            "lines_count": len(lines),
            "chars": chars,
            "tokens": tokens,
            "summary": summary,
        })

    by_type = {}
    for d in docs:
        by_type[d["type"]] = by_type.get(d["type"], 0) + 1
    by_prefix = {p: {"type": info["type"], "pillar": info["pillar"], "count": sum(1 for d in docs if d["prefix"] == p)} for p, info in PREFIXES.items()}

    index = {
        "cerg_version": cerg_version(),
        "generated": date.today().isoformat(),
        "source": "local markdown corpus",
        "total_documents": len(docs),
        "total_tokens_estimate": sum(d["tokens"] for d in docs),
        "by_type": by_type,
        "by_prefix": by_prefix,
        "prefixes": PREFIXES,
        "documents": docs,
    }
    OUT.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {OUT} with {len(docs)} documents")


if __name__ == "__main__":
    main()
