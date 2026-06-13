# CERG — Guide for AI Agents

This file is loaded automatically by AI agents (Claude Code, Copilot, Codex CLI, Cursor, etc.) to understand the CERG cybersecurity operating model repository and work effectively with it.

---

## Project Overview

CERG is an open‑source cybersecurity operating model — not a control framework or compliance checklist. It gives security teams the policies, standards, procedures, workforce architecture, and evidence model to run a real program. Three pillars: Engineering, Risk, and Governance.

## Directory Layout

```
governance/         Policies, governance instruments, competency models, risk framework
standards/          Technical security standards (15 docs)
procedures/         Operational procedures (12 docs)
plans/              Regulatory operational packages (7 docs)
templates/          Fill‑in artifacts for routine work (10 docs)
roles/              Workforce architecture:
  JF-001.md         Job Families Overview
  JF-002.md         NICE Workforce Framework Crosswalk
  jf-exec/          Executive leadership JDs
  jf-seceng/        Security engineering JDs
  jf-riskops/       Risk operations JDs
  jf-govcomp/       Governance & compliance JDs
  jf-adjunct/       Adjunct function JDs
machine-readable/   YAML + JSON artifacts derived from markdown source
tools/              Validation and population scripts
examples/           Adoption profiles
```

## Document Anatomy

Every CERG document follows STY‑001 conventions:

### Metadata Table (top of file)

11‑field table in STY‑001 §4 format:

```
| | |
|---|---|
| **Document ID** | CERG-XXX-YYY-NNN |
| **Version** | X.X |
| **Status** | Approved |
| **Classification** | Public / Internal / Confidential |
| **Owner** | Role Name |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Quarterly / Annual |
| **Frameworks** | NIST CSF 2.0 · NIST 800‑53r5 · … |
| **Regulations** | NERC‑CIP · CMMC L2 · SOX ITGC · … |
| **Environments** | All in‑scope environments |
```

### Section Numbering

- Top‑level: `## N. Section Title`
- Subsection: `### N.M Subsection Title`
- Must be sequential — no gaps. Section renumbering works from HIGHEST number to LOWEST to prevent cascading replacements.

### Links

- Resolved relative to source file's directory
- Same‑dir: `FILENAME.md`
- Parent dir: `../governance/FILENAME.md`
- Grandparent: `../../governance/FILENAME.md`
- `roles/` → `governance/`: `../governance/FILENAME.md`
- `roles/jf-seceng/` → `governance/`: `../../governance/FILENAME.md`

### Cross‑References

Format: `[CERG‑XXX‑YYY‑NNN](FILENAME.md)` — always include the filename link, not just the ID.

### Document Control Section (last section before appendices)

Contains Revision History (a table), Review Triggers, Related Documents.

## Machine‑Readable Index

`machine-readable/cerg-llm-index.json` contains:

- Per‑document metadata (id, title, type, pillar, status, version, owner, path, line range in llms‑full.txt, token estimate, summary)
- Prefix registry (POL, STD, PRC, GOV, PLN, TMPL, JF, JD meanings)
- Pillar breakdowns
- Document counts

**Load this first** — it gives you the complete map of the framework in ~200 lines.

## Validation

### CI Gate (must pass before committing)

```bash
python3 tools/cerg-validate.py
```

This is the authoritative CI check — requires 0 errors. Common error classes:
- `FILE_NOT_IN_CATALOG` — document not registered in CAT‑001 §5
- `ID_NOT_IN_CATALOG` — cross‑reference to an unregistered ID
- `STATUS_MISMATCH` — file status ≠ catalog status
- `LINK_MISSING` — markdown link target doesn't exist on disk
- `DRAFT_VERSION` — status says Approved but version contains "Draft"
- `RESTRICTED_CLASSIFICATION` — Public doc references Internal/Confidential doc

### Integrity Checker (supplementary)

```bash
python3 tools/cerg-integrity-check.py
```

Broader scan — finds metadata issues, catalog drift, orphan files. May have pre‑existing false positives (~1,250 `unknown_id_reference` from 4‑part IDs, 3 pre‑existing `missing_document_id`).

### Validator Config

The `cerg-validate.py` `DOC_ID_PATTERN` in the regex may need extension for 4‑part IDs like `CERG-GOV-JD-SECENG-001` (hyphenated subdomains). Current pattern: `[A-Z]{2,6}` — may need `[A-Z]{2,6}(?:-[A-Z]{1,6})?`.

## Git Workflow for Agents

### Branching

- For cross‑cutting changes (renames, restructures, bulk link fixes): create a feature branch from `main`, work there, merge back.
- For single‑document edits: work directly on `main`.

### Committing

- **One commit per file.** Do not batch multiple files into one commit.
- Commit messages: very short, human‑readable. Examples:
  - `add missing Roles section, renumber`
  - `fix version inconsistency`
  - `update metadata table to STY-001 §4 format`
- For mechanical batch fixes (e.g., same regex applied to 20 files): single commit with a message like `bulk fix: unify Ownership field across per-role JDs`

### Pushing

Push immediately after each commit. Do not accumulate local commits.

```bash
git add FILENAME.md
git commit -m "short message"
git push origin main
```

### Git Config

If not already set:
```bash
git config user.name "m0dernz"
git config user.email "m0dernz@users.noreply.github.com"
```

## Editing Rules

### CRITICAL: Do NOT use the `patch` tool

The `patch` tool's fuzzy matching fails catastrophically on CERG docs because `---` (markdown section separator) appears 30‑80 times per file. The pattern `---` matches ALL separator lines regardless of surrounding context.

