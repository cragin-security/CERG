
# SURGE: Cyber Engineering, Risk & Governance

## MATURITY SELF-ASSESSMENT AND SCORECARD
### Tier Self-Scoring · Pillar Domains · Gap Output · Re-Measurement

---

| | |
|---|---|
| **Document ID** | CERG-GOV-MAT-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) · [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| **Review Cycle** | Annual / On any change to the V1 library |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · NIST 800-55 · ISO/IEC 27004 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How the Assessment Works](#2-how-the-assessment-works)
3. [The Tier Scale](#3-the-tier-scale)
4. [Scoring Rules](#4-scoring-rules)
5. [The Assessment: Governance Domains](#5-the-assessment-governance-domains)
6. [The Assessment: Engineering Domains](#6-the-assessment-engineering-domains)
7. [The Assessment: Risk Domains](#7-the-assessment-risk-domains)
8. [The Assessment: Cross-Pillar Domains](#8-the-assessment-cross-pillar-domains)
9. [Scoring the Result](#9-scoring-the-result)
10. [The Scorecard Output](#10-the-scorecard-output)
11. [Turning Gaps Into Work](#11-turning-gaps-into-work)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

[`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) §6 sets the target: the CERG model is designed to produce NIST CSF Adaptive-tier behavior. That is the aspiration. This document supplies the missing instrument: a way for an adopter to measure where the program actually sits today, and what stands between today and Adaptive.

It is a self-assessment. An organization scores itself against 24 domains, each tied to real CERG artifacts and observable evidence. The output is a tier per domain, a tier per pillar, an overall tier, and a ranked list of the gaps worth closing first.

It applies program-wide. It is run at day 1 of adoption to set a baseline, at day 90 to measure first-quarter movement (see [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §5), and annually after that.

> **A Self-Assessment Is Only Useful If It Is Honest**
>
> The temptation in any self-scoring exercise is to score the intention rather than the evidence. CERG maturity scoring has one rule above all others: a domain scores at a tier only if the organization can produce the evidence named for that tier. Not "we do that," but "here is the artifact." A maturity score that cannot survive an auditor reading it is worth nothing. Score what you can show.

---

## 2. How the Assessment Works

The assessment has four moving parts.

1. **Domains.** 24 assessment domains, grouped by pillar (Governance, Engineering, Risk) plus a Cross-Pillar group. Each domain is a coherent slice of the program tied to specific CERG artifacts.
2. **The tier scale.** Each domain is scored against the four NIST CSF tiers: Partial, Informed, Repeatable, Adaptive. Section 3 defines them.
3. **Evidence anchors.** Each domain lists what the organization must be able to show to claim each tier. Scoring is anchored to evidence, not opinion.
4. **The scorecard.** Domain scores roll up to pillar scores and an overall score, and the lowest-scoring domains become the gap list.

The assessment is run by the Governance Pillar Leader, scored with the pillar leaders, and reviewed by the CISO. It is not run by one person in a room. A domain tier is agreed by the pillar that owns the work, and challenged by Governance.

> **This Maps to the Same Tiers the Framework Uses**
>
> The four tiers here are exactly the four tiers in [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) §6.1. This is deliberate. The framework says where CERG aims; this assessment says where you are on the same ruler. The gap between them is your roadmap.

---

## 3. The Tier Scale

| **Tier** | **Score** | **What It Means for a Domain** |
|---|---|---|
| **Partial** | 1 | Ad hoc. The work happens reactively or not at all. No adopted CERG artifact governs it. Evidence is absent or accidental. |
| **Informed** | 2 | The relevant CERG artifact is adopted and adapted, but practice is inconsistent. The work happens in some places, by some people, some of the time. Evidence is partial. |
| **Repeatable** | 3 | The artifact is adopted and the practice is consistent. The work happens on its defined cadence, by the named role, every time. Evidence is collected systematically and is current. |
| **Adaptive** | 4 | Repeatable, plus the domain improves itself. Metrics drive change, lessons and intelligence feed back in, and the practice is reviewed and tuned. Evidence shows a trend, not just a snapshot. |

A domain never scores above the evidence. If a domain has consistent practice but no metric driving improvement, it is Repeatable, not Adaptive, no matter how well it runs.

---

## 4. Scoring Rules

1. **Score to the evidence floor.** A domain scores at the highest tier for which every evidence anchor at that tier and below can be produced. One missing anchor caps the domain at the tier below.
2. **A domain with no adopted artifact is Partial.** Tier 2 and above require the governing CERG artifact to be adopted. An un-adopted domain is Partial by definition, score 1.
3. **Partial implementation counts as half.** Where a domain is genuinely between two tiers, score the lower tier. Do not round up. This mirrors the anti-shallow-metrics discipline in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §8.
4. **Score the domain, not the document.** A standard can be beautifully written and score Partial because no one follows it. The score reflects practice and evidence, not prose.
5. **One scorer cannot self-clear.** The pillar that owns the work proposes the tier; Governance challenges it; the CISO accepts the final score. A domain tier is never set by a single unchallenged voice.
6. **Record the evidence.** Every domain score is recorded with the specific artifact, register, or report that supports it. A score with no recorded evidence is not a score.

---

## 5. The Assessment: Governance Domains

Score each domain 1 to 4 against the tier scale. The evidence column names what supports the Repeatable (3) tier; Adaptive (4) additionally requires a metric or review loop driving improvement.

| **#** | **Domain** | **Governing Artifact(s)** | **Repeatable-Tier Evidence** | **Score** |
|---|---|---|---|---|
| G1 | Policy and accountability | [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) | Signed policy; named CISO; named Executive Sponsor; review date current. | |
| G2 | Document control and catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Catalog matches the live library; every artifact has an ID, owner, and status. | |
| G3 | Operating model and roles | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical roles assigned to named people; decision rights understood. | |
| G4 | Control baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control set adopted; each control has a named evidence owner. | |
| G5 | Risk management framework | [`CERG-GOV-RMF-001`](CERG_Risk_Management_Framework_v1.0.md) | Risk scored and treated per the RMF; approval authority table applied. | |
| G6 | Risk register operation | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Live register; Monthly Risk Register Review held; exceptions tracked. | |
| G7 | Metrics and CISO reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | CISO dashboard published on cadence; metrics defined with bands. | |
| G8 | Compliance and audit posture | [`CERG-GOV-CMX-001`](CERG%20Compliance%20Matrix.md), applicable `CERG-PLN` packages | Compliance matrix maintained; per-regulator package adopted for each regulator in scope. | |

---

## 6. The Assessment: Engineering Domains

| **#** | **Domain** | **Governing Artifact(s)** | **Repeatable-Tier Evidence** | **Score** |
|---|---|---|---|---|
| E1 | Architecture review and project intake | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Projects routed through intake; pre-production reviews recorded. | |
| E2 | Secure configuration and hardening | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Baselines defined and deployed; drift detected and corrected. | |
| E3 | Identity and access management | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md), [`CERG-PRC-AC-002`](CERG-PRC-AC-002_Access_Management_Runbook.md) | Access provisioned and reviewed per the runbook; MFA and PAM in force. | |
| E4 | Cryptography and key management | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Cipher and key lifecycle managed; certificate inventory current. | |
| E5 | Cyber resilience and backup | [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | RTO/RPO defined; backups verified; recovery tested. | |
| E6 | IT, cloud, and SaaS security | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Cloud and SaaS controls applied; landing-zone posture enforced. | |
| E7 | OT and control systems security | [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | OT controls applied where OT exists; IT/OT boundary defined. Score `N/A` if no OT. | |
| E8 | Pre-production go-live readiness | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Pre-production checklist owned and signed before go-live; findings remediated or risk-accepted. | |

---

## 7. The Assessment: Risk Domains

| **#** | **Domain** | **Governing Artifact(s)** | **Repeatable-Tier Evidence** | **Score** |
|---|---|---|---|---|
| R1 | Vulnerability management | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | Scanning runs on cadence; remediation SLAs tracked and met. | |
| R2 | Adversarial validation | [`CERG-PRC-AV-001`](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Pen test, red team, or purple team exercises run and findings tracked. | |
| R3 | Third-party and supply chain risk | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendors tiered and assessed; supply chain risks in the register. | |
| R4 | Logging, monitoring, and detection | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Log sources defined; retention enforced; detection coverage mapped. | |
| R5 | Risk taxonomy and exposure posture | [`CERG-GOV-TAX-001`](CERG%20Risk%20Taxonomy.md) | Risks categorized to the taxonomy; exposure posture reported. | |
| R6 | Threat intelligence | [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) §6.2 | Intelligence collected and distributed to Engineering, Detection, and Governance. | |
| R7 | Pre-production versus post-production risk discipline | [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) §4.3 | Pre-production findings handled as engineering inputs; post-production findings as managed risks. | |

> **R6 Threat Intelligence Has No Dedicated Procedure Yet**
>
> Domain R6 is scored against the framework narrative because the V1 library does not yet contain a standalone threat intelligence procedure. An organization can still score R6 honestly against observable practice. When a threat intelligence procedure is added to the catalog, this domain's governing artifact is updated to point at it.

---

## 8. The Assessment: Cross-Pillar Domains

These domains measure how well the pillars work as one program. They are where the CERG model either delivers on its premise or does not.

| **#** | **Domain** | **Governing Artifact(s)** | **Repeatable-Tier Evidence** | **Score** |
|---|---|---|---|---|
| X1 | Pillar handoffs | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | The structured handoffs in the README lifecycle table happen, with no work dropped between pillars. | |
| X2 | Coordination cadence | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | The standing coordination cadence is held; cross-pillar blockers are surfaced. | |
| X3 | Incident response liaison | [`CERG-PLN-IR-001`](CERG-PLN-IR-001_Incident_Response_Plan.md) | CERG feeds detection, vulnerability, and asset data to the IR team; liaison roles are named. | |
| X4 | Adoption and adaptation discipline | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md), [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Corpus adapted via the render tool; one profile file; catalog kept current. | |
| X5 | Single-point-of-failure resilience | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6 | Critical roles are backstopped; no role is held by exactly one person with no cover. | |

---

## 9. Scoring the Result

### 9.1 Domain to Pillar

For each pillar, average its domain scores. Exclude any domain scored `N/A` (for example, E7 OT for an organization with no operational technology) from both the sum and the count.

```
Pillar score = sum of in-scope domain scores / count of in-scope domains
```

### 9.2 Pillar to Overall

The overall program tier is the average of the four group scores (Governance, Engineering, Risk, Cross-Pillar), then mapped:

| **Average** | **Overall Tier** |
|---|---|
| 1.00 to 1.74 | Partial |
| 1.75 to 2.49 | Informed |
| 2.50 to 3.49 | Repeatable |
| 3.50 to 4.00 | Adaptive |

### 9.3 The Honesty Check

Before the score is accepted, the CISO applies one test: the **weakest-link read**. If any single domain is scored Partial, the program is not Repeatable overall in practice, regardless of the average. A Partial domain is a hole, and an average cannot fill a hole. The CISO records the overall tier *and* the count of Partial domains. Both numbers are reported.

> **The Average Can Lie. The Partial Count Cannot.**
>
> An organization with twenty Repeatable domains and four Partial ones averages out near Repeatable. But those four Partial domains are four places the program does not function. CERG reports the average and the Partial count side by side, exactly as the metrics standard reports score-sum alongside raw count. A program is only as mature as its weakest in-scope domain.

---

## 10. The Scorecard Output

The assessment produces a one-page scorecard. It is the artifact the CISO carries into the Cyber Oversight Group brief.

### 10.1 Scorecard Layout

```
CERG MATURITY SCORECARD
Organization: {{ORG_NAME}}        Assessment date: {{ADOPTION_DATE}}
Assessed by: Governance Pillar Leader   Accepted by: CISO

OVERALL TIER:  [ Partial | Informed | Repeatable | Adaptive ]
Overall average: X.XX        Partial domains: N

PILLAR SCORES
  Governance     X.XX   [tier]
  Engineering    X.XX   [tier]
  Risk           X.XX   [tier]
  Cross-Pillar   X.XX   [tier]

DOMAIN RADAR
  A four-axis radar (one axis per group) or a 24-spoke radar (one
  spoke per domain), each axis plotted 1 to 4. The shape shows
  concentration of weakness at a glance.

THIS ASSESSMENT vs LAST
  Per pillar: arrow up / flat / down, with the delta.

TOP FIVE GAPS
  The five lowest-scoring in-scope domains, lowest first, each with
  its governing artifact and the tier it needs to reach.
```

### 10.2 Radar Specification

The radar is the headline visual. Plot one axis per assessment domain (24 spokes) or, for a board-altitude view, one axis per group (4 spokes). Each axis runs 1 (center) to 4 (edge). The current assessment is one filled shape; the prior assessment is an outline overlaid on top. A program moving toward Adaptive grows the shape outward over successive assessments. A dent in the shape is a gap, visible without reading a number.

This pairs with the trend-over-snapshot principle in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §2: the radar is only fully useful from the second assessment onward, when it carries an overlay.

### 10.3 Cadence

| **Assessment** | **When** | **Purpose** |
|---|---|---|
| Baseline | Day 1 of adoption | Set the starting tier; seed the risk register with Partial domains. |
| First-quarter | Day 90 of adoption | Measure first-cycle movement per [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §5.3. |
| Annual | Every 12 months | Track the trend toward Adaptive; reset the gap list. |
| Triggered | After a major incident, audit finding, or org change | Re-score the affected domains. |

---

## 11. Turning Gaps Into Work

A scorecard that is filed and forgotten is vanity. The assessment is only finished when its gaps become tracked work.

1. **Every Partial domain becomes a risk register entry.** A domain scored Partial is an accepted gap until it is closed. It goes in the register per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), with an owner and a target tier.
2. **The top five gaps get named owners and dates.** The lowest five in-scope domains are the program's improvement backlog for the period. Each gets a pillar leader as owner and a target date.
3. **The next assessment measures the close.** A gap is closed when the domain re-scores at its target tier with evidence. The radar overlay shows it.
4. **Adaptive is a destination, not a checkbox.** A domain reaches Adaptive only when a metric or review loop is demonstrably driving its improvement. Closing gaps to Repeatable is the bulk of the work; reaching Adaptive is the last and hardest step, and it is what [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) §6 describes.

> **The Assessment Is Not the Goal**
>
> Scoring the program is half a day of work. Closing the gaps it finds is a year of work. An organization that runs the assessment, files the scorecard, and changes nothing has measured its program without improving it. The deliverable of this document is not a tier. It is the next five things the program will fix.

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-MAT-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | Chief Information Security Officer (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to the V1 library |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); NIST 800-55; ISO/IEC 27004 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-21 | Cyber Governance | Initial release. Establishes the four-tier self-assessment, 24 assessment domains across Governance, Engineering, Risk, and Cross-Pillar groups, evidence-anchored scoring rules, the domain-to-pillar-to-overall rollup with the weakest-link honesty check, the one-page scorecard and radar output specification, the assessment cadence, and the gaps-into-work discipline. |

### Review Triggers

- Any artifact added to or retired from the V1 library, which changes the domain set
- A standalone threat intelligence procedure is added to the catalog (updates domain R6)
- Material change to the tier definitions in [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) §6
- Adopter feedback indicating a domain is missing or mis-scoped
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Document Control) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG%20-%20Cybersecurity%20Policy.md) | Parent policy |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative artifact inventory; the domain set tracks the catalog |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) | Defines the four tiers and the Adaptive target this assessment measures against |
| Implementation and Adaptation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Schedules the baseline and day-90 assessments |
| Organization Adaptation Profile | [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Supplies the tokens used in the scorecard layout |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical roles that own domain scores |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control set assessed by domain G4 |
| Metrics, Dashboard, and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Shares the trend-over-snapshot and score-sum reporting discipline |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Where Partial domains are tracked as accepted gaps |
