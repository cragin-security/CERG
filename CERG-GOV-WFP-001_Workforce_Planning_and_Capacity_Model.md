# SURGE: Cyber Engineering, Risk & Governance

## WORKFORCE PLANNING AND CAPACITY MODEL
### Staffing Methodology · Workload Drivers · Scaling Guidance

---

| | |
|---|---|
| **Document ID** | CERG-GOV-WFP-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) · [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) · [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) |
| **Review Cycle** | Annual / Before each budget cycle |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.7.1 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The Capacity Problem](#2-the-capacity-problem)
3. [Workload Drivers by Pillar](#3-workload-drivers-by-pillar)
4. [The Staffing Methodology](#4-the-staffing-methodology)
5. [Engineering Pillar: Capacity Model](#5-engineering-pillar-capacity-model)
6. [Risk Pillar: Capacity Model](#6-risk-pillar-capacity-model)
7. [Governance Pillar: Capacity Model](#7-governance-pillar-capacity-model)
8. [The Scaling Map: From 5 to 60+](#8-the-scaling-map-from-5-to-60)
9. [Validating the Model](#9-validating-the-model)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

A CISO walks into a budget meeting and says "I need three more Cloud Security Engineers." The CFO asks "why three, and why Cloud Security Engineers specifically?" The CISO who cannot answer that question with a methodology will get zero, or one, or a contractor for six months with no renewal path. The CISO who produces a capacity model built on workload drivers, not headcount comparisons, will get a conversation about which assumptions the CFO disagrees with. A conversation about assumptions is a negotiation. A conversation without assumptions is a request.

This document provides the methodology. It defines the workload drivers for each pillar, translates them into staffing formulas, and provides the scaling guidance that supports a headcount request from a 5-person startup CERG to a 60-person enterprise function. It is designed to be a live tool: organizations plug in their numbers and get a recommended staffing range with documented rationale.

It applies to every CERG role. It does not prescribe exact headcount; it prescribes the method for arriving at a defensible headcount. The output is a range, not a single number, because judgment about organizational context, team composition, and automation maturity always matters.

> **Headcount Without Methodology Is a Wish**
>
> Every CISO has a wishlist. The capacity model turns wishes into requests and requests into negotiations. It will not eliminate the budget conversation. It will make the conversation about the model's assumptions, not about whether the CISO is credible. That is a better conversation to have.

---

## 2. The Capacity Problem

### 2.1 Why Cybersecurity Staffing Is Hard to Model

Most corporate functions have stable workload-to-headcount ratios. Accounts payable: X invoices per clerk per month. IT support: Y tickets per technician per day. Cybersecurity does not work this way for three reasons:

1. **Workload is adversary-driven, not business-driven.** A new ransomware variant can multiply the detection engineering workload overnight. A zero-day in a widely deployed platform can turn every Cloud Security Engineer's week into emergency response.
2. **Work is invisible when done well.** A Cloud Security Engineer who prevents a misconfigured S3 bucket from reaching production has done some of the highest-value work in the organization. The work produced no ticket, no finding, and no metric other than the absence of a breach. Capacity models that measure only tickets undercount security engineering by design.
3. **Regulatory scope changes the workload non-linearly.** Adding NERC-CIP to an organization's compliance scope does not add one FTE of Governance work. It adds a compliance manager, an evidence librarian, OT engineering support, and a new audit cycle. Frameworks multiply; they do not add.

### 2.2 The Capacity Model's Answer

This model addresses the capacity problem by defining workload drivers that are:

- **Observable.** An organization can count its projects, assets, vendors, and frameworks.
- **Predictive.** The relationship between the driver and the staffing need is grounded in how CERG roles actually spend their time.
- **Ranged.** Every formula produces a range (minimum, target, maximum), not a point estimate. The range accounts for organizational context, automation maturity, and team experience.
- **Calibratable.** Organizations that track actual time allocation can refine the model's coefficients. An organization that discovers its Cloud Security Engineers spend 40% of their time on architecture review rather than the model's assumed 30% can adjust the formula for its next cycle.

---

## 3. Workload Drivers by Pillar

### 3.1 Engineering Pillar Drivers

| Driver | Definition | Why It Matters |
|---|---|---|
| **Active projects** | Number of concurrently active projects receiving Engineering engagement (architecture review through go-live) | Each project consumes recurring Engineering time for architecture review, pre-production check, and go-live support |
| **Project complexity mix** | Distribution of projects across Low, Medium, and High complexity tiers | A High-complexity project (new cloud region, major platform migration, M&A integration) consumes 3-5x the Engineering hours of a Low-complexity project (SaaS onboarding, minor feature deployment) |
| **Platform count** | Number of distinct platforms requiring reference architecture and security engineering (e.g., AWS, Azure, GCP, on-prem virtualization, OT environments) | Each platform requires a reference architecture, configuration baselines, and ongoing security engineering. Platforms multiply workload, not just add to it |
| **Pre-production review volume** | Number of pre-production reviews per week | A hard gate that requires Engineering attendance; cannot be automated away entirely |
| **Vertical coverage** | Number of business verticals or operating companies requiring dedicated engineering alignment | A Cloud Security Engineer assigned to a specific business unit develops context that a pooled engineer cannot. Vertical alignment improves quality but reduces fungibility |

### 3.2 Risk Pillar Drivers

| Driver | Definition | Why It Matters |
|---|---|---|
| **Assets under management** | Number of IP-addressable assets (servers, endpoints, network devices, cloud resources, OT devices) in the vulnerability management and CSPM scope | Scanning, triage, and remediation tracking effort scales with asset count, though not linearly (automation absorbs some growth) |
| **Vendor portfolio size** | Number of vendors in the third-party risk assessment program, weighted by tier (Critical, High, Medium, Low) | Critical-tier vendors require annual reassessment with deeper due diligence; Low-tier vendors may be assessed once and monitored |
| **Scan frequency** | Vulnerability scan cadence (continuous, daily, weekly) and scope (internal, external, cloud, OT) | Continuous scanning produces more findings to triage; weekly scanning produces manageable volumes with acceptable risk windows |
| **Testing cycle requirements** | Number of penetration tests, red team exercises, and purple team engagements per year, plus any regulatory-mandated testing | A NERC-CIP entity has mandated testing cycles. A commercial entity may have an annual pen test. The difference is 4-6x in Adversarial Testing Lead workload |
| **Threat intelligence production** | Number of threat advisories, briefings, and intelligence products produced per week or month | A team producing daily threat briefs for leadership needs more analyst capacity than one producing weekly summaries |
| **Detection surface** | Number of log sources, detection rules, and use cases under active management | Each new log source requires parsing, baseline profiling, and detection rule authoring. Detection engineering workload grows with the detection surface, not with headcount |

### 3.3 Governance Pillar Drivers

| Driver | Definition | Why It Matters |
|---|---|---|
| **Regulatory frameworks** | Number of distinct regulatory or compliance frameworks in scope (e.g., NERC-CIP, CMMC, SOX, ISO 27001, PCI) | Each framework adds its own evidence requirements, audit cycle, and regulatory change monitoring. Frameworks with overlapping controls reduce the multiplier but do not eliminate it |
| **Control count** | Number of controls in the unified control baseline that require evidence collection and testing | Each control has an evidence refresh cycle. More controls = more evidence librarian and compliance manager hours |
| **Audit frequency** | Number of external audits, assessments, and regulatory exams per year | Each audit consumes 4-8 weeks of Governance pillar time for preparation, walkthroughs, evidence delivery, and finding response |
| **Evidence volume** | Number of evidence items maintained in the evidence library, refreshed on defined cycles | Evidence that is stale at audit time must be recollected under pressure, consuming 2-3x the effort of evidence maintained on schedule |
| **Policy and standard count** | Number of policies, standards, and procedures requiring annual review, update, and stakeholder coordination | Each document has a review cycle, a stakeholder list, and an approval workflow. Document count drives Policy & Standards Manager workload directly |

---

## 4. The Staffing Methodology

### 4.1 The Base Formula

For each role, the recommended staffing range is calculated as:

```
Headcount = ⌈(Driver1 / Throughput1) + (Driver2 / Throughput2) + ...⌉ × Complexity Factor × Automation Discount
```

Where:
- **Driver** is the workload driver value for the organization (e.g., 45 active projects)
- **Throughput** is the number of driver units one FTE can handle at target quality (e.g., 8-12 active projects per Cloud Security Engineer)
- **Complexity Factor** adjusts for organizational complexity beyond the baseline (1.0 = baseline; 1.3 = highly complex; 0.8 = low complexity)
- **Automation Discount** reduces headcount for mature automation (1.0 = no automation; 0.85 = moderate automation; 0.70 = high automation)

The ceiling brackets ⌈...⌉ indicate rounding up to the nearest whole person. A calculation that produces 2.3 FTEs means 3 people; the 0.7 surplus is absorbed by management overhead, surge capacity, and the reality that cybersecurity work does not divide evenly.

### 4.2 The Role Consolidation Rule

The scaling map in CERG-GOV-RAC-001 §8 shows how 27 canonical roles consolidate onto as few as 5 people. This model respects that consolidation. When the formula produces less than 1.0 FTE for a role, the role is consolidated onto an adjacent role rather than fractionalized:

- If the model says 0.4 Detection Engineers and 0.6 Threat Intelligence Analysts, both roles consolidate onto one person who splits their time, or the Detection Engineering work is absorbed by the Vulnerability Management Lead
- Pillar Leader roles consolidate downward: in a 5-person CERG, the CISO directly manages all pillars, and the senior-most practitioner in each pillar operates as a player-coach at S3-S4

The model reports both the unconsolidated headcount (what the formula says) and the consolidated headcount (how roles combine for organizations below a certain scale).

### 4.3 The Management Overhead Factor

Every IC headcount carries a management overhead. The overhead is not linear (a 3-person team does not need 0.3 Managers; it needs zero) but emerges at certain thresholds:

| IC Headcount in Function | Management Overhead |
|---|---|
| 1-5 | 0 (consolidated onto pillar leader or CISO) |
| 6-10 | 1 Manager (M1) |
| 11-20 | 1 Senior Manager (M2) + 1 Manager (M1), or 2 Managers |
| 21-40 | 1 Principal Manager (M3) + 1-2 Senior Managers (M2) + 1-2 Managers (M1) |
| 40+ | 1 Director (M4) + management hierarchy as above |

---

## 5. Engineering Pillar: Capacity Model

### 5.1 Cloud Security Engineer

**Primary driver:** Active projects requiring cloud security engagement.

| Complexity Tier | Projects per Engineer (Baseline) | Description |
|---|---|---|
| **Low** | 12-15 | SaaS tool security review, minor IAM policy change, CSPM alert tuning |
| **Medium** | 6-8 | New AWS account onboarding with landing zone, cloud network segmentation change, significant IaC module development |
| **High** | 2-3 | New cloud region deployment, multi-cloud architecture design, major platform migration, M&A cloud integration |

**Formula:**
```
CE = ⌈(Low_Projects / 14) + (Med_Projects / 7) + (High_Projects / 2.5)⌉ × CF × AD
```

**Additional drivers:**
- +0.5 CE for every distinct major cloud platform beyond the first (AWS + Azure = 0.5 additional)
- +0.5 CE if the organization operates SaaS security posture management separately from IaaS security
- +1.0 CE if the organization has a dedicated cloud security engineering function for OT/ICS environments

### 5.2 Identity Engineer

**Primary driver:** Identity platform complexity and integration surface.

| Scope | Engineers Required | Trigger |
|---|---|---|
| **Single IdP, cloud-native, no federation** | 0.5-1.0 | Organization uses one identity provider (e.g., Azure AD/Entra ID), minimal external federation, no PAM program |
| **Multi-IdP, federation, basic PAM** | 1.0-2.0 | Multiple identity providers, B2B federation, a PAM solution for privileged access |
| **Complex identity: multi-cloud, legacy, PAM, customer IAM** | 2.0-4.0 | Identity spans on-prem AD, cloud IdP, customer-facing CIAM, legacy application authentication, PAM with session management |

**Formula:**
```
IE = Base(Org_Size_Tier) + Federation_Count × 0.3 + PAM_Program × 0.5 + CIAM_Program × 0.5
```

Where Base(Org_Size_Tier) is: Small = 0.5, Medium = 1.0, Large = 1.5, Enterprise = 2.0.

### 5.3 OT Security Engineer

**Primary driver:** OT environment count and complexity.

| Scope | Engineers Required |
|---|---|
| **No OT environment** | 0 |
| **Single OT site, limited CIP scope** | 1.0 |
| **Multiple OT sites, NERC-CIP Medium impact** | 1.5-2.5 |
| **Multiple OT sites, NERC-CIP High impact, IT/OT convergence** | 2.5-4.0 |

OT Security Engineers are rarely filled below S2. The minimum staffing for any organization with an OT environment is 1.0 FTE; below that, the role consolidates onto a Cloud Security Engineer with OT training (and the risk of that consolidation should be explicitly acknowledged).

### 5.4 Application Security Engineer

**Primary driver:** Development team count and deployment frequency.

| Scope | Engineers Required |
|---|---|
| **1-3 development teams, quarterly releases** | 0.5-1.0 |
| **4-10 development teams, monthly releases** | 1.0-2.0 |
| **11-25 development teams, bi-weekly or continuous deployment** | 2.0-4.0 |
| **Enterprise software organization with multiple product lines** | 4.0-8.0 |

**Formula:**
```
AppSec = ⌈Dev_Teams / 8⌉ + (CI_CD_Maturity × 0.5)
```

Where CI_CD_Maturity = 0 (quarterly/manual), 1 (monthly), 2 (continuous).

### 5.5 Endpoint Engineer

**Primary driver:** Endpoint count and platform diversity.

| Scope | Engineers Required |
|---|---|
| **<2,000 endpoints, single OS** | 0.5 |
| **2,000-10,000 endpoints, 2 OS platforms** | 1.0 |
| **10,000-50,000 endpoints, 3+ OS platforms, mobile** | 1.5-2.5 |
| **50,000+ endpoints, multi-OS, VDI, mobile, OT endpoint overlap** | 2.5-4.0 |

### 5.6 Cryptography Engineer

**Primary driver:** PKI scale and regulatory crypto requirements.

| Scope | Engineers Required |
|---|---|
| **Basic TLS, no on-prem PKI, no regulatory crypto mandate** | 0.5 (consolidate with Cloud Security or Identity Engineer) |
| **On-prem PKI, internal CA, TLS certificate lifecycle management** | 1.0 |
| **Enterprise PKI, HSM management, FIPS compliance, code signing** | 1.5-2.5 |
| **Multi-tier CA, cross-certification, regulatory crypto (CIP, CMMC)** | 2.5-4.0 |

---

## 6. Risk Pillar: Capacity Model

### 6.1 Vulnerability Management Lead / Analyst

**Primary driver:** Assets under management and scan frequency.

| Scope | Staff Required |
|---|---|
| **<5,000 assets, weekly scanning** | 1.0 |
| **5,000-25,000 assets, continuous scanning** | 1.5-3.0 |
| **25,000-100,000 assets, continuous scanning, multi-platform** | 3.0-6.0 |
| **100,000+ assets, continuous scanning, OT segmentation** | 6.0-12.0 |

**Formula:**
```
VM = ⌈(Assets / 8000) × Scan_Freq_Factor⌉ + OT_Assets × 0.3
```
Where Scan_Freq_Factor = 0.8 (weekly), 1.0 (daily), 1.3 (continuous). OT_Assets is in thousands.

### 6.2 Adversarial Testing Lead

**Primary driver:** Testing cycles and scope breadth.

| Scope | Staff Required |
|---|---|
| **Annual external pen test (outsourced)** | 0.0 (the outsourced test is managed by the Risk Pillar Leader or VM Lead) |
| **Annual pen test (internal or co-sourced) + one purple team exercise** | 1.0 |
| **Semi-annual pen test + quarterly purple team + annual red team** | 2.0-3.0 |
| **Continuous testing program + red team operations + purple team + regulatory-mandated cycles** | 3.0-6.0 |

### 6.3 Threat Intelligence Analyst

**Primary driver:** Intelligence production volume and source diversity.

| Scope | Staff Required |
|---|---|
| **Consuming third-party threat feeds, no production** | 0.5 (consolidate with Detection Engineer or VM Lead) |
| **Weekly threat briefings, 2-3 intelligence sources, basic actor tracking** | 1.0 |
| **Daily threat briefings, 5+ intelligence sources, sector-specific ISAC participation** | 1.5-2.5 |
| **Full threat intelligence program: strategic/operational/tactical, dedicated platforms, external collaboration** | 2.5-5.0 |

### 6.4 Vendor Risk Analyst

**Primary driver:** Vendor portfolio size weighted by tier.

| Scope | Staff Required |
|---|---|
| **<50 vendors, mostly Low/Medium tier** | 0.5 (consolidate with Governance or Risk role) |
| **50-200 vendors, mixed tiers, annual reassessment cycle** | 1.0-2.0 |
| **200-500 vendors, significant Critical-tier population, continuous monitoring** | 2.0-4.0 |
| **500+ vendors, regulatory supply chain requirements (CMMC, CIP-013), dedicated TPRM platform** | 4.0-8.0 |

**Formula:**
```
VRA = ⌈(Critical_Vendors / 30) + (High_Vendors / 60) + (Medium_Vendors / 100) + (Low_Vendors / 200)⌉
```

### 6.5 Detection Engineer

**Primary driver:** Detection surface (log sources and use cases).

| Scope | Staff Required |
|---|---|
| **<10 log sources, SIEM managed by external SOC or MSSP** | 0.5 (consolidate with VM Lead or Threat Intel Analyst) |
| **10-50 log sources, in-house SIEM, basic use case library** | 1.0-2.0 |
| **50-200 log sources, detection-as-code, ATT&CK coverage mapping** | 2.0-5.0 |
| **200+ log sources, multi-SIEM, detection engineering pipeline, 90%+ ATT&CK technique coverage target** | 5.0-10.0 |

### 6.6 OT Risk Analyst and Identity Risk Analyst

These roles are additive to the Risk pillar based on specific organizational scope:

- **OT Risk Analyst:** +1.0 for any organization with an OT environment; +0.5 per additional OT site beyond the first; +1.0 if NERC-CIP regulated
- **Identity Risk Analyst:** +1.0 if the organization operates UEBA or identity threat detection; +0.5 if the organization has a dedicated identity security program; consolidates onto Detection Engineer or Threat Intelligence Analyst if below 1.0

---

## 7. Governance Pillar: Capacity Model

### 7.1 NERC-CIP / CMMC / SOX Compliance Managers

Each major regulatory framework that requires a dedicated compliance program generates its own staffing demand. The base staffing per framework is:

| Framework | Base Staff | Notes |
|---|---|---|
| **NERC-CIP (Medium impact)** | 1.0-1.5 | CIP-002 through CIP-014; annual self-certification; triennial audit |
| **NERC-CIP (High impact)** | 1.5-3.0 | Broader scope; more evidence; more frequent regulatory engagement |
| **CMMC L2 (CUI)** | 1.0-2.0 | SSP and POA&M maintenance; pre-assessment and assessment cycles; supplier flow-down |
| **SOX ITGC** | 0.5-1.5 | Quarterly evidence cycles; external audit coordination; control rationalization |
| **ISO 27001** | 0.5-1.0 | Annual certification cycle; continuous improvement; internal audit program |
| **PCI DSS** | 0.5-1.0 | Annual ROC/SAQ; quarterly ASV scans; evidence maintenance |

Frameworks with overlapping controls reduce the combined staffing need. Use the higher of two overlapping frameworks plus 30% of the lower, not the sum:

```
Combined_Staff = max(Framework_A, Framework_B) + 0.3 × min(Framework_A, Framework_B)
```

### 7.2 Evidence Librarian

**Primary driver:** Evidence volume and refresh frequency.

| Scope | Staff Required |
|---|---|
| **<100 evidence items, annual refresh, single framework** | 0.5 (consolidate onto a compliance manager) |
| **100-500 evidence items, quarterly refresh, 2-3 frameworks** | 1.0 |
| **500-1,500 evidence items, continuous refresh, 3-5 frameworks** | 1.0-2.0 |
| **1,500+ evidence items, continuous refresh, 5+ frameworks, automated evidence collection** | 2.0-3.0 |

### 7.3 Policy & Standards Manager

**Primary driver:** Document count and review cycle complexity.

| Scope | Staff Required |
|---|---|
| **<20 documents, annual review, single author/approver chain** | 0.5 (consolidate onto Governance Pillar Leader) |
| **20-50 documents, semi-annual review, cross-pillar stakeholder coordination** | 1.0 |
| **50-100 documents, continuous review cycle, multi-stakeholder, public-facing documentation** | 1.0-2.0 |
| **100+ documents, multiple frameworks, version-controlled library with rendering/export tooling** | 2.0-3.0 |

### 7.4 Risk Register Owner

**Primary driver:** Risk register size and exception volume.

| Scope | Staff Required |
|---|---|
| **<50 active risks, <5 exceptions, monthly review** | 0.5 (consolidate onto Governance Pillar Leader or compliance manager) |
| **50-200 active risks, monthly review, quarterly exception renewal cycle** | 1.0 |
| **200-500 active risks, continuous review, exception lifecycle management, board reporting** | 1.0-1.5 |
| **500+ active risks, risk committee support, multiple risk registers (IT, OT, vendor, project)** | 1.5-2.0 |

---

## 8. The Scaling Map: From 5 to 60+

### 8.1 Illustrative Staffing at Different Scales

The table below applies the capacity model to four illustrative organization profiles. These are examples, not prescriptions. Every organization's numbers will differ.

| Role | 5-Person CERG (Small Utility) | 15-Person CERG (Mid-Size) | 35-Person CERG (Large Enterprise) | 60-Person CERG (Major Utility) |
|---|---|---|---|---|
| **CISO** | 1 | 1 | 1 | 1 |
| **Engineering Pillar Leader** | 0* | 1 (M4) | 1 (M4) | 1 (M4) |
| Cloud Security Engineer | 0.5* | 1.5 | 3 | 5 |
| Identity Engineer | 0* | 1 | 2 | 3 |
| OT Security Engineer | 1* | 1.5 | 2 | 4 |
| Application Security Engineer | 0* | 0.5 | 1.5 | 3 |
| Endpoint Engineer | 0* | 0.5 | 1 | 2 |
| Cryptography Engineer | 0* | 0 | 1 | 1.5 |
| **Risk Pillar Leader** | 0* | 1 (M4) | 1 (M4) | 1 (M4) |
| Vulnerability Management Lead | 0.5* | 1 | 2 | 3 |
| Adversarial Testing Lead | 0* | 0.5 | 1 | 2 |
| Threat Intelligence Analyst | 0* | 0.5 | 1 | 2 |
| Vendor Risk Analyst | 0* | 0.5 | 1.5 | 3 |
| OT Risk Analyst | 0* | 0.5 | 1 | 2 |
| Identity Risk Analyst | 0* | 0 | 0.5 | 1 |
| Detection Engineer | 0.5* | 1 | 2 | 3 |
| **Governance Pillar Leader** | 0* | 1 (M4) | 1 (M4) | 1 (M4) |
| NERC-CIP Compliance Manager | 0.5* | 1 | 1.5 | 2 |
| CMMC/Federal Compliance Mgr | 0.5* | 0.5 | 1 | 1.5 |
| SOX ITGC Lead | 0* | 0.5 | 1 | 1 |
| Policy & Standards Manager | 0* | 0.5 | 1 | 1.5 |
| Risk Register Owner | 0* | 0.5 | 1 | 1 |
| Evidence Librarian | 0* | 0.5 | 1 | 1.5 |
| **Total (Unconsolidated)** | ~5 | ~15 | ~27 | ~44 |
| **Management Overhead** | 0 | 0.5 | 3 | 5 |
| **Consolidated Total** | **5** | **15** | **30** | **49** |

*In a 5-person organization, these roles are consolidated per the RACI scaling map (RAC-001 §8). The CISO manages all pillars directly. The senior-most practitioner in each pillar operates at S3-S4 level with expanded scope covering adjacent roles.

### 8.2 When to Split a Role

A role that reaches 2.5+ FTE in the model should be evaluated for a split:

| Trigger | Action |
|---|---|
| **2.5 FTE** | Consider whether the role has developed sub-specializations. A Cloud Security Engineer at 2.5 may indicate the need for distinct AWS and Azure engineers, or a Cloud Security Engineer plus a SaaS Security Engineer |
| **3.5 FTE** | Split the role. Create a management layer (Manager or Senior Manager) to lead the sub-team |
| **5.0+ FTE** | The role is a function. It needs a dedicated manager, defined career paths for the sub-specializations, and its own workforce planning cycle |

---

## 9. Validating the Model

### 9.1 The First-Year Reality Check

The capacity model produces a theoretical headcount. The first year of tracking actual time allocation validates or refutes the model's assumptions. Organizations should:

1. **Track time allocation** for at least one quarter. Use broad categories: project work, operational work, unplanned/incident work, administrative overhead. Do not ask for timesheets in 15-minute increments; ask for a weekly estimate by category.
2. **Compare actual to modeled.** If Cloud Security Engineers are spending 50% of their time on unplanned work, the model's project-throughput assumptions are wrong for this organization. Adjust the model or fix the source of unplanned work.
3. **Refine the coefficients.** The throughput numbers in this model are baseline estimates. An organization that discovers its Engineers can handle 10 medium-complexity projects (not the model's 7) should update its formula. The model improves with use.
4. **Recalibrate before each budget cycle.** An organization that is growing, adding platforms, adding regulatory frameworks, or maturing its automation should run the model fresh each year.

### 9.2 Automation Maturity Adjustment

Organizations with mature security automation should apply the Automation Discount (AD) factor from §4.1. Signs of automation maturity include:

| Indicator | Discount Signal |
|---|---|
| Policy-as-code for cloud security (OPA, Terraform Sentinel, AWS SCPs) | Cloud Security Engineer throughput improves 15-25% |
| Detection-as-code pipeline with automated testing and deployment | Detection Engineer throughput improves 20-30% |
| Automated evidence collection from security tools to evidence library | Evidence Librarian throughput improves 30-50% |
| Vulnerability scanner to ticketing system bi-directional integration with auto-triage rules | VM Lead throughput improves 15-25% |
| Automated vendor risk scoring from security rating services | Vendor Risk Analyst throughput improves 20-30% |

### 9.3 The Experience Adjustment

A team of predominantly S3-S4 practitioners handles more throughput per person than a team of S1-S2 practitioners. An organization with a senior-heavy team may increase throughput coefficients by 15-25%. An organization with a junior-heavy team (common during rapid growth) should decrease throughput coefficients by 15-25% and budget for the mentoring overhead that junior practitioners require.

> **The Model Is Honest About Its Limits**
>
> This model will not tell you that you need exactly 2.3 Cloud Security Engineers. It will tell you that based on your project count, complexity mix, and automation maturity, your range is 2-3. The decision between 2 and 3 depends on factors no model captures: your risk appetite, your team's current burnout level, your ability to hire, and whether you have a major platform migration coming in Q3 that is not yet on the project register. The model provides the range and the rationale. The CISO provides the judgment.

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-WFP-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and before each budget cycle |
| **Next Scheduled Review** | 2027-05-27 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.7.1 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-27 | Cyber Governance | Initial release. Defines workload-driver-based staffing methodology for all CERG roles. Provides capacity models for Engineering (6 roles), Risk (6 roles), and Governance (6 roles) pillars with formulas, throughput coefficients, and scope-based staffing ranges. Includes scaling map from 5 to 60+ personnel with role consolidation rules and management overhead factors. Provides model validation guidance and automation maturity adjustments. |

### Review Triggers

- Before each annual budget cycle (re-run the model with current data)
- Material change to organizational scope: new platforms, new regulatory frameworks, major initiative launches
- Material change to automation maturity
- Feedback from time allocation tracking indicating model coefficients need adjustment
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Pillar structure and canonical role roster |
| RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Role consolidation scaling map |
| Job Architecture | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade-level experience adjustments |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Illustrative 60-person staffing model |
| Maturity Assessment | [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | Automation maturity context |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.