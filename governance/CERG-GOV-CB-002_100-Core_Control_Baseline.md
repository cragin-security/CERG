# 100-Core Control Baseline (Extended)

## Practitioner-Ready Control Set with MSP Copy-Paste Instructions

| | |
|---|---|
| **Document ID** | CERG-GOV-CB-002 |
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **Review Cycle** | Quarterly |
| **Frameworks** | NIST 800-53r5 · NIST 800-171r3 · NIST CSF 2.0 · CIS Controls v8 · ISO/IEC 27001 A.5-A.8 |
| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 · HIPAA Security Rule |
| **Environments** | All in-scope assets — IT, cloud, SaaS, OT (partial), CUI (where scoped) |

---

## Table of Contents

1. [Relationship to Upstream CERG](#1-relationship-to-upstream-cerg)
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

## 1. Relationship to Upstream CERG

The upstream CERG baseline ([CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md)) defines the framework architecture and a schematic control matrix. This document — part of the cragin-security fork — extends the upstream baseline into a **practitioner-ready control set**.

Differences from upstream:

| Dimension | Upstream (CB-001) | This Document (CB-002) |
|-----------|-------------------|------------------------|
| Control count | ~18 schematic entries | 97 enumerated controls |
| Audience | Program architects, auditors | MSPs, MSSPs, IT generalists |
| Instructions | None | Copy-paste deployment per control |
| Tool bindings | Framework-level | Tied to [Opinionated Tool Matrix](../practice-assets/tools/opinionated-tool-matrix-v1.md) |
| Evidence | Named artifact | Named artifact + collection method + frequency |
| Inheritance | Described in Section 5 of CB-001 | Per-control inheritance notes where applicable |

Upstream CB-001 remains the authoritative architecture. This document is the implementation companion. Control IDs (e.g., AC-001) correspond to NIST 800-53r5 identifiers where applicable; CERG-native controls use domain-specific prefixes.

---

## 2. Control Format

Every control entry follows this structure:

| **Control ID** | NIST-aligned or CERG-native identifier |
| **Action Statement** | What the control requires, in plain language an IT generalist can understand |
| **System Applicability** | Hardware, Software, Network, Cloud, Data, Process — one or more |
| **Owning Pillar** | Engineering, Risk, or Governance |
| **Named Evidence** | The specific artifact that proves the control is operating |
| **Minimum Frequency** | How often evidence must be collected |
| **Subordinate Standard** | Link to the relevant CERG standard with parameter detail |
| **MSP Implementation Note** | Copy-paste instructions for MSPs/MSSPs (where applicable) |
| **Tool Binding** | Which tool(s) from the [Opinionated Tool Matrix](../practice-assets/tools/opinionated-tool-matrix-v1.md) satisfy this control |

---

## 3. Access Control

### AC-001: Account Lifecycle Management

| **Control ID** | AC-001 |
| **Action Statement** | Every user and service account has a documented request, named owner, defined access level, and Join-Move-Leave (JML) record. Accounts are disabled within 24 hours of termination. Dormant accounts (no login in 90 days) are disabled. |
| **System Applicability** | Hardware, Software, Network, Cloud, Data, Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | JML ticket log or HRIS integration report showing account lifecycle events |
| **Minimum Frequency** | Continuous (automated) / Quarterly (manual review) |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Connect HRIS to IdP for automated provisioning/deprovisioning. For clients without HRIS integration, run this script quarterly: `Get-ADUser -Filter {LastLogonDate -lt (Get-Date).AddDays(-90)} | Disable-ADAccount`. Document all terminations in the ticket system within one business day. |
| **Tool Binding** | Okta / Entra ID (IdP), HaloPSA (ticketing), NinjaOne (RMM verification) |

### AC-002: MFA Enforcement

| **Control ID** | AC-002 |
| **Action Statement** | Multi-factor authentication is enforced for all user accounts accessing company systems. No exceptions for executives, IT staff, or administrators. Service accounts with non-interactive login must have documented compensating controls (network restriction, monitoring, credential rotation). |
| **System Applicability** | Software, Cloud, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | IdP MFA enrollment report showing 100% enrollment for active human users |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | See [MSP Runbook](../practice-assets/msp-runbook-v1.md) AC-002 section for full deployment steps. Core commands: Okta > Security > Multifactor > Require for all. Entra ID > Conditional Access > Require MFA for all users. Test: attempt login without MFA — must be rejected. |
| **Tool Binding** | Okta / Entra ID |

### AC-003: Access Enforcement

| **Control ID** | AC-003 |
| **Action Statement** | All access to systems uses approved authentication and authorization controls. Local accounts, shared accounts, hard-coded credentials, and static passwords are prohibited where an IdP can enforce authentication. |
| **System Applicability** | Hardware, Software, Network, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | IdP policy export showing authentication policies; PAM solution deployment report (if applicable) |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Enforce SAML/OIDC SSO for all SaaS apps. Block legacy authentication protocols in Entra ID. For on-prem systems: join to domain, enforce Kerberos, disable NTLM where possible. Audit local accounts monthly: `Get-LocalUser | Where-Object Enabled` on all servers. |
| **Tool Binding** | Okta / Entra ID |

### AC-004: Least Privilege

| **Control ID** | AC-004 |
| **Action Statement** | Users and services operate with the minimum access necessary. Administrative privileges are granted through just-in-time or privileged access management, not standing group membership. Default and over-privileged accounts are identified and restricted. |
| **System Applicability** | Hardware, Software, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Quarterly privilege audit report; PAM session log for administrative access |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Remove all users from Domain Admins. Create tiered admin groups (Workstation Admin, Server Admin, Domain Admin). Use PAM for elevation. For SMB without PAM budget: dedicated admin accounts (u-admin) separate from daily driver accounts, with 12-hour credential rotation. |
| **Tool Binding** | Okta / Entra ID (PIM), CyberArk / Delinea (PAM for enterprise) |

### AC-005: Remote Access

| **Control ID** | AC-005 |
| **Action Statement** | Remote access to internal systems requires MFA, encrypted transport, and device posture validation. Split-tunnel VPN configurations are prohibited unless documented with compensating controls. |
| **System Applicability** | Network, Cloud, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | VPN/firewall configuration export; remote access policy |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | FortiGate: enable SSL-VPN with SAML to Okta/Entra ID for MFA. Require client certificate in addition to MFA for admin VPN. Disable split tunneling unless explicitly scoped and documented. Verify: `show vpn ssl settings` shows `require-certificate enable`. |
| **Tool Binding** | Fortinet (firewall/VPN), Okta / Entra ID (auth) |

### AC-006: Quarterly Access Review

| **Control ID** | AC-006 |
| **Action Statement** | Access to all systems is reviewed quarterly by the system or data owner. Access that is no longer required is revoked within 5 business days. The review is documented and signed. |
| **System Applicability** | Software, Cloud, Data, Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Signed access review report with reviewer name, date, systems reviewed, and actions taken |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Export all users with group memberships from Entra ID/Okta + all SaaS admin roles. Send to department heads with 5-day deadline. Revoke flagged access immediately. Document the review — even if no changes, the documentation IS the evidence. |
| **Tool Binding** | Okta / Entra ID |

### AC-007: Separation of Duties

| **Control ID** | AC-007 |
| **Action Statement** | No single individual can both request and approve access, or both develop and deploy code to production, or both initiate and approve payments. Conflicts are identified and mitigated through policy and tooling. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Governance |
| **Named Evidence** | Separation of duties matrix; access policy defining incompatible roles |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | For SMB clients where one person wears every hat: implement two-person approval in the ticketing system for production changes. The incompatible duties are: (1) request access / approve access, (2) write code / deploy to production, (3) configure firewall / approve firewall change. |
| **Tool Binding** | HaloPSA (ticketing approval workflows), ServiceNow GRC |

### AC-008: Session Lock

| **Control ID** | AC-008 |
| **Action Statement** | User sessions lock after 15 minutes of inactivity. Re-authentication requires the full credential, not just screen dismissal. Device-level screen lock is enforced via MDM or GPO. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | GPO/MDM policy export showing screen lock settings |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Windows GPO: Computer Config > Policies > Windows Settings > Security Settings > Local Policies > Security Options > "Interactive logon: Machine inactivity limit" = 900 seconds. Verify: `gpresult /r` on a domain workstation. |
| **Tool Binding** | Active Directory GPO, Intune, Jamf |

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
| **MSP Implementation Note** | Use a phishing simulation platform (KnowBe4, Proofpoint) with monthly simulated phishing. Track click rates. Anyone who clicks gets immediate remediation training. Annual full training via the same platform. |
| **Tool Binding** | KnowBe4, Proofpoint SAT, or M365 Attack Simulation Training |

### AT-002: Role-Based Training

| **Control ID** | AT-002 |
| **Action Statement** | Personnel in security-sensitive roles (developers, admins, executives, IR team) receive role-specific training on the threats, tools, and procedures relevant to their function. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Role-specific training assignments and completion records |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |
| **MSP Implementation Note** | Developers: OWASP Top 10, secure coding. Admins: hardening, detection response. Executives: ransomware decision-making, breach notification obligations. Track in LMS or ticketing system. |
| **Tool Binding** | KnowBe4, PluralSight, SANS |

### AT-003: Insider Threat Awareness

| **Control ID** | AT-003 |
| **Action Statement** | Personnel are trained to recognize and report indicators of insider threat — unusual access patterns, data exfiltration warning signs, behavioral red flags. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Training module completion records |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |
| **MSP Implementation Note** | Include insider threat module in annual training. Content: "If you see a coworker downloading large amounts of data before resigning, or accessing systems they don't normally use, report it. You will not get in trouble for a good-faith report." |
| **Tool Binding** | KnowBe4, Proofpoint SAT |

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
| **MSP Implementation Note** | Windows: enable Event Log Forwarding or deploy Wazuh agent. Network: syslog to SIEM. Cloud: CloudTrail (AWS), Activity Log (Azure), Cloud Audit Logs (GCP) → SIEM. SaaS: API connectors to SIEM. Minimum log sources per client: endpoints, firewalls, domain controllers, IdP, cloud admin activity, email gateway. |
| **Tool Binding** | Elastic Security / Wazuh |

### AU-002: Log Protection

| **Control ID** | AU-002 |
| **Action Statement** | Audit logs are protected from unauthorized modification, deletion, and access. Log integrity is verifiable. Log retention meets the longest applicable regulatory requirement (minimum 90 days online, 1 year offline). |
| **System Applicability** | Data, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | SIEM configuration showing access controls and retention settings |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **MSP Implementation Note** | Wazuh: default retention is filesystem-based — ensure sufficient disk. Elastic: configure index lifecycle management (hot 30d → warm 60d → cold 365d → delete). Restrict SIEM access to named MSP security personnel only. |
| **Tool Binding** | Elastic Security / Wazuh |

### AU-003: Log Review

| **Control ID** | AU-003 |
| **Action Statement** | Security logs are reviewed regularly. Automated alerting is configured for high-severity events. Weekly manual review of SIEM dashboards for anomalies that escaped automated detection. |
| **System Applicability** | Data, Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Weekly review log (screenshot or SIEM audit entry); alert configuration export |
| **Minimum Frequency** | Weekly (manual review), Continuous (automated) |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **MSP Implementation Note** | Schedule 30-minute weekly review session per client. Check: top alerts, new log sources, detection coverage gaps, suppressed alerts that should be re-enabled. Document the session in the ticketing system. |
| **Tool Binding** | Elastic Security / Wazuh |

### AU-004: Time Synchronization

| **Control ID** | AU-004 |
| **Action Statement** | All systems use a common time source synchronized to a reliable NTP server. Log timestamps are consistent and usable for correlation and forensic analysis. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | NTP configuration export from domain controller or cloud platform |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **MSP Implementation Note** | Domain controllers sync to pool.ntp.org or time.windows.com. All domain-joined systems inherit. Linux: `timedatectl set-ntp true`. Network devices: `ntp server <dc-ip>`. Verify: `w32tm /query /status` on Windows, `timedatectl` on Linux. |
| **Tool Binding** | Built-in OS NTP |

### AU-005: Audit Record Retention

| **Control ID** | AU-005 |
| **Action Statement** | Audit records are retained according to a defined schedule. Online retention: minimum 90 days. Offline/archive retention: minimum 1 year. Retention schedule is documented and enforced by tooling. |
| **System Applicability** | Data |
| **Owning Pillar** | Risk |
| **Named Evidence** | Retention policy document; SIEM configuration showing retention settings |
| **Minimum Frequency** | Annual review of retention settings |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **MSP Implementation Note** | Higher retention for regulated clients: PCI requires 1 year online. HIPAA: 6 years (can be offline). CMMC: minimum 90 days, recommend 1 year. Scale storage accordingly. |
| **Tool Binding** | Elastic Security / Wazuh (with appropriate storage) |

### AU-006: Audit Generation

| **Control ID** | AU-006 |
| **Action Statement** | Information systems generate audit records for defined event types: account creation/modification/deletion, privilege use, logon/logoff, object access, policy changes, system events, and security tool alerts. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Audit policy configuration export (GPO, cloud platform, SaaS settings) |
| **Minimum Frequency** | Continuous generation; quarterly configuration review |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **MSP Implementation Note** | Windows: Advanced Audit Policy via GPO. Enable: Account Logon, Account Management, Logon/Logoff, Object Access (at minimum file shares), Policy Change, Privilege Use, System. Cloud: enable all management-plane logging (CloudTrail, Activity Log, Audit Logs). |
| **Tool Binding** | Active Directory GPO, Cloud native logging |

### AU-007: Audit Reduction and Report Generation

| **Control ID** | AU-007 |
| **Action Statement** | The SIEM supports ad-hoc querying and scheduled report generation for audit events. The MSP can produce a human-readable report of security-relevant events for a given time period within 1 hour of request. |
| **System Applicability** | Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Sample audit report generated from SIEM |
| **Minimum Frequency** | Capability verification quarterly |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **MSP Implementation Note** | Elastic: create saved dashboards per client. Wazuh: use the reporting module. Both should support "give me all authentication failures for Client X in March 2026" in < 1 hour. |
| **Tool Binding** | Elastic Security / Wazuh |

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
| **MSP Implementation Note** | Required dashboards per client: SentinelOne agent status, Tenable vulnerability summary, Wiz cloud findings, Veeam backup health, Entra ID/Okta MFA status. Review all five weekly. Any gap gets a ticket. |
| **Tool Binding** | SentinelOne, Tenable, Wiz, Veeam, Okta/Entra ID → ServiceNow GRC |

### CA-002: Security Assessment

| **Control ID** | CA-002 |
| **Action Statement** | A security assessment of in-scope systems is conducted at least annually. The assessment evaluates control effectiveness, identifies gaps, and produces a prioritized remediation plan. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Annual assessment report with findings, severity, and remediation status |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | This is the CERG Assessment engagement (see [Engagement Playbook](../practice-assets/engagement-playbook-v1.md)). For ongoing clients, repeat the assessment annually with reduced scope — verify existing controls, focus on changes since last assessment. |
| **Tool Binding** | Tenable/Nessus (technical assessment), ServiceNow GRC (control assessment) |

### CA-003: Authorization

| **Control ID** | CA-003 |
| **Action Statement** | Systems are formally authorized to operate by the appropriate authority before entering production. Authorization is based on a review of security controls, risk acceptance, and residual risk. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Signed Authorization to Operate (ATO) document per system, or consolidated ATO for the environment |
| **Minimum Frequency** | Per system deployment; annual reaffirmation |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | For SMB clients: a single ATO document covering the core IT environment, signed by the business owner. For CMMC clients: formal authorization package per CMMC assessment scope. |
| **Tool Binding** | ServiceNow GRC (authorization workflow) |

### CA-004: Interconnection Monitoring

| **Control ID** | CA-004 |
| **Action Statement** | Connections between the client's environment and external systems (MSP tools, cloud providers, SaaS platforms, partner networks) are documented and monitored. Changes to interconnections are reviewed and authorized. |
| **System Applicability** | Network, Cloud |
| **Owning Pillar** | Governance |
| **Named Evidence** | Interconnection inventory; firewall ruleset review |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | Document every site-to-site VPN, every API integration, every SaaS OAuth connection. Review quarterly: is this connection still needed? Is the partner still authorized? Are credentials rotated? |
| **Tool Binding** | Fortinet (firewall rules), ServiceNow GRC (interconnection register) |

### CA-005: Plan of Action and Milestones (POA&M)

| **Control ID** | CA-005 |
| **Action Statement** | All findings from assessments, audits, and continuous monitoring are tracked in a POA&M. Each entry has: finding description, severity, remediation owner, target date, and status. The POA&M is reviewed monthly. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Current POA&M export with all open items |
| **Minimum Frequency** | Monthly review; continuous update |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | ServiceNow GRC: use the POA&M module. Vanta: use risk register with due dates. Track every finding from vuln scans, assessments, audits, and monitoring gaps. Nothing older than 90 days without a funded remediation plan. |
| **Tool Binding** | ServiceNow GRC / Vanta |

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
| **MSP Implementation Note** | Start with CIS Benchmarks. Download the PDF for Windows Server, Ubuntu, and your firewall model. Apply the Level 1 profile (safe for production). Document which settings diverge and why. |
| **Tool Binding** | CIS Benchmark PDFs + Wazuh SCA module for enforcement |

### CM-002: Change Control

| **Control ID** | CM-002 |
| **Action Statement** | Changes to production systems follow a documented change management process. Changes are requested, reviewed, approved, tested where feasible, and documented. Emergency changes are permitted but require post-hoc review within 24 hours. |
| **System Applicability** | Process, Hardware, Software, Network, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Change tickets for the review period; change management policy |
| **Minimum Frequency** | Per-change documentation; quarterly process review |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Use the ticketing system for all production changes. Minimum fields: what's changing, why, rollback plan, approver, test results. For SMB with a single IT person: self-approve is acceptable for routine changes; major changes (firewall, domain controller, backup config) require a second set of eyes. |
| **Tool Binding** | HaloPSA / ConnectWise Manage |

### CM-003: Configuration Drift Detection

| **Control ID** | CM-003 |
| **Action Statement** | Systems are monitored for configuration drift from their approved baseline. Drift findings are detected within the scan interval and remediated or excepted. |
| **System Applicability** | Hardware, Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Configuration scan results showing baseline compliance; drift findings and remediation records |
| **Minimum Frequency** | Weekly (critical), Monthly (all) |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Wazuh SCA module: load CIS policies, schedule weekly scans. Wiz: continuous CSPM for cloud. Tenable: monthly compliance scans against CIS benchmarks. Any finding > Medium opens a ticket. |
| **Tool Binding** | Wazuh (SCA), Tenable/Nessus (compliance scans), Wiz (CSPM) |

### CM-004: Least Functionality

| **Control ID** | CM-004 |
| **Action Statement** | Systems are configured to provide only the functions and services necessary for their purpose. Unnecessary software, services, ports, and protocols are removed or disabled. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Server build checklist; port scan results showing only required services |
| **Minimum Frequency** | Per-build; quarterly verification |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Server build checklist: remove all roles/features not required. Disable SMBv1, LLMNR, NetBIOS, WPAD. Uninstall unnecessary software (browser toolbars, outdated Java, trial software). Verify with `nmap -sV <target>` — every open port must have a documented purpose. |
| **Tool Binding** | CIS Benchmark checklists, Nmap |

### CM-005: Software Whitelisting

| **Control ID** | CM-005 |
| **Action Statement** | Only authorized software executes on endpoints and servers. Unapproved software is blocked by default. Whitelisting is based on publisher certificate, file hash, or path — not user discretion. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Application control policy export; blocked execution events |
| **Minimum Frequency** | Continuous enforcement; quarterly policy review |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Windows: AppLocker in audit-only mode for 30 days to build the baseline, then enforce. SentinelOne: Application Control module. For simple SMB deployments: Software Restriction Policies via GPO (path-based) is better than nothing. |
| **Tool Binding** | Windows AppLocker, SentinelOne Application Control |

### CM-006: Software Inventory

| **Control ID** | CM-006 |
| **Action Statement** | A current inventory of all software installed on in-scope systems is maintained. Unauthorized or unmanaged software is identified and removed or approved. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Software inventory report; unauthorized software findings log |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | NinjaOne agent collects installed software inventory automatically. Review monthly: flag anything not in the approved list. SentinelOne also provides software inventory with threat context. |
| **Tool Binding** | NinjaOne (RMM), SentinelOne |

### CM-007: Hardware Inventory

| **Control ID** | CM-007 |
| **Action Statement** | A current inventory of all in-scope hardware assets is maintained. Inventory includes: asset ID, type, location, owner, operating system, IP address, and last seen date. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Hardware inventory report covering all in-scope assets |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | NinjaOne provides automated hardware inventory. Reconcile monthly against the client's asset list. Flag any device not in RMM but present on the network (rogue device detection). |
| **Tool Binding** | NinjaOne (RMM) |

### CM-008: Automated Patching

| **Control ID** | CM-008 |
| **Action Statement** | Operating system and application patches are deployed within defined SLAs. Critical security patches: 7 days. High-severity: 14 days. Medium: 30 days. Patch deployment is automated via RMM or native update management. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Patch compliance report showing deployment status by severity |
| **Minimum Frequency** | Monthly (reporting), Continuous (deployment) |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | NinjaOne: configure automated approval for Critical and Security patches. Test on pilot group (5% of endpoints), then deploy to all. Servers: maintenance window. Document any patch that breaks something and the exception. |
| **Tool Binding** | NinjaOne, Windows Update for Business, Tenable (vuln → patch mapping) |

---

## 8. Contingency Planning (CP)

### CP-001: Contingency Plan

| **Control ID** | CP-001 |
| **Action Statement** | A written contingency plan exists for the in-scope environment. The plan identifies critical systems, recovery objectives (RTO/RPO), roles and responsibilities, and recovery procedures. |
| **System Applicability** | Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Contingency plan document, signed and current |
| **Minimum Frequency** | Annual review; update on major system change |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Minimum plan contents: critical system list (priority order), RTO per system (how fast to recover), RPO per system (how much data loss is acceptable), who does what during recovery, communication plan, test schedule. Keep it under 10 pages — it needs to be usable during an incident. |
| **Tool Binding** | ServiceNow GRC (plan repository) |

### CP-002: Backup Configuration

| **Control ID** | CP-002 |
| **Action Statement** | All critical systems and data are backed up on a defined schedule. Backups are stored in at least two locations with at least one immutable or offline copy. Backup configuration is documented. |
| **System Applicability** | Hardware, Software, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Backup job configuration export; storage location documentation |
| **Minimum Frequency** | Quarterly review of configuration |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Veeam: configure daily incremental, weekly full, monthly archival. Enable immutability on all backup repositories (Linux hardened repo or object storage with Object Lock). Backup copy to offsite (Veeam Cloud Connect to MSP infrastructure). Document the 3-2-1 rule: 3 copies, 2 media types, 1 offsite. |
| **Tool Binding** | Veeam |

### CP-003: Backup Testing

| **Control ID** | CP-003 |
| **Action Statement** | Backups are tested regularly to confirm they can be restored. Test results are documented. Failed tests generate an incident and immediate remediation. |
| **System Applicability** | Hardware, Software, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Backup test results log showing date, system tested, outcome |
| **Minimum Frequency** | Monthly (automated), Quarterly (manual full restore test) |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Veeam SureBackup: schedule weekly automated test restores of sample workloads. Quarterly manual test: restore a production file server, verify users can access data. Any failure = high-severity incident. |
| **Tool Binding** | Veeam |

### CP-004: Alternate Storage Site

| **Control ID** | CP-004 |
| **Action Statement** | Backup data is stored at a geographically separate location from the primary site. The alternate site is far enough to survive a regional disaster (minimum 50 miles for physical sites; different cloud region for cloud). |
| **System Applicability** | Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Storage location documentation showing geographic separation |
| **Minimum Frequency** | Annual verification |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | For on-prem clients: Veeam backup copy to MSP's cloud repository (different region). For cloud-native: cross-region replication. Verify: "if the primary site burns down, do we still have backups?" |
| **Tool Binding** | Veeam, AWS S3 Cross-Region Replication, Azure GRS |

### CP-005: System Recovery Procedures

| **Control ID** | CP-005 |
| **Action Statement** | Documented procedures exist for recovering each critical system from backup. Procedures are tested and updated annually. Recovery time and recovery point objectives are defined and measured. |
| **System Applicability** | Process, Hardware, Software, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Recovery procedure document; test results with RTO/RPO measurements |
| **Minimum Frequency** | Annual test; quarterly review of procedures |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Write recovery procedures in order: domain controller first (authentication), then file server, then application servers, then email. Each procedure: step-by-step commands. Test once a year and time it. If DR test takes 8 hours but the plan says 4 hours, update the plan or fix the process. |
| **Tool Binding** | Veeam (orchestration), HaloPSA (procedure documentation) |

---

## 9. Identification and Authentication (IA)

### IA-001: Unique Identification

| **Control ID** | IA-001 |
| **Action Statement** | Every user and system component has a unique identifier. Shared accounts are prohibited for interactive login. Service accounts are uniquely named and documented. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | User account list showing unique identifiers; service account inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | One person = one account. No "admin" account shared among IT staff. Service accounts follow naming convention: `svc-Purpose-Env`. Document all service accounts in Hudu/IT Glue. |
| **Tool Binding** | Okta / Entra ID, Hudu (documentation) |

### IA-002: Strong Authentication

| **Control ID** | IA-002 |
| **Action Statement** | Authentication uses phishing-resistant methods where possible (FIDO2, certificate-based). Password-based authentication requires minimum 12 characters and is combined with MFA. Default passwords are changed on first use. |
| **System Applicability** | Software, Cloud, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | MFA enrollment report; password policy configuration |
| **Minimum Frequency** | Monthly verification |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Entra ID: Password Protection enabled. Minimum 12 characters (set higher if possible). Ban common passwords. FIDO2 security keys for privileged accounts where budget allows. At minimum: MFA on everything. |
| **Tool Binding** | Okta / Entra ID |

### IA-003: Identifier Management

| **Control ID** | IA-003 |
| **Action Statement** | User identifiers are managed throughout their lifecycle. Identifiers are never reused for 12 months after deactivation. Group accounts are prohibited. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Account lifecycle policy; disabled accounts report |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Disable, don't delete — retains audit trail. No username reuse for 12 months. No group/shared accounts ("reception", "warehouse"). Every human gets their own account. |
| **Tool Binding** | Okta / Entra ID |

### IA-004: Authenticator Management

| **Control ID** | IA-004 |
| **Action Statement** | Authenticators (passwords, tokens, certificates, keys) are managed through their lifecycle: issuance, storage, rotation, revocation, and disposal. Default authenticators are changed on first use. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Password policy; certificate inventory; token management process |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Passwords: 12+ characters, no expiration if MFA is enforced (per NIST 800-63B). Service account passwords: rotate every 90 days or use managed identities. API keys: rotate quarterly, store in vault/Hudu. |
| **Tool Binding** | Okta / Entra ID, Hudu (credential documentation) |

### IA-005: Device Authentication

| **Control ID** | IA-005 |
| **Action Statement** | Devices connecting to the network or accessing resources are uniquely identified and authenticated. Certificate-based or domain authentication is preferred over pre-shared keys. |
| **System Applicability** | Hardware, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Network access control configuration; device certificate inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Windows: domain-joined = authenticated. Network: 802.1X with device certificates for wired/wireless (enterprise). Guest network: separate SSID, internet-only. At minimum: MAC filtering + separate VLAN for unknown devices. |
| **Tool Binding** | Active Directory, Fortinet (802.1X/NAC) |

---

## 10. Incident Response (IR)

### IR-001: Incident Response Plan

| **Control ID** | IR-001 |
| **Action Statement** | A written incident response plan exists. It defines incident types, severity classification, roles, communication procedures, and escalation paths. The plan is tested annually. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | IR plan document; test/exercise results |
| **Minimum Frequency** | Annual review and test |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Minimum plan contents: incident definition (what counts), severity levels (1-4), who to call first (and second and third), containment steps, evidence preservation, notification obligations, post-incident review. Keep it short — 5-10 pages. |
| **Tool Binding** | ServiceNow GRC (plan repository), HaloPSA (incident workflow) |

### IR-002: Incident Detection and Reporting

| **Control ID** | IR-002 |
| **Action Statement** | Incidents are detected through automated monitoring and reported through a defined channel. All personnel know how to report a security incident. Reports are acknowledged within 1 hour and triaged within 4 hours. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Alert configuration; incident report log |
| **Minimum Frequency** | Continuous |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | SIEM alerts → MSP ticketing system (auto-create ticket). End user reports → dedicated email (security@client.com) or phone. Quarterly test: send a test alert, verify it creates a ticket within 5 minutes. |
| **Tool Binding** | Elastic/Wazuh → HaloPSA, SentinelOne → HaloPSA |

### IR-003: Incident Containment

| **Control ID** | IR-003 |
| **Action Statement** | The IR team can contain an incident within defined timeframes. Containment procedures exist for common incident types (ransomware, account compromise, data exfiltration, denial of service). |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Containment procedure documents; post-incident reports with containment timelines |
| **Minimum Frequency** | Annual review; per-incident execution |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Ransomware containment procedure: isolate affected systems (disable switch port or remove from network), revoke compromised credentials, preserve evidence (forensic image before reimaging), engage IR firm if beyond MSP capability. Pre-stage: SentinelOne network isolation capability for rapid containment. |
| **Tool Binding** | SentinelOne (network isolation), Fortinet (ACL changes) |

### IR-004: Post-Incident Review

| **Control ID** | IR-004 |
| **Action Statement** | Within 14 days of incident closure, a post-incident review is conducted. The review identifies root cause, timeline, response effectiveness, lessons learned, and control improvements. Findings are tracked to remediation. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Post-incident review document per incident |
| **Minimum Frequency** | Per incident |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Standard post-incident template: (1) What happened (timeline), (2) How we found out (detection source), (3) What we did (response actions), (4) What worked / what didn't, (5) What changes are needed (controls, training, tooling). Track action items in POA&M. |
| **Tool Binding** | ServiceNow GRC / HaloPSA |

### IR-005: Incident Evidence Preservation

| **Control ID** | IR-005 |
| **Action Statement** | During incident response, evidence is preserved for forensic analysis and potential legal action. Chain of custody is maintained. Evidence retention follows legal and regulatory requirements. |
| **System Applicability** | Process, Data |
| **Owning Pillar** | Risk |
| **Named Evidence** | Evidence handling procedure; chain of custody log for incidents |
| **Minimum Frequency** | Per incident |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Before reimaging a compromised system: take forensic image (FTK Imager or dd). Preserve SIEM logs, firewall logs, endpoint telemetry for the incident window. Store evidence on write-once media or immutable storage. Do not delete anything until legal/insurance confirms it's clear. |
| **Tool Binding** | FTK Imager, Veeam (forensic backup), Elastic/Wazuh (log export) |

---

## 11. Maintenance (MA)

### MA-001: Controlled Maintenance

| **Control ID** | MA-001 |
| **Action Statement** | System maintenance is planned, scheduled, and performed by authorized personnel. Maintenance activities are logged. Remote maintenance sessions are authenticated, encrypted, and monitored. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Maintenance schedule; maintenance logs |
| **Minimum Frequency** | Per maintenance event |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | All maintenance: scheduled in ticketing system, approved before execution. Remote sessions: use the RMM (NinjaOne) which logs all activity. No RDP directly from the internet — always through VPN or RMM. |
| **Tool Binding** | NinjaOne, HaloPSA |

### MA-002: Maintenance Tools

| **Control ID** | MA-002 |
| **Action Statement** | Maintenance tools (diagnostic utilities, remote access tools, patching tools) are approved, inventoried, and kept current. Unapproved tools are blocked. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Approved tool list; tool inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Standardize on: NinjaOne (RMM), HaloPSA (ticketing), SentinelOne (EDR), Veeam (backup). These are the approved maintenance tools. Everything else requires a documented exception. No TeamViewer, AnyDesk, LogMeIn — use the RMM. |
| **Tool Binding** | NinjaOne, SentinelOne (application control to block unapproved tools) |

### MA-003: Firmware and Hardware Updates

| **Control ID** | MA-003 |
| **Action Statement** | Network device firmware, server firmware (BIOS/UEFI), and hardware component firmware are updated when security vulnerabilities are announced. Critical firmware updates: 30 days. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Firmware inventory with version and update status |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Fortinet: subscribe to security advisories. Apply critical firmware within 30 days. Servers: vendor firmware update tools (Dell OpenManage, HPE iLO). Document firmware versions in Hudu. |
| **Tool Binding** | NinjaOne (inventory), Hudu (documentation), vendor update tools |

---

## 12. Media Protection (MP)

### MP-001: Media Sanitization

| **Control ID** | MP-001 |
| **Action Statement** | Digital media (hard drives, SSDs, USB drives, tapes) is sanitized before disposal or reuse. Sanitization method is appropriate to the data classification. NIST SP 800-88 methods are the standard. |
| **System Applicability** | Hardware, Data |
| **Owning Pillar** | Governance |
| **Named Evidence** | Media disposal log with sanitization method per device |
| **Minimum Frequency** | Per disposal event |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |
| **MSP Implementation Note** | Standard IT equipment: secure erase (ATA Secure Erase) or cryptographic erase (destroy encryption key). CUI/regulated data: physical destruction (shredder, degausser, certified destruction service). Document what was destroyed, when, by whom, method used. |
| **Tool Binding** | DBAN (secure erase), certified destruction service |

### MP-002: Media Transport

| **Control ID** | MP-002 |
| **Action Statement** | Media containing sensitive data is protected during transport. Encryption is applied. Access is restricted to authorized couriers. Chain of custody is maintained. |
| **System Applicability** | Data, Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Transport log; encryption verification |
| **Minimum Frequency** | Per transport event |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |
| **MSP Implementation Note** | Backup tapes/disks for offsite storage: encrypt before transport (Veeam encryption at rest). Use bonded courier. Document: what was transported, when, from where to where, who transported it, encryption status. |
| **Tool Binding** | Veeam (encryption), Hudu (chain of custody log) |

### MP-003: Media Access

| **Control ID** | MP-003 |
| **Action Statement** | Access to media containing sensitive data is restricted to authorized personnel. Media is stored in physically secure locations. Access is logged. |
| **System Applicability** | Data, Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Access control list for media storage; access log |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |
| **MSP Implementation Note** | Backup media: locked cabinet or data center cage. Access restricted to named personnel. Document who has keys/codes. For cloud-native clients without physical media: this control is satisfied by cloud provider's physical security (documented via SOC 2 report). |
| **Tool Binding** | Physical security (locked storage), Cloud provider SOC 2 (inheritance) |

---

## 13. Physical and Environmental (PE)

### PE-001: Physical Access Control

| **Control ID** | PE-001 |
| **Action Statement** | Physical access to facilities housing in-scope systems is controlled and monitored. Access is granted based on role and need. Visitor access is logged and escorted. |
| **System Applicability** | Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Physical access policy; access log (or badge system report) |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | For on-prem clients: verify badge/key system, locked server rooms, visitor escort policy. For cloud-only clients: inheritance from cloud provider's physical security (document SOC 2 report). For MSP's own facility: same controls apply to client backup media. |
| **Tool Binding** | Client's physical security system; Cloud provider SOC 2 (inheritance) |

### PE-002: Environmental Controls

| **Control ID** | PE-002 |
| **Action Statement** | Facilities housing in-scope systems have environmental controls: temperature, humidity, fire suppression, and power protection (UPS + generator). Controls are monitored and tested. |
| **System Applicability** | Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Environmental monitoring logs; UPS/generator test records |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | For on-prem clients with server rooms: verify UPS capacity, generator test schedule, temperature monitoring. For cloud-only: inheritance. Flag: if the client's "server room" is a closet with no cooling and a $50 UPS, document as a finding. |
| **Tool Binding** | Client's environmental monitoring; Cloud provider SOC 2 |

### PE-003: Monitoring Physical Access

| **Control ID** | PE-003 |
| **Action Statement** | Physical access to facilities is monitored. Access events are logged and reviewed. Unauthorized access attempts are investigated. |
| **System Applicability** | Physical, Data |
| **Owning Pillar** | Governance |
| **Named Evidence** | Access log review records; incident reports for unauthorized access |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Minimum: door access log, reviewed quarterly. For higher-security: cameras at entry points, motion sensors, 24/7 monitoring (or review of footage after-hours). Cloud: inheritance. |
| **Tool Binding** | Client's physical security system; Cloud provider SOC 2 |

---

## 14. Planning (PL)

### PL-001: System Security Plan

| **Control ID** | PL-001 |
| **Action Statement** | A System Security Plan (SSP) exists for the in-scope environment. The SSP describes system boundaries, security controls, implementation status, and interconnection with other systems. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | System Security Plan document |
| **Minimum Frequency** | Annual review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | For SMB clients: a single SSP covering the core IT environment. Contents: system description, boundary diagram, control implementation status (this baseline mapped to the environment), interconnection table, responsible parties. |
| **Tool Binding** | ServiceNow GRC (document management) |

### PL-002: Architecture Documentation

| **Control ID** | PL-002 |
| **Action Statement** | The in-scope system architecture is documented. Documentation includes: network topology, data flows, trust boundaries, external connections, and security tool placement. |
| **System Applicability** | Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Architecture diagram; data flow diagram |
| **Minimum Frequency** | Quarterly review; update on change |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Maintain architecture diagram in Hudu. Minimum: internet → firewall → LAN/VLANs, with servers, workstations, cloud connections, and security tools labeled. Update when anything changes. An outdated diagram is worse than no diagram. |
| **Tool Binding** | Hudu, Draw.io / Lucidchart |

### PL-003: Rules of Behavior

| **Control ID** | PL-003 |
| **Action Statement** | Users of in-scope systems acknowledge rules of behavior before being granted access. Rules cover acceptable use, data handling, security responsibilities, and consequences of violation. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Signed rules of behavior acknowledgments |
| **Minimum Frequency** | On hire; annual reaffirmation |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Include in employee handbook or new-hire onboarding. Annual reaffirmation via training platform. Signed PDF stored in HR system or Hudu. |
| **Tool Binding** | KnowBe4, HRIS, Hudu |

---

## 15. Personnel Security (PS)

### PS-001: Personnel Screening

| **Control ID** | PS-001 |
| **Action Statement** | Personnel with access to in-scope systems undergo background screening before access is granted. Screening level is appropriate to the sensitivity of the data and systems accessed. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Screening policy; screening completion records (high-level confirmation, not detailed results) |
| **Minimum Frequency** | Pre-hire; re-screening per policy (typically 3-5 years) |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Minimum for IT staff: criminal background check, employment verification. For CMMC-regulated: adds citizenship verification. Document that screening occurred — don't store detailed results in client systems. |
| **Tool Binding** | Client's HR/background check provider |

### PS-002: Personnel Termination

| **Control ID** | PS-002 |
| **Action Statement** | Upon termination of employment, access to all systems is revoked within 24 hours. Physical access is revoked. Company equipment is recovered. Exit interview covers security obligations. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Termination checklist; access revocation confirmation |
| **Minimum Frequency** | Per termination event |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Ideally automated via HRIS → IdP deprovisioning. Manual: termination checklist covers all systems. Critical: disable IdP account first (this cascades to SSO apps). Then: VPN, email, remote access, physical access. Confirm within 24 hours. |
| **Tool Binding** | Okta/Entra ID, HRIS |

### PS-003: Personnel Transfer

| **Control ID** | PS-003 |
| **Action Statement** | When personnel change roles, access is reviewed and adjusted to match the new role within 5 business days. Old access is removed; new access is granted only as needed. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Role change access review records |
| **Minimum Frequency** | Per transfer event |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Trigger: HR system or manager notifies of role change → review all group memberships and app assignments → remove old, add new → document. Use IdP group-based access to make this scalable (change group = change access everywhere). |
| **Tool Binding** | Okta/Entra ID |

---

## 16. Risk Assessment (RA)

### RA-001: Risk Assessment

| **Control ID** | RA-001 |
| **Action Statement** | A risk assessment of the in-scope environment is conducted at least annually. The assessment identifies threats, vulnerabilities, likelihood, impact, and resulting risk level. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Risk assessment report |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | Annual CERG Assessment engagement covers this. Deliverables: risk register with scored risks, threat analysis, vulnerability correlation. Start with the top 10 risks — don't try to enumerate 200 low-probability scenarios. Focus on what could actually hurt the business. |
| **Tool Binding** | ServiceNow GRC (risk module) |

### RA-002: Vulnerability Scanning

| **Control ID** | RA-002 |
| **Action Statement** | In-scope systems are scanned for vulnerabilities at defined intervals. Results are triaged, prioritized, and remediated per defined SLAs. Exceptions are tracked in the risk register. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vulnerability scan report; remediation log |
| **Minimum Frequency** | Weekly (external), Monthly (internal) |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | See [MSP Runbook](../practice-assets/msp-runbook-v1.md) RA-005 section. Tenable authenticated scans weekly (external) and monthly (internal). Critical vulns: 7 days. High: 30 days. Medium: 90 days. |
| **Tool Binding** | Tenable/Nessus |

### RA-003: Risk Register

| **Control ID** | RA-003 |
| **Action Statement** | A risk register tracks all identified risks: threat, vulnerability, likelihood, impact, inherent risk, treatment (accept/mitigate/transfer/avoid), residual risk, owner, and review date. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Current risk register export |
| **Minimum Frequency** | Monthly review; continuous update |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | ServiceNow GRC: risk module. Vanta: risk register. Minimum fields per risk entry: ID, description, threat source, affected assets, likelihood (1-5), impact (1-5), inherent risk score, treatment, residual risk, owner, target review date. Review monthly. |
| **Tool Binding** | ServiceNow GRC, Vanta |

### RA-004: Risk Acceptance

| **Control ID** | RA-004 |
| **Action Statement** | When a risk cannot be mitigated or transferred, it is formally accepted by the appropriate authority. Risk acceptances have an expiration date (maximum 12 months), documented compensating controls, and an approving signature. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Signed risk acceptance documents |
| **Minimum Frequency** | Per acceptance; review on expiration |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | The risk acceptance template: (1) What risk are we accepting? (2) Why can't we fix it now? (3) What compensating controls reduce the risk? (4) When does this acceptance expire? (5) Who's signing? The signer should be the business owner, not IT — it's a business decision. |
| **Tool Binding** | ServiceNow GRC (risk acceptance workflow) |

### RA-005: Threat Intelligence Integration

| **Control ID** | RA-005 |
| **Action Statement** | The risk assessment process incorporates current threat intelligence. Emerging threats relevant to the client's industry and technology stack are reviewed and risk-assessed at least quarterly. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Threat intelligence review notes; risk register updates based on threat intel |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | Subscribe to: CISA alerts, MS-ISAC (state/local gov), vendor advisories (Fortinet, Microsoft, SentinelOne). Quarterly review: any new threat that applies to our clients? Add to risk register if relevant. Sector-specific: healthcare clients = HHS alerts, financial = FS-ISAC, energy = E-ISAC. |
| **Tool Binding** | CISA, vendor advisories, ISAC memberships |

---

## 17. System and Services Acquisition (SA)

### SA-001: Security Requirements in Procurement

| **Control ID** | SA-001 |
| **Action Statement** | Security requirements are included in RFPs, contracts, and vendor selection criteria for all system and service acquisitions (software, hardware, and services). Vendors are evaluated against CERG control requirements before purchase. Hardware is sourced only from authorized resellers. Software is sourced from trusted, integrity-verified channels only. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Security requirements in RFP/contract; vendor evaluation checklist |
| **Minimum Frequency** | Per acquisition |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | Before buying any new tool/service: (1) Does it integrate with our stack? (2) Does it have an API for ServiceNow/Vanta? (3) Does it support MFA? (4) Does it have a SOC 2 or ISO 27001 report? (5) Can we manage it multi-tenant for MSP? Score each vendor. Reject if they fail on 2+ criteria. |
| **Tool Binding** | ServiceNow GRC (vendor risk module) |

### SA-002: Software Development Security

| **Control ID** | SA-002 |
| **Action Statement** | Custom-developed software and public-facing web applications follow secure development practices. Code is reviewed, tested for security flaws (SAST/DAST), and scanned for vulnerabilities before production deployment. Critical-severity findings block release. |
| **System Applicability** | Software, Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Secure coding policy; code review records; SAST/SCA scan results |
| **Minimum Frequency** | Per release |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | For clients who write custom code: add Semgrep to CI/CD pipeline. Block merges on high-severity findings. For MSP-developed scripts/automation: peer review before production deployment. |
| **Tool Binding** | Semgrep, Trivy |

### SA-003: Supply Chain Risk Management

| **Control ID** | SA-003 |
| **Action Statement** | Third-party software and services are assessed for supply chain risk before acquisition. SBOMs are collected for critical software. Vendor security posture is reviewed annually. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vendor risk assessment; SBOM inventory |
| **Minimum Frequency** | Pre-acquisition; annual vendor review |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | For critical software (firewalls, backup, EDR, SIEM): collect SBOMs. For all vendors: annual SOC 2 review. Flag any vendor who won't provide a SOC 2 or who has had a breach in the last 12 months without remediation. |
| **Tool Binding** | Trivy (SBOM generation), ServiceNow GRC (vendor risk) |

### SA-004: Development Environment Security

| **Control ID** | SA-004 |
| **Action Statement** | Development and testing environments are separate from production. Production data is not used in development without sanitization. Development access does not grant production access. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Environment separation documentation; data sanitization procedure |
| **Minimum Frequency** | Annual review |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | Separate dev/test/prod in different networks or cloud accounts. No production credentials in dev. No production data in dev without scrubbing (remove PII, replace with dummy data). Developers do not have admin access to production. |
| **Tool Binding** | Cloud IAM (AWS Organizations, Azure Management Groups), Git branching strategy |

### SA-005: Outsourced Development

| **Control ID** | SA-005 |
| **Action Statement** | When software development is outsourced, the contract requires adherence to the client's security standards. Deliverables are scanned for vulnerabilities before acceptance. Source code and build artifacts are escrowed or delivered. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Contract with security requirements; acceptance test results |
| **Minimum Frequency** | Per outsourced development engagement |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | Contract clause: "Developer shall adhere to CERG-STD-IT-001 Section X. Code will be scanned with Semgrep and Trivy. SBOM will be delivered with each release. Source code will be delivered to client upon termination." Scan every delivery before accepting it. |
| **Tool Binding** | Semgrep, Trivy |


---

## 18. System and Communications Protection (SC)

### SC-001: Network Segmentation

| **Control ID** | SC-001 |
| **Action Statement** | The network is segmented into trust zones (servers, workstations, guest, DMZ, OT, CUI enclave). Inter-zone traffic is restricted to explicitly authorized ports and protocols. Boundary protection (firewalls, ACLs) enforces segmentation. Lateral movement between zones requires a firewall rule change. |
| **System Applicability** | Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Network diagram showing trust zones; firewall ruleset export |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-STD-NET-001](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) |
| **MSP Implementation Note** | Minimum zones: Guest (internet only), Workstation (corporate LAN), Server (restricted access), DMZ (internet-facing), Management (admin access). OT clients: physically separate network or firewall-enforced with one-way data diode where possible. Fortinet: create zones, apply policies between each zone pair. Test: can a workstation ping a server in a different zone? If yes, segmentation is broken. |
| **Tool Binding** | Fortinet (zone-based firewall), VLANs, 802.1Q |


