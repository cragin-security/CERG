# SURGE: Cyber Engineering, Risk & Governance

## AI SYSTEM AND MODEL REGISTER TEMPLATE
### Model Inventory · Data Sources · Agency Boundary · Integrations · Monitoring · Ownership

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-AI-003 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Application Security Engineer |
| **Parent Document** | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) - Artificial Intelligence Security Standard |
| **Supporting Documents** | [`CERG-TMPL-AI-001`](CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) · [`CERG-TMPL-AI-002`](CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) · [`CERG-STD-SDL-001`](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) · [`CERG-STD-AM-001`](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) |
| **Review Cycle** | Quarterly / On material change to model, data source, agency, integration, or deployment |
| **Frameworks** | NIST AI RMF 100-1 · NIST 800-53r5 CM / RA / SA / SI · OWASP Top 10 for LLM Applications · ISO/IEC 42001 |
| **Regulations** | Cross-cutting; CMMC L2 / 800-171r3, SOX ITGC, privacy, and contractual obligations where applicable |
| **Environments** | Built AI systems, embedded AI systems, AI agents, model-serving platforms, RAG systems, and AI-enabled integrations in CERG-managed environments |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [Template Instructions](#2-template-instructions)
3. [Fill-In Register Template](#3-fill-in-register-template)
4. [Review and Maintenance](#4-review-and-maintenance)
5. [Document Control](#5-document-control)

---

## 1. Purpose and Use

This template provides the inventory record for built and embedded AI systems, models, retrieval stores, agents, and AI-enabled integrations. It complements the sanctioned AI tools register by focusing on systems the organization builds, configures, integrates, or operates as part of a business process or product.

The register documents model provenance, data sources, classification, access, agency boundary, integrations, human oversight, monitoring, and lifecycle status. It is the AI-specific extension of asset inventory, secure development, architecture review, and threat modeling.

> **A Model Is a Component, Not Magic**
>
> CERG treats a model like any other material component: it has a source, version, owner, dependencies, access path, data boundary, and change history. AI-specific behavior matters, but it does not erase normal inventory, change, access, logging, and software assurance requirements.

---

## 2. Template Instructions

1. Maintain one current register for built and embedded AI systems and models.
2. Create or update an entry when an AI system is approved through [`CERG-TMPL-AI-001`](CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md), enters architecture review, changes model/provider, adds a retrieval store, gains new agency, or expands data classification.
3. Record the model as an inventoried component and link the entry to the asset inventory, SBOM, architecture review, threat model, and change record where applicable.
4. Do not treat a third-party model API as invisible. If the system depends on it, record the provider, model family, approved version or version policy, and contractual or technical constraints.
5. Use `Not Applicable` only with an explanation.
6. Store completed register records in the evidence library governed by `CERG-PRC-AUD-001`.

---

## 3. Fill-In Register Template

### 3.1 Register Metadata

| **Field** | **Value** |
|---|---|
| Register Owner | `[Application Security Engineer / delegated owner]` |
| Maintainer | `[Role or team]` |
| Register Location | `[System of record / link]` |
| Last Review Date | `[Date]` |
| Next Review Date | `[Date]` |
| Relationship to Asset Inventory | `[Asset inventory link / CMDB reference]` |

### 3.2 AI System Inventory

| **Field** | **Value** |
|---|---|
| AI System ID | `[AI-SYS-YYYY-NNN]` |
| System / Product Name | `[Name]` |
| Business Owner | `[Owner]` |
| Technical Owner | `[Owner]` |
| AI Use Category | `[Built AI / Embedded AI / Agent / RAG / Model-serving platform / Other]` |
| Business Process Supported | `[Process or product]` |
| Production Status | `[Prototype / Pilot / Production / Suspended / Retired]` |
| Criticality | `[Critical / High / Moderate / Low]` |
| Highest Data Classification | `[Public / Internal / Confidential / Restricted]` |
| Regulatory Scope | `[CUI / FCI / BES Cyber System Information / SOX / privacy / contractual / none]` |
| Linked AI Intake | `[AI intake ID]` |
| Linked Architecture Review | `[Architecture review ID]` |
| Linked Threat Model | `[Threat model ID]` |
| Linked Asset / CMDB Record | `[Record ID]` |

### 3.3 Model and Provider Record

| **Field** | **Value** |
|---|---|
| Model Name / Family | `[Model]` |
| Model Provider / Source | `[Provider, repository, internal team]` |
| Model Version or Version Policy | `[Pinned version / provider-managed / internal release]` |
| Model Type | `[LLM / classifier / recommender / computer vision / forecasting / other]` |
| Deployment Location | `[SaaS API / organization cloud / on-premises / endpoint / embedded vendor platform]` |
| Model Provenance Evidence | `[Source validation, attestation, repository, contract, vendor assessment]` |
| Fine-Tuned? | `[Yes / No]` |
| Fine-Tuning Owner | `[Owner or Not Applicable with reason]` |
| Training / Fine-Tuning Data Classification | `[Public / Internal / Confidential / Restricted / Not Applicable with reason]` |
| Provider Training Use Allowed? | `[Yes / No / Not Applicable with reason]` |
| Retention Position | `[Retention period, deletion capability, or Not Applicable with reason]` |

### 3.4 Data Sources and Retrieval Stores

| **Data Source / Store** | **Purpose** | **Classification** | **Owner** | **Trust Level** | **Update Cadence** | **Access Control** | **Evidence** |
|---|---|---|---|---|---|---|---|
| `[Prompt input / RAG corpus / vector store / database / file share / telemetry source]` | `[Purpose]` | `[Public / Internal / Confidential / Restricted]` | `[Owner]` | `[Trusted / semi-trusted / untrusted]` | `[Cadence]` | `[Control]` | `[Link]` |

### 3.5 Agency, Tools, and Integrations

| **Field** | **Value** |
|---|---|
| Can the AI invoke tools, plugins, APIs, scripts, workflows, or transactions? | `[Yes / No]` |
| Tool / Integration List | `[List systems and actions]` |
| Maximum Action Authority | `[Read-only / draft-only / recommend / execute low-risk action / execute high-risk action with approval]` |
| Human Approval Required For | `[Actions requiring confirmation]` |
| Privilege Boundary | `[Service account, role, scope, time limits]` |
| Secrets Handling | `[Secret store, no secret access, or other control]` |
| Production Change Capability | `[None / proposes changes / executes with approval / executes autonomously]` |
| External Communication Capability | `[None / drafts messages / sends with approval / sends autonomously]` |
| Kill Switch / Disable Path | `[How to disable model, agent, connector, or feature]` |

### 3.6 Security Controls and Monitoring

| **Control Area** | **Required Record** | **Evidence / Link** |
|---|---|---|
| Architecture review | `[Completed / Not required with rationale]` | `[Link]` |
| AI threat model | `[Completed / Not required with rationale]` | `[Link]` |
| Secure development gates | `[SAST / DAST / SCA / code review / pipeline evidence]` | `[Link]` |
| Prompt injection controls | `[Instruction/data separation, allowlists, output constraints, other]` | `[Link]` |
| Output handling controls | `[Validation, encoding, human review, downstream guardrails]` | `[Link]` |
| Data loss prevention | `[DLP, logging, masking, access restriction]` | `[Link]` |
| Logging and monitoring | `[Prompts, outputs, actions, admin events, errors, abuse signals]` | `[Link]` |
| Abuse and anomaly detection | `[Detection logic or monitoring process]` | `[Link]` |
| Red-team / adversarial test | `[Completed / scheduled / not required with rationale]` | `[Link]` |
| Incident response handoff | `[Playbook or escalation path]` | `[Link]` |

### 3.7 Change and Review Log

| **Date** | **Change / Review Trigger** | **Changed By** | **Risk Impact** | **Required Follow-Up** | **Linked Record** |
|---|---|---|---|---|---|
| `[Date]` | `[Model change / data source added / agency expanded / provider change / quarterly review]` | `[Name / role]` | `[None / Low / Medium / High / Critical]` | `[Action]` | `[Change, risk, review, or evidence link]` |

### 3.8 Disposition

| **Field** | **Value** |
|---|---|
| Current Disposition | `[Approved / Approved with conditions / Pilot / Blocked pending remediation / Suspended / Retired]` |
| Conditions of Use | `[Conditions]` |
| Maximum Approved Data Classification | `[Public / Internal / Confidential / Restricted]` |
| Consequential Decision Use Approved? | `[Yes / No / Not Applicable with reason]` |
| Review Cadence | `[Quarterly / Semiannual / Annual / On material change]` |
| Next Review Date | `[Date]` |
| Retirement / Rollback Plan | `[Plan or Not Applicable with reason]` |

---

## 4. Review and Maintenance

| **Role** | **Responsibility** |
|---|---|
| Application Security Engineer | Owns register content for built and embedded AI systems; confirms model, software, threat model, and AI-specific security controls. |
| Engineering Pillar Leader | Accountable for architecture review, secure build, and technical disposition of AI systems. |
| Business Owner | Owns business use, consequence, human oversight, and operational acceptance. |
| Governance Pillar Leader | Confirms conformance to approved AI use, evidence expectations, and reporting needs. |
| Vendor Risk Analyst | Confirms provider, model, or vendor-feature assessment where third-party AI services are used. |
| Detection Engineer | Confirms monitoring and detection requirements where AI-system behavior or tool use must be observed. |
| Risk Register Owner | Links material findings, residual risk, exceptions, and acceptance decisions to the risk register. |

A register entry must be reviewed when any of the following occur:

- Model family, model version policy, provider, deployment location, or serving platform changes.
- A new data source, retrieval corpus, vector store, plugin, connector, or downstream action is added.
- The system gains new agency, privilege, autonomous action, or external communication capability.
- The system begins processing Confidential or Restricted data or enters regulated scope.
- A threat model, architecture review, test, incident, vendor reassessment, or audit produces a material finding.
- The CISO, Engineering Pillar Leader, Risk Pillar Leader, or Governance Pillar Leader directs review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-AI-003 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Application Security Engineer |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) - Artificial Intelligence Security Standard |
| **Review Cycle** | Quarterly; and on material change to model, data source, agency, integration, or deployment |
| **Next Scheduled Review** | 2026-09-17 |
| **Frameworks** | NIST AI RMF 100-1 · NIST 800-53r5 CM / RA / SA / SI · OWASP Top 10 for LLM Applications · ISO/IEC 42001 |
| **Regulations** | Cross-cutting; CMMC L2 / 800-171r3, SOX ITGC, privacy, and contractual obligations where applicable |
| **Environments** | Built AI systems, embedded AI systems, AI agents, model-serving platforms, RAG systems, and AI-enabled integrations in CERG-managed environments |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-17 | Cyber Engineering | Initial release. Establishes the AI system and model register template for built and embedded AI systems, including model provenance, data sources, agency boundary, integrations, monitoring, and lifecycle review. |

### Review Triggers

- Parent standard or related procedure change
- Material change to model, provider, data source, retrieval store, agency, integration, deployment location, or regulated scope
- Significant AI-related finding, incident, or audit issue
- New or changed AI regulation
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Artificial Intelligence Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Parent standard; requires models to be inventoried components |
| AI Intake and Sanctioning Template | [`CERG-TMPL-AI-001`](CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) | Intake and approval source for AI system entries |
| Sanctioned AI Tools Register Template | [`CERG-TMPL-AI-002`](CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) | Companion register for consumed AI tools and AI-enabled vendor features |
| Secure Software Development and Application Security Standard | [`CERG-STD-SDL-001`](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) | Governs built AI systems as software |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Governs models as inventoried components |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Governs review of AI systems and integrations |
| Threat Modeling Procedure | [`CERG-PRC-TM-001`](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Defines AI-specific threat model categories |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Governs monitoring of sensitive AI interactions and anomalous AI-system behavior |
