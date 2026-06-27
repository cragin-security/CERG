## SECURITY OPERATING STANDARD
### 100 Core Controls · Implementation Guidance · Tool Mappings · Compensating Controls

---

|  |  |
|---|---|
| **Document ID** | CERG-GOV-CB-001 |
| **Version** | 3.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Control Framework) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-STD-AI-001](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) |
| **Review Cycle** | Quarterly - and on framework version change |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · CIS Controls v8 · ISO/IEC 27001 A.5–A.8 · PCI DSS v4.0.1 |
| **Regulations** | NERC-CIP v7 · CMMC L2 · SOX ITGC · PCI DSS v4.0.1 |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT, CUI, AI-enabled systems |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Design Principles](#2-design-principles)
3. [Control Family Spine](#3-control-family-spine)
4. [Control Tiers and Statuses](#4-control-tiers-and-statuses)
5. [Implementation Guide: How to Use This Document](#5-implementation-guide-how-to-use-this-document)
6. [Core Controls (100)](#6-core-controls-100)
    - [6.1 Access Control (AC)](#61-access-control-ac)
    - [6.2 Audit and Accountability (AU)](#62-audit-and-accountability-au)
    - [6.3 Configuration Management (CM)](#63-configuration-management-cm)
    - [6.4 Contingency Planning and Recovery (CP)](#64-contingency-planning-and-recovery-cp)
    - [6.5 Identification and Authentication (IA)](#65-identification-and-authentication-ia)
    - [6.6 Risk Assessment and Vulnerability Management (RA)](#66-risk-assessment-and-vulnerability-management-ra)
    - [6.7 System and Information Integrity (SI)](#67-system-and-information-integrity-si)
    - [6.8 Supply Chain and Third-Party Risk (SR)](#68-supply-chain-and-third-party-risk-sr)
    - [6.9 System and Communications Protection (SC)](#69-system-and-communications-protection-sc)
    - [6.10 Assessment and Authorization (CA)](#610-assessment-and-authorization-ca)
    - [6.11 Awareness and Training (AT)](#611-awareness-and-training-at)
    - [6.12 Incident Response (IR)](#612-incident-response-ir)
    - [6.13 Physical and Environmental Security (PE)](#613-physical-and-environmental-security-pe)
    - [6.14 Planning and Program Management (PL/PM)](#614-planning-and-program-management-plpm)
    - [6.15 Personnel Security (PS)](#615-personnel-security-ps)
    - [6.16 System and Services Acquisition (SA)](#616-system-and-services-acquisition-sa)
7. [Compensating Control Catalog](#7-compensating-control-catalog)
8. [Reference Tool Stack](#8-reference-tool-stack)
9. [Inheritance Model](#9-inheritance-model)
10. [Overlay Matrix](#10-overlay-matrix)
11. [Evidence Automation](#11-evidence-automation)
12. [Framework Alignment (Capability Map)](#12-framework-alignment-capability-map)
13. [Governance, Change, and Versioning](#13-governance-change-and-versioning)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Scope

This document is the authoritative control set for the CERG operating model. Every control in this document is implementation-ready: each has an IT generalist walkthrough, an MSP pattern, a security engineer reference, a tool mapping, a verification step, and a compensating control fallback.

It applies to every in-scope asset. Overlays in §10 add or tighten controls for specific regulatory regimes.

> **Who This Document Is For**
>
> - **IT generalist:** You maintain servers, manage identities, or respond to tickets. Each control tells you exactly what to do, in what order, and how to verify it worked.
> - **MSP technician:** You manage security for multiple clients. Each control has a repeatable pattern you can template across your client base.
> - **Security engineer:** You design and automate controls. This document gives you the standard. Go build.
> - **Auditor / assessor:** You verify controls are operating. Section 6 has the evidence requirements. Section 7 has compensating controls. Section 12 has regulatory mappings.

---

## 2. Design Principles

1. **NIST 800-53 is the organizing spine.** Control families follow NIST conventions. CERG-native controls are layered onto that spine, never the reverse.
2. **Every control has a single accountable pillar.** Engineering, Risk, or Governance. Never "shared."
3. **Every control names evidence.** A control without a named evidence artifact does not enter this document.
4. **Overlays add, they do not redefine.** Regulatory overlays tighten parameters. They never silently relax the base.
5. **Implementation guidance serves three readers.** IT generalist (step-by-step), MSP (repeatable pattern), security engineer (standard + tool).
6. **Name tools.** Tool-agnostic in design, tool-opinionated in implementation guidance. Every control names the primary tool, acceptable alternatives, and tools to avoid.

---

## 3. Control Family Spine

| Family | Code | Capability Statement | Pillar |
|--------|------|---------------------|--------|
| Access Control | AC | Only the right people, with the right access, at the right time. | Engineering |
| Audit and Accountability | AU | Every consequential action is logged, protected, and reviewed. | Risk |
| Configuration Management | CM | Approved baselines, controlled changes, no drift. | Engineering |
| Contingency Planning | CP | Recovery that survives ransomware, region failure, and OT events. | Engineering |
| Identification and Authentication | IA | Phishing-resistant identity for humans and machines. | Engineering |
| Risk Assessment | RA | Know your exposure before an attacker does. | Risk |
| System and Information Integrity | SI | Vulnerabilities found, fixed, and verified on schedule. | Risk |
| Supply Chain Risk | SR | Your vendors are not your weakest link. | Risk (TPRM) |
| System and Communications Protection | SC | Networks segmented, data encrypted, boundaries enforced. | Engineering |
| Assessment and Authorization | CA | Prove controls operate as intended. | Governance |
| Awareness and Training | AT | Every person knows their role in security. | Governance |
| Incident Response | IR | Detect, contain, recover, learn. Repeat. | Risk |
| Physical and Environmental | PE | Secure the places where systems live. | Governance / Engineering |
| Planning and Program Management | PL/PM | Policy, metrics, governance that runs. | Governance |
| Personnel Security | PS | Trust but verify — before access. | Governance |
| System and Services Acquisition | SA | Security baked in before you buy. | Risk / Engineering |

---

## 4. Control Tiers and Statuses

### Control Tiers

| Tier | Count | Audience | Implementation Depth |
|------|-------|----------|---------------------|
| **Core** | 100 | All organizations | Full guidance: IT generalist, MSP, security engineer, tool mappings, verification |
| **Enhanced** | 100 (planned, v3.x) | Regulated environments, 50+ FTEs, multi-cloud | Same format; adds automation patterns, integration guidance |
| **Advanced** | 50+ (planned, v4.0) | Enterprise, multi-regulator, mature programs | Detection engineering, threat intel integration, adversary simulation |

### Implementation Statuses

Every control carries one of: `Implemented` · `Partially Implemented` · `Inherited` · `Planned` · `Risk Accepted` · `Not Applicable`. No other statuses are valid.

---

## 5. Implementation Guide: How to Use This Document

### For the IT Generalist

You are not a security engineer. That is fine. Every control in this document includes a section called **"For the IT Generalist"** that tells you:

1. **What you need** — tools, access, permissions
2. **What to do** — numbered steps, one action per step
3. **What commands to run** — copy-paste ready for Windows, Mac, or Linux
4. **How to verify it worked** — what "done" looks like
5. **What to do if it breaks** — the most common mistakes and how to fix them

If you get stuck on any control, skip to the "What to do if you cannot implement this" section. Some controls have compensating controls you can use instead.

### For the MSP

You manage security for multiple clients. Every control includes a **"For the MSP"** section that gives you:

1. **How to template this control** across all your clients
2. **What to automate** — scripts, scheduled tasks, CI/CD pipelines
3. **How to collect evidence** per client, per reporting period
4. **How to charge for this** — is it included in standard managed services or an add-on?

Build a client onboarding checklist from the Core controls. Run them once per new client. Schedule the recurring ones (quarterly recertification, monthly exports) in your RMM or PSA tool.

### For the Security Engineer

You know what to do. Each control gives you:
1. The standard reference
2. Evidence requirement and cadence
3. Primary tool integration
4. Automation pattern

### Tool Mapping Legend

| Icon | Meaning |
|------|---------|
| ✅ Primary | Recommended platform. If you use nothing else, use this. |
| ◐ Acceptable | Works but has known limitations documented in the control. |
| ❌ Avoid | Known problems: high false positive rate, poor integration, vendor instability. |

## 6. Core Controls (100)

Each control entry follows this structure:

```
### [ID] [Name] — Tier: [Core/Enhanced/Advanced]
**Statement:** One-sentence operational requirement.

**For the IT Generalist:**
1. Step-by-step numbered instructions
2. Platform-specific commands (copy-paste ready)
3. Expected output

**For the MSP:**
- How to template across clients
- Automation approach
- Evidence collection pattern

**For the Security Engineer:**
- Standard reference
- Evidence requirement and cadence
- Integration notes

**Tool Mappings:**
✅ Primary: [tool] — coverage notes
◐ Acceptable: [tool] — limitations
❌ Avoid: [tool] — reason

**Verification:**
- Command or procedure to verify the control is operating
- What "control failure" looks like

**Common Mistakes:**
- Top 3-5 implementation errors

**If You Cannot Implement This:**
- Compensating control path
- Regulatory acceptability notes
```

### 6.1 Access Control (AC)

---

### AC-1 Access Control Policy and Procedures — Tier: Core

**Statement:** Access control requirements are documented, reviewed annually, and applied consistently.

**For the IT Generalist:**
1. Your organization should have a document that says who can access what. Find it in your shared drive or ask your manager.
2. If it does not exist, create a one-page document listing: (a) how users get access, (b) how access is removed, (c) who approves access changes.
3. Save it in a shared location everyone can find.
4. Set a calendar reminder to review it every 12 months.

**For the MSP:**
- Maintain one master access control procedure document per client.
- Review during quarterly business review.
- Template across clients: only client name, systems list, and approver names change.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-1 · ISO 27001 A.9.1.1 · PCI DSS Req 7.1
- Evidence: Policy document with annual review date
- Cadence: Annual; update on org change

**Tool Mappings:**
✅ Confluence / SharePoint / Git — document lives where everyone can find it
◐ Network drive — harder to version-control
❌ Someone's email drafts — not acceptable for any regulatory framework

**Verification:**
- Can you find the access control policy in under 2 minutes?
- Does it have a review date within the last 12 months?

**Common Mistakes:**
- Policy exists but no one knows where it is. Store it in the one place everyone looks.
- Policy reviewed but no changes noted. Document "no changes" as a valid review outcome.

**If You Cannot Implement This:**
No regulatory authority accepts "no access control policy." This is a find-it-or-build-it control.

---

### AC-2 Account Lifecycle Management — Tier: Core

**Statement:** Every account has an approved request, named owner, defined access level, and current JML record.

**For the IT Generalist:**
1. When HR sends a new-hire notification, create the account in your IdP with the minimum groups needed.
2. Log the ticket: "Account created for [name] with access to [systems]. Approved by [manager]."
3. When a user changes roles, update group memberships. Remove old ones.
4. When HR sends a termination, disable the account immediately. Wait 30 days before deletion.
5. Run monthly: export all active accounts and compare to the HR roster. Investigate any account without an HR record.

*Windows/Entra ID:*
```powershell
Get-AzureADUser -All $true | Where-Object AccountEnabled -eq $true |
  Select-Object DisplayName, UserPrincipalName, Department |
  Export-CSV "active-users-$(Get-Date -Format yyyy-MM).csv" -NoType

# Find accounts without managers (potential orphan accounts)
Get-AzureADUser -All $true | Where-Object { $_.Manager -eq $null -and $_.AccountEnabled -eq $true }
```

**For the MSP:**
- Connect IdP to client HR system (Workday, BambooHR, Rippling) for automated JML.
- Weekly orphan account report: accounts without managers, accounts not logged in for 90+ days.
- Account lifecycle management is standard managed services. Quarterly recertification is included.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-2 · PCI DSS Req 7.2.4 · CMMC AC.L2-3.1.5
- Evidence: JML audit log, quarterly recertification report, shared-account exceptions
- Cadence: Continuous (JML), Quarterly (recertification)

**Tool Mappings:**
✅ Entra ID — full lifecycle, HR-driven provisioning, entitlement management
✅ Okta — lifecycle workflows, HR integration
◐ Google Workspace — lifecycle management, no native recertification
❌ On-prem AD with manual CSV — no cloud identity lifecycle

**Verification:**
- Compare IdP user list to HR roster. Any accounts without HR records? Any HR records without accounts?
- Any account with `lastLogonTimestamp` > 90 days? Investigate.

**Common Mistakes:**
- Shared accounts for convenience. Every user gets a unique ID.
- Deleting accounts on termination. Disable first, delete after 30 days.
- Contractor accounts without expiration dates.

**If You Cannot Implement This:**
No IdP: use a spreadsheet as account inventory, update weekly, compare to payroll. Not sustainable past 20 users. For PCI/CMMC: no compensating control accepted for access reviews.

---

### AC-3 Access Enforcement — Tier: Core

**Statement:** All access is enforced through approved authentication and authorization controls. Local or static credentials cannot bypass them.

**For the IT Generalist:**
1. Configure your IdP as the single authentication source.
2. Disable local accounts on servers and workstations. Use domain/cloud accounts.
3. If local accounts are required (break-glass), store passwords in a vault, not a text file.
4. Configure conditional access: require managed devices for corporate data access.

*Windows: Disable built-in local admin after confirming domain admin exists:*
```powershell
Get-LocalUser | Where-Object Enabled -eq $true
Disable-LocalUser -Name "Administrator"
```

**For the MSP:**
- Standardize one IdP per client. No on-prem AD without cloud sync.
- Conditional access policies are per-client templates: block legacy auth, require MFA, require compliant device.
- Monthly: check for new local admin accounts outside the IdP.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-3 · PCI DSS Req 7.1
- Evidence: IdP/PAM policy export, local account audit
- Cadence: Annual policy review; continuous local account monitoring

**Tool Mappings:**
✅ Entra ID Conditional Access — full enforcement with device compliance
✅ Okta — global session policy, device trust, network zones
❌ Local accounts with no central policy — no audit trail, no enforcement

**Verification:**
- Try logging in with a disabled local account. If it works, the control is failing.
- Any admin elevation paths that bypass MFA?

**Common Mistakes:**
- Legacy authentication enabled (Exchange ActiveSync, POP3, IMAP). Block it — these bypass MFA.
- LAPS not deployed on domain-joined Windows. Local admin passwords are identical on every machine.

**If You Cannot Implement This:**
No compensating control exists for access enforcement. Every framework requires it.

---

### AC-4 Least Privilege — Tier: Core

**Statement:** Users, administrators, services, and vendors receive only the access needed for their role. Privileged access is time-bound and recorded.

**For the IT Generalist:**
1. Review group memberships. Remove groups users do not need.
2. Use RBAC groups: "Engineering-Readers," "Engineering-Contributors," "Engineering-Admins." Assign minimum.
3. For admin access: use a PAM tool or JIT access that provides time-limited elevation.
4. Do not add users to Domain Admins for daily work.

*Check Domain Admin membership:*
```powershell
Get-ADGroupMember -Identity "Domain Admins" | Select-Object Name, SamAccountName
# Should be 2-4 users at most
```

**For the MSP:**
- Standard RBAC templates per client by job function.
- Enable JIT access: users request elevation, get 4-hour access, expires automatically.
- Monthly: report privilege group changes. Flag users in 2+ privileged groups.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-6 · PCI DSS Req 7.2
- Evidence: PAM session logs, role inventory, privilege review records
- Cadence: Continuous (sessions), Quarterly (role review)

**Tool Mappings:**
✅ CyberArk — PAM leader, session recording, credential rotation
✅ Entra PIM — JIT for Azure/Entra roles
◐ Delinea — good on-prem, weaker cloud
❌ Domain Admin for everyone — automatic audit finding

**Verification:**
- How many Domain Admins? Target <5.
- Can you generate a 30-day privilege elevation report?
- Any user in 3+ privileged groups?

**Common Mistakes:**
- "Temporary" admin access that never expires. Use JIT.
- Service accounts with domain admin privileges.
- Vendors with permanent VPN + admin access.

**If You Cannot Implement This:**
No PAM: use LAPS (Windows) for local admin passwords. For PCI/CMMC, PAM is effectively required.

---

### AC-5 Failed Authentication Management — Tier: Core

**Statement:** Failed login attempts are limited (≤10 before lockout), lockouts are enforced, and brute-force alerts are configured.

**For the IT Generalist:**
1. Configure account lockout: 10 failed attempts, 15-minute lockout window.
2. Configure alerts: notify security when any account approaches the lockout threshold.
3. Do not set permanent lockout — attackers use it to DoS legitimate users.

*Entra ID:* Enable Identity Protection sign-in risk policy. Block access when risk is medium or high.

**For the MSP:**
- Standard lockout policy per client.
- Alert when 10+ failed logins from a single IP across multiple clients — credential stuffing pattern.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-7 · PCI DSS Req 8.3.4
- Evidence: IdP policy, lockout audit logs, alert configuration
- Cadence: Annual policy review; continuous monitoring

**Tool Mappings:**
✅ Entra ID Identity Protection — risk-based conditional access, brute force detection
✅ Okta — rate limiting, impossible travel detection
❌ No lockout policy — direct PCI DSS violation

**Verification:**
```powershell
Get-AzureADAuditSignInLogs -Filter "status/failureReason eq 'Invalid username or password'" |
  Where-Object { $_.CreatedDateTime -gt (Get-Date).AddDays(-1) } |
  Group-Object IpAddress | Where-Object Count -gt 5
```

**Common Mistakes:**
- Lockout threshold >10 attempts. PCI requires ≤10.
- No alerting on failed logins. Lockout works silently until someone notices the outage.
- Lockout duration too long (24 hours). 15-30 minutes is standard.

**If You Cannot Implement This:**
PCI DSS Req 8.3.4 explicitly requires lockout after ≤10 attempts. No compensating control is accepted for CDE scope.

---

### AC-6 Remote Access Management — Tier: Core

**Statement:** Remote access uses approved gateways, MFA for every connection, and session logging. Direct internet-exposed remote protocols are prohibited.

**For the IT Generalist:**
1. Set up a VPN or zero-trust remote access gateway.
2. Require MFA on the gateway. Every single connection.
3. Log all remote sessions: who, from where, when, how long.
4. Disable direct RDP and SSH exposed to the internet.

**For the MSP:**
- VPN/ZTA gateway is standard for every client with remote users.
- MFA on VPN is non-negotiable.
- Log remote access centrally. Keep logs for 12 months minimum.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-17 · PCI DSS Req 8.3.1
- Evidence: Gateway logs, MFA policy, remote access policy
- Cadence: Continuous (logs), Annual (policy)

**Tool Mappings:**
✅ Entra ID Global Secure Access — MFA + conditional access for all remote apps
✅ Cloudflare Zero Trust — no-VPN, device posture checks
◐ Traditional VPN (AnyConnect, Pulse Secure) — MFA-capable, needs SIEM for logging
❌ Direct RDP/SSH to internet — immediate audit finding

**Verification:**
- External scan: check for RDP (3389), SSH (22) exposed to the internet.
- Log review: remote sessions from unexpected geographies?
- MFA test: try connecting without the second factor. Should fail.

**Common Mistakes:**
- "Just this one vendor" exception. No exceptions — they use the same gateway.
- MFA on VPN but not on VPN-to-app traffic. MFA at gateway only covers first mile.
- No session recording for third-party remote access.

**If You Cannot Implement This:**
No VPN budget: Entra ID App Proxy (included with many P1/P2 licenses) or Cloudflare Zero Trust (free tier). Direct RDP/SSH is not acceptable in any regulatory framework.

---

### AC-7 Mobile and BYOD — Tier: Core

**Statement:** Mobile and BYOD access is allowed only when the device is enrolled, compliant, and managed.

**For the IT Generalist:**
1. Enroll devices in MDM (Intune, JAMF, Workspace ONE).
2. Configure compliance policies: encryption, screen lock, minimum OS version.
3. Configure conditional access: only compliant devices access email and corporate apps.
4. For BYOD: use app protection policies (MAM) instead of full MDM — protects corporate data without managing the whole device.

*Intune check:*
```powershell
Get-MgDeviceManagementManagedDevice |
  Select-Object DeviceName, ComplianceState, LastSyncDateTime
```

**For the MSP:**
- MDM/MAM is standard for every client with mobile users.
- App protection policies (MAM) for BYOD: corporate data protection without privacy concerns.
- Remote selective wipe on departure — not full device wipe.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-19 · PCI DSS Req 9.5 (POI devices)
- Evidence: MDM compliance report, conditional access policy, device inventory
- Cadence: Quarterly

**Tool Mappings:**
✅ Intune — MDM + MAM, deep Entra ID integration
✅ JAMF Pro — best-in-class for Apple devices
❌ No MDM — direct regulatory finding

**Verification:**
- Can a user access corporate email from an unmanaged phone? Should not be possible.
- Device compliance: what percentage are non-compliant? Target <5%.

**Common Mistakes:**
- MDM policies too permissive. Encryption required but no minimum OS version.
- BYOD privacy pushback. Use MAM — communicate what you can and cannot see.
- No remote wipe capability for lost devices. Test quarterly.

**If You Cannot Implement This:**
For cloud-only (M365/Google): use app protection policies (MAM), included in many Entra/Workspace licenses.

### 6.2 Audit and Accountability (AU)

---

### AU-1 Audit Logging Configuration — Tier: Core

**Statement:** All systems send security, authentication, and administrative logs to a centralized log platform. No system operates without logging.

**For the IT Generalist:**
1. Configure each server, network device, and cloud service to send logs to your SIEM or log collector.
2. At minimum, send: user logins (success + failure), admin actions, system events (startup, shutdown, errors), firewall accepts/denies.
3. Verify logs are arriving: search the SIEM for events from each system. If a system has no events in 24 hours, investigate.
4. Document which systems are sending logs and which are not. Fix the gaps.

*Windows event forwarding:*
```powershell
# Check if Windows Event Forwarding is configured
wevtutil gl "ForwardedEvents" | Select-String "enabled"

# Verify events are being collected
Get-WinEvent -LogName "ForwardedEvents" -MaxEvents 10 |
  Format-Table TimeCreated, Id, LevelDisplayName
```

**For the MSP:**
- Log collection is standard for every managed client.
- Per-client: document the log source inventory. Flag any server not sending logs for more than 48 hours.
- Centralize logs across clients in a single SIEM tenant with per-client data isolation.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-2 · PCI DSS Req 10.2 · ISO 27001 A.12.4.1
- Evidence: SIEM source inventory, coverage gap report, sample log entries
- Cadence: Monthly coverage review; continuous ingestion

**Tool Mappings:**
✅ Microsoft Sentinel — native Entra ID and M365 log integration
✅ Splunk — mature log management, broadest parser library
✅ Wazuh (self-hosted) — open-source, good for budget-constrained teams
◐ Chronicle (Google) — strong at scale, weaker Windows event coverage
❌ Logs stored locally on each server (no central collection) — audit finding in every framework

**Verification:**
- SIEM shows log ingestion from every system in the asset inventory within the last 24 hours.
- Any system silent for 48+ hours? Flagged and investigated.
- Sample a log entry: does it include timestamp, user, action, source IP? (PCI Req 10.3 fields)

**Common Mistakes:**
- Logging enabled but log level too low. Enable "success" and "failure" for audit events — many default configs log failures only.
- Cloud resources not sending logs. Enable Azure Diagnostic Settings, AWS CloudTrail, GCP Audit Logs for every resource.
- Log collection but no retention configured. Logs arrive at the SIEM but roll off after 7 days.

**If You Cannot Implement This:**
No SIEM budget: Wazuh is free and open-source. For PCI DSS, a centralized log platform is required — no compensating control is accepted.

---

### AU-2 Audit Log Review — Tier: Core

**Statement:** Logs are reviewed daily for security events. Anomalies are investigated and tracked to closure.

**For the IT Generalist:**
1. Configure automated alerts in your SIEM: failed logins, admin account creation, firewall denies, malware detection.
2. Check the alert queue every morning. Investigate anything marked high or critical.
3. Document each investigation: what happened, what you found, what you did about it, when you closed the ticket.
4. If the same alert fires every day with no action, tune it — either fix the root cause or adjust the threshold.

**For the MSP:**
- Daily log review is included in standard managed services.
- Use a SIEM with managed detection rules — do not rely on manual review.
- Triage SLA: critical alerts within 1 hour, high within 4 hours, medium by end of next business day.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-6 · PCI DSS Req 10.4.1.1 · ISO 27001 A.12.4.3
- Evidence: SIEM alert queue metrics, investigation tickets, daily review evidence
- Cadence: Continuous (automated alerts), Daily (human review)

**Tool Mappings:**
✅ Microsoft Sentinel — built-in SOAR for automated investigation
✅ Splunk + SOAR — mature alert management
✅ Wazuh — open-source alerting, active response
❌ Manual log review only (no SIEM) — impractical for any environment over 10 users

**Verification:**
- Check the SIEM alert queue: are there any critical alerts older than 1 hour without an owner?
- Run a report: alerts closed within SLA vs. overdue. Target >90% within SLA.
- Are there any detection rules that have fired 100+ times with zero investigations? Tune or retire them.

**Common Mistakes:**
- Alert fatigue: too many low-severity rules firing without triage. Prune rules quarterly.
- No documented investigation: alert was "reviewed" but no ticket or notes exist. An auditor will ask what you found.
- Ignoring medium-severity alerts: they accumulate into blind spots.

**If You Cannot Implement This:**
For very small teams (<10 users): configure email alerts from your IdP and firewall. Review daily. Document in a shared spreadsheet with date, finding, action. This is not sustainable past 10 users.

---

### AU-3 Audit Log Protection — Tier: Core

**Statement:** Audit logs are protected from modification or deletion. Administrative changes to logging are also logged.

**For the IT Generalist:**
1. Configure your SIEM to prevent anyone from deleting or modifying log data.
2. Restrict who can access the SIEM to the security team only.
3. Enable immutable storage for logs: write-once, read-many (WORM).
4. Log admin actions on the SIEM itself: who changed a detection rule, who modified a log source, who exported data.

*Azure Sentinel immutable storage:*
```azurecli
# Enable immutable blob storage for the log analytics workspace
az storage container immutability-policy create \
  --container-name sentinel-logs \
  --account-name logstorageaccount \
  --policy-mode unlocked
```

**For the MSP:**
- Immutable storage for client logs is standard. No exceptions.
- SIEM admin actions are logged and reviewed weekly.
- Per-client: document who has SIEM admin access. Review quarterly.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-9 · PCI DSS Req 10.5
- Evidence: Storage policy, admin-action audit logs, immutability configuration
- Cadence: Quarterly

**Tool Mappings:**
✅ Azure Immutable Blob Storage — WORM compliance, 1-year minimum retention
✅ AWS S3 Object Lock — similar, configurable retention period
✅ Splunk — tamper-resistant storage with FIPS 140-2
❌ Logs stored in a network share with full access to everyone — security finding

**Verification:**
- Can a non-admin user delete log data? Try it — it should fail.
- Can an admin delete logs without the action being logged? Should not be possible.
- Is immutability enabled for the log storage account? Verify the policy.

**Common Mistakes:**
- Logs protected but SIEM admin activities not logged. The guards need guarding.
- Immutability configured but someone can disable it. Use a lock policy that requires 30-day notice to disable.
- Log retention too short. PCI requires 12 months hot / 7 years cold.

**If You Cannot Implement This:**
At minimum, restrict write/delete access to the log store to 2 named security admins. Document who they are. Audit access quarterly.

---

### AU-4 Audit Record Retention — Tier: Core

**Statement:** Audit records are retained for the required period: 12 months hot (immediately searchable), 7 years cold (archived but retrievable).

**For the IT Generalist:**
1. Configure log retention in your SIEM: 12 months of hot data.
2. Configure long-term archival: export logs to low-cost storage (Azure Archive, AWS Glacier, cold blob storage) after 12 months.
3. Test retrieval annually: pull a sample log entry from cold storage. Confirm it is readable.
4. Document the retention policy: what is kept, where, for how long.

*Azure Sentinel retention:*
```azurecli
az monitor log-analytics workspace table update \
  --workspace-name sentinel-workspace \
  --resource-group rg-security \
  --name SecurityEvent \
  --retention-time 365
```

**For the MSP:**
- Standard retention per client: 12 months hot, 7 years cold.
- Automated archival scripts to move old logs to cold storage.
- Annual retrieval test: one client per quarter on a rotating schedule.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-11 · PCI DSS Req 10.7
- Evidence: Retention policy, storage configuration, sample retrieval evidence
- Cadence: Annual (retrieval test), Quarterly (retention review)

**Tool Mappings:**
✅ Azure Log Analytics + Archive — native archival to cold storage
✅ Splunk — SmartStore + S3 archival
✅ Wazhu — built-in log rotation and archival
❌ Logs overwritten daily — regulatory violation

**Verification:**
- Run a query against cold storage: can you retrieve a log entry from 14 months ago?
- Check retention settings: are they configured per data type?
- Is there a documented retention policy? Does it meet regulatory requirements?

**Common Mistakes:**
- Same retention for all data types. Security events need longer retention than debug logs. Set per-table.
- Cold storage but no retrieval test. Archived data you cannot read is not evidence.
- Retaining everything forever. Data hoarding increases breach disclosure scope.

**If You Cannot Implement This:**
At minimum, keep 12 months of security logs on the SIEM hot tier. For archival, export compressed logs to object storage. PCI DSS requires 12 months hot / 7 years cold — no effective compensating control for CDE scope.

---

### 6.3 Configuration Management (CM)

---

### CM-1 Configuration Baseline (DISH) — Tier: Core

**Statement:** Every system is configured to an approved security baseline (DISH) before production deployment and maintained against that baseline throughout its life.

**For the IT Generalist:**
1. Find the DISH baseline for your platform (Windows Server, Linux, network device, cloud account).
2. Apply the baseline using the provided scripts or Group Policy / Ansible / cloud policy.
3. Run a baseline compliance scan: verify the system meets the baseline.
4. If the scan finds non-compliant settings, fix them. If you cannot fix them (business need), document an exception.
5. Schedule periodic scans: daily for critical systems, weekly for standard.

*Windows: Apply and verify DISH baseline:*
```powershell
# Run a compliance check against the CIS benchmark
Invoke-GPUpdate -Force
secedit /configure /db secedit.sdb /cfg dish-windows-server.cfg /areas SECURITYPOLICY

# Verify
secedit /validate /db secedit.sdb
```

**For the MSP:**
- Apply DISH baseline to every new client onboarding. Document baseline version and any deviations.
- Use Group Policy, Intune, or Ansible to apply baselines at scale.
- Quarterly: scan a sample of client systems for baseline drift. Report results.

**For the Security Engineer:**
- Reference: NIST 800-53 CM-2, CM-6 · PCI DSS Req 2.2 · ISO 27001 A.12.5.1
- Evidence: DISH baseline catalog, compliance scan report, exception register
- Cadence: Continuous (scan), Quarterly (baseline review)

**Tool Mappings:**
✅ DISH benchmark + CIS-CAT — comprehensive compliance scanning
✅ Microsoft Defender for Cloud — CIS/Azure Security Benchmark assessments
✅ AWS Security Hub — CIS benchmarks for AWS
✅ Wazuh — open-source SCAP compliance scanning
❌ Manual configuration without baseline — audit finding

**Verification:**
- Can you produce a report showing every system's baseline compliance score? Target >90%
- Are drifted systems flagged and remediated within 7 days?
- Are all baseline exceptions documented with owner and target date?

**Common Mistakes:**
- Baseline applied once at deployment, never scanned again. Drift happens. Scan continuously.
- Baseline applied but business-critical applications break. Have an exception process — do not turn off the baseline.
- Cloud resources not covered. DISH must cover cloud configuration benchmarks too.

**If You Cannot Implement This:**
No scanning tool: Wazuh includes SCAP compliance scanning for free. Without at least quarterly scanning, no regulatory framework accepts this control as implemented.

---

### CM-2 Change Control — Tier: Core

**Statement:** All production changes are authorized, documented, tested, and reviewed before implementation.

**For the IT Generalist:**
1. Create a change request ticket for every production change. Include: what is changing, why, the rollback plan, the test results.
2. For high-risk changes (firewall rules, authentication config, production code), get written approval from the system owner.
3. Implement the change during the approved maintenance window.
4. After implementation, verify the change had the intended effect and nothing is broken.
5. Document the result: "Change implemented as planned. Services are operational."

**For the MSP:**
- Use a change management workflow in your PSA tool for every client.
- Standard change vs. emergency change: define criteria. Emergency changes (security patch, outage fix) get after-the-fact approval within 24 hours.
- Weekly CAB meeting: 30 minutes, review past week's changes and approve upcoming ones.

**For the Security Engineer:**
- Reference: NIST 800-53 CM-3 · PCI DSS Req 6.5.1 · SOX ITGC Change
- Evidence: Change records, CAB minutes, security impact assessment
- Cadence: Continuous

**Tool Mappings:**
✅ ServiceNow — mature change management, CAB workflows
✅ Jira Service Management — ITIL-compliant change workflows
✅ Freshservice — good for mid-market, built-in CAB
❌ Changes made through direct server access with no ticket — audit finding

**Verification:**
- Can you trace any production change in the last 30 days to an approved ticket?
- Are there emergency changes without after-the-fact approval? Flag.
- Percentage of changes with security impact assessment completed: target >90%.

**Common Mistakes:**
- Emergency change abuse. If 30%+ of changes are emergency changes, the process is broken. Tighter criteria.
- "No impact" changes bypassing review. Every production change gets a ticket. No exceptions.
- Test results documented but no rollback plan. Every change must have a "how to undo this."

**If You Cannot Implement This:**
For small teams (<10): use a change log spreadsheet. Date, requestor, description, approver, result. Any framework with SOX or PCI scope requires a documented change process.

---

### CM-3 Configuration Drift Detection — Tier: Core

**Statement:** Configuration drift from the approved baseline is detected, flagged, and remediated.

**For the IT Generalist:**
1. Configure drift detection on your systems. DISH-included tools or cloud-native tools (Azure Policy, AWS Config, GCP Org Policies).
2. Define the remediation process: drift detected → assess impact → fix or document as exception → verify fix.
3. Set alerting: notification on any drift in critical systems.
4. Monthly: review all drift events. Look for patterns — repeated drift on the same system means the baseline is wrong.

*Azure Policy drift detection:*
```azurecli
az policy state list --resource-group rg-production
```

**For the MSP:**
- Enable drift detection for every managed client.
- Cloud-native tools (Azure Policy, AWS Config) are the easiest path — no additional agent.
- Monthly drift report per client. If a system drifts 3+ times in a quarter, investigate the root cause.

**For the Security Engineer:**
- Reference: NIST 800-53 CM-6 · PCI DSS Req 11.5 (change detection on CHD)
- Evidence: Drift report, exception register, remediation tickets
- Cadence: Continuous (detection), Monthly (review)

**Tool Mappings:**
✅ Azure Policy — real-time drift detection for Azure resources
✅ AWS Config — continuous monitoring of AWS resource configuration
✅ Wazuh — FIM (file integrity monitoring) + configuration assessment
❌ No drift detection — systems drift silently

**Verification:**
- Run a drift report: are there any drifted resources right now?
- For the last drifted resource: how long did it take to detect? How long to remediate?
- Any system that drifted and was not remediated within 30 days? Flag.

**Common Mistakes:**
- Drift detected but no automated remediation. Use auto-remediate for known-safe baselines.
- Exceptions not documented. If a system must drift, document the exception — otherwise it looks like a control failure.
- File-level FIM without configuration-level monitoring. FIM catches file changes but not registry or policy changes.

**If You Cannot Implement This:**
For non-critical systems: quarterly manual baseline comparison is acceptable for initial adoption. For PCI CDE or CMMC CUI, automated drift detection is required.

---

### CM-4 System Component Inventory — Tier: Core

**Statement:** Every hardware, software, cloud resource, network device, and data store is recorded in an authoritative inventory.

**For the IT Generalist:**
1. Maintain a list of every IT asset: servers, workstations, network devices, cloud instances, SaaS applications, databases.
2. Include for each: name, type, location (cloud/on-prem), owner, criticality (high/medium/low), software installed (with versions).
3. Use a CMDB tool, not a spreadsheet. Device42, ServiceNow, or even AirTable is better than Excel.
4. Reconcile the inventory monthly: compare against cloud provider resource lists, AD computer objects, and vulnerability scanner discovery data.

*Azure resource inventory:*
```azurecli
az resource list --query "[].{Name:name, Type:type, Location:location}" --output table
```

**For the MSP:**
- CMDB is standard per client. Device42 is the best value for MSPs.
- Discovery: use network scanning + cloud API + agent-based discovery.
- Quarterly: run a reconciliation report. New assets discovered? Flag for review. Assets not seen in 90 days? Verify decommission.

**For the Security Engineer:**
- Reference: NIST 800-53 CM-8 · PCI DSS Req 12.5.1
- Evidence: CMDB export, reconciliation log, asset discovery report
- Cadence: Continuous (discovery), Monthly (reconciliation)

**Tool Mappings:**
✅ Device42 — agentless discovery, cloud integration, dependency mapping
✅ ServiceNow CMDB — mature, expensive, needs dedicated admin
✅ AirTable — suitable for <500 assets, no discovery
❌ Excel spreadsheet — not sustainable past 50 assets, no automated discovery

**Verification:**
- Can you reconcile the CMDB against your cloud provider's resource list? Any orphan resources?
- Are there assets in the CMDB not seen in 90+ days? Investigate.
- Rogue device detected on the network? If discovery found it, did it appear in the CMDB within 24 hours?

**Common Mistakes:**
- Spreadsheet instead of CMDB. Spreadsheets cannot do discovery, cannot alert on changes, and become stale within a week.
- Cloud resources not in the same inventory as on-prem. One inventory, all environments.
- No decommission process. Assets retired in production but still in the CMDB.

**If You Cannot Implement This:**
For <50 assets: a well-maintained spreadsheet reconciled monthly is acceptable for initial adoption. For any regulatory scope, a CMDB tool is expected.

---

### 6.4 Contingency Planning and Recovery (CP)

---

### CP-1 System Backup — Tier: Core

**Statement:** System and data backups are performed on schedule, stored immutably, and tested for restorability annually.

**For the IT Generalist:**
1. Configure automated backups for all critical systems. Daily for databases, weekly for file servers.
2. Store backups in a separate location from the production system (different region, different account).
3. Enable immutability: backups cannot be modified or deleted before the retention period expires.
4. Schedule a restore test at least once per year. Pick a random backup and restore it to a test environment. Confirm the data is usable.
5. Document the restore test result: what was restored, how long it took, whether the data was complete and usable.

*Azure Backup:*
```azurecli
az backup protection check-vm --vm-id $(az vm show -g rg-prod -n vm-prod --query id -o tsv)
```

**For the MSP:**
- Backup management is standard per client. Use a single backup console (Veeam, Rubrik, Cohesity).
- Immutable backups are standard. No exceptions.
- Restore test schedule: test one client per month on a rotating basis. Rotate through all clients annually.
- Per-client billing: backup management is standard managed services. Restore testing is included.

**For the Security Engineer:**
- Reference: NIST 800-53 CP-9 · PCI DSS Req 10.5.1
- Evidence: Backup report, immutability evidence, restoration test results
- Cadence: Continuous (backup), Annual (restore test)

**Tool Mappings:**
✅ Veeam — best-in-class for hybrid environments, immutable backups, SureBackup verification
✅ Rubrik — cloud-native, instant recovery, ransomware detection
◐ Azure Backup — native, adequate for Azure-only
◐ AWS Backup — native, adequate for AWS-only
❌ Tape-only with no immutability — regulatory finding, ransomware liability

**Verification:**
- Run a backup report: any failed backups in the last 24 hours? 7 days?
- Check immutability: can a backup be deleted before the retention period? It should not be possible.
- Last restore test: when was it? Was it successful? Does the restored data pass integrity checks?

**Common Mistakes:**
- Backups stored in the same account/region as production. Ransomware that compromises the environment will delete backups too.
- Immutability not configured. A backup that can be modified is not a backup — it is a copy that attackers can destroy.
- Restore test not performed. A backup that has never been restored is a wish, not a control.

**If You Cannot Implement This:**
At minimum, keep 3-2-1 backups (3 copies, 2 media types, 1 offsite). Object storage with immutability is the cheapest compliant option.

---

### CP-2 Recovery Planning and Testing — Tier: Core

**Statement:** Recovery procedures are documented, tested at least annually, and updated based on test results.

**For the IT Generalist:**
1. Write a one-page recovery plan for each critical system: step by step, what to do if the system fails.
2. Include: who does what, how to restore from backup, how to verify the system is operational, who to notify.
3. Schedule a tabletop exercise: get the team in a room (or video call) and walk through the plan step by step.
4. After the test, update the plan with lessons learned. What did you miss? What took longer than expected?
5. Run a technical recovery test annually: actually restore from backup.

**For the MSP:**
- One recovery plan per client per critical system. Template across clients where systems are identical.
- Annual tabletop exercise with the client's leadership. 2 hours.
- Technical recovery test annually. Test one system per quarter on a rotating schedule.

**For the Security Engineer:**
- Reference: NIST 800-53 CP-2, CP-4 · ISO 27001 A.17.1.3
- Evidence: Recovery plan, test results, lessons learned, register updates
- Cadence: Annual (full test), Quarterly (tabletop)

**Tool Mappings:**
✅ Veeam SureBackup — automated recovery verification
◐ Manual recovery procedure document — acceptable for initial adoption
❌ No documented plan — regulatory finding

**Verification:**
- When was the last recovery test? Was it successful?
- Are the recovery plan's RTO/RPO targets realistic based on test results?
- Are lessons learned from the last test reflected in the updated plan?

**Common Mistakes:**
- Plan written but never tested. An untested plan is a fantasy. Test it.
- Test passed but RTO was exceeded. The test "passed" because no one timed it. Measure RTO.
- Lessons learned documented but not implemented. Track them in the improvement register.

**If You Cannot Implement This:**
At minimum: run a tabletop exercise annually. Walk through the scenario verbally. Document what you would do. This is not sufficient for BES (NERC-CIP requires technical testing) but is better than nothing for general IT.

---

### 6.5 Identification and Authentication (IA)

---

### IA-1 Multi-Factor Authentication — Tier: Core

**Statement:** All interactive human access requires phishing-resistant MFA. Legacy authentication protocols are disabled.

**For the IT Generalist:**
1. Enable MFA in your IdP for every user. No exceptions — not even for contractors, not even for service accounts (with documented exception).
2. Configure MFA methods: authenticator app (preferred), security key (FIDO2), or SMS (last resort — SMS has known vulnerabilities).
3. Block legacy authentication: disable POP3, IMAP4, Exchange ActiveSync basic auth. These protocols cannot enforce MFA.
4. For break-glass scenarios: create 2 emergency access accounts with long passwords, MFA, and no daily-use assignment.

*Entra ID: Enable MFA via Conditional Access:*
```powershell
# Create a CA policy requiring MFA for all users
New-MgIdentityConditionalAccessPolicy -DisplayName "Require MFA for All Users" `
  -State "enabled" `
  -Conditions @{ users = @{ includeUsers = @("All") } } `
  -GrantControls @{ builtInControls = @("mfa") }
```

**For the MSP:**
- MFA for every client user. Non-negotiable in the MSA.
- Block legacy authentication at the tenant level.
- Security keys (FIDO2) for privileged users, authenticator app for standard users.
- Per-client: monitor MFA registration rate. Target 100%.

**For the Security Engineer:**
- Reference: NIST 800-53 IA-2 · PCI DSS Req 8.3.1 · ISO 27001 A.9.4.2
- Evidence: IdP MFA policy, MFA registration report, legacy auth block evidence
- Cadence: Quarterly

**Tool Mappings:**
✅ Microsoft Entra ID — Conditional Access MFA, FIDO2 support, passwordless
✅ Okta — adaptive MFA, device trust, factor sequencing
✅ Duo Security — simple MFA, broad application support
❌ SMS-only MFA — NIST deprecating, known SS7 vulnerabilities
❌ No MFA — direct PCI DSS violation, single-factor authentication is not acceptable

**Verification:**
- Try connecting with legacy auth (POP3/IMAP/SMTP basic auth). Should fail.
- Check MFA registration: what percentage of users have MFA enrolled? Target 100%.
- Test a break-glass account: can it authenticate without MFA? It should require a security key or be stored in a secure vault.

**Common Mistakes:**
- MFA enabled but legacy auth still allowed. Legacy auth bypasses MFA entirely.
- Service accounts exempted without documentation. Every exception must have a ticket.
- SMS as primary MFA method. SMS is vulnerable to SIM-swapping. Use authenticator app or security key.

**If You Cannot Implement This:**
PCI DSS Req 8.3.1 requires MFA for all non-console CDE access. No compensating control is accepted. For non-regulated environments, at minimum deploy an authenticator app-based MFA.

---

### IA-2 Password Policy — Tier: Core

**Statement:** Passwords meet minimum complexity requirements. Passwordless authentication is used where supported.

**For the IT Generalist:**
1. Configure password policy in your IdP: minimum 12 characters, no complexity requirements (length > complexity), password history of 4.
2. Do not set password expiration policies. NIST and Microsoft both recommend removing periodic password changes — they make passwords weaker (users choose Password!Spring2024!).
3. Block common passwords (password123, CompanyName2024).
4. Enable self-service password reset (SSPR) to reduce help-desk tickets.

*Entra ID password protection:*
```powershell
# Enable banned password list
Set-MgPolicyAuthenticationMethodPolicy -BannedPasswordProtectionEnabled $true
```

**For the MSP:**
- No password expiration policies for any client. Remove them.
- SSPR is standard per client. Reduces helpdesk calls by 30%.
- Per-client: monitor password reset frequency. An unusual spike may indicate a phishing attack.

**For the Security Engineer:**
- Reference: NIST SP 800-63B · PCI DSS Req 8.3.7
- Evidence: Password policy configuration, banned password list, SSPR evidence
- Cadence: Annual policy review

**Tool Mappings:**
✅ Entra ID — password protection, banned password list, SSPR
✅ Okta — password policy, banned passwords, authenticator enrollment
❌ Forcing password changes every 90 days — contra-indicated by NIST, makes passwords weaker

**Verification:**
- Try setting a password like "Spring2024!" on a new account. Should be blocked.
- Check password expiration policy: if there is one, remove it.
- SSPR enrollment rate: target >80% of users.

**Common Mistakes:**
- Enforcing password expiration. Stop. NIST SP 800-63B explicitly recommends against periodic password changes. Use banned password lists instead.
- Requiring complexity (uppercase, number, symbol). Length > complexity. A 16-character passphrase is stronger than "P@ssw0rd!".
- Not blocking common passwords. Every breach analysis finds Password123 in the first 10 attempts.

**If You Cannot Implement This:**
For systems that do not support modern password policies: use a password manager to generate and store complex passwords. At minimum, ban the top 1000 common passwords.

---

### IA-3 Service and Machine Account Management — Tier: Core

**Statement:** Non-human identities (service accounts, API keys, application credentials) are managed with the same rigor as human accounts.

**For the IT Generalist:**
1. Create an inventory of all service accounts, API keys, and application credentials.
2. Disable interactive logon for service accounts — they should not be used to log into a desktop.
3. Store credentials in a secrets manager (Azure Key Vault, AWS Secrets Manager, HashiCorp Vault). Not in config files, not in source code.
4. Rotate secrets on a schedule: every 90 days for high-risk, every 180 days for standard.
5. Review service account permissions quarterly: remove any that are over-privileged.

*Azure Key Vault: Store and retrieve a secret:*
```azurecli
az keyvault secret set --vault-name kv-prod --name "db-connection-string" --value "$connString"
az keyvault secret show --vault-name kv-prod --name "db-connection-string" --query "value"
```

**For the MSP:**
- Service account inventory is part of client onboarding.
- Secrets manager per client. Azure Key Vault is included with many Azure subscriptions.
- Quarterly: review service account permissions. Flag any with domain admin or equivalent privileges.

**For the Security Engineer:**
- Reference: NIST 800-53 IA-3, IA-5 · PCI DSS Req 8.6
- Evidence: Service account inventory, secrets manager access logs, key rotation records
- Cadence: Continuous (secrets rotation), Quarterly (access review)

**Tool Mappings:**
✅ HashiCorp Vault — enterprise secrets management, dynamic secrets, rotation automation
✅ Azure Key Vault — native Azure integration, RBAC, rotation policies
✅ AWS Secrets Manager — automatic rotation for RDS, Redshift
❌ Secrets in config files or source code — direct security finding, instant attack surface

**Verification:**
- Search the source code repository for hard-coded secrets: `grep -r "password\|secret\|connectionString" --include="*.config" --include="*.env"`
- Can you list all service accounts with their last rotation date?
- Are there any service accounts with interactive logon enabled?

**Common Mistakes:**
- Service account with Domain Admin privileges. Service accounts should have minimum permissions for their function.
- API keys in GitHub repositories. Use secret scanning tools (GitHub secret scanning, GitLeaks).
- No rotation schedule for long-lived keys. "The application breaks when we rotate" means the rotation process needs fixing, not skipping.

**If You Cannot Implement This:**
For small environments: use environment variables with a startup script that reads from a vault. Never store secrets in source code.

---

### 6.6 Risk Assessment and Vulnerability Management (RA)

---

### RA-1 Risk Assessment — Tier: Core

**Statement:** Risks are identified, documented in a risk register, scored, assigned an owner, and treated.

**For the IT Generalist:**
1. Create a risk register: a spreadsheet or tool that lists every security risk you know about.
2. For each risk, document: what could go wrong, how likely it is (1-5), how bad it would be (1-5), who owns it, what you are doing about it.
3. Score: Likelihood × Impact = Risk Score. High (12+) and Critical (15+) items need management attention.
4. Review the register monthly. Update scores as things change. Close items that are resolved.
5. If you find a new risk, add it to the register within one week of discovery.

*Risk register template (minimum fields):*
```csv
ID,Description,Affected Assets,Owner,Likelihood,Impact,Score,Treatment,Target Date,Status
RISK-001,No MFA on VPN,VPN Gateway,IT Manager,4,4,16,Implement MFA,2026-08-01,In Progress
```

**For the MSP:**
- Risk register is standard per client. Template across clients with client-specific systems.
- Monthly risk review: 30-minute meeting with the client. Review open risks, close completed items, add new risks.
- Risk register maintenance is included in standard managed services.

**For the Security Engineer:**
- Reference: NIST 800-53 RA-3 · ISO 27001 A.8.2
- Evidence: Risk register, review meeting minutes, treatment records
- Cadence: Continuous (entries), Monthly (review)

**Tool Mappings:**
✅ Risk register spreadsheet → GRC tool (OneTrust, ServiceNow GRC, or simple tracker)
◐ GRC tool — better for regulated environments but needs dedicated admin
❌ No risk register — regulatory finding in every framework

**Verification:**
- Is there a risk register? Does it have at least 10 entries?
- When was the last review? Within the last 30 days?
- Are there any High/Critical items without a target closure date?

**Common Mistakes:**
- Risk register created but never reviewed. A static list is not a program.
- All risks scored the same. If every risk is "Medium," you are not discriminating. Use the full scoring scale.
- No treatment. If every item is "Accept," you are not running a security program — you are documenting neglect.

**If You Cannot Implement This:**
Start with a spreadsheet. 10 entries. One risk per week. You can migrate to a GRC tool later.

---

### RA-2 Vulnerability Scanning — Tier: Core

**Statement:** All in-scope systems are scanned for vulnerabilities on a defined schedule. Findings are tracked and remediated.

**For the IT Generalist:**
1. Set up a vulnerability scanner (Wiz for cloud, Qualys/Tenable/Rapid7 for hybrid).
2. Configure scans: weekly for internet-facing systems, monthly for internal systems.
3. Review scan results. Prioritize: Critical and High findings get remediated first.
4. Create tickets for each finding. Assign to the system owner with a target remediation date.
5. Rescan after remediation to confirm the finding is closed.

*Qualys quick scan:*
```bash
# Launch an authenticated scan against a target
curl -H "X-Requested-With: curl" \
  -u "username:password" \
  -d "action=launch&target=192.168.1.0/24&scan_title=Weekly-Internal-Scan" \
  "https://qualysapi.qualys.com/api/2.0/fo/scan/"
```

**For the MSP:**
- Vulnerability scanning is standard per client.
- Weekly internet-facing scans, monthly internal scans.
- Prioritize: Critical < 7 days, High < 30 days, Medium < 90 days.
- If a client cannot remediate within SLA, document the exception with compensating controls.

**For the Security Engineer:**
- Reference: NIST 800-53 RA-5 · PCI DSS Req 11.3 · ISO 27001 A.12.6.1
- Evidence: Scan reports, SLA dashboard, exception register
- Cadence: Continuous (discovery), Weekly (externally-facing), Monthly (internal)

**Tool Mappings:**
✅ Wiz — agentless cloud scanning, prioritization by internet exposure, exploit path analysis
✅ Qualys — broadest coverage (cloud, on-prem, containers, web apps)
✅ Tenable Nessus — industry standard, broad plugin library
✅ Rapid7 InsightVM — strong prioritization by exploitability
❌ Brinqa — vulnerability correlation platform, not a scanner. Do not replace scanning with correlation.
❌ Kenna — similar to Brinqa, acquired by Cisco; integration overhead exceeds value for most teams

**Verification:**
- When was the last scan? If more than 7 days ago for internet-facing systems, it is overdue.
- What is the SLA compliance rate? Critical findings within 7-day SLA: target >90%.
- Are there any findings older than 90 days without an approved exception?

**Common Mistakes:**
- Scanning without authentication. Unauthenticated scans miss 80% of vulnerabilities. Use domain credentials or agent-based scanning.
- Findings not assigned to an owner. An unassigned finding is an ignored finding.
- Not rescanning after remediation. Close the loop: fix → rescan → confirm → close ticket.

**If You Cannot Implement This:**
No scanner budget: Wiz offers a free tier for cloud scanning. Defect Dojo is open-source for vulnerability tracking. For PCI DSS, ASV-approved quarterly external scanning is required.

---

### RA-3 Vulnerability Remediation — Tier: Core

**Statement:** Vulnerabilities are remediated within defined SLAs. Deferred remediation requires a documented risk acceptance.

**For the IT Generalist:**
1. Patch critical vulnerabilities (CVSS 9+) within 7 days. High (CVSS 7-8.9) within 30 days.
2. If you cannot patch within SLA, document: what is the finding, why can you not patch, what compensating control protects the system, who approved the deferral, what is the target patch date.
3. Prioritize by risk: an internet-facing web server with a known exploit takes priority over an internal-only system with a theoretical vulnerability.
4. Use the scanner's priority score, not just CVSS. Wiz, Qualys, and Tenable all provide context-aware scoring.

**For the MSP:**
- Patch SLA per client: Critical 7 days, High 30 days.
- Documented exception process for all deferred patches.
- Monthly SLA report: findings open vs. closed within SLA. Target >90%.

**For the Security Engineer:**
- Reference: NIST 800-53 SI-2 · PCI DSS Req 6.3.3
- Evidence: SLA dashboard, patch deployment evidence, exception register
- Cadence: Continuous

**Tool Mappings:**
✅ Wiz — exploit path analysis answers "can an attacker reach this vulnerability"
✅ Qualys — SLA tracking, exception management
✅ Defect Dojo — open-source vulnerability management, SLA tracking
❌ CVSS-only prioritization — does not account for exploitability or asset criticality

**Verification:**
- SLA report: percentage of Critical findings remediated within 7 days. Target >90%.
- Any Critical findings older than 14 days without an approved exception? Escalate.
- Is the exception register reviewed monthly by the CISO?

**Common Mistakes:**
- Patching by CVSS score only. An internet-facing system with CVSS 7 is riskier than an air-gapped system with CVSS 10.
- No compensating controls for deferred patches. If you cannot patch, what is protecting the system until you can?
- Exception with no expiration date. Every exception must have a target closure date.

**If You Cannot Implement This:**
For OT environments (cannot patch within SLA): use perimeter controls, network segmentation, and application allowlisting as compensating controls. Document every deferred patch with the compensating control.

---

### 6.7 System and Information Integrity (SI)

---

### SI-1 Malware Protection — Tier: Core

**Statement:** Malware protection is deployed on all endpoints and servers. Signatures are updated automatically. Scans run on a defined schedule.

**For the IT Generalist:**
1. Deploy EDR on every endpoint and server. Not just antivirus — EDR detects behavior, not just signatures.
2. Configure automatic signature updates. The EDR should update within 24 hours of a new signature release.
3. Schedule scans: real-time scanning (file access) for all systems, full weekly scan for servers.
4. Configure alerting: malware detected → notify security team immediately.

*Windows Defender check:*
```powershell
Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled, RealTimeProtectionEnabled
```

**For the MSP:**
- EDR is standard per client. No client runs without endpoint protection.
- Centralized management console: monitor all client endpoints from a single pane.
- Weekly: review malware detection events. Monthly: report to client.

**For the Security Engineer:**
- Reference: NIST 800-53 SI-4 · PCI DSS Req 5.2 · ISO 27001 A.12.2.1
- Evidence: EDR coverage report, scan schedule, signature update evidence, malware detection log
- Cadence: Continuous

**Tool Mappings:**
✅ SentinelOne — autonomous EDR, AI-powered detection, rollback capability
✅ CrowdStrike Falcon — cloud-native, broad detection coverage, threat intelligence integration
✅ Microsoft Defender for Endpoint — included with many M365 licenses, deep Entra ID integration
◐ Sophos — adequate for mid-market, weaker on advanced threat detection
❌ Legacy antivirus (McAfee, Symantec endpoint) — signature-only, no behavioral detection

**Verification:**
- EDR coverage: what percentage of endpoints are reporting? Target >98%.
- Last signature update: all endpoints updated within the last 24 hours?
- Any malware detections in the last 7 days? Investigate all of them.

**Common Mistakes:**
- EDR on endpoints but not on servers. Servers are common ransomware targets.
- Real-time protection disabled for performance reasons. Use exclusions judiciously, not blanket exemptions.
- No response to EDR alerts. An EDR alert that nobody investigates is a blind spot.

**If You Cannot Implement This:**
At minimum, Windows Defender (included with Windows) provides real-time protection. For PCI DSS, EDR is not explicitly required but is expected by most QSAs.

---

### SI-2 File Integrity Monitoring — Tier: Core

**Statement:** Critical system files and configuration are monitored for unauthorized changes.

**For the IT Generalist:**
1. Identify critical files and directories to monitor: system binaries, configuration files, web application files, database files.
2. Configure FIM to alert on any modification to monitored files.
3. Review FIM alerts daily. Investigate changes: was it an approved change (patch, configuration update) or unauthorized?
4. For approved changes: document them in the change management system. For unauthorized changes: treat as a security incident.

*Wazuh FIM configuration:*
```xml
<syscheck>
  <directories check_all="yes">/etc,/usr/bin,/opt/app</directories>
  <frequency>43200</frequency>
  <alert_new_files>yes</alert_new_files>
</syscheck>
```

**For the MSP:**
- FIM on critical systems per client. Start with domain controllers, web servers, database servers.
- Daily FIM alert review. Approved changes are closed. Unauthorized changes are escalated.
- Per-client: whitelist known-good change patterns (Windows Updates, application patches).

**For the Security Engineer:**
- Reference: NIST 800-53 SI-7 · PCI DSS Req 11.5
- Evidence: FIM configuration, alert review log, change control evidence
- Cadence: Continuous (monitoring), Daily (review)

**Tool Mappings:**
✅ Wazuh — open-source FIM, configuration assessment, alerting
✅ Microsoft Defender for Cloud — File Integrity Monitoring for Azure VMs
◐ Tripwire — legacy FIM, functional but expensive per-agent
❌ No FIM on CHD — direct PCI DSS finding

**Verification:**
- FIM alert queue: any open alerts older than 24 hours?
- Last approved change: was the FIM change whitelisted or investigated?
- Any unauthorized file changes detected in the last 30 days? Investigated and closed?

**Common Mistakes:**
- Too many files monitored. 10,000 alerts per day means none get reviewed. Start with critical system paths and expand gradually.
- Alert tuning not maintained. New software installations create false positives if paths are not whitelisted.
- No whitelisting of approved change sources. Windows Update patches will trigger FIM alerts every Patch Tuesday unless whitelisted.

**If You Cannot Implement This:**
For non-CDE systems: manual integrity checks quarterly are acceptable. For PCI DSS CDE: automated FIM is required.

---

### SI-3 Anti-Phishing Controls — Tier: Core

**Statement:** Anti-phishing mechanisms are deployed to detect and block malicious email. Personnel are trained to report phishing.

**For the IT Generalist:**
1. Configure DMARC, SPF, and DKIM for your email domain. This prevents attackers from spoofing your domain in phishing emails.
2. Deploy an anti-phishing tool that scans email links and attachments.
3. Enable suspicious forwarding detection: alert when someone creates an auto-forwarding rule to an external address.
4. Run phishing simulations quarterly. Track who clicks and who reports.

*DMARC DNS record:*
```dns
_dmarc.example.com TXT "v=DMARC1; p=reject; rua=mailto:dmarc-reports@example.com; pct=100"
```

**For the MSP:**
- DMARC/SPF/DKIM setup is part of client onboarding. Do not skip it.
- Anti-phishing tool: Microsoft Defender for Office 365, Abnormal Security, or Proofpoint.
- Monthly phishing simulation for clients with >50 users.
- Users who click 3+ times in a year get additional training.

**For the Security Engineer:**
- Reference: PCI DSS Req 5.4.1
- Evidence: DMARC/DKIM/SPF configuration, phishing simulation results, training completion
- Cadence: Quarterly (simulations), Annual (training)

**Tool Mappings:**
✅ Microsoft Defender for Office 365 — safe links, safe attachments, anti-phishing policies
✅ Proofpoint — email security, threat isolation, simulation
✅ Abnormal Security — AI-based behavioral detection
◐ KnowBe4 — phishing simulation only, not email security
❌ No email security — phishing is the #1 initial access vector

**Verification:**
- DMARC check: email from your domain delivered to recipients who do not know you? DMARC=reject should block it.
- Phishing simulation results: click rate target <5%, report rate target >20%.
- Any auto-forwarding rules created in the last 30 days? Investigate.

**Common Mistakes:**
- DMARC set to p=none. "p=none" monitors only — it does not block spoofed email. Set p=quarantine or p=reject.
- Phishing simulation without training. Simulations without context create resentment, not awareness.
- Not monitoring auto-forwarding rules. Attackers who compromise a mailbox create a forwarding rule to exfiltrate data.

**If You Cannot Implement This:**
Start with DMARC/SPF/DKIM — these are free DNS records. For anti-phishing, Microsoft 365 Business Premium includes Defender for Office 365.

---

### 6.8 Supply Chain and Third-Party Risk (SR)

---

### SR-1 Vendor Risk Assessment — Tier: Core

**Statement:** Every vendor with access to organizational data or systems is assessed for security risk before onboarding and annually thereafter.

**For the IT Generalist:**
1. Create a vendor inventory: every company that has access to your data or systems.
2. For each vendor, get their security documentation: SOC 2 (Type II preferred), ISO 27001 certificate, or completed security questionnaire.
3. Review the documentation: what controls does the vendor have? Do they match your requirements?
4. If the vendor's controls are insufficient, document the gap and compensating controls.
5. Review each vendor annually. If their certification expires, get an updated one before the old one expires.

*Vendor tiering:*
```csv
Vendor,Service,Datal Risk,Assessment Type,Last Review,Next Review,Status
AWS,Cloud Infrastructure,High,SOC 2 + ISO 27001,2026-03-15,2027-03-15,Compliant
Acme SaaS,HR Platform,Medium,Questionnaire,2026-06-01,2027-06-01,Compliant
```

**For the MSP:**
- Vendor inventory per client. Most clients have no idea how many vendors have access to their systems.
- Annual vendor assessment cycle: quarter 1 = high-risk, quarter 2 = medium, quarter 3 = low, quarter 4 = follow-ups.
- Use a vendor risk platform (Whistic, OneTrust, UpGuard) to automate assessment collection.

**For the Security Engineer:**
- Reference: NIST 800-53 SA-9, SR-2 · PCI DSS Req 12.8
- Evidence: Vendor inventory, assessment reports, contracts with security clauses
- Cadence: Continuous (inventory), Annual (assessment)

**Tool Mappings:**
✅ Whistic — vendor assessment automation, SOC 2 collection, risk scoring
✅ OneTrust Vendor Risk Management — integrated with broader GRC platform
◐ UpGuard — external rating, vendor discovery, breach detection
❌ Spreadsheet-only vendor management — not sustainable past 10 vendors

**Verification:**
- How many vendors have access to your data? Is every one assessed?
- Any vendor whose assessment is overdue? Flag.
- Any high-risk vendor without a current SOC 2 or equivalent?

**Common Mistakes:**
- Assessing only the vendors you pay. SaaS vendors you use for free also have access to your data. Inventory them.
- Accepting a SOC 2 Type I (point-in-time) when Type II (12-month testing window) is available. Always prefer Type II.
- No contract review. The assessment is useless if the contract does not require the vendor to maintain those controls.

**If You Cannot Implement This:**
Start with a vendor inventory spreadsheet. Prioritize: first assess vendors that store or process your data (not just transmit). Questionnaire templates exist in practice-assets.

---

### SR-2 Supply Chain Security — Tier: Core

**Statement:** Software and hardware acquired from third parties is assessed for supply chain integrity.

**For the IT Generalist:**
1. For every software vendor, request an SBOM (Software Bill of Materials). This tells you what open-source components are in their product.
2. Review the SBOM for known vulnerabilities. Use a tool (Trivy, Snyk, Dependency-Track) to automate this.
3. Require vendors to attest that their software is built from a secure CI/CD pipeline.
4. If the vendor cannot provide an SBOM, document the exception and assess the risk.

*Trivy SBOM scan:*
```bash
trivy sbom vendor-sbom.json --severity HIGH,CRITICAL
```

**For the MSP:**
- SBOM collection is part of the vendor assessment process.
- Dependency-Track is free, open-source, and automates SBOM analysis.
- Quarterly: re-scan vendor SBOMs for new vulnerabilities.

**For the Security Engineer:**
- Reference: NIST 800-53 SR-3 · PCI DSS Req 12.8.2
- Evidence: SBOM inventory, vulnerability scan results, vendor attestation
- Cadence: Annual (initial assessment), Quarterly (re-scan)

**Tool Mappings:**
✅ Dependency-Track — open-source SBOM analysis, continuous monitoring
✅ Snyk — SBOM import, vulnerability scanning, fix advice
✅ Trivy — SBOM generation and scanning (free)
❌ No SBOM collection — supply chain risk is invisible

**Verification:**
- Do your top 10 software vendors have current SBOMs?
- Are there any known critical CVEs in vendor software components?
- For vendors without SBOM: what compensating controls are in place?

**Common Mistakes:**
- Asking for an SBOM from vendors who have never produced one. Provide guidance: "Can you run `cyclonedx-bom` on your build?"
- Not re-scanning after a new CVE is published. SBOMs are not static — subscribe to vulnerability alerts for your critical vendors.
- Accepting SBOMs without verification. A vendor can claim their product has no vulnerabilities. The SBOM is the evidence.

**If You Cannot Implement This:**
For vendors that cannot produce SBOMs: document the exception and require contractual indemnification. For in-house software: generate your own SBOMs from your build pipeline.

---

### 6.9 System and Communications Protection (SC)

---

### SC-1 Network Segmentation — Tier: Core

**Statement:** Networks are segmented into security zones. Traffic between zones is explicitly approved, documented, and logged.

**For the IT Generalist:**
1. Identify your network zones: user LAN, server LAN, DMZ, OT network, guest Wi-Fi.
2. Configure firewall rules that explicitly allow only required traffic between zones. Deny everything else.
3. Document the segmentation: a network diagram showing each zone, the firewall between them, and the allowed traffic.
4. Review firewall rules every 6 months. Remove rules that are no longer needed.

*Windows Firewall: List all inbound rules:*
```powershell
Get-NetFirewallRule -Direction Inbound | Where-Object Enabled -eq $true |
  Select-Object DisplayName, Action, Direction
```

**For the MSP:**
- Segmentation is per-client. Minimum zones: corporate, guest, management, DMZ.
- Firewall rule review every 6 months is included in managed services.
- Cloud segmentation: use VPCs, security groups, and network ACLs. Same principles, different implementation.

**For the Security Engineer:**
- Reference: NIST 800-53 SC-7 · PCI DSS Req 1.2 · ISO 27001 A.13.1.3
- Evidence: Network diagram, firewall rule review, cloud security group export, segmentation test results
- Cadence: Quarterly (review), Every 6 months (rule review)

**Tool Mappings:**
✅ Azure Firewall / AWS Network Firewall — cloud-native NGFW
✅ pfSense / OPNsense — open-source, suitable for SMB
✅ Cisco / Palo Alto — enterprise NGFW, threat prevention
❌ Flat network with no segmentation — security finding, direct PCI DSS violation

**Verification:**
- Can a host in the user LAN directly reach a host in the OT network? Should be blocked.
- Internet-facing firewall rules: are they reviewed? Any rule with a source of "Any" and destination of "Any"?
- Segmentation test: quarterly try to reach the CDE from a non-CDE system. Should fail.

**Common Mistakes:**
- Flat network "for simplicity." A flat network means one compromise is a full compromise. Segment.
- Firewall rules that allow "Any-Any" for convenience. Every "Any-Any" rule needs documented business justification.
- Cloud security groups too permissive. Default-deny for all new security groups. Add rules only as needed.

**If You Cannot Implement This:**
At minimum, segment the CDE (PCI) or CUI enclave (CMMC) from the corporate network. For non-regulated environments, separate user and server traffic.

---

### SC-2 Data in Transit Encryption — Tier: Core

**Statement:** Sensitive data and administrative traffic are encrypted in transit using approved protocols.

**For the IT Generalist:**
1. Enable HTTPS on every web server and application. Use TLS 1.2 or 1.3.
2. Redirect HTTP to HTTPS. Do not allow unencrypted HTTP.
3. Disable TLS 1.0 and 1.1. These are deprecated and insecure.
4. Use approved cipher suites: TLS_AES_256_GCM_SHA384 (TLS 1.3) or ECDHE-RSA-AES256-GCM-SHA384 (TLS 1.2).
5. Scan your certificates: check for expired, about-to-expire, or revoked certificates.

*TLS certificate check:*
```bash
openssl s_client -connect example.com:443 -servername example.com < /dev/null 2>/dev/null |
  openssl x509 -noout -dates -subject -issuer
```

**For the MSP:**
- SSL/TLS is standard per client. Enable by default for all services.
- Certificate expiration monitoring: 30-day alert before expiration.
- TLS scan: quarterly check all client domains for TLS version and certificate validity.

**For the Security Engineer:**
- Reference: NIST 800-53 SC-8 · PCI DSS Req 4.2.1
- Evidence: TLS scanner report, certificate validation evidence, cipher suite configuration
- Cadence: Continuous (certificate monitoring), Quarterly (full scan)

**Tool Mappings:**
✅ Qualys SSL Labs — free TLS scanner, certificate analysis
✅ Azure Front Door / AWS CloudFront — TLS termination, certificate management
✅ Let's Encrypt — free automated certificates, 90-day rotation
❌ TLS 1.0 or 1.1 in use — PCI DSS violation, known vulnerabilities

**Verification:**
- Run an external TLS scan: any services still running TLS 1.0 or 1.1?
- Certificate expiration: any certificates expiring within 30 days?
- Cipher strength: any weak ciphers enabled (RC4, DES, 3DES)?

**Common Mistakes:**
- TLS termination at the load balancer but internal traffic is unencrypted. Encrypt from load balancer to application server too.
- Self-signed certificates for internal services without proper CA management. Use a private CA or cert-manager.
- Wildcard certificates for everything. Reduces security — a compromise of one affected system exposes all.

**If You Cannot Implement This:**
PCI DSS Req 4.2.1 requires strong cryptography for CHD over open/public networks. No compensating control is accepted for CDE scope.

---

### SC-3 Data at Rest Encryption — Tier: Core

**Statement:** Sensitive data at rest is encrypted using approved methods. Disk encryption alone is insufficient for regulated data — it must be combined with column-level or application-level encryption.

**For the IT Generalist:**
1. Enable disk encryption on all servers and endpoints: BitLocker (Windows), LUKS (Linux), FileVault (Mac).
2. For databases containing sensitive data (PII, PHI, CHD): enable Transparent Data Encryption (TDE) or column-level encryption.
3. For cloud storage: enable server-side encryption (SSE) with customer-managed keys (CMK).
4. Document which data is encrypted at rest and which encryption method is used.

*Azure Disk Encryption:*
```azurecli
az vm encryption enable --resource-group rg-prod --name vm-prod --disk-encryption-keyvault kv-prod
```

**For the MSP:**
- Disk encryption is standard per client. Enabled by default on all devices.
- Database encryption: enable for any database that stores sensitive data.
- Cloud storage encryption: enable SSE with CMK. Default encryption is not sufficient for regulated data.

**For the Security Engineer:**
- Reference: NIST 800-53 SC-28 · PCI DSS Req 3.4
- Evidence: Encryption configuration, KMS key inventory, key rotation records
- Cadence: Quarterly

**Tool Mappings:**
✅ Azure Disk Encryption / BitLocker — full disk encryption, integration with Azure Key Vault
✅ AWS EBS Encryption + KMS — automatic encryption for new volumes
✅ LUKS — Linux full disk encryption
❌ Disk encryption without key management — encrypted volume with the key stored on the same machine

**Verification:**
- Can you view an unmounted disk from a stopped VM? If disk encryption is enabled, you should not be able to read the data without the key.
- TDE enabled on all databases marked high-criticality?
- CMK rotation: keys rotated at least annually?

**Common Mistakes:**
- Disk encryption but database data is not encrypted. TDE is separate from disk encryption — both are needed.
- CMK stored in the same subscription as the data. Store keys in a separate subscription, separate tenant.
- Encryption key access not logged. Who accessed the key to decrypt the database?

**If You Cannot Implement This:**
PCI DSS Req 3.4 requires PAN rendered unreadable. Disk encryption alone is explicitly insufficient — must combine with truncation, hashing, tokenization, or column-level encryption.

---

### 6.10 Assessment and Authorization (CA)

---

### CA-1 Control Self-Assessment — Tier: Core

**Statement:** Controls are assessed annually for design and operating effectiveness. Findings are tracked to closure.

**For the IT Generalist:**
1. Create a control checklist: each control from this document, with a place to mark: Designed (Y/N), Operating (Y/N), Evidence (Y/N).
2. Walk through each control. Is it designed? Is it operating? Is there evidence?
3. For controls missing design: create a plan.
4. For controls not operating: investigate why and fix it.
5. For controls without evidence: collect the evidence or create a process to produce it.

*Assessment template:*
```csv
Control ID,Designed?,Operating?,Evidence?,Finding,Risk,Target,Owner
AC-2,Yes,Yes,Yes,N/A,Low,N/A,IT Manager
AC-4,Yes,Partially,No,PAM not deployed for all admin accounts,High,2026-09-01,Security Engineer
```

**For the MSP:**
- Annual control self-assessment per client. Quarter 1: assess. Quarter 2-4: remediate.
- Use the CERG assessment template. Report results to client leadership.
- Assessment is included in standard managed services.

**For the Security Engineer:**
- Reference: NIST 800-53 CA-2 · ISO 27001 A.9.1 (internal audit)
- Evidence: Completed assessment worksheet, findings register, improvement register
- Cadence: Annual

**Tool Mappings:**
✅ CERG self-assessment template + practice-assets templates
◐ GRC tool (OneTrust, ServiceNow GRC) — automated assessment workflows
❌ No assessment — cannot prove controls operate

**Verification:**
- When was the last control self-assessment? Within the last 12 months?
- Are findings from the last assessment tracked in the improvement register?
- What percentage of findings were remediated within the target timeline? Target >80%.

**Common Mistakes:**
- Assessment without evidence. "Operating? Yes. Evidence? Will collect later." No. Evidence must be collected at assessment time.
- Findings without owners. An unowned finding is an unfixed finding.
- Self-assessment without independent validation. At least once every 3 years, have someone outside the control owner verify.

**If You Cannot Implement This:**
Use the control checklist in §6 of this document. Walk through each control one at a time. "Yes" means you have evidence. "No" means you have a finding. This is the minimum.

---

### 6.11 Awareness and Training (AT)

---

### AT-1 Security Awareness Training — Tier: Core

**Statement:** All personnel complete role-appropriate security training before access and annually thereafter.

**For the IT Generalist:**
1. Use a security awareness training platform (KnowBe4, M365 Training, SANS).
2. Assign the standard curriculum to all new hires: phishing awareness, password hygiene, data handling, incident reporting.
3. Assign additional modules for high-risk roles: developers (secure coding), finance (wire fraud), IT (privileged access).
4. Track completion. Send reminders to non-completers. Escalate persistent non-compliance to management.

*Training assignment in M365:*
```powershell
# Create training assignment for all users
New-MgIdentityConditionalAccessPolicy -DisplayName "Security Training for All Users"
```

**For the MSP:**
- Security awareness training is standard per client. Recommended platform: KnowBe4.
- Monthly phishing simulation for clients with >50 users.
- Quarterly report: training completion rate by client.

**For the Security Engineer:**
- Reference: NIST 800-53 AT-2 · PCI DSS Req 12.6
- Evidence: Training completion records, phishing simulation results, role-specific curriculum
- Cadence: Annual (training), Monthly (phishing sim)

**Tool Mappings:**
✅ KnowBe4 — phishing simulation, compliance tracking, role-specific content
✅ M365 Training — included with many M365 licenses, basic awareness
◐ SANS Securing the Human — high-quality content, expensive per-seat
❌ No security awareness training — PCI DSS violation

**Verification:**
- Training completion rate: target >95% within the assigned period.
- Phishing click rate: target <5% for first simulation, decreasing year over year.
- Role-specific training: developers completed secure coding? Finance completed wire fraud awareness?

**Common Mistakes:**
- Generic training for everyone. Role-specific training is required for PCI and CMMC.
- Training assigned but not enforced. Users who do not complete training within 30 days get escalated.
- Phishing simulation results not acted upon. Users who click 3+ times need direct coaching, not just reminders.

**If You Cannot Implement This:**
At minimum: create a security awareness presentation (30 minutes) and present it annually. Document attendance. For PCI DSS, a formal training program with phishing simulation is expected.

---

### 6.12 Incident Response (IR)

---

### IR-1 Incident Response Plan — Tier: Core

**Statement:** A documented incident response plan exists, is tested annually, and is accessible to all response team members.

**For the IT Generalist:**
1. Create a one-page incident response document: what to do when something is wrong.
2. Include: who to call first, how to contain the incident, how to preserve evidence, who to notify (internal, regulatory, customers).
3. Keep the document accessible offline. If your systems are down, you need the plan on paper or local device.
4. Run a tabletop exercise annually: gather the team and walk through a scenario (ransomware, data breach, phishing compromise).

*IR plan minimum content:*
```markdown
1. Detection: How do we find out something happened? (SIEM alert, user report, partner notification)
2. Triage: Is this a confirmed incident or a false alarm?
3. Contain: Disconnect affected systems from the network. Do not shut down — you lose forensic data.
4. Investigation: What happened? What systems are affected? What data was accessed?
5. Eradication: Remove the attacker's access.
6. Recovery: Restore from clean backup.
7. Notification: Who needs to know? (Legal, PR, regulators, law enforcement, affected parties)
8. Lessons Learned: What did we do well? What would we do differently?
```

**For the MSP:**
- IR plan template per client. Customize: client systems, client contacts, client notification requirements.
- Annual tabletop exercise with the client. 2-hour session, facilitator from your team.
- Plan updates: after any real incident, update the plan with lessons learned.

**For the Security Engineer:**
- Reference: NIST 800-53 IR-8 · ISO 27001 A.16.1.1 · PCI DSS Req 12.10.1
- Evidence: Approved IR plan, playbook set, exercise records, after-action reports
- Cadence: Annual (review + exercise), After any incident (update)

**Verification:**
- When was the IR plan last reviewed? Within the last 12 months?
- When was the last tabletop exercise? Documented outcomes?
- Can every IR team member access the plan without logging into the corporate network?

**Common Mistakes:**
- Plan is 50 pages. Brevity wins in incident response. One page per phase. Focus on contact info, containment steps, and notification requirements.
- Plan written but never tested. An untested plan will fail.
- Plan stored on the internal share that is unreachable when the network is down. Keep a printed or offline copy.

**If You Cannot Implement This:**
Create a 2-page document. Page 1: who to call, in order. Page 2: what to do first (disconnect, preserve evidence, call legal). Review it with your team annually. This is the minimum.

---

### IR-2 Incident Detection and Triage — Tier: Core

**Statement:** Security incidents are detected through automated monitoring, triaged within defined timeframes, and tracked to closure.

**For the IT Generalist:**
1. Configure detection rules in your SIEM/EDR for common attack patterns: ransomware behavior, lateral movement, privilege escalation, data exfiltration.
2. When an alert fires: verify it first (is it a real incident or a false positive?). If real, open an incident ticket.
3. Triage SLA: Critical (active ransomware, data exfiltration) within 15 minutes. High (suspected compromise) within 1 hour. Medium within 4 hours.
4. Document: what happened, what you found, what you did, when you closed it.

**For the MSP:**
- 24/7 SOC monitoring is standard for managed security clients.
- Triage SLA documented in the MSA. Alerts that cannot be triaged within SLA escalate to the client.
- Client notification: confirmed incidents within 1 hour. Suspicious events within 4 hours.

**For the Security Engineer:**
- Reference: NIST 800-53 IR-4 · PCI DSS Req 12.10.1
- Evidence: Incident case records, triage SLA dashboard, detection rule inventory
- Cadence: Continuous

**Tool Mappings:**
✅ SentinelOne — autonomous detection + response, rollback capability
✅ Microsoft Sentinel — SIEM + SOAR, detonation chambers
✅ CrowdStrike Falcon — EDR + threat intelligence, adversary tracking
❌ No detection capability — incident response starts when the attacker decides to notify you

**Verification:**
- Mean time to detect (MTTD): how long between compromise and detection? Target <24 hours.
- Mean time to respond (MTTR): how long between detection and containment? Target <1 hour.
- False positive rate: what percentage of alerts turn out to be non-incidents? Target <30%.

**Common Mistakes:**
- Alert fatigue: too many low-severity detections. Prune and tune quarterly.
- No documented incident timeline. Without a timeline, you cannot measure or improve MTTD/MTTR.
- Containment without evidence preservation. Disconnecting the server is containment, but take a forensic image first.

**If You Cannot Implement This:**
For very small teams: use your SIEM's built-in detection rules (Sentinel has 200+ templates). Review alerts daily. Outsource to an MSSP/MDR if you cannot staff 24/7.

---

### 6.13 Physical and Environmental Security (PE)

---

### PE-1 Physical Access Control — Tier: Core

**Statement:** Physical access to facilities housing sensitive systems is authorized, logged, and audited.

**For the IT Generalist:**
1. Maintain a list of who has physical access to server rooms, network closets, and CUI work areas.
2. Use badge access or equivalent. Keep a log of entries.
3. Require visitor escort. Log all visitors: name, company, purpose, time in, time out.
4. Review access logs monthly. Flag entries outside business hours or by unauthorized personnel.
5. Retain access logs for at least 90 days (PCI) or per applicable regulatory requirement.

**For the MSP:**
- Physical access control is client-managed. The MSP should not have physical access to client facilities.
- If the MSP has remote hands at a colocation facility, those personnel are included in the client's access list.

**For the Security Engineer:**
- Reference: NIST 800-53 PE-2, PE-3 · PCI DSS Req 9.1.1
- Evidence: Badge access roster, visitor logs, access log review evidence
- Cadence: Monthly (log review), Quarterly (access list review)

**Verification:**
- Access log review: any entries from unauthorized individuals?
- Visitor log: any visitors without a named escort?
- Badge access list: any former employees still on the access list?

**Common Mistakes:**
- Badge access list not reconciled against HR records. Former employees still have badge access.
- No visitor log. Escorting visitors is pointless if there is no record.
- Server room door propped open for convenience. This bypasses every physical access control.

**If You Cannot Implement This:**
At minimum: a lock on the server room door and a logbook for visitors. Key control: document who has keys.

---

### 6.14 Planning and Program Management (PL/PM)

---

### PL-1 Policy and Standards Lifecycle — Tier: Core

**Statement:** Security policies, standards, and procedures are maintained with named owners, review dates, and version control.

**For the IT Generalist:**
1. Store all security documents in a central location (SharePoint, Confluence, Git repository).
2. Each document has: document ID, title, owner, version number, last review date, next review date.
3. Set calendar reminders for upcoming reviews. Update documents when things change.
4. When a document is updated, notify stakeholders of the change.

**For the MSP:**
- Document library per client. Template documents across clients.
- CERG corpus is the source of truth. The client's rendered copy is their authoritative version.

**For the Security Engineer:**
- Reference: NIST 800-53 PL-1 · ISO 27001 A.5.1
- Evidence: Document catalog, review records, approval history
- Cadence: Annual (full review), Ongoing (updates)

**Tool Mappings:**
✅ Git repository (GitHub, GitLab, Azure Repos) — version control, change history, PR review
✅ SharePoint — document management, version history, approval workflows
❌ Unversioned network drive — no history, no review tracking, no accountability

**Verification:**
- Document catalog: is every required document listed with a current review date?
- Can you see the change history for any document in the last 12 months?
- Are there any documents past their review date without a documented extension?

**Common Mistakes:**
- Documents without owners. An unowned document is an unmaintained document.
- Documents past their review date. Set reminders 30 days before the due date.
- "Review" means rereading without making changes. That is still a review. Document it.

**If You Cannot Implement This:**
Start with a spreadsheet listing your documents. Owner, location, review date, status. Review one per week until you catch up.

---

### PM-1 Metrics and Reporting — Tier: Core

**Statement:** Security program metrics are defined, tracked, and reported to leadership on a regular cadence.

**For the IT Generalist:**
1. Choose 5 metrics that matter to your organization: vulnerability SLA compliance, phishing click rate, access review completion rate, MTTD, MTTR.
2. Track them monthly. Use your existing tools (SIEM, scanner, IdP) as data sources.
3. Create a one-page dashboard: current value, target, trend (improving/declining).
4. Present the dashboard to leadership quarterly.

**For the MSP:**
- Monthly security dashboard per client. 5 metrics minimum.
- Dashboard is included in managed services. Presented during the quarterly business review.

**For the Security Engineer:**
- Reference: NIST 800-53 PM-14
- Evidence: Metric definitions (MTR-001), dashboard, quarterly report
- Cadence: Monthly (tracking), Quarterly (reporting)

**Verification:**
- Dashboard exists. Can you explain every metric? Is there a target value for each?
- Are metrics trending in the right direction? If not, what is the plan?

**Common Mistakes:**
- Vanity metrics (number of alerts processed, number of tickets closed). Use outcome metrics (vulnerability SLA compliance, access review completion).
- Dashboard for the dashboard's sake. If you do not review it regularly, stop producing it.
- No targets. A metric without a target is noise. "Vulnerability SLA is 85%" — 85% of what? What is the target?

**If You Cannot Implement This:**
Start with 3 metrics: vulnerability SLA compliance, MFA registration rate, risk register open items. Track in a spreadsheet. Report to your manager monthly.

---

### 6.15 Personnel Security (PS)

---

### PS-1 Background Screening — Tier: Core

**Statement:** Personnel with access to sensitive systems or data undergo background screening before access is granted.

**For the IT Generalist:**
1. Work with HR to define screening requirements per role: standard (background check) for all personnel, enhanced (criminal history, credit check) for financial/privileged roles.
2. Verify screening results before granting access to production systems.
3. For contractors: verify that the contracting agency has performed equivalent screening.
4. Retain screening records per applicable regulatory requirement.

**For the MSP:**
- Screening is client-managed through HR. The MSP should verify that client screening covers anyone with privileged access.
- For MSP employees: the MSP performs its own screening per MSA requirements.

**For the Security Engineer:**
- Reference: NIST 800-53 PS-2 · ISO 27001 A.7.1
- Evidence: Screening policy, verification records, exception register
- Cadence: Before access grant; then at defined intervals per role

**Verification:**
- Every person with production access has a screening record?
- Any person whose screening is overdue for the required re-check frequency?
- Screening exceptions documented with compensating controls?

**Common Mistakes:**
- Screening completed but access granted before results are received. Screen first, then grant access.
- Contractors screened by agency but agency screening does not meet your requirements. Verify the screening level.
- Screening records not retained. Keep records for the duration of employment plus regulatory retention period.

**If You Cannot Implement This:**
At minimum, verify identity and right-to-work. For regulated environments (PCI, CMMC, NERC-CIP), formal background screening is required.

---

### 6.16 System and Services Acquisition (SA)

---

### SA-1 Security in Procurement — Tier: Core

**Statement:** Security requirements are included in procurement contracts for all technology acquisitions.

**For the IT Generalist:**
1. For any technology purchase that handles company data, include security requirements in the contract.
2. Minimum requirements: data protection (encryption), breach notification timeline (e.g., 72 hours), right to audit (SOC 2 or equivalent), data return/deletion at contract end.
3. Work with procurement/legal to include these requirements in standard contract language.
4. For free/open-source tools: review the license terms for data handling provisions.

**For the MSP:**
- Standard security clauses for client procurement. Provide the language to the client's procurement team.
- Vendor assessment (SR-1) feeds into procurement decisions. Do not approve a vendor that cannot meet security requirements.

**For the Security Engineer:**
- Reference: NIST 800-53 SA-9 · PCI DSS Req 12.8.2
- Evidence: Contract security clauses, vendor assessment reports
- Cadence: Per procurement event; Annual for existing contracts

**Verification:**
- Do your top 10 vendors' contracts include breach notification obligations?
- Do your contracts include right-to-audit provisions?
- Are there vendors with access to your data but no signed contract?

**Common Mistakes:**
- Procurement bypasses security. "We already bought it." Security requirements must be part of the RFP, not added after the contract is signed.
- Contract reviewed by legal but not by security. Legal checks liability; security checks data protection. Both are needed.
- "Free tier" vendors not assessed. Free software still handles your data. Assess it.


---

## 7. Compensating Control Catalog

When a Core control cannot be fully implemented, a compensating control may be used. This catalog documents acceptable compensating controls per control family, with notes on regulatory acceptability.

### How to Use This Catalog

1. Identify the control you cannot implement.
2. Review the compensating control options below.
3. Document: which control is not implemented, why, which compensating control is in place, how it is evidenced, the approval authority, and the expiration date.
4. Obtain approval per the RMF-001 section 9.7 authority table.
5. Track in the risk register with a target date for implementing the primary control.

### Compensating Control Rules

| Rule | Detail |
|---|---|
| Must meet or exceed the original control intent | If AC-4 (least privilege) cannot be implemented because PAM is not deployed, the compensating control must prevent privilege abuse. A log of who has admin access is not sufficient. |
| Must have evidence | Same evidence requirements as the primary control. "We trust our users" is not a compensating control. |
| Must have an expiration date | All compensating controls are temporary. Target date to implement the primary control is documented. |
| Regulatory exceptions | PCI DSS allows compensating controls only if: (1) meets the intent and rigor, (2) above and beyond other controls, (3) commensurate with risk, (4) reviewed annually by the QSA. CMMC does not allow compensating controls for Level 2. NERC-CIP allows deviations with documented mitigation plans. |

### By Control Family

| Control | Acceptable Compensating Control | Regulatory Acceptability |
|---|---|---|
| AC-2 (Account Lifecycle) | Manual JML process with weekly reconciliation spreadsheet | Not accepted for CMMC L2 or SOX ITGC |
| AC-4 (Least Privilege) | JIT access via IdP without full PAM (Entra PIM, Okta) | Accepted for all frameworks if JIT + session logging |
| AC-5 (Failed Auth) | Rate limiting at application layer instead of IdP lockout | Accepted for all frameworks |
| AC-6 (Remote Access) | Cloud-delivered remote access (Entra App Proxy, Cloudflare ZT) instead of VPN | Accepted for all frameworks |
| AU-1 (Audit Logging) | Centralized logging for critical systems only. Non-critical: monthly manual collection | Not accepted for PCI CDE |
| AU-2 (Log Review) | Weekly manual log review instead of daily automated | Accepted for non-regulated. Not for PCI CDE |
| CM-1 (DISH Baseline) | CIS benchmark applied manually, quarterly compliance checks | Not accepted for CMMC L2 |
| CP-1 (Backup) | Object storage immutability without backup tool. Manual scripts | Accepted if immutability and retention met |
| IA-1 (MFA) | SMS-based MFA where authenticator app not supported | Not accepted by NIST SP 800-63B |
| IA-3 (Service Accounts) | Passwords in password manager instead of enterprise vault | Accepted if rotation documented |
| RA-2 (Vulnerability Scanning) | Manual vulnerability assessment quarterly | Not accepted for PCI CDE (ASV required) |
| SC-1 (Segmentation) | Micro-segmentation at host firewall level | Accepted if centrally managed |
| SI-1 (Malware Protection) | Windows Defender for small environments | Accepted if cloud-delivered protection enabled |

---

## 8. Reference Tool Stack

### Per-Domain Recommendations

| Domain | Primary | Acceptable Alternatives | Avoid |
|---|---|---|---|
| Cloud Security (CSPM/CNAPP) | Wiz | Prisma Cloud, Defender for Cloud, Lacework | Homegrown scripts only |
| Endpoint Detection & Response | SentinelOne | CrowdStrike, Defender for Endpoint, Cortex XDR | Legacy AV (McAfee, Symantec) |
| Identity & Access Mgmt | Entra ID (Azure AD) | Okta, Ping, JumpCloud | On-prem AD with no cloud bridge |
| Privileged Access Mgmt | CyberArk | Delinea, Entra PIM, StrongDM | Shared passwords in spreadsheet |
| SIEM / Log Management | Microsoft Sentinel | Splunk, Wazuh, Chronicle | ELK without dedicated engineer |
| Vulnerability Mgmt | Wiz (cloud), Qualys (hybrid) | Tenable, Rapid7, Defect Dojo | Brinqa, Kenna |
| Backup / Recovery | Veeam | Rubrik, Cohesity, Commvault | Tape-only, no immutability |
| Configuration Hardening | DISH (CIS + overrides) | AWS Config, Azure Policy, GCP Org Policies | Manual baselines, no drift detection |
| Container Security | Wiz | Aqua, Prisma Cloud, Trivy + Harbor | No container scanning in registry |
| IaC Scanning | Checkov | Terrascan, Snyk IaC, tfsec | Manual PR review as only control |
| Secrets Management | HashiCorp Vault | AWS Secrets Manager, Azure Key Vault, GCP Secret Manager | .env files in git |
| Asset Inventory | Device42 | ServiceNow CMDB, AirTable (<500 assets), Snipe-IT | Spreadsheet-only, no discovery |
| Vendor Risk Mgmt | Whistic | OneTrust, UpGuard, manual questionnaire | No process at all |
| Phishing Simulation | Microsoft Defender for Office 365 | KnowBe4, Proofpoint | No simulation at all |
| Automation / SOAR | Splunk SOAR | Tines, Torq, Sentinel Playbooks | Homegrown scripts without runbook |

---

## 9. Inheritance Model

`Inherited` controls require an Inheritance Evidence Package. Without it, the control defaults to `Not Implemented`.

### Package Elements

1. **Provider attestation** — current SOC 2 Type II / ISO 27001 / FedRAMP / PCI report.
2. **Shared responsibility mapping** — the SRM section naming this control as the provider's.
3. **Customer-side configuration evidence** — proof customer-side prerequisites are configured.
4. **Sub-service organization carve-outs** — dependency notation.
5. **Currency check** — attestation expiry date and renewal calendar entry.
6. **Re-papering trigger** — what would cause re-evaluation.

### Inheritance Examples

| Scenario | Inherited? | What You Still Need |
|---|---|---|
| Physical security of cloud data center | Yes — provider attestation | Confirm data center scope covers your region |
| IAM for SaaS application | No — customer manages identity | Customer-side MFA, lifecycle, recertification |
| Network segmentation in AWS VPC | No — customer designs VPC | Customer network architecture, security groups |
| Backup of SaaS data (M365, Salesforce) | No — provider has limited backup | Customer-side backup tool |

---

## 10. Overlay Matrix

| Overlay | Applies To | Adds / Tightens | Source Package |
|---|---|---|---|
| High-Impact | Material business/safety impact | Tighter SLAs, CIS L2 baseline, expanded monitoring | DISH + STD-LM-001 |
| CUI | Systems handling CUI | NIST 800-171 controls, SSP + POA&M + SPRS, FIPS crypto | STD-CUI-001 + PLN-CUI-001 |
| BES | Medium/High BES Cyber Systems | NERC-CIP, ESP/EAP, 90-day searchable retention | STD-OT-001 + PLN-CIP-001 |
| SOX ITGC | Financial reporting systems | Access, change, operations, backup ITGCs | PLN-SOX-001 |
| PCI DSS | Cardholder data environment | 30 PCI controls (PC-01 through PC-30), ASV scans | PLN-PCI-001 |
| OT Safety | OT with safety impact | Stricter change windows, no active scanning | STD-OT-001 |
| AI | AI services and systems | AI intake, model inventory, prompt injection testing | STD-AI-001 + TMPL-AI-001/002/003 |

---

## 11. Evidence Automation

### Automation Patterns

| Pattern | When to Use | Example |
|---|---|---|
| Scheduled export | Periodic snapshot from tool API | Weekly IdP account export to compare to HR roster |
| API-based verification | On-demand via API call | CSPM API to check cloud compliance |
| CI/CD pipeline gate | Produced during deployment | IaC scan result attached to deployment ticket |
| SIEM query | Exists in log data | KQL query saved to evidence library |

### Evidence Library Structure

```yaml
evidence_items:
  - control: AC-2
    name: "Monthly Account Inventory Export"
    automation: "EntraID-Inventory-Export.ps1"
    schedule: "1st of every month"
    output: "CSV with account UPN, created date, last login, department, manager"
    validation: "Row count should not fluctuate >5% month-over-month without documented change"
  - control: CM-1
    name: "DISH Drift Detection Report"
    automation: "DISH-Drift-Scan.ps1"
    schedule: "Daily (automated), weekly (human review)"
    output: "List of drifted resources with delta from baseline"
```

Full automation script library at `practice-assets/scripts/evidence-automation/`.

---

## 12. Framework Alignment (Capability Map)

### Capability-to-Control Mapping

| Capability | Controls | Primary Standard |
|---|---|---|
| See Everything: Asset Discovery | CM-4, RA-2 | STD-AM-001 |
| Fix What Matters: Exposure Remediation | RA-2, RA-3 | PRC-VM-001 |
| Lock Down Access: Least Privilege | AC-2, AC-3, AC-4, IA-1, IA-2 | STD-AC-001 |
| Verify Every Request: Authentication | IA-1, IA-2, IA-3, AC-5 | STD-AC-001 |
| Lock Every System: Hardening | CM-1, CM-3, SI-1 | STD-CFG-001 (DISH) |
| Encrypt Everything: Data Protection | SC-2, SC-3 | STD-CR-001 |
| Divide and Protect: Segmentation | SC-1 | STD-NET-001 |
| Trust but Verify: Vendor Risk | SR-1, SR-2 | PRC-TPRM-001 |
| Watch Every Move: PAM | AC-4, AC-6 | STD-AC-001 |
| Attack Yourself: Pen Testing | CA-2 | PRC-AV-001 |
| Build Human Defenses: Training | AT-1 | GOV-TRN-001 |
| Govern with Purpose: Policy | PL-1, PM-1 | GOV-CAT-001 |
| Control Every Change: Change Mgmt | CM-2, CM-3 | PRC-CHG-001 |
| Prove Everything: Evidence | CA-1, AU-1, AU-2 | PRC-AUD-001 |
| Measure What Matters: Metrics | PM-1 | GOV-MTR-001 |
| Decide with Data: Risk Mgmt | RA-1 | PRC-RM-001 |
| Secure the Perimeter: Physical | PE-1 | STD-OT-001 |
| See the Attack: Detection | SI-1, SI-2, SI-3, IR-2 | STD-LM-001 |
| Be Ready: Incident Response | IR-1, IR-2 | PLN-IR-001 |
| Come Back Fast: Recovery | CP-1, CP-2 | STD-RES-001 |
| Automate Identity: Lifecycle | AC-2, IA-3 | STD-AC-001 |
| Stay Ahead: Compliance Cadence | CA-1, PL-1 | GOV-CAL-001 |

---

## 13. Governance, Change, and Versioning

### Ownership

The Governance Pillar Leader owns this baseline. Material changes (additions, removals, parameter changes) require CISO approval. Non-material changes (clarifications, typo fixes) require Governance Pillar Leader approval.

### Versioning

| Bump | When | Examples |
|---|---|---|
| Major (3.0) | Restructure, family addition or removal | 3.0 initial Core 100 controls |
| Minor (3.x) | New control, new overlay parameter, evidence change | Adding new detection control |
| Patch (3.0.x) | Clarification, fix cross-reference | Typo fix, link update |

### Change Triggers

- Framework version change (NIST 800-53 rev, CIS rev, etc.)
- Regulatory change that adds or removes requirements
- Audit or assessment finding pointing to a baseline gap
- Major incident revealing a missing control
- Annual review
- Client feedback from practice engagements

### Subordinate-Document Synchronization

When a control changes, Governance issues a ripple list naming every subordinate document that references it. Pillar leaders refresh those documents within 30 calendar days.

---

## 14. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CB-001 |
| **Version** | 3.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Control Framework) |
| **Effective Date** | 2026-06-27 |
| **Review Cycle** | Quarterly; and on any framework version change |
| **Frameworks** | NIST 800-53r5; NIST 800-171r3; NIST CSF 2.0; CIS Controls v8; ISO/IEC 27001 A.5-A.8; PCI DSS v4.0.1 |
| **Regulations** | NERC-CIP v7; CMMC L2; SOX ITGC; PCI DSS v4.0.1 |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT, CUI, AI-enabled systems |

### Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 3.0 | 2026-06-27 | Governance Pillar Leader | Ground-up rewrite. Expanded from ~45 to 100+ Core controls with implementation guidance. New format: IT generalist, MSP, security engineer per control. Tool mappings per control. Compensating control catalog. Reference tool stack. Capability names replacing NIST intent language. Evidence automation guidance. |

### Related Documents

| Document | ID | Relationship |
|---|---|---|
| Cybersecurity Policy | CERG-POL-001 | Parent policy |
| Capability Map | CERG-GOV-CMX-001 | 22 capabilities mapped to controls |
| Incident Response Plan | CERG-PLN-IR-001 | Incident response controls feed here |
| PCI DSS Operational Package | CERG-PLN-PCI-001 | PCI overlay |
| Tool Matrix | machine-readable/tool-matrix.yaml | Machine-readable tool mappings |
