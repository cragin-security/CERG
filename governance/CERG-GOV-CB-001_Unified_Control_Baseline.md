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

**Statement:** User sessions are locked after 15 minutes of inactivity. Re-authentication is required to unlock.

**For the IT Generalist:**
1. Configure screen saver or device lock timeout to 15 minutes.
2. Enable password-protected screen saver on all workstations and servers.
3. For cloud apps: configure IdP session timeout to 15 minutes for inactivity.
4. Test: walk away from your workstation for 15 minutes. Come back — it should be locked.

*Windows: Deploy via GPO:*
```powershell
# Set screen saver timeout to 900 seconds (15 min)
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Personalization" -Name "ScreenSaveTimeOut" -Value 900
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Personalization" -Name "ScreenSaverIsSecure" -Value 1
```

*Entra ID session timeout:*
```powershell
# Configure conditional access session control
New-MgIdentityConditionalAccessPolicy -DisplayName "Session Timeout 15min" -State "enabled" `
  -Conditions @{ applications = @{ includeApplications = @("All") } } `
  -SessionControls @{ signInFrequency = @{ value = 15; type = "timeBased" } }
```

**For the MSP:**
- Standard GPO for all clients: 15-minute lockout.
- Cloud app session timeout: configure at the tenant level via Conditional Access.
- Exceptions: documented for shared workstation scenarios (nursing stations, factory floor terminals).

**Tool Mappings:**
✅ GPO / Intune — device lock policy enforced centrally
✅ Entra ID Conditional Access — cloud app session timeout
◐ Third-party MDM — varies by platform
❌ No session lock — direct security finding in every framework

**Verification:**
- Workstation: sit idle for 15 minutes — does the screen lock?
- Cloud app: open a browser session, walk away — does the app require re-auth after 15 min?
- Report: devices without screen lock timeout >15 min should be <5% of fleet.

**Common Mistakes:**
- Screen saver enabled but not password-protected. A locked screen without a password is decorative.
- Session timeout too long (>30 min). PCI requires 15 minutes for CDE access.
- No distinction between corporate device and BYOD. BYOD should have the same lock policy via MAM.

**If You Cannot Implement This:**
For shared workstations (kiosk, manufacturing floor): documented exception with compensating physical controls. For PCI DSS CDE: 15-minute lock timeout is required.

---

### AC-9 Session Termination — Tier: Core

**Statement:** Sessions are terminated when users log out, idle timeout expires, or an admin terminates the session.

**For the IT Generalist:**
1. Train users to lock their workstation when leaving (Win+L on Windows).
2. Configure IdP session length: max 8 hours for normal users, 4 hours for privileged.
3. Enable "sign out from all sessions" on account termination — immediately revoke all active tokens.
4. Test: terminate a test user's account, then attempt to use their active browser session. It should fail.

*Entra ID: Revoke all sessions:*
```powershell
# Revoke all tokens for a terminated user
Revoke-MgUserSignInSession -UserId "user@domain.com"

# Verify no active sessions remain
Get-MgUserAuthenticationSignInPreference -UserId "user@domain.com"
```

**For the MSP:**
- Idle session timeout: standard configuration per client.
- Session revocation on termination: automate via lifecycle workflows.
- Quarterly: audit active sessions for terminated users — there should be zero.

**Tool Mappings:**
✅ Entra ID Conditional Access — session controls, sign-in frequency
✅ Okta — session policy, global sign-out
❌ No session termination for terminated users — data exfiltration risk

**Verification:**
- Terminate an account. Can their existing browser session still access resources? It should not.
- Monthly report: active sessions for accounts disabled >24 hours ago.

**Common Mistakes:**
- "Remember this device" checkboxes extend session indefinitely. Limit to 14 days max.
- No session revocation on termination. Disabling the account prevents new logins but existing tokens remain valid. Use `Revoke-MgUserSignInSession`.

**If You Cannot Implement This:**
At minimum, reset the user's password on termination. This invalidates existing token-based sessions in most IdPs.

---

### AC-10 Wireless Access Control — Tier: Core

**Statement:** Wireless networks are authorized, configured securely, and monitored for rogue access points.

**For the IT Generalist:**
1. Configure corporate Wi-Fi with WPA3 (or WPA2-Enterprise with 802.1X). No PSK/pre-shared key.
2. Create a separate guest Wi-Fi network isolated from the corporate network.
3. Disable WPS (Wi-Fi Protected Setup) on all access points.
4. Run a quarterly wireless survey to detect rogue access points.

*Windows: Detect nearby wireless networks:*
```powershell
netsh wlan show networks mode=bssid
```

**For the MSP:**
- WPA2-Enterprise with 802.1X is standard per client. No PSK except for IoT devices with documented exception.
- Guest Wi-Fi is isolated via VLAN.
- Quarterly: walk the client site with a wireless scanner or use cloud-based WLAN controller reporting.

**For the Security Engineer:**
- Reference: NIST 800-53 AC-18 · PCI DSS Req 4.1 (wireless)
- Evidence: Wireless configuration, AP inventory, rogue AP scan results
- Cadence: Quarterly (scan), Annual (config review)

**Tool Mappings:**
✅ Cisco Meraki — cloud-managed WLAN, rogue AP detection
✅ UniFi — affordable, enterprise features
◐ SOHO router Wi-Fi — insufficient for >10 users
❌ WEP or WPA — deprecated, known broken

**Verification:**
- Can you connect to the corporate Wi-Fi with just a PSK? If yes, the wireless is not secure.
- Quarterly scan report: any unauthorized access points detected?
- Guest Wi-Fi: can a guest device reach the corporate network? Should be isolated.

**Common Mistakes:**
- Corporate and guest on the same SSID with a VLAN tag. The VLAN tag can be stripped. Use separate SSIDs or physical APs.
- WPS enabled. WPS brute force takes 4-8 hours. Disable it.
- No rogue AP detection. An employee plugging in a $40 AP creates an unmonitored entry point.

**If You Cannot Implement This:**
For small offices: WPA2-PSK with a strong passphrase is acceptable (minimum 14 characters, rotated annually). Not acceptable for PCI CDE.

---

### AC-11 External System Use — Tier: Core

**Statement:** Use of external systems (personal devices, third-party platforms) to access organizational data follows documented security requirements.

**For the IT Generalist:**
1. Define which external systems are allowed to access organizational data.
2. For each external system, document: what data it accesses, how authentication is handled, what security controls the provider has.
3. Require MFA and device compliance for external system access.
4. Block access from unmanaged devices using conditional access.

*Entra ID: Block unmanaged devices:*
```powershell
New-MgIdentityConditionalAccessPolicy -DisplayName "Block Unmanaged Devices" -State "enabled" `
  -Conditions @{ devices = @{ deviceStates = @{ include = @("All"); exclude = @("Compliant") } } } `
  -GrantControls @{ builtInControls = @("block") }
```

**For the MSP:**
- Conditional access to block unmanaged devices is standard per client.
- Third-party app consent: disable the ability for users to grant consent to third-party apps. Only admins should approve.
- Quarterly: review third-party app permissions in the tenant.

**Tool Mappings:**
✅ Entra ID Conditional Access — device compliance enforcement, app consent policies
✅ Okta — device trust, third-party app integration
❌ Users allowed to OAuth-consent any third-party app — common data exfiltration vector

**Verification:**
- Can a user access corporate data from a personal, unmanaged phone? Should be blocked.
- Third-party app consent: users can approve apps? Disable and require admin consent.

**Common Mistakes:**
- Allowing OAuth consent for third-party apps without review. Attackers create apps that look legitimate and harvest data via OAuth.
- No device compliance check for external system access. MFA on an unmanaged device still exposes data.
- Contractors with personal devices treated differently. Contractors also need managed or compliant devices.

**If You Cannot Implement This:**
Use app protection policies (MAM) for BYOD access — protects corporate data in approved apps without managing the device.

---


### AC-12 Access Control for Shared and Group Resources — Tier: Core

**Statement:** Shared resources (shared mailboxes, service accounts, team folders) have documented ownership and access governance.

**For the IT Generalist:**
1. Inventory all shared resources: shared mailboxes, distribution groups, team sites, shared folders.
2. Assign a named owner to each shared resource. Put an expiration date on the resource.
3. Review access to shared resources quarterly. Remove users who no longer need access.
4. Do not use shared mailboxes for authentication. Every user has a unique identity.

*Exchange: List shared mailboxes:*
```powershell
Get-Mailbox -RecipientTypeDetails SharedMailbox |
  Select-Object DisplayName, PrimarySmtpAddress, GrantSendOnBehalfTo
```

**For the MSP:**
- Shared resource inventory is part of client onboarding.
- Quarterly review: shared resources without an owner in the last 180 days get locked.
- No shared credentials. Ever.

**Tool Mappings:**
✅ Entra ID / Exchange Admin Center — shared resource management
✅ Microsoft 365 Admin Center — shared mailbox delegation review
❌ Shared credentials among team members — audit finding

**Verification:**
- Shared mailboxes without a named owner? Flag for review.
- Any distribution group with >50 members and no owner? Flag.

**Common Mistakes:**
- Shared mailboxes used as service accounts. Service accounts need individual identities.
- No owner for shared resources. A resource without an owner is a persistence vector.
- Shared credentials stored in a company-wide password manager. Every user gets a unique identity.

**If You Cannot Implement This:**
At minimum, document every shared resource's business purpose and owner. Review annually.

---

### AC-13 Information Sharing and Collaboration — Tier: Core

**Statement:** External information sharing (external sharing links, guest access, federation) is authorized and monitored.

**For the IT Generalist:**
1. Configure external sharing policies: disable anonymous sharing links for sensitive data.
2. Set default sharing link type to "Specific people" (not "Anyone" or "Organization").
3. Review external sharing activity weekly: who shared what with whom.
4. Guest access: require MFA for all guest users. Set guest access expiration.

*SharePoint: Restrict external sharing:*
```powershell
Set-SPOSite -Identity "https://tenant.sharepoint.com/sites/sales" -SharingCapability ExistingExternalUsers
```

**For the MSP:**
- External sharing policy is standard per client: "Specific people" only.
- Automated alerts: when any user creates an "Anyone" link, flag within 24 hours.
- Guest user review: quarterly, remove guests who have not authenticated in 90 days.

**Tool Mappings:**
✅ Microsoft Purview — data loss prevention, external sharing controls
✅ Microsoft Entra Entitlement Management — access reviews for external users
◐ Manual SharePoint permission review — acceptable for <50 users
❌ Anyone/Anonymous sharing links enabled — instant data exfiltration path

