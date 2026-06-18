## ROLE READER PATHS
### Sequenced Reading Orders for New CERG Roles · CISO, Risk Lead, Engineering Lead

---

| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-007 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On adoption-architecture change |
| **Frameworks** | NIST CSF 2.0 (GOVERN: Organizational Context) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The Reader Path Format](#2-the-reader-path-format)
3. [CISO Reader Path](#3-ciso-reader-path)
4. [Risk Lead Reader Path](#4-risk-lead-reader-path)
5. [Engineering Lead Reader Path](#5-engineering-lead-reader-path)
6. [When to Skip the Path](#6-when-to-skip-the-path)
7. [Document Control](#7-document-control)

---

## 1. Purpose and Scope

CERG is intentionally complete. That completeness can make the first hour difficult for a new reader. This document is the antidote.

Each section below is a sequenced reading order for a specific role. The order is chosen because each document in the sequence builds on the previous one. Total time for the CISO path is approximately 35 minutes. Total time for the Risk and Engineering paths is approximately 30 minutes each.

Use this document when:

- A new CISO, Risk Lead, or Engineering Lead joins a team that has adopted CERG.
- An existing leader takes on a new CERG role for the first time.
- An executive sponsor wants to understand what the leader they hired will be reading.

This document does not replace the documents it points at. It tells the reader which document to open next and why.

## 2. The Reader Path Format

Each reader path follows the same format:

| Field | Meaning |
|---|---|
| **Read time** | Approximate minutes for the focused reader |
| **Goal** | What the reader should be able to do or say after finishing |
| **Sequence** | Documents in the order to read them, with a one-line reason before each |
| **Skip if** | Conditions under which a step can be omitted |
| **After the path** | What to do once the sequence is complete |

The reader path is a reading list, not an action list. For action items, see the role-based implementation checklists ([`CERG-GOV-IMP-006`](CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md)). For the adoption-mode selection that determines which reader path is relevant, see [`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md).

## 3. CISO Reader Path

**Read time:** 35 minutes.

**Goal:** You can explain the CERG program to a board member in five minutes, name the three pillars and what each one owns, identify your adoption mode (Lite, Standard, Regulated), and produce your first quarterly oversight checklist.

**Sequence:**

| # | Document | Time | Why this comes next |
|---|----------|------|---------------------|
| 1 | [`README.md`](../README.md) | 5 min | Establishes what CERG is and what it is not. The mission statement, the three pillars, and the link to [START-HERE.md](../START-HERE.md). |
| 2 | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | 5 min | The narrative Framework. Explains the conceptual organization: principles, three pillars, operating layers, value driver maturity. |
| 3 | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6 only | 5 min | Role consolidation for small teams. If you are CERG Lite, §6 tells you which canonical roles collapse onto which people. If you are Standard or Regulated, skim §6 to understand the consolidation logic and then move on. |
| 4 | [`CERG-GOV-FRM-002`](CERG-GOV-FRM-002_Framework_System_Map.md) | 5 min | The system map. Front door for the rest of the library. Use it as a navigation reference, not a cover-to-cover read. |
| 5 | [`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) | 5 min | The decision tree and dependency matrix. Pick your adoption mode (Lite, Standard, Regulated) and learn what must be adopted together. |
| 6 | [`CERG-GOV-IMP-006`](CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) §3 | 5 min | The CISO checklist at 48 hours, 30 days, and 90 days. This is your action list once the reading is done. |
| 7 | [Day in the Life Story 10](../examples/day-in-the-life/story-10-new-ciso-90-days.md) | 5 min | A worked example: another new CISO's first 90 days. Read this last, when the framework is in your head, to see it all in motion. |

**Skip if:**

- You have held a CISO role at a CERG-adopting organization before. Skip step 7 and read steps 1-6 only.
- You are CERG Lite with fewer than 5 people. Spend the OM-001 time on the consolidation map (step 3) and the Small Team Adoption Path ([`CERG-GOV-IMP-003`](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md)) instead of the Operating Model detail.

**After the path:**

1. Run [`CERG-GOV-IMP-006`](CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) §3.1 (First 48 hours) immediately. The reader path is preparation, not a substitute.
2. Schedule the first 30-day review (step §3.2) before the 30th day.
3. Bookmark [`CERG-GOV-FRM-002`](CERG-GOV-FRM-002_Framework_System_Map.md) for the duration of your tenure. It is the navigation reference.
4. Add the [Day in the Life stories](../examples/day-in-the-life/README.md) to your onboarding checklist for future new hires on your team.

## 4. Risk Lead Reader Path

**Read time:** 30 minutes.

**Goal:** You can name the risk pillar's scope (exposure management, threat intelligence, threat modeling, adversarial validation, vendor risk), describe the canonical cross-pillar flows, and triage a critical finding from intake to closure.

**Sequence:**

| # | Document | Time | Why this comes next |
|---|----------|------|---------------------|
| 1 | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) §3-4 | 5 min | Risk pillar scope within the framework narrative. |
| 2 | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | 8 min | Risk taxonomy, scoring, treatment, acceptance, monitoring. The Risk pillar's parent governance instrument. |
| 3 | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-04 | 5 min | The Finding to Remediation flow. The Risk pillar's most-used flow. Read the SLA and decision logic carefully. |
| 4 | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | 5 min | The Exposure Management Procedure. Your operating procedure for vulnerability and finding work. |
| 5 | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | 5 min | The TPRM Procedure. Your operating procedure for vendor risk. |
| 6 | [Day in the Life Story 2](../examples/day-in-the-life/README.md#story-2-critical-vulnerability) | 2 min | A critical vulnerability walked end to end through F-04. Read this last, when the framework is in your head, to see it all in motion. |

**Skip if:**

- You have held a Risk Lead role at a CERG-adopting organization before. Skip step 6.

**After the path:**

1. Open the risk register and the exposure backlog. Read both before the next weekly cadence.
2. Run the biweekly vulnerability SLA review per [`CERG-GOV-IMP-003`](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) §3.
3. Bookmark [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) §1 (Operating Principles) for reference.

## 5. Engineering Lead Reader Path

**Read time:** 30 minutes.

**Goal:** You can name the engineering pillar's scope (architecture review, asset coverage, configuration baseline, secure development, remediation), describe how a project goes through intake to disposition, and route a high-risk architecture review correctly.

**Sequence:**

| # | Document | Time | Why this comes next |
|---|----------|------|---------------------|
| 1 | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) §3-4 | 5 min | Engineering pillar scope within the framework narrative. |
| 2 | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §4-5 | 5 min | Engineering pillar ownership of the consulting model and architecture review. |
| 3 | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-02 | 5 min | The Project Intake, Architecture Review, and Threat Modeling flow. The Engineering pillar's most-used flow. Read the tier routing carefully. |
| 4 | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | 5 min | The Architecture Review and Project Intake Procedure. Your operating procedure for project intake work. |
| 5 | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | 5 min | The Secure Configuration Baseline (DISH). Your default hardening reference for new systems. |
| 6 | [Day in the Life Story 1](../examples/day-in-the-life/README.md#story-1-new-saas-application) | 5 min | A new SaaS application walked through F-02 end to end. Read this last, when the framework is in your head, to see it all in motion. |

**Skip if:**

- You have held an Engineering Lead role at a CERG-adopting organization before. Skip step 6.

**After the path:**

1. Open the architecture review queue and the asset coverage report. Read both before the next weekly cadence.
2. Run the weekly intake review per [`CERG-GOV-IMP-003`](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) §3.
3. Bookmark the standards catalog ([`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) §5.3) for the standards you are most likely to apply this quarter.

## 6. When to Skip the Path

Reader paths are for new readers. Skip them if:

- You are the **executive sponsor**, not a CERG role. Read [README.md](../README.md), [START-HERE.md](../START-HERE.md) Path selection, and [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §3 (Board Reporting). Total time: 15 minutes.
- You are a **program-level contributor** (auditor, consultant, advisor). Read [README.md](../README.md), [`CERG-GOV-FRM-002`](CERG-GOV-FRM-002_Framework_System_Map.md), and one Day in the Life story relevant to your engagement. Total time: 20 minutes.
- You have **already adopted CERG and run it for six months or more**. Use [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) §5 as your reference, not the reader path.

The reader paths are designed for the first hour of engagement. They are not a substitute for the operating rhythm that follows.

## 7. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-IMP-007 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-18 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On adoption-architecture change |
| **Next Scheduled Review** | 2027-06-18 |
| **Frameworks** | NIST CSF 2.0 (GOVERN: Organizational Context) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

### Revision History

| **Version** | **Date** | **Author** | **Change** |
|---|---|---|---|
| 1.0 | 2026-06-18 | Governance Pillar Leader (Policy & Standards) | Initial publication. Establishes sequenced reading orders for the CISO, Risk Lead, and Engineering Lead roles. Each path totals 30-35 minutes and points at the documents the new reader needs in the order each builds on the previous. |

### Review Triggers

- A change to the role consolidation map in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md).
- A change to the canonical cross-pillar flows in [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md).
- A new role added to the workforce architecture in [`roles/`](../roles/) that warrants its own reader path.
- A material change to adoption sequencing in [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) or [`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md).
- User feedback indicating the path is too long, too short, or in the wrong order.

### Related Documents

- [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) - Implementation and Adaptation Guide
- [`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) - Adoption Decision Tree and Dependency Matrix
- [`CERG-GOV-IMP-006`](CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) - Role-Based Implementation Checklists (action lists)
- [`CERG-GOV-FRM-002`](CERG-GOV-FRM-002_Framework_System_Map.md) - Framework System Map (navigation reference)
- [`README.md`](../README.md) - Top-level project README
- [`START-HERE.md`](../START-HERE.md) - First-48-hours adoption guide
- [`examples/day-in-the-life/`](../examples/day-in-the-life/README.md) - Worked examples referenced from each reader path
