#!/usr/bin/env python3
"""
Regenerate machine-readable/cerg-llm-index.json from the latest llms-full.txt
and the existing cerg-manifest.yaml.

Run from repo root:  python3 tools/regenerate-llm-index.py
Or:                 cd /home/lupus/CERG && python3 tools/regenerate-llm-index.py
"""

import json, re, os, sys

CERG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLMS_URL = "https://cerg.nexus/llms-full.txt"
LLMS_LOCAL = "/tmp/llms-full.txt"

# ── Download or use local llms-full.txt ──
if not os.path.exists(LLMS_LOCAL):
    print(f"Downloading {LLMS_URL}...")
    import urllib.request
    urllib.request.urlretrieve(LLMS_URL, LLMS_LOCAL)
    print(f"  Saved to {LLMS_LOCAL}")

with open(LLMS_LOCAL) as f:
    content = f.read()
    full_lines = content.split("\n")

# ── Parse document boundaries ──
boundaries = []
for i, line in enumerate(full_lines, 1):
    m = re.match(r'<!-- ===== (.+?) ===== -->', line)
    if m:
        boundaries.append({"start": i, "path": m.group(1)})

total_lines = len(full_lines)
for idx, b in enumerate(boundaries):
    b["end"] = boundaries[idx+1]["start"] - 1 if idx+1 < len(boundaries) else total_lines
    lines_slice = full_lines[b["start"]-1:b["end"]]
    b["chars"] = sum(len(l) + 1 for l in lines_slice)

# ── Extract CERG doc IDs from file paths ──
def extract_doc_id(filepath):
    patterns = [
        r'(CERG-[A-Z]+-[A-Z]{2,8}-[A-Z]{2,8}-\d{3})',  # 5-part
        r'(CERG-[A-Z]+-[A-Z]{2,8}-\d{3})',              # 4-part
        r'(CERG-[A-Z]+-\d{3})',                          # 3-part
    ]
    for p in patterns:
        m = re.search(p, filepath)
        if m: return m.group(1)
    basename = os.path.basename(filepath).replace(".md", "").replace(".txt", "")
    return basename

def unique_id(filepath):
    doc_id = extract_doc_id(filepath)
    dirname = os.path.dirname(filepath) or "."
    if doc_id == "README" and dirname != ".":
        return f"README-{dirname.replace('/', '-')}"
    return doc_id

def clean_title(filepath):
    basename = os.path.basename(filepath).replace(".md", "")
    cleaned = re.sub(r'^CERG-[A-Z]+-[A-Z0-9]+(?:-[A-Z]+)?-?\d{3}_?', '', basename)
    cleaned = cleaned.replace("_", " ").strip()
    if not cleaned:
        cleaned = re.sub(r'^CERG-[A-Z]+-', '', basename).replace("_", " ").strip()
    if not cleaned:
        cleaned = basename.replace("_", " ").strip()
    return cleaned

# ── Get existing index for summaries we want to preserve ──
OLD_INDEX = os.path.join(CERG, "machine-readable", "cerg-llm-index.json")
old_summaries = {}
if os.path.exists(OLD_INDEX):
    with open(OLD_INDEX) as f:
        old_data = json.load(f)
    for d in old_data.get("documents", []):
        old_summaries[d["id"]] = d.get("summary", "")

# ── Classify documents ──
def classify(dirname, filename, doc_id, uid):
    if dirname == "governance":
        if "POL" in doc_id: return "policy", "governance", "POL"
        if "JD" in doc_id: return "job-description", "workforce", "JD"
        if "JF" in doc_id: return "job-family", "workforce", "JF"
        if doc_id in ("CERG-GOV-RMF-001", "CERG-GOV-TAX-001", "CERGGOV-CMX-001"): return "governance-instrument", "risk", "GOV"
        if doc_id in ("CERG-GOV-CB-001", "CERG-GOV-TRC-001", "CERG-GOV-CEF-001"): return "governance-instrument", "engineering", "GOV"
        return "governance-instrument", "governance", "GOV"
    if dirname == "standards": return "standard", "engineering", "STD"
    if dirname == "procedures": return "procedure", "risk", "PRC"
    if dirname == "plans": return "plan", "governance", "PLN"
    if dirname == "templates": return "template", "governance", "TMPL"
    if dirname.startswith("roles"):
        return ("job-description" if "JD" in doc_id else "job-family"), "workforce", ("JF" if "JF" in doc_id else "JD")
    return ("readme" if "README" in uid else "meta"), "cross-cutting", "META"

