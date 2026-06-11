| | |
|---|---|
| **Document ID** | CERG-GOV-JF-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [What a Job Family Is](#2-what-a-job-family-is)
3. [The Five CERG Job Families](#3-the-five-cerg-job-families)
4. [Family-to-Family Career Lattice](#4-family-to-family-career-lattice)
5. [Why Five Families Instead of Three](#5-why-five-families-instead-of-three)
6. [Job Levels Within Each Family](#6-job-levels-within-each-family)
7. [How Levels Interact With CERG's Grade Framework](#7-how-levels-interact-with-cergs-grade-framework)
8. [Level Progression Gates](#8-level-progression-gates)
9. [Per-Family Level Definitions](#9-per-family-level-definitions)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

This document establishes the formal Job Family structure for CERG's workforce architecture. It groups the 27 canonical CERG roles into five job families, defines career progression tiers within each family, and maps those tiers to CERG's existing grade framework (S1-S4 / M1-M4).

This document does NOT rename, add, or remove canonical roles. The authoritative role roster remains [OM-001 §6.1](CERG-GOV-OM-001_CERG_Operating_Model.md). Job families are a VIEW into the role architecture — a career-development and hiring lens — not a replacement for the operating model's pillar structure.

---

## 2. What a Job Family Is

A Job Family is a grouping of similar roles that share a core competency profile, career progression path, and broad functional purpose. Job families enable:

- **Career tracks.** A person can see: "I am in the Security Engineering family. From here I can progress to Advisor, Sr. Advisor, or laterally to the Risk Operations family."
- **Hiring clarity.** Requisitions are opened against a family, a level, and a specific role. HR and compensation can calibrate within and across families.
- **Training alignment.** Certification and training pathways are defined per family, not per role.

---

## 3. The Five CERG Job Families

| Family ID | Family Name | Description | CERG Roles (Canonical) | NICE Categories | Entry Grade | Terminal Grade |
|-----------|-------------|-------------|------------------------|-----------------|-------------|----------------|
| **JF-SECENG** | Security Engineering | Design and build secure systems, platforms, and infrastructure | Cloud Security Engineer, Identity Engineer, OT Security Engineer, Application Security Engineer, Endpoint Engineer, Cryptography Engineer | SP, OM | S1 | S4 |
| **JF-RISKOPS** | Risk Operations | Maintain continuous visibility into organizational exposure; test controls; drive remediation | Vulnerability Management Lead, Adversarial Testing Lead, Threat Intelligence Analyst, Detection Engineer, OT Risk Analyst, Identity Risk Analyst, Vendor Risk Analyst | PR, AN | S1 | S4/M3 |
| **JF-GOVCOMP** | Governance & Compliance | Own policy, compliance posture, risk register, and evidence; translate regulation into action | NERC-CIP Compliance Manager, CMMC/Federal Compliance Manager, SOX ITGC Lead, Policy & Standards Manager, Risk Register Owner, Evidence Librarian | OV | S1 | S4/M3 |
| **JF-EXEC** | Cybersecurity Executive Leadership | Set strategy, approve risk, report to board, lead the function | Chief Information Security Officer (CISO) | OV | Executive | Executive |
| **JF-ADJUNCT** | Incident Response & Investigation | Respond to and investigate cybersecurity incidents | Incident Commander, Lead Investigator | PR, IN | S2 | S4/M4 |

---

## 4. Family-to-Family Career Lattice

```
                    ┌──────────────────────────────────────┐
                    │         JF-EXEC (CISO)               │
                    │  Entry: Executive | Terminal: Exec    │
                    └──────────────────────────────────────┘
                                      ▲
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
┌─────────┴─────────┐     ┌──────────┴──────────┐     ┌──────────┴──────────┐
│  JF-SECENG        │     │   JF-RISKOPS         │     │   JF-GOVCOMP        │
│  Security Eng.    │◄───►│   Risk Operations    │◄───►│   Governance &       │
│  S1→S4            │     │   S1→S4/M3           │     │   Compliance        │
│                    │     │                      │     │   S1→S4/M3          │
└─────────┬─────────┘     └──────────┬───────────┘     └──────────┬──────────┘
          │                           │                           │
          └───────────────────────────┼───────────────────────────┘
                                      │
                          ┌───────────┴───────────┐
                          │   JF-ADJUNCT           │
                          │   Incident Response    │
                          │   S2→S4/M4             │
                          └───────────────────────┘
```

Left-right arrows (◄──►) indicate encouraged cross-family movement. Vertical arrows indicate progression toward executive leadership. CERG's existing "Left-Right Knowledge Model" ([FRM-001 §9.2](CERG-GOV-FRM-001_CERG_Framework.md)) and cross-training expectations ([OM-001 §10.4](CERG-GOV-OM-001_CERG_Operating_Model.md)) are the operational mechanisms that make this lattice real.

---

## 5. Why Five Families Instead of Three

The current three-pillar structure (Engineering, Risk, Governance) works well for the operating model but conflates functional grouping with career grouping:

- **Engineering Pillar** maps cleanly to JF-SECENG (one family = one pillar). No change needed.
- **Risk Pillar** contains two distinct functional families: JF-RISKOPS (vulnerability management, threat intel, detection — operations work) and adjacent roles that are more incident-response-oriented (JF-ADJUNCT). The current structure puts Detection Engineer and Threat Intelligence Analyst in the same pillar as Vendor Risk Analyst, but their day-to-day work, certifications, and career paths differ significantly. This proposal keeps them in the same pillar operationally but gives them distinct family designations for career development.
- **Governance Pillar** maps cleanly to JF-GOVCOMP (one family = one pillar). No change needed.

The distinction between JF-RISKOPS and JF-ADJUNCT is important: Incident Commander and Lead Investigator are NOT CERG roles (they belong to the standing IR team per OM-001 §3.4). They appear in CERG documents only for cross-functional clarity. Giving them their own family makes this boundary explicit in the career architecture.

---

## 6. Job Levels Within Each Family

Each Job Family has 4 tiers that map directly to CERG's existing SME grade structure (S1-S4) and Management grade structure (M1-M4). This section defines what each tier means WITHIN each family — providing family-specific expectations that a hiring manager and a team member can reference without consulting multiple documents.

See Section 9 for per-family level definition tables.

---

## 7. How Levels Interact With CERG's Grade Framework

The Job Family levels (L1-L4) are a VIEW into the grade framework, not a replacement for it. Think of them as:

- **CERG Grades (S1-S4, M1-M4)** = the internal calibration standard used by HR, compensation, and promotion panels. These are precise, defined in [JA-001](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md), and carry compensation bands.
- **Job Family Levels (L1-L4)** = the external-facing and career-development language. These appear in job postings, career conversations, and succession plans.

The mapping is:

```
Job Family Level  |  SME Track Grade  |  Management Track Grade
L1               |  S1               |  N/A
L2               |  S2               |  N/A
L3               |  S3               |  M1-M2
L4               |  S4               |  M3-M4
```

An "L3 Security Engineer" could be an S3 Advisor (SME track) or an M1 Manager (Management track). The external title is the same; the internal grade reflects whether their primary contribution is through individual expertise or people leadership.

---

## 8. Level Progression Gates

Progression from one level to the next requires demonstration of capabilities. The gates below define what a promotion case must show. These supplement (not replace) the JA-001 grade definitions and [CMP-001](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) behavioral anchors.

### 8.1 L1 → L2 Gate (All Families)

- Has completed at least one full cycle of the family's core process (e.g., for JF-SECENG: a project from intake to go-live; for JF-GOVCOMP: a compliance cycle from preparation to audit close)
- No longer needs direction on daily work
- Has identified and corrected at least one process gap or documentation error
- Peer feedback confirms reliability

### 8.2 L2 → L3 Gate (All Families)

- Has led at least one cross-pillar initiative or authored/revised a standard or procedure
- Has formally mentored at least one L1 or L2 team member (documented in [PERF-001](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md))
- Has represented the pillar in at least two cross-functional forums or engagements
- Manager confirms self-direction against objectives

### 8.3 L3 → L4 Gate (All Families)

- Has contributed to CISO-level decisions (documented: strategy input, risk assessment, budget recommendation)
- Has mentored across pillars, not just within the home pillar
- Has represented the organization externally (conference, regulatory forum, industry working group, publication)
- Peer pillar leaders confirm cross-organizational influence
- For JF-SECENG specifically: has authored at least one standard or reference architecture adopted organization-wide
- For JF-RISKOPS specifically: has led an organization-wide risk posture assessment
- For JF-GOVCOMP specifically: has represented the organization to an external auditor or regulator without supervision

---

## 9. Per-Family Level Definitions

### 9.1 JF-SECENG — Security Engineering Levels

| Tier | CERG Grade(s) | Title Suffix | Scope | Autonomy | Influence | Key Differentiator |
|------|--------------|--------------|-------|----------|-----------|-------------------|
| **L1: Associate Engineer** | S1 | "Associate" or "I" | Single domain, defined tasks | Requires direction on approach | Immediate team | Follows engineering procedures |
| **L2: Engineer** | S2 | (no suffix) or "II" | Primary domain + awareness of adjacencies | Independent day-to-day | Recognized within pillar | Owns engineering work streams end-to-end |
| **L3: Senior Engineer** | S3 | "Senior" or "Staff" | Cross-pillar awareness; shapes engineering approach | Self-directed against objectives | Trusted by pillar leaders | Authors standards and leads engineering initiatives |
| **L4: Principal Engineer** | S4 | "Principal" or "Distinguished" | Organization-wide; sets engineering agenda | Defines what problems matter | Influences CISO-level decisions | Sets the technical bar for the entire pillar |
| **Engineering Manager** | M1-M3 | "Manager," "Senior Manager" | Team/function/pillar-segment | Translates goals into plans | Team and cross-team | Delivers through others; develops engineers |
| **Director of Engineering** | M4 | "Director" | Full Engineering pillar | Sets multi-year direction | CISO, board, regulators | Pillar leader accountability |

### 9.2 JF-RISKOPS — Risk Operations Levels

| Tier | CERG Grade(s) | Title Suffix | Scope | Key Differentiator |
|------|--------------|--------------|-------|-------------------|
| **L1: Associate Analyst** | S1 | "Associate" or "I" | Single risk domain (e.g., vulnerability scanning, basic threat feed triage) | Follows risk procedures |
| **L2: Analyst** | S2 | (no suffix) or "II" | Primary domain; owns a risk work stream | Independently operates risk processes |
| **L3: Senior Analyst** | S3 | "Senior" or "Lead" | Cross-pillar; shapes risk assessment approach | Authors risk procedures; mentors analysts |
| **L4: Principal Analyst** | S4 | "Principal" or "Distinguished" | Organization-wide risk posture | Influences CISO risk decisions |
| **Risk Operations Manager** | M1-M3 | "Manager," "Senior Manager" | Team/function within Risk | Leads risk operations teams |

### 9.3 JF-GOVCOMP — Governance & Compliance Levels

| Tier | CERG Grade(s) | Title Suffix | Scope | Key Differentiator |
|------|--------------|--------------|-------|-------------------|
| **L1: Associate** | S1 | "Associate" or "I" | Single compliance domain (e.g., evidence collection for one framework) | Follows governance procedures |
| **L2: Specialist** | S2 | (no suffix) or "II" | Owns a compliance work stream (e.g., one regulatory framework) | Independently manages compliance activities |
| **L3: Senior Specialist** | S3 | "Senior" or "Lead" | Cross-framework; shapes compliance approach | Authors compliance procedures; represents org to auditors |
| **L4: Principal Specialist** | S4 | "Principal" or "Distinguished" | Organization-wide governance | Influences regulatory strategy; trusted by CISO |
| **Governance Manager** | M1-M3 | "Manager," "Senior Manager" | Team/function within Governance | Leads compliance teams |
| **Director of Governance** | M4 | "Director" | Full Governance pillar | Pillar leader accountability |

### 9.4 JF-EXEC — Executive Leadership Levels

| Tier | Grade | Title | Scope | Key Differentiator |
|------|-------|-------|-------|-------------------|
| **L1: CISO** | Executive | Chief Information Security Officer | Full cybersecurity program | See [JD-001 §3.1](CERG-GOV-JD-001_CERG_Job_Descriptions.md) for full description |

### 9.5 JF-ADJUNCT — Incident Response Levels

| Tier | CERG Grade | Title | Scope | Key Differentiator |
|------|-----------|-------|-------|-------------------|
| **L2: Investigator** | S2 | "Investigator" or "Responder" | Executes IR procedures under IC direction | Operates during incidents |
| **L3: Senior Investigator** | S3 | "Senior Investigator" | Leads investigation workstreams | Technical lead during incidents |
| **L4: Incident Commander** | S4/M4 | "Incident Commander" | Single-decision authority during active incidents | Highest IR authority per incident |

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-JF-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | Pending |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Established five CERG Job Families, four-tier level structure, progression gates, and mapping to existing grade framework. |

### Review Triggers

- Addition or retirement of a canonical role in OM-001 §6.1
- Change to the NICE Workforce Framework affecting CERG role mappings
- Revision to JA-001 grade definitions
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster |
| Consolidated Roles and RACI | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Role descriptions and RACI assignments |
| Job Architecture | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade definitions |
| NICE Crosswalk | [`CERG-GOV-JF-002`](roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE mapping for each role |
