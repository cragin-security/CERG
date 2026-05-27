
# SURGE: Cyber Engineering, Risk & Governance

## ADVERSARIAL VALIDATION PROCEDURE
### Pen Test · Red Team · Purple Team · Cloud Attack Sim · App Test · OT Safety · Finding-to-Closure

---

| | |
|---|---|
| **Document ID** | CERG-PRC-AV-001 |
| **Version** | 1.21 |
| **Status** | Published |
| **Classification** | Public |
| **Owner** | Adversarial Testing Lead |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-LM-001](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [CERG-PLN-IR-001](CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **Review Cycle** | Annual / On material program change |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CA-8) · NIST 800-115 · PTES · MITRE ATT&CK · MITRE D3FEND · OWASP WSTG / MASTG |
| **Regulations** | NERC-CIP CIP-007 (vulnerability assessment) · [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.11.2) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) (indirect via control testing) |
| **Environments** | All - IT · cloud · SaaS · OT (with safety constraints) · application · identity |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Engagement Types](#2-engagement-types)
3. [Annual Cadence and Scoping](#3-annual-cadence-and-scoping)
4. [Rules of Engagement (RoE) Template](#4-rules-of-engagement-roe-template)
5. [Red-Team Engagement Charter](#5-red-team-engagement-charter)
6. [Purple-Team Detection Validation](#6-purple-team-detection-validation)
7. [Cloud Attack Simulation](#7-cloud-attack-simulation)
8. [Application Penetration Test Checklist](#8-application-penetration-test-checklist)
9. [OT Adversarial Assessment, Safety Protocol](#9-ot-adversarial-assessment--safety-protocol)
10. [Finding Rating, Routing, and Retest](#10-finding-rating-routing-and-retest)
11. [Evidence Retention](#11-evidence-retention)
12. [Roles and Responsibilities](#12-roles-and-responsibilities)
13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Scope

The Cybersecurity Policy requires periodic adversarial testing. The vulnerability procedure names the adversarial activities CERG performs. The risk taxonomy distinguishes adversarial testing from vulnerability scanning. Until this procedure, the operating model, scope, rules, safety, finding routing, evidence, for adversarial validation was implicit.

This procedure makes it explicit. It applies to every CERG-led or CERG-overseen adversarial engagement: external pen test, internal pen test, cloud red-team / attack simulation, web/mobile/API pen test, OT adversarial assessment, purple-team detection validation, and social-engineering work conducted with the adjacent Awareness function.

> **Adversarial Validation Is the Antidote to Drift**
>
> A control library that exists on paper but has never been tested is a hope. Adversarial validation tests the assumption that the control library implements actual defense. CERG runs it on a cadence; documents the rules; routes findings into vulnerability management or the risk register; and uses purple-team work to upgrade detection, not just to score the team.

---

## 2. Engagement Types

| **Type** | **Goal** | **Default Frequency** | **Adversary Model** |
|---|---|---|---|
| External Pen Test | Validate the perimeter - internet-facing surface, edge identity, public services. | Annual | Unauthenticated external attacker. |
| Internal Pen Test | Validate post-foothold lateral movement, privilege escalation, segmentation. | Annual | Authenticated low-privilege user / compromised workstation. |
| Cloud Red Team / Attack Sim | Validate cloud control plane, identity, KMS, logging detection. | Annual + on material cloud change | Compromised cloud identity / supply-chain attack on cloud workloads. |
| Application Pen Test | Validate web / mobile / API surface of in-scope applications. | Annual for T1/T2 apps; risk-based for others; pre-launch for new apps. | Authenticated and unauthenticated. |
| OT Adversarial Assessment | Validate OT boundary, ESP/EAP, jump server, OT detection set. | Per CIP-007 cadence (at least every 15 months for BES) | Compromised IT-side identity attempting OT pivot; vendor-channel compromise. |
| Purple-Team Detection Validation | Validate the day-one + tuned detection set fires as designed. | Quarterly | ATT&CK technique emulation. |
| Social Engineering | Validate identity and awareness controls; phishing-resistance. | Per Awareness program | External commodity + targeted scenarios. |
| Tabletop / Crisis Simulation | Validate IR plan + CERG interfaces during a simulated incident. | Annual | Scenario-driven. |

---

## 3. Annual Cadence and Scoping

CERG produces an annual Adversarial Validation Plan that schedules the engagements above against the in-scope environments. The plan is reviewed and approved by the CISO; it is updated quarterly to reflect emerging threats and program priorities.

Scoping inputs:

- Highest-residual-score risks in the register.
- Recently introduced systems and architectures ([`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) Phase 5 records).
- Regulatory cadence requirements (CIP, [CMMC](https://dodcio.defense.gov/CMMC/)).
- ATT&CK coverage gaps identified by detection engineering.
- Threat intelligence pointing at adversary activity relevant to the organization.

---

## 4. Rules of Engagement (RoE) Template

Every engagement has a signed RoE before any activity begins. The template:

```
RULES OF ENGAGEMENT - <Engagement Name>      AV-YYYY-NNNN

1. ENGAGEMENT IDENTITY
   Type                  : (External / Internal / Cloud / App / OT / Purple / SE / TT)
   Sponsor (named role)  :
   Test Lead             :
   Period                :
   Time Windows          :

2. OBJECTIVES
   What we are testing   :
   Success criteria      :
   Risk-register / control gaps this engagement is intended to validate

3. SCOPE - IN
   IPs / URLs / Apps / Cloud accounts / OT segments / Identity tenants explicitly in scope

4. SCOPE - OUT
   Explicit out-of-scope: e.g., production-impacting denial-of-service, mass account lockouts, third-party-hosted out-of-scope assets

5. PROHIBITED ACTIONS
   (Defaults below; engagement may add. None may be removed.)
   - No denial-of-service against production
   - No data destruction or modification
   - No persistence beyond engagement window
   - No exfiltration of regulated data (CUI / BCSI / PHI / PII); proof-of-concept counts; data is staged and discarded
   - No exploitation of safety-impacting OT systems (Section 9)
   - No social engineering of named C-suite without explicit prior approval
   - No physical intrusion outside agreed scope

6. SAFETY AND ABORT
   Stop conditions       : (defined; e.g., OT process alarms, anomalous business impact)
   Abort signal          : (named individual + backup; mechanism - phone / Signal channel)
   Operator on-call (OT) : (if OT)
   Incident handoff path : if findings cross the "test" → "real incident" threshold

7. AUTHORIZATION
   Authorization letter signed by   :
   Distribution                     :
   Authority to act in our environment

8. COMMUNICATIONS
   SOC informed?         : Yes - passive (no detection assistance) / Yes - active (purple)
   Liaison on Tester side:
   Liaison on CERG side  :
   Reporting cadence     : (daily standups / weekly status / final report)

9. EVIDENCE COLLECTION
   What is captured      :
   How it's stored       :
   What is sanitized in final report

10. CONFIDENTIALITY
    Findings classification (default: Restricted)
    Handling : encrypted at rest, named distribution, no email of unredacted

11. SIGNATURES
    Tester Lead          :
    CERG Sponsor         :
    System / Business Owner :
    CISO (red team / OT / cloud red team) :
```

---

## 5. Red-Team Engagement Charter

Red-team engagements are scope-broader, time-longer, goal-driven simulations of a realistic adversary. Each red team has a Charter in addition to its RoE.

```
RED-TEAM CHARTER - <Engagement Name>     AV-YYYY-NNNN

A. ADVERSARY MODEL
   Threat actor profile        :
   Capability                  : (commodity / advanced / nation-state-equivalent)
   Resourcing (time, tools, ops infrastructure)

B. OBJECTIVES - IN PRIORITY ORDER
   Crown Jewel(s) to attempt to reach
   Detection escape required?  :
   Persistence required?       :
   Specific TTPs to emulate    : (ATT&CK technique IDs)

C. ENGAGEMENT WINDOW
   Start / End                 :
   No-Op windows               : (financial close, regulatory exam, major event)

D. PRE-AGREED LIMITS
   Production-impact threshold :
   OT touch                    : (forbidden unless explicit)

E. WHITE-CELL
   Named coordinators on both sides; channels for clarification without breaking the test
```

---

## 6. Purple-Team Detection Validation

Purple work is the collaboration between offensive and detection engineering. It is **not** a graded exam of the SOC; it is a measurement of detection coverage and the basis for upgrading rules and baselines.

### 6.1 Cadence and Coverage

- Quarterly purple-team cycle covering a rotating slice of the ATT&CK matrix in scope.
- Annual full-scope purple-team across the IT spine; semi-annual on cloud sub-matrix; annual on OT sub-matrix.
- Each cycle has 8–20 techniques tested; the cycle's selection is risk-driven (recent threat intel, recent infrastructure changes, prior-cycle failures).

### 6.2 Validation Workflow

1. **Plan**, choose techniques (ATT&CK IDs); map to expected detections in the SIEM; document expected alert.
2. **Execute**, emulate technique in non-production where possible; in production with controlled, documented action where required.
3. **Observe**, did the expected detection fire? With expected priority? In expected time?
4. **Classify**, Pass · Pass-with-Latency · Pass-with-Tuning-Needed · Fail (no detection) · Fail-Suppressed (existed but suppressed).
5. **Action**, Pass: no change. Pass-with-Tuning: tune. Fail / Fail-Suppressed: open detection backlog item + risk register entry until restored.
6. **Reflect**, feed result into detection inventory; update DT-002 metric in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md).

### 6.3 Purple-Team Outcome to Baseline

> **The Purple Cycle Updates Detection, Not Just the Scorecard**
>
> If a technique fires nine times out of ten because logs were missing for one source, the fix is to fix the source, not to re-grade the test. If a technique fires reliably but the alert routes to the wrong queue, the fix is the queue. Purple cycles end with a list of concrete changes to the detection set; if they don't, the cycle is incomplete.

---

## 7. Cloud Attack Simulation

Cloud engagements emulate adversary activity at the cloud control plane and identity layer, historically the most-attacked surface in modern enterprises.

| **Focus** | **Examples** |
|---|---|
| Identity | OAuth consent grant abuse; consent phishing; token theft; federation tampering. |
| Cloud control plane | IAM privilege enumeration and escalation; CloudTrail / Activity Log disable attempts; key policy changes; cross-account assumption. |
| KMS / Secrets | Unauthorized key access; envelope-encryption bypass attempts. |
| Workloads | Container escape; metadata service abuse; misconfigured serverless. |
| Logging / monitoring | Visibility evasion - disable, alter, route around. |

Cloud engagements explicitly include detection validation; CSPM/SSPM signals and cloud-native detection (GuardDuty, Defender for Cloud, Security Command Center) are exercised.

---

## 8. Application Penetration Test Checklist

Application tests use OWASP WSTG (web), MASTG (mobile), and API Security Top 10 as the technical reference. The checklist below is the minimum coverage at scoping; specific apps may need more.

| **Domain** | **Coverage** |
|---|---|
| Authentication | MFA enforcement, credential stuffing resistance, password-reset flow, session handling. |
| Authorization | IDOR, function-level access, multi-tenant isolation, RBAC enforcement. |
| Input handling | Injection (SQL, command, template), deserialization, file upload, SSRF. |
| Output / data exposure | Information disclosure, sensitive data in responses, error verbosity. |
| Configuration | Headers (HSTS, CSP, etc.), TLS conformance to [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md), exposed admin endpoints. |
| Business logic | Workflow bypass, race conditions, abuse of intended functionality. |
| API | OWASP API Top 10: object-level, function-level, mass assignment, rate limiting, etc. |
| Mobile | OWASP MASTG: storage, transport, platform interaction, code quality, resilience. |

---

## 9. OT Adversarial Assessment: Safety Protocol

OT testing is uniquely constrained. Safety overrides any test objective.

### 9.1 Prohibited Without Explicit Approval

The following are prohibited absent a documented exception with engineering and operations sign-off:

- **Active scanning of live SCADA/HMI/RTU/relay surfaces.** Passive monitoring and engineering-supervised authenticated checks only.
- **Exploitation that could affect setpoints, alarms, relays, breakers, or control logic.**
- **Denial-of-service against any OT segment, including saturation testing.**
- **Disabling of OT monitoring or logging.**
- **Persistence on OT systems.**
- **Engagement during operational events**: storms, demand peaks, planned outages, regulatory windows.

### 9.2 Permitted Approaches

- IT-side validation of paths into OT (jump server, vendor remote access, IT/OT crossing).
- Lab / digital-twin replication of OT systems for offensive testing.
- Passive observation and documentation of OT exposure.
- Engineering-supervised authenticated checks in a defined window.
- Tabletop / scenario-based assessment with OT operators.

### 9.3 Authority and Safety Officer

Every OT engagement has a named OT Safety Officer (an operator with substation / process engineering authority) who can stop the test for any reason without justification. The Safety Officer's "stop" is binding.

> **The Cost of Getting OT Testing Wrong**
>
> A pen-test misstep on an enterprise web app produces a ticket. A misstep on a relay setting group can shed load or trip a substation. CERG conducts OT adversarial work with the same care a power engineer applies in the field, and structures the engagement so the engineer's call always wins.

---

## 10. Finding Rating, Routing, and Retest

### 10.1 Rating

Findings are rated using a uniform schema regardless of engagement type, aligning to [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) severity bands so they can co-route into vulnerability management:

| **Severity** | **Definition** |
|---|---|
| Critical | Direct path to Crown Jewel, regulated data, safety impact, or persistent foothold. |
| High | Significant escalation or material exposure of sensitive data; widespread bypass of a control. |
| Medium | Notable control gap with limited exploitability or limited scope. |
| Low | Hygiene or hardening recommendation. |
| Informational | Observations and recommended improvements not tied to a control gap. |

### 10.2 Routing

| **Source of Finding** | **Routes To** |
|---|---|
| Specific software / asset vulnerability | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) finding + risk register entry per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) if Critical/High |
| Control / design weakness | Risk register entry directly per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| Detection gap | Detection backlog + risk register if material |
| Process / runbook weakness | Owning procedure (AR / IR / TPRM) + risk register if material |
| Vendor / supply chain weakness | TPRM record per [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| OT-specific weakness | OT VM procedure within [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) + risk register |

### 10.3 Retest and Closure

- Critical findings retested within 30 days of remediation claim.
- High findings retested within 60 days.
- Medium/Low retested at next routine engagement or by sampled VM scan.
- A finding moves to Closed only after retest demonstrates remediation; a finding that cannot be remediated moves through the risk register acceptance path with explicit Approver.
- Closed findings inform the threat model for the affected system at next architecture review.

---

## 11. Evidence Retention

| **Artifact** | **Retention** | **Access** |
|---|---|---|
| Signed RoE | Engagement + 7 years | Sponsor, CISO, Audit |
| Signed Charter (red team) | Engagement + 7 years | Sponsor, CISO, Audit |
| Engagement plan / scope | Engagement + 5 years | Sponsor, Test Lead, CISO |
| Tester daily logs / standup notes | Engagement + 2 years | Test Lead, CERG sponsor |
| Final report (sanitized) | Engagement + 7 years | Distribution per RoE |
| Final report (full / unsanitized) | Engagement + 5 years | Named distribution only |
| Detection validation results (purple) | Engagement + 3 years | Detection eng + audit |
| Finding records | Per VM tool retention; closed findings retained per audit retention | - |
| Retest evidence | Per finding record retention | - |

Final reports are distributed under the confidentiality terms in the RoE. Full reports are not emailed; access is via a controlled location with audit logging.

> **Findings Carry Sensitive Information About How to Compromise Us**
>
> An unsanitized pen-test report is a road map for attackers and should be treated as Restricted. Distribution is named, encrypted, and audited; "wider sharing" requests are reviewed by the Engagement Sponsor.

---

## 12. Roles and Responsibilities

| **Role** | **Responsibility** |
|---|---|
| Risk - Offensive Security | Owns this procedure. Maintains the annual Adversarial Validation Plan. Conducts or oversees engagements. Authors RoEs and Charters. |
| Detection Engineer | Partners on purple-team cycles; turns findings into detection upgrades. |
| Engineering - Platforms | Remediates identified misconfigurations and control gaps. |
| Engineering - Identity | Remediates identity-related findings; tunes identity detections. |
| Governance - Compliance | Tracks regulator-required cadence (CIP, [CMMC](https://dodcio.defense.gov/CMMC/)); audit interface. |
| CISO | Approves Red-Team Charters and high-impact / cloud / OT engagements.