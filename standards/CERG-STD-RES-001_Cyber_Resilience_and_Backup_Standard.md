
# SURGE: Cyber Engineering, Risk & Governance

## CYBER RESILIENCE AND BACKUP STANDARD
### Recovery Tiers · Backup Protection · Restoration Testing · Regulated Overlays · BCP Interface

---

| | |
|---|---|
| **Document ID** | CERG-STD-RES-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Resilience) |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-CFG-001](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-STD-LM-001](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Review Cycle** | Annual / On major platform change |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CP) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (RECOVER) · NIST 800-184 · ISO/IEC 27031 |
| **Regulations** | NERC-CIP CIP-009 · [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.8 / 3.6) · SOX ITGC (Backups / Operations) |
| **Environments** | Owned data center · IaaS / PaaS · SaaS Tier 1 · OT (BES and non-BES) · CUI scopes |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Boundary: Cyber Resilience vs. Enterprise BCP](#2-boundary-cyber-resilience-vs-enterprise-bcp)
3. [Recovery Tiers and RTO/RPO Model](#3-recovery-tiers-and-rtorpo-model)
4. [Backup Protection and Immutability](#4-backup-protection-and-immutability)
5. [Restoration Testing](#5-restoration-testing)
6. [Cloud and SaaS Recovery](#6-cloud-and-saas-recovery)
7. [OT Recovery and CIP-009](#7-ot-recovery-and-cip-009)
8. [CUI Recovery](#8-cui-recovery)
9. [SOX Availability Evidence](#9-sox-availability-evidence)
10. [Roles and BCP Interface](#10-roles-and-bcp-interface)
11. [Recovery Plan Template](#11-recovery-plan-template)
12. [Regulatory and Framework Alignment Summary](#12-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

The policy, IT standard, OT standard, CUI standard, compliance matrix, and RMF all require documented and tested recovery plans, backup protection, and restoration evidence. Until this standard, those obligations had no shared executable definition, RTO/RPO tiers, immutability requirements, restoration evidence formats, and the boundary with enterprise BCP were left for each subordinate document to imply.

This standard closes that gap. It applies to every in-scope asset that has data, configuration, or workload state worth recovering.

> **Cyber Resilience Is Not BCP**
>
> Business continuity owns the *business* recovery: order processing keeps moving, customers are notified, alternate sites stand up. CERG owns the *cyber* recovery: the systems and data are restored from clean, immutable backups onto known-good baselines, with identity and detection re-enabled. The two programs coordinate; they do not substitute for each other.

---

## 2. Boundary: Cyber Resilience vs. Enterprise BCP

| **Question** | **Owner** |
|---|---|
| Are critical backups taken, protected, and restorable? | CERG (this standard). |
| Are systems restored to a clean, hardened state with known-good baselines? | CERG (this standard). |
| Is identity, detection, and logging brought back online on the recovered system? | CERG (this standard). |
| Are operational workarounds and customer communications in place during the outage? | Enterprise BCP. |
| Is the business processing relocated to an alternate site / process? | Enterprise BCP. |
| Are non-cyber dependencies (people, facilities, supplies) recovered? | Enterprise BCP. |

CERG produces inputs to Enterprise BCP: tested cyber recovery plans, RTO/RPO actuals, and clean-restore preconditions. Enterprise BCP produces inputs to CERG: business criticality tiering, alternate-site cyber dependencies, and recovery priority calls during an event.

---

## 3. Recovery Tiers and RTO/RPO Model

Every in-scope asset has a CERG recovery tier. The tier drives RTO/RPO targets, backup frequency, immutability requirements, and restoration test cadence. Tiering is owned by Engineering in partnership with the business and Enterprise BCP, the business sets criticality, CERG sets the cyber tier consistent with criticality.

| **Tier** | **Description** | **RTO (Cyber)** | **RPO** | **Backup Frequency** | **Restoration Test** |
|---|---|---|---|---|---|
| **T1 - Mission-Critical** | Outage causes safety, regulatory, or material financial loss within hours. | ≤ 4 hours | ≤ 15 minutes | Continuous / near-continuous | Quarterly full restore; annual full DR exercise |
| **T2 - Business-Critical** | Outage materially impairs operations within one business day. | ≤ 24 hours | ≤ 4 hours | Hourly to every 4 hours | Semi-annual restore; annual exercise |
| **T3 - Important** | Outage degrades operations but is tolerable for a few days. | ≤ 72 hours | ≤ 24 hours | Daily | Annual restore |
| **T4 - Standard** | Outage is inconvenient; standard business hours recovery acceptable. | ≤ 1 week | ≤ 24 hours | Daily | Annual restore |
| **T5 - Non-Production** | Dev/test/sandbox. Recovery is rebuild from code/IaC. | Best effort | n/a | n/a (rebuild from IaC) | n/a |

> **The RTO Number Is Honest or It Is Useless**
>
> A T1 RTO of 4 hours that has never been demonstrated by a real restoration is a number on a slide. CERG only certifies an asset to a tier after a restoration test demonstrates the RTO/RPO. Until then the asset is classified Tier "Aspirational" and tracked in the resilience register as a Planned control.

---

## 4. Backup Protection and Immutability

Every backup of an in-scope asset meets the following requirements at minimum. Tier-specific tightening is named where it applies.

### 4.1 The Backup Protection Checklist

| **Requirement** | **All Tiers** | **T1 / T2 / BES / CUI** |
|---|---|---|
| Backups taken at the frequency in Section 3 | ✓ | ✓ |
| Backups encrypted at rest (CMK where Restricted/CUI per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)) | ✓ | ✓ |
| At least one copy stored on immutable storage (object-lock / WORM / air-gap) | ✓ | ✓ |
| Backups stored in a separately-credentialled tenancy / account / domain | ✓ | ✓ |
| Backup admin role separate from production admin role; MFA enforced | ✓ | ✓ |
| Backup deletion / shortening requires two-person approval | - | ✓ |
| Backup retention period meets the longer of: business need · regulatory minimum · 13 months default | ✓ | ✓ |
| Backups validated for integrity at write and on a sample cadence | ✓ | ✓ |
| Backup of configurations / firmware / logic / historian (OT scope) per Section 7 | n/a | ✓ (BES) |
| One offline / "cold" copy of critical baselines and recovery preconditions | - | ✓ |

### 4.2 The Air-Gap and Immutability Rationale

Ransomware tooling routinely attacks backup systems before triggering encryption. The immutability and credential separation requirements above exist specifically because production-attached, production-credentialled backups are not a defense.

> **If the Backup Lives on Production, It's Not a Backup**
>
> A snapshot taken on the same storage system as production, accessible by the same credentials, is a convenience feature. It is not a cyber backup. The cyber backup lives somewhere a compromised production-domain identity cannot reach.

---

## 5. Restoration Testing

A backup that has never been restored is a hope, not a control. Restoration tests produce evidence per [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) control-to-evidence mapping.

### 5.1 Cadence

| **Tier** | **Backup Integrity Check** | **Sample Restore** | **Full Restore Test** | **Full DR Exercise** |
|---|---|---|---|---|
| T1 | Continuous | Monthly | Quarterly | Annual |
| T2 | Continuous | Quarterly | Semi-annual | Annual |
| T3 | Daily | Quarterly | Annual | n/a |
| T4 | Daily | Annual | Annual | n/a |
| BES | Daily | Quarterly | Annual (CIP-009 R3) | Annual (CIP-009 R2) |
| CUI | Daily | Quarterly | Annual | Annual |

### 5.2 Restoration Test Procedure

Each full restoration test follows the procedure below and produces the evidence artifact in Section 5.3.

1. **Pre-test brief**, scope, success criteria, RTO/RPO targets, dependencies, business / OT owner notified.
2. **Isolate** the recovery environment from production where applicable (no risk of overwriting production).
3. **Restore** from immutable copy onto a clean baseline (DISH profile per [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)).
4. **Bring up identity, logging, detection, and monitoring** before declaring the system available.
5. **Validate** data integrity against last known-good (hash, checksum, sample query).
6. **Measure** RTO actual and RPO actual against targets. Document deltas.
7. **Tear down** or promote per scope.
8. **Lessons learned** captured into the resilience register and, where applicable, the risk register.

### 5.3 Restoration Test Evidence

| **Field** | **Required?** | **Notes** |
|---|---|---|
| Asset / System ID | ✓ | From asset inventory |
| Tier | ✓ | Per Section 3 |
| Backup Source (system, location, immutability evidence) | ✓ | - |
| Date / Duration | ✓ | - |
| Participants and roles | ✓ | - |
| RTO Target / Actual | ✓ | - |
| RPO Target / Actual | ✓ | - |
| Baseline applied during recovery | ✓ | DISH tier reference |
| Identity / logging / detection re-enabled | ✓ | Named systems |
| Integrity check method and result | ✓ | - |
| Issues encountered | ✓ | - |
| Lessons learned and follow-up actions | ✓ | Risk register IDs if any |
| Approver sign-off | ✓ | Engineering Pillar Leader + Asset Owner |

---

## 6. Cloud and SaaS Recovery

Cloud and SaaS recovery is shaped by the shared-responsibility model. CERG does not assume provider recovery covers customer-side obligations.

### 6.1 Cloud-Native Workloads (IaaS / PaaS)

- **IaC reconstruction**: production environments rebuildable from version-controlled IaC plus data backups.
- **Account / subscription / project failure modes**: tested at the in-scope cadence, including region failure, account compromise, and IAM root account loss.
- **Provider-side recovery contacts and escalation paths**: documented in the Recovery Plan; verified annually.
- **Cross-region or cross-cloud failover**: where required by Tier, tested and evidenced.

### 6.2 Tier 1 SaaS

Provider native restore is the first line; CERG-managed SaaS backup is added where provider native restore is insufficient or where regulator requires customer-controlled backup.

| **Tier 1 SaaS** | **Provider Native Restore Sufficient?** | **CERG-Managed SaaS Backup?** |
|---|---|---|
| M365 (Exchange / SharePoint / OneDrive / Teams) | Limited (retention / point-in-time) | Yes - for CUI workspaces and SOX-relevant mailboxes/sites |
| Salesforce | Limited | Yes - daily export for SOX in-scope orgs |
| ServiceNow | Yes (provider managed) | Audit-only export quarterly |
| Other Tier 1 | Decision per onboarding review | Documented in shared responsibility matrix |

---

## 7. OT Recovery and CIP-009

OT recovery is uniquely prescriptive. CERG implements CIP-009 fully and extends it where multiple operating segments demand more.

### 7.1 OT Artifacts That Must Be Backed Up

CIP-009 R1 specifies recovery plans; CERG requires that the following OT artifacts are explicitly in backup scope:

- Configuration files (SCADA, HMI, historian, jump server, network device, firewall)
- Firmware images and versions in service (RTU, relay, OT switch, controller)
- Software installers for the in-service OS, application, and engineering tool versions
- Logic files (PLC ladder logic, RTU configuration, relay setting groups)
- Historian data sets at the retention required for operational and regulatory needs
- Relay setting groups with version, date, and operator metadata
- Engineering tool images and licensing artifacts
- Jump server images / known-good baselines
- Documentation: as-built diagrams, ESP/EAP topology, vendor compatibility matrices

### 7.2 CIP-009 R1 / R2 / R3 Implementation

- **R1, Recovery Plan Specifications:** documented per asset class; reviewed annually; includes roles, processes for backup management, and methods to preserve data essential for restoration.
- **R2, Recovery Plan Implementation and Testing:** tested at least once every 15 months; one full operational exercise every 36 months (per CIP-009 R2.2).
- **R3, Lessons Learned and Plan Updates:** documented within 90 days of any plan implementation or test.

### 7.3 OT Restoration Cautions

> **OT Recovery Has Safety Implications**
>
> Restoring a misconfigured relay setting group from backup can shed load or trip a substation. OT restoration is supervised by an operator with substation-engineering authority, never by Cyber alone. The Recovery Plan names the operator role explicitly.

---

## 8. CUI Recovery

CUI recovery aligns with [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.8 (Media Protection, backups) and 3.6 (Incident Response, recovery from incident affecting CUI).

- **Backup encryption** uses FIPS-validated cryptography per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md).
- **Backup storage** stays within the CUI enclave or its provider-equivalent boundary; no cross-spillage to non-CUI environments.
- **Restoration test** validates that CUI labeling, access control, and logging are intact after recovery.
- **Post-incident updates** to SSP and POA&M per [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md).
- **Incident-driven recovery**: if a CUI system is recovered following an incident, the recovery itself is documented as POA&M follow-up.

---

## 9. SOX Availability Evidence

SOX-relevant systems (per [`CERG-PLN-SOX-001`](../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) SOX-Relevant System Register) require evidence of backup, restoration, and availability controls reusable in the SOX cycle.

| **SOX ITGC - Backup / Operations** | **Reused CERG Evidence** |
|---|---|
| Backups are taken | Backup tool report; failure logs |
| Backups can be restored | Restoration test evidence (this standard, Section 5.3) |
| Restoration is timely | RTO actual against tier target |
| Failed jobs are remediated | Backup job ticket history |
| Availability incidents are tracked | Incident records (per [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)) with cyber annotation |

SOX evidence reuses these artifacts; no duplicate "SOX-only" restoration test is performed.

---

## 10. Roles and BCP Interface

| **Role** | **Resilience Responsibilities** |
|---|---|
| **CERG - Engineering (Resilience)** | Owns this standard. Maintains the resilience register (tier per asset, last test result, next test date). Coordinates restoration tests. Maintains Recovery Plans (Section 11) for in-scope assets. Provides clean-restore preconditions to BCP. |
| **CERG - Risk** | Tracks resilience-related risks (untested plans, expired tests, T1 gaps). Adversarial validation may include backup/recovery as an attack target. |
| **CERG - Governance** | Tracks evidence currency (control CP-2, CP-4, CP-9, CP-10 in [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md)). Liaises with auditors. |
| **Asset / Business Owners** | Define business criticality. Participate in restoration tests. Approve Recovery Plan changes. |
| **OT Operations** | Lead OT restoration; consume Recovery Plan; supervise restorations with operational safety authority. |
| **Enterprise BCP** | Owns business recovery. Consumes CERG cyber readiness signals; provides recovery priority decisions during an event. |
| **Incident Response** | Activates Recovery Plans during incidents; CERG provides clean-restore baselines and recovery support. |

---

## 11. Recovery Plan Template

Every in-scope asset (or asset cluster) has a Recovery Plan in the format below.

```
RECOVERY PLAN - <System / Cluster Name>           PLAN-RES-YYYY-NNNN

1. ASSET CONTEXT
   System ID(s)              :
   Tier                      :  (T1–T5)
   Business Owner            :
   Engineering Owner         :
   OT Operator (if OT)       :
   Regulatory Scope          :  CUI / BES / SOX / None
   Dependencies              :  (named upstream/downstream systems)

2. TARGETS
   RTO (cyber)               :
   RPO                       :
   Last Demonstrated RTO     :
   Last Demonstrated RPO     :
   Test Cadence              :

3. BACKUP CONFIGURATION
   Backup System(s)          :
   Frequency                 :
   Immutability Mechanism    :
   Retention                 :
   Backup Credentials/Owner  :  (separately credentialled)
   Encryption / Key Source   :  (CMK ref per [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md))

4. RESTORATION PROCEDURE
   Pre-test brief            :  (process / template)
   Restore steps             :  (ordered; reference runbooks)
   Identity / logging / detection re-enable steps
   Validation steps          :
   Tear-down / promotion     :

5. CIP-009 NOTES (if BES)
   R1 / R2 / R3 references   :
   Operator role with restore authority :

6. CUI NOTES (if CUI)
   FIPS crypto evidence      :
   POA&M update path         :

7. SOX NOTES (if SOX in-scope)
   Evidence reuse mapping    :  (per Section 9)

8. INTERFACE TO ENTERPRISE BCP
   BCP Plan reference        :
   Hand-off triggers         :

9. CHANGE LOG
```

A populated example is maintained in the resilience program library; the template is reused without modification.

---
## 12. Document Control

| | |
|---|---|
| **Document ID** | CERG-STD-RES-001 |
| **Version** | 1.21 |
| **Approved By** | CISO |
| **Next Review** | Annual / major platform change |
| **Change Log** | 1.0 - Initial publication. Establishes recovery tiers, backup protection, restoration testing, regulated overlays, and BCP interface. |

