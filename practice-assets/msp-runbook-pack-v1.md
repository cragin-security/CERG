# CERG MSP Runbook Pack v1
| | |
|---|---|
| **Document ID** | CERG-PA-MSP-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CERG Practice Lead |

**Purpose:** Per-control playbook for MSPs deploying CERG across 10+ clients simultaneously.
**Target audience:** MSP delivery teams (Tier 1-2 support, delivery engineers, compliance leads)
**Scale:** Designed for MSPs managing 5-200 clients

---

## 1. MSP Operating Model for CERG

### Client Tiering

| Tier | Client Profile | CERG Depth | Billing Model |
|------|---------------|------------|---------------|
| Bronze | <20 users, no regulatory pressure | Tier 1 (MVC + 40 controls) | Bundled in managed services |
| Silver | 20-200 users, basic compliance | Tier 2 (MVC + standards + 60 controls) | +$500-1000/mo |
| Gold | 200-1000 users, regulated | Tier 3 (full 99 controls + regulatory overlay) | +$2000-5000/mo |
| Platinum | 1000+ users, multi-regulator | Tier 4 (full + GRC tool + continuous evidence) | $5000-15000/mo |

### Multi-Tenant Architecture

```text
┌─────────────────────────────────────────────┐
│              MSP Security Stack              │
│  ┌─────────┐  ┌─────────┐  ┌──────────────┐ │
│  │ Sentinel │  │ Sentinel│  │ Kaseya /   │ │
│  │ SIEM     │  │One EDR  │  │ ConnectWise  │ │
│  └─────────┘  └─────────┘  └──────────────┘ │
│  ┌─────────┐  ┌─────────┐  ┌──────────────┐ │
│  │ Veeam    │  │ Entra   │  │ MSP PSA     │ │
│  │ Backup   │  │ID per   │  │ (ticketing)  │ │
│  │ (multi)  │  │client   │  │              │ │
│  └─────────┘  └─────────┘  └──────────────┘ │
└─────────────────────────────────────────────┘
         │           │             │
    ┌────┘     ┌─────┘      ┌─────┘
    ▼          ▼            ▼
Client A    Client B    Client C
```

---

## 2. Per-Control MSP Playbook

Each playbook entry covers: **what to do / how often / what to bill / what evidence to keep**

### AC-1: Access Control Policy

| Attribute | Value |
|-----------|-------|
| **MSP action** | Template the master policy. Change client name, approver names, systems list. |
| **Cadence** | Create during onboarding. Review during QBR (quarterly). |
| **Evidence** | Policy document with client name, approver, review date. Store in client SharePoint. |
| **Billing** | Included in onboarding. QBR review is included in tier. |
| **Escalate if** | Client refuses to name an approver or review the policy within 12 months. |

### AC-2: Account Lifecycle Management

| MSP action | Script: weekly orphan account detection across all client tenants. Automated disable for accounts >90d inactive. |
|------------|---------------------------------------------------------------------------------------------------------------|
| Cadence | Continuous (HR → IdP integration). Weekly orphan scan. Quarterly recertification. |
| Automation | `connect-msgraph -tenant $ClientTenantId; Get-MgUser -Filter "accountEnabled eq true" | Where-Object { $_.Manager -eq $null }` |
| Billing | HR integration setup: one-time project fee. Quarterly recertification: included in Silver+ tiers. |
| Escalate if | Client does not provide HR roster for comparison. |

### AC-3: Access Enforcement

| MSP action | Block legacy auth at tenant level during onboarding. Deploy LAPS to all on-prem AD clients. Monthly local admin audit. |
|------------|---------------------------------------------------------------------------------------------------------------------|
| Cadence | One-time setup (legacy auth). Monthly (local admin audit). |
| Automation | `New-MgIdentityConditionalAccessPolicy -DisplayName "Block Legacy Auth - $ClientName" -State "enabled" -GrantControls @{ BuiltInControls = @("Block") }` |
| Billing | Included in onboarding. Monthly audit is standard SOC work. |

