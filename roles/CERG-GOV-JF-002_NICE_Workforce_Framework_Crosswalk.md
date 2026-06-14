| | |
|---|---|
| **Document ID** | CERG-GOV-JF-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; or upon NICE framework update |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Mapping Methodology](#2-mapping-methodology)
3. [JF-SECENG — Security Engineering NICE Mapping](#3-jf-seceng--security-engineering-nice-mapping)
4. [JF-RISKOPS — Risk Operations NICE Mapping](#4-jf-riskops--risk-operations-nice-mapping)
5. [JF-GOVCOMP — Governance & Compliance NICE Mapping](#5-jf-govcomp--governance--compliance-nice-mapping)
6. [JF-EXEC — Executive Leadership NICE Mapping](#6-jf-exec--executive-leadership-nice-mapping)
7. [JF-ADJUNCT — Incident Response NICE Mapping](#7-jf-adjunct--incident-response-nice-mapping)
8. [Complete Crosswalk Table](#8-complete-crosswalk-table)
9. [NICE Work Role Categories Reference](#9-nice-work-role-categories-reference)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

This document provides the complete mapping of all 27 canonical CERG roles to NIST NICE Work Roles (NIST SP 800-181r1). It is the authoritative crosswalk for CERG's workforce architecture, enabling:

- **Hiring precision.** Job postings can reference NICE work roles so candidates from other industries understand the role immediately.
- **Regulatory alignment.** NERC-CIP, CMMC, and DoD 8140.03 all reference NICE; CERG compliance managers benefit from a shared taxonomy with their regulators.
- **Skills-gap analysis.** Mapping CERG roles to NICE TKS statements enables systematic identification of team-wide skill gaps.
- **Career portability.** Team members who understand their NICE mapping can pursue external certifications and career paths aligned to recognized standards.

---

## 2. Mapping Methodology

Each CERG canonical role is mapped to 1–3 NICE Work Roles. The mapping follows these rules:

1. **Primary NICE Work Role** = the single NICE role that most closely describes the CERG role's core accountability. If a job posting references only one NICE code, use this one.
2. **Secondary NICE Work Role(s)** = NICE roles that describe significant portions of the CERG role's work. Useful for skills-gap analysis.
3. **NICE Work Role Category** = the high-level category the primary role belongs to. Used for job family alignment.

**Note on NICE Work Role IDs:** The IDs below use a simplified format (e.g., `SP-ARC-001`) for readability. Actual NIST SP 800-181r1 Work Role IDs should be verified against the authoritative source at https://niccs.cisa.gov/tools/nice-framework.

---

## 3. JF-SECENG — Security Engineering NICE Mapping

| CERG Canonical Role | Primary NICE Work Role | Primary NICE Code | Secondary NICE Work Role(s) | NICE Category |
|---------------------|----------------------|-------------------|-----------------------------|--------------|
| **Cloud Security Engineer** | Security Architect | SP-ARC-001 | Systems Security Analyst (OM-ANA-001), Enterprise Architect (SP-ARC-002) | SP |
| **Identity Engineer** | Systems Security Analyst | OM-ANA-001 | Security Architect (SP-ARC-001) | OM / SP |
| **OT Security Engineer** | Security Architect | SP-ARC-001 | Systems Security Analyst (OM-ANA-001), Network Operations Specialist (OM-NET-001) | SP |
| **Application Security Engineer** | Secure Software Assessor | SP-DEV-001 | Software Developer (SP-DEV-002), Vulnerability Assessment Analyst (PR-VAM-001) | SP |
| **Endpoint Engineer** | Systems Security Analyst | OM-ANA-001 | Cyber Defense Infrastructure Support (PR-INF-001) | OM |
| **Cryptography Engineer** | Security Architect | SP-ARC-001 | Systems Security Analyst (OM-ANA-001) | SP |

---

## 4. JF-RISKOPS — Risk Operations NICE Mapping

| CERG Canonical Role | Primary NICE Work Role | Primary NICE Code | Secondary NICE Work Role(s) | NICE Category |
|---------------------|----------------------|-------------------|-----------------------------|--------------|
| **Exposure Management Lead** | Vulnerability Assessment Analyst | PR-VAM-001 | Cyber Defense Analyst (PR-CDA-001), Security Control Assessor (OV-SCA-001) | PR |
| **Adversarial Testing Lead** | Vulnerability Assessment Analyst | PR-VAM-001 | (limited CO overlap) | PR |
| **Threat Intelligence Analyst** | Threat/Warning Analyst | AN-TWA-001 | All-Source Analyst (AN-ASA-001), Cyber Intelligence Planner (CO-CIP-001) | AN |
| **Detection Engineer** | Cyber Defense Analyst | PR-CDA-001 | Systems Security Analyst (OM-ANA-001), Threat/Warning Analyst (AN-TWA-001) | PR |
| **OT Risk Analyst** | Threat/Warning Analyst | AN-TWA-001 | Vulnerability Assessment Analyst (PR-VAM-001) | AN |
| **Identity Risk Analyst** | Cyber Defense Analyst | PR-CDA-001 | Systems Security Analyst (OM-ANA-001) | PR |
| **Vendor Risk Analyst** | Security Control Assessor | OV-SCA-001 | Threat/Warning Analyst (AN-TWA-001) | OV |

---

## 5. JF-GOVCOMP — Governance & Compliance NICE Mapping

| CERG Canonical Role | Primary NICE Work Role | Primary NICE Code | Secondary NICE Work Role(s) | NICE Category |
|---------------------|----------------------|-------------------|-----------------------------|--------------|
| **NERC-CIP Compliance Manager** | Security Control Assessor | OV-SCA-001 | Systems Authorization (OV-SAA-001), Cyber Policy and Strategy Planner (OV-PSP-001) | OV |
| **CMMC / Federal Compliance Manager** | Security Control Assessor | OV-SCA-001 | Systems Authorization (OV-SAA-001), Cyber Policy and Strategy Planner (OV-PSP-001) | OV |
| **SOX ITGC Lead** | Security Control Assessor | OV-SCA-001 | IT Program Auditor (OV-PMA-001) | OV |
| **Policy & Standards Manager** | Cyber Policy and Strategy Planner | OV-PSP-001 | Cyber Workforce Developer and Manager (OV-WDM-001), Information Systems Security Manager (OV-ISSN-001) | OV |
| **Risk Register Owner** | Information Systems Security Manager | OV-ISSN-001 | Security Control Assessor (OV-SCA-001) | OV |
| **Evidence Librarian** | Security Control Assessor | OV-SCA-001 | Knowledge Manager (OM-KMG-001) | OV |

---

## 6. JF-EXEC — Executive Leadership NICE Mapping

| CERG Canonical Role | Primary NICE Work Role | Primary NICE Code | NICE Category |
|---------------------|----------------------|-------------------|---------------|
| **Chief Information Security Officer (CISO)** | Executive Cyber Leader | OG-WRL-001 | OV |
| **Executive Sponsor** | (Business-side role; not mapped to NICE) | N/A | N/A |

---

## 7. JF-ADJUNCT — Incident Response NICE Mapping

| CERG Canonical Role | Primary NICE Work Role | Primary NICE Code | NICE Category | Notes |
|---------------------|----------------------|-------------------|---------------|-------|
| **Incident Commander** | Cyber Defense Incident Responder | PR-CIR-001 | PR | Not a CERG role per OM-001 §3.4; mapped for cross-reference |
| **Lead Investigator** | Cyber Defense Incident Responder | PR-CIR-001 | PR | Not a CERG role per OM-001 §3.4; mapped for cross-reference |

---

## 8. Complete Crosswalk Table

This table provides the complete mapping of all 27 canonical CERG roles plus the three Pillar Leaders to NICE Work Roles. It is the single-source reference for NICE alignment.

| CERG Canonical Role | Job Family | CERG Pillar | Primary NICE Work Role | NICE Category | Secondary NICE Work Role(s) | NICE Work Role ID (Primary) |
|---------------------|-----------|-------------|----------------------|---------------|-----------------------------|----------------------------|
| Chief Information Security Officer (CISO) | JF-EXEC | Executive | Executive Cyber Leader | OV | — | OG-WRL-001 |
| Executive Sponsor | JF-EXEC | Business/Executive | (Business role; N/A) | — | — | — |
| Engineering Pillar Leader | JF-SECENG | Engineering | Executive Cyber Leader / Security Architect | OV / SP | — | OG-WRL-001 / SP-ARC-001 |
| Cloud Security Engineer | JF-SECENG | Engineering | Security Architect | SP | Systems Security Analyst | SP-ARC-001 |
| Identity Engineer | JF-SECENG | Engineering | Systems Security Analyst | OM | Security Architect | OM-ANA-001 |
| OT Security Engineer | JF-SECENG | Engineering | Security Architect | SP | Systems Security Analyst | SP-ARC-001 |
| Application Security Engineer | JF-SECENG | Engineering | Secure Software Assessor | SP | Software Developer | SP-DEV-001 |
| Endpoint Engineer | JF-SECENG | Engineering | Systems Security Analyst | OM | Cyber Defense Infrastructure Support | OM-ANA-001 |
| Cryptography Engineer | JF-SECENG | Engineering | Security Architect | SP | Systems Security Analyst | SP-ARC-001 |
| Pre-production Reviewer | JF-SECENG | Engineering | Security Control Assessor | OV | Systems Security Analyst | OV-SCA-001 |
| Risk Pillar Leader | JF-RISKOPS | Risk | Executive Cyber Leader / Vulnerability Assessment Analyst | OV / PR | — | OG-WRL-001 / PR-VAM-001 |
| Exposure Management Lead | JF-RISKOPS | Risk | Vulnerability Assessment Analyst | PR | Cyber Defense Analyst | PR-VAM-001 |
| Adversarial Testing Lead | JF-RISKOPS | Risk | Vulnerability Assessment Analyst | PR | (limited CO overlap) | PR-VAM-001 |
| Threat Intelligence Analyst | JF-RISKOPS | Risk | Threat/Warning Analyst | AN | All-Source Analyst | AN-TWA-001 |
| Detection Engineer | JF-RISKOPS | Risk | Cyber Defense Analyst | PR | Systems Security Analyst | PR-CDA-001 |
| OT Risk Analyst | JF-RISKOPS | Risk | Threat/Warning Analyst | AN | Vulnerability Assessment Analyst | AN-TWA-001 |
| Identity Risk Analyst | JF-RISKOPS | Risk | Cyber Defense Analyst | PR | Systems Security Analyst | PR-CDA-001 |
| Vendor Risk Analyst | JF-RISKOPS | Risk | Security Control Assessor | OV | Threat/Warning Analyst | OV-SCA-001 |
| Governance Pillar Leader | JF-GOVCOMP | Governance | Executive Cyber Leader / Security Control Assessor | OV | — | OG-WRL-001 / OV-SCA-001 |
| NERC-CIP Compliance Manager | JF-GOVCOMP | Governance | Security Control Assessor | OV | Systems Authorization | OV-SCA-001 |
| CMMC / Federal Compliance Manager | JF-GOVCOMP | Governance | Security Control Assessor | OV | Systems Authorization | OV-SCA-001 |
| SOX ITGC Lead | JF-GOVCOMP | Governance | Security Control Assessor | OV | IT Program Auditor | OV-SCA-001 |
| Policy & Standards Manager | JF-GOVCOMP | Governance | Cyber Policy and Strategy Planner | OV | Cyber Workforce Developer and Manager | OV-PSP-001 |
| Risk Register Owner | JF-GOVCOMP | Governance | Information Systems Security Manager | OV | Security Control Assessor | OV-ISSN-001 |
| Evidence Librarian | JF-GOVCOMP | Governance | Security Control Assessor | OV | Knowledge Manager | OV-SCA-001 |
| Incident Commander | JF-ADJUNCT | Adjacent (IR) | Cyber Defense Incident Responder | PR | — | PR-CIR-001 |
| Lead Investigator | JF-ADJUNCT | Adjacent (IR) | Cyber Defense Incident Responder | PR | Cyber Crime Investigator | PR-CIR-001 |

---

## 9. NICE Work Role Categories Reference

The seven NICE Work Role Categories (NIST SP 800-181r1) with their official descriptions:

| Category Code | Category Name | Official NICE Description |
|---------------|---------------|---------------------------|
| **SP** | Securely Provision | Conceptualizes, designs, procures, and/or builds secure information technology (IT) systems, with responsibility for aspects of system and/or network development. |
| **OM** | Operate and Maintain | Provides the support, administration, and maintenance necessary to ensure effective and efficient information technology (IT) system performance and security. |
| **OV** | Oversee and Govern | Provides leadership, management, direction, or development and advocacy so the organization may effectively conduct cybersecurity work. |
| **PR** | Protect and Defend | Identifies, analyzes, and mitigates threats to internal information technology (IT) systems and/or networks. |
| **AN** | Analyze | Performs highly-specialized review and evaluation of incoming cybersecurity information to determine its usefulness for intelligence. |
| **CO** | Collect and Operate | Provides specialized denial and deception operations and collection of cybersecurity information that may be used to develop intelligence. |
| **IN** | Investigate | Investigates cybersecurity events or crimes related to information technology (IT) systems, networks, and digital evidence. |

**Reference:** NIST SP 800-181r1, Workforce Framework for Cybersecurity (NICE Framework). Available at https://www.nist.gov/itl/applied-cybersecurity/nice

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-JF-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; or upon NICE framework update |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Complete NICE-to-CERG crosswalk for all 27 canonical roles, plus Pillar Leaders. Includes NICE Work Role Categories reference. |

### Review Triggers

- Update to NIST SP 800-181r1 (NICE Framework)
- Addition or retirement of a canonical role in OM-001 §6.1
- Change in NICE Work Role codes or categories
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Job Families Overview | [`CERG-GOV-JF-001`](CERG-GOV-JF-001_Job_Families_Overview.md) | Job family structure and level definitions |
| CERG Operating Model | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster |
| Competency Model | [`CERG-GOV-CMP-001`](../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Competency-to-NICE crosswalk |
