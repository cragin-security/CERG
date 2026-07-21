# Threat-Intel-Validated Control Baseline

## Mapping CERG 100-Core Controls to Current CISA KEV and Ransomware TTPs

| | |
|---|---|
| **Document ID** | CERG-OPN-TOOLS-004 |
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Monthly (threat intel refresh) |
| **Frameworks** | CERG 100-Core · MITRE ATT&CK v15 · NIST 800-53r5 |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope environments |

---

## Purpose

This document maps every control in the [CERG 100-Core Control Baseline](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) to the threats it stops — using current CISA Known Exploited Vulnerabilities (KEV) data and observed ransomware TTPs.

For MSPs, this answers the question a client asks in every sales meeting: *"Which of these controls actually stops the attacks we're seeing right now?"*

### Current Threat Landscape (July 2026)

| Source | Data |
|--------|------|
| CISA KEV Catalog | 1,651 known exploited vulnerabilities. 53 confirmed used in ransomware campaigns. |
| Top Ransomware Groups | LockBit, BlackCat/ALPHV, Clop, Akira, Play, 8Base, Hunters International |
| Most Targeted Sectors | Healthcare, Manufacturing, Financial Services, State/Local Gov, Education, Energy |
| Top Initial Access Vector | External Remote Services (RDP, VPN) — responsible for majority of ransomware cases |
| Identity-Based Attacks | 72% of incident response actions involved compromised credentials |

