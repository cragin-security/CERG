## GRID & CONTROL SYSTEMS CYBERSECURITY STANDARD
### BES and Non-BES Operational Technology Environments

---

| | |
|---|---|
| **Document ID** | CERG-STD-OT-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (OT/NERC-CIP) |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Significant Change / CIP Standard Revision |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · NIST RMF |
| **Regulations** | NERC-CIP v6/v7 · IEC 62443 |
| **Environments** | OT / ICS / BES / Non-BES Control Systems |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [CERG Roles in Grid and Control System Security](#2-cerg-roles-in-grid-and-control-system-security)
3. [GOVERN, Program Foundation and Risk Management](#3-govern--program-foundation-and-risk-management)
4. [IDENTIFY, Visibility Into Assets and Threats](#4-identify--visibility-into-assets-and-threats)
5. [PROTECT, Reduce Attack Surface and Limit Blast Radius](#5-protect--reduce-attack-surface-and-limit-blast-radius)
6. [DETECT, Find Threats Before They Find the Grid](#6-detect--find-threats-before-they-find-the-grid)
7. [RESPOND, React Without Making It Worse](#7-respond--react-without-making-it-worse)
8. [RECOVER, Restore Operations and Capture Learning](#8-recover--restore-operations-and-capture-learning)
9. [Training and Personnel Security](#9-training-and-personnel-security)
10. [Regulatory and Framework Alignment Summary](#10-regulatory-and-framework-alignment-summary)
11. [Exceptions and Escalation](#11-exceptions-and-escalation)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

This standard implements the foundational principles established in [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) for grid and control system environments. It defines specific, measurable security requirements for all operational technology (OT), industrial control systems (ICS), and grid automation assets, regardless of whether those assets are classified as Bulk Electric System (BES) Cyber Systems under NERC-CIP or operate outside that regulatory scope.

These requirements are organized around the NIST Cybersecurity Framework 2.0 functions, Govern, Identify, Protect, Detect, Respond, and Recover, and are cross-mapped to NERC-CIP standards, NIST SP 800-82 (Guide to OT Security), [NIST SP 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), and IEC 62443 where applicable. Where BES and non-BES requirements differ materially, both are stated explicitly.

### 1.1 Scope

This standard applies to:

- All BES Cyber Systems and BES Cyber Assets as categorized under NERC-CIP CIP-002
- All non-BES control systems, including distribution automation, advanced metering infrastructure (AMI), substation automation not meeting BES categorization thresholds, and generation assets below NERC registration thresholds
- All Electronic Access Control or Monitoring Systems (EACMS), Physical Access Control Systems (PACS), and Protected Cyber Assets (PCA) associated with BES Cyber Systems
- All systems in the IT/OT convergence zone, including historian servers, data diodes, jump servers, and DMZ infrastructure serving OT environments
- All personnel with authorized electronic or physical access to in-scope systems, including employees, contractors, integrators, and vendors

### 1.2 The BES / Non-BES Distinction

> **How to Read BES vs. Non-BES Requirements**
>
> Throughout this standard, requirements that apply exclusively to BES Cyber Systems are marked **[BES ONLY]**. Requirements that apply to all in-scope OT systems carry no marker. Where BES systems have a more stringent version of a common requirement, both versions are stated. Never apply only the baseline to a BES system.

The NERC-CIP CIP-002 asset categorization process determines which assets carry BES Cyber System obligations. This standard does not replace that process. Governance maintains the BES Cyber System inventory. Engineering ensures controls reflect each asset's classification. Risk validates compliance against both BES and non-BES requirements during exposure management and assessment activities.

### 1.3 Relationship to Parent Policy

This standard is subordinate to [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md). It implements specific requirements; it does not limit any principle established in that policy. Where this standard is silent, the policy governs. Exceptions follow the process defined in [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) Section 7. BES Cyber System exceptions require CISO approval.

---

## 2. CERG Roles in Grid and Control System Security

The three CERG pillars operate in grid and control system environments with the same structure as enterprise IT, with operational adaptations that reflect the unique risk profile of OT.

| **CERG Pillar** | **OT-Specific Responsibilities** |
|---|---|
| **Engineering** | Architects and validates security controls for new and modified OT systems before deployment. Conducts pre-production security reviews for all OT integrations, grid modernization projects, and IT/OT convergence initiatives. Defines and maintains secure configuration baselines for each OT platform class. Serves as the OT security SME in vendor selection and system acquisition. Ensures CIP-010 configuration management controls are embedded in project delivery. |
| **Risk** | Operates the OT exposure management program using passive monitoring, vendor-provided scan tools, and approved active scanning windows that do not introduce operational risk. Tracks OT patch compliance separately from IT, with NERC-CIP deviation workflows initiated when SLAs cannot be met. Conducts OT-specific adversarial testing coordinated with operational teams. Maintains ICS/OT-specific threat intelligence from E-ISAC, ICS-CERT, and vendor security advisories. Manages the CIP-013 supply chain risk program for OT vendors and integrators. |
| **Governance** | Owns the NERC-CIP compliance program including BES Cyber System inventory (CIP-002), CIP deviation and mitigation plan processes, and the NERC-CIP evidence library. Maintains this standard and all subordinate OT procedures. Coordinates regulatory examinations and self-certifications. Produces implementation guidance that translates CIP requirements into actionable technical direction for Engineering and IT/OT operations teams. Tracks all OT security findings and remediation commitments in the risk register. |

> **The Operational Priority Rule**
>
> In OT environments, the CERG model adjusts its default risk posture: availability of grid and control system operations takes precedence over confidentiality. This does not mean confidentiality and integrity controls are skipped, it means that when a control action or remediation activity would create operational risk, it is planned, coordinated, and executed during an approved maintenance window or with appropriate operational safeguards. Security events are never resolved by actions that could themselves cause a grid disturbance.

---

## 3. GOVERN: Program Foundation and Risk Management

### 3.1 Asset Categorization and Inventory

All in-scope assets must be inventoried and categorized before security controls can be applied, compliance obligations determined, or risk assessed. This is the foundational requirement from which all others flow.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain a current inventory of all OT assets including make, model, firmware version, network connectivity, and physical location. | All OT | Engineering | [NIST CSF 2.0](https://www.nist.gov/cyberframework) GV.AM · 800-53 CM-8 · 800-82 §6.2 |
| Perform CIP-002 BES Cyber System categorization annually and upon any change to the environment that could affect categorization. Document the rationale for each categorization decision. | **BES ONLY** | Governance | CIP-002-5.1a R1 |
| Classify each BES Cyber System as High, Medium, or Low impact per CIP-002 Attachment 1 criteria. | **BES ONLY** | Governance | CIP-002-5.1a R1 |
| Identify all EACMS, PACS, and PCAs associated with each BES Cyber System and include them in the asset register. | **BES ONLY** | Engineering / Governance | CIP-002-5.1a R1.3 |
| Maintain an OT network topology diagram current within 90 days, including all Electronic Security Perimeters (ESPs) and Electronic Access Points (EAPs). | All OT | Engineering | CIP-005-6 R1 · [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.2 |
| Track OT asset lifecycle from acquisition through decommission. Decommissioning must include secure data destruction and removal from all access control lists. | All OT | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-8(4) · CIP-004-6 R4 |

### 3.2 Risk Register and Risk Acceptance

All identified security risks to grid and control systems must be documented in the organizational risk register. BES Cyber System risks require CISO approval for risk acceptance.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Document all OT security findings and unmitigated risks in the centralized risk register within 5 business days of identification. | All OT | Governance | [NIST CSF 2.0](https://www.nist.gov/cyberframework) GV.RM · 800-53 RA-3 |
| Assign a risk owner to every open risk item. Risk owners are accountable for treatment plan execution. | All OT | Governance | NIST RMF Step 2 · 800-53 RA-3(1) |
| Risk acceptance for BES Cyber System findings requires documented CISO approval and must be reviewed annually. Accepted risks do not close the finding - they suspend the SLA with documented rationale. | **BES ONLY** | Governance / CISO | CIP-007-6 · NIST RMF Step 4 |
| Initiate a NERC-CIP deviation and mitigation plan when a CIP compliance obligation cannot be met on schedule. Notify the CISO immediately upon identification. | **BES ONLY** | Governance | NERC Rules of Procedure §410 |

### 3.3 Third-Party and Supply Chain Risk

OT vendors, integrators, and managed service providers present significant supply chain risk. Compromised vendor software or hardware in a grid environment can affect physical operations.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| All OT vendors and integrators must complete a security assessment before being granted access to in-scope systems. Assessment depth is tiered by access level and system criticality. | All OT | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SA-9 · IEC 62443-2-1 |
| Implement and maintain a supply chain risk management plan for all OT software and hardware suppliers. The plan must address software integrity verification, hardware authenticity, and vendor incident notification requirements. | **BES ONLY** | Risk / Governance | CIP-013-2 |
| Vendor contracts for OT systems must include: right-to-audit provisions, mandatory incident notification within 24 hours, software bill of materials (SBOM) requirements for new deployments, and security patch commitment timelines. | All OT | Governance / Risk | CIP-013-2 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SR-3 |
| Verify software and firmware integrity before deployment using vendor-provided hashes or cryptographic signatures. Do not deploy unverified software to any OT system. | All OT | Engineering | CIP-013-2 R1.2 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SR-4 |

---

## 4. IDENTIFY: Visibility Into Assets and Threats

### 4.1 OT Network Monitoring

Continuous visibility into OT network activity is essential for detecting threats that vulnerability scans cannot see. Monitoring in OT environments requires methods that do not introduce operational risk.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Deploy passive network monitoring for all OT network segments. Passive monitoring must not generate active probes or queries toward OT devices. | All OT | Risk / Engineering | [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.3 · IEC 62443-3-3 SR 6.1 |
| Collect security event logs from all OT assets capable of generating them. For assets that cannot forward logs natively, use syslog aggregators or protocol translators deployed in the OT DMZ. | **BES ONLY** | Engineering / Risk | CIP-007-6 R4 |
| Retain OT security event logs for a minimum of 90 days immediately accessible and 12 months total. | **BES ONLY** | Engineering / Governance | CIP-007-6 R4.1.1 |
| Integrate OT monitoring data with the enterprise SIEM via one-way data transfer controls through the OT DMZ. Do not create bidirectional monitoring connections into OT networks. | All OT | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-4 · CIP-005-6 R1 |
| Define and document alert thresholds for OT-specific anomalies: unexpected outbound connections from OT segments, unauthorized protocol usage, configuration changes outside maintenance windows, and communications with unknown external endpoints. | All OT | Risk | [NIST CSF 2.0](https://www.nist.gov/cyberframework) DE.CM · 800-53 SI-4(5) |

### 4.2 Vulnerability Identification

OT exposure management operates under different constraints than IT. Scanning must be OT-safe. Patch timelines reflect vendor testing requirements and operational windows. The risk calculus weights availability alongside confidentiality and integrity.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Conduct OT vulnerability assessments at least annually using OT-safe methods: passive monitoring analysis, vendor-provided assessment tools, or active scanning during approved maintenance windows coordinated with the operational team. | All OT | Risk | [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.4 · IEC 62443-2-1 |
| Subscribe to and process vendor security advisories and CISA ICS-CERT advisories for all OT platforms in use. Advisories must be reviewed within 5 business days of publication. | **BES ONLY** | Risk / Engineering | CIP-007-6 R2 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-5 |
| Track all identified OT vulnerabilities with CVSS scores and OT-specific impact assessment (operational, safety, reliability). CVSS scores alone are insufficient for OT prioritization - availability impact must be assessed separately. | All OT | Risk | [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.4 · CIP-007-6 R2 |
| OT exposure treatment and patch hygiene follow [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) with the BES schedule and CIP deviation overlay in [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md). When vendor-tested patches or OT-safe maintenance windows prevent treatment within the governing SLA, initiate risk acceptance and, for BES scope, the CIP deviation process. | **BES ONLY** | Risk / Governance | CIP-007-6 R2.2 |
| Where patches cannot be applied, document compensating controls reviewed by Engineering and approved by the CISO. | All OT | Risk / Engineering | CIP-007-6 R2.3 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-2(6) |

---

## 5. PROTECT: Reduce Attack Surface and Limit Blast Radius

### 5.1 Network Segmentation and Electronic Security Perimeters

Network segmentation is the primary architectural control in OT environments. It limits the blast radius of a compromise, prevents IT threats from crossing into OT, and is a non-negotiable NERC-CIP obligation for BES Cyber Systems.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Define and document all Electronic Security Perimeters (ESPs) surrounding BES Cyber Systems. ESPs must have a documented topology, all Electronic Access Points (EAPs) identified, and all permitted communications documented. | **BES ONLY** | Engineering / Governance | CIP-005-6 R1 |
| All communication across an ESP boundary must traverse an EAP with access controls. No BES Cyber System shall have an uncontrolled path to an external network. | **BES ONLY** | Engineering | CIP-005-6 R1.3 |
| All non-BES OT networks must be segmented from enterprise IT by a firewall or equivalent access control enforcing a default-deny posture. Permitted flows must be documented and reviewed annually. | All OT | Engineering | [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.2 · IEC 62443-3-3 SR 5.1 |
| Deploy an OT DMZ between enterprise IT and OT networks. The DMZ hosts historians, data aggregators, and systems requiring bidirectional IT/OT communication. No direct routed paths between IT and OT shall exist. | All OT | Engineering | [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §5.4 · IEC 62443-3-2 |
| Use unidirectional gateways (data diodes) for operationally one-directional data flows. Bidirectional connections must be justified and approved by Engineering and the CISO. | All OT | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SC-7(8) · IEC 62443-3-3 SR 5.2 |
| Segment OT networks internally by function and criticality. Control networks (SCADA, DCS, RTU) must be isolated from OT support networks (engineering workstations, HMI, historian). Lateral movement between OT zones must traverse an access control point. | All OT | Engineering | IEC 62443-3-2 · [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §5.4 |
| Wireless communications in OT environments require explicit Engineering approval, documented risk assessment, and compensating controls. No unapproved wireless access points shall be connected to any OT network. | All OT | Engineering / Risk | CIP-005-6 R2 · [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.5 |

### 5.2 Access Control and Identity Management

Controlling who can reach OT systems, and what they can do when they get there, is as important as network segmentation. Privileged access to OT systems is high-consequence access.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Grant access to OT systems using least privilege. Personnel receive only the access required for their specific role. No shared accounts on BES Cyber Systems. | **BES ONLY** | Engineering / Governance | CIP-007-6 R5.1 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6 |
| Implement and enforce a personnel risk assessment (PRA) program for all individuals with authorized access to BES Cyber Systems. PRAs must be completed before access is granted and renewed per CIP-004 requirements. | **BES ONLY** | Governance / Engineering | CIP-004-6 R3 |
| Maintain access authorization lists for BES Cyber Systems current within 7 calendar days. Revoke access within 24 hours of personnel departures or role changes. | **BES ONLY** | Engineering / Governance | CIP-004-6 R4 |
| Enforce multi-factor authentication (MFA) for all interactive remote access to BES Cyber Systems. Remote access must traverse an Intermediate System. | **BES ONLY** | Engineering | CIP-005-6 R2 |
| Log all access to OT systems - electronic and physical. Logs must capture user identity, system accessed, date/time, and session duration. | **BES ONLY** | Engineering | CIP-006-6 R1 · CIP-007-6 R4 |
| Conduct quarterly access reviews for all OT systems. Reviews must verify that access authorizations remain current, appropriate, and within least-privilege bounds. | All OT | Governance / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(7) · CIP-004-6 R4.2 |
| Prohibit the use of vendor default credentials on any OT system. Vendor-supplied default usernames and passwords must be changed before deployment or first connection to an OT network. | All OT | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-5(1) · CIP-007-6 R5.5 |

### 5.3 System Hardening and Configuration Management

OT systems must be hardened to their minimum required operational configuration. Unnecessary services, ports, and software expand the attack surface without adding operational value.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Enable only the ports, services, and software components required for operational function. Disable or remove all others. Document permitted ports and services per device class. | All OT | Engineering | CIP-007-6 R1 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-7 |
| Establish and maintain a secure configuration baseline for each OT platform class (SCADA servers, HMIs, historian, RTUs, protection relays, engineering workstations). Baselines must be reviewed annually and upon significant change. | All OT | Engineering | CIP-010-3 R1 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-6 |
| Detect and alert on unauthorized configuration changes to BES Cyber Systems within 35 days. Configuration change detection must be automated where technically feasible. | **BES ONLY** | Engineering / Risk | CIP-010-3 R1.4 |
| Manage all authorized configuration changes through a formal change management process. Emergency changes to OT systems require post-hoc documentation within 24 hours. | All OT | Governance / Engineering | CIP-010-3 R1 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-3 |
| Prohibit connecting removable media (USB drives, portable hard drives, maintenance laptops) to OT systems without an authorized malware scan and documented approval. | All OT | Engineering / Governance | CIP-010-3 R3 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) MP-7 |
| Implement application whitelisting or equivalent execution control on OT systems where technically feasible. Where not feasible, document the technical limitation and implement compensating controls. | All OT | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-7(5) · IEC 62443-3-3 SR 3.2 |

### 5.4 Physical Security

Cyber protections for OT systems are only as strong as the physical controls protecting the hardware. Physical security for BES Cyber Systems is a NERC-CIP compliance obligation, not a facilities management function.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Define and document Physical Security Perimeters (PSPs) for all locations containing High and Medium impact BES Cyber Systems. | **BES ONLY** | Governance / Engineering | CIP-006-6 R1 |
| Control and log all physical access to PSPs. Access must be restricted to authorized personnel. Visitors require escort. | **BES ONLY** | Engineering / Governance | CIP-006-6 R1.1–R1.6 |
| Protect all in-scope OT equipment - including substations, control rooms, and remote sites - with physical access controls appropriate to the criticality of housed assets: locked enclosures, controlled entry, and visitor logging at minimum. | All OT | Engineering / Governance | CIP-006-6 · [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.1 |
| Conduct physical security reviews of all PSP locations annually and upon significant change. Review findings feed the risk register. | **BES ONLY** | Risk / Governance | CIP-006-6 R1.10 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PE-1 |

---

## 6. DETECT: Find Threats Before They Find the Grid

### 6.1 Security Event Monitoring

Detection in OT environments requires purpose-built methods. Standard IT security tools applied naively to OT networks can cause operational disruptions. Monitoring must be passive-first and operationally coordinated.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Generate, collect, and review security event logs from all OT assets capable of log generation. Log collection must not rely on active polling of field devices where polling could affect device availability. | All OT | Risk / Engineering | CIP-007-6 R4 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-2 |
| Define and document OT-specific security events that require alerting: unauthorized access attempts, account lockouts, failed authentication, service start/stop, configuration changes, and connections to unexpected endpoints. | All OT | Risk | CIP-007-6 R4.1 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-4 |
| Route OT security event alerts to analysts capable of evaluating both security and operational context. A SCADA server communicating with an unknown external endpoint requires both cybersecurity analysis and operational team notification. | All OT | Risk / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4 · CIP-008-6 |
| Conduct security event log reviews on a defined and documented cycle. Reviews must include OT-specific anomaly detection analysis, not only signature-based alerting. | **BES ONLY** | Risk | CIP-007-6 R4.2 |

### 6.2 Threat Intelligence for OT

Enterprise threat feeds optimized for IT adversaries provide incomplete coverage of ICS/OT threat actors and attack techniques. OT-specific sources are required.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain active subscriptions to ICS/OT-specific threat intelligence sources: CISA ICS-CERT advisories, E-ISAC (Electricity ISAC), and vendor security bulletins for all OT platforms in use. | All OT | Risk | [NIST CSF 2.0](https://www.nist.gov/cyberframework) DE.CM · CIP-013-2 |
| Produce OT threat intelligence summaries for Engineering and Incident Response at least quarterly. Summaries must include relevant threat actor activity, newly disclosed ICS vulnerabilities, and intelligence specific to the organization's OT platforms. | All OT | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PM-16 · IEC 62443-2-1 |
| Participate in E-ISAC information sharing. Report indicators of compromise related to BES Cyber Systems per E-ISAC and NERC requirements. | **BES ONLY** | Risk / Governance | NERC Rules of Procedure · CIP-008-6 |

---

## 7. RESPOND: React Without Making It Worse

> **The OT Response Imperative**
>
> Response actions in OT environments carry consequences that IT incidents do not. Isolating a compromised IT server is a containment decision. Isolating a compromised SCADA workstation that controls generation dispatch or substation protection may affect grid reliability. Every response action in an OT environment must be evaluated for operational impact before execution. Response plans must be pre-coordinated with operational teams, not improvised during an incident.

### 7.1 Incident Response Planning

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain an OT Cybersecurity Incident Response Plan (IRP) that addresses: incident classification, notification and escalation paths, containment actions with operational impact assessment, evidence preservation, and recovery initiation. | All OT | Governance | [NIST CSF 2.0](https://www.nist.gov/cyberframework) RS · CIP-008-6 R1 |
| The OT IRP must include pre-coordinated response playbooks for high-probability OT scenarios: ransomware impacting OT networks, unauthorized access to BES Cyber Systems, loss of SCADA visibility, and supply chain compromise. | All OT | Governance / Engineering | CIP-008-6 R1 · [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) §6.7 |
| For BES Cyber System incidents, document and follow NERC-CIP CIP-008 reporting timelines. Personnel with reporting responsibilities must know the timelines and have them documented in the IRP. | **BES ONLY** | Governance | CIP-008-6 R1.3 |
| Conduct OT incident response tabletop exercises at least annually involving operational team representation - not only cybersecurity personnel. Lessons learned must be documented and drive IRP updates. | All OT | Governance / Risk | CIP-008-6 R3 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-3 |

---

## 8. RECOVER: Restore Operations and Capture Learning

### 8.1 Recovery Planning for OT Systems

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain documented recovery plans for all in-scope OT systems including: restoration procedures, backup media locations, vendor contacts, and RTOs aligned with operational requirements. | All OT | Governance / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-2 · IEC 62443-2-1 |
| BES Cyber System recovery plans must meet NERC-CIP CIP-009 requirements including documented plans, testing cadence, and plan update requirements. | **BES ONLY** | Governance | CIP-009-6 R1 |
| Maintain offline, verified backups of all OT system configurations, firmware, software, and operational data required for restoration. Backups must be stored in a location not accessible from the OT network being backed up. | All OT | Engineering | CIP-009-6 R1.2 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-9 |
| Test OT recovery plan procedures at least annually. Testing must validate that backups can be restored and that documented procedures produce a functional system. | **BES ONLY** | Governance / Engineering | CIP-009-6 R2 |
| Conduct post-incident reviews within 30 days of any significant OT security event. Reviews must identify root cause, control failures, and corrective actions. Corrective actions feed the risk register. | All OT | Governance / Risk | CIP-009-6 R3 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4(4) |

---

## 9. Training and Personnel Security

Personnel with access to OT systems must understand the unique risk environment they operate in. Security awareness for OT personnel must go beyond general enterprise training.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| All personnel with authorized access to BES Cyber Systems must complete OT cybersecurity awareness training annually. Training must be documented and records retained. | **BES ONLY** | Governance | CIP-004-6 R2 |
| All personnel with authorized access to any in-scope OT system must complete OT-specific security awareness training covering: social engineering in OT contexts, removable media risks, physical access procedures, and incident reporting. | All OT | Governance | CIP-004-6 R2 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AT-2 |
| Personnel with OT incident response responsibilities must complete role-based training covering their specific response duties before being assigned incident response roles. | All OT | Governance | CIP-004-6 R2.4 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AT-3 |
| CERG team members assigned to OT environments must maintain current knowledge of OT security principles, NERC-CIP requirements, and [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) / IEC 62443 guidance. Professional development plans must reflect this requirement. | All OT | Governance / CISO | CIP-004-6 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AT-3 |

---

## 10. Regulatory and Framework Alignment Summary

The following table maps this standard's major requirement areas to applicable regulatory frameworks and NIST controls. This is a compliance reference. Governance maintains the full NERC-CIP evidence matrix separately.

| **Requirement Area** | **NERC-CIP** | **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | **[NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)** | **IEC 62443** |
|---|---|---|---|---|---|
| Asset Inventory & Categorization | CIP-002-5.1a | GV.AM | CM-8 | §6.2 | SR 7.8 |
| Network Segmentation & ESPs | CIP-005-6 | PR.IR | SC-7 | §5.4, 6.2 | SR 5.1, 5.2 |
| Access Control | CIP-004/007-R5 | PR.AA | AC-2, AC-6 | §6.3 | SR 1.1–1.5 |
| Remote Access | CIP-005-6 R2 | PR.AA | AC-17, IA-3 | §6.3 | SR 1.13 |
| System Hardening | CIP-007-6 R1 | PR.PS | CM-6, CM-7 | §6.2 | SR 7.6 |
| Configuration Management | CIP-010-3 | PR.PS | CM-3, CM-6 | §6.2 | SR 7.6 |
| Patch Management | CIP-007-6 R2 | PR.PS | SI-2 | §6.4 | SR 3.3 |
| Physical Security | CIP-006-6 | PR.AA | PE-2, PE-3 | §6.1 | SR 2.1 |
| Security Monitoring | CIP-007-6 R4 | DE.CM | SI-4, AU-2 | §6.3 | SR 6.1, 6.2 |
| Incident Response | CIP-008-6 | RS | IR-2, IR-4 | §6.7 | SR 6.1 |
| Recovery Planning | CIP-009-6 | RC | CP-2, CP-9 | §6.7 | SR 7.3 |
| Supply Chain Risk | CIP-013-2 | GV.SC | SA-9, SR-3 | §5.2 | SR 1.9 |
| Personnel Training | CIP-004-6 | GV.RR | AT-2, AT-3 | §6.1 | SR 2.5 |
| Exposure Management | CIP-007-6 R2 | ID.RA | RA-5, SI-2 | §6.4 | SR 3.2 |

---

## 11. Exceptions and Escalation

No control in this standard may be waived without a documented exception. Exceptions to BES Cyber System requirements carry additional obligations.

| **Exception Type** | **Approval Required** | **Process** | **Review Cycle** |
|---|---|---|---|
| Standard exception (non-BES OT) | CISO | Submit risk acceptance via risk register with compensating control documentation. Engineering must review compensating controls before CISO approval. | Annual |
| BES Cyber System - compliance posture unaffected | CISO | Same as above, plus notation in NERC-CIP evidence library. Exception must not create a compliance gap. | Annual |
| BES Cyber System - CIP compliance impact | CISO + NERC-CIP deviation process | Initiate CIP deviation and mitigation plan. Notify regulatory liaison. Document mitigation plan with timeline. | Per mitigation plan milestones |
| Emergency exception (operational necessity) | CISO (post-hoc within 24 hours) | Operational team may take emergency exception to prevent grid disturbance. Document immediately. CISO reviews and either approves formal exception or directs expedited remediation. 30-day maximum duration. | 30 days maximum |

---

## 12. Document Control

| | |
|---|---|
| **Document ID** | CERG-STD-OT-001 |
| **Version** | 1.21 |
| **Approved By** | CISO |
| **Next Review** | Annual / Upon Significant Change / CIP Standard Revision |
| **Change Log** | 1.0 - Initial publication. BES and non-BES OT environments. |


### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 DRAFT | 2025 | CERG Governance | Initial release - BES and non-BES OT environments |

### Review Triggers

This standard must be reviewed annually and upon any of the following triggering events:

- Revision to any applicable NERC-CIP standard (CIP-002 through CIP-014)
- Significant change to the OT environment, new BES Cyber System categorizations, major architecture changes, or significant new vendor deployments
- A significant cybersecurity incident affecting any in-scope OT system
- Changes to [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) or IEC 62443 that materially affect the requirements herein
- Direction from the CISO or regulatory examination findings

Governance owns this document. The Governance Pillar Leader (OT/NERC-CIP) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

References below use the canonical IDs in [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) Document Catalog. Where the catalog notes an artifact is embedded in a parent operational package for V1, the parent is the authoritative location.

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - this standard is subordinate |
| Document Catalog and Naming Convention | [CERG-GOV-CAT-001](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative inventory of all CERG artifacts referenced here |
| Unified Control Baseline | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control spine, overlay matrix, evidence mapping (BES overlay) |
| NERC-CIP Operational Package | [CERG-PLN-CIP-001](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | OT/CIP operational binder - contains the NERC-CIP Evidence Library Procedure (formerly `CERG-GOV-CIP-001`), OT Exposure Management Procedure, BES access overlay, deviation template, CIP-013 plan, CIP-009 recovery package, and CIP-015 tracking |