### SC-003: Encryption at Rest

| **Control ID** | SC-003 |
| **Action Statement** | Sensitive data at rest is encrypted. Encryption keys are managed separately from the encrypted data. Key rotation follows a defined schedule. |
| **System Applicability** | Hardware, Software, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Encryption configuration export; key management procedure document |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| **MSP Implementation Note** | Windows: BitLocker on all workstations and servers. Cloud: enable default encryption (AWS EBS, Azure SSE, GCP CSEK). Database: TDE if available. Key management: use platform key management (Entra ID, AWS KMS, Azure Key Vault). Do not store encryption keys on the same server as the encrypted data. |
| **Tool Binding** | BitLocker, AWS KMS, Azure Key Vault, Veeam (backup encryption) |

### SC-004: Encryption in Transit

| **Control ID** | SC-004 |
| **Action Statement** | Data in transit is encrypted using TLS 1.2 or higher. SSL 3.0, TLS 1.0, and TLS 1.1 are disabled. Internal network traffic between sensitive systems is encrypted where traversing untrusted segments. |
| **System Applicability** | Network, Cloud, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | TLS configuration scan report; cipher suite configuration |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| **MSP Implementation Note** | FortiGate: disable SSLv3, TLS 1.0, TLS 1.1 in SSL/SSH inspection profile. Web servers: configure TLS 1.2+ in IIS/Apache/Nginx. Test with nmap --script ssl-enum-ciphers -p 443 <target>. Flag any server supporting TLS < 1.2. |
| **Tool Binding** | Fortinet (SSL inspection), Nmap (scan), Qualys SSL Labs (external) |


