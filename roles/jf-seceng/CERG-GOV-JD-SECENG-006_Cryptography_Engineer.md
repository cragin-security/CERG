| | |
|---|---|
| **Document ID** | CERG-GOV-JD-SECENG-006 |
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

# Cryptography Engineer

**Job Family:** JF-SECENG — Security Engineering
**Job Level Range:** L1-L4 (CERG Grade S1-S4)
**CERG Canonical Role:** Cryptography Engineer (OM-001 §6.1)

---

## 1. Role Summary

The Cryptography Engineer owns cryptography and key management: the key management platforms, the certificate authority hierarchy, the transport security posture, and FIPS compliance. They ensure that encryption is correctly implemented, keys are protected, certificates do not expire unexpectedly, and cryptographic standards are met across the estate.

## 2. NICE Workforce Framework Mapping

| Mapping Level | NICE Work Role | NICE Work Role ID | NICE Work Role Category |
|---------------|----------------|-------------------|-------------------------|
| Primary | Security Architect | SP-ARC-001 | SP |

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

- Design, implement, and maintain the enterprise key management infrastructure (HSM, cloud KMS, secrets vaults) - Govern the certificate authority (CA) hierarchy: internal CA, public CA integrations, certificate lifecycle automation - Define and enforce transport security requirements: TLS versions, cipher suites, certificate validation - Manage secrets rotation for machine identities, API keys, and service accounts - Ensure FIPS 140-2/140-3 compliance for cryptographic modules in regulated environments - Conduct cryptographic assessments of new systems, applications, and vendor products - Support the rotation of exposed secrets during incident response - Contribute to the Cryptography and Key Management Standard and maintain its technical requirements - Advise Engineering and IT teams on cryptographic design decisions

### 4.2 Grade-Level Responsibility Differentiation

Grade-level responsibility differentiation for this role is defined in [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) (Role-to-Grade Mapping). The grade definitions (S1-S4 SME Track, M1-M4 Management Track) and leveling dimensions are in JA-001 §4-5. Behavioral anchors at each grade are in [CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md).

## 5. Required Knowledge, Skills, and Abilities (KSAs)

### 5.1 Domain Expertise

- Deep expertise in cryptographic principles: symmetric and asymmetric encryption, hashing, digital signatures, key agreement protocols - PKI architecture and certificate lifecycle management - Key management platforms: HashiCorp Vault, cloud-native KMS, Thales/CipherTrust, Utimaco - Hardware security modules (HSMs) - TLS/PKI tools and protocols: ACME, OCSP, CRL, S/MIME, code signing - FIPS 140-2/140-3 and Common Criteria standards - Post-quantum cryptography awareness (preparing for transition, not yet implementing)

### 5.2 Technical Skills

Technical skills for this role are documented in the original JD-001 content extracted into this file (see §5.1 Domain Expertise). Additional technical skill definitions aligned to NICE Skill Statements are maintained in [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md).

### 5.3 CERG-Specific Knowledge

CERG-specific knowledge requirements for this role are defined in [OM-001 §6](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) (Canonical Role Roster) and [RAC-001 §7](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) (Role Descriptions). See §12 (Related CERG Documents) for the complete list of standards and procedures relevant to this role.

## 6. NICE TKS Statement References

The following Task, Knowledge, and Skill statements are extracted from the NIST NICE Framework v2.2.0 Work Role [DD-WRL-001 — Cryptography Engineer primary mapping] and filtered by relevance to this CERG role. The full TKS database is maintained at https://www.nist.gov/nice/framework/.

| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |
|---------------|-------------|-------------------|------------------------|
| Task | T0084 | Employ secure configuration management processes | Core work activity for this NICE Work Role |
| Task | T0542 | Translate proposed capabilities into technical requirements | Core work activity for this NICE Work Role |
| Task | T1010 | Communicate enterprise information technology architecture | Core work activity for this NICE Work Role |
| Task | T1019 | Determine special needs of cyber-physical systems | Core work activity for this NICE Work Role |
| Task | T1020 | Determine the operational and safety impacts of cybersecurity lapses | Core work activity for this NICE Work Role |
| Knowledge | K0698 | Knowledge of cryptographic key management principles and practices | Foundational knowledge for this role |
| Knowledge | K0876 | Knowledge of key management service (KMS) key rotation policies and procedures | Foundational knowledge for this role |
| Knowledge | K0694 | Knowledge of computer algorithm capabilities and applications | Foundational knowledge for this role |
| Knowledge | K0859 | Knowledge of encryption tools and techniques | Foundational knowledge for this role |
| Knowledge | K0874 | Knowledge of key management service (KMS) principles and practices | Foundational knowledge for this role |
| Skill | S0657 | Skill in implementing Public Key Infrastructure (PKI) encryption | Core capability for this role |
| Skill | S0658 | Skill in implementing digital signatures | Core capability for this role |
| Skill | S0141 | Skill in assessing security systems designs | Core capability for this role |
| Skill | S0172 | Skill in applying secure coding techniques | Core capability for this role |
| Skill | S0383 | Skill in analyzing an organization's enterprise information technology architecture | Core capability for this role |

> **Full TKS Reference:** The complete TKS statement set for the primary NICE Work Role (SP-ARC-001 → DD-WRL-001) is in the NICE Framework Components v2.2.0 dataset ([download](https://csrc.nist.gov/csrc/media/Projects/cprt/documents/nice/v2-2-0_nf_components.json)). JF-002 contains the complete CERG-to-NICE crosswalk with secondary role mappings.

## 7. Typical Qualifications

### 7.1 Education

- 5-15+ years in cybersecurity, with 3+ years focused on cryptography or PKI - Bachelor's degree in computer science, mathematics, or a related field - Relevant certifications: CISSP, CISM, vendor-specific HSM/KMS certifications, or equivalent

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
| **Document ID** | CERG-GOV-JD-SECENG-006 |
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
