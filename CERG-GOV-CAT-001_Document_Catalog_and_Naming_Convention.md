
# SURGE: Cyber Engineering, Risk & Governance

## DOCUMENT CATALOG AND NAMING CONVENTION
### Authoritative Inventory · ID Scheme · Roadmap

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.0 |
| **Status** | Approved (V1) |
| **Classification** | Internal - Confidential |
| **Owner** | Cyber Governance Manager (Document Control) |
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

New domains are added only by amendment to this catalog.

> **Type-Code Discipline**
>
> Only the seven type codes defined in §3 are valid: `POL`, `STD`, `PRC`, `PLN`, `GL`, `TMPL`, `GOV`. Any document that uses a different type code (e.g., `PROC` instead of `PRC`) is mis-named; the correction is to rename, not to silently accept the variant. Forward references to non-existent or planned artifacts must follow §6.2 and §7.

---

## 3. Document Types

| **Type Code** | **Type** | **Authority** | **What It Looks Like** |
|---|---|---|---|
| `POL` | Policy | CISO / Executive | Durable principles. Short. Rarely changes. One per program. |
| `STD` | Standard | Cyber Governance Manager | Specific, measurable, technology-aware requirements that implement policy principles. |
| `PRC` | Procedure | Pillar Owner | Step-by-step "how" - workflow, owner, evidence, frequency. |
| `PLN` | Plan / Operational Package | Pillar Owner | Bundled procedure + templates + checklists for a regulated or assessor-facing program (e.g., CIP, CUI, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)). |
| `GL` | Guideline | Pillar Owner | Recommendations and good practice, not mandatory. |
| `TMPL` | Template | Pillar Owner | A blank artifact to be filled in (intake form, exception request, SSP). |
| `GOV` | Governance Instrument | Cyber Governance Manager | Cross-cutting instruments that aren't a single policy/standard/procedure - catalogs, control baselines, operating model, metrics dictionary. |

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
- Standard (`STD`), Cyber Governance Manager approves; CISO endorses.
- Procedure / Plan / Guideline (`PRC`, `PLN`, `GL`), Pillar Owner approves; Cyber Governance Manager endorses.
- Template (`TMPL`), Pillar Owner approves.
- Governance instrument (`GOV`), Cyber Governance Manager approves.

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
| `CERG-GOV-CAT-001` | Document Catalog and Naming Convention | Cyber Governance Manager | Approved (this doc) |
| [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Unified Control Baseline | Cyber Governance Manager | Approved |
| [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Metrics, Dashboard, and CISO/Board Reporting | Cyber Governance Manager | Approved |
| [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) | SURGE / CERG Framework (narrative) | CISO | Approved |
| [`CERG-GOV-RMF-001`](CERG_Risk_Management_Framework_v1.0.md) | Risk Management Framework | Cyber Governance Manager | Approved |
| [`CERG-GOV-TAX-001`](CERG%20Risk%20Taxonomy.md) | Risk Taxonomy | Cyber Risk | Approved |
| [`CERG-GOV-CMX-001`](CERG%20Compliance%20Matrix.md) | Compliance Matrix | Cyber Governance Manager | Approved |

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

### 5.4 Procedures

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | Vulnerability Management Procedure | Cyber Risk | Approved |
| [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk Register and Exception Process | Cyber Governance - Risk Register | Approved |
| [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Architecture Review and Project Intake Procedure | Cyber Engineering | Approved |
| [`CERG-PRC-AC-002`](CERG-PRC-AC-002_Access_Management_Runbook.md) | Access Management Runbook | Cyber Engineering - Identity (or IAM team if external) | Approved |
| [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Third-Party and Supply Chain Risk Procedure | Cyber Risk - Vendor Risk | Approved |
| [`CERG-PRC-AV-001`](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Adversarial Validation Procedure | Cyber Risk - Offensive Security | Approved |

> **Numbering note: CERG-PRC-AC-001.** The Access Management Runbook is identifier `CERG-PRC-AC-002` rather than `-001` because the original `-001` slot was reserved for a planned standalone Access Review Runbook that has not been authored; the work was folded into the parent standard [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) §9. The `-002` ID is preserved to avoid renumbering existing references. The `-001` slot is reserved for future use.

### 5.5 Plans / Operational Packages

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) | Incident Response Plan (owned by standing IR team; CERG provides liaison) | Standing IR team / CERG liaison | Approved |
| [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | CUI / CMMC Operational Package | Cyber Governance - CUI/CMMC | Approved |
| [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | NERC-CIP Operational Package | Cyber Governance - OT | Approved |
| [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | SOX ITGC Operational Package | Cyber Governance - SOX | Approved |

### 5.6 Templates

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Risk Register Templates and Reporting | Cyber Governance - Risk Register | Approved |

Other templates are embedded as appendices of their parent procedure or plan unless they have independent reuse outside that artifact. The Document Catalog references the parent. V2 may promote heavy-use templates to standalone `TMPL` artifacts.

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
> A new CERG team member opens 