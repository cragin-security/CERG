
# SURGE: Cyber Engineering, Risk & Governance

## CERG OPERATING MODEL
### Pillar Structure · Engagement Models · Staffing · Interaction Patterns

---

| | |
|---|---|
| **Document ID** | CERG-GOV-OM-001 |
| **Version** | 1.0 DRAFT |
| **Status** | For Review |
| **Classification** | Internal - Confidential |
| **Owner** | Chief Information Security Officer |
| **Parent Policy** | [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Organizational Change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · NIST RMF · ISO 27001 |
| **Audience** | All CERG personnel; business sponsors; IT and OT leadership; executive leadership |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Operating Premise](#2-operating-premise)
3. [The Three Pillars](#3-the-three-pillars)
4. [Authority, Reporting, and Decision Rights](#4-authority-reporting-and-decision-rights)
5. [Engagement Models](#5-engagement-models)
6. [Staffing and Roles](#6-staffing-and-roles)
7. [Coordination Cadence](#7-coordination-cadence)
8. [Interfaces With Other Functions](#8-interfaces-with-other-functions)
9. [RACI Patterns](#9-raci-patterns)
10. [Maturity, Metrics, and the Adaptive Target](#10-maturity-metrics-and-the-adaptive-target)
11. [Operating Model Control](#11-operating-model-control)

---

## 1. Purpose and Scope

This document describes the operating model for the Cyber Engineering, Risk, and Governance (CERG) function. It defines the three pillars, the authority and reporting structure, the engagement models through which CERG delivers value to the business, the staffing patterns that support those engagements, and the cadence by which CERG operates as one team rather than three silos.

This is not a policy. [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) is the policy. This document is the operating description that every CERG team member, business sponsor, and adjacent function partner can use to understand how the function works and how to engage it.

### 1.1 Scope

This document applies to:

- The CERG function itself, Engineering, Risk, and Governance pillars under CISO authority
- The interfaces between CERG and adjacent security functions (Awareness, Incident Response), IT and OT delivery teams, business owners, and executive leadership
- The engagement models by which CERG is consumed: project delivery, continuous service, advisory, and program oversight
- The staffing roles within each pillar and the rules of engagement among them

### 1.2 Relationship to Other Documents

This document is referenced by every CERG standard, procedure, and plan. Where another document assigns work to "Engineering," "Risk," or "Governance," this document defines what those terms operationally mean.

---

## 2. Operating Premise

### 2.1 Why CERG Exists

The traditional separation of cybersecurity into siloed functions, operational security here, GRC over there, engineering security as a third team, produces a predictable failure pattern. Engineering is asked to deliver, then security reviews it after the fact and asks for changes that are now expensive. Risk identifies findings that have no clear path back into engineering planning. Governance writes policy that operators interpret variously, or not at all. Audits and incidents reveal the seams.

CERG consolidates the three core security activities, building secure systems, managing exposure, and governing the program, into one function with one authority. The pillars are distinct in skill set and discipline, but they operate as one team with one CISO and one set of priorities.

### 2.2 The Yes-And Default

> **Governance Does Not Exist to Block the Business**
>
> CERG's default orientation is to enable the business with guardrails, not to close doors. When a risk cannot be eliminated, it is documented, owned, treated, and monitored, not refused on principle. Reflexive denial is not a risk management strategy. The hard work is making "yes" safe; "no" is the easy answer, and the wrong one.

### 2.3 Three Pillars, One Team

CERG operates as one team. The pillars provide structure for skill development, work intake, and accountability, not boundaries to hide behind. Cross-pillar collaboration is the norm. Every Engineering review involves Risk perspective. Every Risk finding has a Governance disposition. Every Governance policy is validated for operational practicability by Engineering and Risk before publication.

---

## 3. The Three Pillars

### 3.1 Cyber Engineering

**Mandate.** Build secure systems by design. Embed security into architecture, configuration, and operational baselines before production. Be the technical security partner to project delivery.

**Core activities.**

- Pre-production security architecture review for all in-scope projects
- Reference architectures, landing zones, and configuration baselines per platform class
- Security infrastructure-as-code, policy-as-code, and admission control
- IT/OT convergence advisory and Electronic Security Perimeter design
- Identity platform engineering (IdP, MFA, SSO, PAM, secrets management)
- Cryptography and key management platform engineering
- Endpoint, server, container, and cloud security tooling engineering
- Operational handoff documentation that supports Governance compliance evidence

**Engagement default.** Project-aligned engagement. Engineering is engaged early in project planning and follows the work through go-live.

### 3.2 Cyber Risk

**Mandate.** Maintain continuous visibility into organizational exposure. Drive the work that reduces it. Test that controls hold up under attack.

**Core activities.**

- Vulnerability management (scanning, prioritization, remediation tracking) per **[CERG-PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md)**
- Adversarial validation: penetration testing, red-team operations, purple-team detection validation
- Threat intelligence consumption and translation into detection and posture controls
- Vendor and third-party security risk assessment
- Cloud security posture management (CSPM) and SaaS security posture management (SSPM)
- Identity-threat detection and continuous identity-risk monitoring
- Risk-register intake from technical sources

**Engagement default.** Continuous service. Risk is always on; engagement is by exposure type, not by ticket.

### 3.3 Cyber Governance

**Mandate.** Own the policy library, the compliance posture, the risk register, and the evidence library. Translate regulation into actionable expectations. Coordinate regulator and auditor engagements.

**Core activities.**

- Policy, standards, and procedures library, including [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) and all subordinate documents
- Compliance program management: NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC, and customer-contractual frameworks
- Risk register operation per **[CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)**
- Evidence library curation; production of audit and assessment evidence
- Regulator and assessor liaison
- Awareness program coordination (program ownership rests with a separate Awareness function; Governance coordinates content alignment)
- Risk-register intake from policy, audit, and assessment sources
- Risk treatment data feeds into the standing Incident Response team (a separate function under CISO oversight - see §3.4)

**Engagement default.** Program oversight and advisory. Governance is engaged when policy interpretation, exception decisions, or regulatory implications enter the conversation.

### 3.4 What CERG Is Not Responsible For

The following functions are intentionally outside CERG and operate under separate charters:

- **Security Awareness program ownership.** A distinct function under CISO oversight, coordinated with Governance.
- **Incident Response operations and the IR plan itself.** A standing Incident Response team within Cybersecurity, reporting to the CISO, owns [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) and operates the IR capability. CERG feeds detection, vulnerability context, asset documentation, and post-incident risk-register entries into the IR team; CERG does not maintain the plan, run the exercises, or own the regulatory notification clocks. During an active incident, CERG pillars provide Lead Investigator, Engineering Lead, and Governance Lead roles per the IR team's call.
- **Physical Security (non-cyber).** Owned by Facilities; CERG coordinates for assets within CIP-006 / PE-family scope.
- **Privacy program.** A distinct function under Legal / Privacy leadership; coordinates with Governance for breach notification and Restricted-data handling.
- **Business Continuity (non-cyber).** Owned by Enterprise Risk / Operations; CERG coordinates for cyber-driven business continuity activations.

---

## 4. Authority, Reporting, and Decision Rights

### 4.1 Reporting Line

CERG reports to the CISO. The CISO reports per the organizational structure (typically to the CIO or directly to the CEO depending on org design) and has a defined reporting line to the board (Audit Committee, Risk Committee, or a dedicated Cyber/Technology Committee, per board protocol).

The three pillars report to the CISO through pillar leaders (Manager / Director / VP titles vary by organizational scale).

### 4.2 Decision Rights

| **Decision** | **Authority** |
|---|---|
| Policy approval ([CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) and subordinate standards) | CISO |
| Standards / procedure approval | Pillar leader; CISO for material changes |
| Risk acceptance - all severities | Per the canonical Risk Acceptance Authority table in [`CERG_Risk_Management_Framework_v1.0`](CERG_Risk_Management_Framework_v1.0.md) §9.7 |
| Exception approval | Per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) §8, which routes to RMF §9.7 for approval authority |
| Incident classification & containment | Incident Commander (CISO or designee), per the standing IR team (see §3.4) |
| External notification (regulator, public) | IC + CISO + Legal |
| Pre-production go/no-go for in-scope projects | Engineering pillar leader with Risk input; escalation to CISO if business and CERG disagree |
| Vendor onboarding approval (Tier 1) | Risk pillar leader; CISO for material risk exceptions |
| New SaaS / cloud service approval | Governance + Engineering; CISO for Restricted-data placements |
| Budget allocation across pillars | CISO |

### 4.3 Escalation Path

Disagreements that the pillars cannot resolve are escalated to the CISO. The CISO maintains a published escalation path that includes a stop-the-line capability for any CERG team member who believes a decision is being made that materially violates policy or creates regulatory exposure.

### 4.4 Cyber Oversight Group (COG)

The **Cyber Oversight Group (COG)** is the standing internal forum that reviews cyber risk posture between board cycles. It is chaired by the CISO. Members include the CIO, the COO or operational equivalent, the General Counsel, the Chief Financial Officer (or designee), the Enterprise Risk lead, and business-unit risk owners for systems in CERG scope. The COG meets monthly and serves three purposes:

1. **Posture review.** The CISO presents the open Risk Register summary, top KRIs from [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md), and any High or Critical risk acceptance decisions made since the last meeting.
2. **Cross-functional treatment alignment.** Risks whose treatment crosses business boundaries - e.g., a risk that requires Operations to change a maintenance practice, or Finance to fund a remediation - are surfaced for cross-functional decision or escalation.
3. **Pre-board review.** The COG serves as the dress rehearsal for board-cycle reporting; material risk decisions surface here first so the board reporting is informed by cross-functional perspective.

The COG is not a risk-acceptance authority. Acceptance authority lives in the [`CERG_RMF`](CERG_Risk_Management_Framework_v1.0.md) §9.7 table. The COG is the forum where the right decision-makers are in the room, informed, and aligned. Downstream reports - including the metrics dashboard in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §9 and the risk-register reporting cadence in [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) §7.3 - have the COG as their primary audience.

---

## 5. Engagement Models

CERG is consumed by the rest of the organization through four engagement models. Most major initiatives use more than one.

### 5.1 Project Engagement (Engineering-Led)

Used for new systems, major changes, and significant integrations.

| **Phase** | **CERG Activity** | **Lead Pillar** |
|---|---|---|
| Concept | Lightweight architectural consult; data classification and environment-tier discussion. | Engineering |
| Design | Formal security architecture review; reference-architecture / landing-zone selection; threat-model session for novel components. | Engineering (+ Risk for threat modeling) |
| Build | Engineering partner embedded with the project team; pipeline gates configured; identity / cryptography / monitoring requirements implemented. | Engineering |
| Pre-production | Pre-production security review; vulnerability assessment; pen-test where warranted; risk-register entries for any acceptance sought. | Engineering + Risk |
| Production | Handoff to operations; baselines committed; ongoing CSPM / SSPM coverage; vulnerability management onboarding. | Engineering → Risk |
| Continuous | Continuous monitoring; periodic re-review; governance evidence integration. | Risk + Governance |

### 5.2 Continuous Service (Risk-Led)

Used for ongoing exposure management across the entire estate.

- Vulnerability management operates as a standing service per [CERG-PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md).
- CSPM / SSPM operates continuously across approved cloud and SaaS.
- Threat intelligence consumption produces standing detection and posture work.
- Identity-threat detection operates continuously.

Continuous services do not require project tickets. Business teams are partners in remediation rather than initiators of the work.

### 5.3 Advisory (Cross-Pillar)

Used when a business unit, IT team, or OT team has a question, decision, or exploration that does not yet require a project.

- Architecture review office hours
- Cloud / SaaS service evaluation advisory
- M&A / divestiture cyber due diligence support
- Vendor selection advisory
- Policy interpretation advisory

Advisory engagements are intentionally low-friction. They are tracked at the activity level but not treated as a queued service.

### 5.4 Program Oversight (Governance-Led)

Used for regulatory programs, audits, exam cycles, and board reporting.

- NERC-CIP self-certification cycle and CIP-014 / CIP-013 program management
- [CMMC](https://dodcio.defense.gov/CMMC/) pre-assessment and assessment management
- [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC evidence cycle (quarterly)
- Internal audit coordination
- Customer / partner assessment response

Program oversight engagements are time-bounded with defined entry, milestone, and exit criteria. They are led by Governance with Engineering and Risk supplying evidence and SMEs.

---

## 6. Staffing and Roles

CERG staffing is intentionally consistent across the pillars: a pillar leader, senior practitioners with platform / domain ownership, individual contributors who execute the standing work, and rotations or shared roles where the pillars converge.

The structure below is a pattern, not a fixed org chart. Smaller organizations consolidate roles; larger organizations expand them.

### 6.1 Canonical Role Roster

This roster is the single source of truth for role names used throughout the CERG document library. When a standard, procedure, plan, or template refers to "the Risk Manager" or "the IR Plan Steward," it means the canonical name listed below. Documents that use a synonym (column 3) are calling the same role; the corrective action is to update the citing document to the canonical name on its next revision, not to invent a new role.

Roles are organized by pillar. Sub-role variants (e.g., Cyber Engineering Manager - Cloud vs. Cyber Engineering Manager - OT) are scaled out from the canonical name with a parenthetical domain qualifier.

| Canonical Role | Pillar / Group | Common Synonyms (Do Not Use) | Primary Responsibilities |
|---|---|---|---|
| **Chief Information Security Officer (CISO)** | Executive | - | Strategy, board reporting, final authority on High and Critical risk acceptance per [`CERG_RMF`](CERG_Risk_Management_Framework_v1.0.md) §9.7. |
| **Executive Sponsor** | Business / Executive | "VP," "Business Sponsor," "Leadership" | Concurrence for Critical risk acceptance per RMF §9.7; business representative on the COG; named per system in the categorization register. |
| **Engineering Pillar Leader** | Engineering | "Cyber Engineering Manager," "Engineering Manager" (when speaking of the pillar lead) | Pillar accountability; project intake; reference-architecture authority. |
| **Cloud Security Engineer** | Engineering | "Cyber Engineering - Cloud" | Cloud platforms, IaC, CSPM gating, landing-zone authority. |
| **Identity Engineer** | Engineering | "Cyber Engineering - Identity," "Cyber Engineering Manager (Identity)" | IdP, MFA, SSO, PAM, secrets management, federation. |
| **OT Security Engineer** | Engineering | "Cyber Engineering - OT," "OT/ICS Engineer" | IT/OT convergence, ESP/EAP design, BES Cyber System baselines. |
| **Application Security Engineer** | Engineering | "AppSec Engineer," "Product Security Engineer" | SAST/DAST, SDLC controls, threat modeling. |
| **Endpoint Engineer** | Engineering | "Workplace Engineer" | Endpoint, EDR, OS baselines. |
| **Cryptography Engineer** | Engineering | "Cyber Engineering - Platforms (Crypto)" | Key management, CA hierarchy, TLS posture, FIPS compliance. |
| **Pre-production Reviewer** | Engineering (rotated) | - | Owns the pre-production checklist; signs off on go-live readiness. |
| **Risk Pillar Leader** | Risk | "Cyber Risk Manager" (when speaking of the lead), "Risk Manager" | Pillar accountability; exposure posture reporting; Medium severity risk-acceptance authority per RMF §9.7. |
| **Vulnerability Management Lead** | Risk | "Cyber Risk Manager (Vulnerability Management)" | Operates [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md); owns SLAs and posture metrics. |
| **Adversarial Testing Lead** | Risk | "Cyber Risk Manager (Offensive Security)," "Red Team Lead" | Operates [`CERG-PRC-AV-001`](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md); pen test, red team, purple team. |
| **Threat Intelligence Analyst** | Risk | "Senior Risk Analyst - Threat Intelligence" | Threat-actor tracking; advisories; intel-to-detection translation. |
| **Vendor Risk Analyst** | Risk | "Cyber Risk Manager (Vendor Risk)," "TPRM Analyst" | Operates [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md); SCCT participation. |
| **OT Risk Analyst** | Risk | - | OT-safe vuln assessment, ICS threat intelligence. |
| **Identity Risk Analyst** | Risk | - | UEBA, identity-threat detection, OAuth and token risk. |
| **Detection Engineer** | Risk | "Risk - Detection Engineering," "Cloud Posture / Detection Engineer" | Detection-rule authoring; ATT&CK coverage; tuning lifecycle. |
| **Governance Pillar Leader** | Governance | "Cyber Governance Manager," "Governance Manager" (when speaking of the lead) | Pillar accountability; regulator and auditor liaison; CISO reporting; Low and Informational severity risk-acceptance authority per RMF §9.7. |
| **NERC-CIP Compliance Manager** | Governance | "Senior Governance Analyst - OT/NERC-CIP" | OT and BES Cyber System compliance posture. |
| **CMMC / Federal Compliance Manager** | Governance | "Governance / Compliance Analyst - Federal Programs" | CUI posture; SSP and POA&M maintenance. |
| **SOX ITGC Lead** | Governance | "Governance / Compliance Analyst - Commercial Frameworks (SOX)" | ITGC control evidence and audit coordination. |
| **Policy & Standards Manager** | Governance | "Governance / Compliance Analyst - Policy & QA" | Document library, version control, review cycles. |
| **Risk Register Owner** | Governance | "Risk Register Manager" | Operates [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md); curates the register; runs the Monthly Risk Register Review. |
| **Evidence Librarian** | Governance | - | Cross-framework evidence library curation. |
| **Incident Commander** | Adjacent (IR team) | "IC" | Single-decision authority during an active incident. |
| **Lead Investigator** | Adjacent (IR team) | - | Risk-side technical lead during an active incident. |

> **"CISO designee"**
>
> Several subordinate documents reference a "CISO designee" as an approval authority for tactical risk decisions. The CISO designee is whichever named pillar leader (Engineering, Risk, or Governance) the CISO has formally delegated to act on the CISO's behalf for a specific approval class. Designation is recorded in writing and reviewed at the CISO's discretion at least annually. Where a document needs to name a specific approver, use the canonical role name (e.g., "Risk Pillar Leader"); reserve "CISO designee" for cases where the delegation may rotate between pillars.

### 6.2 Cyber Engineering: Typical Roles

| **Role** | **Focus** |
|---|---|
| Engineering Pillar Leader | Pillar accountability; project intake; reference-architecture authority. |
| Cloud Security Engineer | Cloud platforms, landing zones, IaC, CSPM gating. |
| Identity Engineer | IdP, MFA, SSO, PAM, secrets management, federation. |
| OT Security Engineer | IT/OT convergence, ESP/EAP design, BES Cyber System baselines (see [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)). |
| Application / Product Security Engineer | SAST/DAST integration, SDLC controls, threat modeling. |
| Endpoint / Workplace Engineer | Endpoint controls, EDR engineering, OS baselines. |
| Cryptography Engineer | Key management, CA, TLS posture, FIPS compliance. |
| Pre-production Reviewer (often a rotated function) | Owns the pre-production checklist; signs off on go-live readiness. |

### 6.3 Cyber Risk: Typical Roles

| **Role** | **Focus** |
|---|---|
| Risk Pillar Leader | Pillar accountability; exposure posture reporting. |
| Vulnerability Management Lead | Operates [CERG-PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md); owns the SLAs and posture metrics. |
| Cloud Posture / Detection Engineer | CSPM / SSPM operations and detection rules. |
| Threat Intelligence Analyst | Source curation, internal advisories, detection translation. |
| Adversarial Testing Lead (Red Team) | Internal or partner-managed offensive validation. |
| Vendor / Third-Party Risk Analyst | Vendor assessment and continuous monitoring. |
| OT Risk Analyst | OT-safe vulnerability assessment; ICS threat intelligence. |
| Identity Risk Analyst | UEBA, identity-threat detection, OAuth / token risk. |

### 6.4 Cyber Governance: Typical Roles

| **Role** | **Focus** |
|---|---|
| Governance Pillar Leader | Pillar accountability; regulator and auditor liaison; CISO reporting. |
| NERC-CIP Compliance Manager | OT/BES compliance posture (see [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)). |
| [CMMC](https://dodcio.defense.gov/CMMC/) / Federal Compliance Manager | CUI posture (see [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md)). |
| [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC Lead | ITGC control evidence and audit coordination. |
| Policy & Standards Manager | Document library curation; review cycles. |
| Risk Register Manager | Operates [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md); curates the register. |
| Evidence Librarian | Maintains the cross-framework evidence library. |
| IR Plan Steward | Maintains [CERG-PLN-IR-001](CERG-PLN-IR-001_Incident_Response_Plan.md); coordinates exercises and notification clocks. |

### 6.5 Shared and Rotational Roles

Several roles intentionally sit between pillars and rotate:

- **Architecture Review Office Hours.** Engineering + Risk on rotation.
- **Incident Response on-call.** Risk-led with Engineering and Governance rotational coverage.
- **Audit liaison.** Governance-led with Engineering and Risk SMEs.

---

## 7. Coordination Cadence

CERG operates as one team because it talks like one team. The standing cadence below is the minimum; teams add working sessions as needed.

| **Forum** | **Cadence** | **Participants** | **Purpose** |
|---|---|---|---|
| CERG Leadership Sync | Weekly | CISO + pillar leaders | Cross-pillar priorities, blockers, escalations. |
| Risk Posture Review (High / Critical items) | Weekly | Risk + Engineering + Governance | Top-of-list High and Critical risks, treatment progress, SLA breaches. Aligns with [`CERG_RMF`](CERG_Risk_Management_Framework_v1.0.md) §8.2