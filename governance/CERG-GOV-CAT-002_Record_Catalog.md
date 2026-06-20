## RECORD CATALOG
### Authoritative Record Types · Required Fields · Evidence Value

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-002 |
| **Version** | 1.2 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly / Upon new procedure or record type |
| **Frameworks** | NIST CSF 2.0 (GOVERN) · NIST 800-53r5 CA, PL, PM |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed records and evidence stores |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Record Principles](#2-record-principles)
3. [Minimum Required Fields](#3-minimum-required-fields)
4. [Authoritative Record Catalog](#4-authoritative-record-catalog)
5. [Minimum Viable Evidence Library](#5-minimum-viable-evidence-library)
6. [Record Storage and Tooling Patterns](#6-record-storage-and-tooling-patterns)
7. [Record Quality Checks](#7-record-quality-checks)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

CERG procedures create records. Records become evidence. Evidence supports metrics, oversight, audits, and risk decisions.

This catalog defines the canonical record types a CERG implementation should maintain. It prevents a common adoption failure: performing security work but losing the proof, ownership, decision trail, or closure evidence.

This document applies to all CERG adopters. Small teams may maintain these records in spreadsheets. Larger teams may maintain them in GRC platforms, ticketing systems, CMDBs, repositories, or evidence platforms. The tool may change. The required record attributes do not.

---

## 2. Record Principles

1. **Every record has an owner.** Shared awareness is not ownership.
2. **Every record has a state.** Open, approved, accepted, closed, superseded, or retired must be visible.
2a. **Canonical names win over local aliases.** Teams may use local ticket names, queue names, or tool object names, but reporting, evidence indexes, and cross-references must map those aliases back to the canonical record types in §4.
3. **Every record has evidence.** The evidence may be lightweight, but it must exist.
4. **Every risk decision is explicit.** Silence is not acceptance.
5. **Every exception expires.** Permanent exceptions are risk acceptances or control changes.
6. **Every record can be traced.** A record should link to the policy, standard, procedure, control, system, asset, or decision that caused it.
7. **Every metric has a source record.** Dashboard values must be reproducible from records.

---

## 3. Minimum Required Fields

Every CERG record should include these fields unless the source procedure explicitly narrows them.

| Field | Purpose |
|---|---|
| Record ID | Stable identifier unique within the record type |
| Record type | One of the catalog types in §4; aliases must map back to this value |
| Title | Human-readable summary |
| Description | What happened, what is required, or what decision is needed |
| Owner | Role accountable for action or decision |
| Supporting roles | Roles that must provide input or evidence |
| Pillar | Engineering, Risk, Governance, CISO, or cross-pillar |
| Related asset / system / vendor / project | Scope anchor |
| Related control / standard / procedure | Governance anchor |
| Severity / priority | Triage value where applicable |
| Status | Current lifecycle state |
| Open date | When the record was created |
| Due date / review date | When action, review, or expiration is required |
| Decision | Approved, rejected, accepted, deferred, remediated, or not applicable where applicable |
| Decision date | Date the current decision was recorded where a decision is required |
| Evidence link | Pointer to supporting evidence |
| Last validated date | Date the record was last validated against operational reality, evidence, owner, and control/risk state |
| Closure rationale | Why the record is closed or no longer active |
| Last updated | Date of most recent material change |

---

## 4. Authoritative Record Catalog

The record names in this section are authoritative. Other CERG documents may use local operational wording such as "ticket," "case," "register entry," "memo," "worksheet," or "backlog item," but those terms are aliases unless they appear as a canonical record type below. When a procedure, flow, template, example, or tool uses an alias, it must preserve the CAT-002 canonical record type in metadata, tags, evidence index, or cross-reference.

### 4.0 Common Alias Map

| Canonical record type | Common aliases / local names | Alias rule |
|---|---|---|
| Control Implementation Record | Control Change Record, control implementation row, control status record, control snapshot | Use canonical name for control-baseline evidence and reporting. |
| Evidence Index Entry | Evidence record, evidence library row, evidence package index | The artifact may be evidence; the index entry is the cataloged record. |
| Program Improvement Record | Improvement Record, improvement backlog item, lessons-learned action | Use Program Improvement Record when the item changes CERG process, control, metric, or cadence. |
| Risk Register Entry | Risk Record, risk register row, risk item | `Risk Record` is allowed as shorthand in flows; evidence indexes should map it to Risk Register Entry. |
| Security Exception Record | Exception Record, deviation record, waiver ticket | `Waiver` and `deviation` are local aliases only; the canonical CERG record is Security Exception Record. |
| Risk Acceptance Record | Risk acceptance memo, accepted-risk entry, acceptance request | `TMPL-RM-004` is the required acceptance form; `TMPL-RM-003` may support it but does not replace it. |
| Finding Record | Finding ticket, vulnerability ticket, exposure item, audit finding | Raw scanner output becomes a Finding Record only after triage/validation. |
| Exposure Backlog Item | Vulnerability backlog row, scanner observation, exposure ticket | Use for PRC-VM exposure workflow; promote to Finding Record or Risk Register Entry when criteria are met. |
| Project Security Review Record | Project Intake Record, Architecture Review Record, security review ticket | Intake and architecture-review tools may split the workflow; the evidence package maps to this canonical record. |
| Security Change Review Record | Change Record, security impact assessment, release security review | `Change Record` is acceptable shorthand where the change system is the source of truth. |
| Asset Inventory Record | Asset Record, CMDB item, system inventory row | Local CMDB object names must preserve owner, classification, criticality, and coverage status. |
| System Control Profile Record | SCP, system control profile, per-system control profile, SSP control implementation extract | Use for per-system or per-system-class control implementation, evidence, validation, and review state. It supports but does not replace regulated SSPs, POA&Ms, or CIP evidence packages. |
| Incident Record | IR ticket, incident case, security incident record | Owned by the standing IR team; CERG support evidence links to, but does not replace, this record. |
| Lessons Learned Record | Post-incident action, after-action item, PIR finding | Use Program Improvement Record when the lesson changes the CERG program. |

### 4.1 Governance and program records

| Record type | Primary owner | Created by | Required when | Evidence value |
|---|---|---|---|---|
| Organization Adaptation Profile | Governance Pillar Leader | [VAR-001](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | First adoption and material organizational change | Proves scope, regulators, tailoring decisions, and role consolidation |
| Role Assignment Map | CISO / Governance Pillar Leader | [OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md), [RAC-001](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | First adoption and role change | Proves accountability for canonical CERG roles |
| Document Catalog Entry | Governance Pillar Leader | [CAT-001](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | New, changed, retired, or superseded artifact | Proves document authority and status |
| Control Implementation Record | Governance Pillar Leader | [CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md), FLOW F-01 | Control baseline adoption or control change | Proves implementation status, owner, inheritance, and evidence |
| Evidence Index Entry | Evidence Librarian | [AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md), [PRC-AUD-001](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence is collected or refreshed | Proves evidence location, quality tier, source, and period |
| Program Improvement Record | Governance Pillar Leader | [IMPREG-001](CERG-GOV-IMPREG-001_Program_Improvement_Register.md), FLOW F-07 | Lesson, metric miss, audit issue, maturity gap, or recurring failure | Proves the program learns and changes |
| Oversight Decision Record | CISO / COG Chair | [MTR-001](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Board, CISO, or COG decision | Proves executive risk and resource decisions |
| Maturity Assessment Record | Governance Pillar Leader | [MAT-001](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | Annual assessment or quarterly checkpoint | Proves maturity tier, gaps, and resulting work |

### 4.2 Risk records

| Record type | Primary owner | Created by | Required when | Evidence value |
|---|---|---|---|---|
| Risk Register Entry | Risk Register Owner | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md), [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Material cybersecurity risk is identified | Proves risk statement, scoring, treatment, owner, and status |
| Security Exception Record | Risk Register Owner | [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), [TMPL-RM-002](../templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md) | Temporary deviation from a policy, standard, or control | Proves temporary approval, compensating controls, expiration, and owner |
| Risk Acceptance Record | Business Owner / Executive Sponsor with Risk Register Owner | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md), [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), [TMPL-RM-004](../templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md) | Residual risk is formally accepted under RMF-001 §9.7 | Proves explicit business consequence acceptance, CISO approval where required, conditions, expiration, and review cadence |
| Finding Record | Exposure Management Lead / relevant Risk owner | FLOW F-04, [PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Vulnerability, audit issue, test result, control gap, or observation is validated | Proves triage, severity, ownership, and disposition |
| Exposure Backlog Item | Exposure Management Lead | [PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Vulnerability requires tracking to remediation or exception | Proves remediation status and SLA performance |
| Threat Intelligence Record | Threat Intelligence Analyst | [PRC-TI-001](../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) | Intelligence changes risk, detection, or prioritization | Proves source, relevance, action, and disposition |
| Adversarial Validation Record | Adversarial Testing Lead | [PRC-AV-001](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Penetration test, red team, purple team, or validation exercise occurs | Proves test scope, findings, detection results, and remediation |
| Vendor Risk Assessment Record | Vendor Risk Analyst | [PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor, SaaS, MSP, subprocessors, or supply-chain dependency is assessed | Proves tiering, security review, contractual requirements, and decision |
| Edge Register Entry | Vendor Risk Analyst / Governance Pillar Leader | [EDG-001](CERG-GOV-EDG-001_Edge_Register.md) | Boundary exists where third-party control can affect posture | Proves external dependency, owner, monitoring, and control path |
| Crown Jewel Scenario Record | Risk Pillar Leader | [CJ-001](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md) | Crown jewel or material loss scenario is identified | Proves top-down risk context and scenario-driven prioritization |

### 4.3 Engineering records

| Record type | Primary owner | Created by | Required when | Evidence value |
|---|---|---|---|---|
| Project Security Review Record | Pre-production Reviewer / Security Architecture | [PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md), FLOW F-02 | New project, material change, SaaS adoption, cloud workload, app, or OT change | Proves review tier, requirements, decision, and handoff |
| Approved Pattern Record | Engineering Pillar Leader / pattern owner | [PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) §4.5 | Reference architecture, IaC module, service-catalog template, SaaS configuration, citizen-dev guardrail, or pipeline profile is approved for reuse | Proves approved scope, required controls, evidence, limitations, review date, and triggers for re-review |
| Threat Model Record | Risk / Engineering jointly | [PRC-TM-001](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Review tier requires threat modeling | Proves threats, misuse cases, mitigations, and residual risk |
| Asset Inventory Record | Asset owner / Engineering | [STD-AM-001](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md), FLOW F-03 | Asset enters, changes, or leaves scope | Proves asset existence, classification, owner, and lifecycle |
| Asset Coverage Record | Engineering Pillar Leader | FLOW F-03 | Asset needs coverage for logging, scanning, backup, endpoint, identity, or monitoring | Proves required security coverage exists or is exceptioned |
| System Control Profile Record | System Owner / Engineering Pillar Leader | [TMPL-SCP-001](../templates/CERG-TMPL-SCP-001_System_Control_Profile_Template.md), [CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md), [TRC-001](CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) | A system or system class needs a consolidated control implementation, evidence, last-validation, and next-review profile | Proves per-system control implementation, evidence linkage, residual condition, and review state; supports SSP, NERC-CIP, SOX, and audit assertions |
| Configuration Baseline Record | Platform / Endpoint / Cloud Engineer | [STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Baseline is created, changed, tested, or applied | Proves approved configuration and drift management |
| Security Change Review Record | Engineering Pillar Leader | [PRC-CHG-001](../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md), FLOW F-05 | Change may affect security posture | Proves security review, decision, and release condition |
| Access Review Record | Identity Engineer / Governance | [STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md), [PRC-AC-002](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) | Scheduled recertification or privileged access review occurs | Proves entitlement review and corrective actions |
| Backup and Recovery Test Record | Engineering / Resilience owner | [STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md), [PLN-BC-001](../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md) | Backup, restore, DR, or cyber recovery test occurs | Proves recoverability and restoration evidence |
| Detection Coverage Record | Detection Engineer | [STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | New detection, data source, or ATT&CK coverage claim is created | Proves monitoring coverage and validation status |

### 4.4 Incident and continuity records

| Record type | Primary owner | Created by | Required when | Evidence value |
|---|---|---|---|---|
| Incident Record | Incident Commander | [PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | Security incident is declared | Proves timeline, decisions, containment, eradication, and recovery |
| Incident Action Log | Incident Commander | [PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md), [PRC-IR-002](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) | Incident response is active | Proves actions, owners, timestamps, and communications |
| Lessons Learned Record | Governance Pillar Leader | [PRC-LL-001](../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md), FLOW F-06 | Incident, tabletop, audit, test, or failed control produces learning | Proves cause, corrective action, owner, and program feedback |
| Business Continuity Exercise Record | Business Continuity owner / Governance | [PLN-BC-001](../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md) | BCDR exercise or tabletop occurs | Proves resilience exercise and improvement actions |

### 4.5 Regulatory package records

| Record type | Primary owner | Created by | Required when | Evidence value |
|---|---|---|---|---|
| System Security Plan | CMMC / Federal Compliance Manager | [PLN-CUI-001](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md), [TMPL-CUI-001](../templates/CERG-TMPL-CUI-001_System_Security_Plan_Template.md) | CUI / FCI environment is in scope | Proves system boundary, control implementation, and inheritance |
| POA&M Item | CMMC / Federal Compliance Manager | [TMPL-CUI-002](../templates/CERG-TMPL-CUI-002_POAM_Template.md) | CUI control gap requires tracked correction | Proves remediation plan and status |
| NERC-CIP Evidence Record | NERC-CIP Compliance Manager | [PLN-CIP-001](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | NERC-CIP requirement applies | Proves requirement-specific compliance evidence |
| SOX ITGC Test Record | SOX ITGC Lead | [PLN-SOX-001](../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | SOX-relevant control is tested | Proves test design, sample, exception, and conclusion |
| ISO ISMS Record | Governance Pillar Leader | [PLN-ISO-001](../plans/CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md) | ISO 27001 readiness or certification is in scope | Proves ISMS scope, control applicability, and management review |
| Privacy Security Support Record | Governance / Privacy interface owner | [PLN-PRIV-001](../plans/CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md) | Privacy, data protection, or data-subject process needs security support | Proves security contribution to privacy obligations |

---

## 5. Minimum Viable Evidence Library

### 5.1 CERG Lite

A small-team implementation should be able to produce at least:

1. Signed cybersecurity policy.
2. Organization Adaptation Profile.
3. Role Assignment Map.
4. Asset inventory extract.
5. Initial top risks in the risk register.
6. Exposure backlog.
7. Exception register, even if empty.
8. Evidence index.
9. Control implementation snapshot.
10. Regulatory applicability decision.
11. First 30-day improvement backlog.
12. Access review evidence for the highest-risk identity groups.
13. Backup or restore test evidence for the most critical system.

### 5.2 CERG Standard

A standard implementation adds:

- Project security review records.
- Vendor risk assessment records.
- Security change review records.
- Configuration baseline records.
- Detection coverage records.
- Quarterly metrics dashboard.
- Quarterly oversight decision records.
- Annual maturity assessment record.

### 5.3 CERG Regulated

A regulated implementation adds the applicable package records:

- SSP and POA&M for CUI / CMMC.
- NERC-CIP evidence records for applicable requirements.
- SOX ITGC test records for SOX-relevant systems.
- ISO ISMS records for ISO certification or readiness.
- Privacy security support records where privacy obligations apply.

---

## 6. Record Storage and Tooling Patterns

| Pattern | Acceptable for | Minimum condition |
|---|---|---|
| Spreadsheet | CERG Lite, first 90 days, low-complexity teams | Stable IDs, owners, dates, status, evidence links, access control |
| Ticketing system | Findings, vulnerabilities, exceptions, changes, improvements | Required fields preserved and reports exportable |
| GRC platform | Controls, risks, evidence, regulatory packages | Cross-links preserved between controls, risks, evidence, and owners |
| Git repository | Policies, standards, procedures, templates, decision records | Version history, review workflow, and sensitive evidence kept out of public repos |
| Evidence platform / document library | Audit evidence and recurring exports | Retention, access control, period labeling, and source integrity |

Tool choice must not remove required CERG fields. If the tool cannot represent a required field, the implementation must add a custom field, tag, linked record, or evidence note.

---

## 7. Record Quality Checks

A record is not complete unless it passes these checks:

| Check | Question |
|---|---|
| Ownership | Is one role accountable? |
| Scope | Is the affected system, asset, vendor, project, control, or process clear? |
| Decision | Is the decision explicit where one is required? |
| Evidence | Is supporting evidence linked and readable? |
| Date discipline | Are open date, due date, expiration date, or review date present? |
| Traceability | Can the record be traced to the relevant policy, standard, procedure, or flow? |
| Closure | If closed, is the closure rationale documented? |
| Metric impact | If the record feeds a metric, can the metric be recalculated from the record? |

---

## 8. Document Control

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-002 |
| **Version** | 1.2 |
| **Status** | Approved |
| **Approved By** | CISO |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Next Review** | Quarterly / Upon new procedure or record type |

### Revision History

| **Version** | **Date** | **Author** | **Change** |
|---|---|---|---|
| 1.2 | 2026-06-20 | Governance Pillar Leader | Added System Control Profile Record, minimum decision/validation fields supporting Definition of Done, and SCP alias discipline. |
| 1.1 | 2026-06-18 | Governance Pillar Leader | Added canonical record-name and alias discipline, common alias map, and aligned risk acceptance records to RMF-001 §9.7 and TMPL-RM-004. |
| 1.0 | 2026-06-13 | Governance Pillar Leader | Initial publication. Establishes the authoritative CERG record catalog, minimum required fields, and minimum viable evidence library. |

### Review Triggers

- New procedure creates or retires a record type.
- New operational package creates regulatory records.
- Audit feedback identifies missing or inconsistent records.
- Metrics cannot be reproduced from source records.
- Tooling migration changes record storage.

### Related Documents

- [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) - Document Catalog and Naming Convention
- [CERG-GOV-FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) - Cross-Pillar Operational Flows
- [CERG-GOV-AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) - Evidence Quality Standard
- [CERG-PRC-AUD-001](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) - Audit and Evidence Management Procedure
- [CERG-GOV-MTR-001](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) - Metrics and Reporting
