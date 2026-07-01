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

### AC-1 Access Control Policy — Tier: Core

**Statement:** Access control rules are written down, approved, and told to everyone. If you cannot point to the document that says how access works, you do not have a policy.

**For the IT Generalist:**

Your job: produce one document everyone can find. Here is exactly what goes in it.

*What your policy must say (copy these 8 headings):*
1. Purpose — Why this exists (one paragraph)
2. Scope — Which systems, people, and data this covers
3. Account Creation — Who can request and approve new accounts
4. Access Changes — How to request more/less access when roles change
5. Access Removal — When and how accounts are disabled (immediately on termination)
6. Access Reviews — How often we check who has access (at least quarterly)
7. Exceptions — How to request one and who approves it
8. Review Cycle — This document is reviewed every 12 months by [ROLE]

*To create the policy:*
1. Copy the 8 headings into a SharePoint or Confluence document.
2. Fill in who approves access (e.g., "department manager") and who reviews annually (e.g., "CISO").
3. Save where everyone can find it. Not email. Not your desktop.
4. Set a calendar to review in 12 months. Update the date even if nothing changed.
5. Email all staff: "Policy is at [LINK]. Please read it."

**For the MSP:**
- One master policy templated across clients. Only client name and approvers change.
- Store in each client's SharePoint. Client must own it.
- Review during QBR. Update the review date.
- Do not skip because the client is small. A 5-person company still needs documented access rules.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-1 · ISO 27001 A.9.1.1 · PCI DSS Req 7.1
- Evidence: Policy document with named approver and annual review date
- Cadence: Annual

**Tool Mappings:**
✅ SharePoint — version history, approval workflow, findable
✅ Confluence — same, preferred by engineers
❌ Emailed Word doc — will drift, be lost, or both

**Verification:**
1. Open the shared drive. Find the policy. Took less than 2 minutes? Good.
2. Does it name who approves new accounts? Who removes them?
3. Review date within 12 months? If not, schedule it today.

**Common Mistakes:**
- 40-page policy nobody reads. One page per section, 8 pages max.
- Policy exists but nobody told staff. Email the link.
- "Too small for a policy." Every framework requires documented policies.
- Policy written but approved by no one. Must have a named approver.

**If You Cannot Implement This:**
No framework accepts "no access control policy." Use the 8 headings above as your draft.
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

**Statement:** Every system sends security, authentication, and administrative events to a centralized log platform. No system operates without logging.

**For the IT Generalist:**

Your job: every server, network device, and cloud service sends its logs to the SIEM. If a system stops sending logs, you find out within 4 hours.

*Step 1: Configure log sources:*

**Windows servers (via Azure Monitor Agent or WEF):**
```powershell
# Install Azure Monitor Agent on Windows
# Azure Portal -> Monitor -> Data Collection Rules -> Create -> Add Windows Event Logs
# Required event logs: Security, System, Application, PowerShell (Operational)
```

**Linux servers (via Syslog or Azure Monitor Agent):**
```bash
# Configure rsyslog to forward to SIEM
sudo bash -c 'echo "*.* @siem.company.com:514" >> /etc/rsyslog.conf'
sudo systemctl restart rsyslog
```

**Azure resources (enable diagnostic settings):**
```azurecli
az monitor diagnostic-settings create   --name "SendToSentinel"   --resource /subscriptions/.../resourceGroups/rg-prod/providers/Microsoft.Compute/virtualMachines/vm-prod   --workspace sentinel-workspace   --logs '[{"category":"SecurityEvent","enabled":true},{"category":"Syslog","enabled":true}]'
```

*Step 2: Verify logs are arriving:*
```kusto
// Sentinel: check all log sources reporting in the last 24h
Heartbeat | where TimeGenerated > ago(24h)
| summarize LastHeartbeat = max(TimeGenerated) by Computer
| where LastHeartbeat < ago(4h)
| project Computer, LastHeartbeat, Status = "STALE"
```

**For the MSP:**
- Log collection for every managed client. Minimum: Domain Controllers, Exchange, file servers, firewalls.
- Weekly log source audit: any source silent for >48 hours gets a ticket.
- Per-client: document the log source inventory in the client's documentation.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-2 · PCI DSS Req 10.2 · ISO 27001 A.12.4.1
- Evidence: SIEM source inventory, coverage gap report, sample log entries
- Cadence: Monthly coverage review, continuous ingestion

**Tool Mappings:**
✅ **Microsoft Sentinel** — native Entra ID + M365 + Azure log integration. KQL query language.
✅ **Splunk** — broadest parser library. Universal Forwarder for Windows/Linux.
◐ **Wazuh** — free and open-source. Good for budget-constrained teams. Syslog + agent-based.
❌ **Logs stored only locally** — no central search, no alerting, audit finding.

**Verification:**
1. SIEM shows log ingestion from every system in the asset inventory within the last 24h.
2. Any system silent for >48 hours? Flagged?
3. Sample a log entry: does it include timestamp, user, action, source IP?

**Common Mistakes:**
- Log level too low. Enable "success" AND "failure" for audit events.
- Cloud resources not sending logs. Enable Diagnostic Settings / CloudTrail / GCP Audit Logs.
- Logs arrive at SIEM but roll off in 7 days. PCI requires 12 months.

**If You Cannot Implement This:**
No SIEM budget: Wazuh is free and open-source. For PCI DSS: centralized logging is required.
### AU-2 Audit Log Review — Tier: Core

**Statement:** Security logs are reviewed daily. Alerts are investigated and closed within SLA.

**For the IT Generalist:**

Your job: check the SIEM alert queue every morning. Investigate anything marked High or Critical. If the same alert fires every day, fix the root cause or tune the rule.

*Daily review using Sentinel:*
```kusto
// Check for uninvestigated high/critical alerts in the last 24h
SecurityIncident
| where TimeGenerated > ago(24h)
| where Severity in ("High", "Critical")
| where Status == "New"
| project TimeGenerated, Title, Severity, AssignedTo
| order by Severity desc
```

*Weekly: check for log sources that went silent:*
```kusto
Heartbeat | where TimeGenerated > ago(7d)
| summarize LastReport = max(TimeGenerated) by SourceComputerId
| where LastReport < ago(2d)
| project LastReport, SourceComputerId
```

**For the MSP:**
- Daily log review included in standard managed services.
- Critical alerts: 1-hour SLA. High: 4-hour SLA. Medium: end of next business day.
- If SIEM generates 100+ alerts/day, tune rules. Too much noise means real alerts get missed.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-6 · PCI DSS Req 10.4.1.1
- Evidence: SIEM alert queue metrics, investigation tickets, daily review evidence
- Cadence: Continuous (automated detection), Daily (human review)

**Tool Mappings:**
✅ Microsoft Sentinel — built-in SOAR for automated investigation
✅ Splunk + SOAR — mature alert management
❌ No automated log review — impossible to triage alerts in any org over 10 users

**Verification:**
1. Open the SIEM alert queue. Any critical alerts older than 1 hour without an owner?
2. SLA compliance: alerts closed within SLA >90%?
3. Any detection rule firing 100+ times with zero investigations? Tune or retire.

**Common Mistakes:**
- Alert fatigue: too many low-severity rules. Prune quarterly.
- No documented investigation. "Alert reviewed" with no ticket means nothing to an auditor.
- Ignoring medium-severity alerts. They accumulate into blind spots.
### AU-3 Audit Log Protection — Tier: Core

**Statement:** Audit logs are protected from modification or deletion. Admin changes to logging are also logged.

**For the IT Generalist:**

Your job: configure your SIEM to prevent anyone from deleting or modifying log data.

*Step 1: Enable immutable storage:*
```azurecli
# Azure: enable immutable blob storage for log analytics
az storage container immutability-policy create   --container-name sentinel-logs   --account-name logstorageaccount   --policy-mode unlocked  # Switch to "locked" after testing
```

*Step 2: Restrict SIEM admin access:*
Only 2-3 named security admins can modify detection rules or delete log sources.
Document who they are. Review quarterly.

*Step 3: Log admin actions on the SIEM itself:*
```kusto
// Track changes to Sentinel detection rules
AuditLogs | where OperationName has_any ("Update analytic rule", "Delete analytic rule")
| project TimeGenerated, InitiatedBy.user.userPrincipalName, OperationName, TargetResources
```

**For the MSP:**
- Immutable storage for client logs is standard. No exceptions.
- SIEM admin access is restricted to 2 named engineers per client.
- Weekly: review SIEM admin actions.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-9 · PCI DSS Req 10.5
- Evidence: Immutability config, admin-action audit logs, restricted SIEM access
- Cadence: Quarterly