# ── Build document list ──
seen = set()
documents = []
FALLBACK_SUMMARY = {
    "README": "CERG repository root — project overview, adoption paths, architecture, reader guides.",
    "START-HERE": "First 48 hours adoption guide — Lite, Standard, and Regulated paths.",
    "CONTRIBUTING": "Contributing guide — validation requirements, conventions, PR workflow.",
    "ROADMAP": "CERG development roadmap and planned improvement workstreams.",
    "SECURITY": "Security policy and vulnerability disclosure.",
    "CODE_OF_CONDUCT": "Community code of conduct for CERG contributors.",
    "AGENTS": "Guide for AI agents working on CERG — conventions, pitfalls, tools, git workflow.",
    "README-machine-readable": "Machine-readable artifact governance — derived YAML/JSON artifacts.",
    "README-flows": "Cross-Pillar Operational Flows overview.",
    "README-roles": "Workforce architecture overview — 5 job families.",
    "README-examples": "Example adoption profiles.",
    "README-examples-regulated-utility-profile": "Example profile for a regulated utility.",
}

for b in boundaries:
    path = b["path"]
    dirname = os.path.dirname(path) or "."
    filename = os.path.basename(path)
    doc_id = extract_doc_id(path)
    uid = unique_id(path)
    
    if uid in seen: continue
    seen.add(uid)
    
    doc_type, pillar, prefix = classify(dirname, filename, doc_id, uid)
    title = clean_title(path)
    token_est = round(b["chars"] / 3.5)
    
    # Use existing summary if available, fall back to one-shot description
    if uid in old_summaries and old_summaries[uid]:
        summary = old_summaries[uid]
    else:
        summary = FALLBACK_SUMMARY.get(uid, f"CERG {prefix} document: {title}")
    
    documents.append({
        "id": uid if uid != doc_id else doc_id,
        "prefix": prefix,
        "title": title,
        "type": doc_type,
        "pillar": pillar,
        "path": path,
        "lines": [b["start"], b["end"]],
        "lines_count": b["end"] - b["start"] + 1,
        "chars": b["chars"],
        "tokens": token_est,
        "summary": summary
    })

# Add AGENTS.md if not in corpus
if "AGENTS" not in seen:
    agents_path = os.path.join(CERG, "AGENTS.md")
    if os.path.exists(agents_path):
        agents_chars = os.path.getsize(agents_path)
        documents.append({
            "id": "AGENTS", "prefix": "META", "title": "AI Agent Guide",
            "type": "readme", "pillar": "cross-cutting", "path": "AGENTS.md",
            "lines": [0, 0], "lines_count": 0, "chars": agents_chars,
            "tokens": round(agents_chars / 3.5),
            "summary": "Guide for AI agents working on CERG — conventions, pitfalls, tools, git workflow."
        })

# ── Prefix registry ──
prefixes = {
    "POL": {"type": "Policy", "pillar": "governance"},
    "GOV": {"type": "Governance Instrument", "pillar": "governance"},
    "STD": {"type": "Standard", "pillar": "engineering"},
    "PRC": {"type": "Procedure", "pillar": "risk"},
    "PLN": {"type": "Plan / Package", "pillar": "governance"},
    "TMPL": {"type": "Template", "pillar": "governance"},
    "JF": {"type": "Job Family", "pillar": "workforce"},
    "JD": {"type": "Job Description", "pillar": "workforce"},
    "META": {"type": "Repository Metadata", "pillar": "cross-cutting"},
}

by_prefix = {p: {"type": pi["type"], "pillar": pi["pillar"], "count": sum(1 for d in documents if d["prefix"] == p)} for p, pi in prefixes.items()}
type_counts = {}
for d in documents:
    type_counts[d["type"]] = type_counts.get(d["type"], 0) + 1

# ── Assemble and write ──
llm_index = {
    "cerg_version": "1.22",
    "generated": "2026-06-12",
    "total_documents": len(documents),
    "total_tokens_estimate": sum(d["tokens"] for d in documents),
    "by_type": type_counts,
    "by_prefix": by_prefix,
    "prefixes": prefixes,
    "documents": documents
}

output_path = os.path.join(CERG, "machine-readable", "cerg-llm-index.json")
with open(output_path, "w") as f:
    json.dump(llm_index, f, indent=2)

print(f"✅ Regenerated: {len(documents)} documents ({llm_index['total_tokens_estimate']:,} total tokens)")
print(f"   Written to {output_path}")