
# SURGE: Cyber Engineering, Risk & Governance

## AUDIT AND EVIDENCE MANAGEMENT PROCEDURE
### Evidence Library · Control Testing · Audit Intake · Auditor Response · Finding Tracking

---

| | |
|---|---|
| **Document ID** | CERG-PRC-AUD-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) · [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) · [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) |
| **Review Cycle** | Annual / After major audit, assessor, or regulator feedback |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CA, PM, AU) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.5, A.8 · CIS Controls v8 |
| **Regulations** | CMMC L2 / 800-171r3 · NERC-CIP · SOX ITGC · privacy and contractual audit obligations where applicable |
| **Environments** | All CERG-managed control evidence, audits, assessments, and regulator or customer requests |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Evidence Library Structure](#3-evidence-library-structure)
4. [Evidence Types and Quality Bar](#4-evidence-types-and-quality-bar)
5. [Evidence Collection Cadence](#5-evidence-collection-cadence)
6. [Control Testing](#6-control-testing)
7. [Audit Intake and Response](#7-audit-intake-and-response)
8. [Findings and Corrective Actions](#8-findings-and-corrective-actions)
9. [Metrics](#9-metrics)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

The README assigns audit response and control evidence to Cyber Governance. The Unified Control Baseline names evidence for controls. The compliance matrix maps intent to frameworks. The operational packages for CUI, NERC-CIP, and SOX depend on durable evidence. What was missing was the operating procedure that tells the organization how evidence is collected, stored, tested, produced to auditors, and tracked when it fails. This procedure provides that machinery.

This procedure governs CERG's evidence library, control-testing cadence, audit intake, evidence production, auditor response, and finding tracking. It applies to every control framework CERG supports and to every audit, assessor request, regulator request, customer security review, and internal control test that depends on CERG evidence.

> **Evidence Is Produced by Running the Program**
>
> CERG does not create evidence by staging screenshots the week before an audit. Evidence is the exhaust of a working program: access reviews completed on schedule, vulnerabilities remediated or accepted, backups tested, keys rotated, risks reviewed, exceptions approved, controls measured. A program that runs well produces evidence naturally. A program that does not run well produces scramble folders.

---

## 2. Principles

1. **Evidence is collected continuously.** Audit readiness is a steady-state operating condition, not a seasonal project.
2. **Evidence maps to controls.** Every retained evidence item maps to at least one control, framework requirement, or audit request.
3. **Evidence is attributable.** Evidence shows who produced it, when, from what system or process, and what period it covers.
4. **Evidence is reproducible.** A reasonable reviewer can understand how the evidence was produced and, where possible, reproduce it.
5. **Evidence is protected.** Evidence often contains sensitive configuration, user, asset, or vulnerability data. It is classified and handled under [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md).
6. **One evidence item can serve many frameworks.** The same access-review record can support CMMC, SOX, ISO, and NIST. CERG collects once and maps many times.

---

## 3. Evidence Library Structure

The Evidence Librarian maintains the evidence library. The exact platform may vary by adopting organization, but the structure is fixed.

```text
/evidence
  /control-baseline
    /<control-id>
      /<YYYY-QN>
  /frameworks
    /cmmc
    /nerc-cip
    /sox-itgc
    /iso-27001
  /audits
    /<audit-or-request-name>
      /requests
      /responses
      /submitted
      /findings
  /metrics
  /exceptions
  /attestations
```

The control-baseline view is the source view. Framework views may link to or reference the same evidence. The audit view contains exactly what was requested, what was submitted, when, and by whom.

> **Collect Once, Map Many Times**
>
> The control does not care which auditor asked the question. Access reviews, backup tests, vulnerability remediation, and risk reviews are real control activity. CERG stores evidence by control first, then maps it to CMMC, NERC-CIP, SOX, ISO, customer questionnaires, or internal audit. That prevents duplicate collection and prevents different audit teams from getting different versions of the truth.

---

## 4. Evidence Types and Quality Bar

### 4.1 Evidence Types

| **Type** | **Examples** |
|---|---|
| System-generated records | Export from identity provider, vulnerability platform, backup system, ticketing system, CI/CD platform, cloud control plane. |
| Approved artifacts | Policies, standards, procedures, plans, risk acceptances, exceptions, architecture reviews. |
| Review records | Access reviews, risk reviews, vendor reviews, control tests, change approvals. |
| Attestations | Signed owner confirmations where system evidence is not available. |
| Meeting records | Agendas, minutes, decision logs, oversight briefings. |
| Test results | Backup restore test, disaster recovery test, control test, adversarial validation, configuration validation. |

### 4.2 Quality Bar

Evidence is acceptable only if it is complete enough to support the control claim. At minimum it shows:

- what control or request it supports;
- what period it covers;
- source system or process;
- date generated or approved;
- owner or approver;
- scope, including included and excluded systems;
- result, decision, or conclusion;
- any exceptions or limitations.

A screenshot without date, scope, and source is weak evidence. A spreadsheet with no source and no owner is weak evidence. A ticket with approval, scope, timestamp, and closure is usually stronger than a polished narrative.

---

## 5. Evidence Collection Cadence

Evidence cadence follows the control's operating cadence. Evidence is not all collected at year-end.

| **Cadence** | **Examples** | **Owner** |
|---|---|---|
| Continuous or event-driven | Change approvals, vulnerability findings, risk entries, security exceptions, incidents handed off to IR. | Process owner. |
| Monthly | Vulnerability posture, risk register review, key metrics, backup-job review where applicable. | Relevant pillar owner. |
| Quarterly | Access reviews, control owner attestations, metric package, evidence completeness review. | Evidence Librarian with control owners. |
| Semiannual | Disaster recovery or restore tests where applicable, privileged-access review if not quarterly. | Relevant Engineering owner. |
| Annual | Policy and standard review, risk assessment, operational package refresh, major control test. | Governance Pillar Leader. |

The Evidence Librarian maintains the evidence calendar and follows up with owners before due dates.

---

## 6. Control Testing

Control testing confirms that a control is not only documented but operating.

### 6.1 Test Plan

Each test plan records:

- control or requirement tested;
- population and sample method, if sampling is used;
- period under review;
- evidence used;
- expected result;
- test steps;
- tester;
- result;
- exceptions and corrective actions.

### 6.2 Testing Outcomes

| **Outcome** | **Meaning** |
|---|---|
| Effective | Evidence supports that the control operated as designed. |
| Effective with observation | Control operated, but improvement is warranted. |
| Deficient | Control did not operate as designed or evidence is insufficient. |
| Not tested | Test could not be completed; reason and next step required. |

Deficient controls create corrective actions under Section 8. A repeated evidence failure is treated as a control failure, not an administrative miss.

---

## 7. Audit Intake and Response

### 7.1 Intake

Every audit, assessor, regulator, customer, or internal evidence request enters through Governance and is recorded in the audit intake log.

Minimum intake fields:

| **Field** | **Purpose** |
|---|---|
| Request name and source | Identifies the audit or request. |
| Framework or obligation | CMMC, NERC-CIP, SOX, customer, internal audit, other. |
| Due date and priority | Drives response planning. |
| Requested evidence | Exact request text. |
| Scope | Systems, controls, period, environment. |
| Owner | Governance role accountable for response. |
| Producing roles | Engineering, Risk, or Governance roles that must supply evidence. |
| Submission status | Open, in review, submitted, accepted, rejected, closed. |

### 7.2 Response Rules

1. **Answer the request asked.** Do not over-produce. Extra evidence creates extra review surface.
2. **Submit through Governance.** Evidence leaves the library through Governance so the organization knows what was provided.
3. **Preserve the submitted set.** The exact package submitted is retained in the audit view, including date and submitter.
4. **Do not alter evidence to satisfy a request.** If the evidence is weak, record the weakness. Manufacturing better-looking evidence is a governance failure.
5. **Escalate ambiguous or broad requests.** Requests with unclear scope or excessive breadth are clarified before production.

> **Do Not Feed the Audit Monster**
>
> Auditors and assessors need evidence, not a data dump. Over-sharing wastes time, creates contradictions, and invites questions that were never in scope. CERG responds precisely: the requested control, the requested period, the requested population, the evidence that proves it, and nothing theatrical. Discipline in evidence production is a security control and a legal hygiene practice.

---

## 8. Findings and Corrective Actions

Audit findings, control-test deficiencies, rejected evidence, and repeated evidence misses are tracked to closure.

| **Finding Type** | **Tracking Path** |
|---|---|
| Control deficiency | Corrective action plan owned by the control owner; risk register entry where residual risk remains. |
| Evidence deficiency | Evidence Librarian opens corrective action with the producing owner. |
| Policy or standard gap | Policy & Standards Manager opens document update action. |
| Technical control gap | Relevant Engineering or Risk owner opens remediation action. |
| Accepted residual risk | Risk Register Owner tracks through [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |

A corrective action records owner, due date, remediation plan, verification method, and closure evidence. Closure requires evidence that the condition was corrected, not merely a statement that it was.

---

## 9. Metrics

Audit and evidence metrics are reported through [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md).

| **Metric** | **Purpose** |
|---|---|
| Evidence completeness by control | Shows which controls are audit-ready. |
| Evidence items overdue | Shows collection discipline. |
| Audit requests open by due date | Shows response workload and urgency. |
| Evidence rejected or returned for rework | Shows evidence quality. |
| Control tests completed on schedule | Shows testing discipline. |
| Deficient controls by severity and age | Shows unresolved control exposure. |
| Corrective actions closed on time | Shows follow-through. |
| Repeat findings | Shows whether the program learns. |

---

## 10. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Audit and Evidence Responsibility** |
|---|---|
| **Governance Pillar Leader** | Accountable for this procedure, audit response, compliance posture, and CISO reporting. |
| **Evidence Librarian** | Operates the evidence library, evidence calendar, evidence completeness review, and submitted-package archive. |
| **Policy & Standards Manager** | Maintains evidence-related document updates and ensures catalog and artifact references remain current. |
| **CMMC / Federal Compliance Manager** | Leads CMMC and CUI evidence mapping and assessor response. |
| **NERC-CIP Compliance Manager** | Leads NERC-CIP evidence mapping and audit response. |
| **SOX ITGC Lead** | Leads SOX ITGC evidence mapping, control testing coordination, and audit response. |
| **Risk Register Owner** | Records residual risks and accepted exceptions arising from audit findings or evidence deficiencies. |
| **Engineering Pillar Leader** | Ensures Engineering control evidence is produced and corrected when deficient. |
| **Risk Pillar Leader** | Ensures Risk control evidence is produced and corrected when deficient. |
| **Chief Information Security Officer (CISO)** | Receives material audit findings, posture reporting, and escalations. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Procedure** |
|---|---|---|
| NIST 800-53r5 | CA, PM, AU families | Sections 3, 4, 6, 8 |
| NIST CSF 2.0 | GOVERN function | Sections 5, 7, 9 |
| ISO/IEC 27001 | A.5 and A.8 evidence and control operation | Sections 3, 6, 8 |
| CMMC L2 / NIST 800-171r3 | Evidence for assessment and POA&M support | Sections 3, 7, 8 |
| NERC-CIP | Compliance evidence, audit response, and finding closure | Sections 3, 7, 8 |
| SOX ITGC | ITGC control evidence and testing | Sections 5, 6, 7 |
| CIS Controls v8 | Control implementation evidence | Sections 3, 6 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-AUD-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and after major audit, assessor, or regulator feedback |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-53r5 (CA, PM, AU); NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.5 and A.8; CIS Controls v8 |
| **Regulations** | CMMC L2 / 800-171r3; NERC-CIP; SOX ITGC; privacy and contractual audit obligations where applicable |
| **Environments** | All CERG-managed control evidence, audits, assessments, and regulator or customer requests |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes the evidence library structure, evidence quality bar, collection cadence, control testing outcomes, audit intake and response rules, finding and corrective-action tracking, metrics, and canonical role responsibilities for audit and evidence management. |

### Review Triggers

- Major audit, assessor, regulator, or customer evidence feedback
- Significant evidence rejection or repeated finding
- Change to CERG operational packages or control baseline
- New framework or regulatory evidence obligation
- Direction from the CISO

Cyber Governance owns this document. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control and evidence source |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Cross-framework mapping |
| Metrics and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Audit and evidence metrics reporting |
| Consolidated Roles, Responsibilities, and RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Role accountability reference |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Residual risk and exception tracking |
| CUI / CMMC Operational Package | [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | CMMC evidence mapping |
| NERC-CIP Operational Package | [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | NERC-CIP evidence mapping |
| SOX ITGC Operational Package | [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | SOX evidence mapping |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `AUD` domain |
