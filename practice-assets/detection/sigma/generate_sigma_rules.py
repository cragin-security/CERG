#!/usr/bin/env python3
"""
Generate standalone Sigma rule files from the CERG Detection Engineering Framework v1.0.
Creates one .yml file per MITRE ATT&CK technique in practice-assets/detection/sigma/.
"""

import uuid
import os
import json

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

techniques = [
    {
        "t_id": "T1078",
        "name": "valid_accounts",
        "title": "Valid Accounts - T1078",
        "category": "authentication",
        "product": "windows",
        "description": "anomalous remote logons from unusual IP addresses indicating use of valid accounts by adversaries",
        "detection_yaml": """  selection:
    EventID: 4624
    LogonType: '3'
  filter_known:
    AccountName|startswith:
      - SYSTEM
      - ANONYMOUS
      - LOCAL
  condition: selection and not filter_known""",
        "level": "medium",
        "tags_extra": ["attack.initial-access", "attack.t1078"],
        "falsepositives": ["Legitimate remote workers with dynamic IPs", "VPN gateway IPs that rotate"]
    },
    {
        "t_id": "T1136",
        "name": "create_account",
        "title": "Create Account - T1136",
        "category": "authentication",
        "product": "windows",
        "description": "creation of new user accounts as a persistence technique",
        "detection_yaml": """  selection:
    EventID: 4720
  condition: selection""",
        "level": "medium",
        "tags_extra": ["attack.persistence", "attack.t1136"],
        "falsepositives": ["IT helpdesk creating accounts for new hires", "Automated provisioning systems"]
    },
    {
        "t_id": "T1098",
        "name": "account_manipulation",
        "title": "Account Manipulation - T1098",
        "category": "authentication",
        "product": "windows",
        "description": "password reset and account modification events performed by non-administrative accounts",
        "detection_yaml": """  selection:
    EventID: 4724
  filter_admins:
    SubjectUserName|endswith:
      - '$'
      - 'Administrator'
      - 'ADM_'
  condition: selection and not filter_admins""",
        "level": "high",
        "tags_extra": ["attack.persistence", "attack.t1098", "attack.privilege-escalation"],
        "falsepositives": ["Delegated password reset via helpdesk tools", "Self-service password reset systems"]
    },
    {
        "t_id": "T1552",
        "name": "unsecured_credentials",
        "title": "Unsecured Credentials - T1552",
        "category": "process_creation",
        "product": "windows",
        "description": "command-line searches for credential-related files or registry keys",
        "detection_yaml": """  selection:
    CommandLine|contains:
      - 'passwords'
      - 'secrets'
      - 'credentials'
      - '.kdbx'
      - 'id_rsa'
      - 'vaultcmd'
  condition: selection""",
        "level": "medium",
        "tags_extra": ["attack.credential-access", "attack.t1552"],
        "falsepositives": ["IT audit or password rotation scripts", "Password managers performing lookups"]
    },
    {
        "t_id": "T1040",
        "name": "network_sniffing",
        "title": "Network Sniffing - T1040",
        "category": "process_creation",
        "product": "windows",
        "description": "execution of common network sniffing and packet capture tools",
        "detection_yaml": """  selection_img:
    Image|endswith:
      - '\\tcpdump.exe'
      - '\\wireshark.exe'
      - '\\tshark.exe'
      - '\\dumpcap.exe'
      - '\\pktmon.exe'
      - '\\windump.exe'
  selection_cli:
    CommandLine|contains:
      - ' -i '
      - ' promisc'
      - ' -P '
  condition: selection_img or selection_cli""",
        "level": "high",
        "tags_extra": ["attack.credential-access", "attack.t1040", "attack.discovery"],
        "falsepositives": ["Network administrators performing legitimate packet analysis", "Threat hunting team's approved tools"]
    },
    {
        "t_id": "T1059",
        "name": "command_and_scripting_interpreter",
        "title": "Command and Scripting Interpreter - T1059",
        "category": "process_creation",
        "product": "windows",
        "description": "PowerShell execution with suspicious parameters commonly used by attackers",
        "detection_yaml": """  selection:
    Image|endswith: '\\powershell.exe'
    CommandLine|contains:
      - '-EncodedCommand'
      - '-ExecutionPolicy Bypass'
      - 'IEX ('
      - 'Invoke-Expression'
      - 'DownloadString'
      - '-WindowStyle Hidden'
      - '-NoProfile'
  condition: selection""",
        "level": "high",
        "tags_extra": ["attack.execution", "attack.t1059", "attack.t1059.001"],
        "falsepositives": ["IT automation and deployment scripts (SCCM, PDQ, Ansible)", "Approved administrative tooling"]
    },
    {
        "t_id": "T1053",
        "name": "scheduled_task_job",
        "title": "Scheduled Task/Job - T1053",
        "category": "process_creation",
        "product": "windows",
        "description": "creation of scheduled tasks, especially those executing scripts as a persistence mechanism",
        "detection_yaml": """  selection:
    EventID: 4698
  filter_microsoft:
    TaskName|startswith: 'Microsoft\\Windows\\'
  condition: selection and not filter_microsoft""",
        "level": "medium",
        "tags_extra": ["attack.execution", "attack.persistence", "attack.t1053", "attack.t1053.005"],
        "falsepositives": ["Software installers creating update tasks", "IT management tools (SCCM, GPO scheduling)"]
    },
    {
        "t_id": "T1003",
        "name": "os_credential_dumping",
        "title": "OS Credential Dumping - T1003",
        "category": "process_creation",
        "product": "windows",
        "description": "execution of known credential dumping tools targeting LSASS or SAM",
        "detection_yaml": """  selection_img:
    Image|endswith:
      - '\\procdump.exe'
      - '\\procdump64.exe'
      - '\\mimikatz.exe'
  selection_cli:
    CommandLine|contains:
      - 'sekurlsa::logonPasswords'
      - '-ma lsass'
      - 'comsvcs.dll #24'
      - 'MiniDump'
  condition: selection_img or selection_cli""",
        "level": "critical",
        "tags_extra": ["attack.credential-access", "attack.t1003", "attack.t1003.001"],
        "falsepositives": ["Forensic investigators performing legitimate memory analysis", "Approved EDR/Linux cross-platform tooling"]
    },
    {
        "t_id": "T1087",
        "name": "account_discovery",
        "title": "Account Discovery - T1087",
        "category": "process_creation",
        "product": "windows",
        "description": "use of net.exe/net1.exe for user and group enumeration",
        "detection_yaml": """  selection:
    Image|endswith:
      - '\\net.exe'
      - '\\net1.exe'
    CommandLine|contains:
      - ' user '
      - ' group '
      - ' localgroup '
      - ' accounts '
  condition: selection""",
        "level": "low",
        "tags_extra": ["attack.discovery", "attack.t1087", "attack.t1087.001"],
        "falsepositives": ["Helpdesk scripts performing user lookups", "Logon scripts enumerating groups", "IT inventory tools"]
    },
    {
        "t_id": "T1069",
        "name": "permission_groups_discovery",
        "title": "Permission Groups Discovery - T1069",
        "category": "process_creation",
        "product": "windows",
        "description": "enumeration of local or domain admin groups for discovery purposes",
        "detection_yaml": """  selection:
    CommandLine|contains:
      - 'administrators'
      - 'domain admins'
      - 'enterprise admins'
      - 'schema admins'
  condition: selection""",
        "level": "medium",
        "tags_extra": ["attack.discovery", "attack.t1069", "attack.t1069.002"],
        "falsepositives": ["Domain admin troubleshooting tools", "Security tools performing access reviews"]
    },
    {
        "t_id": "T1082",
        "name": "system_information_discovery",
        "title": "System Information Discovery - T1082",
        "category": "process_creation",
        "product": "windows",
        "description": "common system information discovery commands used by adversaries for reconnaissance",
        "detection_yaml": """  selection:
    CommandLine|contains:
      - 'systeminfo'
      - 'msinfo32'
      - 'hostname'
  condition: selection""",
        "level": "low",
        "tags_extra": ["attack.discovery", "attack.t1082"],
        "falsepositives": ["Helpdesk remote troubleshooting", "Software inventory tools", "User-initiated system information lookups"]
    },
    {
        "t_id": "T1046",
        "name": "network_service_discovery",
        "title": "Network Service Discovery - T1046",
        "category": "network_connection",
        "product": "windows",
        "description": "rapid connections to multiple remote hosts indicative of port scanning for network service discovery",
        "detection_yaml": """  selection:
    DestinationPort|contains:
      - '445'
      - '3389'
      - '5985'
      - '5986'
      - '22'
  condition: selection""",
        "level": "medium",
        "tags_extra": ["attack.discovery", "attack.t1046"],
        "falsepositives": ["Vulnerability scanners (Nessus, Qualys)", "Network monitoring tools", "Application load balancers"]
    },
    {
        "t_id": "T1005",
        "name": "data_from_local_system",
        "title": "Data from Local System - T1005",
        "category": "file_event",
        "product": "windows",
        "description": "bulk file access from user profile directories by non-explorer processes indicating data collection",
        "detection_yaml": """  selection:
    ObjectName|contains:
      - '\\Desktop\\'
      - '\\Documents\\'
      - '\\Downloads\\'
  filter_explorer:
    ProcessName|endswith: '\\explorer.exe'
  condition: selection and not filter_explorer""",
        "level": "medium",
        "tags_extra": ["attack.collection", "attack.t1005"],
        "falsepositives": ["Backups (OneDrive, Google Drive, Acronis)", "IT migration tools", "Antivirus scanning"]
    },
    {
        "t_id": "T1074",
        "name": "data_staged",
        "title": "Data Staged - T1074",
        "category": "process_creation",
        "product": "windows",
        "description": "archive tools compressing data from user profile directories as staging before exfiltration",
        "detection_yaml": """  selection_img:
    Image|endswith:
      - '\\7z.exe'
      - '\\rar.exe'
      - '\\winrar.exe'
      - '\\zip.exe'
  selection_dir:
    CommandLine|contains:
      - '\\Users\\'
      - '\\Desktop\\'
      - '\\Documents\\'
  condition: selection_img and selection_dir""",
        "level": "high",
        "tags_extra": ["attack.collection", "attack.t1074"],
        "falsepositives": ["User manually backing up documents to archives", "IT migration creating backups", "Archival tools"]
    },
    {
        "t_id": "T1048",
        "name": "exfiltration_over_alternative_protocol",
        "title": "Exfiltration Over Alternative Protocol - T1048",
        "category": "network_connection",
        "product": "windows",
        "description": "large outbound data transfers over alternative protocols (SMTP, FTP) indicating exfiltration",
        "detection_yaml": """  selection:
    DestinationPort: 25
  condition: selection""",
        "level": "high",
        "tags_extra": ["attack.exfiltration", "attack.t1048"],
        "falsepositives": ["Email servers sending legitimate mail", "Monitoring or log shipping tools"]
    },
    {
        "t_id": "T1567",
        "name": "exfiltration_over_web_service",
        "title": "Exfiltration Over Web Service - T1567",
        "category": "network_connection",
        "product": "windows",
        "description": "large data uploads to common web storage and file sharing services indicating exfiltration",
        "detection_yaml": """  selection:
    DestinationHostname|contains:
      - 'pastebin.com'
      - 'transfer.sh'
      - 'file.io'
      - 'dropbox.com'
      - 'drive.google.com'
  condition: selection""",
        "level": "high",
        "tags_extra": ["attack.exfiltration", "attack.t1567"],
        "falsepositives": ["Corporate cloud storage sync clients", "Developers uploading legitimate code"]
    },
    {
        "t_id": "T1490",
        "name": "inhibit_system_recovery",
        "title": "Inhibit System Recovery - T1490",
        "category": "process_creation",
        "product": "windows",
        "description": "attempts to delete volume shadow copies or disable system recovery (ransomware precursor)",
        "detection_yaml": """  selection:
    CommandLine|contains:
      - 'vssadmin delete shadows'
      - 'wmic shadowcopy delete'
      - 'bcdedit /set {default} recoveryenabled No'
      - 'wbadmin delete catalog'
  condition: selection""",
        "level": "critical",
        "tags_extra": ["attack.impact", "attack.t1490"],
        "falsepositives": ["IT administrators reclaiming disk space", "Scripted cleanup routines"]
    },
    {
        "t_id": "T1486",
        "name": "data_encrypted_for_impact",
        "title": "Data Encrypted for Impact - T1486",
        "category": "file_event",
        "product": "windows",
        "description": "file extensions commonly associated with ransomware encryption indicating data encrypted for impact",
        "detection_yaml": """  selection:
    TargetFilename|endswith:
      - '.locked'
      - '.encrypted'
      - '.crypt'
      - '.wannacry'
      - '.cryptor'
  condition: selection""",
        "level": "critical",
        "tags_extra": ["attack.impact", "attack.t1486"],
        "falsepositives": ["User intentionally renaming files", "Legitimate encryption tools (BitLocker, EFS)", "Penetration testing exercises"]
    },
    {
        "t_id": "T1562",
        "name": "impair_defenses",
        "title": "Impair Defenses - T1562",
        "category": "process_creation",
        "product": "windows",
        "description": "attempts to disable Windows Defender real-time monitoring or other security controls",
        "detection_yaml": """  selection:
    CommandLine|contains|all:
      - 'Set-MpPreference'
      - 'DisableRealtimeMonitoring'
      - 'true'
  condition: selection""",
        "level": "critical",
        "tags_extra": ["attack.defense-evasion", "attack.t1562", "attack.t1562.001"],
        "falsepositives": ["IT administering defender policies via script", "GPO application reconfiguring settings"]
    },
    {
        "t_id": "T1218",
        "name": "signed_binary_proxy_execution",
        "title": "Signed Binary Proxy Execution - T1218",
        "category": "process_creation",
        "product": "windows",
        "description": "mshta.exe executing an HTA from a remote URL as a signed binary proxy execution technique",
        "detection_yaml": """  selection:
    Image|endswith: '\\mshta.exe'
    CommandLine|contains:
      - 'http://'
      - 'https://'
  condition: selection""",
        "level": "high",
        "tags_extra": ["attack.defense-evasion", "attack.t1218", "attack.t1218.005"],
        "falsepositives": ["Legitimate web-based HTA applications", "Internal tools using HTA for UI"]
    },
]


