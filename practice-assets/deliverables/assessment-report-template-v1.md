# CERG Client Assessment Report Template v1

**Purpose:** Standard report structure for delivering security assessment findings to clients.
**Target audience:** Client CISO, IT Director, and executive stakeholders.
**Format:** Delivered as PDF or client-shared document. Customize sections per engagement.

---

## 1. Executive Summary

*[1-2 paragraphs — what we assessed, what we found, what matters most]*

**Bottom Line:** *[Single sentence — the one thing the client must act on]*

| Metric | Finding |
|--------|---------|
| **Current Maturity Level** | Tier 1 / Tier 2 / Tier 3 / Tier 4 |
| **Controls Assessed** | X of 100 Core Controls |
| **Controls Passing** | X (%) |
| **Critical Findings** | X |
| **High Findings** | X |
| **Estimated Remediation** | X weeks / months |

---

## 2. Engagement Scope

| Field | Value |
|-------|-------|
| **Client** | [Client Name] |
| **Engagement Type** | Tier 1 Foundations / Tier 2 Structure / Tier 3 Compliance / Tier 4 Strategic |
| **Assessment Date** | YYYY-MM-DD |
| **CERG Practitioner** | [Name] |
| **Framework Used** | CERG Core Controls (100) · [NIST CSF 2.0 / NIST 800-53 / Other] |
| **In Scope Systems** | [Brief description] |
| **Out of Scope** | [Brief description] |

---

## 3. Methodology

CERG controls were assessed using:
- **Self-attestation:** Client response to CERG intake questionnaire
- **Technical validation:** Evidence collection via [Entra ID / SentinelOne / Wiz / other tools]
- **Interview:** Stakeholder interviews with [IT / Security / Compliance teams]

### Scoring

| Score | Meaning |
|-------|---------|
| **Implemented** | Control is fully implemented and evidenced |
| **Partially Implemented** | Control exists but has gaps in coverage, automation, or evidence |
| **Not Implemented** | Control does not exist or cannot be evidenced |
| **Not Applicable** | Control does not apply to this environment (with rationale) |

---

## 4. Control Assessment Results

### 4.1 Overall Summary

| Domain | Total Controls | Implemented | Partial | Not Implemented | N/A |
|--------|---------------|-------------|---------|-----------------|-----|
| Access Control (AC) | 13 | | | | |
| Audit & Accountability (AU) | 9 | | | | |
| Configuration Management (CM) | 8 | | | | |
| Contingency Planning (CP) | 6 | | | | |
| Identification & Auth (IA) | 8 | | | | |
| Incident Response (IR) | 5 | | | | |
| Risk Assessment (RA) | 5 | | | | |
| System & Comms Protection (SC) | 7 | | | | |
| System & Info Integrity (SI) | 8 | | | | |
| Supply Chain (SR) | 2 | | | | |
| Other Families | 29 | | | | |
| **Total** | **100** | | | | |

### 4.2 Critical & High Findings

| Control | Finding | Severity | Current State | Recommendation |
|---------|---------|----------|---------------|---------------|
| [ID] | [Description] | Critical / High | [What exists] | [What to do] |

### 4.3 Per-Control Detail

*[One section per control, following this pattern]:*

#### AC-1: Access Control Policy — **Implemented** / **Partial** / **Not Implemented**

| Evidence | Status |
|----------|--------|
| Policy document exists | ✅ / ❌ |
| Approver named | ✅ / ❌ |
| Review cycle documented | ✅ / ❌ |

**Assessment notes:** [Detailed observations]

---

## 5. Risk Register (Findings)

| ID | Control | Finding | Severity | Likelihood | Impact | Risk Score | Remediation |
|----|---------|---------|----------|------------|--------|------------|-------------|
| RISK-001 | AC-3 | Legacy auth enabled | High | Likely | Major | 16 | Disable legacy auth via CA |

---

## 6. Recommendations

### Priority 1 — Immediate Actions (0-30 days)

| Action | Control | Effort | Impact |
|--------|---------|--------|--------|
| [Action] | [ID] | [Hours] | [Which risk it addresses] |

### Priority 2 — Short Term (30-90 days)

| Action | Control | Effort | Impact |
|--------|---------|--------|--------|

### Priority 3 — Strategic (90+ days)

| Action | Control | Effort | Impact |
|--------|---------|--------|--------|

---

## 7. Remediation Roadmap

| Phase | Timeline | Focus | Controls | Budget (est.) |
|-------|----------|-------|----------|---------------|
| Phase 1: Foundation | 0-30 days | Quick wins, policy, MFA | AC-1, AC-3, IA-1, SI-1 | $X |
| Phase 2: Structure | 30-90 days | Process, logging, vulnerability | AU-1, AU-2, CM-1, RA-2 | $X |
| Phase 3: Maturity | 90-180 days | Compliance, supply chain, DR | CP-1, SR-1, CA-1, PL-1 | $X |

---

## 8. Appendix

### A. Full Control Matrix

*[Link to or include full CSV export from CB-001]*

### B. Evidence Collected

| Control | Evidence Type | Source | Date |
|---------|--------------|--------|------|
| [ID] | [Policy/Script/Config] | [What tool] | YYYY-MM-DD |

### C. Maturity Scorecard

| Pillar | Current Score | Target Score | Gap |
|--------|--------------|--------------|-----|
| Engineering | 1.X | X.X | X.X |
| Risk | 1.X | X.X | X.X |
| Governance | 1.X | X.X | X.X |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | CERG-DELIV-ASMT-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Confidential |
| **Owner** | CERG Practice Lead |
| **Effective Date** | YYYY-MM-DD |

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 | 2026-06-30 | CERG Practice Lead | Initial version |
