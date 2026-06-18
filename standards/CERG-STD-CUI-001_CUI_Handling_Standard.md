## CUI HANDLING STANDARD
### [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) · [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 · Federal Contract Information

---

| | |
|---|---|
| **Document ID** | CERG-STD-CUI-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CMMC / Federal Compliance Manager |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Significant Change / [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Revision |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r2/final) (and r3 transition) · [NIST 800-172](https://csrc.nist.gov/pubs/sp/800/172/final) · NIST RMF |
| **Regulations** | [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 · DFARS 252.204-7012, -7019, -7020, -7021 · 32 CFR Part 2002 · FAR 52.204-21 (FCI) |
| **Environments** | Any system that processes, stores, or transmits CUI or FCI - owned, hybrid, cloud, contractor |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [CERG Roles in CUI Environments](#2-cerg-roles-in-cui-environments)
3. [GOVERN, CUI Program Foundation](#3-govern--cui-program-foundation)
4. [IDENTIFY, Inventory, Boundary, and Flow](#4-identify--inventory-boundary-and-flow)
5. [PROTECT, Control Implementation for CUI](#5-protect--control-implementation-for-cui)
6. [DETECT, Monitoring CUI Environments](#6-detect--monitoring-cui-environments)
7. [RESPOND, Cyber Incident Reporting Under DFARS](#7-respond--cyber-incident-reporting-under-dfars)
8. [RECOVER, Recovery and Lessons Learned](#8-recover--recovery-and-lessons-learned)
9. [Training and Personnel](#9-training-and-personnel)
10. [Regulatory and Framework Alignment Summary](#10-regulatory-and-framework-alignment-summary)
11. [Exceptions, POA&M, and SSP Maintenance](#11-exceptions-poam-and-ssp-maintenance)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

This standard implements the foundational principles established in **CERG-POL-001** for systems that process, store, or transmit Controlled Unclassified Information (CUI) and Federal Contract Information (FCI). It defines the specific, measurable security requirements drawn from **[NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)** (the source of [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 practices), **[NIST SP 800-172](https://csrc.nist.gov/pubs/sp/800/172/final)** (where enhanced protection is contractually required), and the cyber incident reporting and flow-down obligations established by **DFARS 252.204-7012** and the **[CMMC](https://dodcio.defense.gov/CMMC/)** program rule under DFARS 252.204-7021.

This standard does not replace the System Security Plan (SSP), the Plan of Action and Milestones (POA&M), or the contract-specific requirements that may apply to a given award. It establishes the organization-wide requirements that every CUI-handling system shall meet, and the governance that translates those requirements into auditable evidence.

### 1.1 Scope

This standard applies to:

- All information systems that **process, store, or transmit CUI** as defined in 32 CFR Part 2002 and the CUI Registry
- All information systems handling **Federal Contract Information (FCI)** under FAR 52.204-21 (subject to the more limited 15-control baseline)
- All **contractor and subcontractor** systems with access to CUI on behalf of the organization, including managed service providers
- All **cloud service providers (CSPs)** hosting CUI on the organization's behalf (FedRAMP Moderate equivalency or higher required per DFARS 252.204-7012(b)(2)(ii)(D))
- All **personnel** with authorized access to CUI, including employees, contractors, consultants, and authorized third parties

### 1.2 The [CMMC](https://dodcio.defense.gov/CMMC/) / DFARS Reality

CUI obligations are contractual. Failure to meet them is not solely a security finding, it is a contract-compliance issue that can affect eligibility for award, payment, or continued performance. The DoD's [CMMC](https://dodcio.defense.gov/CMMC/) program operationalizes 800-171 compliance with third-party certification (C3PAO) at Level 2 for most contracts handling CUI. SPRS scoring is reported and visible to contracting officers.

> **One Spreadsheet Away From a Finding**
>
> A single CUI document stored in an unapproved location (personal email, generic file share, unmanaged endpoint) places that system inside the assessment boundary, and exposes the organization to [CMMC](https://dodcio.defense.gov/CMMC/) findings, DFARS clawback, and contract eligibility risk. Scope discipline is the foundational control. Everything else depends on knowing where CUI is, and where it is not.

### 1.3 Relationship to Parent Policy

This standard is subordinate to **[CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md)**. It implements specific requirements; it does not limit any principle established in that policy. Where the Cloud / SaaS Standard ([CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md)) and this standard both apply, both shall be satisfied, and the more stringent requirement controls. Exceptions follow the process defined in [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) Section 7, with additional obligations defined in Section 11 of this standard.

---

## 2. CERG Roles in CUI Environments

The three CERG pillars operate in CUI environments with the same structure as elsewhere, with adaptations for contractual compliance evidence.

| **CERG Pillar** | **CUI-Specific Responsibilities** |
|---|---|
| **Engineering** | Architects the CUI enclave - the bounded set of systems, networks, services, and endpoints inside the assessment boundary. Designs and maintains the technical controls that satisfy each 800-171 requirement. Embeds CUI handling guardrails into endpoint, identity, collaboration, and cloud platforms. Produces the technical evidence artifacts (configurations, screenshots, exported policies) that support the SSP. |
| **Risk** | Operates the exposure management program inside the CUI boundary. Conducts annual self-assessments against 800-171 and tracks SPRS scores. Manages the [CMMC](https://dodcio.defense.gov/CMMC/) pre-assessment readiness program and coordinates external C3PAO engagements. Tracks 800-171 control posture as a first-class risk register category. Assesses third parties handling CUI on the organization's behalf. |
| **Governance** | Owns the **System Security Plan (SSP)**, **Plan of Action and Milestones (POA&M)**, and the **[CMMC](https://dodcio.defense.gov/CMMC/) evidence library**. Maintains this standard, the CUI Registry mapping, and the data classification authority for CUI. Manages **DFARS 252.204-7012 cyber incident reporting** to DC3 within 72 hours. Coordinates contractual flow-down to subcontractors. Maintains SPRS submissions and supports DoD assessor engagements. |

> **The Evidence-as-Byproduct Rule for CUI**
>
> [CMMC](https://dodcio.defense.gov/CMMC/) assessors do not score intentions, they score implementation evidence. The CERG model treats SSP and POA&M maintenance as continuous, byproduct work of Engineering and Risk activities, not as a one-time pre-assessment scramble. If the only time the SSP is touched is in the 90 days before a C3PAO visit, the program is not yet operating at the maturity the regulation expects.

---

## 3. GOVERN: CUI Program Foundation

### 3.1 SSP, POA&M, and [CMMC](https://dodcio.defense.gov/CMMC/) Posture

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain a current System Security Plan (SSP) describing how each [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) requirement is satisfied, with documented control implementations, responsible parties, and evidence references. Update upon any material change to the CUI environment. | All CUI | Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.12.4 · [CMMC](https://dodcio.defense.gov/CMMC/) CA.L2-3.12.4 |
| Maintain a Plan of Action and Milestones (POA&M) for any 800-171 requirement not fully implemented. Each POA&M item shall have a documented remediation path, owner, and target closure date. POA&M items shall not exceed the closure window allowed by the current [CMMC](https://dodcio.defense.gov/CMMC/) rule. | All CUI | Governance / Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.12.2 · [CMMC](https://dodcio.defense.gov/CMMC/) CA.L2-3.12.2 |
| Submit and maintain a current Supplier Performance Risk System (SPRS) score reflecting the organization's [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) self-assessment. Re-score upon any material change to the CUI environment. | All CUI | Governance | DFARS 252.204-7019, -7020 |
| Maintain readiness for [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 third-party assessment (C3PAO). Engage C3PAO on the cadence required by the applicable contract or rule version. | All CUI | Governance / Risk | DFARS 252.204-7021 · [CMMC](https://dodcio.defense.gov/CMMC/) rule |
| Designate a senior official (e.g., CISO) as the accountable executive for CUI compliance posture. Reporting cadence to leadership and the board shall include 800-171 score, open POA&M items, and assessment status. | All CUI | CISO / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.12.3 · [CMMC](https://dodcio.defense.gov/CMMC/) CA.L2-3.12.3 |

### 3.2 Third-Party and Flow-Down

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Flow DFARS 252.204-7012 (and [CMMC](https://dodcio.defense.gov/CMMC/) clauses as required) to all subcontractors and service providers handling CUI on behalf of the organization. Maintain a current register of flow-down recipients. | All CUI | Governance | DFARS 252.204-7012(m) |
| Assess each third party handling CUI before onboarding and annually thereafter. Assessment shall cover 800-171 posture, incident reporting capability, and DFARS flow-down compliance. | All CUI | Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.20 · [CMMC](https://dodcio.defense.gov/CMMC/) AC.L2-3.1.20 |
| Cloud service providers hosting CUI shall meet FedRAMP Moderate baseline (or equivalent as authorized under DFARS 252.204-7012(b)(2)(ii)(D)). Maintain the equivalency documentation in the SSP. | All CUI (Cloud) | Risk / Governance | DFARS 252.204-7012(b)(2)(ii)(D) |
| Contract clauses with CUI handlers shall include: 72-hour incident notification to the organization, mandatory cooperation with damage assessment, malicious software preservation, and right-to-audit provisions. | All CUI | Governance | DFARS 252.204-7012 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.20 |

### 3.3 Risk and Configuration Authorities

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Document all CUI-system risk acceptance decisions in the organizational risk register with: control reference, business justification, compensating controls, and expiration. CUI risk acceptances require CISO approval at minimum. | All CUI | Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.11.1 · [CMMC](https://dodcio.defense.gov/CMMC/) RA.L2-3.11.1 |
| Maintain documented Configuration Control Board (CCB) or equivalent authority for changes to CUI-system baselines. Changes shall be reviewed for impact on 800-171 control posture before approval. | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.4.3 · [CMMC](https://dodcio.defense.gov/CMMC/) CM.L2-3.4.3 |
| Maintain a CUI environment architecture diagram showing the boundary, all components inside, all external interfaces, and all data flows in/out of the boundary. Update upon material change. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.4.1 · [CMMC](https://dodcio.defense.gov/CMMC/) CM.L2-3.4.1 |

---

## 4. IDENTIFY: Inventory, Boundary, and Flow

### 4.1 CUI Identification and Boundary Definition

> **CUI Scope Is Not Aspirational**
>
> The 800-171 control set applies to "the components of nonfederal information systems that process, store, or transmit CUI, or that provide security protection for such components." Every system inside the assessment boundary inherits the full obligation. Engineering and Governance define the boundary deliberately to minimize the assessment surface, and then enforce that boundary technically and procedurally.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Identify all CUI categories handled by the organization (e.g., CDI, ITAR, Export Control, Privacy, Procurement) per the CUI Registry. Document the contractual or regulatory basis for each. | All CUI | Governance | 32 CFR 2002 · CUI Registry |
| Define and document the CUI assessment boundary. The boundary shall enumerate all systems, networks, services, endpoints, and personnel that fall inside scope. | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.4.1 |
| Inventory all components inside the CUI boundary: servers, workstations, mobile devices, cloud services, applications, network components, and removable media. Update inventory upon any in-scope change. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.4.1 · [CMMC](https://dodcio.defense.gov/CMMC/) CM.L2-3.4.1 |
| Maintain a CUI data-flow map showing how CUI enters, moves within, and leaves the boundary, including any cross-domain interactions (e.g., to FCI systems, to non-CUI corporate systems, to subcontractors). | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.3, 3.13.1 |
| Mark CUI per CUI Registry handling instructions on creation. Maintain labeling controls (e.g., document-level classification labels, container marking) in collaboration platforms inside the boundary. | All CUI | Governance / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.8.4 · 32 CFR 2002 |

### 4.2 Risk and Vulnerability Identification

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Periodically assess risk to CUI confidentiality, integrity, and availability. Document threat sources, vulnerabilities, likelihood, and impact. Output feeds the risk register and POA&M. | All CUI | Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.11.1 · [CMMC](https://dodcio.defense.gov/CMMC/) RA.L2-3.11.1 |
| Scan CUI environment systems for vulnerabilities at least monthly, and upon advisory of new significant vulnerabilities. Authenticated scans are required where technically feasible. | All CUI | Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.11.2 · [CMMC](https://dodcio.defense.gov/CMMC/) RA.L2-3.11.2 |
| Treat confirmed exposures in the CUI environment per the SLAs defined in **[CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)**. Where treatment cannot meet SLA, open a POA&M entry. | All CUI | Risk / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.11.3 · [CMMC](https://dodcio.defense.gov/CMMC/) RA.L2-3.11.3 |

---

## 5. PROTECT: Control Implementation for CUI

The fourteen [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) control families collectively define the protection requirements. The tables below summarize the organization's implementation. Detailed implementation evidence is maintained in the SSP and the [CMMC](https://dodcio.defense.gov/CMMC/) evidence library.

### 5.1 Access Control (3.1)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Limit system access to authorized users, processes, and devices. Enforce least privilege; restrict access to CUI on a need-to-know basis. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.1, 3.1.2, 3.1.5 |
| Control information flows so CUI is not transmitted outside the boundary except through approved channels. Separate duties to reduce risk of malicious activity without collusion. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.3, 3.1.4 |
| Control and monitor remote access and wireless access to CUI systems. All remote access to CUI shall traverse a documented secure path (e.g., VPN with MFA, conditional access). | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.12–3.1.17 |
| Encrypt CUI on mobile devices and removable media. Control the use of mobile devices in the CUI environment. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.18, 3.1.19 |
| Establish usage restrictions and configuration controls for external systems handling CUI. Authorize use of external systems for CUI explicitly. | All CUI | Governance / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.20–3.1.22 |

### 5.2 Awareness and Training (3.2)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Provide security awareness training to all CUI users on the risks associated with their activities and the applicable policies, standards, and procedures. | All CUI | Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.2.1, 3.2.2 |
| Provide insider threat awareness training to all CUI users. | All CUI | Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.2.3 |

### 5.3 Audit and Accountability (3.3)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Generate audit logs sufficient to support investigation. Protect audit information and audit logging functionality from unauthorized access, modification, and deletion. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.3.1, 3.3.8, 3.3.9 |
| Correlate audit record review, analysis, and reporting processes. Provide a system capability to alert on inappropriate or unusual activity. | All CUI | Risk / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.3.5, 3.3.6 |
| Ensure system clocks are synchronized for accurate audit records. Retain audit logs for the period required by contract or by the SSP, whichever is longer. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.3.7 |

### 5.4 Configuration Management (3.4)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Establish and maintain baseline configurations and inventories of CUI-system components. Enforce least functionality and prohibit unnecessary software and ports. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.4.1, 3.4.6, 3.4.7 |
| Track, review, approve, and log changes to organizational systems. Analyze the security impact of changes prior to implementation. | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.4.3, 3.4.4 |
| Apply application allow-listing (deny-by-default) for CUI-system endpoints where technically feasible. Control user-installed software. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.4.8, 3.4.9 |

### 5.5 Identification and Authentication (3.5)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Uniquely identify and authenticate organizational users, processes acting on behalf of users, and devices. Use multi-factor authentication for local and network access to privileged accounts and for network access to non-privileged accounts. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.5.1, 3.5.2, 3.5.3 |
| Employ replay-resistant authentication mechanisms. Prevent reuse of identifiers for a defined period. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.5.4, 3.5.5 |
| Enforce minimum password complexity, prohibit password reuse for a defined number of generations, and store and transmit only cryptographically protected passwords. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.5.7–3.5.10 |
| Obscure feedback of authentication information. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.5.11 |

### 5.6 Incident Response (3.6)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| The standing Incident Response team (a separate function under CISO oversight per CERG-GOV-OM-001 §3.4) owns and maintains the operational incident-handling capability. CERG coordinates with the IR team by providing detection feeds, vulnerability context, asset documentation, and post-incident risk-register entries. Test participation follows the IR team's exercise schedule. | All CUI | Incident Response Team (CERG coordinates) | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.6.1, 3.6.3 |
| Track, document, and report incidents to designated officials and authorities both internal and external (including DC3 under DFARS) - see Section 7. | All CUI | Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.6.2 · DFARS 252.204-7012 |

### 5.7 Maintenance (3.7)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Perform maintenance on CUI systems using approved tools and techniques. Sanitize equipment removed for off-site maintenance. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.7.1, 3.7.3 |
| Check media containing diagnostic and test programs for malicious code. Require MFA for nonlocal maintenance sessions and terminate them when complete. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.7.4, 3.7.5 |
| Supervise maintenance activities performed by personnel without required access. | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.7.6 |

### 5.8 Media Protection (3.8)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Protect CUI on system media - paper and digital - through marking, access controls, transport protections, and sanitization. | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.8.1–3.8.4 |
| Sanitize or destroy media containing CUI before disposal or reuse. Maintain records of media sanitization. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.8.3 · NIST 800-88 |
| Encrypt CUI on portable storage media outside controlled areas. Control use of removable media on CUI systems. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.8.6–3.8.9 |

### 5.9 Personnel Security (3.9)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Screen individuals before authorizing access to CUI systems. Re-screen upon role change to higher-privilege CUI access. | All CUI | HR / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.9.1 |
| Ensure CUI and CUI systems are protected during and after personnel actions such as termination and transfer (access revocation, asset recovery, exit interviews where appropriate). | All CUI | Engineering / HR | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.9.2 |

### 5.10 Physical Protection (3.10)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Limit physical access to CUI systems, equipment, and operating environments to authorized individuals. Escort visitors and monitor visitor activity. | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.10.1, 3.10.3 |
| Maintain audit logs of physical access. Control and manage physical access devices. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.10.2, 3.10.4, 3.10.5 |
| Enforce safeguarding measures for CUI at alternate work sites (e.g., remote work). | All CUI | Governance / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.10.6 |

### 5.11 Risk Assessment (3.11)

See Section 4.2 above.

### 5.12 Security Assessment (3.12)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Periodically assess security controls for effectiveness. Develop and implement POA&M to correct deficiencies. | All CUI | Risk / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.12.1, 3.12.2 |
| Monitor security controls on an ongoing basis to ensure continued effectiveness. Develop, document, and periodically update the SSP. | All CUI | Risk / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.12.3, 3.12.4 |

### 5.13 System and Communications Protection (3.13)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Monitor, control, and protect communications at external boundaries and key internal boundaries of CUI systems. Employ subnetworks for publicly accessible system components, separated from internal networks. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.13.1, 3.13.5 |
| Deny network communications traffic by default and allow by exception. Prevent unauthorized and unintended information transfer via shared resources. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.13.6, 3.13.4 |
| Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission and at rest. Use FIPS-validated cryptography where required. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.13.8, 3.13.11, 3.13.16 |
| Terminate network connections at session end or after a defined period of inactivity. Establish and manage cryptographic keys for cryptography used in the system. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.13.9, 3.13.10 |
| Control and monitor the use of mobile code and Voice over IP (VoIP) technologies. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.13.13, 3.13.14 |

### 5.14 System and Information Integrity (3.14)

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Identify, report, and correct system flaws in a timely manner. Provide protection from malicious code at designated locations. | All CUI | Risk / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.14.1, 3.14.2 |
| Monitor system security alerts and advisories and take action in response. Update malicious code protection mechanisms when new releases are available. | All CUI | Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.14.3, 3.14.4 |
| Monitor CUI systems, including inbound and outbound communications, to detect attacks, indicators of potential attacks, and unauthorized use. Identify unauthorized use through monitoring. | All CUI | Risk / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.14.6, 3.14.7 |

---

## 6. DETECT: Monitoring CUI Environments

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Collect security event logs from all CUI-system components capable of generating them. Centralize logs in a SIEM or equivalent inside (or logically aligned with) the CUI boundary. | All CUI | Engineering / Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.3.1 · [CMMC](https://dodcio.defense.gov/CMMC/) AU.L2-3.3.1 |
| Define alerts for CUI-relevant events: failed authentication patterns, privilege escalation, CUI exfiltration indicators, configuration changes, and anti-malware events. | All CUI | Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.3.5, 3.14.6 |
| Apply endpoint detection and response (EDR) tooling to all endpoints inside the CUI boundary. EDR shall include behavioral detection, not only signature-based AV. | All CUI | Engineering / Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.14.6 · [CMMC](https://dodcio.defense.gov/CMMC/) SI.L2-3.14.6 |
| Subscribe to and act on relevant security alerts and advisories - including CISA, DC3, and applicable program-specific advisories. | All CUI | Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.14.3 |

---

## 7. RESPOND: Cyber Incident Reporting Under DFARS

> **The 72-Hour Clock**
>
> DFARS 252.204-7012 requires reporting of any "cyber incident" affecting covered defense information or the contractor's ability to perform operationally critical support, to DoD via the DC3 reporting portal, within **72 hours of discovery**. The clock starts at discovery, not at confirmation. Reporting under DFARS does not waive contractual notification to the contracting officer or customer.

### 7.1 Cyber Incident Reporting

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain a cyber incident response procedure that includes the 72-hour DC3 reporting workflow, evidence preservation requirements, and damage assessment cooperation. | All CUI | Governance / Risk | DFARS 252.204-7012(c) |
| Hold a current DoD-approved medium assurance certificate to submit incident reports through the DC3 portal (Defense Industrial Base Network / DIBNet). Validate certificate currency annually. | All CUI | Governance | DFARS 252.204-7012(c)(3) |
| Upon a reportable cyber incident: preserve images of affected systems, malicious software (if detected), and packet capture for at least 90 days. Make available to DoD upon request. | All CUI | Risk / Engineering | DFARS 252.204-7012(d), (e) |
| Cooperate with DoD damage assessment activities including providing access to additional information, equipment, or facilities as requested. | All CUI | Governance / Risk | DFARS 252.204-7012(f), (g) |
| Notify the contracting officer in addition to DC3 reporting when required by the applicable contract. | All CUI | Governance | DFARS 252.204-7012 · contract-specific |

### 7.2 Incident Response Coordination

This standard does not replace the master Incident Response Plan (**[CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)**). CUI-specific procedures supplement that plan with: DC3 reporting playbook, evidence preservation procedure, subcontractor-flow notification template, and customer / contracting officer notification template.

---

## 8. RECOVER: Recovery and Lessons Learned

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain documented recovery procedures for CUI systems including backup restoration, system rebuild from approved baselines, and integrity validation post-recovery. | All CUI | Engineering / Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.8.9 · [CMMC](https://dodcio.defense.gov/CMMC/) MP.L2-3.8.9 |
| Protect backups of CUI with the same controls as production CUI (encryption, access control, retention). Test restoration on a defined cadence. | All CUI | Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.8.9, 3.13.11 |
| Conduct post-incident reviews for any cyber incident affecting CUI. Document root cause, control failures, and corrective actions. Update SSP and POA&M as needed. | All CUI | Governance / Risk | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.6.1, 3.12.2 |

---

## 9. Training and Personnel

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| All personnel with CUI access shall complete CUI-specific training before access is granted and annually thereafter. Training includes CUI marking, handling, transmission, storage, and incident reporting obligations. | All CUI | Governance / HR | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.2.1, 3.2.2 |
| Personnel with privileged CUI-system roles shall complete role-based training covering the specific security responsibilities of their role. | All CUI | Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.2.2 |
| Personnel responsible for CUI incident reporting (DC3 submitters, IR leads) shall be trained on the 72-hour reporting procedure and shall validate their access to the DIBNet portal at least quarterly. | All CUI | Governance | DFARS 252.204-7012(c) |
| Insider threat awareness training shall be provided to all CUI personnel and documented. | All CUI | Governance | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.2.3 · [CMMC](https://dodcio.defense.gov/CMMC/) AT.L2-3.2.3 |

---

## 10. Regulatory and Framework Alignment Summary

| **800-171 Control Family** | **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Family** | **[CMMC L2](https://dodcio.defense.gov/CMMC/) Domain** |
|---|---|---|---|
| 3.1 Access Control | PR.AA | AC | AC |
| 3.2 Awareness & Training | GV.RR | AT | AT |
| 3.3 Audit & Accountability | DE.AE | AU | AU |
| 3.4 Configuration Management | PR.PS | CM | CM |
| 3.5 Identification & Authentication | PR.AA | IA | IA |
| 3.6 Incident Response | RS / RC | IR | IR |
| 3.7 Maintenance | PR.MA | MA | MA |
| 3.8 Media Protection | PR.DS | MP | MP |
| 3.9 Personnel Security | GV.RR | PS | PS |
| 3.10 Physical Protection | PR.AA | PE | PE |
| 3.11 Risk Assessment | ID.RA | RA | RA |
| 3.12 Security Assessment | GV.SC, ID.IM | CA | CA |
| 3.13 System & Communications Protection | PR.IR | SC | SC |
| 3.14 System & Information Integrity | DE.CM, PR.PS | SI | SI |

**Contract clauses:** DFARS 252.204-7012 (Safeguarding & cyber incident reporting), DFARS 252.204-7019 ([NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) DoD Assessment Requirements), DFARS 252.204-7020 ([NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) DoD Assessment Requirements, Offeror Submission), DFARS 252.204-7021 (Cybersecurity Maturity Model Certification Requirements). FAR 52.204-21 governs FCI for the 15-control subset.

---

## 11. Exceptions, POA&M, and SSP Maintenance

CUI control deficiencies do not follow the ordinary exception process. Open deficiencies are tracked in the POA&M and reflected in the SPRS score. The exception process in [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) Section 7 applies in addition for organizational risk acceptance.

| **Deficiency / Exception Type** | **Mechanism** | **Approval / Tracking** | **Review** |
|---|---|---|---|
| 800-171 requirement not fully implemented | POA&M entry in SSP | CISO + Governance | Until closed; [CMMC](https://dodcio.defense.gov/CMMC/) rule defines max open windows |
| Compensating control in lieu of an 800-171 control | Documented in SSP with rationale | CISO; assessor judgment at C3PAO | Annual |
| Risk acceptance for an open POA&M item beyond standard window | Risk register + POA&M annotation | CISO + executive sponsor | Quarterly |
| Subcontractor flow-down gap | Contract amendment process; risk register entry | Governance + Legal + Procurement | Per contract cycle |
| Emergency operational deviation (e.g., temporarily expanded access) | 24-hour formal exception + POA&M update | CISO post-hoc within 24 hours | 30 days maximum |

---

## 12. Document Control

| | |
|---|---|
| **Document ID** | CERG-STD-CUI-001 |
| **Version** | 1.21 |
| **Approved By** | CISO |
| **Next Review** | Annual / Upon Significant Change / NIST 800-171 Revision |
| **Change Log** | 1.0 - Initial publication. NIST 800-171r3, DFARS 252.204-7012, CMMC Level 2. |


### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 DRAFT | 2026 | CERG Governance | Initial release - [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final), DFARS 252.204-7012, [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 |

### Review Triggers

This standard shall be reviewed annually and upon any of the following triggering events:

- Revision to [NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) (e.g., transition to Rev 3) or [NIST SP 800-172](https://csrc.nist.gov/pubs/sp/800/172/final)
- Material change to the DFARS 252.204-7012 / -7019 / -7020 / -7021 clauses or the [CMMC](https://dodcio.defense.gov/CMMC/) rule
- Material change to the CUI environment, boundary expansion, new CUI category, new subcontractor flow-down
- A reportable cyber incident affecting CUI
- DoD assessor or C3PAO finding requiring corrective action

Governance owns this document. The Governance Pillar Leader ([CMMC](https://dodcio.defense.gov/CMMC/) / Federal Compliance) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - this standard is subordinate |
| IT (Hosted/Cloud/SaaS) Security Standard | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Peer standard - applies in addition to this where CUI is hosted on cloud/SaaS |
| Grid and Control System Standard | [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | Peer standard - governs OT estates |
| Access Management Standard | [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) | Peer standard - identity/access requirements applied inside CUI boundary |
| Exposure Management Procedure | [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Exposure classification, treatment, patch hygiene, and remediation SLA source |
| Risk Register and Exception Process | [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk acceptance and exception workflow for CUI-related residual risk |
| CUI / CMMC Operational Package | [CERG-PLN-CUI-001](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | SSP, POA&M, SPRS, and assessment-readiness package |
