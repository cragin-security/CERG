## DATA GOVERNANCE AND CLASSIFICATION STANDARD
### Classification Scheme · Labeling · Handling · Retention · Data Loss Prevention · Data Lifecycle

---

| | |
|---|---|
| **Document ID** | CERG-STD-DG-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Review Cycle** | Annual / On material change to data handling obligations |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (MP, SC-28, AC families) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.AM, PR.DS) · ISO/IEC 27001 A.5.12, A.5.13 · [CIS Controls v8](https://www.cisecurity.org/controls) (Control 3) |
| **Regulations** | CMMC L2 / 800-171r3 (CUI) · SOX ITGC (financial data) · NERC-CIP (BES Cyber System Information) · privacy regimes where applicable |
| **Environments** | All in-scope environments and all data CERG-managed systems store, process, or transmit |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [The Classification Scheme](#3-the-classification-scheme)
4. [Classifying Data](#4-classifying-data)
5. [Labeling](#5-labeling)
6. [Handling Requirements by Classification](#6-handling-requirements-by-classification)
7. [The Data Lifecycle](#7-the-data-lifecycle)
8. [Retention and Disposal](#8-retention-and-disposal)
9. [Data Loss Prevention](#9-data-loss-prevention)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

CERG protects data. Every other standard is, in the end, in service of keeping the right data confidential, intact, and available. Yet the program has had no general scheme for saying how sensitive a given piece of data is. The CUI Handling Standard governs one specific regulated category exhaustively; nothing governed the rest. The Asset Management Standard requires every asset to carry a data classification but pointed at a scheme that did not yet exist. This standard is that scheme.

This standard establishes the general data governance framework for CERG: the classification scheme, how data is classified and labeled, the handling requirements each classification carries, the data lifecycle, retention and disposal, and data loss prevention.

It applies to all data CERG-managed systems store, process, or transmit, in every environment. It does not replace [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md); CUI is a regulated category with its own exhaustive handling rules, and where data is CUI, the CUI standard governs. This standard provides the general scheme into which CUI fits as the most restrictive category.

> **Classification Is Not About Labels. It Is About Treatment.**
>
> A classification scheme that produces labels and nothing else is a filing exercise. The point of classifying data is that the classification decides how the data is treated: who may access it, whether it is encrypted, how it is backed up, how long it is kept, and what happens if someone tries to send it outside. Section 6 is the part of this standard that matters. The scheme in Section 3 exists to drive it.

---

## 2. Principles

1. **All data has a classification.** Data is classified, explicitly or by a sensible default. Unclassified data is not a category; it is an unfinished task.
2. **Classify by impact.** Data's classification reflects the harm that would result from its unauthorized disclosure, alteration, or loss, not who created it or where it lives.
3. **The highest element sets the classification.** A collection of data carries the classification of the most sensitive element it contains. A report that mixes public figures with one Confidential number is Confidential.
4. **Classification drives treatment.** The classification is the input to access, encryption, backup, retention, and monitoring decisions in the other standards. This standard produces the classification once.
5. **Classification travels with the data.** When data is copied, exported, or moved, its classification and its handling requirements move with it. A copy is not a way to launder a classification away.
6. **Least data.** Data that is not collected cannot be breached. The program collects and retains the data it needs and disposes of data it no longer needs.

---

## 3. The Classification Scheme

CERG uses four classification levels. An organization adopting CERG may rename the levels to fit its own conventions through [`CERG-GOV-VAR-001`](../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md), but the four-level structure and its meaning are fixed.

| **Level** | **Definition** | **Examples** |
|---|---|---|
| **Public** | Disclosure causes no harm. Approved for release outside the organization. | Published marketing material, public filings, this document. |
| **Internal** | For use within the organization. Disclosure causes minor harm. The default for ordinary business data. | Internal procedures, routine internal email, non-sensitive project material. |
| **Confidential** | Disclosure causes significant harm to the organization, its people, or its partners. Access is limited to those with a need. | Financial data before release, contracts, personal data, security documentation, most regulated data. |
| **Restricted** | Disclosure causes severe harm. Access is tightly limited and individually justified. | CUI, BES Cyber System Information, secrets and keys, the most sensitive personal and legal data. |

> **Four Levels, Not Fourteen**
>
> The temptation in a classification scheme is to add levels until every shade of sensitivity has its own. A scheme with too many levels is one nobody can apply consistently, and an inconsistently applied scheme is worse than a coarse one. Four levels is enough to drive genuinely different treatment and few enough that every employee can learn them. Regulated categories like CUI are not new levels; they are Restricted data with additional handling rules layered on by their own standard.

---

## 4. Classifying Data

1. **The data owner classifies.** Every data asset has an owner, per [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md). The owner assigns the classification and is accountable for it being correct.
2. **Classify at creation.** Data is classified when it is created or acquired, not when someone later notices it is sensitive.
3. **The default is Internal.** Data created without an explicit classification is treated as Internal. The default is deliberately not Public; data is not exposed by omission. Data is not defaulted to Confidential either, because a default that over-classifies trains people to ignore the scheme.
4. **Regulated data is classified by its regime.** Data subject to a regulatory category, CUI, BES Cyber System Information, financial data in SOX scope, is classified at the level that regime requires, which is Confidential or Restricted, and handled additionally per the relevant standard or operational package.
5. **Reclassification is deliberate.** A classification changes only by a recorded decision of the data owner. Data is commonly declassified when it is approved for release, for example a financial figure once it is published. Lowering a classification is a decision, not a drift.

---

## 5. Labeling

1. **Confidential and Restricted data is labeled.** Data at the Confidential and Restricted levels carries a visible classification label wherever the format allows: document headers or footers, email subject or banner, dataset metadata.
2. **Internal and Public labeling is recommended, not required.** Labeling Internal and Public data is encouraged for clarity but not mandatory, so the labeling effort concentrates where it matters.
3. **Labels are machine-readable where possible.** Where the platform supports classification metadata, the label is applied as metadata, not only as visible text, so that data loss prevention (Section 9) and access controls can act on it.
4. **An unlabeled Confidential or Restricted item is a finding.** Discovering sensitive data with no label is a handling failure and is corrected.

---

## 6. Handling Requirements by Classification

This table is the operative core of the standard. It states the minimum handling for each classification. The other standards implement these requirements; this table is the single place they are stated together.

| **Handling Control** | **Public** | **Internal** | **Confidential** | **Restricted** |
|---|---|---|---|---|
| Access model | Open | All employees | Need-to-know, per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Individually justified, need-to-know |
| Encryption in transit | Recommended | Required | Required | Required |
| Encryption at rest | Optional | Recommended | Required | Required |
| Storage location | Any approved | Approved internal or managed cloud | Approved, access-controlled repositories only | Approved, access-controlled, and monitored repositories only |
| External sharing | Permitted | Approved business need | Approved, with recipient agreement and controls | Prohibited unless an explicit, recorded authorization exists |
| Removable media | Permitted | Permitted | Discouraged; encrypted if used | Prohibited unless an exception is recorded |
| Backup | Per asset class | Per asset class | Required, per [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Required, with recovery tested |
| Logging of access | Optional | Recommended | Required, per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Required, access logged and reviewable |
| Disposal | Standard | Standard | Secure disposal, evidenced | Secure disposal, evidenced, per [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) §9 |
| Data loss prevention | Not monitored | Monitored | Monitored and enforced | Monitored and enforced |

Encryption requirements are met using the algorithms and key management of [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md). Where a regulated category imposes a stricter requirement than this table, the stricter requirement governs.

---

## 7. The Data Lifecycle

Data moves through a lifecycle, and a handling requirement applies at each stage.

| **Stage** | **What Happens** | **Handling Requirement** |
|---|---|---|
| **Create or acquire** | Data is generated or received. | Classified per Section 4; labeled per Section 5. |
| **Store** | Data is held at rest. | Stored and encrypted per the Section 6 table for its classification. |
| **Use and process** | Data is accessed and worked with. | Accessed on a need-to-know basis; access logged per classification. |
| **Share and transmit** | Data moves between people, systems, or organizations. | Transmitted encrypted; external sharing constrained per Section 6; classification travels with it. |
| **Archive** | Data is retained but no longer in active use. | Retained per Section 8; access narrowed; still classified and protected. |
| **Dispose** | Data is destroyed at the end of retention. | Securely disposed per Section 8; disposal evidenced for Confidential and Restricted data. |

---

## 8. Retention and Disposal

1. **Data has a retention period.** Each category of data has a defined retention period, set by business need and by legal and regulatory obligation. The retention schedule is maintained by Governance.
2. **Retention is enforced.** Data is kept for its retention period and is disposed of at the end of it. Keeping data indefinitely "in case" is not a retention decision; it is the absence of one, and it grows the breach surface every year.
3. **Legal hold overrides retention.** Data subject to a legal hold is preserved regardless of its retention period until the hold is lifted. Legal hold is the one authorized reason to retain data past its schedule.
4. **Disposal is secure and evidenced.** Disposal of Confidential and Restricted data is secure, sanitization appropriate to the medium and classification, and produces a retained disposal record. Disposal of data assets is coordinated with asset disposal per [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) §9.
5. **Backups respect retention conceptually but follow their own cycle.** Backup copies follow the backup retention cycle in [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md). Where a regulation requires data to be provably destroyed everywhere, including backups, that requirement is handled through the relevant operational package.

> **Data You No Longer Need Is Pure Liability**
>
> Old data has all of the breach exposure and almost none of the value. The customer records from a system retired six years ago cannot help the business, but they can absolutely be stolen. Retention discipline is one of the few security controls that reduces risk and reduces cost at the same time, because storing less data costs less and exposes less. CERG treats indefinite retention as a finding, not a safe default.

---

## 9. Data Loss Prevention

1. **DLP monitors Confidential and Restricted data.** Data loss prevention monitors for Confidential and Restricted data moving in ways its classification does not permit: leaving the organization by email, upload, or removable media.
2. **DLP enforces, it does not only observe.** For Confidential and Restricted data, DLP blocks or quarantines unauthorized movement, not merely logs it after the fact.
3. **DLP uses the classification labels.** DLP acts on the machine-readable labels from Section 5 and on content inspection. This is why labeling sensitive data is required, not optional.
4. **DLP events are detection signals.** A DLP block or alert is a signal delivered to the detection platform per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md). A pattern of DLP events involving one user or one dataset is investigated.
5. **DLP coverage spans the data paths.** DLP covers the realistic exfiltration paths for the estate: email, web upload, cloud storage sync, and removable media. Coverage gaps are recorded as accepted risk until closed.

---

## 10. Roles and Responsibilities

Roles below are the canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Data Governance Responsibility** |
|---|---|
| **Governance Pillar Leader** | Owns this standard. Owns the classification scheme, the retention schedule, and the handling-requirements table. |
| **Policy & Standards Manager** | Maintains this document; maintains the retention schedule; coordinates labeling guidance. |
| **Asset Owners** | Classify the data assets they own; assign and maintain the classification; make reclassification decisions. |
| **Identity Engineer** | Implements need-to-know access for Confidential and Restricted data per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md). |
| **Cloud Security Engineer** | Implements DLP on cloud and SaaS data paths; enforces approved storage locations. |
| **Endpoint Engineer** | Implements DLP and removable-media control on endpoints per [`CERG-STD-EP-001`](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md). |
| **Cryptography Engineer** | Provides the encryption that the handling table requires. |
| **Detection Engineer** | Owns detection content for DLP events and anomalous data access. |
| **CMMC / Federal Compliance Manager** | Ensures CUI, as Restricted data, is also handled per [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md). |
| **Evidence Librarian** | Retains disposal records and classification evidence for audit. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Standard** |
|---|---|---|
| NIST 800-53r5 | RA-2 (security categorization), MP family (media protection), SC-28 (protection at rest), AC-3, AC-21 | Sections 3, 6, 8 |
| NIST CSF 2.0 | ID.AM-05 (data classification), PR.DS (data security) | Sections 3, 6, 7 |
| ISO/IEC 27001 | A.5.12 (classification of information), A.5.13 (labelling), A.5.14 (information transfer) | Sections 3, 5, 6 |
| CIS Controls v8 | Control 3 (data protection) | Sections 6, 8, 9 |
| NIST 800-171r3 / CMMC L2 | CUI as Restricted data; media protection 3.8.x | Sections 3, 6 |
| SOX ITGC | Financial data confidentiality and retention | Sections 6, 8 |
| NERC-CIP | BES Cyber System Information as Restricted data | Sections 3, 6 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-DG-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to data handling obligations |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST 800-53r5 (MP, SC-28, AC); NIST CSF 2.0 (ID.AM, PR.DS); ISO/IEC 27001 A.5; CIS Controls v8 (3) |
| **Regulations** | CMMC L2 / 800-171r3; SOX ITGC; NERC-CIP; privacy regimes where applicable |
| **Environments** | All in-scope environments and data |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-21 | Cyber Governance | Initial release. Establishes the four-level classification scheme, how data is classified and labeled, the handling-requirements table that drives treatment across the other standards, the data lifecycle, retention and disposal with indefinite retention treated as a finding, and data loss prevention. Provides the general classification scheme that CERG-STD-AM-001 and CERG-STD-CUI-001 reference. |

### Review Triggers

- New or changed regulatory data-handling obligation
- Revision of relevant NIST or ISO data-protection guidance
- A significant data-loss or data-exposure incident
- Internal audit or regulatory finding affecting data governance
- Direction from the CISO

Cyber Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CUI Handling Standard | [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md) | CUI is Restricted data with additional regulated handling |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Assets carry the classification this standard defines; data assets and disposal |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Need-to-know access for Confidential and Restricted data |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Encryption that the handling table requires |
| Cyber Resilience and Backup Standard | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Backup of Confidential and Restricted data |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Access logging and DLP detection content |
| Endpoint and Mobile Security Standard | [`CERG-STD-EP-001`](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) | Endpoint DLP and removable-media control |
| Organization Adaptation Profile | [`CERG-GOV-VAR-001`](../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Adopter may rename the classification levels |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `DG` domain |
