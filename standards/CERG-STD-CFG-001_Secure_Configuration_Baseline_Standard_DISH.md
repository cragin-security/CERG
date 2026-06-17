
# SURGE: Cyber Engineering, Risk & Governance

## SECURE CONFIGURATION BASELINE STANDARD: DISH
### Defensive Infrastructure System Hardening · IT and OT Hardening Profile

---

| | |
|---|---|
| **Document ID** | CERG-STD-CFG-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-LM-001](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| **Review Cycle** | Annual / Upon CIS Benchmark version change or new platform class |
| **Frameworks** | CIS Benchmarks v8+ · CIS Controls v8 · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CM family) · [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) (OT) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) · IEC 62443-3-3 / 4-2 |
| **Regulations** | NERC-CIP v7 CIP-007/CIP-010 · [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.4.x) · SOX ITGC (Change/Operations) |
| **Environments** | Owned data center · IaaS / PaaS · SaaS (Tier 1) · OT (BES and non-BES) · Endpoint · Network · Cloud control plane · Container/K8s |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The DISH Profile](#2-the-dish-profile)
3. [Baseline Tiers and When Each Applies](#3-baseline-tiers-and-when-each-applies)
4. [Baseline Catalog](#4-baseline-catalog)
5. [IT Platform Baselines](#5-it-platform-baselines)
6. [Cloud Baselines](#6-cloud-baselines)
7. [Container and Kubernetes Baseline](#7-container-and-kubernetes-baseline)
8. [Network and Firewall Baselines](#8-network-and-firewall-baselines)
9. [SaaS Tier 1 Baselines](#9-saas-tier-1-baselines)
10. [OT Platform Baselines](#10-ot-platform-baselines)
11. [Drift Detection and Exception Handling](#11-drift-detection-and-exception-handling)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

[CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) requires approved baselines per asset class. The Operating Model names baselines, IaC, and policy-as-code as core Engineering activities. The IT, OT, and CUI standards each independently call for baselines. Until this standard, those requirements existed without a unified implementation set, which made hardening impossible to delegate or assess.

This standard establishes the **DISH** profile - **D**efensive **I**nfrastructure **S**ystem **H**ardening - applicable to every in-scope asset class, IT and OT, with a single hardening minimum, an elevated tier for High-Impact and BES systems, and explicit fallbacks where CIS does not apply. The acronym is used throughout the CERG document library to refer to the baselines, scan profiles, and drift-detection signals derived from this standard; it is defined here and in [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) §3.

> **Hardening Is Not Optional**
>
> A baseline that exists "in policy" but cannot be enumerated, scanned, or remediated is not a baseline. CERG treats hardening as a deliverable artifact (the baseline document), a scan profile (DISH), and a continuous control (drift detection). All three are required or the asset is non-compliant.

### 1.1 Scope

Applies to every in-scope asset class:

- Windows Server, Linux server, workstation/endpoint, mobile (MDM-managed)
- Network device (switch/router), firewall, load balancer
- Cloud landing zone and control plane (AWS, Azure, GCP)
- Container and Kubernetes (cluster + workload)
- Tier 1 SaaS (M365, Salesforce, ServiceNow, etc.)
- SCADA server, HMI, historian, RTU, relay, engineering workstation, OT jump server
- Identity systems (IdP, IGA, PAM), see also [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md)

---

## 2. The DISH Profile

DISH is the CERG-native, IT-and-OT-spanning hardening scan profile. It is implemented in the vulnerability scanning platform as a custom scan template that aggregates the requirements below.

### 2.1 Composition

| **Source** | **Role in DISH** |
|---|---|
| **CIS Benchmark Level 1** | Inescapable floor for every in-scope asset where a CIS Benchmark exists. |
| **CIS Benchmark Level 2** | Required for High-Impact systems, BES Cyber Systems, CUI components. |
| **[NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)** | Authoritative for ICS/OT where CIS does not apply or contradicts safe OT operation. |
| **IEC 62443-3-3 (SR) and 62443-4-2 (CR)** | Authoritative for OT component-level requirements, including vendor-supplied systems. |
| **[NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final)** | Authoritative for CUI-component-specific parameters. |
| **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM family parameters** | Authoritative for any control where [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) names a parameter (timeouts, lockouts, retention). |
| **CERG-specific overrides** | Documented in this standard. Overrides are an exception to CIS, not a relaxation - they are tighter than CIS, never looser. |

> **Why a Named Profile**
>
> DISH gives Engineering, Risk, and the Audit team a single label they all mean the same thing by. "Did this asset pass DISH?" is a yes/no auditable question. "Is this asset hardened?" is not.

### 2.2 DISH Scan Output

The DISH scan produces, per asset:

1. Pass/fail per check, with CIS/NIST/IEC citation.
2. CERG-X-03 compliance status (`Implemented` / `Partially Implemented`).
3. Severity-weighted score for trending (used by [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) CM-001).
4. Exception annotation for any check covered by an approved exception in the Exception Register.

---

## 3. Baseline Tiers and When Each Applies

| **Tier** | **DISH Profile** | **Applies To** |
|---|---|---|
| **Tier 0 - Standard** | CIS L1 (or [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) / IEC 62443 fallback) | Every in-scope asset with no overlay. |
| **Tier 1 - High-Impact** | CIS L2 (or [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) / IEC 62443 strict) | Systems whose loss would materially impact operations or safety. |
| **Tier 2 - BES** | CIS L2 (or [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) / IEC 62443 strict) + CIP-007 R1–R5 + CIP-010 R1 parameters | Medium/High Impact BES Cyber Systems and their EACMS, PACS, and PCAs. |
| **Tier 3 - CUI** | CIS L2 + 800-171r3 parameters + FIPS crypto profile (via [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)) | CUI in-scope assets. |
| **Tier 4 - OT Safety** | [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) / IEC 62443 strict + change-management lockdown | OT systems whose disruption can cause safety impact. |

Multiple tiers may apply (a BES Cyber System that processes CUI is Tier 2 + Tier 3); the tighter parameter wins per control.

---

## 4. Baseline Catalog

The catalog below names each baseline, points at the authoritative source, and identifies CERG overrides where they exist. Each row corresponds to one DISH scan policy in the VM tool.

| **Baseline** | **Authoritative Source** | **DISH Tier(s)** | **CERG Overrides?** |
|---|---|---|---|
| Windows Server 2019/2022 | CIS Microsoft Windows Server Benchmark | T0 / T1 / T3 | Yes - Section 5.1 |
| Linux Server (Ubuntu LTS, RHEL 8/9) | CIS Distribution Benchmarks | T0 / T1 / T3 | Yes - Section 5.2 |
| Windows 10/11 Workstation | CIS Windows 10/11 Benchmark | T0 | Yes - Section 5.3 |
| macOS Endpoint | CIS macOS Benchmark | T0 | Limited - Section 5.3 |
| Network Device - Switch/Router (Cisco IOS/NX-OS) | CIS Cisco Benchmark | T0 / T1 | Yes - Section 8.1 |
| Firewall (Palo Alto, Fortinet, Cisco FTD) | CIS Vendor Benchmarks | T0 / T1 | Yes - Section 8.2 |
| AWS Account / Landing Zone | CIS AWS Foundations Benchmark | T0 / T1 / T3 | Yes - Section 6.1 |
| AWS Control Plane | CIS AWS Foundations + CERG | T0 / T1 / T3 | Yes - Section 6.1 |
| Azure Subscription / Landing Zone | CIS Microsoft Azure Foundations Benchmark | T0 / T1 / T3 | Yes - Section 6.2 |
| GCP Project / Landing Zone | CIS GCP Foundations Benchmark | T0 / T1 / T3 | Yes - Section 6.3 |
| Kubernetes Cluster (CNCF) | CIS Kubernetes Benchmark | T0 / T1 / T3 | Yes - Section 7 |
| Container Image | CIS Docker Benchmark + CERG | T0 / T1 / T3 | Yes - Section 7 |
| M365 Tenant | CIS M365 Foundations Benchmark | T0 / T1 / T3 | Yes - Section 9.1 |
| Salesforce Org | CIS or CERG-equivalent baseline | T0 / T1 | Yes - Section 9.2 |
| ServiceNow Instance | CERG baseline (no CIS) | T0 / T1 | - Section 9.3 |
| Other Tier 1 SaaS | CERG SaaS Baseline Pattern | T0 / T1 | Section 9 pattern |
| SCADA Server | [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) + IEC 62443-3-3 | T2 / T4 | Yes - Section 10.1 |
| HMI | [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) + IEC 62443-4-2 | T2 / T4 | Yes - Section 10.2 |
| Historian | [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) + CIS (where Win/Linux) | T2 / T4 | Yes - Section 10.3 |
| RTU / Relay | [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) + IEC 62443-4-2 + vendor hardening | T2 / T4 | Yes - Section 10.4 |
| Engineering Workstation | CIS Windows + 800-82r3 add-ons | T2 / T4 | Yes - Section 10.5 |
| OT Jump Server | CIS Windows L2 + CERG | T2 / T4 | Yes - Section 10.6 |

---

## 5. IT Platform Baselines

### 5.1 Windows Server

The Windows Server baseline is CIS L1 (Tier 0) or L2 (Tier 1 / 3) with the following CERG overrides:

- **Local administrator** disabled; named administrative accounts only, via PAM JIT per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md).
- **SMBv1 disabled** without exception (override is a hard fail; exceptions must be reviewed annually).
- **LM/NTLMv1 disabled**; NTLMv2 only as transitional with documented sunset.
- **Audit policy** matches the mandatory log source list in [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), specifically Process Creation, Logon, Object Access (privileged file shares), and PowerShell ScriptBlock logging enabled and forwarded to SIEM.
- **PowerShell** Constrained Language Mode for non-admin sessions; signed script enforcement for admin sessions.
- **Time** synchronized to authoritative time source; drift > 5 minutes is a finding.
- **CMK / disk encryption** per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) for any system holding Restricted or CUI.

### 5.2 Linux Server

CIS L1 / L2 with CERG overrides:

- **Root SSH** prohibited; key-based authentication; password authentication disabled.
- **sudoers** scoped via named groups; no NOPASSWD escalations outside of break-glass accounts.
- **`auditd`** enabled with rules covering identity events, sudo, privileged file access, and process execution; forwarded to SIEM.
- **Time, hostname, syslog destination, package repository allowlist** managed by configuration management.
- **Kernel module load** restricted via signed-module enforcement where supported.
- **Disk encryption** for any system holding Restricted or CUI.

### 5.3 Workstation / Endpoint

CIS L1 with the additional CERG requirements:

- **EDR agent installed, healthy, and tamper-protected.**
- **Full-disk encryption** with key escrow.
- **Local admin** removed for standard users; administrative tasks via just-in-time elevation.
- **Conditional access** binds device posture to access.
- **USB mass storage controlled** (allowlist / read-only / blocked per data classification).

---

## 6. Cloud Baselines

CERG hardens both **landing zone** (account / subscription / project provisioning) and **control plane** (IAM, logging, networking, key management).

### 6.1 AWS

CIS AWS Foundations Benchmark L1 (Tier 0) / L2 (Tier 1+) with CERG overrides:

- **Org-level Service Control Policies (SCPs)** enforce: deny root access keys; deny region pinning except approved regions; deny disabling of CloudTrail / GuardDuty / Config / Security Hub; deny public S3 by default.
- **CloudTrail** multi-region, organization trail, log-file integrity validation enabled, KMS-encrypted, immutable storage.
- **GuardDuty / Security Hub / Config / Inspector** enabled in every account.
- **IAM**: no root usage; IAM Identity Center as the only human-access path; permissions boundaries on workload roles; access keys disabled for human users.
- **Networking**: no default VPC use in production; egress allowlist; VPC flow logs enabled and routed to SIEM.
- **KMS**: CMK for any data classified Restricted or CUI; rotation per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md).

### 6.2 Azure

CIS Azure Foundations Benchmark L1 / L2 with CERG overrides:

- **Management group hierarchy** enforces policy inheritance; Azure Policy initiatives are mandatory.
- **Microsoft Defender for Cloud** enabled at Standard tier for in-scope subscriptions.
- **Activity Logs / Diagnostic Settings** routed to immutable Log Analytics workspace and SIEM.
- **Entra ID**: privileged access via PIM only; Conditional Access for all administrative roles; phishing-resistant MFA for all admins; legacy authentication blocked.
- **Storage Accounts**: public access disabled by default; CMK for Restricted/CUI workloads.

### 6.3 GCP

CIS GCP Foundations Benchmark L1 / L2 with CERG overrides:

- **Organization Policies** enforce: domain-restricted sharing; uniform bucket-level access; require OS Login; disable service-account key creation by default.
- **Security Command Center** Premium tier in-scope.
- **Cloud Audit Logs**: admin activity + data access enabled and exported to immutable destination + SIEM.
- **CMEK** for Restricted/CUI workloads.

---

## 7. Container and Kubernetes Baseline

CIS Kubernetes Benchmark for control plane and worker node, plus CERG application-layer requirements:

- **Pod Security Standards**: `restricted` for production namespaces.
- **Network Policies**: default-deny ingress and egress; explicit allowlists per service.
- **Admission controllers** enforce signed images (cosign / sigstore), no privileged pods, no host network/PID, no `:latest` tags.
- **Image provenance**: images built only from approved base images; SBOM produced at build; scan results gate promotion.
- **Secrets**: Kubernetes secrets disabled or encrypted via external secrets manager per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md).
- **Cluster audit log** routed to SIEM.

---

## 8. Network and Firewall Baselines

### 8.1 Switches / Routers

CIS Cisco IOS/NX-OS L1 / L2 with CERG overrides:

- **Management plane**: out-of-band management network; SSH only; TACACS+/RADIUS via central IdP; local accounts only as break-glass per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md).
- **Control plane policing** enabled with documented thresholds.
- **Logging** to syslog and SIEM; NTP authenticated.
- **Unused services** disabled (CDP/LLDP scoped, HTTP server off, etc.).
- **Configuration management** under version control; out-of-band changes detected and alerted.

### 8.2 Firewalls

CIS vendor benchmark plus CERG overrides:

- **Default deny** ingress and egress; explicit allowlists.
- **Rule lifecycle**: every rule has owner, business justification, and review date; review cadence ≤ 12 months.
- **TLS inspection** policy aligned with [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) and data classification.
- **Log forwarding** to SIEM with session-level and threat-event-level detail.

---

## 9. SaaS Tier 1 Baselines

### 9.1 M365 Tenant

CIS M365 Foundations Benchmark L1 / L2 with CERG overrides:

- **Phishing-resistant MFA** for all admin roles, enforced by Conditional Access.
- **External sharing**: domain allowlist or full lockdown by default; SharePoint anonymous links disabled.
- **Defender for Office 365** Plan 2 features enabled (Safe Links, Safe Attachments, anti-phish).
- **Audit log retention** ≥ 1 year (advanced audit license); routed to SIEM.
- **CUI Enclave (if applicable)** uses GCC High or FedRAMP-equivalent tenant per [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md).

### 9.2 Salesforce

CIS or vendor baseline plus CERG overrides:

- **SSO mandatory** for human users; legacy username/password disabled except as documented break-glass.
- **MFA** phishing-resistant where supported.
- **Field-level / record-level access** restricted to least privilege; permission set assignments reviewed quarterly.
- **Event Monitoring** enabled with logs forwarded to SIEM.

### 9.3 ServiceNow

CERG baseline (no CIS):

- **SSO** mandatory; admin role assignments reviewed quarterly.
- **Inbound integrations** scoped via OAuth with rotated client secrets per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md).
- **Audit & system logs** forwarded to SIEM.
- **Domain separation** documented when shared with vendors or sub-orgs.

### 9.4 Pattern for Other Tier 1 SaaS

Where no published baseline exists, the CERG SaaS Baseline Pattern (Section 9 generic) requires: SSO + MFA + admin role review + audit log export + tenancy isolation + CMK or BYOK for Restricted/CUI + documented shared responsibility matrix.

---

## 10. OT Platform Baselines

OT baselines lead with [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and IEC 62443; CIS is used where the underlying OS supports it (typically engineering workstations and historian servers).

> **Active Scanning is Forbidden in OT Without Engineering Approval**
>
> DISH for OT is delivered via passive monitoring, configuration capture, vendor management interfaces, and engineering-supervised authenticated checks. Active vulnerability scanning of a live SCADA or RTU surface is not permitted under this standard except under an approved scope and time window per [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md).

### 10.1 SCADA Server

- Underlying OS hardened to CIS L2 with vendor compatibility exceptions documented and risk-accepted per [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).
- Application allowlisting enforced; only vendor-approved SCADA application binaries permitted.
- Local accounts via PAM; vendor accounts gated by approved workflow per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md).
- Anti-malware where vendor-supported; otherwise compensating controls per IEC 62443-3-3 SR 3.2.
- Logging to one-way SIEM transfer per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).
- Patch posture per OT VM procedure in [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md).

### 10.2 HMI

- Locked-down kiosk-style desktop; standard Windows hardening minus features that interfere with operator workflow (documented).
- USB and removable media controlled, read-only or disabled outside maintenance windows.
- Screen-lock parameters appropriate to operator console operating context (per safety analysis).

### 10.3 Historian

- Hardened to CIS L2 for Windows/Linux base.
- Database engine hardening (SQL Server / time-series engine) per vendor + CERG.
- Backups per [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md), including historian data sets.

### 10.4 RTU / Relay

- Vendor hardening guidance applied as a minimum; CERG overrides only where they tighten.
- Disable unused protocols; restrict management interfaces; rotate default credentials.
- Firmware version pinned; updates per [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) CIP-010 procedure.
- Configuration captured to backup per [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) (configurations, firmware, logic files).

### 10.5 Engineering Workstation

- CIS Windows L2 baseline.
- Dedicated to OT use only; no general business workload.
- USB / removable media policy stricter than enterprise default; tool-import policy documented.
- Application allowlist of engineering tools and supporting libraries.

### 10.6 OT Jump Server

- CIS Windows L2 baseline + CERG hardening above general workstation.
- Brokered session recording for all sessions to OT.
- MFA on entry; no clipboard / file transfer beyond named workflow.

---
## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Section(s)** | **Where in This Standard** |
|---|---|---|
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM family | CM-2, CM-6, CM-7 | Sections 2 – 11 |
| [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) | 3.4.x | Tier 3 in Section 3, parameters in Sections 5, 6, 9 |
| [NIST 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | All | Tier 4 in Section 3; Section 10 |
| IEC 62443-3-3 / 4-2 | SR / CR families | Section 10 |
| CIS Controls v8 | Controls 4, 12 | Sections 5–9 |
| NERC-CIP CIP-007 R1, R2, R5 | Ports, patching, accounts | Section 10 + `CERG-PLN-CIP-001` |
| NERC-CIP CIP-010 R1 | Baseline configuration | All sections, especially Section 11 |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.4.x) | Configuration management | Tier 3 in Section 3; Section 5–9 |
| SOX ITGC | Change / Operations | Section 11 |

---

## 12. Document Control

| | |
|---|---|
| **Document ID** | CERG-STD-CFG-001 |
| **Version** | 1.21 |
| **Approved By** | CISO |
| **Next Review** | Annual / CIS Benchmark or [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) revision |
| **Change Log** | 1.0 - Initial publication. Establishes DISH profile, baseline catalog, and platform-specific baselines for IT, cloud, container, SaaS, and OT. |

