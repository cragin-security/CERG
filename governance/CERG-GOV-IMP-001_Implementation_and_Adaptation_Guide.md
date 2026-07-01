## IMPLEMENTATION AND ADAPTATION GUIDE
### The On-Ramp: Fork, Adapt, Run · Talent Brand · Interview Guide


---

> **Not Legal or Regulatory Advice.** CERG provides a framework and sample operating artifacts. It does not determine legal obligations, registered-entity status, contract scope, or certification readiness. Organizations must validate regulatory applicability with qualified counsel, compliance leadership, and assessors. References to NERC-CIP, CMMC, SOX, ISO 27001, and privacy regulations are for integration mapping — they do not constitute compliance claims.


| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-001 |
| **Version** | 1.11 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) · [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) · [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) · [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) |
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
6. [Scaling the Model: Consolidate, Then Split](#6-scaling-the-model-consolidate-then-split)
7. [Adapting the Documents](#7-adapting-the-documents)
8. [First-Adoption Sign-Off Workflow](#8-first-adoption-sign-off-workflow)
9. [Common Adoption Pitfalls](#9-common-adoption-pitfalls)
10. [Employer Brand and Talent Attraction](#10-employer-brand-and-talent-attraction)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

CERG is a cybersecurity operating model starter kit — the spine, artifacts, workflows, and evidence model to run a program. What it has needed is a clear on-ramp: a single document that tells an organization which has just forked the repository what to do on Monday morning.

This is that document. It is the first thing a new adopter should read after the [README](../README.md) and the [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) framework narrative.

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

### 3.4 Operating Leverage Test

CERG adoption should reduce coordination drag. If adoption creates more meetings, more manual status chasing, or more ambiguous ownership, the organization is probably adopting documents without adopting the operating model.

Look for operating leverage by the end of the first cycle:

- recurring decisions have named owners and records;
- common security questions stop being re-litigated because standards answer them;
- evidence is produced by normal work instead of reconstructed later;
- handoffs between Engineering, Risk, and Governance are visible;
- staffing conversations are based on workload and capability gaps, not vague pressure;
- fewer issues require heroics from the same senior person.

If CERG is not creating leverage, stop adding artifacts and fix the workflow that is creating drag.

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
| 6 | Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | The first procedure that produces running work. |
| 7 | Risk Register Templates | [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | The fill-in artifact that makes the register real. |
| 8 | Exposure Management Procedure | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | The second source of running work, and the one auditors look for first. |

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
| 9 | Adopt the Architecture Review and Project Intake Procedure [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). | Engineering Pillar Leader |
| 10 | Stand up exposure management against [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) SLAs. | Exposure Management Lead |
| 11 | Adopt the Access Management Standard [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) and its runbook [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md). | Identity Engineer |
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

> **Gate 2→3 Transition Criteria**
>
> Day-90 readiness is a necessary condition for full adoption but not sufficient. Before layering on standards, operational packages, and remaining procedures, the organization should demonstrate stable operating cadence defined in [`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) §6 Gate 2→3 Transition Test: consistent risk register reviews, measurable vulnerability SLA performance, at least one completed architecture or project intake disposition, and a standard-layer adoption plan with owners and target dates.

---

## 6. Scaling the Model: Consolidate, Then Split

A small team and a full-scale security function run the same model at different density. This section shows how. The mechanism is role consolidation, not document deletion.

### 6.1 The Principle

The canonical role roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1 lists every role CERG names. A small team does not delete roles. It assigns several roles to one person. The documents do not change; the **assignment map** changes. One person can hold the CISO role, the Governance Pillar Leader role, and the Risk Register Owner role at once. The work of each role still happens; it happens in one head.

> **Consolidate Roles, Never Delete Them**
>
> When a role is deleted, the work it owned silently stops. When a role is consolidated onto a person already carrying three others, the work is still owned, still visible, and still re-assignable the day a fourth person is hired. Always consolidate. The role roster is fixed; only the assignment map scales.

### 6.2 Reference Assignment Maps

These are starting points, not mandates. Adjust to the skills you actually have.

**Small-team example.** Every person carries a pillar plus shared duties.

| **Person** | **Holds These Canonical Roles** |
|---|---|
| 1 | CISO; Executive Sponsor liaison |
| 2 | Governance Pillar Leader; Policy & Standards Manager; Risk Register Owner; Evidence Librarian |
| 3 | Risk Pillar Leader; Exposure Management Lead; Threat Intelligence Analyst |
| 4 | Engineering Pillar Leader; Cloud Security Engineer; Identity Engineer; Pre-production Reviewer |
| 5 | Application Security Engineer; Endpoint Engineer; Cryptography Engineer; Detection Engineer |

**Mid-size team example.** Pillar leaders are dedicated; senior practitioners own a domain each; the rest are individual contributors. Compliance manager roles are assigned only for regulators in scope.

**Full-scale function example.** The full roster maps roughly one role to one person, with sub-role domain qualifiers (for example, Engineering Pillar Leader - Cloud and Engineering Pillar Leader - OT) split out as described in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

### 6.3 What Does Not Scale Down

Two things hold regardless of headcount.

1. **Separation of approval authority.** The person who accepts a risk cannot be the only person who assessed it. Even on a small team, risk acceptance follows the authority table in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. If one person genuinely holds every role, the Executive Sponsor provides the second set of eyes on High and Critical acceptance.
2. **The cadence.** A small team still runs the Monthly Risk Register Review and the Quarterly Cyber Oversight Group brief. The meetings are shorter. They are not skipped.

---

## 7. Adapting the Documents

### 7.1 Mechanical Adaptation

Names, headcounts, regulators, and illustrative examples are variables. They are adapted with the token scheme and render tool defined in [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md). Do not hand-edit. Build the organization profile once, render the corpus, review the output.

### 7.2 Choosing Standards

Adopt every standard whose environment you operate. Skip none that apply.

| **Standard** | **ID** | **Adopt If** |
|---|---|---|
| IT / Cloud / SaaS Security | [`CERG-STD-IT-001`](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | You run any cloud or SaaS. Nearly everyone. |
| Grid Control Systems Security | [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | You operate operational technology or industrial control systems. |
| CUI Handling | [`CERG-STD-CUI-001`](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) | You handle Controlled Unclassified Information or pursue CMMC. |
| Access Management | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) | Required-Path for Standard and Regulated. Every organization has identities. |
| Asset Management and Inventory | [`CERG-STD-AM-001`](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Required-Path for Standard and Regulated. Exposure management and evidence depend on owned assets. |
| Secure Configuration Baseline | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Required-Path for Standard and Regulated. Every organization has systems to harden. |
| Logging, Monitoring, and Detection | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Required-Path for Standard and Regulated. |
| Cyber Resilience and Backup | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Required-Path for Standard and Regulated. |
| Cryptography and Key Management | [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Recommended for Standard; required where managed keys, certificates, encryption controls, CUI, OT, SOX, or other regulated scope applies. |

If you defer an applicable standard, record the decision and a target adoption date in the risk register. A deferred applicable standard is an accepted risk, not a silent gap.

### 7.3 Choosing Operational Packages

Operational packages are adopted per regulator. Adopt only what applies to you.

| **Package** | **ID** | **Adopt If** |
|---|---|---|
| NERC-CIP | [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | You are a registered entity under NERC-CIP. |
| CUI / CMMC | [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | You are pursuing CMMC certification. |
| SOX ITGC | [`CERG-PLN-SOX-001`](../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | You are a public company subject to SOX. |
| Incident Response Plan | [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | Ensure a standing IR plan exists for every implementation. This plan is owned by the standing IR team, not by CERG; see [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4. |

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

## 10. Employer Brand and Talent Attraction

### 10.1 The Talent Problem CERG Solves

The cybersecurity talent market is brutal. Organizations that cannot articulate why someone should work there lose candidates to organizations that can. CERG's structure is a genuine differentiator. Most candidates have never heard of it. The organization's job is to make them hear it and want it.

CERG's employee value proposition is not "competitive salary and benefits." Every organization says that. CERG's EVP is that a CERG-structured team is a better place to practice cybersecurity than a traditionally structured team. This section articulates why, provides role-specific candidate messaging, and includes a structured interview guide aligned to the competency model.

### 10.2 The CERG Employee Value Proposition

Working in a CERG-structured team means:

**You are a generalist who specializes.** In a traditional security organization, a Cloud Security Engineer reviews architectures and never sees a risk register. A Threat Intelligence Analyst writes threat reports and never touches an architecture diagram. In CERG, the left-right knowledge model means every practitioner understands the full lifecycle. You specialize in your domain, but you are not confined to it. After three years in a CERG Engineering team, you can credibly discuss risk methodology with a Risk practitioner and compliance requirements with a Governance practitioner. That breadth makes you more valuable than a specialist who has done one thing for five years.

**You see the impact of your work.** A CERG architect's design decision is visible in the Risk pillar's posture report two quarters later. A CERG threat analyst's intelligence brief drives Engineering's next quarter of control improvements. The pillars are not silos; they are feedback loops. When you do your job well, the other two pillars get better. When they do their jobs well, you get better. The work you do on Tuesday is visible in the organization's security posture on Friday.

**Your career path is defined, not discovered.** JA-001 defines exactly what each grade expects across five dimensions. CMP-001 defines the specific behaviors at each level. PERF-001 defines how you are evaluated and promoted. You do not need to guess what it takes to reach the next level or hope your manager advocates for you loudly enough. The path is documented, and the promotion process is designed to be consistent regardless of which manager you report to.

**The best idea wins, regardless of who brings it.** CERG's "yes, and" operating philosophy and its three-pillar structure create an environment where a Specialist's well-reasoned finding carries as much weight as a Sr. Advisor's, and a Risk analyst can tell an Engineering director that a control design has a flaw without political consequence. The structure rewards rigor, not rank. Iron sharpens iron.

**You are building a program, not running a tool.** Many cybersecurity roles are tool-operating jobs. The organization bought a scanner; you run the scanner. The organization bought a SIEM; you stare at the SIEM. CERG roles are program-building roles. You design how the function works, not just execute it. You improve procedures, author standards, mentor incoming practitioners, and shape the organization's security posture. If you want to be told what to do, CERG is not for you. If you want to define how it is done, CERG is.

### 10.3 Role-Specific Candidate Messaging

The EVP above applies to every CERG role. Each role family adds specific messaging for candidates:

**Engineering candidates:**
"You will not just review architectures; you will own reference architectures. You will not just configure security tools; you will design how the organization secures its cloud, identity, and application platforms. You will work with Risk to understand how your controls perform under attack and with Governance to ensure your designs are audit-ready by design, not retrofit."

**Risk candidates:**
"You will not just triage alerts; you will shape how the organization understands and responds to its exposure. Your threat assessments will drive Engineering's control priorities. Your risk judgments will inform executive decisions. You will work with Engineering to design controls that address the root cause of findings, not just ticket the symptoms."

**Governance candidates:**
"You will not just manage evidence binders; you will design the compliance program that makes audit findings rare. You will translate between regulatory language and technical reality, ensuring standards are both compliant and implementable. You will work with Engineering and Risk to build compliance into the operating model, not bolt it on after the fact."

### 10.4 Structured Interview Guide

The interview process assesses candidates against the CMP-001 competency domains. The guide below provides question banks for each domain, calibrated to the target grade. Use it to design interview panels that evaluate every candidate against the same dimensions.

#### Interview Structure

| Round | Focus | Interviewers | Duration |
|---|---|---|---|
| **Screening** | Role fit, communication, basic domain knowledge | Hiring manager | 30-45 min |
| **Technical** | Technical Depth assessment calibrated to target grade | 1-2 senior practitioners from the candidate's pillar | 60-90 min |
| **Cross-Pillar** | Cross-Pillar Fluency, Risk Judgment, Communication | 1 practitioner from each of the other two pillars | 60 min |
| **Leadership / Final** | Influence, Operational Discipline, Continuous Learning; culture fit | Pillar leader or CISO | 45-60 min |

#### Technical Depth Questions by Grade

**S1-S2 (Specialist / Sr. Specialist):**

- Walk me through a technical problem you solved recently in your domain. What was the problem, how did you diagnose it, what was the solution?
- Describe a time you followed a procedure and discovered it needed improvement. What did you change, and why?
- [Role-specific technical scenario, e.g., for Cloud Security Engineer: "A development team wants to deploy a new microservice that will store PII. Walk me through your security review."]

**S3-S4 (Advisor / Sr. Advisor):**

- Describe the hardest technical decision you have influenced in your current or previous role. Who disagreed with you, how did you resolve it, and what was the outcome?
- You are evaluating a new technology or platform for organizational adoption. Walk me through your evaluation framework.
- A junior team member has made a technical recommendation you believe is wrong. It is not dangerously wrong; it is suboptimal. How do you handle it?

#### Cross-Pillar Fluency Questions

- Describe a time you worked with a function outside your immediate team to solve a security problem. What made the collaboration effective or difficult?
- [For Engineering candidates]: A Risk analyst has rated a finding Critical. You believe compensating controls reduce the actual risk to Medium. Walk me through how you would handle that disagreement.
- [For Risk candidates]: An Engineering team tells you they cannot remediate a High finding within your SLA due to architectural constraints. How do you respond?
- [For Governance candidates]: An Engineering team tells you a compliance requirement is technically impossible to implement as written. What do you do?

#### Risk Judgment Questions

- Describe the most significant security risk you have identified that others did not see. Why did they miss it? What did you do about it?
- You have limited resources and two findings: a Critical vulnerability in an internet-facing system with compensating controls, and a High vulnerability in an internal system with a known exploitation path. Which do you address first? Why?
- Tell me about a time you were wrong about a risk assessment. What did you miss, and what did you change about your approach afterward?

#### Communication Questions

- Describe a time you had to explain a technical security issue to a non-technical audience. How did you structure your explanation? What was the result?
- You are briefing an executive on a material risk. They have five minutes before their next meeting. What do you say?
- You have identified a significant security gap that requires budget to address. Write (or describe) the first three paragraphs of the business case you would present.

#### Influence and Mentorship Questions

- Tell me about someone you mentored or developed. What did they need, what did you do, and where are they now?
- Describe a time you changed how your team or organization approached a security problem, without formal authority to mandate the change.
- A peer is consistently producing work that is technically correct but poorly documented. Their evidence would not survive an audit. How do you address it?

#### Operational Discipline Questions

- Walk me through how you manage your work. How do you prioritize, how do you track what is done and what is pending, how do you handle interruptions?
- Describe a time you discovered that something you thought was done was not actually done. What had you missed, and what did you change to prevent it from happening again?
- How do you ensure your work is defensible under audit or regulatory scrutiny?

#### Continuous Learning Questions

- What is the last thing you learned about cybersecurity that changed how you think about your work?
- What are you currently learning or working on improving?
- If you had an annual professional development budget and time to use it, what would you invest in and why?

### 10.5 Candidate Evaluation Rubric

Interviewers rate candidates on each assessed dimension using a four-point scale:

| Rating | Definition |
|---|---|
| **Strong Yes** | The candidate's response demonstrates clear, specific evidence of the competency at or above the target grade. I would be confident putting them in front of the organization's stakeholders. |
| **Yes** | The candidate demonstrates the competency at the target level. Minor gaps that onboarding will close. |
| **No** | The candidate does not demonstrate the competency at the target level. The gap is material and would require significant development to close. |
| **Strong No** | The candidate's response raises a red flag: dismissive of process, inability to explain their own work, or concerning judgment. |

A "Strong No" from any interviewer on any dimension should trigger a panel discussion before proceeding. A "No" on a dimension that is critical to the role (e.g., Technical Depth for an S3 Engineer, Risk Judgment for an S3 Risk Analyst) should also trigger discussion.

### 10.6 Careers Page Guidance

Organizations adopting CERG should consider adding a "Working in Our CERG Team" section to their careers page. The section should:

1. Explain what CERG is in one paragraph (plain language, no jargon)
2. Articulate what makes working in a CERG-structured team different (the EVP from §10.2, adapted for the organization's voice)
3. List the role families (Engineering, Risk, Governance) and what kind of person thrives in each
4. Link to the public CERG Framework so candidates can understand what they are signing up for
5. Include the structured interview process so candidates know what to expect

> **The Framework Itself Is the Brand**
>
> A candidate who reads the CERG Framework, the Job Architecture, the Competency Model, and the job description for their role before they apply has self-selected. They understand the structure, they want to work in it, and they arrive with a mental model of how the organization operates. The careers page does not need to sell CERG. It needs to surface CERG, make it understandable, and let the framework do the selling.

---

## 11. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-IMP-001 |
| **Version** | 1.11 |
| **Status** | Approved |
| **Effective Date** | 2026-06-14 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to the V1 library |
| **Next Scheduled Review** | 2027-05-27 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.12 | 2026-06-18 | Governance Pillar Leader | Added Gate 2→3 transition criteria reference at §5.3 linking to CERG-GOV-IMP-005 §6 Gate 2→3 Transition Test as prerequisite before standard-layer adoption. |
| 1.11 | 2026-06-14 | Governance Pillar Leader | Aligned core-standard guidance with the adoption decision tree and clarified that the IR plan is an adjacent-function requirement, not a CERG-owned package. |
| 1.1 | 2026-05-27 | Cyber Governance | Added §10 Employer Brand and Talent Attraction: CERG employee value proposition, role-specific candidate messaging, structured interview guide aligned to CMP-001 competency domains, candidate evaluation rubric, and careers page guidance. Updated supporting documents to reference JA-001, CMP-001, and JD-001. |
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
