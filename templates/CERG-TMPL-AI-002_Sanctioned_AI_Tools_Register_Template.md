## SANCTIONED AI TOOLS REGISTER TEMPLATE
### Approved Tools · Data Classification Limits · Use Cases · Conditions · Review Cadence

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-AI-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Document** | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) - Artificial Intelligence Security Standard |
| **Supporting Documents** | [`CERG-TMPL-AI-001`](CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) · [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) · [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Review Cycle** | Quarterly / On material change to AI provider terms, data classification, or approved use |
| **Frameworks** | NIST AI RMF 100-1 · NIST 800-53r5 PM / SA / AC · ISO/IEC 42001 |
| **Regulations** | Cross-cutting; CMMC L2 / 800-171r3, SOX ITGC, privacy, and contractual obligations where applicable |
| **Environments** | All in-scope CERG environments where AI tools or AI-enabled vendor features are sanctioned for use |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [Template Instructions](#2-template-instructions)
3. [Fill-In Register Template](#3-fill-in-register-template)
4. [Review and Maintenance](#4-review-and-maintenance)
5. [Document Control](#5-document-control)

---

## 1. Purpose and Use

This template provides the authoritative local register of sanctioned AI tools and AI-enabled vendor features. It is the operational artifact that makes the approved AI path visible to staff and reviewable by Governance.

The register does not approve AI in general. Each entry defines the approved tool, owner, user population, maximum data classification, approved use cases, prohibited use cases, required controls, and reassessment cadence.

> **Visibility Is a Control**
>
> A sanctioned AI list is not only a convenience for users. It is a control surface. Staff can see where approved use exists, Governance can see what must be reviewed, Risk can see which vendor assessments remain current, and Engineering can see which tools require technical monitoring.

---

## 2. Template Instructions

1. Maintain one current register as the authoritative source for sanctioned AI tools.
2. Add a register entry only after intake is completed through [`CERG-TMPL-AI-001`](CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) or an equivalent local workflow.
3. Do not list a tool as broadly approved unless all data classifications, use cases, and user populations in scope have been explicitly reviewed.
4. Use `Not Approved` rather than blank fields where a classification, use case, or user group is prohibited.
5. Link each entry to its intake, vendor assessment, architecture review, risk record, exception, and evidence where applicable.
6. Review the register at least quarterly and whenever provider terms, AI features, retention, training use, or approved data classification changes.
7. Publish a user-facing subset that is appropriate for staff; retain assessment details in the evidence library where needed.

---

## 3. Fill-In Register Template

### 3.1 Register Metadata

| **Field** | **Value** |
|---|---|
| Register Owner | `[Governance Pillar Leader / delegated owner]` |
| Maintainer | `[Policy & Standards Manager or assigned role]` |
| Register Location | `[System of record / link]` |
| Last Review Date | `[Date]` |
| Next Review Date | `[Date]` |
| Publication Location for Staff | `[Intranet / portal / policy site]` |

### 3.2 Sanctioned AI Tools Register

| **Tool / Feature** | **Provider** | **AI Use Category** | **Business Owner** | **Approved Users** | **Approved Use Cases** | **Prohibited Use Cases** | **Maximum Data Classification** | **Training / Retention Position** | **Required Controls** | **Linked Intake / Evidence** | **Review Cadence** | **Status** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `[Tool name]` | `[Provider]` | `[Consumed AI service / Embedded AI]` | `[Owner]` | `[Users / groups]` | `[Summarization, coding assistance, analysis, etc.]` | `[Employment decisions, Restricted data, autonomous action, etc.]` | `[Public / Internal / Confidential / Restricted / Not Approved]` | `[No provider training; retention period; enterprise controls]` | `[SSO, DLP, logging, admin controls, contractual terms]` | `[AI intake ID, TPRM ID, evidence links]` | `[Quarterly / Semiannual / Annual / On change]` | `[Approved / Approved with conditions / Pilot / Suspended / Retired]` |

### 3.3 Conditional Approval Tracker

Use this section for tools approved only after conditions are satisfied, pilots, or limited exceptions.

| **Tool / Feature** | **Condition** | **Owner** | **Due Date** | **Current Status** | **Evidence** |
|---|---|---|---|---|---|
| `[Tool name]` | `[Condition]` | `[Owner]` | `[Date]` | `[Open / Complete / Overdue]` | `[Evidence link]` |

### 3.4 Staff-Facing Use Statement

For each sanctioned tool, publish a short user-facing statement in plain language.

| **Tool / Feature** | **Staff-Facing Statement** |
|---|---|
| `[Tool name]` | `[Example: Approved for Internal data and lower for drafting, summarization, and coding assistance. Do not enter Confidential, Restricted, CUI, BES Cyber System Information, personal data, customer secrets, or production credentials. Human review is required before relying on output.]` |

### 3.5 Reassessment Log

| **Date** | **Tool / Feature** | **Trigger** | **Reviewer** | **Outcome** | **Linked Record** |
|---|---|---|---|---|---|
| `[Date]` | `[Tool name]` | `[Quarterly review / Provider term change / New AI feature / Incident / Regulation change]` | `[Reviewer]` | `[No change / Conditions added / Classification changed / Suspended / Retired]` | `[Record link]` |

---

## 4. Review and Maintenance

| **Role** | **Responsibility** |
|---|---|
| Governance Pillar Leader | Owns the register, approves sanctioned-use entries, and ensures the staff-facing list remains current. |
| Policy & Standards Manager | Maintains register content and coordinates periodic review. |
| Vendor Risk Analyst | Confirms vendor assessments and provider-term evidence for third-party AI services and AI-enabled vendor features. |
| Application Security Engineer | Confirms AI-specific technical control conditions where the tool interacts with code, applications, or built AI systems. |
| Cloud Security Engineer | Confirms SaaS, network, DLP, CASB, SSPM, or other technical monitoring where applicable. |
| Risk Register Owner | Ensures material AI risk, exceptions, and shadow AI patterns are linked to the risk register. |

A register entry must be reassessed when any of the following occur:

- The provider changes training, retention, confidentiality, or subprocessor terms.
- The tool adds a new AI feature, agent capability, connector, plugin, or data integration.
- The approved data classification or user population expands.
- The tool is proposed for regulated, safety, financial, employment, legal, or other consequential decisions.
- A security incident, audit finding, or material risk finding involves the tool.
- The CISO, Governance Pillar Leader, Risk Pillar Leader, or Engineering Pillar Leader directs review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-AI-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) - Artificial Intelligence Security Standard |
| **Review Cycle** | Quarterly; and on material change to AI provider terms, data classification, or approved use |
| **Next Scheduled Review** | 2026-09-17 |
| **Frameworks** | NIST AI RMF 100-1 · NIST 800-53r5 PM / SA / AC · ISO/IEC 42001 |
| **Regulations** | Cross-cutting; CMMC L2 / 800-171r3, SOX ITGC, privacy, and contractual obligations where applicable |
| **Environments** | All in-scope CERG environments where AI tools or AI-enabled vendor features are sanctioned for use |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-17 | Cyber Governance | Initial release. Establishes the sanctioned AI tools register template for recording approved tools, maximum data classifications, use-case limits, conditions, evidence, and review cadence. |

### Review Triggers

- Parent standard change
- Material change to any sanctioned AI tool, provider term, approved data classification, approved use case, or user population
- New or changed AI regulation
- Significant AI-related finding, incident, or audit issue
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Artificial Intelligence Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Parent standard; requires a sanctioned AI tools list |
| AI Intake and Sanctioning Template | [`CERG-TMPL-AI-001`](CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) | Source intake and approval record for register entries |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Defines data classification limits for AI use |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Governs assessment of third-party AI services and AI-enabled vendor features |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Tracks material AI risk, exceptions, and shadow AI patterns |