**Tool Mappings:**
✅ Azure Immutable Blob Storage — WORM compliance
✅ AWS S3 Object Lock — similar
❌ Logs on a network share everyone can access — security finding

**Verification:**
1. Can a non-admin user delete log data? Should not be possible.
2. Can an admin delete logs without the action being logged? Should not be possible.
3. Immutability enabled? Verify the policy is active.
### AU-4 Audit Record Retention — Tier: Core

**Statement:** Audit logs retained 12 months hot, 7 years cold. You can retrieve a log from 13 months ago within 24 hours.

**For the IT Generalist:**
**Sentinel:**
```powershell
Update-AzOperationalInsightsTable -WorkspaceName sentinel-workspace -ResourceGroupName rg-security -TableName SecurityEvent -RetentionInDays 365 -TotalRetentionInDays 2555
```
**Splunk:** Settings -> Indexes -> max days = 365. Configure cold storage for 7 years.
Test retrieval annually.

**For the MSP:** 12 months hot, 7 years cold per client. Annual retrieval test.

**For the Security Engineer:** Ref NIST 800-53 AU-11 · PCI DSS Req 10.7. Evidence: Retention policy, storage config, retrieval test.

**Verification:** SIEM retention >=365 days? Retrieve a 13-month-old log? Works?

### 6.3 Configuration Management (CM)
### CM-1 Configuration Baseline (DISH) — Tier: Core

**Statement:** Every system configured to DISH baseline before production. Maintained against it.

**For the IT Generalist:**
```powershell
secedit /configure /db secedit.sdb /cfg dish-windows-server.cfg /areas SECURITYPOLICY
secedit /validate /db secedit.sdb
```

**For the MSP:** Apply DISH during onboarding. Weekly compliance scan. Azure Policy for cloud.

**For the Security Engineer:** Ref NIST 800-53 CM-2, CM-6 · PCI DSS Req 2.2. Evidence: Baseline catalog, scan reports.

**Tool Mappings:** ✅ DISH + CIS-CAT · ✅ Defender for Cloud · ❌ Manual config without baseline

**Verification:** Every system's compliance score >90%? Below 90% flagged?
### CM-2 Change Control — Tier: Core

**Statement:** All production changes authorized, documented, tested. No change without a ticket.

**For the IT Generalist:** 1) Create ticket for every production change. 2) High-risk changes need written approval. 3) Emergency changes: after-fact approval within 24h. 4) Weekly CAB.

**For the MSP:** Change management in PSA per client. If 30%+ are emergency, process is broken.

**For the Security Engineer:** Ref NIST 800-53 CM-3 · PCI DSS Req 6.5.1. Evidence: Change records, CAB minutes.

**Verification:** Every change in last 30d -> approved ticket? Emergency changes without after-fact approval?
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

**Statement:** Every hardware, software, cloud resource, and network device is recorded in an authoritative inventory.

**For the IT Generalist:**
*Azure resource inventory:*
```azurecli
az resource list --query "[].{Name:name, Type:type, Location:location}" --output table
```
Reconcile monthly: compare against cloud resource lists, AD computer objects, scanner discovery.

**For the MSP:** CMDB per client. Device42 best for MSPs. Quarterly reconciliation.

**For the Security Engineer:** Ref NIST 800-53 CM-8 · PCI DSS Req 12.5.1. Evidence: CMDB export, reconciliation log.

**Tool Mappings:** ✅ Device42 — agentless discovery ✅ ServiceNow CMDB ❌ Excel spreadsheet

**Verification:** Can you reconcile CMDB vs cloud provider's resource list? Any orphan resources?

### 6.4 Contingency Planning and Recovery (CP)
### CP-1 System Backup — Tier: Core

**Statement:** Daily automated backups. Immutable storage. Annual restore test.

**For the IT Generalist:**
*Azure Backup:*
```azurecli
az backup protection check-vm --vm-id $(az vm show -g rg-prod -n vm-prod --query id -o tsv)
```
Backups stored in separate region. Immutability enabled. Test restore annually.

**For the MSP:** Veeam or cloud-native backup per client. Immutable storage standard. Annual restore test.

**For the Security Engineer:** Ref NIST 800-53 CP-9 · PCI DSS Req 10.5.1. Evidence: Backup report, immutability evidence, restore test.

**Tool Mappings:** ✅ Veeam — hybrid, immutable ✅ Rubrik — cloud-native ❌ Tape without immutability

**Verification:** Any failed backups in last 24h? Can a backup be deleted before retention expires?
### CP-2 Recovery Planning and Testing — Tier: Core

**Statement:** Recovery procedures documented and tested annually.

**For the IT Generalist:**
1. Write a one-page recovery plan per critical system: step-by-step restore instructions.
2. Run an annual tabletop exercise with the team.
3. Technical recovery test: actually restore from backup. Verify data is usable.
4. Update plan with lessons learned.

**For the MSP:** One recovery plan per client per critical system. Annual tabletop. Technical test: one system per quarter on rotation.

**For the Security Engineer:** Ref NIST 800-53 CP-2, CP-4 · ISO 27001 A.17.1.3. Evidence: Plan, test results, lessons learned.

**Verification:** Last recovery test date? Successful? RTO/RPO realistic based on test results?

### 6.5 Identification and Authentication (IA)
### IA-1 Multi-Factor Authentication — Tier: Core

**Statement:** All interactive human access requires phishing-resistant MFA. Legacy auth disabled.

**For the IT Generalist:**
*Entra ID: Enable MFA via Conditional Access:*
```powershell
New-MgIdentityConditionalAccessPolicy -DisplayName "Require MFA All Users" -State "enabled" `
  -Conditions @{ users = @{ includeUsers = @("All") } } `
  -GrantControls @{ builtInControls = @("mfa") }
```
*Block legacy authentication (POP3, IMAP, ActiveSync basic auth):*
```powershell
New-MgIdentityConditionalAccessPolicy -DisplayName "Block Legacy Auth" -State "enabled" `
  -Conditions @{ clients = @{ includeClientTypes = @("ExchangeActiveSync", "Other") } } `
  -GrantControls @{ builtInControls = @("block") }
```

**For the MSP:** MFA for every client user. Non-negotiable. Block legacy auth at tenant level.

**For the Security Engineer:** Ref NIST 800-53 IA-2 · PCI DSS Req 8.3.1. Evidence: MFA policy, registration report.

**Tool Mappings:** ✅ Entra ID CA — MFA, FIDO2 support ✅ Duo — simple, broad app support ❌ SMS-only — NIST deprecating

**Verification:** Connect with legacy auth (POP3/IMAP). Should fail. MFA enrollment >99%?
### IA-2 Password Policy — Tier: Core

**Statement:** Minimum 12-character passwords. No periodic password changes (NIST says stop this). Banned password list enabled.

**For the IT Generalist:**
```powershell
Set-MgPolicyAuthenticationMethodPolicy -BannedPasswordProtectionEnabled $true
```
Do NOT set password expiration policies. NIST SP 800-63B explicitly recommends against them.

**For the MSP:** No password expiration for any client. SSPR reduces helpdesk tickets 30%.

**For the Security Engineer:** Ref NIST SP 800-63B · PCI DSS Req 8.3.7. Evidence: Password policy, banned password list.

**Verification:** Try setting "Spring2024!" on a new account. Blocked? Password expiration policy exists? Remove it.
### IA-3 Service Account Management — Tier: Core

**Statement:** Non-human identities are managed with the same rigor as human accounts. Secrets stored in a vault.

**For the IT Generalist:**
*Store a secret in Azure Key Vault:*
```azurecli
az keyvault secret set --vault-name kv-prod --name "db-connection-string" --value "$connString"
```
*Search source code for hardcoded secrets:*
```bash
grep -r "password\|secret\|connectionString" --include="*.config" --include="*.env" --include="*.py" --include="*.js"
```

**For the MSP:** Service account inventory per client. Secrets manager per client. Quarterly: review permissions.

**For the Security Engineer:** Ref NIST 800-53 IA-3, IA-5 · PCI DSS Req 8.6. Evidence: Secret inventory, rotation records.

**Tool Mappings:** ✅ HashiCorp Vault — enterprise secrets ✅ Azure Key Vault — native Azure ❌ Secrets in source code

**Verification:** Source code scanned for secrets? Any service accounts with interactive logon enabled?

### 6.6 Risk Assessment and Vulnerability Management (RA)
### RA-1 Risk Assessment — Tier: Core

**Statement:** Risks are documented in a risk register, scored, assigned to an owner, and treated.

