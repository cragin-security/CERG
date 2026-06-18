
# SURGE: Cyber Engineering, Risk & Governance

## NERC-CIP OPERATIONAL PACKAGE
### Evidence Library · OT VM · BES Access · Deviations · IT/OT Convergence · BES Categorization · ESP/EAP · CIP-013 · CIP-009 · CIP-015 (Forward-Looking)

---

| | |
|---|---|
| **Document ID** | CERG-PLN-CIP-001 |
| **Version** | 1.22 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | NERC-CIP Compliance Manager |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Standard** | [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) - Grid Control Systems Security Standard |
| **Supporting Documents** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) · [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [CERG-PRC-AV-001](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) · [CERG-PLN-IR-001](CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **Review Cycle** | Annual / Continuous tracking - evidence currency monthly |
| **Frameworks** | [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · IEC 62443-3-3 / 4-2 |
| **Regulations** | NERC-CIP v7 (CIP-002 through CIP-014) · CIP-015 (draft, forward-looking) · CIP-013-2 |
| **Environments** | BES Cyber Systems (Low / Medium / High Impact) + associated EACMS / PACS / PCAs |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Three-Lines-of-Defense Model](#2-three-lines-of-defense-model)
3. [CIP Version Strategy](#3-cip-version-strategy)
4. [BES Cyber System Categorization Procedure](#4-bes-cyber-system-categorization-procedure)
5. [ESP / EAP Topology Documentation](#5-esp--eap-topology-documentation)
6. [NERC-CIP Evidence Library Procedure (`CERG-GOV-CIP-001`)](#6-nerc-cip-evidence-library-procedure-cerg-gov-cip-001)
7. [OT Exposure Management Procedure (`CERG-PRC-VM-001`)](#7-ot-exposure-management-procedure-cerg-prc-vm-001)
8. [BES Cyber System Access Management Overlay](#8-bes-cyber-system-access-management-overlay)
9. [CIP Deviation and Mitigation Plan Template (`CERG-TMPL-CIP-001`)](#9-cip-deviation-and-mitigation-plan-template-cerg-tmpl-cip-001)
10. [IT/OT Convergence Security Architecture Guideline](#10-itot-convergence-security-architecture-guideline)
11. [CIP-013 Supply Chain Risk Management Plan](#11-cip-013-supply-chain-risk-management-plan)
12. [CIP-009 Recovery Plan Package](#12-cip-009-recovery-plan-package)
13. [CIP-015 INSM Implementation Annex](#13-cip-015-insm-implementation-annex)
14. [Operating Cadence and Reporting](#14-operating-cadence-and-reporting)
15. [Regulatory and Framework Alignment Summary](#15-regulatory-and-framework-alignment-summary)
16. [Document Control](#16-document-control)

---

## 1. Purpose and Scope

The OT Standard names several subordinate artifacts and obliges CERG to maintain a full NERC-CIP evidence library separately. Until this package, those named subordinates did not exist. This package assembles them: an evidence library procedure, an OT VM procedure, a BES access management procedure, a CIP deviation template, an IT/OT convergence guideline, BES categorization and ESP/EAP topology procedures, the CIP-013 supply chain plan, the CIP-009 recovery plan package, and a forward-looking treatment of CIP-015 INSM.

It applies to every BES Cyber System (Low / Medium / High Impact) and the associated Electronic Access Control / Monitoring Systems (EACMS), Physical Access Control Systems (PACS), and Protected Cyber Assets (PCAs).

> **Operate the Compliance, Don't Just Document It**
>
> A binder of CIP requirements is not compliance. Compliance is the continuous evidence that the controls are operating, RTO measured, configurations baselined, access reviewed, deviations tracked, lessons learned actioned. This package is the operating manual for producing that evidence on a schedule the regulator can audit.

---

## 2. Three-Lines-of-Defense Model

CERG operates as the **second line of defense** for CIP controls.

| **Line** | **Role** | **Who** |
|---|---|---|
| **First** | Implementation of controls in the field. | OT Operators (substation engineering, control center operations, OT IT support). |
| **Second** | Review, track implementation, evidence, and deviation; coordinate with Operators on control design and remediation. | CERG (NERC-CIP Compliance Manager, OT Risk Analyst, OT Security Engineer). |
| **Third** | Dispassionate assurance independent of both. | Internal Audit and/or external firms. |

The model is intentionally explicit so audit trails are clean: Operators do; CERG reviews and tracks; Audit independently assures. CERG never grades its own homework on first-line activities, and Operators are not asked to be their own auditors.

---

## 3. CIP Version Strategy

CERG operates against the **latest approved** version of each CIP Standard, with a documented adoption window for newly approved versions and a draft-tracking posture for proposed standards. Specifically:

- Active version baseline reviewed at every CIP filing-effective-date change.
- Migration period for newly approved CIP versions tracked as risk register entries until cutover is complete.
- Draft / proposed standards (presently including CIP-015 INSM) tracked per Section 13.

---

## 4. BES Cyber System Categorization Procedure

CIP-002 requires identification and categorization of BES Cyber Systems. CERG categorizes following Attachment 1 criteria; the procedure:

1. **Inventory all BES Cyber Assets** in the enterprise inventory with required metadata (function, location, criticality input from Operations).
2. **Apply Attachment 1 criteria** (Section 1, High Impact criteria; Section 2, Medium Impact; everything else Low).
3. **Group BCAs into BES Cyber Systems** along functional / physical lines per operator input.
4. **Identify associated systems**: EACMS, PACS, PCAs, BCSI repositories.
5. **Document the rationale** for each categorization, the assessor will want to see it.
6. **Review annually** and on material grid configuration / asset changes.

The categorization is reflected in the asset inventory and drives every subsequent CIP obligation.

---

## 5. ESP / EAP Topology Documentation

CIP-005 requires Electronic Security Perimeters (ESPs) and Electronic Access Points (EAPs). CERG maintains:

- A network diagram set showing every Medium and High Impact ESP, the EAPs defining it, and the connections crossing each EAP.
- Per-EAP documentation: device, firmware version, rule set, last reviewed, owner, evidence of inbound/outbound deny-by-default, and authentication for interactive remote access.
- Per-ESP documentation: enclosed BCS, EACMS, PACS, PCAs; supported categorization (Medium/High); evidence of monitoring (CIP-007 R4, and forthcoming CIP-015 INSM).
- Annual review (or sooner on architecture change) with evidence routed into the library (Section 6).

---

## 6. NERC-CIP Evidence Library Procedure (`CERG-GOV-CIP-001`)

The Evidence Library is the single, authoritative repository of CIP compliance evidence, what the auditor opens first.

### 6.1 Library Structure

The library is organized by CIP Standard, then by Requirement, then by Sub-requirement. Each leaf has:

| **Field** | **Description** |
|---|---|
| Standard / Requirement / Sub-Req | E.g., CIP-007-6 R2.2 |
| Applicability | Low / Medium / High |
| Owner | CERG role + Operator role |
| Evidence Artifact(s) | Specific document / report / configuration / log |
| Evidence System of Record | Where the live artifact lives |
| Refresh Cadence | Monthly / Quarterly / Annual / 15-month / 36-month |
| Last Refresh | Date |
| Next Refresh | Date |
| Status | Current · Approaching Expiry · Expired |
| Deviation in Place? | Per Section 9 |
| Notes | - |

### 6.2 Evidence Discipline

- Every CIP Requirement applicable to in-scope assets has at least one Evidence Artifact named in the library.
- Evidence is gathered through normal operations (CERG-managed scans, configuration capture, access reviews), not assembled at audit time.
- Refresh cadences are driven from this library to the operating cadence (Section 14).

### 6.3 Reused Evidence

CIP evidence reuses the broader CERG evidence catalog wherever possible (per [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 8). The library cites where it lives rather than duplicating the artifact.

---

## 7. OT Exposure Management Procedure (`CERG-PRC-VM-001`)

The enterprise exposure management procedure ([`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)) governs IT scopes; this OT-specific procedure overlays it with OT-safe practices.

### 7.1 Identification

- **Passive scanning** is the default for live OT surfaces.
- **Authenticated checks** under engineering supervision in defined windows.
- **Vendor advisories** subscribed; advisories triaged against in-service firmware / software inventories.
- **NVD / CISA ICS Advisories** subscribed.
- Active scanning is permitted only under an approved scope and time window per [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) Section 9.

### 7.2 Risk Assessment and Treatment

- Vulnerabilities mapped against CIP-007 R2 patch evaluation cycle (35 calendar days from release for Medium/High Impact to evaluate; per the standard's specifics).
- Treatment options: apply patch in next maintenance window · implement compensating control · accept via Risk Register and CIP deviation if a deviation is required (Section 9).

### 7.3 Patching

- Patch evaluation cadence per CIP-007 R2.
- Patch deployment per CIP-010 R1, configuration changes require baseline update, security impact analysis, and authorization.
- Patch evidence retained in the Evidence Library per CIP-007 R2.4.

### 7.4 Documentation

- Per the procedure in [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) Section 6 with OT-specific fields: applicability to BES, CIP-007 R2 timing, CIP-010 R1 change record.

---

## 8. BES Cyber System Access Management Overlay

CIP-004 R4 / R5 obligations are operationalized as an embedded BES overlay on [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md).

### 8.1 Authorization

- Access to BES Cyber Systems is authorized only after the individual has met CIP-004 personnel risk assessment requirements (background check, training).
- Authorization is documented with a named approver per role.
- Reviews per CIP-004 cadence (every 15 months, plus on role change).

### 8.2 Provisioning and Revocation

- Provisioning of unescorted physical access to ESPs and electronic access to BCS goes through PAM-mediated workflows where supported.
- Revocation within 24 hours of termination (CIP-004 R5.1), CERG operates against 1 hour for involuntary terminations.
- BCSI access is governed under CIP-011 (information protection).

### 8.3 Vendor Remote Access

- Brokered through approved gateways with session recording.
- Authenticated per CIP-005 R2; monitored per CIP-005 R2.5 (interactive remote access via intermediate system).
- Vendor identities enrolled via [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) Section 10 and [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md).

---

## 9. CIP Deviation and Mitigation Plan Template (`CERG-TMPL-CIP-001`)

When a CIP requirement cannot be met as written (or cannot be met for a defined window), CERG documents a deviation and mitigation plan. This is in addition to the risk register entry in [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

```
CIP DEVIATION AND MITIGATION PLAN - DEV-CIP-YYYY-NNNN

A. DEVIATION IDENTIFICATION
   Standard / Requirement   :  (e.g., CIP-007-6 R2.2)
   Applicability            :  Low / Medium / High
   Affected BCS / EACMS / PACS / PCAs
   Discovered By            :
   Discovery Date           :
   Description              :  Specific, requirement-citing language

B. CAUSE
   Why the requirement is not met as written

C. RISK
   Risk Register ID (per [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md))
   Residual Risk Score
   Operator Sign-Off

D. MITIGATION
   Compensating control(s) - specific, in-place, named, evidenced
   Detection coverage uplift (if applicable)

E. PLAN TO ELIMINATE THE DEVIATION
   Steps                    :
   Owner                    :
   Target Closure           :

F. APPROVAL
   CERG NERC-CIP Compliance Manager     :
   CISO                :
   Operations               :

G. RECORD
   Library Reference        :  (where deviation lives in Section 6 library)
   Self-Report Required?    :  Y/N
   Self-Report Submitted    :  Date if applicable
```

> **Deviations Get Self-Reported When Self-Reporting Is the Right Call**
>
> CERG works with Operations and Legal to determine when a deviation is a self-reportable noncompliance under the regional entity's self-reporting program. The deviation record above always exists; whether to self-report is a deliberate Legal / Compliance / CISO decision, not a default.

---

## 10. IT/OT Convergence Security Architecture Guideline

This embedded convergence guideline informs architecture decisions where IT systems touch OT systems. It is the V1 authoritative location for the planned standalone `CERG-GL-OT-001` guideline until that reserved artifact is promoted in a future catalog amendment. It is referenced by [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) for any project crossing the IT/OT boundary.

### 10.1 Foundational Patterns

- **No flat IT/OT networks.** Convergence happens at named, documented EAPs.
- **One-way logging out of OT, brokered control into OT.** Data flows out of OT to SIEM are one-way; control / management flows into OT traverse identity, authorization, and recording controls.
- **Identity-first segmentation.** IT identity does not auto-translate to OT identity; OT identities are separate and governed by Section 8.
- **DMZ / industrial DMZ.** Where IT systems consume OT data, an industrial DMZ holds data brokers, historians, and integration services.
- **Engineering-tool isolation.** Engineering tools live on managed engineering workstations only; not on general-purpose corporate endpoints.

### 10.2 Pattern Reviews

The guideline catalogs approved IT/OT integration patterns:

- Historian-as-publisher (read-only, broker-mediated).
- Operator workstation reading OT data via DMZ.
- Vendor remote access via brokered jump.
- Cloud-hosted analytics consuming OT data via one-way export.
- IT identity using OT data in business analytics platforms.

Each pattern lists the controls, the diagrams required, and the architecture review depth.

### 10.3 Anti-Patterns

- Direct IT→OT VPN without brokering.
- OT-side credentials used by IT business processes.
- IT-side patching tools reaching into OT.
- Cloud agents installed directly on OT endpoints.
- File shares straddling IT and OT trust boundaries.

---

## 11. CIP-013 Supply Chain Risk Management Plan

Operationalized in coordination with [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). The CIP-013 Plan satisfies CIP-013-2 R1 and is reviewed annually (R3).

### 11.1 Scope

Vendor relationships involving Medium or High Impact BCS planning, design, installation, deployment, software/firmware/services, vendor remote access.

### 11.2 Components

| **R1 Risk Area** | **CERG Implementation** |
|---|---|
| Notification of vendor incidents | Contract clause + SCCT activation per [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) Section 15 |
| Coordination of incident response | SCCT + [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) interface |
| Notification of vendor personnel changes affecting access | Contract clause + CIP-004 access revocation per Section 8 |
| Disclosure of known vulnerabilities | Subscription to vendor advisories + Section 7 OT VM |
| Software / firmware integrity verification | [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) + [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) Section 11 |
| Vendor remote access - coordination of session controls | Section 8 + [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### 11.3 Evidence

CIP-013 evidence flows from this section into the Evidence Library (Section 6).

---

## 12. CIP-009 Recovery Plan Package

Operationalized in coordination with [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md). The CIP-009 obligations:

| **CIP-009 Requirement** | **CERG Implementation** |
|---|---|
| R1.1 Plan specifications | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) Section 11 Recovery Plan template + Section 7 OT artifacts |
| R1.2 Roles and responsibilities | Documented per plan |
| R1.3 Process for backup management | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) Section 4 |
| R1.4 Method for preserving recovery data | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) Section 7.1 |
| R1.5 Operator-led recovery | Plan names operator with substation engineering authority |
| R2.1 Testing | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) Section 5 - at least every 15 months |
| R2.2 Operational exercise | Every 36 months - full operational exercise |
| R3 Lessons learned and plan update within 90 days | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) Section 5.2 step 8 |

---

## 13. CIP-015 INSM Implementation Annex

CIP-015 (Internal Network Security Monitoring) is tracked as a forward-looking obligation for Medium and High Impact BES Cyber Systems. This annex operationalizes the CIP-015 readiness overlay referenced in CB-001 §8 BES Overlay. Until CIP-015 becomes enforceable for the organization, CERG treats this annex as a readiness investment; upon applicability, it becomes an audit-asserted operational procedure.

> **INSM Is Not Optional for Medium/High Impact BCS**
>
> Once CIP-015 becomes enforceable, operators of Medium and High Impact BES Cyber Systems must demonstrate continuous internal network security monitoring. This annex ensures CERG is not scrambling on day one.

### 13.1 Scope and Applicability

| **Scope Element** | **Coverage** |
|---|---|
| BES Impact Levels | Medium and High Impact BES Cyber Systems |
| Associated Systems | EACMS, PACS, PCAs within the ESP boundary |
| INSM Objective | Detect anomalous or malicious activity on internal OT networks at the ESP/EAP boundary and within the BES Cyber System interior |
| Regulatory Driver | CIP-015 (draft, forward-looking); CB-001 §8 BES Overlay |
| CERG Readiness Obligation | Produce evidence of readiness decisions, sensor coverage maps, and gap analysis until applicability |

### 13.2 Network Sensor Placement

Sensor placement follows the ESP/EAP topology documented in Section 5 and the IT/OT convergence architecture in Section 10.

| **Sensor Location** | **Placement Requirement** | **Monitoring Purpose** |
|---|---|---|
| EAP ingress/egress (IT side) | One sensor per EAP monitoring all inbound and outbound traffic crossing the ESP boundary | Detect unauthorized traversal, protocol anomalies, command-and-control patterns, data exfiltration attempts |
| EAP interior (OT side) | One sensor within each ESP monitoring east-west traffic between BCS inside the same ESP | Detect lateral movement, insider-threat activity, protocol violations, unauthorized device-to-device communication |
| IT/OT DMZ | Sensor at each industrial DMZ monitoring historian and data-broker flows | Detect data exfiltration, unauthorized data access, corrupted historian feeds |
| Vendor remote-access gateway | Sensor at the vendor VPN/concentrator egress monitoring all remote sessions | Detect unauthorized vendor activity, session hijacking, credential misuse |
| Field-location aggregation point | Where substations or remote sites aggregate, a sensor at the aggregation uplink | Detect compromised field devices communicating anomalously |

#### Sensor Density Guidelines

- Each Medium Impact ESP: Minimum 1 sensor covering EAP ingress/egress.
- Each High Impact ESP: Minimum 2 sensors — one at EAP boundary, one for interior east-west monitoring.
- Any ESP with >50 BCA devices: Add 1 sensor per additional 50 BCAs or fraction thereof, distributed across logical segments.
- Sensor coverage evidence: Documented in the ESP/EAP topology diagram (Section 5) with sensor locations annotated.

### 13.3 Data Collection Requirements

| **Data Type** | **Source** | **Collection Method** | **Retention** | **CIP-015 Relevance** |
|---|---|---|---|---|
| NetFlow / IPFIX | Network switches and routers at EAPs and interior segments | Flow export to collector; minimum 1:4096 sampling for high-throughput links | 90 days (CIP-006 minimum); 365 days for High Impact | Network baseline, anomaly detection |
| Full packet capture | EAP ingress/egress for High Impact ESPs | 10% sampled PCAP at EAP; 100% on High Impact EAPs for control-session traffic | 30 days rolling; 90 days for security events | Forensic analysis, threat-hunting |
| DNS query logs | Authoritative DNS resolvers serving OT zones | Syslog to SIEM | 365 days | C2 detection, beacon identification |
| Authentication events | Active Directory / LDAP, PAM, RADIUS servers | Syslog / Windows Event Forwarding to SIEM | 365 days | Unauthorized access detection |
| OT protocol logs | Protocol-aware monitoring (DNP3, Modbus, IEC 61850, IEC 104 pass-through) | Deep packet inspection via OT-IDPS or protocol-aware sensor | 90 days; 365 days for security events | Protocol anomaly detection, control-command validation |
| Firewall / ACL logs | ESP boundary firewalls, EAP devices | Syslog to SIEM | 90 days; 365 days for High Impact | Policy violation detection |
| Endpoint detection logs | OT endpoints with approved host-based monitoring | Agent-based (where available and OT-safe) or log export | 90 days | Host compromise detection |
| Vendor remote-access logs | PAM gateway, VPN concentrator | Session recording + metadata to SIEM | 365 days; indefinite for security incidents | Vendor anomaly detection |

#### Collection Integration

- All INSM data sources feed into the enterprise SIEM per [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) Section 4.
- Where SIEM ingestion is not feasible (e.g., air-gapped OT environments), a local log collector forwards to SIEM via one-way data diode.

### 13.4 Alerting Rules and Detection Baseline

The following alert categories are the minimum detection baseline for Medium and High Impact BES Cyber Systems. Rules are implemented in the SIEM and maintained by the Detection Engineer per [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) Section 6.

| **Alert Category** | **Rule Description** | **Severity** | **Response SLA** |
|---|---|---|---|
| Unauthorized EAP traversal | Device not on authorized BCA list communicating across EAP | Critical | 1 hour |
| Protocol anomaly | DNP3/Modbus/IEC 61850 message outside allowed function codes or address range | High | 2 hours |
| Beaconing / C2 | Outbound connection to untrusted destination with periodic patterns | Critical | 1 hour |
| New device on OT segment | MAC or IP not in asset inventory detected on OT LAN | High | 4 hours |
| Authentication spike | >10 failed authentication attempts on any OT system in 5 minutes | Medium | 4 hours |
| Vendor session anomaly | Vendor remote access outside approved schedule or from unexpected location | Medium | 2 hours |
| Configuration drift | Baseline comparison of ESP/ EAP rule set differs from authorised baseline | High | 4 hours |
| Data volume anomaly | Outbound data transfer from OT DMZ exceeding 3x rolling 30-day average | High | 2 hours |
| Controller firmware change | Firmware hash change on BES Cyber System controller | Critical | 1 hour |
| Rogue DHCP / ARP spoof | DHCP server or unexpected ARP announcement within ESP | High | 2 hours |

#### Alert Tuning and False-Positive Management

- All alerting rules start in test mode for 30 days post-deployment.
- After 30 days, rules are moved to active monitoring with a 14-day tuning window.
- False-positive rate >5% per rule triggers re-evaluation and rule revision.
- Tuning documentation is retained in the evidence library.

### 13.5 Evidence Package

CIP-015 evidence is collected and stored in the NERC-CIP Evidence Library (Section 6) under CIP-015 requirements.

| **Evidence Item** | **Source** | **Cadence** | **CIP-015 Requirement** |
|---|---|---|---|
| Sensor inventory and placement diagram | Section 13.2 sensor tables + ESP/EAP diagrams | Annual + on change | R1 (monitoring coverage) |
| Data collection configuration | SIEM data source inventory | Quarterly | R2 (data collection) |
| Alerting rule inventory | SIEM rule registry | Quarterly | R3 (analysis) |
| Sample alert records | SIEM alert history (10 per category per quarter) | Quarterly | R3 (analysis) |
| False-positive tuning log | SIEM tuning tickets | Quarterly | R3 (analysis) |
| Sensor health check | Sensor uptime report | Monthly | R1 (monitoring coverage) |
| Coverage gap analysis | Section 13.6 | Quarterly | R1, R2 |
| Response time measurement | Alert-to-investigation timestamp logs | Quarterly | R4 (response) |
| INSM governance record | Risk-register entries, readiness decisions | Annual | Cross-cutting |

### 13.6 Coverage Gap Analysis

A formal gap analysis is performed quarterly, comparing current INSM coverage against the CIP-015 draft requirements and CB-001 §8 BES Overlay expectations.

| **Gap Category** | **Assessment Question** | **Acceptable State** | **Escalation Path** |
|---|---|---|---|
| Sensor coverage | Does every Medium/High ESP have at least one sensor? | Yes for Medium; minimum 2 for High | Gap >30 days → CISO escalation |
| Data source coverage | Are all data types in Section 13.3 being collected? | ≥80% of required data types collected | Gap >90 days → Risk Register entry |
| Alert coverage | Are all alert categories in Section 13.4 active? | 100% of Critical/High alert categories active | Gap >14 days → Risk Register entry |
| Retention compliance | Are data retention periods meeting Section 13.3 minimums? | 100% of data types at min retention | Gap → Deviation record per Section 9 |
| Response time adherence | Are alert response SLAs being met? | ≥90% within SLA | Gap → Corrective action per Section 8 |

Gaps are documented in the risk register and tracked as deviation items per Section 9 until closure.

### 13.7 Integration with Existing CERG Capabilities

| **CERG Capability** | **Integration Point** | **INSM Dependency** |
|---|---|---|
| Exposure Management ([`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)) | Vulnerability scan findings correlated with INSM alert data to identify actively exploited vulnerabilities | INSM provides active-threat context for vulnerability prioritisation |
| Logging and Detection ([`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)) | OT telemetry added to SIEM as mandatory log source per LM-001 §4; alert rules follow LM-001 §6 | LM-001 is the procedural owner of SIEM ingestion and rule management |
| Threat Intelligence ([`CERG-PRC-TI-001`](../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md)) | OT-specific threat intel feeds enrich INSM alerts (e.g., ICS-CERT advisories, sector-specific IOCs) | INSM alerting rules consume threat intel for contextual alerting |
| Incident Response ([`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md)) | INSM alerts feed incident triage; playbooks incorporate OT-specific containment | IR team requires INSM evidence for OT incident scoping |
| Architecture Review ([`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)) | New OT projects include INSM sensor placement review in architecture intake | INSM coverage is a gate criterion for OT project production handoff |
| Adversarial Validation ([`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)) | Penetration test scope includes INSM alert evasions to test detection coverage | AV tests validate INSM effectiveness |
| Risk Register ([`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)) | INSM coverage gaps recorded as risk items with compensating controls | Risk register tracks residual detection risk |

### 13.8 Readiness Activities (Pre-Applicability)

Until CIP-015 is enforceable, CERG performs the following readiness activities:

1. **Map existing OT telemetry sources** to expected INSM coverage objectives (Section 13.3).
2. **Identify ESP / EAP monitoring gaps** that would affect Medium or High Impact BES Cyber Systems.
3. **Deploy minimum viable sensors** at EAP ingress/egress for High Impact ESPs.
4. **Implement baseline alerting rules** for Critical and High alert categories (Section 13.4).
5. **Route monitoring backlog items** through [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) and the risk register when coverage cannot be implemented immediately.
6. **Preserve evidence of readiness decisions** in the Evidence Library (Section 6).

### 13.9 Cutover Trigger

When CIP-015 becomes applicable, Governance:
1. Updates this annex from "readiness" to "enforceable" status.
2. Sets evidence collection cadences from "on readiness" to Section 13.5 table frequencies.
3. Activates all alerting rules from test mode to active monitoring.
4. Updates compliance calendar with enforceable evidence requirements.
5. Notifies all NERC-CIP Compliance Manager, OT Security Engineer, and Detection Engineer roles.
6. Creates CIP-015-specific evidence library entries per Section 6.

---
## 14. Operating Cadence and Reporting

| **Activity** | **Cadence** |
|---|---|
| Evidence library refresh sweep | Continuous; full review monthly |
| BES categorization review | Annual + on material change |
| ESP/EAP topology review | Annual + on architecture change |
| CIP-004 access reviews | Per CIP cadence (≤ 15 months); CERG operates quarterly |
| CIP-007 R2 patch evaluation | Per CIP cadence |
| CIP-009 recovery testing | Every 15 months minimum; full exercise every 36 months; CERG operates annually |
| CIP-010 baseline review | Per CIP cadence |
| CIP-013 plan review | Annual (R3) |
| Deviation register review | Monthly |
| Reg posture report | Quarterly per `CERG-GOV-MTR-001` |
| Internal CIP walkthrough | Quarterly (sampling) |
| Independent (third-line) review | Annual minimum |

---

## 15. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Package** |
|---|---|
| CIP-002 | Section 4 |
| CIP-003 | Cross-cutting (policy + program); Section 2 |
| CIP-004 | Section 8 |
| CIP-005 | Section 5 |
| CIP-006 | Interface to Facilities (out of CERG scope; coordinated) |
| CIP-007 | Sections 5–7, evidence library |
| CIP-008 | Interface to `CERG-PLN-IR-001` |
| CIP-009 | Section 12 + `CERG-STD-RES-001` |
| CIP-010 | Sections 5, 7 + `CERG-STD-CFG-001` |
| CIP-011 | Section 8 + `CERG-STD-CR-001` |
| CIP-013 | Section 11 + `CERG-PRC-TPRM-001` |
| CIP-014 | Interface to Facilities |
| CIP-015 (draft) | Section 13 + `CERG-STD-LM-001` |
| [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Sections 7, 10 + `CERG-STD-OT-001` / `CERG-STD-CFG-001` |
| IEC 62443-3-3 / 4-2 | Sections 7, 10 |

---

## 16. Document Control

| | |
|---|---|
| **Document ID** | CERG-PLN-CIP-001 |
| **Version** | 1.22 |
| **Approved By** | CISO |
| **Next Review** | Annual / on CIP version or filing change |
| **Change Log** | 1.0 - Initial publication. Evidence library, OT VM, BES access, deviation template, IT/OT convergence guideline, categorization, ESP/EAP, CIP-013, CIP-009, CIP-015 forward-looking. 1.22 - Expanded CIP-015 §13 from preliminary section to full INSM Implementation Annex with sensor placement, data collection, alerting rules, evidence package, gap analysis, and integration map. |

