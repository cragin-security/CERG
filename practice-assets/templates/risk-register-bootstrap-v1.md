# CERG Risk Register Bootstrap
## Practice Asset — Not a CERP Corpus Document
## Purpose: Seed file for first risk register population

---

## How to Use

This file contains 10 representative risk entries that cover the common risk patterns a first-time CERG adopter will encounter. The entries are intentionally generic — replace the affected systems, owners, and compensating controls with the client's actual environment before the first risk review.

The bootstrap is designed to:
1. Demonstrate the required fields per TMPL-RM-001 schema
2. Give the first risk review meeting something to discuss immediately
3. Establish the scoring discipline before client-specific risks are identified

---

## Bootstrap Entries

### RISK-001: Asset Inventory Incomplete

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-001 |
| Description | Asset inventory does not cover all in-scope systems. Unknown assets represent unmanaged attack surface and a compliance documentation gap. |
| Affected Assets | All systems (scope incomplete) |
| Risk Owner | {{Risk Pillar Leader}} |
| Severity | High |
| Likelihood | 4 (Very Likely) |
| Impact | 4 (Major) |
| Risk Score | 16 (High) |
| Treatment | Accept (monitor); reduce via CM-8 implementation |
| Compensating Controls | Active network scanning discovers unknown devices within 24 hours |
| Target Closure | {{DAY_90_DATE}} |
| Status | Open |

### RISK-002: No Formal Risk Acceptance Process

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-002 |
| Description | Risk acceptances are informal (email, verbal). No audit trail exists for regulatory review. |
| Affected Assets | All systems |
| Risk Owner | {{Governance Pillar Leader}} |
| Severity | High |
| Likelihood | 3 (Likely) |
| Impact | 4 (Major) |
| Risk Score | 12 (High) |
| Treatment | Accept (monitor); reduce via PRC-RM-001 adoption |
| Compensating Controls | CISO reviews all exception decisions weekly |
| Target Closure | {{DAY_60_DATE}} |
| Status | Open |

### RISK-003: MFA Not Enforced on All Remote Access

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-003 |
| Description | Remote access to production systems does not require MFA in all cases. Credential theft would enable direct access. |
| Affected Assets | {{List production systems}} |
| Risk Owner | {{Engineering Pillar Leader}} |
| Severity | Critical |
| Likelihood | 3 (Likely) |
| Impact | 5 (Catastrophic) |
| Risk Score | 15 (Critical) |
| Treatment | Reduce: implement MFA per STD-AC-001 timeline |
| Compensating Controls | VPN with certificate-based authentication; access limited to business hours |
| Target Closure | {{DAY_60_DATE}} |
| Status | Open |

### RISK-004: Vulnerability Remediation SLA Not Defined

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-004 |
| Description | No formally documented SLA for remediating discovered vulnerabilities. Remediation is ad hoc and does not prioritize by severity. |
| Affected Assets | All systems |
| Risk Owner | {{Risk Pillar Leader}} |
| Severity | High |
| Likelihood | 4 (Very Likely) |
| Impact | 3 (Moderate) |
| Risk Score | 12 (High) |
| Treatment | Reduce: adopt PRC-VM-001 SLA framework |
| Compensating Controls | CISO reviews all critical vulnerabilities within 48 hours of discovery |
| Target Closure | {{DAY_60_DATE}} |
| Status | Open |

### RISK-005: No Architecture Security Review Process

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-005 |
| Description | Projects and system changes proceed to production without a documented security architecture review. Security gaps are discovered post-deployment. |
| Affected Assets | All new systems and major changes |
| Risk Owner | {{Engineering Pillar Leader}} |
| Severity | High |
| Likelihood | 3 (Likely) |
| Impact | 4 (Major) |
| Risk Score | 12 (High) |
| Treatment | Reduce: adopt PRC-AR-001 |
| Compensating Controls | Engineering lead reviews all production changes informally |
| Target Closure | {{DAY_60_DATE}} |
| Status | Open |

### RISK-006: No Formal Third-Party Risk Assessment

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-006 |
| Description | Third-party vendors with access to organizational data are not formally assessed for security risk. Contractual security requirements are inconsistent. |
| Affected Assets | {{List critical vendors}} |
| Risk Owner | {{Risk Pillar Leader (TPRM)}} |
| Severity | High |
| Likelihood | 3 (Likely) |
| Impact | 4 (Major) |
| Risk Score | 12 (High) |
| Treatment | Reduce: adopt PRC-TPRM-001; prioritize Tier 1 vendors within 90 days |
| Compensating Controls | Legal review of vendor contracts includes basic security clauses |
| Target Closure | {{DAY_90_DATE}} |
| Status | Open |