**For the IT Generalist:**
Create a risk register (spreadsheet or GRC tool). For each risk: description, likelihood (1-5), impact (1-5), score, owner, treatment, target date.
Score = Likelihood x Impact. High (12+) needs management attention.
Review monthly. Add new risks within a week of discovery.

**For the MSP:** Risk register per client. Monthly risk review with client. 30-min meeting.

**For the Security Engineer:** Ref NIST 800-53 RA-3 · ISO 27001 A.8.2. Evidence: Risk register, review minutes.

**Tool Mappings:** ✅ Spreadsheet -> GRC tool (OneTrust, ServiceNow) ❌ No risk register — finding in every framework

**Verification:** Risk register exists with 10+ entries? Last review within 30 days? Any High/Critical items without target date?
### RA-2 Vulnerability Scanning — Tier: Core

**Statement:** All systems scanned for vulnerabilities on a defined schedule. Findings tracked to remediation.

**For the IT Generalist:**
*Set up scanning:* Wiz for cloud, Qualys/Tenable/Rapid7 for hybrid.
*Schedule:* Weekly for internet-facing, monthly for internal.
*Prioritize:* Critical <7 days, High <30 days, Medium <90 days.
```bash
# Qualys: launch authenticated scan
curl -u "username:password" -d "action=launch&target=192.168.1.0/24" "https://qualysapi.qualys.com/api/2.0/fo/scan/"
```

**For the MSP:** Weekly internet-facing scans, monthly internal. Standard per client.

**For the Security Engineer:** Ref NIST 800-53 RA-5 · PCI DSS Req 11.3. Evidence: Scan reports, SLA dashboard.

**Tool Mappings:** ✅ Wiz — agentless cloud, exploit path analysis ✅ Qualys — broadest coverage ❌ Brinqa — correlation platform, not a scanner

**Verification:** Any internet-facing system not scanned in 7 days? SLA compliance >90%? Open findings >90 days?
### RA-3 Vulnerability Remediation — Tier: Core

**Statement:** Critical vulnerabilities patched within 7 days. High within 30 days. Deferred patches documented.

**For the IT Generalist:** Critical (CVSS 9+): 7 days. High (CVSS 7-8.9): 30 days. If you cannot patch within SLA, document the exception with compensating control. Priorize by risk: internet-facing > internal.

**For the MSP:** SLA per client: Critical 7d, High 30d. Monthly SLA report. Exception process for deferred patches.

**For the Security Engineer:** Ref NIST 800-53 SI-2 · PCI DSS Req 6.3.3. Evidence: SLA dashboard, patch evidence, exception register.

**Verification:** Critical findings remediated within 7 days >90%? Any Critical open >14 days without approved exception?

### 6.7 System and Information Integrity (SI)
### SI-1 Malware Protection — Tier: Core

**Statement:** EDR on every endpoint and server. Automatic updates. Behavioral detection (not just signatures).

**For the IT Generalist:**
```powershell
Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled, RealTimeProtectionEnabled
```
EDR coverage must be >98% of endpoints.

**For the MSP:** EDR standard per client. SentinelOne primary recommendation. Weekly: review detection events.

**For the Security Engineer:** Ref NIST 800-53 SI-4 · PCI DSS Req 5.2. Evidence: EDR coverage report, scan schedule.

**Tool Mappings:** ✅ SentinelOne — AI-powered, rollback ✅ CrowdStrike — cloud-native ❌ Legacy AV (McAfee, Symantec)

**Verification:** EDR coverage >98%? All endpoints updated within 24h of signature release? Any detections in last 7d?
### SI-2 File Integrity Monitoring — Tier: Core

**Statement:** Critical system files monitored for unauthorized changes.

**For the IT Generalist:**
*Wazuh FIM config:* Monitor /etc, /usr/bin, /opt/app. Alert on any modification.
Review FIM alerts daily. Approved changes (patches) are whitelisted.

**For the MSP:** FIM on critical systems per client. Daily alert review. Whitelist known-good change patterns.

**For the Security Engineer:** Ref NIST 800-53 SI-7 · PCI DSS Req 11.5. Evidence: FIM config, alert review log.

**Tool Mappings:** ✅ Wazuh — open-source FIM ✅ Defender for Cloud — Azure FIM ❌ No FIM on CHD — PCI finding

**Verification:** Any open FIM alerts >24h old? Unauthorized file changes in last 30d investigated?
### SI-3 Anti-Phishing Controls — Tier: Core

**Statement:** DMARC/SPF/DKIF configured. Anti-phishing tool deployed. Phishing simulations quarterly.

**For the IT Generalist:**
*DMARC DNS record:*
```dns
_dmarc.example.com TXT "v=DMARC1; p=reject; rua=mailto:dmarc@example.com; pct=100"
```
*M365: Enable anti-phishing:* Defender for Office 365 -> Anti-phishing -> Create policy.

**For the MSP:** DMARC setup during onboarding. Anti-phishing tool (Defender for Office 365, Proofpoint). Monthly simulations for >50 users.

**For the Security Engineer:** Ref PCI DSS Req 5.4.1. Evidence: DMARC config, simulation results, training.

**Verification:** DMARC=p reject? Click rate target <5%. Report rate target >20%.

### 6.8 Supply Chain and Third-Party Risk (SR)
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

**Statement:** Networks segmented into security zones. Traffic between zones explicitly approved.

**For the IT Generalist:**
*Windows: List firewall rules:*
```powershell
Get-NetFirewallRule -Direction Inbound | Where-Object Enabled -eq $true | Select-Object DisplayName, Action
```
Minimum zones: corporate, guest, management, DMZ. Cloud segmentation via VPCs/security groups.

**For the MSP:** Segmentation per client. Minimum: corp, guest, management. Firewall rule review every 6 months.

**For the Security Engineer:** Ref NIST 800-53 SC-7 · PCI DSS Req 1.2. Evidence: Network diagram, firewall rule review.

**Tool Mappings:** ✅ Azure Firewall / AWS NGFW ✅ pfSense/OPNsense for SMB ❌ Flat network — PCI violation

**Verification:** Can a user LAN host directly reach OT network? Blocked. Firewall rules reviewed? Any "Any-Any" rules?
### SC-2 Data in Transit Encryption — Tier: Core

**Statement:** Sensitive data and admin traffic encrypted in transit. TLS 1.2+.

**IT Generalist:** Enable HTTPS. Redirect HTTP to HTTPS. Disable TLS 1.0/1.1.

**MSP:** TLS by default. Cert expiration 30-day alert.

**Ref:** NIST SC-8, PCI 4.2.1.

**Verification:** Any services on TLS 1.0/1.1? Certs expiring within 30d?
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


**Threat Intel Validation — Cloud Data Exfiltration:**
The Shai Hulud operation (June 2026) exploited CI/CD credentials to access Redshift databases and exfiltrate data to attacker-controlled storage. This attack chain: CI/CD credentials → database access → bulk export → external transfer. Standard perimeter-based data exfiltration detection does not detect internal data movement — the attack never crossed a perimeter firewall.

**Additional Guidance for Cloud Data Exfiltration Detection:**

*For the IT Generalist:*
1. Monitor cloud data export volumes: any database query that returns >1GB of data in a single query is anomalous.
2. Detect bulk data exports to unexpected locations: data should go to the application or reporting system, not to an external IP.
3. Monitor for first-time data exports: a user or service account exporting data from a system they have never exported from before.
4. Set alerts on cloud storage events: S3 bucket policy changes, storage account access key rotation, cross-region replication enablement.

*Redshift/S3 exfiltration detection:*
```kusto
// Detect bulk data export from Redshift to external
CloudTrail
| where TimeGenerated > ago(7d)
| where EventName in~ ("Unload", "CreateJob", "ExecuteSql")
| where Resources has "redshift-cluster-prod"
| extend DataVolume = toint(JsonData["dataScannedInBytes"])
| where DataVolume > 1000000000  // >1GB
| project TimeGenerated, UserIdentity, SourceIPAddress, DataVolume
| extend Severity = "High"

// Detect S3 bucket policy changes (potential data exfil setup)
CloudTrail
| where EventName in~ ("PutBucketPolicy", "PutBucketAcl", "PutBucketPublicAccessBlock")
| where TimeGenerated > ago(24h)
| project TimeGenerated, UserIdentity, Resources, EventName
| extend Severity = "High"
```

*Azure: Detect data export operations:*
```kusto
AzureDiagnostics
| where OperationName has_any ("EXPORT", "COPY INTO", "BULK INSERT")
| where TimeGenerated > ago(24h)
| project TimeGenerated, Identity, Resource, OperationName, 
          RowCount_s
| where RowCount_s > 100000
```

