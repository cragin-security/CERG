# CERG (surge) · Cybersecurity Operating Model

**A spine, not shelfware.**

CERG gives you the structure, artifacts, workflows, and evidence model to run a cybersecurity program. It does not become a program until you assign owners, run the cadence, make decisions, and produce evidence from real work.

Cybersecurity teams have struggled with the same structural problem for twenty years: fragmented tools, siloed teams, and a culture of "no" that slows the business without meaningfully reducing risk. CERG is a deliberate answer to that problem — an operating model where Engineering builds security in early, Risk understands actual exposure, and Governance makes the rules clear enough that work moves faster.

---

## Choose your adoption path

You do not adopt 70+ documents in week one. You adopt the spine first. Pick the path that matches your organization:

| Path | Audience | Starting set | First 30 days |
|------|----------|-------------|---------------|
| **CERG Lite** | Small security team (2-8 people) or early security function | MVC only (8 docs) + adoption aids | Policy, Framework, Operating Model, RMF, Risk Register, VM Procedure, Record Catalog |
| **CERG Standard** | Existing security team (6-30 people) | MVC + core standards + AR/TPRM | Lite start + Access, Asset, Config, IT/Cloud, Logging, Resilience standards; Architecture Review; TPRM |
| **CERG Regulated** | NERC-CIP, CMMC, SOX, OT environments | Standard + overlays/packages | Standard start + relevant operational packages (CIP, CUI/CMMC, SOX) |

### Minimum Viable CERG (the spine)

These eight documents constitute a real program. Everything else layers on after:

| Order | Artifact | What it does |
|-------|----------|--------------|
| 1 | Cybersecurity Policy | The durable principles everything hangs from. Sign this first. |
| 2 | CERG Framework | The three-pillar model the rest of the library assumes. |
| 3 | Operating Model | Pillars, decision rights, canonical roles. |
| 4 | Document Catalog | Your authoritative inventory. Update as you adopt. |
| 5 | Risk Management Framework | How risk is identified, scored, treated, accepted. |
| 6 | Risk Register & Exception Process | The first procedure that produces running work. |
| 7 | Risk Register Templates | The fill-in artifact that makes the register real. |
| 8 | Exposure Management Procedure | The second source of running work, and the one auditors look for first. |

**[START-HERE.md](START-HERE.md)** walks through the first 48 hours for each path.

### Adoption usability aids

If you are deciding what to adopt, what to defer, or what records to create, use these companion guides:

| Need | Artifact |
|------|----------|
| Understand how the whole library fits together | [Framework System Map](governance/CERG-GOV-FRM-002_Framework_System_Map.md) |
| Choose Lite, Standard, Regulated, and required overlays | [Adoption Decision Tree and Dependency Matrix](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) |
| Know what each role should do first | [Role-Based Implementation Checklists](governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) |
| Know which records and evidence to create | [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md) |

---

## What CERG is

Not a control framework. Not a compliance checklist. A cybersecurity operating model with the policies, standards, procedures, and evidence model a security function needs to produce real work.

### Three pillars. One accountability model.

Most control failures trace back to ambiguous ownership. CERG assigns every piece of security work to exactly one of three pillars:

**Cyber Engineering** — Build securely. Deploy confidently. Consult continuously.
Engineers embed in projects from first conversation through production handoff. They review architecture, drive pre-launch remediation, and ensure teams inheriting new systems know their security posture.

**Cyber Risk** — Know your exposure. Manage it deliberately. Never be surprised.
Risk hunts for problems rather than waiting for them to surface. Continuous exposure management, adversarial testing, threat intelligence, and vendor risk assessment. Pre-production findings are engineering inputs. Post-production findings are managed risks.

**Cyber Governance** — Set the rules. Track the work. Enable the business to move with confidence.
Governance defines what good looks like. Policy, standards, compliance tracking, control evidence, risk register, audit response. The operating philosophy is "yes, and…" — guardrails that make business movement faster, not slower.

### Philosophy

Regulatory alignment — NIST 800-53r5, NIST 800-171r3, NIST CSF 2.0, NERC-CIP, CMMC L2, SOX ITGC — is a byproduct of running the program well, not the point of it.