### AC-4: Least Privilege

| MSP action | Enable Entra PIM for all privileged roles. Move all users from permanent admin to eligible. Monthly privileged group report. |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| Cadence | One-time PIM setup. Monthly privileged membership report. |
| Script | `Get-MgRoleManagementDirectoryRoleAssignment | Where-Object PrincipalType -eq "User" | Export-Csv "$ClientName-privileged-roles.csv"` |
| Billing | PIM setup: project fee. Monthly report: included. |
| Escalate if | Client has >10 Domain Admins or refuses to remove permanent admin assignments. |

### IA-1: Multi-Factor Authentication

| MSP action | Enable MFA via CA for all client users. Block legacy auth. Weekly MFA enrollment report. |
|------------|------------------------------------------------------------------------------------------|
| Cadence | One-time setup. Weekly enrollment check. |
| Evidence | CA policy export + enrollment report showing >98% |
| Escalate if | Client refuses MFA for any user group. Document as risk acceptance. |

### RA-2: Vulnerability Scanning

| MSP action | Weekly external scan + monthly internal scan per client. SLA report. |
|------------|----------------------------------------------------------------------|
| Cadence | Weekly (internet-facing). Monthly (internal). |
| Tool | Qualys VMDR (multi-tenant) or Wiz (cloud-native clients). |
| Billing | Scanning: included in Silver+ tiers. Report review: billable project time for remediation planning. |
| Escalate if | Critical findings past 7-day SLA not patched. |

### IR-1: Incident Response Plan

| MSP action | Create 2-page IR plan per client. Keep offline copy accessible. Annual tabletop. |
|------------|----------------------------------------------------------------------------------|
| Cadence | Create during onboarding. Update contacts quarterly. Tabletop annually. |
| Billing | Plan creation: onboarding. Tabletop facilitation: billable (half-day). |
| Escalate if | Client will not identify an Incident Commander. |


### AU-1: Audit Logging Configuration

| Attribute | Value |
|-----------|-------|
| **MSP action** | Enable unified audit logging across all client tenants. Route all logs to MSP SIEM (Sentinel/co-managed). Configure retention per client tier (Gold: 1 year, Silver: 6 months, Bronze: 90 days). |
| **Cadence** | Enable during onboarding. Quarterly log source audit. |
| **Automation** | `Set-MgIdentityConditionalAccessPolicy` for sign-in logs. Azure Policy to enforce diagnostic settings on all subscriptions. |
| **Billing** | SIEM ingestion: passed through (billable per GB). Configuration: included in onboarding. |
| **Escalate if** | Any client refuses to enable logging on domain controllers or Entra ID. |

### AU-2: Audit Log Review

| Attribute | Value |
|-----------|-------|
| **MSP action** | Deploy weekly SIEM review schedule per client. Analyst triages: failed logins, privilege changes, anomalous behavior. Maintain case notes per client. |
| **Cadence** | Weekly review (all tiers). Daily for Platinum (dedicated SOC analyst). |
| **Automation** | Scheduled Sentinel analytics rules with automated incident creation. Escalate confirmed incidents to client security contact. |
| **Billing** | Included in managed security tier. Platinum: dedicated analyst surcharge. |
| **Escalate if** | Client has >100 failed logins/day with no MFA — escalate as imminent breach risk. |

### AU-4: Audit Record Retention

| Attribute | Value |
|-----------|-------|
| **MSP action** | Configure log retention per client regulatory requirement. Gold/SOX: 7 years. CMMC: 1 year minimum. Bronze/Silver: 90 days (default). Archive cold logs to Azure blob/GCS nearline. |
| **Cadence** | Set during onboarding. Review quarterly for regulatory changes. |
| **Automation** | Azure Policy `Deploy-LogAnalyticsRetention` enforced per client subscription. Retention policies in centralized Log Analytics workspace. |
| **Billing** | Cold storage: minimal cost, passed through. Configuration: included. |
| **Escalate if** | Client regulatory requirement supersedes budget — must document risk acceptance for shorter retention. |

