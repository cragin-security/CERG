
# SURGE: Cyber Engineering, Risk & Governance

## SECURITY CHANGE MANAGEMENT PROCEDURE
### Change Security Review · Emergency Changes · Control Impact · SOX ITGC Linkage

---

| | |
|---|---|
| **Document ID** | CERG-PRC-CHG-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) · [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) |
| **Review Cycle** | Annual / On material change to enterprise change management or SOX scope |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CM, SA, CA) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN, PROTECT) · ISO/IEC 27001 A.8.32 · CIS Controls v8 |
| **Regulations** | SOX ITGC · CMMC L2 / 800-171r3 · NERC-CIP where changes affect scoped systems |
| **Environments** | All security-relevant changes to CERG-managed systems, platforms, controls, and regulated environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [What Is a Security-Relevant Change](#3-what-is-a-security-relevant-change)
4. [Change Categories](#4-change-categories)
5. [Security Review Requirements](#5-security-review-requirements)
6. [Emergency Changes](#6-emergency-changes)
7. [SOX and Regulated-Scope Changes](#7-sox-and-regulated-scope-changes)
8. [Evidence and Records](#8-evidence-and-records)
9. [Metrics](#9-metrics)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

CERG does not replace the enterprise change management process. It supplies the security review discipline that process needs. A change can be operationally approved and still be a bad security change if it weakens a baseline, creates a new trust boundary, bypasses logging, changes privileged access, affects SOX scope, or pushes unresolved risk into production.

This procedure defines how security-relevant changes are identified, reviewed, evidenced, escalated, and linked to risk acceptance or architecture review. It also defines the minimum security handling for emergency changes and for changes affecting SOX ITGC, CUI, NERC-CIP, and other regulated scope.

> **Change Management Is Where Controls Stay True**
>
> A baseline is not defeated all at once. It erodes one exception, one rushed firewall rule, one emergency admin grant, one disabled log source at a time. Security change management is the discipline that catches that erosion while it is still a change request, not a finding six months later.

---

## 2. Principles

1. **CERG reviews security impact, not business priority.** The business decides whether a change is important. CERG decides whether the change weakens, bypasses, or requires controls.
2. **Security review is proportional.** A minor baseline-preserving change does not need a full architecture review. A material change to identity, network, data, cloud, OT, or regulated scope does.
3. **Emergency does not mean undocumented.** Emergency changes may move faster, but they still record what changed, why, who approved it, and how it was reviewed afterward.
4. **Changes with residual risk use the risk process.** A change that introduces unresolved security risk is not waved through informally. It is remediated or accepted through [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).
5. **SOX scope gets evidence discipline.** Financially relevant systems require stronger change evidence: request, approval, testing, implementation, and segregation of duties.

---

## 3. What Is a Security-Relevant Change

A change is security-relevant if it creates, removes, weakens, bypasses, or materially alters a security control, trust boundary, privileged access path, sensitive data path, or regulated system.

Security-relevant changes include:

- network segmentation, firewall, routing, remote access, VPN, or proxy changes;
- identity provider, MFA, SSO, privileged access, service account, or federation changes;
- cloud landing zone, account, subscription, tenant, storage, or policy changes;
- endpoint, EDR, MDM, logging, backup, or cryptography control changes;
- changes to applications that process Confidential or Restricted data;
- changes to SOX, CUI, NERC-CIP, OT, or safety-impacting environments;
- new third-party data exchange or vendor integration;
- emergency control bypasses;
- new AI capability or AI-enabled feature touching business data;
- changes that resolve or introduce a risk-register item.

A change not on this list may still be security-relevant if the Engineering Pillar Leader, Risk Pillar Leader, or Governance Pillar Leader determines that it affects control posture.

---

## 4. Change Categories

| **Category** | **Definition** | **Security Handling** |
|---|---|---|
| Standard security-preserving change | Pre-approved, low-risk, repeatable, and does not weaken a control. | Evidence retained; no separate CERG review unless sampled. |
| Normal security-relevant change | Planned change with security impact. | CERG review before implementation. |
| Material architecture change | Creates new trust boundary, data path, identity pattern, internet exposure, vendor integration, AI capability, or regulated scope. | Architecture review under [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). |
| Emergency change | Must be implemented before normal review to restore service, contain risk, or meet urgent operational need. | Emergency approval plus post-implementation security review. |
| Control bypass or exception | Temporarily or permanently weakens an approved control. | Risk acceptance or exception under [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |

---

## 5. Security Review Requirements

### 5.1 Minimum Review Questions

Every normal security-relevant change answers these questions before implementation:

1. What system, control, data path, or trust boundary changes?
2. What data classification is affected?
3. Does the change affect identity, privilege, logging, encryption, backup, segmentation, endpoint posture, or vendor access?
4. Does the change affect SOX, CUI, NERC-CIP, OT, or other regulated scope?
5. Does the change create a new threat model trigger under [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md)?
6. Does the change create residual risk, and if so, is that risk recorded and approved?
7. What evidence will prove the change was approved, tested, implemented, and verified?
8. What rollback or recovery plan exists?

### 5.2 Review Outcomes

| **Outcome** | **Meaning** |
|---|---|
| Approved | Security review finds no unresolved issue blocking implementation. |
| Approved with conditions | Change may proceed only if named conditions are met. |
| Requires architecture review | Change exceeds normal change review and enters [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). |
| Requires risk acceptance | Change introduces residual risk requiring [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |
| Rejected | Change weakens control posture without sufficient mitigation or acceptance. |

A change cannot be closed as security-approved until conditions, risk acceptances, or architecture-review actions are linked.

---

## 6. Emergency Changes

Emergency changes are allowed, but they are not a loophole.

### 6.1 Emergency Criteria

A change may be treated as emergency only when delay creates unacceptable operational, security, safety, or compliance impact. Convenience is not an emergency.

### 6.2 Minimum Emergency Record

The emergency change record contains:

- business or operational reason for emergency treatment;
- systems and controls affected;
- approver;
- implementer;
- start and completion time;
- change performed;
- testing or validation performed;
- rollback result or reason rollback was not needed;
- post-implementation security review outcome.

### 6.3 Post-Implementation Review

Emergency changes receive post-implementation security review within the organization's defined emergency-change window, and no later than the next business review cycle. The review confirms that:

1. the emergency criteria were valid;
2. the change is documented;
3. no unintended control bypass remains;
4. required evidence is retained;
5. any residual risk is recorded;
6. any temporary access, firewall rule, control disablement, or exception is removed or formally accepted.

> **Emergency Is a Speed, Not a Standard**
>
> An emergency change moves faster because the situation requires speed. It does not get a lower evidence bar, a lower approval bar, or a free pass on residual risk. The evidence may be completed after implementation, but it still exists. The review may occur after the change, but it still occurs. Emergency is the route, not the destination.

---

## 7. SOX and Regulated-Scope Changes

Changes affecting SOX ITGC, CUI, NERC-CIP, OT, or other regulated environments require additional evidence and review.

### 7.1 SOX ITGC

For SOX-scope systems, the change record must show:

- request and business justification;
- approval before implementation, except valid emergency changes;
- evidence of testing;
- implementer and approver;
- segregation of duties or compensating control where the same person requests, approves, tests, or implements;
- implementation evidence;
- post-implementation validation;
- link to the relevant SOX ITGC control in [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md).

### 7.2 CUI, NERC-CIP, and OT

For CUI, NERC-CIP, and OT-scope systems, the change record must show the regulatory scope considered, the relevant compliance manager consulted, and any required evidence retained in the evidence library under [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md).

---

## 8. Evidence and Records

Security change records are evidence. They are retained under [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) and include, at minimum:

| **Evidence Item** | **Required For** |
|---|---|
| Change request and scope | Every security-relevant change. |
| Security review decision | Normal, material, emergency post-review, and control-bypass changes. |
| Approval record | Every change requiring approval. |
| Test or validation result | Normal, material, SOX, CUI, NERC-CIP, and emergency changes. |
| Implementation record | Every implemented change. |
| Rollback plan or recovery note | Normal, material, and emergency changes. |
| Risk acceptance or exception | Any unresolved residual risk or control bypass. |
| Architecture review link | Any material architecture change. |

---

## 9. Metrics

| **Metric** | **Purpose** |
|---|---|
| Security-relevant changes reviewed | Measures volume of security change engagement. |
| Percent of reviewed changes approved with conditions | Shows how often review changes the outcome. |
| Changes requiring architecture review | Shows material design-change volume. |
| Changes requiring risk acceptance | Shows how often changes introduce residual risk. |
| Emergency changes by system and owner | Shows emergency-change pattern and possible process weakness. |
| Emergency changes reviewed within required window | Measures emergency discipline. |
| SOX-scope changes with complete evidence | Measures audit readiness. |
| Repeat change findings | Shows whether the process is improving. |

---

## 10. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Security Change Responsibility** |
|---|---|
| **Engineering Pillar Leader** | Accountable for this procedure and for security review of changes. Determines when a change requires architecture review. |
| **Cloud Security Engineer** | Reviews cloud, SaaS, network, and platform changes. |
| **Identity Engineer** | Reviews identity, MFA, privileged access, service account, federation, and secrets-related changes. |
| **OT Security Engineer** | Reviews OT, BES Cyber System, and IT/OT boundary changes. |
| **Application Security Engineer** | Reviews application, SDLC, API, and AI-related changes. |
| **Endpoint Engineer** | Reviews endpoint, MDM, EDR, and device posture changes. |
| **Cryptography Engineer** | Reviews key, certificate, TLS, and cryptographic control changes. |
| **Risk Pillar Leader** | Consulted on residual risk and risk treatment for changes. |
| **Risk Register Owner** | Records accepted residual risk and control exceptions arising from changes. |
| **SOX ITGC Lead** | Reviews and validates SOX-scope change evidence. |
| **CMMC / Federal Compliance Manager** | Reviews CUI-scope change implications. |
| **NERC-CIP Compliance Manager** | Reviews NERC-CIP-scope change implications. |
| **Evidence Librarian** | Retains change evidence for audits and control testing. |
| **Chief Information Security Officer (CISO)** | Approves High and Critical residual risk acceptance where required. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Procedure** |
|---|---|---|
| NIST 800-53r5 | CM-3, CM-4, CM-5, SA-10, CA-7 | Sections 3, 5, 6, 8 |
| NIST CSF 2.0 | GOVERN and PROTECT | Sections 5, 7, 9 |
| ISO/IEC 27001 | A.8.32 change management | Sections 4, 5, 6 |
| CIS Controls v8 | Secure configuration and change-related safeguards | Sections 5, 8 |
| SOX ITGC | Change approval, testing, implementation evidence, segregation of duties | Section 7 |
| CMMC L2 / NIST 800-171r3 | Configuration management and security assessment | Sections 5, 7 |
| NERC-CIP | Change and configuration controls for BES Cyber Systems | Sections 6, 7 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-CHG-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Approved By** | Governance Pillar Leader (pending); CISO endorses |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to enterprise change management or SOX scope |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-53r5 (CM, SA, CA); NIST CSF 2.0 (GOVERN, PROTECT); ISO/IEC 27001 A.8.32; CIS Controls v8 |
| **Regulations** | SOX ITGC; CMMC L2 / 800-171r3; NERC-CIP where changes affect scoped systems |
| **Environments** | All security-relevant changes to CERG-managed systems, platforms, controls, and regulated environments |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Engineering | Initial release. Establishes security-relevant change criteria, change categories, minimum security review questions, review outcomes, emergency-change handling, SOX and regulated-scope evidence requirements, retained evidence, metrics, and canonical role responsibilities. |

### Review Triggers

- Material change to enterprise change management
- Material change to SOX scope or ITGC expectations
- Repeated emergency-change findings
- Significant incident or audit finding caused by a change
- Direction from the CISO

Cyber Engineering owns this document. The Engineering Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Material changes enter architecture review |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Residual risk and exceptions from changes |
| SOX ITGC Operational Package | [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | SOX change-control evidence linkage |
| Secure Configuration Baseline Standard | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Baseline-impacting changes |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Identity and access changes |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Logging and monitoring changes |
| Secure Software Development and Application Security Standard | [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) | Application and SDLC changes |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Change evidence retention |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `CHG` domain |
