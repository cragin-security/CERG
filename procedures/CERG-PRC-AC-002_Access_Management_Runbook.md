# SURGE: Cyber Engineering, Risk & Governance

## ACCESS MANAGEMENT RUNBOOK
### JML · Access Requests · Recertification · PAM · Break-Glass · Service Accounts · Secrets · Vendor Access · MFA

---

| | |
|---|---|
| **Document ID** | CERG-PRC-AC-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Identity Engineer |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) - Access Management Standard |
| **Supporting Documents** | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Review Cycle** | Annual / On IAM tooling change |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (AC, IA, AU) · [NIST 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (PROTECT) |
| **Regulations** | NERC-CIP CIP-004 / CIP-005 · [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.1, 3.5) · SOX ITGC (Access) |
| **Environments** | All in-scope identities - human, machine, service, vendor |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The Two Operating Models, CERG-Owned vs. Cyber-Contributing](#2-the-two-operating-models--cerg-owned-vs-cyber-contributing)
3. [Joiner / Mover / Leaver](#3-joiner--mover--leaver)
4. [Access Request and Approval](#4-access-request-and-approval)
5. [Access Review and Recertification](#5-access-review-and-recertification)
6. [Privileged Access Management (PAM)](#6-privileged-access-management-pam)
7. [Break-Glass Access](#7-break-glass-access)
8. [Service Accounts and Machine Identities](#8-service-accounts-and-machine-identities)
9. [Secrets, API Keys, and Tokens](#9-secrets-api-keys-and-tokens)
10. [Vendor Access](#10-vendor-access)
11. [MFA Enrollment and Exception](#11-mfa-enrollment-and-exception)
12. [Roles and Responsibilities](#12-roles-and-responsibilities)
13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Scope

The Access Management Standard explicitly says implementation details, IdP baselines, MFA enrollment, PAM workflows, recertification runbooks, are maintained separately. This runbook is that "separately." It defines the executable workflows behind every identity decision [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) requires.

The runbook covers every identity in the environment: human (employee, contractor), machine (system, service, agent), and vendor / third-party.

> **One Runbook, Two Owners**
>
> Many organizations run IAM under IT (not Cyber). The runbook is written so it is complete under either operating model: where IAM reports into CERG, this is the operational manual; where IAM reports outside CERG, this is the cyber-required content the IAM team must implement or formally diverge from with documented compensating controls.

---

## 2. The Two Operating Models: CERG-Owned vs. Cyber-Contributing

| **Aspect** | **CERG-Owned IAM** | **CERG-Contributing IAM** |
|---|---|---|
| Procedural authority | CERG owns this runbook and the IAM operations team. | IAM team owns operations; CERG provides cyber requirements via this runbook. |
| Tooling decisions | CERG-driven. | IAM-driven with CERG sign-off where security-material. |
| Day-to-day operations | CERG. | IAM. |
| Recertification execution | CERG runs. | IAM runs; CERG audits. |
| Detection / monitoring | CERG (always). | CERG (always). |
| Audit interface | CERG. | Shared. |

Where IAM is outside CERG, every requirement below is either implemented by the IAM team, or a formal documented divergence is recorded in the risk register per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

---

## 3. Joiner / Mover / Leaver

### 3.1 Joiner

| **Step** | **Trigger / Owner / SLA** |
|---|---|
| HR record created in HRIS | HR - at offer signed |
| Account provisioned by IGA from HRIS | IGA system - within 1 business day of start date |
| Baseline entitlements assigned by role | IGA via role / SoD model |
| MFA enrollment notification | IdP - at first sign-in |
| Required training assignment | Awareness function |
| Phishing-resistant MFA enrolled before privileged use | User + Identity Engineer |
| Hardware token issued (where required by role) | Identity Engineer |
| Privileged role(s) requested separately | Manager + named approver per role |

### 3.2 Mover

| **Step** | **Trigger / Owner / SLA** |
|---|---|
| Role / department change in HRIS | HR |
| IGA recalculates entitlements; out-of-role accesses flagged | IGA - within 1 business day |
| Out-of-role accesses removed by default; retained only by exception with new manager approval | Manager - within 5 business days |
| Privileged roles re-justified | Manager + role owner - within 5 business days |
| Recertification triggered for new role | IGA - within 30 days of move |

### 3.3 Leaver

| **Step** | **Trigger / Owner / SLA** |
|---|---|
| HR termination event in HRIS | HR - same day |
| Active sessions terminated | IdP - within 1 hour |
| Account disabled | IGA - within 1 business day (within 1 hour for involuntary) |
| Privileged credentials and secrets attributed to user rotated | PAM + Engineering - within 1 business day |
| MFA tokens / hardware deauthorized | Identity Engineer - within 1 business day |
| Mailbox and data retention applied per Legal | Engineering - IT |
| Account permanently deleted | IGA - after retention period |

### 3.4 Involuntary or High-Sensitivity Leavers

Same as 3.3 with all SLAs collapsed to "immediately" and the SOC alerted to monitor for credential reuse and data exfiltration.

---

## 4. Access Request and Approval

### 4.1 Request Patterns

| **Pattern** | **Use** |
|---|---|
| Role / role-bundle request | Standard entitlements bundled into roles aligned to job function. |
| Birthright role | Auto-assigned based on HRIS attributes. |
| Project / time-bound role | Access for a defined project, with expiration. |
| Privileged role | Always separately requested; PAM-mediated. |
| Sensitive system role | System owner approval required. |
| Vendor / external | See Section 10. |

### 4.2 Approval Chain

| **Access Class** | **Approvers** |
|---|---|
| Standard role | Direct manager |
| Sensitive role | Direct manager + system owner |
| Privileged role | Direct manager + role owner + Identity Engineer |
| Vendor / external | Sponsor + Identity Engineer + TPRM record |
| Break-glass | Per Section 7 |

### 4.3 Approval Discipline

- Approvers are accountable parties; rubber-stamping is detected via approval-velocity metrics.
- Requests that violate SoD rules are blocked at submission; override requires named additional approver.
- Time-bound roles auto-expire; no implicit renewal.

---

## 5. Access Review and Recertification

### 5.1 Cadence

| **Scope** | **Cadence** |
|---|---|
| All standard accounts | Annual (full base) |
| SOX-relevant access | Quarterly |
| CUI scope access | Quarterly |
| BES Cyber System access | Quarterly (CIP-004 alignment, 15-month cap) |
| Privileged access (any) | Quarterly |
| High-blast-radius admin roles | Monthly attestation |
| Service accounts / non-human | Semi-annual |
| Vendor / external | Quarterly + per project closeout |

### 5.2 Recertification Workflow

1. **Campaign launched** via IGA with named reviewers.
2. **Reviewers presented with**: identity, current entitlements, last-used dates, role rationale.
3. **Decision** per entitlement: Certify · Modify · Remove. "Bulk Certify" is permitted only where reviewer has reviewed actual access patterns.
4. **Auto-removal** of Removed entitlements within 5 business days.
5. **Audit log** captured per IGA for the cycle.
6. **Exceptions** flagged to Engineering, Identity for follow-up.

### 5.3 Anti-Rubber-Stamp Controls

- Reviewers who certify > X% of items in < Y minutes are flagged for sampling-audit.
- Certifications of dormant accounts (> 60 days unused) require explicit justification.
- Reviewers who never modify or remove are sampled.

---

## 6. Privileged Access Management (PAM)

### 6.1 Coverage

Every privileged action across the in-scope estate is mediated by PAM. Specifically:

- Domain admin / cloud root / SaaS tenant admin.
- Network device, firewall, hypervisor, storage admin.
- Database privileged accounts.
- OT engineering interfaces and jump-server access.
- CUI workspace admin.

### 6.2 PAM Workflow

| **Step** | **Detail** |
|---|---|
| Onboard the privileged credential into PAM | Credential never returned to a human; PAM brokers the session. |
| Just-in-time (JIT) elevation | User requests; approval where required; time-bound. |
| Session brokered | RDP / SSH / web session through PAM; session recorded; commands logged. |
| Session ended | Credentials rotated if vaulted-and-checked-out pattern. |
| Logs and recordings retained per [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

### 6.3 PAM Operating Disciplines

- No direct admin password use; PAM-only.
- Standing privileged access avoided where JIT is supported.
- Quarterly audit of dormant privileged accounts.
- Session recordings sampled by Risk on a quarterly cadence; high-risk roles sampled monthly.

---

## 7. Break-Glass Access

### 7.1 Definition

Break-glass accounts are the credentials of last resort, used only when normal identity systems are unavailable or compromised. Misuse is a P1 detection per [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) Section 11.

### 7.2 Operating Rules

| **Rule** | **Detail** |
|---|---|
| Existence | Documented break-glass per system / domain / cloud root. |
| Storage | Vaulted in PAM or sealed envelope in physical safe; access logged. |
| Two-person retrieval | Two named operators required to retrieve credential. |
| Rotation | After every use; rotation completed within 24 hours of use. |
| Monitoring | Any successful authentication generates a P1 alert. |
| Quarterly hygiene check | Verify credential current, rotation works, retrieval procedure rehearsed. |
| Annual exercise | Tabletop or real exercise of break-glass retrieval and use. |

---

## 8. Service Accounts and Machine Identities

### 8.1 Preference Order

1. **Workload identity** (cloud-native): managed identities, IRSA, workload identity federation. Preferred.
2. **Short-lived issued credentials** via STS / IdP-integrated token service.
3. **Long-lived static credentials in secrets manager**, only when 1–2 are infeasible.

### 8.2 Lifecycle

| **Step** | **Owner** |
|---|---|
| Request via service-account intake | Owner team + Identity Engineer |
| Named human owner required | Owner team |
| Scope and entitlements minimized | Identity Engineer |
| Stored in PAM / secrets manager per [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Identity Engineer |
| Detection on anomalous use | Detection Engineer |
| Recertification semi-annual | Identity Engineer |
| Rotation per [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) Section 8 | Identity Engineer / Workload owner |
| Decommission on system retirement | Identity Engineer |

### 8.3 Service Account Disciplines

- No human use of service accounts.
- No interactive logon for service accounts; flagged and alerted if observed.
- No service accounts in default admin groups (Domain Admins, etc.).
- Service accounts in OT scope follow tighter restrictions and engineering review.

---

## 9. Secrets, API Keys, and Tokens

This section operationalizes [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) Section 7. See that standard for storage and rotation requirements.

| **Action** | **Path** |
|---|---|
| Request a new secret | Through secrets manager / IdP token service - never via ticket. |
| Retrieve at runtime | Workload pulls; never stored in repo or container image. |
| Rotate | Schedule + event triggers (compromise indicator, vendor incident, workforce change). |
| Revoke | On detection of compromise, on user departure, on service retirement. |
| Audit | Continuous via SIEM; quarterly review of long-lived static credentials with bias toward replacement. |

---

## 10. Vendor Access

### 10.1 Onboarding

| **Step** | **Owner** |
|---|---|
| Vendor record created in TPRM with tier and country-of-access | Vendor Risk Analyst |
| Sponsor identified (named human in our org) | Business / Sponsor |
| Access scope defined - minimum required entitlements, time-bounded | Identity Engineer |
| MFA enrolled - phishing-resistant required for privileged | Identity Engineer |
| Sessions brokered through PAM where privileged | Identity Engineer |
| Country-of-access validated against Country Risk Register ([`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) Section 10) | Vendor Risk Analyst |
| Time-boxed: explicit expiration; renewal requires re-justification | Identity Engineer |

### 10.2 Monitoring

- Vendor sessions recorded per PAM policy.
- Geographic anomalies trigger alerts.
- Quarterly review of all active vendor access.
- Off-boarding triggered by project closeout, vendor termination, or country reclassification.

---

## 11. MFA Enrollment and Exception

### 11.1 Enrollment

| **Step** | **Detail** |
|---|---|
| Default factor | Phishing-resistant (FIDO2 security key, platform authenticator with attestation, certificate-based). |
| Backup factor | A second phishing-resistant factor where possible; one-time recovery code as fallback. |
| Enrollment moment | At first sign-in or pre-issued via secure handoff. |
| Privileged roles | Phishing-resistant only; SMS / voice prohibited. |
| Hardware tokens | Inventoried; loss reported and revoked within 4 hours. |
| Re-enrollment | On factor loss, suspected compromise, or 24-month routine refresh. |

### 11.2 Exceptions

MFA exceptions are time-bounded and tracked.

| **Exception Case** | **Treatment** |
|---|---|
| Legacy system unable to support phishing-resistant MFA | Time-boxed transitional exception with compensating controls (network segmentation, monitoring) per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) §7. |
| Operational technology operator console | Engineering review required; compensating controls per [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md). |
| Vendor unable to use phishing-resistant factor | Renegotiate; if unavoidable, time-bound exception with detection routing. |

Phishing-resistant MFA coverage is reported as `ID-001` in [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md).

---

## 12. Roles and Responsibilities

| **Role** | **Responsibility** |
|---|---|
| **Identity Engineer** | Owns this runbook. Designs, implements, and maintains the identity infrastructure including IGA, IdP, PAM, and secrets management. Ensures JML workflows execute within SLAs. Manages MFA enrollment, service account lifecycle, and vendor access provisioning. |
| **Manager / Approver** | Reviews and approves access requests for direct reports. Validates business need and role alignment. Participates in recertification campaigns; certifies, modifies, or removes entitlements with accountability. Initiates mover and leaver notifications to HR/IGA. |
| **System Owner** | Approves access to sensitive systems under their ownership. Defines role requirements and entitlement baselines for their systems. Participates in recertification for system-specific access. Ensures service accounts under their systems have named human owners. |
| **PAM Administrator** | Operates the PAM platform. Onboards privileged credentials, brokers sessions, manages session recording and retention. Executes credential rotation on checkout and post-use. Maintains break-glass credentials and coordinates quarterly hygiene checks. |
| **Vendor Risk Analyst** | Owns the vendor access lifecycle from a risk perspective. Creates and maintains vendor records in TPRM. Validates country-of-access against the Country Risk Register. Ensures vendor access is time-bounded, scoped to minimum required, and terminated on project closeout. |
| **User** | Uses only approved authentication factors. Reports MFA token loss immediately. Does not share credentials or service accounts. Completes required security awareness training before first access. Complies with access request and recertification requirements. |
| **SOC / Detection Engineer** | Monitors identity events for anomalies per [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md). Detects and escalates break-glass misuse, service account interactive logon, credential reuse, and geographic anomalies. Tunes detection rules in coordination with the Identity Engineer. |
| **CISO** | Endorses this runbook. Resolves disputes escalated beyond the Identity Engineer and Cyber Engineering Pillar Leader. Approves risk acceptances for MFA exceptions and compensating controls beyond standard tolerance. Signs off on annual recertification program results. |

---
## 13. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Runbook** |
|---|---|
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC / IA | All sections |
| [NIST 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) | Section 11 |
| [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) PROTECT | All sections |
| NERC-CIP CIP-004 R4/R5, CIP-005 R2 | Sections 3, 5, 6, 10 |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) / 800-171r3 (3.1, 3.5) | All sections |
| SOX ITGC (Access) | Sections 3, 4, 5, 6 |

---

## 14. Document Control

| | |
|---|---|
| **Document ID** | CERG-PRC-AC-002 |
| **Version** | 1.0 |
| **Approved By** | CISO |
| **Next Review** | Annual / IAM tooling change |
| **Change Log** | 1.0 - Initial publication. JML, access request, recertification, PAM, break-glass, service accounts, secrets, vendor access, MFA. Dual operating model preserved. |
