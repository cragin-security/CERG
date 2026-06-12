| | |
|---|---|
| **Document ID** | CERG-GOV-JD-RISKOPS-007 |
| **Version** | 1.0 |
| **Status** | Draft |
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

**NICE Work Role Definition:** [Placeholder — requires live NICE TKS database access at https://www.nist.gov/nice/framework/]

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

*[Placeholder — requires per-role specification. See Feedback_Mary.md Appendix C for the Cloud Security Engineer sample pattern.]*

## 5. Required Knowledge, Skills, and Abilities (KSAs)

### 5.1 Domain Expertise

- SIEM expertise: Splunk, Elastic, Microsoft Sentinel, or equivalent - Detection rule authoring: Sigma, KQL, SPL, YARA, YARA-L - MITRE ATT&CK framework fluency: technique-level understanding and mapping - Log analysis: Windows Event Log, Sysmon, network traffic, cloud audit logs, endpoint telemetry - Understanding of adversary TTPs and how they manifest in logs - Scripting and automation: Python, PowerShell, or equivalent - Data engineering: understanding of log pipelines, data normalization, and detection architecture

### 5.2 Technical Skills

*[See JD-001 original content for role-specific technical skills.]*

### 5.3 CERG-Specific Knowledge

*[Reference OM-001, RAC-001, and relevant standards/procedures for this role.]*

## 6. NICE TKS Statement References

*Placeholder — requires live NICE TKS database access at https://www.nist.gov/nice/framework/. When populated, filter by the primary NICE Work Role (OV-SCA-001) and extract the 5-10 most relevant Task, Knowledge, and Skill statements.*

| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |
|---------------|-------------|-------------------|------------------------|
| Task | T#### | [From NICE TKS database] | [How this task manifests] |
| Knowledge | K#### | [From NICE TKS database] | [How this knowledge applies] |
| Skill | S#### | [From NICE TKS database] | [How this skill is used] |

## 7. Typical Qualifications

### 7.1 Education

- 3-12+ years in cybersecurity, security operations, or detection engineering - Bachelor's degree in a relevant technical field or equivalent experience - Relevant certifications: GCIH, GCIA, GMON, GCDA, or equivalent

### 7.2 Certifications

*[Placeholder — see TRN-001 certification matrix for this role.]*

| Grade | Required | Recommended | Aspirational |
|-------|----------|-------------|--------------|
| S1 | [From TRN-001] | [From TRN-001] | [From TRN-001] |

### 7.3 Experience

*[Placeholder — see JD-001 original content + JA-001 grade definitions.]*

## 8. Key Performance Indicators (KPIs)

*[Placeholder — KPIs sourced from MTR-001. Populate with 5-8 measurable metrics with grade-level thresholds.]*

| KPI | MTR-001 ID | Description | L1 Target | L2 Target | L3 Target | L4 Target |
|-----|-----------|-------------|-----------|-----------|-----------|-----------|
| [KPI name] | [MTR-001 ID] | [Description] | [Threshold] | [Threshold] | [Threshold] | [Threshold] |

## 9. Competency Expectations by Grade

*[Placeholder — embed CMP-001 behavioral anchors for this role's family and grade.]*

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

*[Placeholder — see the Family-to-Family Career Lattice in [JF-001 §4](../CERG-GOV-JF-001_Job_Families_Overview.md).]*

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
| **Status** | Draft |
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
