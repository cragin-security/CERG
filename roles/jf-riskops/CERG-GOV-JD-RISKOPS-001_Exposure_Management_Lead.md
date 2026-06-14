| | |
|---|---|
| **Document ID** | CERG-GOV-JD-RISKOPS-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](../../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

---

# Exposure Management Lead

**Job Family:** JF-RISKOPS — Risk Operations
**Job Level Range:** L1-L4 (CERG Grade S1-S4/M3)
**CERG Canonical Role:** Exposure Management Lead (OM-001 §6.1)

---

## 1. Role Summary

The Exposure Management Lead operates the Vulnerability Management Procedure. They own the vulnerability scanning program, the finding prioritization and triage process, the remediation SLAs, and the vulnerability posture metrics that feed the CISO dashboard. They ensure that every vulnerability in the environment is known, prioritized, tracked to remediation, and reported.

## 2. NICE Workforce Framework Mapping

| Mapping Level | NICE Work Role | NICE Work Role ID | NICE Work Role Category |
|---------------|----------------|-------------------|-------------------------|
| Primary | Vulnerability Assessment Analyst | PR-VAM-001 | PR |

**NICE Work Role Definition:** See [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) for the official NICE Work Role definition and complete CERG-to-NICE mapping. The NICE TKS database is available at https://www.nist.gov/nice/framework/.

## 3. Job Family & Level Placement

| Family | JF-RISKOPS — Risk Operations |
|--------|---------------------------|
| Level Range | L1 through L4 |
| CERG Grade Range | S1-S4/M3 |
| Terminal Grade | S4/M3 — see [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) for details |
| Track | SME / Dual-track |

## 4. Key Responsibilities

### 4.1 Core Responsibilities (All Grades)

- Operate and maintain the vulnerability scanning infrastructure across IT, cloud, and OT environments - Define and enforce vulnerability triage criteria: severity, exploitability, asset criticality, exposure - Own remediation SLAs and track compliance, escalating overdue findings per the defined process - Report vulnerability posture metrics: open findings by severity and age, SLA compliance, mean time to remediate, coverage gaps - Coordinate with IT, OT, and Engineering teams to drive remediation - Manage false-positive triage and scanner tuning to maintain scan hygiene - Govern OT-safe scanning procedures, ensuring scan techniques do not introduce operational risk - Contribute to vulnerability management tooling selection, configuration, and optimization - Support incident response with vulnerability context for compromised systems

### 4.2 Grade-Level Responsibility Differentiation

Grade-level responsibility differentiation for this role is defined in [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) (Role-to-Grade Mapping). The grade definitions (S1-S4 SME Track, M1-M4 Management Track) and leveling dimensions are in JA-001 §4-5. Behavioral anchors at each grade are in [CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md).

## 5. Required Knowledge, Skills, and Abilities (KSAs)

### 5.1 Domain Expertise

- Deep expertise in vulnerability management platforms: Tenable, Qualys, Rapid7, CrowdStrike Spotlight, or equivalent - Vulnerability scoring and prioritization: CVSS, EPSS, CISA KEV, asset-contextual risk scoring - Understanding of remediation workflows and the operational constraints on patching - OT/ICS vulnerability management awareness (if the organization has OT) - Data analysis and reporting: ability to produce actionable metrics from scan data - Scripting and automation: Python, PowerShell, or equivalent

### 5.2 Technical Skills

Technical skills for this role are documented in the original JD-001 content extracted into this file (see §5.1 Domain Expertise). Additional technical skill definitions aligned to NICE Skill Statements are maintained in [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md).

### 5.3 CERG-Specific Knowledge

CERG-specific knowledge requirements for this role are defined in [OM-001 §6](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) (Canonical Role Roster) and [RAC-001 §7](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) (Role Descriptions). See §12 (Related CERG Documents) for the complete list of standards and procedures relevant to this role.

## 6. NICE TKS Statement References

The following Task, Knowledge, and Skill statements are extracted from the NIST NICE Framework v2.2.0 Work Role [PD-WRL-007 — Exposure Management Lead primary mapping] and filtered by relevance to this CERG role. The full TKS database is maintained at https://www.nist.gov/nice/framework/.

| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |
|---------------|-------------|-------------------|------------------------|
| Task | T1119 | Recommend vulnerability remediation strategies | Core work activity for this NICE Work Role |
| Task | T1091 | Perform authorized penetration testing on enterprise network assets | Core work activity for this NICE Work Role |
| Task | T1619 | Perform risk and vulnerability assessments | Core work activity for this NICE Work Role |
| Task | T1020 | Determine the operational and safety impacts of cybersecurity lapses | Core work activity for this NICE Work Role |
| Task | T1041 | Determine impact of software configurations | Core work activity for this NICE Work Role |
| Knowledge | K1076 | Knowledge of risk scoring principles and practices | Foundational knowledge for this role |
| Knowledge | K0674 | Knowledge of computer networking protocols | Foundational knowledge for this role |
| Knowledge | K0675 | Knowledge of risk management processes | Foundational knowledge for this role |
| Knowledge | K0676 | Knowledge of cybersecurity laws and regulations | Foundational knowledge for this role |
| Knowledge | K0677 | Knowledge of cybersecurity policies and procedures | Foundational knowledge for this role |
| Skill | S0543 | Skill in scanning for vulnerabilities | Core capability for this role |
| Skill | S0483 | Skill in identifying software communications vulnerabilities | Core capability for this role |
| Skill | S0492 | Skill in performing threat environment analysis | Core capability for this role |
| Skill | S0532 | Skill in analyzing software configurations | Core capability for this role |
| Skill | S0544 | Skill in recognizing vulnerabilities | Core capability for this role |

> **Full TKS Reference:** The complete TKS statement set for the primary NICE Work Role (PR-VAM-001 → PD-WRL-007) is in the NICE Framework Components v2.2.0 dataset ([download](https://csrc.nist.gov/csrc/media/Projects/cprt/documents/nice/v2-2-0_nf_components.json)). JF-002 contains the complete CERG-to-NICE crosswalk with secondary role mappings.

## 7. Typical Qualifications

### 7.1 Education

- 5-12+ years in cybersecurity, with 3+ years in vulnerability management - Bachelor's degree or equivalent experience - Relevant certifications: CISSP, GCIH, GMON, or equivalent

### 7.2 Certifications

Certifications for this role are defined in [TRN-001 §3](../../governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) (Certification Matrix). The matrix specifies Required, Recommended, and Aspirational certifications per role and grade.

### 7.3 Experience

Typical experience ranges by grade are defined in [JA-001 §4-5](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md). See §7.1 (Education) above for education requirements.

## 8. Key Performance Indicators (KPIs)

KPIs for this role are defined in [MTR-001](../../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) (Metrics, Dashboard, and CISO/Board Reporting). KPI allocation by job family and grade-level thresholds are documented in [PERF-001](../../governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md). Each role's evaluation criteria are embedded in the per-role JD document structure defined by [JF-001](../CERG-GOV-JF-001_Job_Families_Overview.md).

## 9. Competency Expectations by Grade

Competency expectations for this role follow the Risk pillar behavioral anchors from [CMP-001]. Each cell describes observable behavior demonstrating the competency at that grade. Anchors are cumulative: an L3 expectation includes the L1 and L2 anchors.

| Competency Domain (CMP-001) | L1 Expectation | L2 Expectation | L3 Expectation | L4 Expectation |
|-----------------------------|----------------|----------------|----------------|----------------|
| Technical Depth | Operates the Risk pillar's tools (vulnerability scanner, CSPM platform, threat intel platform, detection pipeline) under supervision. Triages alerts following established procedures. Recognizes false positives and true positives with increasing accuracy. | Owns a Risk domain (e.g., vulnerability management for a platform class, vendor assessments for a business unit, a set of detection rules). Tunes tools to reduce noise and improve signal. Independently investigates findings and determines root cause. | Shapes the Risk pillar's approach to exposure management. Designs assessment methodologies. Correlates findings across tools to identify systemic weaknesses that individual alerts miss. | Sets the analytical bar for the entire Risk pillar. Called upon for the hardest exposure questions. Represents the organization's risk posture to regulators, auditors, and industry peers. |
| Cross-Pillar Fluency | Understands that Engineering builds systems and Governance owns compliance. Reads architecture review outputs and compliance standards that affect their risk assessments. | Delivers risk findings in a format Engineering can act on. Understands what evidence Governance needs from Risk assessments and provides it proactively. Participates in cross-pillar threat modeling sessions. | Collaborates with Engineering to design controls that address risk findings, not just report them. Feeds risk intelligence into Governance's compliance calendar. Anticipates which risk findings will become audit findings. | Operates fluently across all three pillars. Contributes to Engineering architecture decisions and Governance standards as a peer. The person a pillar leader calls when a risk question spans all three pillars. |
| Risk Judgment | Applies the risk taxonomy correctly when triaging findings. Distinguishes between Critical, High, Medium, and Low severity using the defined criteria. Escalates findings that exceed SLA without delay. | Independently assesses the business impact of findings in their domain. Adjusts risk ratings based on context and documents the rationale. Produces risk assessments that the Risk Pillar Leader accepts without material revision. | Assesses systemic risk: identifies patterns across individual findings that indicate a deeper weakness. Evaluates risk from new technologies, vendors, or business initiatives before they are operational. | Shapes the organization's risk appetite. Called upon by the CISO for independent risk evaluation on material decisions. Their risk judgment on novel or ambiguous situations is treated as authoritative. |
| Communication | Writes clear finding descriptions with reproducible steps, impact statements, and remediation guidance. Updates stakeholders on finding status without being prompted. | Delivers risk briefings to business owners and project teams. Translates vulnerability data into business risk without losing technical accuracy. Writes vendor risk assessment reports that procurement and legal can act on. | Presents risk posture to executive audiences. Communicates threat landscape changes and their organizational implications. Writes threat intelligence products consumed by leadership. | Communicates organizational risk posture to the board, regulators, and external stakeholders. Represents the organization's risk position in industry forums. |
| Operational Discipline | Triages findings within SLA. Documents assessment results in the designated system. Follows the vulnerability management and risk register procedures. | Owns operational SLAs for their domain. Ensures risk register entries are current and complete. Maintains scanning schedules, detection rule lifecycles, or vendor assessment cadences without gaps. | Designs risk assessment workflows that produce consistent, auditable output. Ensures the Risk pillar's operational cadence is documented, measured, and improving. Identifies and automates repetitive risk assessment tasks. | Sets operational standards for the Risk pillar. Defines what "defensible" risk assessment looks like under regulatory scrutiny. |
| Influence and Mentorship | Learns from senior analysts. Asks good questions about methodology and judgment. Shares interesting findings with the team. | Trains new analysts on Risk tools and procedures. Peer-reviews risk assessments and detection rules. Their analytical judgment is sought by other team members. | Mentors analysts across Risk domains. Leads cross-functional risk initiatives. Their risk assessments shape how Engineering and business owners prioritize remediation. | Develops the analytical capability of the entire Risk team. Sets the quality bar for risk assessment, threat intelligence, and detection engineering. Influences organizational risk culture. |
| Compliance and Regulatory Literacy | Knows which regulatory frameworks apply and can describe how Risk assessments support compliance. | Understands the specific regulatory requirements that govern their Risk domain. Produces risk assessments that meet the evidence standards of the relevant frameworks. | Anticipates how regulatory changes will affect the Risk program's scope and cadence. Advises Governance on the risk implications of compliance findings. | Contributes to the organization's regulatory strategy from a risk perspective. Engages with regulators on risk methodology. |
| Continuous Learning | Completes assigned training. Pursues foundational certifications. Learns the organization's threat landscape. | Maintains current certifications. Tracks the threat actors, TTPs, and vulnerabilities relevant to the organization's industry. | Pursues advanced certifications. Contributes threat research or methodology improvements adopted by the team. Represents the organization in threat-sharing communities. | Recognized externally for risk or threat expertise. Contributes to industry threat intelligence, risk methodology, or detection frameworks. |

> **Full Reference:** See [CMP-001] for the complete competency model, including the Management Track addendum (§7) and guidance on using the model for hiring, development, and promotion (§8).

## 10. Success Profile

A Exposure Management Lead is successful when the organization knows its exposure posture in real time and is actively reducing it. Key indicators: scanning coverage is complete across all in-scope assets; vulnerability age is trending down, not up; remediation SLAs are met for each severity tier; the vulnerability register is the authoritative source of truth for exposure decisions. The lead ensures that every Critical and High finding has an owner, a plan, and a due date — and that the CISO can report exposure status to the board in under an hour.

## 11. Career Path

### 11.1 Within-Family Progression

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
| **Document ID** | CERG-GOV-JD-RISKOPS-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
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
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Extracted from monolithic JD-001 into enhanced per-role format with NICE mapping, KPI placeholders, and competency anchor placeholders. |

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
