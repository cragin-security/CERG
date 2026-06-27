# CERG MSP Runbook Pack v1

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
