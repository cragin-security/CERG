
## PCI DSS OPERATIONAL PACKAGE
### Control Library · CDE System Register · Evidence Reuse · Deficiency Workflow · ASV Program Interface

---

|  |  |
|---|---|
| **Document ID** | CERG-PLN-PCI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (PCI Program) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Documents** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) · [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) |
| **Supporting Documents** | [`CERG-STD-IT-001`](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) · [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) |
| **Review Cycle** | Annual / Per PCI DSS version change / Per QSAR cycle |
| **Frameworks** | PCI DSS v4.0.1 · NIST 800-53r5 mappings · NIST SP 800-115 (penetration testing) |
| **Regulations** | Payment Card Industry Data Security Standard v4.0.1 |
| **Environments** | Cardholder data environment (CDE) and connected system components |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [CDE Scope Definition](#2-cde-scope-definition)
3. [CDE System Register](#3-cde-system-register)
4. [PCI Control Library](#4-pci-control-library)
5. [Evidence Reuse Mapping](#5-evidence-reuse-mapping)
6. [ASV Program Interface](#6-asv-program-interface)
7. [SAQ / ROC Deficiency Workflow](#7-saq--roc-deficiency-workflow)
8. [Auditor and QSAR Interface](#8-auditor-and-qsar-interface)
9. [Operating Cadence](#9-operating-cadence)
10. [Regulatory and Framework Alignment Summary](#10-regulatory-and-framework-alignment-summary)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

PCI DSS compliance is a business requirement that has traditionally sat outside the cybersecurity operating model, treated as a separate exercise with separate evidence, separate scans, and a separate audit cycle. CERG inverts this: PCI DSS is a scope filter over the controls CERG already operates, with CDE-specific parameters, a dedicated system register, and a defined interface to the ASV program and QSAR auditor.

This package fills the gap. It assumes the organization stores, processes, or transmits cardholder data (CHD) or sensitive authentication data (SAD) as defined by PCI DSS v4.0.1.

> **The CERG PCI Model in One Sentence**
>
> PCI DSS is not a separate control universe; it is a scope filter over the controls CERG already operates, with automated evidence collection for the CDE, quarterly ASV integration, and a documented SAQ/ROC evidence package that is current between assessments.

### 1.1 Scope of This Package

- All system components that store, process, or transmit CHD or SAD
- All system components with unrestricted connectivity to CDE components
- All third-party service providers (TPSPs) that store, process, or transmit CHD on behalf of the organization
- All network security controls (NSCs) that segment the CDE from untrusted networks

### 1.2 Out of Scope

- Compliance with PCI DSS for acquiring banks, issuing banks, or payment processors that maintain their own PCI scope separate from the organization
- PIN pad certification or EMV implementation details (these are handled by the acquiring bank's certification program)
- Physical security of POI devices owned by a third-party acquirer or processor (but the organization must confirm the provider's PCI compliance)

---

## 2. CDE Scope Definition

CDE scope follows the PCI DSS definition: any system component that stores, processes, or transmits CHD/SAD, or any system component with unrestricted connectivity to such systems.

### 2.1 Segmentation Decision Tree

| Question | Action |
|---|---|
| Does the system store, process, or transmit PAN? | Yes → In scope (CDE) |
| No → Does the system have unrestricted network connectivity to a CDE system? | Yes → In scope (CDE) |
| No → Is the system a security control (NSC, logging, authentication) that manages CDE traffic? | Yes → In scope (CDE) |
| No → Is the system in the same flat network segment as CDE systems? | Yes → In scope (CDE) unless formally segmented |
| No → OUT OF SCOPE | Document rationale per §3 register |

> **Segmentation Reduces Scope; It Does Not Eliminate Burden**
>
> Properly segmented networks with documented NSCs reduce the scope of PCI compliance. Every claim of segmentation must be evidenced by a network diagram, firewall rule exports, and a segmentation test result performed at least quarterly. Unsubstantiated segmentation claims are the most common source of scope-scope creep during QSARs.

### 2.2 Scope Validation Cadence

| Activity | Cadence | Evidence |
|---|---|---|
| Scope confirmation | Quarterly — before ASV scan cycle | Updated CDE System Register (§3) with scope rationale |
| Segmentation test | Quarterly | Segmentation testing result (per Req 1.4) |
| Network diagram review | Every 6 months | Reviewed and approved CDE data-flow diagram |
| TPSP scope confirmation | Annual — before SAQ/ROC submission | Updated TPSP register with PCI relevance flag |

---

## 3. CDE System Register

The Register is the scope filter for PCI DSS: every system in this register is treated as in-scope for PCI controls. Out-of-scope systems are listed with segmentation rationale.

| Field | Description |
|---|---|
| System Name / Asset ID | — |
| Owner | Named role (may be same as CERG asset owner) |
| CHD/SAD Status | Stores CHD / Processes CHD / Transmits CHD / No CHD (segmented) |
| Segmentation Method | Flat (in scope) / NSC (firewall segment) / Air-gapped / No connectivity |
| Last Segmentation Test | Date of most recent quarterly segmentation test (in scope — Req 1.4) |
| SAQ Relevance | Merchant / Service provider / Both / Neither (e.g., supporting infrastructure) |
| In-Scope Domains | Access · Change · Operations · Backup · Networking · Physical (multi-select) |
| Outstanding PCI Findings | IDs referencing §7 register |
| Status | In Scope · Segmentation-Pending · Out-of-Scope (with rationale) · Transitional |

The register is owned jointly by CERG Governance (PCI program) and the named system owners. CERG owns the cyber control slice; the business unit owns scope accuracy.

---

## 4. PCI Control Library

Each control names the PCI DSS requirement it satisfies, the CERG control it reuses from [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md), the PCI-specific evidence the QSAR auditor expects, and the test approach.

### 4.1 Access PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-01 Access by Need-to-Know | Access to CDE systems is granted on business need and least privilege; reviewed every 6 months for humans, per risk analysis for app/system accounts. | AC-2, AC-6 ([`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md)) | Quarterly access recert; bi-annual privilege review; app/system account review | Sample of N per period |
| PC-02 MFA for CDE Access | MFA required for all non-console access into the CDE; replay-resistant mechanism (unique session IDs, timestamps, TOTP). | IA-2, AC-3 ([`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md)) | IdP policy export; MFA enforcement report; replay-attack protection evidence | Configuration review + sample |
| PC-03 Account Lockout | Lock account after ≤10 unsuccessful logon attempts; minimum 12-character password/passphrase. | AC-7, IA-2 ([`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md)) | IdP policy export; lockout audit logs | Configuration review |
| PC-04 Unique IDs | Every user and system account has a unique ID; group/shared IDs only on documented exception. | AC-2 ([`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md)) | User inventory; exception register | Sample of N |
| PC-05 Application/System Account Controls | Interactive login disabled for system accounts; credentials managed in password vault; business justification documented for exceptions. | IA-3, IA-5 ([`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md)) | Service account inventory; credential vault evidence; exception register | Configuration review + sample |

### 4.2 Network Security PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-06 Network Segmentation | CDE is segmented from untrusted networks via NSCs; deny-all-default with explicit allow rules; rules reviewed every 6 months. | SC-7 ([`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md)) | Network diagram; firewall rule export; NSC review evidence | Configuration review + quarterly segmentation test |
| PC-07 Boundary Protection | Inbound/outbound traffic to/from CDE is restricted to approved services only; anti-spoofing measures enabled. | SC-7 ([`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md)) | ACL exports; traffic-flow documentation; anti-spoofing config | Configuration review + quarterly test |
| PC-08 Transmission Encryption | CHD transmitted over open/public networks uses strong cryptography; certificates are valid, unexpired, and not revoked. | SC-8 ([`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)) | TLS scanner report; certificate validation evidence | Configuration review + continuous scanning |
| PC-09 Wireless Security | Wireless environments in or connected to CDE have vendor defaults changed; encryption keys rotated on personnel departure or compromise suspicion. | SC-7, CM-2 ([`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md)) | Wireless config export; key rotation log; AP inventory | Configuration review |

### 4.3 Data Protection PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-10 PAN Rendering Unreadable | PAN is rendered unreadable via truncation, hashing (keyed), tokenization, or strong cryptography; disk encryption alone is insufficient — must be combined with one of the above. | SC-28 ([`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)) | Data-at-rest validation report; keyed hash config; token vault config | Design review + sample validation |
| PC-11 Key Management | Cryptographic keys for CHD protection are managed with split knowledge and dual control; access restricted; stored separately from encrypted data. | IA-5 ([`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)) | KMS policy export; key access logs; split-knowledge evidence | Configuration review + sample inspection |
| PC-12 Data Retention and Disposal | SAD is not stored after authorization; SAD prior to authorization encrypted with strong cryptography; CHD retention policy documented; data disposed per policy. | — (PCI-specific, see PCI-SAD-001, PCI-SAD-002) | Data retention policy; SAD destruction evidence; CHD disposal log | Sample inspection |
| PC-13 CHD Messaging Protection | CHD is not transmitted via end-user messaging (email, SMS, chat) unless protected by approved encryption. | — (PCI-specific, see PCI-MSG-001) | Messaging policy; DLP evidence; exception register | Policy review + tool scan |

### 4.4 Logging and Monitoring PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-14 Automated Audit Logging | All CDE components produce automated audit trails capturing: user ID, event type, date/time, success/failure, origination, identity — per Req 10.2.1–10.2.8. | AU-2, AU-12 ([`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)) | SIEM source inventory with PCI event coverage; sample log entries per Req 10.3 fields | Configuration review + sample validation |
| PC-15 Automated Log Review | Logs are reviewed daily via automated mechanisms (SIEM); anomalies are investigated and tracked to closure. | AU-6 ([`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)) | SIEM dashboard; daily review evidence; investigation tickets | Sample of daily reviews |
| PC-16 Log Protection and Retention | Audit logs are protected from alteration and retained 12 months (most recent 3 months online). | AU-9, AU-11 ([`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)) | Storage policy; log integrity check; sample retrieval evidence | Configuration review + sample retrieval |
| PC-17 Change Detection | Change-detection mechanism deployed on CDE systems to alert on unauthorized modification of CHD or critical system files. | CM-6 ([`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)) | FIM config; change alert evidence; remediation tickets | Sample of detected changes + response |

### 4.5 Vulnerability Management PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-18 ASV Program | Quarterly external ASV scans by PCI SSC–approved scanning vendor; evidence of scan, remediation, and rescan. | RA-5 ([`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §ASV appendix) | ASV scan reports; ASV certificate; remediation evidence; rescans | Period review |
| PC-19 Internal Vulnerability Scanning | Internal vulnerability scans of CDE systems quarterly and after significant changes; authenticated scanning where supported. | RA-5 ([`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)) | Internal scan reports; vulnerability SLA dashboard; change-triggered scans | Period review |
| PC-20 Patch Management | Critical security patches deployed within 1 month; other patches per risk analysis. | SI-2 ([`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)) | Patch deployment evidence; SLA dashboard; exception register | Sample of N patches |
| PC-21 Anti-Malware | Anti-malware deployed on all at-risk CDE systems; automatic updates; periodic or real-time scanning; user cannot disable. | RA-5, SI-4 ([`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)) | Anti-malware coverage report; scan schedule; config evidence | Configuration review + coverage report |
| PC-22 Anti-Phishing | Anti-phishing mechanisms deployed (DMARC, SPF, DKIM); personnel trained on phishing detection. | SI-4, AT-2 ([`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)) | DMARC/SPF/DKIM config; phishing simulation results; training completion | Configuration review + sample of simulations |

### 4.6 Penetration Testing PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-23 Network Penetration Testing | Network-layer penetration testing of CDE perimeters annually and after significant infrastructure changes. | CA-8 ([`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)) | Pen test plan (NIST SP 800-115 methodology); findings report; remediation evidence; retest | Annual inspection |
| PC-24 Application Penetration Testing | Application-layer penetration testing of CDE-facing web applications annually and after significant changes. | CA-8, SDL-001 ([`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)) | App pen test plan; findings; remediation; retest | Annual inspection |
| PC-25 Payment Page Script Integrity | Inventory of all scripts that load in payment pages; integrity verification via SRI or CSP; change detection for unauthorized script injection. | — (PCI-specific, see PCI-SCR-001) | Payment script inventory; SRI/CSP config; change alert evidence | Configuration review + inventory reconciliation |

### 4.7 Physical Security PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-26 Physical CDE Access Control | Physical access to CDE facilities secured with video cameras or electronic access controls; logs retained at least 90 days. | PE-2, PE-3 ([`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) PSP model) | Video/access control logs; visitor logs; media inventory | Sample of logs |
| PC-27 POI Device Management | POI devices in CDE are inventoried, tamper-evident, inspected periodically; personnel trained on POI tamper detection. | — (PCI-specific, see PCI-POI-001) | POI inventory; tamper inspection records; training records | Sample of devices + training records |

### 4.8 Policy and TPSP PCI Controls

| PCI Ref | Control Statement | Reused CERG Control | PCI Evidence | Test Approach |
|---|---|---|---|---|
| PC-28 Information Security Policy | Information security policy covers PCI-specific requirements; reviewed annually; distributed to personnel with acknowledgment. | PL-1 ([`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md)) | Policy document; annual review record; acknowledgment evidence | Policy review |
| PC-29 TPSP Oversight | TPSPs that store, process, or transmit CHD are listed, assessed annually, under written agreement, and provide compliance evidence on request. | SR-2, SR-3 ([`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)) | TPSP PCI register; written agreements; compliance evidence; annual assessment | Sample of N TPSPs |
| PC-30 Security Awareness | Personnel with CDE access complete annual security awareness training covering CHD handling. | AT-2 ([`CERG-GOV-TRN-001`](../governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md)) | Training completion records; curriculum content evidence | Sample of records |

---

## 5. Evidence Reuse Mapping

The mapping in Section 4 reuses CERG's existing evidence library. The principle:

> **PCI DSS Reuses CERG Evidence; CERG Does Not Create PCI-Only Tests**
>
> If a CERG control test is already running at the cadence the QSAR requires, on a system in the CDE register, the QSAR test consumes that evidence. CERG does not produce a parallel "PCI-only" version. Where reuse is impossible — e.g., ASV requires an approved scanning vendor — CERG supplements with the PCI-specific artifact while documenting the reuse principle.

### 5.1 Most-Reused Artifacts

- Quarterly access recertification reports (PC-01)
- PAM session logs (PC-01)
- IdP policy and MFA enforcement reports (PC-02)
- Firewall rule exports and segmentation test results (PC-06, PC-07)
- TLS scanner reports and certificate validation (PC-08)
- Data-at-rest encryption validation (PC-10)
- KMS and key access policies (PC-11)
- SIEM source inventory with PCI event coverage (PC-14)
- Vulnerability scan reports and SLA dashboards (PC-18, PC-19)
- Patch deployment records (PC-20)
- Anti-malware coverage reports (PC-21)
- DMARC/SPF/DKIM configuration (PC-22)
- Penetration test plans and findings (PC-23, PC-24)
- Training completion records (PC-30)
- TPSP register and written agreements (PC-29)

### 5.2 PCI-Specific Evidence (Not Produced by CERG Baseline)

| PC Ref | Unique PCI Evidence | Production Responsibility |
|---|---|---|
| PC-12 | Data retention and disposal policy (SAD-specific) | Governance (PCI Program) |
| PC-13 | CHD messaging protection evidence | Governance (PCI Program) |
| PC-18 | ASV scan reports from approved scanning vendor | Risk (Exposure Management) |
| PC-22 | Phishing simulation results | Governance (Training) |
| PC-25 | Payment page script inventory; SRI/CSP configuration | Engineering (Application Security) |
| PC-27 | POI device inventory; tamper inspection records | Engineering / Business unit |
| PC-29 | TPSP compliance evidence requests | Risk (TPRM) |

---

## 6. ASV Program Interface

### 6.1 ASV Scan Cycle

| Step | Action | Owner | Cadence |
|---|---|---|---|
| 1 | Identify CDE external IP ranges from CDE System Register | PCI Program Lead | Before each scan cycle |
| 2 | Submit IP range(s) to approved ASV per contract | PCI Program Lead | Quarterly |
| 3 | ASV performs external vulnerability scan per PCI SSC Approved Scanning Vendor rules | Approved ASV | On submission |
| 4 | Review ASV findings; assign severity; create remediation tickets | Risk (Exposure Management) | Within 5 business days of ASV report |
| 5 | Remediate High/Critical findings per CERG PRC-VM-001 SLA (or within ASV rescans window, whichever is tighter) | Engineering / System owner | Within 2 weeks |
| 6 | Request ASV rescan on remediated IPs | PCI Program Lead | After remediation |
| 7 | Archive ASV report and rescan results in evidence library under `/frameworks/pci-dss/asv/<YYYY-QN>/` | Evidence Librarian | On receipt |
| 8 | Record scan status in CDE System Register (§3) | PCI Program Lead | On completion |

### 6.2 ASV Failure Handling

| Condition | Action | Escalation |
|---|---|---|
| ASV finds a High/Critical vulnerability | Open remediation ticket per PRC-VM-001 SLA | Risk Pillar Leader within 48 hours |
| ASV rescan shows same vulnerability unfixed | Escalate to system owner and Engineering Pillar Leader | If unresolved after 30 days, escalate to CISO |
| ASV reports new finding not in internal scanner | Reconcile scanner coverage; update internal scan scope | Risk Pillar Leader (Exposure Management) |
| ASV report missed the scan window | Contact ASV for SLA remediation; document in PCI risk register | Governance Pillar Leader |

---

## 7. SAQ / ROC Deficiency Workflow

| Step | Detail |
|---|---|
| Identification | Deficiency identified via ASV report, internal scan, control test failure, internal audit, external QSAR, or management self-assessment. |
| Categorization | Non-Compliance / Deficiency / Remediation Required — per the applicable SAQ type or ROC template. CERG provides facts; QSAR determines severity. |
| Root cause analysis | CERG performs RCA; identifies whether issue is design (control missing) vs. operating (control exists but failed). |
| Remediation plan | Owner, milestones, target date; recorded in the PCI finding register (§3 Outstanding PCI Findings) and the CERG risk register. |
| Compensating control | If applicable, named and evidenced per PCI DSS compensating control requirements (eligible only if: meets business need, meets the objective as well as or better than the original requirement, is above and beyond other controls, commensurate with risk). |
| Validation | At completion of remediation, control evidence is validated internally before next ASV or QSAR cycle. |
| Disclosure | Findings that would affect SAQ/ROC attestation are reported to executive management and the acquiring bank. |

---

## 8. Auditor and QSAR Interface

| Activity | CERG Action |
|---|---|
| Scoping meeting with QSAR | Provide updated CDE System Register; reconcile in/out of scope; confirm segmentation evidence. |
| ASV evidence for QSAR | Provide current-year ASV approval letter, quarterly scan and rescans reports. |
| Evidence package assembly | Compile per §5 reuse mapping; evidence library current by control; POA&M for open items. |
| SAQ / ROC walkthrough | CERG participates with system owners; provides evidence references. |
| QSAR testing | CERG provides evidence per the library; supports walkthroughs with system owners. |
| Findings response | Per §7 deficiency workflow. |
| Attestation of Compliance (AoC) | CERG produces summary of PCI control posture for executive sign-off. |

### 8.1 QSAR Evidence Package

| Package Element | Source | Status |
|---|---|---|
| CDE System Register (§3) — current | CERG | Required |
| CDE network diagram with segmentation evidence | CERG Engineering (Network) | Required |
| ASV scan reports (all 4 quarters + rescans) | Approved ASV | Required |
| Internal vulnerability scan reports (quarterly) | CERG Risk (Exposure Management) | Required |
| Penetration test reports (annual network + app) | CERG Risk (Adversarial Validation) | Required |
| PCI control library evidence per §4 | CERG evidence library | Required |
| POA&M (open findings) | CERG risk register | Required if above items exist |
| TPSP PCI compliance evidence | TPSPs per §4 PC-29 | Required |
| Data-flow diagram (PCI scope) | CERG Engineering | Required |
| Training completion evidence | CERG Governance (Training) | Required |

---

## 9. Operating Cadence

| Activity | Cadence |
|---|---|
| CDE System Register reconciliation | Quarterly (before ASV cycle) |
| External ASV scan + rescan | Quarterly |
| Internal vulnerability scan | Quarterly |
| Segmentation test | Quarterly |
| NSC / NPM rule review | Every 6 months |
| Network diagram review | Every 6 months |
| Access recertification (human accounts) | Every 6 months |
| Access recertification (app/system accounts) | Per targeted risk analysis |
| Penetration test (network) | Annual |
| Penetration test (application) | Annual |
| Anti-phishing simulation | Per risk analysis (minimum annual) |
| PCI control test execution | Cumulative; full evidence package before QSAR |
| TPSP PCI compliance assessment | Annual |
| Security awareness training (PCI scope) | Annual |
| SAQ / ROC evidence package assembly | Before QSAR submission date |
| QSAR walkthrough | Per SAQ/ROC cycle |
| Post-QSAR deficiency review | Within 30 days of QSAR report |
| PCI program review | Annual |

---

## 10. Regulatory and Framework Alignment Summary

| Regulation / Framework | Where in This Package |
|---|---|
| PCI DSS v4.0.1 | Sections 2–9 |
| NIST 800-53r5 (mappings) | Section 4 reused control IDs |
| NIST SP 800-115 | Section 4 PC-23 (penetration testing methodology) |

---

## 11. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-PCI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (PCI Program) |
| **Effective Date** | 2026-06-27 |
| **Review Cycle** | Annual / Per PCI DSS version change / Per QSAR cycle |
| **Next Scheduled Review** | 2027-06-27 |
| **Frameworks** | PCI DSS v4.0.1; NIST 800-53r5; NIST SP 800-115 |
| **Regulations** | Payment Card Industry Data Security Standard v4.0.1 |
| **Environments** | Cardholder data environment (CDE) and connected system components |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-27 | Governance Pillar Leader (PCI Program) | Initial release. PCI DSS scope definition, CDE system register, 30-control PCI control library (PC-01 through PC-30), evidence reuse mapping, ASV program interface, SAQ/ROC deficiency workflow, QSAR evidence package, and operating cadence. |

### Review Triggers

- PCI DSS version change (v4.0.1 → v5.0 or mid-cycle revision)
- QSAR finding indicating a control library gap or scope misinterpretation
- Material change to CDE scope (new payment channel, new TPSP handling CHD, cloud migration of CDE)
- ASV vendor change or approved scanning vendor program change
- Direction from CISO or Governance Pillar Leader

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Unified Control Baseline | [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) | Reused control library; PCI overlay defined in §8 and §10.5 |
| CERG Operating Model | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Operating model |
| CDE System Register | §3 of this package | Owned register |
| Exposure Management Procedure | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | ASV program integration; vulnerability SLAs |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | PCI finding register; deficiency workflow |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | TPSP PCI oversight |
| Adversarial Validation Procedure | [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Penetration testing PCI overlay |
| NERC-CIP Operational Package | [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | Physical security PSP model reused for CDE physical controls |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Master document inventory |