CERG's strongest idea is not the document library. It is the operating philosophy: Engineering builds security in early, Risk understands actual exposure, Governance makes the rules clear enough that work moves faster, and compliance becomes exhaust from good operations.

---

## Architecture overview

A visual map of how CERG's document categories, pillars, and cross-pillar flows connect: **[architecture.html](architecture.html)** (open in browser).

## Reader paths

Different roles need different entry points:

| Your Role | Start Here | Then Read |
|-----------|-----------|-----------|
| **CISO / Security Executive** | [Cybersecurity Policy](governance/CERG-POL-001_Cybersecurity_Policy.md) | [Framework System Map](governance/CERG-GOV-FRM-002_Framework_System_Map.md) → [Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md) → [Operating Model](governance/CERG-GOV-OM-001_CERG_Operating_Model.md) → [Metrics & Reporting](governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| **Governance / Compliance Lead** | [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md) → [RACI](governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) → [RMF](governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) → [Compliance Matrix](governance/CERG-GOV-CMX-001_Compliance_Matrix.md) |
| **Risk Lead** | [Risk Management Framework](governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) | [Exposure Management Procedure](procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) → [Risk Register](procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) → [Third-Party Risk](procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Engineering Lead** | [Architecture Intake](procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | [IT/Cloud Standard](standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) → [Access Standard](standards/CERG-STD-AC-001_Access_Management_Standard.md) → [Config Baseline](standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **Small Org Adopter (2-8 people)** | [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | [Decision Tree](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) → [Role Checklists](governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) → [Small Team Adoption Path](governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) |
| **Auditor / Assessor** | [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md) → [Control Baseline](governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) → [Evidence Procedure](procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) → [Compliance Matrix](governance/CERG-GOV-CMX-001_Compliance_Matrix.md) |

---

## Document inventory

The full corpus is cataloged in [CAT-001](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md). Key groupings:

- **Spine (8 docs)** — Policy, Framework, Operating Model, Catalog, RMF, Risk Register, Risk Templates, VM Procedure
- **Governance instruments (32 docs)** — Control Baseline, Compliance Matrix, Risk Taxonomy, Metrics, Calendar, Style Guide, Traceability, Evidence Quality, Maturity Assessment, Crown Jewel Register and Scenario Library, CERG Service-Level Commitments, and workforce documents (Job Architecture, Descriptions, Competency Model, Performance, Workforce Planning, Succession, Training, Onboarding, Contractor Integration, Program Improvement)
- **Adoption & scaling (6 docs)** — Implementation Guide, Adoption Safety Guide, Small Team Adoption Path, Implementation Cards, Adoption Decision Tree and Dependency Matrix, Role-Based Implementation Checklists
- **Standards (15 docs)** — Access, Configuration (DISH), Cryptography, CUI, IT/Cloud/SaaS, Logging/Monitoring, OT/Grid, Resilience/Backup, Asset Management, Data Governance, Network Segmentation, Endpoint/Mobile, Email/Messaging, AI Security, Secure Development
- **Procedures (12 docs)** — Architecture Review, Access Runbook, Adversarial Validation, Risk Register, TPRM, Exposure Management, Change Management, Audit/Evidence, Threat Intelligence, Threat Modeling, Lessons Learned
- **Operational packages (7 docs)** — Business Continuity, NERC-CIP, CUI/CMMC, SOX ITGC, ISO 27001, Privacy, IR Plan
- **Templates (10 docs)** — Risk Register, Exception Form, Risk Acceptance Memo, Intake Form, Evidence Worksheet, SSP, POA&M, Vendor Questionnaire, Board Deck, Stakeholder Survey
- **Workforce architecture (35 docs)** — 5 job families, 27 per-role descriptions, NICE crosswalk, Job Families Overview — all derived from 11 core capabilities (see [Operating Model](governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.0)
- **Machine-readable artifacts (14 YAML)** — Manifests, requirements, flows, record schemas, runtime model
- **Examples** — Sample organization profiles (small team, SaaS, regulated utility, MSP-heavy)

---

## Scales to fit you

The framework is designed to scale from a 5-person startup CERG to a large enterprise security function. Every team structure, headcount, and engagement model scales down — a 5-person team runs the same model with fewer people covering more pillars. The [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) and [Small Team Adoption Path](governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) provide concrete guidance for small organizations.

See [`/examples/`](examples/) for sample organization profiles across different sectors and sizes.

---

## For LLMs and automation

Every document is Markdown. The full corpus is available:

- **[llms.txt](https://cerg.nexus/llms.txt)** — document index for AI tools and crawlers
- **[llms-full.txt](https://cerg.nexus/llms-full.txt)** — full corpus concatenated into one file
- **[Bulk download](https://cerg.nexus/downloads/cerg-docs.zip)** — all documents as a single ZIP
- **[`machine-readable/`](machine-readable/)** — YAML manifests, atomic requirements, flow specifications, record schemas, and runtime models for LLM and automation ingestion

---

## Authoritative source

**The GitHub repository is authoritative.** The website at [cerg.nexus](https://cerg.nexus) is a convenience mirror and may lag the repo. Where the two differ, the repository controls.

---

## Document taxonomy

CERG documents fall into three categories:

| Category | Label | Meaning | Examples |
|----------|-------|---------|----------|
| **CERG Core** | (no label — default) | Owned, maintained, and governed by CERG. Subject to CERG review cycles, validation, and CI gates. | All POL, GOV, STD, PRC, PLN (non-IR), TMPL documents |
| **Adjacent Security Function Package** | ⚠ ADJACENT | Owned by a security function that operates alongside CERG (e.g., Incident Response, Security Awareness). Included in the CERG repository for integration clarity — so adopters can see how CERG interfaces with these functions. Not subject to CERG review cycles. | IR Plan (PLN-IR-001), IR Playbook Set (PRC-IR-002) |
| **Reference Artifact** | 📋 REFERENCE | Informational or illustrative material that is not a governed CERG artifact. Not subject to review cycles or CI gates. | Examples directory, sample profiles |

## Adjacent functions

These documents belong to functions that operate alongside CERG, not within it. They are included for integration clarity:

| Document | ID | Owned By | Category |
|----------|-----|----------|----------|
| Incident Response Plan | CERG-PLN-IR-001 | Standing IR Team / Incident Commander | ⚠ ADJACENT |
| Incident Response Playbook Set | CERG-PRC-IR-002 | Standing IR Team / Incident Commander | ⚠ ADJACENT |

During an incident, the standing IR team's procedures and the Incident Commander's authority take precedence over any CERG workflow. CERG's role during an incident is supporting: evidence collection, reporting, and lessons-learned feedback per [FLOW-001](governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-06. IR team roles (Incident Commander, Lead Investigator) are included in the role catalog for cross-reference only — they are not CERG positions.

---

## When CERG is not a good fit

CERG requires organizational commitment. It may not be the right choice if:

- You have no named executive sponsor or security owner
- Your organization only wants certification paperwork, not operational security
- You cannot name asset owners or business owners for risk acceptance
- You want security to absorb all business risk without business accountability
- You cannot tolerate documented exceptions or formal risk acceptance
- You intend to hand-edit documents without version control
- You lack a vulnerability scanner, identity provider, or asset inventory

In these cases, start with a lighter framework (NIST CSF, CIS Controls) and adopt CERG when organizational readiness supports it.

---

> **CERG is not a certification scheme.** An organization may adopt CERG and still fail a regulatory assessment if controls are not implemented and evidenced. CERG provides a framework and sample operating artifacts. It does not determine legal obligations, registered-entity status, contract scope, or certification readiness. Organizations must validate regulatory applicability with qualified counsel, compliance leadership, and assessors.

## Contributing

CERG is open source and contributions are welcome.

**Ways to contribute:**
- Improve existing documents (fix gaps, clarify language, add cross-references)
- Propose new documents (standards, procedures, templates, example profiles)
- Report bugs (broken links, catalog errors, validation failures)
- Suggest structural improvements

**[CONTRIBUTING.md](CONTRIBUTING.md)** has the full details: document conventions, the review process, how to register new domain codes, and what the CI checks.

**[Open an issue](https://github.com/m0dernz/CERG/issues/new/choose)** — we have templates for document improvements, new document proposals, and validation errors.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — fork freely, adapt openly, attribute generously.