**Verification:**
- Search for "Anyone" sharing links in the tenant. Any active ones?
- Guest users: how many have not authenticated in 90+ days? Remove or re-invite.
- External sharing report: who shared externally in the last 7 days?

**Common Mistakes:**
- "Anyone" links for convenience. A OneDrive "Anyone" link means no authentication required. Use "Specific people."
- Guest accounts never removed. Ex-employees and expired vendors accumulate.
- No external sharing audit trail. You cannot investigate a data leak if you do not know who shared what.

**If You Cannot Implement This:**
Disable all external sharing. Use secure file transfer (SFTP, encrypted email) for external collaboration. This is operationally painful but secure.

---

### AU-5 Response to Audit Processing Failures — Tier: Core

**Statement:** When the logging system fails, an alert is generated and the event is documented.

**For the IT Generalist:**
1. Configure your SIEM to generate an alert when any log source stops sending data for >4 hours.
2. If the SIEM itself fails, ensure a notification goes to the security team (email, SMS, or alternate channel).
3. Document every logging failure: what stopped, when it stopped, when it resumed, what logs were lost.
4. For PCI CDE: if logging fails for a CDE system, treat as a security event — data may have been accessed without logging.

*Sentinel: Log source health check:*
```kusto
Heartbeat
| where TimeGenerated > ago(4h)
| summarize LastReported = max(TimeGenerated) by Computer
| where LastReported < ago(4h)
| project Computer, LastReported
```

**For the MSP:**
- SIEM health monitoring is standard per client.
- If a log source stops sending, alert the SOC within 1 hour.
- Monthly: report on logging uptime. Target >99.5%.

**Tool Mappings:**
✅ Microsoft Sentinel — health monitoring workbooks
✅ Splunk — monitoring console, input health alerts
✅ Wazuh — agent status monitoring
❌ No monitoring of log collection — days of missing logs without detection

**Verification:**
- Check the SIEM health dashboard: any log sources silent for >4 hours?
- Last SIEM outage: how many logs were lost? Documented?

**Common Mistakes:**
- Log source stops sending, nobody notices for weeks. Configure uptime alerting on log sources.
- "The log collector ran out of disk space." Monitor disk space on log collectors.
- SIEM goes down and no one notices. Critical systems need an alternate notification path for SIEM health.

**If You Cannot Implement This:**
At minimum, check SIEM health weekly. For PCI CDE, automated alerting on logging failure is required.

---

### AU-6 Audit Reduction and Reporting — Tier: Core

**Statement:** Audit logs are reduced to actionable reports. Raw logs are available for forensic investigation.

**For the IT Generalist:**
1. Configure daily summary reports from your SIEM: failed logins, admin actions, firewall denies, malware events.
2. Keep raw logs searchable for 90 days minimum (hot tier) for forensic investigation.
3. Train the incident response team on how to query raw logs during an investigation.
4. Document common queries: user activity timeline, IP address investigation, data access patterns.

*Sentinel: Failed login summary:*
```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != "0"
| summarize FailedAttempts = count() by UserPrincipalName, IPAddress, ResultType
| order by FailedAttempts desc
| take 20
```

**For the MSP:**
- Daily summary reports: automated email to SOC team.
- Forensic log retention: 90 days hot, 12 months warm, 7 years cold.
- Per-client: document the top 5 queries the SOC uses during investigations.

**For the Security Engineer:**
- Reference: NIST 800-53 AU-7 · PCI DSS Req 10.4
- Evidence: Report configurations, SIEM query library, forensic investigation examples
- Cadence: Continuous (reports), Annual (query library review)

**Verification:**
- Can you produce a report of all admin actions in the last 24 hours? In under 2 minutes?
- Can you search raw logs from 60 days ago?
- Query library documented and accessible to IR team?

**Common Mistakes:**
- Only storing rolled-up reports, not raw logs. Reports are summaries — you need raw logs for forensic investigation.
- Log retention too short. 90 days hot minimum. For PCI: 12 months.
- No documented queries. Every IR team member writes their own KQL. Document the standard queries.

**If You Cannot Implement This:**
At minimum, keep raw logs for 30 days and produce a weekly summary report.

---

### AU-7 Time Synchronization — Tier: Core

**Statement:** All systems synchronize time with an authoritative time source. Audit log timestamps are accurate and consistent across systems.

