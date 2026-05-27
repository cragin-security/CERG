
# SURGE: Cyber Engineering, Risk & Governance

## ISO/IEC 27001 OPERATIONAL PACKAGE
### ISMS Scope · Statement of Applicability · Annex A Mapping · Internal Audit · Management Review

---

| | |
|---|---|
| **Document ID** | CERG-PLN-ISO-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Documents** | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) · [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) |
| **Supporting Documents** | [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) · [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-PRC-CHG-001`](CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) · [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) · [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) |
| **Review Cycle** | Annual / Per ISO audit cycle / On material ISMS scope change |
| **Frameworks** | ISO/IEC 27001:2022 · ISO/IEC 27002:2022 · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) |
| **Regulations** | Cross-cutting; supports customer assurance and certification readiness |
| **Environments** | ISMS scope selected by the organization; CERG-managed controls and evidence supporting that scope |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [ISMS Boundary](#2-isms-boundary)
3. [ISO 27001 Operating Model](#3-iso-27001-operating-model)
4. [Statement of Applicability](#4-statement-of-applicability)
5. [Annex A Mapping](#5-annex-a-mapping)
6. [Risk Assessment and Treatment Interface](#6-risk-assessment-and-treatment-interface)
7. [Internal Audit Program](#7-internal-audit-program)
8. [Management Review Package](#8-management-review-package)
9. [Certification and External Audit Interface](#9-certification-and-external-audit-interface)
10. [Evidence Library](#10-evidence-library)
11. [Metrics](#11-metrics)
12. [Roles and Responsibilities](#12-roles-and-responsibilities)
13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Scope

CERG already aligns many artifacts to ISO/IEC 27001 and ISO/IEC 27002. Alignment is not the same thing as operating an Information Security Management System. An ISO-ready program needs an ISMS scope, a Statement of Applicability, risk treatment linkage, internal audit, management review, corrective actions, and evidence organized for assessors.

This operational package turns the CERG library into an ISO-operable system. It is designed for organizations seeking formal certification, customer-assurance readiness, or disciplined internal operation against ISO/IEC 27001 without immediate certification.

> **ISO Is a Management System, Not a Control Checklist**
>
> Annex A matters, but certification succeeds or fails on the management system: scope, risk treatment, evidence, internal audit, corrective action, and management review. A control may be technically strong and still fail ISO if the organization cannot show why it is in scope, who owns it, how it is reviewed, and what happens when it fails.

---

## 2. ISMS Boundary

The ISMS scope statement defines what the ISO program covers. It is approved by the CISO and reviewed at least annually.

Minimum scope fields:

| **Field** | **Description** |
|---|---|
| Scope Name | Name of the ISMS scope. |
| Business Processes | Processes included in the ISMS. |
| Locations | Physical and logical locations included. |
| Systems and Assets | Asset classes and key systems included. |
| Data Classes | Highest data classification processed. |
| Exclusions | Areas not in scope and rationale. |
| Interfaces | Dependencies on third parties, shared services, and adjacent programs. |
| Regulatory Drivers | Customer, contractual, or regulatory reasons for the scope. |
| Scope Owner | Accountable owner. |
| Approval Date | Date approved by the CISO or delegated authority. |

A scope exclusion is valid only when it is truthful, documented, and does not hide a control failure. Exclusions are reviewed during internal audit and management review.

---

## 3. ISO 27001 Operating Model

| **ISO Function** | **CERG Mechanism** |
|---|---|
| Context and scope | ISMS scope record in this package. |
| Leadership and policy | `CERG-POL-001` and CISO governance. |
| Risk assessment | `CERG-PRC-RM-001` scoring and risk register. |
| Risk treatment | Risk treatment plans, exceptions, and control ownership. |
| Controls | `CERG-GOV-CB-001` and subordinate standards. |
| Competence and awareness evidence | Evidence from the enterprise awareness program where applicable, not owned by CERG. |
| Communication | Governance reporting and management review package. |
| Documented information | `CERG-GOV-CAT-001` and evidence library. |
| Performance evaluation | `CERG-GOV-MTR-001`, `CERG-GOV-MAT-001`, and internal audit. |
| Internal audit | `CERG-PRC-AUD-001` plus the ISO internal audit schedule. |
| Management review | Section 8 of this package. |
| Nonconformity and corrective action | Audit finding workflow and risk register linkage. |

---

## 4. Statement of Applicability

The Statement of Applicability (SoA) is the authoritative ISO control decision record. It states which Annex A controls apply, why they apply, which CERG artifacts implement them, and whether any control is excluded.

Minimum SoA fields:

| **Field** | **Description** |
|---|---|
| Annex A Control ID | ISO/IEC 27001:2022 Annex A control reference. |
| Control Title | Official or shortened control name. |
| Applicability | Applicable / Not Applicable. |
| Applicability Rationale | Why the control applies or does not apply. |
| Implementation Status | Implemented / Partially Implemented / Planned / Not Implemented. |
| CERG Control Source | CERG artifact and section implementing the control. |
| Evidence Source | Evidence library folder, report, or record. |
| Control Owner | Canonical CERG role or business owner. |
| Risks Linked | Risk-register IDs, if applicable. |
| Last Reviewed | Review date. |

> **A Bad SoA Is Worse Than No SoA**
>
> A copied SoA that says every control applies and everything is implemented tells the auditor the program has not done real scoping. A useful SoA makes decisions visible: what applies, what does not, why, who owns it, and what evidence proves the claim.

---

## 5. Annex A Mapping

The mapping below is the starting spine. The maintained SoA provides row-level detail.

| **Annex A Theme** | **CERG Implementation Sources** |
|---|---|
| Organizational controls | `CERG-POL-001`, `CERG-GOV-OM-001`, `CERG-GOV-CB-001`, `CERG-GOV-RAC-001`, `CERG-PRC-RM-001`, `CERG-PRC-AUD-001`, `CERG-PRC-TPRM-001` |
| People controls | Enterprise HR and awareness programs supply evidence; CERG records interfaces where controls affect privileged access, exceptions, and training-dependent control claims. |
| Physical controls | Enterprise physical security supplies evidence; CERG records physical dependencies for data centers, OT, and backup media where applicable. |
| Technological controls | `CERG-STD-IT-001`, `CERG-STD-OT-001`, `CERG-STD-AC-001`, `CERG-STD-CFG-001`, `CERG-STD-LM-001`, `CERG-STD-RES-001`, `CERG-STD-CR-001`, `CERG-STD-SDL-001`, `CERG-STD-DG-001`, `CERG-STD-MSG-001`, `CERG-STD-AI-001` |

Controls owned outside CERG are not ignored. They are listed in the SoA with the external evidence owner and the CERG dependency clearly stated.

---

## 6. Risk Assessment and Treatment Interface

ISO risk treatment uses the CERG risk register rather than a parallel ISO-only risk log. ISO-specific risk requirements are met by ensuring each ISMS-scope risk includes:

- risk statement;
- asset or process scope;
- likelihood, impact, and rating;
- selected treatment;
- treatment owner;
- target date;
- linked Annex A controls;
- linked SoA row;
- residual risk decision;
- approver;
- review date.

Risk treatment decisions that leave a control gap use `CERG-PRC-RM-001` exception or acceptance workflow.

---

## 7. Internal Audit Program

The ISO internal audit program uses `CERG-PRC-AUD-001` and adds ISO-specific scope and independence rules.

Minimum audit schedule:

| **Audit Area** | **Minimum Cadence** |
|---|---|
| ISMS scope and context | Annual |
| SoA accuracy | Annual |
| Risk assessment and treatment | Annual |
| Evidence library and documented information | Annual |
| Selected Annex A controls | Risk-based rotation; all applicable themes covered over the certification cycle |
| Corrective action closure | Quarterly until closed |

Internal auditors must be independent of the control operation being audited. In small organizations, independence may mean cross-pillar review, external reviewer support, or documented CISO-approved independence constraints.

---

## 8. Management Review Package

Management review is held at least annually and before certification or surveillance audits.

Management review package contents:

1. ISMS scope changes.
2. Internal audit results.
3. External audit findings.
4. Risk posture and material risk changes.
5. SoA changes and exclusions.
6. Control performance metrics.
7. Corrective action status.
8. Supplier and third-party security issues.
9. Incident and continuity lessons.
10. Resource constraints and improvement needs.
11. Decisions and assigned actions.

Management review minutes are retained as evidence. Decisions that create work become tracked actions, risk-register entries, or cataloged document updates.

---

## 9. Certification and External Audit Interface

For certification readiness, Governance maintains an audit pack:

- ISMS scope statement;
- information security policy;
- SoA;
- risk assessment and treatment records;
- internal audit schedule and results;
- management review records;
- corrective action register;
- evidence index mapped to Annex A;
- document catalog and version record;
- list of exclusions and interfaces owned outside CERG.

External auditor requests are handled through `CERG-PRC-AUD-001`. Auditor observations that indicate control weakness become findings or risks, not side emails.

---

## 10. Evidence Library

Evidence is organized by ISO requirement and by CERG control source.

| **Folder / Index** | **Contents** |
|---|---|
| 01 Scope and Context | Scope statement, boundaries, exclusions, interested parties. |
| 02 Policy and Governance | Policy, operating model, RACI, catalog. |
| 03 Risk Assessment and Treatment | Risk methodology, register extracts, treatment plans, acceptances. |
| 04 Statement of Applicability | SoA, change history, rationale records. |
| 05 Annex A Evidence | Control evidence indexed by Annex A control. |
| 06 Internal Audit | Audit plans, test sheets, findings, corrective actions. |
| 07 Management Review | Agendas, decks, minutes, decisions, action register. |
| 08 External Audit | Auditor requests, evidence provided, findings, responses. |
| 09 Corrective Actions | Nonconformities, root cause, action plans, closure evidence. |

---

## 11. Metrics

| **Metric** | **Purpose** |
|---|---|
| Applicable Annex A controls with current owner | Measures SoA ownership quality. |
| Applicable Annex A controls with current evidence | Measures audit readiness. |
| SoA rows reviewed on schedule | Measures SoA hygiene. |
| Open ISO nonconformities by age | Measures corrective-action performance. |
| Internal audits completed on schedule | Measures audit program execution. |
| Risk treatments overdue in ISMS scope | Measures risk-treatment discipline. |
| Management review actions overdue | Measures leadership follow-through. |
| External audit repeat findings | Measures systemic weakness. |

---

## 12. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **ISO Responsibility** |
|---|---|
| **Governance Pillar Leader** | Accountable owner for this package, ISMS governance, SoA maintenance, internal audit coordination, and management review package. |
| **Policy & Standards Manager** | Maintains documented information and updates CERG artifacts that implement ISO controls. |
| **Evidence Librarian** | Maintains ISO evidence library and audit pack. |
| **Risk Pillar Leader** | Ensures ISO risk assessment and treatment use the CERG risk process. |
| **Risk Register Owner** | Maintains risk-register entries, treatments, acceptances, and review dates for ISMS-scope risks. |
| **Engineering Pillar Leader** | Owns implementation evidence for technical controls. |
| **Vendor Risk Analyst** | Supplies third-party evidence and supplier-risk inputs. |
| **SOX ITGC Lead** | Coordinates reusable evidence where ISO and SOX overlap. |
| **CMMC / Federal Compliance Manager** | Coordinates reusable evidence where ISO and CUI/CMMC overlap. |
| **NERC-CIP Compliance Manager** | Coordinates reusable evidence where ISO and CIP overlap. |
| **Chief Information Security Officer (CISO)** | Approves ISMS scope, accepts material residual risk, and chairs or delegates management review. |

---

## 13. Regulatory and Framework Alignment Summary

| **Framework** | **Reference** | **Where in This Package** |
|---|---|---|
| ISO/IEC 27001:2022 | Clauses 4 through 10 | Sections 2 through 10 |
| ISO/IEC 27001:2022 | Annex A | Sections 4, 5, 10 |
| ISO/IEC 27002:2022 | Control implementation guidance | Sections 4, 5, 10 |
| NIST CSF 2.0 | GOVERN | Sections 2, 3, 8, 11 |
| NIST 800-53r5 | Crosswalk source for controls | Sections 5, 10 |
| Customer assurance | ISO evidence pack | Sections 9, 10 |

---

## 14. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-ISO-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; per ISO audit cycle; and on material ISMS scope change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | ISO/IEC 27001:2022; ISO/IEC 27002:2022; NIST CSF 2.0; NIST 800-53r5 |
| **Regulations** | Cross-cutting; supports customer assurance and certification readiness |
| **Environments** | ISMS scope selected by the organization; CERG-managed controls and evidence supporting that scope |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes ISMS scope requirements, ISO operating model, Statement of Applicability structure, Annex A mapping, risk-treatment interface, internal audit program, management review package, certification audit interface, evidence library, metrics, and canonical role responsibilities. |

### Review Triggers

- Material ISMS scope change
- ISO certification, surveillance, or recertification audit
- Material SoA change or control exclusion
- Major internal audit finding or external nonconformity
- Management review direction
- Direction from the CISO

Cyber Governance owns this package. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control source for ISO mapping |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Framework crosswalk source |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `ISO` domain |
| Maturity Self-Assessment and Scorecard | [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | Maturity evidence and measurement |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence and audit process |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk treatment and acceptance process |
| Security Change Management Procedure | [`CERG-PRC-CHG-001`](CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) | Change-control evidence and corrective action support |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Asset and scope evidence |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Information classification and handling evidence |
