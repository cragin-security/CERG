
# SURGE: Cyber Engineering, Risk & Governance

## The CERG Framework

### A Scalable, Adaptive Cybersecurity Operating Model

> Designed for Adaptive [NIST CSF](https://www.nist.gov/cyberframework) maturity. Applicable to IT and OT environments. Calibrated for [CMMC](https://dodcio.defense.gov/CMMC/), NERC-CIP,, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204).
> 
> _For illustrative purposes, examples in this document reference a major electrical utility with 14,000 employees, an equal population of consultants and contractors, and a 60-person CERG team, representing the upper-bound of the framework so readers can scale down to fit their environment._

---

| **Version**        | 1.21 |
| ------------------ | --------- |
| **Status**         | Published |
| **Classification** | Public |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The CERG Operating Model](#2-the-cerg-operating-model)
3. [Cyber Engineering](#3-cyber-engineering)
4. [Cyber Risk](#4-cyber-risk)
5. [Cyber Governance](#5-cyber-governance)
6. [Targeting NIST CSF Adaptive Maturity](#6-targeting-nist-csf-adaptive-maturity)
7. [Regulatory Alignment](#7-regulatory-alignment)
8. [IT/OT Considerations](#8-itot-considerations)
9. [Team Structure and Talent Model](#9-team-structure-and-talent-model)
10. [Getting Started, The Path to Adaptive](#10-getting-started--the-path-to-adaptive)

---

## 1. Executive Summary

Cybersecurity teams of all sizes have struggled with the same structural problem for two decades: fragmented tools, siloed teams, and a culture of "no" that slows the business without meaningfully reducing risk. The CERG framework, Cyber Engineering, Risk, and Governance, is a deliberate answer to that problem.

CERG consolidates the core work of a mature cybersecurity function into three tightly coupled, clearly bounded pillars. Together they are pronounced **"Surge"**, because effective security is fast, powerful, and directional. Surge is not a support function. It is an operational force that enables the business to move confidently.

### Why Three Pillars

Most cybersecurity work, outside of Security Awareness and Incident Response, falls naturally into one of three activities:

- **Building and deploying secure technology** alongside the business
- **Assessing exposure and managing risk** continuously
- **Setting standards, ensuring compliance, and tracking conformance**

The CERG model names these activities explicitly, Engineering, Risk, and Governance, and assigns clear ownership, accountabilities, and interaction patterns so that work flows between them without dropping and without creating new silos.

### Design Principles

- **Scale up or down:** applicable to a 5-person team or a 500-person organization
- **Regulatory-ready:** designed to satisfy [CMMC](https://dodcio.defense.gov/CMMC/), NERC-CIP, [NIST CSF](https://www.nist.gov/cyberframework), 800-53, 800-171,, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)
- **IT/OT aware:** principles apply equally to enterprise IT and operational technology environments
- **Talent resilient:** cross-pillar knowledge sharing means no single person is a point of failure
- **Adaptive-targeted:** the framework describes what operating at [NIST CSF](https://www.nist.gov/cyberframework) Adaptive maturity looks like in practice
- **"Yes, and..." oriented:** Governance enables the business through risk treatment, not reflexive refusal

---

## 2. The CERG Operating Model

### 2.1 The Full Cybersecurity Team

CERG operates as one of three functional groups within the Cybersecurity department, all reporting to the Chief Information Security Officer (CISO). The full structure is:

|Function|Teams / Scope|
|---|---|
|**SURGE (CERG)**|Engineering · Risk · Governance|
|**Security Awareness**|Training programs · Phishing simulations · Culture campaigns|
|**Incident Response**|SOC / detection · Threat hunting · IR planning & execution|
|**CISO**|Strategy & vision · Executive & board reporting · Budget & resource authority|

> **CERG Scope Note:** This framework focuses on the CERG pillars. Security Awareness and Incident Response are adjacent, equally critical functions with distinct operating models. CERG coordinates closely with both, Engineering embeds security requirements that IR and Awareness depend on; Risk produces threat intelligence that feeds both; Governance sets the standards all three operate under.

### 2.2 The Three Pillars at a Glance

---

#### 🔧 E: Cyber Engineering

**Build securely. Deploy confidently. Consult continuously.**

Internal security consultants who partner with IT and business leaders to design, build, and deploy secure technology across the enterprise, in both IT and OT environments.

---

#### 🔍 R: Cyber Risk

**Know your exposure. Manage it deliberately. Never be surprised.**

Continuous assessment and management of the organization's exposure through vulnerability management, penetration testing, vendor risk assessment, and threat intelligence.

---

#### 📋 G: Cyber Governance

**Set the rules. Track the work. Enable the business to move with confidence.**

The rule-makers, compliance managers, and quality assurance function, responsible for policies, standards, implementation guidance, regulatory compliance, and control evidence.

---

### 2.3 How the Pillars Interact

CERG pillars are not sequential. They operate simultaneously and continuously, with structured handoffs and shared accountability for outcomes.

|Lifecycle Stage|Primary Pillar|Supporting Pillars|
|---|---|---|
|Business requirement / new project|Engineering|Governance sets standards; Risk flags vendor/solution concerns|
|Design and architecture review|Engineering|Risk performs threat modeling and vendor assessment|
|Pre-production vulnerability scan|Risk|Engineering remediates findings pre-launch|
|Risk acceptance (if vuln unresolvable)|Engineering + Risk|Governance provides risk treatment plan template; CISO/leadership signs off on High/Critical|
|Production deployment|Engineering|Governance and Risk assume post-production monitoring|
|Ongoing compliance monitoring|Governance|Risk tracks patch status and emerging CVEs; Engineering supports remediation|
|Audit and evidence collection|Governance|Engineering and Risk produce artifacts from their daily work|
|Penetration test / red team|Risk|Engineering reviews findings for architectural impact; Governance logs findings|
|Regulatory exam or audit|Governance|All pillars provide evidence; Engineering and Risk support responses|

---

## 3. Cyber Engineering

> **Mission:** Build securely. Deploy confidently. Consult continuously.

### 3.1 Mission

The Cyber Engineering team serves as the organization's internal security consulting practice. Engineers are assigned to enterprise and IT projects, often as the first security touch point in a project lifecycle, and carry security requirements, design review, and implementation guidance from concept through production handoff.

Engineers do not own the systems they help build. Their role is to ensure that security is designed in from the beginning, that pre-production findings are remediated or risk-accepted before go-live, and that the receiving operations team understands the security posture of what they are taking on.

### 3.2 Core Functions

- **Project intake and early engagement**: review of business requirements, solution architecture documents, and procurement specifications
- **Security architecture consultation**: participating in design reviews, advising on control selection aligned to [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and organizational standards
- **Pre-production security review**: working with the Risk team to understand vulnerability scan findings and driving remediation with project teams before go-live
- **Risk treatment support**: assisting project teams in drafting risk acceptance documentation and treatment plans when a vulnerability cannot be remediated prior to launch
- **OT/IT convergence advisory**: guiding teams through the security implications of connecting or modernizing operational technology environments
- **Production handoff**: ensuring Governance and Risk have the configuration baseline, asset documentation, and control evidence needed to assume post-production oversight

### 3.3 Engagement Model

Engineering operates on a lightweight internal consulting model. The goal is to minimize administrative overhead and maximize time on engineering work.

|Element|Description|
|---|---|
|Intake|Engineers are engaged via a lightweight request - a brief summary of the project, timeline, and primary contact. No complex ticketing or lengthy intake forms.|
|Assignment|Each engagement is assigned a lead engineer. On large projects, multiple engineers may be assigned. Engineers manage their own capacity with CISO visibility.|
|Engagement scope|Engineers work alongside project teams, not above them. They advise, review, and recommend - the project team retains implementation accountability.|
|Pre-production gate|Before any system or tool goes live, Engineering confirms that open vulnerabilities have been remediated or formally risk-accepted. This is a lightweight confirmation, not a gate that stops work.|
|Handoff documentation|At production cutover, Engineering produces or confirms existence of: asset registration, configuration baseline, control mapping, and any open risk items.|
|Post-production|Once a system is in production, Engineering moves to the next project. Risk and Governance assume ongoing oversight. Engineering may be re-engaged for significant changes.|

### 3.4 Illustrative Example: Electrical Utility

> **Scenario: IT/OT Network Modernization**
> 
> The utility's operations team wants to add remote monitoring capability to its substation SCADA systems. An Engineering team member is engaged at the business requirements stage. They review the vendor's solution architecture, flag the absence of encrypted communications between the historian and the enterprise DMZ, and work with the project team to require TLS enforcement before go-live. The Risk team performs a pre-production scan and finds an unpatched firmware version. Engineering works with the vendor on a patch timeline. When the patch cannot be applied before the project deadline, Engineering helps draft a risk treatment plan with compensating controls, network segmentation, enhanced logging, that Governance reviews for NERC-CIP CIP-005 conformance. VP and CISO sign off. The system goes live with a 90-day remediation commitment documented.

### 3.5 NIST Framework Alignment: Engineering

|NIST Framework|Relevant Controls / Functions|Engineering Role|
|---|---|---|
|[NIST CSF](https://www.nist.gov/cyberframework)|GOVERN, IDENTIFY (Asset Mgmt, Risk Assessment), PROTECT (Identity Mgmt, Data Security, Platform Security)|Primary driver of PROTECT function; co-owner of IDENTIFY|
|[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)|SA (System & Services Acquisition), CM (Configuration Mgmt), SI (System & Info Integrity)|Implements SA and CM controls during project delivery|
|[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)|3.13 System & Communications Protection, 3.14 System & Info Integrity|Ensures CUI protection controls are designed into systems handling federal data|
|NIST RMF|Steps 2 (Select), 3 (Implement), 4 (Assess - pre-production)|Leads control selection and implementation; supports pre-production assessment|
|NERC-CIP|CIP-005 (Electronic Security Perimeters), CIP-007 (Systems Security Mgmt), CIP-010 (Config Mgmt)|Designs systems to conform to CIP requirements from the start|
|[CMMC](https://dodcio.defense.gov/CMMC/)|Level 2: Access Control, Configuration Mgmt, Identification & Auth|Ensures [CMMC](https://dodcio.defense.gov/CMMC/) practices are implemented in applicable systems|

---

## 4. Cyber Risk

> **Mission:** Know your exposure. Manage it deliberately. Never be surprised.

### 4.1 Mission

The Cyber Risk team is responsible for understanding the organization's threat landscape and exposure at all times. Risk does not wait for problems to surface, it hunts for them. Through continuous vulnerability management, periodic penetration testing, vendor risk assessment, and threat intelligence, Risk produces the clearest possible picture of what is threatening the organization and how severe those threats are.

Risk serves both a pre-production function (finding issues before systems go live) and a post-production function (tracking drift, emerging CVEs, and changes in the threat environment after systems are in operation).

### 4.2 Core Functions

- **Vulnerability Management**: continuous scanning of IT and OT environments; prioritization of findings by criticality, exploitability, and asset value; tracking remediation to closure
- **Penetration Testing**: periodic adversarial testing of systems, networks, and applications; coordination of external red team engagements; findings fed back to Engineering and Governance
- **Threat Intelligence**: monitoring of threat actor activity, emerging CVEs, and sector-specific intelligence (including ICS/SCADA threats for OT environments); distribution of actionable intelligence to Engineering, IR, and Governance
- **Vendor and Third-Party Risk**: security review of vendor contracts, SaaS solutions, and third-party integrations; contract redline support for security requirements
- **Pre-Production Assessment**: vulnerability scanning and risk analysis of systems prior to go-live; classification of findings by severity; coordination with Engineering on remediation
- **Risk Treatment and Acceptance**: for findings that cannot be immediately remediated, Risk co-develops treatment plans with Engineering and provides analysis to support leadership sign-off decisions

### 4.3 Pre-Production vs. Post-Production Risk

> **An Important Distinction**
> 
> A vulnerability found in a pre-production system is not a realized risk, the system is not yet live and has not been exposed. The Risk team treats pre-production findings as engineering inputs, working with the Engineering team to drive remediation before launch. Post-production findings are realized risks to be managed, tracked, and reported. This distinction shapes how findings are communicated, prioritized, and escalated.

|Finding Type|Handling|
|---|---|
|Pre-production, Low/Medium severity|Engineering remediates with project team before go-live. Tracked to closure by Risk.|
|Pre-production, High/Critical severity|Engineering and Risk jointly assess. If unremediated, a risk treatment plan is required with VP+ sign-off before go-live.|
|Post-production, Low/Medium severity|Tracked in vulnerability register. Assigned to appropriate owner (IT/OT ops) with SLA. Governance monitors SLA compliance.|
|Post-production, High/Critical severity|Escalated immediately. CISO notified. Risk treatment plan required. Engineering may be re-engaged for architectural remediation. NERC-CIP and [CMMC](https://dodcio.defense.gov/CMMC/) deviation processes invoked as applicable.|
|Vendor/Third-party finding|Risk documents and includes in vendor risk register. Governance tracks contractual remediation commitments. Engineering consulted if architectural change is needed.|

### 4.4 Illustrative Example: Electrical Utility

> **Scenario: NERC-CIP Vulnerability in a BES Cyber System**
> 
> During monthly vulnerability scanning, the Risk team identifies that a critical relay management workstation, classified as a BES Cyber System under NERC-CIP CIP-002, is running an operating system version with a known critical vulnerability (CVSS 9.1). The asset cannot be patched within the standard 35-day window due to vendor testing requirements. Risk notifies Governance of a potential CIP-007-6 deviation. Governance initiates the deviation documentation process. Risk produces a threat analysis showing no current exploitation activity targeting this specific system type. Engineering is engaged to add network monitoring on the affected segment as a compensating control. The CISO and VP of Operations sign the deviation. Risk tracks the patch to closure within the extended timeline and provides attestation documentation to Governance for the compliance record.

### 4.5 NIST Framework Alignment: Risk

|NIST Framework|Relevant Controls / Functions|Risk Team Role|
|---|---|---|
|[NIST CSF](https://www.nist.gov/cyberframework)|GOVERN (Risk Strategy), IDENTIFY (Risk Assessment, Improvement), DETECT (Adverse Event Analysis)|Primary driver of IDENTIFY and DETECT; co-owner of GOVERN risk functions|
|[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)|RA (Risk Assessment), CA (Assessment & Authorization), PM (Program Mgmt), SI-2 (Flaw Remediation)|Executes RA and CA controls; owns SI-2 for patch and vuln tracking|
|[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)|3.11 Risk Assessment|Performs periodic assessments of CUI-handling environments|
|NIST RMF|Step 4 (Assess), Step 6 (Monitor)|Primary executor of continuous monitoring; supports periodic assessments|
|NERC-CIP|CIP-007 (Patch Mgmt), CIP-010 (Vuln Assessments), CIP-011 (Info Protection)|Manages CIP-007 patch tracking; conducts CIP-010 annual vuln assessments|
|[CMMC](https://dodcio.defense.gov/CMMC/)|Level 2: Risk Assessment (RA), Audit & Accountability (AU)|Performs [CMMC](https://dodcio.defense.gov/CMMC/) risk assessments; supports audit log review program|

---

## 5. Cyber Governance

> **Mission:** Set the rules. Track the work. Enable the business to move with confidence.

### 5.1 Mission

The Cyber Governance team is the rule-making, compliance management, and quality assurance function of the CERG model. Governance defines what good looks like, through policies, standards, and implementation guidance, and then ensures the organization actually gets there through compliance tracking, audit support, and control evidence management.

Governance operates from a **"yes, and..."** philosophy. The goal is never to block the business but to ensure that when the business accepts risk, that risk is documented, owned, and managed. Governance provides the framework within which Engineering and Risk do their best work.

### 5.2 Core Functions

- **Policy and Standard Development**: creating, maintaining, and retiring cybersecurity policies, standards, and procedures aligned to [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), 800-171, [CSF](https://www.nist.gov/cyberframework), and applicable regulations
- **Implementation Guidance**: translating policy requirements into practical, actionable guidance for IT and OT teams; bridging the gap between regulatory language and operational reality
- **Compliance Management**: tracking the organization's compliance posture against NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/),, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and other applicable requirements; managing the compliance calendar
- **Control Evidence Management**: setting standards for what constitutes acceptable evidence; collecting, organizing, and maintaining the control evidence library; coordinating audit responses
- **Risk Treatment Tracking**: maintaining the organization's risk register; tracking open risk treatment plans to completion; escalating overdue or deteriorating items to the CISO
- **Quality Assurance**: periodic review of Engineering deliverables and Risk outputs to ensure conformance with organizational standards; not an adversarial audit but a collaborative QA function
- **Regulatory Liaison**: serving as the primary point of contact for regulators and external auditors; managing examination logistics; coordinating response to findings and enforcement actions

### 5.3 The "Yes, And..." Standard

Governance reserves the right to say no, particularly for significant NERC-CIP deviations or [CMMC](https://dodcio.defense.gov/CMMC/) non-conformances where regulatory exposure is material. But the default orientation is enabling the business with guardrails, not closing doors.

|Situation|"Yes, And..." Response|
|---|---|
|Project team cannot patch within standard SLA|Yes, you can extend the patching window - and we need a risk treatment plan, documentation of affected systems, compensating controls, and VP sign-off within 5 business days.|
|New SaaS tool handles CUI but lacks FedRAMP authorization|Yes, you can evaluate this vendor - and Risk needs to complete a vendor security assessment before procurement, and we'll need contractual security requirements in the agreement.|
|OT team needs remote access to SCADA during maintenance window|Yes, remote access is possible - and it must route through the approved jump server, use MFA, be logged, and the session record retained per CIP-007.|
|Business unit wants to skip architecture review to meet deadline|Yes, we can compress the review timeline - and Engineering must complete at minimum a 2-hour express review, and any open items become tracked exceptions with a remediation commitment.|
|NERC-CIP deviation required for emergency maintenance|Yes, the deviation can proceed - and we'll invoke the CIP deviation process: document the circumstances, notify as required, implement compensating measures, and close the deviation within the regulatory window.|

### 5.4 Evidence Standards

Governance sets the evidence standard, what constitutes acceptable proof that a control is operating effectively. Each pillar collects evidence appropriate to its work:

- **Engineering produces:** architecture review documentation, pre-production checklists, risk acceptance packages, handoff documentation, configuration baselines
- **Risk produces:** vulnerability scan reports, penetration test findings, threat intelligence reports, vendor risk assessments, patch tracking records
- **Governance produces:** policy documents, compliance matrices, audit reports, risk register entries, regulatory correspondence, exception approvals

Governance maintains the evidence library and ensures that evidence is organized, dated, attributed, and retained per regulatory requirements, NERC-CIP requires evidence retention for specified periods; [CMMC](https://dodcio.defense.gov/CMMC/) requires evidence available for assessment.

### 5.5 Illustrative Example: Electrical Utility

> **Scenario: [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 Assessment Preparation**
> 
> The utility has a contract with the Department of Energy that requires [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 compliance. Governance leads the preparation effort. They map all 110 [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) practices to the organization's existing controls, identifying 14 gaps. Governance works with Engineering to remediate 9 of the gaps through technical implementation. Three gaps are addressed through policy and procedure updates that Governance drafts. Two gaps require Risk to perform additional scanning and document compensating controls. Governance manages the evidence package, pulling architecture review records from Engineering, vulnerability reports from Risk, and policy documents from its own library. When the C3PAO assessment team arrives, Governance coordinates the logistics, manages the information requests, and tracks findings to closure post-assessment.

### 5.6 NIST Framework Alignment: Governance

|NIST Framework|Relevant Controls / Functions|Governance Role|
|---|---|---|
|[NIST CSF](https://www.nist.gov/cyberframework)|GOVERN (all functions), IDENTIFY (Improvement), RESPOND (Improvements)|Primary owner of the GOVERN function across all six sub-functions|
|[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)|PL (Planning), PM (Program Mgmt), CA (Assessment), PS (Personnel Security)|Owns PL and PM control families; coordinates CA; sets PS standards|
|[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)|3.12 Security Assessment, all documentation requirements|Manages 800-171 assessment readiness and documentation compliance|
|NIST RMF|Step 1 (Categorize), Step 2 (Select - policy), Step 5 (Authorize), Step 6 (Monitor - compliance)|Leads categorization; co-leads authorization; owns compliance monitoring|
|NERC-CIP|CIP-003 (Security Mgmt Controls), CIP-004 (Personnel Training), CIP-014 (Physical Security Policy)|Primary owner of CIP-003; coordinates CIP-004 with Awareness team; maintains all deviation records|
|[CMMC](https://dodcio.defense.gov/CMMC/)|All documentation and evidence requirements across all domains|Manages assessment readiness, evidence collection, and C3PAO coordination|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC|IT General Controls documentation, change management evidence|Maintains ITGC control library; coordinates with external auditors|

---

## 6. Targeting [NIST CSF](https://www.nist.gov/cyberframework) Adaptive Maturity

### 6.1 What Adaptive Means

The NIST Cybersecurity Framework defines four tiers of organizational maturity: Partial, Informed, Repeatable, and Adaptive. Most organizations operating a mature security program reach Repeatable, processes are defined, practiced, and reviewed. Adaptive goes further.

At the Adaptive tier, an organization does not just respond to the threat environment, it anticipates it. Risk management is integrated into the fabric of business decision-making. Cybersecurity considerations are part of every significant investment, acquisition, and operational change. The security function continuously learns from internal events and external intelligence, and updates its practices accordingly.

|[CSF](https://www.nist.gov/cyberframework) Tier|What It Looks Like in Practice|
|---|---|
|**Partial (Tier 1)**|Ad hoc processes. Risk decisions made reactively. Limited awareness of threats. No consistent policy or evidence collection.|
|**Informed (Tier 2)**|Policies exist but are not consistently applied. Risk management happens in silos. Some awareness of threat environment. Inconsistent evidence.|
|**Repeatable (Tier 3)**|Defined, documented, and practiced processes. Risk management is consistent. Compliance calendar exists. Evidence is collected systematically. Teams understand their roles.|
|**Adaptive (Tier 4)**|Cybersecurity is integrated into organizational decision-making. Threat intelligence actively shapes priorities. Lessons learned drive continuous improvement. Risk appetite is clearly defined and applied. The business views security as a value driver, not a cost center.|

### 6.2 How CERG Produces Adaptive Behavior

The CERG model is designed to produce Adaptive-tier behavior through its structure, not just its aspirations.

|Adaptive Criterion|CERG Mechanism|Pillar(s)|
|---|---|---|
|Risk management is integrated into business decisions|Engineering engages at the business requirements stage - before designs are set or budgets committed. Security cost is a design input, not an afterthought.|Engineering|
|Threat intelligence informs priorities|Risk maintains a live threat intelligence function including ICS/OT-specific sources. Intelligence is distributed to Engineering (design decisions), IR (detection), and Governance (policy updates).|Risk|
|Lessons learned drive improvement|Post-incident reviews, penetration test retrospectives, and audit findings are tracked in the Governance risk register with assigned owners and improvement actions.|Governance, Risk|
|Risk appetite is defined and applied consistently|Governance maintains a documented risk appetite and tolerance framework. The "yes, and..." model applies this consistently across all risk treatment decisions.|Governance|
|Continuous improvement of the security program|Governance conducts periodic QA reviews of Engineering and Risk outputs. The CISO reviews CERG performance metrics quarterly.|Governance, All|
|Cybersecurity is viewed as a value driver|Engineering's consulting model and "yes, and..." Governance orientation build organizational trust. The business experiences security as an enabler, not an obstacle.|All|
|Cross-pillar knowledge transfer prevents single points of failure|CERG roles are designed with deliberate left-right knowledge sharing. Engineers learn Risk thinking; Risk analysts understand Governance requirements; Governance understands operational constraints.|All|

### 6.3 [CSF](https://www.nist.gov/cyberframework) Core Function Coverage

The [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) Core consists of six functions. CERG provides primary or strong supporting ownership for all six.

|[CSF](https://www.nist.gov/cyberframework) Function|Primary Owner|CERG Coverage|
|---|---|---|
|**GOVERN**|Governance|Governance owns the risk strategy, policy, roles, and accountability structures. Risk contributes risk appetite data. Engineering ensures operational compliance.|
|**IDENTIFY**|Risk + Engineering|Risk owns asset, risk, and improvement identification. Engineering contributes asset documentation through project handoffs.|
|**PROTECT**|Engineering|Engineering designs and implements protective controls. Governance sets the standard. Risk validates effectiveness through vuln management.|
|**DETECT**|Risk + IR (adjacent)|Risk owns vuln and threat detection. Incident Response owns event detection and SOC. Risk feeds intelligence to IR.|
|**RESPOND**|IR (adjacent) + Governance|IR leads response execution. Governance owns the playbook library and post-incident documentation. Risk provides threat context during incidents.|
|**RECOVER**|IR (adjacent) + Governance|IR leads recovery. Governance manages lessons-learned documentation and improvement tracking. Engineering supports system restoration where architectural changes are needed.|

---

## 7. Regulatory Alignment

### 7.1 NERC-CIP

NERC-CIP is the primary regulatory framework for bulk electric system (BES) cybersecurity. For an electrical utility, NERC-CIP requirements are non-negotiable and carry significant enforcement risk.

|CIP Standard|CERG Ownership and Application|
|---|---|
|**CIP-002:** BES Cyber System Categorization|Governance leads the annual categorization process. Engineering provides technical input on system connectivity and function. Risk validates the asset inventory.|
|**CIP-003:** Security Management Controls|Governance owns all CIP-003 policies and senior manager approval processes. Risk provides threat context for policy updates.|
|**CIP-004:** Personnel & Training|Governance sets training requirements and coordinates with the Security Awareness team for delivery. Engineering and Risk fulfill their own training obligations.|
|**CIP-005:** Electronic Security Perimeters|Engineering designs and implements ESPs and EAPs. Governance maintains ESP documentation. Risk validates perimeter integrity through scanning.|
|**CIP-006:** Physical Security|Governance maintains physical security policy. Engineering reviews physical security requirements for new OT deployments.|
|**CIP-007:** Systems Security Management|Risk owns patch management tracking and vulnerability assessment. Engineering implements port/service controls during deployment. Governance tracks compliance.|
|**CIP-010:** Configuration Management & Vuln Assessments|Engineering produces and maintains configuration baselines. Risk performs CIP-010 annual vulnerability assessments. Governance retains assessment records.|
|**CIP-011:** Information Protection|Governance defines BES Cyber System Information (BCSI) handling requirements. Engineering implements technical protections. Risk validates through scanning.|
|**CIP-013:** Supply Chain Risk Management|Risk leads vendor risk assessment. Governance maintains the supply chain risk management plan. Engineering applies controls to vendor-supplied systems.|
|**CIP-014:** Physical Security (Transmission)|Governance maintains risk assessment documentation. Engineering consults on physical-cyber interdependencies.|

### 7.2 [CMMC](https://dodcio.defense.gov/CMMC/): Cybersecurity Maturity Model Certification

[CMMC](https://dodcio.defense.gov/CMMC/) Level 2 requires implementation and assessment of all 110 practices in [NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final). For organizations handling Controlled Unclassified Information (CUI) on behalf of the federal government, [CMMC](https://dodcio.defense.gov/CMMC/) certification is a contract requirement. CERG provides the operational backbone for [CMMC](https://dodcio.defense.gov/CMMC/) compliance.

- **Engineering** implements the technical controls across the 14 [CMMC](https://dodcio.defense.gov/CMMC/) domains, access control, configuration management, system and communications protection, and others, during project delivery
- **Risk** performs the periodic assessments required by [CMMC](https://dodcio.defense.gov/CMMC/) practice CA.2.157 and manages the Plan of Action & Milestones (POA&M) for open findings
- **Governance** maintains the System Security Plan (SSP), manages the evidence library, coordinates C3PAO assessment logistics, and tracks POA&M items to closure

### 7.3 [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)

For organizations subject to [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC requirements, CERG provides the structural foundation for compliance without requiring a separate compliance team.

- **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC:** Governance owns the IT General Controls framework and evidence library. Engineering ensures change management controls are embedded in deployment processes. Risk monitors access and configuration integrity in financial systems.

> **The Regulatory Advantage of CERG**
> 
> Organizations with multiple regulatory obligations, a utility managing NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) simultaneously, typically struggle with duplicated effort and conflicting timelines. CERG centralizes the regulatory function in Governance while ensuring that Engineering and Risk produce compliance evidence as a byproduct of their daily work, not as a separate compliance exercise. One team, one evidence library, one compliance posture.

---

## 8. IT/OT Considerations

### 8.1 The Air-Gapped Starting Point

Most organizations with OT environments today maintain a degree of air-gap separation between their operational technology networks and enterprise IT. For an electrical utility, this typically means:

- SCADA systems, energy management systems (EMS), and substation automation on isolated OT networks
- Historian servers in a DMZ acting as the data bridge between OT and IT
- Jump servers or data diodes controlling any permitted data flows
- Physical controls limiting access to OT environments

CERG is designed to operate in this context. The air-gap is a security control, Governance documents it, Risk validates it, and Engineering designs to preserve it while enabling the operational visibility the business needs.

### 8.2 The Modernization Pressure

The push to modernize OT infrastructure is real. Utilities are evaluating advanced metering infrastructure (AMI), remote monitoring, predictive maintenance, and grid modernization initiatives that all require some level of IT/OT integration. CERG's role is to ensure that modernization happens securely, not to prevent it.

> **Engineering's Role in IT/OT Convergence**
> 
> When the business initiates an IT/OT convergence project, Engineering must be engaged before the vendor is selected and before the architecture is set. The engineering team reviews whether the proposed integration can be achieved while maintaining the electronic security perimeters required by CIP-005, the configuration management discipline required by CIP-010, and the segmentation required to limit the blast radius of a cyber event in either direction. This is far more effective and far less expensive than retrofitting security after the system is installed.

### 8.3 OT-Specific Risk Considerations

The Risk team's approach to OT environments differs from IT in several important ways:

- **Scanning must be OT-safe:** active network scanning of OT environments can disrupt control processes. Risk uses passive monitoring, vendor-provided scan tools, and approved active scanning windows coordinated with OT operations.
- **Patch windows are constrained:** OT systems often cannot be patched on standard IT timelines due to vendor testing requirements, operational windows, and redundancy limitations. Risk tracks OT patch compliance separately and initiates NERC-CIP deviation processes when SLAs cannot be met.
- **Availability is the primary objective:** in OT environments, availability often outranks confidentiality in the risk calculus. Risk team members must understand this trade-off and communicate findings in terms of operational impact, not just CVSS scores.
- **Threat intelligence must include ICS-specific sources:** Risk maintains subscriptions to ICS-CERT advisories, E-ISAC threat intelligence, and vendor-specific security bulletins for all OT platforms in use.

### 8.4 Governance in OT Environments

NERC-CIP creates a distinct compliance obligation for BES Cyber Systems that sits alongside, and sometimes in tension with, broader IT governance. Governance manages this by:

- Maintaining separate but linked policy structures for IT and OT, common principles, tailored implementation requirements
- Tracking CIP-002 categorized assets separately in the risk and compliance registers with their specific regulatory requirements
- Managing NERC-CIP deviation and mitigation plan processes as a distinct workflow with defined escalation paths to the CISO and, where required, regulatory notification
- Coordinating with the reliability operations team to ensure that security controls and compliance actions do not inadvertently introduce reliability risk

---

## 9. Team Structure and Talent Model

### 9.1 Illustrative Team Structure

The illustrative organization for this framework is a major electrical utility with approximately 14,000 employees and a roughly equal population of consultants and contractors, a total protected population approaching 28,000 people, identities, devices, and access relationships to manage. CERG for this organization is a 60-person team reporting to the CISO, operating alongside Security Awareness and Incident Response.

This is an intentionally large example. The goal is to show what CERG looks like at full scale, with real operational velocity and complexity, so that teams of any size can see the complete model and trim to fit their environment. A 6-person CERG running this framework looks different in headcount, not in structure.

At this scale, the workload is substantial across all three pillars. Engineering carries approximately 125 active project engagements per year with roughly 40 running concurrently at any given time, spanning IT infrastructure, enterprise applications, OT modernization, cloud migrations, and third-party integrations. Engineers are aligned to specific business verticals (generation, transmission, distribution, enterprise IT, corporate functions) and are expected to develop genuine fluency in the systems, applications, networks, and operational processes they support, not just the security controls that apply to them. A generation-aligned engineer who doesn't understand how a historian feeds an EMS is less effective, not just less credible.

Risk operates at equivalent velocity. The vendor risk program covers more than 2,500 active vendors and an extended workforce of thousands of remote contractors accessing systems and maintaining infrastructure across the enterprise. Vulnerability management covers more than 100,000 assets spanning enterprise IT, OT networks, substations, and cloud environments, with OT-safe scanning disciplines applied where active scanning would introduce operational risk. Penetration testing and red team operations run on a continuous cycle across IT and OT targets. Threat intelligence is a production function, not a feed subscription, analysts produce actionable intelligence distributed to Engineering, Incident Response, and leadership, with ICS/OT-specific coverage given the utility's bulk electric system exposure.

Governance operates as a domain-expert function, not a generalist compliance team. Subject matter experts carry deep technical knowledge in specific domains, network security, identity and access management, cloud security, OT/ICS security, cryptography, and translate that expertise into implementation guidance that Engineering and IT operations teams can actually use. The compliance portfolio spans NERC-CIP (across dozens of registered entities and hundreds of categorized BES Cyber Systems), [CMMC](https://dodcio.defense.gov/CMMC/),, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC, and state regulatory requirements. The evidence library is a living system, not a pre-audit scramble. The policy and standards catalog is actively maintained, version-controlled, and tied to regulatory citation so that any control can be traced to its source requirement.

A representative staffing structure for a CERG of this scale:

|Role|Pillar|Key Responsibilities|
|---|---|---|
|CISO|Executive|Strategy, CERG leadership, board and executive reporting, regulatory escalation, budget authority|
|Engineering Pillar Leader|Engineering|Engagement portfolio oversight; vertical alignment model; OT/IT convergence program lead; senior architecture decisions; team development|
|Senior Cyber Engineer - OT/ICS (×3)|Engineering|Generation, transmission, and distribution vertical leads; SCADA and substation security architecture; CIP-005/CIP-010 design consultation; OT modernization advisory|
|Senior Cyber Engineer - IT/Cloud (×3)|Engineering|Enterprise IT and cloud vertical leads; application and infrastructure security architecture; identity and access design; pre-production assessment leadership|
|Cyber Engineer (×8)|Engineering|Project-level security consultation across assigned verticals; pre-production coordination with Risk; vendor solution review; risk treatment plan drafting; handoff documentation|
|Risk Pillar Leader|Risk|Program ownership across vuln management, pen testing, threat intel, and vendor risk; OT risk strategy; executive risk reporting|
|Senior Risk Analyst - Vulnerability Management (×3)|Risk|Enterprise vuln scan operations; OT-safe scanning program; finding prioritization and triage; SLA tracking and escalation; remediation verification|
|Threat Intelligence Analyst (×2)|Risk|Threat actor tracking; ICS/OT-specific intelligence production; E-ISAC and ICS-CERT liaison; intelligence distribution to Engineering and IR|
|Senior Risk Analyst - Vendor & Third-Party Risk (×2)|Risk|Vendor security assessment program; contractor access risk; contract redline support; supply chain risk reporting|
|Risk Analyst - Penetration Testing & Red Team (×3)|Risk|Internal pen test execution; external red team coordination; OT adversarial testing; findings documentation and tracking|
|Risk Analyst (×5)|Risk|Day-to-day vuln tracking and owner follow-up; vendor assessment support; threat feed monitoring; finding remediation documentation|
|Governance Pillar Leader|Governance|Policy and standard ownership; NERC-CIP compliance program leadership; regulatory and audit liaison; risk register governance; Governance team development|
|NERC-CIP Compliance Manager (×3)|Governance|BES Cyber System compliance; CIP deviation and mitigation management; NERC-CIP evidence library; regulatory exam coordination; reliability-security interface|
|Senior Governance Analyst - Technical Domains (×4)|Governance|Domain SME coverage across network security, IAM, cloud, and cryptography; implementation guidance production; standard development; Engineering QA reviews|
|CMMC / Federal Compliance Manager (×3)|Governance|[CMMC](https://dodcio.defense.gov/CMMC/) SSP and POA&M management; 800-171 control tracking; C3PAO coordination; federal contract compliance calendar|
|Governance / Compliance Analyst - Commercial Frameworks (×3)|Governance|and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC compliance; external audit coordination; evidence collection and library management; compliance calendar|
|Policy & Standards Manager (×3)|Governance|Policy and procedure documentation; version control and review cycles; cross-pillar QA reviews; training content support for Security Awareness|

This distributes the 60-person CERG across approximately 14 Engineering staff, 15 Risk staff, and 13 Governance staff, with the CISO and pillar managers rounding out the team. The specific allocation will shift based on organizational priorities, a utility in the middle of a major grid modernization program will weight Engineering more heavily; one preparing for a [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 assessment or a NERC-CIP audit cycle will weight Governance.

> **Scaling the Model**
> 
> Most organizations will run a smaller CERG than this example, and that is by design. A municipal utility with a 6-person cyber team might place 2 engineers, 2 risk analysts, and 2 governance analysts in CERG, with each person carrying the full scope of their pillar. A regional cooperative with a single cybersecurity hire might have that person operate across all three pillars with the CISO providing strategic direction. The framework is the same at every size. The roles compress; the responsibilities do not disappear, they concentrate. Understanding the full-scale model helps smaller teams identify what they are covering, what they are deferring, and where they need to prioritize as they grow.

### 9.2 The Left-Right Knowledge Model

One of CERG's explicit design goals is talent resilience, the ability to absorb the loss of any single team member without stopping work. The mechanism for achieving this is deliberate left-right knowledge sharing within and across pillars.

- Within each pillar, team members document their work in a shared and accessible way, not as bureaucratic overhead but as operational artifacts that others can follow
- Governance's policies and standards serve as the knowledge base for Engineering and Risk, new arrivals can orient themselves by reading what Governance has documented
- Risk's vulnerability reports and threat intelligence give Engineering context for why certain design decisions matter
- Engineering's architecture and handoff documents give Risk a current map of what is in the environment and how it is configured

In practice, this means that a new Cyber Engineer can learn the organization's standards from Governance, understand the current threat environment from Risk, and have context for every major system from Engineering's project documentation. Onboarding accelerates. Knowledge is in the system, not in someone's head.

### 9.3 CERG and the Adjacent Teams

|Interaction|Description|
|---|---|
|CERG → Security Awareness|Governance provides policy and procedure content for awareness training. Risk provides threat intelligence for targeted awareness campaigns (e.g., spear-phishing scenarios relevant to ICS/OT). Engineering feeds real-world examples from project work into training scenarios.|
|CERG → Incident Response|Risk provides threat intelligence and vulnerability context during incidents. Engineering provides architecture and configuration documentation to support containment and recovery. Governance provides playbooks and manages post-incident documentation.|
|Security Awareness → CERG|Awareness provides metrics on training completion and phishing simulation results - inputs for Governance's compliance tracking and risk register.|
|Incident Response → CERG|IR provides post-incident findings and lessons learned - inputs for Risk (threat landscape updates), Engineering (architectural improvements), and Governance (policy and playbook updates).|

---

## 10. Getting Started: The Path to Adaptive

### 10.1 Phase 1: Establish (Months 1–3)

The first priority is standing up the CERG structure and establishing the baseline work products each pillar needs to function.

- **Engineering:** Document the active project portfolio. Identify any in-flight projects that should receive a retroactive engineering review. Establish the lightweight intake process.
- **Risk:** Stand up or audit the vulnerability management program. Ensure IT and OT environments are covered with appropriate scanning approaches. Inventory threat intelligence feeds.
- **Governance:** Conduct a policy gap assessment against [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and applicable regulatory frameworks. Identify the three to five most critical missing or out-of-date policies. Build or inherit the risk register.

### 10.2 Phase 2: Operate (Months 4–9)

With the structure in place, the focus shifts to operating CERG as a team and building the cross-pillar working rhythms.

- Establish a regular CERG operating cadence, weekly pillar syncs, monthly cross-pillar review, quarterly CISO briefing
- Engineering begins processing the project intake queue and building the first round of handoff documentation
- Risk begins producing regular vulnerability reports with prioritized findings and tracking remediation to SLA
- Governance completes the first compliance self-assessment against NERC-CIP and [CMMC](https://dodcio.defense.gov/CMMC/); begins building the evidence library
- All pillars begin practicing the "yes, and..." model on real business requests

### 10.3 Phase 3: Mature (Months 10–18)

The CERG model begins demonstrating Repeatable behavior. The path to Adaptive requires building the continuous improvement and integration functions.

- Risk begins producing structured threat intelligence reports distributed to Engineering, IR, and leadership
- Governance launches a formal QA cycle, quarterly reviews of Engineering and Risk work products against defined standards
- Engineering demonstrates consistent early engagement on projects, present at business requirements stage, not called in at go-live
- First external validation: coordinate a NERC-CIP compliance audit or [CMMC](https://dodcio.defense.gov/CMMC/) readiness assessment to measure progress and identify gaps
- Begin building the metrics program, vulnerability SLA adherence, time-to-engage on new projects, evidence collection completeness, policy currency

### 10.4 Adaptive Indicators

An organization operating at Adaptive maturity will demonstrate these observable behaviors:

- The security team is engaged in business planning conversations before projects are funded, not after they are designed
- Threat intelligence from Risk actively changes Engineering design decisions and Governance policy priorities
- When a significant vulnerability or threat emerges, the organization has a clear, practiced process for assessing impact, communicating status, and executing response, within hours, not days
- External auditors and regulators find organized, complete, and timely evidence, because evidence collection is a byproduct of daily work, not a pre-audit scramble
- New team members become productive faster because the CERG knowledge base, policies, standards, architecture documents, risk reports, is current, accessible, and well-organized
- The CISO can credibly report the organization's risk posture to the board using data from the risk register and compliance program, not gut feel

---

> ## SURGE
> 
> **Engineering. Risk. Governance.** _Fast. Powerful. Directional._

---
