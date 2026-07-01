#!/usr/bin/env python3
"""
CERG Upstream CI Check — v1
Practice Asset — Not a CERG Corpus Document

Purpose: Detect when upstream CERG (m0dernz/CERG) has published changes
that may affect active client engagements. Compares the client's rendered
corpus against the upstream HEAD and flags structural differences in
document inventory, token catalog, and validator rules.

Usage:
  python3 practice-assets/scripts/check-upstream-drift.py
    --upstream m0dernz/CERG
    --client-repo /path/to/client/fork
    --out drift-report.md

  python3 practice-assets/scripts/check-upstream-drift.py
    --ci            # CI mode: exit 1 if drift detected
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path


def run(cmd, cwd=None, capture=True):
    """Run a shell command and return stdout + return code."""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd, capture_output=capture, text=True
    )
    return result.stdout.strip(), result.returncode


def fetch_upstream_llm_index(upstream_repo):
    """Fetch the latest cerg-llm-index.json from upstream GitHub."""
    url = f"https://raw.githubusercontent.com/{upstream_repo}/main/machine-readable/cerg-llm-index.json"
    index_path = Path(tempfile.gettempdir()) / "upstream-cerg-llm-index.json"
    run(f"curl -sL '{url}' -o {index_path}")
    if not index_path.exists():
        print(f"ERROR: Failed to fetch upstream index from {url}")
        sys.exit(1)
    return index_path


def compare_document_inventory(upstream_index_path, client_repo):
    """Compare upstream document count and IDs against client's rendered corpus."""
    with open(upstream_index_path) as f:
        upstream = json.load(f)

    client_llm_index = Path(client_repo) / "machine-readable" / "cerg-llm-index.json"
    if not client_llm_index.exists():
        print(f"WARN: No cerg-llm-index.json found in client repo at {client_llm_index}")
        return {"status": "unknown", "detail": "Client LLM index not found"}

    with open(client_llm_index) as f:
        client = json.load(f)

    upstream_docs = {d["id"] for d in upstream.get("documents", [])}
    client_docs = {d["id"] for d in client.get("documents", [])}

    added = upstream_docs - client_docs
    removed = client_docs - upstream_docs

    result = {
        "upstream_count": upstream["total_documents"],
        "client_count": client["total_documents"],
        "added_documents": sorted(list(added)),
        "removed_documents": sorted(list(removed)),
        "status": "change" if added or removed else "current",
    }
    return result


def compare_validator(client_repo):
    """Run the CERG validator against the client repo and report pass/fail."""
    validator = Path(client_repo) / "tools" / "cerg-validate.py"
    if not validator.exists():
        return {"status": "unknown", "detail": "Validator not found in client repo"}

    output, rc = run(f"python3 {validator}", cwd=client_repo)
    return {"status": "pass" if rc == 0 else "fail", "output": output[:500]}


def check_upstream_commit(upstream_repo):
    """Check the latest upstream commit hash and message."""
    url = f"https://api.github.com/repos/{upstream_repo}/commits/main"
    index_path = Path(tempfile.gettempdir()) / "upstream-latest-commit.json"
    run(f"curl -sL '{url}' -o {index_path}")
    if not index_path.exists():
        return {"sha": "unknown", "message": "Could not fetch"}

    with open(index_path) as f:
        data = json.load(f)

    return {
        "sha": data.get("sha", "unknown")[:12],
        "message": data.get("commit", {}).get("message", "unknown").split("\n")[0],
        "date": data.get("commit", {}).get("committer", {}).get("date", "unknown"),
    }


def generate_report(inventory, validator_status, upstream_commit, client_repo, ci_mode):
    """Generate drift report as markdown."""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    report = f"# CERG Upstream Drift Report\n\n"
    report += f"**Generated:** {now}\n"
    report += f"**Client Repo:** {client_repo}\n"
    report += f"**Upstream:** {upstream_commit['sha']} — {upstream_commit['message']}\n\n"

    # Inventory comparison
    report += f"## Document Inventory\n\n"
    report += f"| Metric | Value |\n|---|---|\n"
    report += f"| Upstream Document Count | {inventory['upstream_count']} |\n"
    report += f"| Client Document Count | {inventory['client_count']} |\n"
    report += f"| Status | {inventory['status']} |\n\n"

    if inventory["added_documents"]:
        report += f"**Documents added upstream (not in client corpus):**\n\n"
        for doc_id in inventory["added_documents"]:
            report += f"- {doc_id}\n"
        report += "\n"

    if inventory["removed_documents"]:
        report += f"**Documents removed upstream (present in client corpus):**\n\n"
        for doc_id in inventory["removed_documents"]:
            report += f"- {doc_id}\n"
        report += "\n"

    # Validator status
    report += f"## Client Validator\n\n"
    report += f"| Metric | Value |\n|---|---|\n"
    report += f"| Status | {validator_status['status']} |\n"
    if validator_status.get("detail"):
        report += f"| Detail | {validator_status['detail']} |\n"
    if validator_status.get("output"):
        report += f"| Output | {validator_status['output'][:300]} |\n"
    report += "\n"

    # Recommendation
    report += f"## Recommendation\n\n"
    if inventory["status"] == "change":
        report += (
            "**Action required.** The upstream CERG corpus has changed since the "
            "client's last render. Review the document differences above and "
            "determine whether a re-render and evidence update is needed before "
            "the next audit or assessment cycle.\n\n"
            "Steps:\n"
            "1. Pull upstream changes into your fork.\n"
            "2. Run `python3 tools/regenerate-machine-readable.py`.\n"
            "3. Re-render client corpus: `python3 tools/cerg-render.py`.\n"
            "4. Review rendered output for sector and regulatory accuracy.\n"
            "5. Update evidence library where control language changed.\n"
        )
    else:
        report += "No action required. Client corpus is current with upstream.\n"

    return report


def main():
    parser = argparse.ArgumentParser(description="CERG Upstream Drift Check")
    parser.add_argument(
        "--upstream",
        default="m0dernz/CERG",
        help="Upstream CERG repository (default: m0dernz/CERG)",
    )
    parser.add_argument(
        "--client-repo",
        required=True,
        help="Path to client's CERG fork repository",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Path to write drift report (default: stdout)",
    )
    parser.add_argument(
        "--ci",
        action="store_true",
        help="CI mode: exit 1 if drift detected",
    )
    args = parser.parse_args()

    print(f"Checking upstream: {args.upstream}")
    print(f"Client repo: {args.client_repo}")

    upstream_commit = check_upstream_commit(args.upstream)
    upstream_index = fetch_upstream_llm_index(args.upstream)
    inventory = compare_document_inventory(upstream_index, args.client_repo)
    validator_status = compare_validator(args.client_repo)

    report = generate_report(
        inventory, validator_status, upstream_commit, args.client_repo, args.ci
    )

    if args.out:
        with open(args.out, "w") as f:
            f.write(report)
        print(f"Report written to {args.out}")
    else:
        print(report)

    if args.ci and inventory["status"] == "change":
        print("DRIFT DETECTED: exiting 1")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
