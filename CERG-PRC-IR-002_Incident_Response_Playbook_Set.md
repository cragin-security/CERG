
# SURGE: Cyber Engineering, Risk & Governance

## INCIDENT RESPONSE PLAYBOOK SET
### CERG Inputs · IR Team Handoff · Scenario Checklists · Evidence and Recovery Support

---

| | |
|---|---|
| **Document ID** | CERG-PRC-IR-002 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [`CERG-STD-MSG-001`](CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md) · [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| **Review Cycle** | Annual / After significant incident or IR plan change |
| **Frameworks** | [NIST 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (IR, AU, SI, CP) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (RESPOND, RECOVER) |
| **Regulations** | CMMC L2 / 800-171r3 · NERC-CIP · SOX ITGC · breach notification and contractual obligations where applicable |
| **Environments** | CERG-facing support to incidents affecting CERG-managed systems, controls, data, and evidence |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Ownership Boundary](#2-ownership-boundary)
3. [Common Playbook Structure](#3-common-playbook-structure)
4. [Playbook 1: Ransomware](#4-playbook-1-ransomware)
5. [Playbook 2: Business Email Compromise](#5-playbook-2-business-email-compromise)
6. [Playbook 3: Data Breach or Exfiltration](#6-playbook-3-data-breach-or-exfiltration)
7. [Playbook 4: Phishing Campaign](#7-playbook-4-phishing-campaign)
8. [Playbook 5: Distributed Denial of Service](#8-playbook-5-distributed-denial-of-service)
9. [Playbook 6: Insider Threat](#9-playbook-6-insider-threat)
10. [Playbook 7: Cloud Account Compromise](#10-playbook-7-cloud-account-compromise)
11. [Post-Incident CERG Actions](#11-post-incident-cerg-actions)
12. [Roles and Responsibilities](#12-roles-and-responsibilities)
13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Scope

[`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) establishes the Incident Response Plan. [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4 states that incident response is owned by a standing Incident Response team, not by CERG. That boundary is correct and must remain. At the same time, CERG owns many controls, records, and technical inputs the Incident Response team needs during an incident.

This document provides CERG-facing incident playbooks: what CERG prepares, what CERG hands to the Incident Response team, what CERG supports during containment, eradication, recovery, communications, and evidence preservation, and what CERG does after the incident to turn lessons into risks, controls, and evidence.

This is not a SOC procedure, forensics manual, or replacement Incident Response Plan. It is a support and handoff playbook set for CERG-managed systems and controls.

> **CERG Does Not Command the Incident. CERG Makes the Incident Runnable.**
>
> During an active incident, the Incident Commander commands. CERG does not create a parallel command structure. CERG brings the material the Incident Response team needs: asset context, data classification, control evidence, logging posture, recovery dependencies, risk history, vendor context, and the owners who can change the environment safely. The boundary is simple: the IR team runs the incident; CERG makes sure the IR team is not guessing.

---

## 2. Ownership Boundary

| **Area** | **Owner** | **CERG Role** |
|---|---|---|
| Incident declaration and severity | Incident Commander | Informed and consulted. |
| Tactical containment, eradication, and recovery direction | Incident Commander | Supports with Engineering and Risk expertise. |
| Forensic investigation | Lead Investigator | Supports with logs, asset data, and control context. |
| Legal, privacy, customer, and regulator notification decisions | Incident Commander with legal and executive process | Governance supplies data classification, scope, evidence, and regulatory mapping. |
| Detection content and telemetry readiness | Detection Engineer under CERG standards | Supplies and improves signals before and after incident. |
| Post-incident risk and control remediation | CERG | Records risks, updates controls, tracks remediation. |

CERG may author and maintain this playbook set, but scenario execution during an active incident is under the Incident Commander.

---

## 3. Common Playbook Structure

Each scenario uses the same structure so teams can move quickly.

| **Phase** | **CERG Support Question** |
|---|---|
| Triage | What do we know, what systems and data are involved, and what evidence must be preserved now? |
| Containment | What control changes, access restrictions, network actions, or vendor actions can safely limit spread? |
| Eradication | What root cause, vulnerability, misconfiguration, credential, or malicious artifact must be removed? |
| Recovery | What dependencies, backups, baselines, and validation are required before restoring service? |
| Communications | What technical, regulatory, customer, and executive facts can CERG supply? |
| Evidence | What logs, approvals, configurations, decisions, and artifacts must be preserved? |

---

## 4. Playbook 1: Ransomware

### 4.1 Triage

CERG supports the Incident Response team by rapidly identifying:

- affected assets and asset owners from the inventory;
- criticality and recovery priority from [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md);
- data classification and regulated data exposure from [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md);
- backup status and last known good recovery point from [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md);
- identity paths and privileged sessions that may be involved;
- relevant vulnerabilities, open risks, or exceptions.

### 4.2 Containment

CERG-supported containment may include: disabling compromised identities, isolating affected network segments or endpoints, blocking command-and-control indicators, freezing risky privileged access, pausing affected automation, and preserving backup systems from contamination.

### 4.3 Eradication and Recovery

CERG supports eradication by identifying the likely control failure: exposed remote access, missing MFA, vulnerable service, endpoint control gap, credential theft, misconfiguration, or vendor path. Recovery support includes baseline validation, restore validation, vulnerability remediation, and logging confirmation before production return.

### 4.4 Evidence and Communications Inputs

CERG preserves asset inventory snapshots, backup evidence, affected-data classification, security-control status, risk-register history, exception history, and relevant logs. Governance supplies regulatory mapping and evidence for customer, regulator, or executive communication.

---

## 5. Playbook 2: Business Email Compromise

### 5.1 Triage

CERG identifies the compromised mailbox or identity, MFA status, sign-in history, mailbox rules, forwarding rules, suspicious OAuth grants, sent mail volume, external recipients, and whether payments, regulated data, or executive impersonation are involved.

### 5.2 Containment

CERG support may include: disabling the account, revoking sessions and tokens, removing malicious mailbox rules, disabling external forwarding, resetting credentials, blocking indicators, quarantining related messages, and identifying other recipients or compromised accounts.

### 5.3 Eradication and Recovery

CERG validates that the mailbox, identity, OAuth grants, rules, and recovery methods are clean before returning access. Email and messaging control gaps are tracked under [`CERG-STD-MSG-001`](CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md).

### 5.4 Evidence and Communications Inputs

CERG preserves sign-in logs, mailbox audit logs, message traces, rule changes, MFA status, external forwarding evidence, DLP alerts, and related risk or exception records. Governance supplies SOX, privacy, and customer-scope implications where relevant.

---

## 6. Playbook 3: Data Breach or Exfiltration

### 6.1 Triage

CERG determines what data may be involved, its classification, the affected systems, the likely exfiltration path, volume, time window, data owner, and regulated or contractual obligations. Restricted data, CUI, BES Cyber System Information, personal data, and financial reporting data receive immediate Governance involvement.

### 6.2 Containment

Containment may include blocking exfiltration paths, disabling identities, revoking vendor access, suspending risky integrations, enforcing DLP blocks, rotating exposed secrets, and isolating affected repositories or storage locations.

### 6.3 Eradication and Recovery

CERG identifies and remediates the control gap: access failure, DLP failure, storage exposure, vendor path, compromised credential, misconfiguration, or logging gap. Recovery includes validating access, storage, DLP, and monitoring controls before normal operations resume.

### 6.4 Evidence and Communications Inputs

CERG preserves data classification records, data-owner confirmation, access logs, DLP events, storage configuration, vendor access logs, risk-register entries, and evidence of containment actions.

---

## 7. Playbook 4: Phishing Campaign

### 7.1 Triage

CERG identifies reported messages, sender infrastructure, subject and lure, affected users, clicked users, credential submissions, malicious links or attachments, and whether the campaign targets executives, privileged users, finance, or regulated environments.

### 7.2 Containment

Containment may include message purge, URL or attachment blocking, credential resets, session revocation, OAuth grant removal, mailbox rule review, and user notification. Employee reporting remains blame-free under [`CERG-STD-MSG-001`](CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md).

### 7.3 Eradication and Recovery

CERG supports control tuning: email filtering, DMARC/SPF/DKIM review, user-reporting workflow, DLP, mailbox auditing, and detection content. If the phish leads to account compromise, Playbook 2 also applies.

### 7.4 Evidence and Communications Inputs

CERG preserves reported messages, message trace, user-report timestamps, click and submission evidence, containment actions, and affected-account actions.

---

## 8. Playbook 5: Distributed Denial of Service

### 8.1 Triage

CERG identifies affected services, customer or operational impact, upstream providers, DDoS protection status, network paths, service dependencies, and whether the incident masks another attack.

### 8.2 Containment

Containment support may include activating DDoS protection, coordinating with providers, changing routing or filtering, scaling resilient services, protecting management interfaces, and preserving logs showing attack characteristics.

### 8.3 Eradication and Recovery

DDoS is rarely eradicated in the traditional sense. CERG supports service restoration, resilience validation, provider review, and permanent control improvements after the attack subsides.

### 8.4 Evidence and Communications Inputs

CERG preserves traffic metrics, provider tickets, protection activation evidence, affected-service timelines, customer-impact timeline, and recovery evidence.

---

## 9. Playbook 6: Insider Threat

### 9.1 Triage

CERG supports the Incident Response team carefully and discreetly. Triage identifies affected systems, data classification, access history, anomalous behavior, DLP events, privileged activity, and risk to investigation integrity. Access to information is strictly need-to-know.

### 9.2 Containment

Containment may include access suspension, privilege reduction, session revocation, monitoring preservation, device preservation, and targeted control changes. Actions are coordinated with the Incident Commander and appropriate legal, HR, or executive process outside CERG.

### 9.3 Eradication and Recovery

CERG identifies control improvements: access review gaps, segregation-of-duties gaps, logging gaps, DLP gaps, privileged access gaps, or data governance failures. Recovery may include access recertification and control strengthening.

### 9.4 Evidence and Communications Inputs

CERG preserves access logs, DLP events, privileged activity, data classification, asset ownership, risk records, and evidence-chain notes as directed by the Incident Commander and Lead Investigator.

---

## 10. Playbook 7: Cloud Account Compromise

### 10.1 Triage

CERG identifies the affected tenant, account, subscription, project, workload, identity, access keys, service principals, secrets, exposed data, privilege level, and recent control-plane activity. Cloud account compromise is treated as both identity and platform compromise.

### 10.2 Containment

Containment may include disabling or isolating identities, revoking sessions, rotating keys and secrets, blocking suspicious IPs, quarantining workloads, snapshotting evidence, disabling risky automation, and preserving control-plane logs.

### 10.3 Eradication and Recovery

CERG identifies the root path: credential theft, exposed secret, misconfigured federation, over-privileged role, vulnerable workload, or malicious OAuth or service principal. Recovery requires validation of IAM, logging, network controls, baseline conformance, and secrets rotation.

### 10.4 Evidence and Communications Inputs

CERG preserves cloud audit logs, IAM history, key and secret rotation records, workload inventory, network flows, storage access logs, risk-register records, and affected-data classification.

---

## 11. Post-Incident CERG Actions

After the Incident Commander closes active response, CERG completes its own post-incident work.

| **Action** | **Owner** | **Purpose** |
|---|---|---|
| Record residual risk | Risk Register Owner | Ensure unresolved exposure is tracked. |
| Update controls or standards | Policy & Standards Manager with relevant owner | Close program gaps revealed by the incident. |
| Update baselines | Relevant Engineering role | Prevent recurrence through configuration or architecture change. |
| Update detection and logging requirements | Detection Engineer | Improve observability and alerting where in scope. |
| Update evidence library | Evidence Librarian | Preserve incident-relevant control and response evidence. |
| Review vendor or third-party implications | Vendor Risk Analyst | Reassess suppliers or integrations involved. |
| Report material lessons | Governance Pillar Leader | Feed metrics, CISO reporting, and oversight. |

---

## 12. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Playbook Responsibility** |
|---|---|
| **Incident Commander** | Commands the active incident. Owns tactical incident decisions. |
| **Lead Investigator** | Leads investigation and evidence direction during active response. |
| **Governance Pillar Leader** | Owns this CERG-facing playbook set; supplies regulatory, evidence, and reporting support. |
| **Risk Pillar Leader** | Coordinates Cyber Risk support and post-incident risk capture. |
| **Engineering Pillar Leader** | Coordinates Cyber Engineering support and technical control changes. |
| **Detection Engineer** | Supplies telemetry context and post-incident detection improvements where in scope. |
| **Risk Register Owner** | Records residual risks and post-incident risk entries. |
| **Evidence Librarian** | Preserves CERG evidence and submitted incident support material. |
| **Cloud Security Engineer** | Supports cloud, SaaS, email, and platform incidents. |
| **Identity Engineer** | Supports identity, privilege, token, session, and account-containment actions. |
| **Endpoint Engineer** | Supports endpoint isolation and recovery where needed. |
| **Cryptography Engineer** | Supports key, certificate, token, and secret rotation. |
| **Vendor Risk Analyst** | Supports vendor and third-party implications. |
| **CMMC / Federal Compliance Manager** | Supports CUI and federal implications. |
| **NERC-CIP Compliance Manager** | Supports NERC-CIP implications. |
| **SOX ITGC Lead** | Supports SOX ITGC implications. |
| **Chief Information Security Officer (CISO)** | Receives material incident briefings and risk escalations. |

---

## 13. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Playbook Set** |
|---|---|---|
| NIST 800-61r2 | Preparation, detection and analysis, containment, eradication, recovery, post-incident activity | Sections 3 through 11 |
| NIST 800-53r5 | IR, AU, SI, CP families | Sections 3 through 11 |
| NIST CSF 2.0 | RESPOND and RECOVER | Sections 4 through 11 |
| CMMC L2 / NIST 800-171r3 | Incident response and CUI handling implications | Sections 6, 11, 12 |
| NERC-CIP | Incident and BES Cyber System implications | Sections 6, 11, 12 |
| SOX ITGC | Evidence, access, and change implications for financial systems | Sections 5, 11, 12 |

---

## 14. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-IR-002 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO (pending); Incident Commander owner concurrence required |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and after significant incident or IR plan change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-61r2; NIST 800-53r5 (IR, AU, SI, CP); NIST CSF 2.0 (RESPOND, RECOVER) |
| **Regulations** | CMMC L2 / 800-171r3; NERC-CIP; SOX ITGC; breach notification and contractual obligations where applicable |
| **Environments** | CERG-facing support to incidents affecting CERG-managed systems, controls, data, and evidence |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes CERG-facing incident playbooks for ransomware, business email compromise, data breach or exfiltration, phishing campaign, distributed denial of service, insider threat, and cloud account compromise. Preserves the Operating Model boundary that the standing Incident Response team owns active incident command while CERG supplies control, evidence, risk, and recovery support. |

### Review Triggers

- Significant incident or exercise finding
- Change to [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md)
- Material change to logging, resilience, data governance, email, or cloud security standards
- Change to legal, regulatory, or contractual incident-notification obligations
- Direction from the CISO or Incident Commander

Cyber Governance owns this CERG-facing playbook set. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval and Incident Commander owner concurrence for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines IR ownership boundary and adjacent roles |
| Incident Response Plan | [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) | Active incident response plan owned by the IR team |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Telemetry and detection support |
| Email and Messaging Security Standard | [`CERG-STD-MSG-001`](CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md) | Email, phishing, BEC, and messaging controls |
| Cyber Resilience and Backup Standard | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Recovery and backup support |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Data classification and handling support |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Post-incident residual risk tracking |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence preservation and audit support |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |
