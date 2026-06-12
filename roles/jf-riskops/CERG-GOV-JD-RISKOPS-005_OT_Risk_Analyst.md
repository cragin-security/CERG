| | |
|---|---|
| **Document ID** | CERG-GOV-JD-RISKOPS-005 |
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

# OT Risk Analyst

**Job Family:** JF-RISKOPS — Risk Operations
**Job Level Range:** L1-L4 (CERG Grade S1-S4/M3)
**CERG Canonical Role:** OT Risk Analyst (OM-001 §6.1)

---

## 1. Role Summary

The OT Risk Analyst owns OT-safe vulnerability assessment and industrial control system threat intelligence. They are the Risk pillar's specialist for operational technology environments, where a misconfigured scan can have physical consequences and threat actors have different motivations and techniques than in enterprise IT.

## 2. NICE Workforce Framework Mapping

| Mapping Level | NICE Work Role | NICE Work Role ID | NICE Work Role Category |
|---------------|----------------|-------------------|-------------------------|
| Primary | Threat/Warning Analyst | AN-TWA-001 | AN |

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

- Conduct OT-safe vulnerability assessments: passive scanning, protocol-aware assessment, and where appropriate, controlled active scanning during maintenance windows - Track ICS-specific threat actors and campaigns: their targets, TTPs, and relevance to the organization's OT environment - Produce OT threat intelligence products for OT operators, Engineering, and leadership - Map OT threats to MITRE ATT&CK for ICS and translate into detection and control recommendations - Partner with OT Security Engineer to prioritize remediation based on operational context - Support the NERC-CIP compliance program with OT vulnerability data and risk assessments - Support incident response for OT incidents with threat context and containment guidance that respects operational constraints - Maintain OT-specific vulnerability and threat intelligence tooling

### 4.2 Grade-Level Responsibility Differentiation

Grade-level responsibility differentiation for this role is defined in [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) (Role-to-Grade Mapping). The grade definitions (S1-S4 SME Track, M1-M4 Management Track) and leveling dimensions are in JA-001 §4-5. Behavioral anchors at each grade are in [CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md).

## 5. Required Knowledge, Skills, and Abilities (KSAs)

### 5.1 Domain Expertise

- Deep expertise in OT/ICS environments and their operational constraints - OT vulnerability assessment tools and techniques (passive and active) - ICS threat landscape: actors, campaigns, malware (BlackEnergy, CrashOverride, Triton/Trisis, Pipedream/Incontroller) - MITRE ATT&CK for ICS - NERC-CIP requirements, particularly CIP-007 and CIP-010 - Understanding of OT operational constraints: safety systems, real-time requirements, change windows

### 5.2 Technical Skills

Technical skills for this role are documented in the original JD-001 content extracted into this file (see §5.1 Domain Expertise). Additional technical skill definitions aligned to NICE Skill Statements are maintained in [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md).

### 5.3 CERG-Specific Knowledge

CERG-specific knowledge requirements for this role are defined in [OM-001 §6](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) (Canonical Role Roster) and [RAC-001 §7](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) (Role Descriptions). See §12 (Related CERG Documents) for the complete list of standards and procedures relevant to this role.

## 6. NICE TKS Statement References

The following Task, Knowledge, and Skill statements are extracted from the NIST NICE Framework v2.2.0 Work Role [PD-WRL-006 — OT Risk Analyst primary mapping] and filtered by relevance to this CERG role. The full TKS database is maintained at https://www.nist.gov/nice/framework/.

| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |
|---------------|-------------|-------------------|------------------------|
| Task | T1020 | Determine the operational and safety impacts of cybersecurity lapses | Core work activity for this NICE Work Role |
| Task | T0685 | Evaluate threat decision-making processes | Core work activity for this NICE Work Role |
| Task | T0845 | Identify cyber threat tactics and methodologies | Core work activity for this NICE Work Role |
| Task | T1772 | Identify indications and warnings of target communication changes or processing failures | Core work activity for this NICE Work Role |
| Task | T1799 | Notify appropriate personnel of imminent hostile intentions or activities | Core work activity for this NICE Work Role |
| Knowledge | K0675 | Knowledge of risk management processes | Foundational knowledge for this role |
| Knowledge | K0674 | Knowledge of computer networking protocols | Foundational knowledge for this role |
| Knowledge | K0684 | Knowledge of cybersecurity threat characteristics | Foundational knowledge for this role |
| Knowledge | K0786 | Knowledge of physical computer components | Foundational knowledge for this role |
| Knowledge | K0788 | Knowledge of adversarial tactics principles and practices | Foundational knowledge for this role |
| Skill | S0430 | Skill in collaborating with others | Core capability for this role |
| Skill | S0433 | Skill in creating analytics | Core capability for this role |
| Skill | S0516 | Skill in performing threat emulation tactics | Core capability for this role |
| Skill | S0709 | Skill in developing analytics | Core capability for this role |
| Skill | S0111 | Skill in interfacing with customers | Core capability for this role |

