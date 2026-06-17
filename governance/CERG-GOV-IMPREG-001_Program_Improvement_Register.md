# SURGE: Cyber Engineering, Risk & Governance

## PROGRAM IMPROVEMENT REGISTER
### Register Schema · Lifecycle · Integration · Reporting · Operating Procedure

---

| | |
|---|---|
| **Document ID** | CERG-GOV-IMPREG-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-PRC-LL-001`](../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) · [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) · [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) |
| **Review Cycle** | Annual / Reviewed at each quarterly CERG leadership review |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.IM, GOVERN) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (PM) · ISO/IEC 27001 A.10 |
| **Regulations** | Cross-cutting : applies to all CERG-supported frameworks |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Why a Separate Improvement Register](#2-why-a-separate-improvement-register)
3. [Register Schema](#3-register-schema)
4. [Improvement Lifecycle](#4-improvement-lifecycle)
5. [Integration with the Risk Register](#5-integration-with-the-risk-register)
6. [Integration with Other CERG Instruments](#6-integration-with-other-cerg-instruments)
7. [Reporting](#7-reporting)
8. [Roles and Responsibilities](#8-roles-and-responsibilities)
9. [Register Maintenance and Hygiene](#9-register-maintenance-and-hygiene)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

The CERG Framework targets NIST CSF Adaptive maturity. A defining characteristic of an Adaptive program is that it does not just respond to findings : it changes itself in response to what it learns. It identifies systemic weaknesses, alters its own controls and procedures, and verifies that the changes worked.

This document defines the Program Improvement Register: the authoritative, durable record of every program-level change CERG makes, why it was made, who was accountable, and whether it produced the intended effect. It is the audit trail that answers the assessor's question: "How has your program evolved, and can you prove that evolution made it better?"

This document applies to every CERG program improvement, regardless of source: lessons learned (PRC-LL-001), intelligence-driven reprioritization, maturity assessment gaps (MAT-001), metric threshold breaches (MTR-001), CISO direction, or external requirement changes.

> **Program Improvement vs. Operational Change**
>
> Patching a server is an operational change. It does not go in the improvement register. Adding a control to CB-001 that requires automated patch verification is a program improvement. It goes in the improvement register.
>
> The test: "Would this change still be relevant to an assessor reviewing our program two years from now?" If yes, it belongs here.

---

## 2. Why a Separate Improvement Register

CERG already has a risk register (PRC-RM-001). Using it for program improvements creates three problems:

1. **Category error.** A risk is a threat-vulnerability-impact-likelihood construct with a treatment plan. A program improvement : "we consolidated two duplicate procedures," "we raised the architecture review SLA from 85% to 95%," "we added a new leading indicator" : is not a risk. Forcing it into a risk register schema distorts both the risk data and the improvement data.

2. **Noise in risk reporting.** The CISO and board review the risk register to understand exposure. Mixing in program improvements : which are positive, forward-looking changes : dilutes the risk signal.

3. **Wrong lifecycle.** Risks have treatment plans, residual scores, and acceptance decisions. Improvements have implementation, verification, and effectiveness outcomes. The lifecycles are different; the register should be different.

> **When to Use Each Register**
>
> | Situation | Correct Register |
> |---|---|
> | A vulnerability is found on a production server | Risk register (PRC-RM-001) |
> | The same vulnerability class appears across four pen tests and an audit; the root cause is a missing standard | Improvement register (this document) |
> | A business unit wants to accept a risk for 6 months | Risk register |
> | The exception process itself needs a revision because it takes too long | Improvement register |
> | An incident occurred; the IR team contained it | Risk register (post-incident risk entry) |
> | The incident revealed that detection rules need updating for an entire attack technique family | Improvement register |

---

## 3. Register Schema

The improvement register is a structured record. Every entry contains the following fields. The register may be maintained in any platform that supports structured data (spreadsheet, database, GRC tool), but the schema is fixed.

| Field | Description | Example |
|---|---|---|
| **Improvement ID** | IMP-YYYY-NNN (year assigned, sequential) | IMP-2026-001 |
| **Title** | Short description of the change | "Add automated firmware-version discovery to asset management" |
| **Source** | What triggered this improvement | Lesson ID LL-2026-Q2-003 / Intelligence review Q2 2026 / MAT-001 domain 14 gap / MTR-001 VM-001 threshold breach / CISO directive / External requirement change |
| **Source Detail** | Specific reference to the triggering event or analysis | "Quarterly Lessons Aggregation Q2 2026 : pattern cluster: firmware versions not tracked in CMDB" |
| **Type** | Improvement action type per PRC-LL-001 Section 6.1 | Control amendment / Standard revision / Procedure update / New capability / Training gap flag / Staffing or budget / Metric or threshold change / Retirement |
| **Current State** | What exists today, including why it is insufficient | "Firmware versions tracked manually in spreadsheets; three of last four critical vulns had un-tracked firmware" |
| **Target State** | What will exist after the change | "Firmware versions auto-discovered by CMDB agent; STD-AM-001 requires firmware version as a tracked attribute; PRC-VM-001 adds firmware-age SLA" |
| **Affected Artifacts** | CERG document IDs that will be modified | STD-AM-001, PRC-VM-001 |
| **Accountable Role** | Single owner per the canonical role roster (OM-001 Section 6.1) | Engineering Pillar Leader |
| **Approved By** | CISO | CISO |
| **Approval Date** | When approved | 2026-04-15 |
| **Target Date** | When this should be operational | 2026-09-30 (Q3) |
| **Status** | Current lifecycle state (see Section 4) | In Progress |
| **Actual Completion Date** | When the change reached Complete status | (blank until status reaches Complete) |
| **Verification Method** | How effectiveness will be proven | "Firmware attribute appears in CMDB for 100% of critical assets; next quarterly VM report shows zero firmware-related vulns past SLA" |
| **Verification Date** | When verification occurred | (blank until verification occurs) |
| **Verification Outcome** | Effective / Partially Effective / Ineffective | (blank until verification occurs) |
| **Re-open Reason** | If Ineffective, what was the gap and what is the revised approach | (blank unless re-opened) |
| **Notes** | Free-text for context, blockers, dependencies | "Dependency: CMDB agent deployment scheduled for Q2; Engineering will coordinate with IT ops" |

> **One Improvement, One Entry**
>
> If an improvement requires changes to three documents and a new tool, it is still one improvement : one root cause analysis, one decision, one accountable owner. The "Affected Artifacts" field captures the scope. Do not create multiple entries for one improvement decision.

---

## 4. Improvement Lifecycle

Every improvement follows a defined lifecycle. Status changes are recorded with a date and the role making the change.

### 4.1 Lifecycle States

```
Proposed → Approved → In Progress → Complete → Verified → Closed
                  ↘                        ↘
              Declined              Ineffective → Re-Opened → In Progress (revised)