**Verification:**
- Can you detect a 10GB database export in near real-time? (Test: export a test dataset and verify the alert fires.)
- Are S3 bucket policies monitored for changes that could enable public access?
- Does the security team investigate bulk data exports?

*Threat references:* Shai Hulud CI/CD → Redshift exfiltration (June 2026, Fortinet)

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


### AC-8 Session Lock — Tier: Core

Statement: Devices lock after 15 min inactivity. Re-auth required to unlock.

IT Generalist:
Windows GPO:
  Set-ItemProperty ... ScreenSaveTimeOut 900
  Set-ItemProperty ... ScreenSaverIsSecure 1
Mac:
  sudo defaults write ... idleTime 900

MSP: 15-min lock standard GPO per client. Cloud timeout via Entra ID CA.

Ref: NIST AC-11, PCI 8.3.1.1

Verification: Walk away 15 min locked? Compliance >99%?

Mistake: Screensaver without password = decorative.

Compensating: PCI requires 15 min for CDE.
### AC-9 Session Termination — Tier: Core

Statement: Sessions revoked on account termination. No persistent tokens.

IT Generalist:
  Revoke-MgUserSignInSession -UserId "user@domain.com"
  Token lifetime: 8h normal, 4h admin.

MSP: Automate revocation when HR marks termination.

Ref: NIST AC-12.

Verification: Terminate account, cached session should fail.

Mistake: Account disabled but sessions valid. Run Revoke.
### AC-10 Wireless Access Control

Statement: Corporate wireless 802.1X. Guest isolated. Rogue AP detected.

IT Generalist:
  Corporate: WPA2-Enterprise, each user authenticates individually.
  Guest: WPA2-PSK, VLAN isolated. Rotate password quarterly.

MSP: Meraki/UniFi 802.1X per client. Rogue AP detection enabled.

Ref: NIST AC-18, PCI 4.1.1.

Verification: Corporate SSID requires username? Guest can ping internal? Should not.

Mistake: WPS enabled. Disable on every AP.
### AC-11 External System Use

Statement: Users cannot grant third-party app access without admin approval.

IT Generalist:
  Update-MgPolicyAuthorizationPolicy -DefaultUserRolePermissions @{ PermissionGrantPoliciesAssigned = @() }
  Review existing app permissions quarterly.

MSP: Disable user consent at every client. App permission review quarterly.

Ref: NIST AC-20.

Verification: Grant third-party app to email? Should say Contact your admin.
### AC-12 Shared Resource Access

Statement: Every shared resource has a named owner. Ownerless locked after 90 days.

IT Generalist:
  Get-Mailbox -RecipientTypeDetails SharedMailbox | Where-Object { $_.CustomAttribute1 -eq $null }
  Clean up resources not accessed in 90 days.

MSP: Quarterly inventory. Ownerless flagged. No claim = disable in 30 days.
### AC-13 External Sharing

Statement: External sharing requires authentication. Anonymous Anyone links disabled.

IT Generalist:
  Set-SPOTenant -AnyoneLinkUsers $false
  Set-SPOTenant -ExternalUserExpirationInDays 30

MSP: Default sharing Specific people. Guest expires 30 days. Quarterly review.

Ref: NIST AC-21.

Verification: Anyone link blocked? Guest inactive >90d? Remove.
### AU-5 Audit Processing Failure Alerting

Statement: Logging failure (disk full, SIEM offline) alerts within 4 hours.

IT Generalist:
  Heartbeat | where TimeGenerated < ago(4h) | project Computer, Status=STALE

MSP: Alert per client on any log source silence >4h. Weekly coverage.

Ref: NIST AU-5, PCI 10.5.2.

Verification: Agent stopped? Alert fires within 4h?
### AU-6 Audit Reduction

Statement: Daily summary of critical events. Raw logs searchable.

IT Generalist:
  SigninLogs | where ResultType != "0" | summarize count() by UserPrincipalName, IPAddress

MSP: Daily summary per client. Failed logins, admin actions, new accounts.

Ref: NIST AU-7, PCI 10.4.
### AU-7 Time Synchronization

Statement: All systems sync to authoritative NTP. Timestamps consistent.

IT Generalist:
  w32tm /config /manualpeerlist:"time.windows.com" /syncfromflags:manual /update
  w32tm /resync

MSP: NTP standard per client. Verify w32tm /query /status.

Ref: NIST AU-8, PCI 10.4.1.

Verification: All systems within 1s of source?
### AU-8 Cross-Organization Logging

Statement: Cross-org audit events logged and traceable.

IT Generalist: Each org actions logged separately. Central correlation.

MSP: Separate audit retention per client. No cross-client visibility.

Ref: NIST AU-12.

Verification: Client A sees Client B logs? Should not.
### CM-5 Change Access Restrictions

Statement: Production systems can only be changed by authorized personnel. Changes reviewed before deployment.

IT Generalist:
  1. Only named engineers can deploy to production.
  2. Code review required before every deployment.
  3. Branch protection: main requires PR + approval.

MSP: Named deployers per client. Code review required. PR approvals recorded.

Ref: NIST CM-5, PCI 6.5.1.

Verification: Non-deployer tried deploying to prod? Blocked? Every PR has approval?
### CM-6 Software Restrictions

Statement: Only authorized software can be installed. AppLocker or equivalent enforces this.

IT Generalist:
  Enable WDAC or AppLocker: only signed, approved binaries run.
  Block executables from Temp/AppData folders.

MSP: AppLocker standard per client. Allowlist approach (blocklist fails).

Ref: NIST CM-7, PCI 2.2.4.

Tool: AppLocker, WDAC, CrowdStrike FP.

Verification: Try running unsigned .exe from Downloads. Blocked?
### CM-7 Baseline Exceptions

Statement: Configuration baseline exceptions have documented business justification, compensating controls, and expiration.

IT Generalist:
  Exception record: system, finding (what deviates), business justification, compensating control, owner, expiration.
  No exception lasts >12 months without re-approval.

MSP: Exception register per client. Quarterly review. Report outstanding.

Ref: NIST CM-6, PCI 2.2.

Verification: Any exception past its expiration? Any without compensating control documented?
### CP-3 Alternate Storage

Statement: Critical data and processing capability maintained at an alternate location.

IT Generalist:
  Define critical systems. For each: alternate location (cloud region, second datacenter).
  DR plan documents: failover procedure, RTO, RPO.

MSP: Cloud-based DR per client (Azure Paired Region, AWS AZ).

Ref: NIST CP-6.

Verification: DR plan tested annually? Failover worked within RTO?
### CP-4 Contingency Plan Testing

Statement: Contingency plan tested annually via tabletop and technical exercise.

IT Generalist:
  Annual tabletop (simulate outage).
  Annual technical exercise (actually fail over).
  After-action report with findings and closure.

MSP: Annual test per client. Q1 tabletop, Q2 technical. Findings tracked.

Ref: NIST CP-4.

Verification: Last test date? Results documented? Findings closed?
### IA-4 Identifier Management

Statement: Every user has a unique identifier. Shared accounts prohibited.

IT Generalist:
  Each user = unique account. No shared mailboxes used for login.
  Naming convention: first.last@domain.com.
  Disable accounts instead of reusing.

MSP: Unique IDs for every client. No shared accounts.

Ref: NIST IA-4, PCI 8.1.1.

Verification: Any shared accounts? Any disabled account reused?
### IA-5 Identity Proofing

Statement: Identity verified before account creation. Remote proofing meets NIST IAL2.

IT Generalist:
  In-person: government ID verification.
  Remote: video call + knowledge-based verification.
  Entra ID: identity verification via ID.me or LexisNexis.

MSP: Identity verification per client during onboarding. Consistent process.

Ref: NIST IA-2, SP 800-63A.

Verification: Can someone create an account without ID verification? Should not.
### RA-4 System Categorization

Statement: Every system categorized by impact level (Low/Moderate/High) per FIPS 199.

IT Generalist:
  For each system: CIA impact (Low/Mod/High).
  Overall = highest of the three.
  Categorization drives baseline security controls.

MSP: System categorization during onboarding. Maps to DISH baseline tier.

Ref: NIST RA-2, FIPS 199.

Tool: CERG system profile template.

Verification: Every system has a categorization? Controls match categorization?
### SI-4 Security Alerts

Statement: Security alerts from all sources (SIEM, EDR, cloud, network) centralized and triaged.

IT Generalist:
  Centralize alerts into SIEM (Sentinel, Splunk, Wazuh).
  Triage within SLA: Critical 15min, High 1hr, Medium 4hr.
  Escalate uninvestigated alerts at SLA threshold.

