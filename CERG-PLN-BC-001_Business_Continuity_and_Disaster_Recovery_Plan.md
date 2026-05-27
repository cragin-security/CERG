
# SURGE: Cyber Engineering, Risk & Governance

## BUSINESS CONTINUITY AND DISASTER RECOVERY PLAN
### Business Impact Analysis · Recovery Sequencing · Crisis Roles · DR Exercises · Cyber Recovery Interface

---

| | |
|---|---|
| **Document ID** | CERG-PLN-BC-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) |
| **Supporting Documents** | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) · [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) · [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) · [`CERG-PRC-IR-002`](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) · [`CERG-PRC-CHG-001`](CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| **Review Cycle** | Annual / After major outage, DR exercise, or business-process change |
| **Frameworks** | [NIST 800-34r1](https://csrc.nist.gov/pubs/sp/800/34/r1/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CP, IR) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (RECOVER) · ISO 22301 · ISO/IEC 27031 |
| **Regulations** | SOX ITGC · CMMC L2 / 800-171r3 · NERC-CIP CIP-009 where applicable |
| **Environments** | Business-critical processes, supporting systems, regulated environments, and CERG-managed recovery controls |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [BCP and Cyber Recovery Boundary](#2-bcp-and-cyber-recovery-boundary)
3. [Business Impact Analysis](#3-business-impact-analysis)
4. [Recovery Tier Model](#4-recovery-tier-model)
5. [Recovery Sequencing](#5-recovery-sequencing)
6. [Crisis Roles and Governance](#6-crisis-roles-and-governance)
7. [Plan Activation and Communications](#7-plan-activation-and-communications)
8. [Disaster Recovery Exercise Program](#8-disaster-recovery-exercise-program)
9. [Evidence and Records](#9-evidence-and-records)
10. [Metrics](#10-metrics)
11. [Roles and Responsibilities](#11-roles-and-responsibilities)
12. [Regulatory and Framework Alignment Summary](#12-regulatory-and-framework-alignment-summary)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

[`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) defines the technical recovery bar: backup protection, immutable copies, restoration testing, and cyber recovery tiers. This plan defines the operational wrapper around that bar: business impact analysis, recovery sequencing, crisis roles, recovery decisioning, exercise cadence, and evidence.

This plan applies to business processes and systems whose interruption could cause material operational, regulatory, customer, safety, financial, or reputational impact. It is written as a CERG-operable plan, not a full enterprise business-continuity program charter. It gives the program-in-a-box enough structure to survive an outage and to prove the recovery discipline existed before the outage.

> **A Backup Is Not a Continuity Plan**
>
> A clean restore is necessary, but it is not sufficient. The business still has to know which process comes back first, which degraded process is acceptable, who declares the crisis, who talks to customers, who approves operating below normal control posture, and what evidence proves the recovery was controlled. Disaster recovery restores technology. Business continuity restores the business.

---

## 2. BCP and Cyber Recovery Boundary

| **Question** | **Primary Owner** | **CERG Contribution** |
|---|---|---|
| Which business processes are most critical? | Business owner / Enterprise BCP | Uses the BIA output to align recovery tiers. |
| Can backups be restored cleanly? | Engineering Pillar Leader | Owns technical restoration validation under `CERG-STD-RES-001`. |
| Which systems support the process? | Business owner with Asset Management | Uses the asset inventory and dependency records. |
| Who declares a crisis? | Enterprise crisis process / CISO when cyber-led | Provides security impact, risk, and control-state facts. |
| Can the business operate manually or degraded? | Business owner / Enterprise BCP | Identifies cyber control implications of degraded operation. |
| What residual risk exists during recovery? | Risk Pillar Leader | Records and routes risk acceptance under `CERG-PRC-RM-001`. |
| What evidence proves recovery readiness? | Governance Pillar Leader | Maintains evidence package and audit trail. |

CERG does not replace Enterprise BCP. CERG supplies the cyber, risk, evidence, and control integrity layer that BCP needs.

---

## 3. Business Impact Analysis

The Business Impact Analysis (BIA) is the source record for recovery priority. Each in-scope business process has a BIA record with the fields below.

| **Field** | **Purpose** |
|---|---|
| Business Process | Named process or service being protected. |
| Business Owner | Accountable owner for recovery priority and acceptable degradation. |
| Supporting Systems / Assets | Asset IDs from `CERG-STD-AM-001`. |
| Data Classification | Highest data classification processed. |
| Regulated Scope | SOX, CUI, NERC-CIP, privacy, contractual, or other obligations. |
| Maximum Tolerable Downtime | Business tolerance for interruption. |
| Target RTO | Required recovery time objective. |
| Target RPO | Required recovery point objective. |
| Manual Workaround | Whether degraded manual operation exists and for how long. |
| Upstream Dependencies | Vendors, networks, identity, facilities, data feeds. |
| Downstream Dependencies | Processes or customers that rely on this process. |
| Recovery Priority | Sequencing tier for restoration. |
| Minimum Control Posture | Security controls required before operation resumes. |

BIA records are reviewed at least annually and whenever a critical process, system dependency, regulated scope, or business owner changes.

---

## 4. Recovery Tier Model

The plan uses the recovery tiers defined in [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md). The BIA may assign a stricter business requirement than the technical recovery tier, but it may not silently assign a weaker one for a regulated or mission-critical process.

| **Tier** | **Business Meaning** | **Minimum Planning Requirement** |
|---|---|---|
| T1 - Mission-Critical | Outage creates safety, regulatory, material financial, or severe customer impact within hours. | Documented recovery runbook, quarterly restore evidence, annual full DR exercise, named crisis owner. |
| T2 - Business-Critical | Outage materially impairs operations within one business day. | Documented recovery runbook, semi-annual restore evidence, annual tabletop or technical exercise. |
| T3 - Important | Outage degrades operations but is tolerable for several days. | Documented recovery steps, annual restore evidence, annual review. |
| T4 - Standard | Outage is inconvenient but manageable through ordinary support. | Backup and rebuild path documented. |
| T5 - Non-Production | Recovery is rebuild from code, infrastructure-as-code, or golden image. | Rebuild method documented where needed. |

> **RTO and RPO Are Claims Until Tested**
>
> A stated RTO or RPO does not become a planning fact until it has been demonstrated. Until then, the recovery tier is aspirational and the gap is tracked as a resilience risk. The plan may still operate, but leadership must know which recovery promises are proven and which are hoped for.

---

## 5. Recovery Sequencing

Recovery sequencing is decided before an outage, not during the worst hour of one. Each T1 and T2 process has a sequencing record:

1. Confirm safety, legal, and regulatory constraints.
2. Confirm identity, network, logging, and backup platform availability.
3. Restore or fail over platform dependencies.
4. Restore core data stores and integrity checks.
5. Restore application or operational service.
6. Validate security controls: access, logging, encryption, endpoint posture, segmentation, backup protection.
7. Validate business function with the business owner.
8. Approve return to production or degraded operation.
9. Record residual risk and exceptions.
10. Preserve recovery evidence.

A process may resume in degraded mode only when the business owner, Engineering Pillar Leader, Risk Pillar Leader, and CISO or delegate understand the missing controls and approve the risk path.

---

## 6. Crisis Roles and Governance

| **Role** | **Continuity Responsibility** |
|---|---|
| Chief Information Security Officer (CISO) | Receives crisis briefings, approves material cyber risk during recovery, escalates to executive leadership. |
| Governance Pillar Leader | Owns this plan, evidence discipline, and continuity governance reporting. |
| Engineering Pillar Leader | Owns cyber recovery execution, restoration validation, and technical sequencing. |
| Risk Pillar Leader | Owns residual-risk assessment and risk-register entries arising from recovery decisions. |
| Evidence Librarian | Maintains exercise and outage evidence. |
| Risk Register Owner | Records resilience risks, accepted degraded operations, and post-event remediation. |
| Cloud Security Engineer | Supports cloud, SaaS, platform, and tenant recovery. |
| Identity Engineer | Restores and validates identity, MFA, privilege, service accounts, and federation. |
| OT Security Engineer | Supports OT recovery and NERC-CIP implications where applicable. |
| SOX ITGC Lead | Ensures SOX-relevant recovery evidence is retained. |
| CMMC / Federal Compliance Manager | Ensures CUI recovery obligations are addressed. |
| NERC-CIP Compliance Manager | Ensures CIP recovery obligations and evidence are addressed. |

Where an enterprise BCP or crisis-management program names additional roles, those roles remain outside CERG. CERG coordinates through its canonical roles.

---

## 7. Plan Activation and Communications

This plan is activated when an outage, incident, disaster, supplier failure, cyber event, facility issue, or platform failure threatens a T1 or T2 process, or when the CISO, Governance Pillar Leader, Engineering Pillar Leader, or enterprise crisis process requests activation.

Activation record:

- date and time activated;
- activating role and reason;
- affected business process and systems;
- current impact and expected trajectory;
- recovery tier and sequencing priority;
- cyber control state;
- communication cadence;
- recovery decision log;
- risk acceptances or exceptions;
- closure criteria.

Communications use the enterprise crisis communications process where one exists. CERG supplies technical facts, control posture, data classification, regulated-scope facts, recovery evidence, and residual-risk statements.

---

## 8. Disaster Recovery Exercise Program

| **Exercise Type** | **Minimum Cadence** | **Required For** | **Evidence** |
|---|---|---|---|
| Tabletop | Annual | T1 and T2 processes | Scenario, participants, decisions, gaps, actions. |
| Technical restore test | Per `CERG-STD-RES-001` tier | Systems with recoverable state | Restore time, data currency, validation result. |
| Full DR exercise | Annual for T1; at least every two years for T2 where feasible | Mission-critical process chains | End-to-end recovery evidence and lessons learned. |
| Regulated-scope exercise | Per regulator or audit cycle | SOX, CUI, NERC-CIP, and contractual scopes | Control-specific evidence package. |

Exercise findings become risk-register entries or tracked remediation actions. A passed exercise with missing evidence is not a passed exercise for audit purposes.

---

## 9. Evidence and Records

Continuity records are retained under [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md).

| **Evidence Item** | **Required When** |
|---|---|
| BIA record | Every in-scope T1 through T3 business process. |
| Recovery runbook | Every T1 and T2 process. |
| Restore test evidence | Per recovery tier. |
| DR exercise package | Every tabletop, technical exercise, and full DR exercise. |
| Activation record | Every plan activation. |
| Recovery decision log | Every active continuity event. |
| Risk acceptance or exception | Any degraded operation or missing control. |
| Post-event report | Every material outage or exercise. |

---

## 10. Metrics

| **Metric** | **Purpose** |
|---|---|
| T1/T2 processes with current BIA | Measures planning coverage. |
| T1/T2 processes with current recovery runbook | Measures executable readiness. |
| Restore tests completed on schedule | Measures technical recovery discipline. |
| RTO achieved in tests | Measures recovery realism. |
| RPO achieved in tests | Measures data-loss realism. |
| Open recovery gaps by age and severity | Measures remediation backlog. |
| Exercises completed on schedule | Measures governance cadence. |
| Degraded-operation risk acceptances | Measures how often recovery requires control compromise. |

---

## 11. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Plan Responsibility** |
|---|---|
| **Governance Pillar Leader** | Accountable owner for this plan and continuity governance evidence. |
| **Engineering Pillar Leader** | Accountable for cyber recovery execution and restoration validation. |
| **Risk Pillar Leader** | Accountable for residual-risk assessment during recovery. |
| **Evidence Librarian** | Maintains BIA, exercise, activation, and recovery evidence. |
| **Risk Register Owner** | Records recovery gaps, resilience risks, and accepted degraded operations. |
| **Cloud Security Engineer** | Supports platform and SaaS recovery. |
| **Identity Engineer** | Supports identity restoration and access validation. |
| **Endpoint Engineer** | Supports endpoint recovery and device posture validation. |
| **OT Security Engineer** | Supports OT continuity and CIP-009 interfaces. |
| **SOX ITGC Lead** | Ensures financially relevant recovery evidence is audit-ready. |
| **CMMC / Federal Compliance Manager** | Ensures CUI recovery obligations are addressed. |
| **NERC-CIP Compliance Manager** | Ensures NERC-CIP recovery obligations are addressed. |
| **Chief Information Security Officer (CISO)** | Approves material recovery risk acceptance and executive escalation. |

---

## 12. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Plan** |
|---|---|---|
| NIST 800-34r1 | Contingency planning guide | Sections 3 through 9 |
| NIST 800-53r5 | CP, IR, CA | Sections 4, 5, 8, 9 |
| NIST CSF 2.0 | RECOVER | Sections 5, 7, 8 |
| ISO 22301 | Business continuity management | Sections 3, 6, 7, 8 |
| ISO/IEC 27031 | ICT readiness for business continuity | Sections 4, 5, 8 |
| SOX ITGC | Backup, operations, change, evidence | Sections 4, 8, 9 |
| CMMC L2 / 800-171r3 | Contingency and incident response support | Sections 5, 8, 9 |
| NERC-CIP CIP-009 | Recovery plans for BES Cyber Systems | Sections 4, 8, 11 |

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-BC-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO (pending); Enterprise BCP owner concurrence required where applicable |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and after major outage, DR exercise, or business-process change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-34r1; NIST 800-53r5 (CP, IR); NIST CSF 2.0 (RECOVER); ISO 22301; ISO/IEC 27031 |
| **Regulations** | SOX ITGC; CMMC L2 / 800-171r3; NERC-CIP CIP-009 where applicable |
| **Environments** | Business-critical processes, supporting systems, regulated environments, and CERG-managed recovery controls |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes BIA requirements, recovery tiers, recovery sequencing, crisis roles, activation records, DR exercise cadence, continuity evidence, metrics, and the boundary between Enterprise BCP and CERG cyber recovery. |

### Review Triggers

- Major outage or disaster-recovery event
- Material change to business-process criticality
- Material change to recovery tiering or backup architecture
- Failed DR exercise or missed RTO/RPO target
- New regulated-scope recovery requirement
- Direction from the CISO

Cyber Governance owns this plan. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval and Enterprise BCP owner concurrence where applicable.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines canonical roles and CERG boundaries |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control source for continuity and recovery obligations |
| Cyber Resilience and Backup Standard | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Technical recovery and backup standard |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Asset and dependency source |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Data classification and regulated data support |
| Incident Response Plan | [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) | Incident-driven activation interface |
| Incident Response Playbook Set | [`CERG-PRC-IR-002`](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) | CERG incident support playbooks |
| Security Change Management Procedure | [`CERG-PRC-CHG-001`](CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) | Recovery changes and emergency changes |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Residual risk and degraded-operation acceptance |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence retention |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `BC` domain |
