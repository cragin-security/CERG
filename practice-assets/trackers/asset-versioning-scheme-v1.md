# CERG Practice Asset Versioning Scheme v1
## Practice Asset — Not a CERG Corpus Document
## Purpose: Version practice assets independently from the CERG corpus

---

## Why Independent Versioning

Practice assets (intake forms, scope templates, checklists, sector profiles, scripts) evolve on a different cadence than the CERG corpus. The corpus changes on framework releases, regulatory updates, and CISO-directed policy changes. Practice assets change on client feedback, practice methodology improvements, and new sector patterns.

Mixing the two versioning schemes creates confusion about what changed and why.

---

## Versioning Model

All practice assets use **semantic-ish versioning** matching the CERG catalog convention:

| Bump | When | Example |
|---|---|---|
| **Major** (v2.0) | Breaking change: field removed from intake form, tier guardrails restructured, sector profile retired | Form restructured from 22 to 18 questions with different routing logic |
| **Minor** (v1.x) | Additive change: new field, new gate criterion, new sector scenario, new checklist item | Adding "client satisfaction score" field to the engagement tracker |
| **Patch** (v1.0.x) | Clarification, typo, reference fix, format alignment | Correcting a CERG document ID reference in the guardrails |

---

## Version Tracking

Each asset has its version in:
1. **Frontmatter** — metadata header at the top of the file
2. **Revision history** — version table at the bottom of the file (mirroring CERG document control convention)
3. **Git log** — commit messages reference the asset path and version

### Frontmatter format

```
---
asset_id: PRACTICE-ASSETS-{CATEGORY}-{NNN}
version: 1.0
last_reviewed: 2026-06-27
owner: Governance Pillar Leader (Practice Enablement)
---
```

### Revision history format

```
| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-06-27 | Governance | Initial release |
```

---

## Asset ID Scheme

```
PRACTICE-ASSETS-{CATEGORY}-{NNN}
```

| Category | Code | Examples |
|---|---|---|
| Intake | INTK | INTK-001: Intake questionnaire |
| Scope | SCP | SCP-001–004: Tier 1–4 templates |
| Checklist | CHK | CHK-001: Org profile checklist |
| Tracker | TRK | TRK-001: Engagement status tracker |
| Script | SCR | SCR-001: Upstream CI check |
| Sector | SCT | SCT-001: Threat model catalog |
| Debrief | DEB | DEB-001: Debrief protocol |

---

## Change Workflow

1. **Proposal.** Practitioner identifies a change needed based on client feedback or practice improvement.
2. **Review.** Practice Principal reviews the change for backward compatibility and cross-asset consistency.
3. **Version bump.** Apply the correct semantic version bump (major/minor/patch).
4. **Update revision history.** Add a row to the revision history table.
5. **Commit.** Commit with message format: `{asset_id}: {description of change} (v{new_version})`.
6. **Notify.** Post to practice communication channel with change summary.

---

## Directory Conventions

```
practice-assets/
  intake/       INTK-001  → intake-questionnaire-v1.md
  scope-templates/  SCP-001  → ...
  checklists/   CHK-001  → ...
  trackers/     TRK-001  → ...
  scripts/      SCR-001  → ...
  sector-profiles/ SCT-001  → ...
```

The asset ID maps to a file. Renaming the asset ID requires updating every cross-reference across all assets.
