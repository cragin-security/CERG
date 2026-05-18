
# SURGE: Cyber Engineering, Risk & Governance

## METRICS, DASHBOARD, AND CISO / BOARD REPORTING
### Metrics Dictionary · KRI/KPI Data Source Map · CISO Dashboard · Brief and Report Templates

---

| | |
|---|---|
| **Document ID** | CERG-GOV-MTR-001 |
| **Version** | 1.0 |
| **Status** | For Review |
| **Classification** | Internal - Confidential |
| **Owner** | Cyber Governance Manager (Reporting) |
| **Parent Policy** | [CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-TMPL-RM-001](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · [CERG-PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) · [CERG_Risk_Management_Framework_v1.0](CERG_Risk_Management_Framework_v1.0.md) |
| **Review Cycle** | Annual / On metrics-platform change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · NIST 800-55 · ISO/IEC 27004 |
| **Regulations** | All - board reporting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Reporting Principles](#2-reporting-principles)
3. [Metrics Dictionary](#3-metrics-dictionary)
4. [KRI / KPI Data Source Map](#4-kri--kpi-data-source-map)
5. [CISO Risk and Posture Dashboard](#5-ciso-risk-and-posture-dashboard)
6. [Quarterly Cyber Oversight Group Brief Template](#6-quarterly-cyber-oversight-group-brief-template)
7. [Monthly CERG Leadership Report Template](#7-monthly-cerg-leadership-report-template)
8. [Anti-Shallow-Metrics Guardrails](#8-anti-shallow-metrics-guardrails)
9. [Cadence and Ownership](#9-cadence-and-ownership)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

[CERG-POL-001](CERG%20-%20Cybersecurity%20Policy.md) commits the CISO to reporting compliance posture and material risk to executive leadership and the board. The Operating Model defines maturity indicators; the RMF defines KRIs and escalation triggers; the VM and Risk procedures define standing metrics. This document closes the gap between those conceptual metrics and the operational reporting the CISO actually publishes.

It applies to every CERG-produced metric and every CERG-produced report consumed by the Cyber Oversight Group (CISO's reporting line, operating unit leadership, executives, or board depending on org structure), executive leadership, and the board.

---

## 2. Reporting Principles

Five principles govern how CERG reports, in order of priority:

1. **Trend over snapshot.** A single-point metric tells the consumer almost nothing. Every CISO-facing visual shows direction and rate of change.
2. **Heat-map over count.** The consumer wants to know *where* concentration is, not the totalled number. Bands and concentration over raw counts.
3. **Score sum over volume.** Closing 200 Lows while 4 Criticals sit is worse than closing 8 Criticals. CERG reports residual-score weighted sums first, raw counts second.
4. **Compare, then explain.** Operating units against each other; this period against last; us against peer benchmarks where credible. Narrative memos are reserved for the board's specific questions.
5. **Audience-appropriate altitude.** The CISO sees comparison and trend. The Cyber Oversight Group sees the same plus a narrative. The board sees the top five risks and one strategic chart per pillar.

> **What the CISO Does Not Care About**
>
> The CISO does not care that the team scanned 14,000 assets last month. The CISO cares which OU is worse than the others, where the concentration is, whether it's getting better, and what's blocking it. Metrics that don't answer one of those four questions don't reach the dashboard.

---

## 3. Metrics Dictionary

The dictionary is the source-of-truth definition for every CERG metric. Each entry has: ID · Name · Definition · Formula · Source · Owner · Refresh · Threshold (Green/Amber/Red) · Trend Direction · Reported In.

### 3.1 Risk-Side Metrics (Owner: Cyber Risk + Risk Register Owner)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| RM-001 | Open Critical+High Residual Risks | Count of `Status ∈ {Open, In Treatment}` with residual band ≥ High | Risk register | Daily | ≤ 10 / 11–25 / > 25 | CISO Dashboard, COG Brief |
| RM-002 | Residual Risk Score (Sum) | Σ residual score over open risks | Risk register | Daily | ≤ baseline−10% / ±10% / > baseline+10% | CISO Dashboard, Trend Lines |
| RM-003 | Mean Time to Close (High+) | Mean days from `Open` → `Closed/Accepted` for High and Critical | Risk register | Monthly | ≤ 60d / 61–120d / > 120d | CISO Dashboard |
| RM-004 | Exception Backlog | Open exceptions count | Exception register | Weekly | ≤ 25 / 26–60 / > 60 | CISO Dashboard |
| RM-005 | Exception Aging | % of open exceptions older than 12 months | Exception register | Monthly | ≤ 5% / 6–15% / > 15% | CISO Dashboard, COG Brief |
| RM-006 | OU Risk Concentration Index | Std deviation of OU residual-score weighted sums | Risk register | Monthly | ≤ baseline / ±10% / > baseline+10% | CISO Dashboard |

### 3.2 Vulnerability / Detection Metrics (Owner: Cyber Risk)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| VM-001 | DISH Critical Open Past SLA | Count of DISH-flagged Critical findings past SLA per [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | VM tool | Daily | 0 / 1–5 / > 5 | CISO Dashboard |
| VM-002 | DISH High Open Past SLA | Same for High | VM tool | Daily | ≤ 10 / 11–50 / > 50 | CISO Dashboard |
| VM-003 | Critical Closure Velocity | Critical findings closed this month / Critical findings opened this month | VM tool | Monthly | ≥ 1.0 / 0.8–1.0 / < 0.8 | CISO Dashboard |
| VM-004 | Critical Asset Coverage | Authenticated-scan coverage of Critical/High asset class | VM tool + Asset Inventory | Monthly | ≥ 98% / 90–98% / < 90% | CISO Dashboard, COG Brief |
| DT-001 | Day-One Detection Coverage | % of in-scope environments with full Day-One Set from [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | SIEM | Monthly | ≥ 95% / 80–95% / < 80% | CISO Dashboard |
| DT-002 | Purple Test Pass Rate | % of validated detections firing as expected | Purple results | Quarterly | ≥ 90% / 75–90% / < 75% | COG Brief |
| DT-003 | Mandatory Log Source Onboarding | % of mandatory sources from [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) onboarded | SIEM source inventory | Monthly | ≥ 98% / 90–98% / < 90% | CISO Dashboard |

### 3.3 Engineering / Configuration Metrics (Owner: Cyber Engineering)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| CM-001 | Baseline Drift Rate | % of assets failing DISH baseline | DISH scan | Daily | ≤ 2% / 3–8% / > 8% | CISO Dashboard |
| CM-002 | Architecture Reviews Completed Pre-Production | % of in-scope projects with completed AR before go-live | AR log | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard, COG Brief |
| CM-003 | Citizen-Dev Platforms with Guardrails | % of approved citizen-dev platforms with documented guardrails | Platform register | Quarterly | 100% / 90–100% / < 90% | COG Brief |
| CM-004 | Backup Success Rate (Critical Systems) | % of Critical-tier backups completed successfully | Backup tool | Daily | ≥ 99% / 95–99% / < 95% | CISO Dashboard |
| CM-005 | Restoration Test Currency | % of Tier-1 systems with current restoration test evidence | Resilience register | Quarterly | ≥ 95% / 80–95% / < 80% | CISO Dashboard |

### 3.4 Identity Metrics (Owner: Cyber Engineering: Identity)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| ID-001 | Phishing-Resistant MFA Coverage (Privileged) | % of privileged accounts with phishing-resistant MFA | IdP | Daily | 100% / 95–100% / < 95% | CISO Dashboard |
| ID-002 | Access Recertification Currency | % of in-scope systems with current recert | IGA | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard |
| ID-003 | Dormant Privileged Accounts | Count of privileged accounts with no use in 60 days | PAM | Weekly | 0 / 1–10 / > 10 | CISO Dashboard |
| ID-004 | Break-Glass Account Hygiene | % of break-glass accounts within rotation policy | PAM | Monthly | 100% / 90–100% / < 90% | CISO Dashboard |

### 3.5 Third-Party / Supply Chain Metrics (Owner: Cyber Risk: TPRM)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| TP-001 | Tier 1 Vendors with Current Attestation | % | TPRM tool | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard |
| TP-002 | SCCT Activations (Trailing 12m) | Count of SCCT activations | TPRM tool | Monthly | n/a - informational | COG Brief |
| TP-003 | International Access Exceptions | Open international-access exceptions | Exception register | Monthly | ≤ baseline / ±20% / > baseline+20% | CISO Dashboard |
| TP-004 | SBOM Coverage (Tier 1 Software) | % of Tier 1 software products with SBOM on file | TPRM tool | Quarterly | ≥ 90% / 75–90% / < 75% | COG Brief |

### 3.6 Governance / Regulatory Metrics (Owner: Cyber Governance)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| GV-001 | CUI Practices Implemented ([CMMC L2](https://dodcio.defense.gov/CMMC/)) | % of in-scope 800-171 practices `Implemented` (Partial = 0.5) | CUI register | Monthly | 100% / 95–100% / < 95% | CISO Dashboard, Reg Posture |
| GV-002 | Open POA&M Items (CUI) | Count + age of open POA&M | POA&M | Monthly | n/a - age-weighted | Reg Posture |
| GV-003 | NERC-CIP Evidence Library Currency | % of CIP requirements with current evidence ≤ cycle | OT GRC | Monthly | ≥ 98% / 90–98% / < 90% | Reg Posture |
| GV-004 | CIP Deviations Open | Count of approved deviations + average days open | OT GRC | Monthly | n/a | Reg Posture |
| GV-005 | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC Control Pass Rate | % of in-scope [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC tests passed in cycle | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) program | Quarterly | 100% / 95–100% / < 95% | Reg Posture |
| GV-006 | Policy/Standard Currency | % of CERG-managed artifacts within review cycle | Document Catalog | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard |

---

## 4. KRI / KPI Data Source Map

The data source map tells the reporting team where each metric's underlying data comes from, who keeps it healthy, and what happens when it breaks.

| **Metric IDs** | **Primary System of Record** | **Owning Role** | **Refresh Path** | **Failure Mode** |
|---|---|---|---|---|
| RM-001 – RM-006 | Risk register tool | Risk Register Owner | Nightly extract → metrics platform | Stale ETL: hold the day's CISO Dashboard, raise an Amber data-quality flag. |
| VM-001 – VM-004 | VM tool (e.g., Tenable) | Cyber Risk - VM | Hourly API → metrics platform | Tool outage: fall back to last-known-good snapshot with timestamp banner. |
| DT-001 – DT-003 | SIEM + detection coverage tool | Cyber Risk - Detection | Nightly source inventory + detection registry export | Missing source: detection coverage shown as Red. |
| CM-001 – CM-005 | Configuration / VM / Backup tools | Cyber Engineering - Platforms / Resilience | Nightly aggregation | Backup tool outage: pull from job log; flag as Amber. |
| ID-001 – ID-004 | IdP / IGA / PAM | Cyber Engineering - Identity | Nightly export | Source change: re-baseline before publishing. |
| TP-001 – TP-004 | TPRM tool | Cyber Risk - TPRM | Daily/weekly export | - |
| GV-001 – GV-006 | CUI register / OT GRC / [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) program / Document Catalog | Cyber Governance - domain owners | Monthly publish | - |

> **One Source per Metric**
>
> Each metric has exactly one system of record. Where two systems disagree, the system named here is authoritative and the other is reconciled. Reports that average two disagreeing sources hide the truth.

---

## 5. CISO Risk and Posture Dashboard

The CISO dashboard is the single page that opens every monthly review. It is laid out around the five standing views defined in [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) Section 7, plus the regulatory posture strip.

```
┌────────────────────────────────────────────────────────────────────────┐
│  CISO RISK & POSTURE - <Month> <YYYY>                                  │
├────────────────────────────────────────────────────────────────────────┤
│  TREND LINES (13-mo rolling)                                           │
│  · Residual Score Sum (RM-002)        ▁▂▃▄▄▅▆▇▆▅▄▄▃    ↓             │
│  · Critical+High Open Count (RM-001)  ▆▆▅▅▄▄▄▃▃▃▃▂▂   ↓             │
│  · Mean Time to Close H+ (RM-003)     ▂▃▄▅▅▄▃▃▃▂▂▂▂   ↓             │
├────────────────────────────────────────────────────────────────────────┤
│  OU SCORECARD (residual-score weighted, ranked)                        │
│  OU         │ Crit │ High │  Σ  │ Δ vs prior │ Trend │ Exc │ SLA breach│
│  Gen Ops    │   2  │   8  │ 184 │     -12    │  ↓    │  6  │     1     │
│  Trans Ops  │   1  │   5  │ 121 │      +4    │  ↑    │  3  │     2     │
│  Dist Ops   │   0  │   4  │  98 │      -3    │  →    │  4  │     0     │
│  Corp IT    │   1  │   3  │  85 │      -7    │  ↓    │  9  │     0     │
│  CUI Enclave│   0  │   2  │  46 │      -2    │  →    │  1  │     0     │
├────────────────────────────────────────────────────────────────────────┤
│  OU × FAMILY HEAT MAP (Critical+High concentration)                    │
│           AC  AU  CM  CP  IA  RA  SC  SI  SR                           │
│  Gen Ops  .   .   ▓▓  .   ▓   .   ▓▓  ▓   .                           │
│  Trans    .   .   ▓   .   .   .   ▓▓  ▓   .                           │
│  ...                                                                   │
├────────────────────────────────────────────────────────────────────────┤
│  TOP 10 RISKS                                                          │
│  ID         │ OU       │ Score │ Age │ Owner       │ Next Milestone   │
│  R-2026-0048│ Gen Ops  │  12   │ 91d │ Gen Ops Dir │ MFA wave 1 - Q3  │
│  ...                                                                   │
├────────────────────────────────────────────────────────────────────────┤
│  REGULATORY POSTURE                                                    │
│  CUI/CMMC L2 │ Practices: 92%  POA&M open: 18 (mean 67d)  Assessor: H1│
│  NERC-CIP    │ Evidence currency: 96%  Deviations open: 3              │
│  SOX ITGC    │ Test pass rate: 98%  Open deficiencies: 1               │
└────────────────────────────────────────────────────────────────────────┘
```

The dashboard is published from the metrics platform; the ASCII above is the layout reference for designers and dashboard builders. Color rules follow Section 3 Green/Amber/Red bands.

---

## 6. Quarterly Cyber Oversight Group Brief Template

The Cyber Oversight Group is whoever the CISO reports to, depending on org structure, it is IT and OU leadership, executive leadership, or the board itself. The brief is identical in structure regardless of audience; depth is calibrated by audience.

```
QUARTERLY CYBER OVERSIGHT GROUP BRIEF - Q<n> <YYYY>

1. EXECUTIVE TAKEAWAY (1 page max)
   · Are we more or less exposed than last quarter? Why?
   · The one decision the group needs to make this quarter.

2. STATE OF RISK
   · Trend Lines slide (RM-002, RM-001, RM-003)
   · OU Scorecard
   · Top 10 Risks with one-line status per risk

3. STATE OF THE PROGRAM
   · Maturity indicators against [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) targets
   · CERG capability deltas this quarter (people, tooling, scope expansion)

4. REGULATORY POSTURE
   · CUI / NERC-CIP / SOX one-line state each
   · Upcoming assessments / audits with dates and gating issues

5. INCIDENTS AND NEAR-MISSES (CERG-facing summary; full IR report separate)
   · Material events this quarter; lessons learned actioned

6. ASKS
   · Decisions, funding, scope, or organizational moves required from the group

7. APPENDIX
   · OU × Family Heat Map
   · Standing dashboard exports
   · Risk register changes since last brief
```

The brief is published five business days before the meeting. Slides are read-ahead; the meeting is for discussion of the Asks.

---

## 7. Monthly CERG Leadership Report Template

The internal CERG leadership report is consumed by Engineering / Risk / Governance pillar owners and the CISO. It is operational where the CISO Dashboard is comparative.

```
MONTHLY CERG LEADERSHIP REPORT - <Month> <YYYY>

A. SCORECARD vs. METRIC TARGETS
   · Full Section 3 dictionary, this month, with G/A/R indicator and 3-month spark

B. THIS MONTH'S DELTAS
   · Metrics that moved out of Green
   · Metrics that recovered into Green
   · Net new risks ≥ High and exceptions opened

C. PILLAR HIGHLIGHTS (one paragraph each)
   · Engineering - projects intaken, ARs completed, baselines deployed
   · Risk - VM trends, vendor activity, adversarial validation results
   · Governance - policy/standard changes, regulatory milestones, audit interactions

D. CROSS-PILLAR ITEMS
   · Items where ownership is unclear or work is blocked across pillars

E. NEXT MONTH
   · Top three deliverables and named owner
```

---

## 8. Anti-Shallow-Metrics Guardrails

The guardrails baked into the metric definitions and reporting views above:

1. **Score sum first, count second.** Headline figures are residual-score weighted (RM-002), not raw count.
2. **Partial = 0.5, not 1.** Regulatory implementation percentages count Partially Implemented as half. (Forces honesty.)
3. **Age weighting on regulatory openness.** POA&M items report mean age, not just count.
4. **Closure velocity, not closure count.** VM-003 reports closed/opened ratio so closing 200 lows doesn't mask 4 critical opens.
5. **Concentration over volume.** OU heat map colors on Critical+High concentration, not total findings.
6. **No "scanned X assets" headlines.** Activity metrics are operational, never on the CISO dashboard.
7. **Trend direction is the headline.** Every CISO-facing metric carries a 13-month spark or arrow.
8. **Bands published with the metric.** Green/Amber/Red bands are part of the definition; moving them requires a change request, not an editorial decision.

> **A Metric That Can't Show "Worse" Should Not Be Reported**
>
> If a metric is structured such that good operating units always look good and bad ones can hide, it's vanity. CERG either reframes the metric to expose the gap or removes it from the dashboard.

---

## 9. Cadence and Ownership

| **Artifact** | **Cadence** | **Owner** | **Audience** |
|---|---|---|---|
| CISO Dashboard | Monthly | Cyber Governance - Reporting | CISO |
| Monthly CERG Leadership Report | Monthly | Cyber Governance - Reporting | CERG Leadership |
| Quarterly COG Brief | Quarterly | CISO + Cyber Governance - Reporting | Cyber Oversight Group (per org structure) |
| Board read-out slice | Quarterly | CI