# CERG (surge) · Cybersecurity Operating Model

**A spine, not shelfware.**

CERG gives you the structure, artifacts, workflows, and evidence model to run a cybersecurity program. It does not become a program until you assign owners, run the cadence, make decisions, and produce evidence from real work.

Cybersecurity teams have struggled with the same structural problem for twenty years: fragmented tools, siloed teams, and a culture of "no" that slows the business without meaningfully reducing risk. CERG is a deliberate answer to that problem — an operating model where Engineering builds security in early, Risk understands actual exposure, and Governance makes the rules clear enough that work moves faster.

---

## What CERG is

CERG is not a control framework or compliance checklist. It is a cybersecurity operating model with the policies, standards, procedures, templates, workflows, and evidence model a security function needs to produce real work.

Regulatory alignment — NIST 800-53r5, NIST 800-171r3, NIST CSF 2.0, NERC-CIP, CMMC L2, SOX ITGC — is a byproduct of running the program well, not the point of it.

---

## The operating model

Most control failures trace back to ambiguous ownership. CERG assigns every piece of security work to one of three pillars:

- **Cyber Engineering** — Build securely. Deploy confidently. Consult continuously.
- **Cyber Risk** — Know your exposure. Manage it deliberately. Never be surprised.
- **Cyber Governance** — Set the rules. Track the work. Enable the business to move with confidence.

CERG's core philosophy is that Engineering builds security in early, Risk understands actual exposure, Governance makes the rules clear enough that work moves faster, and compliance becomes exhaust from good operations.

---

## How to use this repository

| I want to... | Go here |
|-------------|---------|
| Adopt CERG for the first time | [START-HERE.md](START-HERE.md) |
| Choose Lite, Standard, or Regulated adoption | [Adoption Decision Tree and Dependency Matrix](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) |
| Understand how the library fits together | [Framework System Map](governance/CERG-GOV-FRM-002_Framework_System_Map.md) and [architecture.html](architecture.html) |
| See the authoritative document inventory | [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) |
| Find required records and evidence | [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md) |
| Understand roles and decision rights | [Operating Model](governance/CERG-GOV-OM-001_CERG_Operating_Model.md) and [RACI](governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) |
| Use CERG with automation or LLMs | [`machine-readable/`](machine-readable/), [llms.txt](https://cerg.nexus/llms.txt), and [llms-full.txt](https://cerg.nexus/llms-full.txt) |
| Contribute | [CONTRIBUTING.md](CONTRIBUTING.md) |

---

## Adoption modes

You do not adopt 70+ documents in week one. CERG can be adopted in three modes:

- **CERG Lite** — minimum viable program for a small team or early security function.
- **CERG Standard** — core operating model for an established security team.
- **CERG Regulated** — Standard plus overlays for NERC-CIP, CMMC, SOX, OT, or other regulated environments.

Start with [START-HERE.md](START-HERE.md). It walks through the first 48 hours and points to the right adoption path.

### Minimum Viable CERG

The minimum viable CERG spine includes:

1. Cybersecurity Policy
2. CERG Framework
3. Operating Model
4. Document Catalog
5. Risk Management Framework
6. Risk Register and Exception Process
7. Risk Register Templates
8. Exposure Management Procedure

Everything else layers on after the spine is owned, adopted, and producing evidence.

---

## What is included

CERG includes:

- **Governance artifacts** — policy, framework, operating model, catalogs, control baseline, compliance matrix, metrics, RACI, traceability, maturity, and workforce governance.
- **Standards** — access, asset, configuration, cryptography, data, endpoint, IT/cloud/SaaS, logging, network, resilience, secure development, AI, OT, and related security standards.
- **Procedures** — architecture review, exposure management, risk register, third-party risk, audit/evidence, change management, threat intelligence, threat modeling, adversarial validation, access, and lessons learned.
- **Operational packages** — business continuity, NERC-CIP, CUI/CMMC, SOX ITGC, ISO 27001, privacy, and incident response integration artifacts.
- **Templates** — risk, exception, acceptance, intake, evidence, SSP, POA&M, vendor assessment, board reporting, and stakeholder survey templates.
- **Workforce architecture** — job families, role descriptions, NICE crosswalks, competency model, workforce planning, onboarding, training, performance, and succession artifacts.
- **Machine-readable artifacts** — manifests, requirements, flow specifications, evidence schemas, record schemas, runtime models, and related YAML/JSON files.
- **Examples** — sample organization profiles for different sectors and sizes.

The full inventory is maintained in the [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md).

---

## Automation and machine-readable use

Every CERG document is Markdown. Automation-oriented artifacts are available here:

- **[llms.txt](https://cerg.nexus/llms.txt)** — document index for AI tools and crawlers.
- **[llms-full.txt](https://cerg.nexus/llms-full.txt)** — full corpus concatenated into one file.
- **[Bulk download](https://cerg.nexus/downloads/cerg-docs.zip)** — all documents as a single ZIP.
- **[`machine-readable/`](machine-readable/)** — YAML manifests, atomic requirements, flow specifications, record schemas, and runtime models.

---

## Source of truth

**The GitHub repository is authoritative.** The website at [cerg.nexus](https://cerg.nexus) is a convenience mirror and may lag the repo. Where the two differ, the repository controls.

---

## Scope notes

Most CERG documents are core operating-model artifacts. A small number are included only to clarify handoffs with adjacent security functions, such as Incident Response. During an incident, the standing IR team and Incident Commander retain authority; CERG supports evidence collection, reporting, and lessons-learned feedback.

The [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) is authoritative for document classification and ownership.

### When CERG is not a good fit

CERG requires organizational commitment. It may not be the right choice if you have no named executive sponsor or security owner, only want certification paperwork, cannot identify business owners for risk acceptance, cannot tolerate documented exceptions, or intend to manage documents without version control.

In these cases, start with a lighter framework such as NIST CSF or CIS Controls and adopt CERG when organizational readiness supports it.

> **CERG is not a certification scheme.** An organization may adopt CERG and still fail a regulatory assessment if controls are not implemented and evidenced. CERG provides a framework and sample operating artifacts. It does not determine legal obligations, registered-entity status, contract scope, or certification readiness. Organizations must validate regulatory applicability with qualified counsel, compliance leadership, and assessors.

---

## Contributing

CERG is open source and contributions are welcome. You can improve existing documents, propose new artifacts, report broken links or validation failures, and suggest structural improvements.

See [CONTRIBUTING.md](CONTRIBUTING.md) for document conventions, the review process, domain-code registration, and CI expectations.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — fork freely, adapt openly, attribute generously.
