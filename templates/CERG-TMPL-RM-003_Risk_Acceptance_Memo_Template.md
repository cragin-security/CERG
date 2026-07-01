## RISK ACCEPTANCE MEMO TEMPLATE
### Supporting Memo · Residual Risk · Business Rationale · Conditions · Expiration

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-RM-003 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Supporting Documents** | [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) · [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · [`CERG-TMPL-RM-004`](CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md) |
| **Review Cycle** | Annual / On process or control change |
| **Frameworks** | NIST 800-30r1 · NIST 800-39 · ISO 31000 |
| **Regulations** | Cross-cutting |
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

This memo is a lightweight supporting artifact for a risk acceptance decision governed by [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 and submitted through [`CERG-TMPL-RM-004`](CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md). It may summarize rationale, conditions, and review triggers, but it does not create a separate acceptance path. The completed memo must attach to the Risk Acceptance Request Form, link to the risk register, and must not replace either artifact.

> **Acceptance Is a Decision, Not an Absence of Action**
>
> Risk is not accepted because nobody fixed it. Risk is accepted only when the right authority understands the scenario, impact, residual exposure, conditions, expiration, and alternatives, then records the decision. The Business Owner accepts the business consequence; Security assesses and recommends but does not accept business risk.

---

## 2. Template Instructions

1. Use this memo only as an attachment or supporting decision narrative for [`CERG-TMPL-RM-004`](CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md).
2. Replace every bracketed field with case-specific information.
3. Do not delete fields that appear not applicable. Mark them `Not Applicable` and explain why.
4. Use canonical CERG role names from `CERG-GOV-OM-001` and approval authority from `CERG-GOV-RMF-001` §9.7.
5. Link risks, findings, exceptions, evidence, and approvals to the system of record.
6. Store the completed artifact with the completed Risk Acceptance Request Form and risk-register entry in the evidence library governed by `CERG-PRC-AUD-001`.

---

## 3. Fill-In Template

### 3.1 Decision Summary

| **Field** | **Value** |
|---|---|
| Memo ID | `[RA-YYYY-NNN]` |
| Risk ID | `[Risk ID]` |
| Risk Statement | `[Because of..., affecting..., there is a possibility that..., resulting in...]` |
| Requesting Owner | `[Owner]` |
| Business Owner / Risk Owner | `[Name and role accepting business consequence]` |
| Affected Assets / Processes | `[Scope]` |
| Regulatory Scope | `[CUI / SOX / CIP / privacy / none]` |
| Residual Risk Rating | `[Low / Medium / High / Critical]` |
| Acceptance Period | `[Start date to expiration date]` |

### 3.2 Business Rationale

`[Explain why acceptance is appropriate compared with mitigation, transfer, or avoidance.]`

### 3.3 Conditions of Acceptance

| **Condition** | **Owner** | **Evidence / Monitoring** |
|---|---|---|
| `[Condition]` | `[Owner]` | `[Evidence]` |

### 3.4 Alternatives Considered

| **Alternative** | **Reason Not Selected** |
|---|---|
| `[Alternative]` | `[Reason]` |

### 3.5 Expiration and Review

| **Field** | **Value** |
|---|---|
| Expiration Date | `[Date]` |
| Review Cadence | `[Cadence]` |
| Renewal Criteria | `[Criteria]` |
| Trigger for Early Review | `[Trigger]` |

---

## 4. Review and Approval

Approval authority follows [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 and is recorded on [`CERG-TMPL-RM-004`](CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md). This memo is not valid unless the required `TMPL-RM-004` approvals are complete.

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Risk Register Owner | Confirms register entry, scoring, and linkage. | `[Name / Date]` |
| Risk Pillar Leader | Confirms risk assessment methodology and recommendation. | `[Name / Date]` |
| Business Owner | Accepts the business consequence of residual risk. Required for every Low, Medium, or High acceptance. | `[Name / Date]` |
| Chief Information Security Officer (CISO) | Approves High and Critical acceptance where required by RMF-001 §9.7. | `[Name / Date]` |
| Executive Sponsor | Accepts the business consequence for Critical risk where required by RMF-001 §9.7. | `[Name / Date]` |

Completed templates are reviewed at the cadence defined by their parent procedure or plan. Material changes require a new review through `TMPL-RM-004`.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-RM-003 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-30r1 · NIST 800-39 · ISO 31000 |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.1 | 2026-06-18 | Governance Pillar Leader | Recast this memo as a supporting attachment to TMPL-RM-004 and RMF-001 §9.7, added Business Owner / Executive Sponsor acceptance language, and removed standalone acceptance authority. |
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a standalone fill-in template for risk acceptance memo template. |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Governing risk acceptance lifecycle |
| Risk Acceptance Request Form | [`CERG-TMPL-RM-004`](CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md) | Required acceptance form; this memo may attach as support |
| Risk Management Framework | [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) | Canonical scoring and acceptance authority (§9.5 and §9.7) |
