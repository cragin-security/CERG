
# SURGE: Cyber Engineering, Risk & Governance

## ASSET MANAGEMENT AND INVENTORY STANDARD
### Authoritative Inventory · Asset Classes · Ownership · Classification · Lifecycle · End-of-Life

---

| | |
|---|---|
| **Document ID** | CERG-STD-AM-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Review Cycle** | Annual / On material change to the asset estate or inventory tooling |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.AM) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CM-8, PM-5) · [CIS Controls v8](https://www.cisecurity.org/controls) (Controls 1 and 2) · ISO/IEC 27001 A.5.9 |
| **Regulations** | NERC-CIP (CIP-002 BES Cyber System identification) · CMMC L2 / 800-171r3 (3.4.1, 3.4.2) · SOX ITGC (in-scope system inventory) |
| **Environments** | All in-scope assets: owned, hybrid, cloud, SaaS, OT, and CUI |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Asset Classes](#3-asset-classes)
4. [The Authoritative Inventory](#4-the-authoritative-inventory)
5. [Required Attributes](#5-required-attributes)
6. [Asset Ownership](#6-asset-ownership)
7. [Asset Criticality and Classification](#7-asset-criticality-and-classification)
8. [The Asset Lifecycle](#8-the-asset-lifecycle)
9. [End-of-Life and Secure Disposal](#9-end-of-life-and-secure-disposal)
10. [Inventory Accuracy and Reconciliation](#10-inventory-accuracy-and-reconciliation)
11. [Roles and Responsibilities](#11-roles-and-responsibilities)
12. [Regulatory and Framework Alignment Summary](#12-regulatory-and-framework-alignment-summary)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

Every other control in CERG assumes the program knows what it is protecting. Vulnerability management scans an asset list. Access management governs access to systems. The control baseline maps evidence to assets. Logging collects from sources. Each of those depends on an authoritative answer to a deceptively simple question: what do we have? Until this standard, CERG had no document that owned that question.

This standard establishes the requirement for an authoritative asset inventory: the asset classes that must be tracked, the inventory itself, the attributes every asset record carries, how ownership is assigned, how assets are classified by criticality, and how assets move through a lifecycle from acquisition to secure disposal.

It applies to every in-scope asset across every environment: owned hardware, cloud and hybrid infrastructure, SaaS, operational technology, and the data assets the rest of the estate exists to serve.

> **You Cannot Protect, Detect, or Recover What You Have Not Named**
>
> An unknown asset is an uncontrolled asset. It is not patched, because vulnerability management does not know it exists. Its access is not reviewed, because access management has no record of it. It is not backed up, monitored, or hardened. Asset management is not paperwork; it is the precondition for every other thing CERG does. This is why NIST CSF places asset management first, in the IDENTIFY function, and why CIS makes it Control 1.

---

## 2. Principles

1. **One authoritative inventory.** There is exactly one authoritative source for each asset class. Spreadsheets maintained in parallel are not the inventory. Where multiple tools hold asset data, one is named authoritative and the others reconcile to it.
2. **Every asset has exactly one owner.** Ambiguous ownership is the root cause CERG exists to remove. An asset with no owner, or two owners, is a finding.
3. **The inventory is current, not annual.** An inventory that is accurate once a year is inaccurate the other 364 days. The inventory updates as assets change, driven by automation wherever possible.
4. **Discovery is continuous.** The program actively looks for assets it does not know about. An inventory built only from what teams choose to register will always be incomplete.
5. **Classification drives treatment.** An asset's criticality and data classification determine the controls applied to it. Asset management produces the classification; the other standards consume it.
6. **Disposal is part of the lifecycle.** An asset is tracked until it is securely disposed of, not until it stops being interesting. Forgotten assets at end-of-life are a common breach path.

---

## 3. Asset Classes

CERG tracks five asset classes. Each has a named authoritative inventory.

| **Class** | **What It Covers** | **Examples** |
|---|---|---|
| **Hardware** | Physical computing and network devices. | Servers, workstations, laptops, network gear, mobile devices, OT field devices. |
| **Software** | Operating systems, applications, and firmware in use. | OS images, installed applications, in-house software per [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md), firmware versions. |
| **Cloud and SaaS** | Cloud infrastructure resources and subscribed SaaS services. | Cloud compute, storage, managed services, accounts and subscriptions, SaaS tenants. |
| **Data** | Information assets, governed for classification and handling. | Datasets, databases, document repositories. Handling is governed by [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) (Planned, V1.x). |
| **Identity** | Accounts and service principals that act on the estate. | User accounts, service accounts, machine identities, API principals. Governed by [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md); inventoried here. |

> **OT Assets Are In Scope and Need Care**
>
> Operational technology assets are tracked like every other asset, but discovery against OT is constrained: active scanning can disrupt control systems. OT asset discovery uses passive and OT-safe methods per [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md). The requirement to inventory OT assets is identical to any other class. The method of discovery is not. For NERC-CIP entities, the OT hardware inventory is also the basis of BES Cyber System identification under CIP-002.

---

## 4. The Authoritative Inventory

1. **Each asset class has one named authoritative inventory.** The authoritative inventory for each class is recorded, with its owner, in the organization profile or an organization-specific appendix to this standard.
2. **The inventory is a system, not a document.** For any estate beyond the smallest, the inventory is a tooled system fed by automated discovery, not a hand-maintained file. A five-person team may start with a structured file; it migrates to tooling as the estate grows.
3. **Inventories interconnect.** A software record references the hardware or cloud asset it runs on. A data asset references the system that hosts it. An identity references what it can access. The inventory is a graph, not five disconnected lists.
4. **The inventory feeds the program.** The inventory is the source list for vulnerability management scanning, the access-review population, the logging source catalog, and the control-baseline evidence mapping. Those consumers reconcile to the inventory; they do not maintain their own.

---

## 5. Required Attributes

Every asset record, regardless of class, carries the following attributes at minimum. An asset record missing a required attribute is incomplete and is a reconciliation finding.

| **Attribute** | **Meaning** |
|---|---|
| Asset identifier | A unique, stable identifier for the asset. |
| Asset class | One of the five classes in Section 3. |
| Description | What the asset is, in plain language. |
| Owner | The single accountable owner, per Section 6. |
| Custodian | The team or role operating the asset day to day, where different from the owner. |
| Environment | Owned, hybrid, cloud, SaaS, OT, or CUI. |
| Criticality | The criticality tier, per Section 7. |
| Data classification | The highest classification of data the asset stores or processes. |
| Lifecycle state | The current state, per Section 8. |
| Location | Physical site, cloud region, or logical placement. |
| Acquisition date | When the asset entered the estate. |
| Last verified | When the record was last confirmed accurate, per Section 10. |

Regulated scopes carry additional attributes: NERC-CIP assets carry their BES Cyber System categorization; CUI assets carry their CUI category. Those overlays are defined in the relevant operational package.

---

## 6. Asset Ownership

1. **Every asset has exactly one owner.** The owner is a named role accountable for the asset's security posture, its classification, and decisions about its lifecycle. The owner is not necessarily the person who operates it.
2. **Ownership is assigned at acquisition.** An asset does not enter the estate without an owner. The acquisition step of the lifecycle (Section 8) does not complete until ownership is recorded.
3. **Ownership is reassigned, never dropped.** When an owner leaves a role, the asset's ownership transfers to a named successor. An asset whose owner has left and has no successor is an orphaned asset and is a finding.
4. **The custodian is distinct from the owner.** A cloud platform team may operate a server an application team owns. The inventory records both. The owner decides; the custodian runs.

> **An Orphaned Asset Is How Programs Get Breached**
>
> The asset no one owns is the asset no one patches, no one reviews, and no one decommissions. It runs an unsupported operating system for three years because removing it is no one's job. Orphaned assets are found in nearly every significant breach retrospective. CERG treats an asset with no current owner as an open finding, tracked in the risk register until ownership is restored.

---

## 7. Asset Criticality and Classification

### 7.1 Criticality Tiers

Every asset is assigned a criticality tier. Criticality reflects the business and safety impact if the asset is compromised or unavailable.

| **Tier** | **Definition** |
|---|---|
| **Critical** | Compromise or loss causes severe business, safety, regulatory, or financial impact. Includes BES Cyber Systems, SOX-relevant financial systems, and systems processing regulated data. |
| **High** | Compromise or loss causes significant impact to a major business function. |
| **Moderate** | Compromise or loss causes limited, contained impact. |
| **Low** | Compromise or loss causes negligible impact. |

### 7.2 Data Classification

Every asset carries the classification of the highest-classified data it stores or processes. The classification scheme itself is owned by [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) (Planned, V1.x). Until that standard is published, assets carry the data classification used by [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md) for CUI scope and a simple internal scheme elsewhere.

### 7.3 What Classification Drives

The criticality tier and data classification of an asset determine, at minimum: its vulnerability remediation SLA under [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md), its access-review frequency under [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md), its logging requirements under [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), and its backup and recovery objectives under [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md). Asset management produces the classification once; every other standard consumes it.

---

## 8. The Asset Lifecycle

Every asset moves through a defined lifecycle. The inventory records the asset's current state.

| **State** | **What Happens** | **Security Requirement** |
|---|---|---|
| **Requested** | Acquisition is proposed. | Intake through [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) where the asset is part of a project. |
| **Acquired** | The asset enters the estate. | Inventory record created; owner assigned; criticality and classification set. |
| **Provisioned** | The asset is configured for use. | Secure configuration baseline applied per [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md). |
| **Operational** | The asset is in service. | Subject to vulnerability management, access review, logging, and backup per its classification. |
| **Decommissioning** | The asset is being retired. | Data securely removed; access revoked; dependencies migrated. |
| **Disposed** | The asset has left the estate. | Secure disposal completed per Section 9; record retained for audit. |

An asset record is never deleted. A disposed asset is marked Disposed and retained, so the inventory carries a complete history for audit.

---

## 9. End-of-Life and Secure Disposal

1. **End-of-life is planned, not discovered.** An asset approaching the end of vendor support is identified before support ends, and a replacement or extended-support decision is made deliberately. An asset running past end-of-support with no decision recorded is a finding and a risk register entry.
2. **Data is removed before disposal.** Before an asset leaves the estate, data on it is securely sanitized to a standard appropriate to the data's classification. Cryptographic erasure per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) is acceptable where keys can be destroyed; physical destruction is used where it cannot.
3. **Access and identity are revoked.** Decommissioning includes revoking the asset's own credentials and any access granted to it, per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md).
4. **Disposal is evidenced.** Secure disposal produces a record: what asset, what sanitization method, when, and by whom. The record is retained as control evidence. For regulated assets, the disposal record is part of the regulatory evidence set.
5. **Cloud and SaaS disposal counts.** Decommissioning a cloud resource or terminating a SaaS tenant is disposal. Data deletion, key destruction, and confirmation of tenant closure are required exactly as for physical hardware.

---

## 10. Inventory Accuracy and Reconciliation

An inventory is only as useful as it is accurate. Accuracy is maintained, not assumed.

1. **Continuous discovery runs against every environment.** Automated discovery identifies assets and compares them to the inventory. An asset found by discovery but absent from the inventory is an unmanaged asset and is investigated.
2. **Reconciliation runs on a defined cadence.** The inventory is reconciled against discovery output, against the consuming systems (vulnerability scanner, access platform, logging catalog), and against procurement records. Discrepancies are findings.
3. **An unmanaged asset is contained.** An asset discovered outside the inventory is either brought under management (owner assigned, baseline applied, record created) or removed from the estate. It is not left in an unknown state.
4. **Inventory completeness is a reported metric.** The percentage of the estate under management, and the count of unmanaged assets found, are reported per [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md). A program that does not measure its inventory accuracy does not know it has one.

> **The Inventory You Do Not Reconcile Is a Guess**
>
> Every inventory drifts. Assets are spun up outside process, shadow SaaS is subscribed with a credit card, a contractor leaves a virtual machine running. An inventory that is not actively reconciled against independent discovery slowly becomes fiction while still being trusted as fact, which is worse than having no inventory at all. Reconciliation is what keeps the inventory honest.

---

## 11. Roles and Responsibilities

Roles below are the canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Asset Management Responsibility** |
|---|---|
| **Engineering Pillar Leader** | Owns this standard. Accountable for the authoritative inventories and for continuous discovery across environments. |
| **Cloud Security Engineer** | Owns discovery and inventory accuracy for the cloud and SaaS asset class. |
| **OT Security Engineer** | Owns OT-safe discovery and inventory accuracy for OT hardware; supports BES Cyber System identification. |
| **Endpoint Engineer** | Owns inventory accuracy for endpoint hardware and software. |
| **Identity Engineer** | Owns the identity asset class inventory, in coordination with [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md). |
| **Asset Owners** | Named per asset. Accountable for their asset's posture, classification, lifecycle decisions, and end-of-life planning. |
| **Vulnerability Management Lead** | Consumes the inventory as the scan population; reports inventory gaps found during scanning. |
| **Governance Pillar Leader** | Tracks inventory-completeness metrics; cross-references this standard with the control baseline; tracks orphaned and end-of-life assets in the risk register. |
| **Policy & Standards Manager** | Maintains this document, its version, and its review cycle. |

---

## 12. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Standard** |
|---|---|---|
| NIST CSF 2.0 | ID.AM-01 through ID.AM-08 | Sections 3, 4, 5, 7, 8 |
| NIST 800-53r5 | CM-8 (system component inventory), PM-5 (system inventory), MP-6 (media sanitization) | Sections 4, 5, 9 |
| CIS Controls v8 | Control 1 (enterprise assets), Control 2 (software assets) | Sections 3, 4, 10 |
| ISO/IEC 27001 | A.5.9 (inventory of information and assets), A.5.11 (return of assets) | Sections 4, 9 |
| NERC-CIP | CIP-002 (BES Cyber System categorization) | Sections 3, 7 |
| NIST 800-171r3 / CMMC L2 | 3.4.1, 3.4.2 (baseline configuration and inventory) | Sections 4, 5 |
| SOX ITGC | In-scope system inventory | Sections 4, 7 |

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-AM-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Approved By** | Governance Pillar Leader; CISO endorses |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to the asset estate or inventory tooling |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST CSF 2.0 (ID.AM); NIST 800-53r5 (CM-8, PM-5, MP-6); CIS Controls v8 (1, 2); ISO/IEC 27001 A.5 |
| **Regulations** | NERC-CIP (CIP-002); CMMC L2 / 800-171r3; SOX ITGC |
| **Environments** | All in-scope assets |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-21 | Cyber Engineering | Initial release. Establishes the five asset classes, the authoritative inventory requirement, required asset attributes, single-owner asset ownership, criticality and data classification, the six-state asset lifecycle, end-of-life and secure disposal requirements, and continuous discovery with reconciliation. |

### Review Triggers

- Material change to the asset estate, environments, or inventory tooling
- Publication of the Data Governance and Classification Standard, which sets the classification scheme
- Revision of NIST CSF, CIS Controls, or NERC-CIP CIP-002
- Internal audit or regulatory finding affecting asset inventory
- Direction from the CISO

Cyber Engineering owns this document. The Engineering Pillar Leader (Platforms) is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Secure Configuration Baseline Standard (DISH) | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Baselines applied at the Provisioned lifecycle state |
| IT / Cloud / SaaS Security Standard | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Cloud and SaaS asset controls |
| Grid Control Systems Security Standard | [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | OT-safe discovery; BES Cyber System identification |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Identity asset class; access revocation at disposal |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Inventory feeds the logging source catalog |
| Cyber Resilience and Backup Standard | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Classification drives backup and recovery objectives |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Cryptographic erasure at disposal |
| Vulnerability Management Procedure | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | Inventory is the scan population |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Intake at the Requested lifecycle state |
| Metrics, Dashboard, and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Inventory-completeness reporting |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `AM` domain |