MSP: SOC triages alerts per client. Client notification: Critical 1hr.

Ref: NIST SI-4, PCI 10.4.

Tool: Sentinel, Splunk, Wazuh.

Verification: Any critical alert uninvestigated >15min? SLA compliance >90%?
### SC-4 DoS Protection

Statement: Internet-facing systems protected against Denial-of-Service attacks.

IT Generalist:
  Enable DDoS protection at cloud provider: Azure DDoS Protection, AWS Shield.
  Configure rate limiting on WAF/firewall.
  Monitor for DDoS indicators: traffic spike, latency increase, error rate change.

MSP: DDoS protection standard for internet-facing services.

Ref: NIST SC-5.

Tool: Azure DDoS Protection, Cloudflare, AWS Shield.

Verification: DDoS protection enabled on internet-facing resources? Rate limiting configured?
### SC-5 Key Management

Statement: Cryptographic keys managed through a secure KMS. Keys rotated annually. CMK preferred over platform-managed for regulated data.

IT Generalist:
  Azure Key Vault: store keys, rotate annually.
  Use managed HSM for regulated environments.
  Audit key access: who used which key when.

MSP: Key Vault per client. Keys rotated annually. Alert on unauthorized key access.

Ref: NIST SC-12, PCI 3.5.

Tool: Azure Key Vault, AWS KMS, HashiCorp Vault.

Verification: Keys rotated within 12 months? CMK used for regulated data? Key access audited?
### SC-6 Collaborative Device Control

Statement: Cameras, microphones, and screen sharing on company devices can be disabled by the user and cannot be enabled remotely without notification.

IT Generalist:
  Intune policy: disable camera/mic for apps that do not need them.
  Remote meeting tools require user consent before sharing.

MSP: Camera/mic policy per client via MDM.

Ref: NIST SC-15.

Verification: Can a remote admin enable camera without user notification? Should not.
### MA-1 Controlled Maintenance

Statement: System maintenance performed by authorized personnel. Maintenance activities logged.

IT Generalist:
  1. Maintenance requests require ticket approval.
  2. Escort non-employee maintenance personnel.
  3. Log all maintenance: who, what system, when, what done.

MSP: Maintenance tracking per client. Vendors require prior approval.

Ref: NIST MA-2.

Verification: Maintenance logs for last 90 days available? Any unapproved maintenance?
### MA-2 Remote Maintenance

Statement: Remote maintenance sessions require MFA, are recorded, and terminated when complete.

IT Generalist:
  Remote maintenance via approved tool (TeamViewer, BeyondTrust, Bomgar).
  MFA on every remote session. Session recorded.
  Terminate session immediately when maintenance completes.

MSP: Remote maintenance via PAM tool per client. Session recording standard.

Ref: NIST MA-4, PCI 12.3.

Tool: BeyondTrust, Bomgar, CyberArk.

Verification: Remote session logs for last 30d? Any without MFA?
### MP-1 Media Disposal

Statement: Media containing sensitive data is sanitized before disposal or reuse.

IT Generalist:
  HDD: degauss or shred. SSD: ATA Secure Erase + physical destruction.
  Cloud: verify all storage deleted no snapshots remain.
  Certificate of destruction for audit trail.

MSP: Disposal procedure per client. Vendor with certificate of destruction.

Ref: NIST MP-6, PCI 9.2.5.

Tool: Blancco, certified shredding vendor.

Verification: Media disposed in last 12 months? Certificate of destruction on file?
### MP-2 Portable Media

Statement: Portable media (USB, external drives) encrypted. Auto-run disabled. Unencrypted media blocked.

IT Generalist:
  Group Policy: disable USB write access except for authorized devices.
  Encrypt all portable media: BitLocker To Go.
  Block auto-run from USB.

MSP: USB restriction policy per client. Encrypted media only.

Ref: NIST MP-7, PCI 9.2.5.

Verification: Try plugging in unencrypted USB drive. Blocked? Auto-run disabled?
### MA-3 Maintenance Tools

Statement: Maintenance tools and diagnostic equipment are authorized and malware-free.

IT Generalist:
  1. Only approved tools used for maintenance.
  2. Scan maintenance laptops/tools for malware before connecting.
  3. Vendor tools verified as malware-free.

MSP: Maintenance laptops managed per client. EDR and encryption required.

Ref: NIST MA-3.

Verification: Maintenance tools scanned before use? Any unauthorized tools in use?
### IA-6 Re-Authentication

Statement: Re-authentication required for privilege escalation or accessing sensitive data.

IT Generalist:
  Entra ID: sign-in frequency policy requiring re-auth every session for sensitive apps.
  PIM activation requires re-authentication.

MSP: Re-auth for privileged roles per client.

Ref: NIST IA-11.

Verification: Authenticate as standard user, try privileged portal. Prompted for MFA again?
### RA-5 Alert SLA Management

Statement: Security alerts have defined SLAs. SLA compliance tracked and reported monthly.

IT Generalist:
  SLAs: Critical 15min, High 1hr, Medium 4hr.
  Dashboard tracking alert age vs SLA.
  Escalate approaching SLA limit.
  Monthly report: SLA compliance target >90%.

MSP: SLA per client. Monthly report. Overdue alerts reviewed daily.

Ref: NIST SI-4.

Verification: SLA dashboard exists? Critical alerts >90% within SLA?
### SI-6 Software Integrity

Statement: Software verified for integrity before install. Signed binaries and checksums validated.

IT Generalist:
  PowerShell: Get-AuthenticodeSignature -FilePath setup.exe
  Linux: dpkg-sig --verify package.deb
  Verify SHA256 against publisher published value.

MSP: Signed software only. WDAC/AppLocker enforces.

Ref: NIST SI-7, PCI 6.4.3.

Verification: Try installing unsigned binary. Blocked? In-house code signed?
### SC-7 Session Management

Statement: Sessions managed securely: Secure+HttpOnly cookies, 15-min timeout, server-side invalidation on logout.

IT Generalist:
  Cookies: Secure, HttpOnly, SameSite=Strict.
  Session timeout: 15 min sensitive, 30 min standard.
  Invalidate session server-side on logout.
  New session ID on re-authentication.

Ref: NIST SC-23, OWASP ASVS.

Verification: Cookie has Secure+HttpOnly? Session reuse after logout blocked?
### AT-2 Role-Based Training

Statement: Personnel receive role-specific security training beyond general awareness.

IT Generalist:
  Devs: secure coding, OWASP Top 10.
  IT: system hardening, patch management.
  Finance: wire fraud awareness.
  HR: identity lifecycle, privacy.
  Exec: governance, oversight.

MSP: Role-based content per client via KnowBe4.

Ref: NIST AT-3.

Verification: Devs completed secure coding? Finance completed fraud awareness?
### IR-3 IR Training and Exercises

Statement: IR team trained on roles. Annual tabletop + technical exercise.

IT Generalist:
  Annual tabletop: walk through scenario with team.
  Annual technical exercise: actually run the playbook.
  After-action report documents gaps.

MSP: Annual IR exercise per client. Q3 tabletop.

Ref: NIST IR-2, IR-3, PCI 12.10.1.

Verification: Last tabletop date? Gaps closed within 90 days?
### IR-5 Incident Reporting

Statement: All personnel know how to report incidents. Reports acknowledged within 1 hour.

IT Generalist:
  Published channel: security@domain.com or SOC phone.
  Include reporting instructions in annual training.
  Acknowledge every report within 1 hour.
  Track to closure.

MSP: Reporting per client. 1-hour acknowledgement SLA.

Ref: NIST IR-5, IR-6.

Verification: Can you explain how to report? Any report unacknowledged >1 hour?
### PE-2 Physical Monitoring

Statement: Physical access to sensitive areas monitored. Video retained 90 days.

IT Generalist:
  Badge access logs reviewed monthly.
  Video surveillance covering entrances.
  Video retention: 90 days (PCI) minimum.

MSP: Physical security client-managed. Verify access logs quarterly.

Ref: NIST PE-6, PCI 9.1.1.

Verification: Former employees still on badge list? Video accessible from 60 days ago?
### PL-2 System Security Plan

Statement: Authoritative SSPs exist for all in-scope systems. Current, accurate, reviewed annually.

IT Generalist:
  SSP: system name, owner, data classification, regulatory scope, boundary diagram, control status.
  Review annually. Update on significant changes.
  Link SSP to evidence library.

MSP: SSP per client for regulated systems. CERG template.

Ref: NIST PL-2, RMF Step 2.

Verification: Every critical system has current SSP? Reviewed within 12 months?
### PM-2 Risk Management Strategy

Statement: Risk appetite, tolerance thresholds, and decision authority documented.

IT Generalist:
  Document: what level of risk is acceptable?
  Thresholds: Critical (15+) CISO/board, High (12-14) CISO, Medium (8-11) risk owner.
  Review quarterly with leadership.

MSP: Risk appetite per client. Documented during onboarding.

Ref: NIST PM-9, ISO 27001 A.8.2.

Verification: Documented risk appetite? Risks exceeding appetite flagged? Board sees reports?
### PM-3 Security Program Plan

Statement: Security program documented with scope, governance, resources, maturity targets.

IT Generalist:
  Document: scope (systems, locations, regulations), governance (pillars, steering), resources (headcount, budget), maturity targets.
  Review annually.

MSP: Program plan per client. CERG operating model as framework.

Ref: NIST PM-1, ISO 27001 A.5.1.

Verification: Program plan exists? Reviewed this year? Budget aligned to priorities?
### SA-2 Supply Chain Integrity

Statement: Software supply chain verified. SBOMs collected and scanned.

IT Generalist:
  1. Request SBOM from vendors.
  2. Scan SBOM with Dependency-Track or Trivy.
  3. Verify digital signatures.
  4. For open-source: verify checksums from official source.

MSP: SBOM collection during vendor assessment. Quarterly re-scan.

Ref: NIST SR-4, SLSA.

Tool: Dependency-Track, Trivy, Snyk.

Verification: Top 5 vendors have current SBOMs? Known CVEs scanned and addressed?
### AU-9 Non-Repudiation

Statement: Actions attributable to a named individual. No shared accounts.

IT Generalist:
  Unique IDs for every action.
  Centralized, immutable logs.
  Session recording for admin actions (PAM).

MSP: Unique accounts per client. SIEM centralizes logs.

Ref: NIST AU-10.

Verification: Any shared accounts? Can admin delete/modify logs?
### CP-5 Telecom Resilience

Statement: Critical communication paths have redundancy.

IT Generalist:
  Dual ISP, diverse paths (fiber + cellular).
  SD-WAN for automatic failover.
  Test failover quarterly: disconnect primary ISP.

MSP: Dual ISP per client. SD-WAN standard. Failover test quarterly.

Ref: NIST CP-8.

Verification: Disconnect primary ISP. Can you reach internet within 2 min?
### IA-7 External User Auth

Statement: External users authenticate to same standard as employees. Guest MFA required.

IT Generalist:
  Guest users: MFA required. Same IdP.
  Federation: trusted IdPs only.
  Guest accounts expire: no auth in 90 days = remove.

MSP: Guest MFA per client. Expiration policy.

Ref: NIST IA-8.

Verification: Any guest without MFA? Any guest not active in 90 days?
### PS-2 Personnel Termination

Statement: Access revoked immediately on termination. Assets returned.

IT Generalist:
  1. Disable account immediately.
  2. Revoke all active sessions.
  3. Reset app-specific passwords.
  4. Verify asset return (laptop, badge, phone).
  5. Archive data within 30 days.

MSP: Termination automation via HR->IdP. Asset return tracked.

Ref: NIST PS-4, ISO 27001 A.7.3.1.

Verification: Account disabled within 1 hour of notice? Sessions revoked? Assets returned?
### PM-4 Plan of Action and Milestones — Tier: Core

**Statement:** Open security findings are tracked in a POA&M with owners, target dates, and closure evidence.

**For the IT Generalist:**
1. For every open finding (vulnerability, audit finding, control gap), create a POA&M entry.
2. Each entry: finding ID, description, severity, assigned owner, target closure date, compensating controls, status.
3. Review POA&M entries monthly. Update dates if needed. Close entries when evidence is produced.
4. For CMMC: the POA&M is a compliance artifact. Keep it current.

*POA&M entry format:*
```csv
POA&M ID,Finding,Severity,Owner,Target Date,Compensating Control,Status
POAM-001,"MFA not enabled on VPN",Critical,IT Manager,2026-09-01,"VPN restricted to known IPs only",Open
POAM-002,"No vulnerability scanning for cloud workloads",High,Security Engineer,2026-10-01,"Wiz scanning being implemented",In Progress
```

**For the Security Engineer:**
- Reference: NIST 800-53 PM-4 · CMMC CA.L2-3.12.4 · PCI DSS Req 12.3
- Evidence: Current POA&M, review meeting minutes, closure evidence
- Cadence: Monthly (review), Continuous (tracking)

**Verification:**
- POA&M exists with entries? Current?
- Any entries past their target date? Flag and escalate.
- Closed entries: evidence of closure attached?

**Common Mistakes:**
- POA&M entries without owners. An unowned POA&M entry is an unfixed finding.
- Target dates set and never updated. When a target changes, update the date with a note explaining why.
- POA&M not tied to the risk register. POA&M entries should map to risk register entries.

**If You Cannot Implement This:**
At minimum, track open findings in a spreadsheet. Review monthly. This is the minimum for any audit.

---

### CA-2 Continuous Monitoring — Tier: Core

**Statement:** Control effectiveness is monitored continuously, not just during annual assessments.

**For the IT Generalist:**
1. Configure automated evidence collection for key controls.
2. Examples: weekly account inventory from IdP, daily vulnerability scan coverage report, monthly access review report.
3. Set up dashboards to show control health: green = compliant, yellow = at risk, red = non-compliant.
4. Review dashboards weekly. Investigate red items within 24 hours.

*Sentinel dashboard: Control health:*
```kusto
// Account recertification coverage
let totalUsers = materialize(AzureADAuditSignInLogs | where TimeGenerated > ago(30d) | summarize by UserPrincipalName | count);
let reviewedUsers = materialize( // users who went through recertification loop
  AuditLogs | where OperationName == "AccessReview" | summarize by TargetResources
);
totalUsers | extend ReviewRate = reviewedUsers / totalUsers * 100
```

**For the Security Engineer:**
- Reference: NIST 800-53 CA-7 · NIST CSF 2.0 MONITOR
- Evidence: Control health dashboard, monitoring reports
- Cadence: Continuous (monitoring), Weekly (review)

**Tool Mappings:**
✅ Azure Sentinel — control health workbooks
✅ Splunk — custom dashboards for control monitoring
✅ Wazuh — compliance score, control monitoring
❌ Annual assessment only — 364-day blind spot between assessments

**Verification:**
- Control health dashboard: visible to the security team?
- Any control red for >7 days? Investigate.
- Automated evidence collection configured for top 10 controls?

**Common Mistakes:**
- Dashboard built but not looked at. If nobody reviews the dashboard, it provides no value.
- Too many controls on the dashboard. Start with top 10. Expand as the team matures.
- No action on red items. A red control with no investigation ticket is just noise.

**If You Cannot Implement This:**
At minimum, set up weekly automated reports for your top 5 controls.

---

### AT-3 Third-Party Security Awareness — Tier: Core

**Statement:** Third parties (contractors, vendors) with access to organizational data complete security awareness training.

**For the IT Generalist:**
1. Include a security awareness training requirement in vendor/contractor agreements.
2. Provide contractors with a condensed version of the annual security training.
3. Verify training completion before granting access.
4. Track third-party training completion separately from employee training.

**For the MSP:**
- Contractor training: include in the onboarding process for each client.
- Training evidence: contractor completion certificate.
- Quarterly: review contractor training compliance.

**For the Security Engineer:**
- Reference: NIST 800-53 AT-2
- Evidence: Training policy, third-party completion records, contract clauses
- Cadence: Per contractor onboarding, Annual (review)

**Verification:**
- All contractors with system access have completed training?
- Contractor training completion rate: target >95%.
- Any contractors past the 30-day onboarding window without training?

**Common Mistakes:**
- Contractors excluded from training because "they will be here for 2 weeks." Short-term contractors also need training.
- No training for vendor personnel with admin access. Vendors managing your systems need training on your policies.

**If You Cannot Implement This:**
At minimum, provide contractors with a one-page security policy summary. Document that they received it.

---

### PE-3 Portable Device Security — Tier: Core

**Statement:** Portable devices (laptops, tablets, phones) are encrypted, managed, and can be remotely wiped.

**For the IT Generalist:**
1. Enable full-disk encryption on all portable devices: BitLocker (Windows), FileVault (Mac), device encryption (mobile).
2. Enroll all portable devices in MDM.
3. Enable remote wipe capability. Test it quarterly.
4. Configure device lock: 5-minute timeout for mobile, 15 minutes for laptops.