```

| State | Meaning | Entry Criteria | Exit Criteria |
|---|---|---|---|
| **Proposed** | Improvement has been identified and documented but not yet approved | Improvement identified per PRC-LL-001 pipeline or equivalent source | Approval decision |
| **Approved** | Improvement has been approved by the appropriate authority | Approver signs off | Work begins |
| **In Progress** | Work is actively underway | Accountable role accepts; resources allocated | All affected artifacts updated, new capabilities deployed, or other Target State achieved |
| **Complete** | Target state achieved; improvement implemented | All "Affected Artifacts" updated; operator confirms change is operational | Verification checkpoint |
| **Verified** | Verification confirms the improvement was effective | Verification method executed; outcome assessed | Closure |
| **Closed** | Improvement is permanently closed | Verified Effective | : |
| **Declined** | Improvement was reviewed and rejected | Approver declines with rationale | : (entry retained for audit trail) |
| **Ineffective** | Verification showed the improvement did not work or partially worked | Verification outcome is Partially Effective or Ineffective | Re-opened with revised approach |
| **Re-Opened** | Previously Complete or Verified improvement is re-activated with a revised approach | Root cause analysis of ineffectiveness complete; revised approach defined | In Progress (with revised Target State) |

> **Complete Is Not Closed**
>
> "Complete" means the change was made : the standard was amended, the tool was deployed, the procedure was updated. "Verified" means the change worked : the amendment actually prevented recurrence, the tool actually caught the thing it was designed to catch, the procedure actually improved the outcome. An improvement that sits at "Complete" without verification is an open item, not a success.

### 4.2 Aging Rules

- An improvement in "Proposed" for more than 30 days without an approval decision is escalated to the CISO.
- An improvement in "In Progress" past its target date is flagged at the next quarterly review.
- An improvement in "Complete" for more than one quarter without verification is escalated : the verification was either not planned or is being avoided.
- An improvement in "Re-Opened" for more than two quarters is escalated to the CISO for a decision: revise the approach, accept the gap, or close with a documented rationale.

---

## 5. Integration with the Risk Register

The risk register (PRC-RM-001) and the improvement register are distinct instruments with a defined interface.

### 5.1 Risk-to-Improvement Linkage

When a risk register entry identifies a systemic weakness that requires a program change (not just a risk treatment), the risk register entry references the improvement ID. Example:

- Risk register entry RM-2026-047: "Critical vulnerability in SCADA firmware : CVSS 9.1 : treatment: patch within 90 days."
- Improvement register entry IMP-2026-001: "Add automated firmware-version discovery to CMDB; amend STD-AM-001 and PRC-VM-001."
- Risk register entry RM-2026-047 is updated with a reference: "Systemic improvement tracked in IMP-2026-001."

The risk itself is still managed in the risk register. The systemic fix is managed in the improvement register. They reference each other; neither subsumes the other.

### 5.2 Improvement-to-Risk Linkage

When an improvement is approved that will reduce a class of risk, the risk register owner is notified. If the improvement changes the residual risk score for any open risk, the risk entry is re-scored at the next monthly risk register review.

### 5.3 What Does NOT Go in the Improvement Register

- Individual risk entries (use PRC-RM-001)
- Exception requests (use PRC-RM-001 exception workflow)
- Vulnerability remediation tracking (use PRC-VM-001)
- Access review findings (use PRC-AC-002)
- Incident response actions (use PRC-IR-002)
- Audit finding remediation (tracked in PRC-AUD-001; systemic improvements from audit patterns go in the improvement register)

---

## 6. Integration with Other CERG Instruments

| Instrument | Integration Point |
|---|---|
| **PRC-LL-001** (Lessons Learned) | Primary intake pipeline. Approved improvements from the quarterly aggregation are created here. |
| **GOV-MTR-001** (Metrics) | Improvement register metrics (Section 7) are reported alongside risk metrics. Open improvements, aging improvements, and recently verified improvements are included in the quarterly CISO brief. |
| **GOV-MAT-001** (Maturity) | When the maturity scorecard identifies a domain gap, the gap may be recorded as an improvement entry rather than a risk register entry if it requires a program change. |
| **GOV-CAL-001** (Calendar) | The improvement register is reviewed at each quarterly CERG leadership review. Annual catalog amendments triggered by improvements are scheduled in the calendar. |
| **GOV-TRC-001** (Traceability) | When an improvement amends a control, the traceability matrix is updated to reflect the new or changed control-to-procedure mapping. |
| **GOV-CAT-001** (Catalog) | When an improvement creates, amends, or retires an artifact, the catalog is amended. |
| **GOV-RAC-001** (RACI) | When an improvement changes ownership or accountability, the RACI instrument is updated. |

---

## 7. Reporting

### 7.1 Quarterly CISO Brief

At each quarterly CISO Risk and Posture Review (per GOV-CAL-001), the Governance Pillar Leader presents:

- **Improvement register summary:** total open, count by status, count by type
- **Aging report:** improvements past target date, improvements in "Complete" without verification
- **Recently verified:** improvements verified in the trailing quarter with outcome
- **Re-opened count:** improvements re-opened in the trailing quarter
- **Pipeline health:** lessons-intake-to-improvement-approval cycle time (median days)

### 7.2 Annual Program Evolution Report

At the annual program review, the improvement register provides the narrative backbone for "how the program evolved this year." The report includes:

- Total improvements proposed, approved, completed, verified, and declined
- Verification pass rate (Effective / total verified)
- Improvements grouped by source (lessons learned, intelligence-driven, maturity gaps, CISO direction)
- Top 5 most impactful improvements (by assessor-visible program change)
- Improvements that changed the control baseline, standards, or metrics

> **The Annual Evolution Narrative**
>
> The improvement register is the raw material for the single most important answer an Adaptive program must give: "How did your program get better this year?" Every improvement that reached "Verified Effective" is a data point in that answer. If the register is empty, the program did not improve : it only operated.

---

## 8. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **Governance Pillar Leader** | Owns this instrument. Maintains the improvement register. Presents improvement metrics at quarterly reviews. Escalates aging improvements. |
| **CISO** | Approval authority for improvements that affect the control baseline, require budget, or change staffing. Reviews the improvement register quarterly. |
| **Risk Pillar Leader** | Proposes improvements from Risk pillar sources (vulnerability, adversarial, intelligence). Accountable for Risk-owned improvement actions. |
| **Engineering Pillar Leader** | Proposes improvements from Engineering pillar sources (architecture, configuration, SDLC). Accountable for Engineering-owned improvement actions. |
| **Risk Register Owner** | Links risk register entries to improvement entries per Section 5.1. Re-scores affected risks when an improvement changes the risk landscape. |
| **Policy & Standards Manager** | Executes catalog amendments triggered by improvements. Updates cross-references when artifacts are modified. |
| **Evidence Librarian** | Archives improvement register snapshots for audit trail. Maintains the verification evidence for completed improvements. |

---

## 9. Register Maintenance and Hygiene

### 9.1 Platform and Access

The improvement register is maintained in a structured platform accessible to all pillar leaders and the CISO. The minimum viable platform is a shared spreadsheet with column-level permissions and an audit log. Larger organizations may use a GRC tool or database.

Regardless of platform, the register must support:

- Filtering by status, type, accountable role, and source
- Date-based aging queries (items past target date, items in Complete without verification)
- Export for quarterly and annual reporting
- Audit trail of status changes (who changed what, when)

### 9.2 Hygiene Rules

- **No orphan entries.** Every entry has an accountable role and a target date. Entries without both are returned to Proposed.
- **No stale entries.** The Governance Pillar Leader reviews the register monthly for entries that have not been updated in 60 days. Stale entries are flagged at the next CERG leadership sync.
- **Declined entries are retained.** A declined improvement is an audit artifact : it shows the improvement was considered and rejected with rationale. It is not deleted.
- **Ineffective entries are re-opened, not deleted.** The failure is itself a data point. The original approach, the verification evidence, and the re-open rationale are preserved.

### 9.3 Archival

The improvement register is archived annually. The archived register becomes an audit artifact. The active register continues with a new year prefix (IMP-YYYY-NNN).

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-IMPREG-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-26 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-05-26 |
| **Frameworks** | NIST CSF 2.0 (ID.IM, GOVERN); NIST 800-53r5 (PM); ISO/IEC 27001 A.10 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-26 | Cyber Governance | Initial draft. Established the Program Improvement Register: schema, lifecycle, risk register integration, reporting, and maintenance procedure. Addresses NIST CSF Adaptive gap: tracking program evolution as a distinct management discipline from risk management. |
