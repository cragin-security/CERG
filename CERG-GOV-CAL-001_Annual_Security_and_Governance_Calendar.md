
# SURGE: Cyber Engineering, Risk & Governance

## ANNUAL SECURITY AND GOVERNANCE CALENDAR
### Program Cadence · Control Reviews · Audit Readiness · Exercises · Board Reporting

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CAL-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) · [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) |
| **Review Cycle** | Annual / On major program, regulatory, or reporting cadence change |
| **Frameworks** | NIST CSF 2.0 GOVERN · NIST 800-53r5 PM, CA · ISO/IEC 27001 Clauses 9 and 10 |
| **Regulations** | Cross-cutting; SOX, CMMC, NERC-CIP, privacy, customer assurance where applicable |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Calendar Rules](#2-calendar-rules)
3. [Standing Cadence Summary](#3-standing-cadence-summary)
4. [Annual Calendar by Quarter](#4-annual-calendar-by-quarter)
5. [Monthly Operating Rhythm](#5-monthly-operating-rhythm)
6. [Quarterly Operating Rhythm](#6-quarterly-operating-rhythm)
7. [Annual Operating Rhythm](#7-annual-operating-rhythm)
8. [Event-Driven Triggers](#8-event-driven-triggers)
9. [Calendar Maintenance](#9-calendar-maintenance)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

CERG contains review cycles, reporting cycles, test cadences, evidence refreshes, access reviews, tabletop exercises, audits, board reporting, DR tests, policy reviews, vendor reviews, and maturity assessments across many documents. This calendar consolidates those recurring obligations into one operating instrument.

It applies to all CERG-owned governance, risk, engineering, audit, evidence, and reporting activities. It does not replace the detail in each governing standard or procedure. It gives the CISO, Governance Pillar Leader, Risk Pillar Leader, Engineering Pillar Leader, and Evidence Librarian a single look-ahead view of what must happen, when, and who owns it.

> **A Program That Has No Calendar Has No Operating System**
>
> Policies say what must be true. Procedures say how work happens. The calendar says when the program proves it. Without a calendar, every review becomes a surprise, every audit becomes a scramble, and every control owner becomes a heroic exception handler.

---

## 2. Calendar Rules

1. The calendar is maintained by the Governance Pillar Leader.
2. Each activity has exactly one accountable role, using canonical roles from `CERG-GOV-RAC-001`.
3. The more specific source document controls when a cadence conflict exists.
4. Evidence-producing activities create or refresh evidence under `CERG-PRC-AUD-001`.
5. Missed calendar activities are tracked as program findings or risk-register entries.
6. Activities may be consolidated for small teams, but the role accountability does not disappear.
7. Regulated-scope activities are not moved without approval from the appropriate accountable role.

---

## 3. Standing Cadence Summary

| **Cadence** | **Activity** | **Accountable Role** | **Primary Evidence** | **Source** |
|---|---|---|---|---|
| Daily / Continuous | Critical risk, vulnerability, logging, backup, identity, and monitoring signals reviewed through dashboards and queues. | Risk Pillar Leader | Dashboard snapshots, queue metrics, risk updates | `CERG-GOV-MTR-001`, `CERG-PRC-VM-001`, `CERG-STD-LM-001` |
| Weekly | High-priority risk, exception, vulnerability, vendor, and audit blockers reviewed. | Risk Pillar Leader | Weekly action tracker | `CERG-PRC-RM-001`, `CERG-PRC-AUD-001` |
| Monthly | CERG leadership operating review. | Governance Pillar Leader | Monthly leadership report | `CERG-GOV-MTR-001`, `CERG-TMPL-MTR-001` |
| Monthly | POA&M and remediation status review. | Risk Register Owner | POA&M status report | `CERG-TMPL-CUI-002`, `CERG-PRC-RM-001` |
| Monthly | Asset inventory reconciliation. | Engineering Pillar Leader | Inventory export, reconciliation log | `CERG-STD-AM-001`, `CERG-GOV-CB-001` |
| Monthly | Logging and detection coverage review. | Risk Pillar Leader | SIEM source inventory, coverage gap report | `CERG-STD-LM-001`, `CERG-GOV-CB-001` |
| Quarterly | Access recertification and privileged access review. | Engineering Pillar Leader | Recertification report, PAM review | `CERG-STD-AC-001`, `CERG-GOV-CB-001` |
| Quarterly | Metrics and risk posture brief to oversight forum. | Governance Pillar Leader | CISO / board reporting deck | `CERG-GOV-MTR-001`, `CERG-TMPL-MTR-001` |
| Quarterly | Exception aging and renewal review. | Risk Register Owner | Exception register extract | `CERG-PRC-RM-001`, `CERG-TMPL-RM-002` |
| Quarterly | Evidence quality sample. | Evidence Librarian | Evidence sample worksheet | `CERG-PRC-AUD-001`, `CERG-TMPL-AUD-001` |
| Semiannual | Vendor tier refresh for Critical and High vendors. | Vendor Risk Analyst | TPRM refresh report | `CERG-PRC-TPRM-001`, `CERG-TMPL-TPRM-001` |
| Annual | Policy, standard, procedure, plan, and template reviews. | Governance Pillar Leader | Review record, revision decision | `CERG-GOV-CAT-001` |
| Annual | Maturity self-assessment. | Governance Pillar Leader | Maturity scorecard | `CERG-GOV-MAT-001` |
| Annual | Disaster recovery and cyber recovery exercise. | Engineering Pillar Leader | DR test report, lessons learned | `CERG-PLN-BC-001`, `CERG-STD-RES-001` |
| Annual | Tabletop exercise. | Risk Pillar Leader | Tabletop package and after-action items | `CERG-PRC-IR-002` |
| Annual | Control baseline review. | Governance Pillar Leader | Baseline review record | `CERG-GOV-CB-001` |
| Annual | Penetration test or adversarial validation planning and results review. | Risk Pillar Leader | Test plan, report, remediation tracker | `CERG-PRC-AV-001` |
| Annual | ISO management review and internal audit package where ISO scope applies. | Governance Pillar Leader | Internal audit report, management review record | `CERG-PLN-ISO-001` |

---

## 4. Annual Calendar by Quarter

### Q1: Reset, Baseline, and Plan

| **Month** | **Activity** | **Accountable Role** | **Output** |
|---|---|---|---|
| January | Confirm annual CERG calendar, owners, and regulated-scope milestones. | Governance Pillar Leader | Approved calendar and owner list |
| January | Refresh artifact review schedule from the catalog. | Governance Pillar Leader | Document review tracker |
| January | Review prior-year risks, exceptions, audit findings, POA&M items, and open executive actions. | Risk Pillar Leader | Prior-year closeout summary |
| February | Confirm annual audit and assurance plan. | Evidence Librarian | Evidence request forecast |
| February | Refresh vendor tiers for Critical and High providers. | Vendor Risk Analyst | Vendor tier report |
| March | Prepare Q1 CISO / board posture deck. | Governance Pillar Leader | Q1 reporting deck |

### Q2: Evidence, Testing, and Assurance

| **Month** | **Activity** | **Accountable Role** | **Output** |
|---|---|---|---|
| April | Run quarterly access review and privileged access review. | Engineering Pillar Leader | Access review evidence |
| April | Execute evidence quality sample. | Evidence Librarian | Evidence sample worksheet |
| May | Run tabletop exercise or scenario workshop. | Risk Pillar Leader | Tabletop after-action report |
| May | Review threat modeling and architecture review throughput. | Engineering Pillar Leader | Architecture review metrics |
| June | Prepare Q2 CISO / board posture deck. | Governance Pillar Leader | Q2 reporting deck |

### Q3: Resilience, Maturity, and Regulatory Readiness

| **Month** | **Activity** | **Accountable Role** | **Output** |
|---|---|---|---|
| July | Run DR / cyber recovery exercise planning or execution. | Engineering Pillar Leader | DR exercise package |
| July | Review backup immutability and restore evidence. | Engineering Pillar Leader | Backup assurance record |
| August | Conduct maturity self-assessment. | Governance Pillar Leader | Maturity scorecard |
| August | Refresh control baseline and control-to-procedure traceability. | Governance Pillar Leader | Baseline and traceability update |
| September | Prepare Q3 CISO / board posture deck. | Governance Pillar Leader | Q3 reporting deck |

### Q4: Closeout, Certification, and Next-Year Planning

| **Month** | **Activity** | **Accountable Role** | **Output** |
|---|---|---|---|
| October | Complete annual policy, standard, procedure, plan, and template reviews. | Governance Pillar Leader | Review records and revision backlog |
| October | Review ISO, CMMC, SOX, CIP, privacy, and customer-assurance readiness. | Governance Pillar Leader | Assurance readiness summary |
| November | Approve next-year cyber governance plan, test plan, and budget inputs. | Chief Information Security Officer (CISO) | Next-year plan |
| November | Review exception aging and risk acceptance renewals before year end. | Risk Register Owner | Exception renewal packet |
| December | Prepare Q4 / annual CISO and board posture deck. | Governance Pillar Leader | Annual reporting deck |

---

## 5. Monthly Operating Rhythm

The monthly operating review uses a standard agenda:

1. material risk changes;
2. open Critical and High residual risks;
3. exception aging and upcoming expirations;
4. vulnerability and remediation SLA posture;
5. audit findings and evidence blockers;
6. vendor risk escalations;
7. project intake and threat modeling throughput;
8. metrics outside threshold;
9. decisions needed from the CISO or oversight forum;
10. open actions from the prior meeting.

The output is a monthly action tracker and a metrics snapshot. The action tracker is not optional. If a meeting produces decisions but no action record, the program has no memory.

---

## 6. Quarterly Operating Rhythm

The quarterly rhythm produces CISO or oversight reporting using `CERG-TMPL-MTR-001`. At minimum, the quarterly package includes:

- posture summary and trend;
- material risk changes;
- open High and Critical risks;
- exceptions opened, closed, expired, or renewed;
- control and audit findings;
- program maturity movement;
- vendor and supply-chain risk movement;
- incident and resilience summary;
- decisions required from leadership.

---

## 7. Annual Operating Rhythm

The annual rhythm resets the program. It includes:

- artifact review and catalog reconciliation;
- maturity self-assessment;
- control baseline review;
- annual assurance plan;
- annual tabletop and recovery exercises;
- annual review of regulated-scope requirements;
- budget, staffing, and roadmap input;
- board / executive annual summary.

Annual work should not wait until Q4. Q4 is for closeout and next-year planning, not for discovering that the year's required evidence was never collected.

---

## 8. Event-Driven Triggers

Calendar activities also occur when triggered by events.

| **Trigger** | **Required Calendar Action** | **Accountable Role** |
|---|---|---|
| Major incident | Post-incident review, risk updates, evidence preservation, recovery lessons learned | Risk Pillar Leader |
| Material architecture change | Architecture review, threat modeling, risk treatment update | Engineering Pillar Leader |
| New regulated scope | Catalog, control baseline, evidence, and reporting cadence review | Governance Pillar Leader |
| New Critical or High vendor | TPRM assessment and executive risk decision where required | Vendor Risk Analyst |
| Failed control test | POA&M entry, risk update, retest schedule | Evidence Librarian |
| Missed recovery objective | DR plan update, risk entry, executive escalation | Engineering Pillar Leader |
| New law, framework version, or customer obligation | Applicability assessment and artifact update plan | Governance Pillar Leader |

---

## 9. Calendar Maintenance

The Governance Pillar Leader maintains this calendar. The Evidence Librarian maintains evidence that required activities occurred. The Risk Register Owner tracks missed or materially delayed activities when they create residual risk.

Calendar maintenance includes:

- annual confirmation of all recurring activities;
- monthly review of upcoming activities due in the next 60 days;
- quarterly reconciliation against the document catalog and roadmap;
- update after any new artifact introduces a review cycle or evidence cadence;
- removal of activities that are retired by approved catalog amendment.

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CAL-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on major program, regulatory, or reporting cadence change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST CSF 2.0 GOVERN; NIST 800-53r5 PM, CA; ISO/IEC 27001 Clauses 9 and 10 |
| **Regulations** | Cross-cutting; SOX, CMMC, NERC-CIP, privacy, customer assurance where applicable |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes the annual CERG security and governance operating calendar, including monthly, quarterly, annual, and event-driven activities. |

### Review Triggers

- New artifact introduces a recurring activity
- Existing artifact changes review cycle or evidence cadence
- New regulated scope enters CERG
- CISO changes reporting cadence
- Audit or assessment finding related to program cadence

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative artifact inventory and review trigger source |
| Metrics Dashboard and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Reporting cadence and dashboard source |
| Maturity Self-Assessment and Scorecard | [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | Annual maturity assessment source |
| Consolidated Roles and RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Accountability source for calendar activities |
