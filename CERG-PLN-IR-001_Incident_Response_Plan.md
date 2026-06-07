
# SURGE: Cyber Engineering, Risk & Governance

## INCIDENT RESPONSE PLAN
### Detection · Containment · Investigation · Notification · Recovery · Lessons Learned

---

| | |
|---|---|
| **Document ID** | CERG-PLN-IR-001 |
| **Version** | 1.21 |
| **Status** | Published |
| **Classification** | Public |
| **Owner** | CISO · IR Plan Steward |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) |
| **Review Cycle** | Annual / After Any Significant Incident / Regulatory Change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (RS, RC) · [NIST 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r2/final) · NIST RMF |
| **Regulations** | NERC-CIP CIP-008 · [CMMC](https://dodcio.defense.gov/CMMC/) IR.L2 · DFARS 252.204-7012 · SEC 8-K Item 1.05 (where applicable) · State breach laws · GDPR (where applicable) |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Authority and Activation](#2-authority-and-activation)
3. [Roles and the Incident Response Team](#3-roles-and-the-incident-response-team)
4. [Incident Lifecycle](#4-incident-lifecycle)
5. [Severity Classification](#5-severity-classification)
6. [Notification Obligations](#6-notification-obligations)
7. [Environment-Specific Considerations](#7-environment-specific-considerations)
8. [Playbooks](#8-playbooks)
9. [Communications](#9-communications)
10. [Evidence, Forensics, and Legal Privilege](#10-evidence-forensics-and-legal-privilege)
11. [Exercises and Plan Maintenance](#11-exercises-and-plan-maintenance)
12. [Regulatory and Framework Alignment Summary](#12-regulatory-and-framework-alignment-summary)
13. [Plan Control](#13-plan-control)

---

## 1. Purpose and Scope

This plan operationalizes the incident response principle established in **[CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Principle 10**. It defines how the organization detects, contains, investigates, notifies, recovers from, and learns from cybersecurity events across all in-scope environments.

The plan is intentionally cross-environment. A single incident may span enterprise IT, cloud, SaaS, OT, and CUI environments simultaneously. The plan provides one structure of authority, classification, and notification, with environment-specific overlays that reflect the operational and regulatory reality of each domain.

### 1.1 Scope

This plan applies to:

- All confirmed and suspected cybersecurity events affecting organizational assets, data, or personnel
- All in-scope environments, owned data center, hybrid, cloud, SaaS, OT, BES Cyber Systems, CUI environments
- All third-party incidents that materially affect the organization (vendor compromises, software supply-chain compromises, shared-tenant impacts)
- All personnel involved in detection, response, decision-making, communication, and recovery

### 1.2 Definitions

| **Term** | **Definition** |
|---|---|
| **Event** | Any observable occurrence in a system or network. Not all events are incidents. |
| **Incident** | An event that violates security policy, threatens confidentiality, integrity, or availability, or has the realistic potential to do so. |
| **Significant Cyber Incident** | An incident classified Sev 1 or Sev 2 under Section 5, or any incident triggering an external notification obligation. |
| **Reportable Cyber Incident (DFARS)** | A cyber incident that affects covered defense information or the contractor's ability to perform operationally critical support - triggers 72-hour DC3 reporting. |
| **Reportable Cyber Security Incident (NERC-CIP)** | An incident as defined in NERC Glossary that compromises or attempts to compromise an ESP, PSP, or BES Cyber System, or disrupts BES operations. |
| **Material Cybersecurity Incident (SEC)** | An incident determined material under SEC Item 1.05 (Form 8-K), based on reasonable-investor materiality - triggers a 4-business-day disclosure clock. |
| **Incident Commander (IC)** | The CISO or designated deputy with single-decision authority for an active incident. |
| **Lead Investigator** | Risk-side technical lead for the investigation. Reports to the IC. |

### 1.3 Relationship to Parent Policy and Standards

This plan is subordinate to **[CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md)** and implements the response and recovery obligations of the peer standards. Where a peer standard imposes additional or more stringent notification, evidence, or recovery requirements, the more stringent requirement controls.

---

## 2. Authority and Activation

### 2.1 Authority

> **Single Decision Authority During Active Response**
>
> Incident response is not a consensus activity. The Incident Commander has single decision authority during active response. Containment and notification decisions are made by the IC after consultation with the appropriate Subject Matter Experts; they are not voted on. The IC remains accountable to the CISO and executive leadership and is briefed continuously.

The CISO is the standing Incident Commander. The CISO may delegate IC authority to a named deputy for a specific incident, with notification to executive leadership. Authority transitions are explicit and logged.

### 2.2 Activation Triggers

Activate this plan upon any of the following:

- Confirmed compromise of credentials with privileged access, or of a privileged identity platform
- Confirmed or strongly suspected unauthorized access to organizational systems or data
- Confirmed presence of ransomware, destructive malware, or unauthorized cryptographic activity on organizational systems
- Confirmed exfiltration or unauthorized disclosure of Confidential or Restricted-tier data
- Significant denial of service, integrity, or availability event affecting Tier 1 systems
- Any cyber event affecting BES Cyber Systems, CUI environments, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems, or other regulated assets, where regulatory notification timelines may apply
- Vendor or supply-chain notification indicating the organization may be affected
- External notification (law enforcement, regulator, partner, customer) of a credible threat or breach

### 2.3 Activation Process

1. **Triage.** SOC / on-call analyst confirms the event meets activation criteria using documented triage criteria. When in doubt, activate.
2. **Notify.** Page the on-call IC and Lead Investigator. The IC confirms activation and assigns an incident identifier.
3. **Establish.** Open the incident channel (defined out-of-band communication path), open the incident record (ticketing system), and begin the timeline log.
4. **Brief.** Initial brief to the IC within 30 minutes of activation. The IC determines initial severity classification.
5. **Mobilize.** IC convenes the Incident Response Team appropriate to severity (Section 3).

---

## 3. Roles and the Incident Response Team

### 3.1 Standing Roles

| **Role** | **Standing Responsibility** |
|---|---|
| **Incident Commander (CISO / designated deputy)** | Single-decision authority; convenes and directs the IRT; owns external notification decisions; briefs executive leadership. |
| **Lead Investigator** | Owns technical investigation; coordinates evidence collection and forensic analysis; produces the incident technical timeline. |
| **Engineering Pillar Leader** | Executes containment and recovery technical actions; coordinates with platform teams; advises on architectural impact. |
| **Governance Pillar Leader** | Owns the regulatory notification clock; maintains the SSP / POA&M impact tracking; coordinates with Legal on privilege; supports evidence preservation; assembles the post-incident report. |
| **Legal (external function)** | Advises on privilege, notification obligations, regulator engagement, customer / partner contractual notifications, law enforcement engagement. |
| **Communications (external function)** | Coordinates internal, customer, partner, and external public communications under IC direction. |
| **Executive Sponsor (CEO / COO / CIO / CFO as appropriate)** | Provides executive decision support for material business, regulatory, or financial determinations. |
| **Operations Representative (external function)** | Coordinates operational impact assessment and recovery sequencing. For OT events, the operations liaison is the on-shift operations supervisor or designee. |

### 3.2 Tier of Engagement

| **Severity** | **Engaged at Activation** | **Engaged on Escalation** |
|---|---|---|
| Sev 4 | SOC / Lead Investigator | - |
| Sev 3 | Lead Investigator + Engineering Lead | IC (notified) |
| Sev 2 | IC + Lead Investigator + Engineering Lead + Governance | Legal + Communications + Executive Sponsor |
| Sev 1 | Full IRT incl. Legal + Communications + Executive Sponsor + Board notification | External support (forensics retainer, law enforcement liaison, breach coach) |

### 3.3 Third-Party Engagement

The CISO maintains the following pre-arranged external retainers, activated by the IC as needed:

- **External forensics / digital investigation retainer**: for surge capacity, specialized expertise, or independent investigation
- **Breach coach / outside counsel**: for privilege, multi-jurisdictional notification, and external communication
- **Public relations / crisis communications partner**: engaged at IC direction for material incidents
- **Law enforcement / federal liaison contacts**: FBI, CISA, sector ISAC, and DC3 (for CUI incidents)

Retainer contacts and activation procedures are maintained in the IRT contact roster, reviewed quarterly and distributed only to the standing IRT.

---

## 4. Incident Lifecycle

The lifecycle follows [NIST 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) phases adapted for cross-environment operations.

### 4.1 Preparation (Continuous)

Preparation is the work performed before any specific incident. It includes maintaining this plan, training the IRT, exercising playbooks, validating tooling, maintaining external retainers, and ensuring detection telemetry is functioning. Preparation is not optional and is not "off the clock."

### 4.2 Detection and Analysis

| **Step** | **Action** | **Owner** |
|---|---|---|
| 1 | Detection signal arrives (SIEM, EDR, CSPM/SSPM, partner / vendor notification, user report, external alert). | SOC / Risk |
| 2 | Initial triage applies documented criteria to determine whether the event warrants activation. | SOC / Risk |
| 3 | Activation triggers the procedure in Section 2.3. The incident timeline log begins. | IC |
| 4 | Lead Investigator builds a working hypothesis: scope, affected systems, suspected technique, blast radius. Re-evaluates continuously. | Lead Investigator |
| 5 | IC sets initial severity (Section 5). Severity is re-evaluated at each major learning. | IC |

### 4.3 Containment

Containment objectives: stop ongoing harm, prevent lateral movement, preserve evidence, maintain operational integrity.

| **Containment Type** | **Use** | **Considerations** |
|---|---|---|
| **Short-term** | Immediate isolation actions to stop ongoing impact (disable account, revoke session, isolate host, block IOC at firewall / EDR). | Designed to be reversible and to preserve forensic data. |
| **Long-term** | Architectural changes that prevent the same path being used during recovery (e.g., new IAM policies, network segmentation, rebuilt systems). | Implemented before declaring eradication complete. |
| **Operational hold** | Pause of non-essential activity to focus response (e.g., temporary block on outbound SaaS connections, suspension of non-essential remote access). | Approved by IC with operations input. |

> **The "Don't Tip Your Hand" Reminder**
>
> Premature containment can warn an adversary and accelerate destructive action, particularly in ransomware or supply-chain scenarios where the attacker may be actively monitoring response. Pace containment to scope, prefer reversible isolation, and coordinate with the Lead Investigator on telemetry implications before each major action.

### 4.4 Eradication

Eradication removes the adversary's access and the means by which it was obtained. Eradication is declared complete only when:

- All identified persistence mechanisms (accounts, scheduled tasks, services, OAuth grants, IaC backdoors, malicious code) have been removed.
- Underlying vulnerabilities or misconfigurations have been remediated.
- Compensating controls are in place for issues that cannot be fully remediated immediately.
- Independent verification confirms the eradication actions.

### 4.5 Recovery

Recovery restores affected systems to operational service. Recovery is coordinated with operations, sequenced by business priority, and monitored for indications of recurrence.

| **Step** | **Action** | **Owner** |
|---|---|---|
| 1 | Identify systems for restoration and the sequence. Critical operations restored first with elevated monitoring. | Engineering / Operations |
| 2 | Restore from verified-clean baselines or trusted backups. Validate integrity before bringing systems online. | Engineering |
| 3 | Validate that restored systems are not reinfected; monitor with enhanced detection. | Risk / Engineering |
| 4 | Phased return-to-service with documented validation gates. | IC / Operations |
| 5 | Operations confirms business resumption; IC closes the operational response phase. | IC |

### 4.6 Post-Incident Activity (Lessons Learned)

A post-incident review is mandatory for every Sev 1 and Sev 2 incident, and recommended for Sev 3. Sev 1 reviews occur within 14 calendar days of recovery; Sev 2 within 30 days.

The review produces:

- A factual timeline (detection, containment, eradication, recovery, notification milestones)
- A root-cause analysis (technical and process)
- A list of corrective actions categorized as Engineering, Risk, or Governance backlog items
- Updates to playbooks, detection rules, and this plan
- Lessons-learned briefing to leadership and to the IRT

Corrective actions are tracked to closure in the risk register with assigned owners and due dates.

---

## 5. Severity Classification

Severity drives engagement, communication cadence, and notification scrutiny. Severity may be revised at any time during response.

| **Severity** | **Indicative Criteria (any of)** | **Engagement** | **Reporting** |
|---|---|---|---|
| **Sev 1 - Critical** | Confirmed material data loss or destruction; ransomware encrypting Tier 1 or regulated systems; confirmed compromise affecting BES Cyber System operations; broad customer / partner impact; meets reasonable-investor materiality threshold for SEC disclosure. | Full IRT, executive sponsor, board notification, external partners as needed. | Hourly IC briefing to executive leadership during active response. |
| **Sev 2 - Significant** | Confirmed unauthorized access to Tier 1 systems or Confidential/Restricted data; ransomware contained to non-critical scope; confirmed cyber incident triggering DFARS / NERC-CIP / breach-law notification. | IC + full IRT + Legal + Communications. | At least twice-daily IC briefing during active response. |
| **Sev 3 - Moderate** | Localized compromise (single endpoint, scoped credential), with no confirmed sensitive-data impact; significant phishing wave with successful but contained credential theft. | IC notified; Lead Investigator + Engineering active. | Daily IC update until closure. |
| **Sev 4 - Minor** | Failed attack with no impact; isolated malware blocked by EDR; SOC-triaged anomaly with no escalation criteria met. | SOC / Risk only. | Routine SOC reporting. |

The IC may up- or down-grade severity at any time based on emerging information. Severity changes are logged on the incident timeline.

---

## 6. Notification Obligations

Notification is one of the highest-risk areas of incident response. Many obligations operate on clocks that begin at discovery, not at confirmation. The Governance Lead owns the notification clock for each in-flight incident and tracks all applicable obligations on a per-incident notification register.

### 6.1 Internal Notification

| **Audience** | **Trigger** | **Owner** | **Timing** |
|---|---|---|---|
| CISO / IC | Plan activation | SOC / on-call | Immediate |
| Executive leadership (CEO/CIO/CFO/COO) | Sev 1 / Sev 2 activation | IC | Within 1 hour of activation |
| Board (Audit / Risk Committee) | Sev 1; or Sev 2 with regulatory / financial implications | CISO via CEO | Within 24 hours of confirmation per board protocol |
| Workforce communications | Sev 1; or any incident requiring workforce action | Communications + IC | As approved by IC |
| Internal Audit | Sev 1; [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant incidents | Governance | Per [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) protocol |

### 6.2 External Notification (Regulator and Statutory)

| **Authority / Obligation** | **Trigger** | **Clock** | **Owner** | **Reference** |
|---|---|---|---|---|
| **DoD DC3 / DIBNet** | Reportable cyber incident affecting CUI or operationally critical support | **72 hours** from discovery | Governance + Legal | DFARS 252.204-7012(c) |
| **NERC E-ISAC and Regional Entity** | Reportable Cyber Security Incident or attempt against BES Cyber Systems | Per CIP-008 timelines (1 hour for compromise of BCS; 24 hours for attempts) | Governance | NERC-CIP CIP-008-6 R1.4 |
| **SEC (Form 8-K Item 1.05)** | Material cybersecurity incident at a public-company registrant | **4 business days** from materiality determination | CISO + Legal + CFO | SEC Reg S-K Item 106(b); Form 8-K Item 1.05 |
| **State breach notification laws** | Unauthorized acquisition of state-defined personal information | Per state - often "without unreasonable delay"; specific deadlines vary (e.g., 30/45/60 days) | Legal + Governance | State statutes |
| **GDPR Supervisory Authority** (where applicable) | Personal data breach with risk to data subjects | **72 hours** from awareness | Legal / DPO | GDPR Art 33 |
| **HIPAA Breach Notification** (where applicable) | Breach of unsecured PHI | Per HIPAA timelines | Legal / Privacy | HIPAA 164.400 series |
| **Sector / customer contractual notification** | Per contract terms (often 24–72 hours) | Per contract | Governance + Account Management | Contractual |
| **Law enforcement (FBI / Secret Service / local)** | Sev 1 events at IC / Legal discretion; mandated reporting in some jurisdictions | At IC discretion unless mandated | IC + Legal | Jurisdiction-specific |
| **CISA voluntary reporting (and CIRCIA when in force)** | Significant cyber incidents at critical infrastructure entities | Per CIRCIA rule (72 hours for incidents; 24 hours for ransom payments) once effective | Governance + Legal | CIRCIA (when final rule effective) |

### 6.3 Notification Decision Discipline

> **Two Failure Modes**
>
> The two notification failure modes are: notifying too early on incomplete information, or notifying too late after the regulatory clock has run. Both are damaging. The discipline is: (a) start the regulatory clock log at the moment of discovery, not at the moment of confirmation; (b) make notification decisions through the IC + Legal + Governance triad, not unilaterally; (c) document the rationale at each decision point. If you would not be willing to defend the rationale to a regulator after the fact, do not adopt it during the incident.

---

## 7. Environment-Specific Considerations

### 7.1 Enterprise IT / Cloud / SaaS

Containment leverages cloud-native isolation (quarantine IAM, account suspension, security-group changes), conditional-access lockdowns, and SaaS admin-controlled session revocation. Forensic acquisition depends on provider-exposed artifacts; pre-staged acquisition procedures are maintained per **[CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) §7**.

### 7.2 OT / BES Cyber Systems

> **Operational Priority Rule**
>
> Response in OT environments evaluates every containment action for operational impact before execution. Isolation that would be routine in IT can produce a grid disturbance in OT. OT response actions require operations-team participation in the decision, not just notification.

OT incidents engage the operations liaison as a peer decision-maker on containment options. Containment defaults to least-disruptive options first (passive monitoring intensification, network-edge controls) before in-band actions. NERC-CIP CIP-008 reporting timelines run regardless of operational readiness, Governance owns those clocks.

### 7.3 CUI Environments

CUI incidents trigger DFARS 252.204-7012 reporting via DC3 / DIBNet within 72 hours of discovery (Section 6.2). Evidence preservation requirements (90-day retention of images and malware) apply per **[CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) §7**. The Governance Lead coordinates with the contracting officer when required by contract.

### 7.4 [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-Relevant Systems

Incidents affecting [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems require Internal Audit and CFO designee engagement to assess ITGC control implications. Material control gaps may require disclosure considerations under SEC Item 1.05.

### 7.5 Third-Party / Supply-Chain Incidents

When the originating compromise is a third party (vendor, SaaS provider, software supplier), the IC owns the determination of whether the organization is itself affected, what containment actions are appropriate, and what onward notification is required. Vendor incident notifications are not a substitute for the organization's own investigation.

---

## 8. Playbooks

The plan is supported by detailed playbooks maintained as living artifacts in the CERG Governance library. Each playbook follows a consistent structure: trigger criteria, immediate actions, investigation steps, containment options, recovery steps, evidence checklist, and notification triggers.

Currently maintained playbooks:

| **Playbook** | **Scenario** |
|---|---|
| PB-01 | Ransomware / Destructive Malware |
| PB-02 | Privileged Credential Compromise (IT) |
| PB-03 | Privileged Credential Compromise (Cloud / SaaS) |
| PB-04 | OAuth / Third-Party App Abuse (SaaS) |
| PB-05 | Compromised Cloud Workload (IaaS) |
| PB-06 | Cloud Control-Plane Compromise |
| PB-07 | Public Exposure of Sensitive Data (cloud storage / database) |
| PB-08 | Data Exfiltration Confirmed or Suspected |
| PB-09 | Supply Chain / Vendor Compromise |
| PB-10 | Phishing Wave with Successful Credential Theft |
| PB-11 | Insider Threat - Authorized User Misuse |
| PB-12 | DDoS / Availability Attack |
| PB-13 | BES Cyber System Compromise (CIP-008) |
| PB-14 | OT - Loss of SCADA Visibility / Control |
| PB-15 | CUI Cyber Incident (DFARS 7012 reporting) |
| PB-16 | Lost / Stolen Endpoint with Sensitive Data |
| PB-17 | Business Email Compromise (BEC) |
| PB-18 | Web Application Compromise |

Playbooks are reviewed annually and updated upon material change to environment, tooling, or regulation. Playbook updates derived from post-incident reviews are tracked as Engineering / Risk / Governance backlog items.

---

## 9. Communications

### 9.1 Internal Communications

Internal communications channels for active response are pre-established and exercised. The plan assumes the possibility that organizational productivity systems (email, chat, ticketing) are compromised or unavailable.

| **Channel** | **Use** |
|---|---|
| Primary incident channel | Coordination among IRT; updated by IC and Lead Investigator. |
| Out-of-band channel | Used when primary collaboration tooling is potentially compromised or unavailable. Defined and tested in advance. |
| Executive briefing channel | IC → executive sponsors and CEO. |
| Workforce broadcast | Used for actions required of the broader workforce (e.g., reset credentials, do not click links). Approved by IC. |

### 9.2 External Communications

External communications during an active incident are owned by the IC, with content prepared by Communications and reviewed by Legal. The principles are:

- Say only what is established as fact. If a claim is not supported by current evidence, do not make it.
- Lead with the actions being taken and the protections in place for affected parties.
- Coordinate timing of public statements with regulatory and contractual notifications.
- Refer technical questions to the appropriate IRT spokesperson; refer regulatory questions to Governance.
- Document every external statement in the incident timeline.

---

## 10. Evidence, Forensics, and Legal Privilege

### 10.1 Evidence Handling Principles

| **Principle** | **Description** |
|---|---|
| Preserve before you contain | Where feasible, capture volatile state (memory, network captures, ephemeral cloud telemetry) before destructive containment. |
| Chain of custody | Every evidence artifact is logged: source system, time captured, method, custodian, hash. |
| Original integrity | Work from images and copies. Do not modify original artifacts. |
| Provider-side evidence | For cloud and SaaS, identify which artifacts are obtainable from the provider and what the retention window is - request promptly. |
| Retention | Evidence is retained per the most stringent applicable obligation. DFARS requires 90-day minimum for CUI incidents. |

### 10.2 Privilege

The Legal Lead is involved at activation for all Sev 1 and Sev 2 events. Privileged work product is created under counsel direction and labeled accordingly. Whether and how privilege applies to forensic findings is a judgment of counsel; the IRT operates with privilege awareness from the outset.

### 10.3 Law Enforcement Engagement

Engagement with law enforcement is at the IC's discretion in consultation with Legal, except where reporting is mandated. Law enforcement engagement may affect notification timing and content; Governance maintains the contact procedure for FBI Cyber, Secret Service, CISA, and DC3.

---

## 11. Exercises and Plan Maintenance

| **Activity** | **Cadence** | **Owner** |
|---|---|---|
| Tabletop exercise - Sev 1 scenario (cross-environment) | Annual | Governance + Risk |
| Tabletop exercise - OT (CIP-008) | Annual | Governance + Risk + OT Ops |
| Tabletop exercise - CUI (DFARS 7012 reporting) | Annual | Governance |
| Functional exercise / detection validation (purple-team) | Quarterly | Risk |
| IRT contact roster validation | Quarterly | Governance |
| External retainer activation test | Annual | Governance |
| Playbook review | Annual; after each use | Governance / Risk |
| This plan review | Annual; after any Sev 1 / Sev 2 incident; upon regulatory change | Governance |

Exercise results, including identified gaps and corrective actions, are recorded in the risk register and tracked to closure.

---

## 12. Regulatory and Framework Alignment Summary

| **Process Area** | **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | **[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)** | **NERC-CIP** | **[CMMC L2](https://dodcio.defense.gov/CMMC/)** | **Other** |
|---|---|---|---|---|---|---|
| IR Capability / Plan | RS / RC | IR-2, IR-4, IR-8 | 3.6.1 | CIP-008 R1 | IR.L2-3.6.1 | DFARS 252.204-7012 |
| Detection & Analysis | DE.AE, RS.AN | IR-4, AU-6, SI-4 | 3.6.1 | CIP-007 R4 | IR.L2-3.6.1 | - |
| Containment / Eradication | RS.MI | IR-4, IR-4(1)(2) | 3.6.2 | CIP-008 | IR.L2-3.6.2 | - |
| Notification (regulator / law enforce.) | RS.CO | IR-6 | 3.6.2 | CIP-008 R1.4 | IR.L2-3.6.2 | DFARS · GDPR · State |
| Recovery | RC.RP | CP-2, CP-10, IR-4 | 3.6.3 | CIP-009 | RE.L2-3.6.3 | - |
| Lessons Learned | ID.IM, RC.IM | IR-4(4), CA-7 | 3.6.3 | CIP-008 R3 | IR.L2-3.6.3 | - |
| Exercises & Testing | ID.IM | IR-3, IR-3(2) | 3.6.3 | CIP-008 R3 | IR.L2-3.6.3 | - |
| Disclosure (public registrant) | GV.RR | - | - | - | - | SEC 8-K Item 1.05 |

---

## 13. Plan Control

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 DRAFT | 2026 | CERG Governance | Initial release |

### Review Triggers

This plan shall be reviewed annually and upon any of the following:

- Any Sev 1 or Sev 2 incident affecting the organization
- Material change to applicable regulation (DFARS, CIP, SEC, breach laws, CIRCIA)
- Material change to the organization's environments or tooling
- IRT structural change (CISO transition, new external retainer)
- Direction from the CISO, internal audit, or external examination

Cyber Governance owns the plan as a document. The CISO owns the operational capability the plan describes. Updates require CISO approval and IRT acknowledgment.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - Principle 10 |
| Grid and Control System Standard | [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | OT IR overlay, CIP-008 obligations |
| IT (Hosted/Cloud/SaaS) Security Standard | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Cloud / SaaS IR overlay |
| CUI Handling Standard | [CERG-STD-C