# Expanded Control Baseline

## Supplemental NIST-Aligned Control Reference for CERG Adopters

| | |
|---|---|
| **Document ID** | CERG-GOV-CB-002 |
| **Version** | 1.0 |
| **Status** | Draft (RFC) |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Control Baseline) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly |
| **Frameworks** | NIST 800-53r5 · NIST 800-171r3 · NIST CSF 2.0 · CIS Controls v8 · ISO/IEC 27001 A.5–A.8 · CSA CCM v4 |
| **Regulations** | NERC-CIP v7 · CMMC L2 · SOX ITGC · PCI DSS v4 · HIPAA Security Rule |
| **Environments** | All in-scope assets — owned, hybrid, cloud, SaaS, OT (partial), CUI |

---

## Table of Contents

1. [Purpose and Relationship to CB-001](#1-purpose-and-relationship-to-cb-001)
2. [Control Format](#2-control-format)
3. [Access Control](#3-access-control)
4. [Awareness and Training](#4-awareness-and-training)
5. [Audit and Accountability](#5-audit-and-accountability)
6. [Assessment, Authorization, and Monitoring](#6-assessment-authorization-and-monitoring)
7. [Configuration Management](#7-configuration-management)
8. [Contingency Planning (CP)](#8-contingency-planning-cp)
9. [Identification and Authentication (IA)](#9-identification-and-authentication-ia)
10. [Incident Response (IR)](#10-incident-response-ir)
11. [Maintenance (MA)](#11-maintenance-ma)
12. [Media Protection (MP)](#12-media-protection-mp)
13. [Physical and Environmental (PE)](#13-physical-and-environmental-pe)
14. [Planning (PL)](#14-planning-pl)
15. [Personnel Security (PS)](#15-personnel-security-ps)
16. [Risk Assessment (RA)](#16-risk-assessment-ra)
17. [System and Services Acquisition (SA)](#17-system-and-services-acquisition-sa)
18. [System and Communications Protection (SC)](#18-system-and-communications-protection-sc)
19. [System and Information Integrity (SI)](#19-system-and-information-integrity-si)
20. [Supply Chain Risk Management (SR)](#20-supply-chain-risk-management-sr)
21. [Program Management (PM)](#21-program-management-pm)
22. [Document Control](#22-document-control)

---

## 1. Purpose and Relationship to CB-001

The [Unified Control Baseline](CERG-GOV-CB-001_Unified_Control_Baseline.md) (CB-001) defines the CERG control architecture — the family spine, implementation statuses, inheritance model, overlay matrix, and a compact schematic control set. CB-001 is the document an auditor opens first, the artifact that binds the regulatory crosswalks, and the architecture that holds the program together.

This document — the Expanded Control Baseline (CB-002-EXP) — is a supplemental reference. It extends the schematic entries in CB-001 Section 6 into 97 enumerated controls across all 19 NIST 800-53r5 families. Each entry adds an action statement an IT practitioner can act on, named evidence, minimum frequency, system applicability, and a cross-reference to the subordinate CERG standard or procedure.

**CB-001 remains authoritative.** This document adds detail; it does not change the architecture, create new mandatory requirements, or raise the adoption floor. Adopters who only need the control spine should stay with CB-001. Adopters who want more control-level specificity can use this document as a companion reference.

Control IDs correspond to NIST 800-53r5 identifiers where the NIST family covers the intent. CERG-native controls use domain-specific prefixes where additional coverage is needed.

| Dimension | CB-001 (Core) | This Document (Expanded) |
|-----------|---------------|--------------------------|
| Control count | Schematic (~18 entries) | 97 enumerated controls |
| Purpose | Architecture + regulatory crosswalks | Implementation reference |
| Relationship | Authoritative framework | Supplemental companion |
| Evidentiary standard | Named evidence | Named evidence + frequency |
| Standard/Procedure binding | Referenced in body | Per-control subordinate standard reference |

---

## 2. Control Format

Each CB-002 control entry uses a standard table format:

| Field | Description |
|---|---|
| **Control ID** | Local expanded-control identifier, e.g. `CB2-AC-001`. The `CB2-` prefix distinguishes CB-002 local IDs from NIST 800-53r5 identifiers and CB-001 anchors. |
| **Primary CB-001 / NIST Anchor** | The main CB-001 or NIST control this entry expands or supports, e.g. `AC-2 Account Management`. |
| **Related Anchors** | Other CB-001 or NIST controls relevant to this entry. |
| **Relationship** | `Expands CB-001` (adds detail to an existing CB-001 control), `Supplements CB-001` (covers an area not explicit in CB-001), or `Overlay / Where Applicable` (applies only when specific conditions exist). |
| **Action Statement** | What the control requires, in language an implementer can act on. |
| **System Applicability** | Hardware, Software, Network, Cloud, Data, Process — one or more values. |
| **Owning Pillar** | Engineering, Risk, or Governance — one accountable pillar per control. |
| **Named Evidence** | The specific artifact that proves the control is operating. |
| **Minimum Frequency** | How often evidence must be collected, or the trigger condition. |
| **Subordinate Standard** | Cross-reference to the CERG standard or procedure that provides parameter detail. Uses current approved artifact IDs. |
| **Implementation Guidance** | Generic, vendor-neutral guidance on what must be true to satisfy the control (where applicable). This guidance is implementation-focused, not effectiveness-focused. |

## 3. Access Control

### AC-001: Account Lifecycle Management

| **Control ID** | AC-001 |
| **Action Statement** | Every user and service account has a documented request, named owner, defined access level, and Join-Move-Leave (JML) record. Accounts are disabled within 24 hours of termination. Dormant accounts (no login in 90 days) are disabled. |
| **System Applicability** | Hardware, Software, Network, Cloud, Data, Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | JML ticket log or HRIS integration report showing account lifecycle events |
| **Minimum Frequency** | Continuous (automated) / Quarterly (manual review) |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### AC-002: MFA Enforcement

| **Control ID** | AC-002 |
| **Action Statement** | Multi-factor authentication is enforced for all user accounts accessing company systems. No exceptions for executives, IT staff, or administrators. Service accounts with non-interactive login must have documented compensating controls (network restriction, monitoring, credential rotation). |
| **System Applicability** | Software, Cloud, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | IdP MFA enrollment report showing 100% enrollment for active human users |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### AC-003: Access Enforcement

| **Control ID** | AC-003 |
| **Action Statement** | All access to systems uses approved authentication and authorization controls. Local accounts, shared accounts, hard-coded credentials, and static passwords are prohibited where an IdP can enforce authentication. |
| **System Applicability** | Hardware, Software, Network, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | IdP policy export showing authentication policies; PAM solution deployment report (if applicable) |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### AC-004: Least Privilege

| **Control ID** | AC-004 |
| **Action Statement** | Users and services operate with the minimum access necessary. Administrative privileges are granted through just-in-time or privileged access management, not standing group membership. Default and over-privileged accounts are identified and restricted. |
| **System Applicability** | Hardware, Software, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Quarterly privilege audit report; PAM session log for administrative access |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### AC-005: Remote Access

| **Control ID** | AC-005 |
| **Action Statement** | Remote access to internal systems requires MFA, encrypted transport, and device posture validation. Split-tunnel VPN configurations are prohibited unless documented with compensating controls. |
| **System Applicability** | Network, Cloud, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | VPN/firewall configuration export; remote access policy |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### AC-006: Quarterly Access Review

| **Control ID** | AC-006 |
| **Action Statement** | Access to all systems is reviewed quarterly by the system or data owner. Access that is no longer required is revoked within 5 business days. The review is documented and signed. |
| **System Applicability** | Software, Cloud, Data, Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Signed access review report with reviewer name, date, systems reviewed, and actions taken |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### AC-007: Separation of Duties

| **Control ID** | AC-007 |
| **Action Statement** | No single individual can both request and approve access, or both develop and deploy code to production, or both initiate and approve payments. Conflicts are identified and mitigated through policy and tooling. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Governance |
| **Named Evidence** | Separation of duties matrix; access policy defining incompatible roles |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### AC-008: Session Lock

| **Control ID** | AC-008 |
| **Action Statement** | User sessions lock after 15 minutes of inactivity. Re-authentication requires the full credential, not just screen dismissal. Device-level screen lock is enforced via MDM or GPO. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | GPO/MDM policy export showing screen lock settings |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

---

## 4. Awareness and Training

### AT-001: Security Awareness Training

| **Control ID** | AT-001 |
| **Action Statement** | All personnel receive security awareness training within 30 days of hire and annually thereafter. Training covers phishing recognition, password hygiene, data handling, incident reporting, and the CERG program structure. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Training completion report with user list, completion dates, and course content summary |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |

### AT-002: Role-Based Training

| **Control ID** | AT-002 |
| **Action Statement** | Personnel in security-sensitive roles (developers, admins, executives, IR team) receive role-specific training on the threats, tools, and procedures relevant to their function. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Role-specific training assignments and completion records |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |

### AT-003: Insider Threat Awareness

| **Control ID** | AT-003 |
| **Action Statement** | Personnel are trained to recognize and report indicators of insider threat — unusual access patterns, data exfiltration warning signs, behavioral red flags. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Training module completion records |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |

---

## 5. Audit and Accountability

### AU-001: Audit Log Collection

| **Control ID** | AU-001 |
| **Action Statement** | All systems generate audit logs for security-relevant events. Logs are forwarded to a centralized SIEM within 5 minutes of generation. Log sources include: endpoints, servers, network devices, firewalls, IdP, cloud platforms, and SaaS applications. |
| **System Applicability** | Hardware, Software, Network, Cloud, Data |
| **Owning Pillar** | Risk |
| **Named Evidence** | SIEM dashboard showing log source count and ingestion status |
| **Minimum Frequency** | Continuous |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### AU-002: Log Protection

| **Control ID** | AU-002 |
| **Action Statement** | Audit logs are protected from unauthorized modification, deletion, and access. Log integrity is verifiable. Log retention meets the longest applicable regulatory requirement (minimum 90 days online, 1 year offline). |
| **System Applicability** | Data, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | SIEM configuration showing access controls and retention settings |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### AU-003: Log Review

| **Control ID** | AU-003 |
| **Action Statement** | Security logs are reviewed regularly. Automated alerting is configured for high-severity events. Weekly manual review of SIEM dashboards for anomalies that escaped automated detection. |
| **System Applicability** | Data, Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Weekly review log (screenshot or SIEM audit entry); alert configuration export |
| **Minimum Frequency** | Weekly (manual review), Continuous (automated) |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### AU-004: Time Synchronization

| **Control ID** | AU-004 |
| **Action Statement** | All systems use a common time source synchronized to a reliable NTP server. Log timestamps are consistent and usable for correlation and forensic analysis. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | NTP configuration export from domain controller or cloud platform |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### AU-005: Audit Record Retention

| **Control ID** | AU-005 |
| **Action Statement** | Audit records are retained according to a defined schedule. Online retention: minimum 90 days. Offline/archive retention: minimum 1 year. Retention schedule is documented and enforced by tooling. |
| **System Applicability** | Data |
| **Owning Pillar** | Risk |
| **Named Evidence** | Retention policy document; SIEM configuration showing retention settings |
| **Minimum Frequency** | Annual review of retention settings |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### AU-006: Audit Generation

| **Control ID** | AU-006 |
| **Action Statement** | Information systems generate audit records for defined event types: account creation/modification/deletion, privilege use, logon/logoff, object access, policy changes, system events, and security tool alerts. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Audit policy configuration export (GPO, cloud platform, SaaS settings) |
| **Minimum Frequency** | Continuous generation; quarterly configuration review |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### AU-007: Audit Reduction and Report Generation

| **Control ID** | AU-007 |
| **Action Statement** | The SIEM supports ad-hoc querying and scheduled report generation for audit events. The organization can produce a human-readable report of security-relevant events for a given time period within 1 hour of request. |
| **System Applicability** | Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Sample audit report generated from SIEM |
| **Minimum Frequency** | Capability verification quarterly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

---

## 6. Assessment, Authorization, and Monitoring

### CA-001: Continuous Monitoring

| **Control ID** | CA-001 |
| **Action Statement** | The security posture of in-scope systems is monitored continuously through automated tooling. Monitoring covers: endpoint protection status, vulnerability scan results, cloud configuration, backup status, and identity hygiene. Deviations from baseline generate alerts. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Governance |
| **Named Evidence** | Consolidated monitoring dashboard; alert configuration |
| **Minimum Frequency** | Continuous |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CA-002: Security Assessment

| **Control ID** | CA-002 |
| **Action Statement** | A security assessment of in-scope systems is conducted at least annually. The assessment evaluates control effectiveness, identifies gaps, and produces a prioritized remediation plan. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Annual assessment report with findings, severity, and remediation status |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CA-003: Authorization

| **Control ID** | CA-003 |
| **Action Statement** | Systems are formally authorized to operate by the appropriate authority before entering production. Authorization is based on a review of security controls, risk acceptance, and residual risk. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Signed Authorization to Operate (ATO) document per system, or consolidated ATO for the environment |
| **Minimum Frequency** | Per system deployment; annual reaffirmation |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CA-004: Interconnection Monitoring

| **Control ID** | CA-004 |
| **Action Statement** | Connections between the organizational environment and external systems (cloud providers, SaaS platforms, partner networks) are documented and monitored. Changes to interconnections are reviewed and authorized. |
| **System Applicability** | Network, Cloud |
| **Owning Pillar** | Governance |
| **Named Evidence** | Interconnection inventory; firewall ruleset review |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CA-005: Plan of Action and Milestones (POA&M)

| **Control ID** | CA-005 |
| **Action Statement** | All findings from assessments, audits, and continuous monitoring are tracked in a POA&M. Each entry has: finding description, severity, remediation owner, target date, and status. The POA&M is reviewed monthly. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Current POA&M export with all open items |
| **Minimum Frequency** | Monthly review; continuous update |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

---

## 7. Configuration Management

### CM-001: Configuration Baseline

| **Control ID** | CM-001 |
| **Action Statement** | Every system type has a documented, approved configuration baseline. Baselines are based on CIS Benchmarks or equivalent hardening standards. Deviations require documented exception. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Configuration baseline document per system type; exception log |
| **Minimum Frequency** | Annual review; update on major version change |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CM-002: Change Control

| **Control ID** | CM-002 |
| **Action Statement** | Changes to production systems follow a documented change management process. Changes are requested, reviewed, approved, tested where feasible, and documented. Emergency changes are permitted but require post-hoc review within 24 hours. |
| **System Applicability** | Process, Hardware, Software, Network, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Change tickets for the review period; change management policy |
| **Minimum Frequency** | Per-change documentation; quarterly process review |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CM-003: Configuration Drift Detection

| **Control ID** | CM-003 |
| **Action Statement** | Systems are monitored for configuration drift from their approved baseline. Drift findings are detected within the scan interval and remediated or excepted. |
| **System Applicability** | Hardware, Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Configuration scan results showing baseline compliance; drift findings and remediation records |
| **Minimum Frequency** | Weekly (critical), Monthly (all) |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CM-004: Least Functionality

| **Control ID** | CM-004 |
| **Action Statement** | Systems are configured to provide only the functions and services necessary for their purpose. Unnecessary software, services, ports, and protocols are removed or disabled. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Server build checklist; port scan results showing only required services |
| **Minimum Frequency** | Per-build; quarterly verification |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CM-005: Software Whitelisting

| **Control ID** | CM-005 |
| **Action Statement** | Only authorized software executes on endpoints and servers. Unapproved software is blocked by default. Whitelisting is based on publisher certificate, file hash, or path — not user discretion. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Application control policy export; blocked execution events |
| **Minimum Frequency** | Continuous enforcement; quarterly policy review |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CM-006: Software Inventory

| **Control ID** | CM-006 |
| **Action Statement** | A current inventory of all software installed on in-scope systems is maintained. Unauthorized or unmanaged software is identified and removed or approved. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Software inventory report; unauthorized software findings log |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CM-007: Hardware Inventory

| **Control ID** | CM-007 |
| **Action Statement** | A current inventory of all in-scope hardware assets is maintained. Inventory includes: asset ID, type, location, owner, operating system, IP address, and last seen date. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Hardware inventory report covering all in-scope assets |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CM-008: Automated Patching

| **Control ID** | CM-008 |
| **Action Statement** | Operating system and application patches are deployed within defined SLAs. Critical security patches: 7 days. High-severity: 14 days. Medium: 30 days. Patch deployment is automated via RMM or native update management. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Patch compliance report showing deployment status by severity |
| **Minimum Frequency** | Monthly (reporting), Continuous (deployment) |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

---

## 8. Contingency Planning (CP)

### CB2-CP-001: Contingency Plan

| **Control ID** | CB2-CP-001 |
| **Action Statement** | A written contingency plan exists for the in-scope environment. The plan identifies critical systems, recovery objectives (RTO/RPO), roles and responsibilities, and recovery procedures. |
| **System Applicability** | Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Contingency plan document, signed and current |
| **Minimum Frequency** | Annual review; update on major system change |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |

### CB2-CP-002: Backup Configuration

| **Control ID** | CB2-CP-002 |
| **Action Statement** | All critical systems and data are backed up on a defined schedule. Backups are stored in at least two locations with at least one immutable or offline copy. Backup configuration is documented. |
| **System Applicability** | Hardware, Software, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Backup job configuration export; storage location documentation |
| **Minimum Frequency** | Quarterly review of configuration |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |

### CB2-CP-003: Backup Testing

| **Control ID** | CB2-CP-003 |
| **Action Statement** | Backups are tested regularly to confirm they can be restored. Test results are documented. Failed tests generate an incident and immediate remediation. |
| **System Applicability** | Hardware, Software, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Backup test results log showing date, system tested, outcome |
| **Minimum Frequency** | Monthly (automated), Quarterly (manual full restore test) |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |

### CB2-CP-004: Alternate Storage Site

| **Control ID** | CB2-CP-004 |
| **Action Statement** | Backup data is stored at a geographically separate location from the primary site. The alternate site is far enough to survive a regional disaster (minimum 50 miles for physical sites; different cloud region for cloud). |
| **System Applicability** | Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Storage location documentation showing geographic separation |
| **Minimum Frequency** | Annual verification |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |

### CB2-CP-005: System Recovery Procedures

| **Control ID** | CB2-CP-005 |
| **Action Statement** | Documented procedures exist for recovering each critical system from backup. Procedures are tested and updated annually. Recovery time and recovery point objectives are defined and measured. |
| **System Applicability** | Process, Hardware, Software, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Recovery procedure document; test results with RTO/RPO measurements |
| **Minimum Frequency** | Annual test; quarterly review of procedures |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |

---

## 9. Identification and Authentication (IA)

### CB2-IA-001: Unique Identification

| **Control ID** | CB2-IA-001 |
| **Action Statement** | Every user and system component has a unique identifier. Shared accounts are prohibited for interactive login. Service accounts are uniquely named and documented. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | User account list showing unique identifiers; service account inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### CB2-IA-002: Strong Authentication

| **Control ID** | CB2-IA-002 |
| **Action Statement** | Authentication uses phishing-resistant methods where possible (FIDO2, certificate-based). Password-based authentication requires minimum 12 characters and is combined with MFA. Default passwords are changed on first use. |
| **System Applicability** | Software, Cloud, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | MFA enrollment report; password policy configuration |
| **Minimum Frequency** | Monthly verification |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### CB2-IA-003: Identifier Management

| **Control ID** | CB2-IA-003 |
| **Action Statement** | User identifiers are managed throughout their lifecycle. Identifiers are never reused for 12 months after deactivation. Group accounts are prohibited. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Account lifecycle policy; disabled accounts report |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### CB2-IA-004: Authenticator Management

| **Control ID** | CB2-IA-004 |
| **Action Statement** | Authenticators (passwords, tokens, certificates, keys) are managed through their lifecycle: issuance, storage, rotation, revocation, and disposal. Default authenticators are changed on first use. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Password policy; certificate inventory; token management process |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

### CB2-IA-005: Device Authentication

| **Control ID** | CB2-IA-005 |
| **Action Statement** | Devices connecting to the network or accessing resources are uniquely identified and authenticated. Certificate-based or domain authentication is preferred over pre-shared keys. |
| **System Applicability** | Hardware, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Network access control configuration; device certificate inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |

---

## 10. Incident Response (IR)

### CB2-IR-001: Incident Response Plan

| **Control ID** | CB2-IR-001 |
| **Action Statement** | A written incident response plan exists. It defines incident types, severity classification, roles, communication procedures, and escalation paths. The plan is tested annually. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | IR plan document; test/exercise results |
| **Minimum Frequency** | Annual review and test |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |

### CB2-IR-002: Incident Detection and Reporting

| **Control ID** | CB2-IR-002 |
| **Action Statement** | Incidents are detected through automated monitoring and reported through a defined channel. All personnel know how to report a security incident. Reports are acknowledged within 1 hour and triaged within 4 hours. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Alert configuration; incident report log |
| **Minimum Frequency** | Continuous |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |

### CB2-IR-003: Incident Containment

| **Control ID** | CB2-IR-003 |
| **Action Statement** | The IR team can contain an incident within defined timeframes. Containment procedures exist for common incident types (ransomware, account compromise, data exfiltration, denial of service). |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Containment procedure documents; post-incident reports with containment timelines |
| **Minimum Frequency** | Annual review; per-incident execution |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |

### CB2-IR-004: Post-Incident Review

| **Control ID** | CB2-IR-004 |
| **Action Statement** | Within 14 days of incident closure, a post-incident review is conducted. The review identifies root cause, timeline, response effectiveness, lessons learned, and control improvements. Findings are tracked to remediation. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Post-incident review document per incident |
| **Minimum Frequency** | Per incident |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |

### CB2-IR-005: Incident Evidence Preservation

| **Control ID** | CB2-IR-005 |
| **Action Statement** | During incident response, evidence is preserved for forensic analysis and potential legal action. Chain of custody is maintained. Evidence retention follows legal and regulatory requirements. |
| **System Applicability** | Process, Data |
| **Owning Pillar** | Risk |
| **Named Evidence** | Evidence handling procedure; chain of custody log for incidents |
| **Minimum Frequency** | Per incident |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |

---

## 11. Maintenance (MA)

### CB2-MA-001: Controlled Maintenance

| **Control ID** | CB2-MA-001 |
| **Action Statement** | System maintenance is planned, scheduled, and performed by authorized personnel. Maintenance activities are logged. Remote maintenance sessions are authenticated, encrypted, and monitored. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Maintenance schedule; maintenance logs |
| **Minimum Frequency** | Per maintenance event |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CB2-MA-002: Maintenance Tools

| **Control ID** | CB2-MA-002 |
| **Action Statement** | Maintenance tools (diagnostic utilities, remote access tools, patching tools) are approved, inventoried, and kept current. Unapproved tools are blocked. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Approved tool list; tool inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

### CB2-MA-003: Firmware and Hardware Updates

| **Control ID** | CB2-MA-003 |
| **Action Statement** | Network device firmware, server firmware (BIOS/UEFI), and hardware component firmware are updated when security vulnerabilities are announced. Critical firmware updates: 30 days. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Firmware inventory with version and update status |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |

---

## 12. Media Protection (MP)

### CB2-MP-001: Media Sanitization

| **Control ID** | CB2-MP-001 |
| **Action Statement** | Digital media (hard drives, SSDs, USB drives, tapes) is sanitized before disposal or reuse. Sanitization method is appropriate to the data classification. NIST SP 800-88 methods are the standard. |
| **System Applicability** | Hardware, Data |
| **Owning Pillar** | Governance |
| **Named Evidence** | Media disposal log with sanitization method per device |
| **Minimum Frequency** | Per disposal event |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |

### CB2-MP-002: Media Transport

| **Control ID** | CB2-MP-002 |
| **Action Statement** | Media containing sensitive data is protected during transport. Encryption is applied. Access is restricted to authorized couriers. Chain of custody is maintained. |
| **System Applicability** | Data, Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Transport log; encryption verification |
| **Minimum Frequency** | Per transport event |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |

### CB2-MP-003: Media Access

| **Control ID** | CB2-MP-003 |
| **Action Statement** | Access to media containing sensitive data is restricted to authorized personnel. Media is stored in physically secure locations. Access is logged. |
| **System Applicability** | Data, Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Access control list for media storage; access log |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |

---

## 13. Physical and Environmental (PE)

### CB2-PE-001: Physical Access Control

| **Control ID** | CB2-PE-001 |
| **Action Statement** | Physical access to facilities housing in-scope systems is controlled and monitored. Access is granted based on role and need. Visitor access is logged and escorted. |
| **System Applicability** | Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Physical access policy; access log (or badge system report) |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PE-002: Environmental Controls

| **Control ID** | CB2-PE-002 |
| **Action Statement** | Facilities housing in-scope systems have environmental controls: temperature, humidity, fire suppression, and power protection (UPS + generator). Controls are monitored and tested. |
| **System Applicability** | Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Environmental monitoring logs; UPS/generator test records |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PE-003: Monitoring Physical Access

| **Control ID** | CB2-PE-003 |
| **Action Statement** | Physical access to facilities is monitored. Access events are logged and reviewed. Unauthorized access attempts are investigated. |
| **System Applicability** | Physical, Data |
| **Owning Pillar** | Governance |
| **Named Evidence** | Access log review records; incident reports for unauthorized access |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

---

## 14. Planning (PL)

### CB2-PL-001: System Security Plan

| **Control ID** | CB2-PL-001 |
| **Action Statement** | A System Security Plan (SSP) exists for the in-scope environment. The SSP describes system boundaries, security controls, implementation status, and interconnection with other systems. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | System Security Plan document |
| **Minimum Frequency** | Annual review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PL-002: Architecture Documentation

| **Control ID** | CB2-PL-002 |
| **Action Statement** | The in-scope system architecture is documented. Documentation includes: network topology, data flows, trust boundaries, external connections, and security tool placement. |
| **System Applicability** | Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Architecture diagram; data flow diagram |
| **Minimum Frequency** | Quarterly review; update on change |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PL-003: Rules of Behavior

| **Control ID** | CB2-PL-003 |
| **Action Statement** | Users of in-scope systems acknowledge rules of behavior before being granted access. Rules cover acceptable use, data handling, security responsibilities, and consequences of violation. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Signed rules of behavior acknowledgments |
| **Minimum Frequency** | On hire; annual reaffirmation |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

---

## 15. Personnel Security (PS)

### CB2-PS-001: Personnel Screening

| **Control ID** | CB2-PS-001 |
| **Action Statement** | Personnel with access to in-scope systems undergo background screening before access is granted. Screening level is appropriate to the sensitivity of the data and systems accessed. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Screening policy; screening completion records (high-level confirmation, not detailed results) |
| **Minimum Frequency** | Pre-hire; re-screening per policy (typically 3-5 years) |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PS-002: Personnel Termination

| **Control ID** | CB2-PS-002 |
| **Action Statement** | Upon termination of employment, access to all systems is revoked within 24 hours. Physical access is revoked. Company equipment is recovered. Exit interview covers security obligations. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Termination checklist; access revocation confirmation |
| **Minimum Frequency** | Per termination event |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PS-003: Personnel Transfer

| **Control ID** | CB2-PS-003 |
| **Action Statement** | When personnel change roles, access is reviewed and adjusted to match the new role within 5 business days. Old access is removed; new access is granted only as needed. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Role change access review records |
| **Minimum Frequency** | Per transfer event |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

---

## 16. Risk Assessment (RA)

### CB2-RA-001: Risk Assessment

| **Control ID** | CB2-RA-001 |
| **Action Statement** | A risk assessment of the in-scope environment is conducted at least annually. The assessment identifies threats, vulnerabilities, likelihood, impact, and resulting risk level. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Risk assessment report |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |

### CB2-RA-002: Vulnerability Scanning

| **Control ID** | CB2-RA-002 |
| **Action Statement** | In-scope systems are scanned for vulnerabilities at defined intervals. Results are triaged, prioritized, and remediated per defined SLAs. Exceptions are tracked in the risk register. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vulnerability scan report; remediation log |
| **Minimum Frequency** | Weekly (external), Monthly (internal) |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-RA-003: Risk Register

| **Control ID** | CB2-RA-003 |
| **Action Statement** | A risk register tracks all identified risks: threat, vulnerability, likelihood, impact, inherent risk, treatment (accept/mitigate/transfer/avoid), residual risk, owner, and review date. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Current risk register export |
| **Minimum Frequency** | Monthly review; continuous update |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |

### CB2-RA-004: Risk Acceptance

| **Control ID** | CB2-RA-004 |
| **Action Statement** | When a risk cannot be mitigated or transferred, it is formally accepted by the appropriate authority. Risk acceptances have an expiration date (maximum 12 months), documented compensating controls, and an approving signature. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Signed risk acceptance documents |
| **Minimum Frequency** | Per acceptance; review on expiration |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |

### CB2-RA-005: Threat Intelligence Integration

| **Control ID** | CB2-RA-005 |
| **Action Statement** | The risk assessment process incorporates current threat intelligence. Emerging threats relevant to the client's industry and technology stack are reviewed and risk-assessed at least quarterly. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Threat intelligence review notes; risk register updates based on threat intel |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |

---

## 17. System and Services Acquisition (SA)

### CB2-SA-001: Security Requirements in Procurement

| **Control ID** | CB2-SA-001 |
| **Action Statement** | Security requirements are included in RFPs, contracts, and vendor selection criteria for all system and service acquisitions. Vendors are evaluated against CERG control requirements before purchase. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Security requirements in RFP/contract; vendor evaluation checklist |
| **Minimum Frequency** | Per acquisition |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SA-002: Software Development Security

| **Control ID** | CB2-SA-002 |
| **Action Statement** | Custom-developed software follows secure development practices. Code is reviewed, tested for security flaws, and scanned for vulnerabilities before deployment. |
| **System Applicability** | Software, Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Secure coding policy; code review records; SAST/SCA scan results |
| **Minimum Frequency** | Per release |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SA-003: Supply Chain Risk Management

| **Control ID** | CB2-SA-003 |
| **Action Statement** | Third-party software and services are assessed for supply chain risk before acquisition. SBOMs are collected for critical software. Vendor security posture is reviewed annually. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vendor risk assessment; SBOM inventory |
| **Minimum Frequency** | Pre-acquisition; annual vendor review |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SA-004: Development Environment Security

| **Control ID** | CB2-SA-004 |
| **Action Statement** | Development and testing environments are separate from production. Production data is not used in development without sanitization. Development access does not grant production access. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Environment separation documentation; data sanitization procedure |
| **Minimum Frequency** | Annual review |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SA-005: Outsourced Development

| **Control ID** | CB2-SA-005 |
| **Action Statement** | When software development is outsourced, the contract requires adherence to the client's security standards. Deliverables are scanned for vulnerabilities before acceptance. Source code and build artifacts are escrowed or delivered. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Contract with security requirements; acceptance test results |
| **Minimum Frequency** | Per outsourced development engagement |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

---

## 18. System and Communications Protection (SC)

### CB2-SC-001: Network Segmentation

| **Control ID** | CB2-SC-001 |
| **Primary CB-001 / NIST Anchor** | SC-7 Boundary Protection |
| **Related Anchors** | AC-4, CA-3 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Network segmented to isolate critical systems, restrict lateral movement, separate trust zones. VLANs for servers, workstations, guest, DMZ. OT physically/logically isolated from IT. |
| **System Applicability** | Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Network diagram, firewall ruleset |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SC-002: Boundary Protection

| **Control ID** | CB2-SC-002 |
| **Primary CB-001 / NIST Anchor** | SC-7 Boundary Protection |
| **Related Anchors** | SC-5, AC-4 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Firewalls restrict traffic to authorized ports/protocols. Default-deny inbound/outbound. Rules reviewed quarterly. |
| **System Applicability** | Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Firewall config export, review log |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SC-003: Encryption at Rest

| **Control ID** | CB2-SC-003 |
| **Primary CB-001 / NIST Anchor** | SC-28 Protection of Information at Rest |
| **Related Anchors** | SC-12, SC-13 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Sensitive data at rest encrypted. Keys managed separately. |
| **System Applicability** | Hardware, Software, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Encryption config, key management procedure |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |

### CB2-SC-004: Encryption in Transit

| **Control ID** | CB2-SC-004 |
| **Primary CB-001 / NIST Anchor** | SC-8 Transmission Confidentiality and Integrity |
| **Related Anchors** | SC-12, SC-13, AC-17 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | TLS 1.2+ required. Legacy protocols disabled. |
| **System Applicability** | Network, Cloud, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | TLS scan report |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |

### CB2-SC-005: VoIP Protection

| **Control ID** | CB2-SC-005 |
| **Primary CB-001 / NIST Anchor** | SC-7 Boundary Protection |
| **Related Anchors** | CM-7 |
| **Relationship** | Supplements CB-001 |
| **Action Statement** | VoIP isolated on separate VLAN. Default credentials changed. |
| **System Applicability** | Network, Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | VoIP config, credential log |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SC-006: Wireless Security

| **Control ID** | CB2-SC-006 |
| **Primary CB-001 / NIST Anchor** | AC-18 Wireless Access |
| **Related Anchors** | SC-8, SC-7 |
| **Relationship** | Supplements CB-001 |
| **Action Statement** | WPA2-Enterprise with 802.1X. No PSK for corporate. Guest isolated. |
| **System Applicability** | Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Wireless config |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SC-007: Mobile Device Security

| **Control ID** | CB2-SC-007 |
| **Primary CB-001 / NIST Anchor** | AC-19 Access Control for Mobile Devices |
| **Related Anchors** | CM-8, AC-18 |
| **Relationship** | Supplements CB-001 |
| **Action Statement** | MDM enforced: screen lock, encryption, min OS, remote wipe. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | MDM policy, compliance report |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SC-008: DNS Security

| **Control ID** | CB2-SC-008 |
| **Primary CB-001 / NIST Anchor** | SC-7 Boundary Protection / SC-20 Secure Name/Address Resolution |
| **Related Anchors** | SI-3, SC-5 |
| **Relationship** | Supplements CB-001 |
| **Action Statement** | DNS filtering blocks malicious domains. Internal DNS hardened. |
| **System Applicability** | Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | DNS config, filtering policy |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

## 19. System and Information Integrity (SI)

### CB2-SI-001: Malware Protection

| **Control ID** | CB2-SI-001 |
| **Primary CB-001 / NIST Anchor** | SI-3 Malicious Code Protection |
| **Related Anchors** | SI-4, SI-7, CM-8 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Anti-malware deployed. Real-time protection. Auto-update. Coverage monitored. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | EDR dashboard |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CB2-SI-002: Vulnerability Monitoring

| **Control ID** | CB2-SI-002 |
| **Primary CB-001 / NIST Anchor** | SI-2 Flaw Remediation / RA-5 Vulnerability Scanning |
| **Related Anchors** | CA-7, CM-8 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | New vulns assessed within 24h. CISA KEV, vendor advisories monitored. |
| **System Applicability** | Hardware, Software, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Advisory review log |
| **Minimum Frequency** | Weekly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CB2-SI-003: File Integrity Monitoring

| **Control ID** | CB2-SI-003 |
| **Primary CB-001 / NIST Anchor** | SI-7 Software, Firmware, and Information Integrity |
| **Related Anchors** | SI-3, CM-3, CM-6 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Critical files monitored for unauthorized changes. Alerts generated. |
| **System Applicability** | Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | FIM config, alert log |
| **Minimum Frequency** | Continuous |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CB2-SI-004: Detection Engineering

| **Control ID** | CB2-SI-004 |
| **Primary CB-001 / NIST Anchor** | SI-4 System Monitoring |
| **Related Anchors** | AU-6, CA-7, IR-4 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Sigma rules deployed, ATT&CK mapped. Tested with Atomic Red Team. Gaps documented. |
| **System Applicability** | Software, Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Rule inventory, test results |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CB2-SI-005: Email Security

| **Control ID** | CB2-SI-005 |
| **Primary CB-001 / NIST Anchor** | SI-3 Malicious Code Protection / SC-7 Boundary Protection |
| **Related Anchors** | SC-8 |
| **Relationship** | Supplements CB-001 |
| **Action Statement** | SPF/DKIM/DMARC enforced. Safe Links/Attachments. Phish investigated. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Email config, phish metrics |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CB2-SI-006: Web Filtering

| **Control ID** | CB2-SI-006 |
| **Primary CB-001 / NIST Anchor** | SI-3 Malicious Code Protection / SC-7 Boundary Protection |
| **Related Anchors** | SC-8 |
| **Relationship** | Supplements CB-001 |
| **Action Statement** | Web traffic filtered for malicious/phishing/inappropriate sites. |
| **System Applicability** | Network, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Filtering config |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CB2-SI-007: Data Loss Prevention

| **Control ID** | CB2-SI-007 |
| **Primary CB-001 / NIST Anchor** | SI-4 System Monitoring / AC-4 Information Flow Enforcement |
| **Related Anchors** | SC-7, CM-7 |
| **Relationship** | Overlay / Where Applicable |
| **Action Statement** | DLP for email, cloud, endpoints. Sensitive data exfiltration blocked. |
| **System Applicability** | Data, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | DLP config, incident log |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### CB2-SI-008: Application Security Testing

| **Control ID** | CB2-SI-008 |
| **Primary CB-001 / NIST Anchor** | SI-2 Flaw Remediation / SA-11 Developer Testing |
| **Related Anchors** | SA-8 |
| **Relationship** | Supplements CB-001 |
| **Action Statement** | Web apps tested for vulns. Critical remediated before production. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | App test report |
| **Minimum Frequency** | Per release |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

## 20. Supply Chain Risk Management (SR)

### CB2-SR-001: Software Bill of Materials

| **Control ID** | CB2-SR-001 |
| **Primary CB-001 / NIST Anchor** | SR-1 Supply Chain Policy / CM-8 System Component Inventory |
| **Related Anchors** | SA-9, SA-4 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | SBOM collected for critical software. Components, versions, vulns tracked. |
| **System Applicability** | Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | SBOM inventory |
| **Minimum Frequency** | Per acquisition |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SR-002: Vendor Risk Assessment

| **Control ID** | CB2-SR-002 |
| **Primary CB-001 / NIST Anchor** | SR-3 Supply Chain Controls and Processes / SA-9 External System Services |
| **Related Anchors** | SA-4, RA-3 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Vendors assessed: posture, history, compliance, data handling. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vendor assessment, tier list |
| **Minimum Frequency** | Annual (critical) |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |

### CB2-SR-003: Trusted Software Sources

| **Control ID** | CB2-SR-003 |
| **Primary CB-001 / NIST Anchor** | SR-1 Supply Chain Policy |
| **Related Anchors** | SA-4, CM-8 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Software from trusted sources only. Integrity verified before install. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Approved source list |
| **Minimum Frequency** | Per acquisition |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

### CB2-SR-004: Hardware Supply Chain

| **Control ID** | CB2-SR-004 |
| **Primary CB-001 / NIST Anchor** | SR-1 Supply Chain Policy |
| **Related Anchors** | SA-4, CM-8 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Hardware from authorized resellers. Counterfeit/tampered rejected. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Risk |
| **Named Evidence** | Authorized reseller list |
| **Minimum Frequency** | Per acquisition |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |

## 21. Program Management (PM)

### CB2-PM-001: Information Security Program Plan

| **Control ID** | CB2-PM-001 |
| **Primary CB-001 / NIST Anchor** | PM-1 Information Security Program Plan |
| **Related Anchors** | PM-2, PM-5 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Documented plan: scope, org structure, roles, resources, metrics. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Program plan document |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PM-002: Senior Security Officer

| **Control ID** | CB2-PM-002 |
| **Primary CB-001 / NIST Anchor** | PM-2 Senior Agency Information Security Officer |
| **Related Anchors** | PM-1 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Named individual accountable for program. Budget authority. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Appointment/org chart |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PM-003: Security Metrics Program

| **Control ID** | CB2-PM-003 |
| **Primary CB-001 / NIST Anchor** | PM-4 Plan of Action and Milestones Process |
| **Related Anchors** | PM-1, PM-6 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Performance measured. Reported to leadership. Improves program. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Metrics dashboard |
| **Minimum Frequency** | Monthly/Quarterly |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

### CB2-PM-004: Continuous Improvement

| **Control ID** | CB2-PM-004 |
| **Primary CB-001 / NIST Anchor** | PM-6 Measures of Performance |
| **Related Anchors** | PM-1, PM-4 |
| **Relationship** | Expands CB-001 |
| **Action Statement** | Program reviewed and improved. Lessons learned feed updates. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Review minutes, action items |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |

## 22. Document Control

### Control Count Summary

| Family | Controls |
|--------|----------|
| AC — Access Control | 8 |
| AT — Awareness and Training | 3 |
| AU — Audit and Accountability | 7 |
| CA — Assessment, Authorization, Monitoring | 5 |
| CM — Configuration Management | 8 |
| CP — Contingency Planning | 5 |
| IA — Identification and Authentication | 5 |
| IR — Incident Response | 5 |
| MA — Maintenance | 3 |
| MP — Media Protection | 3 |
| PE — Physical and Environmental | 3 |
| PL — Planning | 3 |
| PS — Personnel Security | 3 |
| RA — Risk Assessment | 5 |
| SA — System and Services Acquisition | 5 |
| SC — System and Communications Protection | 8 |
| SI — System and Information Integrity | 8 |
| SR — Supply Chain Risk Management | 4 |
| PM — Program Management | 4 |
| **Total** | **97** |

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | Governance Pillar Leader (Control Baseline) | RFC: 97 controls across 19 families, stripped for upstream review |

### Review Triggers

- Quarterly review against threat intelligence and regulatory changes
- Re-review if upstream CERG CB-001 is updated
- Re-review on major tool stack changes (vendor acquisition, breach, EOL)

### Related Documents

- [Upstream CERG Unified Control Baseline](CERG-GOV-CB-001_Unified_Control_Baseline.md)

