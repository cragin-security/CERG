# CERG Style Compliance Tracker

**Purpose:** Track known STY-001 and governance compliance gaps across the CERG corpus.  
**Owner:** Governance Pillar Leader (Document Control)  

| | |
|---|---|
| **Document ID** | CERG-GOV-STY-002 |
| **Version** | 1.01 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |



---

## Known Contradictions Resolved

The following contradictions existed in the corpus at the time of the June 2026 review. Each has been resolved as documented below.

| Contradiction | Artifacts | Resolution | Fixed In |
|--------------|-----------|------------|----------|
| IR documents included in repo but IR is not CERG-owned | PLN-IR-001, PRC-IR-002, OM-001 §3.4 | Marked IR docs as ADJACENT FUNCTION (External Interface status, IR team owner, "included for cross-reference only" banners at top) | Commit fb71eeb |
| Approved status with Pending approvers | 36 documents across all families | Set all "Approved By" to CISO (per user convention). Pending is now only possible in Draft documents. | Commit 20606a3 |
| Per-role documents owned by Governance per CAT-001 §4.2 says Pillar Leaders | 32 per-role JD files | Updated file Owner fields to match CAT-001 delegation (Engineering → Engineering PL, Risk → Risk PL, etc.). | Commit 5c2c105 |
| Risk acceptance expiration defaults not defined | RMF-001, PRC-RM-001 | Added default expiration durations per severity (Critical 30d, High 90d, Medium 180d, Low 365d) in IMP-002 §5. | Commit 3d9305c |
| FLOW-001 timeout-bypass may conflict with RMF-001 approval authority | FLOW-001 §1 principle 9, RMF-001 §9.7 | Noted as intentional design: timeout-bypass includes documented rationale requirement and does not apply to statutory/regulatory approval decisions. | Noted in errors.md |
| Self-service closure defined in FLOW-001 but not referenced in PRC-RM-001 | FLOW-001 F-04, PRC-RM-001 | PRC-RM-001 references F-04 for finding treatment. Update on next PRC-RM-001 review cycle. | Deferred to next PRC-RM-001 review |

---
**Generated:** 2026-06-11  
**Status:** Approved tracker — items are resolved by amending the affected document on its next scheduled review

---

## Known Compliance Gaps

### Missing Document Control Sections (STY-001 §7.5)

The following Approved documents lack a Document Control section, which STY-001 requires for every artifact:

| Document ID | Document | Status | Scheduled Fix |
|-------------|----------|--------|---------------|
| CERG-GOV-OM-001 | CERG Operating Model | Approved | Next annual review (2027) |
| CERG-PLN-IR-001 | Incident Response Plan | Approved | Next annual review (2027) |
| CERG-PRC-RM-001 | Risk Register and Exception Process | Approved | Next semi-annual review |
| CERG-PRC-VM-001 | Exposure Management Procedure | Approved | Next semi-annual review |
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
| **Document ID** | <CERG-TYPE-DOMAIN-NNN> |
| **Version** | X.X |
| **Status** | [Draft / For Review / Approved / Retired] |
| **Effective Date** | YYYY-MM-DD |
| **Classification** | [Public / Internal / Restricted] |
| **Owner** | [Role Name] |
| **Approved By** | CISO |
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
| [Document Name] | [`<CERG-TYPE-DOMAIN-NNN>`](../filename.md) | [Relationship] |
```

---



---

## Known Contradictions Resolved

The following contradictions existed in the corpus at the time of the June 2026 review. Each has been resolved as documented below.

| Contradiction | Artifacts | Resolution | Fixed In |
|--------------|-----------|------------|----------|
| IR documents included in repo but IR is not CERG-owned | PLN-IR-001, PRC-IR-002, OM-001 §3.4 | Marked IR docs as ADJACENT FUNCTION (External Interface status, IR team owner, "included for cross-reference only" banners at top) | Commit fb71eeb |
| Approved status with Pending approvers | 36 documents across all families | Set all "Approved By" to CISO (per user convention). Pending is now only possible in Draft documents. | Commit 20606a3 |
| Per-role documents owned by Governance per CAT-001 §4.2 says Pillar Leaders | 32 per-role JD files | Updated file Owner fields to match CAT-001 delegation (Engineering → Engineering PL, Risk → Risk PL, etc.). | Commit 5c2c105 |
| Risk acceptance expiration defaults not defined | RMF-001, PRC-RM-001 | Added default expiration durations per severity (Critical 30d, High 90d, Medium 180d, Low 365d) in IMP-002 §5. | Commit 3d9305c |
| FLOW-001 timeout-bypass may conflict with RMF-001 approval authority | FLOW-001 §1 principle 9, RMF-001 §9.7 | Noted as intentional design: timeout-bypass includes documented rationale requirement and does not apply to statutory/regulatory approval decisions. | Noted in errors.md |
| Self-service closure defined in FLOW-001 but not referenced in PRC-RM-001 | FLOW-001 F-04, PRC-RM-001 | PRC-RM-001 references F-04 for finding treatment. Update on next PRC-RM-001 review cycle. | Deferred to next PRC-RM-001 review |

## Compliance by the Numbers

| Metric | Count |
|--------|-------|
| Total CERG documents | 72 governed markdown files |
| Documents with Document Control section | 67 (93%) |
| Documents missing Document Control section | 5 (7%) — tracked above |
| Documents using non-standard metadata format | 5 (7%) — tracked above |
| Documents created 2026-06-11 needing style review | 34 (all in roles/) |
