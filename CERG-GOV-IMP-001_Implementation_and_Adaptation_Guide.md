
# SURGE: Cyber Engineering, Risk & Governance

## IMPLEMENTATION AND ADAPTATION GUIDE
### The On-Ramp: Fork, Adapt, Run

---

| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) · [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) |
| **Review Cycle** | Annual / On any change to the V1 library |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Before You Start](#2-before-you-start)
3. [The Adoption Model](#3-the-adoption-model)
4. [Minimum Viable CERG](#4-minimum-viable-cerg)
5. [The 30/60/90-Day Rollout](#5-the-306090-day-rollout)
6. [Scaling the Model: 5 People to 60](#6-scaling-the-model-5-people-to-60)
7. [Adapting the Documents](#7-adapting-the-documents)
8. [First-Adoption Sign-Off Workflow](#8-first-adoption-sign-off-workflow)
9. [Common Adoption Pitfalls](#9-common-adoption-pitfalls)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

CERG is a security program in a box. The box is full. What it has been missing is the on-ramp: a single document that tells an organization which has just forked the repository what to do on Monday morning.

This is that document. It is the first thing a new adopter should read after the [README](README.md) and the [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) framework narrative.

It applies to any organization adopting CERG, whether that organization is standing up a security function for the first time, replacing a pile of disconnected policies, or formalizing a program that has run on tribal knowledge. It does not assume a large team, a big budget, or an existing document library.

> **What This Guide Is Not**
>
> This is not a maturity model and it is not a control catalog. The maturity self-assessment is [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md); the control set is [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md). This guide is the sequencing layer that tells you the order to do things in. Read it once, then keep it open during the first 90 days.

---

## 2. Before You Start

CERG adoption needs four things in place. None of them is a tool or a budget line.

| **Prerequisite** | **Why It Matters** | **Minimum Bar** |
|---|---|---|
| A named accountable owner | Someone has to own the program. Ambiguous ownership is the failure mode CERG exists to fix. | One person carries the **Chief Information Security Officer (CISO)** role, even part-time, even if the title is informal. |
| Executive endorsement | The "yes, and..." operating model only works if leadership backs the guardrails. | One **Executive Sponsor** who will sign the adopted Cybersecurity Policy. |
| A content repository | CERG is Markdown. It needs a home where versions are tracked. | A Git repository, a wiki with history, or a controlled document store. |
| Honest scope | You cannot protect what you have not named. | A rough list of systems, business units, and regulators in scope. |

If any of the four is missing, fix that first. Adopting the documents on top of an absent owner or an absent repository produces a library, not a program.

> **The Owner Comes First**
>
> The most common adoption failure is treating CERG as a documentation exercise. It is not. Before a single file is edited, one person must hold the CISO role and one Executive Sponsor must agree to endorse the policy. Everything else in this guide assumes those two seats are filled.

---

## 3. The Adoption Model

CERG adoption has three moves. They are deliberately simple.

### 3.1 Fork

Take a copy of the entire V1 library. Do not cherry-pick individual files on day one. The documents are interconnected; a standard cites a procedure, a procedure cites the operating model, the operating model cites the policy. A partial fork breaks cross-references and produces exactly the fragmentation CERG was built to remove.

Fork the whole thing. Decide what to defer later, in the open, as a recorded decision.

### 3.2 Adapt

Adaptation is mechanical, not creative. Every place the documents name an organization, a headcount, a regulator, or an example is a variable. [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) defines the full token scheme and ships a render tool that turns the generic corpus into an organization-specific one. Use it. Do not hand-edit 28 documents.

What you do change by hand is judgment: which optional standards apply, which regulators are in scope, where the team structure consolidates. Section 6 and Section 7 cover both.

### 3.3 Run

A program runs when work is happening on the cadence the documents describe: intake reviews, risk register updates, vulnerability SLAs, metrics reporting. Adoption is complete not when the files are edited but when the first cycle of that cadence has been completed and reported. Section 5 sequences the first cycle.

> **One Source, Many Exports**
>
> The authoritative copy of every adopted CERG document is the Markdown file in your repository. Word exports, PDF deliverables, intranet pages, and regulator uploads are exports. This rule is inherited from [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) and it matters from day one. If you start editing a Word copy, you have already lost version control.

---

## 4. Minimum Viable CERG

You do not adopt 28 documents in week one. You adopt the spine first. Minimum Viable CERG (MVC) is the smallest set of artifacts that constitutes a real program. Everything else is layered on after.

### 4.1 The MVC Set

| **Order** | **Artifact** | **ID** | **Why It Is in the Spine** |
|---|---|---|---|
| 1 | Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | The durable principles everything else hangs from. Nothing is authoritative until this is signed. |
| 2 | CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Explains the three-pillar model the rest of the library assumes. |
| 3 | Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines pillars, decision rights, and the canonical role roster. |
| 4 | Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Your authoritative inventory. Update it as you adopt. |
| 5 | Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | How risk is identified, scored, treated, and accepted. |
| 6 | Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | The first procedure that produces running work. |
| 7 | Risk Register Templates | [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | The fill-in artifact that makes the register real. |
| 8 | Vulnerability Management Procedure | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | The second source of running work, and the one auditors look for first. |

Eight artifacts. A policy, three governance instruments, a framework, two procedures, and a template. That is a program. It has an owner, a way to record risk, and a way to drive remediation.

### 4.2 What MVC Deliberately Defers

The standards (Access Management, Logging, Cryptography, and the rest), the operational packages (NERC-CIP, CUI/CMMC, SOX), and the remaining procedures are layered in after the spine runs one full cycle. They are not optional in the long run. They are sequenced.

> **Resist the Big-Bang Adoption**
>
> The temptation is to adapt all 28 documents, approve them in one meeting, and announce the program. That adoption never runs. The team drowns in review and the cadence never starts. Adopt the eight-artifact spine, run it for 30 days, prove the cadence works, then layer. A small program that runs beats a complete program that sits.

---

## 5. The 30/60/90-Day Rollout

This is the sequence for a first adoption. Dates are guidance; the order is not.

### 5.1 Days 1 to 30: Stand Up the Spine

| **Step** | **Action** | **Lead Role** |
|---|---|---|
| 1 | Fork the full V1 library into your content repository. | Governance Pillar Leader |
| 2 | Build the organization profile and run the render tool per [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md). | Policy & Standards Manager |
| 3 | Review and adapt the eight MVC artifacts (Section 4.1). | Governance Pillar Leader |
| 4 | Baseline current maturity using [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md). | CISO |
| 5 | CISO signs the Cybersecurity Policy; Executive Sponsor endorses. | CISO |
| 6 | Stand up the risk register; load known risks from the maturity baseline. | Risk Register Owner |
| 7 | Run the first Monthly Risk Register Review. | Risk Register Owner |

By day 30 the program has a signed policy, a populated risk register, a maturity baseline, and one completed review cycle. That is the floor.

### 5.2 Days 31 to 60: Add the Operating Layer

| **Step** | **Action** | **Lead Role** |
|---|---|---|
| 8 | Adopt the standards that match your environment (Section 7.2). | Governance Pillar Leader |
| 9 | Adopt the Architecture Review and Project Intake Procedure [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). | Engineering Pillar Leader |
| 10 | Stand up vulnerability management against [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) SLAs. | Vulnerability Management Lead |
| 11 | Adopt the Access Management Standard [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) and its runbook [`CERG-PRC-AC-002`](CERG-PRC-AC-002_Access_Management_Runbook.md). | Identity Engineer |
| 12 | Route the first real project through architecture review. | Engineering Pillar Leader |

### 5.3 Days 61 to 90: Close the Loop

| **Step** | **Action** | **Lead Role** |
|---|---|---|
| 13 | Adopt [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md); publish the first CISO dashboard. | Governance Pillar Leader |
| 14 | Adopt the operational package for each regulator in scope (Section 7.3). | Governance Pillar Leader |
| 15 | Adopt remaining procedures: third-party risk, adversarial validation. | Risk Pillar Leader |
| 16 | Run the first Quarterly Cyber Oversight Group brief. | CISO |
| 17 | Re-run [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md); compare to the day-1 baseline. | CISO |

By day 90 every pillar is producing work, the CISO is reporting on a cadence, and the maturity score has moved. That is a running program.

> **The 90-Day Test**
>
> At day 90, ask one question: if an auditor walked in, could you show them a signed policy, a current risk register, vulnerability SLAs being met, and a CISO report with a trend line? If yes, CERG is running. If no, find the step that did not happen and finish it before adopting anything new.

---

## 6. Scaling the Model: 5 People to 60

The README promises a five-person team runs the same model as a sixty-person team. This section shows how. The mechanism is role consolidation, not document deletion.

### 6.1 The Principle

The canonical role roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1 lists every role CERG names. A small team does not delete roles. It assigns several roles to one person. The documents do not change; the **assignment map** changes. One person can hold the CISO role, the Governance Pillar Leader role, and the Risk Register Owner role at once. The work of each role still happens; it happens in one head.

> **Consolidate Roles, Never Delete Them**
>
> When a role is deleted, the work it owned silently stops. When a role is consolidated onto a person already carrying three others, the work is still owned, still visible, and still re-assignable the day a fourth person is hired. Always consolidate. The role roster is fixed; only the assignment map scales.

### 6.2 Reference Assignment Maps

These are starting points, not mandates. Adjust to the skills you actually have.

**Five-person team.** Every person carries a pillar plus shared duties.

| **Person** | **Holds These Canonical Roles** |
|---|---|
| 1 | CISO; Executive Sponsor liaison |
| 2 | Governance Pillar Leader; Policy & Standards Manager; Risk Register Owner; Evidence Librarian |
| 3 | Risk Pillar Leader; Vulnerability Management Lead; Threat Intelligence Analyst |
| 4 | Engineering Pillar Leader; Cloud Security Engineer; Identity Engineer; Pre-production Reviewer |
| 5 | Application Security Engineer; Endpoint Engineer; Cryptography Engineer; Detection Engineer |

**Fifteen-person team.** Pillar leaders are dedicated; senior practitioners own a domain each; the rest are individual contributors. Compliance manager roles are assigned only for regulators in scope.

**Sixty-person team.** The full roster maps roughly one role to one person, with sub-role domain qualifiers (for example, Engineering Pillar Leader - Cloud and Engineering Pillar Leader - OT) split out as described in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

### 6.3 What Does Not Scale Down

Two things hold regardless of headcount.

1. **Separation of approval authority.** The person who accepts a risk cannot be the only person who assessed it. Even on a five-person team, risk acceptance follows the authority table in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. If one person genuinely holds every role, the Executive Sponsor provides the second set of eyes on High and Critical acceptance.
2. **The cadence.** A five-person team still runs the Monthly Risk Register Review and the Quarterly Cyber Oversight Group brief. The meetings are shorter. They are not skipped.

---

## 7. Adapting the Documents

### 7.1 Mechanical Adaptation

Names, headcounts, regulators, and illustrative examples are variables. They are adapted with the token scheme and render tool defined in [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md). Do not hand-edit. Build the organization profile once, render the corpus, review the output.

### 7.2 Choosing Standards

Adopt every standard whose environment you operate. Skip none that apply.

| **Standard** | **ID** | **Adopt If** |
|---|---|---|
| IT / Cloud / SaaS Security | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | You run any cloud or SaaS. Nearly everyone. |
| Grid Control Systems Security | [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | You operate operational technology or industrial control systems. |
| CUI Handling | [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md) | You handle Controlled Unclassified Information or pursue CMMC. |
| Access Management | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Always. Every organization has identities. |
| Secure Configuration Baseline | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Always. Every organization has systems to harden. |
| Logging, Monitoring, and Detection | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Always. |
| Cyber Resilience and Backup | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Always. |
| Cryptography and Key Management | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Always. |

If you defer a standard, record the decision and a target adoption date in the risk register. A deferred standard is an accepted risk, not a silent gap.

### 7.3 Choosing Operational Packages

Operational packages are adopted per regulator. Adopt only what applies to you.

| **Package** | **ID** | **Adopt If** |
|---|---|---|
| NERC-CIP | [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | You are a registered entity under NERC-CIP. |
| CUI / CMMC | [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | You are pursuing CMMC certification. |
| SOX ITGC | [`CERG-PLN-SOX-001`](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | You are a public company subject to SOX. |
| Incident Response Plan | [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) | Always. Note this plan is owned by a standing IR team, not by CERG; see [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4. |

### 7.4 Keep the Catalog Honest

Every adoption decision updates your copy of [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md). An artifact you adopted is `Approved` in your catalog. An artifact you deferred is `Planned`. The catalog is the one place anyone can see what your program actually consists of. Letting it drift is the first sign the program is becoming a library again.

---

## 8. First-Adoption Sign-Off Workflow

A first adoption is approved once, as a package. After that, individual documents follow the per-type approval authority in [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) §4.

| **Step** | **What Happens** | **Authority** |
|---|---|---|
| 1 | Governance Pillar Leader confirms the MVC spine is adapted and the render output reviewed. | Governance Pillar Leader |
| 2 | Each pillar leader confirms the artifacts assigned to their pillar are accurate for the organization. | Engineering / Risk / Governance Pillar Leaders |
| 3 | CISO reviews the maturity baseline and the adoption scope, including every deferred artifact. | CISO |
| 4 | CISO approves the Cybersecurity Policy. Executive Sponsor endorses it. | CISO; Executive Sponsor |
| 5 | Governance Pillar Leader records the adoption in the catalog revision history and sets each artifact status. | Governance Pillar Leader |

The adoption is complete when step 5 is recorded. Not before.

---

## 9. Common Adoption Pitfalls

| **Pitfall** | **Why It Happens** | **The Fix** |
|---|---|---|
| Big-bang adoption | The library looks complete, so the team tries to approve all of it at once. | Adopt the MVC spine. Layer the rest. Section 4. |
| Editing exports | Someone opens a Word copy and edits it. | The Markdown source is authoritative. Exports are downstream. Section 3.3. |
| Inventing roles | The team writes a role name that feels natural instead of using the roster. | Use only canonical roles from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1. Consolidate, never invent. |
| Deleting roles to "fit" a small team | The roster looks too big for five people. | Consolidate roles onto people. The roster is fixed. Section 6.1. |
| Skipping the cadence | The reviews feel like overhead before the program is "ready." | The cadence is the program. A short review is still a review. Section 6.3. |
| Silent gaps | A standard is deferred and never recorded. | Every deferral is a risk register entry with a target date. Section 7.2. |
| Catalog drift | The catalog is not updated as documents are adopted. | The catalog is updated at sign-off and on every later change. Section 7.4. |
| Treating CERG as documentation | Files get adapted; no work starts. | Adoption completes when the first cadence cycle is reported, not when files are edited. Section 3.3. |

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-IMP-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | Chief Information Security Officer (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to the V1 library |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-21 | Cyber Governance | Initial release. Establishes the adoption model (fork, adapt, run), the Minimum Viable CERG spine, the 30/60/90-day rollout, the role-consolidation approach to scaling, document-adaptation guidance, the first-adoption sign-off workflow, and the adoption pitfalls register. |

### Review Triggers

- Any artifact added to or retired from the V1 library
- Material change to the canonical role roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1
- Material change to the token scheme in [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md)
- Adopter feedback indicating a sequencing or scaling gap
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Document Control) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative artifact inventory; adoption updates the catalog |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster used by the scaling guidance |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Narrative framework an adopter reads before this guide |
| Organization Adaptation Profile | [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Token scheme and render tool used in mechanical adaptation |
| Maturity Self-Assessment and Scorecard | [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | Day-1 baseline and day-90 re-measurement |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk acceptance authority cited by the scaling guidance |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | The control set layered in after the MVC spine |
