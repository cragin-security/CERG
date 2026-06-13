# SURGE: Cyber Engineering, Risk & Governance

## STAKEHOLDER PERCEPTION SURVEY
### Survey Instrument · Administration Cadence · Analysis · Program Integration

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-GOV-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-PRC-LL-001`](../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) · [`CERG-GOV-IMPREG-001`](../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) |
| **Review Cycle** | Annual / After administration cycle |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN: Organizational Context) |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Why Measure Perception](#2-why-measure-perception)
3. [Survey Instrument](#3-survey-instrument)
4. [Administration](#4-administration)
5. [Analysis and Reporting](#5-analysis-and-reporting)
6. [Program Integration](#6-program-integration)
7. [Document Control](#7-document-control)

---

## 1. Purpose and Scope

The CERG Framework (FRM-001 Section 6.1) states that at Adaptive maturity, "The business views security as a value driver, not a cost center." Section 6.2 lists "Cybersecurity is viewed as a value driver" as an Adaptive criterion, backed by "Engineering's consulting model and yes-and Governance orientation."

This is a cultural claim that requires evidence. An assessor cannot verify stakeholder perception without a measurement instrument. This survey template provides the instrument, the administration cadence, and the analysis framework.

This survey is administered to business stakeholders who interact with CERG: project managers, business unit leaders, IT and OT operations managers, procurement leads, and any role that has been through a CERG engagement in the assessment period.

> **The Value-Driver Test**
>
> An assessor asks a business unit leader: "Does security help you move faster or slower?" If the answer is "slower," the program has an Adaptive gap regardless of its control maturity. An Adaptive program proves it is a value driver by measuring whether the business agrees.

---

## 2. Why Measure Perception

A program that does not measure stakeholder perception is guessing about its most important relationship. Five reasons this survey matters:

1. **Governance mandate.** The Framework claims Adaptive organizations view security as a value driver. Without measurement, the claim is untestable.
2. **Engagement model feedback.** Engineering's consulting model and Governance's yes-and orientation are operational choices. The survey measures whether they are working.
3. **Early warning.** Declining perception scores precede declining engagement, which precedes shadow IT, workarounds, and missed security reviews.
4. **Assessor evidence.** "The business views security as a value driver" requires evidence. A declining or neutral survey trend is evidence of the opposite.
5. **Improvement driver.** Open-ended feedback reveals what the program should start, stop, or continue doing, in the stakeholder's own words.

---

## 3. Survey Instrument

### 3.1 Target Respondents

The survey is administered to business stakeholders who have interacted with CERG in the assessment period (trailing 12 months for annual survey; trailing project period for post-project survey). Minimum respondent set:

- Project managers for projects that went through architecture review
- Business unit leaders or product owners whose teams were engaged by Engineering
- IT and OT operations managers who interact with Risk (VM, adversarial, TPRM)
- Procurement or vendor-management leads who worked with TPRM
- Any role that submitted an exception request or risk acceptance

### 3.2 Survey Questions

Each question uses a 5-point Likert scale: Strongly Agree (5), Agree (4), Neutral (3), Disagree (2), Strongly Disagree (1).

| # | Question | What It Measures |
|---|---|---|
| 1 | Security engaged early enough to influence the project outcome. | Engineering intake timeliness |
| 2 | The security review added value beyond checking a compliance box. | Perceived value of engagement |
| 3 | Security requirements were clear and actionable : I knew what to do. | Quality of guidance |
| 4 | The yes-and approach was evident : we got to yes with guardrails rather than a flat no. | Governance orientation |
| 5 | I would proactively engage security on my next project. | Willingness to re-engage (the ultimate value test) |
| 6 | Security understood our business constraints and worked within them. | Business empathy and pragmatism |
| 7 | The security engagement did not meaningfully delay our timeline. | Operational efficiency |

### 3.3 Open-Ended Questions

| # | Question | What It Measures |
|---|---|---|
| 8 | What should security START doing that it does not do today? | Unmet needs |
| 9 | What should security STOP doing that creates friction or adds no value? | Friction and waste |

> The friction signal from this annual survey is paired with the continuous CERG service-responsiveness metrics (SR-001 through SR-005) defined in [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) and the published commitments in [`CERG-GOV-SLC-001`](../governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md), so friction is caught monthly (quantitative), not only once a year (qualitative).
| 10 | What should security CONTINUE doing that works well? | Strengths to preserve |
| 11 | Any other feedback you want the CISO to hear. | Unprompted signal |

### 3.4 Administration Options

The survey may be administered in any format that preserves anonymity (respondents must feel safe giving honest feedback):

- Survey platform (preferred): online form, anonymous by default
- Paper form: for OT or field environments where online access is limited
- Structured interview: Governance Pillar Leader or a neutral third party conducts the interview; responses are recorded without attribution

The minimum viable instrument is a shared anonymous form. The template above is the content; the platform is the adopter's choice.

---

## 4. Administration

### 4.1 Cadence

| Trigger | Respondents | Purpose |
|---|---|---|
| **Annual** | All stakeholders who interacted with CERG in the trailing 12 months | Trend measurement; program-health indicator |
| **Post-major-project** | Project team for projects exceeding a defined threshold (budget, risk, or regulatory scope) | Engagement-quality feedback while the experience is fresh |

The annual survey is administered in Q4 so results are available for the annual program review and the next year's planning cycle.

### 4.2 Administration Rules

1. **Anonymity is mandatory.** Responses must not be attributable to individuals. If the organization is too small for anonymity (fewer than 10 respondents), use a neutral third party to administer.
2. **The CISO is copied on results, not raw responses.** The Governance Pillar Leader administers, analyzes, and reports. Individual responses are not shared, even with the CISO.
3. **Minimum response threshold.** If fewer than 10 responses are received for the annual survey, the results are reported as directional only and the low response rate is itself a finding (why are stakeholders not engaging?).
4. **Do not survey during an active incident or audit.** Survey fatigue and contextual noise distort results.

---

## 5. Analysis and Reporting

### 5.1 Scoring

- Each Likert question is scored 1-5. The overall perception score is the mean across all Likert questions.
- Scores are trended year-over-year. A single-year score is nearly useless; the trend tells the story.
- Any question with a mean score below 3.0 (Neutral) triggers a program review.

### 5.2 Open-Ended Analysis

Open-ended responses are analyzed for themes. The Governance Pillar Leader groups responses into themes and counts them. A theme that appears in three or more responses is flagged for program review. A theme that appears across both "START doing" and "STOP doing" suggests a known pain point.

### 5.3 Reporting

The annual survey produces a Stakeholder Perception Report, included in the CISO's annual program review package. It contains:

- Overall perception score (mean), with year-over-year trend
- Question-level scores with trend
- Any question scoring below 3.0 with recommended action
- Top 3 "START," "STOP," and "CONTINUE" themes from open-ended responses
- Response rate and respondent demographics (role categories, not individuals)
- Comparison to the CISO dashboard: does the perception trend align with or contradict the metric trends?

---

## 6. Program Integration

### 6.1 Metrics Dashboard

The overall perception score is reported as a program-health indicator alongside the risk and compliance metrics in MTR-001:

| ID | Name | Formula | Source | Refresh | G / A / R | Reported In |
|---|---|---|---|---|---|---|
| PH-001 | Stakeholder Perception Score | Mean of Q1-Q7 Likert scores | Annual survey | Annual | >= 4.0 / 3.0-4.0 / < 3.0 | CISO Dashboard (annual report) |
| PH-002 | Re-Engagement Willingness | Mean of Q5 ("I would proactively engage security") | Annual survey | Annual | >= 4.0 / 3.0-4.0 / < 3.0 | CISO Dashboard |

### 6.2 Lessons Learned

Open-ended feedback themes are an intake source for the Lessons Learned procedure (PRC-LL-001). A recurring theme of "security takes too long" or "requirements were unclear" is a lesson that must be addressed through the program improvement pipeline.

### 6.3 Improvement Register

When a perception score decline or an open-ended theme triggers a program change, the change is recorded in the improvement register (IMPREG-001) with the source "Stakeholder Perception Survey YYYY."

---

## 7. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-GOV-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-26 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / After each survey administration cycle |
| **Next Scheduled Review** | 2027-05-26 |
| **Frameworks** | NIST CSF 2.0 (GOVERN: Organizational Context) |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-26 | Cyber Governance | Initial draft. Established the stakeholder perception survey instrument: 7 Likert-scale questions, 4 open-ended questions, annual and post-project administration cadence, analysis and reporting framework, and integration with MTR-001 metrics, lessons learned, and the improvement register. Addresses NIST CSF Adaptive gap: measuring whether the business views security as a value driver. |