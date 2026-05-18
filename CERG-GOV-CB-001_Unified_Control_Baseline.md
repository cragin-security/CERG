
# SURGE: Cyber Engineering, Risk & Governance

## UNIFIED CONTROL BASELINE
### Organizational Baseline · Overlay Matrix · Implementation, Evidence, and Inheritance Model

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CB-001 |
| **Version** | 1.0 |
| **Status** | For Review |
| **Classification** | Internal - Confidential |
| **Owner** | Cyber Governance Manager (Control Baseline) |
| **Parent Policy** | [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-LM-001](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-RES-001](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| **Review Cycle** | Annual - and on framework version change ([NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) rev, [CMMC](https://dodcio.defense.gov/CMMC/) rev, NERC-CIP version) |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · CIS Controls v8 · ISO/IEC 27001 A.5–A.8 · CSA CCM v4 |
| **Regulations** | NERC-CIP v7 (and CIP-015 draft) · [CMMC L2](https://dodcio.defense.gov/CMMC/) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT, CUI |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Design Principles](#2-design-principles)
3. [The CERG Control Family Spine](#3-the-cerg-control-family-spine)
4. [Implementation Statuses](#4-implementation-statuses)
5. [Inheritance Model](#5-inheritance-model)
6. [Organizational Baseline (Core)](#6-organizational-baseline-core)
7. [Overlay Matrix](#7-overlay-matrix)
8. [Control-to-Evidence Mapping](#8-control-to-evidence-mapping)
9. [Regulatory Crosswalks](#9-regulatory-crosswalks)
10. [Governance, Change, and Versioning](#10-governance-change-and-versioning)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

The Unified Control Baseline turns the principles in [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md), the requirements in subordinate standards, and the philosophy in the [CERG Risk Management Framework](CERG_Risk_Management_Framework_v1.0.md) into an implementation-ready control set. It is the document a control owner, an internal auditor, a [CMMC](https://dodcio.defense.gov/CMMC/) C3PAO, a NERC-CIP auditor, or a [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) auditor opens first.

It applies to every in-scope asset and every CERG-owned control. Where a subordinate standard imposes a more specific requirement, the standard controls and is referenced from the relevant entry here.

> **One Baseline, Many Audiences**
>
> Most programs maintain a separate control library per regulator, one for NIST, one for [CMMC](https://dodcio.defense.gov/CMMC/), one for NERC-CIP, one for [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and then spend a quarter of every audit reconciling them. CERG inverts that: one baseline is implemented once and evidenced once. The crosswalks in Section 9 translate the same evidence into the language each regulator expects.

---

## 2. Design Principles

The baseline is built on five non-negotiable principles. Anything that violates them is not in the baseline.

1. **NIST is the spine.** [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) control families are the organizing structure. CERG-native controls are layered onto that spine, never the reverse. When a NIST family fully covers an intent, CERG inherits the NIST language and identifier rather than coining a new one.
2. **Each control has one accountable CERG pillar.** Engineering, Risk, or Governance, never "shared." Supporting roles are listed separately. Accountability without ambiguity is the prerequisite to evidence.
3. **Each control has named evidence.** A control without a named evidence artifact is a control without proof; it does not enter the baseline.
4. **Overlays add, they do not redefine.** CUI, BES, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and Safety overlays add controls or tighten parameters of base controls. They never silently relax the base.
5. **Inheritance is documented or it does not exist.** Inheritance from cloud/SaaS providers requires the artifact named in Section 5. "We assume the provider handles it" is not inheritance.

---

## 3. The CERG Control Family Spine

CERG uses [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) control families as the top-level grouping. Each family has a one-line CERG intent and a primary owning pillar.

| **Family** | **NIST Code** | **CERG Intent (one line)** | **Primary Owner** |
|---|---|---|---|
| Access Control | AC | Identity-bound, least-privilege access enforced consistently across IT, cloud, SaaS, OT, and CUI. | Engineering |
| Awareness and Training | AT | Role-relevant security training; CERG defines the cyber content, Awareness function delivers. | Governance (content) |
| Audit and Accountability | AU | Log every consequential action; protect, retain, and review the logs. | Risk (detection) |
| Assessment, Authorization, and Monitoring | CA | Continuous, evidence-driven assurance that controls operate as intended. | Governance |
| Configuration Management | CM | Approved baselines, change control, and drift detection across every platform. | Engineering |
| Contingency Planning | CP | Cyber recovery and backup that survive ransomware, region failure, and OT event. | Engineering (cyber side) |
| Identification and Authentication | IA | Strong, phishing-resistant identity for humans and machines. | Engineering |
| Incident Response | IR | CERG-side requirements that IR depends on (telemetry, identity, baselines, recovery, evidence). | Risk (interface) |
| Maintenance | MA | Controlled, evidenced maintenance; tighter in OT and BES scope. | Engineering |
| Media Protection | MP | CUI and Restricted-data media handling. | Governance |
| Physical and Environmental | PE | Cyber dependency on physical controls (data center, OT, CUI work area). | Governance (interface) |
| Planning | PL | SSPs, security plans, authorization packages, architecture documentation. | Engineering / Governance |
| Personnel Security | PS | Screening and access-tied personnel controls. | Governance (interface to HR) |
| Risk Assessment | RA | Continuous risk identification, scoring, and treatment. | Risk |
| System and Services Acquisition | SA | Security in procurement, vendor risk, SBOMs, secure SDLC. | Risk (TPRM) / Engineering (SDLC) |
| System and Communications Protection | SC | Network segmentation, cryptography, OT boundary protection. | Engineering |
| System and Information Integrity | SI | Vulnerability, malware, monitoring, advisories, integrity. | Risk |
| Supply Chain Risk Management | SR | Software, hardware, and service supply chain integrity. | Risk (TPRM) |
| Program Management | PM | The CERG program itself - policy, metrics, board reporting. | Governance |

---

## 4. Implementation Statuses

Every control entry in the baseline carries one of the following statuses. The set is intentionally small, it survives audits in every framework CERG must support.

| **Status** | **When to Use** | **Evidence Expected** |
|---|---|---|
| `Implemented` | Control is in place, tested, and operating as designed. | Named evidence artifact for the current cycle. |
| `Partially Implemented` | Control is in place for some scope or is operating at reduced effectiveness. | Evidence of what is in place plus a POA&M entry. |
| `Inherited` | Implementation is provided by another party - cloud provider, SaaS provider, parent enterprise control, IAM team. | Inheritance Evidence Package (Section 5). |
| `Planned` | Control is in the roadmap with an owner and target date. | POA&M entry with date and owner. |
| `Risk Accepted` | Deviation is approved and tracked via [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) Section 7. | Risk register entry, exception ID, approver. |
| `Not Applicable` | Control does not apply to this scope. | Documented N/A rationale (system type, no in-scope data, etc.). |

> **What's Not on the List**
>
> "In Progress," "TBD," "Working On It," and "Vendor Says Yes" are not statuses. Every entry in the baseline maps to one of the six above. Honesty about Partially Implemented and Planned is worth far more than optimism about Implemented.

---

## 5. Inheritance Model

`Inherited` is the most-abused status in cloud-era control libraries. CERG requires the following Inheritance Evidence Package for any control marked `Inherited`. Without it, the status defaults to `Not Implemented` and a finding is opened.

The package has six elements:

1. **Provider attestation**, current SOC 2 Type II / ISO 27001 / FedRAMP / PCI report containing the inherited control.
2. **Shared responsibility mapping**, the section of the provider's shared responsibility matrix that names this control as the provider's.
3. **Customer-side evidence of configuration**, proof the customer-side prerequisites are configured (e.g., logging enabled, region selected, IAM lockdown applied) that allow the inherited control to actually protect the customer's tenancy.
4. **Sub-service organization carve-outs**, explicit notation if the inherited control depends on a sub-service organization (e.g., AWS underlying Snowflake) and how that dependency is covered.
5. **Currency check**, attestation expiry date and the calendar entry that re-runs this check.
6. **Re-papering trigger**, what would cause CERG to re-evaluate inheritance (provider control failure, attestation lapse, scope change, customer-side prerequisite drift).

This package is the basis of every "we inherit it from AWS / Azure / GCP / M365 / Salesforce / ServiceNow / our [CMMC](https://dodcio.defense.gov/CMMC/) enclave provider" claim CERG makes.

---

## 6. Organizational Baseline (Core)

The organizational baseline applies to every in-scope asset. Overlays in Section 7 add or tighten controls for High-Impact, CUI, BES, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and OT Safety scopes.

The full implementation-ready control set is captured by family in the sections that follow. Each entry has: Control ID · Action Statement · System Applicability · Owning Pillar · Named Evidence · Frequency · Subordinate Standard.

System Applicability uses one or more of the following values: Hardware, Software, Network, Cloud, Data, Process.

Section 6 entries below are organized by family and reference the subordinate standard for parameter detail. Where parameter detail differs by environment (IT/cloud/SaaS, OT, CUI), the subordinate standard is authoritative; the baseline names the control once.

### 6.1 Access Control (AC)

| **Control**                      | **Statement**                                                                                                                                                                                                   | **System Applicability**                          | **Owner**   | **Evidence**                      | **Min Freq**           | **Std**                 |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------- | --------------------------------- | ---------------------- | ----------------------- |
| AC-2 Account Management          | Make sure every account used with your system has an approved request, named owner, defined access level, and current JML record; update or remove access when roles change or access is no longer needed.      | Hardware, Software, Network, Cloud, Data, Process | Engineering | JML log, quarterly recert report  | Continuous / Quarterly | STD-AC-001              |
| AC-3 Access Enforcement          | Make sure your system uses approved authentication and authorization controls for all access, and that local, shared, hard-coded, or static credentials cannot bypass them.                                     | Hardware, Software, Network, Cloud, Data          | Engineering | IdP/PAM policy export             | Annual                 | STD-AC-001              |
| AC-6 Least Privilege             | Grant users, administrators, services, and vendors only the access needed for their role; make privileged access time-bound, just-in-time where supported, and recorded.                                        | Hardware, Software, Network, Cloud, Data, Process | Engineering | PAM session logs, role inventory  | Quarterly              | STD-AC-001              |
| AC-7 Unsuccessful Logon Attempts | Configure failed-login thresholds, lockouts, and identity-attack alerts according to STD-AC-001 and verify they are operating.                                                                                  | Hardware, Software, Network, Cloud                | Engineering | IdP policy export, detection rule | Annual                 | STD-AC-001 / STD-LM-001 |
| AC-17 Remote Access              | Make sure remote access to your system uses approved gateways, MFA, and session logging; do not create direct or undocumented remote access paths. Access outside of the US will need documented exceptions.    | Network, Cloud                                    | Engineering | Gateway logs, MFA policy export   | Continuous             | STD-AC-001              |
| AC-19 Mobile / BYOD              | Allow mobile or BYOD access only when the device is enrolled, compliant, and approved by conditional-access policy.                                                                                             | Hardware                                          | Engineering | MDM compliance report             | Quarterly              | STD-AC-001              |

### 6.2 Audit and Accountability (AU)

| **Control**                          | **Statement**                                                                                                                                                               | **System Applicability**                          | **Owner** | **Evidence**                                    | **Min Freq** | **Std**    |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --------- | ----------------------------------------------- | ------------ | ---------- |
| AU-2 Event Logging                   | Make sure your system sends required security, administrative, authentication, and activity logs to the SIEM or approved OT one-way collection point.                       | Hardware, Software, Network, Cloud, Data          | Risk      | SIEM source inventory, gap report               | Monthly      | STD-LM-001 |
| AU-6 Audit Review                    | Review and respond to alerts generated from your system logs, and correct coverage or tuning gaps identified by Risk.                                                       | Hardware, Software, Network, Cloud, Data, Process | Risk      | Detection coverage report, triage queue metrics | Continuous   | STD-LM-001 |
| AU-9 Protection of Audit Information | Protect your system's audit logs from alteration or deletion, and make sure administrative changes to logging are also logged.                                              | Software, Cloud, Data, Process                    | Risk      | Storage policy, admin-action review             | Quarterly    | STD-LM-001 |
| AU-11 Audit Record Retention         | Keep audit records for the required retention period, including 13 months hot / 7 years cold by default and BES minimums when applicable; verify a sample can be retrieved. | Hardware, Software, Network, Cloud, Data, Process | Risk      | Retention policy, sample retrieval              | Annual       | STD-LM-001 |

### 6.3 Configuration Management (CM)

| **Control**                     | **Statement**                                                                                                                                                                                         | **System Applicability**                          | **Owner**          | **Evidence**                               | **Min Freq** | **Std**                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------ | ------------------------------------------ | ------------ | ----------------------- |
| CM-2 Baseline Configuration     | Apply the correct DISH baseline for your platform class and keep evidence showing the baseline was applied.                                                                                           | Hardware, Software, Network, Cloud                | Engineering        | DISH baseline catalog, scan report         | Continuous   | STD-CFG-001             |
| CM-3 Change Control             | Submit production changes through change management before implementation and include security review when required.                                                                                  | Hardware, Software, Network, Cloud, Data, Process | Engineering        | CAB minutes, change records                | Continuous   | STD-IT-001 / STD-OT-001 |
| CM-6 Configuration Settings     | Create and confirm a system baseline so cyber can detect and remediate drift; document and route exceptions through Section 4.                                                                        | Hardware, Software, Network, Cloud                | Engineering        | Drift report, exception register           | Continuous   | STD-CFG-001             |
| CM-7 Least Functionality        | Disable unnecessary services and ports, and make sure only approved software is installed.                                                                                                            | Hardware, Software, Network, Cloud                | Engineering        | App allowlist, port scan report            | Quarterly    | STD-CFG-001             |
| CM-8 System Component Inventory | Make sure your hardware, software, cloud resources, network devices, data stores, and process owners are recorded in the correct CMDB or authoritative inventory with all applicable fields complete. | Hardware, Software, Network, Cloud, Data, Process | Engineering / Risk | Asset inventory export, reconciliation log | Monthly      | STD-IT-001 / STD-OT-001 |

### 6.4 Contingency Planning (CP)

| **Control**                       | **Statement**                                                                                                                                            | **System Applicability**                          | **Owner**   | **Evidence**                                 | **Min Freq**                | **Std**     |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------- | -------------------------------------------- | --------------------------- | ----------- |
| CP-2 Contingency Plan             | Make sure your system has a current cyber recovery plan mapped to its tier and coordinated with enterprise BCP requirements.                             | Hardware, Software, Network, Cloud, Data, Process | Engineering | Plan document, BCP interface record          | Annual                      | STD-RES-001 |
| CP-4 Contingency Plan Testing     | Test the recovery plan on the required cadence, document lessons learned, and update RTO/RPO assumptions when results show gaps.                         | Hardware, Software, Network, Cloud, Data, Process | Engineering | Test report, lessons learned, register entry | Annual / BES Annual         | STD-RES-001 |
| CP-9 System Backup                | Make sure backups for your system and data are immutable, isolated, and restorable; for OT, include configurations, firmware, logic, and historian data. | Hardware, Software, Network, Cloud, Data          | Engineering | Backup report, immutability evidence         | Continuous / Annual restore | STD-RES-001 |
| CP-10 Information System Recovery | Run recovery tests that prove your system can meet its defined RTO and RPO, and retain restoration evidence.                                             | Hardware, Software, Network, Cloud, Data, Process | Engineering | Restoration test evidence                    | Annual                      | STD-RES-001 |

### 6.5 Identification and Authentication (IA)

| **Control**                                                   | **Statement**                                                                                                                                           | **System Applicability**                          | **Owner**   | **Evidence**                    | **Min Freq** | **Std**                 |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------- | ------------------------------- | ------------ | ----------------------- |
| IA-2 Identification and Authentication (Organizational Users) | Make sure all interactive human access to your system requires phishing-resistant MFA and does not allow legacy authentication.                         | Hardware, Software, Network, Cloud, Data          | Engineering | IdP policy, exception register  | Quarterly    | STD-AC-001              |
| IA-3 Device Identification and Authentication                 | Make sure your system, device, or service presents the identifiers needed for IdP, NAC, CAP, or other network controls to recognize it where supported. | Hardware, Network, Cloud                          | Engineering | NAC / conditional-access policy | Annual       | STD-AC-001              |
| IA-5 Authenticator Management                                 | Store and rotate credentials, secrets, API keys, and certificates in approved tools and follow the STD-CR-001 lifecycle.                                | Hardware, Software, Network, Cloud, Data, Process | Engineering | Secrets manager, cert inventory | Continuous   | STD-CR-001 / STD-AC-001 |

### 6.6 Risk Assessment, System and Information Integrity, Supply Chain (RA / SI / SR)

| **Control**                                | **Statement**                                                                                                                                                                                                  | **System Applicability**                          | **Owner**          | **Evidence**                              | **Min Freq** | **Std**                  |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------ | ----------------------------------------- | ------------ | ------------------------ |
| RA-3 Risk Assessment                       | Identify risks for your system, data, or process; document impact and likelihood; assign treatment; and keep the risk register current.                                                                        | Hardware, Software, Network, Cloud, Data, Process | Risk / Governance  | Risk register                             | Continuous   | PRC-RM-001               |
| RA-5 Vulnerability Monitoring and Scanning | Make sure your system is assessed on the required cadence using authenticated scanning and the applicable DISH profile, or an approved passive/alternative method where active scanning is not allowed.        | Hardware, Software, Network, Cloud                | Risk               | Scan reports, SLA dashboard               | Continuous   | PRC-VM-001 / STD-CFG-001 |
| SI-2 Flaw Remediation                      | Remediate Critical and High findings within SLA, or document an approved exception or risk acceptance before the SLA is missed.                                                                                | Hardware, Software, Network, Cloud, Process       | Risk / Engineering | SLA report, exception register            | Continuous   | PRC-VM-001               |
| SI-4 System Monitoring                     | Make sure the required monitoring tools for your environment cover your system and that SIEM, EDR, NDR, CSPM/SSPM, or OT-passive monitoring gaps are documented.                                               | Hardware, Software, Network, Cloud, Data          | Risk               | Coverage report                           | Continuous   | STD-LM-001               |
| SR-2 Supply Chain Risk Management Plan     | Make sure each vendor or service supporting your system or process is tiered, tier-specific evidence requirements are understood, contract clauses match the tier, and required SCCT information is collected. | Hardware, Software, Network, Cloud, Data, Process | Risk (TPRM)        | TPRM register, SCCT roster                | Continuous   | PRC-TPRM-001             |
| SR-3 Supply Chain Controls and Processes   | Do not allow international access unless the country-risk exception is approved and documented.                                                                                                                | Software, Network, Cloud, Data, Process           | Risk (TPRM)        | Country-risk register, exception register | Quarterly    | PRC-TPRM-001             |

## 7. Overlay Matrix

Overlays add to the organizational baseline. They never silently relax it.

| **Overlay** | **Applies To** | **Adds / Tightens** | **Source Standard** |
|---|---|---|---|
| **High-Impact** | Systems whose loss would materially impact the business or safety | Tighter remediation SLAs, CIS L2 baseline, expanded monitoring, MFA for all non-human identities. | STD-CFG-001 + STD-LM-001 |
| **CUI** | Any system that stores/processes/transmits CUI | [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) controls; SSP + POA&M + SPRS; FIPS-validated cryptography; DFARS flow-down; [CMMC L2](https://dodcio.defense.gov/CMMC/) assessment readiness. | STD-CUI-001 + PLN-CUI-001 |
| **BES** | Medium/High Impact BES Cyber Systems | NERC-CIP v7 controls including CIP-007, CIP-010, CIP-013; ESP/EAP topology; 90-day searchable / 12-month total log retention; annual recovery exercise; CIP-015 INSM where applicable. | STD-OT-001 + PLN-CIP-001 |
| **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC** | Systems supporting financial reporting | Access, change, operations, backup, interface, and report ITGC controls; quarterly SoD review; SOC 1 reuse for hosted financi