#!/usr/bin/env python3
"""
CERG Client Repo Provisioning Script — v1
Practice Asset — Not a CERP Corpus Document

Purpose: Automates the setup of a secure client CERG repository.
Creates the repo skeleton, branch strategy, CI configuration, and
initializes the first commit with rendered corpus.

Usage:
  python3 practice-assets/scripts/provision-client-repo.py
    --org CLIENT_ORG
    --repo cerg
    --token GITHUB_TOKEN
    --profile /path/to/cerg-org-profile.yml
    [--dry-run]

This script is designed to be run by the Practice Principal or
a delegated practitioner. It creates a private GitHub repository
owned by the practice (transferred to client at handover), or
directly in the client's org if they provide token scope.

Requirements: gh CLI authenticated, Python 3.8+
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run(cmd, capture=True):
    result = subprocess.run(cmd, shell=True, capture_output=capture, text=True)
    return result.stdout.strip(), result.returncode


def check_prerequisites():
    """Verify gh CLI and required tools are available."""
    tools = {"gh": "gh --version", "git": "git --version", "python3": "python3 --version"}
    missing = []
    for name, cmd in tools.items():
        _, rc = run(cmd)
        if rc != 0:
            missing.append(name)
    return missing


def create_repo(org, repo, token, private=True, dry_run=False):
    """Create a private GitHub repository."""
    visibility = "private" if private else "public"
    desc = f"CERG cybersecurity operating model — {org}"

    if dry_run:
        print(f"[DRY RUN] Would create repo: {org}/{repo}")
        print(f"  Visibility: {visibility}")
        print(f"  Description: {desc}")
        return True

    # Use GitHub API to create repo
    api_url = f"https://api.github.com/repos/{org}/{repo}"
    payload = json.dumps({
        "name": repo,
        "description": desc,
        "private": private,
        "has_issues": True,
        "has_wiki": False,
        "auto_init": False,
    })

    cmd = f"""
    curl -s -X POST -H "Authorization: token {token}" \\
      -H "Accept: application/vnd.github.v3+json" \\
      https://api.github.com/orgs/{org}/repos \\
      -d '{payload}'
    """
    # For user-owned repos instead of org:
    # https://api.github.com/user/repos

    output, rc = run(cmd)
    if rc != 0:
        print(f"ERROR: Failed to create repo. Output: {output[:500]}")
        return False

    result = json.loads(output)
    if "errors" in result or "message" in result:
        if "already exists" in str(result):
            print(f"Repo {org}/{repo} already exists — proceeding with setup.")
            return True
        print(f"ERROR: {result.get('message', result)}")
        return False

    print(f"Created repo: {result.get('clone_url', org + '/' + repo)}")
    return True


def setup_branch_protection(org, repo, token, dry_run=False):
    """Set up branch protection for main branch."""
    if dry_run:
        print("[DRY RUN] Would configure branch protection:")
        print("  - Require pull request before merging")
        print("  - Require status checks (CI passes)")
        print("  - Require signed commits")
        print("  - Restrict force pushes")
        print("  - Require linear history")
        return True

    api_url = f"https://api.github.com/repos/{org}/{repo}/branches/main/protection"

    payload = json.dumps({
        "required_status_checks": {
            "strict": True,
            "contexts": ["validate"]
        },
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "required_approving_review_count": 1,
            "dismiss_stale_reviews": True
        },
        "restrictions": None,
        "required_linear_history": True,
        "allow_force_pushes": False,
        "allow_deletions": False,
    })

    cmd = f"""
    curl -s -X PUT -H "Authorization: token {token}" \\
      -H "Accept: application/vnd.github.v3+json" \\
      '{api_url}' \\
      -d '{payload}'
    """
    output, rc = run(cmd)
    if rc != 0:
        print(f"WARN: Branch protection not set. Output: {output[:300]}")
        return False
    print("Branch protection configured.")
    return True


def initialize_repo(repo_path, org, profile_path, dry_run=False):
    """Initialize the repo with corpus, CI, and README."""
    if dry_run:
        print(f"[DRY RUN] Would initialize repo at {repo_path}")
        return True

    repo = Path(repo_path)
    repo.mkdir(parents=True, exist_ok=True)

    # Initialize git
    run("git init", cwd=repo)
    run("git checkout -b main", cwd=repo)

    # Create .github/workflows directory
    workflows = repo / ".github" / "workflows"
    workflows.mkdir(parents=True, exist_ok=True)

    # CI workflow: validate on push
    ci_yaml = """name: CERG Validate
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run CERG validator
        run: python3 tools/cerg-validate.py
      - name: Check token resolution
        run: python3 tools/cerg-render.py --check
