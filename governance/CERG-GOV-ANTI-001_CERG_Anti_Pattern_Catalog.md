## CERG ANTI-PATTERN CATALOG
### Common Failure Modes · Observable Symptoms · Corrective Actions

---

| | |
|---|---|
| **Document ID** | CERG-GOV-ANTI-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) · [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) · [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) · [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) · [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **Review Cycle** | Annual / On material adoption feedback |
| **Frameworks** | NIST CSF 2.0 (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How to Use This Catalog](#2-how-to-use-this-catalog)
3. [Anti-Pattern Index](#3-anti-pattern-index)
4. [Workforce and Role Anti-Patterns](#4-workforce-and-role-anti-patterns)
5. [Capability Anti-Patterns](#5-capability-anti-patterns)
6. [Evidence and Compliance Anti-Patterns](#6-evidence-and-compliance-anti-patterns)
7. [Incident Response Anti-Patterns](#7-incident-response-anti-patterns)
8. [Vendor and Third-Party Anti-Patterns](#8-vendor-and-third-party-anti-patterns)
9. [Risk Management Anti-Patterns](#9-risk-management-anti-patterns)
10. [People and Culture Anti-Patterns](#10-people-and-culture-anti-patterns)
11. [Metrics and Reporting Anti-Patterns](#11-metrics-and-reporting-anti-patterns)
12. [AI Anti-Patterns](#12-ai-anti-patterns)
13. [Organizational Anti-Patterns](#13-organizational-anti-patterns)
14. [Using Anti-Patterns in Program Review](#14-using-anti-patterns-in-program-review)
15. [Document Control](#15-document-control)

---

## 1. Purpose and Scope

CERG is easier to adopt when failure modes are explicit. A good operating model does not only say what right looks like; it also names the patterns that make programs look mature while leaving capability weak, ownership unclear, or evidence unusable.

This catalog collects common CERG anti-patterns across adoption, workforce design, capability development, evidence management, compliance alignment, incident response, vendor oversight, risk management, people and culture, metrics and reporting, AI and automation, and organizational dynamics. It is a teaching artifact and a diagnostic aid. It does not replace the detailed guidance in the source documents; it points adopters to the corrective action and the governing artifact.

An anti-pattern is included when it meets three tests:

1. It is common enough that adopters are likely to encounter it.
2. It creates operational risk, governance confusion, or false confidence.
3. It has a practical correction available inside CERG.

---

## 2. How to Use This Catalog

Use this catalog during implementation planning, quarterly program review, lessons learned, and maturity assessment.

- **Adopters** use it to avoid common failure modes before they become embedded.
- **CISOs and pillar leaders** use it to challenge optimistic status reporting.
- **Governance teams** use it to convert recurring failure modes into improvement items.
- **Auditors and assessors** use it to understand where CERG expects evidence, ownership, and validation.
- **Contributors** use it to identify gaps in the framework itself; if a repeated anti-pattern has no corrective guidance, the corpus needs improvement.

The catalog is intentionally blunt. The goal is not to shame teams. The goal is to make weak operating patterns visible early, when they are still cheap to correct.

---

## 3. Anti-Pattern Index

| ID | Anti-Pattern | Domain | Observable Symptom | Corrective Anchor |
|---|---|---|---|---|
| ANTI-ADOPT-001 | Fork-and-Declare | Adoption | Repository forked, names changed, no operating cadence or evidence | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) |
| ANTI-ADOPT-002 | Delete Roles Instead of Consolidating | Adoption / Workforce | Unstaffed accountabilities disappear from the RACI | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) |
| ANTI-WF-001 | Hero Role | Workforce | One senior person informally owns too many critical functions | [`CERG-GOV-WFP-001`](CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md) |
| ANTI-WF-002 | Title Inflation Instead of Career Pathing | Workforce | Management titles used to retain single-domain experts without management scope | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) |
| ANTI-WF-003 | Accountability Without Capacity | Workforce | A named owner has no time, authority, tooling, or escalation path | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) |
| ANTI-CAP-001 | Capability by Tool Purchase | Capability | A tool is bought and the capability is declared implemented | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) §3 |
| ANTI-CAP-002 | Capability by Meeting | Capability | Meetings exist, but decisions, owners, and evidence do not | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) |
| ANTI-CAP-003 | Capability by Dashboard | Capability | Dashboards show state, but no one acts or validates outcomes | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| ANTI-CAP-004 | Capability Without Validation | Capability | A capability is claimed but has never been tested, sampled, or exercised | [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) |
| ANTI-EVID-001 | Screenshot Theater | Evidence | Screenshots lack scope, owner, timestamp, or control mapping | [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| ANTI-EVID-002 | Pre-Audit Archaeology | Evidence | Evidence is reconstructed immediately before an audit | [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) |
| ANTI-EVID-003 | Policy-as-Evidence | Evidence | A policy statement is used as proof that a control operated | [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| ANTI-COMP-001 | Control Mapping as Control Operation | Compliance | A mapped control is treated as implemented without operating evidence | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) |
| ANTI-COMP-002 | POA&M as Permission Slip | Compliance | Gaps are parked in POA&M with no credible owner, funding, or date | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| ANTI-COMP-003 | Regulation-First Operating Model | Compliance | Teams organize around frameworks instead of reusable capabilities and evidence | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) §12 |
| ANTI-IR-001 | Restore-and-Declare-Resolved | Incident Response | Systems recovered, root cause unidentified, same incident repeats | [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) |
| ANTI-IR-002 | Tabletop Read-Through | Incident Response | Exercise is a script read-aloud with no injects, decisions, or communication breakdowns | [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) |
| ANTI-IR-003 | Incident Commander by Rotation | Incident Response | IC role rotates through people with no authority to make resource calls | [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) · [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) |
| ANTI-VEND-001 | MSSP as Black Box | Vendor | Provider treated as sealed unit; no validation of alert triage or SLA compliance | [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| ANTI-VEND-002 | Questionnaire-as-Due-Diligence | Vendor | 300-question assessment replaces understanding the provider's actual operating model | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| ANTI-VEND-003 | Contract-as-Control | Vendor | SLA language treated as proof of operating capability without measurement | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) |
| ANTI-RISK-001 | Risk Register as Cemetery | Risk | Risks enter the register and never leave; no treatment, reassessment, or trigger | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| ANTI-RISK-002 | Risk Acceptance by Exhaustion | Risk | Risks accepted just to clear queue; no expiration, compensating control, or re-review | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| ANTI-RISK-003 | Quantitative Theater | Risk | Precise ALE/SLE calculations based on unchecked assumptions drive no decision | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| ANTI-PEOPLE-001 | Training-as-Competency | People / Culture | Training completed declared as proof the capability is staffed | [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) |
| ANTI-PEOPLE-002 | Security as the Team That Says No | People / Culture | Security defined entirely by blocking; no enablement, advisory, or fast-lane path | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) |
| ANTI-METRIC-001 | Green Dashboard | Metrics | Thresholds calibrated to always show green; dashboard is compliance theater | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| ANTI-METRIC-002 | Activity as Outcome | Metrics | Activity counts reported as proof of capability effectiveness | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| ANTI-METRIC-003 | Vanity SLA | Metrics | SLA targets set to match observed performance; no stretch, no improvement pressure | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) |
| ANTI-AI-001 | AI-as-Headcount | AI / Automation | AI tool deployed, staffing gap declared closed; no review of AI output or edge cases | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) |
| ANTI-AI-002 | Prompt-as-Policy | AI / Automation | Security decisions outsourced to LLM via single-engineer system prompt with no change management | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) · [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) |
| ANTI-AI-003 | AI Hallucination as Evidence | AI / Automation | LLM-generated compliance mapping or risk assessment enters evidence chain unvalidated | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) · [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| ANTI-ORG-001 | Do-More-with-Less as Strategy | Organizational | Permanent austerity treated as a strategy; no risk acceptance for unfunded mandates | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| ANTI-ORG-002 | Good News Only Chain | Organizational | Bad news filtered at every level; executives surprised by avoidable failures | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) |
| ANTI-ORG-003 | Responsibility Without Authority | Organizational | Role carries accountability but no budget, hiring, or decision power | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) |

---

## 4. Workforce and Role Anti-Patterns

### 4.1 ANTI-WF-001 — Hero Role

**What it looks like:** One senior person informally owns architecture review, risk acceptance preparation, incident support, vendor risk review, evidence quality, and executive reporting. The work gets done because that person is exceptional.

**Why it fails:** The program works only while the hero is present. The capability lives in a person, not in the operating model. When the person is unavailable, leaves, or burns out, handoffs fail and institutional memory disappears.

**Corrective action:** Move the work into explicit roles, procedures, records, and review cadences. Consolidation is allowed, but hidden ownership is not. If one person must cover multiple roles, record the consolidation in the Decision Log and define compensating controls for self-review risk.

### 4.2 ANTI-WF-002 — Title Inflation Instead of Career Pathing

**What it looks like:** A single strong engineer becomes "Manager of Cloud Security" or "Director of Risk" to improve retention, even though they do not manage people, budget, or a multi-team function.

**Why it fails:** The title creates management expectations without management scope. It also hides the real need: a strong SME career path. The organization may end up with inflated titles, unclear authority, and no real management capacity.

**Corrective action:** Use the SME track in [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md). Promote depth and influence as Advisor or Sr. Advisor when the work is expert contribution. Create management roles only when span of control, domain divergence, succession need, or distribution requires one.

### 4.3 ANTI-WF-003 — Accountability Without Capacity

**What it looks like:** A RACI names an owner, but the person has no time allocation, decision authority, tools, budget input, or escalation path. The owner is accountable in the document but powerless in practice.

**Why it fails:** Named ownership without capacity is symbolic governance. It creates a false sense that the work is covered while guaranteeing overdue actions, unreviewed evidence, and quiet risk acceptance by neglect.

**Corrective action:** Every accountable role must have enough capacity, authority, and escalation support to perform the work. If capacity is unavailable, reduce scope, defer the capability explicitly, automate part of the workflow, or escalate for staffing and budget. Do not mark the role covered merely because a name appears in the table.

---

## 5. Capability Anti-Patterns

### 5.1 ANTI-CAP-001 — Capability by Tool Purchase

**What it looks like:** The organization buys a SIEM, scanner, GRC platform, CSPM, SSPM, or ticketing workflow and declares the related capability implemented.

**Why it fails:** Tools support capabilities; they do not create them. Detection requires telemetry, tuned analytics, triage ownership, response paths, and validation. Exposure management requires coverage, prioritization, owner follow-up, SLA tracking, and treatment decisions. Governance requires decision rights, evidence quality, review cadence, and accountable owners.

**Corrective action:** For each tool, name the capability it supports, the procedure it feeds, the owner who acts on its output, and the evidence that proves the capability operates. If those outputs are absent, the capability is still Ad Hoc.

### 5.2 ANTI-CAP-002 — Capability by Meeting

**What it looks like:** A weekly risk meeting, architecture review board, or compliance sync exists, so leaders believe the capability is operating.

**Why it fails:** Meetings are coordination mechanisms, not evidence of capability. A meeting that produces no decision, no owner, no due date, no evidence link, and no follow-up is operational theater.

**Corrective action:** Every recurring CERG meeting must produce one or more operational records: decision log entry, risk record update, finding update, evidence request, exception decision, improvement item, or escalation. If a meeting does not produce records, redesign or cancel it.

### 5.3 ANTI-CAP-003 — Capability by Dashboard

**What it looks like:** A dashboard shows vulnerability counts, alert volume, compliance percentages, or project queue status. Because the dashboard exists, the capability is treated as mature.

**Why it fails:** Dashboards report state. They do not prove that the organization can act. A metric without owner action, threshold logic, and escalation path becomes passive observation.

**Corrective action:** Tie each dashboard metric to an owner, threshold, decision rule, and corrective action path. If a metric crosses a threshold and nothing happens, the metric is decorative, not operational.

### 5.4 ANTI-CAP-004 — Capability Without Validation

**What it looks like:** The organization claims detection, recovery, segmentation, vendor response, or evidence retrieval capability, but the capability has never been tested, sampled, exercised, or independently reviewed.

**Why it fails:** Untested capability is an assumption. The gap usually appears during an incident, audit, or executive deadline, when correction is most expensive.

**Corrective action:** Define a validation method for each material capability: adversarial validation, tabletop exercise, evidence spot-check, restore test, sample audit, control effectiveness test, or automated re-validation. The maturity level is capped by the weakest unvalidated link.

---

## 6. Evidence and Compliance Anti-Patterns

### 6.1 ANTI-EVID-001 — Screenshot Theater

**What it looks like:** Evidence folders contain screenshots with no timestamp, no scope statement, no accountable owner, no system identifier, and no control mapping.

**Why it fails:** Screenshots can be useful supporting evidence, but unmanaged screenshots prove little. They are hard to validate, easy to misread, and often impossible to tie to a control period.

**Corrective action:** Evidence must be dated, attributable, scoped, relevant, complete, and retrievable. Use screenshots only when they are linked to a control, system, period, and owner, and when no stronger system export or record exists.

### 6.2 ANTI-EVID-002 — Pre-Audit Archaeology

**What it looks like:** Evidence is assembled weeks before an audit by searching shared drives, asking engineers for exports, and reconstructing decisions from chat history.

**Why it fails:** Evidence reconstructed under audit pressure is incomplete, inconsistent, and expensive. It also proves the program is not producing evidence as a byproduct of normal operations.

**Corrective action:** Use the evidence calendar, record catalog, and audit procedure to collect evidence on cadence. If evidence cannot be retrieved without heroics, create a Program Improvement Register entry.

### 6.3 ANTI-EVID-003 — Policy-as-Evidence

**What it looks like:** A policy says access reviews, backups, logging, or risk reviews must happen, so the control is marked implemented.

**Why it fails:** A policy proves intent. It does not prove operation. Auditors and leaders need evidence that the activity occurred, exceptions were handled, and outcomes were reviewed.

**Corrective action:** Pair every policy requirement with operating evidence: review record, log export, ticket, register update, test result, or approval record. Use policy as design evidence, not operating evidence.

### 6.4 ANTI-COMP-001 — Control Mapping as Control Operation

**What it looks like:** A control is mapped to NIST, CMMC, NERC-CIP, SOX, or ISO and is therefore treated as mature.

**Why it fails:** Mapping proves alignment intent. It does not prove that the control is designed, operating, evidenced, or effective.

**Corrective action:** Treat mapping as the start of the evidence chain. A mapped control still needs owner, implementation path, operating record, evidence quality, and validation.

### 6.5 ANTI-COMP-002 — POA&M as Permission Slip

**What it looks like:** Every gap becomes a POA&M item, but the item has no credible owner, funding, schedule, dependency plan, or evidence of progress.

**Why it fails:** A POA&M is a plan for closing a gap, not permission to ignore it. Weak POA&Ms create the appearance of management while preserving the exposure.

**Corrective action:** Every POA&M item must have an owner, target date, funding or capacity path, interim risk treatment, and progress evidence. Stale POA&M items must promote to risk or executive escalation.

### 6.6 ANTI-COMP-003 — Regulation-First Operating Model

**What it looks like:** Separate teams, evidence stores, calendars, and status reports are built for each framework: one for CMMC, one for SOX, one for NERC-CIP, one for ISO.

**Why it fails:** The organization duplicates work and confuses ownership. Operators experience compliance as multiple parallel asks rather than one evidence-producing operating model.

**Corrective action:** Build reusable capabilities and evidence factories first. Map the resulting evidence to frameworks through the Compliance Matrix and regulatory operational packages. Compliance should reuse operational evidence, not create a parallel universe.

---

## 7. Incident Response Anti-Patterns

CERG treats incident response as an adjacent function owned by the standing IR team. The patterns below describe failure modes in the CERG / IR boundary — how CERG capabilities support IR through evidence provision, asset and exposure context, lessons-learned routing, and procedure synchronization. They are not intended as an IR governance framework; the Incident Response Plan ([`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)) and playbook set ([`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md)) serve that role.

### 7.1 ANTI-IR-001 — Restore-and-Declare-Resolved

**What it looks like:** Systems are restored, the incident ticket is closed, and remediation is declared complete. Root cause analysis is skipped or deferred. Lessons learned are not conducted. Procedure updates are not made. The same incident pattern repeats the next quarter.

**Why it fails:** Restoring service is the first step, not the last. Without root cause, evidence preservation, procedure improvement, and capability validation, the organization learns nothing from the incident. It becomes a treadmill of repeat events with no maturity gain.

**Corrective action:** Every material incident must complete a full lifecycle: containment, eradication, root cause identification, evidence preservation, lessons learned, and procedure update. Use the incident response playbook at [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) as the procedural anchor. Tie closure criteria to completed actions, not just uptime.

### 7.2 ANTI-IR-002 — Tabletop Read-Through

**What it looks like:** The incident response exercise is a group of people sitting in a room reading a script aloud. No injects, no time pressure, no decision forks, no communication breakdowns to work through. Everyone leaves believing the IR capability is tested.

**Why it fails:** A script read-through exercises reading comprehension, not incident response. Real incidents require decision-making under uncertainty, role delegation under pressure, and communication across fragmented channels. A passive exercise surfaces none of these failure modes.

**Corrective action:** Design tabletop exercises with injects that force decisions, communication gaps that require status-update discipline, and time constraints that simulate real incident pressure. Use the validation framework at [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) to define exercise design standards. After the exercise, produce a findings register, not just a sign-in sheet.

### 7.3 ANTI-IR-003 — Incident Commander by Rotation

**What it looks like:** The Incident Commander role rotates through a pool of people who have no budget authority, no override on business decisions, no practiced escalation path, and no delegated decision rights. During a real event, the IC becomes a note-taker who must seek approval for every material decision.

**Why it fails:** An IC who cannot commit resources, authorize containment actions, or override normal business approval cycles cannot command the response. The bottleneck shifts from technical response to managerial approval, and containment timelines slip.

**Corrective action:** Define IC authority explicitly in the Incident Response Plan ([`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)) and service-level commitments at [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md), with IC role boundaries and delegation rules documented in the operating model at [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md). The IC must have pre-delegated authority to commit resources, authorize containment, and make risk decisions within defined thresholds during an active incident. Test this authority in exercises, not only in the policy document.

---

## 8. Vendor and Third-Party Anti-Patterns

### 8.1 ANTI-VEND-001 — MSSP as Black Box

**What it looks like:** Security operations are outsourced to an MSSP, and the internal team treats the provider as a sealed unit. No validation that the MSSP is triaging alerts to standard. No evidence sampling. No SLA compliance verification. The capability is declared mature because the contract exists.

**Why it fails:** A contract covers liability and terms of service. It does not guarantee that detection, triage, escalation, and reporting are operating effectively. Without validation, the organization cannot distinguish between a working SOC and a quiet one. The gap appears during an incident or audit.

**Corrective action:** Treat the MSSP as a capability provider with measurable outputs, not a black box. Validate evidence quality at defined intervals per [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md): sample closed alerts for triage quality, verify escalation SLAs independently, conduct joint exercises that test handoffs. Define the internal team's oversight and validation role explicitly in the RACI.

### 8.2 ANTI-VEND-002 — Questionnaire-as-Due-Diligence

**What it looks like:** Third-party risk assessment consists of sending a 300-question questionnaire to every vendor. The questionnaire is filled out by the provider's sales engineering team, filed in a shared drive, and never reviewed against operational evidence.

**Why it fails:** A questionnaire captures self-reported intent, not operating reality. It tells you what the vendor says they do, not what they actually do. It is also point-in-time: by the time the next assessment cycles, the vendor's operating environment, staffing, and tooling may have changed entirely.

**Corrective action:** Use questionnaires as the starting point, not the whole assessment. Combine them with evidence-based validation: review audit certificates, sample operational evidence, conduct joint exercises, and verify SLA performance against actual records. The TPRM procedure at [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) defines the tiers and evidence expectations. A questionnaire alone is sufficient only for the lowest-risk tier.

### 8.3 ANTI-VEND-003 — Contract-as-Control

**What it looks like:** "The SLA says 15-minute response time for critical alerts." This contract language is presented as proof that the control is operating. No one measures actual response times. No one reviews SLA breach reports. No one tests whether the provider can actually staff to that SLA during holidays, weekends, or concurrent events.

**Why it fails:** A contract term proves intent, not operation. SLAs that are not measured, reported, and enforced are aspirational text. The gap is invisible until the provider misses a critical alert and the contract language is tested in a post-incident review rather than through routine oversight.

**Corrective action:** Every SLA in a provider contract must have a corresponding measurement, reporting cadence, breach escalation, and periodic validation. Use the service-level commitment framework at [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) to define the oversight model. Conduct periodic SLA stress tests: can the provider actually meet response targets during concurrent incidents, after-hours, or staffing transitions?

---

## 9. Risk Management Anti-Patterns

### 9.1 ANTI-RISK-001 — Risk Register as Cemetery

**What it looks like:** Risks enter the register and never leave. No treatment tracking, no reassessment cadence, no closure criteria, no retirement process. The register grows with every quarterly review but no risk is ever retired, accepted, or mitigated to closure. The oldest entries become noise that drowns out current concerns.

**Why it fails:** This is a lifecycle and closure failure, distinct from a cadence failure (where risks exist but are never reviewed). A cemetery register may be reviewed quarterly yet still accumulate — entries are discussed but never resolved. It becomes an inventory problem rather than a risk management tool. Owners stop distinguishing material from stale, and material risks are buried under entries that should have been closed, accepted, or escalated long ago.

**Corrective action:** Every risk in the register must have a treatment plan, reassessment interval, and exit criteria. Use the risk management framework at [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) to define lifecycle stages. Archive or close risks whose circumstances have changed. If a risk has had no owner action for two consecutive review cycles, escalate it as a governance concern.

### 9.2 ANTI-RISK-002 — Risk Acceptance by Exhaustion

**What it looks like:** A risk is escalated repeatedly through reviews. Eventually, someone accepts it not because the residual risk is tolerable, but because the escalation is exhausting, the queue is full, and accepting clears a blocker. The acceptance has no expiration date, no compensating control requirement, and no re-review trigger.

**Why it fails:** Acceptance by exhaustion is not risk management; it is queue management. It creates a register full of accepted risks that were never genuinely evaluated as tolerable. The exposure remains, but the governance trail makes it look managed.

**Corrective action:** Every risk acceptance must have an expiration date, documented compensating controls, a named reviewer, and a re-review trigger. Use the risk acceptance template in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md). If an acceptance has no expiration, it is not an acceptance; it is an unresolved risk with a label. Escalate expired acceptances to the next governance level.

### 9.3 ANTI-RISK-003 — Quantitative Theater

**What it looks like:** Annualized Loss Expectancy (ALE) and Single Loss Expectancy (SLE) are calculated to two or three decimal places for every identified risk. The model's assumptions are unchecked. The inputs are guessed or benchmarked from industry reports that do not reflect the organization's context. The output is presented with the authority of a financial calculation but drives no decision.

**Why it fails:** Quantitative precision creates the appearance of rigor without the substance. A precise estimate built on guessed inputs is less honest than a qualitative ordinal rating with a stated rationale. The energy goes into the arithmetic rather than the assumptions, treatment options, and decision.

**Corrective action:** Use quantitative methods only when the inputs are based on observable data relevant to the organization's environment. Otherwise, use qualitative ordinal ratings with clear anchor definitions and a stated decision rule. The risk framework at [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) provides both approaches and prescribes when each is appropriate. Invest modeling energy in assumptions, sensitivity ranges, and treatment analysis instead of decimal places.

---

## 10. People and Culture Anti-Patterns

### 10.1 ANTI-PEOPLE-001 — Training-as-Competency

**What it looks like:** Someone completed the annual security awareness training module, passed the quiz, and received the certificate. The organization marks the related capability as staffed and trained. No assessment of whether the person can actually perform the procedure under pressure, distinguish normal from anomalous, or make a sound security decision without a playbook.

**Why it fails:** Training completion proves attendance, not competency. It does not assess whether the person can apply the knowledge in context, make judgment calls, or perform under operational conditions. A team of trained-but-not-competent people looks compliant on paper but fails under stress.

**Corrective action:** Define competency expectations per role using the competency model at [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md). Pair training with demonstrated assessment: simulation, observed procedure walkthrough, scenario-based evaluation, or peer review. Use training completion as a prerequisite, not as the full measure of readiness.

### 10.2 ANTI-PEOPLE-002 — Security as the Team That Says No

**What it looks like:** The security function is defined entirely by blocking: blocking tools, blocking vendor approvals, blocking project timelines, blocking access requests. Every interaction with security begins with a denial or a delay. There is no enablement path, no advisory capability, no fast lane for compliant innovation.

**Why it fails:** A security team defined by blocking becomes a bottleneck. Business units learn to route around security — hiding projects, making exceptions without review, or self-attesting compliance. The organization loses visibility and the security team loses credibility.

**Corrective action:** Define the security function as both gate and guide. For every control or review point, provide an enablement path: a pre-approved pattern, a self-service check, an advisory consultation, or an expedited exception process. Use the operating model at [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) to define security's advisory and enablement responsibilities alongside its control responsibilities. Track the ratio of enabled-to-blocked decisions as a health metric.

---

## 11. Metrics and Reporting Anti-Patterns

### 11.1 ANTI-METRIC-001 — Green Dashboard

**What it looks like:** Every metric on the dashboard is green. All thresholds are within range. The dashboard is presented quarterly to leadership as evidence that the program is healthy. No one asks why nothing is ever yellow or red.

**Why it fails:** A dashboard that never shows degradation is not measuring operational reality; it is calibrated to always report success. Thresholds are set wide enough that nothing triggers, or the metrics are selected to reflect activity rather than outcomes. The dashboard becomes a compliance artifact instead of an operational tool.

**Corrective action:** Set metric thresholds so that yellow and red states are reachable and meaningful. A healthy program should occasionally cross yellow thresholds during routine variation; if it never does, the thresholds are too loose. Tie each metric to a decision rule: at red, a specific escalation or corrective action is triggered. Use the metrics framework at [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) for threshold design.

### 11.2 ANTI-METRIC-002 — Activity as Outcome

**What it looks like:** The security report features metrics like "scans run: 2,400," "alerts triaged: 850," "training modules completed: 1,200." These activity counts are presented as proof that security capabilities are operating effectively.

**Why it fails:** Activity measures effort, not effectiveness. Running 2,400 scans means nothing if critical vulnerabilities are not being remediated. Triaging 850 alerts means nothing if triage quality is poor or the same alert fires 800 times. Activity metrics create the illusion of productivity without answering the question: is the outcome improving?.

**Corrective action:** Pair every activity metric with an outcome metric. Scans run should pair with mean-time-to-remediate and recurrence rate. Alerts triaged should pair with time-to-triage, false-positive rate, and incidents detected. Training completed should pair with demonstrated competency or reduced security incidents from human error. Use the reporting guidance at [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) for outcome-oriented metric design.

### 11.3 ANTI-METRIC-003 — Vanity SLA

**What it looks like:** SLA targets are set to match observed performance. If the team currently resolves critical incidents in four hours on average, the SLA is set to four hours. The target confirms current behavior rather than driving improvement. The SLA is always met and never challenged.

**Why it fails:** An SLA that matches current performance does not create accountability or improvement pressure. It is a vanity target: it makes the dashboard look good while the organization stagnates. The gap between where the capability is and where it needs to be is invisible.

**Corrective action:** Set SLA targets based on business risk tolerance and capability maturity goals, not historical averages. Use benchmarking, business impact analysis, and maturity targets. A well-set SLA should require process improvement to achieve consistently. Use the service-level commitment framework at [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) for target-setting methodology. Review SLA targets annually as capability matures.

---

## 12. AI Anti-Patterns

### 12.1 ANTI-AI-001 — AI-as-Headcount

**What it looks like:** An AI code scanner, AI SOC analyst, AI GRC assistant, or AI compliance-mapping tool is deployed. The organization declares the related staffing gap closed. No one is assigned to review the AI's output, handle edge cases it cannot resolve, or take responsibility for its false negatives. The tool is treated as equivalent to a human operator.

**Why it fails:** AI tools augment capability; they do not create independent capability. An AI code scanner finds the patterns it was trained to find and misses everything else. An AI SOC analyst cannot exercise judgment about novel attack patterns, handle communication with stakeholders, or take responsibility for a missed detection. Treating AI as headcount creates capability gaps that are invisible until they fail.

**Corrective action:** For every AI tool, define the human oversight role, edge-case handling path, false-negative review cadence, and accountability assignment. Use the AI security standard at [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) for AI use categorization, output review requirements, and model governance, and the capability model in [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) §3 to distinguish tool support from capability ownership. An AI tool reduces workload; it does not replace accountable ownership.

### 12.2 ANTI-AI-002 — Prompt-as-Policy

**What it looks like:** Security decisions are delegated to a language model via a system prompt written by one engineer. The prompt determines mapping decisions, risk scoring criteria, control assertions, or evidence classification. There is no change management for the prompt, no version control, no review, and no audit trail for what the model actually decided in any given case.

**Why it fails:** A prompt is not a policy. It is a set of natural-language instructions that an LLM interprets probabilistically. Without change control, the prompt drifts silently. Without audit, the organization cannot reconstruct why a particular decision was made. The model's output may look authoritative while being consistently wrong in ways that are hard to detect.

**Corrective action:** Treat AI system prompts as controlled artifacts subject to the same change management and audit requirements as written policy. Version-control prompts, require review before deployment, and maintain an audit trail linking each model output to the prompt version used. The AI security standard at [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) provides AI use categories and governance requirements; the audit and evidence procedure at [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) defines the change management and audit processes for prompt governance.

### 12.3 ANTI-AI-003 — AI Hallucination as Evidence

**What it looks like:** An LLM generates a compliance mapping, risk assessment, control description, or evidence summary. The output looks plausible, uses the right terminology, and cites reasonable-seeming references. It is entered into the evidence chain without validation. No one checks whether the mapping is correct, the risk assessment is accurate, or the cited sources actually say what the model claims.

**Why it fails:** LLMs produce plausible-sounding outputs that can be factually wrong in subtle ways. A hallucinated compliance mapping can misrepresent audit posture. A hallucinated control description creates a false evidence record. Once in the evidence chain, errors propagate across reviews, audits, and decisions. The organization discovers the error during an audit or incident, when correction is most expensive.

**Corrective action:** Every AI-generated artifact that enters the evidence chain must be validated by a competent human reviewer before acceptance. The AI security standard at [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) defines AI output review requirements and AI use categories; the evidence quality standard at [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) defines evidence chain hygiene. Define validation criteria per artifact type: for compliance mappings, spot-check a sample against the source framework; for risk assessments, verify factual claims against system data; for evidence summaries, trace each claim to an originating record. Treat AI-generated evidence as draft evidence requiring review, not as final evidence.

---

## 13. Organizational Anti-Patterns

### 13.1 ANTI-ORG-001 — Do-More-with-Less as Strategy

**What it looks like:** "We need to do more with less" is repeated as a strategic direction every budget cycle. Security scope expands — new regulations, new tool categories, new threat vectors — but headcount and budget remain flat or shrink. No explicit risk acceptance is documented for the resulting gaps. The team absorbs the workload until burnout, attrition, or a material failure forces acknowledgment.

**Why it fails:** "Do more with less" is not a strategy; it is the absence of one. It conflates efficiency with scope creep and treats unfunded mandates as acceptable. Without a documented risk acceptance for the gap between assigned scope and available capacity, the organization is operating with invisible risk. The failure, when it comes, will be attributed to execution rather than to the strategic decision to underfund.

**Corrective action:** When scope increases without corresponding capacity, require an explicit risk acceptance or exception per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md). Document the gap between assigned responsibilities and funded capacity. Prioritize and defer explicitly rather than absorbing silently. A team cannot do everything; a well-run program documents what it is not doing and why.

### 13.2 ANTI-ORG-002 — Good News Only Chain

**What it looks like:** Bad news is filtered at every level of the organization before it reaches executives. Team leads smooth over findings before reporting up. Managers present optimistic timelines. Pillar leaders frame risks as manageable. By the time information reaches leadership, every signal is green. Executives are consistently surprised by avoidable failures.

**Why it fails:** A culture that filters bad news destroys decision quality. Executives make resource, priority, and risk-acceptance decisions based on incomplete data. Surprise failures erode trust and trigger reactive over-correction that is more expensive than the original gap. The filtering is rarely malicious; it is a learned behavior from a culture that rewards good news and penalizes the messenger.

**Corrective action:** Design reporting chains that surface bad news early. Require pillar leaders to present one material risk or finding at each executive review, not only achievements. Protect and reward people who raise issues early. Use the operating model at [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) to design escalation paths that by-pass the filtering chain when a finding meets materiality thresholds. Track the ratio of early-reported to late-discovered issues as a culture health metric.

### 13.3 ANTI-ORG-003 — Responsibility Without Authority

**What it looks like:** A role carries accountability for a security capability — risk management, evidence quality, third-party oversight — but has no budget control, no hiring authority, no decision rights over the systems or processes that determine the outcome. The person is responsible for the result but cannot change the inputs.

**Why it fails:** Responsibility without authority is a failure of role design. It creates frustration, turnover, and capability stagnation. The person in the role can report problems but cannot fix them. The gap between what the role is accountable for and what it can control is invisible in the RACI but visible in the outcomes.

**Corrective action:** For every accountable role, audit the authority it needs to fulfill its accountabilities: budget input, staffing input, decision rights, tool access, escalation path, and veto power over changes that affect the capability. If authority is missing, either grant it or reduce the accountability scope. Use the RACI instrument at [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) to document the authority profile alongside the accountability assignment.

---

## 14. Using Anti-Patterns in Program Review

During quarterly program review, ask each pillar leader to identify any anti-patterns currently present in their scope. For each selected anti-pattern, record:

| Field | Description |
|---|---|
| Anti-pattern ID | The catalog ID, e.g., ANTI-CAP-003 |
| Affected capability or workflow | The capability, procedure, or team where the pattern appears |
| Evidence observed | What shows the pattern is present |
| Risk created | The operational or governance risk the pattern creates |
| Corrective action | The specific change to role, procedure, evidence, tooling, or cadence |
| Owner and due date | Named owner and target closure |
| Tracking record | Risk record, finding, exception, or Program Improvement Register item |

If the same anti-pattern appears in two consecutive reviews, it must be tracked as a program improvement item. If it appears in three consecutive reviews, it is a maturity constraint: the affected capability cannot score above Defined until the pattern is corrected.

---

## 15. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-ANTI-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Effective Date** | 2026-06-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On material adoption feedback |
| **Next Scheduled Review** | 2027-06-27 |
| **Frameworks** | NIST CSF 2.0 (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.1 | 2026-06-27 | Governance Pillar Leader | Expanded catalog from 15 to 35 anti-patterns across 7 new domains: incident response, vendor and third-party management, risk management, people and culture, metrics and reporting, AI governance, and organizational dynamics. Updated Supporting Documents, Frameworks, TOC, corrective anchors, and Related Documents. |
| 1.0 | 2026-06-24 | Governance Pillar Leader | Initial release. Establishes the cross-domain anti-pattern catalog, including workforce, capability, evidence, and compliance failure modes. |

### Review Triggers

- Adoption feedback identifies a recurring failure mode not represented here
- A lessons-learned review identifies a systemic operating-model weakness
- A maturity assessment finds repeated capability overstatement
- A new CERG artifact introduces an anti-pattern callout that should be registered centrally
- An emerging technology introduces a new class of capability confusion (e.g., new AI patterns)
- Direction from the CISO or Governance Pillar Leader

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Adoption Safety Guide | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) | Source of adoption anti-patterns and safety rules |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Capability model and evidence-factory framing |
| Job Architecture and Grade Framework | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Workforce and career-path corrective guidance |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk lifecycle, acceptance, and quantitative rigor guidance |
| Evidence Quality Standard | [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) | Evidence anti-pattern corrective guidance |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Compliance mapping and evidence reuse guidance |
| Service Level Commitments | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) | SLA design, measurement, and validation guidance |
| Metrics Dashboard and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Metric design and outcome-oriented reporting guidance |
| Capability Maturity and Effectiveness | [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) | Validation method guidance for tabletop exercises and capability testing |
| Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Security role definition, advisory function, and reporting-chain design |
| Consolidated Roles and RACI | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Role accountability, authority profile, and separation of duties |
| Competency Model and Behavioral Anchors | [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Role-specific competency expectations and demonstrated-assessment guidance |
| Program Improvement Register | [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) | Tracks recurring anti-pattern correction actions |
| AI Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | AI use categorization, output review, model governance, and prompt governance requirements |
| Incident Response Plan | [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | IR governance framework, IC authority, and role boundaries |
| Incident Response Playbook Set | [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) | IR lifecycle guidance for restore-and-declare anti-pattern |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Prompt governance and AI-generated evidence handling procedure |
| Third Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor risk assessment tiers and evidence expectations |

---