**For the IT Generalist:**
1. Configure all systems to use the same NTP server(s). Use a trusted source (pool.ntp.org, your cloud provider's NTP, or your domain controller).
2. Verify that audit logs show accurate timestamps.
3. When investigating an incident, time discrepancies between systems make reconstruction impossible.

*Windows: Configure NTP:*
```powershell
# Set time server
w32tm /config /manualpeerlist:"time.windows.com" /syncfromflags:manual /update

# Verify synchronization
w32tm /query /status

# Check time offset
w32tm /stripchart /computer:time.windows.com /samples:5
```

*Linux:*
```bash
# Check NTP status
timedatectl status

# Force sync
sudo timedatectl set-ntp true
sudo chronyc -a makestep
```

**For the MSP:**
- Time synchronization is standard per client. All client systems point to the same NTP source.
- Domain controllers are the default time source for domain-joined Windows machines. Ensure the PDC emulator syncs with an external source.
- Cloud resources: cloud provider NTP is authoritative.

**Tool Mappings:**
✅ Windows Time Service / NTP — built-in, standard
✅ Cloud provider NTP — authoritative for cloud instances
❌ Systems with >5 second time drift — audit log timeline becomes unreliable

**Verification:**
- Pick any 3 systems across different environments. Check their current time. The difference should be <1 second.
- Firewall log timestamps vs. server log timestamps for the same event: do they match?
- Any system with time drift >5 seconds? Investigate.

**Common Mistakes:**
- Domain-joined workstations not syncing time from the domain controller. Group Policy: configure NTP client.
- Virtual machines not syncing time from the host AND from NTP. Configure both — VM time drifts without host sync.
- Time zone differences not logged. Log in UTC. Convert to local time in reports.

**If You Cannot Implement This:**
Single time source for all systems. At minimum, ensure all production systems use the same NTP server.

---

### AU-8 Cross-Organization Audit Logging — Tier: Core

**Statement:** When systems span multiple organizations (MSP, cloud provider, SaaS), audit logs from all parties are collected and correlated.

**For the IT Generalist:**
1. For cloud providers: enable resource logs (Azure Diagnostic, AWS CloudTrail, GCP Audit Logs) and forward to your SIEM.
2. For SaaS providers: collect audit logs via API (M365: Unified Audit Log, Salesforce: Event Monitoring, etc.).
3. For MSP-managed systems: establish a standard for how logs are shared: SIEM-to-SIEM, direct shipping, or periodic exports.
4. Verify quarterly that all cross-org log sources are still sending data to your SIEM.

*Enable Microsoft 365 Unified Audit Log:*
```powershell
# Enable unified audit log in M365
Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true

# Search audit log for the last 24 hours
Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -ResultSize 100
```

**For the MSP:**
- SIEM-to-SIEM log sharing for MSP-managed clients. Standard per MSA.
- Cloud provider logging is enabled during client onboarding. Do not skip.
- Quarterly: verify cross-org log sources. Any silent source older than 48 hours is flagged.

**Tool Mappings:**
✅ Azure Diagnostic Settings / AWS CloudTrail / GCP Audit Logs — cloud resource logging
✅ Microsoft 365 Unified Audit Log — M365 activity logging
◐ API-based log collection for each SaaS app — manual integration
❌ No cross-org logging — blind spot for cloud and SaaS systems

**Verification:**
- SIEM shows logs from all cloud subscriptions, SaaS apps, and managed providers in the last 24 hours?
- Any SaaS app whose API integration has stopped working? Test quarterly.
- CloudTrail/Diagnostic Settings enabled for all subscriptions? Audit annually.

**Common Mistakes:**
- CloudTrail/Diagnostic Settings enabled for some subscriptions but not all. Enable organization-wide, not per-subscription.
- SaaS app API integration breaks and nobody notices. Test the integration monthly.
- MSP logs not available during an incident. Define the SLA for log delivery in the MSA.

**If You Cannot Implement This:**
At minimum, collect cloud provider audit logs. Export SaaS logs monthly.

---

### CM-5 Access Restrictions for Change — Tier: Core

**Statement:** Only authorized personnel can make production changes. Change authority is documented and reviewed.

**For the IT Generalist:**
1. Create a change-authority roster: who is authorized to approve changes? Who is authorized to implement them?
2. Restrict write/production access to authorized personnel only. Read-only for everyone else.
3. Use role-based access for change management tools.
4. Review the change-authority roster quarterly.

*Windows: Restrict who can install software:*
```powershell
# Remove users from local admin group (prevents software installation)
Remove-LocalGroupMember -Group "Administrators" -Member "Domain Users"
```

**For the MSP:**
- Change-authority roster per client. Client approvers + MSP engineering team.
- MSP technicians do not make production changes without client-approved change ticket.
- Quarterly: review who has production access. Remove anyone without a change in the last 90 days.

**For the Security Engineer:**
- Reference: NIST 800-53 CM-5
- Evidence: Change-authority roster, emergency change review, production access audit
- Cadence: Quarterly

**Tool Mappings:**
✅ PAM (CyberArk, Entra PIM) — JIT production access
✅ ServiceNow — change authority role-based access
❌ All IT staff have production access — no separation of duties

**Verification:**
- How many people have production access? Should match the change-authority roster.
- Any emergency changes without post-approval? Investigate.
- Monthly: audit production access against the roster.

**Common Mistakes:**
- Developers have production access. Developers should deploy through CI/CD, not with direct credentials.
- No separation between change approver and change implementer. The same person should not both approve and implement.
- Vendors with permanent production access. Vendors get JIT access approved per change.

**If You Cannot Implement This:**
At minimum, document who has production access. Review quarterly.

---

### CM-6 Software Usage Restrictions — Tier: Core

**Statement:** Only approved software is installed on organizational systems. Unapproved software is blocked.

**For the IT Generalist:**
1. Create an approved software list: the specific software titles and versions allowed on organizational systems.
2. Configure application control: block unapproved executables.
3. For Windows: use AppLocker or WDAC. For macOS: use Xprotect or MDM controls.
4. Exceptions: document and review quarterly.

*Windows AppLocker: Allow Microsoft and Windows components only:*
```powershell
# Create AppLocker default rules (allows Windows + Microsoft Store apps)
New-AppLockerPolicy -RuleType Publisher,Path,Hash -User Everyone -RuleMode Enforce -XmlPolicy .\applocker-policy.xml
```

**For the MSP:**
- Approved software list is standard per client. Start with: Microsoft Office, Adobe Reader, web browsers, line-of-business apps.
- Application control via Intune or GPO.
- Quarterly: audit installed software against approved list. Flag non-compliant installations.

**For the Security Engineer:**
- Reference: NIST 800-53 CM-7, CM-10 · CIS Control 2
- Evidence: Approved software list, application control policy, non-compliant software report
- Cadence: Quarterly

**Tool Mappings:**
✅ Microsoft AppLocker / WDAC — built-in Windows application control
✅ Microsoft Intune — application management, compliance policies
✅ SentinelOne — application control module
❌ No application control — users can install any software, including malware

**Verification:**
- Try installing unapproved software. It should be blocked.
- Report: systems with unapproved software installed. Target 0.
- Software inventory: does the tool match the approved software list?

**Common Mistakes:**
- Approved software list too narrow. Users will find a way around overly restrictive controls. Start broad, tighten gradually.
- Exceptions process unknown to users. Document how to request new software approval.
- No application control on servers. Servers are where ransomware runs.

**If You Cannot Implement This:**
For small environments: document the approved software list and audit manually via software inventory tool. For regulated environments, automated application control is expected.

---

### CM-7 Baseline Exception Management — Tier: Core

**Statement:** Configuration baseline exceptions are documented, approved, time-limited, and reviewed.

**For the IT Generalist:**
1. When a system cannot meet the DISH baseline (e.g., legacy application requires an insecure setting), create an exception record.
2. Exception record includes: system name, control ID, reason for exception, compensating control, owner, expiration date.
3. Submit for approval per the RMF authority table.
4. Review exceptions quarterly. Renew or close.

*Exception register format:*
```csv
Exception ID,System,Control ID,Reason,Compensating Control,Owner,Approved By,Expiration,Status
EXC-001,legacy-app-01,CM-1,"Legacy app requires TLS 1.0","TLS terminated at WAF, legacy app only reachable via internal network",App Owner,CISO,2026-12-31,Active
```

**For the MSP:**
- Exception register is part of the risk register per client.
- Quarterly exception review: flag expired exceptions. Renew or escalate.
- Exceptions without an expiration date are not allowed.

**For the Security Engineer:**
- Reference: NIST 800-53 CM-6 · PCI DSS Req 2.2
- Evidence: Exception register, approval records, quarterly review evidence
- Cadence: Continuous (tracking), Quarterly (review)

**Verification:**
- Any exceptions past their expiration date? Flag.
- Any exception without a named owner? Flag.
- Any exception older than 12 months? The baseline or the application should have been updated.

**Common Mistakes:**
- "Permanent" exceptions. Every exception has an expiration date. All of them.
- Exception without compensating control. "We cannot fix this" is not an exception without documenting the alternate protection.
- Exception never reviewed. Set a calendar reminder for the quarterly review.

**If You Cannot Implement This:**
A verbal exception is not an exception. It must be documented with owner, date, approver, and compensating control.


### CP-3 Alternate Storage and Processing — Tier: Core

**Statement:** Critical data and processing capability are maintained at an alternate location to support recovery.

**For the IT Generalist:**
1. Identify which systems are critical enough to need an alternate site. At minimum: identity provider, core business apps, and their databases.
2. Store backups in a geographically separate region from production.
3. If your cloud provider has a region failure, can you fail over to another region? Test it.
4. Document the failover plan: who triggers it, what systems fail over, how long it takes.

*Azure: Paired region failover:*
```powershell
# Check Azure Paired Region for your primary region
Get-AzLocation | Where-Object GeographyGroup -eq "United States" |
  Select-Object Location, PairedRegion
```

**For the MSP:**
- Alternate storage: backups in a different region/cloud/on-prem location.
- For cloud-only clients: multi-region architecture with automated failover for critical systems.
- For on-prem clients: backup to cloud or colocation facility.

**For the Security Engineer:**
- Reference: NIST 800-53 CP-6, CP-7
- Evidence: Alternate site plan, failover test results, cross-region backup evidence
- Cadence: Annual (test)

**Tool Mappings:**
✅ Azure Site Recovery — automated failover to paired region
✅ AWS Disaster Recovery — cross-region recovery
✅ Veeam — cross-site backup and replication
❌ Single region/on-prem with no alternate location — single point of failure

**Verification:**
- Can you fail over your critical system to the alternate region? When was the last test?
- Are backups stored in a different region from production? Verify.
- RTO for failover: documented and tested?

**Common Mistakes:**
- Backups in the same region as production. Region failure destroys both. Use a different region.
- Failover plan written but never tested. An untested failover plan is a fantasy.
- No communication plan for failover events. Who notifies users? Who decides to fail over?

**If You Cannot Implement This:**
For small businesses: cloud backups from on-prem. Store in a different geographic region.

---

### CP-4 Contingency Plan Testing and Training — Tier: Core

**Statement:** Recovery procedures are tested at least annually. Personnel are trained on their recovery roles.

**For the IT Generalist:**
1. Schedule an annual tabletop exercise: 2 hours, key stakeholders, walk through a disaster scenario.
2. Schedule a technical recovery test: actually restore a system from backup and verify it works.
3. Train recovery team members on their roles before they are needed.
4. Document lessons learned and update the recovery plan.

*Tabletop scenario example:*
```markdown
# Tabletop: Ransomware Recovery
**Scenario:** A ransomware attack encrypts all production servers.
**Inject 1:** IT reports that the last known-good backup is from 72 hours ago.
**Discussion questions:**
- Decision: Pay ransom or restore from backup?
- How long will restoration take? Is the business willing to wait that long?
- What systems do we restore first? What is the priority order?
- What do we tell customers? Employees? Media?
```

**For the MSP:**
- Annual tabletop with each client. Facilitated by your team.
- Technical recovery test: test one client system per quarter on rotation.
- Training: include recovery procedures in new employee onboarding for managed services staff.

**Tool Mappings:**
✅ Tabletop exercise facilitator guide — included in CERG practice-assets
✅ Veeam SureBackup — automated recovery verification
❌ No testing — plan will fail under pressure

**Verification:**
- When was the last tabletop? Documented outcomes?
- When was the last technical recovery test? Successful?
- Are recovery roles assigned to named individuals?

**Common Mistakes:**
- Tabletop without technical validation. Walking through a plan verbally is not the same as actually restoring.
- Recovery test on a non-production system only. Test on a production-like environment.
- Lessons learned not implemented. Update the plan immediately after the test.

**If You Cannot Implement This:**
At minimum, run a tabletop exercise annually. No technical test is acceptable for non-critical systems.

---

### IA-4 Identifier Management — Tier: Core

**Statement:** User identifiers are unique, traceable to a named individual, and managed through a lifecycle process.

**For the IT Generalist:**
1. Every user gets a unique identifier. No shared accounts.
2. Use a consistent naming convention: firstname.lastname@domain.com.
3. Disable identifiers when the user leaves or changes roles.
4. Contractor identifiers are flagged with an expiration date.

*Entra ID: List users with no manager (potential orphans):*
```powershell
Get-AzureADUser -All $true | Where-Object {$_.Manager -eq $null -and $_.AccountEnabled -eq $true} |
  Select-Object DisplayName, UserPrincipalName, CreationType
```

**For the MSP:**
- Naming convention: standardize across all clients. firstname.lastname.
- No shared accounts. Period.
- Contractor accounts: named per-client policy (e.g., c-firstname.lastname or with expiration attribute).

**For the Security Engineer:**
- Reference: NIST 800-53 IA-4 · PCI DSS Req 8.1.2
- Evidence: IdP user inventory, lifecycle automation, shared-account exception register
- Cadence: Continuous

**Verification:**
- Unique user report: any duplicate display names with different UPNs? Investigate.
- Contractor accounts: any without an expiration date?
- Disabled accounts: any enabled for >90 days without activity?

**Common Mistakes:**
- Generic accounts for temporary workers. Every worker gets a unique ID.
- Naming convention not enforced. Users create their own accounts with inconsistent names.
- Contractor accounts not separated from employee accounts. Flag them with a naming convention or attribute.

**If You Cannot Implement This:**
At minimum, every human user has a unique ID. No exceptions. For PCI DSS, unique IDs are required.

---

### IA-5 Identity Proofing — Tier: Core

**Statement:** User identity is verified before account creation. Proofing level matches the risk of the access granted.

**For the IT Generalist:**
1. Before creating an account, verify the user's identity: government ID, in-person verification, or video call with document check.
2. For remote users: use identity verification tools (Entra ID Verified ID, ID.me, or similar).
3. For privileged access: enhanced proofing (in-person or notarized).
4. Retain proofing records per applicable regulatory requirements.

*Entra ID: Identity Governance:*
```powershell
# Enable identity verification
Set-MgIdentityGovernanceLifecycleWorkflow -Settings @{ identityProofing = $true }
```

**For the MSP:**
- Identity proofing is standard per client for all user creations.
- Remote proofing: video call with government ID check.
- Records retention: 2 years after account termination (default). Per regulatory: consult DPP schedule.

**For the Security Engineer:**
- Reference: NIST 800-63A (IAL2) · ISO 27001 A.7.1.1
- Evidence: Proofing policy, verification records, exception register
- Cadence: Per account creation

**Verification:**
- Sample of 5 recently created accounts: does each have a corresponding identity verification record?
- Remote hires: how was identity verified without in-person meeting?
- Privileged accounts: enhanced proofing applied?

**Common Mistakes:**
- No identity verification for remote hires. Just because you see them on video does not confirm their identity. Use verified ID.
- Proofing records not retained. Keep them. You may need to prove who had access to what during an investigation.
- Contractors proofed by their employer but not by you. Verify the contractor's identity yourself.

**If You Cannot Implement This:**
At minimum, verify identity via video call with government ID. Document the verification.

---

### RA-4 System Categorization — Tier: Core

**Statement:** Systems are categorized by criticality and data sensitivity. The categorization drives control selection and assessment frequency.

**For the IT Generalist:**
1. Categorize every system: Critical (data breach = existential), High (data breach = material), Medium (data breach = operational impact), Low (no sensitive data).
2. Document the categorization for each system in the asset inventory.
3. Review categorizations annually or on significant system change.
4. Apply control selection based on categorization: Critical/High systems get the Enhanced control baseline.

*Categorization matrix:*
```csv
System Name,Data Classification,Regulatory Scope,Criticality,Control Baseline
payment-prod,CHD,PCI,High,Enhanced
hr-database,PII,Privacy,Critical,Enhanced
dev-test,None,None,Low,Core
```

**For the MSP:**
- System categorization is part of client asset inventory. Apply during onboarding.
- Critical/High systems get quarterly assessments. Low systems get annual.
- Categorization review: annually during QBR.

**For the Security Engineer:**
- Reference: NIST 800-53 RA-2 · NIST SP 800-60
- Evidence: Categorization register, FIPS 199 mappings
- Cadence: Annual

**Verification:**
- Can you list every Critical system? If not, categorization is incomplete.
- Are there systems processing sensitive data categorized as Low? Investigate.
- Categorization review date: within the last 12 months?

**Common Mistakes:**
- Everything is Critical. If every system is Critical, the categorization is useless. Use the full scale.
- Categorization outdated. A system that processed no PII last year may process PII this year. Review.
- Categorization not tied to control selection. Critical systems should get the Enhanced baseline.

**If You Cannot Implement This:**
At minimum, identify systems that process regulated data (CHD, PII, CUI). Those are Critical.

---

### SI-4 Security Alerts and Advisories — Tier: Core

**Statement:** External security alerts (CISA, vendor, ISAC) are monitored, triaged, and acted upon.

**For the IT Generalist:**
1. Subscribe to CISA alerts (https://www.cisa.gov/newsletter). Also subscribe to your key vendors' security advisory feeds.
2. When an alert arrives: read it, assess relevance to your environment (do you use the affected product? is it internet-facing?).
3. If relevant: create a ticket, assign to the system owner, set a target remediation date.
4. If not relevant: document the finding and close.

*CISA KEV check:*
```powershell
# Download CISA Known Exploited Vulnerabilities catalog
$kev = Invoke-RestMethod -Uri "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
$kev.vulnerabilities | Where-Object {$_.dateAdded -gt (Get-Date).AddDays(-30)} |
  Format-Table vulnerabilityName, product, requiredAction
```

**For the MSP:**
- Security advisory monitoring is standard per client.
- CISA KEV catalog checked daily. Relevant CVEs create tickets automatically.
- Vendor security advisories: monitor for key vendors (Microsoft, Cisco, Palo Alto, VMware).

**For the Security Engineer:**
- Reference: NIST 800-53 SI-5
- Evidence: Alert triage log, CISA KEV review evidence, vendor advisory subscription list
- Cadence: Continuous

**Tool Mappings:**
✅ CISA KEV — free, authoritative, daily updated
✅ Microsoft Security Response Center — Microsoft product alerts
✅ Vendor-specific RSS/API feeds — as available
❌ No security alert monitoring — you will learn about critical vulns on the news

**Verification:**
- Last CISA KEV review: when? Were there applicable vulns? Acted upon?
- Vendor advisory subscriptions: active for all in-scope products?
- Alert triage SLA: critical alerts triaged within 24 hours?

**Common Mistakes:**
- Subscribed to alerts but never read them. 1 hour per week: review the week's security advisories.
- Alert fatigue: too many feeds. Start with CISA KEV + top 5 vendors.
- No action on applicable alerts. Reading an alert without creating a remediation ticket is not triage.

**If You Cannot Implement This:**
Subscribe to CISA KEV. Check it weekly. That alone covers the most exploited vulnerabilities.

---


**Threat Intel Validation — AI-Accelerated Threats:**
Five Eyes intelligence agencies (June 2026) formally warned that AI will accelerate cyberattack speed within months. AI-driven vulnerability discovery, automated phishing generation, and deepfake social engineering are not theoretical — they are being observed in active campaigns. Trust in automated AI vulnerability scanning has collapsed to 9% among security professionals due to hallucination and false-positive rates (InfoSecurity, June 2026).

**Additional Guidance for AI-Specific Threat Monitoring:**

*For the IT Generalist:*
1. Do not rely solely on AI-based detection tools without human validation. AI scanning tools hallucinate findings.
2. Monitor for AI-generated phishing: look for perfect grammar, personalized context, and unusual sender patterns that do not match the typical phishing profile.
3. Be skeptical of automated vulnerability findings from AI-only scanners. Validate before acting.
4. For AI models used in security tooling: understand the model's training data, false positive rate, and known limitations.

*AI-generated phishing detection:*
```kusto
// Unusual email patterns that may indicate AI-generated phishing
EmailEvents
| where Timestamp > ago(7d)
| where SenderDomain !in~ (CompanyDomains)  // External sender
| extend GrammarScore = Email.Body has_any ("Dear valued", "Kindly", "Please find attached")
| where GrammarScore == true
| summarize EmailsPerSender = count() by SenderAddress, Subject
| where EmailsPerSender == 1  // Single email, not a thread — phishing pattern
```

**Verification:**
- Are AI/ML security tools validated periodically? Do you know their false positive rate?
- Has the security team been briefed on AI-generated phishing characteristics?
- Is there a formal evaluation process before deploying AI-based security tools?

*Threat references:* Five Eyes AI warning (June 2026), InfoSecurity "Trust in AI vuln scanning collapses to 9%"

### SC-4 Denial-of-Service Protection — Tier: Core

**Statement:** Systems are protected against denial-of-service attacks. Rate limiting and DDoS protection are in place.

**For the IT Generalist:**
1. Enable DDoS protection on internet-facing resources. Cloud providers offer this as a service.
2. Configure rate limiting on web applications and APIs.
3. Set up alerts for unusual traffic patterns: traffic >200% of baseline for 5+ minutes.
4. Have a DDoS response plan: who to call, when to engage cloud DDoS mitigation.

*Azure DDoS Protection: Enable:*
```azurecli
az network ddos-protection create --resource-group rg-security --name ddos-protection-plan
az network vnet update --resource-group rg-prod --name vnet-prod --ddos-protection-plan ddos-protection-plan
```

**For the MSP:**
- DDoS protection is standard per client for internet-facing resources.
- Rate limiting: configure at the web application firewall or API gateway.
- Traffic baseline: documented for the first 30 days of monitoring to establish normal patterns.

**For the Security Engineer:**
- Reference: NIST 800-53 SC-5
- Evidence: DDoS protection configuration, rate limiting rules, traffic baseline
- Cadence: Quarterly (rule review)

**Tool Mappings:**
✅ Azure DDoS Protection — L3/L4 DDoS mitigation
✅ AWS Shield — standard (free) or Advanced ($3k/mo)
✅ Cloudflare — L3/L7 DDoS protection, rate limiting
✅ Azure WAF / AWS WAF — application-layer rate limiting
❌ No DDoS protection — internet-facing systems are vulnerable

**Verification:**
- DDoS protection enabled on all internet-facing resources?
- Rate limiting configured on all public web endpoints?
- Traffic baseline documented? (Cannot detect an anomaly without a baseline.)

**Common Mistakes:**
- DDoS protection enabled but not tested. Test the DDoS response plan with a tabletop.
- No rate limiting on APIs. API abuse can be a DDoS vector.
- Confusing DDoS protection with WAF. DDoS protects availability; WAF protects integrity. Both needed.

**If You Cannot Implement This:**
Cloudflare free tier provides basic DDoS protection. At minimum, enable your cloud provider's free DDoS protection.

---

### SC-5 Cryptographic Key Management — Tier: Core

**Statement:** Cryptographic keys are managed through a secure lifecycle: generation, storage, rotation, and destruction.

**For the IT Generalist:**
1. Store all cryptographic keys in a key management service (Azure Key Vault, AWS KMS, GCP Cloud KMS). Not in config files.
2. Rotate keys at least annually. For high-risk keys (TLS private keys, database encryption keys), rotate every 6 months.
3. Restrict access to keys: only the applications and administrators that need them.
4. Log all key access: who accessed which key, when, and for what purpose.

*Azure Key Vault: Key rotation:*
```azurecli
# Set key expiration policy
az keyvault key set-attributes --name tls-key --vault-name kv-prod --expires "2027-01-01T00:00:00Z"

# Generate new key version
az keyvault key create --name tls-key --vault-name kv-prod --protection software

# List key versions
az keyvault key list-versions --name tls-key --vault-name kv-prod
```

**For the MSP:**
- Key management is per-client. Use each client's cloud KMS.
- Key rotation policy: annual for standard keys, 6 months for TLS/encryption keys.
- No shared keys across clients. Each client has its own keys.

**For the Security Engineer:**
- Reference: NIST 800-53 SC-12 · PCI DSS Req 3.6.1
- Evidence: Key inventory, rotation records, access logs, KMS configuration
- Cadence: Continuous (rotation), Quarterly (access review)

**Tool Mappings:**
✅ Azure Key Vault — key management, rotation policies, HSM option
✅ AWS KMS + CloudHSM — key management, FIPS 140-2
✅ HashiCorp Vault — dynamic secrets, key management, transit engine
❌ Keys in config files, environment variables, or source code — immediate security finding

**Verification:**
- Key inventory: can you list every key, its purpose, and its last rotation date?
- Any key not rotated in >12 months? Flag.
- Key access logs: any unexpected access to sensitive keys?

**Common Mistakes:**
- Key stored in source code. Use environment variables or secrets manager. Even better: managed identity (no key at all).
- No key rotation. A key that never rotates is a permanent vulnerability if compromised.
- Overly permissive key access. Applications should get the minimum key access they need.

**If You Cannot Implement This:**
For small environments: use your cloud provider's default encryption (SSE-S3, Azure Storage encryption). These use provider-managed keys.

---

### SC-6 Collaborative Computing Device Control — Tier: Core

**Statement:** Collaborative computing devices (webcams, microphones, screen sharing) are explicitly disabled or indicated when in use.

**For the IT Generalist:**
1. Disable or cover webcams on sensitive systems. Use physical camera covers.
2. Require visual or audio indicator when the camera or microphone is active.
3. For meeting rooms: ensure the camera/microphone indicator is visible and functioning.
4. For remote access sessions: indicate when a session is being recorded.

*Windows: Camera privacy settings:*
```powershell
# Disable camera for all users
New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Camera" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Camera" -Name "CameraEnabled" -Value 0
```

**For the MSP:**
- Camera/microphone policies: configure via GPO or MDM.
- Physical camera covers: recommended for all laptops.
- Session recording indicator: standard in PAM tools.

**For the Security Engineer:**
- Reference: NIST 800-53 SC-15
- Evidence: Camera/microphone policy, session recording indicator evidence
- Cadence: Annual

**Verification:**
- Test: Is the camera indicator working? When the camera is on, does the user know?
- Session recording: are there recordings without the participant's knowledge? Should not happen.

**Common Mistakes:**
- Camera disabled but no physical cover. Software-enforced camera disable can be bypassed.
- Session recording without notification. Auditors will flag this. Notify participants.

**If You Cannot Implement This:**
At minimum, use physical camera covers on all laptops. No policy needed for a sticker.

---

### MA-1 Controlled Maintenance — Tier: Core

**Statement:** System maintenance is performed by authorized personnel and logged.

**For the IT Generalist:**
1. Schedule maintenance during approved windows.
2. Log all maintenance activities: who, what system, what was done, when, result.
3. For remote maintenance: use approved remote access tools with MFA and session recording.
4. For OT/ICS maintenance: follow the change management procedure and safety protocols.

*Windows: Check for pending reboots (maintenance needed):*
```powershell
Get-WURebootStatus
# Or
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager" -Name PendingFileRenameOperations
```

**For the MSP:**
- Maintenance is standard per client via RMM tools.
- Remote maintenance: logged and recorded.
- OT maintenance: separate schedule, separate approval.

**For the Security Engineer:**
- Reference: NIST 800-53 MA-1, MA-2
- Evidence: Maintenance logs, RMM session recordings
- Cadence: Continuous

**Verification:**
- Maintenance log for the last 7 days: any unapproved maintenance?
- Remote maintenance sessions: all recorded? Review a sample.
- OT maintenance: approved through the change process?

**Common Mistakes:**
- Maintenance performed outside approved window without documentation.
- Third-party maintenance vendors with unmonitored access. Use the same remote access tools as internal staff.
- No post-maintenance verification. After maintenance, verify the system is still compliant with the baseline.

**If You Cannot Implement This:**
At minimum, log who accesses production systems for maintenance. Review the log weekly.

---

### MA-2 Remote Maintenance — Tier: Core

**Statement:** Remote maintenance sessions are authorized, logged, and recorded.

**For the IT Generalist:**
1. Use the organization's approved remote access gateway for all remote maintenance. No direct RDP/SSH.
2. Record all remote maintenance sessions.
3. Log: who connected, from where, what systems were accessed, duration.
4. Notify the system owner before remote maintenance begins.

*Windows: RDP session logging via GPO:*
```powershell
# Enable RDP session auditing
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name "AuditUserDateTime" -Value 1
```

**For the MSP:**
- Remote maintenance is standard per client via RMM/ScreenConnect/TeamViewer.
- Record all sessions. Retain recordings for 90 days.
- Vendor remote maintenance: use the same gateway. No exceptions.

**For the Security Engineer:**
- Reference: NIST 800-53 MA-4 · PCI DSS Req 8.3.1
- Evidence: Remote session logs, session recordings, vendor maintenance procedure
- Cadence: Quarterly (review)

**Tool Mappings:**
✅ ScreenConnect / ConnectWise — remote maintenance with recording
✅ RMM tool (Ninja, Datto, Kaseya) — per-client remote maintenance
✅ PAM (CyberArk, Delinea) — session recording for privileged access
❌ Direct RDP/SSH for maintenance — no auth barrier, no recording

**Verification:**
- Remote maintenance sessions from the last 7 days: all approved? All recorded?
- Vendor maintenance sessions: conducted through the gateway, not direct access?
- Any direct RDP/SSH to production systems? Investigate.

**Common Mistakes:**
- Vendor maintenance via direct VPN-to-RDP. Vendors use the same remote access gateway.
- Session recording not enabled. Record all remote sessions. Review a sample monthly.
- No notification before remote maintenance. The system owner should know someone is working on their system.

**If You Cannot Implement This:**
At minimum, log remote maintenance. Record vendor sessions.

---

### MP-1 Media Disposal — Tier: Core

**Statement:** Digital and physical media containing sensitive data are securely sanitized before disposal or reuse.

**For the IT Generalist:**
1. Use secure wipe tools: DBAN (drives), BitRaser, or DoD 5220.22-M standards.
2. For SSDs: use ATA Secure Erase. Standard overwrite methods do not work on SSDs.
3. For cloud storage: delete data and verify deletion. Most cloud providers have soft delete.
4. For physical media (paper, tapes): shred or incinerate.

*Windows: Secure wipe a drive:*
```powershell
# Use cipher with /w flag to overwrite deleted data
cipher /w:C:

# Use Microsoft BitLocker: deprovision and deallocate
# For Azure: deallocate VM, delete disks, confirm no snapshots remain
```

**For the MSP:**
- Media disposal policy per client. Standard: NIST SP 800-88 Guidelines for Media Sanitization.
- Hard drive disposal: shred or degauss. Do not rely on software wipe for drives leaving your control.
- Cloud disposal: verify soft delete is disabled after deprovisioning.

**For the Security Engineer:**
- Reference: NIST 800-53 MP-6 · PCI DSS Req 3.2.3
- Evidence: Sanitization policy, disposal logs, certificate of destruction
- Cadence: Per disposal event

**Tool Mappings:**
✅ DBAN — free, industry standard for HDDs (does not work on SSDs!)
✅ ATA Secure Erase — for SSDs
✅ BitRaser — enterprise wipe, supports HDD, SSD, cloud
✅ Azure / AWS / GCP provider-side delete — verify no snapshots or backups remain
❌ Format/reformat — data remains recoverable

**Verification:**
- Disposal log: every disposed drive has a certificate of destruction?
- Cloud resources: any storage accounts/s3 buckets deleted but with active soft-delete backups?
- Verification read: after wiping, can any data be recovered? Test with a sample drive.

**Common Mistakes:**
- Using DBAN on SSDs. DBAN does not work on SSDs — use ATA Secure Erase.
- Cloud resources with soft delete enabled. Delete + verify purge.
- "Delete" without verification. Cloud storage may have versioning, snapshots, or replication. Verify nothing remains.

**If You Cannot Implement This:**
For physical drives: physical destruction (shredder) is the most reliable method. Certify destruction.

---

### MP-2 Portable Media and Devices — Tier: Core

**Statement:** Portable media (USB drives, external hard drives, mobile devices) are controlled and encrypted.

**For the IT Generalist:**
1. Disable USB mass storage on corporate devices via GPO or MDM.
2. If USB is required for business purposes: only allow encrypted USB drives (BitLocker To Go, hardware-encrypted).
3. Require authorization to copy data to portable media. Log and review all transfers.
4. For mobile devices: enable remote wipe capability for lost devices.

*Windows: Block USB mass storage:*
```powershell
# Disable USB mass storage
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\USBSTOR" -Name "Start" -Value 4
```

**For the MSP:**
- USB blocking is standard per client via GPO or MDM.
- If USB is needed: encrypted USB drives with documented business justification.
- Mobile device management: enforce encryption, remote wipe, compliance policy.

**For the Security Engineer:**
- Reference: NIST 800-53 MP-2, MP-4 · PCI DSS Req 9.4.1
- Evidence: USB policy, MDM configuration, data transfer logs
- Cadence: Quarterly

**Tool Mappings:**
✅ GPO / Intune — block USB mass storage
✅ Microsoft Endpoint DLP — monitor and control USB transfers
✅ MDM (Intune, JAMF, Workspace ONE) — mobile device control
❌ No USB controls — data exfiltration via $10 USB drive

**Verification:**
- Plug in a USB drive to a corporate device. It should be blocked.
- Authorized USB devices: are they encrypted? Verify.
- Mobile devices: remote wipe test? Test quarterly.

**Common Mistakes:**
- USB blocked but CD/DVD/Bluetooth not blocked. Attackers use alternate media. Block all.
- Authorized USB drives not encrypted. "We only use encrypted drives" means all of them, always.
- No DLP monitoring. You cannot prevent data exfiltration if you do not know it is happening.

**If You Cannot Implement This:**
At minimum, require encryption on all portable media. This is a PCI DSS requirement for CDE.

---

### MA-3 Maintenance Tools — Tier: Core

**Statement:** Maintenance tools (diagnostic tools, test equipment, vendor tools) are authorized and controlled.

**For the IT Generalist:**
1. Maintain an inventory of maintenance tools used on production systems.
2. Verify that maintenance tools are from a trusted source (vendor download, not unsigned internet download).
3. Remove maintenance tools from production systems after use.
4. For OT environments: maintenance tools must be approved for use on control systems — standard IT tools can disrupt operations.

**Tool Mappings:**
✅ Approved vendor tools — source verified, digitally signed
◐ Open-source diagnostic tools — vet before use on production
❌ Unsigned, untrusted tools on production systems — malware delivery vector

**Verification:**
- Inventory of maintenance tools on production systems: what is there and why?
- Any maintenance tool left on a system after maintenance completed? Should be removed.

**Common Mistakes:**
- Diagnostic tools left on production systems. The same tool can be used by an attacker for reconnaissance.
- Unsigned tools downloaded for "just this one time." Vet and approve before use.

**If You Cannot Implement This:**
At minimum, ensure all maintenance tools are from trusted, signed sources. Remove after use.

---


### IA-6 Re-Authentication — Tier: Core

**Statement:** Re-authentication is required for privilege escalation, accessing sensitive data, or after an idle timeout.

**For the IT Generalist:**
1. Configure your IdP to require re-authentication when a user accesses sensitive applications or elevates privileges.
2. Re-authentication: prompt for MFA again, not just accept an existing session token.
3. For sensitive cloud admin portals (Azure portal, AWS console): require re-auth every session.

*Entra ID: Require re-authentication for sensitive roles:*
```powershell
New-MgIdentityConditionalAccessPolicy -DisplayName "Reauth for Global Admins" -State "enabled" `
  -Conditions @{ users = @{ includeRoles = @("Global Administrator") } } `
  -SessionControls @{ signInFrequency = @{ value = 1; type = "reauthentication" } }
```

**For the MSP:**
- Re-authentication for privileged roles: standard per client.
- Sensitive app re-auth: configure per-application conditional access.
- Frequency: every session for privileged users, every 4 hours for standard.

**Tool Mappings:**
✅ Entra ID Conditional Access — sign-in frequency, session controls
✅ Okta — step-up authentication, re-authentication
❌ No re-authentication — once authenticated, all access is available

**Verification:**
- Authenticate as a standard user, then attempt to access a privileged portal. Should prompt for MFA again.
- Sign-in frequency report: how often are users prompted?

**Common Mistakes:**
- Token lifetimes too long. A token valid for 24 hours means no re-auth is needed for 24 hours.
- Re-auth not required for privilege escalation. Once authenticated, user can escalate without re-verifying.

**If You Cannot Implement This:**
At minimum, require re-authentication for admin role activation (Entra PIM, Okta Admin Console).

---

### RA-5 Security Alert SLA Management — Tier: Core

**Statement:** Security alerts have defined triage and remediation SLAs. SLA compliance is tracked and reported.

**For the IT Generalist:**
1. Define SLA tiers: Critical (active exploitation) triage within 15 min, High within 1 hr, Medium within 4 hr.
2. Configure your SIEM to track alert age and SLA status.
3. Escalate alerts approaching their SLA limit automatically.
4. Report SLA compliance monthly. Target >90% for Critical, >80% for High.

*Sentinel: SLA tracking query:*
```kusto
SecurityIncident
| where TimeGenerated > ago(30d)
| extend TimeToTriage = datetime_diff('minute', FirstActivity, CreatedTime)
| extend SLA = case(
    TimeToTriage <= 15 and Severity == "Critical", "Within SLA",
    TimeToTriage <= 60 and Severity == "High", "Within SLA",
    "Overdue"
  )
| summarize Total = count(), SLA_Compliant = countif(SLA == "Within SLA") by Severity
| extend CompliancePct = (SLA_Compliant * 100.0 / Total)
```

**For the Security Engineer:**
- Reference: NIST 800-53 SI-4 · PCI DSS Req 10.4
- Evidence: SLA dashboard, escalation records, compliance reports
- Cadence: Continuous (tracking), Monthly (reporting)

**Verification:**
- How many Critical alerts missed SLA this month? Investigate each.
- SLA dashboard: visible to SOC team?
- Escalation path for overdue alerts: documented and tested?

**Common Mistakes:**
- No SLA definitions. "Review daily" is not an SLA. Define time-based SLA per severity.
- No escalation for overdue alerts. SLA overdue by 6 hours with no escalation is a process gap.
- SLA compliance below target with no improvement plan. If compliance is 60%, the process or staffing needs fixing.

**If You Cannot Implement This:**
At minimum, define SLA for Critical alerts: triage within 1 hour. Track in a spreadsheet.

---

### SI-6 Software Integrity Verification — Tier: Core

**Statement:** Software is verified for integrity before installation. Signed binaries and checksums are validated.

**For the IT Generalist:**
1. Verify digital signatures on all software before installation: right-click → Properties → Digital Signatures.
2. For open-source software: verify the checksum (SHA256) against the publisher's published value.
3. For in-house software: sign your own binaries. Use your organization's code signing certificate.
4. Only allow execution of signed software via WDAC/AppLocker.

*PowerShell: Verify file signature:*
```powershell
# Check if a file has a valid digital signature
Get-AuthenticodeSignature -FilePath ".\setup.exe" | Format-List Status, SignerCertificate

# Output should show Status = Valid
```

*Linux: Verify package signature:*
```bash
# Debian/Ubuntu
dpkg-sig --verify package.deb

# RPM
rpm -K package.rpm
```

**For the Security Engineer:**
- Reference: NIST 800-53 SI-7 · PCI DSS Req 6.4.3
- Evidence: Code signing policy, binary signature verification logs, CI/CD signing configuration
- Cadence: Continuous (verification), Annual (policy review)

**Tool Mappings:**
✅ Windows Defender Application Control (WDAC) — only signed and approved binaries
✅ AppLocker — executable control based on publisher rules
✅ Azure Code Signing / AWS Signer — CI/CD code signing
❌ No signature verification — unverified binaries may contain malware

**Verification:**
- Try installing an unsigned executable. It should be blocked.
- In-house software: is it signed by your organization's code signing cert?
- Open-source tools: do you verify checksums before installation?

**Common Mistakes:**
- Running unsigned PowerShell scripts. Set execution policy to `AllSigned` or at minimum `RemoteSigned`.
- No code signing for in-house software. Developers build and deploy unsigned binaries.
- Checksums verified via HTTP (not HTTPS). Checksum delivered over HTTP can be tampered with. Use HTTPS.

**If You Cannot Implement This:**
At minimum, enable PowerShell script block logging. You cannot verify every script, but you can detect when unsigned scripts run.

---

### SI-7 Information Input Validation — Tier: Core

**Statement:** All input to applications and APIs is validated for correctness, length, and content. Injection attacks are prevented.

**For the IT Generalist:**
1. Configure your web application firewall (WAF) with OWASP Core Rule Set. This blocks common injection attacks (SQLi, XSS, command injection).
2. Enable parameterized queries in all database interactions.
3. Validate input length on all form fields.
4. Sanitize output to prevent cross-site scripting.

*Azure WAF: Enable OWASP CRS:*
```azurecli
az webapp config set --resource-group rg-prod --name app-prod --web-sites-enable-http-logging true
az network application-gateway waf-policy create --resource-group rg-prod --name waf-policy
az network application-gateway waf-policy managed-rule-set update \
  --resource-group rg-prod --name waf-policy \
  --type OWASP --version 3.2
```

**For the Security Engineer:**
- Reference: NIST 800-53 SI-10 · OWASP Top 10 · PCI DSS Req 6.5
- Evidence: WAF configuration, SAST/DAST scan results, code review findings
- Cadence: Continuous (WAF), Quarterly (SAST/DAST)

**Tool Mappings:**
✅ Azure WAF / AWS WAF — OWASP CRS, rate limiting, IP filtering
✅ ModSecurity — open-source WAF
✅ Snyk / Checkmarx / SonarQube — SAST testing for injection flaws
❌ No input validation or WAF — application directly exposed to injection

**Verification:**
- Run a basic SQL injection test against a public-facing web app. Should be blocked.
- WAF logs: blocked requests in the last 7 days. Review for attempted attacks.
- SAST scan: any injection findings in custom code?

**Common Mistakes:**
- WAF deployed but bypassed by direct-to-server traffic. Route all web traffic through WAF.
- SAST scan findings not remediated. Injection findings in code are an active risk until fixed.
- No input validation at the API level. APIs are the most common injection vector.

**If You Cannot Implement This:**
At minimum, deploy a WAF in front of all internet-facing web apps. Cloud provider WAFs are included in many subscription tiers.

---

### SC-7 Session Management — Tier: Core

**Statement:** Application sessions are managed securely: unique session IDs, secure cookies, session timeouts.

**For the IT Generalist:**
1. Configure cookies with Secure and HttpOnly flags.
2. Set session timeout to 15 minutes for sensitive applications, 30 minutes for standard.
3. Invalidate session on logout (server-side, not just clearing the cookie).
4. Generate a new session ID on re-authentication (prevents session fixation).

*ASP.NET: Secure session configuration:*
```xml
<system.web>
  <sessionState mode="InProc" timeout="15" cookieless="false" regenerateExpiredSessionId="true">
    <providers>
      <add name="Default" type="System.Web.SessionState.SqlSessionStateProvider" />
    </providers>
  </sessionState>
  <httpCookies httpOnlyCookies="true" requireSSL="true" sameSite="Strict" />
</system.web>
```

**For the Security Engineer:**
- Reference: NIST 800-53 SC-23 · OWASP ASVS
- Evidence: Session configuration, code review findings, WAF session protection rules
- Cadence: Annual (review)

**Verification:**
- Intercept a session cookie: does it have Secure, HttpOnly, SameSite flags? Should.
- Log out and try to reuse the session cookie. Should be rejected.
- Session timeout: idle for 15 minutes, then try to access. Should require re-authentication.

**Common Mistakes:**
- Session cookie without Secure flag. Cookie can be transmitted over HTTP.
- Session timeout not enforced server-side. Client-side timeout can be bypassed.
- No session invalidation on logout. Cookie cleared locally, but server session remains valid.

**If You Cannot Implement This:**
At minimum, set secure cookie flags and session timeout. Most web frameworks have reasonable defaults.

---

**Threat Intel Validation — Session Token Theft:**
A Chrome malware campaign (June 2026) with 10M+ installs exfiltrates session cookies to take over authenticated accounts without passwords. This bypasses MFA entirely — the attacker uses the victim's existing session. Standard session timeout controls cannot prevent this; detection and short-lived tokens are required.

**Additional Guidance for Session Token Protection:**

*For the IT Generalist:*
1. Set session token lifetimes to the shortest practical duration: 1 hour for sensitive apps, 8 hours max for standard.
2. Require re-authentication for sensitive actions even within an active session (step-up auth).
3. Bind session tokens to the client IP address and user agent (where practical). Token theft from a different IP should be blocked.
4. Monitor for impossible travel: a session used from New York and then from Moscow 10 minutes later is stolen.
5. Implement token binding (Token Binding Protocol or similar) where the platform supports it.

*Entra ID: Token protection policies:*
```powershell
# Configure token lifetime to 1 hour for sensitive apps
New-MgPolicyTokenLifetimePolicy -Definition @('{"TokenLifetime":{"AccessTokenLifetime":"01:00:00"}}')

# Enable token protection (Entra ID Conditional Access)
# Requires sign-in frequency policy
New-MgIdentityConditionalAccessPolicy -DisplayName "Token Protection Policy" -State "enabled" `
  -Conditions @{ applications = @{ includeApplications = @("All") } } `
  -GrantControls @{ builtInControls = @("mfa") } `
  -SessionControls @{ signInFrequency = @{ value = 1; type = "reauthentication" } }
```

*Session theft detection:*
```kusto
// Impossible travel detection
SigninLogs
| where TimeGenerated > ago(1h)
| summarize FirstLogin = min(TimeGenerated), LastLogin = max(TimeGenerated),
            Locations = make_set(LocationDetails), IPs = make_set(IPAddress) by UserPrincipalName
| where array_length(IPs) > 1
| extend TravelTime = datetime_diff('minute', LastLogin, FirstLogin)
| where TravelTime < 60 and array_length(Locations) > 1
| project UserPrincipalName, IPs, Locations, TravelTime
| extend Severity = "Critical"
```

**Verification:**
- Token lifetime: how long before a session expires? (Target: 1 hour sensitive, 8 hours standard)
- Impossible travel detection: configured and generating alerts?
- Can a stolen cookie from a different IP be used to access the application? (Test by extracting your own session token and using it from a different network.)

*Threat references:* Chrome session-stealing malware (June 2026, 10M+ installs)

### AT-2 Role-Based Security Training — Tier: Core

**Statement:** Personnel receive security training specific to their role. Annual general awareness plus role-specific modules.

**For the IT Generalist:**
1. General training: annual for all personnel (phishing, password hygiene, data handling, incident reporting).
2. Role-specific training:
   - Developers: secure coding, OWASP Top 10, dependency management.
   - IT/Engineering: system hardening, vulnerability management, change management.
   - Finance: wire fraud awareness, invoice verification, payment red flags.
   - HR: identity lifecycle, data privacy, insider threat indicators.
   - Executives: governance, oversight, reporting obligations.
3. Track role-specific training completion separately from general awareness.

**For the Security Engineer:**
- Reference: NIST 800-53 AT-3 · PCI DSS Req 12.6.2
- Evidence: Training curriculum, completion records, role-specific module evidence
- Cadence: Annual (training), Monthly (new hires)

**Tool Mappings:**
✅ KnowBe4 — role-specific content libraries, compliance tracking
✅ M365 Learning — basic training, SharePoint-based
✅ SANS Securing the Human — enterprise awareness, role-specific
❌ One-size-fits-all annual training — misses role-specific risk

**Verification:**
- Completion rate by role: developers completed secure coding? Finance completed fraud awareness?
- Content review: can a developer explain SQL injection? Can finance describe a wire fraud red flag?
- New hire training: completed within 30 days of start? Target >95%.

**Common Mistakes:**
- Same training for everyone. Developers need different content than finance. Role-specific.
- Training completed but not understood. Test comprehension, not just completion.
- No training for third parties. Vendors and contractors with system access need role-specific training too.

**If You Cannot Implement This:**
At minimum, deliver role-specific addendums during the annual general training session.

---

### IR-3 Incident Response Training and Exercises — Tier: Core

**Statement:** IR team members are trained on their roles and participate in exercises at least annually.

**For the IT Generalist:**
1. Identify IR team members: IT, Security, Legal, Communications, Executive.
2. Each member is trained on their specific role before they are needed.
3. Run a tabletop exercise annually: gather the team, walk through a realistic scenario.
4. Run a technical exercise annually: simulate a real incident (phishing, ransomware, data breach).

*Tabletop facilitation outline:*
```markdown
1. Scenario injection: "Your SOC detects ransomware encryption on the file server"
2. For each phase (detection → containment → investigation → recovery → notification):
   - What do we do?
   - Who does it?
   - What do we need that we don't have?
3. Document gaps and create action items
```

**For the Security Engineer:**
- Reference: NIST 800-53 IR-2, IR-3 · PCI DSS Req 12.10.1
- Evidence: Training records, exercise plans, exercise outcomes, after-action reports
- Cadence: Annual

**Verification:**
- When was the last tabletop? Documented?
- When was the last technical exercise? Were participants able to execute the playbook?
- Gaps identified in the last exercise: how many are closed?

**Common Mistakes:**
- Training provided but not practiced. Training without exercise does not build muscle memory.
- Same scenario every year. Vary the scenario: ransomware one year, supply chain attack the next.
- Exercise without an after-action report. No report = no lessons learned.

**If You Cannot Implement This:**
At minimum, run a 1-hour tabletop exercise annually. Use the CERG tabletop scenario library.

---

### IR-5 Incident Reporting — Tier: Core

**Statement:** All personnel know how to report a security incident. Reports are acknowledged and tracked.

**For the IT Generalist:**
1. Publish the incident reporting channel: email alias (security@), phone number, or ticketing portal.
2. Include the reporting process in security awareness training.
3. Acknowledge every report within 1 hour. Even if it is a false alarm, the reporter should know it was received.
4. Track reports to closure. Report the outcome to the reporter.

**For the MSP:**
- Incident reporting channel is per-client. Standardize: security@clientdomain.com or SOC phone number.
- Acknowledgement SLA: 1 hour. Initial triage: 4 hours.
- False positive handling: document why it was a false positive. Trend false positive patterns.

**For the Security Engineer:**
- Reference: NIST 800-53 IR-5, IR-6
- Evidence: Reporting policy, acknowledgement records, report tracking log
- Cadence: Continuous

**Tool Mappings:**
✅ SIEM ticketing integration — automated ticket creation
✅ ServiceNow / Jira — incident tracking, SLA management
✅ Email-to-ticket — for non-technical reporters
❌ "Tell your manager" — informal reporting fails

**Verification:**
- Is the incident reporting process documented and accessible to all personnel?
- Last 10 reported incidents: all acknowledged within 1 hour?
- Any reporter who reported an incident and never heard back? (Survey.)

**Common Mistakes:**
- Security awareness training tells users to report but does not say how. Include the email/phone number in every training.
- No acknowledgement of reports. The reporter thinks "nothing happened" and stops reporting.
- False positives mocked. A user who reports a false alarm and is ridiculed will not report the real one.

**If You Cannot Implement This:**
Set up an email alias (security@domain.com). Include it in the annual training. Check it daily.

---

### PE-2 Physical Access Monitoring — Tier: Core

**Statement:** Physical access to sensitive areas is monitored with video surveillance or electronic access controls.

**For the IT Generalist:**
1. Install video surveillance covering entrances to server rooms, CUI work areas, and network closets.
2. Retain video recordings for at least 90 days (PCI) or per regulatory requirement.
3. Use electronic access control (badge, PIN) for sensitive areas.
4. Review access logs and video for anomalies: after-hours access, repeated failed badge attempts.

**For the Security Engineer:**
- Reference: NIST 800-53 PE-6 · PCI DSS Req 9.1.1
- Evidence: Video retention configuration, access logs, anomaly review evidence
- Cadence: Monthly (review), Daily (video retention check)

**Tool Mappings:**
✅ Badge access system (Lenel, HID, Brivo) — electronic access control
✅ IP video surveillance (Axis, HikVision, Verkada) — cloud-managed video
❌ No physical access monitoring — you will not know if someone entered the server room

**Verification:**
- Can you view video from 60 days ago? (Test quarterly.)
- Badge access log from last weekend: any entries without corresponding work orders?
- Any sensitive area with no badge access or video? Identify and remediate.

**Common Mistakes:**
- Video recorded but not retained. 30-day retention is not enough for PCI (90 days minimum).
- Video camera pointing in the wrong direction. Verify camera coverage quarterly.
- Badge access logs not reviewed. Logs are checked only after an incident.

**If You Cannot Implement This:**
At minimum, use a badge system for server room access. Log who enters and when.

---

### PL-2 System Security Plan — Tier: Core

**Statement:** Authoritative system security plans exist for all in-scope systems. SSPs are current, accurate, and reviewed annually.

**For the IT Generalist:**
1. Create an SSP for each system in regulatory scope (or at minimum, for each critical system).
2. SSP structure: system name, owner, data classification, regulatory scope, system boundary diagram, control implementation status.
3. Review SSPs annually. Update when the system changes significantly.
4. Link the SSP to the evidence library — each control reference should point to the evidence artifact.

**For the Security Engineer:**
- Reference: NIST 800-53 PL-2 · NIST RMF Step 2
- Evidence: Current SSP, annual review record, change log
- Cadence: Annual (review), On significant change (update)

**Tool Mappings:**
✅ CERG TMPL-SCP-001 — system control profile template
✅ CERG TMPL-CUI-001 — SSP template for CUI systems
◐ SharePoint / Confluence — document storage
❌ No SSP — cannot pass RMF Step 2, direct CMMC finding

**Verification:**
- Every system marked Critical has a current SSP?
- SSP review date: within the last 12 months?
- System boundary diagram: accurate as of the last review?

**Common Mistakes:**
- SSP written once and never reviewed. Systems change. Update SSPs annually.
- SSP without evidence references. "Control AC-2 is implemented" — prove it. Link to the evidence.
- SSP stored where no one can find it. SSPs go in the evidence library, accessible to the system owner.

**If You Cannot Implement This:**
Start with one SSP for the most important system. Use the CERG SSP template. Expand to other systems over time.

---

### PM-2 Risk Management Strategy — Tier: Core

**Statement:** Risk appetite, tolerance thresholds, and decision authority are documented and communicated to leadership.

**For the IT Generalist:**
1. Work with the CISO to document: what level of risk is the organization willing to accept?
2. Define thresholds: Critical risk (score 15+) → CISO or board approval. High (12-14) → CISO approval. Medium (8-11) → Risk owner + governance approval.
3. Define what happens when risk exceeds appetite: mandatory remediation, compensating controls, or executive escalation.
4. Review risk posture quarterly with leadership.

**For the Security Engineer:**
- Reference: NIST 800-53 PM-9 · ISO 27001 A.8.2
- Evidence: Risk appetite statement, risk tolerance thresholds, decision authority table
- Cadence: Annual (review), Quarterly (posture reporting)

**Verification:**
- Is there a documented risk appetite statement? Last reviewed?
- Are there risks in the register that exceed the stated appetite? Flag and escalate.
- Does the board see risk reports? At least annually.

**Common Mistakes:**
- Risk appetite undefined. If you have not stated what risk you accept, you accept all risk by default.
- Risk appetite too vague. "We accept moderate risk" — define moderate. Score thresholds.
- Risk decisions made without authority validation. A risk acceptance signed by someone without the authority to accept it is not valid.

**If You Cannot Implement This:**
At minimum, document: who can accept risks at each severity level. Get CISO sign-off.

---

### PM-3 Information Security Program Plan — Tier: Core

**Statement:** The security program is documented with scope, governance, resource plan, and maturity targets.

**For the IT Generalist:**
1. Document the security program scope: which systems, locations, and regulations are covered.
2. Define program governance: who owns what (CISO, pillars, steering committee).
3. Document the resource plan: headcount, budget, tooling.
4. Set maturity targets: where are we today? Where are we going in 12 months?

**For the Security Engineer:**
- Reference: NIST 800-53 PM-1 · ISO 27001 A.5.1
- Evidence: Program charter, budget documentation, maturity scorecard
- Cadence: Annual

**Verification:**
- Security program charter exists? Reviewed this year?
- Budget documented? (Do not need to share actuals, but the plan should exist.)
- Maturity target for the next 12 months: documented and realistic?

**Common Mistakes:**
- No program plan. "We do security" is not a plan. Write it down.
- Plan without resource commitment. "We will implement all controls" without budget or staff is aspirational.
- Plan not reviewed. If you wrote it 3 years ago and never looked at it again, it is outdated.

**If You Cannot Implement This:**
Write a one-page security program plan: scope, governance, and targets for the next 12 months.

---

### SA-2 Software Supply Chain Integrity — Tier: Core

**Statement:** Third-party software is verified for supply chain integrity before deployment.

**For the IT Generalist:**
1. Require an SBOM (Software Bill of Materials) from software vendors.
2. Scan the SBOM for known vulnerabilities using Dependency-Track, Snyk, or Trivy.
3. Verify the software's digital signature. Confirm it is signed by the vendor's trusted certificate.
4. For open-source dependencies: verify against the official source and check the SHA256 checksum.

*Trivy: Scan a software container for vulnerabilities:*
```bash
trivy image --severity HIGH,CRITICAL myapp:latest
trivy sbom vendor-sbom.json
```

**For the Security Engineer:**
- Reference: NIST 800-53 SR-4 · SLSA framework · PCI DSS Req 6.4.3
- Evidence: SBOM inventory, vulnerability scan results, signature verification logs
- Cadence: Per acquisition, Quarterly (re-scan)

**Tool Mappings:**
✅ Dependency-Track — open-source SBOM analysis, continuous monitoring
✅ Snyk — SBOM import, fix advice
✅ Trivy — OSS vulnerability scanning for containers and code
✅ GitHub Dependabot — automated dependency vulnerability alerts
❌ No software supply chain verification — SolarWinds-type compromise invisible

**Verification:**
- Top 10 vendors: do you have SBOMs for their software?
- Any software on your systems with known critical CVEs from the last 60 days?
- Last time you verified a software vendor's distribution integrity?

**Common Mistakes:**
- SBOM collected but not scanned. Having an SBOM does nothing without vulnerability analysis.
- Skip supply chain checks for small/unknown vendors. Small vendors are targeted for supply chain attacks precisely because customers skip checks.
- No verification of open-source mirrors. Use official sources or verified mirrors.

**If You Cannot Implement This:**
Start with your top 5 most critical software vendors. Request SBOMs. Scan with Dependency-Track (free, open-source).

---



**Threat Intel Validation — CI/CD Pipeline Attacks:**
The Miasma malware campaign (June 2026) compromised npm packages and GitHub Actions runners to inject malicious code into the software supply chain. The Shai Hulud operation (June 2026) exploited CI/CD credentials to exfiltrate data from Redshift databases. Both attacks exploited gaps in pipeline security that standard vendor assessment does not cover.

**Additional Guidance for Pipeline Security:**

*For the IT Generalist:*
1. Lock down your CI/CD pipeline: restrict which branches can trigger production deployments.
2. Require code review before any production pipeline run. No direct commits to main.
3. Scan dependencies for known vulnerabilities before every build — not just periodically.
4. Pin dependency versions. Do not use version ranges (^1.2.3) that automatically pull new releases without review.
5. Rotate CI/CD credentials (API keys, service principals, deployment tokens) every 90 days.

*GitHub: Dependency review in pull requests:*
```yaml
# .github/workflows/dependency-review.yml
name: Dependency Review
on: [pull_request]
jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
        with:
          fail-on-severity: high
```

*Dependency pinning (npm):*
```json
{
  "dependencies": {
    "express": "4.18.2",  // Pinned: no ^ or ~
    "lodash": "4.17.21"   // Pinned: exact version only
  }
}
```

**Tool Mappings (pipeline-specific):**
✅ GitHub Dependabot — automated dependency vulnerability alerts + auto-fix PRs
✅ GitHub Secret Scanning — detects credentials in source code
✅ Renovate — dependency update automation with review
✅ Snyk — dependency scanning, license compliance
❌ Unpinned dependencies with version ranges — automatic vulnerable dependency inclusion

**Verification:**
- Check the CI/CD pipeline: are there any direct push triggers to main/production?
- Dependency scan: run against your primary application — any high/critical findings?
- Secret scan: any credentials in the source code?

*Threat references:* Miasma npm supply chain (June 2026), Shai Hulud CI/CD exfil (June 2026)

### AU-9 Non-Repudiation — Tier: Core

**Statement:** Actions are attributable to a named individual. Users cannot deny performing an action.

**For the IT Generalist:**
1. Every user has a unique ID. No shared accounts — this is the foundation of non-repudiation.
2. Enable detailed audit logging for sensitive actions: user creation, privilege changes, data access, configuration changes.
3. Centralize logs so they cannot be altered by the user who performed the action.
4. For financial transactions: require two-person approval for high-value actions.

**Tool Mappings:**
✅ SIEM (Sentinel, Splunk) — centralized, immutable audit trail
✅ PAM (CyberArk) — session recording, keystroke capture
❌ Shared accounts — non-repudiation impossible

**Verification:**
- Can you determine who performed every admin action in the last 30 days?
- Any actions logged with a shared account? This breaks non-repudiation.

**Common Mistakes:**
- Shared accounts for convenience. Breaks non-repudiation entirely.
- Logs stored on the same system that performed the action. Logs can be altered. Centralize.
- No session recording for privileged actions. A log shows a command was run but not by whom.

**If You Cannot Implement This:**
At minimum, eliminate shared admin accounts. Every user gets a unique ID.

---

### CP-5 Telecommunications Resilience — Tier: Core

**Statement:** Critical communication paths (internet, WAN, voice) have redundancy to maintain operations during an outage.

**For the IT Generalist:**
1. Identify which communication paths are critical: internet (primary + backup), WAN links, voice.
2. Maintain diverse paths: two different ISPs, different physical paths into the building.
3. Test failover: disconnect the primary ISP — does traffic automatically route to the backup?
4. Document failover procedures: who triggers it, what to expect, how to verify it worked.

**For the MSP:**
- Dual ISP for each client site. Diverse paths (fiber + cellular or two fiber providers).
- Failover tested quarterly.
- Cellular backup for critical management access.

**For the Security Engineer:**
- Reference: NIST 800-53 CP-8
- Evidence: Circuit inventory, failover test results, SLA documents
- Cadence: Quarterly (test)

**Tool Mappings:**
✅ Dual ISP — primary + backup, diverse paths
✅ SD-WAN (VeloCloud, Meraki) — automatic failover
✅ Cellular failover (Cradlepoint, Peplink) — backup WAN
❌ Single ISP — single point of failure for all external communications

**Verification:**
- Disconnect the primary ISP. Can you reach the internet within 2 minutes?
- Last failover test: when? Documented outcome?
- Cellular backup: is the data plan active and paid?

**Common Mistakes:**
- Two ISPs using the same physical infrastructure. A backhoe cuts both. Verify diverse paths.
- Failover tested manually but automatic failover never verified. Pull the plug, do not just run a test command.
- No cellular backup. Internet outage also kills remote management.

**If You Cannot Implement This:**
At minimum, have a cellular hotspot available as backup for critical management systems.

---

### IA-7 Non-Organizational User Authentication — Tier: Core

**Statement:** External users (partners, vendors, customers) are authenticated to the same standard as employees.

**For the IT Generalist:**
1. Guest users: require MFA. Use the same IdP as employee authentication.
2. External identity federation: configure trusted IdPs (Entra ID B2B, Okta Org2Org).
3. Set guest access expiration. No permanent guest accounts.
4. Remove guest accounts that have not authenticated in 90 days.

*Entra ID: Configure B2B collaboration:*
```powershell
# Set guest invite settings
Set-MgPolicyAuthorizationPolicy -AllowInvitationsFrom "adminsAndGuestInviters"

# Review guest users
Get-AzureADUser -All $true | Where-Object {$_.UserType -eq "Guest"}
```

**For the Security Engineer:**
- Reference: NIST 800-53 IA-8 · SC-8
- Evidence: External auth policy, federation configuration, guest access review
- Cadence: Quarterly (review)

**Verification:**
- Guest users: all with MFA enabled? Any without?
- Guest accounts not authenticated in 90+ days? Remove or re-invite.
- External identity federation: only trusted IdPs configured?

**Common Mistakes:**
- Guest users not subject to MFA. Guest user MFA is a configuration toggle, not automatic.
- No guest expiration. Guest accounts accumulate over years.
- Federation trust too broad. Trust all IdPs in a partner organization.

**If You Cannot Implement This:**
At minimum, create separate accounts for external users in the same IdP. Apply MFA.

---

### PS-2 Personnel Termination — Tier: Core

**Statement:** When personnel leave the organization, their access is revoked immediately and their return of assets is verified.

**For the IT Generalist:**
1. Receipt termination notice from HR. Immediately:
   - Disable the user's account (do not delete — preserve for investigation).
   - Revoke all active sessions.
   - Reset any application-specific passwords.
   - Notify the system owner(s) for systems the user had access to.
2. Arrange return of assets: laptop, badge, phone, keys, access cards.
3. Within 7 days: verify that all access is revoked and all assets are returned.
4. Within 30 days: archive the user's data. Delete the account after 30 days.

*Automated termination checklist:*
```powershell
# Revoke all sessions immediately
Revoke-MgUserSignInSession -UserId "user@domain.com"

# Disable account
Update-MgUser -UserId "user@domain.com" -AccountEnabled:$false

# Remove from all groups
Get-MgUserMemberOf -UserId "user@domain.com" | ForEach-Object {
    Remove-MgGroupMember -GroupId $_.Id -MemberId "user@domain.com"
}

# Verify MFA tokens are revoked
Revoke-MgUserAuthenticationMethod -UserId "user@domain.com"
```

**For the MSP:**
- Termination automation: IdP-connected to HR system.
- If not automated: within 1 hour of notice, disable account manually.
- Asset return: track in the asset management tool. Notify IT of unreturned assets.

**For the Security Engineer:**
- Reference: NIST 800-53 PS-4 · ISO 27001 A.7.3.1
- Evidence: Termination checklist, account revocation logs, asset return records
- Cadence: Per termination event

**Tool Mappings:**
✅ Entra ID Lifecycle Workflows — automated termination
✅ Okta — deprovisioning integration with HR
✅ RMM tool — remote wipe capability
❌ Manual termination with delay — data exfiltration window

**Verification:**
- Disable a test account in HR. Is it disabled in the IdP within 30 minutes?
- Last termination: was the checklist completed? (All systems checked, not just email.)
- Any former employees with active accounts? (Monthly review.)

**Common Mistakes:**
- Account disabled but still in distribution lists/mailboxes with send-as permissions.
- MFA tokens not revoked. User's saved MFA sessions remain valid for token lifetime.
- No verification step. "I disabled the account" assumed but not verified. Check it.

**If You Cannot Implement This:**
At minimum, disable the account within 24 hours of notification. This prevents login but does not revoke active sessions.

---

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


### SI-7 Security Function Verification — Tier: Core

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
