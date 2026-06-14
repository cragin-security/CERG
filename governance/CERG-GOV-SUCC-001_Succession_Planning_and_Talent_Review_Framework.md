# SURGE: Cyber Engineering, Risk & Governance

## SUCCESSION PLANNING AND TALENT REVIEW FRAMEWORK
### Heat Maps · Readiness Ratings · Emergency Succession · Development Plans

---

| | |
|---|---|
| **Document ID** | CERG-GOV-SUCC-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Confidential - CISO and Pillar Leaders |
| **Owner** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) · [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) · [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) |
| **Review Cycle** | Annual talent review; emergency succession list reviewed semi-annually |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.7.2 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The Single-Point-of-Failure Problem](#2-the-single-point-of-failure-problem)
3. [Annual Talent Review](#3-annual-talent-review)
4. [The Succession Heat Map](#4-the-succession-heat-map)
5. [Emergency Succession](#5-emergency-succession)
6. [Successor Development Plans](#6-successor-development-plans)
7. [Cross-Pillar Succession](#7-cross-pillar-succession)
8. [Confidentiality and Access](#8-confidentiality-and-access)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

The CERG Framework (FRM-001 §9.2) states that the left-right knowledge model provides "talent resilience." A team where every member understands the other two pillars is more resilient than one where knowledge is siloed. But cross-pillar understanding is not a succession plan. Knowing how the Risk pillar operates does not make a Cloud Security Engineer ready to lead it. Knowing where the evidence library lives does not make a Detection Engineer ready to represent the organization to a NERC-CIP auditor.

This document closes that gap. It establishes a formal succession planning framework: an annual talent review cadence, a succession heat map for every critical CERG role, readiness ratings for identified successors (Ready Now, Ready in 1-2 Years, Ready in 3-5 Years, No Identified Successor), development plans for closing successor readiness gaps, an emergency succession protocol defining who steps in on 24 hours' notice, and cross-pillar succession requirements that ensure no pillar leader's only potential successor comes from the same pillar.

It applies to every critical CERG role: the CISO, pillar leaders, domain leads, and any role whose sudden vacancy would create a material operational risk. It does not apply to contractor or consultant roles, which are addressed by the knowledge retention requirements in CERG-GOV-CON-001.

> **This Document Is Confidential**
>
> Succession planning is among the most sensitive activities a leadership team undertakes. A person identified as "Ready in 3-5 Years" who learns they are not "Ready Now" may feel passed over. A person not identified as a successor at all may feel their career has plateaued. This document and the heat maps it produces are restricted to the CISO and pillar leaders. Individual development conversations draw from the succession analysis without revealing the analysis itself, the same way a manager uses calibration session output to inform a promotion conversation without naming the people who were rated higher.

---

## 2. The Single-Point-of-Failure Problem

### 2.1 Why Cybersecurity Is Especially Vulnerable

Cybersecurity teams have a single-point-of-failure problem that is worse than most knowledge-work functions for three reasons:

1. **Deep specialization resists documentation.** A Cryptography Engineer who has managed the PKI hierarchy for seven years carries knowledge that lives in their head: which certificates have quirks, which CAs have trust-chain issues with which vendors, which renewal processes have undocumented manual steps. That knowledge is partially documented and partially not. The person who leaves takes both halves.

2. **Regulatory relationships are personal.** A NERC-CIP Compliance Manager who has been the organization's face to its regional entity for a decade has a relationship with the auditors that a replacement cannot replicate on day one. The auditor who trusts the Compliance Manager's evidence because of a decade of demonstrated rigor will not extend that trust automatically to a replacement.

3. **Small teams have no bench.** A 5-person CERG team cannot afford a dedicated understudy for every role. When the person who runs Vulnerability Management leaves, someone else absorbs that work on top of their own. If that person also leaves, the function stops.

### 2.2 What the Left-Right Model Does and Does Not Solve

The left-right knowledge model reduces the SPOF risk by ensuring that:
- Every person knows enough about the other two pillars to collaborate effectively
- Documentation is consumed cross-pillar, not just within the pillar that authored it
- The evidence library, risk register, and document library are structured to survive any single person's departure

It does not solve:
- **Leadership succession.** Cross-pillar understanding is not cross-pillar leadership readiness. The Governance Pillar Leader has a specific set of management, regulatory, and stakeholder skills that are not developed by reading Engineering standards.
- **Deep domain succession.** Understanding what a Cryptography Engineer does is not the same as being able to do it. The left-right model provides awareness; succession requires capability.
- **Emergency succession.** If the Risk Pillar Leader resigns effective immediately, the left-right model provides nobody who can step into the role on 24 hours' notice unless that person has been deliberately developed for it.

---

## 3. Annual Talent Review

### 3.1 Cadence

The talent review occurs annually, within four weeks of the year-end calibration session (PERF-001 §6). It consumes calibrated performance ratings and promotion decisions as input and produces the succession heat map as output. The sequence ensures that succession decisions are based on current, calibrated assessments, not on reputation from two years ago.

### 3.2 Participants

| Organization Size | Participants |
|---|---|
| **5-person CERG** | CISO (sole reviewer; the CISO is also a subject of the review for their own succession, which is addressed with the board or Executive Sponsor) |
| **15-person CERG** | CISO + Pillar Leaders |
| **35+ person CERG** | CISO + Pillar Leaders + Senior Managers (for their functions) |

### 3.3 Agenda

The talent review addresses each critical role in sequence:

1. **Role:** [Canonical role name]
2. **Incumbent:** [Name and current grade]
3. **Retention risk:** Low / Medium / High. Is the incumbent a flight risk? Why?
4. **Succession status:** Review the current heat map ratings for identified successors.
5. **Successor development progress:** What development actions were planned at the last review? What progress was made?
6. **New successors?** Has anyone emerged as a potential successor since the last review?
7. **Emergency successor:** Is the emergency successor still current? Any changes?
8. **Actions:** What will be done in the next 12 months to improve succession readiness for this role?

### 3.4 Output

The talent review produces:

1. **Updated succession heat map** for every critical role (§4)
2. **Updated successor development plans** (§6)
3. **Updated emergency succession list** (§5)
4. **Retention risk register:** roles where the incumbent is a flight risk, with mitigation actions
5. **Succession gaps report:** roles with No Identified Successor, with a timeline and plan for developing one

---

## 4. The Succession Heat Map

### 4.1 Critical Roles

Not every canonical CERG role is critical for succession planning. A role is critical if its sudden vacancy would cause a material operational disruption that cannot be absorbed by the existing team within 30 days. The minimum set of critical roles includes:

| Tier | Roles |
|---|---|
| **Tier 1: Immediate organizational risk** | CISO; Engineering Pillar Leader; Risk Pillar Leader; Governance Pillar Leader |
| **Tier 2: Material function risk** | Cloud Security Engineer (senior/lead); OT Security Engineer (if OT environment); Exposure Management Lead; Detection Engineer (senior/lead); NERC-CIP Compliance Manager (if CIP-regulated); CMMC Compliance Manager (if CMMC-scoped); SOX ITGC Lead (if SOX-scoped); Risk Register Owner; Policy & Standards Manager |
| **Tier 3: Important domain risk** | Identity Engineer (senior/lead); Application Security Engineer (senior/lead); Adversarial Testing Lead; Threat Intelligence Analyst (senior/lead); Vendor Risk Analyst (senior/lead); Evidence Librarian; Cryptography Engineer |

The CISO and pillar leaders may add or remove roles from the critical list at each annual talent review based on current organizational context.

### 4.2 Readiness Ratings

Each identified successor for a critical role receives a readiness rating:

| Rating | Definition | Action Implication |
|---|---|---|
| **Ready Now** | The person could assume the role effectively within 30 days with minimal transition support. They have demonstrated the required competencies at the target level. | No development action required for readiness. Retain the person and ensure they are aware of their readiness (without guaranteeing the role). |
| **Ready in 1-2 Years** | The person has the foundational capabilities but needs specific experiences, training, or exposure to be fully ready. The gap is known and a development plan exists. | Execute the development plan. Review progress at each quarterly check-in. Re-rate at the next talent review. |
| **Ready in 3-5 Years** | The person is a long-term development candidate. They have demonstrated potential but need substantial growth in multiple dimensions. | Long-term development plan with intermediate milestones. May not be ready for emergency succession. |
| **No Identified Successor** | No person in the organization has been identified as a credible successor for this role. | This is a gap that must be addressed. Options: develop an internal candidate, recruit with succession in mind, or document the interim operating model if the role goes vacant. |

### 4.3 The Heat Map Format

For each critical role, the heat map records:

```
Role: [Canonical Role]
Incumbent: [Name]
Retention Risk: [Low/Medium/High]

Successors:
| Name | Current Role | Readiness | Development Priorities |
|---|---|---|---|
| [Name] | [Current role] | Ready Now | N/A |
| [Name] | [Current role] | Ready in 1-2 Yrs | [2-3 specific gaps] |
| No Identified Successor | - | - | [Plan to address] |

Emergency Successor: [Name] or [None]
Cross-Pillar Successor: [Name] or [None]
```

> **"Ready Now" Does Not Mean "Will Get the Role"**
>
> Identifying someone as Ready Now is a statement about their capability, not a promise of succession. The incumbent may stay for another decade. The organization's needs may change. Another candidate may emerge. The Ready Now rating means that if the role became vacant tomorrow, this person is the credible internal candidate. It does not mean the role is theirs.

---

## 5. Emergency Succession

### 5.1 The 24-Hour List

For every Tier 1 critical role (CISO, pillar leaders), an emergency successor is designated. The emergency successor is the person who steps into the role on 24 hours' notice if the incumbent is suddenly unavailable (resignation, illness, termination, or any other sudden departure). The emergency successor is not necessarily the long-term successor. They are the person who keeps the function operating while a permanent replacement is found.

### 5.2 Emergency Successor Requirements

The emergency successor must:

- Be a current CERG team member (not a contractor, not an external party)
- Have sufficient organizational knowledge to perform the role's most critical functions: approve urgent decisions, represent the function to executive leadership, and ensure standing operations continue
- Know they are the emergency successor and have accepted the responsibility
- Have documented access to the systems, contacts, and decision authorities they will need
- Be reviewed semi-annually (not just at the annual talent review) to confirm they are still with the organization and still willing

### 5.3 Emergency Succession by Tier

| Tier | Emergency Successor Model |
|---|---|
| **CISO** | Designated by the board or CEO in consultation with the CISO. Typically a pillar leader or a Deputy CISO if the organization has one. The Executive Sponsor may serve as interim CISO for a limited period per organizational succession policy. |
| **Engineering Pillar Leader** | The senior-most Cloud Security Engineer or OT Security Engineer at S4 or S3, with documented delegation from the CISO. |
| **Risk Pillar Leader** | The Exposure Management Lead or senior-most Detection Engineer at S3-S4, with documented delegation from the CISO. |
| **Governance Pillar Leader** | The NERC-CIP Compliance Manager or Policy & Standards Manager at S3-S4, with documented delegation from the CISO. |

### 5.4 Emergency Succession Documentation

For each emergency successor, the following documentation is maintained and reviewed semi-annually:

1. **Delegation of authority:** A signed document from the CISO (or board, for CISO succession) delegating specific decision authorities to the emergency successor during the interim period.
2. **Access verification:** Confirmation that the emergency successor has (or can rapidly obtain) access to all systems, accounts, and physical spaces needed to perform the role.
3. **Key contacts list:** The 10-15 people the emergency successor needs to contact in the first 24 hours: executive leadership, pillar leaders, key business stakeholders, regulators, critical vendors, the IR team lead.
4. **Standing decisions and deadlines:** A current list of pending decisions, upcoming deadlines, and active escalations that the emergency successor will inherit.
5. **Transition checklist:** Step-by-step actions for the first 24 hours, first week, and first month.

> **Emergency Succession Is Not Optional**
>
> An organization that cannot name who runs Engineering if the Engineering Pillar Leader is hit by a bus tomorrow has not planned; it has hoped. The emergency succession list must exist at all times. A blank emergency successor field for any Tier 1 role is a risk that should be reported to the CISO and recorded in the risk register.

---

## 6. Successor Development Plans

### 6.1 The Development Plan Format

For each successor rated "Ready in 1-2 Years" or "Ready in 3-5 Years," a development plan addresses the specific gaps preventing a "Ready Now" rating. The plan is owned by the successor's manager (or the incumbent, if the successor reports to a different manager) and reviewed at each quarterly check-in.

The development plan contains:

1. **Target role** and target readiness timeline
2. **Gap assessment:** Which CMP-001 competency domains are not yet at the target level? Which JA-001 management dimensions, if the target is a management role?
3. **Development actions** for each gap:
   - **Experiential:** Specific stretch assignments, interim role coverage, cross-pillar initiatives, or acting-manager rotations
   - **Educational:** Specific training, certification, or conference attendance per TRN-001
   - **Relational:** Specific exposure to the stakeholders, regulators, or executive forums the person would need to navigate in the target role
4. **Milestones:** Observable demonstrations that would indicate readiness progress (e.g., "led a CISO Risk & Posture Review presentation," "represented Engineering to a regulator walkthrough," "managed the team for two weeks during the incumbent's leave")
5. **Timeline:** When each action is planned and when readiness will be reassessed

### 6.2 Development by Readiness Gap

| Gap Domain | Typical Development Actions |
|---|---|
| **Strategic thinking** | Assign to lead a pillar strategy initiative. Invite to pillar leadership meetings as an observer-contributor. Pair with the incumbent for budget cycle process. |
| **Executive communication** | Assign to present at CISO Risk & Posture Review. Coach on written executive communications. Shadow the incumbent in board-preparation sessions. |
| **People leadership** | Assign a mentee or intern. Provide acting-manager rotation during the incumbent's leave. Enroll in management training. |
| **Stakeholder management** | Assign as the CERG representative in a cross-functional initiative. Accompany the incumbent to regulator/auditor meetings. Build relationships with key business stakeholders directly. |
| **Budget and resource management** | Involve in the budget planning cycle. Assign vendor relationship management for a tool or service. Review total cost of ownership for a function. |
| **Cross-pillar depth** | Extended cross-pillar rotation (2-4 weeks instead of 1 day). Lead a cross-pillar initiative. Author a standard or procedure in a different pillar's domain with that pillar's review. |

### 6.3 Tracking and Accountability

Successor development plan progress is reviewed at:
- **Quarterly check-ins** (PERF-001 §3.2): Progress against planned actions
- **Annual talent review**: Readiness re-rating based on demonstrated progress
- **CISO quarterly review**: The CISO reviews succession readiness for Tier 1 roles at each CISO Risk & Posture Review

A successor whose development plan shows no progress for two consecutive quarters is either not motivated, not capable, or not receiving the promised development support. The talent review addresses which it is and adjusts the plan or the readiness rating accordingly.

---

## 7. Cross-Pillar Succession

### 7.1 The Principle

Every Tier 1 critical role (CISO and pillar leaders) should have at least one potential successor who comes from a different pillar. The principle is an extension of the left-right knowledge model: a person who has led only Engineering their entire career will struggle to lead Risk or Governance without a deliberate development investment. But a person who knows two pillars deeply and the third well enough to collaborate is a stronger candidate for any pillar leadership role than someone who knows only one.

### 7.2 Cross-Pillar Successor Development

| Target Pillar Leader Role | Cross-Pillar Successor Might Come From | Key Development Need |
|---|---|---|
| **Engineering Pillar Leader** | Senior Risk practitioner (S3-S4) with strong technical background | Deepen engineering craft mastery; lead architecture initiatives; own reference architecture authority |
| **Risk Pillar Leader** | Senior Engineering practitioner (S3-S4) with strong analytical skills | Deepen risk methodology; lead threat assessments; own exposure reporting |
| **Governance Pillar Leader** | Senior Engineering or Risk practitioner (S3-S4) with regulatory exposure | Deepen compliance methodology; lead audit engagements; own regulatory relationships |
| **CISO** | Any pillar leader with cross-pillar experience and executive presence | Board communication; budget ownership at organizational scale; external stakeholder management |

### 7.3 Not a Requirement, a Direction

A Tier 1 role with no cross-pillar successor is not a crisis. It is a development priority for the next 2-3 years. The talent review identifies which pillar leaders have cross-pillar successor potential and adds cross-pillar development actions to their plans. Over multiple cycles, the succession bench becomes cross-pillar by development, not by coincidence.

---

## 8. Confidentiality and Access

### 8.1 Access Controls

The succession heat map, emergency succession list, and successor development plans are confidential. Access is restricted to:

- **CISO:** Full access to all succession materials
- **Pillar Leaders:** Access to succession materials for their pillar and cross-pillar successors from their pillar to other Tier 1 roles. A pillar leader does not see the succession plan for their own role (that is held by the CISO).
- **Board or designated board committee:** Access to CISO succession plan and summary of Tier 1 succession readiness (not individual names unless requested)
- **HR Business Partner:** Access to development plans (not heat maps) for coordination of training, budget, and personnel actions

### 8.2 Communication Guidelines

Succession information is communicated on a need-to-know basis:

| What | Who Is Told | What They Are Told | What They Are Not Told |
|---|---|---|---|
| **"Ready Now" successor** | The successor | "If this role became vacant, you would be a strong internal candidate. Let us discuss what you would need to be ready." | That they are the only Ready Now candidate, or that they have been formally designated |
| **"Ready in 1-2 Years" successor** | The successor | "We see a leadership path for you toward [role]. Here is the development plan to get you there." | Their specific readiness rating or how they compare to other successors |
| **Emergency successor** | The successor | "You are the designated emergency successor for [role]. Here is what that means and what you need." | Nothing about long-term succession |
| **No identified successor (Tier 1 role)** | CISO and board (summary) | "We have a succession gap for [role]. Here is our plan to address it." | Not shared with the broader team unless the role becomes vacant |

> **Do Not Promise Roles You May Not Be Able to Deliver**
>
> A manager who tells a team member "you are my successor" has made a promise that organizational changes, hiring decisions, or the person's own career choices may break. The succession framework identifies readiness and develops capability. It does not make commitments. A Ready Now rating is a professional assessment, not a job offer.

---

## 9. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-SUCC-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-27 |
| **Classification** | Confidential - CISO and Pillar Leaders |
| **Owner** | CISO |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual talent review; emergency succession list reviewed semi-annually |
| **Next Scheduled Review** | 2027-05-27 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.7.2 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-27 | Cyber Governance | Initial release. Establishes annual talent review cadence and succession planning framework for critical CERG roles. Defines four-tier readiness rating scale (Ready Now, Ready in 1-2 Years, Ready in 3-5 Years, No Identified Successor), succession heat map format, emergency succession protocol with 24-hour documentation requirements, successor development plan structure, cross-pillar succession requirements, and confidentiality and access controls. |

### Review Triggers

- Annual talent review (mandatory annual refresh)
- Any Tier 1 role incumbent departure, resignation notice, or extended leave
- Material change to organizational structure affecting role definitions
- CISO direction

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Job Architecture | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade expectations for successor readiness evaluation |
| Competency Model | [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Competency domains for gap assessment |
| Performance Management | [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | Input ratings for talent review |
| Training Framework | [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) | Development resources for successor plans |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster and role definitions |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Left-right knowledge model and talent resilience |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |

Governance owns the framework. The CISO owns the succession plans and heat maps produced under it. The CISO is responsible for initiating the annual talent review, maintaining the emergency succession list, and ensuring successor development plans are resourced and tracked.