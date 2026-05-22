# SURGE: Cyber Engineering, Risk & Governance
## CERG Risk Management Framework
**Document ID:** CERG-RMF-001 · **Version:** 1.21 · **Classification:** Public

> *A NIST-grounded, operationally adaptive risk management framework designed for IT and OT environments across CMMC, NERC-CIP, and SOX.*

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Framework Architecture](#2-framework-architecture)
3. [Phase 1, Categorize](#3-phase-1--categorize)
4. [Phase 2, Select](#4-phase-2--select)
5. [Phase 3, Implement](#5-phase-3--implement)
6. [Phase 4, Assess](#6-phase-4--assess)
7. [Phase 5, Authorize](#7-phase-5--authorize)
8. [Phase 6, Monitor](#8-phase-6--monitor)
9. [Risk Register and Risk Treatment](#9-risk-register-and-risk-treatment)
10. [IT/OT Risk Management Considerations](#10-itot-risk-management-considerations)
11. [Regulatory Alignment Quick Reference](#11-regulatory-alignment-quick-reference)
12. [Document Control and Review](#12-document-control-and-review)

---

## 1. Purpose and Scope

The CERG Risk Management Framework (CERG-RMF) defines how SURGE, the Cyber Engineering, Risk, and Governance function, identifies, assesses, treats, and monitors cybersecurity risk across the enterprise. It is the connective tissue between the three CERG pillars and the foundational document that gives every risk decision a shared vocabulary, a shared process, and a clear owner.

This framework is purpose-built to:

- Align with NIST RMF Steps 1–6 (Categorize, Select, Implement, Assess, Authorize, Monitor) while making each step operationally practical within CERG's three-pillar model.
- Satisfy the risk management requirements of [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (Adaptive tier), [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Rev 5, [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Rev 3, [CMMC](https://dodcio.defense.gov/CMMC/) Level 2, NERC-CIP, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC simultaneously.
- Apply equally to IT and OT environments, accounting for the operational availability constraints and extended patch windows common in industrial and grid-connected systems.
- Scale from a 5-person team to a 500-person organization without requiring structural changes.

> **Design Intent**
>
> Risk management in CERG is not a periodic checkbox exercise. It is a continuous, adaptive cycle, one that feeds intelligence back into Engineering, drives accountability through Governance, and produces a risk posture the CISO can defend to regulators, auditors, and the board at any point in time.

---

## 2. Framework Architecture

### 2.1 The CERG-RMF Cycle

The CERG Risk Management Framework operates as a continuous cycle, not a linear waterfall. Each phase feeds the next, and intelligence gathered in later phases (Monitor, Assess) loops back to update decisions made in earlier ones (Categorize, Select). This is the structural characteristic that distinguishes an Adaptive-tier program from a Repeatable one.

The six phases map directly to the NIST RMF, with CERG pillar ownership assigned at each step:

| Phase         | NIST RMF Step       | CERG Primary Owner | Supporting Pillars |
| ------------- | ------------------- | ------------------ | ------------------ |
| 1. Categorize | Step 1 - Categorize | Governance         | Engineering, Risk  |
| 2. Select     | Step 2 - Select     | Governance         | Engineering        |
| 3. Implement  | Step 3 - Implement  | Engineering        | Governance         |
| 4. Assess     | Step 4 - Assess     | Risk               | Governance         |
| 5. Authorize  | Step 5 - Authorize  | Governance         | Risk, Engineering  |
| 6. Monitor    | Step 6 - Monitor    | Risk + Governance  | Engineering        |

### 2.2 [NIST CSF](https://www.nist.gov/cyberframework) Function Mapping

[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) defines six functions. The CERG-RMF operationalizes all six within the risk cycle:

| [CSF](https://www.nist.gov/cyberframework) Function | CERG-RMF Phase(s) | What CERG Does |
|---|---|---|
| **GOVERN** | Categorize, Authorize | Sets risk strategy, risk appetite, and accountability structures. Maintains policy hierarchy that governs all risk decisions. |
| **IDENTIFY** | Categorize, Assess | Maintains asset inventories and system categorization. Conducts risk assessments, threat modeling, and vendor risk reviews. |
| **PROTECT** | Select, Implement | Engineering designs and deploys protective controls per selected baselines. Governance sets the standard; Risk validates effectiveness. |
| **DETECT** | Monitor, Assess | Risk operates vulnerability scanning, threat intelligence, and anomaly detection. Feeds findings to IR and Governance continuously. |
| **RESPOND** | Monitor (IR hand-off) | Risk provides threat context during incidents. Governance owns playbook library and post-incident documentation. |
| **RECOVER** | Monitor (lessons learned) | Governance captures lessons learned and drives improvement tracking. Engineering supports architectural changes post-incident. |

---

## 3. Phase 1: Categorize

### 3.1 Objective

Categorization establishes the impact level of each system and data type, the foundation for every subsequent risk decision. A system that is improperly categorized will be under-controlled or over-controlled; neither outcome is acceptable.

### 3.2 What Gets Categorized

- All information systems and technology assets (IT and OT) that store, process, or transmit organizational data or perform operational functions.
- Data types by confidentiality, integrity, and availability (CIA) impact: Low, Medium, or High, per FIPS 199 / [NIST 800-60](https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final).
- Operational Technology systems are categorized with additional consideration for Safety, Reliability, and Continuity impacts, recognizing that an OT system failure may carry consequences beyond information loss.

> **OT Categorization Note**
>
> For OT environments, including BES Cyber Systems under NERC-CIP and ICS/SCADA systems in manufacturing or utilities, availability and integrity are typically the dominant impact categories. Confidentiality, while important, is often secondary to the consequences of a system outage or process manipulation. Categorization must reflect this reality, and control selection must weight accordingly.

### 3.3 CERG Roles in Categorization

| Pillar | Categorization Responsibility |
|---|---|
| **Governance** | Leads the categorization process. Maintains the system categorization register. Ensures regulatory designations (BES Cyber System, CUI scope, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) scope) are documented and current. Coordinates annual review. |
| **Engineering** | Provides technical input on system function, data flows, interconnections, and dependencies. Produces or confirms asset documentation at project handoff. |
| **Risk** | Validates asset inventory completeness via scan coverage. Identifies systems that may be missing from the register. Contributes threat context to impact analysis. |

### 3.4 Categorization Outputs

- **System Categorization Register**: master list of all in-scope systems with CIA impact ratings, regulatory designations, and assigned asset owners.
- **Data Classification Map**: inventory of data types by sensitivity level, mapped to the systems that handle them.
- **Regulatory Scope Declarations**: explicit documentation of which systems are in-scope for NERC-CIP (BES/EACMS/PACS), [CMMC](https://dodcio.defense.gov/CMMC/) (CUI enclave), and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC.

### 3.5 Regulatory Alignment: Categorize

| Framework | Categorization Requirement | CERG Satisfies Via |
|---|---|---|
| NIST RMF | Step 1: Categorize the system using FIPS 199 / [NIST 800-60](https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final) | System Categorization Register; CIA impact ratings per asset |
| [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | RA-2: Security Categorization | Governance-maintained categorization register reviewed annually |
| NERC-CIP | CIP-002: BES Cyber System identification and categorization (High/Medium/Low) | Governance leads CIP-002 process; Engineering validates connectivity; Risk confirms inventory |
| [CMMC](https://dodcio.defense.gov/CMMC/) | All 14 domains require defined CUI scope | CUI enclave declaration maintained by Governance; boundary confirmed by Engineering |
| [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) | ITGC scoping: identify systems that support financial reporting | Governance maintains [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC system register in coordination with Finance and Internal Audit |

---

## 4. Phase 2: Select

### 4.1 Objective

Control selection translates categorization outputs into a tailored set of security controls appropriate to the system's impact level, operating environment (IT vs OT), and applicable regulatory requirements. Governance leads selection; Engineering translates selected controls into technical implementation requirements.

### 4.2 Control Baseline Structure

CERG uses a layered baseline model. Every system inherits the Organizational Baseline. Systems with elevated categorization or regulatory scope inherit additional overlay controls:

| Baseline Layer | Applies To | Primary Source |
|---|---|---|
| **Organizational Baseline** | All systems | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Rev 5 Moderate baseline; [NIST CSF](https://www.nist.gov/cyberframework) Subcategories |
| **High Impact Overlay** | Systems with any High CIA impact rating | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) High baseline additions |
| **CUI Overlay** | Systems handling Controlled Unclassified Information | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Rev 3 |
| **BES Overlay** | BES Cyber Systems, EACMs, PACSs | NERC-CIP CIP-002 through CIP-014 |
| **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC Overlay** | Systems supporting financial reporting | COSO/ITGC: Change management, access, availability |
| **OT Safety Overlay** | ICS/SCADA with safety implications | IEC 62443 + [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) supplemental controls |

> **The Overlay Principle**
>
> Overlays do not restart the control selection process, they add to the organizational baseline. A system in both the CUI scope and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) scope carries the organizational baseline plus both applicable overlays. Governance tracks the combined control set per system; Engineering implements it. This prevents the "compliance tunnel vision" problem where teams optimize for one framework and inadvertently create gaps in another.

### 4.3 Tailoring and Scoping

Not every control applies equally to every system. CERG's tailoring process allows for three types of adjustments, all of which require documentation and, above a threshold, CISO or Risk approval:

| Tailoring Action | Definition | Approval Required |
|---|---|---|
| **Compensating Control** | An alternative control that meets the intent of the baseline control when the standard control cannot be implemented (common in OT environments) | Risk assessment + Risk Manager approval |
| **Control Enhancement** | Additional control implementation above baseline, based on threat intelligence or risk assessment findings | Engineering + Governance alignment |
| **Exception / Deviation** | Documented acknowledgment that a control cannot be satisfied; requires compensating controls and risk acceptance | Per the canonical Risk Acceptance Authority table in [§9.4](#94-risk-acceptance-authority) |

---

## 5. Phase 3: Implement

### 5.1 Objective

Implementation translates selected controls into working technical and administrative safeguards. In CERG, implementation is Engineering's domain, but it is not Engineering's burden alone. Governance provides the standard; Risk validates the result.

### 5.2 Engineering's Implementation Model

Cyber Engineering operates as an internal consulting function. Engineers embed with IT and business project teams early, before architecture decisions are locked, and ensure that security controls are designed in, not bolted on after the fact.

| Project Stage | Engineering Role | CERG-RMF Output |
|---|---|---|
| **Concept / Requirements** | Engage at business requirements stage. Identify regulatory scope and control obligations. Flag OT safety considerations early. | Preliminary security requirements documented in project charter. |
| **Design / Architecture** | Review proposed architecture. Validate that selected controls are achievable in the design. Identify gaps and drive remediation before build begins. | Security architecture review (SAR) findings; control gap list. |
| **Build / Configure** | Provide hands-on implementation support. Produce or validate configuration baselines. Document control implementation for evidence library. | Configuration baselines; implementation records for Governance evidence library. |
| **Pre-Production** | Coordinate pre-production Risk assessment (vulnerability scan, architecture review). Confirm open findings are remediated or risk-accepted. | Pre-production sign-off; open risk items transferred to risk register. |
| **Production Handoff** | Produce handoff documentation: asset registration, baseline, control mapping, open risks. Transfer ongoing oversight to Risk and Governance. | Handoff package; asset added to categorization register. |

### 5.3 Implementation Standards

Engineering implements controls to the following baselines, maintained as living standards by Governance:

- **CIS Benchmarks** (Level 1 minimum, Level 2 for High-impact and BES systems) for server, endpoint, and network device hardening.
- **[NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final)** supplemental guidance for OT and ICS system hardening, recognizing that CIS benchmarks may not directly apply to industrial control systems.
- **Organizational configuration baselines** maintained per platform class (Windows Server, Linux, network infrastructure, cloud, OT/ICS), version-controlled by Governance.
- **Zero-trust architecture principles** for network segmentation, identity verification, and least-privilege access, applicable to both IT and OT network boundaries.

> **OT Implementation Reality**
>
> In OT environments, "implement the control" and "deploy the patch" are not always immediately achievable. Operational availability requirements, vendor support limitations, and safety system constraints mean that some controls require compensating measures and extended implementation timelines. CERG's risk register and exception process exist precisely for this situation. Engineering documents the gap, Risk assesses the exposure, and Governance records the compensating controls and target remediation date. For NERC-CIP environments, this triggers the deviation and mitigation plan process.

---

## 6. Phase 4: Assess

### 6.1 Objective

Assessment validates that implemented controls are working as intended. In CERG, assessment is Cyber Risk's core function, executed continuously through vulnerability management and threat intelligence, and periodically through structured security assessments and penetration testing.

### 6.2 Assessment Portfolio

| Assessment Type | Frequency | Pillar Owner | Primary Output |
|---|---|---|---|
| **Continuous Vulnerability Scanning** | Continuous (authenticated scan weekly; unauthenticated daily) | Risk | Prioritized finding register with SLA tracking; remediation evidence. |
| **OT / ICS Vulnerability Assessment** | Quarterly minimum; OT-safe passive scanning methods | Risk + Engineering | OT-specific finding register; compensating control documentation for unpatchable findings. |
| **Penetration Testing - External** | Annual minimum; after significant architecture changes | Risk (internal) / Third Party | Pen test report; findings tracked to closure with Engineering review. |
| **Penetration Testing - Internal** | Annual minimum; includes lateral movement and privilege escalation testing | Risk | Internal pen test report; architecture remediation recommendations for Engineering. |
| **OT / ICS Red Team** | Biennial minimum (or as required by NERC-CIP or contract) | Risk + Third Party | Red team report; OT-specific findings require CISO review before disclosure. |
| **Vendor / Third-Party Risk Assessment** | At onboarding; annually for Critical vendors; triggered by incidents or contract changes | Risk | Vendor risk rating; contract risk terms; ongoing monitoring requirements. |
| **Security Control Assessment (SCA)** | Annual; scope aligned to regulatory cycle | Risk + Governance | SCA report; POA&M updates; evidence for authorization decision. |
| **Threat Intelligence Review** | Continuous ingestion; structured analysis weekly; strategic briefing monthly | Risk | Threat intel products: tactical (IOCs), operational (TTPs), strategic (threat landscape). |

### 6.3 Finding Severity and SLAs

All findings from assessment activities are assigned a severity rating and a remediation SLA. Exceptions to SLAs require documented risk acceptance per the process in [§9.4](#94-risk-acceptance-authority).

The authoritative remediation-SLA table lives in [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) §5. The values published there govern every CERG-managed scan, pen test, and assessment finding across IT, cloud, SaaS, and (with the BES schedule overlay) OT environments. Pillar dashboards and KRIs in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) measure compliance against PRC-VM-001's SLA values, not against a separate table.

> **One Source of Truth**
>
> Earlier drafts of this document carried a parallel SLA table. That table has been retired so that there is exactly one place in the library where a remediation SLA can be changed. If you find a stale SLA citation in another document, the corrective action is to update the citing document to point at PRC-VM-001 — not to restate the values.

---

## 7. Phase 5: Authorize

### 7.1 Objective

Authorization is a formal risk acceptance decision made by an accountable leader before a system is allowed to operate or continue operating. It is the point at which residual risk is explicitly acknowledged, owned, and documented. In CERG, Governance structures and manages the authorization process; the CISO is the primary Authorizing Official (AO) for the cybersecurity program.

### 7.2 Authorization Decision Types

| Decision Type | When Applied | Authorizing Authority |
|---|---|---|
| **Authority to Operate (ATO)** | New systems entering production after pre-production assessment. Full ATO requires all High and Critical findings resolved or risk-accepted. | CISO (with Risk and Engineering concurrence) |
| **Interim Authority to Operate (IATO)** | Systems with residual High findings that have documented compensating controls and an approved remediation timeline (maximum 90 days). OT systems with constrained patch windows may require IATO. | CISO; must include documented compensating controls and target full ATO date |
| **Denial of Authorization (DATO)** | Systems where residual risk exceeds the organization's risk appetite and compensating controls are insufficient. System must be isolated or decommissioned. | CISO (mandatory notification to CEO and Board for business-critical systems) |
| **Ongoing Authorization** | Systems with continuous monitoring in place that demonstrate consistent control effectiveness. Replaces periodic point-in-time reauthorization for mature, stable systems. | CISO with quarterly Risk and Governance attestation |

### 7.3 Authorization Package Contents

Governance assembles the authorization package for CISO review. A complete package includes:

- **System Security Plan (SSP)**: documents system boundary, categorization, control implementation status, and responsible parties.
- **Risk Assessment Report (RAR)**: Risk-produced finding report from pre-authorization assessment activities.
- **Plan of Action and Milestones (POA&M)**: documents all open findings with owners, compensating controls, and target remediation dates.
- **Continuous Monitoring Strategy**: defines ongoing monitoring activities that will maintain risk visibility post-authorization.
- **Regulatory Compliance Attestation**: Governance attestation that applicable regulatory controls are satisfied or that deviations are documented per regulatory process.

> **Authorizing OT Systems**
>
> For OT and BES Cyber Systems, authorization must explicitly address operational continuity risk alongside cybersecurity risk. A finding that would result in DATO for an IT system (e.g., unpatched Critical vulnerability) may result in IATO for a BES system if immediate isolation would cause a reliability event. The NERC-CIP deviation and mitigation plan process must be initiated in parallel. The CISO coordinates with Operations leadership and, where required, the Reliability Coordinator.

---

## 8. Phase 6: Monitor

### 8.1 Objective

Continuous monitoring is the phase that separates Adaptive-tier programs from Repeatable ones. It is not a periodic review, it is an always-on operational posture that keeps the organization's risk picture current, feeds intelligence back into earlier RMF phases, and provides the CISO with real-time awareness of the organization's exposure.

### 8.2 Monitoring Program Components

| Component | Pillar Owner | Frequency | Output / Deliverable |
|---|---|---|---|
| Vulnerability scan coverage | Risk | Continuous | Updated finding register; SLA tracking dashboard; escalation alerts for Critical findings. |
| Configuration drift detection | Risk + Engineering | Continuous (automated) | Drift alerts to Engineering; deviation from baseline triggers change management review. |
| Threat intelligence ingestion | Risk | Continuous; structured analysis weekly | Tactical threat products (IOCs); operational advisories; strategic threat briefings for CISO. |
| Risk register review | Governance | Monthly (full); weekly (high/critical items) | Updated risk register with treatment status; escalation to CISO for items approaching SLA. |
| POA&M status tracking | Governance | Biweekly | POA&M status report; owner accountability communications; escalation for missed milestones. |
| Control effectiveness review | Risk + Governance | Quarterly | Control testing results; evidence library updates; findings fed into next SCA cycle. |
| Compliance calendar execution | Governance | Per regulatory schedule | Regulatory submissions, evidence packages, audit coordination, deviation filings. |
| Vendor and supply chain monitoring | Risk | Continuous (automated); quarterly structured review | Vendor risk rating updates; notification of third-party breaches or advisories. |
| CISO risk dashboard | Governance + Risk | Weekly refresh; real-time for Critical events | Executive risk posture summary; KRI trending; board-ready quarterly summary. |

### 8.3 Key Risk Indicators (KRIs)

| KRI | Target | Owner | Escalation Trigger |
|---|---|---|---|
| Mean Time to Remediate - PPR (0-day) | ≤48 hours (Internet-facing) / ≤72 hours (internal) per [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) §5 | Risk | Any PPR finding past SLA |
| Mean Time to Remediate - Critical | ≤3 days per [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) §5 | Risk | Any Critical past SLA without documented compensating control |
| Mean Time to Remediate - High | ≤15 days per [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) §5 | Risk | Any High past SLA without approved exception |
| Scan Coverage - IT | ≥98% of known assets | Risk | <95% coverage |
| Scan Coverage - OT | ≥90% of known assets (passive methods) | Risk | <85% coverage |
| Open Critical/High Findings | 0 Critical past SLA; <10 High past SLA | Risk + Governance | Any Critical past SLA; >10 High past SLA |
| Risk Register Items Past Target Date | 0 items past target date | Governance | Any item >30 days past target; CISO briefing required if more than 3 items are past target at the monthly Risk Posture Review |
| Policy Review Compliance | 100% of policies reviewed within defined cycle | Governance | Any policy >12 months since last review |
| SSP / Authorization Currency | 100% of in-scope systems with current ATO/IATO | Governance | Any in-scope system without current authorization |
| Vendor Risk Assessments Current | ≥95% of Critical vendors with current assessment | Risk | <90% triggers escalation |
| Security Training Completion | ≥95% completion within defined window | Governance (coord w/ Awareness) | <90% completion triggers escalation to CISO |

---

## 9. Risk Register and Risk Treatment

### 9.1 The Risk Register

The CERG Risk Register is the authoritative record of all identified, assessed, and tracked cybersecurity risks. It is owned by Governance, populated by Risk, and informed by Engineering. It is not a spreadsheet that lives on a network share, it is a living operational tool that drives accountability and informs every authorization decision.

### 9.2 Risk Statement Format (FAIR-Aligned)

Every risk entered into the register is written in a single, consistent statement format derived from the FAIR (Factor Analysis of Information Risk) model. FAIR decomposes risk into a Loss Event Frequency (LEF) and a Loss Magnitude (LM); the CERG statement format makes both halves explicit so that every register entry can be reasoned about, compared, and rolled up the same way.

**Canonical risk statement:**

> *"[Threat community] using [threat action / vector] against [affected asset / scope] could result in [primary and secondary loss types] of [loss magnitude range], at an estimated frequency of [LEF range]."*

**Components:**

| Component | What It Captures | Examples |
|---|---|---|
| **Threat community** | Who or what is initiating the loss event (FAIR Threat Community). See §9.3. | Organized cybercriminal, nation-state, malicious insider, negligent insider, third-party supply chain |
| **Threat action / vector** | How the loss event is initiated | Ransomware, credential stuffing, phishing, exploitation of unpatched CVE, lateral movement from compromised vendor |
| **Affected asset / scope** | What is harmed and the scope of harm | The CUI enclave, a specific BES Cyber System, the SOX-relevant ERP, the corporate identity store |
| **Loss types** | One or more of FAIR's six primary loss forms | Productivity, response, replacement, fines and judgments, competitive advantage, reputation |
| **Loss magnitude range** | Expected loss as a calibrated range (PERT min / most likely / max) | $250K - $1.5M - $4M |
| **LEF range** | Expected frequency the loss event occurs in a year (PERT min / most likely / max) | 0.05 - 0.15 - 0.4 (i.e., once every 2 to 20 years) |

Risk statements that cannot be written in this form are not yet risks; they are observations or findings. Findings remain in the vulnerability or assessment register until they can be expressed in a complete loss-event scenario, at which point they are promoted to the Risk Register.

### 9.3 Threat Community Reference

The FAIR Threat Community is the actor or natural force that initiates a loss event. The taxonomy below is the CERG default. Subordinate documents — particularly [`CERG Risk Taxonomy`](CERG%20Risk%20Taxonomy.md) — extend it with sector-specific actors (e.g., ICS-targeted APTs for OT).

| Community | Examples | Primary Loss Forms |
|---|---|---|
| **Nation-state / APT** | State-aligned threat actors with strategic objectives (intellectual property, infrastructure pre-positioning) | Replacement, competitive advantage, response, reputation |
| **Organized cybercriminal** | Financially motivated groups (ransomware, BEC, fraud) | Response, replacement, productivity, fines and judgments |
| **Hacktivist** | Ideologically motivated; disruption and disclosure | Reputation, productivity, response |
| **Malicious insider** | Authorized user acting against the organization | Replacement, competitive advantage, fines and judgments |
| **Negligent insider** | Authorized user causing loss through error or policy violation | Productivity, response, fines and judgments |
| **Third-party / supply chain** | Trusted vendor or service compromised, propagating to the organization | Response, productivity, fines and judgments |
| **Non-malicious (environmental)** | Natural events, infrastructure failures, accidental conditions | Productivity, replacement, response |

### 9.4 Risk Register Data Elements

| Field | Description |
|---|---|
| **Risk ID** | Unique identifier (format: CERG-RISK-YYYY-NNN) |
| **Source** | How the risk was identified: vulnerability scan, pen test, threat intel, vendor assessment, audit, self-identification, or incident. |
| **Affected System(s)** | System(s) or asset(s) associated with the risk, with regulatory designation (BES/CUI/SOX) noted. |
| **Risk Statement** | The canonical FAIR-aligned statement per §9.2. |
| **Threat Community** | Selected from §9.3 (one primary; additional secondaries permitted). |
| **Threat Action / Vector** | How the loss event is initiated. |
| **Loss Types** | One or more of: productivity, response, replacement, fines and judgments, competitive advantage, reputation. |
| **Likelihood (LEF)** | Rated using the band table in §9.5; supported by a PERT range where calibration data exists. |
| **Impact (LM)** | Rated using the band table in §9.5; supported by a PERT range where calibration data exists. |
| **Overall Severity** | Composite severity rating per §9.5: Critical / High / Medium / Low / Informational. |
| **Risk Owner** | Accountable leader (business unit or IT/OT operations) responsible for risk treatment decision. |
| **Treatment Decision** | Remediate / Mitigate / Transfer / Accept - with documented rationale per §9.6. |
| **Compensating Controls** | Controls in place that reduce exposure while the primary risk remains open. |
| **Target Remediation Date** | Committed date for risk closure or next status review. |
| **Approval** | Authority approving the treatment decision; date; reference to the canonical authority table at §9.7. |
| **Status** | Approved |
| **Regulatory Implication** | Whether the risk has regulatory reporting, deviation, or mitigation plan implications (NERC-CIP, CMMC, SOX). |

### 9.5 Likelihood, Impact, and Severity Bands

CERG uses a 5x5 model: likelihood and impact are each rated 1-5, scored, and mapped to a severity band. The bands below are the canonical CERG model. Every CERG document that scores risk must produce the same severity rating as this table.

**Likelihood (LEF) bands.** Calibrated as expected loss events per year. Tune the numeric ranges against your loss-event history; the band labels are fixed.

| Score | Label | Annualized Frequency |
|---|---|---|
| 5 | Very High | >10 events / year |
| 4 | High | 1 - 10 events / year |
| 3 | Medium | 1 event / 1 - 10 years |
| 2 | Low | 1 event / 10 - 100 years |
| 1 | Very Low | <1 event / 100 years |

**Impact (LM) bands.** Calibrated against organizational loss-magnitude reference points. Placeholder dollar bands are provided as starting calibration; the Risk pillar lead refreshes annually with Finance.

| Score | Label | Loss Magnitude (Placeholder) |
|---|---|---|
| 5 | Catastrophic | >$10M single-event loss; material to financial statements; sustained reputation damage |
| 4 | Major | $1M - $10M single-event loss; regulatory enforcement action; significant reputation damage |
| 3 | Medium | $100K - $1M single-event loss; reportable to leadership; limited reputation impact |
| 2 | Minor | $10K - $100K single-event loss; absorbed within normal operating costs |
| 1 | Negligible | <$10K single-event loss; no leadership notification required |

**Composite severity.** Likelihood score x Impact score = Severity score; mapped to band.

| Severity Score | Severity Band |
|---|---|
| 20 - 25 | **Critical** |
| 12 - 19 | **High** |
| 6 - 11 | **Medium** |
| 2 - 5 | **Low** |
| 1 | **Informational** |

### 9.6 Risk Treatment Options

| Treatment | Definition | When Appropriate | CERG Process |
|---|---|---|---|
| **Remediate** | Eliminate the risk by removing the vulnerability, threat source, or exposure. | When technically feasible within a reasonable timeframe and at proportionate cost. | Engineering leads technical remediation. Risk verifies closure via rescan or retest. Governance closes the risk register item. |
| **Mitigate** | Reduce the likelihood or impact of the risk to an acceptable level through compensating controls. | When full remediation is not immediately feasible (common in OT); when residual risk after mitigation falls within risk appetite. | Engineering implements compensating controls. Risk validates control effectiveness. Governance documents and tracks to eventual remediation. |
| **Transfer** | Shift the financial impact of the risk through insurance or contractual liability provisions. | For risks where cyber insurance coverage is appropriate and available. | Governance coordinates with Legal/Finance for contract and insurance language. Risk quantifies the risk for insurance submission. |
| **Accept** | Formally acknowledge and document the risk without further treatment, when residual risk falls within risk appetite. | For Low/Informational risks where cost of treatment exceeds the risk value; or when all other options have been exhausted and the risk owner is willing to own the consequence. | Requires documented approval at the authority level defined by severity (§9.7). Risk provides a written risk finding. Governance records the acceptance in the risk register. |

### 9.7 Risk Acceptance Authority (Canonical)

This table is the single source of truth for who may accept residual risk. Every other CERG document that references acceptance authority points at this section.

| Severity | Acceptance Authority | Notification | Required Documentation | Maximum Acceptance Duration |
|---|---|---|---|---|
| **Critical** | CISO with Executive Sponsor concurrence | CEO notified; Board notification at next quarterly cycle (or sooner if systemic) | Risk assessment, compensating controls, business justification, target remediation date | 12 months; renewal requires fresh approval cycle |
| **High** | CISO | Executive Sponsor notified | Risk assessment, compensating controls, business justification, target remediation date | 12 months; renewal requires fresh approval cycle |
| **Medium** | Risk Pillar Leader (Risk pillar lead) | CISO informed at monthly Risk Posture Review | Risk assessment, compensating controls, target remediation date | 12 months |
| **Low** | Governance Pillar Leader | Tracked in monthly Risk Register report | Brief justification; tracked in risk register | 12 months |
| **Informational** | Cyber Governance (Risk Register Owner) | Tracked in quarterly trending report | Tracked in risk register | Reviewed annually |

> **Renewals**
>
> No acceptance renews automatically. An acceptance at any tier requires a fresh approval cycle at expiration. An acceptance renewed more than twice without movement on the treatment plan escalates one tier above the original approver.

> **Role names** below match the canonical roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1. If a role name disagrees with that roster, the roster wins.

### 9.8 Risk Appetite and Tolerance

CERG's risk appetite is expressed in two complementary ways: a qualitative posture statement that informs every treatment decision, and a quantitative loss-exposure tolerance that anchors acceptance decisions at the Critical and High bands. The CISO maintains both; the Board reviews appetite annually.

**Qualitative posture.** CERG operates under a "Yes, And…" orientation: the default response to a business request is "yes, and here are the conditions that make this safe." Reflexive refusal is not an acceptable risk management strategy. At the same time, three categories receive a deliberately low appetite:

| Category | Appetite |
|---|---|
| Loss of life, physical safety, or grid reliability | **None.** Any credible scenario triggers immediate Critical treatment regardless of LEF or LM scoring. |
| Material loss of CUI or DFARS-regulated data | **Very Low.** Treatment defaults to Remediate; Accept requires CISO + Executive Sponsor + 90-day re-review. |
| Material misstatement of SOX-relevant financial data caused by ITGC failure | **Very Low.** Treatment defaults to Remediate; Accept requires CISO + Executive Sponsor + Audit Committee notification. |
| Operational disruption to enterprise IT services | Medium. Treatment chosen on a cost / business value basis. |
| Loss of low-sensitivity, broadly available data | Higher. Acceptance is appropriate where treatment cost exceeds loss magnitude. |

**Quantitative tolerance (placeholder calibration).** Annualized Loss Exposure (ALE = LEF x LM) is summed across the open risk register quarterly. CERG operates against the following exposure bands while Finance/Treasury finalizes calibrated values. The CISO updates these in coordination with the CFO at the next CERG/Finance joint review.

| Posture Indicator | Value | Action |
|---|---|---|
| Total open ALE (Critical + High) | <$5M (placeholder) | Within appetite; continue normal monitoring |
| Total open ALE (Critical + High) | $5M - $15M (placeholder) | Within tolerance; CISO briefs Cyber Oversight Group monthly |
| Total open ALE (Critical + High) | >$15M (placeholder) | Above tolerance; CISO briefs Board at the next cycle; mandatory treatment plan within 60 days |
| Single-risk ALE | >$2M (placeholder) | Mandatory CISO review at acceptance; auto-escalates to High at minimum |

> **Calibration is the work.** Numbers above are starting placeholders; they are not approved appetites until Finance signs the calibration. The pattern - qualitative posture per category plus quantitative ALE bands - is the part that does not change.

### 9.9 Worked Example: Risk Register Entry

The example below shows a single register entry written in the canonical format. Fields not relevant to the scenario are marked n/a; everything else is filled in as it would appear in the live register.

```
Risk ID:                 CERG-RISK-2026-0142
Source:                  Pre-production assessment - substation modernization project
Affected System(s):      Substation Gateway "EAST-SS-04" (BES Cyber System, Medium Impact);
                         vendor remote-access path through the EACMS jump server.
Risk Statement:          Organized cybercriminal threat communities using ransomware
                         delivered via a compromised vendor remote-access path against the
                         EAST-SS-04 BES Cyber System could result in productivity loss,
                         response costs, replacement costs, and NERC reliability fines of
                         $1.2M - $3.5M - $8.0M, at an estimated frequency of
                         0.05 - 0.12 - 0.25 events per year.
Threat Community:        Organized cybercriminal (primary); third-party / supply chain (secondary)
Threat Action / Vector:  Ransomware via compromised vendor remote-access path
Loss Types:              Productivity, response, replacement, fines and judgments
Likelihood (LEF):        Score 3 (Medium) - 0.12 events / year most-likely
Impact (LM):             Score 4 (Major) - $3.5M most-likely
Overall Severity:        Score 12 - HIGH
Risk Owner:              VP, Transmission Operations
Treatment Decision:      Mitigate (vendor MFA hardening + session brokering + read-only
                         engineering connection until vendor remediation completes)
Compensating Controls:   PAM session recording on EACMS; deny-by-default on inbound
                         vendor address space outside maintenance windows; passive OT
                         detection on E/W traffic from EACMS
Target Remediation Date: 2026-09-30
Approval:                CISO per §9.7 (HIGH severity); acceptance recorded 2026-05-15
Status:                  In Remediation
Regulatory Implication:  NERC-CIP CIP-005 R2, CIP-013 supply chain; CIP deviation not
                         required because compensating controls maintain ESP integrity.
```

---

## 10. IT/OT Risk Management Considerations

### 10.1 Why OT Requires a Different Lens

IT and OT environments share the same fundamental risk equation - threats, vulnerabilities, and consequences - but OT environments introduce constraints that require deliberate adaptation of standard risk management practices. Availability is not a configuration preference in a power grid or a manufacturing line; it is a safety and reliability imperative that can carry regulatory, legal, and physical-world consequences.

CERG's RMF is designed from the ground up to respect this reality. OT-specific adaptations are documented below.

| RMF Phase | Standard IT Approach | OT Adaptation |
|---|---|---|
| **Categorize** | CIA-based impact ratings per FIPS 199 | Add Safety and Reliability as explicit impact dimensions. BES Cyber Systems classified per CIP-002 High/Medium/Low impact in addition to FIPS 199 ratings. |
| **Select** | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Moderate/High baseline | Apply OT Safety Overlay: IEC 62443 practices; [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) supplemental controls; vendor-specific hardening where CIS benchmarks don't apply. |
| **Implement** | Patch and configure to baseline | OT patch windows are defined by operational schedules (planned outages, maintenance windows). Compensating controls bridge the gap. No emergency patching without operations and safety sign-off. |
| **Assess** | Authenticated vulnerability scans; penetration testing | OT scans use passive/OT-safe methods to avoid disrupting process operations. Active scanning requires operations coordination and maintenance window scheduling. |
| **Authorize** | ATO/IATO per residual risk | OT authorization explicitly documents operational availability risk alongside cybersecurity risk. NERC-CIP deviation process runs in parallel for BES systems. |
| **Monitor** | Continuous automated monitoring | OT monitoring uses passive network visibility tools (e.g., Dragos, Claroty, Nozomi). Change management is stricter; unauthorized changes carry safety implications. |

> **The OT Risk Principle**
>
> An unpatched vulnerability in a BES Cyber System is a real risk. An unplanned outage of a BES Cyber System is also a real risk - one that carries NERC reliability implications, potential regulatory fines, and public safety consequences. CERG's risk management process treats both risks seriously and documents the tradeoff explicitly. The CISO owns the cybersecurity risk. Operations leadership owns the reliability risk. Both sign the authorization.

---

## 11. Regulatory Alignment Quick Reference

The CERG-RMF satisfies the risk management requirements of all applicable frameworks. The table below maps each framework's risk-specific requirements to the CERG-RMF phase and CERG pillar that addresses them.

| Framework | Risk Management Requirement | CERG-RMF Phase | Pillar |
|---|---|---|---|
| **NIST RMF** | Steps 1-6: Categorize, Select, Implement, Assess, Authorize, Monitor | All phases | All pillars |
| **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | GOVERN: Risk strategy, risk appetite, accountability structures | Phase 5 (Authorize) | Governance |
| **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | IDENTIFY: Asset management, risk assessment, improvement | Phases 1, 4, 6 | Risk + Governance |
| **[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | RA-2, RA-3, RA-5, CA-2, CA-5, CA-7 (Categorization, Risk Assessment, Vuln Monitoring, Control Assessments, POA&M, Continuous Monitoring) | All phases | Risk + Governance |
| **[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Rev 3** | 03.11 Risk Assessment family; 03.12 Security Assessment family; all documentation requirements | Phases 1, 4, 5, 6 | Risk + Governance |
| **NERC-CIP** | CIP-002: BES Cyber System categorization; CIP-007 R2: Patch management cadence; CIP-010 R3: Vulnerability assessments; deviation and mitigation plan process | Phases 1, 4, 6 | Governance + Risk |
| **CMMC Level 2** | RA.L2-3.11.1, RA.L2-3.11.2; CA.L2-3.12.1; all 110 practices documented in SSP and POA&M | Phases 1, 4, 5, 6 | Risk + Governance |
| **SOX ITGC** | Change management controls; access controls; IT availability controls; ITGC control assessment and evidence | Phases 4, 5, 6 | Governance + Engineering |

---

## 12. Document Control and Review

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-RMF-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-01 |
| **Classification** | Internal / Restricted |
| **Document Owner** | Cyber Governance (CERG Pillar) |
| **Approved By** | Chief Information Security Officer |
| **Review Cycle** | Annual; triggered by significant regulatory change or organizational change |
| **Next Scheduled Review** | 2027-05-01 |
| **Parent Document** | [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) - CERG Cybersecurity Policy |
| **Related Documents** | [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) · [`CERG-GOV-TAX-001`](CERG%20Risk%20Taxonomy.md) · [`CERG-GOV-CMX-001`](CERG%20Compliance%20Matrix.md) · [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · System Security Plans (per system) · Plan of Action and Milestones (per system) |

### Revision History

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0 | 2026-05-01 | Cyber Governance | Initial release. Establishes the CERG-RMF cycle, the FAIR-aligned risk statement format, the 5x5 likelihood/impact model, the canonical risk acceptance authority table, and the risk appetite and tolerance posture. Retires the parallel SLA table in favor of the single source of truth in CERG-PRC-VM-001. Adopts canonical ID CERG-GOV-RMF-001 per CERG-GOV-CAT-001 §5.2. |