### SC-006: Wireless Security

| **Control ID** | SC-006 |
| **Action Statement** | Corporate wireless networks use WPA2-Enterprise or WPA3-Enterprise with 802.1X authentication. Pre-shared keys are not used for corporate access. Guest wireless is on a separate SSID with internet-only access and client isolation enabled. |
| **System Applicability** | Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Wireless configuration export; RADIUS authentication logs |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-NET-001](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) |
| **MSP Implementation Note** | FortiGate wireless controller: configure SSID for corporate (WPA2-Enterprise + RADIUS to NPS/Entra ID), guest (open portal with captive portal, client isolation). For clients without RADIUS infrastructure: WPA3-SAE is acceptable as an interim measure. |
| **Tool Binding** | Fortinet (wireless controller), NPS/RADIUS, Entra ID (802.1X auth) |


### SC-008: DNS Security

| **Control ID** | SC-008 |
| **Action Statement** | DNS traffic is filtered to block access to known malicious domains, C2 infrastructure, phishing sites, and malware distribution sites. Internal DNS servers are hardened against cache poisoning and zone transfer attacks. |
| **System Applicability** | Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | DNS filtering configuration; DNS resolver security settings |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-NET-001](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) |
| **MSP Implementation Note** | FortiGate: enable DNS filter with malicious-domain categories blocked. Forward all DNS to FortiGuard or Cisco Umbrella for threat intelligence. Internal domain controllers: disable recursion for external queries, enable DNSSEC. Test: nslookup malicious.test-domain.com — must return blocked response. |
| **Tool Binding** | Fortinet (DNS filter), Cisco Umbrella, Active Directory DNS |

