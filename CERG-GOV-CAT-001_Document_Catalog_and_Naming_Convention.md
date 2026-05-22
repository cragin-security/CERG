
# SURGE: Cyber Engineering, Risk & Governance

## DOCUMENT CATALOG AND NAMING CONVENTION
### Authoritative Inventory · ID Scheme · Roadmap

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.27 |
| **Status** | Published |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly - or upon any artifact add/retire |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Naming Convention](#2-naming-convention)
3. [Document Types](#3-document-types)
4. [Authority and Status Lifecycle](#4-authority-and-status-lifecycle)
5. [Authoritative Catalog (V1)](#5-authoritative-catalog-v1)
6. [Cross-Reference Rules](#6-cross-reference-rules)
7. [Artifact Roadmap (V1.x → V2)](#7-artifact-roadmap-v1x--v2)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

[CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) establishes a hierarchy of policy, standards, procedures, and guidelines. As the library grows, that hierarchy is only useful if there is a single, authoritative inventory of which artifacts exist, which are planned, which are authoritative, and which are exports of an authoritative artifact for a specific audience. This document is that inventory.

It applies to every CERG-owned artifact, policy, standard, procedure, plan, guideline, template, and operational package, regardless of medium (Markdown source, exported Word/PDF, intranet page, or third-party portal entry).

> **One Source, Many Exports**
>
> The authoritative source for every CERG document is the Markdown file in the CERG content repository. Everything else, Word exports, PDF deliverables, intranet pages, regulator portal uploads, is an export. Exports inherit the ID and version of the source. If the source and an export disagree, the source wins.

---

## 2. Naming Convention

Every CERG artifact has a Document ID of the form:

```
CERG-<TYPE>-<DOMAIN>-<NNN>
```

Where:

| **Element** | **Meaning** | **Examples** |
|---|---|---|
| `CERG` | Program prefix; never changes | - |
| `<TYPE>` | Document type - see Section 3 | `POL`, `STD`, `PRC`, `PLN`, `GL`, `TMPL`, `GOV` |
| `<DOMAIN>` | Two-to-four-letter domain code | `IT`, `OT`, `CUI`, `AC`, `RM`, `VM`, `CIP`, `LM` |
| `<NNN>` | Three-digit sequence within type+domain | `001`, `002` |

Files are named `<DocumentID>_<Short_Title>.md` using underscore-separated title case (e.g., `CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md`).

> **Convention, Not Bureaucracy**
>
> The ID format exists so that a person reading a control reference can tell at a glance what kind of artifact they're being pointed at. A reader who sees `CERG-STD-OT-001` knows it's a standard; a reader who sees `CERG-PRC-VM-001` knows it's a procedure they can execute. Anything that obscures that signal, clever domain codes, free-form titles in the ID, is a mistake.

### 2.1 Domain Codes (V1)

| **Code** | **Domain** |
|---|---|
| `IT` | IT / cloud / SaaS |
| `OT` | Operational technology / grid control systems |
| `CUI` | Controlled Unclassified Information / [CMMC](https://dodcio.defense.gov/CMMC/) |
| `AC` | Access management / identity |
| `VM` | Vulnerability management |
| `RM` | Risk management (register, exceptions, scoring) |
| `IR` | Incident response (CERG-facing artifacts only) |
| `CIP` | NERC-CIP |
| `SOX` | Sarbanes-Oxley ITGC |
| `LM` | Logging, monitoring, detection |
| `CFG` | Secure configuration / hardening |
| `RES` | Cyber resilience and backup |
| `CR` | Cryptography and key management |
| `AR` | Architecture review / project intake |
| `TPRM` | Third-party / supply chain risk |
| `AV` | Adversarial validation |
| `MTR` | Metrics and reporting |
| `OM` | Operating model |
| `CAT` | Catalog / inventory |
| `CB` | Control baseline |
| `FRM` | Program-level framework narrative (e.g., the CERG Framework) |
| `TAX` | Risk taxonomy |
| `CMX` | Compliance matrix |
| `RMF` | Risk Management Framework |
| `IMP` | Implementation and adaptation guidance |
| `VAR` | Organization adaptation / variable and token scheme |
| `MAT` | Maturity self-assessment |
| `RAC` | Roles, responsibilities, and RACI |
| `SDL` | Secure software development / application security |
| `AM` | Asset management and inventory |
| `NET` | Network security and segmentation |
| `EP` | Endpoint and mobile security |
| `DG` | Data governance and classification |
| `AI` | Artificial intelligence security |
| `MSG` | Email and messaging security |
| `TM` | Threat modeling |
| `TI` | Threat intelligence |
| `AUD` | Audit and evidence management |
| `CHG` | Security change management |
| `BC` | Business continuity and disaster recovery |
| `ISO` | ISO/IEC 27001 operational package |
| `PRIV` | Privacy and data protection |
| `CAL` | Annual security and governance calendar |
| `STY` | Document authoring and style guide |
| `TRC` | Control-to-procedure traceability |

New domains are added only by amendment to this catalog.

> **Type-Code Discipline**
>
> Only the seven type codes defined in §3 are valid: `POL`, `STD`, `PRC`, `PLN`, `GL`, `TMPL`, `GOV`. Any document that uses a different type code (e.g., `PROC` instead of `PRC`) is mis-named; the correction is to rename, not to silently accept the variant. Forward references to non-existent or planned artifacts must follow §6.2 and §7.

---

## 3. Document Types

| **Type Code** | **Type** | **Authority** | **What It Looks Like** |
|---|---|---|---|
| `POL` | Policy | CISO / Executive | Durable principles. Short. Rarely changes. One per program. |
| `STD` | Standard | Governance Pillar Leader | Specific, measurable, technology-aware requirements that implement policy principles. |
| `PRC` | Procedure | Pillar Owner | Step-by-step "how" - workflow, owner, evidence, frequency. |
| `PLN` | Plan / Operational Package | Pillar Owner | Bundled procedure + templates + checklists for a regulated or assessor-facing program (e.g., CIP, CUI, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)). |
| `GL` | Guideline | Pillar Owner | Recommendations and good practice, not mandatory. |
| `TMPL` | Template | Pillar Owner | A blank artifact to be filled in (intake form, exception request, SSP). |
| `GOV` | Governance Instrument | Governance Pillar Leader | Cross-cutting instruments that aren't a single policy/standard/procedure - catalogs, control baselines, operating model, metrics dictionary. |

> **PLN vs. PRC**
>
> A `PRC` is a single procedure. A `PLN` is an operational package that bundles a procedure with templates, checklists, and registers because the regulator or auditor expects to see the bundle together (NERC-CIP, CUI/[CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)). When in doubt, prefer `PRC` and add templates as appendices.

---

## 4. Authority and Status Lifecycle

| **Status** | **Meaning** | **In Catalog?** |
|---|---|---|
| `Planned` | Artifact has an ID and an owner but no draft yet. | Yes - Section 7. |
| `Draft` | Work in progress. Not authoritative. | Yes - Section 5, flagged. |
| `For Review` | Out for stakeholder/CISO review. | Yes - Section 5. |
| `Approved` | Signed off and authoritative. | Yes - Section 5. |
| `Retired` | Replaced or no longer in force. Retained for audit. | Yes - appendix to Section 5. |

Approval authority follows [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) Section 7:

- Policy (`POL`), CISO approves; Executive leadership endorses.
- Standard (`STD`), Governance Pillar Leader approves; CISO endorses.
- Procedure / Plan / Guideline (`PRC`, `PLN`, `GL`), Pillar Owner approves; Governance Pillar Leader endorses.
- Template (`TMPL`), Pillar Owner approves.
- Governance instrument (`GOV`), Governance Pillar Leader approves.

---

## 5. Authoritative Catalog (V1)

The V1 library is the set below. Every artifact listed has either an approved or for-review source in the CERG content repository.

### 5.1 Policy

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) | Cybersecurity Policy | CISO | Approved |

### 5.2 Framework, Operating Model, and Cross-Cutting Instruments

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | CERG Operating Model | CISO / Pillar Owners | Approved |
| `CERG-GOV-CAT-001` | Document Catalog and Naming Convention | Governance Pillar Leader | Approved (this doc) |
| [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Unified Control Baseline | Governance Pillar Leader | Approved |
| [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Metrics, Dashboard, and CISO/Board Reporting | Governance Pillar Leader | Approved |
| [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) | SURGE / CERG Framework (narrative) | CISO | Approved |
| [`CERG-GOV-RMF-001`](CERG_Risk_Management_Framework_v1.0.md) | Risk Management Framework | Governance Pillar Leader | Approved |
| [`CERG-GOV-TAX-001`](CERG%20Risk%20Taxonomy.md) | Risk Taxonomy | Cyber Risk | Approved |
| [`CERG-GOV-CMX-001`](CERG%20Compliance%20Matrix.md) | Compliance Matrix | Governance Pillar Leader | Approved |
| [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Implementation and Adaptation Guide | Governance Pillar Leader | Draft |
| [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Organization Adaptation Profile | Governance Pillar Leader | Draft |
| [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | Maturity Self-Assessment and Scorecard | Governance Pillar Leader | Draft |
| [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Consolidated Roles, Responsibilities, and RACI Instrument | Governance Pillar Leader | Approved |
| [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) | Annual Security and Governance Calendar | Governance Pillar Leader | Draft |
| [`CERG-GOV-STY-001`](CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) | Document Authoring and Style Guide | Governance Pillar Leader (Policy & Standards) | Draft |
| [`CERG-GOV-TRC-001`](CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) | Control-to-Procedure Traceability Matrix | Governance Pillar Leader (Control Baseline) | Draft |

### 5.3 Standards

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | IT / Cloud / SaaS Security Standard | Cyber Governance - IT/Cloud | Approved |
| [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | Grid Control Systems Security Standard | Cyber Governance - OT | Approved |
| [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md) | CUI Handling Standard | Cyber Governance - CUI/CMMC | Approved |
| [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Access Management Standard | Cyber Governance - Identity | Approved |
| [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Secure Configuration Baseline Standard (DISH) | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Logging, Monitoring, and Detection Standard | Cyber Risk - Detection | Approved |
| [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Cyber Resilience and Backup Standard | Cyber Engineering - Resilience | Approved |
| [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Cryptography and Key Management Standard | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) | Secure Software Development and Application Security Standard | Cyber Engineering - Application Security | Approved |
| [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Asset Management and Inventory Standard | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) | Network Security and Segmentation Standard | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-EP-001`](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) | Endpoint and Mobile Security Standard | Cyber Engineering - Endpoint | Approved |
| [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Data Governance and Classification Standard | Cyber Governance - Policy & Standards | Approved |
| [`CERG-STD-AI-001`](CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Artificial Intelligence Security Standard | Cyber Engineering - Application Security | Approved |
| [`CERG-STD-MSG-001`](CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md) | Email and Messaging Security Standard | Cyber Engineering - Platforms | Approved |

### 5.4 Procedures

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | Vulnerability Management Procedure | Cyber Risk | Approved |
| [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk Register and Exception Process | Cyber Governance - Risk Register | Approved |
| [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Architecture Review and Project Intake Procedure | Cyber Engineering | Approved |
| [`CERG-PRC-AC-002`](CERG-PRC-AC-002_Access_Management_Runbook.md) | Access Management Runbook | Identity Engineer (or IAM team if external) | Approved |
| [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Third-Party and Supply Chain Risk Procedure | Cyber Risk - Vendor Risk | Approved |
| [`CERG-PRC-AV-001`](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Adversarial Validation Procedure | Cyber Risk - Offensive Security | Approved |
| [`CERG-PRC-IR-002`](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) | Incident Response Playbook Set | Cyber Governance / standing IR team liaison | Draft |
| [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Threat Modeling Procedure | Cyber Risk | Draft |
| [`CERG-PRC-TI-001`](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) | Threat Intelligence Procedure | Cyber Risk - Threat Intelligence | Draft |
| [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Audit and Evidence Management Procedure | Cyber Governance | Draft |
| [`CERG-PRC-CHG-001`](CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) | Security Change Management Procedure | Cyber Engineering | Draft |

> **Numbering note: CERG-PRC-AC-001.** The Access Management Runbook is identifier `CERG-PRC-AC-002` rather than `-001` because the original `-001` slot was reserved for a planned standalone Access Review Runbook that has not been authored; the work was folded into the parent standard [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) §9. The `-002` ID is preserved to avoid renumbering existing references. The `-001` slot is reserved for future use.

### 5.5 Plans / Operational Packages

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) | Incident Response Plan (owned by standing IR team; CERG provides liaison) | Standing IR team / CERG liaison | Approved |
| [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | CUI / CMMC Operational Package | Cyber Governance - CUI/CMMC | Approved |
| [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | NERC-CIP Operational Package | Cyber Governance - OT | Approved |
| [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | SOX ITGC Operational Package | Cyber Governance - SOX | Approved |
| [`CERG-PLN-BC-001`](CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md) | Business Continuity and Disaster Recovery Plan | Governance Pillar Leader | Draft |
| [`CERG-PLN-ISO-001`](CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md) | ISO/IEC 27001 Operational Package | Governance Pillar Leader | Draft |
| [`CERG-PLN-PRIV-001`](CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md) | Privacy and Data Protection Operational Package | Governance Pillar Leader | Draft |

### 5.6 Templates

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Risk Register Templates and Reporting | Cyber Governance - Risk Register | Approved |
| [`CERG-TMPL-CUI-001`](CERG-TMPL-CUI-001_System_Security_Plan_Template.md) | System Security Plan Template | CMMC / Federal Compliance Manager | Draft |
| [`CERG-TMPL-CUI-002`](CERG-TMPL-CUI-002_POAM_Template.md) | Plan of Action and Milestones Template | CMMC / Federal Compliance Manager | Draft |
| [`CERG-TMPL-RM-002`](CERG-TMPL-RM-002_Security_Exception_Request_Form.md) | Security Exception Request Form | Risk Register Owner | Draft |
| [`CERG-TMPL-AR-001`](CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md) | Architecture and Project Intake Form | Engineering Pillar Leader | Draft |
| [`CERG-TMPL-TPRM-001`](CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md) | Vendor Security Questionnaire and TPRM Assessment Template | Vendor Risk Analyst | Draft |
| [`CERG-TMPL-RM-003`](CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md) | Risk Acceptance Memo Template | Risk Pillar Leader | Draft |
| [`CERG-TMPL-AUD-001`](CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md) | Control Evidence and Test Worksheet | Evidence Librarian | Draft |
| [`CERG-TMPL-MTR-001`](CERG-TMPL-MTR-001_Board_and_CISO_Reporting_Deck_Template.md) | Board and CISO Reporting Deck Template | Governance Pillar Leader | Draft |

Other templates remain embedded as appendices of their parent procedure or plan unless they have independent reuse outside that artifact. The Document Catalog references the parent.

---

## 6. Cross-Reference Rules

These rules govern every "Related Documents" table, every footnote reference, and every link in a CERG artifact.

1. **Link only to artifacts that appear in this catalog.** If the artifact does not appear in Section 5 or Section 7, do not reference it.
2. **Distinguish approved from planned.** When a Related Documents table includes a Planned artifact, mark it `(Planned, V1.x)` or `(Planned, V2)` so the reader knows it does not yet exist.
3. **Use the Document ID, not the file name.** File names change; IDs do not.
4. **Avoid forward references to TMPL artifacts that live inside a parent.** Cite the parent and the appendix (`CERG-PRC-AR-001 Appendix B, Security Project Intake Form`).
5. **External standards (NIST, CIS, IEC, ISO) are cited by short form**, `NIST 800-53r5 AC-2`, `CIS Benchmark Windows Server 2022 L1`, `IEC 62443-3-3 SR 1.1`. Each artifact's metadata table lists the framework set in scope.

> **The Reference Discipline Test**
>
> A new CERG team member opens any artifact, follows a reference, and arrives at exactly the document the reference named, at the version the catalog records, with no dead links and no surprises. If that holds for every reference in the library, the catalog is doing its job. If it does not, the catalog, not the citing document, is the artifact that needs the fix.

---

## 7. Artifact Roadmap (V1.x to V2)

This section is the authoritative list of planned artifacts. Per Cross-Reference Rule 1, a planned artifact may be referenced by another artifact only if it appears here, and the reference is marked `(Planned, V1.x)` or `(Planned, V2)`.

An artifact moves from this section to Section 5 when it is authored and reaches `Draft` or above. An artifact in this section has an ID reserved and an owner assigned but is not yet authoritative and must not be relied upon.

### 7.1 Status of the V1.x Build

The V1.x build extends the original V1 library along six tracks: the adoption layer, the Engineering-pillar standards, the governance glue, the missing procedures, the missing operational packages, and the standalone template library. As of this version of the catalog, the adoption layer (`IMP`, `VAR`, `MAT`), the seven Engineering and data standards (`SDL`, `AM`, `NET`, `EP`, `DG`, `AI`, `MSG`), the consolidated RACI instrument (`RAC`), the Group C in-scope procedures (`IR-002`, `TM`, `TI`, `AUD`, `CHG`), the Group D operational packages (`BC`, `ISO`, `PRIV`), the Group E standalone templates, and the F2-F4 governance instruments (`CAL`, `STY`, `TRC`) are authored and registered in Section 5. The artifacts below remain planned.

### 7.2 Planned Procedures

No in-scope Group C procedures remain planned in V1.x. Security Awareness and Training and SOC / Forensics operations are intentionally out of CERG scope and are not reserved here.

### 7.3 Planned Plans and Operational Packages

No Group D operational packages remain planned. Business Continuity and Disaster Recovery, ISO/IEC 27001, and Privacy and Data Protection packages are authored and registered in Section 5.5.

### 7.4 Planned Templates

No Group E standalone templates remain planned. The System Security Plan, POA&M, security exception request, architecture and project intake form, vendor security questionnaire, risk acceptance memo, control evidence worksheet, and Board / CISO reporting deck templates are authored and registered in Section 5.6.

The incident report and post-incident review template remains embedded in the incident response plan and playbook set unless promoted by a future amendment.

### 7.5 Planned Governance Instruments

No F2-F4 governance instruments remain planned. The Annual Security and Governance Calendar, Document Authoring and Style Guide, and Control-to-Procedure Traceability Matrix are authored and registered in Section 5.2.

> **The Roadmap Is a Commitment, Not a Wishlist**
>
> An ID in this section is a reserved identifier with a named owner. It is not a vague intention. When an artifact is listed here, a citing document is permitted to forward-reference it, which means readers will encounter the reference before the artifact exists. That is only safe if this section is honest: every entry has a real owner and a real target, and an entry that is no longer intended is removed by amendment, not left to mislead.

---

## 8. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.27 |
| **Status** | Published |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly, or upon any artifact add or retire |
| **Next Scheduled Review** | 2026-08-21 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-01 | Cyber Governance | Initial release. Established the naming convention, document types, the authority and status lifecycle, the V1 authoritative catalog, and the cross-reference rules. |
| 1.21 | 2026-05-01 | Cyber Governance | Catalog maintenance release aligning artifact versions across the V1 library. |
| 1.22 | 2026-05-21 | Cyber Governance | Registered the adoption-layer domains `IMP`, `VAR`, and `MAT` in Section 2.1 and added `CERG-GOV-IMP-001`, `CERG-GOV-VAR-001`, and `CERG-GOV-MAT-001` to Section 5.2. |
| 1.23 | 2026-05-21 | Cyber Governance | Registered domains `RAC`, `SDL`, `AM`, `NET`, `EP`, `DG`, `AI`, and `MSG`. Added `CERG-GOV-RAC-001` to Section 5.2 and seven standards to Section 5.3. Set `CERG-GOV-RAC-001` and the seven new standards to `Approved` on CISO sign-off. Restored the document to its full structure: completed the Section 6 Reference Discipline Test callout, and authored Section 7 (Artifact Roadmap) and Section 8 (Document Control), which had been absent. |
| 1.24 | 2026-05-22 | Cyber Governance | Registered domains `TM`, `TI`, `AUD`, and `CHG`; added `CERG-PRC-IR-002`, `CERG-PRC-TM-001`, `CERG-PRC-TI-001`, `CERG-PRC-AUD-001`, and `CERG-PRC-CHG-001` to Section 5.4 as Draft; removed the now-authored Group C procedure reservations from Section 7.2; noted that Security Awareness and Training and SOC / Forensics operations are intentionally out of CERG scope. |
| 1.25 | 2026-05-22 | Cyber Governance | Registered domains `BC`, `ISO`, and `PRIV`; added `CERG-PLN-BC-001`, `CERG-PLN-ISO-001`, and `CERG-PLN-PRIV-001` to Section 5.5 as Draft; removed the now-authored Group D operational package reservations from Section 7.3. |
| 1.26 | 2026-05-22 | Cyber Governance | Added eight standalone Group E templates to Section 5.6 as Draft: `CERG-TMPL-CUI-001`, `CERG-TMPL-CUI-002`, `CERG-TMPL-RM-002`, `CERG-TMPL-AR-001`, `CERG-TMPL-TPRM-001`, `CERG-TMPL-RM-003`, `CERG-TMPL-AUD-001`, and `CERG-TMPL-MTR-001`; updated Section 7.4 to state that no Group E standalone templates remain planned. |
| 1.27 | 2026-05-22 | Cyber Governance | Registered domains `CAL`, `STY`, and `TRC`; added `CERG-GOV-CAL-001`, `CERG-GOV-STY-001`, and `CERG-GOV-TRC-001` to Section 5.2 as Draft; updated Section 7.5 to state that no F2-F4 governance instruments remain planned. |

### Review Triggers

- Any artifact added to, or retired from, the CERG library
- Any new domain or type code required by a new artifact
- A change to the naming convention or the cross-reference rules
- A planned artifact in Section 7 reaching `Draft` or above, which moves it to Section 5
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Document Control) is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) | Parent policy; establishes the document hierarchy this catalog inventories |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines the roles cited as artifact owners |
| Consolidated Roles, Responsibilities, and RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Master RACI for ownership of every artifact in this catalog |
| Implementation and Adaptation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Adoption sequencing; instructs adopters to keep this catalog current | 
