# SURGE: Cyber Engineering, Risk & Governance

## CONTRACTOR AND NON-EMPLOYEE STAFF INTEGRATION GUIDE
### Role Eligibility · Knowledge Retention · Supervision · Onboarding and Offboarding

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CON-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) · [`CERG-GOV-ONB-001`](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) · [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) |
| **Review Cycle** | Annual / On any significant change to contractor population or engagement model |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.7.2 · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PS-7 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The Contractor Reality](#2-the-contractor-reality)
3. [Role Eligibility: Who Can Be a Contractor](#3-role-eligibility-who-can-be-a-contractor)
4. [Engagement Models](#4-engagement-models)
5. [Supervision and Accountability](#5-supervision-and-accountability)
6. [Knowledge Retention and Artifact Ownership](#6-knowledge-retention-and-artifact-ownership)
7. [Contractor Onboarding](#7-contractor-onboarding)
8. [Contractor Offboarding](#8-contractor-offboarding)
9. [Contractor Performance and Renewal](#9-contractor-performance-and-renewal)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

The CERG Framework (FRM-001) notes that the illustrative CERG team operates alongside "an equal population of consultants and contractors." The RACI Instrument (RAC-001) and Job Descriptions (JD-001) assume employees. The Onboarding Program (ONB-001) is built for permanent team members who will be with the organization for years, not contractors who may be engaged for a six-month audit cycle or a twelve-month platform migration.

This document closes the gap. It defines which CERG roles can be filled by contractors and which must remain employee-only, establishes the knowledge retention requirements that prevent a departing contractor from taking the only copy of critical artifacts, defines the supervision model (every contractor has a named employee supervisor who is accountable for the contractor's work product), and provides condensed onboarding and offboarding programs for non-employee staff.

It applies to all non-employee staff performing CERG work: independent contractors, consultants from professional services firms, staff augmentation personnel, and managed service providers whose personnel operate as embedded team members. It does not apply to external auditors, assessors, or penetration testing firms operating under a statement of work with defined deliverables and limited access, though the knowledge retention requirements in §6 apply to any artifacts those external parties produce.

> **Contractors Are a Force Multiplier, Not a Replacement for Capability**
>
> A contractor can accelerate a cloud migration, clear a vulnerability backlog, or run a CMMC assessment readiness program. A contractor cannot be the organization's institutional memory, its regulatory relationship, or its leadership bench. The Framework envisions a CERG team where contractors supplement, not substitute for, the employee core. This document ensures that distinction does not blur in practice.

---

## 2. The Contractor Reality

### 2.1 Why CERG Organizations Use Contractors

CERG-adopting organizations engage contractors for legitimate reasons:

- **Surge capacity.** A major platform migration, an audit cycle, or a regulatory deadline creates temporary workload that does not justify permanent headcount.
- **Specialized expertise.** A cryptographic migration, an OT security assessment, or a specific regulatory framework may require expertise the organization needs for 6-12 months and not permanently.
- **Initial build-out.** An organization adopting CERG for the first time may use contractors to accelerate the build-out while recruiting permanent staff.
- **Headcount constraints.** A budget that funds contractors but not employees is a reality in many organizations. The framework accommodates it without pretending it is ideal.

### 2.2 The Risks

Every contractor engagement carries three risks that this document is designed to mitigate:

1. **Knowledge flight.** A contractor who builds the threat model, designs the detection pipeline, or structures the evidence library and then departs takes that knowledge with them. If the knowledge is not captured in CERG repositories before they leave, the organization has lost both the person and the capability.

2. **Accountability diffusion.** A contractor who reports to an account manager at their firm, not to a CERG manager, operates without the performance management, feedback, and development that ensure quality. When the contractor's work is inadequate, the CERG manager may not discover it until the engagement ends and the cleanup falls to employees.

3. **Cultural separation.** A contractor who is not included in team meetings, not given a CERG buddy, and not expected to understand the left-right model operates as a hired tool, not a team member. Their work reflects their isolation: it meets the letter of the statement of work but misses the context that makes it integrate with the rest of CERG's output.

---

## 3. Role Eligibility: Who Can Be a Contractor

### 3.1 The Eligibility Matrix

| Canonical Role | Contractor Eligible? | Rationale |
|---|---|---|
| **CISO** | No | Executive role. Must be an employee. |
| **Executive Sponsor** | No | Business-side role; by definition an organizational insider. |
| **Engineering Pillar Leader** | No | Management role with organizational authority, budget ownership, and strategic accountability. |
| **Risk Pillar Leader** | No | Same rationale as Engineering Pillar Leader. |
| **Governance Pillar Leader** | No | Same rationale. Additionally, the regulatory relationships this role carries cannot reside with a non-employee. |
| **Cloud Security Engineer** | Yes | Surge capacity for cloud migrations, platform build-outs, and specific cloud expertise is a common contractor use case. |
| **Identity Engineer** | Yes | Specialized identity platform expertise (PAM deployment, federation architecture) is often contractor-delivered. |
| **OT Security Engineer** | Conditional | Yes for specific OT security assessments or architecture engagements. No for ongoing OT security operations in a NERC-CIP environment, where CIP-004 personnel risk assessment requirements make contractor use administratively heavy. |
| **Application Security Engineer** | Yes | Application security testing, SDLC integration, and tool deployment are common contractor engagements. |
| **Endpoint Engineer** | Yes | EDR deployment and migration are common contractor use cases. |
| **Cryptography Engineer** | Conditional | Yes for specific cryptographic migration or PKI deployment projects. No for ongoing key management operations due to the sensitivity of key material access. |
| **Exposure Management Lead** | Conditional | Yes for initial VM program build-out or backlog clearance. No for ongoing VM operations in a regulated environment, where the person managing vulnerability data should be an employee. |
| **Adversarial Testing Lead** | Yes | Penetration testing and red team operations are commonly contractor-delivered. A contractor Adversarial Testing Lead must be supervised by the Risk Pillar Leader; their findings become organizational risk register entries owned by employees. |
| **Threat Intelligence Analyst** | Yes | Threat intelligence production can be contractor-delivered, especially for sector-specific threat expertise. |
| **Vendor Risk Analyst** | Yes | Vendor assessment surge capacity (clearing a backlog, supporting a major procurement cycle) is a common contractor use case. |
| **OT Risk Analyst** | Conditional | Same rationale as OT Security Engineer: yes for specific assessments, no for ongoing operations in CIP environments. |
| **Identity Risk Analyst** | Yes | UEBA deployment and identity threat detection rule authoring can be contractor-delivered. |
| **Detection Engineer** | Yes | Detection rule authoring and SIEM migration are common contractor engagements. |
| **NERC-CIP Compliance Manager** | No | Regulatory relationship role. The person who represents the organization to its regional entity must be an employee. |
| **CMMC / Federal Compliance Manager** | No | Same rationale. The person who signs or represents the organization's CMMC posture must be an employee. |
| **SOX ITGC Lead** | Conditional | Yes for SOX readiness or remediation projects. No for ongoing SOX ITGC operations with external auditor relationship. |
| **Policy & Standards Manager** | Conditional | Yes for document library build-out or framework migration. No for ongoing policy and standards management, which requires organizational authority to enforce. |
| **Risk Register Owner** | No | The person who curates the risk register and runs the Monthly Risk Register Review must be an employee. Risk acceptance decisions and exception management require organizational authority. |
| **Evidence Librarian** | Yes | Evidence collection and organization can be contractor-delivered, especially during audit preparation surges. |

### 3.2 The "Must Be Employee" Principle

A role must be filled by an employee when it:
- Holds risk acceptance or approval authority
- Maintains a primary regulatory relationship with an external auditor, assessor, or regulator
- Manages employees (contractors cannot supervise employees)
- Makes or concurs on budget decisions
- Is accountable for organizational strategy or policy enforcement

> **"Conditional" Means "Ask Before You Engage"**
>
> A role marked Conditional is not a blanket authorization. Each Conditional contractor engagement requires the pillar leader and the CISO to confirm that the specific engagement does not cross the "must be employee" boundaries above. Document the confirmation. A Conditional role engaged without this confirmation is a compliance finding waiting to happen.

---

## 4. Engagement Models

### 4.1 Staff Augmentation

The contractor operates as an embedded team member under the day-to-day direction of a CERG employee manager. They attend team meetings, use CERG tools and repositories, and follow CERG procedures. Their deliverables are integrated into the team's standing output, not delivered as a separate work product.

**Best for:** Surge capacity in roles where the work is ongoing and the contractor needs to collaborate closely with the team (Cloud Security Engineer, Detection Engineer, Vendor Risk Analyst).

**Supervision:** Daily direction from a named CERG employee. The contractor's firm provides administrative support (payroll, benefits, compliance) but does not direct the work.

### 4.2 Project-Based Engagement

The contractor or consulting firm delivers a defined scope of work against a statement of work with milestones, deliverables, and acceptance criteria. The contractor operates with a degree of independence, providing updates at defined intervals rather than participating in daily team operations.

**Best for:** Specialized, time-bounded initiatives (PKI migration, CMMC assessment readiness, SIEM deployment, vulnerability backlog clearance).

**Supervision:** The CERG employee who owns the project outcome is accountable for the contractor's deliverables. The contractor manages their own day-to-day work within the SOW boundaries.

### 4.3 Managed Service

An external provider operates a CERG function or sub-function on an ongoing basis. For example, a managed security service provider (MSSP) operating the SIEM and detection pipeline, or a third-party risk management firm conducting vendor assessments.

**Best for:** Functions that are important but not core to the organization's differentiated security capability, or functions where the organization cannot recruit and retain the necessary expertise.

**Supervision:** A CERG employee (typically a pillar leader or senior manager) owns the service relationship, reviews service levels, and is accountable for the function's output. The managed service provider operates per a service level agreement (SLA) with defined metrics, escalation paths, and regular service reviews.

---

## 5. Supervision and Accountability

### 5.1 The Named Supervisor Rule

Every contractor, regardless of engagement model, has a named CERG employee who is accountable for the contractor's work product. The supervisor:

- Approves the contractor's access to CERG systems, tools, and repositories
- Reviews the contractor's work at defined intervals appropriate to the engagement (daily for staff augmentation, milestone-based for project engagements, monthly for managed services)
- Is the escalation point for issues with the contractor's quality, responsiveness, or conduct
- Signs off on the contractor's deliverables before they are accepted as complete
- Ensures the contractor's artifacts are stored in CERG repositories (§6)
- Conducts the contractor's offboarding (§8)

The supervisor is not the contractor's "manager" in the employment sense. They do not conduct performance reviews, approve time off, or manage the contractor's career development. They are accountable for what the contractor produces and for ensuring the organization retains it when the contractor leaves.

### 5.2 Supervision by Engagement Model

| Engagement Model | Supervision Cadence | Review Method |
|---|---|---|
| **Staff Augmentation** | Daily or near-daily | Work product review; inclusion in team meetings and rituals; informal feedback as with employees |
| **Project-Based** | Weekly or milestone-based | Deliverable review against SOW; progress against timeline; issue escalation |
| **Managed Service** | Monthly service review; quarterly business review | SLA performance review; service improvement planning; relationship health check |

---

## 6. Knowledge Retention and Artifact Ownership

### 6.1 The Repository Rule

All contractor-produced artifacts must be stored in CERG-controlled repositories, not on contractor devices, contractor firm systems, or contractor-managed cloud platforms. This applies to:

- Code: Infrastructure-as-code, policy-as-code, detection rules, automation scripts
- Documents: Architecture diagrams, threat models, risk assessments, compliance documentation, finding reports
- Configurations: Tool configurations, platform settings, baseline definitions
- Data: Scan results, assessment data, evidence items, risk register entries
- Credentials: No contractor stores CERG credentials outside the organization's approved secrets management system

### 6.2 The Artifact Handoff Protocol

At defined intervals (at least monthly for staff augmentation, at each milestone for project engagements, and at minimum quarterly for managed services), the contractor transfers all work-in-progress artifacts to the CERG repository. The supervisor verifies the transfer by:

1. Confirming that the artifacts exist in the CERG repository
2. Opening a sample of artifacts to confirm they are complete and usable, not stubs
3. Confirming that the contractor has not retained copies on non-CERG systems (for regulated environments, this may require a documented verification)

### 6.3 Prohibited Practices

The following are explicitly prohibited:

- **Contractor-maintained repositories.** A contractor who sets up a GitHub organization, a shared drive, or a Confluence space for CERG work has created a knowledge silo the organization cannot access when the contractor leaves. All work product must flow into CERG repositories within one week of creation.
- **Contractor-owned tooling accounts.** A contractor who registers a cloud security tool, a threat intelligence platform, or a GRC instance under their own or their firm's account has created an access dependency. All CERG tooling must be provisioned under organizational accounts.
- **Contractor-exclusive knowledge.** A contractor who is the only person who knows how a specific tool is configured, a specific process works, or a specific system is architected represents a knowledge flight risk. The supervisor must ensure that at least one employee understands the contractor's work well enough to operate it after the contractor departs.

> **The Contractor's Laptop Is Not the Organization's Repository**
>
> A contractor who leaves with the only copy of the threat model on their laptop has not delivered a threat model; they have borrowed one to the organization for the duration of their engagement. The artifact handoff protocol exists to ensure that borrowed becomes owned before the engagement ends.

---

## 7. Contractor Onboarding

### 7.1 Condensed Onboarding Program

Contractors follow a condensed version of the employee onboarding program (ONB-001). The condensed program recognizes that a contractor engaged for 3-12 months does not need the full 90-day program but does need enough context to be effective and enough access to be productive.

| Timeframe | Activity |
|---|---|
| **Before day one** | Supervisor provisions access per ONB-001 §3. Supervisor prepares a contractor-specific 30-day plan focused on the engagement's objectives, not long-term development. |
| **Day one** | Access verification. CERG overview (90-minute version: what CERG is, the three pillars, the contractor's role in the engagement). Introduction to immediate teammates. |
| **Week one** | Read CERG 101 core documents relevant to the engagement (FRM-001 §§1-3, OM-001 §§3-4, the standards and procedures specific to the contractor's domain). Meet key stakeholders. Begin work under supervision. |
| **Day 30** | First artifact handoff (§6.2). Supervisor review of work quality and integration with the team. Adjustment of scope, access, or supervision based on first-month performance. |

### 7.2 What Contractors Do Not Receive

Contractors do not receive:

- **CERG 101 full curriculum.** The condensed reading is sufficient for a time-bounded engagement.
- **Cross-pillar rotation.** Contractors may interact with other pillars as their work requires but are not assigned formal rotation days.
- **Career development planning.** The contractor's development is their firm's responsibility, not CERG's.
- **Performance reviews in the CERG format.** The contractor's performance is evaluated against their SOW, not against CMP-001 competency anchors.
- **A CERG buddy.** The supervisor provides the orientation and support a buddy would provide.

### 7.3 Access Limitations

Contractor access to CERG systems is role-appropriate and time-bounded:

- Access is provisioned for the duration of the engagement plus a defined transition period, not indefinitely
- Access to the risk register, evidence library, and policy repository is read/write as needed for the role but audited
- Access to sensitive systems (PAM, HSM, key management, board reporting) is limited and logged
- All contractor access is reviewed at each artifact handoff and revoked at offboarding

---

## 8. Contractor Offboarding

### 8.1 The Offboarding Checklist

Contractor offboarding begins two weeks before the engagement end date (or immediately, if the engagement ends early). The supervisor and the contractor complete the following checklist:

| Item | Owner | Timeline |
|---|---|---|
| **Final artifact handoff.** All contractor-produced artifacts are in CERG repositories. The supervisor has verified completeness (§6.2). | Supervisor + Contractor | No later than 3 business days before end date |
| **Knowledge transfer.** The contractor has documented or verbally transferred any undocumented knowledge about their work to the supervisor or a designated employee. This includes: tool configurations, known issues, workarounds, undocumented dependencies, and "the thing I was going to fix next week." | Contractor + Supervisor | No later than 3 business days before end date |
| **Access revocation.** All system access, accounts, credentials, VPN, and physical access are revoked. The supervisor confirms with IT/security that revocation is complete. | Supervisor + IT | End date (no later than end of business) |
| **Credential rotation.** Any credentials the contractor had access to (service accounts, API keys, shared secrets) are rotated within 5 business days of the end date. | Supervisor + relevant Engineering team | Within 5 business days |
| **Equipment return.** All organization-owned equipment is returned, wiped, or remotely deprovisioned. | Supervisor + IT | End date |
| **Data retention confirmation.** The contractor confirms in writing that they have not retained CERG data, artifacts, or credentials on personal or firm-owned systems. For regulated environments, this confirmation may be a contractual obligation in the SOW. | Contractor | End date |
| **Exit interview (optional).** For long-duration or high-impact engagements, the supervisor conducts a 30-minute exit interview: what worked, what did not, what would the contractor recommend CERG do differently? The feedback is documented and reviewed for engagement model improvements. | Supervisor | Before end date |

### 8.2 Post-Departure Verification

Within one week of the contractor's departure:

1. The supervisor opens and verifies that key artifacts can be accessed and understood by an employee who was not involved in the engagement. The test: can a peer pick up where the contractor left off?
2. The supervisor confirms that no standing meetings, automated reports, or scheduled processes depend on the contractor's account or credentials.
3. If the engagement will be renewed or a replacement contractor engaged, the supervisor documents lessons learned for the next engagement.

> **Offboarding Is Not Complete Until the Artifacts Are Verified**
>
> A contractor who hands over a repository link, shakes hands, and departs has been transitioned. A contractor whose artifacts have been opened, read, and confirmed usable by an employee who was not part of the engagement has been offboarded. The difference is the difference between a knowledge transfer that happened and one that was assumed to have happened. Assume nothing. Verify.

---

## 9. Contractor Performance and Renewal

### 9.1 Performance Evaluation

Contractor performance is evaluated against the SOW, not against CMP-001 competency anchors. The evaluation addresses:

| Dimension | Question |
|---|---|
| **Quality** | Does the contractor's work meet the standard defined in the SOW? Does it integrate with the team's work without requiring significant rework? |
| **Timeliness** | Are deliverables on schedule? Are issues escalated early or discovered late? |
| **Collaboration** | Does the contractor communicate effectively with the team? Do they share knowledge or hoard it? Do they follow CERG procedures or work around them? |
| **Knowledge transfer** | Is the contractor producing artifacts that are complete and usable? Are they documenting their work without being chased? |

### 9.2 Engagement Renewal

Contractor engagement renewal is a deliberate decision, not an automatic extension. The supervisor evaluates:

1. **Is the work still needed?** The surge that justified the engagement may have passed.
2. **Has the organization developed internal capability?** The engagement may have served its purpose of bridging to an employee hire or developing an internal team member.
3. **Is the contractor the right resource?** The evaluation dimensions above inform whether the same contractor or firm should be re-engaged.
4. **Is the engagement model still appropriate?** A project-based engagement that has become ongoing operational work should be converted to staff augmentation or a managed service, or the work should be absorbed by employees.

An engagement that is renewed more than twice should trigger a review of whether the role should be converted to an employee position. A function that depends on contractors indefinitely has a structural gap that headcount planning should address.

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CON-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any significant change to contractor population or engagement model |
| **Next Scheduled Review** | 2027-05-27 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.7.2; NIST 800-53r5 PS-7 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-27 | Cyber Governance | Initial release. Defines role eligibility matrix identifying which CERG roles can be contractor-filled and which must remain employee-only. Establishes three engagement models (staff augmentation, project-based, managed service), the named supervisor rule, knowledge retention and artifact handoff protocols, condensed contractor onboarding program, mandatory offboarding checklist with post-departure verification, and contractor performance evaluation and renewal criteria. |

### Review Triggers

- Material change to the contractor population (new roles engaged, significant increase in contractor ratio)
- Change to regulatory requirements affecting contractor personnel (CIP-004, CMMC, etc.)
- Lessons learned from a contractor engagement that ended with knowledge retention issues
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster; engagement models |
| Job Architecture | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade structure (contractors are typically engaged at S2-S4 level) |
| RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Accountabilities that determine role eligibility |
| Onboarding Program | [`CERG-GOV-ONB-001`](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) | Full employee onboarding (condensed version for contractors) |
| Implementation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Organizational adoption of CERG |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Illustrative staffing model referencing contractors |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.