---

## 19. System and Information Integrity (SI)



### SI-003: File Integrity Monitoring

| **Control ID** | SI-003 |
| **Action Statement** | Critical system files, configuration files, and binary directories are monitored for unauthorized changes. FIM alerts are generated within 5 minutes of a change. Baseline snapshots are taken after every approved change. |
| **System Applicability** | Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | FIM configuration export; unauthorized change alert log |
| **Minimum Frequency** | Continuous |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Wazuh: enable FIM module, add directories to monitor: /etc, /usr/bin, /usr/local/bin, C:\Windows\System32\drivers\etc, C:\Program Files install dirs. Exclude temp and cache. SentinelOne: enable integrity monitoring via policy. Alert on any change that is not traceable to an approved patch or change ticket. |
| **Tool Binding** | Wazuh (FIM module), SentinelOne (integrity monitoring) |

### SI-004: Detection Engineering

| **Control ID** | SI-004 |
| **Action Statement** | Detection rules are written in Sigma format and deployed to the SIEM. Rules are mapped to MITRE ATT&CK techniques. Each rule is tested quarterly with Atomic Red Team. Detection coverage gaps are documented and prioritized for remediation. |
| **System Applicability** | Software, Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Sigma rule inventory; Atomic Red Team test results showing detection status per technique |
| **Minimum Frequency** | Monthly (rule review), Quarterly (testing) |
| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **MSP Implementation Note** | Deploy Sigma rules via Wazuh/Elastic. Use the Sigma CLI to convert. Map rules to ATT&CK. Run Atomic Red Team tests quarterly: Invoke-AtomicTest All -GetPrereqs, then Invoke-AtomicTest All. Every test that does not generate an alert is a detection gap — document it in POA&M. |
| **Tool Binding** | Sigma (rule format), Atomic Red Team (testing), Elastic Security / Wazuh (deployment) |