### CM-1: Configuration Baseline (DISH)

| Attribute | Value |
|-----------|-------|
| **MSP action** | Create per-client security baseline using DISH (Document, Implement, Scan, Harden) method. Deploy via Intune/GPO with standard templates for Windows Server, M365, and common LOB apps. |
| **Cadence** | Create during onboarding. Review during QBR. |
| **Automation** | Intune security baselines (Windows 10/11, Edge, Defender). GPOs for on-prem AD clients. Azure Policy for subscriptions. |
| **Billing** | Baseline creation: project fee ($2-5k per client depending on complexity). QBR review: included. |
| **Escalate if** | Client runs unsupported OS or refuses to apply any baseline. |

### CM-2: Change Control

| Attribute | Value |
|-----------|-------|
| **MSP action** | Deploy MSP-accessible change calendar shared per client. All firewall, policy, and admin changes go through ticketing (PSA integration). No-change window: client business hours. |
| **Cadence** | Continuous through PSA. Weekly change review meeting. |
| **Automation** | PSA (ConnectWise/Autotask) with change request template. Pre-approved change types: AV signature updates, threat intel feed updates, emergency patches (with post-hoc approval). |
| **Billing** | Included in managed security. Emergency change after-hours: billable at 1.5x. |
| **Escalate if** | Client bypasses change control — escalate to client management and document exception. |

### CM-8: System Component Inventory

| Attribute | Value |
|-----------|-------|
| **MSP action** | Maintain per-client hardware/software inventory in PSA. Weekly delta scan via RMM. Flag unknown devices and unlicensed software. |
| **Cadence** | Continuous discovery. Weekly delta report. |
| **Automation** | RMM (Kaseya/ConnectWise Automate) auto-discovery. Service graph from Entra ID + Intune + Defender for Endpoint. |
| **Billing** | Included in managed security tier. Manual inventory cleanup (initial): project fee. |
| **Escalate if** | Client has >10% unknown devices or refuses to allow agent deployment. |

### CP-1: System Backup

| Attribute | Value |
|-----------|-------|
| **MSP action** | Deploy per-client backup strategy: M365 backup (Datto/Barracuda/AvePoint), server/image backup (Veeam/Datto), cloud resource backup (Azure Backup/AWS Backup). Test restore quarterly. |
| **Cadence** | Daily backup. Weekly health check. Quarterly restore test. |
| **Automation** | Veeam backup reports emailed weekly. Azure Backup health alerts to MSP SIEM. Restore test script: `./test-restore.ps1 -client $Name -vm $CriticalVM` |
| **Billing** | Backup licensing: passed through. Restore test: included in Gold/Platinum. Silver: billable per test. |
| **Escalate if** | Last successful backup >48 hours ago for any critical system. |

### CP-2: Recovery Planning

| Attribute | Value |
|-----------|-------|
| **MSP action** | Create one-page RTO/RPO document per client during onboarding. Identify critical systems, backup methods, and recovery steps. Annual tabletop exercise. |
| **Cadence** | Create during onboarding. Review during QBR. Tabletop annually. |
| **Evidence** | RTO/RPO document signed by client. Tabletop after-action report (with findings). |
| **Billing** | Document creation: included in onboarding. Tabletop facilitation: billable (half-day, $1-2k). |
| **Escalate if** | Client refuses to designate critical systems or accept any RTO. |

### IA-2: Password Policy

| Attribute | Value |
|-----------|-------|
| **MSP action** | Enforce NIST 800-63B password policy per client tenant: ban common passwords, no rotation requirement, minimum 12 chars. Enable Entra Password Protection for all cloud/on-prem. |
| **Cadence** | Configure during onboarding. Audit mismatch quarterly. |
| **Automation** | Entra Password Protection (global banned list + per-tenant custom list). GPO: `MinimumPasswordLength = 12`, `PasswordHistoryCount = 24`. |
| **Billing** | Included in onboarding. Password audit report: automated, included. |
| **Escalate if** | Client refuses to enforce minimum password length >8 characters. |

