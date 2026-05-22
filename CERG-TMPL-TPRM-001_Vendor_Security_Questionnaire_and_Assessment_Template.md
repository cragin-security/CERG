
# SURGE: Cyber Engineering, Risk & Governance

## VENDOR SECURITY QUESTIONNAIRE AND TPRM ASSESSMENT TEMPLATE
### Vendor Intake · Data Scope · Control Evidence · Residual Risk · Approval

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-TPRM-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Vendor Risk Analyst |
| **Parent Document** | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) - Third-Party and Supply Chain Risk Procedure |
| **Supporting Documents** | [`CERG-STD-TPRM-001`](CERG-STD-TPRM-001_Third_Party_and_Supply_Chain_Risk_Standard.md) · [`CERG-PLN-PRIV-001`](CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md) |
| **Review Cycle** | Annual / On process or control change |
| **Frameworks** | NIST CSF 2.0 GV.SC · NIST 800-53r5 SR · ISO/IEC 27001 A.5.19 through A.5.23 |
| **Regulations** | Cross-cutting; privacy, CUI, SOX, and contractual obligations where applicable |
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

This template captures vendor security intake, questionnaire responses, evidence review, risk rating, required remediation, and approval. It is designed to support repeatable third-party and supply-chain risk decisions without forcing every vendor into the same depth of review.

> **Vendor Risk Is Inherited Only If Conditions Hold**
>
> A SOC 2 report or ISO certificate is not a blanket pass. Reliance depends on the service scope, data processed, subprocessor chain, control exceptions, and the customer responsibilities the organization must actually perform.

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

### 3.1 Vendor Intake

| **Field** | **Value** |
|---|---|
| Vendor Name | `[Name]` |
| Service Name | `[Service]` |
| Business Owner | `[Owner]` |
| Vendor Risk Analyst | `[Name]` |
| Contract Stage | `[Prospect / Renewal / Existing / Termination]` |
| Service Criticality | `[Critical / High / Moderate / Low]` |
| Data Classification | `[Highest classification]` |
| Personal Data | `[Yes / No]` |
| CUI / Regulated Data | `[Yes / No / Details]` |

### 3.2 Questionnaire

| **Question** | **Vendor Response** | **Evidence Required** | **Reviewer Notes** |
|---|---|---|---|
| Does the vendor maintain a security program? | `[Response]` | `[SOC 2 / ISO / policy]` | `[Notes]` |
| Is MFA required for administrative access? | `[Response]` | `[Config / policy]` | `[Notes]` |
| Is data encrypted in transit and at rest? | `[Response]` | `[Evidence]` | `[Notes]` |
| Are vulnerabilities managed with defined SLAs? | `[Response]` | `[Report / policy]` | `[Notes]` |
| Are incidents reported within contractual timelines? | `[Response]` | `[Contract / policy]` | `[Notes]` |
| Are subprocessors disclosed? | `[Response]` | `[List]` | `[Notes]` |
| Is deletion or return supported at termination? | `[Response]` | `[Terms / procedure]` | `[Notes]` |

### 3.3 Risk Decision

| **Area** | **Rating / Decision** | **Rationale** |
|---|---|---|
| Inherent vendor risk | `[Low / Medium / High / Critical]` | `[Rationale]` |
| Control evidence quality | `[Strong / Adequate / Weak / None]` | `[Rationale]` |
| Residual vendor risk | `[Low / Medium / High / Critical]` | `[Rationale]` |
| Required remediation | `[Actions]` | `[Owner and due date]` |
| Approval decision | `[Approve / approve with conditions / reject / defer]` | `[Rationale]` |

---

## 4. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Vendor Risk Analyst | Completes assessment and recommended decision. | `[Name / Date]` |
| Risk Pillar Leader | Approves vendor residual-risk treatment. | `[Name / Date]` |
| Chief Information Security Officer (CISO) | Approves High or Critical vendor risk acceptance where required. | `[Name / Date]` |

Completed templates are reviewed at the cadence defined by their parent procedure or plan. Material changes require a new review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-TPRM-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Vendor Risk Analyst |
| **Approved By** | CISO (pending) |
| **Parent Document** | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) - Third-Party and Supply Chain Risk Procedure |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST CSF 2.0 GV.SC · NIST 800-53r5 SR · ISO/IEC 27001 A.5.19 through A.5.23 |
| **Regulations** | Cross-cutting; privacy, CUI, SOX, and contractual obligations where applicable |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a standalone fill-in template for vendor security questionnaire and tprm assessment template. |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Governing procedure |
| Privacy and Data Protection Operational Package | [`CERG-PLN-PRIV-001`](CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md) | Privacy vendor evidence interface |