### SI-005: Email Security

| **Control ID** | SI-005 |
| **Action Statement** | Email is protected against phishing, spoofing, and malware delivery. SPF, DKIM, and DMARC are enforced on the sending domain. Inbound email is filtered for malicious links and attachments. Reported phishing is investigated within 4 hours. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Email security configuration export; phishing investigation log; DMARC report |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-MSG-001](../standards/CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md) |
| **MSP Implementation Note** | M365: enable Safe Links, Safe Attachments, Anti-Phish in Defender for Office 365. Configure SPF (TXT record listing all sending IPs), DKIM (signing enabled in Exchange admin), DMARC (policy p=quarantine or p=reject). Test: Resolve-DnsName client.com TXT to verify SPF. |
| **Tool Binding** | M365 Defender, Proofpoint, DMARC analysis tools |

### SI-006: Web Filtering

| **Control ID** | SI-006 |
| **Action Statement** | Outbound web traffic is filtered to block malicious, phishing, and inappropriate categories. HTTPS inspection is enabled where legally permissible. Filtering bypass is restricted to authorized personnel with documented exceptions. |
| **System Applicability** | Network, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Web filter configuration export; bypass request log |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-NET-001](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) |
| **MSP Implementation Note** | FortiGate: enable web filter with categories: block Malicious, Phishing, Newly Registered Domains, Cryptominers. Block or warn on Adult, P2P, Social Media (per client policy). Enable HTTPS inspection (CA certificate deployed via GPO). Test: browse to test-malicious.site — must be blocked. |
| **Tool Binding** | Fortinet (web filter), SentinelOne (web control), DNS filter |