### IA-3: Service Account Management

| Attribute | Value |
|-----------|-------|
| **MSP action** | Inventory all service accounts per client. Convert to managed identities or gMSAs where possible. 90-day rotation on accounts that can't migrate. Exclude from CA policies that block non-interactive logins. |
| **Cadence** | Inventory during onboarding. Quarterly rotation check. |
| **Automation** | `Get-MgServicePrincipal -All` for Entra ID service principals. `Get-ADServiceAccount -Filter *` for on-prem gMSAs. Scheduled runbook for password rotation. |
| **Billing** | Service account cleanup: project fee (one-time). Rotation: included. |
| **Escalate if** | Any shared service account with standalone credentials used across multiple clients. |

### RA-1: Risk Assessment

| Attribute | Value |
|-----------|-------|
| **MSP action** | Maintain per-client risk register from day one. Seed with standard MSP risks (MFA not enforced, no IR plan, shared admin model). Update during QBRs and after incidents. |
| **Cadence** | Seed during onboarding. Review at QBR. Update on incident. |
| **Template** | Use `CERG-TMPL-RM-001` or CERG practice risk register bootstrap. Store in client SharePoint with quarterly review date.
| **Billing** | Risk register maintenance: included in managed security tier. Full risk assessment (new clients): project fee. |
| **Escalate if** | Client has >3 HIGH risks past 90 days with no remediation plan. |

### RA-3: Vulnerability Remediation

| Attribute | Value |
|-----------|-------|
| **MSP action** | Patch critical vulns within 7 days (14 days for high) per client. Use RMM patching + cloud update rings. Report SLA compliance monthly. |
| **Cadence** | Weekly patch cycle. Emergency patches within 24 hours. |
| **Automation** | RMM patch policies (Kaseya/ConnectWise). Intune update rings for endpoints. Azure Update Manager for servers. |
| **Billing** | Patching: included in all tiers. Emergency out-of-cycle patching: billable (1.5x labor). |
| **Escalate if** | Critical patch older than 7 days unapplied (escalate to client IT manager). |

### SI-1: Malware Protection

| Attribute | Value |
|-----------|-------|
| **MSP action** | Deploy EDR on all endpoints per client. Standard: SentineOne or Defender for Business. Cloud-only: Defender for Cloud Apps. Centralized alerting to MSP SIEM. Block all unsigned executables at the edge. |
| **Cadence** | Deploy during onboarding. Daily agent health check. Weekly alert review. |
| **Automation** | RMM script: `Deploy-SentinelOne.ps1 -siteGroup $ClientName -siteToken $Token`. Defender policy via Intune security baseline. EDR health dashboards in MSP SIEM. |
| **Billing** | EDR licensing: passed through. Response to confirmed incident: billable per-hour or retainer. |
| **Escalate if** | Any endpoint without active EDR agent >24 hours. |

### SI-2: File Integrity Monitoring

| Attribute | Value |
|-----------|-------|
| **MSP action** | Deploy FIM on critical systems (domain controllers, file servers, SQL servers). Baseline system files on onboarding. Alert on unauthorized changes. |
| **Cadence** | Configure during onboarding. Weekly baseline comparison. |
| **Automation** | Wazuh FIM (open source, multi-tenant). Defender for Cloud FIM for Azure VMs. Sentinel rule alerts on `SecurityEvent 4656` (handle to object). |
| **Billing** | Included for Gold+. Silver: additional fee for FIM configuration ($500/client setup). |
| **Escalate if** | Critical system file change without corresponding change ticket. |

### SC-1: Network Segmentation

