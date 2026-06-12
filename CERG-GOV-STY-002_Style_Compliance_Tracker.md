# CERG Style Compliance Tracker

**Purpose:** Track known STY-001 and governance compliance gaps across the CERG corpus.  
**Owner:** Governance Pillar Leader (Document Control)  
**Generated:** 2026-06-11  
**Status:** Active — items are resolved by amending the affected document on its next scheduled review

---

## Known Compliance Gaps

### Missing Document Control Sections (STY-001 §7.5)

The following Approved documents lack a Document Control section, which STY-001 requires for every artifact:

| Document ID | Document | Status | Scheduled Fix |
|-------------|----------|--------|---------------|
| CERG-GOV-OM-001 | CERG Operating Model | Approved | Next annual review (2027) |
| CERG-PLN-IR-001 | Incident Response Plan | Approved | Next annual review (2027) |
| CERG-PRC-RM-001 | Risk Register and Exception Process | Approved | Next semi-annual review |
| CERG-PRC-VM-001 | Vulnerability Management Procedure | Approved | Next semi-annual review |
| CERG-GOV-TAX-001 | Risk Taxonomy | Approved | Next annual review (2027) |

**Remediation:** On the document's next scheduled review, append a Document Control section following the STY-001 §7.5 format (see §7.5 template below). Add a revision history entry noting the addition.

### Metadata Table Format Inconsistencies (STY-001 §3)

| Issue | Affected Documents | Impact |
|-------|-------------------|--------|
| 2-column metadata format instead of standard 3-column | POL-001 | Minor — functionally equivalent; differs visually from other docs |
| Minimal 4-field metadata table | CMX-001, TAX-001, FRM-001 | Minor — missing fields compared to the 11-field STY-001 standard |
| Inline bold-text metadata (no table) | RMF-001 | Minor — unique format in the corpus |

**Remediation:** Convert to standard 3-column, 11-field format on next review. See cerg-framework skill reference for the safe conversion pattern.

### Document Control Section Numbering

STY-001 §7.5 states "Document Control is always the last section" but does not specify a section number. As a result, Document Control appears as §8 in some documents, §9 in others, §10 in STY-001 itself, and §13 in RMF-001. This is not a compliance gap (STY-001 does not mandate a specific number) but contributes to visual inconsistency.

### 4-Part Document IDs

Per-role job description documents use 4-part IDs (e.g., `CERG-GOV-JD-SECENG-001`) where the standard naming convention (§2) specifies 3-part IDs (`CERG-TYPE-DOMAIN-NNN`). The DOC_ID_PATTERN in cerg-validate.py was extended on 2026-06-11 to accept these IDs. Future documents should use flat domain codes per the convention; the 4-part format is accepted for the workforce architecture family.

---

## STY-001 §7.5 Template — Document Control Section

For reference when remediating the missing sections above:

```
## N. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-XXX-XXX-XXX |
| **Version** | X.X |
| **Status** | [Draft / Approved / Retired] |
| **Effective Date** | YYYY-MM-DD |
| **Classification** | [Public / Internal / Restricted] |
| **Owner** | [Role Name] |
| **Approved By** | [Approver Role] |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | [Annual / Semi-Annual / Quarterly] |
| **Next Scheduled Review** | YYYY-MM-DD |
| **Frameworks** | [Applicable frameworks] |
| **Regulations** | [Applicable regulations] |
| **Environments** | [Applicable environments] |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| X.X | YYYY-MM-DD | [Author] | [Summary] |

### Review Triggers

- [Trigger 1]
- [Trigger 2]

[Owner] owns this document. [Owner] is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| [Document Name] | [`CERG-XXX-XXX-XXX`](filename.md) | [Relationship] |
```

---

## Compliance by the Numbers

| Metric | Count |
|--------|-------|
| Total CERG documents | 72 markdown files |
| Documents with Document Control section | 67 (93%) |
| Documents missing Document Control section | 5 (7%) — tracked above |
| Documents using non-standard metadata format | 5 (7%) — tracked above |
| Documents created 2026-06-11 needing style review | 34 (all in roles/) |
