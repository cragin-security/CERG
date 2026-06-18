
# SURGE: Cyber Engineering, Risk & Governance

## RISK REGISTER TEMPLATES AND REPORTING
### Register Schema · Exception Request · Scoring Examples · CISO Slice-and-Dice Reporting

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-RM-001 |
| **Version** | 1.22 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Risk Register) |
| **Parent Procedure** | [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Supporting Documents** | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-GOV-MTR-001](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| **Review Cycle** | Annual / On register tooling change |
| **Frameworks** | [NIST 800-30r1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) · [NIST 800-39](https://csrc.nist.gov/pubs/sp/800/39/final) · ISO 31000 |
| **Regulations** | NERC-CIP · [CMMC L2](https://dodcio.defense.gov/CMMC/) · SOX ITGC |
| **Environments** | All in-scope assets |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Risk Statement Standard](#2-risk-statement-standard)
3. [Risk Register Schema](#3-risk-register-schema)
4. [Worked Examples](#4-worked-examples)
5. [Exception Request Template](#5-exception-request-template)
6. [Risk Scoring Guide](#6-risk-scoring-guide)
7. [CISO Slice-and-Dice Reporting Views](#7-ciso-slice-and-dice-reporting-views)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

[`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) defines how risks and exceptions move through the program. This document is the executable package that makes that procedure operable: the register schema, the exception template, scoring examples, and the reporting views the CISO actually consumes. It is referenced from PRC-RM-001 and from [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) (control-to-evidence mapping).

> **Why Bind Risk Statements to Controls**
>
> A risk that does not map to at least one control is either a controls gap to add to the baseline or an over-broad risk to refine. A control that does not map to at least one risk is a control that nobody can defend. The register is the place those two libraries reconcile.

---

## 2. Risk Statement Standard

Every risk register entry has a single sentence, the **Risk Statement**, in this form:

> Because of [**threat / weakness**], affecting [**asset / scope**], there is a possibility that [**adverse event**] occurs, resulting in [**business impact**].

The Risk Statement is derived from a control. The derivation pattern is:

| **Control State** | **Implied Risk Statement Stem** |
|---|---|
| Implemented | "If the control fails or is bypassed…" |
| Partially Implemented | "Because the control covers only [scope]…" |
| Planned | "Until the control is implemented…" |
| Risk Accepted | "While the exception is in force…" |
| Inherited | "If the provider's control or our inheritance prerequisites fail…" |

If a risk does not map to a control in [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md), one of three things happens: (1) the control is added to the baseline as a CERG-X control, (2) the risk is reframed against an existing control, or (3) the risk is rejected as out of scope.

---

## 3. Risk Register Schema

The schema below is the system-of-record contract regardless of tool (Excel, ServiceNow, Archer, RSA, custom).

| **Field** | **Type** | **Required** | **Description** |
|---|---|---|---|
| Risk ID | `R-YYYY-NNNN` | Yes | Sequential per calendar year. |
| Risk Statement | Free text - Section 2 form | Yes | One sentence. |
| Source | Enum: VM · Pen Test · Vendor · Architecture Review · Audit · Threat Intel · Self-Identified · Incident | Yes | What surfaced the risk. |
| Linked Control(s) | List of [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) IDs | Yes | At least one. |
| Affected Asset(s) | Asset inventory ID(s) | Yes | From the authoritative asset inventory. |
| Operating Unit | Enum (OU list) | Yes | Drives CISO slice-and-dice. |
| Regulatory Scope | Multi-select: CUI · BES · SOX · None | Yes | Drives overlay scoring. |
| Inherent Likelihood | 1–5 | Yes | Before controls. |
| Inherent Impact | 1–5 | Yes | Before controls. |
| Inherent Score | Likelihood × Impact | Auto | - |
| Control Effectiveness | Enum: Strong · Adequate · Weak · None | Yes | Reduces residual score per Section 6. |
| Residual Likelihood | 1–5 | Yes | After controls. |
| Residual Impact | 1–5 | Yes | After controls. |
| Residual Score | Likelihood × Impact | Auto | Drives approval authority per PRC-RM-001 §8. |
| Treatment | Enum: Mitigate · Transfer · Avoid · Accept | Yes | - |
| Treatment Plan | Free text | Yes | Specific actions, owners, dates. |
| Risk Owner | Named role | Yes | Asset/process owner - accountable. |
| CERG Coordinator | Named role | Yes | Pillar contact - keeps it moving. |
| Approver | Named role | Yes | Per PRC-RM-001 §8 matrix. |
| Approval Date | Date | If accepted | - |
| Review Cadence | Quarterly · Semi-Annual · Annual | Yes | Driven by residual score. |
| Next Review | Date | Yes | - |
| Status | Open · In Treatment · Accepted · Closed · Retired | Yes | - |
| Linked Exceptions | Exception ID(s) | If exception in force | - |
| Linked Findings | VM finding ID · Pen test finding ID · Audit finding ID | Optional | - |
| Linked POA&M | POA&M ID | If CUI scope | - |
| Evidence Pointer | URI / artifact reference | Yes | Where the proof lives. |
| Trend Indicator | Improving · Steady · Worsening | Yes (at review) | Set at each review. |
| Free-Form Notes | Free text | Optional | - |

### 3.1 Computed Fields and Workflow States

- **Residual Score** drives auto-routing to the approval queue per PRC-RM-001 §8.
- **Review Cadence** is set by residual score: Critical/High = Quarterly, Medium = Semi-Annual, Low = Annual.
- **Status** transitions: Open → In Treatment → (Closed | Accepted) → Retired. Retired risks are kept for audit history.

---

## 4. Worked Examples

### 4.1 Example A: Risk Derived From a Partially Implemented Control

| Field | Value |
|---|---|
| Risk ID | R-2026-0048 |
| Risk Statement | Because phishing-resistant MFA (IA-2) is not enforced on all legacy interactive logons, affecting the on-prem AD-joined Tier 2 application estate (≈ 180 systems), there is a possibility that credential phishing of a privileged user leads to lateral movement, resulting in operational outage and recovery cost. |
| Source | Self-Identified |
| Linked Control(s) | IA-2 |
| Operating Unit | Generation Operations IT |
| Regulatory Scope | SOX |
| Inherent Likelihood / Impact | 4 / 4 → 16 |
| Control Effectiveness | Weak (legacy auth permitted) |
| Residual Likelihood / Impact | 4 / 3 → 12 (High) |
| Treatment | Mitigate |
| Treatment Plan | Q3: enforce phishing-resistant MFA on Tier 2 high-blast-radius admin paths. Q4: extend to remainder. Exceptions tracked. |
| Risk Owner | Gen Ops IT Director |
| Approver | CISO |
| Review Cadence | Quarterly |

### 4.2 Example B: Risk Derived From a Risk-Accepted Exception

| Field | Value |
|---|---|
| Risk ID | R-2026-0102 |
| Risk Statement | While exception EX-2026-0017 is in force permitting an unmanaged legacy SCADA HMI to remain in service through 2027, affecting a single substation, there is a possibility that an unpatched RCE is exploited via the local engineering jump server, resulting in localized loss-of-view and breach of CIP-007 R2. |
| Source | Architecture Review |
| Linked Control(s) | CM-2 / CM-6 / SI-2 |
| Regulatory Scope | BES |
| Inherent Likelihood / Impact | 3 / 5 → 15 |
| Control Effectiveness | Adequate (compensating: isolated jump, monitored, no internet egress) |
| Residual Likelihood / Impact | 2 / 4 → 8 (Medium) |
| Treatment | Accept (until 2027 replacement) |
| Linked Exceptions | EX-2026-0017 |
| Review Cadence | Quarterly |

### 4.3 Example C: Risk Derived From an Inheritance Failure Mode

| Field | Value |
|---|---|
| Risk ID | R-2026-0153 |
| Risk Statement | If the M365 inherited tenancy isolation control is misconfigured on the customer side (conditional access policy gap), affecting all M365-resident CUI workspaces, there is a possibility that unauthorized cross-tenant access leads to CUI exposure, resulting in [CMMC L2](https://dodcio.defense.gov/CMMC/) finding and DC3 notification. |
| Source | Architecture Review |
| Linked Control(s) | AC-3 / IA-2 / 800-171 3.1.1 |
| Regulatory Scope | CUI |
| Residual Likelihood / Impact | 2 / 5 → 10 (High) |
| Treatment | Mitigate |
| Linked POA&M | POAM-CUI-2026-0019 |

---

## 5. Exception Request Template

The exception is a request to deviate from a baseline control. It is a risk register entry once approved.

```
EXCEPTION REQUEST - EX-YYYY-NNNN

Requestor              :
Business Sponsor       :
Date Submitted         :
Requested Effective    :
Requested Expiration   :   (per RMF §9.7 default durations; shortest applicable regulatory or procedural duration wins)

Affected Asset(s)      :   (inventory ID + name)
Operating Unit         :
Regulatory Scope       :   CUI / BES / SOX / None

Control Being Deviated :   ([CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) control ID + family)
Subordinate Standard   :   (CERG-STD-* reference)
Standard Language      :   (quoted parameter that is being relaxed)
Proposed Deviation     :   (precise; not "we won't do X" but "we will do Y in place of X")

Business Driver        :   (why this is needed)
Compensating Controls  :   (specific, named, in place - not future tense)
Residual Risk Score    :   (per Section 6)
Risk Statement         :   (per Section 2)

Treatment Plan to      :
Close the Exception    :   (what makes this expire - usually a planned control)

Risk Owner             :
CERG Coordinator       :
Approver Required      :   (per PRC-RM-001 §8 - Engineering Mgr / CISO / Exec Sponsor)
```

Exception register fields mirror the risk register schema and add: **Exception ID**, **Standard Reference**, **Deviation Text**, **Compensating Controls**, **Expiration Date**, **Renewal Allowed (Y/N)**, **Renewal History**.

> **Exceptions Are Not "Forever"**
>
> Every exception has an expiration date and a treatment plan that retires it. An exception renewed more than twice without movement on the treatment plan is escalated by the Risk Register Owner to the approver one level above the original.

---

## 6. Risk Scoring Guide

CERG scores risk on a 5×5 matrix, with **control effectiveness** as a step-down from inherent to residual.

### 6.1 Likelihood (1–5)

| **Rating** | **Meaning** | **Indicators** |
|---|---|---|
| 1 - Rare | Unlikely in any 5-year window. | No known precedent; requires sophisticated, targeted attack. |
| 2 - Unlikely | Possible in 5 years. | Known but rare; requires specific conditions. |
| 3 - Possible | Plausible within 1 year. | Industry has examples; ordinary skill required. |
| 4 - Likely | Expected within 1 year. | Observed in peer organizations or commodity attack. |
| 5 - Almost Certain | Expected within 90 days or actively observed. | Active campaign, exposed surface, telemetry indicates attempts. |

### 6.2 Impact (1–5)

Impact is scored across **Safety**, **Operational**, **Financial**, **Regulatory**, and **Reputational** dimensions; the **highest** dimension wins.

| **Rating** | **Safety** | **Operational** | **Financial** | **Regulatory** | **Reputational** |
|---|---|---|---|---|---|
| 1 | None | < 1 hr / 1 system | < $100K | None | Internal only |
| 2 | Minor injury / near miss | < 4 hr / single BU | $100K–$1M | Informal finding | Localized awareness |
| 3 | Recordable injury | < 24 hr / multi-BU | $1M–$10M | Audit finding | Regional press |
| 4 | Serious injury | 24–72 hr / multi-OU | $10M–$50M | Material finding / fine | National press |
| 5 | Fatality / public safety | > 72 hr / safety event | > $50M | License at risk / criminal exposure | Sustained national / international |

### 6.3 Control Effectiveness Step-Down

| **Effectiveness** | **Likelihood Reduction** | **Impact Reduction** |
|---|---|---|
| Strong | −2 | −1 |
| Adequate | −1 | −1 |
| Weak | 0 | 0 |
| None | 0 | 0 |

Residual cannot fall below 1. Step-downs are applied to inherent, never to residual.

### 6.4 Heat Map Bands

| **Residual Score** | **Band** | **Approval Authority (per RMF §9.7 / PRC-RM-001 §8)** |
|---|---|---|
| 20–25 | Critical | CISO + Executive Sponsor; Board notified |
| 12–19 | High | CISO + Business Owner |
| 6–11 | Medium | Business Owner + Pillar Leader or Governance Pillar Leader |
| 2–5 | Low | Business Owner + Risk Register Owner |
| 1 | Informational | Risk Register Owner tracks; no formal acceptance required |

---

## 7. CISO Slice-and-Dice Reporting Views

The CISO will not consume the operational view. The CISO will consume views that compare and trend. The package below is what gets published, heat-maps, trend lines, and scorecards first; narrative memos in reserve for specific questions.

### 7.1 The Five Standing CISO Views

| **View** | **Purpose** | **Data Shape** |
|---|---|---|
| OU Scorecard | Compare operating units against each other on residual risk volume and trend. | One row per OU. Columns: Critical / High / Medium / Low counts; Δ vs. prior month; Open SLA breaches; Open Exceptions; Trend arrow. |
| OU Heat Map | Show where risk concentrates by OU × Family. | Matrix: OU rows × Control Family columns (AC, AU, CM, CP, IA, RA, SC, SI, SR). Cell = count of High/Critical. |
| Trend Lines | Are we getting better or worse? | Monthly: total residual score (sum), Critical+High count, mean time to close, open exception count. 13-month rolling. |
| Top 10 Risks | The set the board cares about. | The ten highest residual-score open risks with risk statement, owner, treatment, next milestone. |
| Regulatory Posture | Per-overlay summary. | CUI / BES / SOX rows; columns: Practices Implemented %, Open POA&M items, Open Exceptions, Next Assessment Date. |

### 7.2 Anti-Shallow-Metrics Guardrails

> **Don't Reward Closing Easy Vulns While Criticals Sit**
>
> The reporting views above deliberately weight *score sum* and *Critical+High count* over raw counts. A view that rewards closing 200 Lows while 4 Criticals sit untouched is a view that lies to the CISO. CERG reports the residual-score weighted sum first; raw counts second.

Additional guardrails baked into the views:

- **OU Scorecard "Trend Arrow"** is computed on residual-score weighted sum, never on count.
- **Top 10 Risks** rows must include the *age of the highest-impact unmitigated finding inside that risk*, so a 6-month-old Critical does not hide behind a freshly closed Low.
- **OU Heat Map** colors on Critical+High concentration, not on total count.
- **Regulatory Posture** "Practices Implemented %" is computed on the in-scope practice set with **Partially Implemented** counted as 0.5, not as 1.

### 7.3 Cadence

| **View** | **Refresh** | **Audience** |
|---|---|---|
| OU Scorecard | Monthly | CERG Leadership · OU Leadership |
| OU Heat Map | Monthly | CISO |
| Trend Lines | Monthly | CISO · Cyber Oversight Group |
| Top 10 Risks | Monthly + ad hoc | CISO · Cyber Oversight Group · Board (quarterly slice) |
| Regulatory Posture | Quarterly | CISO · Audit · Cyber Oversight Group |

---
## 8. Document Control

| | |
|---|---|
| **Document ID** | CERG-TMPL-RM-001 |
| **Version** | 1.22 |
| **Approved By** | CISO |
| **Next Review** | Annual / on tooling change |
| **Change Log** | 1.22 - Aligned scoring bands, approval authorities, and expiration guidance to RMF §9.7 / PRC-RM-001 §8. 1.0 - Initial publication. Schema, examples, exception template, scoring guide, CISO reporting views. |