| Attribute | Value |
|-----------|-------|
| **MSP action** | Audit client network segmentation during onboarding. Ensure: management VLAN isolated from user VLAN, guest WiFi isolated from corp network, OT/ICS isolated with one-way diode or firewall. |
| **Cadence** | Assess during onboarding. Review at QBR or on network change. |
| **Evidence** | Network diagram (client-owned, MSP-reviewed). Firewall rule review (quarterly). |
| **Billing** | Network segmentation assessment: project fee ($2-5k depends on scope). Rule review: included. |
| **Escalate if** | Client flat network with no firewall between user and server VLANs. |

### SC-7: Remote Access Security

| Attribute | Value |
|-----------|-------|
| **MSP action** | Enforce VPN with MFA for all remote access. Block RDP directly to servers (use bastion/jump box). Deploy JIT access for admin portals. |
| **Cadence** | Configure during onboarding. Monthly access review. |
| **Automation** | Entra CA policy: block all sign-ins from non-compliant devices + require MFA for VPN. Azure Bastion for VM access. Conditional Access: session control for admin portals. |
| **Billing** | VPN licensing: passed through. Configuration: included. JIT/PIM setup: project fee. |
| **Escalate if** | Any admin account with direct RDP access to domain controllers. |

### AT-1: Security Awareness Training

| Attribute | Value |
|-----------|-------|
| **MSP action** | Deploy per-client security awareness training (KnowBe4 or M365 Attack Simulator). Mandatory annual training + quarterly phishing simulations. Report completion rates and click rates. |
| **Cadence** | Annual training. Quarterly phishing simulation. Monthly new-hire onboarding. |
| **Evidence** | Training completion report (>90% required). Phishing simulation results (click rate <10% target). |
| **Billing** | Training platform license: passed through. Campaign management: included. |
| **Escalate if** | >25% phishing click rate or <70% training completion after 90 days. |

### PE-1: Physical Security

| Attribute | Value |
|-----------|-------|
| **MSP action** | For client-owned data centers/server rooms: audit badge access, camera coverage, visitor logs. For cloud-only clients: review cloud provider physical security certifications (SOC 2 Type II, ISO 27001). |
| **Cadence** | Initial assessment during onboarding. Annual review for on-prem. Inherited assessment for cloud. |
| **Evidence** | Access log review (quarterly). Visitor log spot-check. Inherited: provider SOC 2 / ISO cert copy. |
| **Billing** | On-prem physical assessment: project fee (per site). Cloud inherited: included. |
| **Escalate if** | Unbadged access to server room or shared data center rack with no lock. |

### PL-1: Security Planning

| Attribute | Value |
|-----------|-------|
| **MSP action** | Create per-client 12-month security roadmap during onboarding. Define maturity target, budget milestones, and regulatory deadlines. Review quarterly. |
| **Cadence** | Create during onboarding. Update at QBR. |
| **Template** | Use CERG `ORGANIZATION_ADAPTATION_PROFILE` as starting point. Roadmap covers: T1 foundations (Q1), T2 structure (Q2), T3 compliance (Q3-Q4 dependent on regulatory pressure). |
| **Billing** | Roadmap creation: included in onboarding. QBR: included in tier. |
| **Escalate if** | Client has no budget allocated for any security improvements. |

### PM-1: Program Management

| Attribute | Value |
|-----------|-------|
| **MSP action** | Assign a delivery lead per client. Monthly status report: controls implemented, findings open, SLA compliance, upcoming work. Quarterly executive summary for client leadership. |
| **Cadence** | Monthly status. Quarterly executive. Pre-QBR evidence collection (automated). |
| **Evidence** | Monthly status report (template). QBR deck. Evidence package collected before each QBR. |
| **Billing** | Delivery lead: included in tier. Executive QBR: included. Custom reporting beyond template: billable. |
| **Escalate if** | Client executive declines three consecutive QBR invitations. |

### PS-1: Personnel Security