### SI-007: Data Loss Prevention

| **Control ID** | SI-007 |
| **Action Statement** | Sensitive data is protected from exfiltration via email, cloud upload, USB transfer, and clipboard. DLP policies identify and block unauthorized transmission of PII, PHI, financial data, and intellectual property. |
| **System Applicability** | Data, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | DLP policy configuration; DLP incident log |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-DG-001](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) |
| **MSP Implementation Note** | M365: enable DLP in Purview. Define policies for: PII (SSN, credit card, bank account), PHI (HIPAA identifiers), financial data. SentinelOne: enable USB device control to block unauthorized removable media. For SMB clients: start with email DLP and USB blocking. |
| **Tool Binding** | Microsoft Purview (M365 DLP), SentinelOne (USB control) |


---

## 20. Supply Chain Risk Management (SR)

### SR-001: Software Bill of Materials

| **Control ID** | SR-001 |
| **Action Statement** | SBOMs are collected for all critical software acquisitions (commercial and open-source). SBOMs are stored centrally, scanned for known vulnerabilities, and reviewed quarterly for newly disclosed CVEs affecting the software supply chain. |
| **System Applicability** | Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | SBOM inventory; vulnerability scan results against SBOM components |
| **Minimum Frequency** | Per acquisition; quarterly review |
| **Subordinate Standard** | [CERG-STD-SDL-001](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) |
| **MSP Implementation Note** | Use Trivy to generate SBOMs: trivy image --format cyclonedx --output sbom.json <image>. For commercial software: request SPDX or CycloneDX SBOM from vendor. Store SBOMs in client documentation (Hudu). Quarterly: trivy sbom sbom.json to re-scan for new CVEs. Flag any Critical/High CVE with no fix available. |
| **Tool Binding** | Trivy (SBOM generation and scanning) |

