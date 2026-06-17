# SURGE: Cyber Engineering, Risk & Governance

## AI INTAKE AND SANCTIONING TEMPLATE
### Use Case · Data Classification · Provider Terms · Human Oversight · Approval Decision

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-AI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Document** | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) - Artificial Intelligence Security Standard |
| **Supporting Documents** | [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) · [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Review Cycle** | Annual / On material change to AI use, provider terms, or AI regulation |
| **Frameworks** | NIST AI RMF 100-1 · NIST 800-53r5 RA / SA / AC · OWASP Top 10 for LLM Applications · ISO/IEC 42001 |
| **Regulations** | Cross-cutting; CMMC L2 / 800-171r3, SOX ITGC, privacy, and contractual obligations where applicable |
| **Environments** | All in-scope CERG environments where AI tools, AI-enabled SaaS, embedded AI, or built AI systems are proposed |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [Template Instructions](#2-template-instructions)
3. [Fill-In Template](#3-fill-in-template)
4. [Review and Approval](#4-review-and-approval)
5. [Document Control](#5-document-control)

---

## 1. Purpose and Use

This template records the intake and sanctioning decision for a proposed AI use. It applies to consumed AI services, AI-enabled vendor features, embedded AI capabilities, and AI systems the organization builds or integrates.

The completed template answers the operating question that CERG requires before AI use begins: what is the AI being used for, what data can enter it, what actions can it take, who reviews its output, what provider or model terms apply, and which CERG path governs the decision.

> **Sanctioned AI Is a Governed Path, Not a Blanket Approval**
>
> Approval of an AI tool or feature is limited to the stated use case, data classification, user population, provider terms, and controls recorded here. Approval for Internal data is not approval for Confidential or Restricted data. Approval for summarization is not approval for autonomous action.

---

## 2. Template Instructions

1. Copy this template before use.
2. Replace every bracketed field with case-specific information.
3. Do not delete fields that appear not applicable. Mark them `Not Applicable` and explain why.
4. Use canonical CERG role names from `CERG-GOV-OM-001`.
5. Link related vendor assessments, architecture reviews, threat models, risk records, exceptions, and evidence to the system of record.
6. Store the completed artifact in the evidence library governed by `CERG-PRC-AUD-001`.
7. If the request is approved, update the sanctioned AI tools list or AI system register as applicable.

---

## 3. Fill-In Template

### 3.1 Intake Summary

| **Field** | **Value** |
|---|---|
| Intake ID | `[AI-INTAKE-YYYY-NNN]` |
| Request Date | `[Date]` |
| Requested Tool / Feature / System | `[Name]` |
| AI Use Category | `[Consumed AI service / Embedded AI / Built AI]` |
| Business Owner | `[Owner]` |
| Technical Owner | `[Owner]` |
| Requesting Team | `[Team]` |
| Proposed Users | `[User population]` |
| Proposed Use Case | `[Describe the intended use]` |
| Existing Vendor / New Vendor / Internal Build | `[Existing vendor / New vendor / Internal build]` |
| Target Go-Live or Use Date | `[Date]` |

### 3.2 Data Classification and Prompt Boundary

| **Question** | **Response** | **Evidence / Notes** |
|---|---|---|
| What is the highest data classification that may enter prompts, uploads, context windows, fine-tuning, or retrieval stores? | `[Public / Internal / Confidential / Restricted]` | `[Data classification record]` |
| Will personal data be processed? | `[Yes / No]` | `[Details]` |
| Will CUI, FCI, BES Cyber System Information, SOX-relevant data, or other regulated data be processed? | `[Yes / No]` | `[Regulatory scope]` |
| Will prompts or uploaded data be retained by a third party? | `[Yes / No / Unknown]` | `[Retention terms]` |
| Will prompts, uploads, outputs, or feedback be used to train provider models? | `[Yes / No / Unknown]` | `[Provider assurance or contract term]` |
| Is data egress monitored or restricted? | `[Yes / No]` | `[DLP, proxy, CASB, SSPM, or logging evidence]` |
| Maximum classification approved for this request | `[Public / Internal / Confidential / Restricted / Not approved]` | `[Rationale]` |

### 3.3 Provider, Model, and Supply Chain

| **Question** | **Response** | **Evidence / Notes** |
|---|---|---|
| Provider or model source | `[Provider / model / repository]` | `[Link or record]` |
| Deployment or inference location | `[SaaS / organization cloud / on-premises / endpoint / other]` | `[Details]` |
| Provider assessment required? | `[Yes / No]` | `[TPRM record or rationale]` |
| Model provenance known and trusted? | `[Yes / No]` | `[Evidence]` |
| Subprocessors or downstream services involved? | `[Yes / No]` | `[List or vendor evidence]` |
| Contractual protections reviewed? | `[Yes / No]` | `[DPA, security addendum, no-training term, retention term]` |
| Material change to existing vendor risk profile? | `[Yes / No]` | `[Reassessment trigger and record]` |

### 3.4 Agency, Access, and Human Oversight

| **Question** | **Response** | **Evidence / Notes** |
|---|---|---|
| Can the AI system take action beyond producing text, code, analysis, or recommendations? | `[Yes / No]` | `[Actions]` |
| What systems, APIs, plugins, tools, repositories, or data stores can the AI access? | `[List]` | `[Access design]` |
| Are privileges least-privilege and time-bound? | `[Yes / No]` | `[Access control evidence]` |
| Are high-consequence actions blocked or subject to human confirmation? | `[Yes / No / Not Applicable]` | `[Control description]` |
| Who reviews AI output before reliance? | `[Role / team]` | `[Review process]` |
| Is AI used for employment, safety, control system, financial, legal, or other consequential decisions? | `[Yes / No]` | `[Human-in-the-loop control]` |

### 3.5 Security Review Routing

| **Routing Question** | **Decision** | **Linked Record** |
|---|---|---|
| Architecture review required under `CERG-PRC-AR-001`? | `[Yes / No]` | `[Review ID]` |
| Threat model required under `CERG-PRC-TM-001`? | `[Yes / No]` | `[Threat model ID]` |
| TPRM assessment required under `CERG-PRC-TPRM-001`? | `[Yes / No]` | `[Vendor assessment ID]` |
| Secure SDLC gates required under `CERG-STD-SDL-001`? | `[Yes / No]` | `[Project / pipeline evidence]` |
| Risk register entry required under `CERG-PRC-RM-001`? | `[Yes / No]` | `[Risk ID]` |
| Exception required? | `[Yes / No]` | `[Exception ID]` |

### 3.6 Required Controls and Conditions

| **Control / Condition** | **Owner** | **Due Date** | **Evidence** |
|---|---|---|---|
| `[Condition, such as no Confidential data until contract updated]` | `[Owner]` | `[Date]` | `[Evidence link]` |
| `[Condition]` | `[Owner]` | `[Date]` | `[Evidence link]` |

### 3.7 Disposition

| **Field** | **Value** |
|---|---|
| Disposition | `[Approved / Approved with conditions / Limited pilot / Blocked pending remediation / Rejected]` |
| Approved Use Cases | `[Use cases]` |
| Prohibited Use Cases | `[Use cases]` |
| Approved User Population | `[Users / groups]` |
| Maximum Approved Data Classification | `[Public / Internal / Confidential / Restricted]` |
| Required Register Update | `[Sanctioned AI tools list / AI system register / Both / None]` |
| Review Cadence | `[Quarterly / Semiannual / Annual / On material change]` |
| Reassessment Triggers | `[Provider term change, new data class, new agency, regulatory change, incident, vendor feature change]` |
| Decision Rationale | `[Rationale]` |

---

## 4. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Business Owner | Owns the use case, business need, and operational consequence. | `[Name / Date]` |
| Application Security Engineer | Confirms AI-specific technical risks, threat model needs, and secure development implications. | `[Name / Date]` |
| Vendor Risk Analyst | Confirms third-party AI service or AI-enabled vendor feature assessment where applicable. | `[Name / Date]` |
| Governance Pillar Leader | Approves sanctioned-use decision, maximum data classification, and governance reporting entry. | `[Name / Date]` |
| CISO | Approves High or Critical residual risk, Restricted data use, or other material escalation. | `[Name / Date]` |

Completed templates are reviewed at the cadence defined by the disposition. Material changes to the use case, data classification, provider terms, model, agency, or regulatory scope require reassessment before expanded use.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-AI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) - Artificial Intelligence Security Standard |
| **Review Cycle** | Annual; and on material change to AI use, provider terms, or AI regulation |
| **Next Scheduled Review** | 2027-06-17 |
| **Frameworks** | NIST AI RMF 100-1 · NIST 800-53r5 RA / SA / AC · OWASP Top 10 for LLM Applications · ISO/IEC 42001 |
| **Regulations** | Cross-cutting; CMMC L2 / 800-171r3, SOX ITGC, privacy, and contractual obligations where applicable |
| **Environments** | All in-scope CERG environments where AI tools, AI-enabled SaaS, embedded AI, or built AI systems are proposed |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-17 | Cyber Governance | Initial release. Establishes a fill-in AI intake and sanctioning template for proposed AI tools, AI-enabled vendor features, embedded AI capabilities, and built AI systems. |

### Review Triggers

- Parent standard or related procedure change
- Material change to provider terms, model behavior, training use, retention, or deployment location
- New or changed AI regulation
- Significant AI-related finding, incident, or audit issue
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Artificial Intelligence Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Parent standard; defines AI use categories and AI-specific security requirements |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Governs what data may enter AI prompts, uploads, training, and retrieval context |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Routes AI applications and higher-risk AI uses through architecture review |
| Threat Modeling Procedure | [`CERG-PRC-TM-001`](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Defines AI-specific abuse cases for built and embedded AI systems |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Assesses third-party AI services and AI-enabled vendor features |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Records material AI risks, shadow AI patterns, and exceptions |
