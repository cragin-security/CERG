#!/usr/bin/env python3
"""
CERG Render-and-Diff Pipeline — v1
Practice Asset — Not a CERG Corpus Document

Purpose: Detects changes between upstream CERG and a client's rendered corpus.
Highlights structural differences in document inventory, token values, and
control references.

Usage:
  python3 practice-assets/scripts/render-and-diff.py
    --client-repo /path/to/client/cerg-fork
    --profile /path/to/client/cerg-org-profile.yml
    --upstream m0dernz/CERG
    --out /path/to/diff-report.md

  python3 practice-assets/scripts/render-and-diff.py --ci
    # CI mode: exit 1 if the client corpus is stale
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path


def run(cmd, cwd=None, capture=True):
    result = subprocess.run(
        cmd, shell=True, cwd=cwd, capture_output=capture, text=True
    )
    return result.stdout.strip(), result.returncode


def fetch_file(url, dest_path):
    run(f"curl -sL '{url}' -o {dest_path}")
    return dest_path.exists()


def get_file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


def get_token_values(profile_path):
    """Extract {{TOKEN}} values from org profile."""
    import yaml
    with open(profile_path) as f:
        data = yaml.safe_load(f)
    tokens = {}
    if data:
        for category, values in data.items():
            if isinstance(values, dict):
                for key, val in values.items():
                    token = "{{" + key.upper() + "}}"
                    tokens[token] = str(val) if val else None
    return tokens


def compare_llm_indexes(client_repo):
    """Compare upstream LLM index to client's index."""
    upstream_url = "https://raw.githubusercontent.com/m0dernz/CERG/main/machine-readable/cerg-llm-index.json"
    upstream_path = Path(tempfile.gettempdir()) / "upstream-llm-index.json"
    client_path = Path(client_repo) / "machine-readable" / "cerg-llm-index.json"

    if not fetch_file(upstream_url, upstream_path):
        return {"error": "Could not fetch upstream LLM index"}
    if not client_path.exists():
        return {"error": "Client LLM index not found"}

    with open(upstream_path) as f:
        upstream = json.load(f)
    with open(client_path) as f:
        client = json.load(f)

    up_docs = {d["id"]: d for d in upstream.get("documents", [])}
    cl_docs = {d["id"]: d for d in client.get("documents", [])}

    added = set(up_docs.keys()) - set(cl_docs.keys())
    removed = set(cl_docs.keys()) - set(up_docs.keys())
    common = set(up_docs.keys()) & set(cl_docs.keys())

    changed = []
    for doc_id in sorted(common):
        up_ver = up_docs[doc_id].get("version", "")
        cl_ver = cl_docs[doc_id].get("version", "")
        if up_ver != cl_ver:
            changed.append({"id": doc_id, "upstream_version": up_ver, "client_version": cl_ver})

    return {
        "total_upstream": upstream["total_documents"],
        "total_client": client["total_documents"],
        "added": sorted(list(added)),
        "removed": sorted(list(removed)),
        "version_changed": sorted(changed, key=lambda x: x["id"]),
        "hash_upstream": get_file_hash(upstream_path),
        "hash_client": get_file_hash(client_path),
    }


def compare_manifest(client_repo):
    """Compare upstream manifest to client's manifest."""
    upstream_url = "https://raw.githubusercontent.com/m0dernz/CERG/main/machine-readable/cerg-manifest.yaml"
    upstream_path = Path(tempfile.gettempdir()) / "upstream-manifest.yaml"
    client_path = Path(client_repo) / "machine-readable" / "cerg-manifest.yaml"

    if not fetch_file(upstream_url, upstream_path):
        return {"error": "Could not fetch upstream manifest"}

    up_hash = get_file_hash(upstream_path)
    cl_hash = get_file_hash(client_path) if client_path.exists() else "n/a"

    return {
        "upstream_hash": up_hash,
        "client_hash": cl_hash,
        "match": up_hash == cl_hash,
    }


def check_token_drift(profile_path):
    """Verify all tokens in the profile render without bare {{TOKEN}} strings."""
    tokens = get_token_values(profile_path)
    unresolved = [t for t, v in tokens.items() if v is None or v == ""]
    return {"total": len(tokens), "unresolved": unresolved}


