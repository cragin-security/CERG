# SURGE: Cyber Engineering, Risk & Governance

## COMPETENCY MODEL AND BEHAVIORAL ANCHORS
### Leveled Knowledge · Skills · Behaviors Across All Three Pillars

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CMP-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) · [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) · [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) |
| **Review Cycle** | Annual / On any change to grade definitions, role roster, or material shift in cybersecurity competency frameworks |
| **Frameworks** | [NIST NICE Workforce Framework](https://www.nist.gov/itl/applied-cybersecurity/nice) (SP 800-181r1) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · [ISO/IEC 27001](https://www.iso.org/standard/27001) A.7.2 · [DCWF](https://public.cyber.mil/wid/dcwf/) (DoD 8140.03) |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How This Model Works](#2-how-this-model-works)
3. [Competency Domains](#3-competency-domains)
4. [Engineering Pillar: Competency Matrix and Behavioral Anchors](#4-engineering-pillar-competency-matrix-and-behavioral-anchors)
5. [Risk Pillar: Competency Matrix and Behavioral Anchors](#5-risk-pillar-competency-matrix-and-behavioral-anchors)
6. [Governance Pillar: Competency Matrix and Behavioral Anchors](#6-governance-pillar-competency-matrix-and-behavioral-anchors)
7. [Management Track Competency Addendum](#7-management-track-competency-addendum)
8. [Using This Model for Hiring, Development, and Promotion](#8-using-this-model-for-hiring-development-and-promotion)
9. [Mapping to NICE and Industry Frameworks](#9-mapping-to-nice-and-industry-frameworks)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

The Job Architecture and Grade Framework (CERG-GOV-JA-001) defines what each grade expects: scope, autonomy, influence, craft mastery, and organizational impact. It tells you *at what altitude* a Specialist, Sr. Specialist, Advisor, or Sr. Advisor operates. What it does not do is define what "craft mastery" actually means for a Cloud Security Engineer at S2 versus S3, or what "influence" looks like for a Threat Intelligence Analyst versus a Vendor Risk Analyst.

This document answers those questions. It defines eight competency domains, distributes them across the SME grades (S1 through S4) for each of the three role families (Engineering, Risk, Governance), and provides behavioral anchors: observable, concrete examples of what competent performance looks like at each level. A person in the role, their manager, and a promotion panel should be able to read the relevant cell and agree on whether the person is meeting, exceeding, or not yet demonstrating that competency at that grade.

It applies to every CERG SME-track role. Management-track competencies are addressed in Section 7 as an addendum, referencing the leadership dimensions already defined in JA-001 §5. The two Adjacent Incident Response roles are out of scope.

> **A Model, Not a Checklist**
>
> No one demonstrates every anchor at their grade simultaneously. The anchors describe the target. A Specialist who is strong in Technical Depth but still developing Cross-Pillar Fluency is on a normal trajectory. A promotion case should address each competency domain honestly, not check every box. The model exists to make the conversation specific, not to automate the decision.

---

## 2. How This Model Works

### 2.1 Structure

For each role family, a matrix maps eight competency domains (rows) against the four SME grades (columns). Each cell contains a behavioral anchor: a one-to-two-sentence description of what that competency looks like at that grade in that role family.

The anchors are cumulative. An Advisor (S3) is expected to demonstrate the S1 and S2 anchors plus the S3 anchor. They do not lose the earlier capabilities; they add new ones.

### 2.2 Role Families

The competencies are calibrated to three role families aligned to the CERG pillars:

| Role Family | Pillar | Roles |
|---|---|---|
| **Engineering** | Cyber Engineering | Cloud Security Engineer, Identity Engineer, OT Security Engineer, Application Security Engineer, Endpoint Engineer, Cryptography Engineer |
| **Risk** | Cyber Risk | Threat Intelligence Analyst, Vendor Risk Analyst, OT Risk Analyst, Identity Risk Analyst, Detection Engineer, Exposure Management Lead (SME track), Adversarial Testing Lead (SME track) |
| **Governance** | Cyber Governance | NERC-CIP Compliance Manager (SME track), CMMC/Federal Compliance Manager (SME track), SOX ITGC Lead (SME track), Policy & Standards Manager (SME track), Risk Register Owner (SME track), Evidence Librarian |

Management-track roles (Pillar Leaders, Managers, Senior Managers) use the SME competencies for their home family plus the management addendum in Section 7.

### 2.3 Reading a Cell

A cell that says "authors new detection rules from threat reports with minimal false positives; peer-reviews rules written by Specialists" is specific enough that a manager and a Detection Engineer can look at a quarter's work and say "yes, that is happening" or "no, the peer review part is not happening yet." It is not a job description. It is a lens for evaluating demonstrated capability.

---

## 3. Competency Domains

The eight domains below apply to every CERG role. Their relative weight varies by role family: Technical Depth is the primary domain for Engineering; Risk Judgment is primary for Risk; Compliance and Regulatory Literacy is primary for Governance. But every domain matters for every role, because the left-right knowledge model in CERG-GOV-FRM-001 §9.2 means a Cloud Security Engineer who cannot read a compliance finding and a SOX ITGC Lead who cannot read a vulnerability report are both half-effective.

| Domain | What It Measures | Primary Family |
|---|---|---|
| **Technical Depth** | Mastery of the tools, platforms, and techniques specific to the role's domain. The ability to execute, troubleshoot, and improve the technical work. | Engineering |
| **Cross-Pillar Fluency** | Understanding of how the other two pillars operate, what they produce, and how the person's work connects to theirs. The left-right knowledge model in practice. | All |
| **Risk Judgment** | The ability to assess severity, likelihood, and business impact of a finding, vulnerability, or design decision. Knowing what is a fire and what is smoke. | Risk |
| **Communication** | The ability to explain technical or regulatory findings to audiences that do not share the person's expertise: business owners, executives, auditors, vendors. Written and verbal. | All |
| **Operational Discipline** | Consistency in following procedures, documenting work, collecting evidence, and meeting operational SLAs. The part of cybersecurity that is a profession, not a calling. | All |
| **Influence and Mentorship** | The ability to improve the team's output through teaching, code review, procedure improvement, or setting standards, without formal authority. | All |
| **Compliance and Regulatory Literacy** | Understanding of the regulatory frameworks in the organization's scope and the ability to translate between regulatory language and technical reality. | Governance |
| **Continuous Learning** | Evidence of active skill maintenance and growth. Cybersecurity skills have a half-life; this domain measures whether the person is investing in keeping theirs current. | All |

> **The Domains Are Interdependent**
>
> An engineer with deep Technical Depth and zero Communication is a risk: their findings die in their terminal. An analyst with strong Risk Judgment and weak Operational Discipline is a liability: their assessments are brilliant but their evidence is missing when the auditor arrives. The model values the whole practitioner, not the specialist who is dangerous in every dimension except one.

---

## 4. Engineering Pillar: Competency Matrix and Behavioral Anchors

### 4.1 Technical Depth

| Grade | Anchor |
|---|---|
| **S1 Specialist** | Executes assigned engineering tasks (IaC module, configuration change, architecture review checklist item) from established procedures. Recognizes when a task result does not match expected output and escalates with context. Learning the organization's technology stack: can name the major platforms, their purpose, and their security control points. |
| **S2 Sr. Specialist** | Owns a technology domain (e.g., AWS security, Azure AD, Kubernetes admission control). Designs and implements security controls independently within that domain. Performs architecture reviews in their domain and produces findings that require minimal rework from the reviewer. Authors and improves procedures for their domain. Debugs non-trivial failures without assistance. |
| **S3 Advisor** | Shapes the organization's technical security strategy in their domain. Designs reference architectures adopted by other engineers. Anticipates how changes in the technology stack (new service, new acquisition, new cloud region) will affect security posture before they land. Performs architecture reviews across domains with credibility. Authors standards that govern how their domain is secured. |
| **S4 Sr. Advisor** | Sets the technical bar for the entire Engineering pillar. Called upon for the hardest cross-domain problems (e.g., "how do we safely federate with this acquisition's identity provider across three clouds and an on-prem OT environment?"). Represents the organization's engineering position to vendors, industry working groups, and regulators. Writes the standards others follow. Can step into any Engineering domain and contribute meaningfully within days. |

### 4.2 Cross-Pillar Fluency

| Grade | Anchor |
|---|---|
| **S1** | Understands that Risk and Governance pillars exist and can describe their basic functions. Reads vulnerability reports and compliance findings that affect their work. |
| **S2** | Consumes Risk pillar output (vulnerability data, threat intelligence) and incorporates it into engineering decisions. Understands what Governance needs from Engineering for an audit and provides it without being chased. Recognizes when a design decision has regulatory implications (e.g., "this crosses CIP boundaries") and raises it. |
| **S3** | Anticipates what Risk and Governance will need from an engineering decision before they ask. Participates in cross-pillar working groups as the Engineering voice. Can represent Engineering's position to a regulator or auditor without a Governance handler. Identifies when a Risk finding or Governance requirement is based on a misunderstanding of the technology and corrects it constructively. |
| **S4** | Operates fluently across all three pillars. Contributes to Risk assessments and Governance standards as a peer, not a guest. Is the person a pillar leader calls when a cross-pillar problem does not fit any procedure. |

### 4.3 Risk Judgment

| Grade | Anchor |
|---|---|
| **S1** | Follows the risk taxonomy when documenting findings. Can distinguish between a configuration drift alert that needs a ticket and one that needs an incident response page. |
| **S2** | Independently assesses the severity and likelihood of findings in their domain. Assigns risk ratings that are consistent with the taxonomy and rarely adjusted by a senior reviewer. Recognizes when a finding they are working on is part of a larger risk pattern and escalates with the pattern, not just the ticket. |
| **S3** | Evaluates risk across domains and articulates the business impact in terms an executive can act on. Identifies compensating controls that reduce risk below what a pure vulnerability score would suggest. Contributes risk assessments to the risk register that the Risk Pillar Leader treats as authoritative. |
| **S4** | Shapes the organization's risk appetite through technical judgment. Called upon by the CISO for independent risk assessments on material decisions. Their risk evaluation carries the same weight as a pillar leader's. |

### 4.4 Communication

| Grade | Anchor |
|---|---|
| **S1** | Writes clear ticket updates and status reports. Explains a technical finding to their immediate team without ambiguity. |
| **S2** | Writes architecture review findings that a project manager or business owner can understand and act on. Presents technical topics to their pillar. Authors clear, usable procedures. Communicates technical trade-offs to non-engineering audiences. |
| **S3** | Represents Engineering in cross-functional forums with credibility. Writes decision memos that frame technical options in business terms. Presents to senior leadership and external stakeholders. Mentors junior engineers on how to structure written analysis. |
| **S4** | Communicates complex technical risk to the CISO, the board (as requested), regulators, and industry peers. Writes the organization's public technical positions. Represents the organization at conferences and in industry working groups. |

### 4.5 Operational Discipline

| Grade | Anchor |
|---|---|
| **S1** | Follows procedures correctly. Updates tickets and documentation when work is complete. Meets assigned SLAs. Admits when they do not know something rather than guessing. |
| **S2** | Owns operational SLAs for their domain work streams. Ensures evidence is collected and stored per the evidence procedure. Improves procedures when they find gaps. Their work is consistently auditable without retroactive cleanup. |
| **S3** | Designs procedures that are operationally sustainable, not just technically correct. Ensures the evidence trail for their domain is audit-ready at all times. Identifies and eliminates toil: automates repetitive operational tasks. |
| **S4** | Sets operational standards for the pillar. Defines what "good" looks like for procedure compliance, evidence quality, and SLA management. Holds the pillar accountable to its own operational commitments. |

### 4.6 Influence and Mentorship

| Grade | Anchor |
|---|---|
| **S1** | Actively learns from senior engineers. Asks good questions. Shares what they learn with peers. |
| **S2** | Onboards new Specialists without assistance. Peer-reviews code and configurations with constructive feedback. Their technical opinion is sought by other engineers in their domain. |
| **S3** | Mentors Specialists and Sr. Specialists across domains. Leads technical initiatives without formal authority. Their architectural recommendations are rarely overruled. Contributes to hiring decisions through candidate evaluations. |
| **S4** | Shapes the development of the entire Engineering team. Sets the technical bar through their own work and their mentoring. Influences hiring profiles, team composition, and organizational design. Represents the engineering culture to leadership. |

### 4.7 Compliance and Regulatory Literacy

| Grade | Anchor |
|---|---|
| **S1** | Knows which regulatory frameworks apply to their organization. Can describe the security implications of the major ones (NERC-CIP, CMMC, SOX) at a high level. |
| **S2** | Understands the specific regulatory requirements that affect their domain (e.g., CIP-007 for OT engineers, CMMC access control requirements for Identity engineers). Can explain to an auditor how a control they implemented satisfies a regulatory requirement. |
| **S3** | Anticipates regulatory implications of engineering decisions. Advises project teams on compliance requirements before design is complete. Represents Engineering in regulatory audits without a Governance chaperone. |
| **S4** | Contributes to the organization's regulatory strategy. Engages with regulators on technical matters. Shapes standards so that compliance is a byproduct of good engineering, not a separate activity. |

### 4.8 Continuous Learning

| Grade | Anchor |
|---|---|
| **S1** | Completes assigned training. Pursues foundational certifications relevant to their domain (e.g., AWS Security Specialty, AZ-500). Learns the organization's technology stack. |
| **S2** | Maintains current certifications. Stays current on developments in their domain (new cloud services, new attack techniques, new regulatory requirements). Shares what they learn with the team. |
| **S3** | Pursues advanced certifications (e.g., CISSP, SANS GIAC, cloud architecture certifications). Contributes to the team's knowledge base through documented research, brown-bag sessions, or internal training. Evaluates new technologies for organizational adoption. |
| **S4** | Recognized externally for expertise (conference presentations, industry working groups, published research). Shapes the organization's technology and certification roadmap. The person other engineers go to when they need to understand an emerging technology or threat. |

---

## 5. Risk Pillar: Competency Matrix and Behavioral Anchors

### 5.1 Technical Depth

| Grade | Anchor |
|---|---|
| **S1 Specialist** | Operates the Risk pillar's tools (vulnerability scanner, CSPM platform, threat intel platform, detection pipeline) under supervision. Triages alerts following established procedures. Recognizes false positives and true positives with increasing accuracy. |
| **S2 Sr. Specialist** | Owns a Risk domain (e.g., vulnerability management for a platform class, vendor assessments for a business unit, a set of detection rules). Tunes tools to reduce noise and improve signal. Independently investigates findings and determines root cause. Authors detection rules, threat advisories, or vendor risk reports that require minimal revision. |
| **S3 Advisor** | Shapes the Risk pillar's approach to exposure management. Designs assessment methodologies. Correlates findings across tools to identify systemic weaknesses that individual alerts miss. Authors threat intelligence products that shape organizational decisions. Evaluates and recommends new Risk tooling. |
| **S4 Sr. Advisor** | Sets the analytical bar for the entire Risk pillar. Called upon for the hardest exposure questions (e.g., "what is our actual risk from this newly disclosed supply chain compromise given our architecture and controls?"). Represents the organization's risk posture to regulators, auditors, and industry peers. |

### 5.2 Cross-Pillar Fluency

| Grade | Anchor |
|---|---|
| **S1** | Understands that Engineering builds systems and Governance owns compliance. Reads architecture review outputs and compliance standards that affect their risk assessments. |
| **S2** | Delivers risk findings in a format Engineering can act on (specific, actionable, prioritized by business impact). Understands what evidence Governance needs from Risk assessments and provides it proactively. Participates in cross-pillar threat modeling sessions. |
| **S3** | Collaborates with Engineering to design controls that address risk findings, not just report them. Feeds risk intelligence into Governance's compliance calendar. Anticipates which risk findings will become audit findings and ensures the trail is complete before the auditor arrives. |
| **S4** | Operates fluently across all three pillars. Contributes to Engineering architecture decisions and Governance standards as a peer. The person a pillar leader calls when a risk question spans all three pillars. |

### 5.3 Risk Judgment

| Grade | Anchor |
|---|---|
| **S1** | Applies the risk taxonomy correctly when triaging findings. Distinguishes between Critical, High, Medium, and Low severity using the defined criteria. Escalates findings that exceed SLA without delay. |
| **S2** | Independently assesses the business impact of findings in their domain. Adjusts risk ratings based on context (compensating controls, exposure path, threat actor capability) and documents the rationale. Produces risk assessments that the Risk Pillar Leader accepts without material revision. |
| **S3** | Assesses systemic risk: identifies patterns across individual findings that indicate a deeper weakness. Evaluates risk from new technologies, vendors, or business initiatives before they are operational. Contributes risk assessments to significant business decisions (vendor selection, architecture change, M&A). |
| **S4** | Shapes the organization's risk appetite. Called upon by the CISO for independent risk evaluation on material decisions. Their risk judgment on novel or ambiguous situations is treated as authoritative. Engages with industry peers on emerging risk methodologies. |

### 5.4 Communication

| Grade | Anchor |
|---|---|
| **S1** | Writes clear finding descriptions with reproducible steps, impact statements, and remediation guidance. Updates stakeholders on finding status without being prompted. |
| **S2** | Delivers risk briefings to business owners and project teams. Translates vulnerability data into business risk without losing technical accuracy. Writes vendor risk assessment reports that procurement and legal can act on. |
| **S3** | Presents risk posture to executive audiences. Communicates threat landscape changes and their organizational implications. Writes threat intelligence products consumed by leadership. Represents Risk in regulatory and customer inquiries. |
| **S4** | Communicates organizational risk posture to the board, regulators, and external stakeholders. Represents the organization's risk position in industry forums. Mentors Risk team members on how to structure risk communication for different audiences. |

### 5.5 Operational Discipline

| Grade | Anchor |
|---|---|
| **S1** | Triages findings within SLA. Documents assessment results in the designated system. Follows the vulnerability management and risk register procedures. |
| **S2** | Owns operational SLAs for their domain. Ensures risk register entries are current and complete. Maintains scanning schedules, detection rule lifecycles, or vendor assessment cadences without gaps. Their assessment records are audit-ready. |
| **S3** | Designs risk assessment workflows that produce consistent, auditable output. Ensures the Risk pillar's operational cadence is documented, measured, and improving. Identifies and automates repetitive risk assessment tasks. |
| **S4** | Sets operational standards for the Risk pillar. Defines what "defensible" risk assessment looks like under regulatory scrutiny. Ensures the pillar's SLAs, coverage targets, and quality standards are defined, measured, and reported. |

### 5.6 Influence and Mentorship

| Grade | Anchor |
|---|---|
| **S1** | Learns from senior analysts. Asks good questions about methodology and judgment. Shares interesting findings with the team. |
| **S2** | Trains new analysts on Risk tools and procedures. Peer-reviews risk assessments and detection rules. Their analytical judgment is sought by other team members. |
| **S3** | Mentors analysts across Risk domains. Leads cross-functional risk initiatives. Their risk assessments shape how Engineering and business owners prioritize remediation. Contributes to hiring through candidate evaluations and interview panel participation. |
| **S4** | Develops the analytical capability of the entire Risk team. Sets the quality bar for risk assessment, threat intelligence, and detection engineering. Influences organizational risk culture. Represents the Risk function's philosophy to leadership and to the broader security community. |

### 5.7 Compliance and Regulatory Literacy

| Grade | Anchor |
|---|---|
| **S1** | Knows which regulatory frameworks apply and can describe how Risk assessments support compliance (e.g., vulnerability scan results as evidence for CIP-007, vendor assessments for CMMC). |
| **S2** | Understands the specific regulatory requirements that govern their Risk domain. Produces risk assessments that meet the evidence standards of the relevant frameworks. Can explain to an auditor how a risk assessment supports a compliance finding. |
| **S3** | Anticipates how regulatory changes will affect the Risk program's scope and cadence. Advises Governance on the risk implications of compliance findings. Represents Risk in regulatory audits. |
| **S4** | Contributes to the organization's regulatory strategy from a risk perspective. Engages with regulators on risk methodology. Ensures the Risk program's output meets the highest standard of regulatory defensibility. |

### 5.8 Continuous Learning

| Grade | Anchor |
|---|---|
| **S1** | Completes assigned training. Pursues foundational certifications (e.g., Security+, CEH, vendor-specific certs for tools in use). Learns the organization's threat landscape. |
| **S2** | Maintains current certifications. Tracks the threat actors, TTPs, and vulnerabilities relevant to the organization's industry. Shares threat intelligence and lessons learned with the team. |
| **S3** | Pursues advanced certifications (e.g., CISSP, GCIH, GCFA, OSCP). Contributes threat research or methodology improvements adopted by the team. Represents the organization in threat-sharing communities (ISACs, sector-specific groups). |
| **S4** | Recognized externally for risk or threat expertise. Contributes to industry threat intelligence, risk methodology, or detection frameworks. Shapes the organization's approach to emerging threats and risk assessment techniques. |

---

## 6. Governance Pillar: Competency Matrix and Behavioral Anchors

### 6.1 Technical Depth

| Grade | Anchor |
|---|---|
| **S1 Specialist** | Operates the Governance pillar's tools (document management system, evidence library, GRC platform). Executes evidence collection, control testing, or policy review tasks from established procedures. Reads and correctly interprets CERG standards and regulatory requirements in their assigned domain. |
| **S2 Sr. Specialist** | Owns a compliance domain (e.g., NERC-CIP evidence for a subset of standards, CMMC control family, SOX ITGC control set). Independently collects, organizes, and presents evidence for audits and assessments. Maps regulatory requirements to CERG controls and identifies gaps. Authors compliance documentation that requires minimal revision from the Governance Pillar Leader. |
| **S3 Advisor** | Shapes the organization's compliance strategy for their domain. Designs evidence collection workflows that survive auditor scrutiny. Interprets ambiguous regulatory guidance and produces defensible organizational positions. Authors standards and policy sections. Evaluates and recommends GRC tooling. |
| **S4 Sr. Advisor** | Sets the compliance and governance bar for the entire Governance pillar. Called upon for the hardest regulatory interpretation questions (e.g., "does this new operational model require a CIP boundary recertification?"). Represents the organization to regulators, assessors, and auditors as the authoritative technical voice. |

### 6.2 Cross-Pillar Fluency

| Grade | Anchor |
|---|---|
| **S1** | Understands the basic functions of Engineering and Risk pillars. Reads engineering architecture outputs and risk assessments that affect their compliance work. |
| **S2** | Engages Engineering and Risk as partners in compliance, not subjects of it. Understands the technical reality behind the controls they are assessing. Requests evidence in terms the providing pillar understands. Recognizes when a control requirement is technically impractical and works with Engineering to design a compensating control. |
| **S3** | Translates between regulatory language and technical reality in both directions. Anticipates which engineering or risk decisions will have compliance implications before they are made. Participates in cross-pillar working groups as the Governance voice. Ensures standards are technically validated by Engineering and risk-prioritized by Risk before publication. |
| **S4** | Operates fluently across all three pillars. Engages with Engineering on architecture and Risk on exposure posture as a peer. Ensures the Governance program enables the other pillars rather than constraining them. |

### 6.3 Risk Judgment

| Grade | Anchor |
|---|---|
| **S1** | Applies the risk taxonomy when documenting compliance findings. Understands the relationship between control failures and organizational risk. |
| **S2** | Assesses the risk implication of control gaps in their domain. Prioritizes compliance findings by actual risk to the organization, not by framework numbering. Contributes compliance-related risk items to the risk register with accurate severity ratings. |
| **S3** | Evaluates the risk impact of regulatory changes. Advises leadership on the risk trade-offs of compliance decisions (e.g., "we can meet the letter of this requirement with a compensating control, but here is the residual risk"). Correlates compliance findings with vulnerability and threat data to produce integrated risk pictures. |
| **S4** | Shapes organizational risk decisions through the compliance lens. Advises the CISO on the risk implications of regulatory strategy. Their judgment on compliance risk is treated as equivalent to the Risk Pillar Leader's on technical risk. |

### 6.4 Communication

| Grade | Anchor |
|---|---|
| **S1** | Writes clear evidence descriptions, control test results, and compliance status updates. Communicates evidence requests to Engineering and Risk without ambiguity. |
| **S2** | Presents compliance status and findings to pillar leadership. Translates regulatory requirements into language project teams can act on. Writes policy and standard sections that are clear and enforceable. Communicates with auditors and assessors under supervision. |
| **S3** | Represents the organization to auditors, assessors, and regulators as a primary point of contact. Writes regulatory responses and compliance positions adopted by leadership. Communicates compliance risk to executive audiences. Mentors junior Governance staff on regulatory communication. |
| **S4** | Communicates the organization's compliance posture to the board, regulators, and external stakeholders. Shapes the organization's regulatory narrative. Represents the organization in industry regulatory working groups. |

### 6.5 Operational Discipline

| Grade | Anchor |
|---|---|
| **S1** | Follows evidence management procedures. Documents compliance activities in the designated systems. Meets regulatory filing deadlines. Maintains organized, retrievable evidence packages. |
| **S2** | Owns the compliance calendar for their domain. Ensures evidence is collected, reviewed, and stored on schedule. Maintains audit-ready evidence packages at all times, not just during audit season. Improves evidence collection workflows. |
| **S3** | Designs compliance operations that are sustainable year-round, not just during audit cycles. Ensures the Governance pillar's operational cadence is documented, measured, and improving. Designs evidence architectures that support multiple frameworks without duplication. |
| **S4** | Sets operational standards for the Governance pillar. Defines what "audit-ready" means in measurable terms. Ensures the compliance program can survive the departure of any single person. |

### 6.6 Influence and Mentorship

| Grade | Anchor |
|---|---|
| **S1** | Learns from senior Governance staff. Asks good questions about regulatory interpretation and evidence standards. Supports peers during audit preparation. |
| **S2** | Trains new Governance staff on compliance domains and evidence procedures. Peer-reviews compliance documentation. Their regulatory knowledge is sought by Engineering and Risk staff who need to understand compliance requirements. |
| **S3** | Mentors Governance staff across compliance domains. Influences how the organization approaches regulatory compliance, moving from reactive (respond to auditor findings) to proactive (operate in a way that makes audit findings rare). Contributes to hiring decisions. |
| **S4** | Develops the compliance capability of the entire Governance team and the broader organization. Sets the quality bar for regulatory interpretation, evidence standards, and auditor engagement. Influences the organization's compliance culture. Represents the Governance function's philosophy to leadership. |

### 6.7 Compliance and Regulatory Literacy

| Grade | Anchor |
|---|---|
| **S1** | Knows the regulatory frameworks in the organization's scope. Can describe the structure and key requirements of each. Correctly applies framework terminology. |
| **S2** | Deep knowledge of the regulatory frameworks in their domain. Independently interprets regulatory requirements and maps them to organizational controls. Stays current on regulatory changes and updates. Can explain to an auditor how the organization's controls satisfy specific regulatory requirements. |
| **S3** | Authority on their regulatory domain. Interprets ambiguous regulatory guidance and produces defensible positions. Anticipates regulatory changes and prepares the organization before they take effect. Advises leadership on regulatory strategy. Represents the organization in regulatory proceedings. |
| **S4** | Shapes the organization's regulatory strategy. Engages directly with regulators and industry bodies on regulatory development. Their regulatory interpretations are treated as authoritative by the organization and respected by external stakeholders. |

### 6.8 Continuous Learning

| Grade | Anchor |
|---|---|
| **S1** | Completes assigned training. Pursues foundational certifications (e.g., Security+, CISA fundamentals, framework-specific training). Learns the organization's regulatory landscape. |
| **S2** | Maintains current certifications. Tracks regulatory developments and framework updates relevant to their domain. Pursues intermediate certifications (e.g., CISA, CRISC, CMMC RP/RPA). Shares regulatory knowledge with the team. |
| **S3** | Pursues advanced certifications (e.g., CISSP, CISM, CGEIT, lead auditor certifications). Contributes to the Governance body of knowledge through documented regulatory analysis. Represents the organization in regulatory working groups. |
| **S4** | Recognized externally for regulatory or compliance expertise. Contributes to regulatory development, industry standards, or professional certification bodies. Shapes the organization's approach to emerging regulatory frameworks. |

---

## 7. Management Track Competency Addendum

CERG managers are expected to demonstrate the SME competencies of their home role family at the S2 level or above, plus the five management-specific domains below. A Governance Pillar Leader who rose through the Risk pillar demonstrates Risk-family SME competencies at S3 or S4 plus the management addendum.

The management competencies are progressive. A Manager demonstrates the M1 anchors; a Director demonstrates the M1 through M4 anchors cumulatively.

The grade definitions in JA-001 §5 establish the performance expectations (span of control, scope, people leadership). This addendum defines the observable behaviors that demonstrate those expectations are being met.

### 7.1 People Leadership

| Grade | Anchor |
|---|---|
| **M1 Manager** | Conducts regular, meaningful 1:1s. Sets clear expectations for each direct report. Delivers honest performance feedback promptly, not just at annual review. Addresses performance issues early, before they become team problems. Hires with a clear understanding of what the role needs. |
| **M2 Senior Manager** | Develops the Managers reporting to them. Ensures consistent people-management practices across their function. Identifies and develops high-potential team members. Manages team composition actively: hires for gaps, addresses skill imbalances, manages departures without disruption. |
| **M3 Principal Manager** | Builds a leadership bench: ensures every critical role has an identified successor or development plan for one. Shapes the people strategy for their scope: hiring profile, retention approach, career pathways. Creates a management culture that reflects CERG values. |
| **M4 Director** | Accountable for the entire pillar's talent health. Develops the next generation of CERG leaders. Owns the pillar's organizational design. Builds a culture of cross-pillar collaboration and continuous development. |

### 7.2 Strategic Thinking

| Grade | Anchor |
|---|---|
| **M1** | Translates pillar goals into actionable team tasks. Prioritizes team work against organizational objectives. Identifies when team priorities need to shift and communicates the rationale. |
| **M2** | Defines a function strategy and roadmap aligned to pillar and organizational objectives. Anticipates how changes in the threat landscape, technology, or regulatory environment will affect the function's priorities. Contributes to pillar strategy discussions. |
| **M3** | Shapes pillar strategy. Identifies emerging organizational needs and positions the pillar to meet them before the need becomes a crisis. Contributes to organizational strategy beyond the pillar. |
| **M4** | Sets the multi-year strategic direction for the pillar. Aligns pillar strategy with organizational strategy, the threat landscape, and the regulatory environment. Represents the pillar's strategic position to the CISO, the board, and external stakeholders. |

### 7.3 Resource and Budget Management

| Grade | Anchor |
|---|---|
| **M1** | Manages team resources effectively. Identifies when the team is over- or under-resourced and communicates the gap to their manager. Advocates for tooling and training investments with clear business justification. |
| **M2** | Owns the function's budget input. Defends headcount requests with workload data, not anecdotes. Manages vendor relationships and tooling procurement for the function. Makes resource allocation trade-offs across teams transparently. |
| **M3** | Owns significant budget lines. Builds multi-year resource plans. Evaluates build-vs-buy decisions with total-cost-of-ownership analysis. Identifies efficiency opportunities that free resources for higher-value work. |
| **M4** | Owns the pillar's budget. Allocates resources across functions in alignment with organizational priorities. Makes investment cases to the CISO and executive leadership. Ensures the pillar's resource allocation reflects its risk priorities. |

### 7.4 Stakeholder Management

| Grade | Anchor |
|---|---|
| **M1** | Represents the team effectively to peer teams, pillar leadership, and business stakeholders. Manages stakeholder expectations: communicates timelines, risks, and trade-offs honestly. Escalates issues that require leadership attention with clear context and recommended actions. |
| **M2** | Manages complex stakeholder relationships across functions and business units. Navigates competing priorities among stakeholders without compromising the function's core mission. Represents the function to executive stakeholders. |
| **M3** | Manages executive stakeholder relationships. Aligns stakeholders with competing interests toward a shared objective. Represents CERG to external stakeholders (regulators, auditors, industry peers) with credibility. |
| **M4** | Manages the organization's most critical stakeholder relationships: the CISO, executive leadership, the board, regulators, and industry peers. Shapes stakeholder expectations rather than just meeting them. Builds organizational consensus for the pillar's strategic direction. |

### 7.5 Organizational Development

| Grade | Anchor |
|---|---|
| **M1** | Contributes to team culture and morale. Recognizes team members' contributions publicly. Addresses behaviors that undermine team cohesion. |
| **M2** | Builds a positive, high-performance culture within the function. Establishes norms for collaboration, knowledge sharing, and professional development. Identifies and removes systemic barriers to team effectiveness. |
| **M3** | Shapes organizational culture across the pillar. Designs organizational structures that enable the strategy. Leads organizational change initiatives. Builds cross-pillar collaboration norms. |
| **M4** | Shapes organizational culture across CERG. Designs the pillar's organizational model to meet current and future needs. Champions diversity of thought, cross-pillar collaboration, and continuous improvement as organizational values. |

---

## 8. Using This Model for Hiring, Development, and Promotion

### 8.1 Hiring

For each open requisition, select the target grade and role family. Use the competency matrix to define the interview assessment plan:

1. **Technical Depth** is assessed through a technical interview or practical exercise calibrated to the target grade.
2. **Cross-Pillar Fluency** and **Communication** are assessed through a panel interview with members from a different pillar.
3. **Risk Judgment** is assessed through a case study or scenario discussion.
4. **Operational Discipline** and **Continuous Learning** are assessed through behavioral questions and resume review.

The model ensures every candidate is evaluated against the same dimensions, reducing the "I liked them but I cannot explain why" hiring pattern.

### 8.2 Development

For each team member, the manager and the team member review the competency matrix for their role family at their current grade and the next grade. Together they identify:

- **Strengths** (competencies where the person consistently demonstrates at-grade or above-grade behavior)
- **Growth areas** (competencies where the person is not yet demonstrating at-grade behavior, or needs development to reach the next grade)
- **Development actions**: specific experiences, training, mentoring, or stretch assignments that will close the gaps

This review should happen at least semi-annually, aligned to the performance management cadence in CERG-GOV-PERF-001.

### 8.3 Promotion

A promotion case addresses every competency domain. The standard is not "checks every box." It is:

1. The candidate consistently demonstrates at-grade behavior in their current role.
2. The candidate demonstrates next-grade behavior in the majority of competency domains.
3. The candidate has a credible development plan for domains where they are not yet at the next grade.
4. The manager, a peer manager from a different pillar, and the pillar leader concur.

> **Calibration Prevents Drift**
>
> Two managers evaluating the same engineer against the same matrix should reach similar conclusions. If they do not, the model is not specific enough or the managers are not applying it consistently. The promotion calibration process defined in CERG-GOV-PERF-001 exists to catch and correct this drift. A promotion that one manager supports and another would block is not a close call to be resolved by advocacy; it is a signal that the competency evidence needs to be examined together.

---

## 9. Mapping to NICE and Industry Frameworks

### 9.1 NIST NICE Workforce Framework (SP 800-181r1)
### 9.1 NIST NICE Workforce Framework (SP 800-181r1)

The NICE Framework defines cybersecurity work through Task, Knowledge, and Skill (TKS) statements organized into Work Roles and Competency Areas. This section maps CERG's eight competency domains to NICE Competency Areas and provides sample TKS references for skills-gap analysis.

#### 9.1.1 CERG Competency Domains → NICE Competency Areas

| CERG Competency Domain | NICE Competency Area(s) | Description |
|------------------------|------------------------|-------------|
| Technical Depth | Technology Management; Systems Integration | Deep expertise in security technologies, architectures, and platforms |
| Cross-Pillar Fluency | Interpersonal Skills; Systems Integration | Ability to work across Engineering, Risk, and Governance boundaries |
| Risk Judgment | Risk Management; Threat Analysis | Sound judgment about security risk, severity, and treatment |
| Communication | Interpersonal Skills; Communication | Clear, audience-appropriate communication of security concepts |
| Operational Discipline | Process Management; Data Management | Reliable execution of security processes and evidence production |
| Influence and Mentorship | Leadership; Training and Education | Developing others; shaping security culture and practice |
| Compliance & Regulatory Literacy | Legal and Regulatory; Policy and Governance | Understanding and applying regulatory requirements |
| Continuous Learning | Continuous Learning; Training and Education | Staying current; developing new capabilities |

#### 9.1.2 Sample TKS References by Competency Domain

| CERG Domain | NICE Task ID (Example) | NICE Knowledge ID (Example) | NICE Skill ID (Example) |
|-------------|----------------------|----------------------------|------------------------|
| Technical Depth | T0452: Develop security architectures | K0004: Knowledge of cybersecurity principles | S0005: Skill in applying security architecture methods |
| Risk Judgment | T0043: Conduct risk assessments | K0002: Knowledge of risk management processes | S0034: Skill in conducting vulnerability assessments |
| Compliance & Regulatory Literacy | T0034: Conduct security audits | K0060: Knowledge of applicable laws and regulations | S0025: Skill in evaluating security controls |
| Operational Discipline | T0012: Maintain security documentation | K0023: Knowledge of configuration management | S0013: Skill in maintaining operational security |
| Communication | T0295: Brief senior leadership on security posture | K0059: Knowledge of business continuity | S0012: Skill in preparing and presenting briefings |

#### 9.1.3 CERG Role Family → NICE Work Role Mapping

The complete mapping of all 27 canonical CERG roles to NICE Work Roles is maintained in [JF-002](../roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md). The summary below maps role families to their primary NICE categories:

| CERG Job Family | Primary NICE Category | Representative NICE Work Roles |
|-----------------|----------------------|-------------------------------|
| **JF-SECENG** (Security Engineering) | SP — Securely Provision | Security Architect (SP-ARC-001), Systems Security Analyst (OM-ANA-001) |
| **JF-RISKOPS** (Risk Operations) | PR — Protect and Defend; AN — Analyze | Vulnerability Assessment Analyst (PR-VAM-001), Threat/Warning Analyst (AN-TWA-001) |
| **JF-GOVCOMP** (Governance & Compliance) | OV — Oversee and Govern | Security Control Assessor (OV-SCA-001), Cyber Policy and Strategy Planner (OV-PSP-001) |
| **JF-EXEC** (Executive) | OV — Oversee and Govern | Executive Cyber Leader (OG-WRL-001) |
| **JF-ADJUNCT** (Incident Response) | PR — Protect and Defend | Cyber Defense Incident Responder (PR-CIR-001) |

#### 9.1.4 How to Use the NICE TKS Database

The full NICE TKS database is available as a downloadable CSV from the NICE Framework Resource Center at https://www.nist.gov/nice/framework/. For each CERG role, filter by the NICE Work Role(s) mapped to that role (see [JF-002](../roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md)) and extract the TKS statements. The most relevant 5-10 Task statements, 5-10 Knowledge statements, and 5-10 Skill statements should be included in each per-role description's §6 (NICE TKS Statement References).

Organizations that need to demonstrate workforce alignment to NICE (e.g., federal agencies, defense contractors under DoD 8140.03) can map each CMP-001 behavioral anchor back to the relevant NICE KSAs using the cross-reference in NIST SP 800-181r1 Appendix C.
### 9.2 Other Frameworks

The competency domains in this model are compatible with:

- **DoD Cyber Workforce Framework (DCWF / DoD 8140.03)**: Work roles and proficiency levels map to CERG grades. Specialist (S1) aligns to DCWF Basic/Intermediate; Sr. Specialist (S2) to Intermediate/Advanced; Advisor (S3) to Advanced; Sr. Advisor (S4) to Advanced/Expert.
- **SANS GIAC Role-Based Certifications**: GIAC certifications provide objective validation of Technical Depth for specific domains and can be referenced in development plans.
- **ISC2 CISSP / CCSP / CSSLP**: These certifications validate breadth across multiple competency domains and are appropriate development targets for Advisor-level practitioners.
- **ISACA CISA / CRISC / CISM / CGEIT**: These certifications validate Governance-family competencies and are appropriate for Governance practitioners and managers.

The Training, Development, and Certification Framework (CERG-GOV-TRN-001) provides the full role-to-certification mapping and training curriculum.

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CMP-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to grade definitions, canonical role roster, or material shift in cybersecurity competency frameworks |
| **Next Scheduled Review** | 2027-05-27 |
| **Frameworks** | NIST NICE SP 800-181r1; NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.7.2; DoD 8140.03 (DCWF) |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-27 | Cyber Governance | Initial release. Defines eight competency domains with leveled behavioral anchors for Engineering, Risk, and Governance role families across SME grades S1-S4. Provides management track competency addendum for M1-M4. Includes hiring, development, and promotion guidance. Maps competency domains to NIST NICE SP 800-181r1 and other industry frameworks. |

### Review Triggers

- Change to the grade definitions in CERG-GOV-JA-001
- Change to the canonical role roster in CERG-GOV-OM-001 §6.1
- Material shift in cybersecurity competency frameworks (NICE, DCWF, industry certification bodies)
- Feedback from promotion panels indicating anchors are unclear or inconsistent
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Job Architecture and Grade Framework | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade definitions and progression dimensions |
| CERG Job Descriptions | [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) | KSA requirements per role |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster |
| Performance Management Framework | [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | Promotion calibration and development planning process |
| Training and Certification Framework | [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) | Role-to-certification mapping |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Left-right knowledge model |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.