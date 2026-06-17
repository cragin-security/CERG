# SURGE: Cyber Engineering, Risk & Governance

## TRAINING, DEVELOPMENT, AND CERTIFICATION FRAMEWORK
### Certification Matrix · Development Curriculum · Budget Guidance · Cross-Training

---

| | |
|---|---|
| **Document ID** | CERG-GOV-TRN-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) · [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) · [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) · [`CERG-GOV-ONB-001`](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) |
| **Review Cycle** | Annual / On any change to certification requirements or competency model |
| **Frameworks** | [NIST NICE Workforce Framework](https://www.nist.gov/itl/applied-cybersecurity/nice) (SP 800-181r1) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.7.2 · [DoD 8140.03](https://public.cyber.mil/wid/dcwf/) |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Training Philosophy](#2-training-philosophy)
3. [Certification Matrix: Required, Recommended, and Aspirational](#3-certification-matrix-required-recommended-and-aspirational)
4. [Training Curriculum by Competency Domain](#4-training-curriculum-by-competency-domain)
5. [Cross-Training: The 5% Rule](#5-cross-training-the-5-rule)
6. [Professional Development Budget](#6-professional-development-budget)
7. [Conference and External Engagement](#7-conference-and-external-engagement)
8. [Training Administration](#8-training-administration)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

Cybersecurity skills have a half-life measured in months, not years. A Detection Engineer whose knowledge stops advancing writes rules for last year's threats. A Cloud Security Engineer who does not track platform evolution reviews architectures against a mental model that is already obsolete. A NERC-CIP Compliance Manager who does not monitor regulatory developments discovers a new requirement when the auditor cites it.

The Job Descriptions (JD-001) list relevant certifications per role. They do not define which are required, which are recommended, who pays, or how certification connects to progression. The Competency Model (CMP-001) defines what good looks like at each grade. It does not define the path to get there. This document closes both gaps.

It provides a role-to-certification matrix with three tiers (required, recommended, aspirational) per role and grade, a training curriculum mapped to CMP-001 competency domains, a cross-training standard that operationalizes the left-right knowledge model into a measurable time commitment, a professional development budget guideline, and conference and external engagement expectations.

It applies to every CERG team member. Certifications are role-dependent; the training philosophy, cross-training expectation, and budget guidelines are universal.

> **Training Is an Investment, Not a Perk**
>
> An organization that treats training as a reward for good performance is sending a signal that capability development is optional. An organization that treats training as a recurring operational expense, budgeted, tracked, and expected, is building a team that gets better every quarter. The first organization loses its best people to the second.

---

## 2. Training Philosophy

1. **Development is a shared responsibility.** The organization provides the budget, the time, and the curriculum. The individual provides the effort, the curiosity, and the follow-through. Neither party can succeed without the other.

2. **Certifications validate, they do not replace.** A certification confirms that a person has demonstrated a body of knowledge at a point in time. It does not confirm that they apply it effectively in their role. Certifications are useful for hiring credibility, regulatory compliance, and structured learning. They are not a substitute for demonstrated competency.

3. **Training closes the gap between current and target.** Every development activity should connect to a gap identified in the person's performance review (PERF-001) or their self-assessment against the competency model (CMP-001). "I want to learn Kubernetes security" is a valid interest. "I need to learn Kubernetes security because my next-grade competency anchor requires architecture reviews of containerized workloads" is a development plan.

4. **Cross-training is not optional.** The left-right knowledge model (FRM-001 §9.2) depends on every CERG team member understanding the other two pillars well enough to collaborate effectively. Cross-training is a standing expectation, not a discretionary activity.

5. **Knowledge shared is knowledge multiplied.** If the organization sends a person to a conference, a training course, or a certification boot camp, that person presents what they learned to the team. The organization's return on the training investment includes not just one person's capability gain but the team's.

---

## 3. Certification Matrix: Required, Recommended, and Aspirational

### 3.1 Certification Tiers

| Tier | Definition | Who Pays | Timeline |
|---|---|---|---|
| **Required** | The person must hold this certification to perform the role. Required certifications are listed in the job description and verified at hire or within a defined post-hire window. | Organization | Maintained continuously; new hires have 6-12 months to obtain if not held at hire |
| **Recommended** | The certification materially improves the person's capability in their role and is expected within the first 18-24 months. | Organization | Expected within 18-24 months of role entry or grade advancement |
| **Aspirational** | The certification represents advanced capability in the role or a related domain. It is a development target for progression to the next grade. | Organization (if aligned to development plan) or individual with organizational support | No fixed timeline; pursued when aligned to development priorities |


> **NICE Mapping**: The NICE Work Role(s) associated with each certification are documented in [JF-002](../roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md). Each certification row below supports the NICE Work Role mapping for the corresponding CERG role. See the individual per-role JD documents for role-specific NICE TKS statement references.

### 3.2 Engineering Pillar: Certification Matrix

#### Cloud Security Engineer

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ or equivalent | AWS Certified Security - Specialty, Microsoft AZ-500, or Google Professional Cloud Security Engineer (one, platform-dependent) | CCSP |
| **S2** | Platform security certification relevant to the organization's primary cloud (as above) | Second platform certification; Terraform Associate or equivalent IaC certification | CISSP, CCSP |
| **S3** | CISSP or CCSP | SANS GIAC (GCLD, GPCS, or relevant cloud security GIAC); Kubernetes security certification (CKS) | ISSAP, platform architecture certifications |
| **S4** | CISSP | One additional advanced certification (ISSAP, ISSMP, or SANS GIAC expert-level) | Industry contributions in lieu of further certifications |

#### Identity Engineer

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | Microsoft SC-300 or equivalent IdP certification | - |
| **S2** | One IdP-specific certification (SC-300, Okta Certified Professional, etc.) | Second IdP certification; basic PAM certification | CISSP |
| **S3** | CISSP | Advanced identity certification (e.g., SC-100, Okta Certified Architect); PAM certification | ISSAP, CIAM-related certification |
| **S4** | CISSP | ISSAP or ISSMP | - |

#### OT Security Engineer

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | GICSP or ISA/IEC 62443 Cybersecurity Specialist | - |
| **S2** | GICSP | ISA/IEC 62443 Expert; CISSP | SANS GIAC (GRID, GCIP) |
| **S3** | CISSP | SANS GIAC relevant to OT; NERC-CIP-specific training if applicable | ISSAP |
| **S4** | CISSP | Advanced ICS/SCADA security certification | - |

#### Application Security Engineer

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | CSSLP or Certified Ethical Hacker (CEH) | - |
| **S2** | CSSLP or CEH | GWEB or relevant SANS GIAC; OWASP certification | CISSP |
| **S3** | CISSP | GWEB, GMOB, or GPEN; cloud-native security (CKS or equivalent) | ISSAP |
| **S4** | CISSP | ISSAP | - |

#### Endpoint Engineer

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | Vendor-specific EDR certification | - |
| **S2** | One EDR/endpoint security certification | Second platform certification; OS-specific security certification | CISSP |
| **S3** | CISSP | GCFE, GNFA, or relevant SANS GIAC | ISSAP |
| **S4** | CISSP | ISSAP or additional GIAC expert-level | - |

#### Cryptography Engineer

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | Vendor PKI/HSM certification | - |
| **S2** | One cryptography or PKI certification | CISSP | SANS GIAC (GSE or relevant crypto) |
| **S3** | CISSP | SANS GIAC advanced crypto; FIPS/Common Criteria training | ISSAP |
| **S4** | CISSP | ISSAP | - |

### 3.3 Risk Pillar: Certification Matrix

#### Exposure Management Lead

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | Qualys/ Tenable/ Rapid7 certified specialist (platform-dependent) | CEH |
| **S2** | One exposure management platform certification | CEH or GPEN; CISSP | GCIH |
| **S3** | CISSP | GPEN, GCIH, or GWAPT | OSCP, OSWE |
| **S4** | CISSP | Two or more advanced GIAC certifications | - |

#### Adversarial Testing Lead

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | CEH | GPEN |
| **S2** | GPEN or CEH (Practical) | OSCP; GWAPT | CISSP |
| **S3** | OSCP | OSCE/OSEP; CISSP; cloud penetration testing certification | GXPN, OSEE |
| **S4** | CISSP | OSEE or equivalent expert-level offensive certification | - |

#### Threat Intelligence Analyst

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | CTIA or equivalent | GCTI |
| **S2** | GCTI or CTIA | CISSP; OSINT certification | GREM |
| **S3** | CISSP | GCTI (if not already held); GREM | Advanced threat intelligence (GCTI expert, FOR578) |
| **S4** | CISSP | GREM or equivalent | - |

#### Vendor Risk Analyst

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | CTPRP or equivalent | - |
| **S2** | CTPRP or equivalent | CISSP; CISA | CRISC |
| **S3** | CISSP | CISA or CRISC; Shared Assessments CTPRP | CGEIT |
| **S4** | CISSP | CISA, CRISC, or CGEIT | - |

#### Detection Engineer

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | SIEM platform certification (Splunk, Sentinel, Chronicle) | GCIA |
| **S2** | SIEM platform certification | GCIA or GCDA; CISSP | GNFA |
| **S3** | CISSP | GCIA, GCDA, or GNFA | GSE, advanced forensics |
| **S4** | CISSP | Two or more advanced GIAC detection/forensics certifications | - |

#### OT Risk Analyst

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | GICSP | - |
| **S2** | GICSP | ISA/IEC 62443; CISSP | GRID |
| **S3** | CISSP | GRID, GCIP | Advanced ICS security |
| **S4** | CISSP | Two or more relevant GIAC certifications | - |

#### Identity Risk Analyst

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | UEBA platform certification | - |
| **S2** | One identity security or UEBA certification | CISSP; GCIA | GNFA |
| **S3** | CISSP | GNFA or equivalent | Advanced identity threat detection |
| **S4** | CISSP | Two or more relevant certifications | - |

### 3.4 Governance Pillar: Certification Matrix

#### NERC-CIP Compliance Manager

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | NERC CIP-specific training (NERC-approved) | CISA |
| **S2** | NERC CIP training completion; Security+ | CISA; CISSP | CRISC |
| **S3** | CISSP or CISA | CRISC; advanced NERC compliance training | CGEIT |
| **S4** | CISSP | CISA and CRISC; or CGEIT | - |

#### CMMC / Federal Compliance Manager

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | CMMC RP or equivalent | CISA |
| **S2** | CMMC RP | CMMC RPA; CISA; CISSP | CRISC |
| **S3** | CISSP or CISA | CMMC RPA (if not held); CCA (once available); CRISC | CGEIT |
| **S4** | CISSP | CISA and CRISC; CCA | - |

#### SOX ITGC Lead

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | SOX/ITGC-specific training | CISA |
| **S2** | CISA (or in progress) | CISSP; CRISC | CIA |
| **S3** | CISA | CISSP; CRISC | CGEIT |
| **S4** | CISA and CISSP | CRISC or CGEIT | - |

#### Policy & Standards Manager

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | ISO 27001 Lead Implementer or Auditor | CISA |
| **S2** | ISO 27001 Lead Implementer or Auditor | CISSP; CISA | CRISC |
| **S3** | CISSP or CISA | CRISC; CGEIT | Advanced GRC certification |
| **S4** | CISSP | CISA and CRISC; or CGEIT | - |

#### Risk Register Owner

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | FAIR or equivalent risk analysis training | CRISC |
| **S2** | FAIR certification or equivalent | CISSP; CRISC | CISA |
| **S3** | CISSP or CRISC | CISA | CGEIT |
| **S4** | CISSP | CRISC and CISA; or CGEIT | - |

#### Evidence Librarian

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **S1** | CompTIA Security+ | GRC platform certification | CISA |
| **S2** | One GRC or audit-related certification | CISA (or in progress) | CISSP |
| **S3** | CISA | CISSP; evidence management or e-discovery certification | CRISC |
| **S4** | CISA | CISSP or CRISC | - |

### 3.5 Management Track Certification Addendum

CERG managers add the following to their home role family's certification matrix:

| Grade | Required | Recommended | Aspirational |
|---|---|---|---|
| **M1 Manager** | CISSP or CISM (if not already held) | Leadership or management training (instructor-led, not self-paced) | PMP or equivalent program management certification |
| **M2 Senior Manager** | CISM or CISSP | PMP or equivalent; advanced management training | CGEIT, CRISC |
| **M3 Principal Manager** | CISM | CGEIT or CRISC | Executive education program |
| **M4 Director** | CISM or equivalent executive cybersecurity certification | Executive education; board governance training | Industry recognition in lieu of further certifications |

> **Certification Is a Floor, Not a Ceiling**
>
> A person who holds every Aspirational certification for their role and grade is not required to stop pursuing credentials. The tiers represent what the organization commits to supporting. Beyond the Aspirational tier, the individual and their manager make the case for organizational support based on relevance to the person's development plan and the organization's needs.

---

## 4. Training Curriculum by Competency Domain

### 4.1 How the Curriculum Works

The training curriculum is organized by CMP-001 competency domain. For each domain, specific training resources, courses, and experiences are recommended at three levels aligned to CERG grades:

- **Foundational** (S1-S2): Builds the base of competence
- **Intermediate** (S2-S3): Deepens capability and adds breadth
- **Advanced** (S3-S4): Develops organizational-level expertise

A person's development plan (PERF-001) identifies which domains and which level are the priority for the current review period. The curriculum provides the resources. The manager and the individual select the specific courses and experiences.

### 4.2 Technical Depth

| Level | Resources |
|---|---|
| **Foundational** | Vendor-specific certification tracks (AWS, Azure, GCP security; Splunk, Sentinel, Chronicle; ServiceNow GRC; Tenable, Qualys, CrowdStrike, etc.); platform-specific security courses; internal pairing with senior practitioners |
| **Intermediate** | SANS GIAC technical courses (GCIA, GCDA, GCLD, GPCS, GWEB, GMOB, GPEN, GCIH, GREM, GNFA, GCFE, GCIP, GRID, GCTI, GICSP); OSCP/OSEP; CSSLP; advanced vendor certifications |
| **Advanced** | SANS GIAC expert-level (GSE, GXPN); advanced cloud architecture (AWS Solutions Architect Professional, Azure Solutions Architect Expert); OSEE; research and publication; teaching internal courses |

### 4.3 Cross-Pillar Fluency

| Level | Resources |
|---|---|
| **Foundational** | CERG 101 curriculum (ONB-001); cross-pillar rotation program; reading the standards and procedures of the other two pillars |
| **Intermediate** | Cross-pillar working group participation; paired work on cross-pillar initiatives; CISSP (broad coverage across domains); reading NIST CSF and NIST 800-53 for the frameworks outside the person's primary pillar |
| **Advanced** | Cross-pillar initiative leadership; representing CERG in multi-function forums; contributing to standards outside the person's primary pillar; mentoring across pillars |

### 4.4 Risk Judgment

| Level | Resources |
|---|---|
| **Foundational** | FAIR training; CERG Risk Taxonomy (TAX-001); CERG Risk Management Framework (RMF-001); internal pairing on risk assessment |
| **Intermediate** | CRISC; quantitative risk analysis training; sector-specific threat assessment training; internal risk assessment authorship with senior review |
| **Advanced** | Advanced quantitative risk methods; scenario-based risk exercises (tabletop facilitation); contributing to organizational risk appetite calibration; external risk methodology contributions |

### 4.5 Communication

| Level | Resources |
|---|---|
| **Foundational** | Technical writing courses; presentation skills training; internal presentation practice (pillar meetings) |
| **Intermediate** | Executive communication training; audit and regulator communication simulation; written analysis with senior review; representing the pillar in cross-functional meetings |
| **Advanced** | Media and public speaking training; conference presentation; board-level communication preparation; mentoring junior team members on communication |

### 4.6 Operational Discipline

| Level | Resources |
|---|---|
| **Foundational** | CERG procedure training (role-specific); internal tool training; evidence management training (AUD-001); pairing with senior team members on operational workflows |
| **Intermediate** | ITIL Foundation; process improvement methodology; procedure authorship; operational metric design |
| **Advanced** | Process design and optimization; Lean/Six Sigma (if applicable); operational framework design; pillar-level operational improvement initiatives |

### 4.7 Compliance and Regulatory Literacy

| Level | Resources |
|---|---|
| **Foundational** | Framework-specific training (NERC-CIP, CMMC, SOX, ISO 27001); CERG compliance documentation; shadowing audit walkthroughs |
| **Intermediate** | CISA; lead auditor training (ISO 27001, or framework-specific); regulatory change monitoring; control mapping methodology |
| **Advanced** | CGEIT; regulatory engagement (direct interaction with regulators/assessors); contributing to regulatory development; organizational regulatory strategy |

### 4.8 Continuous Learning

| Level | Resources |
|---|---|
| **Foundational** | Organizational learning platform access; cybersecurity news and threat feeds; internal brown-bag sessions; foundational certifications |
| **Intermediate** | Conference attendance (as participant); ISAC/industry group membership; advanced certifications; internal training delivery |
| **Advanced** | Conference presentations; industry working group participation; research and publication; mentoring the team's learning culture |

---

## 5. Cross-Training: The 5% Rule

### 5.1 The Standard

Every CERG team member is expected to spend at least 5% of their working time on cross-pillar learning and engagement. For a full-time team member, this is approximately:

- **2 hours per week**, or
- **One day per month**, or
- **Two weeks per year**

This is a performance expectation, not a suggestion. A person who has not engaged with the other two pillars in a quarter should be asked why during their quarterly check-in.

### 5.2 What Counts

Acceptable cross-training activities include:

- Cross-pillar rotation days beyond the onboarding program (ONB-001 §9)
- Participating in cross-pillar working groups or projects
- Attending standing meetings of another pillar (as an observer-contributor)
- Shadowing a senior practitioner in another pillar for a specific activity
- Reading and providing feedback on a draft standard or procedure from another pillar
- Jointly investigating a cross-pillar incident or finding
- Teaching a brown-bag session on a topic relevant to another pillar
- Self-directed study of another pillar's tools, frameworks, or methods

### 5.3 Tracking

The OM-001 §10.4 cross-training log captures cross-training activities. Managers review the log during quarterly check-ins. The log does not need to be granular (it is not a timesheet). It needs to answer: in the last quarter, what did this person do to understand the other two pillars better?

> **The 5% Rule Is a Minimum, Not a Cap**
>
> An Advisor who spends 10% of their time on cross-pillar work because they are leading a cross-pillar initiative is not violating the rule; they are demonstrating advanced Cross-Pillar Fluency. The 5% floor is for team members who are not naturally pulled into cross-pillar work through their role. It ensures that cross-pillar understanding does not become a privilege of seniority.

---

## 6. Professional Development Budget

### 6.1 Per-Person Allocation

CERG organizations should budget an annual per-person professional development allocation. The recommended baseline, adjusted for organizational size and budget, is:

| Allocation Level | Amount (USD, Annual) | Appropriate For |
|---|---|---|
| **Minimum** | $3,000 | Early-stage organization, constrained budget. Covers certification exam fees, one online course or local conference, and basic training platform access. |
| **Target** | $5,000-$8,000 | Established program. Covers certification training and exam, one major conference or SANS course, and ongoing training platform access. |
| **Competitive** | $10,000+ | Mature program competing for top-tier talent. Covers SANS training + GIAC certification, major industry conference attendance, executive education, and external coaching for managers. |

### 6.2 What the Budget Covers

The professional development budget covers:

| Expense | Covered? | Notes |
|---|---|---|
| Certification exam fees | Yes | First attempt only; retakes require manager approval and a study plan |
| Certification preparation courses or materials | Yes | Up to reasonable cost; self-study materials are preferred over boot camps unless the certification requires hands-on lab access |
| Conference registration | Yes | With conference attendance criteria (§7) |
| Conference travel and accommodation | Yes | Per organizational travel policy |
| Training platform subscriptions | Yes | Organization-wide licenses where cost-effective |
| Academic tuition (degree programs) | Partial or case-by-case | Tuition reimbursement per organizational policy; must be relevant to the person's role or progression |
| Professional association memberships | Yes | ISACA, ISC2, ISSA, SANS, ISAC memberships |
| Books and self-study materials | Yes | Reasonable cost; manager approval for items over a defined threshold |

### 6.3 Budget Administration

- The budget is per person, not per team. A manager cannot reallocate a departing team member's unspent budget to a conference trip for themselves.
- Unspent budget does not roll over. The annual cycle encourages regular development activity, not end-of-year spending sprees.
- Budget requests beyond the annual allocation require a business case: what will the person learn, how does it connect to their development plan, and what is the expected organizational benefit?

---

## 7. Conference and External Engagement

### 7.1 Conference Attendance Criteria

The organization supports conference attendance when:

1. The conference content is directly relevant to the person's role or development priorities.
2. The person commits to presenting what they learned to the team within two weeks of returning (a 30-minute brown-bag session, a written summary, or an internal training module).
3. Conference attendance is distributed fairly across the team. The same person attending three conferences while a peer attends none is a signal that the team's development investment is not equitable.

### 7.2 Priority Conferences by Role Family

| Role Family | Priority Conferences |
|---|---|
| **Engineering** | AWS re:Inforce, Microsoft Ignite (security track), Google Cloud Next (security track), KubeCon (security track), fwd:cloudsec, SANS Security East/West |
| **Risk** | RSA Conference, Black Hat, DEF CON, SANS Threat Hunting & IR Summit, FIRST Conference, sector-specific ISAC summits |
| **Governance** | RSA Conference (GRC track), ISACA conferences, IIA conferences, NIST workshops, sector-specific regulatory conferences |
| **Cross-Cutting** | Local BSides events, OWASP Global AppSec, regional cybersecurity summits |

### 7.3 External Engagement Expectations

At the Advisor (S3) level and above, external engagement is an expectation, not a perk:

| Grade | External Engagement Expectation |
|---|---|
| **S1-S2** | Encouraged to attend local events and webinars. Conference attendance supported when aligned to development priorities. |
| **S3** | Expected to attend at least one major conference per year. Encouraged to submit a presentation proposal. Participating in an industry working group or ISAC. |
| **S4** | Expected to present at conferences, participate in industry working groups or standards bodies, and contribute to the broader cybersecurity community. External engagement is part of the Sr. Advisor's influence dimension (CMP-001 §4.6). |

> **External Engagement Is Recruitment**
>
> A Sr. Advisor who presents at RSA, contributes to a NIST working group, and is known in their sector's threat-sharing community is not just developing themselves. They are making the organization visible as a place where serious cybersecurity practitioners work. A candidate who researches the organization and finds its engineers presenting at conferences is more likely to apply than one who finds no public presence at all. External engagement is part of the employer brand strategy.

---

## 8. Training Administration

### 8.1 Individual Development Plan

Each team member maintains an Individual Development Plan (IDP) as part of their performance record (PERF-001 §9). The IDP is updated semi-annually and contains:

- 2-3 development priorities for the current review period, each mapped to a CMP-001 competency domain
- Specific training activities, certifications, or experiences planned to address each priority
- Timeline and estimated cost
- Status tracking (planned, in progress, completed)

### 8.2 Team Training Calendar

Each pillar leader maintains a team training calendar that:

- Tracks certification expirations and renewal deadlines
- Schedules internal knowledge-sharing sessions (brown-bag presentations, tool training, cross-pillar briefings)
- Coordinates conference attendance to avoid staffing gaps
- Identifies team-wide training needs (e.g., a new regulatory framework everyone needs to understand)

### 8.3 Training Record

The organization maintains a training record for each team member as part of their HR file. The record documents:

- Certifications held, with issue and expiration dates
- Formal training courses completed
- Conference attendance
- Internal training delivered (the person teaching counts as development activity)

The record supports regulatory compliance (NERC-CIP CIP-004 requires documented training for personnel with access to BES Cyber Systems; CMMC requires documented role-based training) and provides the evidence base for promotion cases that reference certification achievements.

---

## 9. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-TRN-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to certification requirements or competency model |
| **Next Scheduled Review** | 2027-05-27 |
| **Frameworks** | NIST NICE SP 800-181r1; NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.7.2; DoD 8140.03 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-27 | Cyber Governance | Initial release. Defines three-tier certification matrix (Required, Recommended, Aspirational) for canonical CERG roles across all grades plus management track addendum. Provides training curriculum organized by CMP-001 competency domain at Foundational/Intermediate/Advanced levels. Establishes 5% cross-training standard, per-person professional development budget guidelines ($3K-$10K+), conference attendance criteria, and training administration framework. |

### Review Triggers

- Material change to certification requirements by certifying bodies (ISC2, ISACA, SANS, CompTIA)
- Material change to the competency model (CMP-001)
- New roles added to the canonical roster (OM-001 §6.1)
- Regulatory changes affecting personnel training requirements (NERC-CIP CIP-004, CMMC, etc.)
- Feedback from performance reviews indicating training curriculum gaps
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Competency Model | [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Competency domains the curriculum targets |
| Job Architecture | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade definitions and progression |
| Job Descriptions | [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) | Certification references and KSA requirements |
| Performance Management | [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | Development plans and budget connection |
| Onboarding Program | [`CERG-GOV-ONB-001`](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) | Initial training during onboarding |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Left-right knowledge model |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.