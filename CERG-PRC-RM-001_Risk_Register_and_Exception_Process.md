# SURGE: Cyber Engineering, Risk & Governance

## RISK REGISTER AND EXCEPTION PROCESS
### Identification · Treatment · Acceptance · Review

---

| | |
|---|---|
| **Document ID** | CERG-PRC-RM-001 |
| **Version** | 1.0 DRAFT |
| **Status** | Published |
| **Classification** | Public |
| **Owner** | Risk Register Owner |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) |
| **Review Cycle** | Annual / Upon Significant Change / Major Tooling Change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r2/final) · [NIST 800-30r1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) · [NIST 800-39](https://csrc.nist.gov/pubs/sp/800/39/final) · NIST RMF · ISO 31000 |
| **Regulations** | NERC-CIP · [CMMC L2](https://dodcio.defense.gov/CMMC/) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Roles and Responsibilities](#2-roles-and-responsibilities)
3. [Risk Identification](#3-risk-identification)
4. [Risk Assessment and Scoring](#4-risk-assessment-and-scoring)
5. [Risk Treatment](#5-risk-treatment)
6. [The Risk Register](#6-the-risk-register)
7. [Exception Process](#7-exception-process)
8. [Approval Authority](#8-approval-authority)
9. [Review, Escalation, and Reporting](#9-review-escalation-and-reporting)
10. [Integration With Other Programs](#10-integration-with-other-programs)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Procedure Control](#12-procedure-control)

---

## 1. Purpose and Scope

This procedure operationalizes the risk management principle established in **[CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Principle 9**. It defines how the organization identifies, documents, scores, treats, reviews, and reports cybersecurity risks, and how exceptions to established controls are requested, approved, tracked, and reviewed.

The risk register is the single, authoritative record of organizational cybersecurity risk. The exception process is the single, authoritative record of intentional deviations from established controls. The two are coupled: every approved exception is itself a risk-register entry.

### 1.1 Scope

This procedure applies to:

- All cybersecurity risks affecting in-scope assets, data, or operations
- All deviations from controls established in [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) and its subordinate standards and procedures
- All risk-related decisions requiring documentation: acceptance, transfer, avoidance, and reduction
- All organizational personnel, every CERG team member, every asset owner, every business sponsor of a system or process that holds cybersecurity risk

### 1.2 The Operating Premise

> **Undocumented Risk Is Accepted Risk Without an Owner**
>
> Every organization has more risk than it has time to remediate. The question is not whether risk exists, it is whether the organization has a documented, owned, and reviewed posture toward each one. An undocumented risk that materializes into an incident leaves no audit trail of what was known, who knew it, or why nothing was done. CERG treats the risk register as evidence of program maturity, not as a chore.

---

### 1.3 Risk Appetite and Tolerance

The organization's risk appetite defines the amount and type of risk the organization is willing to accept in pursuit of its objectives. Without a stated appetite, "accept" decisions lack an objective anchor, and scoring discussions drift toward personal calibration.

#### Appetite Statement

The organization accepts residual risk only where (a) the cost or operational impact of further treatment demonstrably exceeds the residual risk, (b) compensating controls are in place and operating effectively, and (c) the risk does not threaten regulatory standing, customer trust, or safety. Risk that cannot satisfy all three conditions must be treated.

#### Quantitative Tolerance Thresholds

| **Tier / Scope** | **Maximum Acceptable Residual Risk Score** | **Maximum Acceptable Duration** | **Notes** |
|---|---|---|---|
| BES Cyber Systems (NERC-CIP) | 6 (Medium-Low) | 90 days | Aligned to CIP mitigation plan timelines |
| CUI Environments (CMMC) | 6 (Medium-Low) | 90 days | Aligned to POA&M timelines; Critical not acceptable |
| SOX-Relevant Systems | 8 (Medium) | 180 days | ITGC compensating controls required |
| Production Tier 1 (Customer-Facing) | 8 (Medium) | 180 days | Critical not acceptable without CISO + Executive Sponsor |
| Production Tier 2 (Internal Business) | 10 (Medium-High) | 365 days | |
| Production Tier 3+ / Non-Production | 12 (High-Low) | 365 days | |
| SaaS / Third-Party | 10 (Medium-High) | Contract cycle | Driven by vendor tier per [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |

#### Tolerance by Business Unit

Tolerance thresholds may vary by business unit where the business unit operates under materially different regulatory, contractual, or operational risk profiles. Business unit tolerance adjustments are proposed by the Risk Owner in that unit, reviewed by the Governance Pillar Leader, and approved by the CISO. Adjustments are recorded in the risk register as a standing annotation on the business unit's scope.

#### Board and Leadership Engagement

The board or an authorized board committee reviews and affirms the organization's risk appetite annually. Material changes to risk appetite - including adjustments to quantitative thresholds or tolerance by business unit - are submitted to the CISO for recommendation and board approval. The CISO owns the annual appetite affirmation cycle and reports the organization's actual risk posture against appetite at each quarterly CISO-level review.

---

## 2. Roles and Responsibilities

| **Role** | **Risk Management Responsibility** |
|---|---|
| **Risk Register Owner** | Owns this procedure and the risk register tool. Maintains the data model, taxonomy, dashboards, and reporting. Coordinates the risk review cadence. Curates the register for quality and completeness. |
| **Risk Pillar Leader** | Identifies risks through vulnerability management, threat intelligence, vendor assessment, adversarial testing, and continuous monitoring. Records risks in the register and recommends scoring and treatment. |
| **Engineering Pillar Leader** | Identifies risks through architecture review and pre-production assessment. Recommends compensating controls. Implements risk-reduction treatments on assets it supports. |
| **Business / Asset Owners (Risk Owners)** | Accountable for the risks associated with the systems and processes they own. Authorize treatment decisions for their scope. Sign on risk acceptances. |
| **Approvers (Engineering Pillar Leader → CISO → Executive Sponsor)** | Apply the approval matrix in Section 8. Approvers do not own risks; they authorize the treatment decision against organizational policy. |
| **CISO** | Approves High and Critical risk acceptances and material exceptions. Owns escalation to executive leadership and the board. Owns the overall organizational risk posture. |
| **Internal Audit and Compliance Partners** | Consume the register as evidence of risk management activity. Verify integrity of the process through periodic audit. |

---

## 3. Risk Identification

A risk is a potential event that could adversely affect organizational assets, operations, or obligations. Risks may be technical (a vulnerability, a misconfiguration, a control gap), programmatic (a process gap, a staffing gap), or external (a regulatory change, a vendor failure, a threat actor's interest).

### 3.1 Sources of Risk

Risks are identified continuously from the following sources, each of which feeds the register:

| **Source** | **Examples** |
|---|---|
| Vulnerability management | Out-of-SLA findings, KEV exposures, structural patching limitations. |
| Engineering review | Architectural gaps identified in pre-production review, IT/OT convergence findings, technical debt with security implications. |
| Adversarial validation | Pen-test findings, red-team paths to crown-jewel assets, control-bypass discoveries. |
| Third-party / vendor risk | SOC 2 / ISO 27001 / FedRAMP exceptions, vendor incidents, supply-chain advisories. |
| Threat intelligence | Threats specifically targeting the organization's industry, technology, or geography. |
| Compliance monitoring | Findings from internal compliance reviews, regulator examination, external audit. |
| Incident review | Root causes from post-incident reviews. |
| Exception requests | Approved exceptions, which become risk-register entries. |
| Strategic / programmatic | Staffing shortfalls, tooling gaps, sunset of unsupported platforms. |
| Self-reporting | Risk submissions by any personnel through the documented intake. |

### 3.2 Intake

Any personnel may submit a candidate risk through the centralized intake. Submissions include the proposed risk statement, affected assets, observed or estimated impact, and supporting context. Governance triages submissions within 5 business days into one of: accept as new register entry, merge with existing entry, escalate to active investigation, or return with explanation.

---

## 4. Risk Assessment and Scoring

### 4.1 Risk Statement

Each risk is expressed in a consistent, declarative form:

> "**[Event / condition]** affecting **[asset class / scope]** could result in **[impact]** within **[likelihood window]** unless **[control / treatment]**."

Risk statements are specific enough to support scoring. "We need better cloud security" is not a risk statement; "Unauthorized changes to production cloud IAM roles could result in privilege escalation enabling exfiltration of customer data within the current control period unless drift detection and JIT elevation are enforced" is.

### 4.2 Scoring Framework

Risks are scored using a 5×5 matrix of **Likelihood** and **Impact**. The matrix produces a residual risk rating after considering controls in place. Inherent risk (controls hypothetically absent) is recorded but not the primary driver of treatment decisions.

#### Likelihood

| **Score** | **Label** | **Meaning** |
|---|---|---|
| 1 | Rare | Conceivable but no specific indicator. Outside common attack patterns for the organization. |
| 2 | Unlikely | Occurs in the industry occasionally; no current indicator at the organization. |
| 3 | Possible | Realistic given the threat landscape; mitigating controls reduce likelihood. |
| 4 | Likely | Frequent in the industry; conditions present at the organization with limited mitigation. |
| 5 | Almost Certain | Active or imminent; observed indicators or active exploitation; minimal current mitigation. |

#### Impact

| **Score** | **Label** | **Meaning (any one criterion qualifies)** |
|---|---|---|
| 1 | Negligible | No regulatory, customer, financial, or operational impact beyond routine response. |
| 2 | Minor | Limited operational disruption or remediation cost; no regulatory or customer-visible impact. |
| 3 | Moderate | Material remediation effort or modest customer impact; localized regulatory finding without breach. |
| 4 | Major | Significant regulatory exposure (CIP, CUI, breach-law notification), material customer impact, or significant operational disruption (Tier 1 systems). |
| 5 | Critical | Material business / financial impact; broad customer harm; regulatory enforcement; safety or reliability consequence; SEC-disclosable. |

#### Rating Bands

| **Score Product** | **Rating** | **Default Treatment Expectation** |
|---|---|---|
| 1–4 | **Low** | Track; treat as resources allow. |
| 5–9 | **Medium** | Treat within a defined plan; review at standing cadence. |
| 10–14 | **High** | Treat with priority; CISO approves risk acceptance. |
| 15–20 | **Critical** | Treat urgently; CISO + executive sponsor approval for any acceptance. |
| 21–25 | **Critical** | Immediate treatment required; executive / board awareness. |

### 4.3 Quantitative Calibration Guide

The qualitative labels in the 5×5 matrix are calibrated against quantitative anchors to promote scoring consistency.

#### Likelihood Calibration (Annualized Probability)

| **Score** | **Label** | **Annual Probability** | **Expected Frequency** |
|---|---|---|---|
| 1 | Rare | < 5% | Less than once every 20 years |
| 2 | Unlikely | 5–20% | Once every 5–20 years |
| 3 | Possible | 20–50% | Once every 2–5 years |
| 4 | Likely | 50–90% | Once every 1–2 years |
| 5 | Almost Certain | > 90% | More than once per year |

#### Impact Calibration (Financial Equivalent)

| **Score** | **Label** | **Financial Impact** | **Non-Financial Equivalent** |
|---|---|---|---|
| 1 | Negligible | < $50K | No regulatory, customer, or operational impact beyond routine response |
| 2 | Minor | $50K–$250K | Limited operational disruption; no regulatory or customer-visible impact |
| 3 | Moderate | $250K–$1M | Material remediation effort or modest customer impact; localized regulatory finding |
| 4 | Major | $1M–$10M | Significant regulatory exposure (CIP, CUI, breach notification), material customer impact, Tier 1 system disruption |
| 5 | Critical | > $10M or regulatory enforcement | Material business/financial impact; broad customer harm; safety or reliability consequence; SEC-disclosable |

#### Using Calibration in Scoring Discussions

The calibration table is a coordination tool, not a precise calculator. When two analysts reach different scores:
1. Each states their rationale in terms of likelihood (what is the annual probability?) and impact (what is the estimated financial or operational consequence?).
2. The Governance Lead facilitates the discussion toward the better-supported score.
3. If disagreement persists, the higher score is used and the rationale for both scores is recorded.

The goal is not perfect precision - it is consistent conversation that produces comparable risk rankings across the register.

### 4.4 Scoring Discipline

> **The 5×5 Trap**
>
> The 5×5 matrix is a coordination tool, not an oracle. Two analysts will reach different scores for the same risk; the value of the matrix is consistency of conversation, not precision of measurement. The Governance Lead enforces consistency within the register and reconciles outliers, but does not fight every score. The goal is comparable risks ranked comparably, not perfect calibration.

Re-score upon: material change in observed threat activity, completion of treatment work, new compensating controls, new exploitation indicators, or regulator / customer engagement that materially changes impact.

---

## 5. Risk Treatment

Each risk has one of four treatment decisions. Treatment is decided by the risk owner with input from CERG and approved per Section 8.

| **Treatment** | **Description** | **When Appropriate** |
|---|---|---|
| **Reduce (Mitigate)** | Implement or strengthen controls to reduce likelihood, impact, or both. The default treatment for most risks. | Almost always preferred where feasible and timely. |
| **Transfer** | Shift the financial or operational consequence to a third party (insurance, contractual indemnity, managed service). | When transfer is economically and operationally rational; not a substitute for treatment of the underlying technical risk. |
| **Avoid** | Cease or decline the activity producing the risk. | When the activity is not essential or when residual risk is unacceptable under any treatment. |
| **Accept** | Acknowledge the risk and proceed without further action beyond monitoring. | When the cost or operational impact of treatment exceeds the residual risk, and the residual is within the organization's tolerance. |

### 5.1 Treatment Plan Elements

Every treatment decision records:

- The selected treatment.
- The plan, for Reduce: target end-state controls and the steps to get there; for Transfer: the instrument and counter-party; for Avoid: the cessation steps; for Accept: the rationale and conditions of acceptance.
- Owner, accountable for the plan's execution.
- Target dates, milestone and final.
- Compensating controls, in place now and required for the duration of the plan.
- Trigger conditions for re-evaluation, what would invalidate the current decision.

### 5.2 Risk Acceptance Has Two Forms

| **Form** | **Description** |
|---|---|
| **Permanent acceptance** | The residual risk is permanently within tolerance; no further treatment is planned. Permanent acceptance still requires periodic re-review and remains in the register. |
| **Time-bound acceptance** | The risk is accepted for a defined window during which compensating controls operate; treatment is expected to occur within the window. This is the predominant form of acceptance for control deficiencies awaiting remediation. |

---

## 6. The Risk Register

### 6.1 Required Fields

| **Field** | **Description** |
|---|---|
| Risk ID | Unique identifier assigned at intake. |
| Risk Statement | The standardized risk statement (Section 4.1). |
| Risk Owner | Business or asset owner accountable for the risk. |
| Risk Category | Taxonomy classification (e.g., Identity & Access, OT / NERC-CIP, Cloud / SaaS, Third-Party / Supply Chain, CUI / Federal, Application Security, Data Protection, Insider, Resilience). |
| Affected Assets / Scope | Systems, data classes, environments. |
| Source | Where the risk was identified (Section 3.1). |
| Likelihood / Impact / Rating | Current scores and band. |
| Inherent Rating | Hypothetical rating absent controls (recorded once at intake; not re-scored each cycle). |
| Controls in Place | Existing controls reducing the risk. |
| Treatment Decision | Reduce / Transfer / Avoid / Accept. |
| Treatment Plan | Plan summary. |
| Target Dates | Milestone and final. |
| Approver | Approver name and approval date per Section 8. |
| Compliance Linkage | Associated regulation, framework, or contract (e.g., 800-171 control reference, CIP standard, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC). |
| Linked Exceptions | Exception IDs created under this risk, if any. |
| Linked Incidents | Incident IDs that derived from or contributed to the risk, if any. |
| Status | Open / In Treatment / Accepted / Closed. |
| Review Date | Next scheduled review. |
| Audit Trail | History of changes - every score change, treatment change, approver change, status change. |

### 6.2 Quality and Integrity

The Governance Lead curates the register for quality. Specifically:

- Risks shall not be duplicated; new submissions are merged with existing entries when appropriate.
- Risk statements that are vague or unscope-able are returned for clarification.
- Risks that are no longer relevant (e.g., the underlying system has been decommissioned) are closed with rationale.
- Closed risks remain queryable; the register is append-only at the audit-trail level.

### 6.3 Risk Taxonomy

The following taxonomy is the controlled vocabulary for risk categorization. Every risk entry must be assigned exactly one category from this taxonomy. Consistent categorization enables trend analysis, ownership clarity, and regulatory mapping.

| **Category** | **Definition** | **Examples** |
|---|---|---|
| **Identity & Access** | Risks related to identity lifecycle, authentication, authorization, privilege management, and access control failures. | Standing privileged access, MFA gaps, orphaned accounts, over-privileged service principals, credential theft. |
| **OT / NERC-CIP** | Risks affecting Operational Technology, BES Cyber Systems, or NERC-CIP compliance posture. | Unpatched OT assets, IT/OT boundary weaknesses, CIP-007 deviation, BCSI exposure. |
| **Cloud / SaaS** | Risks arising from cloud platform misconfiguration, SaaS security posture, or cloud-native service exposure. | Open S3 bucket, excessive IAM roles, SaaS OAuth grant abuse, tenant isolation failure. |
| **CUI / Data Protection** | Risks to the confidentiality, integrity, or availability of Controlled Unclassified Information or other regulated data. | CUI stored outside authorized boundary, FIPS non-compliance, data spillage, missing encryption at rest. |
| **Third-Party / Vendor** | Risks introduced through vendor relationships, supply chain dependencies, or subcontractor access. | Vendor SOC 2 exception, subprocessor concentration, vendor breach with downstream impact. |
| **Endpoint** | Risks related to endpoint security, including workstations, servers, and mobile devices. | Missing EDR coverage, unpatched endpoint, local admin abuse, removable media exposure. |
| **Network** | Risks to network segmentation, perimeter controls, traffic inspection, or remote access. | Flat network, exposed management interface, missing segmentation between regulatory zones. |
| **Application Security** | Risks in custom or third-party application code, APIs, or application architecture. | SQL injection, broken authentication in custom app, API key exposure, SSRF vulnerability. |
| **Cryptography** | Risks related to cryptographic key management, algorithm selection, certificate lifecycle, or secrets handling. | Expired certificate, weak cipher suite, hard-coded secret, missing HSM for CA key. |
| **Governance / Compliance** | Risks from gaps in policy, process, regulatory alignment, or program maturity. | Missing policy review cycle, undocumented exception process, audit finding without remediation plan. |
| **Resilience** | Risks to business continuity, disaster recovery, backup integrity, or service restoration capability. | Untested backups, single-region dependency, RTO/RPO gap for Tier 1 system. |
| **Insider** | Risks from intentional or unintentional actions by authorized personnel. | Data exfiltration by departing employee, accidental PII exposure, privilege misuse. |
| **Physical / Environmental** | Risks from physical access, environmental controls, or facility security. | Unsecured data center access, missing CCTV coverage, inadequate fire suppression. |

Access and Confidentiality

Risk register access is role-based. Business owners see their scope by default; CERG personnel see organization-wide. Specific risk entries may be marked Restricted (e.g., active high-sensitivity exposure, insider matters) with limited visibility. The CISO has full visibility at all times.

---

## 7. Exception Process

### 7.1 What Requires an Exception

An exception is required whenever a system, person, or process intentionally deviates from a control established in [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) or its subordinate standards. Examples include:

- A system that cannot meet a hardening baseline due to a vendor or operational constraint
- A user role that requires standing privileged access despite the JIT requirement
- A SaaS application not behind SSO due to a technical limitation
- A vulnerability remediation that cannot meet the SLA
- A vendor account configuration not meeting the access management standard
- An OT system that cannot satisfy a CIP-007 requirement on schedule (in addition to the CIP deviation process)

### 7.2 Exception Workflow

| **Step** | **Action** | **Owner** |
|---|---|---|
| 1 | Requester submits exception with: control reference, business / operational justification, affected systems, proposed compensating controls, risk owner, and proposed duration. | Requester |
| 2 | Engineering reviews proposed compensating controls. | Engineering |
| 3 | Risk assesses likelihood and impact of the residual risk; provides a written risk finding. | Risk |
| 4 | Governance applies the approval matrix (Section 8); routes for approval. | Governance |
| 5 | Approver decides: approve, approve with conditions, deny, or return for additional information. | Approver |
| 6 | Approved exception is entered into the risk register as a linked acceptance entry; compensating controls are tracked. | Governance |
| 7 | At expiration, the exception is re-evaluated. Renewal requires a new approval cycle. Renewals shall not be granted by default. | Governance |

### 7.3 Exception Discipline

> **Renewals Are Where Programs Decay**
>
> The most common failure mode of an exception program is the silent renewal. An exception is approved with a six-month duration; six months later it is renewed with a single email; six months after that the original reviewers have left the organization, the compensating controls have drifted, and the underlying control gap has become permanent. Governance enforces re-evaluation at every renewal: confirm the compensating controls are still in place, confirm the business justification is still valid, confirm the requested duration is still reasonable.

### 7.4 Regulatory Overlays

For exceptions affecting regulated assets:

- **NERC-CIP (BES Cyber Systems):** A CIP deviation and mitigation plan is initiated in addition to this exception. Governance coordinates per [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) §11.
- **[CMMC](https://dodcio.defense.gov/CMMC/) / 800-171 (CUI environments):** A POA&M entry is opened in addition to this exception, per [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) §11.
- **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems:** Internal Audit and CFO designee are notified for ITGC control gaps. Compensating ITGC controls are documented for audit.
- **Customer / contractual:** Where the affected control supports a customer contractual commitment, Account Management and Legal are notified for customer-notification decisions.

---

### 7.5 Exception Request Form Template

The following template shall be used for all exception requests. Completed forms are submitted through the centralized risk intake and referenced in the risk register.

```
EXCEPTION REQUEST FORM - EXC-YYYY-NNNN

1. REQUESTOR
   Name:
   Role / Title:
   Department / Business Unit:
   Date of Request:

2. CONTROL(S) TO BE EXCEPTED
   Control ID (from CERG-GOV-CB-001 or applicable standard):
   Control Description:
   Standard / Policy Reference:

3. AFFECTED SCOPE
   System(s) / Asset(s):
   Environment (IT / Cloud / SaaS / OT):
   Data Classification(s):
   Regulatory Scope (NERC-CIP / CUI / SOX / Other):
   Number of Users Impacted:

4. BUSINESS JUSTIFICATION
   Why is the exception necessary? What business outcome depends on it?

   What alternatives were considered and why were they rejected?

5. RISK ASSESSMENT OF THE EXCEPTION
   Inherent Risk (Likelihood × Impact):
   Description of the risk created by this exception:
   Existing Compensating Controls:
   Residual Risk after Compensating Controls (Likelihood × Impact):
   Residual Risk Rating (Low / Medium / High / Critical):

6. COMPENSATING CONTROLS (detailed)
   | Control | Description | Owner | Implementation Date | Validation Method |
   |---|---|---|---|---|
   | | | | | |

7. DURATION
   Proposed Start Date:
   Proposed End Date:
   Renewal Expected? (Yes / No):
   If yes, what conditions must be met for renewal?

8. APPROVAL
   | Role | Name | Decision | Date |
   |---|---|---|---|
   | Risk Owner | | Approve / Deny / Conditional | |
   | Engineering Pillar Leader | | Approve / Deny / Conditional | |
   | Governance Pillar Leader | | Approve / Deny / Conditional | |
   | CISO (if High or Critical) | | Approve / Deny / Conditional | |
   | Executive Sponsor (if Critical) | | Approve / Deny / Conditional | |

9. RISK REGISTER LINKAGE
   Risk Register Entry ID:
   Exception ID cross-reference:

10. CLOSURE
    Actual End Date:
    Closure Rationale:
    Closure Approver:
```

---

## 8. Approval Authority

Risk treatment decisions require documented approval from the authority matching the risk's severity. The canonical approval authority table is maintained in [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 and is the single source of truth for acceptance authority by severity tier. The table below reproduces the same authorities for convenience within this procedure, with additional detail on treatment-type distinctions and the emergency exception path.

| **Risk Rating / Treatment** | **Approval Authority** |
|---|---|
| Low risk – any treatment | Risk Owner + Governance Pillar Leader |
| Medium risk – Reduce / Transfer / Avoid | Risk Owner + Engineering or Risk Pillar Leader |
| Medium risk – Accept | Risk Owner + CISO (or CISO designee) |
| High risk – any treatment | Risk Owner + CISO |
| Critical risk – any treatment | Risk Owner + CISO + Executive Sponsor |
| Any exception affecting BES Cyber Systems | CISO + NERC-CIP deviation process |
| Any exception affecting CUI environment posture | CISO + POA&M entry |
| Any exception affecting [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC | CISO + CFO designee |
| Emergency exception (operational necessity) | Risk Pillar Leader or Engineering Pillar Leader may authorize immediately; CISO must approve or deny post-hoc within 24 hours. If denied, the action must be reversed or mitigated, and the residual risk is logged to the risk register with the denial rationale. |

Approvers may delegate within their authority but shall document the delegation. The CISO retains final authority for any risk-related decision. Acceptance of residual risk at any tier follows the canonical authority table in [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. No acceptance expires automatically; every acceptance at every tier requires a fresh approval cycle at expiration.

---

## 9. Review, Escalation, and Reporting

### 9.1 Review Cadence

| **Item** | **Cadence** | **Owner** |
|---|---|---|
| Risk owner self-review of open risks in their scope | Quarterly | Risk Owner |
| Governance curation pass (quality, duplicates, status) | Monthly | Governance |
| CERG leadership review (Engineering + Risk + Governance) | Monthly | Governance |
| CISO-level risk review with material movement and overdue items | Quarterly | CISO + Governance |
| Executive / board risk briefing | Quarterly (or per board protocol) | CISO |
| Standing exception re-review | At exception expiration; no automatic renewal | Governance |

### 9.2 Escalation Triggers

The following trigger escalation to the CISO outside the standing cadence:

- A new High or Critical risk
- A material score increase on any existing risk
- A risk acceptance approaching expiration without a credible treatment plan
- A material deterioration in compensating control performance
- Realization of a risk into an incident
- A regulator or auditor inquiry referencing a register entry
- A renewal request for an exception in its second consecutive cycle

### 9.3 Reporting

Standing reports (consumed by Governance dashboards):

| **Report** | **Audience** | **Cadence** |
|---|---|---|
| Top risks (by rating and by trend) | CISO | Monthly |
| Open exceptions by environment | CERG Leadership | Monthly |
| Overdue treatments / expired exceptions | Governance | Weekly |
| Risks by category trend (Identity, Cloud, OT, CUI, Third-Party, etc.) | CISO + executive | Quarterly |
| Risks linked to active incidents | IC + CISO | Continuous during active response |
| Regulatory-specific posture (CIP, [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)) | Governance + Regulatory partners | Per regulator cycle |

### 9.4 Quality Indicators

The Governance Lead monitors the register itself for health:

- Median age of open High and Critical risks
- % of treatment plans on schedule
- Exception re-evaluation rate (declined vs. renewed)
- % of risks with a documented owner
- % of risks reviewed within their scheduled review date

---

## 10. Integration With Other Programs

The risk register is the integration point for several other programs. Risk-register entries derive from and feed back into:

| **Program** | **Integration** |
|---|---|
| Vulnerability Management ([CERG-PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md)) | Out-of-SLA findings and aggregate exposure feed risk entries; large remediation campaigns are tracked as treatments. |
| Incident Response ([CERG-PLN-IR-001](CERG-PLN-IR-001_Incident_Response_Plan.md)) | Post-incident corrective actions are recorded as risks or risk-acceptance closures. |
| Vendor / Third-Party Risk | Vendor assessment findings open risks; vendor reassessment cadence reviews them. |
| Compliance - NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) | Open compliance gaps map to risk entries; POA&M and CIP deviations link to register entries. |
| Architecture / Engineering Review | Pre-production review findings open risks where acceptance is sought to deploy. |
| Awareness & Insider Programs | Concentrated insider-risk indicators are recorded (with appropriate restricted visibility). |
| Audit | Internal Audit and external audit observations open or update risk entries. |

The register is not a parallel system to these programs. It is the connective tissue that lets each program point to the same set of facts.

---

## 11. Regulatory and Framework Alignment Summary

| **Process Area** | **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | **[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)** | **NIST RMF** | **NERC-CIP** | **[CMMC L2](https://dodcio.defense.gov/CMMC/)** | **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC** |
|---|---|---|---|---|---|---|---|
| Risk Strategy & Governance | GV.RM | PM-9 | 3.11.1 | Steps 1–2 | CIP-003 | RM.L2-3.11.1 | ERM interface |
| Risk Assessment / Scoring | ID.RA | RA-3 | 3.11.1 | Step 3 | CIP-002 / 007 | RM.L2-3.11.1 | - |
| Risk Treatment | GV.RM | PM-4, CA-5 | 3.11.3 | Steps 3–5 | CIP-003 | RM.L2-3.11.3 | - |
| Risk Acceptance | GV.RM | CA-6 | 3.12.2 | Step 5 | CIP-003 | CA.L2-3.12.2 | - |
| Exception / POA&M | GV.RR | CA-5 | 3.12.2 | Step 5 | CIP Mitigation Plans | CA.L2-3.12.2 | - |
| Continuous Monitoring of Risk | DE.CM, ID.IM | CA-7 | 3.12.3 | Step 6 | CIP-007 | CA.L2-3.12.3 | Monitoring |
| Reporting & Communication | GV.RR | PM-9, PM-31 | 3.12.3 | Step 6 | CIP-003 | CA.L2-3.12.3 | Reporting |

---

## 12. Procedure Control

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 DRAFT | 2026 | CERG Governance | Initial release |

### Review Triggers

This procedure shall be reviewed annually and upon any of the following:

- Material change to risk taxonomy or scoring scheme
- Material change to risk-management tooling
- Material change to regulatory expectations affecting risk acceptance, POA&M, or CIP deviation processes
- A significant incident or audit finding affecting the program
- Direction from the CISO

Governance owns this procedure. The Risk Register Owner is responsible for revisions, ongoing maintenance, and obtaining CISO approval for material updates.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - Principle 9 |
| Grid and Control System Standard | [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | OT risk and CIP deviation overlay |
| IT / Cloud / SaaS Security Standard | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | IT/Cloud/SaaS risk scope, tier-based control expectations |
| CUI Handling Standard | [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) | CUI risk scope, POA&M tracking |
| Access Management Standard | [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) | Identity-related risk and access exception handling |
| Unified Control Baseline | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control framework that risk entries reference |
| Vulnerability Management Procedure | [CERG-PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | Vulnerability risk acceptance path |
| Adversarial Validation Procedure | [CERG-PRC-AV-001](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Adversarial testing finding risk acceptance |
| Third Party and Supply Chain Risk Procedure | [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor risk register entries and tier-based acceptance authority |
| Architecture Review and Project Intake Procedure | [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Project review findings flow to risk register |
| CERG Operating Model | [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) | Pillar structure and risk governance |

---

> **SURGE, Cyber Engineering, Risk & Governance**
>
> _Identify it. Score it. Record it. Own it._

---

_CERG-PRC-RM-001 · Version 1.0 DRAFT · CONFIDENTIAL · Internal Use Only_