Also: `**Version**`, `**Status**`, `**Document ID**` appear in BOTH the front‑matter metadata table AND the Document Control section AND Revision History column headers. String replacement hits all occurrences.

**Safe approach:** Line‑targeted Python edits via `execute_code`:

```python
path = '/home/lupus/CERG/governance/CERG-GOV-XXXXX_Title.md'
with open(path) as f:
    lines = f.read().split('\n')

# Find the exact line and replace it
# e.g. lines[12] = '| **Status** | Approved |'
lines[target_line] = new_value

write_file(path, '\n'.join(lines))
```

### Verify After Every Edit

```bash
cd /home/lupus/CERG
git diff --stat        # Check changed-line count — should match expected
python3 tools/cerg-validate.py  # Must pass with 0 errors
```

### Section Renumbering

When inserting or deleting sections:

1. Renumber from HIGHEST to LOWEST to prevent cascading replacement
2. Update TOC entries (both numbers and anchor links)
3. Fix cross‑references in text that point to old numbers
4. Verify with: `grep -n '^## [0-9]' FILENAME.md`

### Document Status Rules

- All CERG‑owned documents pushed to `main` must have Status: `Approved` and Approved By: `CISO`
- Exception: IR documents (PLN‑IR‑001, PRC‑IR‑002) — these are "External Interface" status, owned by "Standing IR Team / Incident Commander", with an ADJACENT FUNCTION banner
- Status + Approved By must be consistent in both the metadata table AND the Document Control section AND the CAT‑001 catalog entry

### Stale Placeholders

Do NOT leave bare "Placeholder", "TBD", or "N/A —" in Approved documents. Use the pattern: "Preliminary default requiring organizational calibration" with a stated basis.

## Document Prefix Registry

| Prefix | Type | Pillar |
|--------|------|--------|
| POL | Policy | governance |
| GOV | Governance Instrument | governance |
| STD | Standard | engineering |
| PRC | Procedure | risk |
| PLN | Plan / Operational Package | governance |
| TMPL | Template | governance |
| JF | Job Family | workforce |
| JD | Job Description | workforce |

## Available Tools

### `tools/cerg-validate.py`

CI gate. Validates markdown links, catalog references, file inventory, metadata consistency. **0 errors required.** This is the authoritative validator.

### `tools/cerg-integrity-check.py`

Supplementary metadata and cross‑reference scanner. Broader than the validator but less precise (more false positives). Use for discovery, not gate‑keeping.

### `tools/cerg-render.py`

Renders CERG markdown with {{TOKEN}} placeholder substitution from an org profile YAML. For adopters customizing the framework for their organization.

### `tools/populate-nice-tks.py`

Populates §6 (NICE TKS Statement References) in per‑role JD files from NIST NICE Framework v2.2.0 dataset.

### `tools/populate-jd-sections.py`

Populates §9 (Competency Anchors from CMP‑001), §10 (Success Profiles), and §11.3 (Management Track from JA‑001) in per‑role JDs.

## Common Pitfalls

1. **Patch tool on `---` separator** — catastrophic false matches. Use line‑targeted Python.
2. **Anchor collision on `**Version**`, `**Status**`, `**Document ID**`** — appears 3+ times in every file (metadata table, DC section, Revision History). Target by line number, not string match.
3. **Section renumbering cascade** — `replace("## 2. ", "## 3. ")` then `replace("## 3. ", "## 4. ")` hits the REPLACED §2 too. Renumber HIGHEST→LOWEST.
4. **Link prefix depth** — files in `roles/jf-seceng/` need `../../` for root docs, `../` for `roles/` files, bare name for same‑subdir.
5. **Validator DOC_ID_PATTERN too narrow** — 4‑part IDs like `CERG-GOV-JD-SECENG-001` may fail silently. Extend `[A-Z]{2,6}` to `[A-Z]{2,6}(?:-[A-Z]{1,6})?` in the regex.
6. **Status in both places** — change metadata table Status AND DC section "Approved By" AND CAT‑001 catalog entry. All three must agree.
7. **Approval rule applies to ALL docs** — Status: Approved + Approved By: CISO, regardless of per‑role delegation in CAT‑001 §4.2.
8. **`read_file` dedup trap** — `hermes_tools.read_file()` returns a dedup stub if same file was already read. Always use `open(path).read()` in `execute_code`.
9. **CI runs committed code only** — `git stash` → test → `git stash pop` to distinguish local fixes from committed state.

## Quick‑Start Checklist (First Visit)

1. `cd /home/lupus/CERG` — set working directory
2. Read `machine-readable/cerg-llm-index.json` — understand the document landscape
3. Read `README.md` — understand CERG's purpose and adoption paths
4. Read `CONTRIBUTING.md` — contribution guidelines
5. Read a spine document: `governance/CERG-POL-001_Cybersecurity_Policy.md` — understand document structure
6. Run `python3 tools/cerg-validate.py` — confirm current state
7. For editing, use `open(path).read()` + line‑targeted Python — never the `patch` tool
8. After each file edit: commit + push with short message

## CERG in Context Windows

For briefings where CERG content must fit in a small context window (e.g., instructing a separate LLM about the framework):

- **Full index (~5 KB, ~1,300 tokens):** `machine-readable/cerg-llm-index.json` — complete document map
- **Regeneration script:** `tools/regenerate-llm-index.py` — regenerates the JSON index from the latest `llms-full.txt`. Run from repo root after any document is added or removed.
- **Condensed reference (optional):** A ~5,000‑token summary of core principles, pillar model, document taxonomy, key rules, and risk framework. Generate on demand.

The full concatenated corpus is at `https://cerg.nexus/llms-full.txt` (2.9 MB, ~800K tokens) — too large for most context windows.