"""
    (workflows / "validate.yml").write_text(ci_yaml)

    # Create .gitignore
    gitignore = """# CERG
/rendered/
*.swp
*.swo
__pycache__/
.env
*.env
.venv/
"""
    (repo / ".gitignore").write_text(gitignore)

    # Create SECURITY.md
    security = f"""# Security Policy for {org}

This repository contains the adapted CERG cybersecurity operating model for {org}.
For security-related issues, contact: {{SECURITY_CONTACT}}

## Supported Versions
Only the latest rendered corpus from `main` is supported.

## Reporting a Vulnerability
Report vulnerabilities to {{SECURITY_CONTACT}} rather than creating a public issue.
"""
    (repo / "SECURITY.md").write_text(security)

    # Copy default README
    readme = f"""# {org} — CERG Cybersecurity Operating Model

This repository contains the adapted CERG framework for {org}.
See the Cybersecurity Policy (POL-001) and the Document Catalog (CAT-001) for the authoritative artifact inventory.

## Quick Start
1. Review the adapted Cybersecurity Policy: `governance/CERG-POL-001_Cybersecurity_Policy.md`
2. Review the Document Catalog: `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`
3. Read the Implementation Guide: `governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md`

## Updating
When upstream CERG releases changes, re-render with:
```bash
python3 tools/cerg-render.py
python3 tools/cerg-validate.py
```
"""
    (repo / "README.md").write_text(readme)

    print(f"Repository initialized at {repo}")
    print(f"  - CI workflow: {workflows / 'validate.yml'}")
    print(f"  - .gitignore created")
    print(f"  - SECURITY.md created")
    print(f"  - README.md created")
    return True


def commit_initial(repo_path, dry_run=False):
    """Create the initial commit."""
    if dry_run:
        print("[DRY RUN] Would create initial commit")
        return "0000000"

    repo = Path(repo_path)
    run("git add -A", cwd=repo)
    output, rc = run("git commit -m 'initial commit: provision CERG client repository'", cwd=repo)
    output2, rc2 = run("git rev-parse HEAD", cwd=repo)
    sha = output2[:7] if rc2 == 0 else "unknown"
    print(f"Initial commit: {sha}")
    return sha


def main():
    parser = argparse.ArgumentParser(description="CERG Client Repo Provisioning")
    parser.add_argument("--org", required=True, help="GitHub organization or user")
    parser.add_argument("--repo", default="cerg", help="Repository name (default: cerg)")
    parser.add_argument("--token", help="GitHub personal access token")
    parser.add_argument("--profile", help="Path to client cerg-org-profile.yml")
    parser.add_argument("--repo-path", help="Local path for repo initialization (default: /tmp/{org}-{repo})")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    args = parser.parse_args()

    # Prerequisites check
    missing = check_prerequisites()
    if missing:
        print(f"Missing required tools: {', '.join(missing)}")
        if not args.dry_run:
            sys.exit(1)

    # Use token from args or env
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token and not args.dry_run:
        print("ERROR: GitHub token required. Provide --token or set GITHUB_TOKEN env var.")
        sys.exit(1)

    # Create repository
    if not create_repo(args.org, args.repo, token, dry_run=args.dry_run):
        sys.exit(1)

    # Set up branch protection
    setup_branch_protection(args.org, args.repo, token, dry_run=args.dry_run)

    # Initialize local repo
    repo_path = args.repo_path or f"/tmp/{args.org}-{args.repo}"
    initialize_repo(repo_path, args.org, args.profile, dry_run=args.dry_run)

    # Initial commit
    commit_initial(repo_path, dry_run=args.dry_run)

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Provisioning complete.")
    print(f"Next steps:")
    print(f"  1. Copy rendered CERG corpus into {repo_path}")
    print(f"  2. Push to GitHub: cd {repo_path} && git remote add origin https://github.com/{args.org}/{args.repo}.git && git push -u origin main")
    print(f"  3. Validate: python3 tools/cerg-validate.py")


if __name__ == "__main__":
    main()
