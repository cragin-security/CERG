# SURGE: Cyber Engineering, Risk & Governance

## ONBOARDING AND INTEGRATION PROGRAM
### 30/60/90-Day Plans · CERG 101 · Buddy System · First Contribution

---

| | |
|---|---|
| **Document ID** | CERG-GOV-ONB-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) · [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) · [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) · [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) · [`CERG-GOV-CON-001`](CERG-GOV-CON-001_Contractor_and_Non-Employee_Staff_Integration_Guide.md) | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) |
| **Review Cycle** | Annual / On any change to organizational structure, tooling, or document library |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.7.2 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Onboarding Philosophy](#2-onboarding-philosophy)
3. [Before Day One: Manager Preparation](#3-before-day-one-manager-preparation)
4. [Week One: Orientation and Access](#4-week-one-orientation-and-access)
5. [The 30/60/90-Day Model](#5-the-306090-day-model)
6. [CERG 101: The Core Curriculum](#6-cerg-101-the-core-curriculum)
7. [The Buddy System](#7-the-buddy-system)
8. [The First Contribution Milestone](#8-the-first-contribution-milestone)
9. [Cross-Pillar Rotation](#9-cross-pillar-rotation)
10. [Role-Specific Onboarding by Family](#10-role-specific-onboarding-by-family)
11. [Onboarding for Managers](#11-onboarding-for-managers)
12. [Measuring Onboarding Effectiveness](#12-measuring-onboarding-effectiveness)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

A new Cloud Security Engineer can take six to nine months to understand their environment well enough to contribute independently. During those months, they are learning where the architecture diagrams live, who owns which platform, what a "normal" alert looks like, and how CERG's pillars interact. They are not yet producing at the level of their grade, and they feel it. The gap between their capability and their output is stressful for them and expensive for the organization.

This document closes that gap. It defines a structured onboarding program that cuts time-to-productivity from a typical six-to-nine months to a target of three to four. It provides role-specific 30/60/90-day plans for each role family, a CERG 101 curriculum that ensures every new hire understands the framework, a cross-pillar buddy system, a first-contribution milestone that builds confidence and visibility, and a cross-pillar rotation that makes the left-right knowledge model real from day one.

It applies to every new CERG hire, regardless of role, grade, or prior experience. A seasoned Sr. Advisor joining from another organization moves through the same structure faster than a new Specialist, but they move through the same structure. The program also applies to internal transfers joining CERG from another function, with adjustments for their existing organizational knowledge. It does not apply to contractors and consultants, who follow the condensed onboarding defined in CERG-GOV-CON-001 (Planned, V1.x).

> **Onboarding Is a Program, Not a Checklist**
>
> The CERG Framework (FRM-001 §9.2) describes the left-right knowledge model: a new engineer can learn the organization's standards from Governance, understand the current threat environment from Risk, and have context for every major system from Engineering's project documentation. That describes the resources available. It does not describe a program. This document is the program. A new hire who spends their first month reading documents alone is not being onboarded; they are being oriented to a library. Onboarding requires structured exposure, guided practice, and human connection.

---

## 2. Onboarding Philosophy

1. **Productivity is a gradient, not a switch.** The goal is not that the person is fully productive on day 30. It is that on day 30 they have made a concrete contribution; on day 60 they are contributing to their pillar's standing work with decreasing supervision; on day 90 they own a defined work stream and their teammates feel the difference.

2. **The pillar owns the person; the program owns the first 90 days.** The hiring manager is accountable for the new hire's success. The onboarding program provides the structure; the manager executes it.

3. **Cross-pillar fluency starts on day one, not year three.** Every new hire spends structured time in the other two pillars during their first 90 days. The left-right knowledge model in FRM-001 §9.2 is not an aspirational goal for senior practitioners; it is built into how every person enters the organization.

4. **The buddy is not the manager.** Every new hire has a peer buddy from a different pillar. The buddy provides the unvarnished perspective a manager cannot: where the documentation is wrong, which team has a feud with which other team, how the espresso machine actually works.

5. **The first contribution is the inflection point.** Within 30 days, every new hire makes a concrete, visible contribution and presents it to their pillar. This is not a test. It is the moment the person transitions from "learning the environment" to "operating in it." It is psychologically important and it should be celebrated.

---

## 3. Before Day One: Manager Preparation

The hiring manager completes the following before the new hire's first day. If these items are not complete, the new hire spends their first week waiting for access and losing momentum that is difficult to regain.

| Item | Owner | Timeline |
|---|---|---|
| **Access provisioning** | Manager + IT | Submitted at offer acceptance; confirmed active before day one |
| - System accounts: email, SSO, VPN, collaboration tools | IT | Day -5 |
| - CERG tool access: CSPM, vulnerability scanner, GRC platform, SIEM, threat intel platform, detection pipeline, code repositories per role | Manager + tool admins | Day -5 |
| - Document library access: CERG repository, policies, standards, procedures | Manager | Day -3 |
| **Hardware** provisioned and imaged per Engineering security baseline | IT | Day -3 |
| **Workspace** prepared (physical desk or virtual collaboration space) | Manager | Day -3 |
| **Buddy assigned** (from a different pillar; confirmed and briefed) | Manager | Day -10 |
| **First-week schedule** published: who the new hire meets, when, and why | Manager | Day -3 |
| **Welcome message** sent to the team and relevant cross-pillar colleagues | Manager | Day -3 |
| **30/60/90-day plan** drafted with role-specific objectives (per §10) | Manager | Day -5 |
| **CERG 101 curriculum** assigned with schedule for completion | Manager | Day -1 |

> **The First-Day Test**
>
> A new hire should be able to log in, access their email, read their first-week schedule, open the CERG document library, and start reading the Framework by 10:00 AM on day one. If they spend their first morning waiting for account provisioning, the manager has not prepared. The cost of a lost first morning is not the four hours of productivity; it is the message that the organization does not have its act together. That message is hard to undo.

---

## 4. Week One: Orientation and Access

The first week is structured but not overloaded. The goal is orientation to the environment, the people, and the framework, not task execution.

### 4.1 Day One

| Time | Activity | With Whom |
|---|---|---|
| 09:00-10:00 | Welcome and logistics: workspace, badging, tools, HR paperwork | Manager |
| 10:00-11:00 | CERG overview: what CERG is, why it exists, the three pillars, the yes-and philosophy, how the new hire's role fits | Manager |
| 11:00-12:00 | Tool access verification: confirm the new hire can access every system on the provisioning list | Manager + IT rep |
| 12:00-13:00 | Lunch with the team (or virtual equivalent) | Manager + immediate team |
| 13:00-14:00 | Read the CERG Framework (FRM-001) §§1-3: the problem statement and the three pillars. Take notes on questions. | Self-directed |
| 14:00-15:00 | Meet the buddy: informal introduction. The buddy explains their role, their pillar, and what they wish they had known on day one. | Buddy |
| 15:00-16:00 | Review the 30/60/90-day plan with the manager. Adjust based on the new hire's questions and observations from day one. | Manager |

### 4.2 Days Two Through Five

By the end of week one, the new hire has:

- Met every member of their immediate team and their pillar leader
- Met at least one person from each of the other two pillars
- Read the CERG Framework (FRM-001) and the CERG Operating Model (OM-001)
- Read their own job description (JD-001)
- Read the competency model for their role family (CMP-001 §§4-6)
- Understood the performance management cadence and what their first review will evaluate (PERF-001 §3-4)
- Completed any mandatory organizational training (security awareness, code of conduct, compliance)
- Had a daily 15-minute check-in with their manager
- Had at least one informal conversation with their buddy
- Started the CERG 101 curriculum (§6)

The manager sends a Friday-afternoon email to the pillar summarizing the new hire's first week (with the new hire's consent) and noting one thing the new hire observed that the team may find useful. This is the first signal that the new hire's perspective is valued.

---

## 5. The 30/60/90-Day Model

### 5.1 Days 1-30: Learn and Contribute

**Goal:** Understand the environment, meet the people, make a first contribution.

**Key activities:**

- Complete the CERG 101 curriculum (§6)
- Shadow at least two standing meetings: one within the home pillar, one cross-pillar
- Pair with a senior team member on one active work item: observe, ask questions, understand the workflow end to end
- Identify a task the person can complete independently and complete it: this becomes the First Contribution (§8)
- Spend one day with the buddy's pillar, observing how that pillar operates (this is the first third of the cross-pillar rotation; §9)
- Daily 15-minute manager check-in (weeks 1-2); every-other-day (weeks 3-4)
- Weekly informal check-in with the buddy

**Success indicators at day 30:**

- The person can describe CERG's three-pillar model, their role's place in it, and how their pillar interacts with the other two
- The person has completed their First Contribution and presented it to the pillar
- The person has met everyone in their pillar and key people in the other two
- The person can navigate the document library: they know where to find the policy, standards, procedures, and templates relevant to their role
- The person has access to all tools and has used at least the primary ones in a supervised context
- The manager has observed the person demonstrate at least one competency from CMP-001 in an authentic work context

### 5.2 Days 31-60: Practice and Deepen

**Goal:** Contribute independently to pillar work; develop cross-pillar understanding; identify development priorities.

**Key activities:**

- Own one defined work stream within the pillar with decreasing supervision (e.g., triage a subset of CSPM alerts, manage evidence collection for a control family, perform supervised architecture reviews for low-complexity projects)
- Complete the second cross-pillar rotation day (§9)
- Participate in at least one cross-pillar working group or project as an observer-contributor
- Review the CMP-001 competency matrix for their role family with their manager. Identify 2-3 development priorities for the first year
- Begin the technical onboarding for their role family per §10
- Weekly manager check-in (30 minutes)
- Bi-weekly buddy check-in

**Success indicators at day 60:**

- The person completes assigned work with minimal rework; their output is consistent with grade expectations for routine tasks
- The person has contributed to a cross-pillar discussion with a relevant observation or question
- The person has a documented development plan with 2-3 priorities aligned to CMP-001
- The person's teammates report that the person is "starting to be useful" (this is a higher bar than it sounds: it means the person is reducing the team's load, not adding to it)
- The manager has observed the person demonstrate at least three CMP-001 competencies in authentic work contexts

### 5.3 Days 61-90: Own and Integrate

**Goal:** Own a defined scope; demonstrate cross-pillar fluency; establish the performance baseline for the first formal review.

**Key activities:**

- Own a defined work stream independently: the manager sets outcomes; the person determines the path
- Complete the third cross-pillar rotation day (§9)
- Lead one item in a standing meeting: present a finding, a status update, or a recommendation to the group
- Complete the role-specific technical onboarding per §10
- Conduct a 90-day retrospective with the manager: what worked, what did not, what support the person needs going forward
- The manager prepares the first quarterly check-in notes per PERF-001 §3.2

**Success indicators at day 90:**

- The person owns at least one defined work stream. Their manager reviews outcomes, not tasks
- The person has worked directly with at least one person from each pillar on a shared objective
- The person can explain how a decision in their domain affects the other two pillars
- The person has identified at least one improvement to a procedure, tool configuration, or documentation item and raised it
- The person's teammates would notice if the person were absent
- The manager can write a credible first quarterly check-in with evidence across at least four of the six SME evaluation dimensions

> **90 Days Is a Target, Not a Deadline**
>
> A new Specialist with no prior cybersecurity experience may need 120 days to reach the day-90 success indicators. A Sr. Advisor joining from another CERG-adopting organization may hit them at day 45. The structure is the same; the pace varies. The manager adjusts the timeline, not the expectations.

---

## 6. CERG 101: The Core Curriculum

Every new hire, regardless of role, grade, or prior experience, completes the CERG 101 curriculum within their first 30 days. The curriculum is a guided reading of the CERG document library, not a passive document dump. For each document, the new hire reads it, writes three questions or observations, and discusses them with their manager or buddy.

### 6.1 Required Reading (First 30 Days)

| Day | Document | Focus |
|---|---|---|
| 1 | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Why CERG exists, the three pillars, the left-right knowledge model, maturity tiers |
| 2 | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | How CERG operates: engagement models, staffing, cadence, interfaces with other functions |
| 3 | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | The policy that governs everything. What is mandatory, who approves what |
| 4 | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Who does what. The RACI for the new hire's own role and adjacent roles |
| 5 | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | The grade structure, the two tracks, the dimensions of growth |
| 6 | [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | What good looks like at each grade in the new hire's role family |
| 7 | [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) | The new hire's own job description and those of their immediate teammates |
| 8 | [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | How performance is evaluated, how promotion decisions are made |
| 9 | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | How the document library is organized, how to find what you need |
| 10 | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | How CERG manages risk: taxonomy, scoring, acceptance authority, exception process |

### 6.2 Role-Specific Reading (Days 10-30)

| Role Family | Additional Required Reading |
|---|---|
| **Engineering** | CERG-STD-IT-001, CERG-STD-CFG-001, CERG-STD-NET-001, CERG-STD-EP-001, CERG-STD-SDL-001, CERG-STD-CR-001, CERG-PRC-AR-001, CERG-PRC-CHG-001 |
| **Risk** | CERG-STD-LM-001, CERG-STD-RES-001, CERG-PRC-VM-001, CERG-PRC-AV-001, CERG-PRC-TPRM-001, CERG-PRC-TI-001, CERG-PRC-TM-001 |
| **Governance** | CERG-STD-CUI-001, CERG-STD-AC-001, CERG-STD-DG-001, CERG-PRC-RM-001, CERG-PRC-AUD-001, CERG-PLN-CIP-001, CERG-PLN-CUI-001, CERG-PLN-SOX-001 |

### 6.3 The CERG 101 Discussion

Within the first two weeks, the new hire and their manager have a 60-minute CERG 101 discussion. The agenda:

1. **What was familiar?** What parts of CERG resemble how the new hire's previous organization operated?
2. **What was different?** What parts of CERG are novel, surprising, or challenging to the new hire's mental model of how cybersecurity should work?
3. **What was unclear?** The manager answers questions and clarifies.
4. **What should CERG 101 teach that it currently does not?** The new hire's fresh perspective is valuable. The manager records suggestions for curriculum improvement.

---

## 7. The Buddy System

### 7.1 Buddy Selection

Every new hire is assigned a buddy before day one. The buddy is:

- A peer (similar grade, not the new hire's manager or the manager's manager)
- From a different pillar than the new hire
- Not on the new hire's immediate team
- Has been with CERG for at least six months (so they have completed their own onboarding and have an informed perspective)
- Volunteers or is selected by their manager; nobody is conscripted into buddy duty

### 7.2 Buddy Responsibilities

The buddy's role is social, practical, and informational. It is not supervisory. The buddy does not evaluate the new hire's performance or report to the manager (except to flag serious concerns, e.g., the new hire seems profoundly unhappy or has disclosed a compliance violation).

| Timeframe | Buddy Activity |
|---|---|
| **Before day one** | Send a welcome message. Introduce yourself, your role, your pillar. Offer to answer any pre-start questions. |
| **Week one** | Have at least two informal conversations (coffee, lunch, virtual chat). Show the new hire where things really are: the best documentation, the useful dashboards, the people who actually know things. |
| **Weeks 2-4** | Weekly check-in: 15-30 minutes. How is it going? What is confusing? What is different from what you expected? Answer questions the new hire may not want to ask their manager. |
| **Days 31-90** | Bi-weekly check-in. By now the new hire should have their own network; the buddy is a continuing resource, not a daily presence. |
| **After 90 days** | The buddy relationship becomes a normal peer relationship. The formal buddy assignment ends. |

### 7.3 The Buddy Is Not

- **A substitute for the manager.** The manager owns the new hire's success. The buddy supplements, not replaces.
- **A performance evaluator.** The buddy does not contribute to the new hire's performance review unless the new hire specifically requests their perspective.
- **An IT help desk.** The buddy can point the new hire to the right resource; they are not expected to troubleshoot the new hire's development environment.
- **A therapist.** The buddy is a peer. If the new hire is experiencing harassment, discrimination, or serious mental health concerns, the buddy directs them to HR or the employee assistance program, not to another coffee chat.

---

## 8. The First Contribution Milestone

### 8.1 What Counts

Within 30 days, every new hire makes a concrete, visible contribution to CERG and presents it to their pillar. The contribution must be:

- **Real, not simulated.** It addresses an actual need, not a fabricated exercise.
- **Complete, not in-progress.** The contribution is delivered, not described as "I started working on."
- **Presented, not just submitted.** The new hire presents the contribution to their pillar in a standing meeting or a dedicated session. They explain what they did, why, and what they learned.

Acceptable first contributions include, but are not limited to:

| Role Family | Examples |
|---|---|
| **Engineering** | First architecture review completed and presented; first IaC module security improvement merged; first CSPM policy tuned with documented rationale; first configuration baseline update reviewed and committed |
| **Risk** | First vulnerability triaged through the full lifecycle and closed; first vendor risk assessment completed; first detection rule authored, tested, and deployed; first threat intelligence brief delivered to the team |
| **Governance** | First evidence item collected, validated, and stored; first control test completed and documented; first policy section reviewed with documented feedback; first risk register entry reviewed and updated |

### 8.2 The First Contribution Presentation

The presentation is 5-10 minutes and follows a simple structure:

1. **What I did.** The contribution, in plain language.
2. **How I did it.** The tools, procedures, and people involved.
3. **What I learned.** One thing about CERG, the technology, or the team that the new hire now understands that they did not understand before.
4. **What I would do differently.** Self-reflection, not self-criticism. Demonstrates that the person is thinking about improvement, not just execution.

The pillar responds with recognition, not evaluation. The point is to make the new hire visible as a contributor, not to grade their first work product. The manager ensures that the presentation is scheduled in a standing meeting that the pillar leader attends.

> **The First Contribution Is Psychologically Loaded**
>
> A new hire who contributes nothing visible for 90 days believes, correctly, that they have not yet proven their value. A new hire who presents a completed contribution to their pillar at day 25 knows they belong. The difference in confidence, engagement, and retention is material. This is not a ceremonial milestone; it is the single most important moment in the first 90 days.

---

## 9. Cross-Pillar Rotation

### 9.1 Structure

Every new hire spends three dedicated days, one per month during the first 90 days, embedded in a different pillar from their own. The rotation implements the left-right knowledge model (FRM-001 §9.2) from day one, not year three.

| Month | Rotation | Host |
|---|---|---|
| **Month 1 (Days 15-30)** | Buddy's pillar | Buddy |
| **Month 2 (Days 31-60)** | Remaining pillar | Designated host from that pillar (Sr. Specialist or above) |
| **Month 3 (Days 61-90)** | Return to buddy's pillar or deeper dive into a specific cross-pillar function | Buddy or host |

### 9.2 Rotation Day Agenda

Each rotation day is structured:

1. **Morning: Observe.** The new hire shadows the host through their morning. They attend the host's standing meetings (read-only), watch the host triage alerts or review evidence or design architecture, and ask questions.
2. **Midday: Discuss.** The host walks the new hire through one end-to-end workflow in their pillar. For example, how a vulnerability goes from scanner alert to closed finding, or how a regulatory change becomes a policy update. The new hire asks: where does your pillar get its inputs? Where do its outputs go? What frustrates you about how my pillar hands off to yours?
3. **Afternoon: Participate.** The new hire contributes to one low-stakes activity in the host's pillar under supervision. The activity should be authentic: review a finding, test a control, walk through an architecture diagram. The output does not need to be perfect; the experience is the point.

### 9.3 Rotation Debrief

After each rotation day, the new hire writes a one-paragraph debrief and sends it to their manager and the host. The debrief answers:

- What did I learn about this pillar that I did not know before?
- What does my home pillar do that makes this pillar's work harder?
- What does this pillar do that my home pillar should know about?

The manager reviews the debriefs at the 90-day retrospective. Patterns across debriefs (e.g., "every new hire discovers that Engineering and Risk use different severity language") are signals that should reach pillar leadership.

---

## 10. Role-Specific Onboarding by Family

### 10.1 Engineering Family

Engineering new hires add the following to the standard 30/60/90-day plan:

| Phase | Technical Milestone |
|---|---|
| **Days 1-30** | Complete architecture review training: shadow two architecture reviews, perform one supervised review. Gain read access to all cloud/platform environments in the person's domain. Clone and understand the reference architecture repository. |
| **Days 31-60** | Perform three independent architecture reviews with senior review. Contribute one improvement to an IaC security module, configuration baseline, or security automation. Present one architecture finding at Pre-production Review Board. |
| **Days 61-90** | Own architecture reviews for low-complexity projects independently. Author one new security control or policy-as-code rule. Present a technical deep-dive on a platform or domain to the Engineering team. |

### 10.2 Risk Family

| Phase | Technical Milestone |
|---|---|
| **Days 1-30** | Complete tool training on the primary Risk platforms (vulnerability scanner, CSPM, SIEM, threat intel, detection pipeline). Shadow the vulnerability triage process, vendor assessment workflow, or detection rule lifecycle end to end. |
| **Days 31-60** | Independently triage findings in one domain (e.g., cloud vulnerabilities, vendor alerts, detection events). Author one detection rule, threat advisory, or risk assessment with senior review. Present one finding at Vulnerability Triage or Threat Intelligence Brief. |
| **Days 61-90** | Own triage for a defined asset group or finding type. Correlate findings across tools: identify one instance where two tools see the same issue differently and document the discrepancy. Present a risk trend or threat landscape update to the Risk team. |

### 10.3 Governance Family

| Phase | Technical Milestone |
|---|---|
| **Days 1-30** | Complete GRC platform and evidence library training. Shadow one audit evidence request from intake to delivery. Shadow one control test from procedure to documentation. Read the organization's last audit report or assessment findings. |
| **Days 31-60** | Independently collect and validate evidence for one control family. Map one regulatory requirement to CERG controls with documented rationale. Participate in one auditor or assessor walkthrough as an observer. |
| **Days 61-90** | Own evidence management for a defined control set. Author one policy or standard section update with senior review. Present a compliance status update at Compliance Pulse. |

---

## 11. Onboarding for Managers

A new CERG Manager or Pillar Leader adds the following to the standard onboarding program. Their first 90 days focus on understanding the team, the operations, and the stakeholder landscape before making changes.

| Phase | Leadership Milestone |
|---|---|
| **Days 1-30** | Meet every direct report individually. Read every team member's most recent performance summary. Attend all standing meetings for the team and the pillar. Identify: what is working well (do not change it), what is fragile (stabilize it), what is broken (plan to fix it). |
| **Days 31-60** | Present an initial assessment to the pillar leader or CISO: observations, not recommendations. Identify one operational improvement and implement it (small, visible, demonstrates the manager's operating style without disrupting the team). Begin building relationships with peer managers in other pillars. |
| **Days 61-90** | Present a 90-day plan for the team: priorities, structural changes (if any), development focus. Have had a meaningful 1:1 with every direct report. Have identified at least one succession risk or single-point-of-failure in the team's operations. |

> **New Managers: Observe Before You Change**
>
> A new Manager who reorganizes the team in their first month is signaling that they value their own preferences over understanding what exists. The team that survived without this Manager for months will survive another 90 days of observation. The Manager who takes the time to understand why things are the way they are before changing them earns trust. The Manager who changes things before understanding them burns trust they will spend years trying to rebuild.

---

## 12. Measuring Onboarding Effectiveness

### 12.1 Metrics

The onboarding program's effectiveness is measured through:

| Metric | Target | Measurement |
|---|---|---|
| **Time to first contribution** | ≤30 days | Days from start date to first contribution presentation |
| **Time to independent work-stream ownership** | ≤90 days | Days from start date to manager-confirmed independent ownership of a defined work stream |
| **90-day retention** | ≥95% | Percentage of new hires still with CERG at day 90 |
| **First-year retention** | ≥85% | Percentage of new hires still with CERG at 12 months |
| **New hire satisfaction** | ≥4.0/5.0 | Survey at day 90: "I feel prepared to do my job," "I understand how my role connects to CERG's mission," "I would recommend CERG's onboarding to a friend joining the organization" |
| **Manager satisfaction** | ≥4.0/5.0 | Survey at day 90: "The onboarding program gave me the structure I needed to bring my new hire up to speed," "My new hire is contributing at the level I expected by day 90" |

### 12.2 Continuous Improvement

The 90-day retrospective (§5.3) includes a structured feedback collection on the onboarding program itself. The manager asks:

1. What part of the onboarding program was most useful?
2. What part was least useful or felt like a waste of time?
3. What was missing that you wish had been included?
4. If you were designing the onboarding program for the next person in your role, what would you change?

Aggregated feedback is reviewed annually by the Governance Pillar Leader as part of this document's review cycle. A pattern of "the CERG 101 curriculum assumed knowledge I did not have" or "the cross-pillar rotation days were too short to be useful" should result in document updates.

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-ONB-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to organizational structure, tooling, or document library |
| **Next Scheduled Review** | 2027-05-27 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.7.2 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-27 | Cyber Governance | Initial release. Defines structured 30/60/90-day onboarding program for all CERG roles. Includes pre-day-one manager preparation checklist, week-one orientation, CERG 101 core curriculum, cross-pillar buddy system, first contribution milestone, cross-pillar rotation program, role-specific technical onboarding for Engineering/Risk/Governance families, manager onboarding addendum, and onboarding effectiveness metrics. |

### Review Triggers

- Material change to the CERG document library (new or retired documents that affect CERG 101)
- Material change to CERG tooling (new platforms that affect role-specific technical onboarding)
- Organizational restructure affecting pillar composition or reporting lines
- Feedback from 90-day retrospectives indicating systemic onboarding gaps
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Left-right knowledge model; onboarding philosophy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Pillar structure, engagement models, cadence |
| Job Architecture | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade expectations that onboarding accelerates toward |
| Competency Model | [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Development priorities identified during onboarding |
| Performance Management | [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | First performance review at 6 months |
| Job Descriptions | [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) | Success profiles inform 90-day objectives |
| Contractor Integration | [`CERG-GOV-CON-001`](CERG-GOV-CON-001_Contractor_and_Non-Employee_Staff_Integration_Guide.md) | Condensed onboarding for non-employee staff |
| Implementation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Organizational adoption of CERG |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.