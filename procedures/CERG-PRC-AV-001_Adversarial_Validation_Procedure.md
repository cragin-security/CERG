# SURGE: Cyber Engineering, Risk & Governance

## ADVERSARIAL VALIDATION PROCEDURE
### Pen Test · Red Team · Purple Team · Cloud Attack Sim · App Test · OT Safety · Finding-to-Closure

---

| | |
|---|---|
| **Document ID** | CERG-PRC-AV-001 |
| **Version** | 1.2 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Adversarial Testing Lead |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-PRC-VM-001](CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) · [CERG-GOV-CEF-001](../governance/CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) · [CERG-GOV-IMPREG-001](../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) · [CERG-PRC-LL-001](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) |
| **Review Cycle** | Annual / On material program change |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CA-8) · NIST 800-115 · PTES · MITRE ATT&CK · MITRE D3FEND · OWASP WSTG / MASTG |
| **Regulations** | NERC-CIP CIP-007 (vulnerability assessment) · [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.11.2) · SOX (indirect via control testing) |
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
11. [Systemic Analysis and Program Feedback Loop](#11-systemic-analysis-and-program-feedback-loop)
12. [Roles and Responsibilities](#12-roles-and-responsibilities)
13. [Evidence Retention](#13-evidence-retention)
14. [Regulatory and Framework Alignment Summary](#14-regulatory-and-framework-alignment-summary)
15. [Document Control](#15-document-control)

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

### 2.1 External Tester Management

When adversarial validation is conducted by an external firm rather than internal staff, the following requirements apply.

#### Minimum Tester Qualifications

| **Engagement Type** | **Minimum Qualification** |
|---|---|
| Network / infrastructure penetration test | OSCP, GPEN, or equivalent; 2+ years of hands-on testing experience |
| Web application penetration test | OSWE, GWAPT, or equivalent; demonstrated web app testing portfolio |
| Red team engagement | GXPN, OSEP, or equivalent; 5+ years of adversarial emulation experience |
| Cloud security assessment | Cloud-specific certification (AWS Security, Azure Security, GCP Professional Security) or equivalent |
| OT / ICS assessment | GICSP, GRID, or equivalent; operational technology experience with safety-aware methodology |
| Social engineering engagement | SE-specific training or certification; understanding of legal and ethical boundaries |

#### Selection and Vetting Requirements

| **Requirement** | **Detail** |
|---|---|
| Conflict of interest disclosure | Firm must disclose any prior or current relationship with the organization's competitors, vendors, or key personnel that could compromise objectivity |
| Background checks | All testers assigned to the engagement must have passed a background check within the last 12 months; evidence of clearance retained by the Vendor Risk Analyst |
| Insurance | Firm must carry professional liability / errors and omissions insurance appropriate to the engagement scope; certificate of insurance on file |
| References | At least two references from engagements of comparable scope and sensitivity in the last 24 months |

#### Vendor Rotation Policy

- External testing vendors are rotated at minimum every 3 years for each scope area (network, application, cloud, OT, social engineering).
- Rotation applies to the firm, not individual testers.
- Exceptions require CISO approval and are documented in the risk register.

#### Contractual Requirements

- Non-disclosure agreement (NDA) covering all findings, data accessed, and methods used
- Data handling: all customer data accessed during testing is treated as Restricted; no data leaves the organization's control without explicit authorization
- Evidence destruction: upon engagement closure or within 30 days, the firm certifies destruction of all engagement data, findings drafts, and tool output in their possession
- Right-to-audit: the organization reserves the right to audit the firm's handling of engagement data
- Notification of subcontractors: the firm must disclose any subcontractors and their qualifications before engagement start

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
6. **Reflect**, feed result into detection inventory; update DT-002 metric in [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md).

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
| Configuration | Headers (HSTS, CSP, etc.), TLS conformance to [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md), exposed admin endpoints. |
| Business logic | Workflow bypass, race conditions, abuse of intended functionality. |
| API | OWASP API Top 10: object-level, function-level, mass assignment, rate limiting, etc. |
| Mobile | OWASP MASTG: storage, transport, platform interaction, code quality, resilience. |

---

### 8.1 Social Engineering Engagements

Social engineering tests the human layer of security controls. These engagements carry unique legal, ethical, and operational risks that require explicit guardrails.

#### Scope Definition

| **Engagement Subtype** | **Description** | **Typical Scope** |
|---|---|---|
| Phishing simulation | Simulated phishing email campaign to test user awareness and reporting behavior | Organization-wide or targeted departments |
| Vishing (voice phishing) | Simulated phone-based social engineering to extract information or credentials | Named individuals or departments with CISO approval |
| Smishing (SMS phishing) | Simulated text message-based social engineering | Named individuals or departments with CISO approval |
| Physical social engineering | Tailgating, badge cloning, or pretext-based physical access attempts | Named facilities with Facility Security coordination |
| USB drop | Simulated malicious USB devices placed in common areas | Named facilities with Facility Security coordination |

#### Pretexting Rules and Limitations

- Pretexts must not impersonate law enforcement, government officials, or regulatory authorities.
- Pretexts must not exploit personal tragedy, medical conditions, or family emergencies.
- Pretexts must not target minors or non-employees.
- Pretexts must not threaten employment status, compensation, or benefits.
- All pretexts are defined in the RoE and approved by the Engagement Sponsor.

#### Prohibited Targets (require explicit CISO approval)

- C-suite executives and their direct administrative staff
- Board members
- Legal counsel (internal and external)
- Human Resources personnel
- Personnel on leave (medical, family, or other protected leave)

#### Coordination Protocol

| **Stakeholder** | **When** | **Purpose** |
|---|---|---|
| Legal | Before RoE approval | Review pretexts for legal risk; confirm no violation of wiretapping, recording, or privacy laws |
| HR | Before RoE approval | Confirm no employee relations risk |
| Facility Security | Before physical or USB engagements | Coordinate access testing; prevent alarm triggers or law enforcement response |
| SOC / Detection Team | Before go-live | Prevent the engagement from being treated as a real incident |
| Incident Commander | Before go-live | Pre-brief: if engagement triggers detection, the IC knows it's a test |

#### Reporting Requirements

Social engineering findings are reported separately from technical findings. The report includes:

- Engagement subtype and scope
- Number of targets and interactions
- Success rate per subtype and per department
- Root cause themes (e.g., lack of verification procedure, urgency exploitation, authority bias)
- Recommended awareness and control improvements
- Comparison to prior social engineering engagements (if applicable)

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

Findings are rated using a uniform schema regardless of engagement type, aligning to [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) severity bands so they can co-route into vulnerability management:

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
| Specific software / asset vulnerability | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) finding + risk register entry per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) if Critical/High |
| Control / design weakness | Risk register entry directly per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| Detection gap | Detection backlog + risk register if material |
| Process / runbook weakness | Owning procedure (AR / IR / TPRM) + risk register if material |
| Vendor / supply chain weakness | TPRM record per [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| OT-specific weakness | OT vulnerability management workflow per [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) §4.3 and §6.3 + risk register |

### 10.3 Retest and Closure

- Critical findings retested within 30 days of remediation claim.
- High findings retested within 60 days.
- Medium/Low retested at next routine engagement or by sampled VM scan.
- A finding moves to Closed only after retest demonstrates remediation; a finding that cannot be remediated moves through the risk register acceptance path with explicit Approver.
- Closed findings inform the threat model for the affected system at next architecture review.

### 10.4 Escalation for Stalled Remediation

When remediation stalls beyond the retest window, the finding escalates.

#### Escalation Triggers

| **Trigger** | **Action** |
|---|---|
| Critical finding not remediated at 30 days | Adversarial Testing Lead escalates to Risk Pillar Leader |
| Critical finding not remediated at 45 days | Risk Pillar Leader escalates to CISO |
| Critical finding not remediated at 60 days | CISO escalates to Executive; risk acceptance required |
| High finding not remediated at 60 days | Adversarial Testing Lead escalates to Risk Pillar Leader |
| High finding not remediated at 90 days | Risk Pillar Leader escalates to CISO |
| Medium finding not remediated at 120 days | Adversarial Testing Lead escalates to system owner's pillar leader |

#### Escalation Ladder

Adversarial Testing Lead → Risk Pillar Leader → CISO → Executive Sponsor

At each level, the responsible party must either (a) produce a credible remediation plan with a committed date, (b) initiate a risk acceptance through [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), or (c) provide a written rationale. Non-response at any level automatically escalates after 5 business days.

#### Risk Acceptance as the Only Alternative

When remediation is not feasible, risk acceptance requires: a written risk statement per PRC-RM-001 §4.1, documented compensating controls, approval per the authority matrix, and a scheduled re-review date. A finding that is neither remediated nor risk-accepted is a program gap, not an operational delay.

---

### 10.5 Adversarial Validation Final Report

Every engagement produces a Final Report - the authoritative record of what was tested, found, and recommended.

#### Required Sections

| **Section** | **Content** |
|---|---|
| Executive Summary | Engagement type, scope, dates; findings summary by severity; top three risks; overall posture assessment; recommended next actions |
| Engagement Overview | RoE reference; scope (systems, networks, applications); out-of-scope items; timeline; tester(s); methodology summary |
| Methodology | Reconnaissance and enumeration techniques; exploitation approach; post-exploitation and lateral movement; tools and frameworks used |
| Findings | Each finding includes ID, severity, title, description, affected assets, evidence (annotated screenshots, command output), risk statement, remediation recommendation, references (CVE, ATT&CK, CWE) |
| Systemic Analysis | Patterns across findings; control themes that failed; root cause candidates |
| Trend Analysis (if applicable) | Comparison to prior engagements; findings closed since last engagement; new vs. recurring findings; trend direction |
| Appendices | Evidence artifacts, exploit code references (sanitized), timeline of key events, tools inventory |

#### Evidence Artifact Standards

- **Screenshots**: Annotated with arrows or captions highlighting relevant detail; include timestamp and host identifier
- **Command output**: Full command and output with timestamp; truncation acceptable with notation
- **Packet captures**: Time-stamped with source/destination; filtered to relevant conversation
- **Exploit code**: Referenced by tool and version, not reproduced in full

---

### 10.6 Inter-Rater Reliability for Finding Ratings

Different testers may rate the same finding differently. The following process ensures severity ratings are consistent and defensible.

#### Peer Review for High-Severity Findings

All Critical and High findings receive a peer review by a second qualified tester before the finding is finalized. The peer reviewer validates:
- The severity rating against the definitions in Section 10.1
- That the evidence supports the severity determination
- That the finding is not a duplicate of a known issue

If the peer reviewer disagrees with the severity, the Adversarial Testing Lead facilitates resolution. The final severity is the consensus rating, or the higher of the two if consensus cannot be reached.

#### Calibration Sessions

Quarterly calibration sessions are conducted using a sample of anonymized findings from recent engagements. All testers independently rate each finding. Results are compared and discussed. The purpose is to:
- Align severity interpretation across testers
- Identify systematic over-rating or under-rating patterns
- Refine severity definitions where ambiguity is found

The Adversarial Testing Lead facilitates calibration and documents outcomes. Calibration results inform tester development and, where appropriate, updates to this procedure's severity definitions.

#### Dispute Resolution

| **Dispute** | **Resolution** |
|---|---|
| Tester and peer reviewer disagree on severity | Adversarial Testing Lead facilitates; default to higher severity if unresolved |
| Tester and system owner disagree on severity | Risk Pillar Leader reviews; severity determined by risk to the organization, not by remediation difficulty |
| Tester and CISO disagree on Critical classification | CISO makes final determination; rationale documented |

---

## 11. Systemic Analysis and Program Feedback Loop

An Adaptive program does not stop at fixing individual pen-test findings. It asks: why did four of six DMZ servers share the same misconfiguration? What standard or procedure failed to prevent this? How do we change the program so the next engagement does not repeat the same class of finding?

This section defines the post-engagement systemic analysis that converts adversarial validation findings into program improvements.

### 11.1 Post-Engagement Systemic Analysis

After every adversarial validation engagement, the Adversarial Testing Lead produces two outputs: a findings report (existing) and a systemic analysis (new). The systemic analysis answers four questions:

1. **Which findings share a common root cause?** Example: four findings relate to default credentials on newly provisioned systems : the provisioning process does not enforce credential rotation. This is not four separate problems; it is one systemic weakness manifesting in four locations.
2. **Which findings indicate a standard or procedure gap?** Example: DMZ web servers all had the same TLS misconfiguration : STD-CFG-001 or STD-NET-001 does not specify DMZ TLS requirements clearly enough.
3. **Which findings indicate a control effectiveness gap?** Example: WAF was deployed per CB-001 but three bypass techniques worked : the WAF control is Implemented but not effective (per CEF-001).
4. **Which findings indicate a detection gap?** Example: testers pivoted laterally for four hours without an alert : detection rules need updating for the observed technique chain.

### 11.2 Systemic Finding Routing

Each systemic finding is routed to the appropriate owner for program-level action:

| Systemic Finding Type | Routed To | Tracking Mechanism |
|---|---|---|
| Standard or procedure gap | Governance Pillar Leader (Policy & Standards Manager) | IMPREG-001 (Type: Standard revision or Procedure update) |
| Control effectiveness gap | Accountable pillar leader (per CB-001) | IMPREG-001 (Type: Control amendment) + CEF-001 control failure analysis |
| Detection gap | Risk Pillar Leader (Detection Engineer) | Detection backlog per LM-001 + IMPREG-001 if systemic |
| Process gap | Accountable procedure owner (per RAC-001) | IMPREG-001 (Type: Procedure update) |
| Tooling or capability gap | Relevant pillar leader | IMPREG-001 (Type: New capability) + CISO if budget required |

Routed systemic findings are tracked in the improvement register (IMPREG-001) per the improvement lifecycle. The source field records the engagement ID and date.

### 11.3 Prevention Verification

At the next adversarial validation engagement of the same type, scope, or target environment, the engagement plan includes re-testing the systemic weaknesses identified in the prior engagement.

- If the same class of finding does NOT recur: the systemic improvement is verified Effective in IMPREG-001.
- If the same class of finding recurs: the improvement is marked Ineffective or Partially Effective, re-opened in IMPREG-001, and the root cause analysis is re-examined. The fact that a deliberate program change did not prevent recurrence is itself a critical lesson.

> **The Recurrence Test**
>
> An assessor reviewing two consecutive pen test reports should see: (a) the specific vulnerabilities from the prior test are closed, AND (b) the systemic weakness that produced them no longer produces new findings of the same class. If the second report finds different specific vulnerabilities but the same systemic root cause : different default credentials on different systems : the improvement failed. The program that only fixes individual findings and never the systemic cause is operating at Repeatable, not Adaptive.

### 11.4 Annual Trend Analysis

Annually, the Adversarial Testing Lead produces an adversarial validation trend analysis covering all engagements in the trailing 12 months:

- Are total findings increasing or decreasing? Segmented by severity.
- Are systemic weaknesses repeating across engagements?
- Which control families (per CB-001) produce the most findings? The most Critical and High findings?
- Which control families show improvement (fewer findings year-over-year)?
- How many systemic findings were routed to IMPREG-001, and what was their verification outcome?

The trend analysis feeds into:
- The control effectiveness program (CEF-001): control families with persistently high finding rates trigger a control failure analysis
- The risk appetite calibration (RMF-001): a finding-rate trend that undermines a risk appetite assumption triggers recalibration
- The annual maturity assessment (MAT-001): finding-rate trends are evidence of control effectiveness or ineffectiveness

---

## 12. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **Adversarial Testing Lead** | Owns this procedure. Produces the annual plan, engagement RoE/Charter, findings report, and systemic analysis. Routes systemic findings. Produces the annual trend analysis. |
| **Risk Pillar Leader** | Accountable for the adversarial validation program. Approves the annual plan. Reviews systemic analysis outputs. |
| **CISO** | Approves the annual plan. Authorizes red-team and OT engagements. Receives Critical finding notifications. |
| **Engineering Pillar Leader** | Receives and acts on design, architecture, and configuration systemic findings. Participates in scoping. |
| **Governance Pillar Leader** | Receives standard and procedure gap systemic findings. Coordinates catalog amendments resulting from systemic improvements. |
| **Detection Engineer** | Receives detection gap findings. Updates detection rules and reports on coverage improvement. |
| **Exposure Management Lead** | Receives specific vulnerability findings. Tracks remediation to closure per PRC-VM-001. |
| **Risk Register Owner** | Records material findings as risk register entries. Links risk entries to improvement entries when systemic. |
| **OT Safety Officer** | Named for each OT engagement. Holds binding stop authority. Reviews OT scope and safety constraints. |

---

## 13. Evidence Retention

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
## 14. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Procedure** |
|---|---|
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CA-8 | All sections |
| NIST 800-115 | All sections |
| PTES | Sections 3–4 |
| MITRE ATT&CK | Sections 6, 7 |
| OWASP WSTG / MASTG / API Top 10 | Section 8 |
| NERC-CIP CIP-007 R3.2 (vulnerability assessment) | Sections 9, 10 |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.11.2) | Sections 3, 8 |

---

## 15. Document Control

| | |
|---|---|
| **Document ID** | CERG-PRC-AV-001 |
| **Version** | 1.2 |
| **Approved By** | CISO |
| **Next Review** | Annual / on material program change |
| **Change Log** | 1.0 - Initial publication. Engagement types, RoE, charter, purple, cloud, app, OT safety, rating/routing, evidence retention. · 1.1 - Added Section 11 Systemic Analysis and Program Feedback Loop: post-engagement systemic analysis, systemic finding routing, prevention verification, and annual trend analysis. · 1.2 - Restored Section 12 Roles and Responsibilities. Renumbered Evidence Retention to Section 13, Regulatory to 14, Document Control to 15. |