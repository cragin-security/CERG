# CERG MSP/MSSP Runbook

## Practitioner Playbook for Delivering CERG at Scale

| | |
|---|---|
| **Document ID** | CERG-OPN-MSP-001 |
| **Version** | 1.1.0 |
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

```powershell
# Quick check: does Entra ID enforce MFA for all users?
# PowerShell (Connect-MgGraph first)
Get-MgUser -All | Where-Object { $_.UserType -eq "Member" } | 
  ForEach-Object { 
    $mfa = Get-MgUserAuthenticationMethod -UserId $_.Id
    if (-not $mfa) { Write-Host "NO MFA: $($_.UserPrincipalName)" }
  }
```

### AC-005: Remote Access Hardening

**Control reference:** [CB-002 AC-005](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#ac-005-remote-access) · [Access Management Standard (STD-AC-001)](../standards/CERG-STD-AC-001_Access_Management_Standard.md)

**What it means:** Remote access is the #1 initial access vector in ransomware. Every remote connection requires MFA, encrypted transport, and device posture validation. Split-tunnel VPN is prohibited unless documented with compensating controls.

**Implementation steps:**

1. **Audit all remote access points** — VPN gateways, RDP exposed to internet, remote desktop gateways, Citrix, VDI, SSH bastions
2. **Close direct RDP to the internet** — if RDP must be exposed, front it with a remote desktop gateway that requires MFA, or use the RMM instead
3. **Configure VPN with MFA:**
   - FortiGate SSL-VPN: enable SAML authentication to Okta/Entra ID. Set `set saml-server` on the SSL-VPN portal
   - Require client certificate for admin VPN access: `config vpn ssl settings; set require-client-cert enable; end`
4. **Disable split tunneling** — all client traffic routes through VPN for inspection. Exception: documented and approved for performance-critical SaaS
   - FortiGate: `config vpn ssl settings; set tunnel-connect enable (split-tunnel = disable); end`
5. **Verify:** `show vpn ssl settings | grep require-client-cert` — must show enabled. Test: attempt VPN without MFA — must be rejected

```powershell
# Quick check: find internet-exposed RDP on the client's public IP range
# Use Tenable scan data or Shodan-like query
# PowerShell (requires Tenable API access)
$scanResult = Invoke-RestMethod -Uri "https://cloud.tenable.com/scans/$scanId/results" -Headers $headers
$scanResult.vulnerabilities | Where-Object { $_.plugin_name -like "*RDP*" -and $_.severity -ge 2 }
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

```powershell
# Quick check: disabled users still in AD groups (they shouldn't be)
Get-ADUser -Filter {Enabled -eq $false} -Properties MemberOf | 
  Where-Object { $_.MemberOf.Count -gt 0 } | 
  Select-Object Name, @{N="Groups";E={($_.MemberOf | ForEach-Object {(Get-ADGroup $_).Name}) -join ", "}}
```

### AC-004: Least Privilege and PAM

**Control reference:** [CB-002 AC-004](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#ac-004-least-privilege) · [Access Management Standard (STD-AC-001)](../standards/CERG-STD-AC-001_Access_Management_Standard.md)

**What it means:** Users and services operate with minimum access. Administrative privileges use just-in-time (PIM/PAM), not standing group membership. Stolen admin credentials are the primary way ransomware spreads laterally.

**Implementation steps:**

1. **Audit all privileged groups** — Domain Admins, Enterprise Admins, local admin on all servers, cloud IAM admin roles
2. **Remove all users from Domain Admins** — create tiered admin groups:
   - Workstation Admin (can manage workstations only)
   - Server Admin (can manage servers only)
   - Domain Admin (emergency only, JIT elevation)
3. **Deploy PAM (for clients with budget):**
   - Entra ID PIM: configure for Global Admin, Security Admin, Exchange Admin, SharePoint Admin roles. Require approval + MFA + justification for activation. Set max activation duration to 4 hours
   - For SMB without PAM budget: dedicated admin accounts (u-admin) separate from daily driver accounts. Rotate passwords every 12 hours via scheduled script
4. **Disable local admin on all workstations** via GPO or Intune. Use LAPS (Local Administrator Password Solution) for server local admin access, with passwords rotated after every use

```powershell
# Quick check: how many users are Domain Admins?
Get-ADGroupMember -Identity "Domain Admins" | Select-Object Name, SamAccountName

# Deploy LAPS (if not already deployed):
# Install LAPS ADMX templates, configure GPO for LAPS, verify with:
Get-LapsADPassword -Identity "DC01" -AsPlainText | Select-Object Password
```

### IA-002: Strong Authentication

**Control reference:** [CB-002 IA-002](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#ia-002-strong-authentication) · [Access Management Standard (STD-AC-001)](../standards/CERG-STD-AC-001_Access_Management_Standard.md)

**What it means:** Passwords alone are not enough. Authentication requires MFA combined with strong password policies. Phishing-resistant methods (FIDO2, certificates) are preferred for privileged accounts.

**Implementation steps:**

1. **Enforce password policy:** minimum 12 characters, ban common passwords (use Entra ID Password Protection or Okta password dictionary)
2. **Deploy MFA** (see AC-002 above)
3. **Where budget allows, deploy FIDO2 security keys** for privileged accounts — these are phishing-resistant and cannot be intercepted by adversary-in-the-middle attacks
4. **Disable legacy authentication protocols** — POP, IMAP, legacy M365 auth. These bypass MFA entirely
   - Entra ID: Conditional Access policy blocking all protocols except modern auth
   - Exchange Online: `Set-OrganizationConfig -LegacyAuthProtocols $false`

```powershell
# Quick check: legacy auth still enabled?
Get-OrganizationConfig | Select-Object LegacyAuthProtocols
# If $true, you have an MFA bypass. Disable it.

# Check which users don't have MFA registered
Get-MgUser -All -Property Id, UserPrincipalName, StrongAuthenticationRequirements |
  Where-Object { $_.StrongAuthenticationRequirements.Count -eq 0 } |
  Select-Object UserPrincipalName
```

### CM-005: Software Whitelisting and Application Control

**Control reference:** [CB-002 CM-005](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#cm-005-software-whitelisting) · [Configuration Baseline Standard (STD-CFG-001)](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)

**What it means:** Only authorized software runs on endpoints. Ransomware, Mimikatz, remote access tools, and other attacker tooling are blocked by default. Whitelisting is based on publisher certificate, file hash, or path.

**Implementation steps:**

1. **Approach:** AppLocker in audit-only mode for 30 days to build the baseline. Monitor event ID 8003 (blocked would-be executions). Add legitimate software to the allowlist
2. **Configure AppLocker rules:**
   - Windows Installer rules: allow digitally signed MSIs from trusted publishers
   - Script rules: allow from Program Files, Windows, and a managed scripts share only
   - DLL rules: allow from Program Files and Windows only
   - Executable rules: allow from Program Files and Windows only
3. **Switch to enforce mode** after 30 days. Monitor for blocks. Add exceptions only through change control
4. **SentinelOne alternative:** Enable Application Control module. SentinelOne maintains its own allowlist of known-good software. Block by file hash, publisher, or path

```powershell
# Build the baseline (run after 30 days audit mode)
$blocked = Get-AppLockerPolicy -Local | Test-AppLockerPolicy -Path C:\Program Files\*, C:\Windows\* -User Everyone
$blocked | Where-Object {$_.Status -eq "Denied"} | Export-Csv applocker-baseline-exceptions.csv

# Get blocked execution events from audit mode
Get-WinEvent -FilterHashtable @{LogName="Applications and Services Logs/Microsoft/Windows/AppLocker"; Id=8003} | 
  Select-Object TimeCreated, Message
```

### SI-004: Detection Engineering

**Control reference:** [CB-002 SI-004](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#si-004-detection-engineering) · [Logging Monitoring and Detection Standard (STD-LM-001)](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)

**What it means:** Detection rules exist for the TTPs attackers actually use. Rules are written in Sigma format, mapped to MITRE ATT&CK, and tested quarterly with Atomic Red Team. The controls that stop ransomware are only effective if they alert when bypassed.

**Implementation steps:**

1. **Deploy the CERG Sigma rule set** (shipped with the detection engineering framework):
   - Navigate to the CERG rules directory: `sigma-rules/`
   - Convert Sigma rules to SIEM format: `sigmac -t elastic -o /output/rules.json rule.yml`
   - Load into SIEM: Elastic `_bulk` API or Wazuh ruleset import
2. **Map rules to ATT&CK** — each rule should reference the technique it detects
3. **Minimum detection coverage by TTP:**

| TTP | Event to Monitor | Sigma Rule Source |
|-----|-----------------|-------------------|
| T1059.001 PowerShell abuse | Script block logging, downgrade detection | Built-in Elastic/Wazuh rules |
| T1003.001 LSASS dumping | Process access to lsass.exe (4663) | sysmon_suspicious_lsass_access |
| T1570 Lateral tool transfer | SMB writes + service creation | sysmon_smb_execution_detection |
| T1219 RAT installation | AnyDesk/TeamViewer binary creation | sysmon_rat_install_events |
| T1560 Archiving data | WinRAR/7-Zip invoked on unusual data paths | sysmon_susp_archiving |
| T1078 Valid accounts | Impossible travel, new device authentication | elastic_rule_auth_anomaly |

4. **Test quarterly with Atomic Red Team:**
```powershell
# Install ART
Install-Module -Name AtomicRedTeam -Force
Invoke-AtomicTest All -GetPrereqs

# Run all tests and check detection
Invoke-AtomicTest All
# Review which tests generated alerts in SIEM
# Any test without an alert = detection gap
```

```powershell
# Quick check: how many of your Sigma rules map to ATT&CK?
# Run this against your SIEM rule set
$rules = Get-ChildItem -Path ".\sigma-rules" -Recurse -Filter "*.yml"
$withTechnique = $rules | Select-String -Pattern "attack.mitre.org"
Write-Host "$($withTechnique.Count) / $($rules.Count) rules mapped to ATT&CK"
```

### CM-008: Automated Patching

**Control reference:** [CB-002 CM-008](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#cm-008-automated-patching) · [Configuration Baseline Standard (STD-CFG-001)](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)

**What it means:** Operating system and application patches are deployed within defined SLAs. Critical security patches: 7 days. High-severity: 14 days. Medium: 30 days. Automated patching is the single highest-ROI control — it blocks 6 of the 10 most common ransomware TTPs.

**Implementation steps:**

1. **Configure automated patch management in RMM:**
   - NinjaOne: Policies > Patch Management > Enable automatic approval for Critical and Security patches
   - Test on pilot group (5% of endpoints), then deploy to all
   - Servers: managed maintenance windows, no automatic reboots during business hours
2. **Configure CISA KEV alerting:**
   - Subscribe to CISA KEV RSS feed or API: `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`
   - Any new KEV entry affecting the client's software stack triggers an emergency patch
   - Emergency patch SLA: 48 hours for internet-facing systems, 7 days for internal
3. **Verify:** Monthly patch compliance report showing deployment status by severity

```powershell
# Quick check: CISA KEV entries relevant to client's software stack
$kev = Invoke-RestMethod -Uri "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
$clientVendors = @("Microsoft", "Fortinet", "VMware", "Palo Alto", "Cisco", "Ivanti")
$kev.vulnerabilities | Where-Object { 
  $_.vendorProject -in $clientVendors -and $_.dateAdded -gt (Get-Date).AddDays(-90)
} | Select-Object cveID, vendorProject, product, vulnerabilityName, dateAdded, dueDate
```

### SI-005: Email Security

**Control reference:** [CB-002 SI-005](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#si-005-email-security) · [Email and Messaging Security Standard (STD-MSG-001)](../standards/CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md)

**What it means:** Email is the initial access vector for ransomware. SPF, DKIM, and DMARC prevent domain spoofing. Safe Links and Safe Attachments block malicious URLs and attachments. Phishing investigations happen within 4 hours.

**Implementation steps:**

1. **Configure SPF record:** identify all sending IP addresses and add them to the client's DNS TXT record:
   ```
   v=spf1 ip4:192.0.2.0/24 include:spf.protection.outlook.com -all
   ```
2. **Configure DKIM:** enable in Exchange Admin Center > Mail flow > DKIM. Generate signing key and publish DNS CNAME records
3. **Configure DMARC:** start with `p=none` to monitor, move to `p=quarantine` after 30 days, then `p=reject` after 90 days
4. **Enable Safe Links and Safe Attachments** in M365 Defender:
   - Safe Links: block URLs at time of click, track URL clicks
   - Safe Attachments: detonate attachments in sandbox before delivery

```powershell
# Quick check: SPF record published correctly?
Resolve-DnsName client.com TXT | Where-Object Strings -like "v=spf*"

# Check DMARC policy
Resolve-DnsName _dmarc.client.com TXT | Select-Object Strings
```

### SI-006: Web Filtering

**Control reference:** [CB-002 SI-006](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#si-006-web-filtering) · [Network Security and Segmentation Standard (STD-NET-001)](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md)

**What it means:** Outbound web traffic is filtered to block malicious, phishing, and inappropriate categories. HTTPS inspection enabled where legally permissible. DNS filtering blocks C2 and malware distribution domains.

**Implementation steps:**

1. **Configure web filter on FortiGate:**
   - Go to Security Profiles > Web Filter > Create New
   - Block: Malicious, Phishing, Newly Registered Domains, Cryptominers
   - Warn or block (per client policy): Adult, P2P, Social Media
2. **Enable DNS filtering** — forward all DNS to FortiGuard or Cisco Umbrella
3. **Enable HTTPS inspection** (CA certificate deployed via GPO):
   - FortiGate: Security Profiles > SSL/SSH Inspection > Full SSL Inspection
   - Deploy the FortiGate CA certificate to domain workstations via GPO
4. **Test:** browse to a known malicious test URL — must be blocked. Check: `diagnose test application urlfilter 1`

```bash
# Quick check: is web filter blocking known bad domains?
# Simulate a blocked query
curl -s -o /dev/null -w "%{http_code}" -x proxy.client.com:3128 http://malicious.test-domain.com
# Expected: 403 or connection reset
```

### SI-007: Data Loss Prevention

**Control reference:** [CB-002 SI-007](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#si-007-data-loss-prevention) · [Data Governance and Classification Standard (STD-DG-001)](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md)

**What it means:** Sensitive data is protected from exfiltration. DLP policies block unauthorized transmission of PII, PHI, financial data, and intellectual property via email, cloud upload, USB transfer, and clipboard.

**Implementation steps:**

1. **Enable M365 DLP in Purview:**
   - Go to Microsoft Purview > Data Loss Prevention > Policies
   - Create policies for: PII (SSN, credit card, bank account), PHI (HIPAA identifiers), financial data
   - Start in audit mode for 30 days, review incident volume, tune false positives
   - Switch to block mode for high-confidence patterns
2. **Enable USB device control via SentinelOne:**
   - In the SentinelOne console: Settings > Policy > Device Control
   - Set USB mass storage to "Read Only" or "Block" (per client policy)
   - Set Bluetooth and tethering to "Block" for managed devices
3. **Test:** attempt to email a file containing PII to an external address — must be blocked

### SC-001: Network Segmentation

**Control reference:** [CB-002 SC-001](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md#sc-001-network-segmentation) · [Network Security and Segmentation Standard (STD-NET-001)](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md)

**What it means:** The network is divided into trust zones — servers, workstations, guest, DMZ, OT, management. Lateral movement between zones requires a firewall rule. This is how you stop ransomware from spreading from a compromised workstation to file servers.

**Implementation steps:**

1. **Map current network topology** — identify all subnets, VLANs, and firewall rules
2. **Define minimum zone architecture:**
   - Zone 1: Guest (internet only, client isolation)
   - Zone 2: Workstation (corporate LAN, no direct server access)
   - Zone 3: Server (domain controllers, file servers, application servers)
   - Zone 4: DMZ (internet-facing web servers, email gateways)
   - Zone 5: Management (admin workstations, jump boxes, RMM infrastructure)
   - Zone 6: OT (physically separate or firewall-enforced one-way data flow)
3. **Configure inter-zone rules (FortiGate example):**
   - Workstation → Server: allow only on required ports (e.g., SMB 445 for file shares, HTTPS 443 for internal apps)
   - Server → Internet: deny outbound by default; allow only what's documented and approved
   - Workstation ↔ Workstation: allow (no blocking intra-VLAN — use EDR for lateral movement detection instead)
4. **Verify:** can a workstation ping a server in a different zone? If yes, segmentation is broken.

```bash
# Quick check: test segmentation from a workstation
ping server-ip        # Should FAIL (unless server is in same zone)
tracert server-ip     # Should show firewall hop
nmap -sn server-subnet # Should show filtered ports

# FortiGate: show zone-to-zone policy
diagnose firewall policy list | grep -A5 "srcintf.*zone-name"
```

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-20 | cragin-security | Expanded Phase 3 from 3 to 11 controls: added AC-005, AC-004, IA-002, CM-005, SI-004, SI-005, SI-006, SI-007, SC-001. Threat-prioritized from ransomware TTP analysis. |
| 1.0.0 | 2026-07-03 | cragin-security | Initial release: 5-phase delivery playbook, tool deployment commands, per-control implementation |

### Related Documents

- [100-Core Control Baseline](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — the full control set with MSP implementation notes for all 19 families
- [Engagement Playbook](../practice-assets/engagement-playbook-v1.md) — scoping, pricing, SOW essentials, engagement lifecycle
- [Opinionated Tool Matrix](tools/opinionated-tool-matrix-v1.md) — tool selection criteria, primary/acceptable/avoid tiers
- [GRC Rollout Guide](tools/grc-rollout-v1.md) — wiring ServiceNow GRC or Vanta to the CERG control framework
- [Access Management Standard](../standards/CERG-STD-AC-001_Access_Management_Standard.md) — authoritative parameter detail for AC family controls
- [Configuration Baseline Standard](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) — DISH baseline, hardening benchmarks, drift detection parameters
- [Implementation Guide](../governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) — adoption paths, MVC sequence, role-based checklists
