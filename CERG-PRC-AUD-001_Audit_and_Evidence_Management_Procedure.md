# SURGE: Cyber Engineering, Risk & Governance

## AUDIT AND EVIDENCE MANAGEMENT PROCEDURE
### Evidence Library · Control Testing · Audit Intake · Auditor Response · Finding Tracking

---

| | |
|---|---|
| **Document ID** | CERG-PRC-AUD-001 |
| **Version** | 1.0 |
| **Status** | Published |
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

### 4.3 Evidence Retention

Evidence is retained according to the following schedule. Retention periods are driven by the most stringent applicable regulatory requirement for that evidence type.

| **Evidence Type** | **Minimum Retention** | **Regulatory Driver** | **Disposition After Retention** |
|---|---|---|---|
| SOX ITGC evidence (access reviews, change approvals, control tests) | 7 years | SOX (SEC 17 CFR 210.2-06) | Secure deletion; certificate of destruction |
| CMMC / NIST 800-171 assessment evidence | 3 years | CMMC (32 CFR 170); DFARS 252.204-7012 | Secure deletion |
| NERC-CIP compliance evidence | 3–5 years (audit cycle + 1) | NERC-CIP (CIP-003 R2); NERC Rules of Procedure | Secure deletion |
| General control evidence (non-regulated) | 3 years | ISO 27001, organizational policy | Secure deletion |
| Incident response evidence | 7 years or duration of legal hold | Litigation hold; breach notification statutes | Secure deletion after legal hold release |
| Risk register history | Permanently (append-only) | NIST RMF; organizational policy | Not disposed; append-only audit trail |

#### Disposal Process

1. **Trigger**: Evidence retention period expired, system decommissioned, or legal hold released.
2. **Authorization**: Evidence Librarian confirms no active audit, investigation, or legal hold referencing the evidence. Governance Pillar Leader authorizes disposal.
3. **Disposal Method**: Evidence is securely deleted using methods appropriate to the storage medium (cryptographic erasure for cloud storage, secure overwrite for on-premises, physical destruction for removable media). A certificate of destruction is produced and retained.
4. **Logging**: Disposal is recorded in the evidence library audit log including: evidence ID, disposal date, authorizing party, method, and certificate of destruction reference.

> **Legal Hold Supersedes Retention Schedule**
>
> When a legal hold is in effect, evidence subject to the hold is preserved regardless of the retention schedule. The Evidence Librarian coordinates with Legal to identify and preserve evidence subject to hold, and disposal is suspended until Legal releases the hold in writing.

### 4.4 Evidence Integrity and Chain of Custody

Evidence must be protected from tampering, loss, or unauthorized modification throughout its lifecycle. The integrity of evidence is foundational to audit credibility and, in some cases, legal defensibility.

#### Integrity Controls

| **Control** | **Requirement** | **Implementation** |
|---|---|---|
| Checksums / hashes | Every evidence artifact is hashed (SHA-256 minimum) at ingestion | Evidence library computes and stores hash at upload; hash is verified on retrieval |
| Write-once / append-only storage | Evidence, once ingested, cannot be modified | Evidence library implements immutable storage or legal-hold policies on the underlying storage platform |
| Tamper detection | Any modification or hash mismatch generates an alert | Evidence library compares stored hash against current hash on access; mismatches trigger Evidence Librarian and Governance investigation |
| Access logging | Every access to evidence (read, copy, export) is logged | Evidence library records: who, what, when, source IP, and purpose |
| Retention of original format | Evidence is retained in its original format; exports or transforms are stored alongside, not replacing, the original | Evidence library preserves original file; derived views (PDF exports, screenshots) are linked as supplementary |

#### Chain of Custody

| **Event** | **Documentation Required** |
|---|---|
| Ingestion | Evidence ID, source system, date ingested, hash, ingested by, control(s) supported |
| Access / retrieval | Evidence ID, accessed by, date, purpose (audit response, control test, investigation) |
| Transfer (to auditor, assessor, legal) | Evidence ID(s), recipient, date transferred, transfer method, hash verification at transfer |
| Return / re-ingestion | Evidence ID(s), returned by, date, hash verified against original |
| Disposal | Evidence ID, date, method, authorized by, certificate reference |

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

### 6.2 Sampling Methodology

Sampling is used when testing the full population is infeasible due to volume or cost. The objective is to draw conclusions about the population with a defined confidence level.

