# CERG MSP/MSSP Runbook

## Practitioner Playbook for Delivering CERG at Scale

| | |
|---|---|
| **Document ID** | CERG-OPN-MSP-001 |
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Quarterly |
| **Frameworks** | CERG 100-Core · NIST 800-53r5 · CIS Controls v8 |
| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 |
| **Environments** | IT · Cloud · SaaS |

---

## Purpose

This runbook is for MSPs and MSSPs who deliver the CERG cybersecurity operating model to small and mid-sized clients. It assumes you've read the [Opinionated Tool Matrix](tools/opinionated-tool-matrix-v1.md), reviewed the [Engagement Playbook](../practice-assets/engagement-playbook-v1.md) for scoping and pricing context, and set up your [GRC platform](tools/grc-rollout-v1.md).

Every section here is written for an **IT generalist** — someone who can follow instructions and run commands, but isn't a dedicated security engineer. If a step requires specialized expertise, it's called out explicitly.

---

## Phase 1: Client Intake and Scoping

### 1.1 Initial Client Assessment

Before deploying a single tool, you need to understand what the client has. Run the CERG Intake Questionnaire (30 questions, 60 minutes with the client's IT lead — see [Engagement Playbook Phase 1](../practice-assets/engagement-playbook-v1.md#phase-1-discover-free-60-minutes)). The questionnaire covers:

- Current tool inventory (what's already in place)
- Regulatory obligations (CMMC, HIPAA, PCI, SOX, none)
- Cloud footprint (AWS, Azure, GCP, M365 only, on-prem only)
- Endpoint count and OS mix
- Identity provider (AD, Entra ID, Okta, Google Workspace, local accounts)
- Backup strategy (what exists, last tested, is it immutable)
- Network topology (flat or segmented, OT presence, guest network)
- Incident history (breaches, ransomware, regulatory findings in last 24 months)
- Budget band (under $10k/yr, $10-50k, $50-150k, $150k+)
- In-house IT capability (none, IT generalist, dedicated security person)

### 1.2 Stack Selection

Based on the assessment, select the tool stack using the [Opinionated Tool Matrix](tools/opinionated-tool-matrix-v1.md) decision guide. The quick-reference:

| Client Profile | GRC | SIEM | EDR | CSPM | IAM | Backup |
|----------------|-----|------|-----|------|-----|--------|
| SMB (<50) | Vanta | Wazuh | SentinelOne | Wiz | Entra ID | Veeam |
| Mid-market | ServiceNow | Elastic | SentinelOne | Wiz | Okta | Veeam |

### 1.3 Scope Document

Write a one-page scope document that names:
- The client's CERG tier (Foundations, Structure, Compliance, Strategic — see [Engagement Playbook](../practice-assets/engagement-playbook-v1.md#phase-3-plan-billable-1-week-after-assessment) pricing and [Implementation Guide](../governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md#5-the-306090-day-rollout))
- Tool stack selected
- Excluded scope (OT, physical security, etc.)
- Evidence collection cadence
- Reporting cadence (monthly for mid-market, quarterly for SMB)
- Client responsibilities (what they must do — e.g., approve exceptions, fund tool licenses)

---

## Phase 2: Tool Stack Deployment

This section provides copy-paste deployment commands for the recommended stack. All commands assume you have admin access and the client has given written authorization.

### 2.1 SentinelOne Deployment

```bash
# Download the SentinelOne agent for the client's site
# 1. Log into SentinelOne console
# 2. Navigate to Sentinels > Packages
# 3. Select the client's site
# 4. Copy the registration token

# Deploy via RMM (NinjaOne example)
# In NinjaOne: Policies > Automation > Add Script
# Script type: PowerShell (Windows) / Bash (Mac/Linux)

# Windows PowerShell deployment:
$TOKEN = "client-registration-token"
$SITE = "client-site-token"
$URL = "https://usea1-install.sentinelone.net"
$Installer = "$env:TEMP\SentinelOneInstaller.exe"
Invoke-WebRequest -Uri "$URL/agents/latest/windows" -OutFile $Installer
Start-Process -FilePath $Installer -ArgumentList "-t $TOKEN -s $SITE -q" -Wait

# Ubuntu/Debian deployment:
TOKEN="client-registration-token"
SITE="client-site-token"
curl -sSL "https://usea1-install.sentinelone.net/agents/latest/linux" -o /tmp/s1-agent.deb
sudo dpkg -i /tmp/s1-agent.deb
sudo /opt/sentinelone/bin/sentinelctl management token set "$TOKEN"
sudo /opt/sentinelone/bin/sentinelctl management site set "$SITE"
sudo /opt/sentinelone/bin/sentinelctl control start

# Verify: agent appears in console within 5 minutes
```

### 2.2 Wazuh Deployment (SMB Stack)

```bash
# Deploy Wazuh server (single VM, 4 vCPU, 8GB RAM, 100GB disk minimum for SMB)
# Ubuntu 22.04 recommended

# Quick install:
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
sudo bash wazuh-install.sh --generate-config-files

# Edit config to disable unneeded modules for SMB:
sudo sed -i 's/wazuh_indexer_install: "yes"/wazuh_indexer_install: "no"/' config.yml
sudo sed -i 's/wazuh_dashboard_install: "yes"/wazuh_dashboard_install: "yes"/' config.yml

# Install:
sudo bash wazuh-install.sh --wazuh-server wazuh-1

# Deploy Wazuh agents to endpoints:
# Windows (via RMM):
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.7.0-1.msi -OutFile $env:TEMP\wazuh-agent.msi
Start-Process msiexec.exe -ArgumentList "/i $env:TEMP\wazuh-agent.msi /q WAZUH_MANAGER='wazuh-server-ip' WAZUH_REGISTRATION_SERVER='wazuh-server-ip'" -Wait

# Linux:
curl -s https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.7.0-1_amd64.deb -o /tmp/wazuh-agent.deb
sudo WAZUH_MANAGER='wazuh-server-ip' dpkg -i /tmp/wazuh-agent.deb
sudo systemctl start wazuh-agent

# Verify: agents appear in Wazuh dashboard
```

### 2.3 Tenable Nessus Deployment

```bash
# Deploy Nessus scanner appliance (VM or cloud instance)
# For MSP multi-client: one Nessus Manager + per-client Nessus scanners

# Download Nessus:
curl -sSL "https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.7.0-ubuntu1404_amd64.deb" -o /tmp/nessus.deb
sudo dpkg -i /tmp/nessus.deb
sudo systemctl start nessusd

# Link scanner to Tenable.io (MSP console):
sudo /opt/nessus/sbin/nessuscli managed link --key=YOUR_LINKING_KEY --cloud

# Create a scan policy for CERG baseline:
# 1. Log into Tenable.io
# 2. Scans > Policies > New Policy
# 3. Select "Basic Network Scan"
# 4. Enable: authenticated scanning, compliance checks (CIS benchmarks)
# 5. Set scan window: weekly, off-hours

# Schedule a scan (via API):
curl -s -H "X-ApiKeys: accessKey=XXX;secretKey=YYY" \
  -H "Content-Type: application/json" \
  -X POST "https://cloud.tenable.com/scans" \
  -d '{
    "uuid": "template-uuid-for-basic-scan",
    "settings": {
      "name": "CERG Weekly Baseline - ClientName",
      "enabled": true,
      "text_targets": "192.168.1.0/24,10.0.0.0/24",
      "launch": "WEEKLY",
      "starttime": "20240701T020000"
    }
  }'
```

### 2.4 Wiz CSPM Onboarding

```bash
# Wiz is agentless — connect cloud accounts via read-only IAM roles

# AWS onboarding (CloudFormation):
# 1. In Wiz console: Settings > Cloud Accounts > Add > AWS
# 2. Choose "Automatic — CloudFormation" 
# 3. Run the provided CloudFormation template in the client's AWS account
# 4. Wiz discovers resources within 15 minutes

# Azure onboarding:
# 1. In Wiz console: Settings > Cloud Accounts > Add > Azure  
# 2. Follow the "Automatic — Terraform" or "Manual" instructions
# 3. Creates a read-only service principal
# 4. Discovery completes within 30 minutes

# Verify onboarding:
# Wiz dashboard shows resource count, findings, and risk score
# First scan typically finds 50-500 misconfigurations in a production cloud account
```

### 2.5 Veeam Backup Configuration

```bash
# Veeam Backup & Replication deployment (Windows Server recommended)
# For MSP: Veeam Service Provider Console for multi-client management

# Core configuration (minimal for CERG compliance):
# 1. Create a backup repository with immutability enabled
#    - Type: Linux Hardened Repository or Object Storage with Object Lock
#    - Immutability period: minimum 30 days
# 2. Create a backup job for each critical workload:
#    - Domain controllers
#    - File servers
#    - Database servers  
#    - Application servers
# 3. Schedule: daily incremental, weekly full
# 4. Enable backup verification (SureBackup) on weekends
# 5. Configure backup copy to offline/air-gapped storage (rotating external drives
#    or a second immutable repository in a different region)

# Offsite copy (via Veeam Cloud Connect to MSP's infrastructure):
# 1. Add service provider in Veeam console
# 2. Create Backup Copy job pointing to cloud repository
# 3. Enable GFS retention: 7 daily, 4 weekly, 12 monthly, 3 yearly
```

---

## Phase 3: Per-Control Implementation

This section covers the controls that MSPs most commonly struggle with. Each entry includes the control, what the client needs, and the exact steps to implement it. For the full 100-control baseline, see [CERG-GOV-CB-002](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md).

### AC-002: MFA Everywhere

**Control reference:** [CB-002 AC-002](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#ac-002-mfa-enforcement) · [Access Management Standard (STD-AC-001)](../standards/CERG-STD-AC-001_Access_Management_Standard.md)

**What it means:** Every user account that accesses company systems must use multi-factor authentication. No exceptions for executives, IT staff, or service accounts with interactive login.

**Implementation steps:**

1. **Identify all authentication surfaces** — IdP (Okta/Entra ID), VPN, email, SaaS apps, remote desktop, server local logins, admin consoles
2. **Enforce MFA at the IdP level first** — this catches 80% of the surface
   - Okta: Security > Multifactor > Factor Enrollment > Require for all users
   - Entra ID: Security > MFA > Per-user MFA > Enable for all users (or Conditional Access policy)
3. **Enforce MFA on VPN and remote access**
   - FortiGate: User & Device > Authentication > Two-factor Authentication
   - Cisco AnyConnect: Use SAML to Okta/Entra ID
4. **Document exceptions in the risk register** — service accounts that cannot use interactive MFA get compensating controls (network restriction, monitoring, frequent credential rotation)
5. **Verify:** Attempt login from outside the network without MFA — must be rejected

```bash
# Quick check: does Entra ID enforce MFA for all users?
# PowerShell (Connect-MgGraph first)
Get-MgUser -All | Where-Object { $_.UserType -eq "Member" } | 
  ForEach-Object { 
    $mfa = Get-MgUserAuthenticationMethod -UserId $_.Id
    if (-not $mfa) { Write-Host "NO MFA: $($_.UserPrincipalName)" }
  }
```

### AC-006: Quarterly Access Review

**Control reference:** [CB-002 AC-006](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#ac-006-quarterly-access-review) · [Access Management Standard (STD-AC-001)](../standards/CERG-STD-AC-001_Access_Management_Standard.md)

**What it means:** Every quarter, someone reviews who has access to what and revokes what's no longer needed. This is the control that catches the ex-employee whose account was never disabled, the contractor whose project ended, and the admin who changed roles.

**Implementation steps:**

1. **Export current access from all systems:**
   - Entra ID/AD: all users with group memberships
   - Okta: all users with app assignments
   - SaaS apps: admin roles, external collaborators (especially M365 guest users, Salesforce admins, GitHub org owners)
   - Network: VPN users, firewall admin accounts
2. **Compare against HR system** — who is still employed, who changed roles
3. **Send the export to department heads** with a 5-day deadline: "Review these people. If anyone should not have access, mark them."
4. **Revoke flagged access immediately** — do not wait for the next cycle
5. **Document the review:** date, reviewer, systems covered, revocations made
6. **Upload evidence to GRC platform**

```bash
# Quick check: disabled users still in AD groups (they shouldn't be)
Get-ADUser -Filter {Enabled -eq $false} -Properties MemberOf | 
  Where-Object { $_.MemberOf.Count -gt 0 } | 
  Select-Object Name, @{N="Groups";E={($_.MemberOf | ForEach-Object {(Get-ADGroup $_).Name}) -join ", "}}
```

### CM-008: Baseline Configuration Drift

**Control reference:** [CB-002 CM-008](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#cm-008-automated-patching) · [Configuration Baseline Standard (STD-CFG-001)](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)

**What it means:** Systems are configured to a known-good baseline. When they drift, you detect it and fix it. This prevents the server that was hardened six months ago from accumulating insecure defaults as administrators make one-off changes.

**Implementation steps:**

1. **Define the baseline per platform:**
   - Windows: CIS Benchmark for Windows Server 2022
   - Linux: CIS Benchmark for Ubuntu 22.04 LTS
   - Network: Manufacturer hardening guide
   - Cloud: CIS Benchmark for AWS/Azure Foundations
2. **Deploy configuration monitoring:**
   - Wazuh: enable SCA (Security Configuration Assessment) module, load CIS policy
   - Tenable: run compliance scans against CIS benchmarks
   - Wiz: continuous CSPM monitoring for cloud
3. **Schedule:**
   - Weekly scan for critical systems (domain controllers, firewalls, internet-facing)
   - Monthly scan for all others
4. **Response:** Any drift finding > Medium severity gets a ticket within 24 hours

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | cragin-security | Initial release: 5-phase delivery playbook, tool deployment commands, per-control implementation |

### Related Documents

- [100-Core Control Baseline](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — the full control set with MSP implementation notes for all 19 families
- [Engagement Playbook](../practice-assets/engagement-playbook-v1.md) — scoping, pricing, SOW essentials, engagement lifecycle
- [Opinionated Tool Matrix](tools/opinionated-tool-matrix-v1.md) — tool selection criteria, primary/acceptable/avoid tiers
- [GRC Rollout Guide](tools/grc-rollout-v1.md) — wiring ServiceNow GRC or Vanta to the CERG control framework
- [Access Management Standard](../standards/CERG-STD-AC-001_Access_Management_Standard.md) — authoritative parameter detail for AC family controls
- [Configuration Baseline Standard](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) — DISH baseline, hardening benchmarks, drift detection parameters
- [Implementation Guide](../governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) — adoption paths, MVC sequence, role-based checklists
