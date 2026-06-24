## RISK ACCEPTANCE REQUEST FORM
### Business Owner Acceptance · Residual Risk · Per-RMF-001 Authority · Conditions · Expiration

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-RM-004 |
| **Version** | 1.2 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Register Owner |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Supporting Documents** | [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) · [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · [`CERG-TMPL-RM-002`](CERG-TMPL-RM-002_Security_Exception_Request_Form.md) |
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

This form records a formal **risk acceptance** decision under the authority framework defined in [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. It is used when leadership chooses to accept residual risk rather than mitigate, transfer, or avoid it. 

**This form is for risk acceptances only.** For deviations from policy or standards (where the control itself is not implemented as written), use the Security Exception Request Form [`CERG-TMPL-RM-002`](CERG-TMPL-RM-002_Security_Exception_Request_Form.md) — which follows the Governance-tracked exception register workflow.

**Key distinction per RMF-001 §9.7a:**
- **Policy Exception** (→ TMPL-RM-002): A specific control or standard cannot be met. Governance approves. Risk assesses. The exception lives in the exception register.
- **Risk Acceptance** (→ this form): The residual risk after controls is within appetite. The **Business Owner** accepts the business consequence. Approval follows the RMF-001 §9.7 authority table. The acceptance lives in the risk register.

> **Acceptance Is a Business Decision, Not a Security Decision**
>
> Security assesses, recommends, and validates. The Business Owner accepts the business consequence of residual risk. No one in Security accepts business risk on behalf of the organization. Every acceptance requires the Business Owner's documented signature at the authority level specified in RMF-001 §9.7.

---

## 2. Template Instructions

1. Copy this template before use.
2. Replace every bracketed field with case-specific information.
3. Do not delete fields that appear not applicable. Mark them `Not Applicable` and explain why.
4. Use canonical CERG role names from `CERG-GOV-OM-001`.
5. Link risks, findings, acceptances, evidence, and approvals to the system of record.
6. Store the completed artifact in the evidence library governed by `CERG-PRC-AUD-001`.
7. The Business Owner must review and sign Section 4 before submission to CERG.

---

## 3. Fill-In Template

### 3.1 Decision Summary

| **Field** | **Value** |
|---|---|
| Acceptance ID | `[RA-YYYY-NNN]` |
| Risk ID | `[Risk ID from risk register]` |
| Related Exception ID (if any) | `[EX-YYYY-NNN or N/A]` |
| Risk Statement | `[Because of... affecting... there is a possibility that... resulting in...]` |
| Requesting Owner | `[Name / Role]` |
| Affected Systems / Assets | `[Asset IDs or system names]` |
| Environment | `[IT / Cloud / SaaS / OT / Hybrid]` |
| Regulatory Scope | `[CUI / SOX / CIP / Privacy / None]` |
| Residual Risk Rating | `[Low / Medium / High / Critical]` |
| Residual Risk Score | `[Likelihood × Impact]` |
| Acceptance Period | `[Start date to expiration date]` |
| Acceptance Type | `[Time-bound / Standing]` |

### 3.2 Business Decision Box

| **Decision Question** | **Business Owner / Required Authority Response** |
|---|---|
| What residual business consequence is being accepted? | `[Plain-language consequence]` |
| Why is acceptance preferable to immediate treatment? | `[Cost / schedule / operational / reliability / contractual rationale]` |
| What funding or resourcing decision would retire this acceptance? | `[Decision, owner, estimate, and timing]` |
| What conditions must remain true for this acceptance to stay valid? | `[Controls, monitoring, scope limits, review triggers]` |
| What event would require immediate re-review or revocation? | `[Trigger]` |
| Who owns treatment after acceptance? | `[Named business or technical owner]` |

### 3.3 Business Rationale

`[Explain why acceptance is the appropriate treatment compared with mitigation, transfer, or avoidance. Address: cost-to-fix vs. residual risk, operational constraints, compensating control adequacy, and regulatory implications.]`

### 3.4 Alternatives Considered

| **Alternative** | **Reason Not Selected** |
|---|---|
| `[Mitigation — implement full control]` | `[Reason]` |
| `[Transfer — insurance or vendor]` | `[Reason]` |
| `[Avoid — cease the activity]` | `[Reason]` |

### 3.5 Risk Assessment (Prepared by CERG Risk)

| **Area** | **Assessment** |
|---|---|
| Inherent Risk (no controls) | `[Likelihood × Impact = Score]` |
| Controls in Place | `[List of existing compensating controls]` |
| Residual Risk (with controls) | `[Likelihood × Impact = Score]` |
| Residual Rating | `[Low / Medium / High / Critical]` |
| Threat or Weakness Created | `[Description]` |
| Affected Data or Process | `[Scope]` |
| Business Consequence if Unaddressed | `[Consequence]` |

### 3.6 Conditions of Acceptance

| **Condition** | **Owner** | **Evidence / Monitoring** | **Review Cadence** |
|---|---|---|---|
| `[Condition]` | `[Owner]` | `[Evidence]` | `[Cadence]` |

### 3.7 Expiration and Review

| **Field** | **Value** |
|---|---|
| Expiration Date | `[Date]` |
| Review Cadence | `[Quarterly / Monthly / Per milestone]` |
| Renewal Criteria | `[Conditions that must be met for renewal]` |
| Trigger for Early Review | `[Control failure, threat intel change, regulatory change]` |

---

## 4. Review and Approval

Approval authority follows [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. An acceptance is not valid until all required signatures are recorded.

| **Role** | **Review Meaning** | **Name** | **Date** | **Decision** |
|---|---|---|---|---|
| **Risk Register Owner** | Confirms risk register entry, scoring accuracy, and linkage completeness. | `[Name]` | `[Date]` | Verified / Returned |
| **Risk Pillar Leader** | Confirms risk assessment methodology and residual score. Recommends disposition. | `[Name]` | `[Date]` | Concur / Returned |
| **Engineering Pillar Leader** | Confirms compensating controls are in place and effective (if controls involve Engineering). | `[Name]` | `[Date]` | Concur / Returned |
| **Governance Pillar Leader** | Confirms regulatory overlay completeness and documentation adequacy. | `[Name]` | `[Date]` | Concur / Returned |
| **Business Owner** | Accepts the business consequence of the residual risk. | `[Name]` | `[Date]` | Accept / Decline |
| **CISO** | Approves High and Critical acceptances per RMF-001 §9.7 authority. | `[Name]` | `[Date]` | Approve / Deny |
| **Executive Sponsor** | Accepts the business consequence for Critical risk acceptance and/or board-notified items per RMF-001 §9.7. | `[Name]` | `[Date]` | Accept / Escalate to Board |

**Approver Note:** Approvers may delegate within their authority but shall document the delegation. No acceptance expires automatically; every acceptance at every tier requires a fresh approval cycle at expiration. Renewal more than twice without material progress toward remediation escalates one approval tier above the original approver.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-RM-004 |
| **Version** | 1.2 |
| **Status** | Approved |
| **Effective Date** | 2026-06-18 |
| **Classification** | Public |
| **Owner** | Risk Register Owner |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-06-18 |
| **Frameworks** | NIST 800-30r1 · NIST 800-39 · ISO 31000 |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.2 | 2026-06-18 | Governance Pillar Leader | Added business-facing decision box for residual consequence, treatment funding, validity conditions, and re-review triggers. |
| 1.1 | 2026-06-18 | Governance Pillar Leader | Aligned acceptance type and related-template wording with RMF-001 authority; clarified that TMPL-RM-003 is supporting only and that Executive Sponsor accepts Critical business consequence. |
| 1.0 | 2026-06-18 | Governance Pillar Leader | Initial release. Establishes Risk Acceptance Request Form as the distinct workflow for risk acceptances (Business Owner + per-RMF-001 authority), separate from Security Exception Requests (TMPL-RM-002). |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Risk Register Templates and Reporting | [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Register and reporting schema |
| Security Exception Request Form | [`CERG-TMPL-RM-002`](CERG-TMPL-RM-002_Security_Exception_Request_Form.md) | Governance-tracked policy/standard exception workflow |
| Risk Acceptance Memo Template | [`CERG-TMPL-RM-003`](CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md) | Optional supporting memo; does not replace this form or RMF-001 approval authority |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Governing risk acceptance lifecycle |
| Risk Management Framework | [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk acceptance authority table (§9.7) |

---

> **SURGE, Cyber Engineering, Risk & Governance**
>
> *Assess it. Accept it. Own it. Review it.*

---

*CERG-TMPL-RM-004 · Version 1.2 · Public*