*BitLocker: Check status:*
```powershell
Get-BitLockerVolume -MountPoint "C:" | Format-List EncryptionMethod, ProtectionStatus, LockStatus
# ProtectionStatus should be "On" for all volumes
```

**For the Security Engineer:**
- Reference: NIST 800-53 PE-3 · MP-2
- Evidence: BitLocker/FileVault compliance report, MDM enrollment report, remote wipe test evidence
- Cadence: Monthly (compliance check), Quarterly (wipe test)

**Tool Mappings:**
✅ BitLocker / Intune — Windows encryption + compliance reporting
✅ FileVault / JAMF — Mac encryption
✅ M365 / Google MDM — mobile device management
❌ Unencrypted laptops — data breach in progress, just waiting for a lost device

**Verification:**
- Encryption compliance report: what percentage of devices are encrypted? Target >99%.
- Any device without encryption for >7 days? Investigate.
- Remote wipe test: can you wipe a test device from the admin console? (Test quarterly.)

**Common Mistakes:**
- BitLocker enabled but recovery key stored with the user. Store recovery keys in Entra ID/AD.
- No remote wipe capability for lost devices. A lost, unencrypted device is a reportable breach.
- MDM enrollment not enforced. Unmanaged devices cannot be encrypted, wiped, or inventoried.

**If You Cannot Implement This:**
At minimum, enable OS-level encryption (BitLocker, FileVault) on all portable devices. This is a PCI DSS expectation.

---

### PS-3 Insider Threat Indicators — Tier: Core

**Statement:** Insider threat indicators are monitored and investigated. Data exfiltration and unauthorized access patterns trigger alerts.

**For the IT Generalist:**
1. Configure alerts for: mass file downloads, access to systems outside of job role, after-hours access to sensitive data, unusual data transfer volume.
2. Review DLP alerts daily.
3. Investigate: rule out false positives (legitimate business need, approved project).
4. True positives: escalate to HR/Legal before confronting the user.

*Data exfiltration detection:*
```kusto
// Unusual data download volume
DeviceFileEvents
| where TimeGenerated > ago(7d)
| where ActionType has_any ("FileCreated", "FileModified")
| summarize TotalSizeMB = sum(FileSize)/1000000 by AccountName, bin(TimeGenerated, 1h)
| where TotalSizeMB > 1000  // >1GB in one hour
| project AccountName, TimeGenerated, TotalSizeMB
```

**For the Security Engineer:**
- Reference: NIST 800-53 PS-3
- Evidence: DLP alert queue, investigation records, escalation evidence
- Cadence: Continuous (monitoring), Daily (review)

**Tool Mappings:**
✅ Microsoft Purview DLP — data loss prevention, alerting
✅ Microsoft Sentinel — UEBA, user behavior analytics
✅ Splunk — custom insider threat detections
❌ No insider threat monitoring — exfiltration detected only after data is published

**Verification:**
- DLP alerts reviewed daily? Any open alerts older than 24 hours?
- Mass download report: any user downloaded >1GB in the last 7 days? Investigate.
- Offboarding user checked for data exfiltration?

**Common Mistakes:**
- Monitoring only external data transfer. Insider threats exfiltrate via internal systems first.
- No baseline. Cannot detect "unusual" behavior without knowing "normal."
- DLP alerts without investigation. An alert that nobody investigates does not exist.

**If You Cannot Implement This:**
At minimum, monitor access to sensitive data after-hours. Spike in access from a single user outside business hours is the highest signal insider threat indicator.

---


### CP-6 Contingency Plan Documentation and Distribution — Tier: Core

**Statement:** The contingency plan is documented, accessible to response teams, and distributed to stakeholders.

**For the IT Generalist:**
1. Write the contingency plan: who to call, what systems to recover first, how to recover them, where to get backups.
2. Store the plan in a location accessible without network access (local copy, printed copy in a sealed envelope).
3. Distribute the plan to all response team members. Collect acknowledgment of receipt.
4. Review the plan annually. Update contact information immediately on personnel changes.

**Verification:**
- Can every response team member access the plan without network connectivity?
- When was the plan last reviewed? Within 12 months?
- Contact list: names, phone numbers, escalation order — current?

**Common Mistakes:**
- Plan stored on the internal SharePoint. When the network is down, the plan is unreachable.
- Contact list outdated. The IT director who left 6 months ago is still listed as the first call.

**If You Cannot Implement This:**
Print the one-page contact list and keep it in a sealed envelope in the server room. Update it quarterly.

---

### IA-8 Customer and Constituent Access — Tier: Core

**Statement:** Access for customers or constituents (non-employees accessing portals, self-service apps) is authenticated and logged.

**For the IT Generalist:**
1. Require authentication for all customer portals and applications. Anonymous access only for public-facing content.
2. Configure session timeout for authenticated portals: 30 minutes.
3. Log customer access: who accessed, what they accessed, when, from where.
4. Provide customers with the ability to self-manage their accounts (password reset, MFA enrollment).

**Verification:**
- Can a customer access their data without authentication? Should not be possible.
- Customer session logs: available for investigation?
- Customer account self-management: password reset works without helpdesk intervention?

**Common Mistakes:**
- No session timeout for customer portals. Customer walks away from shared device, next user sees their data.
- Customer authentication without logging. Cannot investigate unauthorized access to customer accounts.

**If You Cannot Implement This:**
At minimum, require authentication for any customer portal that displays sensitive data.

---

### PM-5 Cybersecurity Insurance Management — Tier: Core

**Statement:** Cybersecurity insurance coverage is maintained, aligned with control implementation, and reported to underwriters.

**For the IT Generalist:**
1. Understand your insurance requirements: what controls does the policy require? (Typically MFA, EDR, backup, access control.)
2. Report control status to the underwriter annually.
3. Document the application process: what questions did you answer, what controls did you attest to.
4. When controls change (new tools, major incidents), review whether coverage is affected.

**Tool Mappings:**
✅ Insurance broker — policy requirements, application support
◐ Internal compliance — control-to-policy mapping
❌ No insurance — increasingly untenable, ransomware recovery costs are self-funded

**Verification:**
- Current policy: renewal date, coverage limits, required controls — documented?
- Controls attestation: if the underwriter asked "Do you have MFA?" and you answered yes, you must have MFA on every applicable system.
- Any control gaps that would invalidate coverage? (Missing MFA on VPN is a common policy exclusion.)

**Common Mistakes:**
- Attesting to controls you do not have. Misrepresentation can void coverage.
- Assuming the policy covers everything. Ransomware coverage often has sub-limits.
- Not reviewing the policy for control requirement changes year over year.

**If You Cannot Implement This:**
At minimum, document which controls your insurance policy requires. Prioritize implementing those.

---

### PM-6 Security Program Budget and Resourcing — Tier: Core

**Statement:** The security program has a defined budget, aligned to control implementation priorities.

**For the IT Generalist:**
1. Document the annual security budget: tools, personnel, training, external assessments.
2. Map budget to control priorities: which controls are funded this year? Which are deferred?
3. Track actual vs. budget monthly.
4. Adjust priorities when budget changes.

**For the Security Engineer:**
- Reference: NIST CSF 2.0 GOVERN
- Evidence: Budget document, priority alignment, variance reporting

**Verification:**
- Budget exists? Reviewed by leadership?
- Budget allocated to top 5 risk priorities?
- Any critical controls unfunded for 2+ consecutive years? Escalate.

**Common Mistakes:**
- No dedicated security budget. Security funded from IT budget and deprioritized when IT needs arise.
- Budget allocated but not spent. Unspent security budget is assumed to mean the risk was not real.

**If You Cannot Implement This:**
At minimum, document the top 5 things you would buy/invest in with budget. This becomes the unfunded priorities list.

---

### IR-6 Incident Response Coordination — Tier: Core

**Statement:** IR activities are coordinated with internal and external stakeholders. Communication follows a defined plan.

**For the IT Generalist:**
1. Identify stakeholders: Legal, PR, Communications, HR, executive leadership, board (for material incidents).
2. Define who communicates with whom during an incident. The CISO communicates technical findings to the board. Legal communicates with regulators. PR communicates with the public.
3. Prepare communication templates: internal notification, regulator notification (breach, CUI, PCI), customer notification.
4. Test the communication plan during tabletop exercises.

**For the MSP:**
- Per-client communication plan: who at the client is notified first, how (phone, email, SMS).
- Client notification SLA: documented in the MSA.
- Regulatory notification: the client's obligation, but the MSP provides the technical details.

**For the Security Engineer:**
- Reference: NIST 800-53 IR-7, IR-8
- Evidence: Communication plan, notification templates, exercise records
- Cadence: Annual (review)