| Attribute | Value |
|-----------|-------|
| **MSP action** | Verify client has background check policy for all employees with system access. Confirm third-party background check vendor is used. Annual review of access list for departed employees. |
| **Cadence** | Check during onboarding. Offboarding verification: monthly (automated). |
| **Automation** | Entra ID `Get-MgAuditLogSignIn` cross-reference with HR offboarding feed. MSP's own staff: background check on hire + annual refresh. |
| **Billing** | Offboarding verification: included. Background check administration for MSP staff: included in overhead. |
| **Escalate if** | Client ex-employee has active account >30 days after termination. |

### SA-1: System Acquisition

| Attribute | Value |
|-----------|-------|
| **MSP action** | Review new system/application requests against CERG security baseline. Quick checklist: auth method (MFA?), data classification, logging capability, vendor SOC 2. Block deployment if fails checklist. |
| **Cadence** | Per-request (architecture review gate). |
| **Automation** | PSA ticket with intake checklist template. Pre-approved: M365/Entra integrated apps with no data export to unsanctioned storage. Requires review: any app with API access to client data. |
| **Billing** | Architecture review: included (up to 1 hour/request). Beyond 1 hour: billable project time. |
| **Escalate if** | Client procures system without MSP security review. |

### SR-1: Vendor Risk Assessment

| Attribute | Value |
|-----------|-------|
| **MSP action** | Maintain per-client vendor register. For each vendor: collect SOC 2 (or equivalent), confirm data handling, review breach notification clause. Prioritize vendors with access to client data. |
| **Cadence** | Add during onboarding. Annual review. Re-assess on breach notification or contract renewal. |
| **Evidence** | Vendor register with SOC 2 collection status. Breach notification policy from each vendor. |
| **Billing** | Vendor register setup: project fee. Annual review: included (up to 10 vendors). Additional vendors: billable. |
| **Escalate if** | Any vendor with client data refuses to provide SOC 2 or equivalent. |

### MA-1: Media Protection

| Attribute | Value |
|-----------|-------|
| **MSP action** | For MSPs handling client media (backup tapes, decommissioned drives): encrypt all media, maintain chain of custody log, use certified destruction service with certificate. |
| **Cadence** | Per-event. Annual destruction audit. |
| **Evidence** | Chain of custody form. Destruction certificate from certified vendor. |
| **Billing** | Media handling: included in managed services. Certified destruction service: passed through. |
| **Escalate if** | Any client media not tracked or destroyed without certificate. |

### CA-1: Security Assessment

| Attribute | Value |
|-----------|-------|
| **MSP action** | Annual external penetration test per client (or inherited from shared assessment for Bronze/Silver). Remediate findings within SLA: Critical 14 days, High 30 days. |
| **Cadence** | Annual pen test. Quarterly vulnerability scan (included in RA-2). |
| **Billing** | Bronze/Silver: shared assessment (inherited, lower cost). Gold/Platinum: dedicated pen test (passed through, $10-25k). |
| **Escalate if** | Critical finding past 14-day SLA with no remediation plan. |

### MP-1: Mobile Device Management

| Attribute | Value |
|-----------|-------|
| **MSP action** | Deploy MDM (Intune) on all client mobile devices accessing corporate data. Require: device PIN, encryption, compliant OS version. Remote wipe capability enabled. Block rooted/jailbroken devices. |
| **Cadence** | Configure during onboarding. Weekly compliance report. |
| **Automation** | Intune compliance policy: require device encryption + minimum OS version. CA: block access from non-compliant devices. |
| **Billing** | MDM licensing: passed through. Configuration: included. |
| **Escalate if** | >10% of devices non-compliant or any device without MDM enrollment. |



---

## 3. Multi-Tenant Automation Scripts

### Weekly Orphan Account Detection (runs across all clients)

