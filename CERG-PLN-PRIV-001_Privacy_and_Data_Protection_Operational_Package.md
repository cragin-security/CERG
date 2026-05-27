
# SURGE: Cyber Engineering, Risk & Governance

## PRIVACY AND DATA PROTECTION OPERATIONAL PACKAGE
### Privacy Scope · DPIA · Data Subject Requests · Breach Clocks · Evidence Interface

---

| | |
|---|---|
| **Document ID** | CERG-PLN-PRIV-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) |
| **Supporting Documents** | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) · [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) · [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [`CERG-PRC-IR-002`](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) · [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| **Review Cycle** | Annual / On material privacy-law, data-processing, or vendor-scope change |
| **Frameworks** | NIST Privacy Framework · ISO/IEC 27701 · ISO/IEC 27001 · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) |
| **Regulations** | GDPR · CCPA / CPRA · state privacy laws · breach-notification laws · contractual privacy obligations |
| **Environments** | Systems, vendors, processes, and data flows involving personal data or privacy-regulated data |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Ownership Boundary](#2-ownership-boundary)
3. [Privacy Data Inventory](#3-privacy-data-inventory)
4. [Privacy Impact and DPIA Workflow](#4-privacy-impact-and-dpia-workflow)
5. [Data Subject Request Support](#5-data-subject-request-support)
6. [Breach Notification Clock Support](#6-breach-notification-clock-support)
7. [Third-Party Privacy Risk](#7-third-party-privacy-risk)
8. [Retention, Deletion, and Minimization](#8-retention-deletion-and-minimization)
9. [Evidence Library](#9-evidence-library)
10. [Metrics](#10-metrics)
11. [Roles and Responsibilities](#11-roles-and-responsibilities)
12. [Regulatory and Framework Alignment Summary](#12-regulatory-and-framework-alignment-summary)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

CERG does not replace the enterprise privacy, legal, or records-management programs. Those programs determine legal obligations, notices, consent requirements, data subject rights, and regulator communications. CERG supplies the cyber, data governance, asset, vendor, incident, risk, and evidence machinery those privacy decisions need.

This operational package defines how CERG supports privacy and data protection obligations: privacy data inventory, DPIA support, data subject request support, breach-clock facts, vendor privacy evidence, retention and deletion control support, metrics, and evidence.

> **Privacy Fails When Nobody Can Find the Data**
>
> Legal can interpret the obligation. The business can decide the purpose. But if the organization cannot say where personal data lives, who owns it, which vendors process it, how long it is retained, how it is deleted, and what happened during an incident, privacy becomes guesswork. CERG's role is to remove the guesswork.

---

## 2. Ownership Boundary

| **Area** | **Primary Owner** | **CERG Contribution** |
|---|---|---|
| Legal interpretation of privacy laws | Enterprise legal / privacy process | Supplies data, system, vendor, and control facts. |
| Privacy notices, consent, and lawful basis | Enterprise privacy process | Supplies processing inventory and system evidence. |
| Data subject request decisioning | Enterprise privacy process | Locates data, verifies systems, supports deletion/export evidence. |
| Breach notification decisions | Incident Commander with legal and executive process | Supplies data classification, affected systems, logs, and containment evidence. |
| Data classification and handling | Governance Pillar Leader | Owns `CERG-STD-DG-001` and evidence of handling controls. |
| Third-party processing risk | Vendor Risk Analyst | Maintains vendor assessment and contractual control evidence. |
| Privacy-related residual risk | Risk Pillar Leader | Routes risk and exception decisions through the risk register. |

This package intentionally uses CERG canonical roles. Where a privacy or legal function exists outside CERG, the package describes the interface without renaming it as a CERG role.

---

## 3. Privacy Data Inventory

The privacy data inventory extends the asset inventory and data classification standard. It identifies where personal data exists and how it moves.

Minimum inventory fields:

| **Field** | **Description** |
|---|---|
| Processing Activity | Business process or activity using personal data. |
| Business Owner | Accountable business owner or Executive Sponsor. |
| Systems / Assets | Asset IDs from `CERG-STD-AM-001`. |
| Data Categories | Personal data categories processed. |
| Sensitive Data | Special category, financial, health, child, biometric, location, or other sensitive data. |
| Data Subjects | Customers, employees, contractors, vendors, applicants, visitors, or other groups. |
| Purpose | Business purpose for processing. |
| Geography | Jurisdictions where data subjects or processing locations exist. |
| Vendors / Processors | Third parties with access to the data. |
| Retention Period | Required or intended retention. |
| Deletion Method | How data is removed, anonymized, or archived. |
| DSR Supportability | Whether search, export, correction, and deletion are technically supported. |
| Security Controls | Key controls protecting the data. |
| Evidence Location | Evidence library reference. |

The inventory is reviewed at least annually and when a new system, vendor, data category, or processing purpose is introduced.

---

## 4. Privacy Impact and DPIA Workflow

A privacy impact assessment or Data Protection Impact Assessment (DPIA) is required when a change introduces material privacy risk.

Triggers:

- new processing of personal data;
- new sensitive-data category;
- new AI or automated decisioning use case involving people;
- new vendor processing personal data;
- new cross-border transfer or hosting location;
- material change to retention, deletion, or data sharing;
- high-volume monitoring, profiling, or behavioral analytics;
- incident or finding showing privacy control weakness.

CERG supports DPIA with:

1. asset and system inventory;
2. data classification;
3. data-flow and vendor mapping;
4. security controls in place;
5. logging and monitoring posture;
6. deletion and retention capability;
7. third-party control evidence;
8. residual-risk record;
9. evidence package for approval.

DPIA outcomes that require controls are tracked as change actions, risk-register entries, vendor-risk actions, or document updates.

---

## 5. Data Subject Request Support

Data subject requests are owned by the enterprise privacy process. CERG supports the technical execution and evidence.

Support steps:

| **Step** | **CERG Support** |
|---|---|
| Intake confirmation | Confirm whether CERG-managed systems may hold responsive data. |
| System search | Identify systems, vendors, backups, archives, and logs in scope. |
| Export support | Support data extraction where permitted and technically feasible. |
| Correction support | Identify records requiring correction and affected systems. |
| Deletion support | Validate deletion, anonymization, retention exception, or legal hold constraints. |
| Evidence capture | Preserve request ID, systems searched, actions taken, exceptions, and completion evidence. |

CERG does not decide whether a request is valid or whether an exemption applies. CERG supplies facts and executes approved technical actions.

---

## 6. Breach Notification Clock Support

Privacy breach notification clocks often start before the full technical story is known. CERG's job is to provide reliable facts quickly.

Within the incident process, CERG supplies:

- affected systems and asset owners;
- data categories and data subject groups;
- regulated geographies and contractual obligations known to CERG;
- approximate data volume if available;
- access logs, DLP events, exfiltration indicators, and containment actions;
- vendor involvement;
- encryption, tokenization, or other protective control status;
- evidence of when the event was detected, escalated, contained, and resolved.

Notification decisions remain with the Incident Commander, legal, executive, and enterprise privacy process. CERG preserves the evidence and records residual control gaps.

> **The Clock Does Not Wait for Perfect Forensics**
>
> Privacy deadlines are measured in hours and days, not in the time it takes to reach certainty. CERG therefore supplies decision-grade facts: what is known, what is unknown, what is being validated, and which controls may change the notification analysis.

---

## 7. Third-Party Privacy Risk

Third parties processing personal data are assessed through `CERG-PRC-TPRM-001` with privacy-specific evidence added.

Minimum vendor privacy evidence:

| **Evidence** | **Purpose** |
|---|---|
| Data categories processed | Confirms scope of personal data exposure. |
| Processing location | Supports geography and transfer analysis. |
| Subprocessor list | Identifies downstream processing. |
| Security control evidence | Confirms protection of personal data. |
| Breach notification commitment | Supports notification timing and coordination. |
| Deletion / return terms | Supports termination and DSR obligations. |
| Audit or assurance report | Supports control reliance. |
| Contractual control mapping | Supports privacy and security clauses. |

Vendor gaps that expose personal data become vendor-risk findings or risk-register entries.

---

## 8. Retention, Deletion, and Minimization

CERG supports retention and minimization by ensuring systems can enforce or evidence the business rule.

Requirements:

1. Systems processing personal data have a documented retention expectation.
2. Retention conflicts are escalated to the business owner and enterprise privacy process.
3. Deletion mechanisms are documented for T1/T2 and high-volume personal-data systems.
4. Backups and archives document restoration and deletion limitations.
5. Logs containing personal data are classified and retained only as long as justified.
6. New systems demonstrate minimization and deletion capability during architecture review.
7. Data that cannot be deleted on request due to legal, technical, or backup constraints has a documented rationale and evidence.

---

## 9. Evidence Library

Privacy evidence is retained under `CERG-PRC-AUD-001`.

| **Evidence Area** | **Contents** |
|---|---|
| Privacy data inventory | Processing records, systems, vendors, data categories. |
| DPIA / privacy impact records | Assessments, approvals, control actions. |
| DSR support evidence | Systems searched, exports, deletion evidence, exceptions. |
| Breach support evidence | Incident facts, data classification, containment, logs. |
| Vendor privacy evidence | Subprocessors, locations, contractual controls, deletion terms. |
| Retention and deletion evidence | Retention rules, deletion tests, exceptions. |
| Risk and exception records | Privacy-related risks and acceptances. |

---

## 10. Metrics

| **Metric** | **Purpose** |
|---|---|
| Systems with personal data inventory complete | Measures inventory coverage. |
| High-risk processing activities with DPIA complete | Measures assessment coverage. |
| DSR requests supported within required technical window | Measures response support. |
| Privacy incidents with complete CERG evidence package | Measures breach-readiness discipline. |
| Vendors processing personal data with current evidence | Measures third-party privacy posture. |
| Systems with documented deletion capability | Measures operational privacy readiness. |
| Privacy-related risks open by age and severity | Measures remediation posture. |
| Data inventory records reviewed on schedule | Measures governance hygiene. |

---

## 11. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Privacy Support Responsibility** |
|---|---|
| **Governance Pillar Leader** | Accountable owner for this package, privacy evidence coordination, and data-governance interface. |
| **Policy & Standards Manager** | Maintains privacy-support documentation and related standard updates. |
| **Evidence Librarian** | Maintains privacy evidence library and request-support evidence. |
| **Risk Pillar Leader** | Assesses privacy-related residual risk and treatment. |
| **Risk Register Owner** | Records privacy-related risks, exceptions, and review dates. |
| **Vendor Risk Analyst** | Assesses vendors processing personal data and maintains vendor privacy evidence. |
| **Engineering Pillar Leader** | Coordinates technical support for deletion, export, logging, control validation, and architecture review. |
| **Cloud Security Engineer** | Supports SaaS, cloud, storage, and platform privacy evidence. |
| **Identity Engineer** | Supports identity, access, and account evidence for privacy investigations and DSR execution. |
| **Application Security Engineer** | Supports application data-flow, SDLC, API, and AI privacy-risk reviews. |
| **Detection Engineer** | Supplies relevant alerting, logging, and exfiltration evidence where in scope. |
| **Incident Commander** | Commands active incident response when a privacy incident is part of a security incident. |
| **Chief Information Security Officer (CISO)** | Approves material privacy-security risk acceptance and executive escalation. |

---

## 12. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Package** |
|---|---|---|
| GDPR | Records of processing, DPIA, data subject rights, breach notification | Sections 3, 4, 5, 6 |
| CCPA / CPRA | Consumer rights, deletion, vendor processing | Sections 3, 5, 7, 8 |
| State privacy laws | Breach and rights support | Sections 5, 6, 9 |
| NIST Privacy Framework | Identify, Govern, Control, Communicate, Protect | Sections 3 through 10 |
| ISO/IEC 27701 | Privacy information management | Sections 3, 4, 7, 9 |
| ISO/IEC 27001 | Data protection, risk, suppliers, incidents | Sections 4, 6, 7, 9 |

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-PRIV-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO (pending); enterprise privacy process concurrence required where applicable |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material privacy-law, data-processing, or vendor-scope change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST Privacy Framework; ISO/IEC 27701; ISO/IEC 27001; NIST CSF 2.0 |
| **Regulations** | GDPR; CCPA / CPRA; state privacy laws; breach-notification laws; contractual privacy obligations |
| **Environments** | Systems, vendors, processes, and data flows involving personal data or privacy-regulated data |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes CERG's privacy support boundary, privacy data inventory, DPIA support workflow, data subject request technical support, breach notification clock support, third-party privacy risk evidence, retention and deletion support, evidence library, metrics, and canonical role responsibilities. |

### Review Triggers

- Material change to privacy law or contractual privacy obligation
- New high-risk processing activity
- Material incident involving personal data
- Material change to data governance, vendor-risk, or incident-response process
- DPIA or audit finding requiring package update
- Direction from the CISO

Cyber Governance owns this package. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval and enterprise privacy process concurrence where applicable.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines canonical roles and adjacent-program boundary |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control source for privacy-support controls |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Classification, labeling, handling, retention, and DLP support |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | System and ownership inventory |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor risk requirements and privacy evidence workflow |
| Incident Response Playbook Set | [`CERG-PRC-IR-002`](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) | Privacy incident support evidence |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence retention |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Privacy-related risks and exceptions |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `PRIV` domain |