**Verification:**
- Communication plan exists? Who calls whom?
- Templates prepared for common notification scenarios? Breach, ransomware, data spill, regulatory report?
- Communication plan tested in the last tabletop? Were the right people notified in the right order?

**Common Mistakes:**
- No communication plan. During an incident, you figure out who to call in real time. That is too late.
- Legal not involved early enough. Legal needs to be part of the investigation team, not called after the facts are known.
- Template not used during the actual incident. Templates written and never used drift from reality.

**If You Cannot Implement This:**
Create a one-page contact list: who to call, in what order, for what type of incident.

---

### SI-8 Secure Name/Address Resolution — Tier: Core

**Statement:** DNS and other name resolution services are secured against spoofing and cache poisoning.

**For the IT Generalist:**
1. Use DNSSEC to sign your DNS zones. This prevents DNS spoofing.
2. Use a reputable DNS resolver. Block known malicious domains.
3. Configure DNS forwarders for internal resolution. Use conditional forwarders, not root hints.
4. Monitor DNS logs for data exfiltration attempts (DNS tunneling).

*Azure DNS: Enable DNSSEC:*
```azurecli
az network dns zone update --name example.com --resource-group rg-dns --query-signing-keys true
```

**For the Security Engineer:**
- Reference: NIST 800-53 SC-20, SC-21, SC-22
- Evidence: DNSSEC configuration, DNS resolver audit, DNS log monitoring
- Cadence: Quarterly (config review)

**Tool Mappings:**
✅ Azure DNS / AWS Route 53 — DNSSEC support, managed DNS
✅ Cloudflare DNS — DNSSEC, DDoS protection, analytics
✅ Quad9 (9.9.9.9) — blocks known malicious domains
❌ Unsecured DNS — vulnerable to spoofing and cache poisoning

**Verification:**
- DNSSEC validation: `dig example.com +dnssec` — the ad flag should be set.
- Internal DNS server: configured with conditional forwarders, not root hints?
- DNS logs reviewed for tunneling patterns?

**Common Mistakes:**
- Internal DNS resolving external names via root hints. Use forwarders to a reputable external resolver.
- No DNS logging. DNS tunneling exfiltrates data in DNS queries — without logs, you cannot detect it.
- DNSSEC not configured. DNSSEC adds authentication to DNS responses preventing spoofing.

**If You Cannot Implement This:**
At minimum, use a secure DNS resolver (Quad9, Cloudflare, or your cloud provider's resolver).

---


### SI-9 Security Function Verification — Tier: Core

**Statement:** Critical security functions (antivirus, firewall, IDS/IPS) are verified to be operating at defined intervals.

**For the IT Generalist:**
1. Configure EDR/AV to report its status to a central console. Set up alerts for any agent that stops reporting.
2. Check firewall rules are applied correctly: run a configuration audit.
3. Verify WAF is in detection or prevention mode (not disabled) for all protected applications.
4. Run a weekly "security tool health" report: all agents reporting, all firewalls enabled, all security services running.

*Sentinel: Agent health check:*
```kusto
Heartbeat
| where TimeGenerated > ago(24h)
| where Category == "Endpoint Protection"
| summarize LastHeartbeat = max(TimeGenerated) by Computer
| where LastHeartbeat < ago(4h)
| project Computer, LastHeartbeat, Status = "STALE"
```

**For the Security Engineer:**
- Reference: NIST 800-53 SI-6
- Evidence: Security tool health dashboard, agent status reports
- Cadence: Continuous (monitoring), Weekly (review)

**Verification:**
- Any endpoint without a security agent heartbeat in the last 24 hours?
- Firewall: all rules enabled (not disabled) and applied to the correct interfaces?
- WAF: in prevention mode, not detection-only?

**Common Mistakes:**
- Security agent uninstalled or stopped and not detected for weeks. Configure agent heartbeat monitoring.
- Firewall rules exist but are disabled. "We kept the old rules in case we need them" — disabled rules with no enable date.

**If You Cannot Implement This:**
At minimum, check security agent status weekly. Most EDR consoles have a health dashboard.

---

### PL-3 Architecture Documentation — Tier: Core

**Statement:** System architecture, network topology, and data flows are documented and current.

**For the IT Generalist:**
1. Create a network diagram: all network segments, firewalls, VPN gateways, internet connections.
2. Create a data flow diagram: how data moves between systems, what data is at rest and in transit.
3. Document system architecture: what runs where, dependencies, external connections.
4. Review and update diagrams when the architecture changes. At minimum, review annually.

*Diagram tool recommendations:*
- draw.io / diagrams.net — free, cloud or local, Visio-compatible
- LucidChart — collaborative, subscription
- Visio — traditional, requires license

**For the Security Engineer:**
- Reference: NIST 800-53 PL-8 · PCI DSS Req 1.2
- Evidence: Network diagram, data flow diagram, architecture documentation
- Cadence: Annual (review), On significant change (update)

**Verification:**
- Network diagram exists? Reviewed within 12 months?
- Data flow for sensitive/regulated data documented? (CHD flow, CUI flow, PHI flow.)
- Can a new engineer understand the network architecture from the diagram? (Test by having a new hire review it.)

**Common Mistakes:**
- Diagram outdated. If it does not match what is actually deployed, it is misleading.
- Only network, no data flow. Network diagrams show connectivity; data flow diagrams show where sensitive data lives.
- No cloud architecture diagram. Cloud resources, VPCs, security groups, and external connections.

**If You Cannot Implement This:**
At minimum, draw a network diagram. draw.io is free. Start with internet → firewall → internal segments.

---

### PS-4 Personnel Screening — Tier: Core

**Statement:** Personnel with privileged or sensitive access are screened before access is granted.

**For the IT Generalist:**
1. Define screening tiers: standard (background check) for all personnel, enhanced (fingerprint, criminal history, credit check) for privileged/CUI/BES roles.
2. Screen before granting access. Not after, not "within 30 days."
3. For contractors: verify the contracting agency has performed equivalent screening.
4. Re-screen at intervals defined by regulatory requirement.

**For the Security Engineer:**
- Reference: NIST 800-53 PS-2 (position categorization), PS-3 (screening)
- Evidence: Screening policy, verification records, exception register
- Cadence: Before access grant, then per defined interval

**Verification:**
- Every person with privileged access has a current screening record?
- Contractors: screening verified with contracting agency?
- Screening records: retained per regulatory requirement?

**Common Mistakes:**
- Access granted before screening completes. Screen first, then grant access.
- Contractors not screened. The contracting agency says they screened them. Verify.

**If You Cannot Implement This:**
At minimum, verify identity and right-to-work. For regulated environments, formal screening is required.

---

### CM-8 System Decommission — Tier: Core

**Statement:** Systems being decommissioned follow a defined process: data sanitized, assets returned, access revoked.

**For the IT Generalist:**
1. Identify the system being decommissioned. Verify no data is needed (legal hold, regulatory retention).
2. Sanitize data per MP-1. For cloud systems: verify no storage, backups, or snapshots remain.
3. Return hardware or verify disposal.
4. Revoke system accounts, service principals, and API keys.
5. Remove the system from monitoring, backup, vulnerability scanning, and asset inventory.
6. Update documentation: network diagrams, CMDB, system categorization register.

*Azure: Deprovision a VM and verify cleanup:*
```azurecli
# Delete VM
az vm delete --resource-group rg-prod --name vm-old --yes

# Verify no remaining disks
az disk list --resource-group rg-prod --query "[?contains(ownerId, 'vm-old')]" --output table

# Verify no remaining NICs
az network nic list --resource-group rg-prod --query "[?contains(virtualMachine.id, 'vm-old')]" --output table
```

**For the Security Engineer:**
- Reference: NIST 800-53 CM-8 (remove from inventory)
- Evidence: Decommission checklist, data sanitization certificate, inventory removal evidence
- Cadence: Per decommission event

**Verification:**
- Decommission checklist completed for every retired system?
- Cloud resources: any orphaned resources from decommissioned systems? (Orphaned disks, unused IPs.)
- Backup data: old backups of decommissioned systems purged per retention policy?

**Common Mistakes:**
- System decommissioned but still in the CMDB. Phantom assets remain in inventory forever.
- Backups not purged. Old backups of decommissioned systems still exist in the backup tool.
- Cloud resources left running. "We turned off the VM but forgot the load balancer and database." Audit cloud resources after decommission.

**If You Cannot Implement This:**
At minimum, mark the system as "Decommissioned" in the CMDB. Remove from vulnerability scanning and monitoring.

---
