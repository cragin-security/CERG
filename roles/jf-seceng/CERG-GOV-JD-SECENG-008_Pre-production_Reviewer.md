| | |
|---|---|
| **Document ID** | CERG-GOV-JD-SECENG-008 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](../../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

---

# Pre-production Reviewer

**Job Family:** JF-SECENG — Security Engineering
**Job Level Range:** L1-L4 (CERG Grade S1-S4)
**CERG Canonical Role:** Pre-production Reviewer (OM-001 §6.1)

---

## 1. Role Summary

The Pre-production Reviewer is a rotated Engineering role, not a permanent position. They own the pre-production checklist and sign off on go-live readiness: confirming that pre-production findings are remediated or risk-accepted, that handoff documentation is complete, and that the team inheriting the system knows its security posture. The role rotates among qualified Engineers to ensure cross-training and to prevent any single person from becoming a go-live bottleneck.

## 2. NICE Workforce Framework Mapping

| Mapping Level | NICE Work Role | NICE Work Role ID | NICE Work Role Category |
|---------------|----------------|-------------------|-------------------------|
| Primary | Security Control Assessor | OV-SCA-001 | OV |

**NICE Work Role Definition:** See [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) for the official NICE Work Role definition and complete CERG-to-NICE mapping. The NICE TKS database is available at https://www.nist.gov/nice/framework/.

## 3. Job Family & Level Placement

| Family | JF-SECENG — Security Engineering |
|--------|---------------------------|
| Level Range | L1 through L4 |
| CERG Grade Range | S1-S4 |
| Terminal Grade | S4 — see [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) for details |
| Track | SME |

## 4. Key Responsibilities

### 4.1 Core Responsibilities (All Grades)

- Own and maintain the pre-production review checklist, keeping it current with evolving standards and threat landscape - Conduct pre-production reviews for systems approaching go-live: verify that architecture review findings are closed, vulnerability scans are clean or accepted, threat model findings are resolved, and handoff documentation is complete - Sign off on go-live readiness, confirming that the system meets the security bar defined in the Architecture Review Procedure - Escalate unresolved pre-production findings to the Engineering Pillar Leader and the project's Executive Sponsor - Ensure the post-go-live operations team receives a complete security handoff package: known risks, accepted findings, monitoring requirements, incident response contacts, and configuration documentation - Coordinate with Risk to confirm that pre-production vulnerability scans and adversarial testing results meet the defined bar - Coordinate with Governance to confirm that compliance-required evidence is collected before go-live

### 4.2 Grade-Level Responsibility Differentiation

Grade-level responsibility differentiation for this role is defined in [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) (Role-to-Grade Mapping). The grade definitions (S1-S4 SME Track, M1-M4 Management Track) and leveling dimensions are in JA-001 §4-5. Behavioral anchors at each grade are in [CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md).

## 5. Required Knowledge, Skills, and Abilities (KSAs)

### 5.1 Domain Expertise

- Broad cybersecurity engineering knowledge across multiple domains (cloud, identity, application, endpoint) - Deep familiarity with the CERG Architecture Review Procedure and pre-production review process - Ability to evaluate security findings in context: what is truly blocking versus what can be accepted and tracked - Strong written communication: the pre-production review sign-off is a durable record that may be reviewed by auditors - Sufficient seniority to push back on project pressure to go live with unresolved material findings

### 5.2 Technical Skills

Technical skills for this role are documented in the original JD-001 content extracted into this file (see §5.1 Domain Expertise). Additional technical skill definitions aligned to NICE Skill Statements are maintained in [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md).

### 5.3 CERG-Specific Knowledge

CERG-specific knowledge requirements for this role are defined in [OM-001 §6](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) (Canonical Role Roster) and [RAC-001 §7](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) (Role Descriptions). See §12 (Related CERG Documents) for the complete list of standards and procedures relevant to this role.

## 6. NICE TKS Statement References

The following Task, Knowledge, and Skill statements are extracted from the NIST NICE Framework v2.2.0 Work Role [OG-WRL-012 — Pre-production Reviewer primary mapping] and filtered by relevance to this CERG role. The full TKS database is maintained at https://www.nist.gov/nice/framework/.

| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |
|---------------|-------------|-------------------|------------------------|
| Task | T0309 | Assess the effectiveness of security controls | Core work activity for this NICE Work Role |
| Task | T1021 | Review cyber defense service provider reporting structure | Core work activity for this NICE Work Role |
| Task | T1022 | Review enterprise information technology (IT) goals and objectives | Core work activity for this NICE Work Role |
| Task | T1263 | Perform security reviews | Core work activity for this NICE Work Role |
| Task | T1269 | Conduct risk analysis of applications and systems undergoing major changes | Core work activity for this NICE Work Role |
| Knowledge | K0711 | Knowledge of evaluation and validation principles and practices | Foundational knowledge for this role |
| Knowledge | K0692 | Knowledge of vulnerability assessment tools and techniques | Foundational knowledge for this role |
| Knowledge | K0720 | Knowledge of Security Assessment and Authorization (SA&A) processes | Foundational knowledge for this role |
| Knowledge | K0881 | Knowledge of learning assessment tools and techniques | Foundational knowledge for this role |
| Knowledge | K0955 | Knowledge of penetration testing principles and practices | Foundational knowledge for this role |
| Skill | S0097 | Skill in applying security controls | Core capability for this role |
| Skill | S0393 | Skill in developing assessments | Core capability for this role |
| Skill | S0394 | Skill in developing security assessments | Core capability for this role |
| Skill | S0463 | Skill in implementing software quality control processes | Core capability for this role |
| Skill | S0632 | Skill in designing Test and Evaluation Strategies (TES) | Core capability for this role |

> **Full TKS Reference:** The complete TKS statement set for the primary NICE Work Role (OV-SCA-001 → OG-WRL-012) is in the NICE Framework Components v2.2.0 dataset ([download](https://csrc.nist.gov/csrc/media/Projects/cprt/documents/nice/v2-2-0_nf_components.json)). JF-002 contains the complete CERG-to-NICE crosswalk with secondary role mappings.

## 7. Typical Qualifications

### 7.1 Education

- An active CERG Engineer at S2 or above, nominated by the Engineering Pillar Leader - Rotation period: typically 6-12 months - No additional certifications required beyond the engineer's existing qualifications

### 7.2 Certifications

Certifications for this role are defined in [TRN-001 §3](../../governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) (Certification Matrix). The matrix specifies Required, Recommended, and Aspirational certifications per role and grade.

### 7.3 Experience

Typical experience ranges by grade are defined in [JA-001 §4-5](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md). See §7.1 (Education) above for education requirements.

## 8. Key Performance Indicators (KPIs)

KPIs for this role are defined in [MTR-001](../../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) (Metrics, Dashboard, and CISO/Board Reporting). KPI allocation by job family and grade-level thresholds are documented in [PERF-001](../../governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md). Each role's evaluation criteria are embedded in the per-role JD document structure defined by [JF-001](../CERG-GOV-JF-001_Job_Families_Overview.md).

## 9. Competency Expectations by Grade

Competency expectations for this role follow the Engineering pillar behavioral anchors from [CMP-001]. Each cell describes observable behavior demonstrating the competency at that grade. Anchors are cumulative: an L3 expectation includes the L1 and L2 anchors.

| Competency Domain (CMP-001) | L1 Expectation | L2 Expectation | L3 Expectation | L4 Expectation |
|-----------------------------|----------------|----------------|----------------|----------------|
| Technical Depth | Executes assigned engineering tasks (IaC module, configuration change, architecture review checklist item) from established procedures. Recognizes when a task result does not match expected output and escalates with context. Learning the organization's technology stack: can name the major platforms, their purpose, and their security control points. | Owns a technology domain (e.g., AWS security, Azure AD, Kubernetes admission control). Designs and implements security controls independently within that domain. Performs architecture reviews in their domain and produces findings that require minimal rework from the reviewer. Authors and improves procedures for their domain. | Shapes the organization's technical security strategy in their domain. Designs reference architectures adopted by other engineers. Anticipates how changes in the technology stack will affect security posture before they land. Performs architecture reviews across domains with credibility. | Sets the technical bar for the entire Engineering pillar. Called upon for the hardest cross-domain problems. Represents the organization's engineering position to vendors, industry working groups, and regulators. Can step into any Engineering domain and contribute meaningfully within days. |
| Cross-Pillar Fluency | Understands that Risk and Governance pillars exist and can describe their basic functions. Reads vulnerability reports and compliance findings that affect their work. | Consumes Risk pillar output (vulnerability data, threat intelligence) and incorporates it into engineering decisions. Understands what Governance needs from Engineering for an audit and provides it without being chased. | Anticipates what Risk and Governance will need from an engineering decision before they ask. Participates in cross-pillar working groups as the Engineering voice. Can represent Engineering's position to a regulator or auditor without a Governance handler. | Operates fluently across all three pillars. Contributes to Risk assessments and Governance standards as a peer, not a guest. Is the person a pillar leader calls when a cross-pillar problem does not fit any procedure. |
| Risk Judgment | Follows the risk taxonomy when documenting findings. Can distinguish between a configuration drift alert that needs a ticket and one that needs an incident response page. | Independently assesses the severity and likelihood of findings in their domain. Assigns risk ratings that are consistent with the taxonomy and rarely adjusted by a senior reviewer. | Evaluates risk across domains and articulates the business impact in terms an executive can act on. Identifies compensating controls that reduce risk below what a pure vulnerability score would suggest. | Shapes the organization's risk appetite through technical judgment. Called upon by the CISO for independent risk assessments on material decisions. Their risk evaluation carries the same weight as a pillar leader's. |
| Communication | Writes clear ticket updates and status reports. Explains a technical finding to their immediate team without ambiguity. | Writes architecture review findings that a project manager or business owner can understand and act on. Presents technical topics to their pillar. Authors clear, usable procedures. | Represents Engineering in cross-functional forums with credibility. Writes decision memos that frame technical options in business terms. Presents to senior leadership and external stakeholders. | Communicates complex technical risk to the CISO, the board (as requested), regulators, and industry peers. Writes the organization's public technical positions. Represents the organization at conferences and in industry working groups. |
| Operational Discipline | Follows procedures correctly. Updates tickets and documentation when work is complete. Meets assigned SLAs. Admits when they do not know something rather than guessing. | Owns operational SLAs for their domain work streams. Ensures evidence is collected and stored per the evidence procedure. Improves procedures when they find gaps. Their work is consistently auditable without retroactive cleanup. | Designs procedures that are operationally sustainable, not just technically correct. Ensures the evidence trail for their domain is audit-ready at all times. Identifies and eliminates toil: automates repetitive operational tasks. | Sets operational standards for the pillar. Defines what "good" looks like for procedure compliance, evidence quality, and SLA management. Holds the pillar accountable to its own operational commitments. |
| Influence and Mentorship | Actively learns from senior engineers. Asks good questions. Shares what they learn with peers. | Onboards new Specialists without assistance. Peer-reviews code and configurations with constructive feedback. Their technical opinion is sought by other engineers in their domain. | Mentors Specialists and Sr. Specialists across domains. Leads technical initiatives without formal authority. Their architectural recommendations are rarely overruled. | Shapes the development of the entire Engineering team. Sets the technical bar through their own work and their mentoring. Influences hiring profiles, team composition, and organizational design. |
| Compliance and Regulatory Literacy | Knows which regulatory frameworks apply to their organization. Can describe the security implications of the major ones (NERC-CIP, CMMC, SOX) at a high level. | Understands the specific regulatory requirements that affect their domain. Can explain to an auditor how a control they implemented satisfies a regulatory requirement. | Anticipates regulatory implications of engineering decisions. Advises project teams on compliance requirements before design is complete. Represents Engineering in regulatory audits without a Governance chaperone. | Contributes to the organization's regulatory strategy. Engages with regulators on technical matters. Shapes standards so that compliance is a byproduct of good engineering, not a separate activity. |
| Continuous Learning | Completes assigned training. Pursues foundational certifications relevant to their domain. Learns the organization's technology stack. | Maintains current certifications. Stays current on developments in their domain. Shares what they learn with the team. | Pursues advanced certifications. Contributes to the team's knowledge base through documented research, brown-bag sessions, or internal training. Evaluates new technologies for organizational adoption. | Recognized externally for expertise. Shapes the organization's technology and certification roadmap. The person other engineers go to when they need to understand an emerging technology or threat. |

> **Full Reference:** See [CMP-001] for the complete competency model, including the Management Track addendum (§7) and guidance on using the model for hiring, development, and promotion (§8).

## 10. Success Profile

A Pre-production Reviewer is successful when security issues are identified and resolved before they reach production, not after. Key indicators: architecture reviews are completed before any infrastructure is provisioned; findings are specific enough that project teams can act on them without reinterpretation; the review cycle time does not delay releases; recurring findings trigger standard updates rather than repeated manual reviews. The reviewer is seen as an enabler of secure delivery, not a gate that slows things down.

## 11. Career Path

### 11.1 Within-Family Progression

The Pre-production Reviewer is a rotated Engineering function rather than a permanent career destination. Progression occurs through the individual's home Engineering role under [JF-001 §9.1](../CERG-GOV-JF-001_Job_Families_Overview.md#91-jf-seceng--security-engineering-levels) and [JA-001 §7.2](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md#72-engineering-pillar). Reviewer qualification is evidence of readiness for higher Engineering levels when the reviewer demonstrates consistent judgment, clear findings, reusable review patterns, and the ability to coach project teams before defects reach production.

---

### 11.2 Cross-Family Movement

Cross-family movement options are defined in the [Family-to-Family Career Lattice (JF-001 §4)](../CERG-GOV-JF-001_Job_Families_Overview.md#4-family-to-family-career-lattice). The Left-Right Knowledge Model ([FRM-001 §9.2](../../governance/CERG-GOV-FRM-001_CERG_Framework.md)) and cross-training expectations ([OM-001 §10.4](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md)) operationalize cross-family career movement.

### 11.3 Management Track Option

At L3+ (SME track), a Management track option may be available per [JA-001 §8.1] (SME to Management Transition). Readiness indicators include: consistently sought out for guidance by junior team members, leading cross-functional initiatives without formal authority, and communicating clearly with non-technical stakeholders. The transition is a track change, not a grade promotion — an S3 Advisor moving to M1 Manager carries their technical credibility into the management role. Management competencies are defined in [CMP-001 §7]. See [JA-001 §5] for Management grade definitions (M1-M4) and §9 (Span of Control and Team Design) for when to create a management role.

## 12. Related CERG Documents

| Document | ID | Relevance |
|----------|-----|-----------|
| Operating Model | [`CERG-GOV-OM-001`](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role name; pillar structure |
| RACI Instrument | [`CERG-GOV-RAC-001`](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | This role's accountability assignments |
| Job Architecture | [`CERG-GOV-JA-001`](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade definitions; progression criteria |
| Competency Model | [`CERG-GOV-CMP-001`](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Full behavioral anchors |
| Performance Framework | [`CERG-GOV-PERF-001`](../../governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | Performance review cadence and calibration |
| Training Framework | [`CERG-GOV-TRN-001`](../../governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) | Certification matrix |
| Job Families Overview | [`CERG-GOV-JF-001`](../CERG-GOV-JF-001_Job_Families_Overview.md) | Family structure and level definitions |
| NICE Crosswalk | [`CERG-GOV-JF-002`](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE Work Role mapping |

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-JD-SECENG-008 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Extracted from monolithic JD-001 into enhanced per-role format with NICE mapping, KPI sections, and competency anchor sections. |

### Review Triggers

- Change to this role's definition in OM-001 §6.1
- Change to this role's NICE Work Role mapping in JF-002
- Change to this role's grade range in JA-001 §7
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Job Families Overview | [`CERG-GOV-JF-001`](../CERG-GOV-JF-001_Job_Families_Overview.md) | Family structure and level definitions |
| NICE Crosswalk | [`CERG-GOV-JF-002`](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE Work Role mapping |
