
# SURGE: Cyber Engineering, Risk & Governance

## CONTROL EVIDENCE AND TEST WORKSHEET
### Control Objective · Sample · Test Steps · Evidence Quality · Result

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-AUD-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Evidence Librarian |
| **Parent Document** | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) - Audit and Evidence Management Procedure |
| **Supporting Documents** | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) · [`CERG-PLN-ISO-001`](CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md) |
| **Review Cycle** | Annual / On process or control change |
| **Frameworks** | NIST 800-53r5 CA · ISO/IEC 27001 Clause 9 · SOX ITGC |
| **Regulations** | SOX ITGC; CMMC; NERC-CIP; ISO; audit and customer assurance |
| **Environments** | All in-scope CERG environments where this template is used |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [Template Instructions](#2-template-instructions)
3. [Fill-In Template](#3-fill-in-template)
4. [Review and Approval](#4-review-and-approval)
5. [Document Control](#5-document-control)

---

## 1. Purpose and Use

This worksheet standardizes control testing and evidence review. It records the control objective, test method, population, sample, evidence examined, result, exceptions, and remediation linkage so audit work is repeatable and defensible.

> **Evidence Must Prove the Control, Not Decorate the File**
>
> A screenshot is useful only if it proves the control objective for the right scope and period. Evidence that cannot be tied to the control, sample, date, and result is not audit-ready evidence.

---

## 2. Template Instructions

1. Copy this template before use.
2. Replace every bracketed placeholder with case-specific information.
3. Do not delete fields that appear not applicable. Mark them `Not Applicable` and explain why.
4. Use canonical CERG role names from `CERG-GOV-OM-001`.
5. Link risks, findings, exceptions, evidence, and approvals to the system of record.
6. Store the completed artifact in the evidence library governed by `CERG-PRC-AUD-001`.

---

## 3. Fill-In Template

### 3.1 Control Test Header

| **Field** | **Value** |
|---|---|
| Test ID | `[TEST-YYYY-NNN]` |
| Control ID | `[CERG / framework control ID]` |
| Control Objective | `[Objective]` |
| Framework Mapping | `[SOX / ISO / CMMC / CIP / NIST]` |
| Test Period | `[Period]` |
| Tester | `[Name / role]` |
| Control Owner | `[Canonical role]` |

### 3.2 Population and Sample

| **Field** | **Value** |
|---|---|
| Population Source | `[Report / system / ticket queue]` |
| Population Size | `[Number]` |
| Sampling Method | `[Full population / judgmental / random / risk-based]` |
| Sample Size | `[Number]` |
| Sample Items | `[IDs]` |

### 3.3 Test Steps and Results

| **Step** | **Procedure** | **Evidence Reviewed** | **Result** | **Notes** |
|---|---|---|---|---|
| `1` | `[Test step]` | `[Evidence]` | `[Pass / Fail / Exception]` | `[Notes]` |

### 3.4 Exceptions and Remediation

| **Exception ID** | **Description** | **Severity** | **Owner** | **POA&M / Risk Link** |
|---|---|---|---|---|
| `[EXC-001]` | `[Exception]` | `[Severity]` | `[Owner]` | `[Link]` |

---

## 4. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Evidence Librarian | Confirms evidence is stored, complete, and indexed. | `[Name / Date]` |
| Governance Pillar Leader | Confirms test is sufficient for audit or assessment use. | `[Name / Date]` |
| Control Owner | Confirms factual accuracy and remediation ownership. | `[Name / Date]` |

Completed templates are reviewed at the cadence defined by their parent procedure or plan. Material changes require a new review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-AUD-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Evidence Librarian |
| **Approved By** | CISO (pending) |
| **Parent Document** | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) - Audit and Evidence Management Procedure |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-53r5 CA · ISO/IEC 27001 Clause 9 · SOX ITGC |
| **Regulations** | SOX ITGC; CMMC; NERC-CIP; ISO; audit and customer assurance |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a standalone fill-in template for control evidence and test worksheet. |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Governing audit and evidence workflow |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control source |