```powershell
# cerg-weekly-orphan-check.ps1
$clients = Import-Csv "C:\MSP\clients.csv"
foreach ($client in $clients) {
    Connect-MgGraph -TenantId $client.TenantId
    $orphans = Get-MgUser -All -Filter "accountEnabled eq true" -Property DisplayName,UserPrincipalName,Manager |
        Where-Object { $_.Manager -eq $null }
    if ($orphans) {
        $orphans | Export-Csv "C:\MSP\Reports\$($client.Name)-orphans-$(Get-Date -Format yyyy-MM).csv"
        Send-MailMessage -To $client.SecurityContact -Subject "Orphan Accounts Found" -Body "Review attached"
    }
    Disconnect-MgGraph
}
```

### Monthly Access Recertification (generates report for client to approve)

```powershell
# cerg-monthly-recert.ps1
param($ClientName, $TenantId, $OutputDir)
Connect-MgGraph -TenantId $TenantId
$users = Get-MgUser -All -Property DisplayName,UserPrincipalName,Department,JobTitle
$users | Select-Object DisplayName, UserPrincipalName, Department, JobTitle |
    Export-Csv "$OutputDir\$ClientName-recert-$(Get-Date -Format yyyy-MM).csv" -NoTypeInformation
Disconnect-MgGraph
```

### Automated Evidence Collection Scheduler

```yaml
# cerg-evidence-schedule.yaml
clients:
  - name: ClientA
    tenant_id: tenant-a.onmicrosoft.com
    evidence:
      - control: IA-1
        source: mfa_report
        schedule: weekly
        query: SigninLogs | where AuthenticationRequirement != "multiFactorAuthentication"
      - control: AC-2
        source: orphan_accounts
        schedule: weekly
        query: Get-MgUser | Where-Object Manager -eq $null
      - control: RA-2
        source: vuln_scan
        schedule: weekly
        tool: qualys
```

---

## 4. Client Onboarding Checklist (MSP Version)

| Week | Task | CERG Docs | Billable? |
|------|------|-----------|-----------|
| W1 | Client tenant assessment (M365/Entra ID/stack audit) | Intake questionnaire | Project |
| W1 | Deploy CERG MVC spine (8 docs, templated) | POL-001, OM-001, FRM-001, CAT-001, RMF-001, PRC-RM-001, TMPL-RM-001, PRC-VM-001 | Project |
| W2 | Enable MFA, block legacy auth | IA-1, AC-3 | Project |
| W2 | Deploy LAPS + configure PIM | AC-3, AC-4 | Project |
| W3 | Configure SIEM log ingestion (all log sources) | AU-1 | Project |
| W3 | Enable weekly vulnerability scanning | RA-2 | Project |
| W4 | Run first monthly access recertification | AC-2 | Project |
| W4 | Create incident response plan + contact sheet | IR-1 | Project |
| W4 | **Handover to managed services** | Handover memo | — |
| Ongoing | Weekly orphan check, monthly recert, quarterly QBR | All | Managed |

---

## 5. Pricing Reference (MSP)

| Service | Bronze | Silver | Gold | Platinum |
|---------|--------|--------|------|----------|
| Monthly managed security | Included | $500-1000 | $2000-5000 | $5000-15000 |
| Onboarding (one-time) | $2500 | $5000 | $10000 | $25000 |
| QBR (quarterly review) | 30 min call | 1 hour + report | 2 hours + report | 4 hours + full review |
| Tabletop facilitation (annual) | — | $2500 | $5000 | $5000 |
| Regulatory assessment (per framework) | — | — | $10000 | $20000+ |
| Incident response (per event) | $250/hr | $250/hr | $250/hr | $200/hr retainer |

---

## 6. Common MSP Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Same password across clients | Shared admin credential used by MSP team | Deploy PIM per client + MSP-secure PAM |
| Client security contact is the MSP | Client doesn't know their own controls | Name a client security contact in SOW |
| Evidence collected but not filed | "We did it but I can't find the report" | Automated evidence collection + timestamped storage |
| One client's incident cascades | Ransomware in Client A uses same MSP tools to reach Client B | Isolate MSP admin access per client tenant |
