
# SURGE: Cyber Engineering, Risk & Governance

## SOX ITGC OPERATIONAL PACKAGE
### Control Library · SOX-Relevant System Register · Evidence Reuse · Deficiency Workflow

---

| | |
|---|---|
| **Document ID** | CERG-PLN-SOX-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (SOX Liaison) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Documents** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) · [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-GOV-OM-001](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) |
| **Supporting Documents** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PRC-AC-002](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) · [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| **Review Cycle** | Annual / Per SOX year |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) mappings · COBIT 2019 (selected) · COSO (selected) |
| **Regulations** | Sarbanes-Oxley Act of 2002 |
| **Environments** | SOX-relevant systems supporting financial reporting |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [In-Scope ITGC Domains](#2-in-scope-itgc-domains)
3. [SOX-Relevant System Register](#3-sox-relevant-system-register)
4. [ITGC Control Library](#4-itgc-control-library)
5. [Evidence Reuse Mapping](#5-evidence-reuse-mapping)
6. [Deficiency Workflow](#6-deficiency-workflow)
7. [Auditor Interface](#7-auditor-interface)
8. [Operating Cadence](#8-operating-cadence)
9. [Roles and Responsibilities](#9-roles-and-responsibilities)
9. [Regulatory and Framework Alignment Summary](#9-regulatory-and-framework-alignment-summary)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

SOX shows up in the policy, the compliance matrix, the IT and Access standards, the risk procedure, and the operating model, but until this package, there was no SOX ITGC control library, no SOX-relevant system register, and no auditor-facing deficiency workflow.

This package fills that gap. It assumes the organization is a publicly-traded U.S. company subject to the Sarbanes-Oxley Act with both external auditor and Internal Audit interaction. Where the organization is private, regulated by an analogous regime, or pre-IPO, the structure of this package adapts but the boundaries, scope by financial-reporting impact, evidence reused from operating controls, remain.

> **The CERG SOX Model in One Sentence**
>
> SOX is not a separate control universe, it is a scope filter over the controls CERG already operates, with formal documentation and quarterly testing for the systems that touch financial reporting.

---

## 2. In-Scope ITGC Domains

The six ITGC domains in scope are the standard set for a publicly traded company:

| **Domain** | **In Scope Because** |
|---|---|
| **Access** | Who can read, modify, or post to financial transactions and master data. |
| **Change** | What changed in financially-relevant logic, configuration, or interfaces. |
| **Operations** | Whether scheduled jobs, interfaces, and batch processing ran as intended. |
| **Backup** | Whether financial records can be recovered. |
| **Interfaces** | Whether data moving between systems remains complete and accurate. |
| **Reports** | Whether financial reports are produced from the intended data and logic. |

If the organization's audit firm scopes differently (some include "End-User Computing" or "Cybersecurity" as separate categories), CERG aligns to that scoping and updates the library; the six above are the durable spine.

---

## 3. SOX-Relevant System Register

The Register is the scope filter, the list of systems whose controls feed external financial reporting. Every CERG control test under SOX scope is performed against systems in this register.

| **Field** | **Description** |
|---|---|
| System Name / Asset ID | - |
| Owner | Named role |
| Business Process Supported | E.g., GL, AP, AR, payroll, fixed assets, treasury |
| Financial Statement Assertion Relevance | Existence · Completeness · Valuation · Rights & Obligations · Presentation |
| Hosted Where | On-prem / IaaS / PaaS / SaaS |
| SOC 1 Available? | Y/N (if hosted) |
| In-Scope Domains | Multi-select of Section 2 domains |
| SOD-Sensitive Roles | Named roles (e.g., AP clerk vs. AP approver) |
| Recovery Tier | Per [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) Section 3 |
| Last Walkthrough | Date |
| Outstanding Deficiencies | IDs |
| Status | In-Scope · Out-of-Scope (with rationale) · Transitional |

The register is owned jointly by CERG Governance (SOX liaison) and Finance / Internal Audit; CERG owns the cyber slice.

---

## 4. ITGC Control Library

Each control names the SOX domain it supports, the CERG control it reuses from [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md), the SOX-specific evidence the auditor expects, and the test approach.

### 4.1 Access ITGCs

| **ITGC** | **Control Statement** | **Reused CERG Control** | **SOX Evidence** | **Test Approach** |
|---|---|---|---|---|
| AX-01 Provisioning | Access to SOX-relevant systems is granted only on documented approval by the system owner. | AC-2 ([`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) §4) | Sample of provisioning tickets with approvals | Sample of N from period |
| AX-02 Termination | Access is removed within defined SLA on user departure. | AC-2 ([`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) §3.3) | Sample of terminations with access-removal evidence | Sample of N from period |
| AX-03 Recertification | SOX-relevant access is recertified quarterly. | AC-2 ([`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) §5) | Quarterly recert campaign results | Full population review of cycle |
| AX-04 Segregation of Duties | SOD enforced on financially-sensitive roles. | AC-5 ([`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) §6.1) | SOD matrix; conflict-resolution log | Quarterly SOD report |
| AX-05 Privileged Access | Privileged access to SOX-relevant systems via PAM with session recording. | AC-6 ([`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) §6) | PAM session log sample; privileged role review | Sample of N |
| AX-06 Authentication | MFA enforced on SOX-relevant system access. | IA-2 ([`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) §11) | IdP policy export; exception register | Configuration review |

### 4.2 Change ITGCs

| **ITGC** | **Control Statement** | **Reused CERG Control** | **SOX Evidence** | **Test Approach** |
|---|---|---|---|---|
| CH-01 Change Authorization | Production changes are authorized before deployment. | CM-3 ([`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) §3) | Change records with named approver | Sample of N |
| CH-02 Segregation of Duties - Change | Developer ≠ deployer for SOX-relevant systems. | CM-3 + AC-5 | CI/CD pipeline review; manual deployment SoD evidence | Configuration review + sample |
| CH-03 Emergency Change | Emergency changes documented within defined window. | CM-3 | Emergency change records with retrospective approval | Sample of N |
| CH-04 Testing | Changes are tested before production deployment. | CM-3 | Test evidence per change record | Sample of N |

### 4.3 Operations ITGCs

| **ITGC** | **Control Statement** | **Reused CERG Control** | **SOX Evidence** | **Test Approach** |
|---|---|---|---|---|
| OP-01 Scheduled Job Monitoring | Scheduled financial jobs are monitored; failures are investigated and remediated. | SI-4 ([`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)) | Job monitoring dashboards; failure tickets | Sample of failures + period review |
| OP-02 System Monitoring | SOX-relevant systems are monitored for availability and security events. | AU-2 / SI-4 | SIEM source inventory; uptime dashboards | Coverage review |
| OP-03 Incident Tracking | Incidents affecting SOX-relevant systems are tracked to closure. | IR family | Incident records with cyber annotation | Sample of N |

### 4.4 Backup ITGCs

| **ITGC** | **Control Statement** | **Reused CERG Control** | **SOX Evidence** | **Test Approach** |
|---|---|---|---|---|
| BK-01 Backup Execution | SOX-relevant systems are backed up per defined schedule. | CP-9 ([`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md)) | Backup tool report; failure tickets | Period review |
| BK-02 Backup Restoration | Restorability is demonstrated at the SOX cadence. | CP-10 ([`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md)) | Restoration test evidence (Section 5.3 of RES-001) | Inspection of test artifact |
| BK-03 Backup Protection | Backups are protected (immutability / separation). | CP-9 ([`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) §4) | Backup configuration evidence | Configuration review |

### 4.5 Interfaces ITGCs

| **ITGC** | **Control Statement** | **Reused CERG Control** | **SOX Evidence** | **Test Approach** |
|---|---|---|---|---|
| IF-01 Interface Inventory | Interfaces between SOX-relevant systems are inventoried. | CM-8 + SC-7 | Interface inventory document | Inspection |
| IF-02 Interface Change Control | Changes to interface logic follow Change ITGCs. | CM-3 | Change records on interface code | Sample of N |
| IF-03 Interface Monitoring | Interface job execution is monitored. | SI-4 | Interface monitoring evidence | Period review |
| IF-04 Interface Integrity | Data integrity controls applied to interface flows. | SC-8 / SI-7 | Configuration / test evidence | Sample / inspection |

### 4.6 Reports ITGCs

| **ITGC** | **Control Statement** | **Reused CERG Control** | **SOX Evidence** | **Test Approach** |
|---|---|---|---|---|
| RP-01 Report Logic Change Control | Changes to financial report logic follow Change ITGCs. | CM-3 | Change records on report objects | Sample of N |
| RP-02 Report Access | Access to financial reports follows Access ITGCs. | AC-2 / AC-6 | Report access review | Sample of N |
| RP-03 Report Reconciliation Support | Reports support reconciliation; data sources are documented. | AU-6 / CM-3 | Report-to-source documentation | Inspection |

---

## 5. Evidence Reuse Mapping

The mapping in Section 4 reuses CERG's existing evidence library. The principle, repeated:

> **SOX Reuses CERG Evidence; CERG Does Not Create SOX-Only Tests**
>
> If a CERG control test is already running at the cadence the SOX auditor needs, on a system in the SOX register, the SOX test consumes that evidence. CERG does not produce a parallel "SOX-only" version. Where reuse is impossible, e.g., the SOX auditor explicitly requires a different sample period, CERG produces the supplemental sample but documents the reuse principle in the test working paper.

Specifically, the most-reused artifacts:

- Quarterly access recertification reports (AX-03, AX-04, AX-05).
- PAM session logs (AX-05).
- Change management records and CI/CD pipeline configuration (CH-01, CH-02, CH-03, CH-04, RP-01).
- SIEM source inventory and detection coverage report (OP-01, OP-02, OP-03, IF-03).
- Backup tool reports and restoration test evidence (BK-01, BK-02, BK-03).
- DISH baseline scan output (where SOX-relevant systems' configuration is tested).

---

## 6. Deficiency Workflow

| **Step** | **Detail** |
|---|---|
| Identification | Deficiency identified via control test failure, internal audit, external audit, or self-assessment. |
| Categorization | Deficiency / Significant Deficiency / Material Weakness - per the auditor's framework. CERG provides facts; auditor categorizes. |
| Root cause analysis | CERG performs RCA; identifies whether issue is design vs. operating. |
| Remediation plan | Owner, milestones, target date; recorded in risk register and in this register. |
| Compensating control | If applicable, named and evidenced. |
| Retest | At completion of remediation, retest performed; result documented. |
| Disclosure | Significant Deficiencies and Material Weaknesses follow the organization's disclosure committee process; CERG provides factual content. |

---

## 7. Auditor Interface

| **Activity** | **CERG Action** |
|---|---|
| Scoping meeting with external auditor | Provide SOX-Relevant System Register; reconcile in/out of scope; confirm test approach per Section 4. |
| SOC 1 reuse for hosted financial systems | Where the financial SaaS or hosting provider has a SOC 1, complementary user-entity control (CUEC) review is conducted; CERG provides the customer-side evidence required. |
| Internal Audit walkthroughs | CERG participates with system owner; provides evidence references. |
| External Auditor testing | CERG provides evidence per the library; supports walkthroughs with system owners. |
| Findings response | Per Section 6. |
| Year-end attestations | CERG produces a summary of control posture by ITGC domain for inclusion in management's assessment. |

---

## 8. Operating Cadence

| **Activity** | **Cadence** |
|---|---|
| SOX-Relevant System Register reconciliation | Quarterly + on material system change |
| ITGC control test execution | Quarterly (cumulative; full year by close) |
| SOD matrix review | Quarterly |
| Internal walkthroughs | Once per period (typically interim Q2 + final Q4) |
| External auditor testing | Per SOX year plan (typically interim + roll-forward) |
| Deficiency review | Continuous; aggregated quarterly |
| Management assessment | Annual at SOX year-end |
| Operating model review (with Internal Audit and Finance) | Annual |

---
## 9. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Package** |
|---|---|
| Sarbanes-Oxley Act §404 | Sections 2–7 |
| COSO Internal Control - Integrated Framework | Cross-cutting |
| COBIT 2019 (selected) | Section 4 |
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (mappings) | Section 4 reused control IDs |

---

## 10. Document Control

| | |
|---|---|
| **Document ID** | CERG-PLN-SOX-001 |
| **Version** | 1.21 |
| **Approved By** | CISO |
| **Next Review** | Annual / per SOX year |
| **Change Log** | 1.0 - Initial publication. ITGC scoping, control library, system register, evidence reuse mapping, deficiency workflow, auditor interface. |

