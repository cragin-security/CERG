| | |
|---|---|
| **Document ID** | CERG-GOV-JD-RISKOPS-007 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](../../CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

---

# Vendor Risk Analyst

**Job Family:** JF-RISKOPS — Risk Operations
**Job Level Range:** L1-L4 (CERG Grade S1-S4/M3)
**CERG Canonical Role:** Vendor Risk Analyst (OM-001 §6.1)

---

## 1. Role Summary

The Detection Engineer owns detection-rule authoring, MITRE ATT&CK coverage, and the detection tuning lifecycle. They turn threat intelligence, vulnerability data, and red team findings into detection content that finds adversaries before the adversary achieves their objective. They are the bridge between knowing what threats exist and being able to see them in the environment.

## 2. NICE Workforce Framework Mapping

| Mapping Level | NICE Work Role | NICE Work Role ID | NICE Work Role Category |
|---------------|----------------|-------------------|-------------------------|
| Primary | Security Control Assessor | OV-SCA-001 | OV |

**NICE Work Role Definition:** See [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) for the official NICE Work Role definition and complete CERG-to-NICE mapping. The NICE TKS database is available at https://www.nist.gov/nice/framework/.

## 3. Job Family & Level Placement

| Family | JF-RISKOPS — Risk Operations |
|--------|---------------------------|
| Level Range | L1 through L4 |
| CERG Grade Range | S1-S4/M3 |
| Terminal Grade | S4/M3 — see [JA-001 §7](../../CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) for details |
| Track | SME / Dual-track |

## 4. Key Responsibilities

### 4.1 Core Responsibilities (All Grades)

- Author, test, and deploy detection rules across SIEM, EDR, NDR, and cloud detection platforms - Map detection coverage to MITRE ATT&CK and maintain the coverage matrix - Tune detection rules to reduce false positives while maintaining true-positive sensitivity - Translate threat intelligence into detection content: new rules, updated logic, expanded data sources - Incorporate adversarial testing findings: write detections for the TTPs the red team successfully executed - Govern the detection lifecycle: new rule authoring, testing, deployment, performance monitoring, tuning, and retirement - Hand off confirmed detections to the Incident Response team per the defined procedure - Maintain and improve the logging and monitoring coverage required to support detection content - Contribute to the Logging, Monitoring, and Detection Standard

### 4.2 Grade-Level Responsibility Differentiation

Grade-level responsibility differentiation for this role is defined in [JA-001 §7](../../CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) (Role-to-Grade Mapping). The grade definitions (S1-S4 SME Track, M1-M4 Management Track) and leveling dimensions are in JA-001 §4-5. Behavioral anchors at each grade are in [CMP-001](../../CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md).

## 5. Required Knowledge, Skills, and Abilities (KSAs)

### 5.1 Domain Expertise

- SIEM expertise: Splunk, Elastic, Microsoft Sentinel, or equivalent - Detection rule authoring: Sigma, KQL, SPL, YARA, YARA-L - MITRE ATT&CK framework fluency: technique-level understanding and mapping - Log analysis: Windows Event Log, Sysmon, network traffic, cloud audit logs, endpoint telemetry - Understanding of adversary TTPs and how they manifest in logs - Scripting and automation: Python, PowerShell, or equivalent - Data engineering: understanding of log pipelines, data normalization, and detection architecture

### 5.2 Technical Skills

Technical skills for this role are documented in the original JD-001 content extracted into this file (see §5.1 Domain Expertise). Additional technical skill definitions aligned to NICE Skill Statements are maintained in [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md).

### 5.3 CERG-Specific Knowledge

CERG-specific knowledge requirements for this role are defined in [OM-001 §6](../../CERG-GOV-OM-001_CERG_Operating_Model.md) (Canonical Role Roster) and [RAC-001 §7](../../CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) (Role Descriptions). See §12 (Related CERG Documents) for the complete list of standards and procedures relevant to this role.

## 6. NICE TKS Statement References

*Placeholder — requires live NICE TKS database access at https://www.nist.gov/nice/framework/. When populated, filter by the primary NICE Work Role (OV-SCA-001) and extract the 5-10 most relevant Task, Knowledge, and Skill statements.*

| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |
|---------------|-------------|-------------------|------------------------|
| Task | See JF-002 | Task statements for this role's primary NICE Work Role | Consult the NICE TKS database at https://www.nist.gov/nice/framework/ |
| Knowledge | See JF-002 | Knowledge statements for this role's primary NICE Work Role | Consult the NICE TKS database at https://www.nist.gov/nice/framework/ |
| Skill | See JF-002 | Skill statements for this role's primary NICE Work Role | Consult the NICE TKS database at https://www.nist.gov/nice/framework/ |

## 7. Typical Qualifications

### 7.1 Education

- 3-12+ years in cybersecurity, security operations, or detection engineering - Bachelor's degree in a relevant technical field or equivalent experience - Relevant certifications: GCIH, GCIA, GMON, GCDA, or equivalent

### 7.2 Certifications

Certifications for this role are defined in [TRN-001 §3](../../CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) (Certification Matrix). The matrix specifies Required, Recommended, and Aspirational certifications per role and grade.

### 7.3 Experience

Typical experience ranges by grade are defined in [JA-001 §4-5](../../CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md). See §7.1 (Education) above for education requirements.

## 8. Key Performance Indicators (KPIs)

KPIs for this role are defined in [MTR-001](../../CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) (Metrics, Dashboard, and CISO/Board Reporting). KPI allocation by job family and grade-level thresholds are documented in [PERF-001](../../CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md). Each role's evaluation criteria are embedded in the per-role JD document structure defined by [JF-001](../CERG-GOV-JF-001_Job_Families_Overview.md).

## 9. Competency Expectations by Grade

Competency expectations for this role are defined in [CMP-001](../../CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md), organized by the eight CERG competency domains (Technical Depth, Cross-Pillar Fluency, Risk Judgment, Communication, Operational Discipline, Influence and Mentorship, Compliance & Regulatory Literacy, Continuous Learning). Behavioral anchors are specified per domain per grade per family.

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

---  ## 6. Governance Pillar Roles

### 11.2 Cross-Family Movement

Cross-family movement options are defined in the [Family-to-Family Career Lattice (JF-001 §4)](../CERG-GOV-JF-001_Job_Families_Overview.md#4-family-to-family-career-lattice). The Left-Right Knowledge Model ([FRM-001 §9.2](../../CERG-GOV-FRM-001_CERG_Framework.md)) and cross-training expectations ([OM-001 §10.4](../../CERG-GOV-OM-001_CERG_Operating_Model.md)) operationalize cross-family career movement.

### 11.3 Management Track Option

*[Placeholder — at L3+, a Management track option may be available per [JA-001 §8](../../CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md).]*

## 12. Related CERG Documents

| Document | ID | Relevance |
|----------|-----|-----------|
| Operating Model | [`CERG-GOV-OM-001`](../../CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role name; pillar structure |
| RACI Instrument | [`CERG-GOV-RAC-001`](../../CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | This role's accountability assignments |
| Job Architecture | [`CERG-GOV-JA-001`](../../CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade definitions; progression criteria |
| Competency Model | [`CERG-GOV-CMP-001`](../../CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Full behavioral anchors |
| Performance Framework | [`CERG-GOV-PERF-001`](../../CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | Performance review cadence and calibration |
| Training Framework | [`CERG-GOV-TRN-001`](../../CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) | Certification matrix |
| Job Families Overview | [`CERG-GOV-JF-001`](../CERG-GOV-JF-001_Job_Families_Overview.md) | Family structure and level definitions |
| NICE Crosswalk | [`CERG-GOV-JF-002`](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE Work Role mapping |

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-JD-RISKOPS-007 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | Pending |
| **Parent Policy** | [`CERG-POL-001`](../../CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
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
| Cybersecurity Policy | [`CERG-POL-001`](../../CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Job Families Overview | [`CERG-GOV-JF-001`](../CERG-GOV-JF-001_Job_Families_Overview.md) | Family structure and level definitions |
| NICE Crosswalk | [`CERG-GOV-JF-002`](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE Work Role mapping |