> **Full TKS Reference:** The complete TKS statement set for the primary NICE Work Role (AN-TWA-001 → PD-WRL-006) is in the NICE Framework Components v2.2.0 dataset ([download](https://csrc.nist.gov/csrc/media/Projects/cprt/documents/nice/v2-2-0_nf_components.json)). JF-002 contains the complete CERG-to-NICE crosswalk with secondary role mappings.

## 7. Typical Qualifications

### 7.1 Education

- 5-15+ years in OT/ICS environments, with 3+ years of cybersecurity focus - Bachelor's degree in engineering or equivalent OT experience - Relevant certifications: GICSP, GRID, CISSP, or equivalent

### 7.2 Certifications

Certifications for this role are defined in [TRN-001 §3](../../governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) (Certification Matrix). The matrix specifies Required, Recommended, and Aspirational certifications per role and grade.

### 7.3 Experience

Typical experience ranges by grade are defined in [JA-001 §4-5](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md). See §7.1 (Education) above for education requirements.

## 8. Key Performance Indicators (KPIs)

KPIs for this role are defined in [MTR-001](../../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) (Metrics, Dashboard, and CISO/Board Reporting). KPI allocation by job family and grade-level thresholds are documented in [PERF-001](../../governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md). Each role's evaluation criteria are embedded in the per-role JD document structure defined by [JF-001](../CERG-GOV-JF-001_Job_Families_Overview.md).

## 9. Competency Expectations by Grade

Competency expectations for this role are defined in [CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md), organized by the eight CERG competency domains (Technical Depth, Cross-Pillar Fluency, Risk Judgment, Communication, Operational Discipline, Influence and Mentorship, Compliance & Regulatory Literacy, Continuous Learning). Behavioral anchors are specified per domain per grade per family.

| Competency Domain (CMP-001) | L1 Expectation | L2 Expectation | L3 Expectation | L4 Expectation |
|-----------------------------|----------------|----------------|----------------|----------------|
| Technical Depth | [Anchor] | [Anchor] | [Anchor] | [Anchor] |
| Cross-Pillar Fluency | [Anchor] | [Anchor] | [Anchor] | [Anchor] |
| Risk Judgment | [Anchor] | [Anchor] | [Anchor] | [Anchor] |
| Communication | [Anchor] | [Anchor] | [Anchor] | [Anchor] |
| Operational Discipline | [Anchor] | [Anchor] | [Anchor] | [Anchor] |
| Influence and Mentorship | [Anchor] | [Anchor] | [Anchor] | [Anchor] |
| Compliance & Regulatory Literacy | [Anchor] | [Anchor] | [Anchor] | [Anchor] |
| Continuous Learning | [Anchor] | [Anchor] | [Anchor] | [Anchor] |

## 10. Success Profile

Placeholder — see JD-001 original content.

## 11. Career Path

### 11.1 Within-Family Progression

---

### 11.2 Cross-Family Movement

Cross-family movement options are defined in the [Family-to-Family Career Lattice (JF-001 §4)](../CERG-GOV-JF-001_Job_Families_Overview.md#4-family-to-family-career-lattice). The Left-Right Knowledge Model ([FRM-001 §9.2](../../governance/CERG-GOV-FRM-001_CERG_Framework.md)) and cross-training expectations ([OM-001 §10.4](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md)) operationalize cross-family career movement.

### 11.3 Management Track Option

*[Placeholder — at L3+, a Management track option may be available per [JA-001 §8](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md).]*

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
| **Document ID** | CERG-GOV-JD-RISKOPS-005 |
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
