#!/usr/bin/env python3
"""
Generate the Detection Engineering Framework v1 document.
Writes to detection-engineering-framework-v1.md in the same directory.
"""

DOC = r"""# Detection Engineering Framework v1.0

**Author:** CERG Detection Engineering Team  
**Version:** 1.0  
**Last Updated:** 2026-06-27  
**Scope:** Enterprise Windows / Azure / M365 Environments  
**Target Audience:** SOC Analysts, Detection Engineers, Threat Hunters

---

## Table of Contents

1. [Purpose & Scope](#purpose--scope)
2. [Data Source Requirements](#data-source-requirements)
3. [Technique-to-Detection Mapping](#technique-to-detection-mapping)
4. [Tuning Guidance Reference](#tuning-guidance-reference)
5. [Query Library Structure](#query-library-structure)
6. [Alert Severity Taxonomy](#alert-severity-taxonomy)
7. [Appendix: Useful References](#appendix-useful-references)

---

## Purpose & Scope

This document provides a repeatable detection engineering framework mapping the top 20 MITRE ATT&CK techniques (Enterprise v14) to production-ready detection rules in **Kusto Query Language (KQL)** for Microsoft Sentinel / Defender and **Sigma** format for SIEM-agnostic deployment.

Each entry includes:
- Technique ID & name
- Required data sources
- Detection logic (KQL + Sigma)
- Expected false positive rate (Low / Medium / High)
- Tuning guidance to reduce noise
- Suggested alert severity

The framework is designed for **enterprise Windows environments** with Microsoft 365 E5 / Defender for Endpoint (MDE) telemetry. Sigma rules follow the Sigma v2 specification.

---

## Data Source Requirements

The following table maps each technique to the log sources required for detection. An **X** indicates the log source is **required**; **(X)** indicates it is **recommended** (enhances detection depth but is not strictly necessary).

| Technique ID | Technique Name | SecurityEvent (4624, 4720, etc.) | DeviceLogonEvents | DeviceProcessEvents | DeviceFileEvents | DeviceNetworkEvents | DeviceRegistryEvents | AuditPolicyChange | AzureActivity / AuditLogs |
|---|---|---|---|---|---|---|---|---|---|
| T1078 | Valid Accounts | X | X | | | (X) | | | X |
| T1136 | Create Account | X | | | | | | X | X |
| T1098 | Account Manipulation | X | | | | | | X | X |
| T1552 | Unsecured Credentials | | | X | X | | X | | |
| T1040 | Network Sniffing | | | X | | (X) | | | |
| T1059 | Command and Scripting Interpreter | | | X | X | | X | | |
| T1053 | Scheduled Task/Job | X | | X | X | | X | X | |
| T1003 | OS Credential Dumping | X | | X | X | (X) | X | | |
| T1087 | Account Discovery | | | X | | | | | |
| T1069 | Permission Groups Discovery | | | X | | | | | |
| T1082 | System Information Discovery | | | X | | | | | |
| T1046 | Network Service Discovery | | | X | | X | | | |
| T1005 | Data from Local System | | | X | X | X | | | |
| T1074 | Data Staged | | | X | X | X | | | |
| T1048 | Exfiltration Over Alternative Protocol | | | | | X | | | |
| T1567 | Exfiltration Over Web Service | | | | | X | | | |
| T1490 | Inhibit System Recovery | | | X | X | | | | |
| T1486 | Data Encrypted for Impact | | | X | X | X | X | | |
| T1562 | Impair Defenses | | | X | X | | | X | |
| T1218 | Signed Binary Proxy Execution | | | X | X | | | | |

---

## Technique-to-Detection Mapping

### T1078 — Valid Accounts

- **Data Sources:** SecurityEvent (4624, 4648), DeviceLogonEvents, AzureActivity
- **Description:** Adversaries may authenticate using valid credentials to gain or maintain access.

**KQL — Anomalous Remote Logon (MDE)**
```kql
DeviceLogonEvents
| where Timestamp > ago(7d)
| where LogonType == "3" // Network logon
    and AccountDomain != "NT AUTHORITY"
    and AccountName != "SYSTEM"
    and isnotempty(RemoteIP)
| summarize LogonCount = count(), FirstLogon = min(Timestamp), LastLogon = max(Timestamp)
    by AccountName, AccountDomain, RemoteIP, DeviceName
| where LogonCount <= 3 // low-frequency accounts from unusual IPs
| join kind=leftanti (
    DeviceLogonEvents
    | where Timestamp > ago(30d)
    | where LogonType == "3"
    | summarize RecentCount = count() by AccountName, RemoteIP
    | where RecentCount > 10
) on AccountName, RemoteIP
| extend Severity = "Medium"
| project Timestamp = LastLogon, AccountName, RemoteIP, DeviceName, LogonCount, Severity
```

**Sigma Rule — Account Login from Unusual IP**
```yaml
title: Account Login from Unusual IP
id: 3b6a8c9d-1e2f-4a5b-8c7d-9e0f1a2b3c4d
status: experimental
description: Detects logons from IP addresses that have not been observed for the account in the past 30 days
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4624
    LogonType: '3'
  filter_known:
    - AccountName|startswith:
        - 'SYSTEM'
        - 'ANONYMOUS'
  condition: selection and not filter_known
falsepositives:
  - Legitimate remote workers with dynamic IPs
  - VPN gateway IPs that rotate
level: medium
tags:
  - attack.initial-access
  - attack.t1078
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist known VPN/VDI egress IP ranges and service accounts. Baseline each account's typical login IPs over 30 days.
- **Severity:** Medium

---

### T1136 — Create Account

- **Data Sources:** SecurityEvent (4720, 4722, 4726), AuditLogs (Azure AD)
- **Description:** Adversaries may create accounts to maintain persistent access.

**KQL — Local or Domain Account Creation**
```kql
SecurityEvent
| where EventID == 4720 // A user account was created
| where Timestamp > ago(1d)
| extend AccountName = TargetUserName
| extend CreatedBy = SubjectUserName
| extend AccountDomain = TargetDomainName
| extend Severity = case(
    AccountName contains "admin" or AccountName contains "backup", "High",
    SubjectUserName contains "svc_" or SubjectUserName contains "CORP\\admin", "Low",
    "Medium"
)
| project Timestamp, AccountName, AccountDomain, CreatedBy, EventID, Severity
```

**Sigma Rule — User Account Creation**
```yaml
title: User Account Creation
id: 9e8d7c6b-5a4f-3e2d-1c0b-9a8f7e6d5c4b
status: experimental
description: Detects when a new user account is created on a domain controller or member server
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4720
  condition: selection
falsepositives:
  - IT helpdesk creating accounts for new hires
  - Automated provisioning systems
level: medium
tags:
  - attack.persistence
  - attack.t1136
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist approved account provisioning automation accounts (HR systems, identity management tools). Alert on accounts created outside business hours or on weekends.
- **Severity:** Medium

---

### T1098 — Account Manipulation

- **Data Sources:** SecurityEvent (4738, 4724, 5136), Azure AD Audit Logs
- **Description:** Adversaries may manipulate account attributes (password reset, group membership, permission changes).

**KQL — Sensitive Account Modification**
```kql
SecurityEvent
| where EventID in (4738, 4724) // Account changed, password reset
| where Timestamp > ago(1d)
| extend TargetAccount = TargetUserName
| extend TargetDomain = TargetDomainName
| extend ChangedBy = SubjectUserName
| join kind=leftanti (
    SecurityEvent
    | where EventID == 4738
    | where SubjectUserName endswith "$"
    | summarize by SubjectUserName
) on SubjectUserName
| extend Severity = "Medium"
| project Timestamp, TargetAccount, TargetDomain, ChangedBy, EventID, Severity
```

**Sigma Rule — Password Reset by Non-Admin**
```yaml
title: Password Reset by Non-Administrator
id: 7a6b5c4d-3e2f-1a0b-9c8d-7e6f5a4b3c2d
status: experimental
description: Detects password reset events performed by accounts not in the Domain Admins group
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4724
  filter_admins:
    SubjectUserName|endswith:
      - '$'
      - 'Administrator'
      - 'ADM_'
  condition: selection and not filter_admins
falsepositives:
  - Delegated password reset via helpdesk tools
  - Self-service password reset systems
level: high
tags:
  - attack.persistence
  - attack.t1098
  - attack.privilege-escalation
```

- **Expected FP Rate:** Medium  
- **Tuning:** Create exceptions for helpdesk service accounts and self-service password reset (SSPR) infrastructure. Baseline account modification patterns per department.
- **Severity:** High

---

### T1552 — Unsecured Credentials

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents, DeviceRegistryEvents
- **Description:** Adversaries may search for credentials in files, the registry, or other locations.

**KQL — Credential File Access**
```kql
DeviceFileEvents
| where Timestamp > ago(1d)
| where FolderPath matches regex @"(?i)\\(passwords?|credentials?|secrets?|\.kdbx|\.ppk|\.pem|id_rsa)"
    or FileName matches regex @"(?i)passwords?\.(txt|docx|xlsx|csv|xml)"
| extend Severity = iif(
    FileName contains "id_rsa" or FileName contains "kdbx", "High",
    "Medium"
)
| project Timestamp, DeviceName, FileName, FolderPath, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Credential File Search**
```yaml
title: Credential File Search via CommandLine
id: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
status: experimental
description: Detects command-line searches for credential-related files or registry keys
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    CommandLine|contains:
      - 'passwords'
      - 'secrets'
      - 'credentials'
      - '.kdbx'
      - 'id_rsa'
      - 'vaultcmd'
      - 'reg query HKLM /v *SAM*'
  condition: selection
falsepositives:
  - IT audit or password rotation scripts
  - Password managers performing lookups
level: medium
tags:
  - attack.credential-access
  - attack.t1552
```

- **Expected FP Rate:** High  
- **Tuning:** Whitelist known password rotation tools (CyberArk, BeyondTrust) and IT audit scripts. Remove common password manager lookup patterns from alerting.
- **Severity:** Medium

---

### T1040 — Network Sniffing

- **Data Sources:** DeviceProcessEvents, DeviceNetworkEvents
- **Description:** Adversaries may sniff network traffic to capture sensitive information.

**KQL — Packet Capture Tool Execution**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where FileName has_any (
    "tcpdump", "wireshark", "tshark", "dumpcap", "pktmon",
    "netsh trace", "pktmon filter", "PacketMonitor", "windump",
    "Npcap", "WinPcap"
)
| where InitiatingProcessFileName != "Microsoft.TriSense.exe"
| extend Severity = "High"
| project Timestamp, DeviceName, FileName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Packet Capture Tool Execution**
```yaml
title: Packet Capture Tool Execution
id: f7e6d5c4-b3a2-1c0d-9e8f-7a6b5c4d3e2f
status: experimental
description: Detects execution of common network sniffing and packet capture tools
logsource:
  category: process_creation
  product: windows
detection:
  selection_img:
    Image|endswith:
      - '\tcpdump.exe'
      - '\wireshark.exe'
      - '\tshark.exe'
      - '\dumpcap.exe'
      - '\pktmon.exe'
      - '\windump.exe'
  selection_cli:
    CommandLine|contains:
      - ' -i '
      - ' promisc'
      - ' -P '
  condition: selection_img or selection_cli
falsepositives:
  - Network administrators performing legitimate packet analysis
  - Threat hunting team's approved tools
level: high
tags:
  - attack.credential-access
  - attack.t1040
  - attack.discovery
```

- **Expected FP Rate:** Medium  
- **Tuning:** Create an approved tool list with network team service accounts. Use process start-time baselines to detect anomalous (non-business-hours) execution.
- **Severity:** High

---

### T1059 — Command and Scripting Interpreter

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents, DeviceRegistryEvents
- **Description:** Adversaries may abuse command and script interpreters to execute arbitrary code.

**KQL — Suspicious PowerShell / WMI / Script Execution**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where FileName has_any ("powershell.exe", "cmd.exe", "wscript.exe", "cscript.exe", "mshta.exe")
| where ProcessCommandLine has_any (
    "-EncodedCommand", "-ExecutionPolicy Bypass", "IEX (",
    "Invoke-Expression", "DownloadString", "Base64String",
    "-WindowStyle Hidden", "-NoProfile"
)
| where InitiatingProcessFileName != "sdiagnhost.exe"
    and InitiatingProcessFileName != "explorer.exe" // common for admin scripts
| extend Severity = case(
    ProcessCommandLine contains "DownloadString" or ProcessCommandLine contains "IEX (New-Object", "High",
    ProcessCommandLine contains "-EncodedCommand", "High",
    "Medium"
)
| project Timestamp, DeviceName, FileName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Suspicious PowerShell Invocation**
```yaml
title: Suspicious PowerShell Invocation
id: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f90
status: experimental
description: Detects PowerShell execution with suspicious parameters commonly used by attackers
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains:
      - '-EncodedCommand'
      - '-ExecutionPolicy Bypass'
      - 'IEX ('
      - 'Invoke-Expression'
      - 'DownloadString'
      - '-WindowStyle Hidden'
      - '-NoProfile'
  condition: selection
falsepositives:
  - IT automation and deployment scripts (SCCM, PDQ, Ansible)
  - Approved administrative tooling
level: high
tags:
  - attack.execution
  - attack.t1059
  - attack.t1059.001
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist management tool process trees (SCCM, PDQ, Lansweeper). Use `InitiatingProcessParentName` to filter out legitimate orchestrators.
- **Severity:** High

---

### T1053 — Scheduled Task/Job

- **Data Sources:** SecurityEvent (4698, 4699, 4700-4702), DeviceProcessEvents, DeviceFileEvents
- **Description:** Adversaries may create or modify scheduled tasks to execute malicious code on a schedule.

**KQL — Scheduled Task Creation**
```kql
SecurityEvent
| where EventID == 4698 // Scheduled task created
| where Timestamp > ago(1d)
| extend TaskName = TaskName
| extend TaskContent = TaskContent
| extend CreatedBy = SubjectUserName
// Filter out common Microsoft tasks
| where TaskName !startswith "Microsoft\\Windows\\"
    and TaskName !startswith "\\Microsoft\\Windows\\"
| extend Severity = case(
    TaskContent contains "powershell" or TaskContent contains "wscript" or TaskContent contains "cmd", "High",
    TaskContent contains "net user" or TaskContent contains "net localgroup", "High",
    "Medium"
)
| project Timestamp, TaskName, CreatedBy, Severity
```

**Sigma Rule — Scheduled Task Creation**
```yaml
title: Scheduled Task Creation
id: 6b7c8d9e-0f1a-2b3c-4d5e-6f7a8b9c0d1e
status: experimental
description: Detects creation of scheduled tasks, especially those executing scripts
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4698
  filter_microsoft:
    TaskName|startswith: 'Microsoft\Windows\'
  condition: selection and not filter_microsoft
falsepositives:
  - Software installers creating update tasks
  - IT management tools (SCCM, GPO scheduling)
level: medium
tags:
  - attack.execution
  - attack.persistence
  - attack.t1053
  - attack.t1053.005
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist tasks created by SCCM, WSUS, and GPO. Use `TaskContent` field to whitelist known-good command lines. Alert on tasks that download external payloads.
- **Severity:** Medium

---

### T1003 — OS Credential Dumping

- **Data Sources:** SecurityEvent (4663), DeviceProcessEvents, DeviceFileEvents
- **Description:** Adversaries may attempt to dump credentials from the OS (LSASS, SAM, etc.).

**KQL — LSASS Access (Credential Dumping)**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where FileName has_any (
    "procdump", "procdump64", "mimikatz", "mimikatz.exe",
    "lsassy", "crackmapexec", "pypykatz", "sekurlsa",
    "dumpert", "SharpDump", "SafetyDump", "Outflank-Dumpert"
)
| extend Severity = "Critical"
| project Timestamp, DeviceName, FileName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Credential Dumping via Procdump/Mimikatz**
```yaml
title: Credential Dumping Tool Detected
id: 2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f
status: experimental
description: Detects execution of known credential dumping tools
logsource:
  category: process_creation
  product: windows
detection:
  selection_img:
    Image|endswith:
      - '\procdump.exe'
      - '\procdump64.exe'
      - '\mimikatz.exe'
  selection_cli:
    CommandLine|contains:
      - 'sekurlsa::logonPasswords'
      - '-ma lsass'
      - 'comsvcs.dll #24'
      - 'MiniDump'
  condition: selection_img or selection_cli
falsepositives:
  - Forensic investigators performing legitimate memory analysis
  - Approved EDR/Linux cross-platform tooling
level: critical
tags:
  - attack.credential-access
  - attack.t1003
  - attack.t1003.001
```

- **Expected FP Rate:** Low  
- **Tuning:** Only whitelist after verified exception request with business justification. Alert on any access to `lsass.exe` from a non-`Lsass` parent process.
- **Severity:** Critical

---

### T1087 — Account Discovery

- **Data Sources:** DeviceProcessEvents
- **Description:** Adversaries may enumerate accounts to identify valid credentials and targets.

**KQL — Account Discovery Commands**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where ProcessCommandLine has_any (
    "net user", "net group", "net localgroup", "dsquery user",
    "Get-ADUser", "Get-LocalUser", "wmic useraccount",
    "Get-WmiObject Win32_UserAccount", "net accounts",
    "Get-ADGroupMember", "Get-LocalGroupMember"
)
| where InitiatingProcessFileName !in~ ("Microsoft.TriSense.exe", "dfsr.exe")
| extend Severity = iif(
    ProcessCommandLine contains "/domain" or ProcessCommandLine contains "ADUser",
    "Medium", "Low"
)
| project Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Account Discovery via Net**
```yaml
title: Account Discovery via Net Commands
id: 3d4e5f6a-7b8c-9d0e-1f2a-3b4c5d6e7f8a
status: experimental
description: Detects use of net.exe/net1.exe for user and group enumeration
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith:
      - '\net.exe'
      - '\net1.exe'
    CommandLine|contains:
      - ' user '
      - ' group '
      - ' localgroup '
      - ' accounts '
  condition: selection
falsepositives:
  - Helpdesk scripts performing user lookups
  - Logon scripts enumerating groups
  - IT inventory tools
level: low
tags:
  - attack.discovery
  - attack.t1087
  - attack.t1087.001
```

- **Expected FP Rate:** High  
- **Tuning:** Baseline per-machine account discovery frequency. Ignore stdlogon scripts and inventory scanners. Focus on workstations (less noise) instead of servers.
- **Severity:** Low

---

### T1069 — Permission Groups Discovery

- **Data Sources:** DeviceProcessEvents
- **Description:** Adversaries may enumerate permission groups (local admin groups, domain groups).

**KQL — Permission Group Enumeration**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where ProcessCommandLine matches regex @"(?i)(net\s+(local)?group|Get-(AD)?(Local)?Group|wmic\s+group)"
    and ProcessCommandLine contains "admin"
| extend Severity = "Medium"
| project Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Admin Group Enumeration**
```yaml
title: Admin Group Enumeration
id: 4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9b
status: experimental
description: Detects enumeration of local or domain admin groups
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    CommandLine|contains:
      - 'administrators'
      - 'domain admins'
      - 'enterprise admins'
      - 'schema admins'
  condition: selection
falsepositives:
  - Domain admin troubleshooting tools
  - Security tools performing access reviews
level: medium
tags:
  - attack.discovery
  - attack.t1069
  - attack.t1069.002
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist security assessment tools and scheduled compliance scanners. Alert on enumeration from non-IT workstations.
- **Severity:** Medium

---

### T1082 — System Information Discovery

- **Data Sources:** DeviceProcessEvents
- **Description:** Adversaries may gather system information about the compromised host.

**KQL — System Information Enumeration**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where ProcessCommandLine has_any (
    "systeminfo", "hostname", "wmic os", "wmic cpu",
    "wmic csproduct", "Get-ComputerInfo", "reg query HKLM\\HARDWARE",
    "Get-CimInstance Win32_ComputerSystem", "msinfo32"
)
| where InitiatingProcessFileName !in~ ("explorer.exe", "SearchIndexer.exe")
| extend Severity = "Low"
| project Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — System Information Discovery**
```yaml
title: System Information Discovery
id: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c
status: experimental
description: Detects common system information discovery commands
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    CommandLine|contains:
      - 'systeminfo'
      - 'msinfo32'
      - 'hostname'
  condition: selection
falsepositives:
  - Helpdesk remote troubleshooting
  - Software inventory tools
  - User-initiated system information lookups
level: low
tags:
  - attack.discovery
  - attack.t1082
```

- **Expected FP Rate:** High  
- **Tuning:** Correlate with other discovery techniques — standalone `hostname` calls are almost always benign. Only alert when multiple discovery commands execute in rapid succession (within 5 minutes).
- **Severity:** Low

---

### T1046 — Network Service Discovery

- **Data Sources:** DeviceProcessEvents, DeviceNetworkEvents
- **Description:** Adversaries may scan network services to identify potential targets.

**KQL — Network Scanning Activity**
```kql
DeviceNetworkEvents
| where Timestamp > ago(1d)
| where RemotePort in (22, 23, 80, 443, 445, 3389, 5985, 5986)
    and RemoteIPType == "LAN"
| summarize ScanningCount = dcount(RemoteIP) by SourceIP = DeviceName,
    InitiatingProcessFileName, bin(Timestamp, 5m)
| where ScanningCount > 10
| extend Severity = iif(ScanningCount > 50, "High", "Medium")
| project Timestamp, SourceIP, InitiatingProcessFileName, ScanningCount, Severity
```

**Sigma Rule — Port Scanning**
```yaml
title: Port Scanning Activity
id: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d
status: experimental
description: Detects rapid connections to multiple remote hosts indicative of port scanning
logsource:
  category: network_connection
  product: windows
detection:
  selection:
    DestinationPort|contains:
      - '445'
      - '3389'
      - '5985'
      - '5986'
      - '22'
  condition: selection
falsepositives:
  - Vulnerability scanners (Nessus, Qualys)
  - Network monitoring tools
  - Application load balancers
level: medium
tags:
  - attack.discovery
  - attack.t1046
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist approved vulnerability scanners and network monitoring IPs. Use threshold baselines per device role (servers scan more than workstations).
- **Severity:** Medium

---

### T1005 — Data from Local System

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents, DeviceNetworkEvents
- **Description:** Adversaries may access data from local system files.

**KQL — Suspicious File Access Patterns**
```kql
DeviceFileEvents
| where Timestamp > ago(1d)
| where FolderPath matches regex @"(?i)(Desktop|Documents|Downloads|\bVPN\b|\bRDP\b|\.config|\.ssh|AppData\\)"
    and FileName matches regex @"(?i)\.(docx?|xlsx?|pptx?|pdf|csv|zip|rar|7z|sql|bak|mdf|ldf)$"
| where InitiatingProcessFileName !in~ ("explorer.exe", "OneDrive.exe", "SearchProtocolHost.exe")
| extend Severity = iif(
    FolderPath contains "\\.ssh\\" or FolderPath contains "VPN", "High",
    "Medium"
)
| project Timestamp, DeviceName, FileName, FolderPath, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Data Collection from Local Files**
```yaml
title: Bulk File Access from User Directories
id: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e
status: experimental
description: Detects bulk file access from user profile directories by non-explorer processes
logsource:
  category: file_access
  product: windows
detection:
  selection:
    ObjectName|contains:
      - '\Desktop\'
      - '\Documents\'
      - '\Downloads\'
  filter_explorer:
    ProcessName|endswith: '\explorer.exe'
  condition: selection and not filter_explorer
falsepositives:
  - Backups (OneDrive, Google Drive, Acronis)
  - IT migration tools
  - Antivirus scanning
level: medium
tags:
  - attack.collection
  - attack.t1005
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist backup and sync applications (OneDrive, Google Drive, iCloud). Alert when file count accessed exceeds 100 in 5 minutes from non-backup process.
- **Severity:** Medium

---

### T1074 — Data Staged

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents, DeviceNetworkEvents
- **Description:** Adversaries may collect and stage data before exfiltration.

**KQL — Data Staging (Compression + File Collection)**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where FileName has_any ("7z.exe", "7za.exe", "rar.exe", "winrar.exe",
    "zip.exe", "gzip.exe", "tar.exe") and not (a| where a=ProcessCommandLine, /* ... */)
| where ProcessCommandLine matches regex @"(?i)(-mx[0-9]|a\s+-t|\.7z|\.rar|\.zip)"
    and ProcessCommandLine matches regex @"(?i)(Documents|Desktop|\.config|\.ssh|AppData)"
| extend Severity = "High"
| project Timestamp, DeviceName, FileName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Data Compression Before Exfiltration**
```yaml
title: Data Compression in User Directories
id: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f
status: experimental
description: Detects archive tools compressing data from user profile directories
logsource:
  category: process_creation
  product: windows
detection:
  selection_img:
    Image|endswith:
      - '\7z.exe'
      - '\rar.exe'
      - '\winrar.exe'
      - '\zip.exe'
  selection_dir:
    CommandLine|contains:
      - '\Users\'
      - '\Desktop\'
      - '\Documents\'
  condition: selection_img and selection_dir
falsepositives:
  - User manually backing up documents to archives
  - IT migration creating backups
  - Archival tools
level: high
tags:
  - attack.collection
  - attack.t1074
```

- **Expected FP Rate:** Medium  
- **Tuning:** Apply threshold of total data > 100 MB within an hour. Whitelist known archival tools running from scheduled tasks.
- **Severity:** High

---

### T1048 — Exfiltration Over Alternative Protocol

- **Data Sources:** DeviceNetworkEvents
- **Description:** Adversaries may exfiltrate data over an alternative protocol (FTP, SMTP, etc.).

**KQL — Unusual Outbound Protocol Usage**
```kql
DeviceNetworkEvents
| where Timestamp > ago(1d)
| where RemotePort in (21, 25, 465, 587, 993, 995) // FTP, SMTP, IMAP, POP3
    and Direction == "Outbound"
| where RemoteUrl !contains ".microsoft.com" and RemoteUrl !contains ".outlook.com"
| summarize ConnectionCount = count(), TotalBytes = sum(SentBytes)
    by DeviceName, RemoteIP, RemotePort, InitiatingProcessFileName, bin(Timestamp, 15m)
| where TotalBytes > 50000000 // > 50 MB
| extend Severity = "High"
| project Timestamp, DeviceName, InitiatingProcessFileName, RemoteIP, RemotePort, TotalBytes, Severity
```

**Sigma Rule — Exfiltration over SMTP**
```yaml
title: Large Outbound Data Transfer over Alternative Protocol
id: 9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4a
status: experimental
description: Detects large outbound data transfers over ports 25, 465, or 587 (SMTP)
logsource:
  category: network_connection
  product: windows
detection:
  selection:
    DestinationPort: 25
  condition: selection
falsepositives:
  - Email servers sending legitimate mail
  - Monitoring or log shipping tools
level: high
tags:
  - attack.exfiltration
  - attack.t1048
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist corporate email servers and approved mail relay IPs. Use byte count thresholds (> 10 MB over SMTP in 1 hour).
- **Severity:** High

---

### T1567 — Exfiltration Over Web Service

- **Data Sources:** DeviceNetworkEvents
- **Description:** Adversaries may exfiltrate data over web services (pastebin, GitHub, cloud storage).

**KQL — Data Exfiltration to Cloud Storage**
```kql
DeviceNetworkEvents
| where Timestamp > ago(1d)
| where RemoteUrl matches regex @"(?i)(pastebin\.com|api\.github\.com|api\.gitlab\.com|api\.bitbucket\.org|
    dropbox\.com|api\.onedrive\.com|s3\.amazonaws\.com|drive\.google\.com|transfer\.sh|file\.io)"
    and Direction == "Outbound"
| summarize TotalBytes = sum(SentBytes), FileCount = count()
    by DeviceName, InitiatingProcessFileName, RemoteUrl, bin(Timestamp, 15m)
| where TotalBytes > 10000000 // > 10 MB
| extend Severity = "High"
| project Timestamp, DeviceName, InitiatingProcessFileName, RemoteUrl, TotalBytes, Severity
```

**Sigma Rule — Exfiltration to Web Services**
```yaml
title: Data Upload to Cloud/Web Service
id: 0e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b
status: experimental
description: Detects large data uploads to common web storage services
logsource:
  category: network_connection
  product: windows
detection:
  selection:
    DestinationHostname|contains:
      - 'pastebin.com'
      - 'transfer.sh'
      - 'file.io'
      - 'dropbox.com'
      - 'drive.google.com'
  condition: selection
falsepositives:
  - Corporate cloud storage sync clients
  - Developers uploading legitimate code
level: high
tags:
  - attack.exfiltration
  - attack.t1567
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist corporate cloud sync clients running from known installation paths. Use DLP integration to inspect content before alerting.
- **Severity:** High

---

### T1490 — Inhibit System Recovery

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents
- **Description:** Adversaries may delete or disable system recovery features (shadow copies, backups).

**KQL — Shadow Copy / Backup Deletion**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where ProcessCommandLine has_any (
    "vssadmin delete shadows", "wmic shadowcopy delete",
    "bcdedit /set {default} recoveryenabled No",
    "bcdedit /set {default} bootstatuspolicy ignoreallfailures",
    "wbadmin delete catalog", "diskshadow -s", "vssadmin resize shadowstorage"
)
| extend Severity = "Critical"
| project Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Volume Shadow Copy Deletion**
```yaml
title: Volume Shadow Copy Deletion
id: 1f2a3b4c-5d6e-7f8a-9b0c-1d2e3f4a5b6c
status: experimental
description: Detects attempts to delete volume shadow copies (ransomware precursor)
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    CommandLine|contains:
      - 'vssadmin delete shadows'
      - 'wmic shadowcopy delete'
      - 'bcdedit /set {default} recoveryenabled No'
      - 'wbadmin delete catalog'
  condition: selection
falsepositives:
  - IT administrators reclaiming disk space
  - Scripted cleanup routines
level: critical
tags:
  - attack.impact
  - attack.t1490
```

- **Expected FP Rate:** Low  
- **Tuning:** Only whitelist after exception with documented approval and time window. Alert should be immediate — this is a strong ransomware indicator.
- **Severity:** Critical

---

### T1486 — Data Encrypted for Impact

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents, DeviceRegistryEvents, DeviceNetworkEvents
- **Description:** Adversaries may encrypt data to impact business operations (ransomware).

**KQL — Ransomware-Like File Extension Changes**
```kql
DeviceFileEvents
| where Timestamp > ago(1d)
| where FolderPath matches regex @"(?i)\.(locked|encrypted|crypt|wanna|payme|help_|readme)"
    or FileName matches regex @"(?i)\.(locked|encrypted|cryptor|wannacry|badger)"
| extend Severity = "Critical"
| project Timestamp, DeviceName, FileName, FolderPath, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Ransomware File Extension Pattern**
```yaml
title: Ransomware File Extension Detection
id: 2a3b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
status: experimental
description: Detects file extensions commonly associated with ransomware encryption
logsource:
  category: file_event
  product: windows
detection:
  selection:
    TargetFilename|endswith:
      - '.locked'
      - '.encrypted'
      - '.crypt'
      - '.wannacry'
      - '.cryptor'
  condition: selection
falsepositives:
  - User intentionally renaming files
  - Legitimate encryption tools (BitLocker, EFS)
  - Penetration testing exercises
level: critical
tags:
  - attack.impact
  - attack.t1486
```

- **Expected FP Rate:** Low  
- **Tuning:** Correlate with process tree — a legitimate encryption tool will have a different parent process chain than ransomware. Alert on > 10 new `.locked` files in 1 minute.
- **Severity:** Critical

---

### T1562 — Impair Defenses

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents, AuditPolicyChange
- **Description:** Adversaries may disable or modify security tools.

**KQL — Security Tool Disabling**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where ProcessCommandLine has_any (
    "net stop", "sc stop", "sc config", "Set-MpPreference",
    "DisableRealtimeMonitoring", "DisableBehaviorMonitoring",
    "Set-ItemProperty -Path HKLM:\\Software\\Policies\\Microsoft\\Windows Defender",
    "reg delete HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
    "wevtutil cl", "wevtutil clear-log", "wevtutil sl"
)
| where ProcessCommandLine matches regex @"(?i)(WinDefend|Sense|NisSrv|MsMpEng|wscsvc|security|defender)"
| extend Severity = "Critical"
| project Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Disabling Windows Defender**
```yaml
title: Windows Defender Disabled via PowerShell
id: 3b4c5d6e-7f8a-9b0c-1d2e-3f4a5b6c7d8e
status: experimental
description: Detects attempts to disable Windows Defender real-time monitoring
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    CommandLine|contains|all:
      - 'Set-MpPreference'
      - 'DisableRealtimeMonitoring'
      - 'true'
  condition: selection
falsepositives:
  - IT administering defender policies via script
  - GPO application reconfiguring settings
level: critical
tags:
  - attack.defense-evasion
  - attack.t1562
  - attack.t1562.001
```

- **Expected FP Rate:** Low  
- **Tuning:** Whitelist configuration management agents (GPO, SCCM, Intune). Alert on registry-based disablement that originates from non-`SYSTEM` or non-management tool processes.
- **Severity:** Critical

---

### T1218 — Signed Binary Proxy Execution

- **Data Sources:** DeviceProcessEvents, DeviceFileEvents
- **Description:** Adversaries may use signed binaries (Mshta, Rundll32, Regsvr32, etc.) to proxy execution of malicious code.

**KQL — Living-off-the-Land Binary Execution**
```kql
DeviceProcessEvents
| where Timestamp > ago(1d)
| where FileName has_any ("mshta.exe", "rundll32.exe", "regsvr32.exe",
    "regsvcs.exe", "regasm.exe", "installutil.exe", "msiexec.exe",
    "cscript.exe", "wscript.exe", "cmstp.exe", "hh.exe", "odbcconf.exe")
| where ProcessCommandLine matches regex @"(?i)(http|https|ftp|file://|javascript:|vbscript:|\.hta|.sct|.cpl)"
| extend Severity = case(
    FileName == "mshta.exe" and ProcessCommandLine contains "http", "High",
    FileName == "rundll32.exe" and ProcessCommandLine contains "http", "High",
    "Medium"
)
| project Timestamp, DeviceName, FileName, ProcessCommandLine, InitiatingProcessAccountName, Severity
```

**Sigma Rule — Mshta Executing Remote URL**
```yaml
title: Mshta Executing Remote URL
id: 4c5d6e7f-8a9b-0c1d-2e3f-4a5b6c7d8e9f
status: experimental
description: Detects mshta.exe executing an HTA from a remote URL
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\mshta.exe'
    CommandLine|contains:
      - 'http://'
      - 'https://'
  condition: selection
falsepositives:
  - Legitimate web-based HTA applications
  - Internal tools using HTA for UI
level: high
tags:
  - attack.defense-evasion
  - attack.t1218
  - attack.t1218.005
```

- **Expected FP Rate:** Medium  
- **Tuning:** Whitelist internal URLs hosting legitimate HTAs. Alert on any `rundll32.exe` or `regsvr32.exe` with network connections to external domains.
- **Severity:** High

---

## Tuning Guidance Reference

| Technique ID | Technique | Common False Positive Sources | Tuning Strategy |
|---|---|---|---|
| T1078 | Valid Accounts | VPN/VPN gateways, service accounts, admins working remotely | Build IP baselines per account; whitelist known VPN egress ranges |
| T1136 | Create Account | HR onboarding systems, identity management tools | Whitelist provisioning service accounts; alert on off-hours creation |
| T1098 | Account Manipulation | Helpdesk password reset tools, SSPR systems | Whitelist approved helpdesk accounts and SSPR infrastructure |
| T1552 | Unsecured Credentials | Password rotation tools, password managers | Whitelist IT audit tools and password manager processes |
| T1040 | Network Sniffing | Network team analysis tools | Maintain approved tool + account list; alert on non-approved execution |
| T1059 | Command & Scripting | Automation scripts (SCCM, PDQ, Ansible) | Whitelist management tool parent processes |
| T1053 | Scheduled Task | Software installers, GPO tasks | Whitelist Microsoft and management tool tasks by path |
| T1003 | OS Credential Dumping | Forensic analysis, approved EDR | Almost always malicious; require formal exception process |
| T1087 | Account Discovery | Helpdesk scripts, logon scripts, inventory scans | Whitelist known admin workstations; baseline per-host frequency |
| T1069 | Permission Groups | Security reviews, compliance scanners | Whitelist scheduled scanner service accounts |
| T1082 | System Info | Helpdesk troubleshooting, inventory tools | Correlate with other discovery; ignore standalone hostname |
| T1046 | Network Service Discovery | Vuln scanners, network monitoring | Whitelist scanner IPs; use per-role baseline thresholds |
| T1005 | Data from Local System | Backups, sync tools, AV scans | Whitelist OneDrive/Google Drive; alert on volume spikes |
| T1074 | Data Staged | Manual user backups, archival tasks | Threshold >100 MB/hour; whitelist known archive tasks |
| T1048 | Exfiltration Alt Protocol | Email servers, log shipping | Whitelist corporate MTA IPs; threshold >10 MB SMTP/hour |
| T1567 | Exfiltration Web Service | Cloud sync, dev git pushes | Whitelist corporate cloud sync; integrate DLP content inspection |
| T1490 | Inhibit System Recovery | Admin disk cleanup routines | Require formal exception; alert immediately |
| T1486 | Data Encrypted for Impact | Penetration tests, legit encryption | Correlate with file count >10 in 1 minute; check process tree |
| T1562 | Impair Defenses | GPO/Intune policy application | Whitelist management tool PIDs; alert on ad-hoc disablement |
| T1218 | Signed Binary Proxy | Internal HTA applications, legacy tools | Whitelist internal URLs; alert on any external URL in LOLBins |

---

## Query Library Structure

The detection queries are organized in the following file hierarchy:

```
detection/
├── detection-engineering-framework-v1.md       ← This document
├── query-library/
│   ├── kql/
│   │   ├── t1078_valid_accounts.kql
│   │   ├── t1136_create_account.kql
│   │   ├── t1098_account_manipulation.kql
│   │   ├── t1552_unsecured_credentials.kql
│   │   ├── t1040_network_sniffing.kql
│   │   ├── t1059_command_scripting.kql
│   │   ├── t1053_scheduled_task.kql
│   │   ├── t1003_credential_dumping.kql
│   │   ├── t1087_account_discovery.kql
│   │   ├── t1069_permission_groups_discovery.kql
│   │   ├── t1082_system_info_discovery.kql
│   │   ├── t1046_network_service_discovery.kql
│   │   ├── t1005_data_from_local_system.kql
│   │   ├── t1074_data_staged.kql
│   │   ├── t1048_exfiltration_alt_protocol.kql
│   │   ├── t1567_exfiltration_web_service.kql
│   │   ├── t1490_inhibit_system_recovery.kql
│   │   ├── t1486_data_encrypted_for_impact.kql
│   │   ├── t1562_impair_defenses.kql
│   │   └── t1218_signed_binary_proxy.kql
│   └── sigma/
│       ├── t1078_valid_accounts/
│       │   ├── win_account_login_unusual_ip.yml
│       │   └── win_account_login_geolocation.yml
│       ├── t1136_create_account/
│       │   ├── win_user_account_created.yml
│       │   └── win_account_creation_non_business_hours.yml
│       ├── t1098_account_manipulation/
│       │   ├── win_password_reset_non_admin.yml
│       │   └── win_account_sid_history_added.yml
│       ├── t1552_unsecured_credentials/
│       │   ├── win_credential_file_search.yml
│       │   └── win_registry_credential_search.yml
│       ├── t1040_network_sniffing/
│       │   ├── win_packet_capture_tools.yml
│       │   └── win_promiscuous_mode_enabled.yml
│       ├── t1059_command_scripting/
│       │   ├── win_powershell_suspicious_params.yml
│       │   ├── win_wmi_script_execution.yml
│       │   └── win_cscript_wscript_execution.yml
│       ├── t1053_scheduled_task/
│       │   ├── win_scheduled_task_creation.yml
│       │   └── win_scheduled_task_modification.yml
│       ├── t1003_credential_dumping/
│       │   ├── win_credential_dumping_tools.yml
│       │   ├── win_lsass_handle_request.yml
│       │   └── win_sam_dump_detection.yml
│       ├── t1087_account_discovery/
│       │   ├── win_account_discovery_net.yml
│       │   └── win_account_discovery_powershell.yml
│       ├── t1069_permission_groups_discovery/
│       │   ├── win_admin_group_enumeration.yml
│       │   └── win_domain_group_enumeration.yml
│       ├── t1082_system_info_discovery/
│       │   ├── win_system_info_commands.yml
│       │   └── win_system_discovery_dxdiag.yml
│       ├── t1046_network_service_discovery/
│       │   ├── win_port_scanning_activity.yml
│       │   └── win_network_connections_scanning.yml
│       ├── t1005_data_from_local_system/
│       │   ├── win_data_collection_user_dirs.yml
│       │   └── win_suspicious_file_access_patterns.yml
│       ├── t1074_data_staged/
│       │   ├── win_data_compression_to_archive.yml
│       │   └── win_staging_directory_creation.yml
│       ├── t1048_exfiltration_alt_protocol/
│       │   ├── win_exfiltration_over_smtp.yml
│       │   ├── win_exfiltration_over_dns.yml
│       │   └── win_exfiltration_over_ftp.yml
│       ├── t1567_exfiltration_web_service/
│       │   ├── win_exfiltration_web_upload.yml
│       │   └── win_exfiltration_pastebin.yml
│       ├── t1490_inhibit_system_recovery/
│       │   ├── win_shadow_copy_deletion.yml
│       │   └── win_backup_deletion.yml
│       ├── t1486_data_encrypted_for_impact/
│       │   ├── win_ransomware_extension_patterns.yml
│       │   └── win_mass_file_renaming.yml
│       ├── t1562_impair_defenses/
│       │   ├── win_defender_disabled.yml
│       │   ├── win_firewall_rule_deletion.yml
│       │   └── win_event_log_cleared.yml
│       └── t1218_signed_binary_proxy/
│           ├── win_mshta_remote_url.yml
│           ├── win_rundll32_remote_url.yml
│           ├── win_regsvr32_squiblydoo.yml
│           └── win_cmstp_execution.yml
└── tuning/
    └── tuning_guidelines.md
```

---

## Alert Severity Taxonomy

| Severity | Color | SLA | Criteria | Example |
|---|---|---|---|---|
| **Critical** | Red | < 15 min | Active ransomware, credential dumping, defense impairment, backup deletion | T1490, T1486, T1003, T1562 |
| **High** | Orange | < 1 hour | Active exfiltration, persistence, LOLBin execution with remote URL | T1048, T1567, T1218, T1074 |
| **Medium** | Yellow | < 4 hours | Suspicious account activity, discovery scans, data access patterns | T1078, T1136, T1098, T1046, T1053 |
| **Low** | Blue | < 24 hours | Benign-but-curious recon, standalone hostname calls | T1087, T1082, T1069 (standalone) |

---

## Appendix: Useful References

1. **MITRE ATT&CK Enterprise v14** — https://attack.mitre.org/
2. **Sigma Rule Specification v2** — https://github.com/SigmaHQ/sigma-specification
3. **Microsoft 365 Security Documentation** — https://learn.microsoft.com/en-us/microsoft-365/security/
4. **Kusto Query Language Reference** — https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/
5. **Microsoft Defender for Endpoint Advanced Hunting** — https://learn.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-overview
6. **Detection Engineering Maturity Model** — https://detectionengineering.io/
7. **LOLBAS Project (Living Off The Land Binaries)** — https://lolbas-project.github.io/

---

*End of Document — Detection Engineering Framework v1.0*
"""

import os

output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "detection-engineering-framework-v1.md"
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(DOC)

print(f"Framework document written to: {output_path}")
print(f"Total characters: {len(DOC)}")
print(f"Approx word count: {len(DOC.split())}")