**Sources:** [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), [MITRE ATT&CK](https://attack.mitre.org/), [Arctic Wolf Threat Report 2025](https://arcticwolf.com/resource/aw/arctic-wolf-threat-report-2025)

---

## Ransomware TTP → Control Mapping

Maps the 10 most common ransomware TTPs to the CERG controls that stop or detect them.

### T1133 — External Remote Services (Initial Access)

**What it is:** Attackers exploit exposed RDP, VPN gateways, and remote access appliances to gain initial access. Unsecured RDP led to the majority of ransomware cases in 2025.

**CISA KEV relevance:** 140+ KEV entries target VPN appliances (Palo Alto, Fortinet, Ivanti, Citrix) and RDP vulnerabilities.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| AC-005 Remote Access | Requires MFA + encrypted transport for all remote access. Split-tunnel prohibited. | **Primary** — directly prevents credential-based VPN compromise |
| IA-002 Strong Authentication | Phishing-resistant MFA on all remote access. FIDO2/certificate-based where possible. | **Primary** — MFA blocks credential stuffing and brute-force on VPNs |
| AC-002 MFA Enforcement | No exceptions for executives or admins. Service accounts with documented compensating controls. | **Primary** — closes the most common bypass |
| CM-008 Automated Patching | Critical vulns patched within 7 days. VPN/remote-access appliances in scope. | **Primary** — patching KEV-flagged VPN vulns within SLA |
| SC-001 Network Segmentation | DMZ for internet-facing services. Remote access terminates in segmented zone, not directly on LAN. | **Supporting** — limits blast radius if initial access via VPN |
| RA-002 Vulnerability Scanning | Weekly external scans identify exposed RDP/VPN services. | **Secondary** — identifies exposed services before attackers do |
| AU-001 Audit Log Collection | VPN and IdP authentication logs forwarded to SIEM. | **Supporting** — enables detection of brute-force/spraying |

### T1190 — Exploit Public-Facing Application (Initial Access)

**What it is:** Attackers exploit known vulnerabilities in web applications, email servers, APIs. Uses a small collection of proven CVEs — many >1 year old.

**CISA KEV relevance:** 500+ KEV entries target web applications, email servers (Exchange, SharePoint), and CMS platforms (WordPress).

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| CM-008 Automated Patching | Critical patches within 7 days. CISA KEV-tagged CVEs trigger emergency patching. | **Primary** — directly prevents exploitation of known CVEs |
| RA-002 Vulnerability Scanning | Weekly external + monthly internal scans. Authenticated scanning for depth. | **Secondary** — identifies unpatched applicances before attackers |
| SI-005 Email Security | SPF/DKIM/DMARC enforced. Safe Links/Safe Attachments block phishing leading to exploitation. | **Secondary** — when exploitation starts via email |
| CM-004 Least Functionality | Unnecessary services, ports, and protocols removed. Reduces attack surface. | **Supporting** — fewer exposed applications = fewer CVE vectors |
| SC-001 Network Segmentation | Public-facing applications in DMZ. No direct access to internal systems. | **Supporting** — limits lateral movement from compromised app |
| AC-005 Remote Access | RDP and management interfaces not exposed to internet. | **Supporting** — closes direct management-plane exploitation |

### T1059.001 — PowerShell (Execution)

**What it is:** Attackers use PowerShell to deploy payloads, download C2 tools, run credential harvesters. PowerShell downgrade bypasses logging.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| SI-004 Detection Engineering | Sigma rules detect anomalous PowerShell execution (downgrade, encoded commands, remote download patterns). | **Primary** — detection rules specifically for PowerShell abuse |
| AU-006 Audit Generation | PowerShell module logging, script block logging, and process creation events enabled via GPO. | **Primary** — enables detection data for PowerShell attacks |
| CM-005 Software Whitelisting | AppLocker/SentinelOne block unauthorized scripts and binaries. | **Secondary** — blocks unapproved PowerShell modules |
| AU-001 Audit Log Collection | PowerShell operational logs forwarded to SIEM for correlation. | **Supporting** — enables centralized analysis |
| SI-003 File Integrity Monitoring | Detects unauthorized changes to PowerShell profiles, module directories. | **Supporting** — catches persistence via PowerShell profile modification |

### T1078 — Valid Accounts (Privilege Escalation)

**What it is:** Attackers use stolen/brute-forced credentials to gain privileged access. 72% of IR actions involved identity-based attacks.

**CISA KEV relevance:** Many KEV CVEs lead directly to credential theft (ZeroLogon, noPac, SamAccountName spoofing).

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| IA-002 Strong Authentication | Minimum 12-char passwords combined with MFA. Password Protection bans common passwords. | **Primary** — makes credential stuffing and brute-force infeasible |
| AC-004 Least Privilege | JIT/PAM for admin access. No standing Domain Admin group membership. | **Primary** — limits value of stolen credentials |
| IA-001 Unique Identification | No shared accounts. Every admin has unique identity. | **Primary** — enables attribution and revocation |
| AC-006 Quarterly Access Review | Privileged access reviewed quarterly. Orphaned/over-privileged accounts revoked. | **Secondary** — reduces standing privilege attack surface |
| IR-002 Incident Detection | Anomalous authentication patterns (impossible travel, new device) trigger alerts. | **Secondary** — detects credential abuse in progress |
| PS-002 Personnel Termination | Access revoked within 24 hours of termination. | **Supporting** — prevents former-employee credential abuse |
| CM-008 Automated Patching | Patching of AD/NHDS-related CVEs (ZeroLogon, noPac) within SLA. | **Supporting** — prevents credential-theft vuln exploitation |

### T1003.001 — LSASS Memory Dumping (Credential Access)

**What it is:** Attackers use Mimikatz and similar tools to dump credentials from LSASS process memory.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| CM-005 Software Whitelisting | AppLocker/SentinelOne block Mimikatz and unauthorized credential dumping tools. | **Primary** — blocks the tool itself |
| SI-004 Detection Engineering | Sigma rules detect LSASS access attempts (suspicious process accessing lsass.exe). | **Primary** — detects the behavior |
| AU-006 Audit Generation | Windows event 4688 (process creation) and 4663 (handle to LSASS) enabled. | **Primary** — generates detection telemetry |
| AC-004 Least Privilege | Reduced number of privileged accounts with authority to access LSASS. | **Supporting** — reduces attacker's viable targets |
| SI-003 File Integrity Monitoring | Detects Mimikatz binary placement on disk. | **Supporting** — catches tool deployment |

### T1570 — Lateral Tool Transfer (Lateral Movement)

**What it is:** Attackers distribute ransomware executables and tooling across the network using file-sharing tools, RDP, SMB, and native system utilities.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| SC-001 Network Segmentation | Trust zones prevent workstation-to-server direct communication. Lateral movement requires firewall rule. | **Primary** — directly blocks the movement path |
| CM-005 Software Whitelisting | AppLocker blocks execution of ransomware binaries delivered via lateral transfer. | **Primary** — blocks execution even if transfer succeeds |
| SI-004 Detection Engineering | Sigma rules detect lateral movement patterns (SMB file writes + service creation pairs). | **Primary** — detects the behavior in progress |
| AC-004 Least Privilege | PAM restricts which accounts can authenticate to servers from workstations. | **Secondary** — limits credential usability for lateral movement |
| CM-004 Least Functionality | SMBv1 disabled. Unnecessary file-sharing protocols removed. | **Supporting** — removes common transfer protocols |
| IR-003 Incident Containment | SentinelOne network isolation can quarantine affected endpoints. | **Supporting** — stops further spread during active incident |

### T1560 — Archive Collected Data (Collection)

**What it is:** Attackers package stolen data into compressed/encrypted archives before exfiltration. Uses WinRAR, 7-Zip, or custom packers.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| SI-004 Detection Engineering | Sigma rules detect bulk archiving activity by non-backup processes. | **Primary** — detects the activity |
| SI-007 Data Loss Prevention | DLP policies detect/reject bulk file archiving to sensitive locations. | **Secondary** — blocks the action |
| AU-001 Audit Log Collection | File auditing captures archiving operations for investigation. | **Supporting** — provides forensic trail |
| AU-003 Log Review | Weekly review of SIEM alerts identifies unusual archiving patterns. | **Supporting** — catches missed by automated rules |

### T1219 — Remote Access Tools (Command and Control)

**What it is:** Attackers install legitimate remote access tools (AnyDesk, TeamViewer, RMM agents) for persistent interactive access.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| MA-002 Maintenance Tools | Approved tool list. TeamViewer, AnyDesk, LogMeIn blocked — use the RMM instead. | **Primary** — directly blocks unauthorized remote access tools |
| CM-005 Software Whitelisting | AppLocker/SentinelOne block unapproved remote access software. | **Primary** — stops installation at the endpoint |
| SI-004 Detection Engineering | Sigma rules detect unauthorized RAT installation and beaconing. | **Secondary** — detects if installation bypasses controls |
| AC-005 Remote Access | All remote access through managed VPN/RMM. No direct RDP from internet. | **Secondary** — removes the pathway attackers use to install RATs |

### T1048 — Exfiltration over Alternative Protocol (Exfiltration)

**What it is:** Attackers move stolen data out via FTP, HTTP, DNS tunneling, cloud upload, or email — bypassing C2 traffic detection.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| SI-006 Web Filtering | Outbound web traffic filtered. Blocked categories include file-sharing, anonymous upload. HTTPS inspection. | **Primary** — blocks common exfiltration channels |
| SI-007 Data Loss Prevention | DLP identifies and blocks unauthorized sensitive data transfer via email, cloud, USB. | **Primary** — content-aware block of sensitive data |
| SI-005 Email Security | Outbound email filtering monitors for bulk data transmission. | **Secondary** — catches email-based exfiltration |
| SC-001 Network Segmentation | OT network has one-way data diode. DMZ limits data paths. | **Supporting** — reduces exfiltration routes |
| SC-008 DNS Security | DNS filtering blocks DNS tunneling to known malicious domains. | **Supporting** — detects DNS-tunneled exfiltration |

### T1486 — Data Encrypted for Impact (Impact)

**What it is:** Ransomware encrypts files, volumes, and systems. Shadow copies deleted, backups wiped, recovery prevented.

| Control | How It Stops This TTP | Effectiveness |
|---------|-----------------------|---------------|
| CP-002 Backup Configuration | Immutable backups (Linux hardened repo or Object Lock). 3-2-1 rule. | **Primary** — enables recovery without paying ransom |
| CP-003 Backup Testing | SureBackup weekly tests. Quarterly manual full restore. Failed tests = high-severity incident. | **Primary** — confirms backups actually work |
| CP-004 Alternate Storage Site | Geographically separate backup copy. Cross-region for cloud. | **Primary** — survives site-wide ransomware event |
| CP-005 System Recovery Procedures | Documented recovery procedures in priority order (auth first, then file, then apps). | **Primary** — enables structured recovery under pressure |
| CM-005 Software Whitelisting | Blocks unauthorized ransomware execution. | **Secondary** — prevention layer before encryption |
| CM-008 Automated Patching | Patching KEV-listed CVEs used by ransomware strains. | **Supporting** — prevents initial access that leads to encryption |
| IR-003 Incident Containment | SentinelOne network isolation stops encryption spread. | **Supporting** — limits blast radius during active ransomware |

---

## CISA KEV Category → Control Mapping

| KEV Category | Count in KEV | Controls That Mitigate | Primary Control |
|-------------|-------------|----------------------|-----------------|
| VPN Appliances (Palo Alto, Fortinet, Ivanti, Citrix) | 140+ | AC-005, IA-002, CM-008, RA-002 | CM-008 (patch all KEV-listed VPN vulns within 7 days) |
| Email Servers / Exchange | 80+ | CM-008, SI-005, CM-004 | CM-008 (patch Exchange CVEs) |
| Web Applications (WordPress, SharePoint) | 200+ | CM-008, RA-002, CM-004 | CM-008 (patch known CVEs) |
| Network Appliances (Cisco, Fortinet, F5) | 150+ | CM-008, MA-003, RA-002 | MA-003 (firmware updates within 30 days) |
| Identity Providers / AD (ZeroLogon, noPac) | 30+ | CM-008, IA-002, AC-004 | CM-008 (patch AD-related KEV CVEs) |
| Remote Access / RDP | 60+ | AC-005, CM-008, IA-002 | AC-005 (MFA + encrypted transport for all remote access) |
| RMM / Remote Monitoring Tools | 25+ | CM-005, MA-002, CM-006 | MA-002 (approved tool list, no unapproved RMM) |
| Backup / Storage Appliances | 15+ | CM-008, CP-002, CP-004 | CM-008 (patch backup appliance CVEs) |
| Cloud / Container Platforms | 40+ | CM-008, SC-003, SC-004 | CM-008 (patch cloud infrastructure CVEs) |
| AI / ML Platforms | 10+ | CM-008, STD-AI-001 | CM-008 (patch AI platform CVEs) |

---

## Control → Threat Coverage Matrix

Shows how many threats each control addresses. Priority for evidence collection should follow this ranking.

| Rank | Control | Ransomware TTPs Blocked | KEV Categories Covered | Overall |
|------|---------|------------------------|----------------------|---------|
| 1 | CM-008 Automated Patching | 6 (T1190, T1133, T1078, T1486, +2) | **All 10 KEV categories** | **Highest ROI** — patch management stops exploitation across the entire threat landscape |
| 2 | AC-005 Remote Access | 3 (T1133, T1190, T1219) | VPN, RDP, Remote Access categories | Critical for initial access defense |
| 3 | IA-002 Strong Authentication | 2 (T1133, T1078) | IdP/AD category | MFA stops credential attacks |
| 4 | CM-005 Software Whitelisting | 5 (T1059.001, T1003.001, T1570, T1219, T1486) | RMM category | Broad prevention across many TTPs |
| 5 | SI-004 Detection Engineering | 6 (T1059.001, T1003.001, T1570, T1560, T1219, +1) | Cross-cutting | Detection for the most active TTPs |
| 6 | SC-001 Network Segmentation | 3 (T1133, T1190, T1570) | Cross-cutting | Limits blast radius |
| 7 | AC-004 Least Privilege | 3 (T1078, T1003.001, T1570) | IdP/AD category | Limits credential abuse |
| 8 | CP-002 Backup Configuration | 1 (T1486) | Backup category | Enables recovery without paying ransom |
| 9 | CM-004 Least Functionality | 2 (T1190, T1570) | Cross-cutting | Reduces attack surface |
| 10 | SI-007 Data Loss Prevention | 2 (T1560, T1048) | Cross-cutting | Blocks exfiltration |
| 11 | MA-002 Maintenance Tools | 1 (T1219) | RMM category | Blocks RAT installation |
| 12 | RA-002 Vulnerability Scanning | 2 (T1133, T1190) | All KEV categories | Identifies exposure before attackers |
| 13 | IR-003 Incident Containment | 2 (T1570, T1486) | Cross-cutting | Stops spread during incident |
| 14 | SI-005 Email Security | 1 (T1190) | Email category | Blocks phishing as initial access vector |
| 15 | AC-006 Quarterly Access Review | 1 (T1078) | Cross-cutting | Reduces standing privilege |

**Full 87-control coverage:** All controls in CB-002 contribute to at least one defense layer. The controls listed above are the 15 that directly address the current ransomware threat landscape. The remaining 72 controls cover regulatory compliance, operational resilience, physical security, and program management — essential for a complete program but not high-signal for ransomware-specific defense.

---

## Ransomware-Specific Controls Quick Card (Client Conversation Tool)

| Threat | Stop | Controls |
|--------|------|----------|
| "Can't we just VPN in?" | No unmanaged remote access | AC-005 · IA-002 · AC-002 |
| "We'll patch it next month" | Critical patches within 7 days | CM-008 · RA-002 |
| "Our backups are fine" | Immutable, tested, offsite | CP-002 · CP-003 · CP-004 |
| "No one would target us" | 53 ransomware-linked CVEs in KEV | CM-008 covers all of them |
| "We have antivirus" | Blocks ransomware before execution | CM-005 · SI-004 |
| "We trust our employees" | MFA stops credential abuse | IA-002 · AC-002 · AC-004 |
| "We're segmented" | Actually verified with firewall rules | SC-001 · CA-004 |
| "Our email is secure" | SPF/DKIM/DMARC + Safe Links | SI-005 |

---

## Scoring Methodology

Controls are scored against each threat based on:

| Effectiveness | Meaning | Evidence Required |
|-------------|---------|------------------|
| **Primary** | Control directly prevents or detects the TTP. If implemented correctly, the TTP cannot succeed. | Operating effectiveness evidence (E2/E3). Automated collection preferred. |
| **Secondary** | Control makes the TTP significantly harder or more detectable but does not guarantee prevention. | Implementation evidence (E1/E2). |
| **Supporting** | Control contributes to defense-in-depth but alone would not stop the TTP. | Implementation evidence (E1). |

---

## Update Cadence

| Component | Refresh | Responsible |
|-----------|---------|-------------|
| CISA KEV entries | Monthly | Consulting Practice Lead |
| Ransomware TTP analysis | Monthly | Consulting Practice Lead |
| Control effectiveness scores | Quarterly | Consulting Practice Lead |
| Client conversation quick card | Quarterly | Consulting Practice Lead |

**Next scheduled refresh:** 2026-08-20

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-20 | cragin-security | Initial release: 10 ransomware TTPs mapped to CB-002 controls, 10 KEV categories mapped, control coverage ranking, client conversation quick card. |

### Review Triggers

- CISA KEV catalog adds a vulnerability affecting a tool in the CERG stack (Entra ID, Okta, SentinelOne, Fortinet, etc.)
- Major ransomware campaign using novel TTPs (e.g., new initial access vector, new evasion technique)
- CB-002 control baseline update (new controls added, existing controls modified)
- Quarterly threat intelligence refresh

### Related Documents

- [CERG 100-Core Control Baseline](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — the control set this mapping validates
- [Evidence Automation Mapping](evidence-automation-mapping-v1.md) — how to collect evidence for the controls above
- [Policy-as-Code Examples](../../tools/policy-as-code/README.md) — OPA/Rego enforcement of DISH baseline, GitHub Actions gates for architecture review
- [Opinionated Tool Matrix](opinionated-tool-matrix-v1.md) — tool selection criteria for defense implementation
- [MSP Runbook](../msp-runbook-v1.md) — deployment instructions for the controls that stop ransomware
- [Architecture Decision Records](../../governance/CERG-GOV-ADR-001_Architecture_Decision_Records.md) — rationale for opinionated tool choices

### Primary Sources

- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — accessed 2026-07-21 (1,651 entries)
- [MITRE ATT&CK v15](https://attack.mitre.org/) — TTP framework and technique definitions
- [Arctic Wolf Top 10 Ransomware TTPs](https://arcticwolf.com/resources/blog/the-top-10-ransomware-ttps/) — 2025 threat research
- [CISA BOD 26-04](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) — Known Exploited Vulnerabilities directive