#### When Sampling Is Appropriate

| **Condition** | **Use Sampling** | **Use Full Population** |
|---|---|---|
| Population size < 50 items | No — test all | Yes |
| Population size 50–250 items | Yes, with minimum sample per table below | Optional |
| Population size > 250 items | Yes | Only if automated or required by regulation |
| Control is automated and fully logged | No — test all programmatically | Yes |
| SOX ITGC key control | Consult SOX ITGC Lead | Often full population |
| CMMC assessment sample | Per CMMC Assessment Guide sampling guidance | Per assessor direction |

#### Minimum Sample Sizes

| **Population Size** | **Minimum Sample (95% confidence, 5% margin)** | **Recommended Sample** |
|---|---|---|
| 50–100 | 45 | 50 |
| 101–250 | 70 | 80 |
| 251–500 | 80 | 100 |
| 501–1,000 | 90 | 120 |
| 1,001–5,000 | 95 | 150 |
| > 5,000 | 100 | 200 |

#### Selection Methods

| **Method** | **When to Use** | **Description** |
|---|---|---|
| Random | Default for most control tests | Items selected using a random number generator or equivalent; every item has equal probability of selection |
| Stratified | When sub-populations have different risk profiles | Population divided into strata (e.g., by environment, by asset tier); random samples drawn from each stratum proportionally |
| Judgmental | When specific items carry disproportionate risk | Tester selects items based on risk criteria (e.g., highest-value transactions, privileged accounts, changes touching regulated scope); rationale must be documented |
| Haphazard | Not recommended | Avoid; lacks statistical basis and is difficult to defend to an auditor |

#### Documentation Requirements

Every sampling decision records:

- Population definition and size
- Sampling method and rationale
- Sample size and how it was determined
- Selection method (including seed or tool used for random selection)
- Confidence level target
- Limitations or caveats

### 6.3 Testing Outcomes

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

### 8.1 Plan of Action and Milestones (POA&M)

A Plan of Action and Milestones (POA&M) is the formal artifact for tracking and resolving control deficiencies, particularly those affecting CMMC assessment posture. POA&M requirements derive from NIST 800-171 and CMMC assessment guidance.

#### When a POA&M Is Required

A POA&M entry is required for:

- Any CMMC assessment finding (regardless of score impact)
- Any control rated "Deficient" in a control test affecting a CUI environment
- Any control gap identified during a formal CMMC assessment, self-assessment, or pre-assessment
- Any finding from a regulator, customer, or internal audit that maps to a CMMC practice
- Significant findings (Critical or High) in non-CMMC environments, at the CISO's direction

#### POA&M Required Fields

| **Field** | **Description** |
|---|---|
| POA&M ID | Unique identifier (POAM-YYYY-NNNN) |
| Weakness Description | Clear description of the control deficiency or finding |
| Affected CMMC Practice(s) | Reference to specific CMMC practices (e.g., AC.L2-3.1.1) |
| Severity | Finding severity (Critical / High / Medium / Low) |
| Remediation Plan | Specific actions to close the deficiency, with milestones |
| Milestones | Discrete, measurable steps with target dates |
| Responsible Party | Named individual accountable for each milestone |
| Resources Required | Funding, staffing, tooling, or external support needed |
| Scheduled Completion Date | Target date for full remediation |
| Actual Completion Date | Date the deficiency was resolved |
| Status | Open / In Progress / Completed / Deferred |
| Disposition | How the finding was resolved (remediated, risk-accepted, control changed) |
| Evidence of Closure | Reference to evidence demonstrating the deficiency is resolved |
| Last Updated | Date of most recent status update |

#### POA&M Tracking and Status Updates

- POA&M entries are reviewed monthly by the CMMC / Federal Compliance Manager
- Status updates are recorded in the POA&M at each milestone or at minimum quarterly
- Overdue milestones are escalated to the Governance Pillar Leader
- The CISO reviews the full POA&M at the quarterly CISO-level risk review

#### POA&M Closure Criteria

A POA&M entry may be closed when:

1. The deficiency has been remediated and closure evidence is on file, OR
2. The deficiency has been formally risk-accepted through [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) with CISO approval, OR
3. The affected system has been decommissioned and the deficiency is no longer applicable

Closure requires sign-off by the CMMC / Federal Compliance Manager and the Governance Pillar Leader. Closure evidence is retained in the evidence library per Section 4.3.

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
| **Status** | Published |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
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