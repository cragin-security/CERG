# CB-001 Control to Detection Rule Mapping
| | |
|---|---|
| **Document ID** | CERG-PA-DET-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CERG Practice Lead |

**Purpose:** Maps existing detection rules from `practice-assets/detection/detection-engineering-framework-v1.md` to CB-001 controls. Every control that can be tested with a detection rule gets one. Output drives SIEM correlation rules and tabletop scenarios.

**Format:** CB-001 Control → MITRE ATT&CK Technique → Detection Rule → Testing Procedure

---

## Legend

- **KQL** = Microsoft Sentinel / Azure Data Explorer query
- **Sigma** = Platform-agnostic Sigma rule format
- **Test** = Atomic Red Team or manual test procedure

---

## Access Control (AC)

### AC-2 Account Lifecycle — Orphan and Stale Accounts

| Attribute | Value |
|-----------|-------|
| **MITRE** | T1078.004 (Valid Accounts: Cloud Accounts) |
| **Why** | Orphan accounts are valid accounts without an owner. Attackers find and use them. |
| **Detection** | [KQL] Active accounts without recent sign-in or without manager attribute |
| **Rule** | `SigninLogs | summarize LastLogin = max(TimeGenerated) by UserPrincipalName | where LastLogin < ago(90d)` |
| **Sigma** | [Sigma rules/windows/builtin/security/win_account_discovery.yml](https://github.com/SigmaHQ/sigma) |
| **Test** | Create a test user, set `Manager` to null, verify alert fires within 24h |
| **Control** | AC-2 — When an orphan account is detected, investigate and disable |

### AC-3 Access Enforcement — Legacy Authentication Bypass

| MITRE | T1078.003 (Valid Accounts: Local Accounts) |
|-------|---------|
| **Detection** | [KQL] Sign-in events using legacy protocols (POP3, IMAP4, SMTP AUTH) |
| **Rule** | `SigninLogs | where ClientAppUsed in~ ("POP3", "IMAP4", "Exchange ActiveSync", "Other")` |
| **Test** | Attempt to connect to Exchange via POP3 with valid credentials |
| **Control** | AC-3 — Legacy authentication should be blocked; log any legacy sign-in |

### AC-4 Least Privilege — Privilege Escalation

| MITRE | T1078 (Valid Accounts) + T1098 (Account Manipulation) |
|-------|---------|
| **Detection** | [KQL] User added to privileged directory role or group |
| **Rule** | `AuditLogs | where OperationName == "Add member to role" and TargetResources contains "Admin"` |
| **Test** | Add a user to Domain Admins — verify alert fires within 15min |
| **Control** | AC-4 — Privileged role changes require approval; alert on unapproved changes |

### AC-5 Failed Auth — Brute Force / Password Spray

| MITRE | T1110.003 (Brute Force: Password Spraying) |
|-------|---------|
| **Detection** | [KQL] Multiple failed logins from same IP across different accounts |
| **Rule** | `SigninLogs | where ResultType != "0" | summarize FailedCount = count() by IPAddress, UserPrincipalName | where FailedCount > 5` |
| **Test** | Use a password spraying tool against a test account (authorised) |
| **Control** | AC-5 — Lockout after 10 attempts; alert on 5+ from same IP |

### AC-6 Remote Access — Anomalous Remote Connection

| MITRE | T1133 (External Remote Services) |
|-------|---------|
| **Detection** | [KQL] VPN or remote access from unexpected geographic location |
| **Rule** | `SigninLogs | where LocationDetails.countryOrRegion !in~ ("US", "GB", "CA") \| summarize by UserPrincipalName, IPAddress` |
| **Test** | Connect via VPN from a simulated foreign IP |
| **Control** | AC-6 — Remote access requires MFA; alert on anomalous geolocation |

### AC-9 Session Termination — Compromised Session

| MITRE | T1525 (Steal Web Session Cookie) |
|-------|---------|
| **Detection** | [KQL] Impossible travel: same user authenticates from 2+ far locations in <1 hour |
| **Rule** | `SigninLogs | summarize Locations = make_set(LocationDetails) by UserPrincipalName, bin(TimeGenerated, 1h) | where array_length(Locations) > 1` |
| **Test** | Export a session token and use it from a different IP |
| **Control** | AC-9 — Short token lifetimes limit session theft damage |

---

## Audit & Accountability (AU)

### AU-2 Log Review — Coverage Gap Detection

| MITRE | T1562.001 (Impair Defenses: Disable or Modify Tools) |
|-------|---------|
| **Detection** | [KQL] Log sources that stopped sending events |
| **Rule** | `Heartbeat | summarize LastReport = max(TimeGenerated) by Computer | where LastReport < ago(4h)` |
| **Test** | Stop the Azure Monitor Agent on a test VM |
| **Control** | AU-2 — Alert on log source silence >4 hours |

### AU-3 Log Protection — Log Tampering

| MITRE | T1070.001 (Indicator Removal: Clear Windows Event Logs) |
|-------|---------|
| **Detection** | [KQL] Event log cleared on a system |
| **Rule** | `SecurityEvent | where EventID == 1102 (Security log cleared)` |
| **Test** | `wevtutil cl Security` on a test system |
| **Control** | AU-3 — Log immutability prevents tampering; alert on log clear events |

---

## Configuration Management (CM)

### CM-3 Drift Detection — Configuration Change

| MITRE | T1574 (Hijack Execution Flow) |
|-------|---------|
| **Detection** | [KQL] File integrity change on a watched system path |
| **Sigma** | `linux/file_integrity.yml` or `windows/file_change.yml` |
| **Test** | Modify `/etc/passwd` or `C:\Windows\System32\drivers\etc\hosts` |
| **Control** | CM-3 — File integrity monitoring alerts on unauthorised changes |

---

## Identification & Authentication (IA)

### IA-1 MFA — MFA Bypass Detection

| MITRE | T1556 (Modify Authentication Process) |
|-------|---------|
| **Detection** | [KQL] Sign-in without MFA challenge for a user who has MFA enabled |
| **Rule** | `SigninLogs | where AuthenticationRequirement != "multiFactorAuthentication" and UserPrincipalName in (mfa_enabled_users)` |
| **Test** | Sign in with a valid password from a trusted IP (bypassing MFA challenge) |
| **Control** | IA-1 — Require MFA for all interactive sign-ins; alert on MFA-skipped logins |

---

## Risk Assessment (RA)

### RA-3 Vulnerability Remediation — Overdue Patches

| MITRE | T1190 (Exploit Public-Facing Application) |
|-------|---------|
| **Detection** | [KQL] CRITICAL vulnerability older than 7 days on an internet-facing system |
| **Rule** | `QualysVulnerability_CL | where severity_s == "CRITICAL" and age_days_d > 7 and asset_public_facing_b == true` |
| **Test** | Leave a test system unpatched past SLA; verify it appears in the overdue report |
| **Control** | RA-3 — Patch critical vulns within 7 days; alert on overdue |

---

## System & Information Integrity (SI)

### SI-1 Malware Protection — EDR Agent Gap

| MITRE | T1562.001 (Impair Defenses: Disable or Modify Tools) |
|-------|---------|
| **Detection** | [KQL] Endpoint without active EDR agent or agent with stale heartbeat |
| **Rule** | `Heartbeat | where Category == "Endpoint Protection" and TimeGenerated < ago(4h)` |
| **Test** | Uninstall the EDR agent from a test workstation |
| **Control** | SI-1 — EDR agent on >98% of endpoints; alert on agent removal |

### SI-3 Anti-Phishing — Phishing Campaign Detection

| MITRE | T1566.001 (Phishing: Spearphishing Attachment) |
|-------|---------|
| **Detection** | [Sigma] Email with suspicious attachment delivered to multiple users |
| **Sigma** | `email/phish_suspicious_attachment.yml` |
| **Test** | Send a simulated phishing email with EICAR test file attachment |
| **Control** | SI-3 — Anti-phishing tool detects and blocks; alert on delivery to >3 users |

### SI-6 Software Integrity — Unsigned Binary Execution

| MITRE | T1204.002 (User Execution: Malicious File) |
|-------|---------|
| **Detection** | [Sigma] Unsigned binary executed from user-writable path |
| **Sigma** | `windows/process_creation/unsigned_binary_in_appdata.yml` |
| **Test** | Download and run an unsigned executable from `%TEMP%` |
| **Control** | SI-6 — WDAC/AppLocker blocks unsigned binaries; alert on block events |

---

## Supply Chain Risk (SR)

### SR-2 Software Supply Chain — Dependency Vulnerability

| MITRE | T1195.001 (Supply Chain Compromise: Compromise Software Dependencies) |
|-------|---------|
| **Detection** | [KQL] New CRITICAL CVE in a in-use software dependency |
| **Rule** | `DependencyTrack_CL | where severity_s == "CRITICAL" and component_in_use_b == true` |
| **Test** | Import a known-vulnerable SBOM into Dependency-Track; verify alert |
| **Control** | SR-2 — Scan dependencies; alert on new critical CVEs |

---

## Incident Response (IR)

### IR-2 Incident Detection — Phishing to Initial Access

| MITRE | T1566.001 → T1204.002 (Phishing → User Execution) |
|-------|---------|
| **Detection** | [KQL] User clicked phishing link AND executed a file within 10 minutes |
| **Rule** | Joins EmailEvents ↗ DeviceProcessEvents on user and time window |
| **Test** | Click a simulated phishing link and run a test payload |
| **Control** | IR-2 — Alert on phish-click-to-payload chain within 10 minutes |

---

## Detection Coverage Summary

| SIEM Type | Rules Provided | Covers Controls |
|-----------|---------------|-----------------|
| Microsoft Sentinel (KQL) | 12 queries | AC-2, AC-3, AC-4, AC-5, AC-6, AC-9, AU-2, AU-3, IA-1, RA-3, SI-1, IR-2 |
| Sigma (any SIEM) | 3 rules | CM-3, SI-3, SI-6 |
| Test procedures | 12 tests | One per detection rule |

---

## How to Use This With CB-001

1. **For each control**, if it has a detection rule above, configure that rule in the client's SIEM.
2. **Run the test procedure** to confirm the rule fires correctly.
3. **The SIEM alert** becomes the VERIFICATION step for the control.
4. **Evidence**: Save the detection rule output as evidence for the GRC tool.

---

## Document Control

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07 | Initial CB-001 to detection rule mapping (15 controls, 12 KQL, 3 Sigma, 12 tests) |