### SR-002: Vendor Risk Assessment

| **Control ID** | SR-002 |
| **Action Statement** | Third-party vendors with access to client systems or data are assessed for security posture annually (or pre-engagement for new vendors). Assessment covers: compliance certifications, breach history, data handling practices, subcontractor relationships, and right-to-audit provisions. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vendor assessment form; tiered vendor list (Critical/High/Medium/Low); annual review records |
| **Minimum Frequency** | Pre-engagement (all vendors); Annual (Critical/High) |
| **Subordinate Standard** | [CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **MSP Implementation Note** | Tier vendors by data access: Critical (production data, admin access), High (PII/PHI read, network access), Medium (non-sensitive data), Low (no data access). Annual review for Critical/High: verify SOC 2 Type II is current, check for breaches in last 12 months, review subcontractor changes. Use ServiceNow GRC vendor module or a simple spreadsheet for SMB. |
| **Tool Binding** | ServiceNow GRC (vendor risk module), Vanta (automated vendor assessment) |



---

## 21. Program Management (PM)

### PM-001: Information Security Program Plan

| **Control ID** | PM-001 |
| **Action Statement** | A written information security program plan defines the scope of the program, organizational structure, roles and responsibilities, resource requirements, and success metrics. The plan is reviewed and updated annually. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Signed information security program plan document |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | SMB clients: a single 5-10 page plan covering: environment description, control implementation approach, staffing model (MSP + client), compliance obligations, metrics, and review cadence. Store in client documentation (Hudu/ServiceNow). |
| **Tool Binding** | ServiceNow GRC (document management), Hudu |


### PM-003: Security Metrics Program

| **Control ID** | PM-003 |
| **Action Statement** | Security program performance is measured through defined metrics and reported to leadership monthly. Metrics cover: vulnerability remediation SLA adherence, MFA coverage, backup success rate, incident response time, and risk register aging. Metrics drive program improvement decisions. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Metrics dashboard or report; trend data showing improvement over time |
| **Minimum Frequency** | Monthly (operational), Quarterly (trend) |
| **Subordinate Standard** | [CERG-GOV-MTR-001](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| **MSP Implementation Note** | Minimum metrics per client: (1) vuln SLA adherence %, (2) MFA coverage %, (3) backup success rate %, (4) critical patch deployment time, (5) open risk acceptances aged > 90 days. ServiceNow GRC: use Performance Analytics. Vanta: built-in compliance metrics. For SMB: a monthly one-page PDF summary to the client's leadership. |
| **Tool Binding** | ServiceNow GRC (Performance Analytics), Vanta (compliance dashboard), Elastic/Wazuh (operational metrics) |

### PM-004: Continuous Improvement

| **Control ID** | PM-004 |
| **Action Statement** | The security program is reviewed quarterly for improvement opportunities. Lessons learned from incidents, audits, assessments, and operational metrics feed program updates. Improvement actions are tracked in the POA&M. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Quarterly program review minutes; POA&M entries for improvement actions |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Quarterly program review agenda: (1) what changed (scope, regulations, threats), (2) metric trends (green/amber/red), (3) open findings from last audit/assessment, (4) improvement priorities for next quarter. Document in POA&M. This is the mechanism that prevents CERG from becoming shelfware. |
| **Tool Binding** | ServiceNow GRC (POA&M), HaloPSA (meeting notes) |

---

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
| SC — System and Communications Protection | 5 |
| SI — System and Information Integrity | 5 |
| SR — Supply Chain Risk Management | 2 |
| PM — Program Management | 3 |
| **Total** | **87** |

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-20 | cragin-security | Culled 9 overlapping shuttle-hand controls, expanded 15 keepers to full 9-field format with MSP notes, tool bindings, and subordinate standards. Total: 87 controls across 19 families. |
| 1.0.0 | 2026-07-03 | cragin-security | Initial release: 97 controls across 19 families |

### Review Triggers

- Quarterly review against threat intelligence and regulatory changes
- Re-review if upstream CERG CB-001 is updated
- Re-review on major tool stack changes (vendor acquisition, breach, EOL)

### Related Documents

- [Upstream CERG Unified Control Baseline](CERG-GOV-CB-001_Unified_Control_Baseline.md)
- [Opinionated Tool Matrix](../practice-assets/tools/opinionated-tool-matrix-v1.md)
- [MSP Runbook](../practice-assets/msp-runbook-v1.md)
- [GRC Rollout Guide](../practice-assets/tools/grc-rollout-v1.md)
- [Engagement Playbook](../practice-assets/engagement-playbook-v1.md)