def render_and_check(client_repo, profile_path):
    """Run the CERG renderer and check exit code."""
    renderer = Path(client_repo) / "tools" / "cerg-render.py"
    if not renderer.exists():
        return {"status": "not_available"}

    output, rc = run(f"python3 {renderer} --check", cwd=client_repo)
    return {
        "status": "pass" if rc == 0 else "fail",
        "output": output[:500],
    }


def generate_report(results, ci_mode):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = []
    lines.append(f"# CERG Render-and-Diff Report")
    lines.append(f"**Generated:** {now}\n")

    # LLM index comparison
    llm = results.get("llm", {})
    lines.append("## Document Inventory")
    lines.append(f"| Metric | Upstream | Client |")
    lines.append(f"|---|---|---|")
    lines.append(f"| Document Count | {llm.get('total_upstream', '?')} | {llm.get('total_client', '?')} |")
    lines.append(f"| Index Hash | {llm.get('hash_upstream', '?')[:8]} | {llm.get('hash_client', '?')[:8]} |")

    if llm.get("added"):
        lines.append(f"\n**Documents added upstream:** {len(llm['added'])}")
        for d in llm["added"][:10]:
            lines.append(f"- {d}")

    if llm.get("removed"):
        lines.append(f"\n**Documents removed upstream:** {len(llm['removed'])}")
        for d in llm["removed"][:10]:
            lines.append(f"- {d}")

    if llm.get("version_changed"):
        lines.append(f"\n**Documents with version changes:** {len(llm['version_changed'])}")
        for c in llm["version_changed"][:10]:
            lines.append(f"- {c['id']}: upstream v{c['upstream_version']} → client v{c['client_version']}")

    # Manifest comparison
    man = results.get("manifest", {})
    lines.append(f"\n## Manifest Status")
    lines.append(f"| Metric | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| Upstream Hash | {man.get('upstream_hash', '?')[:8]} |")
    lines.append(f"| Client Hash | {man.get('client_hash', '?')[:8]} |")
    lines.append(f"| Match | {'✅' if man.get('match') else '❌'} |")

    # Token check
    token = results.get("token", {})
    lines.append(f"\n## Token Profile Status")
    lines.append(f"| Metric | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| Total Tokens | {token.get('total', 0)} |")
    lines.append(f"| Unresolved | {len(token.get('unresolved', []))} |")
    if token.get("unresolved"):
        for t in token["unresolved"]:
            lines.append(f"- ⚠ {t}")

    # Renderer
    render = results.get("render", {})
    lines.append(f"\n## Render Check")
    if render.get("status") == "not_available":
        lines.append("Renderer not available in client repo (expected for forks without tools/).")
    else:
        lines.append(f"| Status | {'✅ Pass' if render.get('status') == 'pass' else '❌ Fail'} |")

    lines.append(f"\n## Summary")
    change_count = len(llm.get("added", [])) + len(llm.get("removed", [])) + len(llm.get("version_changed", []))
    if change_count > 0 or not man.get("match"):
        lines.append(f"**⚠ {change_count} structural differences found.**")
        action = "Client corpus needs re-render before next audit or assessment cycle."
        if ci_mode:
            action += " (CI mode: exiting 1)"
        lines.append(action)
    else:
        lines.append("✅ Client corpus is current with upstream.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="CERG Render-and-Diff Pipeline")
    parser.add_argument("--client-repo", required=True, help="Path to client's CERG fork")
    parser.add_argument("--profile", default=None, help="Path to client cerg-org-profile.yml")
    parser.add_argument("--out", default=None, help="Write report to file (default: stdout)")
    parser.add_argument("--ci", action="store_true", help="Exit 1 on drift")
    args = parser.parse_args()

    results = {}

    results["llm"] = compare_llm_indexes(args.client_repo)
    results["manifest"] = compare_manifest(args.client_repo)
    if args.profile:
        results["token"] = check_token_drift(args.profile)
    results["render"] = render_and_check(args.client_repo, args.profile or args.client_repo)

    report = generate_report(results, args.ci)

    if args.out:
        with open(args.out, "w") as f:
            f.write(report)
        print(f"Report written to {args.out}")
    else:
        print(report)

    has_diff = (
        len(results["llm"].get("added", [])) > 0
        or len(results["llm"].get("removed", [])) > 0
        or len(results["llm"].get("version_changed", [])) > 0
        or not results["manifest"].get("match", True)
    )

    if args.ci and has_diff:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
