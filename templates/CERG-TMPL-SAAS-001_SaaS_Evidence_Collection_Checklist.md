# SURGE: Cyber Engineering, Risk & Governance
## SaaS Evidence Collection Checklist
### Audit-Ready Artifacts for Tier 1/2 SaaS Tenants

---
| | |
|---|---|
| **Document ID** | CERG-TMPL-SAAS-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Document** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **Review Cycle** | Annual / On SaaS baseline change |
| **Frameworks** | NIST 800-53 AU, CM, AC · SOX ITGC · CMMC · CSA CCM |
| **Regulations** | SOX ITGC · CMMC (where applicable) |
| **Environments** | Tier 1/2 SaaS tenants |

---

## Purpose
This checklist ensures consistent, auditable evidence collection from Tier 1 and Tier 2 SaaS tenants for compliance (SOX, CMMC, ISO 27001) and CERG internal assurance. Evidence is stored in the CERG evidence library per CERG-PRC-AUD-001.

---

## Evidence by Category

### Identity & Access
| **Artifact** | **Source** | **Frequency** | **SOX** | **CMMC** | **Notes** |
|---|---|---|---|---|---|
| Admin role assignments export | SaaS admin console / API | Quarterly | ✓ | ✓ | Filter to privileged roles |
| Conditional Access / MFA policies | IdP / SaaS security center | Quarterly | ✓ | ✓ | Include named locations, device compliance |
| OAuth / third-party app grants inventory | SaaS admin console / API | Quarterly | ✓ | ✓ | Scope, publisher, risk rank |
| User provisioning / deprovisioning logs | IdP / SCIM audit log | Monthly | ✓ | | 90-day lookback |
| Break-glass / emergency access log | SaaS / PAM | Per use | ✓ | | Must have post-use review |

### Configuration & Hardening
| **Artifact** | **Source** | **Frequency** | **SOX** | **CMMC** | **Notes** |
|---|---|---|---|---|---|
| Tenant baseline scan results (CIS/CERG) | SSPM / CSPM | Monthly | ✓ | ✓ | Drift findings → PRC-VM-001 |
| DLP policy configuration export | SaaS security center | Quarterly | ✓ | | For Restricted data tenants |
| Data residency / region config | SaaS admin console | Annual | | ✓ (CUI) | Verify approved regions only |
| Sharing / external access settings | SaaS admin console | Quarterly | ✓ | ✓ | Anonymous links, domain allowlist |

### Logging & Monitoring
| **Artifact** | **Source** | **Frequency** | **SOX** | **CMMC** | **Notes** |
|---|---|---|---|---|---|
| Admin activity audit log sample (90 days) | SaaS audit log export / SIEM | Quarterly | ✓ | ✓ | Verify completeness, tamper-resistance |
| Authentication / sign-in log sample | IdP / SaaS auth logs | Monthly | ✓ | | Include MFA events, failures |
| Alert / detection rule coverage matrix | SIEM / SSPM | Quarterly | | ✓ | Map to MITRE ATT&CK SaaS |
| Failed login / brute-force alerts | SIEM | Monthly | ✓ | | Correlate with lockout policy |

### Data Protection
| **Artifact** | **Source** | **Frequency** | **SOX** | **CMMC** | **Notes** |
|---|---|---|---|---|---|
| Encryption at rest verification (CMK/BYOK) | KMS / SaaS security center | Annual | | ✓ (CUI) | Key rotation evidence |
| Backup configuration & test results | SaaS backup / native | Annual | ✓ (ITGC) | ✓ | RPO/RTO, restoration test |
| Retention / legal hold policies | SaaS admin / compliance center | Annual | ✓ | | Per regulatory requirements |

### Incident & Vendor
| **Artifact** | **Source** | **Frequency** | **SOX** | **CMMC** | **Notes** |
|---|---|---|---|---|---|
| Provider SOC 2 Type II report | Vendor portal | Annual | ✓ | ✓ | Review carve-outs, CUECs |
| Provider incident notification log | TPRM tool / email | Per incident | | ✓ | Verify 24/72hr SLA met |
| Subprocessor list & changes | Vendor trust portal | Quarterly | | ✓ (CUI) | New subprocessor = reassessment |

---

## Collection Workflow
1. **Scheduler** (Governance): Quarterly calendar invite to SaaS tenant owners with this checklist
2. **Collector** (Engineering/Risk): Pull artifacts via API / admin console / SSPM export
3. **Reviewer** (Governance): Verify completeness, link to evidence library, note gaps
4. **Gaps**: Open findings in risk register per PRC-RM-001; track to closure

---

## Document Control
| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-SAAS-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Effective Date** | 2026-06-17 |
| **Review Cycle** | Annual / On SaaS baseline change |
| **Next Scheduled Review** | 2027-06-17 |

### Revision History
| Version | Date | Author | Change Summary |
|---|---|---|---|
| 1.0 | 2026-06-17 | Cyber Governance | Initial release - SaaS evidence collection checklist for Tier 1/2 tenants |

### Related Documents
| Document | ID | Relationship |
|---|---|---|
| IT/Cloud/SaaS Security Standard | CERG-STD-IT-001 | Governing standard §5.4, §5.5 |
| Access Management Standard | CERG-STD-AC-001 | NHI, ITDR evidence cross-reference |
| Audit and Evidence Management Procedure | CERG-PRC-AUD-001 | Evidence library governance |
| Exposure Management Procedure | CERG-PRC-VM-001 | Baseline drift findings pipeline |