### RISK-007: Security Awareness Training Lacks Role-Specific Content

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-007 |
| Description | Annual security awareness training is generic and does not address role-specific risks (e.g., developers, OT operators, finance users). |
| Affected Assets | All personnel |
| Risk Owner | {{Governance Pillar Leader}} |
| Severity | Medium |
| Likelihood | 3 (Likely) |
| Impact | 3 (Moderate) |
| Risk Score | 9 (Medium) |
| Treatment | Reduce: implement role-specific training modules per TRN-001 |
| Compensating Controls | Annual phishing simulation covers general awareness gaps |
| Target Closure | {{DAY_90_DATE}} |
| Status | Open |

### RISK-008: Log Retention Below Regulatory Requirements

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-008 |
| Description | Audit logs are retained for less than the minimum period required by applicable regulations (13 months hot / 7 years cold per CERG default). |
| Affected Assets | All systems with logging |
| Risk Owner | {{Risk Pillar Leader}} |
| Severity | Medium |
| Likelihood | 2 (Unlikely) |
| Impact | 4 (Major) |
| Risk Score | 8 (Medium) |
| Treatment | Reduce: implement STD-LM-001 retention parameters |
| Compensating Controls | SIEM retains 90 days of hot data |
| Target Closure | {{DAY_90_DATE}} |
| Status | Open |

### RISK-009: No Documented Recovery Test for Critical Systems

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-009 |
| Description | Recovery procedures exist but have not been tested in the last 12 months. The organization cannot confirm RTO/RPO targets are achievable. |
| Affected Assets | {{List Tier 0 / Tier 1 assets}} |
| Risk Owner | {{Engineering Pillar Leader}} |
| Severity | High |
| Likelihood | 2 (Unlikely) |
| Impact | 5 (Catastrophic) |
| Risk Score | 10 (High) |
| Treatment | Reduce: schedule recovery test for all Tier 0 systems within 90 days |
| Compensating Controls | Backup verification runs daily for Tier 0 systems |
| Target Closure | {{DAY_90_DATE}} |
| Status | Open |

### RISK-010: Configuration Baseline Drift Not Detected

| Field | Value |
|---|---|
| ID | RISK-{{YYYY}}-010 |
| Description | No automated mechanism detects when systems drift from the approved configuration baseline. A hardened system that reverts to an insecure state is not identified until the next manual review. |
| Affected Assets | All managed systems |
| Risk Owner | {{Engineering Pillar Leader}} |
| Severity | Medium |
| Likelihood | 4 (Very Likely) |
| Impact | 2 (Minor) |
| Risk Score | 8 (Medium) |
| Treatment | Reduce: implement DISH drift detection |
| Compensating Controls | Quarterly manual baseline review by Engineering |
| Target Closure | {{DAY_90_DATE}} |
| Status | Open |

---

## Scoring Schema

Each entry uses a 5x5 risk matrix:

| Likelihood | 1 (Rare) | 2 (Unlikely) | 3 (Likely) | 4 (Very Likely) | 5 (Almost Certain) |
|---|---|---|---|---|---|
| **5 (Catastrophic)** | 10 | 10 | 15 | 20 | 25 |
| **4 (Major)** | 8 | 8 | 12 | 16 | 20 |
| **3 (Moderate)** | 6 | 6 | 9 | 12 | 15 |
| **2 (Minor)** | 4 | 4 | 6 | 8 | 10 |
| **1 (Negligible)** | 2 | 2 | 3 | 4 | 5 |

**Score → Severity:** 1-4 Low · 5-8 Medium · 9-12 High · 15-25 Critical

## Field Population Rules

- Replace `{{YYYY}}` with the current year
- Replace `{{DAY_60_DATE}}` / `{{DAY_90_DATE}}` with target dates relative to engagement start
- Replace `{{Role Name}}` placeholders with the named person holding that role in the client's role consolidation map
- Replace `{{List X}}` with the client's actual system names
- Remove entries that do not apply to the client; add client-specific entries before the first review
