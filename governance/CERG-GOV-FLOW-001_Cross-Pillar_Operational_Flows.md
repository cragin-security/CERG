| | |
|---|---|
| **Document ID** | CERG-GOV-FLOW-001 |
| **Version** | 1.4 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed operations |

---

## Table of Contents

1. [Flow Structure Conventions](#1-flow-structure-conventions)
2. [Operating Principles](#2-operating-principles)
3. [Canonical Roles](#3-canonical-roles)
4. [Flow-to-Record Crosswalk](#4-flow-to-record-crosswalk)
5. [CAT-002 Record Field Authority](#5-cat-002-record-field-authority)
6. [Default SLA Policy](#6-default-sla-policy)
7. [Allowed Decision Classes](#7-allowed-decision-classes)
8. [Shared State Models](#8-shared-state-models)
9. [Flow F-01: Control Intent to Implementation](#9-flow-f-01--control-intent-to-implementation)
10. [Flow F-02: Project Intake, Architecture Review, and Threat Modeling](#10-flow-f-02--project-intake-architecture-review-and-threat-modeling)
11. [Flow F-03: Asset Registration and Coverage Validation](#11-flow-f-03--asset-registration-and-coverage-validation)
12. [Flow F-04: Finding to Remediation, Exception, or Residual Risk](#12-flow-f-04--finding-to-remediation-exception-or-residual-risk)
13. [Flow F-05: Change and Release Security Routing](#13-flow-f-05--change-and-release-security-routing)
14. [Flow F-06: Incident to Recovery to Standards Feedback](#14-flow-f-06--incident-to-recovery-to-standards-feedback)
15. [Flow F-07: Metrics, Oversight, and Improvement Routing](#15-flow-f-07--metrics-oversight-and-improvement-routing)
16. [Automation Integration Points](#16-automation-integration-points)
17. [Evidence Quality Tiers](#17-evidence-quality-tiers)
18. [LLM Execution Directives](#18-llm-execution-directives)
19. [Flow-to-CAT-002 Record Crosswalk](#19-flow-to-cat-002-record-crosswalk)
20. [Recommended Implementation Sequence](#20-recommended-implementation-sequence)
21. [Document Control](#21-document-control)

---



## 1. Flow Structure Conventions

Every flow in this document follows a consistent structure. When implementing a flow, use these conventions to ensure completeness.

### Entry and Exit Criteria

| Flow | Trigger (Entry) | Exit Criteria |
|------|----------------|---------------|
| F-01 Control Intent | Policy/standard/baseline change, audit finding, recurring incident, regulatory requirement, CISO directive | Implementation completed + Risk validated + Evidence linked + Dashboard updated |
| F-02 Project Intake | New application/service/change, cloud/SaaS adoption, new integration, regulated/AI/OT project | Security disposition issued + pre-go-live remediation done + post-go-live risks recorded + owners confirmed + handoff delivered |
| F-03 Asset Registration | Go-live approval, new asset, major change, ownership change, decommission | Owner confirmed + classification complete + coverage validated + gaps resolved as finding/risk |
| F-04 Finding → Remediation | Vulnerability, adversarial test, threat intel, third-party, incident, audit, architecture review | Treatment executed + validated + exception/acceptance recorded if used + evidence linked + reporting updated |
| F-05 Change & Release | Normal/major/emergency change, release candidate, config/identity/encryption change | Change executed + control continuity checked + SIA reviewed + emergency bypass recorded + evidence linked |
| F-06 Incident → Recovery | Incident declared by standing IR team, material event, third-party incident with internal impact, active exploitation, regulatory notification support request | IR-owned response closed or stabilized + CERG support evidence delivered + lessons learned routed + corrective actions assigned |
| F-07 Metrics & Oversight | Monthly/quarterly cycle, threshold breach, missed SLA, maturity assessment, board request | Metrics collected + thresholds evaluated + actions assigned for outliers + CISO review done + report published |

### Flow Record Crosswalk

After each flow executes, the CAT-002 canonical records below must exist or be explicitly marked not applicable. If a required record is missing, the flow is incomplete. [`CERG-GOV-CAT-002`](CERG-GOV-CAT-002_Record_Catalog.md) is authoritative for record names, aliases, owners, required fields, and evidence value; this table only shows flow handoff expectations.

| Flow | CAT-002 canonical records | Common local aliases used in this flow |
|------|---------------------------|----------------------------------------|
| F-01 Control Intent | Control Implementation Record; Evidence Index Entry; Reporting Metric Record | Control Change Record; control implementation row |
| F-02 Project Intake | Project Security Review Record; Threat Model Record; Risk Register Entry if deferred risk remains | Project Intake Record; Architecture Review Record; security review ticket |
| F-03 Asset Registration | Asset Inventory Record; Asset Coverage Record; Finding Record or Risk Register Entry if coverage gap remains | Asset Record; CMDB item; coverage row |
| F-04 Finding → Remediation | Finding Record; Risk Register Entry if promoted; Security Exception Record or Risk Acceptance Record if used | Risk Record; Exception Record; acceptance request |
| F-05 Change & Release | Security Change Review Record; Evidence Index Entry; Risk Register Entry or Security Exception Record if emergency bypass creates residual exposure | Change Record; SIA; release security review |
| F-06 Incident → Recovery | IR-owned Incident Record; Lessons Learned Record; Program Improvement Record if CERG changes are required | IR ticket; CERG support log; Improvement Record |
| F-07 Metrics & Oversight | Reporting Metric Record; Oversight Decision Record; Program Improvement Record for assigned actions | Metric row; dashboard item; improvement backlog item |

### SLA Exception Logic

Flow-level SLA rules do not override procedure-specific clocks. For exposure management, [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) is authoritative. For risk acceptance and exception duration, [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) and [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) govern. Use the shortest applicable clock.

| Exception | Applies To | Record outcome |
|-----------|-----------|----------------|
| **False Positive** | F-04 (Findings) | Close Finding Record with rationale and evidence of false-positive determination. |
| **Compensating Control in Place** | F-04 (Findings) | Create Security Exception Record when a control is not met as written; create Risk Register Entry or Risk Acceptance Record if residual exposure remains. |
| **Vendor Patch Unavailable** | F-04 (Findings), F-01 (Control Intent) | Create Third-Party Finding / Finding Record and vendor evidence trail; create Security Exception Record or Risk Acceptance Record only if continued operation creates accepted residual risk. |
| **OT Maintenance Window** | F-04 (Findings), F-05 (Change) | Follow PRC-VM and OT/CIP routing; create Risk Register Entry if delay exceeds allowed window or requires business consequence acceptance. |
| **Business Outage Risk** | F-04 (Findings), F-05 (Change) | Create Risk Register Entry. Business Owner or Executive Sponsor accepts residual business consequence per RMF-001 §9.7 if deferral is chosen. |
| **Emergency Remediation** | F-04 (Findings) | Execute remediation immediately. Create Security Change Review Record post-hoc per F-05 emergency change rules. |
| **Reopened Finding** | F-04 (Findings) | Reopen Finding Record, increment recurrence counter, and apply the owning procedure's clock from reopen/reclassification. |
| **Accepted Risk Expiration** | F-04 (Findings), RMF-001 | Auto-create Finding Record if acceptance expires without renewal; original acceptance approver is notified. |
| **KEV / Active Exploitation Override** | F-04 (Findings) | Reclassify per PRC-VM, including Material Risk — PPR where applicable; PRC-VM SLA governs. |

## 2. Operating Principles


### Record Authority and Conversion Summary

[`CERG-GOV-CAT-002`](CERG-GOV-CAT-002_Record_Catalog.md) is authoritative for record names, aliases, owners, required fields, and evidence value. The table below summarizes how operational terms used in flows map to CAT-002 records; it does not redefine the records.

| Operational term | CAT-002 canonical record | Conversion / handoff rule |
|------|--------------------------|---------------------------|
| **Finding** | Finding Record | May promote to Risk Register Entry if SLA is exceeded, business decision is required, exploitation is active, or crown jewel / regulated scope is affected. |
| **Risk** | Risk Register Entry | May require Security Exception Record if control deviation is involved; may require Risk Acceptance Record if residual risk is accepted. |
| **Exception** | Security Exception Record | Expired exceptions without renewal become Findings; residual risk acceptance follows RMF-001 §9.7. |
| **Vulnerability / exposure observation** | Exposure Backlog Item or Finding Record | Raw scanner output becomes a Finding Record only after PRC-VM triage/validation. |
| **Control Gap** | Finding Record or Risk Register Entry | Usually becomes a Risk Register Entry when systemic impact or business consequence exists. |
| **Incident** | IR-owned Incident Record | Lessons learned may create Findings, Risk Register Entries, Program Improvement Records, or Control Implementation Records. |

**Conversion Rules:**

- A Finding promotes to a Risk Register Entry when: SLA is exceeded, the affected asset is Tier 0/Tier 1, exploitation is active, remediation requires a business decision, or compensating controls are needed.
- A Risk Register Entry that involves a control deviation creates or links to a Security Exception Record.
- A Security Exception Record that expires without renewal auto-creates a Finding Record.
- A recurring Finding in the same control family triggers a Control Implementation Record (flow-local alias: Control Change Record) under F-01.

1. **One material event creates one primary record and one accountable owner.** CERG repeatedly emphasizes authoritative records and explicit ownership as the basis for mature execution.
2. **Pre-production security work is Engineering-led unless explicitly escalated.** CERG positions Engineering as the embedded consulting and architecture-review function for projects before production.
3. **Post-production findings are Risk-led unless they are active incident-response actions.** CERG assigns Risk responsibility for continuous exposure identification through exposure management, adversarial testing, vendor assessment, and monitoring.
4. **Governance owns control intent, conformance scope, exception authority routing, evidence rules, and reporting.** CERG's governance layer includes the control system for the program: baseline, calendar, evidence, metrics, compliance mapping, and oversight artifacts.
5. **No issue may remain in an undefined state.** Every issue must become one of: remediation, compensating control, exception, accepted residual risk, or incident action.
6. **Evidence must be created during execution and linked to the primary record.** CERG's annual calendar and reporting model both assume evidence-producing activities generate or refresh evidence as part of the operating rhythm.
7. **Missed review cadence, missing ownership, or missing evidence creates a finding or risk record.** The CERG annual calendar explicitly states that missed activities are tracked as program findings or risk-register entries.

8. **Routing thresholds prevent ceremony creep.** Not every workflow requires all three pillars. The default is not "all three pillars must agree." The default is: Engineering handles known patterns, Risk engages when exposure is novel or elevated, Governance owns policy and evidence, and Business owns the consequence. Handoffs are good. Endless consensus is not.

| Work Type | Required Pillars | Rationale |
|-----------|-----------------|-----------|
| Low-risk known pattern (e.g., capacity increase, DISH-conformant config change, standard user provisioning) | Engineering only; auto-evidence | Known-safe changes do not require governance or risk review. Evidence is generated automatically. |
| Moderate known pattern (e.g., approved SaaS with no sensitive data, pre-approved architecture pattern) | Engineering + Governance conformance check | Governance confirms the pattern is still valid; no Risk engagement unless the checklist flags a risk concentration threshold. |
| Novel architecture (e.g., new technology stack, first-of-its-kind integration, citizen-development platform) | Engineering + Risk threat model | Risk performs threat modeling; Governance is informed but does not gate. |
| Regulated / OT / Crown Jewel (e.g., BES Cyber System change, CUI environment modification, SOX-relevant system) | All three pillars | Regulatory, safety, or material-financial impact requires full cross-pillar engagement. |
| High residual risk (e.g., accepted Critical risk, exception past SLA with no compensating control) | Risk-led package + Business acceptance | Risk owns the finding and treatment recommendation; Business accepts the residual risk per RMF-001. |
| Policy deviation only, low residual risk (e.g., password length exception, SSO bypass with documented compensating control) | Governance-owned exception | Governance owns the exception workflow, confirms compensating controls, and tracks expiration. |
9. **Every major event must produce a standards/process/metrics feedback decision.** CERG's RMF, incident plan, maturity model, and metrics apparatus all imply that mature operation requires monitoring and response to feed continuous improvement.

10. **If a required actor does not respond within SLA, the primary owner may proceed with documented rationale.** When Governance, Engineering, or Risk fails to act within the flow-defined SLA, the primary owner documents the default decision, proceeds with the next workflow step, and creates a Finding Record noting the missed SLA. No flow may stall indefinitely waiting for a single actor.
---

## 3. Canonical Roles

Use the following canonical role names consistently across all records and flows:

- **Engineering Pillar**
- **Risk Pillar**
- **Governance Pillar**
- **CISO**
- **Business Owner**
- **Asset Owner**
- **Technical Owner**
- **Risk Register Owner**
- **Evidence Librarian**
- **Incident Commander**
- **Control Owner**

---

## 4. Flow-to-Record Crosswalk

Every material workflow must resolve to one primary system-of-record object. FLOW identifies the operational handoff; [`CERG-GOV-CAT-002`](CERG-GOV-CAT-002_Record_Catalog.md) defines the authoritative record name and alias mapping.

| Flow concept | CAT-002 canonical record | Common FLOW alias |
|---|---|---|
| Control intent implementation | Control Implementation Record | Control Change Record |
| Project / architecture review | Project Security Review Record | Project Intake Record; Architecture Review Record |
| Threat modeling | Threat Model Record | Threat model artifact |
| Asset registration | Asset Inventory Record | Asset Record |
| Security coverage validation | Asset Coverage Record | Coverage row |
| Finding treatment | Finding Record | Finding ticket; exposure finding |
| Risk treatment | Risk Register Entry | Risk Record |
| Control deviation | Security Exception Record | Exception Record |
| Residual-risk acceptance | Risk Acceptance Record | Acceptance request; risk memo |
| Security-relevant change | Security Change Review Record | Change Record |
| Incident response | Incident Record | IR ticket / incident case |
| Evidence indexing | Evidence Index Entry | Evidence Record |
| Program improvement | Program Improvement Record | Improvement Record |
| Metrics and oversight | Reporting Metric Record; Oversight Decision Record | Metric row; oversight decision |

---

## 5. CAT-002 Record Field Authority

FLOW does not define required record fields independently. Every authoritative record uses the minimum required fields in [`CERG-GOV-CAT-002`](CERG-GOV-CAT-002_Record_Catalog.md) §3 plus the record-specific fields implied by its source procedure or template. Flow implementers may add local tool fields, but they must preserve CAT-002 canonical record type, owner, status, decision, due/review date, evidence link, and closure rationale.

When a flow below lists a primary record, read it as a CAT-002 canonical record name. Parenthetical names such as `Change Record`, `Risk Record`, or `Control Change Record` are local aliases only.

---

## 6. Default SLA Policy

| Activity | SLA |
|----------|-----|
| Triage due | 5 business days |
| Assignment due | 5 business days |
| Validation due | 5 business days |
| Evidence link due | 3 business days |
| Escalate if past due | Yes |

---

## 7. Allowed Decision Classes

All workflows should terminate in one of the following decision classes:

- **Remediate pre-production**
- **Remediate post-production**
- **Compensating control**
- **Exception required**
- **Risk acceptance required**
- **Block release**
- **Monitor only**
- **Incident response**
- **Standards update required**
- **Metrics update required**

---

## 8. Shared State Models

### 7.1 Project Security Review State Model

Allowed states:

- Intake open
- Scope defined
- Architecture review in progress
- Threat model in progress
- Remediation required pre-go-live
- Approved for go-live
- Approved with post-go-live risk
- Blocked pending prerequisite
- Closed

### 7.2 Finding Lifecycle State Model

Allowed states:

- New
- Triage
- Assigned
- Treatment planned
- In engineering work
- Exception review
- Risk acceptance review
- Validation pending
- Residual monitoring
- Closed

### 7.3 Asset Coverage Lifecycle

Allowed states:

- Discovered
- Registered
- Owner confirmed
- Classified
- Control coverage pending
- Fully covered
- Coverage gap open
- Decommissioned

### 7.4 Incident Lifecycle

Allowed states:

- Detected
- Validated
- Classified
- Containment active
- Investigation active
- Recovery active
- Lessons learned pending
- Corrective action open
- Closed

### 7.5 Control Change Lifecycle

Allowed states:

- Proposed
- Approved for design
- Implementation designed
- Validation defined
- Rollout in progress
- Validation pending
- Evidenced
- Reported
- Closed

---

## 9. Flow F-01 — Control Intent to Implementation

### Purpose
Convert governance-originated control intent into implementable technical change and risk-validated outcomes.

### Primary Owner
**Governance Pillar**

### Supporting Owners
- Engineering Pillar
- Risk Pillar

### Trigger Events
- Policy changed
- Standard changed
- Control baseline changed
- Material audit finding
- Recurring incident pattern
- Repeated exception in same control family
- Regulatory requirement added
- Board or CISO directive

### Primary Record
**Control Implementation Record** (flow-local alias: Control Change Record)

### Required Inputs
- Control ID
- Source reason (policy change, standard change, audit finding, etc.)
- Affected environments
- Affected asset classes
- Implementation deadline
- Required evidence
- Reporting metric target
- Exception path
- Preventive / detective / corrective classification


### Workflow
1. Governance creates the **Control Implementation Record** (or local Control Change Record alias).
2. Governance defines **control intent and conformance scope**.
3. Engineering produces the **implementation design**.
4. Risk defines **validation criteria before rollout**.
5. Governance approves the **evidence plan**.
6. Engineering executes rollout and records implementation evidence.
7. Risk validates effectiveness.
8. Governance updates dashboard/reporting and closes or reopens the record.

### Decision Logic
- If validation is effective, close the record.
- If validation is ineffective, reopen or create Engineering action.
- If the control cannot be met as written or by deadline, route to exception workflow.

### Evidence Required
- Implementation design package
- Validation plan
- Control test or outcome evidence
- Updated Reporting Metric Record
- Linked Evidence Index Entry

### SLA
- Governance publishes package: 5 business days
- Engineering design: 10 business days
- Risk validation plan: 5 business days
- Evidence link: 3 business days

### Escalation
- Missing Engineering design after SLA → escalate to CISO and create finding
- Missing validation → do not allow closure; create risk record

### Closure Criteria
- Implementation completed
- Risk validated
- Evidence linked
- Dashboard updated

---

## 10. Flow F-02 — Project Intake, Architecture Review, and Threat Modeling

### Purpose
Ensure that new systems and major changes enter production with known scope, required controls, and explicit security disposition.

### Primary Owner
**Engineering Pillar**

### Supporting Owners
- Risk Pillar
- Governance Pillar

### Trigger Events
- New application
- New service
- Major change
- New cloud or SaaS adoption
- New integration
- Internet-exposed component
- Regulated-scope project
- AI system introduction
- IT/OT convergence change

### Primary Record
**Project Security Review Record** (front-door alias: Project Intake Record)


### Required Inputs
- Project name
- Business owner
- Technical owner
- Intended go-live date
- Asset class
- Data classification
- Regulatory scope
- AI use category, model/provider, and proposed agency boundary where AI is in scope
- Hosting environment
- External dependencies
- Privilege model
- Logging plan
- Backup / recovery plan

### Review Tiers

Projects are triaged into one of three review tiers based on risk characteristics. The tier determines review depth, not whether a review occurs. PRC-AR-001 provides the detailed procedure for each tier.

| Tier | Criteria | Review Depth | Architecture Review | Threat Model | Governance Conformance |
|------|----------|-------------|---------------------|--------------|------------------------|
| **T1 — Full Review** | Internet-exposed, regulated-scope, sensitive data, OT/safety impact, new platform pattern, high-risk third-party, complex privileged path | Full Phase 2-4 per PRC-AR-001 | Full architecture review | Full threat model | Governance issues Conformance Scope Statement |
| **T2 — Lightweight Review** | Internal service on reviewed platform, reuse of approved architecture pattern, capacity addition to reviewed system, non-sensitive data, no regulatory scope | Checklist review per PRC-AR-001 §4 | Checklist-based architecture review | Threat model review (confirm existing model covers change) | Governance confirms existing conformance applies |
| **T3 — Automated-Only** | Pre-approved change pattern (e.g., config update within baseline, dependency bump within allowed range), citizen-development platform app, pipeline already enforces SAST/policy-as-code/CSPM gates | Automated gates only; no manual review | Automated SAST + policy-as-code pass = architecture review satisfied | N/A (platform-level threat model covers) | Automated CSPM posture check = conformance satisfied |

### AI Routing Rules

When AI is in scope, the Project Intake Record links to an AI intake record using [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) or an equivalent local record. Routing is based on the AI use case, data classification, and agency boundary:

- **Consumed AI services** may follow T2 or a pre-approved architecture pattern when the use case, user population, and maximum data classification match the sanctioned AI tools register.
- **Built AI, embedded AI, AI agents, model-serving platforms, RAG systems, or AI with consequential action capability** default to T1 unless Engineering documents why an approved pattern fully covers the use.
- **AI processing Confidential, Restricted, CUI, BES Cyber System Information, SOX-relevant data, personal data at material scale, or safety-impacting data** requires Governance conformance review and Risk participation.
- **AI-enabled vendor features** trigger third-party reassessment when the feature changes data use, training, retention, subprocessors, user population, or decision impact.
- Approved consumed AI tools update the sanctioned AI tools register using [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md). Built or embedded AI systems update the AI system and model register using [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md).

### Workflow (by Tier)

**T1 — Full Review:**
1. Engineering opens **Project Intake Record** and assigns T1.
2. Engineering performs initial security scoping.
3. Engineering performs full **Architecture Review** (PRC-AR-001 Phase 2).
4. Engineering performs full **Threat Model** (PRC-AR-001 Phase 2).
5. Governance issues **Conformance Scope Statement**.
6. Risk participates per risk concentration thresholds.
7. Engineering classifies issues as pre-go-live or post-go-live.
8. Engineering issues final security disposition.

**T2 — Lightweight Review:**
1. Engineering opens **Project Intake Record** and assigns T2.
2. Engineering completes the T2 checklist (PRC-AR-001 §4).
3. Engineering confirms existing threat model covers the change; documents any delta.
4. Governance confirms existing conformance scope applies.
5. Engineering issues disposition. Risk participates only if checklist flags a risk concentration threshold.

**T3 — Automated-Only:**
1. Engineering opens **Project Intake Record** and assigns T3.
2. Automated gates execute: SAST scan, policy-as-code validation, CSPM posture check.
3. If all gates pass: Engineering issues disposition. No manual review required.
4. If any gate fails: revert to T2 and flag the failure for Engineering review.

### Risk Concentration Thresholds
Risk participation is required when one or more of the following are true:
- Sensitive data present
- Regulated scope present
- Internet exposure present
- High-risk third-party dependency present
- Complex privileged path present
- OT or safety impact present
- AI system has autonomous or tool-using agency beyond draft/recommendation
- AI use expands beyond the sanctioned tool's approved use case, user population, or maximum data classification

### Allowed Dispositions
- Approved for go-live
- Approved with pre-go-live remediation
- Approved with post-go-live risk record
- Blocked pending prerequisite

### Mandatory Rules
- Every identified issue must be classified as **pre-production remediation** or **post-production managed risk**, not both.
- Any issue deferred beyond go-live must create a **Risk Record** and, where nonconformance exists, an **Exception Record candidate**.
- No go-live proceeds without named business and technical owners.
- If the project touches or creates a Tier 0/Tier 1 crown jewel (per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)), the crown-jewel minimum control profile (CJ-001 §3.3) is a pre-go-live requirement, and the relevant loss scenarios become threat-model design targets per [`CERG-PRC-TM-001`](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md).


### Closure Criteria
- Security disposition issued (approved, approved-with-remediation, approved-with-risk, or blocked)
- All pre-go-live remediation completed and validated
- Post-go-live risk records created for deferred issues
- Named business and technical owners confirmed
- Production Handoff Security Summary delivered

### Evidence Required
- Architecture Review Record
- Threat Model Record
- Conformance Scope Statement
- Production Handoff Security Summary
- AI Intake and Sanctioning Record where AI is in scope
- Sanctioned AI Tools Register entry or AI System and Model Register entry where AI is approved

### Escalation
- Go-live requested while blocked → escalate to CISO
- Missing ownership or scope → hold project and create finding

---

## 11. Flow F-03 — Asset Registration and Coverage Validation

### Purpose
Ensure every in-scope asset has ownership, classification, regulatory designation, and required control coverage.

### Primary Owner
**Engineering Pillar**

### Supporting Owners
- Risk Pillar
- Governance Pillar

### Trigger Events
- Project approved for go-live
- New asset discovered
- Major asset change
- Ownership change
- Environment change
- Regulatory scope change
- Asset decommission request

### Primary Record
**Asset Inventory Record** (local alias: Asset Record)


### Asset Classes and Registration Requirements

Assets are classified by lifecycle to determine registration depth. Ephemeral and auto-scaling assets are registered via automated discovery, not manual entry.

| Asset Class | Examples | Registration Method | Required Fields |
|------------|----------|-------------------|-----------------|
| **Persistent** | Physical servers, VMs, databases, network appliances, SaaS platforms | Manual or automated via CMDB integration | All 14 fields below |
| **Dynamic** | Long-lived cloud instances (EC2, GCE), Kubernetes nodes, PaaS services | Automated via cloud API / CSPM discovery | Asset ID, type, environment, classification, owner, scan coverage, logging source. Remaining fields derived from tags or platform defaults. |
| **Ephemeral** | Auto-scaling instances, spot instances, containers, serverless functions, batch jobs | Automated via cloud API / orchestrator; registered at the *workload level*, not per-instance | Workload ID (e.g., ECS service name, Lambda function name, Deployment name), type, environment, classification, owner, scan coverage (inherited from platform). Individual instances tracked as members of the workload group. |

**Workload-level registration** means that a Kubernetes Deployment, an ECS Service, or a Lambda function is registered once. Individual pods, tasks, or invocations are tracked as members of that workload group. Coverage validation (§ Coverage Requirements) is assessed at the workload level, not the instance level.

### Required Inputs
- Asset ID
- Asset type
- Asset owner
- Business owner
- Technical owner
- Environment
- Data classification
- Regulatory scope
- Criticality
- Support team
- Logging source expected
- Scanning required
- Backup required
- Access review required

### Workflow
1. Engineering creates or updates **Asset Record**.
2. Engineering confirms owner and classification.
3. Risk validates scan coverage and exposure visibility.
4. Governance maps asset to control and calendar obligations.
5. Governance determines whether any coverage gap is a finding or risk.

### Coverage Requirements
- Owner assigned
- Classification complete
- Regulatory flag present if applicable
- Scan coverage established if required
- Logging source established if required
- Backup assignment established if required
- Access review population assigned if required
- For crown-jewel assets (Tier 0/Tier 1 per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)), the CJ-001 §3.3 minimum control profile is present and verified, not merely scanned


### Closure Criteria
- Asset owner assigned and confirmed
- Classification complete
- Regulatory flag set if applicable
- Scan coverage established if required
- Logging source established if required
- Backup assignment established if required
- Access review population assigned if required
- Any coverage gap resolved as finding or risk record
- Crown-jewel minimum control profile verified for Tier 0/Tier 1 assets (per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md))

### Evidence Required
- Asset Inventory Record
- Asset Coverage Record / coverage validation result
- Governance obligation map

### Metrics Generated
- Asset coverage completeness %
- Assets missing owner %
- Assets missing scan coverage %
- Assets missing logging %

---

## 12. Flow F-04 — Finding to Remediation, Exception, or Residual Risk

### Purpose
Convert discovered exposure into a deterministic treatment path: remediation, compensating control, exception, formal risk acceptance, or incident handling.

### Primary Owner
**Risk Pillar**

### Supporting Owners
- Engineering Pillar
- Governance Pillar

### Trigger Events
- Vulnerability discovered
- Adversarial validation result
- Threat intelligence match
- Third-party risk result
- Incident follow-on issue
- Audit finding
- Architecture review deferred issue

### Primary Record
**Finding Record**


### Required Inputs
- Finding ID
- Finding source (vulnerability, adversarial, threat intel, third-party, incident, audit, architecture review)
- Severity (Critical, High, Medium, Low)
- Exploitability assessment
- Affected assets
- Business owner
- Technical owner
- Regulatory scope
- Recommended treatment class
- Due date

### Workflow
1. Risk creates **Finding Record** and triages.
2. Risk identifies exposure path and treatment options.
3. Engineering assesses technical feasibility of treatment.
4. Governance determines whether exception or acceptance process is required.
5. Engineering executes remediation or compensating control if approved.
6. Risk validates closure or establishes residual monitoring.
7. Governance updates reporting and escalates recurring patterns.


### SLA Authority

This flow does not define a separate vulnerability or exposure remediation clock. For vulnerabilities, KEV items, active exploitation, scanner observations, and confirmed reachable exposures, [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §7.2 is the canonical SLA source. FLOW F-04 uses the finding state and record handoff; PRC-VM determines the treatment clock.

| PRC-VM Classification | Treatment Clock |
|---|---|
| **Material Risk — PPR** | 48 hours (Internet-facing) / 72 hours (internal) |
| **Confirmed Exposure — Critical** | 3 days |
| **Confirmed Exposure — High** | 15 days |
| **Confirmed Exposure — Medium** | 30 days |
| **Confirmed Flaw, Not Exposed** | 90 days / next maintenance window |
| **Hygiene Debt** | Patch hygiene cadence per PRC-VM §10 |

For non-exposure findings such as audit findings, architecture review issues, or third-party assessment gaps, the owning procedure or record sets the due date. If more than one SLA or due date applies, use the shortest applicable clock.


### Risk Promotion Rules — When a Finding Becomes a Risk Register Entry

Not every finding needs a risk register entry. Promote a Finding to a Risk Record when any of these conditions are met:

| Condition | Action | Rationale |
|-----------|--------|-----------|
| SLA for remediation is exceeded | Create Risk Record with severity based on original finding | An overdue finding represents active, unmanaged exposure |
| Affected asset is Tier 0 (Crown Jewel) or Tier 1 (Critical) | Create Risk Record regardless of severity | High-criticality assets warrant formal risk tracking |
| Active exploitation confirmed (KEV-listed, exploit in wild) | Create Risk Record; treat as Critical | Active exploitation invalidates the original severity assessment |
| Remediation requires a business decision (budget, outage window, vendor coordination) | Create Risk Record with business owner assigned | Business decisions require business accountability |
| Compensating controls are needed | Create Risk Record and Exception Record | Compensating controls represent a deviation from the control baseline |
| Repeated finding — same vulnerability class, same system, more than twice | Create Risk Record; escalate to root cause analysis | Recurrence signals a systemic issue, not a one-time miss |
| Regulatory deviation required (CIP, CMMC, SOX) | Create Risk Record and initiate regulatory deviation process | Regulatory implications require formal tracking |

A Finding that does not meet any promotion condition is closed through the standard remediation → validation → closure path.

### Closure Validation Rules

Who can close a finding, and what evidence is required, depends on severity and source:

| Severity | Who Can Close | Minimum Evidence | Retest Required? |
|----------|--------------|-----------------|-----------------|
| **Critical** | Risk Pillar (must validate) | E3 evidence per AUD-001; authenticated re-scan or adversarial re-test | Yes — mandatory |
| **High** | Risk Pillar (must validate) | E3 evidence; authenticated re-scan or equivalent validation | Yes — mandatory |
| **Medium** | Engineering may self-close with automated validation | E2 minimum; authenticated re-scan or SAST re-scan | Yes — automated re-scan acceptable |
| **Low** | Engineering may self-close with automated validation | E2 minimum; scan report or equivalent | At discretion of closer |

**Additional closure rules:**

- Engineering may not close a Critical or High finding unilaterally. Risk must validate.
- Self-service closure (Medium/Low) requires the automated validation to reference a specific pipeline run, scan job, or test execution with a timestamp.
- If closure validation fails (retest shows finding still present): reopen the finding, increment the recurrence counter, and escalate per the recurring finding rules below.
- Closure must include a statement of what changed: "Patched to version X," "Parameterized query at line Y," "Added WAF rule Z." "Fixed" is insufficient.

### Recurring Finding Escalation

A finding that reappears after closure is different from a new finding. Escalate recurring findings as follows:

| Recurrence | Action | Escalation |
|-----------|--------|-----------|
| 1st recurrence (same vulnerability class, same system) | Reopen with "Recurring" flag; verify original closure evidence was valid | Notify Pillar Leader |
| 2nd recurrence | Root cause analysis required; document why the fix did not hold | Escalate to Pillar Leader; create Finding Record for the root cause |
| 3rd recurrence | Treat as systemic control failure | Create Risk Record; escalate to CISO; consider Control Change Record (F-01) |

Recurring findings across multiple systems in the same control family trigger a Control Change Record regardless of recurrence count per system.

### Allowed Treatment Paths
- Immediate remediation
- Planned remediation
- Redesign
- Compensating control
- Exception request
- Formal risk acceptance
- Incident response (if active exploitation exists)

### Mandatory Rules
- No finding may remain undefined beyond triage SLA or the owning procedure's classification deadline.
- Engineering may not close a Critical, High, Material Risk, PPR, adversarial, audit, or regulated-scope finding unilaterally; Risk must validate.
- **Self-Service Closure (Medium/Low):** Engineering may close Medium and Low findings when automated validation confirms the fix and no regulated-scope, active-exploitation, adversarial-test, or audit requirement requires independent validation. Automated validation includes: authenticated vulnerability re-scan (findings from scanning), SAST re-scan passing (findings from code review), CSPM posture check passing (findings from cloud posture), or policy-as-code gate passing (findings from IaC review). Risk validates Medium/Low findings by exception — spot-checking a sample rather than re-validating every closure.
- Any control not met as written or on time routes to exception review; any residual risk accepted after that review follows [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 and [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).
- Accepted residual risk requires the Business Owner or Executive Sponsor acceptance required by RMF-001 §9.7, rationale, conditions, review cadence, and expiration if applicable.


### Validation Method by Finding Source

| Finding Source | Minimum Validation Method | Sufficient Evidence |
|----------------|--------------------------|---------------------|
| Vulnerability scan | Authenticated re-scan of affected asset | Scan report showing finding resolved |
| Adversarial test | Targeted re-test of the specific finding | Test report confirming closure |
| Code review (SAST) | Re-scan + code diff review for High/Critical | Scan report + reviewer sign-off |
| Architecture review | Architecture Review Record updated | Signed disposition from Engineering |
| Threat intelligence | IOC search across environment | Negative search result |
| Audit finding | Evidence package per auditor specification | Auditor acceptance confirmation |
| Third-party risk | Vendor attestation or re-assessment | Updated vendor assessment |

### Closure Criteria
- Treatment executed (remediation, compensating control, exception, or risk acceptance)
- Risk validation confirms closure or establishes residual monitoring
- Exception or risk-acceptance record created if used
- Evidence linked to finding record
- Reporting updated

### Evidence Required
- Triage result
- Engineering treatment plan
- Remediation or compensating-control evidence
- Validation result
- Exception or risk-acceptance record if used

### Escalation

| Trigger | Escalation Target | Action |
|----------|------------------|--------|
| Material Risk — PPR unassigned after **4 hours** | CISO | Immediate notification; CISO may invoke incident response |
| Material Risk — PPR past PRC-VM SLA | CISO | Mandatory review; create Risk Record for delayed treatment and route any acceptance through RMF-001 §9.7 |
| Confirmed Exposure — Critical unassigned after **1 business day** | Pillar Leader (Risk) | Pillar Leader must assign or explain; CISO informed for regulated or crown-jewel scope |
| Confirmed Exposure — Critical or High past PRC-VM SLA | Governance Pillar Leader + CISO | Create exception/risk-acceptance record as applicable; escalate treatment blocker |
| Confirmed Exposure — Medium past PRC-VM SLA | Risk Pillar Leader | Included in monthly roll-up report; risk of SLA drift |
| Confirmed Flaw Not Exposed or Hygiene Debt past applicable cadence | Risk Pillar Leader | Included in quarterly review or patch-hygiene review |
| Repeated exception in same control family | Governance Pillar Leader | Create Control Change Record (F-01) |
| Engineering refuses or stalls treatment | Pillar Leader (Risk → Engineering) | Cross-pillar escalation; CISO if unresolved after 5 business days |

---

## 13. Flow F-05 — Change and Release Security Routing

### Purpose
Ensure that security-significant changes receive consistent cross-pillar handling.

### Primary Owner
**Engineering Pillar**

### Supporting Owners
- Risk Pillar
- Governance Pillar

### Trigger Events
- Normal change requested
- Major change requested
- Emergency change requested
- Release candidate created
- Production configuration change
- Identity model change
- Encryption or key change
- New external dependency

### Primary Record
**Security Change Review Record** (local alias: Change Record)


### Required Inputs
- Change ID
- Change type (normal, major, emergency)
- Affected assets
- Implementation window
- Rollback plan
- Security impact analysis
- Data classification
- Regulatory scope
- Testing plan

### Change Classification and Required Activities

Not all changes carry the same security risk. The table below defines what each change class requires. "SIA" = Security Impact Analysis. "CC" = Control Continuity check.

| Change Class | Examples | SIA Required | SIA Depth | Control Continuity Scope | Risk Review | Fast-Lane Eligible |
|-------------|----------|-------------|-----------|--------------------------|-------------|--------------------|
| **Pre-Approved** | Documentation update, dashboard color change, log format adjustment, non-security config change within approved baseline, dependency bump within allowed semver range | No | N/A | None — change has no security surface | No | Yes — deploy immediately, record change post-hoc |
| **Standard** | New feature deployment, scaling adjustment, routine cert rotation, IAM role addition within existing policy, database schema change | Yes | Lightweight — confirm change does not alter security boundary | Verify specific controls affected by the change (e.g., cert rotation → CR-001 controls; IAM change → AC-2 controls) | No, unless risk-significant criteria met | No — standard flow |
| **Major** | New service introduction, architecture change, firewall rule change, encryption protocol change, identity model restructure, new external dependency | Yes | Full — assess impact across all control families | Verify all controls on affected assets; confirm no control regression | Yes — mandatory Risk review | No — requires full review |
| **Emergency** | Active incident remediation, zero-day patch, critical service restoration | Yes — post-execution within 24 hours | Full — documented after execution | Verify as soon as practical; automate where possible | Post-execution; linked risk or exception required for any deviation | Yes — bypass normal gates; document rationale and create post-hoc record |

**Control Continuity Scope by Change Class:**
- **Pre-Approved:** No control continuity check required.
- **Standard:** Verify the specific controls directly affected by the change. A cert rotation verifies CR-001 controls. An IAM role addition verifies AC-2 controls for the new role. Do not re-verify unrelated controls.
- **Major:** Verify all controls mapped to the affected assets (per CB-001). Confirm no control has regressed.
- **Emergency:** Verify as soon as practical. Automated CSPM/CNAPP scanning is acceptable as control continuity evidence. Document any gaps as a finding.

### Workflow
1. Engineering classifies the change per the table above and opens the **Security Change Review Record** (or local Change Record alias).
2. For Pre-Approved: deploy immediately; create Change Record post-hoc. Skip to step 6.
3. For Standard: Engineering completes lightweight SIA. For Major/Emergency: Engineering completes full SIA.
4. Risk reviews if change is risk-significant (Standard) or mandatory (Major/Emergency).
5. Governance applies conformance and evidence requirements (Standard/Major/Emergency).
6. Engineering executes the change.
7. Engineering performs control continuity checks per the scope defined above.
8. Governance verifies evidence and closes or reopens the change.

### Risk-Significant Change Criteria
- Internet exposure changed
- Privileged access changed
- Logging coverage impacted
- Backup or recovery path changed
- Encryption or key handling changed
- Third-party dependency added or materially modified
- Regulated-scope asset impacted
- Emergency bypass used

### Mandatory Rules
- Emergency security deviations require linked risk or exception review.
- Change closure requires control continuity verification, not only service success.
- Missing rollback strategy blocks major-change approval.


### Closure Criteria
- Change executed successfully
- Control continuity checks passed
- Security Impact Analysis completed and reviewed
- Risk or exception record created if emergency bypass used
- Evidence linked to change record
- Governance verification complete

### Evidence Required
- Security Impact Analysis
- Test evidence
- Control continuity result
- Linked risk or exception if applicable

---

## 14. Flow F-06 — Incident to Recovery to Standards Feedback

### Purpose
Define how CERG supports the standing Incident Response team during and after an incident, then converts verified lessons into engineering controls, risk posture, governance artifacts, metrics, and program improvements.

> **IR Ownership:** The standing Incident Response team owns incident declaration, classification, command, the IR plan, regulatory notification-clock process, and exercise management. CERG is not responsible for IR operations. This flow defines CERG's *supporting role* during incidents: supplying asset context, exposure analysis, control evidence, recovery dependencies, regulatory mapping support, and post-incident improvement routing. The Incident Commander's authority during an active incident supersedes any CERG workflow step.

### Primary Owner
**Incident Commander / Standing Incident Response Team** for active incident operations.

**CERG Governance Pillar** for CERG-owned evidence packaging, lessons-learned routing, standards feedback, and improvement tracking after the IR team requests support or closes active response.

### Supporting Owners
- Engineering Pillar
- Risk Pillar
- Governance Pillar
- CISO
- Evidence Librarian

### Trigger Events
- Incident declared by the Incident Commander or standing IR team
- Material security event requiring CERG support
- Third-party incident with internal impact
- Active exploitation of a known issue in CERG-managed scope
- Incident Commander, Legal, or Governance request for regulatory evidence or control-impact support

### Primary Record
**IR-owned Incident Record** during active response.

**Lessons Learned Record** and/or **Program Improvement Record** when the incident produces a CERG control, risk, standard, evidence, or metric change.

### Required Inputs
- Incident ID
- Incident Commander
- Severity assigned by the IR process
- Detected time or timeline reference
- Affected assets
- Suspected scope
- Business owner
- Regulatory scope
- CERG support requested
- Evidence-preservation requirements
- Containment or recovery decisions requiring CERG execution

### Incident Severity Reference

Incident severity and response clocks are governed by the Incident Response Plan, not by this flow. CERG records use the paired labels below only to align CERG support records with the IR-owned incident record.

| IR Severity | CERG Support Label | Meaning |
|---|---|---|
| **Sev 1** | **P1 / Critical** | Material business, safety, reliability, regulated-data, or crown-jewel impact. |
| **Sev 2** | **P2 / Significant** | Confirmed compromise or regulated impact requiring full IR coordination. |
| **Sev 3** | **P3 / Moderate** | Scoped compromise or material event requiring targeted CERG support. |
| **Sev 4** | **P4 / Minor** | Localized event or alert requiring routine support or monitoring only. |

### Workflow
1. Incident Commander or standing IR team declares the incident, assigns severity, and opens the IR-owned Incident Record.
2. Incident Commander requests CERG support and names the CERG outputs needed: asset context, logs, control evidence, risk history, vendor context, recovery dependency, regulatory mapping support, or technical execution.
3. Risk supplies exposure context, threat intelligence, affected-control analysis, and investigation support under Incident Commander / Lead Investigator direction.
4. Engineering executes containment, eradication, recovery, access, network, configuration, or restoration changes approved through the IR process.
5. Governance supplies regulatory mapping, evidence indexing, decision-log support, and reporting artifacts under Incident Commander and Legal direction. Governance does not own the notification-clock process.
6. Evidence Librarian preserves CERG-produced evidence and links it to the IR-owned Incident Record or submitted evidence package.
7. After active response is closed or stabilized, Governance opens the CERG Lessons Learned Record and feedback decision record.
8. Engineering, Risk, and Governance assign corrective actions, Risk Register Entry updates, standards/procedure changes, Reporting Metric Record updates, or Program Improvement Records.

### Mandatory Post-Incident CERG Outputs
- CERG support actions and evidence package
- Root cause or control-failure input supplied to the IR team
- Risk-register update decision
- Control, standard, or procedure change decision
- Metrics/KRI update decision
- Corrective-action owner and due date
- Program Improvement Record when the lesson changes how CERG operates

### Mandatory Rules
- CERG does not close the incident; the Incident Commander or standing IR team closes active response.
- CERG's post-incident work is not complete until the lessons-learned decision is recorded, even if technical recovery is complete.
- If an incident exposes previously accepted risk, the acceptance rationale and treatment conditions must be reviewed through the risk process.
- A recurring incident pattern in the same control family creates a Control Change Record or Program Improvement Record.
- Regulatory notification decisions are made through the IR, Legal, and executive process; CERG Governance records and preserves the supporting evidence it supplies.

### Closure Criteria for CERG Support
- Incident Commander has closed or stabilized the active-response phase, or released CERG from active support.
- CERG support actions are recorded and linked to the IR-owned Incident Record.
- CERG-produced evidence package is stored and indexed.
- Root cause and control-failure inputs are delivered to the IR team or lessons-learned process.
- Lessons-learned decision recorded: standards, procedure, risk, control, metric, or no-change-with-rationale.
- Corrective actions assigned with owner and due date.
- Previously accepted risk reviewed if the incident exposed it.

### Evidence Required
- IR timeline reference or incident record link
- CERG support action log
- Asset, data, control, risk, vendor, or recovery evidence supplied to the IR team
- Evidence-preservation and submission package links
- Lessons-learned or Program Improvement Record

---

## 15. Flow F-07 — Metrics, Oversight, and Improvement Routing

### Purpose
Convert operational data into management action, improvement backlog, standards review, risk escalation, and board-grade reporting.

### Primary Owner
**Governance Pillar**

### Supporting Owners
- Risk Pillar
- Engineering Pillar
- CISO

### Trigger Events
- Monthly reporting cycle
- Quarterly reporting cycle
- Metric threshold breach
- Repeated missed SLA
- Maturity assessment run
- Board or executive request
- Repeated control failure pattern

### Primary Record
**Reporting Metric Record**


### Required Inputs
- Metric name
- Metric definition
- Source system
- Reporting period
- Threshold (green / amber / red)
- Actual value
- Evidence link
- Accountable role
- Interpretation note

### Workflow
1. Governance collects metrics per canonical dictionary.
2. Risk supplies exposure and residual-risk metrics.
3. Engineering supplies implementation and quality metrics.
4. Governance evaluates thresholds and trends.
5. Governance assigns action type for each outlier.
6. CISO reviews material outliers and escalations.
7. Governance publishes monthly or quarterly report.

### Allowed Action Types
- Engineering action
- Risk escalation
- Governance standards review
- Exception review
- No action with rationale

### Baseline Cross-Pillar Metrics
- % of new assets fully covered within SLA
- % of pre-production findings closed before go-live
- % of post-production findings assigned within 5 business days
- % of exceptions with active compensating controls
- Median time from discovery to validated closure
- % of incidents resulting in standards or procedure update
- % of board metrics backed by direct evidence

- % of Critical/High findings where validation method was E3 (adversary-facing test or authenticated re-scan) vs. E2 (process artifact only)
- % of accepted risks re-opened due to threat landscape change within 12 months of acceptance
- weighted sum of (open findings × 1) + (open exceptions × 3) + (accepted risks × 2) per NIST control family
- % of exceptions within 30 days of expiration without a renewal or closure decision
- % of flow steps where a pillar missed its SLA, reported monthly per pillar
- **Review cycle time by tier**: median hours/days from F-02 intake to security disposition, reported by review tier (T1/T2/T3) — measures whether review depth is proportional to project risk
- **Deployment frequency of reviewed projects**: number of deployments per week for projects that passed F-02 review — measures whether security review enables or impedes delivery velocity
- **Pre-approved change ratio**: % of F-05 changes classified as Pre-Approved vs. Standard/Major — measures whether the change classification model is appropriately tuned; a ratio below 30% suggests over-classification
- **Automated closure rate**: % of F-04 Medium/Low findings closed via self-service automated validation vs. manual Risk validation — measures automation adoption
- **SLA breach rate by pillar**: % of flow steps where a pillar missed its SLA, reported monthly per pillar — identifies bottlenecks across Engineering, Risk, and Governance
### Mandatory Rules
- Every threshold breach must produce an action type or explicit no-action rationale.
- Metrics without evidence links are not board-reportable.
- Repeated outlier in same control family creates a Control Change Record or Improvement Record.

---


### Closure Criteria
- Metrics collected from all three pillars per canonical dictionary
- Thresholds and trends evaluated
- Action type assigned for every outlier (engineering action, risk escalation, standards review, exception review, or no-action-with-rationale)
- Material outliers reviewed by CISO
- Monthly or quarterly report published
- Repeated outliers in same control family escalated to Control Change Record or Improvement Record



## 16. Automation Integration Points

The flows in this document describe human-driven steps, but automated security controls can satisfy or accelerate many of them. The table below defines where automation is accepted as valid execution and what evidence is required.

| Flow Step | Automated Equivalent | Evidence Required | Tier Equivalent |
|-----------|---------------------|-------------------|-----------------|
| F-02 Architecture Review | SAST scan passes in CI/CD pipeline; policy-as-code gates pass at apply time | Pipeline run ID + scan results | T3 (Automated-Only) for pre-approved patterns; supports T2 (Lightweight) for internal services |
| F-02 Threat Model | Platform-level threat model on file; change within modeled scope | Reference to existing threat model + delta analysis | T2/T3 |
| F-03 Asset Registration | Cloud API / CSPM auto-discovery; tag-based owner/classification assignment | CSPM inventory export; tag audit log | Automated for Dynamic and Ephemeral classes |
| F-04 Finding Validation | Authenticated vulnerability re-scan; SAST re-scan; CSPM posture re-check; policy-as-code gate re-run | Scan report + finding ID correlation | E3 for code/vulnerability findings; E2 for config findings |
| F-05 Security Impact Analysis | IaC diff analysis; policy-as-code evaluation of proposed change; blast radius assessment from CMDB | Automated SIA report; policy evaluation result | Standard/Major — augments but does not replace human SIA for Major changes |
| F-05 Control Continuity Check | CSPM/CNAPP posture scan post-deployment; automated control test suite | Posture scan report; test suite results | Acceptable for Standard changes; augments Major change CC |
| F-07 Metric Collection | API integration with scanning tools, pipeline analytics, CSPM dashboards | API response or dashboard export with timestamp | Fully automated |

**Automation Evidence Standard:** Automated evidence must be traceable to a specific pipeline run, scan job, or API call with a timestamp and a unique identifier. A link to the pipeline run (e.g., CI/CD run #1247) is sufficient; screenshots are not required when a programmatic reference is available.

**When Automation Satisfies a Step Entirely:** For T3 (Automated-Only) projects and Pre-Approved changes, automated gate passage satisfies the requirement with no human review. For T2 and Standard changes, automation satisfies evidence requirements but a human reviewer confirms it. For T1 and Major changes, automation augments but does not replace human review.

---

## 17. Evidence Quality Tiers

Not all evidence proves the same thing. Flows reference evidence by tier so that operators know what level of proof is required.

| Tier | Name | What It Proves | Example | Required For |
|------|------|---------------|---------|--------------|
| **E1** | Control Exists | The artifact that implements the control is present | JML log file exists in the evidence library | Routine governance checks (F-03, F-07) |
| **E2** | Control Operates | The control processed a transaction successfully | JML log shows 3 leavers processed this month; access review spreadsheet completed | Standard evidence collection; Medium/Low finding closure (F-04) |
| **E3** | Control Is Effective | An adversary-facing test, independent verification, or automated re-validation confirms the control works as intended | Automated authenticated vulnerability re-scan confirming fix; SAST re-scan passing with no regressions; policy-as-code gate passing for IaC change; CSPM posture check confirming drift remediation. Full penetration test is E3+ and reserved for adversarial-sourced findings (pen test, red team) or when automated validation is architecturally impossible. | Critical/High finding closure (F-04); control test results (F-01); incident post-mortem validation (F-06) |

Flows that specify "Evidence Required" should note the minimum tier. Where E3 is not feasible (e.g., architecturally impossible to test), the rationale must be documented in the record.

---

## 18. LLM Execution Directives


These instructions tell an LLM how to execute the flows without ambiguity:

1. **Always identify the primary record before taking action.** If no primary record exists, create it first.
2. **Always assign exactly one accountable role.** Supporting roles may be many; accountability must be singular.
3. **If an issue is pre-production, default owner is Engineering.** If post-production, default owner is Risk. If it concerns standards, exceptions, evidence, or reporting, include Governance.
4. **Never close a finding based on implementation evidence alone.** Require validation from Risk.
5. **Never treat control deviation informally.** If deadline or control intent cannot be met, route to an Exception Record.
6. **If required owner, classification, or evidence is missing, mark the item blocked or gap-open and create a finding or risk as defined by the relevant flow.**
7. **At closure of any major event, require a feedback destination:** standards, procedure, metric, backlog, risk register, or no-change-with-rationale.
8. **If SLA breach occurs, escalate according to the flow; do not silently continue.**
9. **Use canonical CERG role names and record names consistently.**
10. **Prefer evidence generation during execution over retrospective evidence collection.**

---

## 19. Flow-to-CAT-002 Record Crosswalk

FLOW does not maintain standalone record templates. Use [`CERG-GOV-CAT-002`](CERG-GOV-CAT-002_Record_Catalog.md) §3 for minimum required fields and §4 for canonical record names, owners, triggers, and evidence value. Use the source procedure or template named in CAT-002 for record-specific fields.

| Flow | Primary CAT-002 record | Source of detailed fields |
|---|---|---|
| F-01 Control Intent | Control Implementation Record | CAT-002 §4.1; CB-001; FLOW F-01 evidence plan |
| F-02 Project Intake | Project Security Review Record; Threat Model Record | PRC-AR-001; PRC-TM-001; TMPL-AR-001 where used |
| F-03 Asset Registration | Asset Inventory Record; Asset Coverage Record | STD-AM-001; FLOW F-03 coverage requirements |
| F-04 Finding Treatment | Finding Record; Risk Register Entry; Security Exception Record; Risk Acceptance Record | PRC-VM-001; PRC-RM-001; TMPL-RM-002; TMPL-RM-004 |
| F-05 Change & Release | Security Change Review Record | PRC-CHG-001 and local change system fields |
| F-06 Incident Support | IR-owned Incident Record; Lessons Learned Record; Program Improvement Record | PLN-IR-001; PRC-IR-002; PRC-LL-001; CAT-002 incident boundary rules |
| F-07 Metrics & Oversight | Reporting Metric Record; Oversight Decision Record; Program Improvement Record | MTR-001; IMPREG-001; CAT-002 §4.1 |

If a local tool cannot use the CAT-002 canonical name directly, store the canonical record type as a tag, custom field, evidence-index value, or cross-reference. Local names are aliases, not separate record authority.

---

## 20. Recommended Implementation Sequence

### Phase 1
Implement:
- Global contract (§1-6)
- Shared state models (§7)
- Flow F-02 (Project Intake / Architecture Review / Threat Model)
- Flow F-03 (Asset Registration / Coverage Validation)
- Flow F-04 (Finding to Remediation / Exception / Risk)

### Phase 2
Implement:
- Flow F-05 (Change and Release Security Routing)
- Flow F-06 (Incident to Recovery to Standards Feedback)

### Phase 3
Implement:
- Flow F-01 (Control Intent to Implementation)
- Flow F-07 (Metrics, Oversight, and Improvement Routing)

---

## 21. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-FLOW-001 |
| **Version** | 1.4 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed operations |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.4 | 2026-06-18 | Governance Pillar Leader | Converted FLOW record sections into CAT-002 crosswalks, removed local record-template authority, updated primary-record names to CAT-002 canonical records, and clarified alias handling. |
| 1.3 | 2026-06-18 | Governance Pillar Leader | Replaced F-04 competing severity SLA table with PRC-VM SLA authority, removed contradictory closure rules, and aligned residual-risk acceptance with RMF-001 §9.7. |
| 1.2 | 2026-06-18 | Governance Pillar Leader | Rewrote F-06 to preserve Incident Commander / standing IR team authority for active incident operations while defining CERG support, evidence, and post-incident improvement routing. |
| 1.1 | 2026-06-17 | Governance Pillar Leader | Added AI routing rules to F-02, including AI intake, sanctioned-tool register, system/model register, and escalation criteria for sensitive data, regulated scope, consequential decisions, and autonomous agency. |
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Seven cross-pillar operational flows, five shared state models, five minimum record templates, LLM execution directives, and recommended implementation sequence. |

### Review Triggers

- Change to the CERG Operating Model (OM-001)
- Change to the Risk Management Framework (RMF-001)
- Change to the Control Baseline (CB-001)
- Material incident or audit finding that exposes a flow gap
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical roles and pillar structure |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk treatment, exception, and acceptance rules |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control inventory and evidence standards |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Regulatory and framework mapping |
| Metrics and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Metric definitions and reporting cadence |
| Annual Calendar | [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) | Operating rhythm and cadence |
| Architecture Review Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Project intake and architecture review process |
| Artificial Intelligence Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Governs AI use categories, AI-specific threats, sanctioned tools, and shadow AI |
| AI Intake and Sanctioning Template | [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) | Required AI intake record for F-02 where AI is in scope |
| Sanctioned AI Tools Register Template | [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) | Register updated when consumed AI tools are approved |
| AI System and Model Register Template | [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) | Register updated when built or embedded AI systems are approved |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Exception and risk acceptance workflow |
| Incident Response Plan | [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | Standing IR procedures |
