
# SURGE: Cyber Engineering, Risk & Governance

## CONTROL-TO-PROCEDURE TRACEABILITY MATRIX
### Control Baseline · Operational Procedure · Evidence · Gap Detection · Audit Routing

---

| | |
|---|---|
| **Document ID** | CERG-GOV-TRC-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Control Baseline) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) · [`CERG-TMPL-AUD-001`](CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md) · [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) |
| **Review Cycle** | Annual / On control baseline, standard, procedure, or evidence model change |
| **Frameworks** | NIST 800-53r5 · NIST 800-171r3 · NIST CSF 2.0 GOVERN · ISO/IEC 27001 |
| **Regulations** | Cross-cutting; CMMC, NERC-CIP, SOX ITGC, privacy, customer assurance where applicable |
| **Environments** | All in-scope CERG controls and evidence-producing processes |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How to Read the Matrix](#2-how-to-read-the-matrix)
3. [Traceability Rules](#3-traceability-rules)
4. [Baseline Control Traceability Matrix](#4-baseline-control-traceability-matrix)
5. [Overlay Traceability](#5-overlay-traceability)
6. [Gap Detection Rules](#6-gap-detection-rules)
7. [Maintenance Workflow](#7-maintenance-workflow)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

`CERG-GOV-CB-001` defines the unified control baseline and names evidence for each control. This matrix adds the missing operating layer: for each baseline control, it identifies the standard or procedure that operationalizes the control, the template or evidence package that proves operation, and the gap signal that should be raised when traceability is incomplete.

This document complements the Unified Control Baseline. It does not replace it. The baseline remains the authoritative source for the control statement, owning pillar, evidence name, frequency, and regulatory crosswalk. This matrix is the operational routing map that tells a control owner, auditor, or AI agent where to go to run, test, or fix the control.

> **Every Control Needs a Runbook or a Reason**
>
> A control baseline says what must be true. A procedure says how the organization makes it true. Evidence proves it happened. If a control has no procedure, no standard, and no evidence path, it is not really operational. This matrix is the gap detector.

---

## 2. How to Read the Matrix

| **Column** | **Meaning** |
|---|---|
| Baseline Control | Control identifier and title from `CERG-GOV-CB-001` Section 6. |
| Control Intent | Short operational purpose. The full statement remains in `CERG-GOV-CB-001`. |
| Governing Standard | The standard that sets requirements or parameters. |
| Operating Procedure / Plan | The procedure or plan that runs the control or review cycle. |
| Evidence / Template | The proof package, worksheet, register, or template that supports testing. |
| Primary Accountable Role | Canonical role accountable for traceability and operation. |
| Gap Signal | What indicates that the control lacks operational coverage. |

---

## 3. Traceability Rules

1. Every baseline control must map to at least one governing standard or procedure.
2. Every baseline control must map to named evidence.
3. Evidence must be testable through `CERG-PRC-AUD-001` or an approved regulated-scope audit procedure.
4. If a control is inherited, the inheritance evidence package from `CERG-GOV-CB-001` Section 5 must be linked.
5. If a control is partially implemented or planned, the POA&M and risk linkage must be present.
6. If no CERG procedure owns an operating step, the row is flagged as a gap for the Governance Pillar Leader.
7. This matrix is updated whenever a new standard, procedure, plan, template, or control baseline revision changes ownership or evidence flow.

---

## 4. Baseline Control Traceability Matrix

| **Baseline Control** | **Control Intent** | **Governing Standard** | **Operating Procedure / Plan** | **Evidence / Template** | **Primary Accountable Role** | **Gap Signal** |
|---|---|---|---|---|---|---|
| AC-2 Account Management | Approved, owned, reviewed accounts. | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Access review and JML process under access standard; audit testing through [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md). | JML log, quarterly recertification report, [`CERG-TMPL-AUD-001`](CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md). | Engineering Pillar Leader | Accounts without owner, recertification, or JML evidence. |
| AC-3 Access Enforcement | Approved authentication and authorization. | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Architecture review through [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). | IdP / PAM policy export, architecture intake record. | Engineering Pillar Leader | Local, shared, hard-coded, or bypass access path. |
| AC-6 Least Privilege | Role-bound and time-bound access. | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Quarterly access review and exception workflow through [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). | PAM session logs, role inventory, exception register. | Engineering Pillar Leader | Privileged access without role basis, expiration, or review. |
| AC-7 Unsuccessful Logon Attempts | Identity attack resistance. | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md), [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Detection coverage review through metrics and audit. | IdP policy export, detection rule, coverage report. | Risk Pillar Leader | Failed-login thresholds or detection rules missing. |
| AC-17 Remote Access | Governed and logged remote access. | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md), [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) | Architecture review, risk exception process for nonstandard paths. | Gateway logs, MFA policy export, exception request form. | Engineering Pillar Leader | Direct or undocumented remote access path. |
| AC-19 Mobile / BYOD | Conditional-access controlled mobile access. | [`CERG-STD-EP-001`](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) | Device posture review and exception workflow. | MDM compliance report, exception register. | Engineering Pillar Leader | Mobile access without enrollment or compliance signal. |
| AU-2 Event Logging | Required events reach logging platform. | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Logging coverage review and audit evidence process. | SIEM source inventory, gap report. | Risk Pillar Leader | Required source missing or unmonitored. |
| AU-6 Audit Review | Alerts are reviewed and acted on. | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Metrics reporting through [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md). | Detection coverage report, triage queue metrics. | Risk Pillar Leader | Alert queue lacks review, ownership, or tuning record. |
| AU-9 Protection of Audit Information | Logs protected from alteration. | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Audit test worksheet and evidence review. | Storage policy, admin-action review. | Risk Pillar Leader | Logging admins can alter or delete evidence without oversight. |
| AU-11 Audit Record Retention | Logs retained and retrievable. | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence retrieval sampling. | Retention policy, sample retrieval evidence. | Evidence Librarian | Required logs stale, unretrievable, or outside retention period. |
| CM-2 Baseline Configuration | Secure baseline applied. | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Security change management and audit testing. | DISH baseline catalog, scan report. | Engineering Pillar Leader | System lacks applicable baseline or scan evidence. |
| CM-3 Change Control | Security-relevant changes governed. | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md), [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | [`CERG-PRC-CHG-001`](CERG-PRC-CHG-001_Security_Change_Management_Procedure.md). | CAB minutes, change records, control-impact review. | Engineering Pillar Leader | Production change lacks approval or security review. |
| CM-6 Configuration Settings | Drift detected and routed. | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Exception workflow through [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). | Drift report, exception register. | Engineering Pillar Leader | Drift exists without exception or remediation. |
| CM-7 Least Functionality | Unneeded services disabled. | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md), [`CERG-STD-EP-001`](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) | Vulnerability and configuration review. | Application allowlist, port-scan report. | Engineering Pillar Leader | Unauthorized service, port, or software persists. |
| CM-8 System Component Inventory | Complete authoritative inventory. | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Monthly inventory reconciliation. | Asset inventory export, reconciliation log. | Engineering Pillar Leader | Asset has no owner, class, lifecycle state, or source-of-truth record. |
| CP-2 Contingency Plan | Current recovery plan exists. | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | [`CERG-PLN-BC-001`](CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md). | Plan document, BCP interface record. | Engineering Pillar Leader | System lacks tiered recovery plan or BCP interface. |
| CP-4 Contingency Plan Testing | Recovery plan tested. | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | DR exercise under [`CERG-PLN-BC-001`](CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md). | Test report, lessons learned, risk-register update. | Engineering Pillar Leader | Recovery test overdue or lessons not tracked. |
| CP-9 System Backup | Backups isolated and restorable. | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Backup assurance and DR testing. | Backup report, immutability evidence. | Engineering Pillar Leader | Backup lacks immutability, isolation, or restore evidence. |
| CP-10 Information System Recovery | RTO/RPO proven. | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | DR exercise and recovery validation. | Restoration test evidence. | Engineering Pillar Leader | Restore test cannot meet RTO or RPO. |
| IA-2 Identification and Authentication | Phishing-resistant human identity. | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Access review and exception workflow. | IdP policy, exception register. | Engineering Pillar Leader | Legacy authentication or missing MFA exception. |
| IA-3 Device Identification and Authentication | Device identity recognized. | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md), [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) | Architecture and network review. | NAC / conditional-access policy. | Engineering Pillar Leader | Unknown device can access protected environment. |
| IA-5 Authenticator Management | Secrets, keys, certificates governed. | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md), [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Security change management and audit test. | Secrets manager export, certificate inventory. | Engineering Pillar Leader | Secret or certificate exists outside approved lifecycle. |
| RA-3 Risk Assessment | Risks identified, scored, treated. | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). | Risk register, acceptance memo, exception request. | Risk Pillar Leader | Material issue exists outside risk register. |
| RA-5 Vulnerability Monitoring and Scanning | Vulnerabilities assessed and prioritized. | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md). | Scan reports, SLA dashboard. | Risk Pillar Leader | Asset missing scanner coverage or alternative method. |
| SI-2 Flaw Remediation | Findings remediated or accepted. | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md), [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). | SLA report, exception register, POA&M. | Risk Pillar Leader | Critical or High finding past SLA without approved treatment. |
| SI-4 System Monitoring | Required monitoring covers system. | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Detection coverage and metrics reporting. | Coverage report, dashboard metric. | Risk Pillar Leader | Tool, source, or detection coverage gap not recorded. |
| SR-2 Supply Chain Risk Management Plan | Vendors tiered and governed. | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). | TPRM register, SCCT roster, questionnaire template. | Vendor Risk Analyst | Vendor lacks tier, evidence, contract requirement, or owner. |
| SR-3 Supply Chain Controls and Processes | Country and supply-chain controls enforced. | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md), [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). | Country-risk register, exception register. | Vendor Risk Analyst | International access or supply-chain exception lacks approval. |

