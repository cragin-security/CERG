
# SURGE: Cyber Engineering, Risk & Governance

## THREAT INTELLIGENCE PROCEDURE
### Sources · Intake · Relevance · Dissemination · Action Tracking

---

| | |
|---|---|
| **Document ID** | CERG-PRC-TI-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) · [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) · [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Review Cycle** | Annual / On material change to threat landscape or intelligence sources |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (RA-3, RA-5, SI-5, PM-16) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.RA, DE.CM) · [MITRE ATT&CK](https://attack.mitre.org/) · [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) |
| **Regulations** | CMMC L2 / 800-171r3 · NERC-CIP · SOX ITGC where threat intelligence affects scoped systems |
| **Environments** | All CERG-managed environments and risk decisions informed by threat intelligence |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Intelligence Sources](#3-intelligence-sources)
4. [Intake and Triage](#4-intake-and-triage)
5. [Relevance and Priority](#5-relevance-and-priority)
6. [Products and Dissemination](#6-products-and-dissemination)
7. [Action Tracking](#7-action-tracking)
8. [Integration With CERG Processes](#8-integration-with-cerg-processes)
9. [Metrics](#9-metrics)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

The README names threat intelligence as a Cyber Risk function. The Operating Model names the Threat Intelligence Analyst as the role that tracks threat actors, advisories, and intelligence-to-detection translation. Existing procedures consume threat intelligence, but no procedure defined how intelligence is sourced, triaged, prioritized, disseminated, or tracked to action. This procedure closes that gap.

Threat intelligence in CERG is operational. Its purpose is not to publish interesting reports. Its purpose is to help the organization make better decisions sooner: patch the right thing faster, change a design before it ships, warn the right owner, tune a detection, reassess a vendor, or record a risk.

This procedure applies to all threat intelligence used by CERG to inform vulnerability management, threat modeling, architecture review, third-party risk, OT risk, detection priorities, and risk-register decisions.

> **Intelligence That Does Not Change Action Is Trivia**
>
> A threat feed can produce thousands of indicators and still produce no security outcome. CERG does not measure intelligence by volume. It measures whether intelligence reached the right owner in time to change a decision: patch this, block that, model this abuse case, watch this vendor, raise this risk. If a piece of intelligence has no decision path, it is context, not work.

---

## 2. Principles

1. **Relevance beats volume.** Intelligence is judged by its relationship to the organization's assets, technologies, vendors, data, and threat exposure.
2. **Timeliness matters.** A perfect advisory delivered after exploitation is history, not intelligence.
3. **Every actionable item has an owner.** If an intelligence item requires action, the action is assigned to a canonical role and tracked to disposition.
4. **Use multiple source types.** No single feed or vendor provides the full threat picture. CERG uses government, commercial, open-source, sector, vendor, and internal sources.
5. **Internal telemetry is intelligence.** Vulnerability trends, incidents, phishing reports, and adversarial testing findings are intelligence inputs, not just local events.
6. **Dissemination is tailored.** The CISO needs posture and decision impact. Engineering needs concrete action. Governance needs evidence and regulatory implication. Risk needs exposure and priority.

---

## 3. Intelligence Sources

The Threat Intelligence Analyst maintains a source register. Sources are reviewed at least annually for relevance, reliability, and usefulness.

| **Source Type** | **Examples** | **Primary Use** |
|---|---|---|
| Government and sector advisories | CISA, FBI, MS-ISAC, ES-ISAC, NCSC, sector regulators | High-confidence alerts, exploited vulnerabilities, sector campaigns. |
| Vendor advisories | Cloud, SaaS, endpoint, identity, OT, and security vendors | Product-specific vulnerabilities and mitigations. |
| Commercial intelligence | Paid intelligence platforms or managed-intelligence feeds | Actor tracking, campaign context, enriched indicators. |
| Open-source intelligence | Public research, blogs, GitHub advisories, abuse reports | Fast context, exploit availability, community findings. |
| Internal telemetry | Vulnerability data, phishing reports, incident lessons, adversarial testing findings | Organization-specific exposure and observed behavior. |
| Peer and trust groups | ISACs, industry groups, trusted peer exchanges | Sector targeting, early warning, practical mitigations. |
| Regulatory and legal updates | Regulator alerts, new requirements, enforcement activity | Governance and compliance implications. |

Restricted-source or sensitive intelligence is handled according to its classification under [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md).

---

## 4. Intake and Triage

### 4.1 Intake Channels

Threat intelligence enters through approved channels: source registers, email subscriptions, vendor portals, ISAC channels, internal reports, incident lessons, adversarial validation reports, and vulnerability advisories. Informal inputs are allowed, but once an item is actionable it is recorded in the intelligence intake log.

### 4.2 Minimum Intake Fields

Every actionable item records:

| **Field** | **Purpose** |
|---|---|
| Source | Where the item came from. |
| Date received | Timeliness and review tracking. |
| Summary | Plain-language statement of what changed. |
| Affected technologies, vendors, or sectors | Relevance check. |
| Associated vulnerabilities, techniques, or indicators | Links to CVEs, ATT&CK techniques, IOCs, or behaviors. |
| Known exploitation | Whether exploitation is observed, likely, or theoretical. |
| Initial priority | Critical, High, Medium, Low. |
| Action owner | Canonical role responsible for next step. |
| Disposition | Monitor, disseminate, create action, create risk, close. |

### 4.3 Triage Outcomes

| **Outcome** | **Meaning** |
|---|---|
| **Close as not relevant** | No affected asset, vendor, technology, sector, or plausible exposure. |
| **Monitor** | Relevant but no immediate action. Review when conditions change. |
| **Disseminate** | Useful context for one or more owners, but no tracked action required. |
| **Create action** | Requires patching, configuration, detection, review, vendor follow-up, or project change. |
| **Create risk** | Residual exposure requires tracking through [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |

---

## 5. Relevance and Priority

Priority is based on relevance, exposure, exploitation, and potential impact. A dramatic threat report with no relationship to the environment is lower priority than a quiet advisory for a product the organization runs on the internet.

| **Priority** | **Criteria** | **Expected Handling** |
|---|---|---|
| **Critical** | Active exploitation against technology the organization uses, especially internet-facing, identity, OT, or Restricted-data systems. | Same-day owner notification; action or risk entry opened immediately. |
| **High** | Likely exploitation or high-impact technique affecting used technology, a key vendor, or a regulated environment. | Owner notification within one business day; tracked action opened. |
| **Medium** | Plausible relevance, limited exposure, or no known exploitation. | Disseminate to relevant owner; monitor or schedule action. |
| **Low** | General context, weak relevance, or awareness-only item. | Record if useful; no action required. |

Priority does not replace vulnerability severity or risk scoring. It informs them. Vulnerability remediation still follows [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md), and residual risk still follows [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

---

## 6. Products and Dissemination

The Threat Intelligence Analyst produces only products with a clear audience and decision purpose.

| **Product** | **Audience** | **Purpose** |
|---|---|---|
| Flash advisory | Engineering, Risk, Governance, CISO as needed | Time-sensitive item requiring immediate awareness or action. |
| Weekly intelligence digest | Risk and Engineering owners | Relevant trends, exploited vulnerabilities, sector activity, and follow-up reminders. |
| Threat-model input brief | Threat modeling participants | Actor, technique, and abuse-case context for design review. |
| Vulnerability context note | Vulnerability Management Lead | Exploitation status, weaponization, and prioritization context. |
| Vendor risk note | Vendor Risk Analyst | Supplier compromise, product vulnerability, or service-risk context. |
| Executive threat brief | CISO and Executive Sponsor | Material changes to threat exposure and decisions needed. |

Dissemination is targeted. Sending every item to everyone trains everyone to ignore the channel.

> **Broadcast Is Not Dissemination**
>
> Dumping every advisory into a shared chat is not a threat intelligence program. It is noise with timestamps. CERG dissemination names the audience, the decision, and the requested action. If the recipient cannot tell what to do with the intelligence, the message failed.

---

## 7. Action Tracking

Actionable intelligence is tracked to disposition. The Threat Intelligence Analyst does not necessarily do the remediation, but owns the intelligence-to-action handoff until the receiving owner accepts it.

| **Action Type** | **Receiving Owner** | **Tracking Path** |
|---|---|---|
| Patch or mitigate vulnerability | Vulnerability Management Lead | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md). |
| Change design or control requirement | Engineering Pillar Leader or relevant Engineering role | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) or relevant standard. |
| Add threat-model abuse case | Threat Intelligence Analyst | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md). |
| Reassess supplier | Vendor Risk Analyst | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). |
| Create or tune detection | Detection Engineer | Detection backlog governed by [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md). |
| Record residual exposure | Risk Register Owner | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |
| Brief leadership | Risk Pillar Leader | CISO dashboard or executive threat brief. |

An item is closed only when the receiving owner records disposition: completed, accepted risk, not applicable with reason, or superseded.

---

## 8. Integration With CERG Processes

Threat intelligence feeds the program through defined channels.

| **CERG Process** | **How Intelligence Feeds It** |
|---|---|
| Architecture review | Supplies threat context and abuse cases for design decisions. |
| Threat modeling | Supplies actor, technique, and campaign context. |
| Vulnerability management | Adds exploitation, weaponization, and environmental relevance to remediation priority. |
| Third-party risk | Identifies supplier compromise, vendor product vulnerabilities, and sector vendor campaigns. |
| Asset management | Helps identify crown-jewel systems and technologies under active targeting. |
| AI security | Tracks prompt-injection, model supply chain, and AI-service data-risk developments. |
| OT risk | Uses ICS-specific intelligence and ATT&CK for ICS where OT is in scope. |
| Risk register | Converts sustained exposure into tracked risk. |
| Metrics and reporting | Provides threat-context narrative for posture reporting. |

---

## 9. Metrics

Threat intelligence metrics measure relevance and action, not raw feed volume.

| **Metric** | **Why It Matters** |
|---|---|
| Actionable intelligence items received | Measures useful signal, not total noise. |
| Items closed as not relevant | Shows filtering discipline and source quality. |
| Time from receipt to owner notification for Critical and High items | Measures timeliness. |
| Percent of actionable items with assigned owner | Measures handoff quality. |
| Percent of actions closed by disposition | Measures follow-through. |
| Intelligence items feeding vulnerability priority | Shows connection to exposure reduction. |
| Intelligence items feeding threat models | Shows design-stage use. |
| Intelligence items resulting in risk-register entries | Shows residual exposure capture. |

---

## 10. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Threat Intelligence Responsibility** |
|---|---|
| **Risk Pillar Leader** | Accountable for this procedure and for intelligence quality, prioritization, and escalation. |
| **Threat Intelligence Analyst** | Operates the procedure; maintains sources; triages intelligence; produces intelligence products; tracks intelligence-to-action handoffs. |
| **Vulnerability Management Lead** | Consumes intelligence for vulnerability prioritization and remediation decisions. |
| **Adversarial Testing Lead** | Uses intelligence to shape adversarial validation scope and scenarios. |
| **Vendor Risk Analyst** | Consumes supplier and vendor intelligence; performs reassessment where needed. |
| **OT Risk Analyst** | Supplies and consumes OT and ICS threat intelligence. |
| **Detection Engineer** | Receives detection leads and maps intelligence to detection backlog where in scope. |
| **Engineering Pillar Leader** | Receives design and architecture-impacting intelligence and assigns relevant Engineering owners. |
| **Governance Pillar Leader** | Receives intelligence with compliance, audit, or executive reporting implications. |
| **Risk Register Owner** | Records sustained exposure or accepted residual risk from intelligence-driven findings. |
| **Chief Information Security Officer (CISO)** | Receives material threat briefings and makes program-level decisions based on intelligence. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Procedure** |
|---|---|---|
| NIST 800-53r5 | RA-3, RA-5, SI-5, PM-16 | Sections 3, 4, 5, 7, 8 |
| NIST CSF 2.0 | ID.RA, DE.CM | Sections 5, 7, 8 |
| MITRE ATT&CK | Adversary technique mapping | Sections 5, 6, 8 |
| MITRE ATT&CK for ICS | OT and ICS threat context | Sections 3, 8, 10 |
| CMMC L2 / NIST 800-171r3 | Risk assessment and flaw remediation support | Sections 5, 7, 8 |
| NERC-CIP | OT threat awareness and BES Cyber System implications | Sections 3, 8, 10 |
| SOX ITGC | Threat context for financially relevant systems | Sections 7, 8 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-TI-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Approved By** | Governance Pillar Leader (pending); CISO endorses |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to threat landscape or intelligence sources |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-53r5 (RA-3, RA-5, SI-5, PM-16); NIST CSF 2.0 (ID.RA, DE.CM); MITRE ATT&CK; MITRE ATT&CK for ICS |
| **Regulations** | CMMC L2 / 800-171r3; NERC-CIP; SOX ITGC where applicable |
| **Environments** | All CERG-managed environments and risk decisions informed by threat intelligence |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Risk | Initial release. Establishes source management, intake fields, triage outcomes, relevance-based prioritization, tailored intelligence products, action tracking, integration with CERG processes, metrics, and canonical role responsibilities for threat intelligence. |

### Review Triggers

- Material change to the organization's threat landscape
- Significant change to threat intelligence sources
- Significant incident showing an intelligence gap
- Change to vulnerability management, threat modeling, third-party risk, or risk-register processes
- Direction from the CISO

Cyber Risk owns this document. The Risk Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines Threat Intelligence Analyst role |
| Vulnerability Management Procedure | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | Consumes vulnerability intelligence |
| Threat Modeling Procedure | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Consumes threat actor and abuse-case context |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Consumes supplier and vendor intelligence |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Tracks residual risk from intelligence-driven findings |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Receives detection leads from intelligence |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `TI` domain |
