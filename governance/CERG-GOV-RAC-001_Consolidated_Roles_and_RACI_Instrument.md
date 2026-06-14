
# SURGE: Cyber Engineering, Risk & Governance

## CONSOLIDATED ROLES, RESPONSIBILITIES, AND RACI INSTRUMENT
### Canonical Role Reference · Master RACI · Role Descriptions · Scaling Map

---

| | |
|---|---|
| **Document ID** | CERG-GOV-RAC-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) · [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) · [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **Review Cycle** | Annual / On any change to the canonical role roster or the artifact catalog |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (PM, PS families) · ISO/IEC 27001 A.5.2, A.5.4 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How This Instrument Relates to the Operating Model](#2-how-this-instrument-relates-to-the-operating-model)
3. [RACI Definitions and Rules](#3-raci-definitions-and-rules)
4. [The Canonical Role Reference](#4-the-canonical-role-reference)
5. [Master RACI: Document Ownership](#5-master-raci-document-ownership)
6. [Master RACI: Standing Processes](#6-master-raci-standing-processes)
7. [Role Descriptions](#7-role-descriptions)
8. [The Scaling Map](#8-the-scaling-map)
9. [Maintaining This Instrument](#9-maintaining-this-instrument)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

[`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1 establishes the canonical role roster, the single source of truth for role names. §9 of that document gives three sample RACI patterns and states plainly that "specific RACI matrices are maintained per process." That sentence describes a document that did not exist. This is that document.

This instrument consolidates, in one place: the canonical role reference, a master RACI covering every CERG artifact and every standing process, a normalized description for each canonical role, and the scaling map that shows how the roles consolidate onto fewer people as a team gets smaller.

It applies program-wide. It is the authoritative answer to two questions a CERG program is asked constantly: "who owns this?" and "who does what when this process runs?"

> **One RACI, So the Answer Is Always the Same**
>
> Role ambiguity is the failure mode CERG was built to remove. When each document carries its own role table and its own RACI, those tables drift: a role is Accountable in one document and merely Consulted in another for the same work. A reader gets a different answer depending on which document they happen to open. This instrument is the single authoritative RACI. Where a subordinate document's role table disagrees with this instrument, this instrument governs, and the subordinate document is corrected on its next revision.

---

## 2. How This Instrument Relates to the Operating Model

The division of labor is deliberate and must stay clean.

| **Document** | **Owns** |
|---|---|
| [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1 | The canonical role roster: the authoritative list of role *names* and their synonyms. |
| This instrument (`CERG-GOV-RAC-001`) | The consolidated RACI and the normalized role *descriptions*: who is Responsible, Accountable, Consulted, and Informed across every artifact and process. |
| Each standard, procedure, and plan | Its own subject matter. It may carry a local roles table for the reader's convenience, but that table conforms to this instrument. |

The Operating Model names the roles. This instrument assigns the work. No new role is introduced here; if a role is needed that the roster does not contain, the roster is amended first, in the Operating Model, and only then does this instrument reference it.

---

## 3. RACI Definitions and Rules

| **Letter** | **Meaning** |
|---|---|
| **R - Responsible** | Does the work. Can be more than one role. |
| **A - Accountable** | Answerable for the outcome. Exactly one role per row. The A approves the work of the R. |
| **C - Consulted** | Provides input before the work is done. Two-way communication. |
| **I - Informed** | Told of the outcome. One-way communication. |

Rules that govern every row in this instrument:

1. **Exactly one A per row.** Accountability is never shared. A row with two A's has no owner; a row with no A is unowned work. Either is a finding.
2. **A and R may be the same role.** On any team, and especially a small one, the role accountable for an outcome often also does the work. That is shown as **R/A**.
3. **The A cannot be only Informed.** A role accountable for an outcome is never merely Informed of it.
4. **Approval authority is not overridden here.** Where a row involves risk acceptance, the accountable approver is the one named in the authority table of [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. This instrument does not change who may accept risk.
5. **Roles are canonical.** Every role in this instrument is a canonical role from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1. No synonyms.

---

## 4. The Canonical Role Reference

The 27 canonical roles, grouped by pillar, as established in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1. This table is a reference copy for use with the RACI below; the Operating Model remains authoritative for the roster itself.

| **Group** | **Canonical Roles** | **NICE Work Role Category** |
|---|---|---|
| Executive | Chief Information Security Officer (CISO); Executive Sponsor | OV (Oversee and Govern) |
| Engineering | Engineering Pillar Leader; Cloud Security Engineer; Identity Engineer; OT Security Engineer; Application Security Engineer; Endpoint Engineer; Cryptography Engineer; Pre-production Reviewer | SP (Securely Provision), OM (Operate and Maintain) |
| Risk | Risk Pillar Leader; Exposure Management Lead; Adversarial Testing Lead; Threat Intelligence Analyst; Vendor Risk Analyst; OT Risk Analyst; Identity Risk Analyst; Detection Engineer | PR (Protect and Defend), AN (Analyze) |
| Governance | Governance Pillar Leader; NERC-CIP Compliance Manager; CMMC / Federal Compliance Manager; SOX ITGC Lead; Policy & Standards Manager; Risk Register Owner; Evidence Librarian | OV (Oversee and Govern) |
| Adjacent (IR team) | Incident Commander; Lead Investigator | PR (Protect and Defend), IN (Investigate) |

The two Adjacent roles belong to the standing Incident Response team, not to CERG, per [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4. They appear in this instrument only where CERG work interfaces with incident response.

---

## 5. Master RACI: Document Ownership

This RACI assigns accountability for each artifact in the CERG library: who owns it (A), who drafts and maintains it (R), and who is Consulted and Informed on its content. Approval authority by document type follows [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) §4; this table shows the working RACI underneath that authority.

Columns are abbreviated: **ENG-L** Engineering Pillar Leader, **RISK-L** Risk Pillar Leader, **GOV-L** Governance Pillar Leader, **P&S** Policy & Standards Manager, **CISO** Chief Information Security Officer.

| **Artifact** | **ENG-L** | **RISK-L** | **GOV-L** | **P&S** | **CISO** |
|---|---|---|---|---|---|
| `CERG-POL-001` Cybersecurity Policy | C | C | R | C | **A** |
| `CERG-GOV-FRM-001` CERG Framework | C | C | R | C | **A** |
| `CERG-GOV-OM-001` Operating Model | C | C | **R/A** | C | C |
| `CERG-GOV-CAT-001` Document Catalog | I | I | **A** | R | I |
| `CERG-GOV-CB-001` Unified Control Baseline | C | C | **R/A** | C | I |
| `CERG-GOV-MTR-001` Metrics and Reporting | C | C | **R/A** | C | C |
| `CERG-GOV-RMF-001` Risk Management Framework | C | C | **R/A** | C | C |
| `CERG-GOV-TAX-001` Risk Taxonomy | C | **R** | **A** | C | I |
| `CERG-GOV-CMX-001` Compliance Matrix | C | C | **R/A** | C | I |
| `CERG-GOV-IMP-001` Implementation and Adaptation Guide | C | C | **A** | R | C |
| `CERG-GOV-VAR-001` Organization Adaptation Profile | C | I | **A** | R | I |
| `CERG-GOV-MAT-001` Maturity Self-Assessment | C | C | **R/A** | C | C |
| `CERG-GOV-RAC-001` This instrument | C | C | **A** | R | I |
| `CERG-STD-IT-001` IT / Cloud / SaaS Security | **R** | C | **A** | C | I |
| `CERG-STD-OT-001` Grid Control Systems Security | **R** | C | **A** | C | I |
| `CERG-STD-CUI-001` CUI Handling | C | C | **R/A** | C | I |
| `CERG-STD-AC-001` Access Management | **R** | C | **A** | C | I |
| `CERG-STD-CFG-001` Secure Configuration Baseline | **R/A** | C | C | C | I |
| `CERG-STD-LM-001` Logging, Monitoring, Detection | C | **R** | **A** | C | I |
| `CERG-STD-RES-001` Cyber Resilience and Backup | **R/A** | C | C | C | I |
| `CERG-STD-CR-001` Cryptography and Key Management | **R/A** | C | C | C | I |
| `CERG-STD-SDL-001` Secure Software Development | **R/A** | C | C | C | I |
| `CERG-STD-AM-001` Asset Management and Inventory | **R/A** | C | C | C | I |
| `CERG-STD-NET-001` Network Security and Segmentation | **R/A** | C | C | C | I |
| `CERG-STD-EP-001` Endpoint and Mobile Security | **R/A** | C | C | C | I |
| `CERG-STD-DG-001` Data Governance and Classification | C | C | **R/A** | C | I |
| `CERG-STD-AI-001` Artificial Intelligence Security | **R/A** | C | C | C | I |
| `CERG-STD-MSG-001` Email and Messaging Security | **R/A** | C | C | C | I |
| `CERG-PRC-VM-001` Vulnerability Management | C | **R/A** | C | C | I |
| `CERG-PRC-RM-001` Risk Register and Exception Process | C | C | **R/A** | C | I |
| `CERG-PRC-AR-001` Architecture Review and Project Intake | **R/A** | C | C | C | I |
| `CERG-PRC-AC-002` Access Management Runbook | **R/A** | C | C | C | I |
| `CERG-PRC-TPRM-001` Third-Party and Supply Chain Risk | C | **R/A** | C | C | I |
| `CERG-PRC-AV-001` Adversarial Validation | C | **R/A** | C | C | I |
| `CERG-PLN-IR-001` Incident Response Plan | C | C | C | I | C |
| `CERG-PLN-CUI-001` CUI / CMMC Operational Package | C | C | **R/A** | C | I |
| `CERG-PLN-CIP-001` NERC-CIP Operational Package | C | C | **R/A** | C | I |
| `CERG-PLN-SOX-001` SOX ITGC Operational Package | C | C | **R/A** | C | I |
| `CERG-TMPL-RM-001` Risk Register Templates | C | C | **R/A** | C | I |

> **Standard Authorship Sits With Engineering; Standard Authority Sits With Governance**
>
> Several standards show the Engineering Pillar Leader as R/A. That is the working reality: Engineering writes and maintains the technical standards because Engineering holds the expertise. It does not change the approval authority in [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) §4, under which a standard is approved by the Governance Pillar Leader with CISO endorsement. The R/A in this table is accountability for the artifact's content and upkeep. The catalog governs who signs it into force. Both are true at once, and neither overrides the other.
>
> The Incident Response Plan shows no CERG role as A, by design: per [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4 it is owned by the standing IR team. CERG roles are Consulted and Informed only.

---

## 6. Master RACI: Standing Processes

This RACI covers the recurring processes that make up the running program. It extends the three sample patterns in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §9 into a complete set.

Columns: **ENG** Engineering pillar, **RISK** Risk pillar, **GOV** Governance pillar, **OWNER** Business or Asset Owner, **CISO** Chief Information Security Officer. A cell names the specific canonical role where one role within the pillar carries it.

### 6.1 Engagement and Build

| **Process** | **ENG** | **RISK** | **GOV** | **OWNER** | **CISO** |
|---|---|---|---|---|---|
| Project intake and architecture review | **R/A** | C | C | C | I |
| Threat modeling during design | C | **R** | I | C | I |
| Secure development gate enforcement | **R/A** | C | I | I | I |
| Pre-production review and go-live readiness | **R/A** Pre-production Reviewer | C | C | C | I |
| Approve go-live | **R** | C | C | **A** | I |
| Asset onboarding to the inventory | **R/A** | C | I | C | I |

### 6.2 Exposure and Risk

| **Process** | **ENG** | **RISK** | **GOV** | **OWNER** | **CISO** |
|---|---|---|---|---|---|
| Vulnerability scanning and SLA tracking | C | **R/A** Exposure Management Lead | I | I | I |
| Vulnerability remediation | **R** | C | I | **A** | I |
| Adversarial validation (pen test, red team) | C | **R/A** Adversarial Testing Lead | I | I | I |
| Threat intelligence collection and dissemination | C | **R/A** Threat Intelligence Analyst | C | I | I |
| Risk register entry and curation | I | C | **R/A** Risk Register Owner | I | I |
| Risk treatment decision | C | C | C | **A** | I (review High+) |
| Risk acceptance approval | per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 | per RMF §9.7 | per RMF §9.7 | C | **A** for High+ |
| Exception request and tracking | C | C | **R/A** Risk Register Owner | C | I |
| Third-party and supply chain risk assessment | C | **R/A** Vendor Risk Analyst | C | C | I |

### 6.3 Governance and Assurance

| **Process** | **ENG** | **RISK** | **GOV** | **OWNER** | **CISO** |
|---|---|---|---|---|---|
| Control evidence collection and curation | C | C | **R/A** Evidence Librarian | I | I |
| Compliance posture tracking | C | C | **R/A** | I | I |
| Audit and assessor liaison | C | C | **R/A** | I | C |
| Metrics production and CISO dashboard | C | C | **R/A** | I | C |
| Quarterly Cyber Oversight Group brief | C | C | **R** | I | **A** |
| Document review-cycle management | C | C | **R/A** Policy & Standards Manager | I | I |
| Maturity self-assessment | C | C | **R** Governance Pillar Leader | I | **A** |

### 6.4 Operations and Detection

| **Process** | **ENG** | **RISK** | **GOV** | **OWNER** | **CISO** |
|---|---|---|---|---|---|
| Access provisioning and review | **R/A** Identity Engineer | C | C | C | I |
| Detection content authoring and tuning | C | **R/A** Detection Engineer | I | I | I |
| Logging and monitoring coverage | C | **R** Detection Engineer | **A** | I | I |
| Incident detection handoff to the IR team | C | **R** | C | I | I |
| Incident response operations | C (Engineering Lead) | C (Lead Investigator) | C (Governance Lead) | I | I |
| Post-incident risk-register entry | I | C | **R/A** Risk Register Owner | I | I |

> **Incident Response Is Supported, Not Owned**
>
> Section 6.4 shows incident response operations with CERG roles as Consulted, never Accountable. This is the boundary set by [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4. The standing IR team owns and runs the incident. CERG detects the incident, hands it off, supplies the Engineering Lead, Lead Investigator, and Governance Lead roles when the IR team calls for them, and afterward records the post-incident risk in the register. The Incident Commander, an Adjacent role, is Accountable for the incident itself, which is why no CERG column carries the A.

---

## 7. Role Descriptions

A normalized one-paragraph description for each canonical role. These are the job-description stubs an adopting organization expands into full descriptions. Each names the role's accountability, its principal artifacts and processes from Sections 5 and 6, and its risk-acceptance authority where it has one.

### 7.1 Executive

**Chief Information Security Officer (CISO).** Accountable for the cybersecurity program as a whole. Sets strategy, reports posture and material risk to executive leadership and the board, and holds final authority on High and Critical risk acceptance per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. Accountable for the Cybersecurity Policy and the CERG Framework, and for the Quarterly Cyber Oversight Group brief.

**Executive Sponsor.** The business voice in the program. Provides concurrence for Critical risk acceptance per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7, sits on the Cyber Oversight Group, and endorses the Cybersecurity Policy on behalf of the business. On a small team, provides the independent second view on risk acceptance where roles are otherwise consolidated.

### 7.2 Engineering

**Engineering Pillar Leader.** Accountable for the Cyber Engineering pillar: project intake, reference architecture, and the secure build of the estate. Accountable for the technical standards authored by Engineering, including configuration, resilience, cryptography, secure development, asset management, network, endpoint, AI, and email security. Resolves software risk-tier disputes.

**Cloud Security Engineer.** Owns cloud and SaaS platform security: infrastructure-as-code, cloud posture management, the landing zone, cloud network security, and the email and messaging platforms where they are SaaS. Responsible for shadow-IT and shadow-AI discovery through cloud signals.

**Identity Engineer.** Owns identity and access engineering: the identity provider, multi-factor authentication, single sign-on, privileged access management, secrets management, and federation. Responsible for access provisioning and review and for the Access Management Runbook.

**OT Security Engineer.** Owns operational technology security engineering: IT/OT convergence, the electronic security perimeter, the IT/OT boundary design, and BES Cyber System baselines. Responsible for OT-safe asset discovery and transient cyber asset control.

**Application Security Engineer.** Owns application security: SAST, DAST, and SCA rulesets, threat modeling, secure-development gate content, and the security of in-house and embedded AI systems. Accountable for the Secure Software Development and the Artificial Intelligence Security standards.

**Endpoint Engineer.** Owns endpoint and mobile security: endpoint and mobile baselines, the management and endpoint detection and response platforms, and the device posture signal consumed by the network and access standards. Accountable for the Endpoint and Mobile Security Standard.

**Cryptography Engineer.** Owns cryptography and key management: the key management and secrets platforms, the certificate authority hierarchy, transport security posture, and FIPS compliance. Supports rotation of exposed secrets.

**Pre-production Reviewer.** A rotated Engineering role. Owns the pre-production checklist and signs go-live readiness, confirming that pre-production findings are remediated or risk-accepted before a system goes live.

### 7.3 Risk

**Risk Pillar Leader.** Accountable for the Cyber Risk pillar: the organization's exposure posture and the reporting of it. Holds Medium severity risk-acceptance authority per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7.

**Exposure Management Lead.** Operates the Vulnerability Management Procedure. Accountable for remediation SLAs and vulnerability posture metrics.

**Adversarial Testing Lead.** Operates the Adversarial Validation Procedure: penetration testing, red team, and purple team exercises, and the tracking of their findings.

**Threat Intelligence Analyst.** Owns threat-actor tracking, advisories, and the translation of intelligence into detection priorities. Disseminates intelligence to Engineering, Detection, and Governance.

**Vendor Risk Analyst.** Operates the Third-Party and Supply Chain Risk Procedure: vendor tiering and assessment, supply chain coordination, and the assessment of third-party AI services.

**OT Risk Analyst.** Owns OT-safe vulnerability assessment and industrial control system threat intelligence.

**Identity Risk Analyst.** Owns identity-threat detection: user and entity behavior analytics, and OAuth and token risk.

**Detection Engineer.** Owns detection-rule authoring, ATT&CK coverage, and the tuning lifecycle. Responsible for logging and monitoring coverage and for handing detected incidents to the standing IR team.

### 7.4 Governance

**Governance Pillar Leader.** Accountable for the Cyber Governance pillar: policy and standards, compliance, control evidence, the risk register, and audit response. Approves standards with CISO endorsement. Holds Low and Informational severity risk-acceptance authority per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. Accountable for most governance instruments and operational packages.

**NERC-CIP Compliance Manager.** Owns OT and BES Cyber System compliance posture and the NERC-CIP Operational Package.

**CMMC / Federal Compliance Manager.** Owns CUI compliance posture, the System Security Plan and POA&M, and the CUI / CMMC Operational Package.

**SOX ITGC Lead.** Owns IT general control evidence, audit coordination for SOX, and the SOX ITGC Operational Package.

**Policy & Standards Manager.** Owns the document library: version control, review cycles, and naming-convention discipline. Responsible for the Document Catalog, the Implementation and Adaptation Guide, the Organization Adaptation Profile, and this instrument.

**Risk Register Owner.** Operates the Risk Register and Exception Process. Curates the register, runs the Monthly Risk Register Review, and records post-incident risks.

**Evidence Librarian.** Owns the cross-framework evidence library: collection, curation, and retention of control evidence for audit.

### 7.5 Adjacent (Incident Response team)

**Incident Commander.** Single-decision authority during an active incident. An Incident Response team role, not a CERG role; included here because CERG processes hand off to it.

**Lead Investigator.** The risk-side technical lead during an active incident. An Incident Response team role; CERG supplies practitioners into incident roles when the IR team calls for them.

---

## 8. The Scaling Map

The canonical role roster is fixed at 27 roles. A small team does not delete roles; it assigns several roles to one person. This is the principle established in [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §6. This section makes the consolidation concrete so a small team can see exactly who holds what.

### 8.1 The Rule

Every one of the 27 roles is held by someone. On a large team that is close to one role per person. On a small team one person holds many roles. The RACI in Sections 5 and 6 does not change when the team shrinks; only the map from role to person changes. A process with the Exposure Management Lead as R/A still has an R/A when that role is held by the same person who is also the Risk Pillar Leader. The work is still owned.

### 8.2 Reference Consolidation: Five-Person Team

| **Person** | **Holds These Canonical Roles** |
|---|---|
| 1 | Chief Information Security Officer (CISO) |
| 2 | Governance Pillar Leader; Policy & Standards Manager; Risk Register Owner; Evidence Librarian; and the applicable Compliance Manager roles for regulators in scope |
| 3 | Risk Pillar Leader; Exposure Management Lead; Adversarial Testing Lead; Threat Intelligence Analyst; Vendor Risk Analyst; Detection Engineer |
| 4 | Engineering Pillar Leader; Cloud Security Engineer; Identity Engineer; Pre-production Reviewer |
| 5 | Application Security Engineer; Endpoint Engineer; Cryptography Engineer; OT Security Engineer where OT is in scope |

The Executive Sponsor is a business role, held by a business leader outside the security team in every team size. The Adjacent IR roles belong to the IR team.

### 8.3 The One Constraint That Does Not Scale Down

Risk-acceptance authority does not consolidate freely. The separation of the person who assesses a risk from the person who accepts it holds at every team size, per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. Where consolidation would put assessment and acceptance of a High or Critical risk in the same person, the Executive Sponsor provides the independent acceptance. A small team consolidates work; it does not consolidate away the second set of eyes on consequential risk.

> **A Consolidated Role Is Still an Owned Role**
>
> The point of the scaling map is that it changes nothing in the RACI. When person 3 on a five-person team holds six Risk roles, every process those six roles own still has exactly one Accountable role, and that role still has a name, and that name still maps to a person. The day the team hires a seventh person, a role lifts cleanly off person 3 and onto the new hire, because the role never stopped existing. This is why CERG consolidates roles and never deletes them. Deletion loses the work. Consolidation only stacks it, visibly, ready to be redistributed.

---

## 9. Maintaining This Instrument

1. **A new artifact is added to Section 5.** When an artifact is registered in [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md), a row is added to the Section 5 RACI in the same change.
2. **A new process is added to Section 6.** When a new standing process is established by a standard or procedure, its RACI row is added to Section 6.
3. **A roster change flows from the Operating Model.** A role is never added, renamed, or retired here. That happens in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1, and this instrument is then updated to match.
4. **Subordinate documents conform to this instrument.** A standard or procedure whose local roles table disagrees with this instrument is corrected on its next revision, per the precedence rule in Section 1.
5. **The instrument is reviewed annually.** The review confirms every row still has exactly one A, every role is still canonical, and the scaling map still reflects the role roster.

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-RAC-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to the canonical role roster or the artifact catalog |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); NIST 800-53r5 (PM, PS); ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-21 | Cyber Governance | Initial release. Consolidates the per-process RACI that CERG-GOV-OM-001 §9 deferred. Establishes RACI definitions and rules, a canonical role reference, a master RACI for document ownership, a master RACI for standing processes across engagement, risk, governance, and operations, normalized descriptions for all 27 canonical roles, and a scaling map showing role consolidation onto a five-person team. |

### Review Triggers

- A new artifact registered in [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md)
- A new standing process established by a standard or procedure
- Any change to the canonical role roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1
- A change to the risk-acceptance authority table in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Authoritative canonical role roster; the sample RACI this instrument completes |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Artifact inventory; per-type approval authority |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk-acceptance authority that this instrument does not override |
| Implementation and Adaptation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Role-consolidation principle that the scaling map makes concrete |
