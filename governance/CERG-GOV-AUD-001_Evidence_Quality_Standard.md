| | |
|---|---|
| **Document ID** | CERG-GOV-AUD-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed evidence |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Evidence Quality Rules](#2-evidence-quality-rules)
3. [Bad Evidence — What Not to Accept](#3-bad-evidence--what-not-to-accept)
4. [Design vs. Operating Effectiveness](#4-design-vs-operating-effectiveness)
5. [Sampling Methodology](#5-sampling-methodology)
6. [Evidence Freshness Rules](#6-evidence-freshness-rules)
7. [Business-Owner Accountability](#7-business-owner-accountability)
8. [Evidence by Control Type](#8-evidence-by-control-type)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

This document defines what qualifies as acceptable evidence in the CERG operating model. It extends the evidence quality tiers (E1/E2/E3) defined in [FLOW-001 §16](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) with specific quality rules, sampling methodology, and freshness requirements.

This standard applies to every CERG artifact that produces or references evidence: the Unified Control Baseline (CB-001), the Audit and Evidence Management Procedure (PRC-AUD-001), the Risk Register and Exception Process (PRC-RM-001), and all standards and procedures that define evidence requirements.

`CERG-GOV-AUD-001` is authoritative for evidence quality, freshness, and sampling expectations. `CERG-PRC-AUD-001` governs how evidence is collected, stored, tested, and produced during audit response. Where the procedure needs to determine whether evidence is acceptable, this standard governs.

> **Evidence proves the control works.** A document that says a control exists is not evidence that it operates. An email that says "done" is not evidence. A screenshot with no date is not evidence. This standard defines what is.

---

## 2. Evidence Quality Rules

Every piece of evidence accepted into the CERG evidence library must answer these questions. If the answer to any required question is "no" or "unknown," the evidence is insufficient for its claimed tier.

### Required for All Evidence (E1 minimum)

| Question | Required | Meaning |
|----------|----------|---------|
| **Who produced it?** | Yes | A named person, system, or automated process. "The security team" is insufficient. |
| **When was it produced?** | Yes | A specific date or timestamp. "Last quarter" is insufficient. |
| **What system/control does it apply to?** | Yes | A specific control ID (from CB-001), asset, or requirement. "Access management" is insufficient. |
| **What period does it cover?** | Yes | A specific time window. "Current" is insufficient — current as of when? |
| **Where is it stored?** | Yes | A file path, URL, or repository location. Must be retrievable by someone other than the person who produced it. |

### Required for E2 (Control Operates)

| Question | Required | Meaning |
|----------|----------|---------|
| **Is it complete?** | Yes | The evidence covers the full scope claimed. A sample must be identifiable as a sample — see §5. |
| **Is it tamper-resistant?** | Preferred | Can the evidence be altered after collection? If yes, compensating controls (hash, read-only storage, audit log) must be documented. |
| **Does it show a sample or full population?** | Yes | Must be explicit. "We reviewed all 250 accounts" or "We sampled 25 of 250 accounts (see sampling methodology §5)." |

### Required for E3 (Control Is Effective)

| Question | Required | Meaning |
|----------|----------|---------|
| **Is it repeatable?** | Yes | Could someone else produce equivalent evidence using the same method? If the method is "I looked at it," the evidence is not repeatable. |
| **Does it prove design, operation, or both?** | Yes | Must be explicit. A configuration export proves design. A test result proves operation. Both may be needed. |
| **Is the evidence independent of the person asserting the control?** | Required for E3 | The person producing the evidence should not be the person whose work is being evidenced. Self-attestation is E2 at best. Independence means: a different person, an automated system, or an external assessor. |
| **Does it include failure conditions?** | Yes | What would the evidence look like if the control had failed? A test that always passes is not a test. |

### Evidence Tier Decision Table

| If... | Then the evidence is at most... |
|-------|-------------------------------|
| Produced by the same person who operates the control | E2 |
| No timestamp or date | E1 — insufficient for E2+ |
| Cannot be retrieved independently | E1 — insufficient for E2+ |
| Scope is undefined ("some accounts were reviewed") | E1 — insufficient for E2+ |
| Method is not documented ("I checked it") | E2 — insufficient for E3 |
| No failure condition defined | E2 — insufficient for E3 |
| Automated, timestamped, independently retrievable, scope-defined, with failure conditions | E3 |

---

## 3. Bad Evidence — What Not to Accept

The following are common evidence submissions that should be rejected. Each represents a pattern, not an exhaustive list.

### Screenshot with No Date

**What it looks like:** A screenshot of a configuration page. No visible timestamp. No URL. No indication of when it was captured or by whom.

**Why it fails:** Screenshots are tamperable, non-repeatable, and usually undated. A screenshot proves someone looked at a screen at some point. It does not prove the configuration was in that state during the audit period.

**What to request instead:** A configuration export with timestamp and origin metadata. A scripted configuration audit with output. An automated CSPM/CNAPP posture report.

### Email Saying "Done"

**What it looks like:** An email thread where someone asks "is the access review done?" and someone replies "yes, done."

**Why it fails:** An email is an assertion, not evidence. It does not show what was reviewed, what was found, what was remediated, or who performed the work. It does not prove the control operated — it proves someone sent an email.

**What to request instead:** The access review output: population list, sample methodology (if sampled), findings, remediations, reviewer sign-off with date.

### Vendor Says Yes

**What it looks like:** A vendor responds to a security questionnaire with "yes" to every question. No supporting evidence.

**Why it fails:** Self-attestation without evidence is not evidence. A vendor that checks "MFA enforced" without providing the IdP policy configuration has not evidenced the control.

**What to request instead:** Vendor-provided evidence: SOC 2 report, ISO 27001 certificate, penetration test summary, configuration exports, or architecture documentation. If the vendor cannot provide evidence, the control status is "Inherited — Unverified" with documented residual risk.

### Meeting Notes with No Action Owner

**What it looks like:** Meeting minutes stating "the team discussed the risk and agreed to monitor it."

**Why it fails:** Discussion is not treatment. "Monitor" without a method, frequency, owner, and trigger is not a treatment strategy. Meeting notes do not create accountability.

**What to request instead:** A risk register entry with named owner, treatment strategy, due date, and next review date. The decision log entry documenting what was decided and by whom.

### Policy Text with No Proof of Operation

**What it looks like:** A policy document excerpt that says "access reviews shall be performed quarterly." No evidence that one was performed.

**Why it fails:** A policy describes intent. Evidence proves execution. The gap between "we have a policy that says we do this" and "we did this" is where controls fail.

**What to request instead:** The output of the access review. Evidence that it was performed, not evidence that it was required.

### Tool Export with No Scope Definition

**What it looks like:** A vulnerability scan report with 10,000 findings. No indication of which assets were scanned, which were excluded, or why.

**Why it fails:** Without scope definition, you cannot determine whether the scan covered the assets it needed to cover. A scan of 80% of assets with 10,000 findings may be worse than a scan of 100% of assets with 12,000 findings — but you cannot tell from the report alone.

**What to request instead:** Scan configuration showing target scope, exclusions with rationale, and scan date. The report should include "X of Y assets scanned; Z excluded with documented rationale."

### Sample with No Population

**What it looks like:** "We reviewed 25 accounts. They were all correct."

**Why it fails:** Without knowing the population size (25 out of how many?) and the sampling method (random? judgmental? convenience?), you cannot assess whether the sample is representative. 25 out of 25 is complete. 25 out of 2,500 with no methodology is not auditable.

**What to request instead:** Population definition (total accounts), sample size, sampling method, and rationale. See §5 Sampling Methodology.

---

## 4. Design vs. Operating Effectiveness

Every control has two dimensions. Evidence must address the right one.

### Design Effectiveness

**Question:** If the control were performed as designed, would it achieve its objective?

**Evidence needed:**
- Control description (what is supposed to happen)
- Configuration or design documentation (how it is implemented)
- Comparison to the control objective (does the design match the intent?)

**Example:** An access review control requires quarterly review of all privileged accounts. The design evidence is the access review procedure document and the IdP configuration showing privileged role definitions. This proves the control is *designed* to identify and review privileged access.

**Design is NOT sufficient to prove the control operates.**

### Operating Effectiveness

**Question:** Was the control actually performed consistently during the period under review?

**Evidence needed:**
- Output of the control's operation (the actual review results)
- Evidence of cadence (was it done when it was supposed to be done?)
- Evidence of completeness (was the full scope covered?)
- Evidence of follow-through (were findings remediated?)

**Example:** The quarterly access review output: population list of 47 privileged accounts, sample of 15 reviewed, 2 accounts flagged for excessive access, both remediated and re-validated. Review performed 2026-06-15, next review due 2026-09-15. This proves the control *operated*.

### Testing Both

For Tier 1 controls (Critical systems, regulated environments), test both:

1. **Design test:** Review the control documentation. Walk through the control with the control owner. Confirm the design addresses the control objective.
2. **Operating test:** Select a sample from the audit period. Examine evidence for each item in the sample. Confirm the control was performed as designed, at the required cadence, with appropriate follow-through.

### Status Implications

| Design | Operating | Control Status |
|--------|-----------|----------------|
| Designed | Operating with evidence | **Implemented** |
| Designed | Operating, evidence incomplete | **Partially Implemented** — evidence gap documented |
| Designed | Not operating consistently | **Partially Implemented** — operating gap documented |
| Designed | Not yet operating | **Planned** — implementation in progress |
| Not designed | N/A | **Planned** or **Not Implemented** |

---

## 5. Sampling Methodology

This section is the canonical CERG sampling standard for evidence review and control testing. When testing a control across a population, sampling is acceptable if the methodology is documented and defensible. Regulatory, assessor, or auditor-specific sampling requirements override these CERG defaults for that engagement and must be documented in the test plan.

### When Sampling Is Acceptable

- The population is large enough that full-population testing is impractical
- The control produces consistent results (not highly variable)
- The sampling method is documented before testing begins
- The sample is representative of the population

### When Full-Population Testing Is Required

- The population is small (<30 items) — test all of them
- The control is Tier 0/Tier 1 (Crown Jewel / Critical systems)
- The control has previously failed
- A regulatory requirement mandates full-population testing
- The evidence is for an E3 claim and the control is high-variability

### Sample Size Guidelines

| Population Size | CERG Baseline Minimum Sample | For High-Risk Controls |
|----------------|------------------------------|----------------------|
| <30 | Full population | Full population |
| 30-100 | 25 | 30 |
| 101-500 | 50 | 80 |
| 501-1,000 | 80 | 120 |
| 1,001-5,000 | 100 | 200 |
| >5,000 | 150 | 300 |

These are baseline defaults, not statistical guarantees. Adjust based on control risk, prior test results, regulatory requirements, assessor direction, and whether the evidence supports an E2 or E3 claim. Document the rationale for any deviation.

### Sampling Method

| Method | When to Use | Documentation Required |
|--------|------------|----------------------|
| **Random** | Preferred. Every item has equal selection probability. | Random seed or selection method. List of selected items. |
| **Judgmental** | When specific high-risk items must be included. Supplement with random sampling of remaining population. | Rationale for judgmental selection. List of items and why each was selected. |
| **Stratified** | When the population has distinct subgroups with different risk profiles. | Stratification criteria. Sample size per stratum. |
| **Convenience** | Not acceptable for audit evidence. | Not applicable; convenience sampling is prohibited. |

### Documentation Required for Every Sample

1. Population definition (what is the full set of items?)
2. Population size (how many items total?)
3. Sampling method (random, judgmental, stratified)
4. Sample size (how many were tested?)
5. Selection rationale (why this method and size?)
6. List of selected items
7. Test results per item
8. Exception handling (what if a selected item cannot be tested?)
9. Extrapolation (do sample results apply to the full population?)
10. Tester name and date

---

## 6. Evidence Freshness Rules

Evidence ages. An access review from 2024 does not prove the control operated in 2026. Every piece of evidence has a shelf life.

### Freshness by Evidence Type

| Evidence Type | Freshness Window | Refresh Trigger | Stale After |
|--------------|-----------------|-----------------|-------------|
| Access review output | Current review cycle + 30 days | Next scheduled review | Review date + 90 days |
| Joiners/movers/leavers (JML) log | Current month | Monthly | 60 days |
| Exposure scan report | Current scan cycle | Next scheduled scan | Scan date + 30 days (IT) / 90 days (OT with approval) |
| MFA/enforcement configuration | Current quarter | Configuration change | 90 days or on change |
| Firewall rule review | Current quarter | Next scheduled review | 120 days |
| Backup restore test | Current test cycle | Next scheduled test | Test date + 180 days |
| Vendor SOC 2 report | Report period + 90 days | New report issued | Report expiration |
| Vendor ISO 27001 certificate | Certificate validity period | Renewal | Certificate expiration |
| Penetration test report | Current test cycle | Next scheduled test | Test date + 365 days |
| Policy/procedure approval | Current approved version | Document change | Version superseded |
| Incident lessons learned | Incident closure + 30 days | Corrective action completion | Action due date + 90 days |
| Risk acceptance | Acceptance date to expiration | Expiration or review date | Expiration date |
| Exception approval | Approval date to expiration | Expiration or review date | Expiration date |
| Training completion record | Current training cycle | Next training cycle | Training date + 365 days |

### Stale Evidence

Evidence that exceeds its freshness window is **stale**. Stale evidence:
- Cannot be used to support E3 claims
- Can be used for E2 claims only if a documented rationale explains why the evidence is still representative
- Creates a Finding Record if the control relies on it and no fresh evidence is available
- Must be flagged in the evidence index with "Stale" quality status

### Freshness Monitoring

The Evidence Librarian checks evidence freshness at the monthly review. The evidence index spreadsheet (§7 of the Small Team Adoption Path) or the GRC platform tracks freshness dates. Stale evidence is flagged in the monthly metrics report.

---

## 7. Business-Owner Accountability

Evidence proves a control operated. The business owner proves the risk is owned. These are different things and both must be present for risk acceptance.

### Every Risk Acceptance Must Include

| Field | Required | Meaning |
|-------|----------|---------|
| **Business Owner Name** | Yes | A specific person outside the security team. Not a role. Not a department. A named individual. |
| **Business Owner Acknowledgement** | Yes | Evidence that the business owner understands and accepts the risk. An email is acceptable. An unsigned form is not. |
| **Business Impact Statement** | Yes | What happens to the business if the risk materializes? Revenue impact, operational impact, customer impact, regulatory impact. Written by the business owner, not by security. |
| **Risk Scenario in Business Terms** | Yes | The risk statement translated from security terminology into business terminology. "Unpatched systems" → "Potential for service outage affecting customer ordering for up to 48 hours." |
| **Acceptance Rationale** | Yes | Why is accepting this risk better than treating it? Cost, operational impact, timing, vendor limitation? Must be specific. |
| **Review Commitment** | Yes | The business owner commits to reviewing this risk on the specified cadence. |

### Red Flags — Return the Acceptance

Reject a risk acceptance if:
- The business owner field says "Security," "CISO," or is blank
- The business impact statement was written by the security team
- The acceptance rationale is "we have always done it this way"
- The review commitment is missing or vague ("we'll review it sometime")
- The business owner cannot be reached to confirm their acknowledgement

### Template Enforcement

Every risk acceptance template, exception request form, and risk register entry must include business-owner fields that cannot be bypassed. The Risk Register Owner is responsible for rejecting incomplete submissions.

---

## 8. Evidence by Control Type

Different controls produce different evidence. This section maps control types to their expected evidence forms.

| Control Type | Expected Evidence (E2 minimum) | E3 Evidence |
|-------------|-------------------------------|-------------|
| **Access Review** | Review output showing population, sample/full scope, findings, remediations, reviewer, date | Independent re-performance of a sample by a different reviewer |
| **JML (Joiners/Movers/Leavers)** | JML log export from HRIS/IdP showing all changes in period | Sample validation: verify 5 leavers' accounts were actually disabled |
| **MFA Enforcement** | IdP policy export showing MFA requirement, exclusions list, date | Authenticated login attempt without MFA — must be rejected |
| **Vulnerability Scanning** | Scan report with scope, exclusions, findings, date | Authenticated re-scan confirming critical/high findings resolved |
| **Patch Management** | Patch compliance report, deployment records | Verify a sample of critical patches were applied within SLA |
| **Firewall Rule Review** | Rule set export, review date, reviewer, findings | Automated rule analysis comparing current rules to approved baseline |
| **Backup Restore Test** | Test plan, test results, RTO/RPO achieved, system owner sign-off, date | Independent observation of a restore test |
| **Change Management** | Change record, security impact analysis, approval, implementation evidence, post-change validation | Verify a sample of changes: did control continuity check pass? |
| **Vendor Risk Assessment** | Completed assessment questionnaire, evidence reviewed, risk rating, review date | Independent review of a sample of vendor-provided evidence |
| **Incident Response** | Incident record, timeline, containment actions, lessons learned, corrective actions | Post-incident tabletop or simulation validating corrective actions |
| **Security Awareness Training** | Training completion report, population coverage, date | Phishing simulation results showing behavior change |
| **Logging/Monitoring** | Log source inventory, coverage report, detection rule inventory | Simulated attack: did the detection rule fire? |

---

## 9. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-AUD-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed evidence |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Evidence quality rules, bad evidence examples, design vs. operating effectiveness, sampling methodology, freshness rules, business-owner accountability, and evidence-by-control-type mapping. |

### Review Triggers

- Change to evidence requirements in CB-001
- Feedback from audit or assessment findings
- Change to regulatory evidence retention requirements
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Cross-Pillar Operational Flows | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) | Evidence quality tiers (E1/E2/E3) |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control definitions and evidence requirements |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Operational evidence collection and audit response |
| Control Effectiveness Framework | [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) | Control testing methodology |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk acceptance evidence requirements |
