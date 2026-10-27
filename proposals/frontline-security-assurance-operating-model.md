# Frontline Security Assurance Operating Model

### Proposal · Companion to the second-line operating model

| | |
|---|---|
| **Proposal reference** | FLA-PROPOSAL-001 |
| **Status** | Proposed — not approved framework content |
| **Owner** | cragin-security |
| **Date** | 2026-10-27 |
| **Classification** | Public |
| **Scope** | NERC CIP and BES operations, plus general IT/OT environments where a second line depends on first-line execution |
| **Companion documents** | [OM-001](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) · [RMF-001](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) · [STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [PLN-CIP-001](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) |

> **Proposal status.** This document carries no CERG document identifier and is not registered
> in the document catalog. It is a candidate contribution to the framework, not normative
> content. Cite it as a draft in proposals and statements of work until it is accepted.

> **Bottom line:** Grid reliability and security share the same objective — a resilient,
> defensible, available grid. This operating model replaces ad-hoc security requests to
> frontline teams with a structured contract: second line defines the control outcome and
> minimum evidence; first line owns safe execution; architecture and tooling own supported
> patterns; the accountable risk owner decides when tradeoffs conflict.
>
> This is not a compliance checklist. It is a practical way of working that explicitly
> accounts for safety, reliability, vendor constraints, and maintenance windows — because
> those are security inputs, not objections to security.
>
> **Implementation sequence:** (1) agree the model and decision rights, (2) define the
> crown-jewel scope, (3) pilot one operational area and one security domain, (4) automate
> core data feeds, (5) establish the feasibility review and exception workflow, (6) expand
> by tier and maturity.

---


## Purpose

A structured set of requests (outcomes, not procedures) from second-line cybersecurity to
first-line IT/OT operations teams managing NERC CIP and broader security controls. Each entry
defines what is needed, from where, how often, in what format, and how completeness is
verified. This replaces ad-hoc "please be CIP compliant" requests with a repeatable contract.

It is intended to protect grid reliability and security at the same time. It is **not** a
mandate to deploy a particular security product or to prioritize reporting over safe
operations.

---

## Core message

> Second line defines the security outcome, minimum evidence, and risk threshold.  
> First line owns safe execution and operational evidence.  
> Architecture and tooling teams provide approved, supportable implementation patterns and
> data integrations.  
> When security, reliability, or operational feasibility conflict, the accountable risk
> owner makes the documented decision.

A reported gap is not automatically a frontline failure. A gap may reflect an architecture
limitation, tooling limitation, vendor constraint, safety concern, maintenance-window
constraint, staffing constraint, or accepted residual risk. Each gap must have an
accountable owner, disposition, and review date.

---

## Regulatory note

CIP mappings in the underlying contract should be treated as indicative references and
reviewed by the organization's compliance and legal functions against the applicable
standards, registered scope, and approved internal interpretations. The operating model is
intended to improve control effectiveness and evidence quality; it is not a substitute for
formal regulatory interpretation.

---

## 1. Operating principles

1. **Outcome before product.** The contract specifies the required security outcome and evidence. It should not prescribe Tool A unless an approved enterprise standard requires it. SAP/CMDB, Industrial Defender, Tenable, Tanium, SentinelOne, Nozomi, Xonius, Armis, Tufin, FireMon, and similar platforms are examples of possible evidence sources.
2. **Reliability and safety are security inputs.** OT/grid operational constraints are evaluated explicitly; they are not treated as informal objections or automatic exceptions.
3. **One source of truth for each data element.** A discovery platform may find an asset, while the CMDB is authoritative for ownership and classification. The contract must identify which source governs each field.
4. **Automate evidence where feasible.** Second line should consume controlled dashboards, APIs, or scheduled exports rather than require recurring screenshots or manual report assembly.
5. **Risk-tiered assurance.** Crown-jewel, high-impact, and critical OT systems receive the highest coverage, cadence, and escalation expectations. General IT is managed proportionately.
6. **Exceptions are managed risk, not permanent status.** Every exception has compensating controls, a business/risk owner, an expiry, and a remediation or replacement plan.
7. **No metric without decision rights.** Teams must not be measured against a target they lack the authority, funding, tooling, or operational opportunity to achieve.
8. **Second line challenges; it does not silently become first line.** Second line defines control intent, assesses evidence quality and effectiveness, challenges risk decisions, trends performance, and escalates unresolved risk. It does not operate tools or own routine remediation.

---

## 2. Roles and decision rights

| Group | Primary responsibilities |
|---|---|
| **Internal first-line service owner** | Accountable for the operated security service — scope, funding, performance, remediation execution, and operational records. Remains accountable when a contracted provider performs the work: the owner is accountable, the provider is responsible. |
| **Operational/grid teams** | Own system availability and safe operation; approve maintenance windows and operational changes; identify safety, reliability, and vendor constraints. |
| **First-line security/control operators** | Execute controls and operate security services — internal staff, a managed security service provider, or a hybrid of both; maintain operational records; remediate within assigned authority; provide complete, timely evidence; escalate material gaps. |
| **Cybersecurity tooling and architecture** | Provide approved reference architectures, supported implementation patterns, integrations, and platform capacity. Define the telemetry each control requires and validate whether it is complete. Does not administer production security tooling or restore failed connectors — that is the operator's work. |
| **Second-line cybersecurity** | Define outcomes and minimum assurance evidence; validate completeness and effectiveness; perform independent challenge; aggregate trends; facilitate risk decisions; escalate unresolved issues. |
| **Compliance/legal** | Maintain approved regulatory interpretation, evidence expectations, reporting obligations, and retention requirements. |
| **Accountable business/risk owner** | Decides whether to fund remediation, accept time-bound residual risk, or select among feasible risk-treatment options. |

### Decision rule

Second line may identify that a control outcome is not met and may challenge the sufficiency of compensating controls. The accountable business/risk owner makes the residual-risk decision. Architecture and operations jointly determine whether a proposed technical pattern is safe and supportable.

A contracted provider changes who performs the work, not who is accountable. Where a managed security service provider or outsourced operator runs a service, the internal first-line service owner remains accountable for scope, performance, and treatment, and second line still validates independently. The assurance question is never whether the provider delivered its contract; it is whether the control outcome holds.

Because a provider's scale exceeds what most adopting organisations can build internally, the interface in Section 3 is written to double as a statement-of-work exhibit: every field can be marked as a provider obligation or a client obligation, and ambiguity is settled at contract rather than after an incident.

### Dispute escalation path

When second-line cybersecurity and the accountable business/risk owner disagree on residual risk acceptance:

1. **Document the dispute.** The specific control outcome, gap, compensating controls, the risk owner's rationale, and second line's challenge rationale are recorded in a decision record (see Section 7 for the format).
2. **Escalate to CISO (or delegate).** Second line elevates the documented dispute to the CISO. The CISO reviews the record and either concurs with the risk owner, directs additional compensating controls, or escalates to the executive risk committee.
3. **Final decision.** The CISO (or executive risk committee, if escalated) makes the binding residual-risk decision. The decision, rationale, and any conditions are documented and retained as an assurance record.
4. **Expedited path for active or imminent risk.** When the dispute involves an actively exploited vulnerability, uncontained malware, or material control failure on a crown-jewel asset, second line may request an interim risk treatment (e.g., temporary containment) within 24 hours while the formal escalation proceeds.

The escalation path is not a failure of the operating model. It is the operating model's release valve when aligned good-faith judgment reaches a genuine impasse.

---

## 3. Control request template

Each request in the frontline contract should use this structure.

| Field | Description | Stage |
|---|---|---|
| **Control objective** | The security outcome required -- not the preferred tool or product. | Foundational |
| **Applicability** | Asset tiers, environments, system types, and CIP scope to which it applies. | Foundational |
| **Minimum assurance evidence** | Smallest set of fields and evidence second line requires to assess the outcome. | Foundational |
| **Control owner** | Team accountable for performing the control. | Foundational |
| **Exception path** | Required compensating controls, risk owner, approval, expiry, and review cadence. | Foundational |
| **Independent observability and re-test rights** | Access second line needs to test the outcome rather than accept a report: raw telemetry read access, the right to sample or replay, and the population to be sampled. | Established |
| **Cadence and event triggers** | Continuous feed, periodic review, and conditions requiring immediate escalation. | Established |
| **Quality checks** | Completeness, freshness, reconciliation, and validation requirements. | Established |
| **Indicative regulatory cross-reference** | A compliance-reviewed mapping; not a substitute for the approved regulatory interpretation. | Established |
| **Approved implementation patterns** | Supported ways to meet the outcome, including compensating-control patterns where appropriate. | Established |
| **Operational constraints** | Safety, availability, vendor, protocol, staffing, maintenance-window, or architecture conditions that could affect implementation. | Established |
| **Platform owner** | Team accountable for the enabling tool, service, connector, or reference architecture. | Target |
| **Data owner / authoritative source** | Owner and source for each required data element. | Target |

Use **“minimum assurance evidence”** rather than “required fields” where possible.

### Mapping to the second-line boundary RFC §5

The boundary RFC lists the fields a first-line service interface must capture. The table above is the request-level form of the same instrument. Correspondence:

| Boundary RFC §5 field | Field in this template |
|---|---|
| Internal first-line service owner | Control owner |
| Operating party and service model | Control owner (internal, contracted, or hybrid) |
| In-scope assets, environments, exclusions | Applicability |
| Operational activities and boundaries | Control objective and Operational constraints |
| Service targets and escalation path | Cadence and event triggers |
| Required operational records and evidence location | Minimum assurance evidence and Quality checks |
| Production-change and acceptance authority | Operational constraints |
| CERG assurance cadence, method, sampling population | Quality checks and Independent observability and re-test rights |
| Provider access, data ownership, exit, and kill-switch | Operational constraints |

Three fields here have no counterpart in the RFC list — minimum assurance evidence, quality checks, and the indicative regulatory cross-reference. They are assurance-specific additions, not alternatives to the RFC's fields.
 The purpose is assurance of the control outcome, not creation of a reporting exercise.

---

## 4. Assurance service domains

Rather than sending 30+ independent requests to frontline teams, organize the work into six service domains.

### 4.1 Know the environment

**Outcome:** The organization can identify in-scope systems, ownership, criticality, connections, and material changes.

Includes: asset inventory, ownership and classification, inventory reconciliation, scope changes, topology/ESP/data-flow diagrams, cloud/SaaS components.

### 4.2 Reduce exposure

**Outcome:** Known weaknesses are prioritized and treated according to risk, operational constraints, and approved exceptions.

Includes: vulnerability posture, remediation aging, patches/firmware, post-change validation, unsupported technology, secure configuration, supply-chain/vendor patch intake, OT compensating controls.

### 4.3 Control access and connectivity

**Outcome:** Only authorized, traceable, and appropriately constrained access and communications paths exist.

Includes: privileged access, remote access, third-party access, firewall rules, segmentation, transient cyber assets, removable media.

### 4.4 Detect and respond

**Outcome:** Material malicious or anomalous activity can be detected, investigated, escalated, and learned from.

Includes: log coverage, security-tool health, internal network security monitoring, alert review, incident handling, and incident classification/escalation.

### 4.5 Recover and change safely

**Outcome:** Security-relevant changes are controlled and systems can be restored within approved recovery objectives.

Includes: change management, backup coverage, restoration testing, recovery plans, and emergency/mutual-aid controls.

### 4.6 Govern and improve

**Outcome:** Exceptions, findings, evidence quality, capability gaps, and trends receive accountable management attention.

Includes: risk acceptances, assessments and audit findings, data-quality attestations, metrics, and maturity roadmaps.

---

## 5. Delivery model

| Delivery type | Examples | Owner of the delivered data |
|---|---|---|
| **Continuous data feed** | Asset inventory, vulnerability results, endpoint coverage, logging health, firewall and IAM data | Tool/platform and data owners provide the feed; frontline validates operational accuracy. |
| **Event-driven notification** | Active exploitation, unauthorized remote access, crown-jewel tool outage, material monitoring gap, confirmed incident | Frontline/SOC notifies immediately using the documented escalation process. |
| **Monthly operational scorecard** | Coverage, aging, overdue remediation, exceptions, tool health, unresolved gaps | Generated centrally where possible from approved source data. |
| **Quarterly assurance review** | Architecture coverage, control effectiveness, recovery tests, segmentation validation, roadmap risks | First line and architecture provide evidence; second line challenges and summarizes. |
| **Annual governance review** | Policies, designations, training, major risk decisions, strategic capability plan | Compliance, HR, leadership, architecture, and second line jointly contribute. |

Second line should own metric definitions and consolidated assurance reporting. First line owns the correctness of source data and execution of assigned corrective actions.

---

## 6. Risk tiers

| Tier | Example scope | Assurance approach |
|---|---|---|
| **Tier 1** | Crown-jewel, high-impact, and critical OT/BES systems | Highest coverage; frequent data feeds; event-driven escalation; explicit compensating controls for any gap. |
| **Tier 2** | Systems supporting Tier 1 or enabling critical business/security functions | Monthly assurance and defined remediation commitments. |
| **Tier 3** | General IT systems | Baseline controls, risk-based sampling, and proportionate remediation expectations. |
| **Exception-managed** | Systems unable to meet a required pattern | Time-bound documented exception, compensating controls, accountable risk owner, and target-state plan. |

---

## 7. Control feasibility review

A control feasibility review is required when the defined outcome cannot be achieved through an approved pattern due to safety, reliability, vendor support, architecture, funding, or operational constraints.

### Trigger examples

- An active scan, agent, patch, or configuration change may affect grid reliability or a vendor-supported configuration.
- A required network-monitoring sensor cannot see relevant traffic without unsafe switch changes or unacceptable oversubscription.
- A remote-access, logging, segmentation, or endpoint-control requirement cannot be met on a legacy OT system.
- The platform owner cannot provide a supported integration or required data within the requested timeframe.

### Required decision record

1. Security objective and affected asset scope
2. Applicable risk tier and regulatory/control context
3. Operational/reliability impact
4. Feasible implementation options and estimated timeline
5. Compensating controls
6. Residual-risk statement
7. Accountable owner and decision
8. Remediation target date or exception expiry
9. Review cadence and evidence location

The objective is not to force a technical answer during a dispute. It is to make tradeoffs visible, risk-based, and owned at the correct level.

---

## 8. Implementation guidance for high-friction controls (companion reference)

*The guidance in this section is operational implementation advice, not contractual requirements. It is maintained as a companion reference that evolves with tooling, vendor capabilities, and operational experience. Requirements appear only in the service-domain descriptions and the control request template above.*

### Vulnerability prioritization

Use CVSS, exploitation status, CISA KEV status, EPSS, asset criticality, exposure, and operational context together. EPSS and KEV should be captured **when a CVE mapping exists**; many vendor or OT findings will not map cleanly. KEV is a high-priority risk signal, not a universal instruction to patch immediately in every environment.

### Patching and post-patch validation

A “deployed” status should include validation evidence. Validation timing should be risk-tiered and operationally feasible; an OT asset may need validation during a controlled operational test or maintenance window. If validation is deferred, record the reason, compensating controls, and planned validation date.

### Remote access

Require authenticated, authorized, logged remote access to applicable systems. MFA, PAM, session recording, just-in-time access, and retention periods should be defined as risk-tiered approved patterns—not arbitrary universal requirements that a legacy environment cannot satisfy.

### Internal network security monitoring

Treat INSM as a jointly owned architecture and operations capability. The assurance request should seek coverage, sensor health, traffic visibility, alert-review performance, blind spots, and an approved roadmap—not merely count sensors. A sensor in learning mode or one that cannot see relevant traffic does not satisfy the intended outcome.

### Security tool health

The platform owner is accountable for the tool/service and integrations; frontline is accountable for deploying and operating the control within its systems. Tool outage reporting must distinguish platform failure, endpoint coverage gaps, network/connectivity issues, and intentional operational suppression.

### Incident classification and reporting

Frontline and the SOC should immediately classify and escalate events through the documented incident process. Compliance/legal and second line should own or validate formal regulatory-reportability determinations under the organization’s approved procedure.

---

## 9. Scope boundaries

Some activities support cybersecurity assurance but should not be presented as frontline operational-security reporting obligations:

- Cyber Security Manager designation and delegation
- Enterprise policy approval and attestation governance
- Formal regulatory interpretation and reporting determinations
- Enterprise metric definition and consolidated executive reporting
- HR-controlled employment screening and broad training administration

These may appear in the broader governance program, but their accountable owners should be correctly identified.

---

## 10. Implementation approach

1. **Agree the operating model and decision rights** before expanding evidence demands.
2. **Define Tier 1 scope** and the authoritative data sources for those systems.
3. **Pilot the six service domains** with one operational area and one cybersecurity architecture/tooling group.
4. **Automate the core feeds**: inventory, vulnerability, endpoint coverage, logging, access, and firewall data.
5. **Establish the control feasibility review** and exception workflow before enforcing strict SLAs.
6. **Measure data quality and unresolved risk**, not report volume.
7. **Expand by tier and maturity**, using lessons from the pilot and approved implementation patterns.
8. **Adopt graduated data-quality expectations, stated as capability rather than percentage.** Sequence the work: Tier 1 asset ownership and support-group completeness in the authoritative inventory first, then minimum-assurance-evidence completeness on submissions, then automated reconciliation across sources. Progress is judged on whether the next capability is actually in place, not on a percentage threshold. A shortfall triggers a data-quality improvement plan with a named owner, not a compliance violation.
9. **Publish an annual data-quality maturity review.** Each service domain reports its top three data-quality gaps, root cause (tooling, process, or staffing), and the funded improvement plan. This prevents the operating model from becoming a reporting burden on top of poor-quality source data.

Nothing in this model is measured against a percentage target. Numbers appear only where they define a commitment: a notification clock, a remediation deadline, or a reconciliation tolerance that changes the response. A percentage target that can be met without improving the outcome becomes a ceiling.

---

## 11. Relationship to the second-line boundary RFC

This model does not allocate the line of defence. That allocation belongs to the upstream discussion
draft `proposals/second-line-service-boundary-rfc.md` on branch `proposal/second-line-service-boundaries`,
which establishes that the line follows the purpose of the activity rather than where a practitioner
reports, and that an MSSP, an internal IT department, a separate cyber division, or an operating division
can all provide first-line operation.

This document takes that allocation as given and answers the next question: what the interface between
the lines must contain for the assurance side to hold a first-line operator accountable, internal or
contracted. Where the two disagree, the boundary RFC governs who owns the work; this document governs
what the interface must capture.

It does not reproduce the RFC's RACI or its document-change plan, and it deliberately introduces no new
CERG role, record type, or control. The one role named here that the framework does not already carry is
the internal first-line service owner, because without a named accountable party a contracted operator has
no counterpart to hold it to account.

Second line remains technically relevant only while it can produce its own technical result rather than
read someone else's. The observability and re-test field in Section 3 is what preserves that: sampled
closed alerts, replayed detection content, verified source health, and confirmed closure. A monthly
provider report is operating evidence; it never establishes effectiveness.

---

## Proposal Status

This document is a candidate framework contribution, not approved CERG content.

- It carries no CERG identifier and has no catalog entry, so it must not be cited as a CERG
  control, standard, or procedure.
- Adoption requires the upstream framework owner to accept it as a companion governance
  instrument and register it in the document catalog.
- Until then, engagement use is per-client: cite it as a draft operating model in the
  statement of work and keep client-specific applicability decisions in the engagement record.