def yaml_list(items, indent=2):
    """Format a list as YAML list items."""
    prefix = " " * indent
    lines = []
    for item in items:
        if isinstance(item, str):
            if "'" in item:
                quoted = '"' + item + '"'
            else:
                quoted = "'" + item + "'"
            lines.append(f"{prefix}- {quoted}")
        else:
            lines.append(f"{prefix}- {item}")
    return "\n".join(lines)


def build_sigma_file(t):
    """Build the complete Sigma YAML file content."""
    t_id = t["t_id"]
    t_lower = t_id.lower()

    lines = []
    lines.append(f"title: {t['title']}")
    lines.append(f"id: {uuid.uuid4()}")
    lines.append(f"status: experimental")
    lines.append(f"description: Detects {t['description']} based on CERG Detection Engineering Framework")
    lines.append(f"references:")
    lines.append(f"  - https://attack.mitre.org/techniques/{t_id}/")
    lines.append(f"author: CERG Detection Engineering Team")
    lines.append(f"date: 2026-06-30")
    lines.append(f"modified: 2026-06-30")
    lines.append(f"tags:")
    # Collect unique tags
    tag_set = []
    seen = set()
    for tag in [f"attack.{t_lower}", f"attack.{t['name']}"] + t["tags_extra"]:
        if tag not in seen:
            seen.add(tag)
            tag_set.append(tag)
    for tag in tag_set:
        lines.append(f"  - {tag}")
    lines.append(f"logsource:")
    lines.append(f"  category: {t['category']}")
    lines.append(f"  product: {t['product']}")
    lines.append(f"detection:")
    lines.append(t["detection_yaml"])
    lines.append(f"falsepositives:")
    for fp in t["falsepositives"]:
        lines.append(f"  - '{fp}'")
    lines.append(f"level: {t['level']}")

    return "\n".join(lines) + "\n"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for t in techniques:
        t_id = t["t_id"]
        filename = f"{t_id.lower()}_{t['name']}.yml"
        filepath = os.path.join(OUTPUT_DIR, filename)

        content = build_sigma_file(t)

        with open(filepath, 'w') as f:
            f.write(content)

        print(f"Created: {filename}")

    # Count files
    files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.endswith('.yml') and f != 'generate_sigma_rules.yml'])
    count = len(files)
    print(f"\nTotal Sigma rule files created: {count}")
    for f in files:
        print(f"  {f}")


if __name__ == "__main__":
    main()
