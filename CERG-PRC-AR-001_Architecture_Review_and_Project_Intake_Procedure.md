# SURGE: Cyber Engineering, Risk & Governance

## ARCHITECTURE REVIEW AND PROJECT INTAKE PROCEDURE
### Intake · Review · Threat Model · Pre-Production · Handoff · Go-Live Risk Acceptance

---

| | |
|---|---|
| **Document ID** | CERG-PRC-AR-001 |
| **Version** | 1.0 |
| **Status** | Published |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-LM-001](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-RES-001](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Review Cycle** | Annual / On platform or process change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (PL, SA, SC) · NIST 800-160 · NIST SSDF · CSA STAR |
| **Regulations** | [CMMC L2](https://dodcio.defense.gov/CMMC/) · NERC-CIP CIP-005/CIP-010 · SOX ITGC (Change) |
| **Environments** | All in-scope projects - IT, cloud, SaaS, OT, hybrid |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Roles and Responsibilities](#2-roles-and-responsibilities)
3. [The Five-Phase Engagement Model](#3-the-five-phase-engagement-model)
4. [Who Needs a Review, and Who Doesn't](#4-who-needs-a-review--and-who-doesnt)
5. [Phase 1, Intake](#5-phase-1--intake)
6. [Phase 2, Architecture Review and Threat Model](#6-phase-2--architecture-review-and-threat-model)
7. [Phase 3, Build-Time Engagement](#7-phase-3--build-time-engagement)
8. [Phase 4, Pre-Production Security Review](#8-phase-4--pre-production-security-review)
9. [Phase 5, Production Handoff and Go-Live](#9-phase-5--production-handoff-and-go-live)
10. [Required Diagrams](#10-required-diagrams)
11. [Templates](#11-templates)
12. [Metrics](#12-metrics)
14. [Regulatory and Framework Alignment Summary](#14-regulatory-and-framework-alignment-summary)
15. [Document Control](#15-document-control)

---

## 1. Purpose and Scope

The Operating Model makes Engineering project engagement a core CERG delivery model. The RMF Phase 3 describes concept, design, build, pre-production, and production handoff outputs. Until this procedure, the intake forms, review checklists, threat modeling guidance, signoff criteria, and handoff packages those phases require existed implicitly.

This procedure defines how a project enters CERG attention, how Engineering reviews it, how Risk threat-models it, how findings flow to remediation or risk acceptance, and how the system enters production with the right documentation, baselines, monitoring, and accepted exceptions.

> **Engineering's Job Is to Be in the Room Early**
>
> Architecture review is not a gate that bolts security onto a project at the end. It is the discipline of having Engineering in the design conversation early enough to change the design cheaply. A review that consistently surfaces "we have to redo the data flow now" is a review that came too late.

---

## 2. Roles and Responsibilities

| **Role** | **Responsibility** |
|---|---|
| **Project Sponsor / Business Owner** | Submits intake. Owns the project's residual risk. Approves go-live decisions for their scope. |
| **Project / Technical Lead** | Produces the architecture artifacts and answers reviewer questions. Drives remediation between reviews. |
| **CERG - Pre-production Reviewer** | Conducts the review. Maintains review record. Determines findings. Recommends handoff disposition. |
| **Application Security Engineer** | Performs threat modeling. Performs vendor risk per [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) if third parties are involved. Adds findings to the risk register. |
| **Governance Pillar Leader** | Maps the project into the regulatory scope (CUI / BES / SOX) and triggers the relevant overlay reviewers. |
| **Engineering Pillar Leader** | Approves Standard findings. Approves Medium risk acceptances per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) §8. |
| **CISO** | Approves High / Critical risk acceptances at go-live. |
| **IT Change Advisory Board (CAB)** | Hosts the go-live conversation; CERG review status is a CAB input, not a substitute for change management. |

---

## 3. The Five-Phase Engagement Model

CERG engagement with a project follows five phases. Not every project hits every phase, Section 4 names the carve-outs.

1. **Intake**, register the project; classify scope; determine review depth.
2. **Architecture Review and Threat Model**, design-stage review; threats and controls aligned to [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md).
3. **Build-Time Engagement**, secure SDLC checks, IaC review, baseline conformance.
4. **Pre-Production Security Review**, readiness against the review findings, baselines, monitoring, and recovery.
5. **Production Handoff and Go-Live**, handoff package complete, risk acceptances approved, asset added to inventory and recurring controls.

---

## 4. Who Needs a Review: and Who Doesn't

Reviewing every Power App or low-code workflow is how Engineering loses a quarter to busywork. Waving them all through is how Shadow IT eats the enterprise. CERG's answer is: **review the platform once, then trust the guardrails the platform enforces.**

### 4.1 Mandatory Review

CERG Architecture Review is mandatory for projects that meet any of the following:

- Introduces a new IaaS / PaaS / cloud account, subscription, or project.
- Introduces a new SaaS service (any tier) handling business data.
- Touches OT / BES Cyber Systems or the IT/OT boundary (per [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)).
- Handles CUI (storage, processing, transmission) or changes the CUI boundary.
- Handles SOX-relevant financial data or process flows.
- Introduces or changes a third-party network connection.
- Modifies the production identity provider, federation, or PAM topology.
- Introduces a new authentication path to a system holding Restricted data.
- Crosses a trust boundary (network, identity, tenant, region, organization).
- Introduces a new data classification or regulatory scope into the environment.

### 4.2 Lightweight Review (Engineering Self-Service)

A lightweight, self-service review pattern (intake form + checklist + Engineering sign-off without full Phase 2) is acceptable for projects that:

- Reuse an already-reviewed pattern (e.g., new microservice on an already-reviewed Kubernetes cluster).
- Add capacity to an already-reviewed system.
- Use a pre-approved IaC module or service catalog template.

### 4.3 Citizen-Development Carve-Out

Citizen-development platforms (Power Platform, low-code app builders, business-managed automation) are not reviewed *per app*. They are reviewed once, at platform onboarding, with the assessment focused on the platform's guardrails, then trusted to police the apps that run on it.

| **Citizen-Dev Platform Assessment** | **Required at Platform Onboarding** |
|---|---|
| Identity and access | SSO + MFA + role-based admin model + audit log to SIEM |
| Data egress | Data Loss Prevention policy on connectors; sensitive connectors restricted |
| Data classification awareness | Sensitivity labels surfaced to citizen developers; export restrictions enforced |
| External sharing | Disabled by default; named exception path |
| Lifecycle | App lifecycle policy: ownership required, dormant apps culled, transfer-on-departure |
| Telemetry | Audit log forwarded to SIEM; admin actions monitored |
| Detection set | Day-one detections per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

Apps built on the platform are governed by these guardrails. Where an app needs to step outside the guardrails (e.g., a new connector, an unusual data classification), it triggers Mandatory Review per Section 4.1.

> **The Test**
>
> If a citizen-development app cannot do anything outside the platform's guardrails, CERG does not need to review it. If a platform's guardrails are weaker than CERG's standards, the platform is unsuitable for the data classification it's hosting. Apps get reviewed only when they need to step outside the boundary.

### 4.4 What Does Not Need CERG Review

- Pure UX or visual changes to an existing system that don't touch authentication, data classification, scope, or interfaces.
- Routine patching covered by [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md).
- Routine configuration changes within the DISH-conformant pattern that don't change trust boundaries.

---

## 5. Phase 1: Intake

Intake is fast (< 5 business days) and produces a Scope Determination that drives every subsequent phase.

### 5.1 Security Project Intake Form (Template)

```
SECURITY PROJECT INTAKE - AR-YYYY-NNNN

A. PROJECT IDENTITY
   Project Name             :
   Sponsor (named role)     :
   Technical Lead           :
   Business Outcome         :
   Target Production Date   :

B. SCOPE
   Data Classifications Handled : Public / Internal / Restricted / CUI / BCSI
   Regulatory Scope             : None / CUI / BES / SOX (multi-select)
   Operating Units Impacted     :
   Environments                 : IT / Cloud / SaaS / OT / Hybrid
   Geographies                  : (countries; flag non-US access)
   Trust Boundaries Crossed     : (network / identity / tenant / org)

C. TECHNOLOGY
   New SaaS introduced?         : Y/N - name(s) - vendor(s)
   New cloud account/sub/proj?  : Y/N
   New OT touch / IT/OT bridge? : Y/N
   New external connection?     : Y/N
   New identity / federation?   : Y/N

D. THIRD PARTIES
   Vendors involved             : list
   Vendor tier (per TPRM)       :
   International access?        : Y/N - countries

E. CHANGE CONTEXT
   New build / migrate / retire / extend
   Existing CERG-tracked asset IDs (if extension)

F. INITIAL SECURITY CONCERNS (from project team)
   What worries us most         :
   What we know is unresolved   :

G. ASKS
   What CERG help do we need at design stage?
```

### 5.2 Scope Determination Output

The Intake reviewer (CERG Engineering) determines:

- Review path: **Mandatory** (Phase 2 full), **Lightweight** (self-service checklist), or **Out of Scope**.
- Overlay reviewers required: CUI, BES, SOX, OT, each named by [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md).
- Threat modeling required: Y/N (default Y for Mandatory; conditional for Lightweight).
- TPRM engagement required: Y/N (default Y if any vendor is new or tier > business default).
- Estimated Phase 2–5 effort and target dates.

A Scope Determination is recorded against the project and visible to the team within five business days.

---

## 6. Phase 2: Architecture Review and Threat Model

### 6.1 Architecture Review Checklist

The reviewer works through the checklist below; findings are recorded with severity and routed per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

| **Area** | **Review Item** | **Standard Reference** |
|---|---|---|
| Identity | SSO + MFA + role model + JIT for privileged + service account pattern | STD-AC-001 |
| Authorization | Least privilege; SoD where applicable; tenant / record / field scoping | STD-AC-001 / GOV-CB-001 AC-5 |
| Data classification | Classification recorded; controls match classification | STD-CUI-001 / STD-IT-001 |
| Cryptography | Algorithms approved; CMK where required; secrets pattern; FIPS where applicable | STD-CR-001 |
| Network | Segmentation; default deny; logging; trust boundaries marked | STD-IT-001 / STD-OT-001 |
| Configuration | DISH tier; baseline applied; drift detection | STD-CFG-001 |
| Logging | Mandatory sources onboarded; retention; immutability | STD-LM-001 |
| Detection | Day-one detection set committed for environment | STD-LM-001 |
| Vulnerability mgmt | Authenticated scanning in scope; SLA targets agreed | PRC-VM-001 |
| Resilience | RTO/RPO tier; backup; restoration test plan | STD-RES-001 |
| Third party | Vendor tier; evidence by tier; SCCT in workflow; international access guardrail | PRC-TPRM-001 |
| OT (if applicable) | Active scan rules; passive monitoring; safety review; CIP applicability | STD-OT-001 / PLN-CIP-001 |
| CUI (if applicable) | Boundary marked; FIPS crypto; flow-down; FedRAMP equivalency captured | STD-CUI-001 / PLN-CUI-001 |
| SOX (if applicable) | ITGC mapping; evidence reuse | PLN-SOX-001 |
| Citizen-dev (if applicable) | Built on approved platform with guardrails; data classification compatible | This procedure §4.3 |
| Diagrams provided | Context · Data flow · Network · Identity · Trust boundary · OT boundary (where applicable) | This procedure §10 |
| Risk register entries | All findings entered; treatment proposed | PRC-RM-001 |

### 6.2 Threat Model

The threat model is owned by CERG Risk in collaboration with the project. It uses STRIDE as the default decomposition for IT and a STRIDE-LM (with Lateral Movement) variant for OT. The format is a short Markdown document with the following structure:

```
THREAT MODEL - <Project Name>            AR-YYYY-NNNN - TM-001

1. ASSETS AND DATA - what's worth protecting, with classification
2. ACTORS AND ENTRY POINTS - humans, machines, external services
3. TRUST BOUNDARIES - drawn on the diagram; named in text
4. THREATS BY BOUNDARY - STRIDE per boundary; OT add Lateral Movement
5. EXISTING CONTROLS - what mitigates each threat
6. RESIDUAL - what remains, mapped to risk register entries
7. ATTACK SIMULATION CANDIDATES - for purple / red engagements (PRC-AV-001)
```

> **The Threat Model Earns Its Keep When It Changes the Design**
>
> A threat model that documents what was already decided is paperwork. A threat model that surfaces a control the design missed, a missing boundary, a misplaced trust, is the reason the review exists.

### 6.3 Phase 2 SLA

Phase 2 review (Architecture Review and Threat Model) is completed within 10 business days of Phase 1 Scope Determination. Extensions may be granted by the Engineering Pillar Leader for complex systems (e.g., multi-cloud, OT-integrated, or CUI-scope systems with novel architecture). The project team is notified of any extension with rationale within the original SLA window.

### 6.4 Phase 2 Output

- Architecture Review record with status `Approved` / `Approved-with-Conditions` / `Not Approved`.
- Threat model attached.
- Findings in the risk register, scored.
- Build-time conditions for Phase 3.

---

## 7. Phase 3: Build-Time Engagement

Build-time engagement is the period between design approval and pre-production. CERG differentiates between routine and novel builds.

### 7.1 Routine vs. Novel Builds

| **Build Type** | **Definition** | **CERG Posture** |
|---|---|---|
| Routine | Deploys a pre-approved architecture pattern or IaC module without modification; uses an existing pipeline with all gates active; no new trust boundary, data path, or integration | Light-touch: CERG does not actively review unless pipeline gate failures trigger review |
| Novel | Introduces a new IaC module, a new service pattern, a new integration, or a material change from the Phase 2 architecture; or is the first deployment of a new application stack | CERG actively reviews the build artifacts |

The Engineering Pillar Leader determines whether a build is routine or novel based on the Phase 2 architecture review record and the project's pipeline configuration.

### 7.2 CERG Review Checklist for Novel Builds

| **Check** | **Pass Criteria** | **Evidence** |
|---|---|---|
| IaC conformance | IaC modules match the approved architecture per Phase 2; no material deviations | IaC diff or module reference |
| Pipeline gates active | DISH baseline scan, container image signing, SBOM generation, and vulnerability scan are all enforced (not optional) in the CI/CD pipeline | Pipeline configuration |
| Secrets scanning | No secrets detected in repository, build artifacts, or container images; secrets manager integration is wired and tested | Secrets scan output |
| SBOM generated | Software Bill of Materials is produced for every build; SBOM is stored with the build artifact | SBOM artifact |
| Image signing | Container images are signed per [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Image signature verification |
| Vulnerability scan gate | Build fails if Critical or High vulnerabilities are detected; Medium and below are flagged for tracking | Pipeline scan output |

### 7.3 Acceptance Criteria for Build-Time Gates

| **Gate** | **Blocking** | **Non-Blocking** |
|---|---|---|
| DISH baseline conformance | Non-conformance on Critical or High severity settings | Low severity or informational deviations (flagged) |
| Vulnerability scan | Critical or High vulnerabilities in application dependencies | Medium or Low vulnerabilities (tracked in backlog) |
| Secrets scanning | Any confirmed secret detected | False positive (documented and suppressed) |
| Image signing | Unsigned image in a pipeline that requires signing | - |

### 7.4 Escalation for Build-Time Findings

Build-time findings are escalated within the development team first, then to CERG:

| **Trigger** | **Action** |
|---|---|
| Pipeline gate failure (Critical/High) | Development team must resolve before build proceeds; CERG notified |
| Repeated gate failure (≥ 3 builds) | CERG reviews; may trigger conditional re-review under Phase 2 |
| Disabling or bypassing a security gate | Treated as a security incident; CISO notified |

### 7.5 SLA for Build-Time Review

CERG completes novel-build review within 3 business days of notification. If the review cannot be completed within SLA, the build may proceed with CERG acknowledgment and a scheduled follow-up review; risk is accepted by the Engineering Pillar Leader.

The artifacts produced during build include: IaC review for new modules and patterns; pipeline gates enforcing DISH baseline conformance, container image signing, SBOM generation, and vulnerability scanning; secrets checking; and conditional re-review if material design changes happen between Phase 2 and Phase 4.

---

## 8. Phase 4: Pre-Production Security Review

Pre-Production review is a focused, time-boxed readiness check. It produces a Pre-Production Security Review Record.

### 8.1 Pre-Production Checklist

| **Check** | **Pass Criteria** | **Evidence** |
|---|---|---|
| DISH baseline applied | Pass against the asset's tier in [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | DISH scan output |
| Vulnerability posture | No un-remediated, un-accepted Critical findings (risk-accepted Critical per CERG-PRC-RM-001 §8 is acceptable); High open ≤ exception count from Phase 2 | VM tool report |
| Identity wired | SSO + MFA enforced; PAM model in place; service accounts via approved pattern | IdP / PAM policy export |
| Logging | Mandatory sources onboarded; SIEM ingest verified; retention configured | SIEM source inventory |
| Detection | Day-one detection set enabled in the environment | Detection coverage report |
| Cryptography | TLS configuration matches [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md); CMK where required; secrets pattern in use | Configuration evidence |
| Resilience | Backups configured per tier; first restoration test scheduled | Backup config; resilience register entry |
| Vendor / TPRM | Vendor records current; evidence-by-tier complete; SCCT in workflow | TPRM tool entries |
| Regulatory overlay artifacts | CUI / BES / SOX artifacts populated per relevant package | Per overlay |
| Phase 2 conditions cleared | All conditions either met or risk-accepted | Phase 2 record annotations |
| Asset inventory | System added; ownership recorded | Asset inventory |
| Run-book / on-call | Service has documented on-call and run-book | Run-book reference |
| Change management | Go-live aligned with CAB cadence | Change record |

### 8.2 Phase 4 SLA

Pre-Production Security Review is completed within 5 business days of the project team submitting the Pre-Production checklist evidence. Extensions may be granted by the Risk Pillar Leader where evidence review requires additional subject matter expertise.

### 8.3 Outcome

- **Ready**: go-live disposition in Phase 5.
- **Ready-with-Risk-Acceptance**: outstanding findings have risk register entries with approved exceptions per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) §7.
- **Not Ready**: go-live blocked until specific items close.

---

## 9. Phase 5: Production Handoff and Go-Live

### 9.1 Production Handoff Package

The handoff package is the single artifact that goes into the asset's record. It is a Markdown bundle with the contents below.

```
PRODUCTION HANDOFF PACKAGE - <System Name>     AR-YYYY-NNNN - PHP-001

1. SYSTEM IDENTITY
   Asset ID(s)  · Tier · Owners · Regulatory scope

2. CERG REVIEW RECORD
   Phase 1 Intake reference
   Phase 2 Architecture Review record (link)
   Phase 2 Threat Model (link)
   Phase 3 build conditions cleared (yes/no)
   Phase 4 Pre-Production record (link)

3. CONTROL POSTURE AT GO-LIVE
   Control-by-control state per [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) (Implemented / Partial / Inherited / Planned / Risk Accepted / N/A)
   Inheritance Evidence Packages on file (cloud / SaaS providers)

4. EVIDENCE POINTERS
   DISH scan output (latest)
   VM scan output (latest)
   Identity / detection / logging configuration
   Backup configuration and first restoration test plan

5. RISK ACCEPTANCES AT GO-LIVE
   Exception IDs and approvers
   Treatment plans and expiration dates

6. ONGOING CONTROL OBLIGATIONS
   Recurring controls (scan cadence, recert cadence, restoration test cadence)
   Owners for each recurring control

7. RUN-BOOK AND ON-CALL
   References

8. SIGN-OFFS
   Engineering Reviewer
   Risk Reviewer
   Governance (overlay) Reviewer(s) - CUI / BES / SOX as applicable
   Engineering Pillar Leader
   CISO (if High / Critical risk acceptance)
   Business Owner
```

### 9.2 Go-Live Risk Acceptance Packet

A separate packet is produced only if go-live ships with one or more risk acceptances. It is the document the CISO and Business Owner sign.

```
GO-LIVE RISK ACCEPTANCE PACKET - <System Name>     AR-YYYY-NNNN - GLR-001

Each accepted risk:
   - Risk Statement (per [CERG-TMPL-RM-001](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md))
   - Linked control(s)
   - Compensating controls in place at go-live
   - Residual score and band
   - Expiration / re-review date
   - Treatment plan that retires the acceptance
   - Approver (per PRC-RM-001 §8)

Aggregate:
   - Combined residual score
   - Top three watch-list items
   - First post-go-live review date (≤ 90 days for Critical / High)
```

### 9.3 Phase 5 SLA

Production Handoff and Go-Live is completed within 3 business days of Phase 4 Ready disposition. The handoff package is the gate; go-live proceeds when the package is complete and signed.

### 9.4 Post-Go-Live Watch Period

- Critical / High risk acceptances trigger a post-go-live watch period of ≤ 90 days with a scheduled re-review.
- Detection telemetry is reviewed at 30 days for unexpected behavior tied to the accepted risk.
- Findings from the watch period feed back into the risk register and, where appropriate, the threat model.

---

### 8.3 Dispute and Appeal Process

If a project team disagrees with a finding, disposition, or outcome from any phase of the architecture review, the following appeal path is available.

#### Appeal Triggers

An appeal may be filed for:
- A finding the project team believes is inaccurate, inapplicable, or overstated
- A "Not Approved" disposition on a Phase 2 review
- A "Not Ready" disposition on a Phase 4 pre-production review
- A go-live condition the project team believes is unreasonable or infeasible

#### Appeal Process

| **Step** | **Action** | **Timing** |
|---|---|---|
| 1 | Project team submits written appeal to the CERG Pre-Production Reviewer, stating the specific finding or disposition being appealed, the rationale, and any supporting evidence | Within 5 business days of the original decision |
| 2 | CERG Pre-Production Reviewer re-evaluates with the project team; may consult additional subject matter experts | Within 5 business days |
| 3 | If resolved: decision is updated and recorded. If not resolved: escalates to Risk Pillar Leader. | - |
| 4 | Risk Pillar Leader reviews the appeal and the CERG position; makes a determination or escalates to CISO | Within 5 business days |
| 5 | CISO makes final determination. CISO's decision is binding and is recorded in the review record. | Within 10 business days of escalation |

#### Criteria for Overturning a Decision

A decision may be overturned if:
- New or overlooked evidence demonstrates the finding is inapplicable
- The project team proposes an alternative compensating control that achieves equivalent or superior risk reduction
- The original decision was based on a misinterpretation of a standard or control requirement
- The business impact of the decision is disproportionate to the risk it addresses

#### Documentation

Every appeal is documented in the review record, including: the appealed finding or disposition, the appellant's rationale, the resolution, and the final decision-maker. Appeal outcomes inform program improvement per [CERG-PRC-LL-001](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md).

---

## 10. Required Diagrams

Every Mandatory Review delivers the diagram set below. Diagrams are produced in a tool that exports to durable formats; the latest version lives with the review record.

| **Diagram** | **Required For** | **Shows** |
|---|---|---|
| **Context** | All | The system, its users, and the systems it depends on. One page. |
| **Data Flow** | All | What data moves where, classified; arrows annotated with protocol and trust boundary crossings. |
| **Network** | All non-pure-SaaS | Network paths, segmentation, ingress/egress, public exposure. |
| **Identity** | All | Identity sources, federation, SSO, MFA enforcement points, service accounts and machine identities. |
| **Trust Boundary** | All | Drawn over the data flow / network diagrams: tenant, network, identity, regulatory boundaries. |
| **OT Boundary** | OT or IT/OT bridge | ESP, EAP, BCS, BCSI flows, control room/operator interface. |
| **CUI Boundary** | CUI scope | Where CUI is processed, stored, and transmitted; FedRAMP-equivalent service edge. |
| **Backup / Recovery** | Tier 1/2 and any BES/CUI scope | Backup source, target, immutability boundary, restoration target. |

Where a diagram is implicit (e.g., a pure SaaS service has no on-prem network), the review record notes "Not Applicable" with rationale rather than omitting silently.

---

## 11. Templates

The templates below are part of this procedure. The intake form (§5.1), threat model (§6.2), handoff package (§9.1), and go-live risk acceptance (§9.2) above are the authoritative templates. Promotion of any of these to a standalone `CERG-TMPL-AR-*` artifact is tracked in [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) Section 7 as a V1.x roadmap item.

---

## 12. Metrics

| **KPI** | **Formula** | **Data Source** | **Refresh** | **Green** | **Amber** | **Red** |
|---|---|---|---|---|---|---|
| **Average Time - Phase 1 (Intake)** | Mean business days from intake submission to Scope Determination recorded | Intake tracker | Monthly | ≤ 3 days | 4–5 days | > 5 days |
| **Average Time - Phase 2 (Arch Review)** | Mean business days from Phase 2 start to review record disposition | Review tracker | Monthly | ≤ 7 days | 8–10 days | > 10 days |
| **Average Time - Phase 3 (Build-Time)** | Mean business days per build-time review cycle | Pipeline / review tracker | Monthly | ≤ 2 days | 3 days | > 3 days |
| **Average Time - Phase 4 (Pre-Prod)** | Mean business days from Phase 4 start to disposition (Ready / Ready-with-Acceptance / Not Ready) | Review tracker | Monthly | ≤ 4 days | 5 days | > 5 days |
| **Average Time - Phase 5 (Handoff)** | Mean business days from Pre-Prod Ready to handoff package signed | Review tracker | Monthly | ≤ 2 days | 3 days | > 3 days |
| **Review Backlog Count** | Number of open reviews past their target disposition date | Review tracker | Weekly | ≤ 2 | 3–5 | > 5 |
| **Finding Severity Distribution** | Count of findings by severity (Critical / High / Medium / Low / Info) recorded across all active reviews | Risk register | Monthly | Baseline to be established in first year of operation | | |
| **Threat Model Coverage Rate** | % of Mandatory Review projects with completed threat model attached to the review record | Review tracker + TM repo | Quarterly | ≥ 95% | 85–94% | < 85% |
| **Handoff Package Completion Rate** | % of projects in Phase 5 with all handoff package sections complete at go-live | Review tracker | Quarterly | ≥ 100% | 90–99% | < 90% |
| **Risk Acceptance Aging** | Mean and maximum age (days) of open risk acceptances raised through the review process | Risk register | Monthly | Mean ≤ 90 days, Max ≤ 180 days | Mean 91–180 days, Max 181–270 days | Mean > 180 days, Max > 270 days |
| **Review SLA Compliance Rate** | % of reviews meeting the SLA for their review path (Mandatory / Lightweight) | Review tracker | Monthly | ≥ 90% | 80–89% | < 80% |

> **Baseline Establishment**
>
> Where a metric is marked "Baseline to be established in first year of operation," the CERG Risk Pillar collects 12 months of data and proposes Green/Amber/Red thresholds at the next annual review. Prior to baseline, the metric is reported without RAG coloring.

---
## 14. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Procedure** |
|---|---|
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PL / SA / SC | All phases |
| NIST 800-160 (Systems Security Engineering) | Phases 2–5 |
| NIST SSDF | Phase 3 |
| NERC-CIP CIP-005 / CIP-010 | Phase 2 OT scope, Phase 4 baseline |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) | CUI scope determination in Phase 1; FIPS check in Phase 2/4 |
| SOX ITGC | SOX scope in Phase 1; change-management interface in Phase 5 |

---

## 15. Document Control

| | |
|---|---|
| **Document ID** | CERG-PRC-AR-001 |
| **Version** | 1.0 |
| **Approved By** | Cyber Engineering Pillar Leader · CISO endorsement |
| **Next Review** | Annual / on platform or process change |
| **Change Log** | 1.0 - Initial publication. Establishes intake, review, threat-model, build-time, pre-prod, and handoff phases with the citizen-development carve-out. |