---

## 5. Overlay Traceability

| **Overlay** | **Operational Package / Standard** | **Evidence Route** | **Gap Signal** |
|---|---|---|---|
| High-Impact | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md), [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Baseline scan, monitoring coverage, vulnerability SLA report. | High-impact system lacks tightened parameters or evidence. |
| CUI | [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md), [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | SSP, POA&M, CUI evidence package, SPRS / CMMC readiness records. | CUI system lacks SSP, POA&M, or control implementation evidence. |
| BES | [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md), [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | CIP evidence package, ESP/EAP topology, recovery exercise, log retention evidence. | BES control lacks CIP-mapped evidence or review cadence. |
| SOX ITGC | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md), [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | Access, change, operations, backup, interface, and report-control evidence. | SOX system lacks quarterly access review, change record, or operations evidence. |
| OT Safety | [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | Engineering review, change window record, passive assessment evidence. | Safety-impacting OT change lacks engineering review or approved scan method. |
| Privacy | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md), [`CERG-PLN-PRIV-001`](CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md) | DPIA support record, data inventory, deletion evidence, breach clock support record. | Personal data processing lacks inventory, DPIA, or retention evidence. |
| ISO/IEC 27001 | [`CERG-PLN-ISO-001`](CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md) | ISMS scope, SoA, internal audit, management review. | ISO-scoped control lacks SoA rationale or audit evidence. |

---

## 6. Gap Detection Rules

A traceability gap exists when any of the following is true:

1. the baseline names a control but no standard or procedure operationalizes it;
2. a control maps to evidence but no evidence owner is named;
3. a control maps to a procedure that is out of scope, retired, or missing from the catalog;
4. a control depends on inherited control evidence but the inheritance package is missing;
5. a control is partially implemented but has no POA&M item;
6. a control is risk accepted but lacks risk-register entry, acceptance memo, or exception request;
7. a control has evidence, but the evidence cannot be retrieved within the audit retrieval window;
8. the catalog changes but this matrix is not reviewed.

Traceability gaps are routed as follows:

| **Gap Type** | **Route To** | **Required Action** |
|---|---|---|
| Missing standard or procedure | Governance Pillar Leader | Create roadmap item or amend artifact. |
| Missing evidence owner | Evidence Librarian | Assign owner and evidence location. |
| Missing risk or exception link | Risk Register Owner | Create or update risk, exception, or acceptance record. |
| Missing implementation evidence | Responsible control owner | Produce evidence or open POA&M. |
| Catalog mismatch | Governance Pillar Leader (Document Control) | Amend catalog or matrix. |

---

## 7. Maintenance Workflow

This matrix is maintained annually and whenever one of these changes occurs:

- `CERG-GOV-CB-001` adds, removes, or changes a control;
- a standard, procedure, plan, or template is added or retired;
- audit testing finds a control without an operational procedure;
- evidence ownership changes;
- regulatory scope changes;
- CISO directs a traceability review.

Maintenance steps:

1. compare the baseline control list to Section 4;
2. confirm each control still has a governing standard or procedure;
3. confirm each control has named evidence or inheritance package;
4. confirm each evidence path is testable through audit or assessment workflow;
5. update gap signals and routing where the operating model changed;
6. amend the catalog if this artifact or referenced artifacts changed status.

---

## 8. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-TRC-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Control Baseline) |
| **Approved By** | CISO (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on control baseline, standard, procedure, or evidence model change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-53r5; NIST 800-171r3; NIST CSF 2.0 GOVERN; ISO/IEC 27001 |
| **Regulations** | Cross-cutting; CMMC, NERC-CIP, SOX ITGC, privacy, customer assurance where applicable |
| **Environments** | All in-scope CERG controls and evidence-producing processes |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes the control-to-procedure traceability matrix, overlay traceability, gap detection rules, and maintenance workflow. |

### Review Triggers

- Control baseline changes
- Standard, procedure, plan, or template added or retired
- Audit finding related to control ownership or evidence traceability
- Evidence model or owner changes
- Regulatory scope change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Source of baseline controls and evidence names |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence and audit testing workflow |
| Control Evidence and Test Worksheet | [`CERG-TMPL-AUD-001`](CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md) | Test worksheet for controls in this matrix |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative artifact inventory |
