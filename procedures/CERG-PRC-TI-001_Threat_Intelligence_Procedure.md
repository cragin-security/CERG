# SURGE: Cyber Engineering, Risk & Governance

## THREAT INTELLIGENCE PROCEDURE
### Sources · Intake · Relevance · Dissemination · Action Tracking · Program Reprioritization · External Collaboration

---

| | |
|---|---|
| **Document ID** | CERG-PRC-TI-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) · [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [`CERG-PRC-LL-001`](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) · [`CERG-GOV-IMPREG-001`](../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) · [`CERG-GOV-CAL-001`](../governance/CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) |
| **Review Cycle** | Annual / On material change to threat landscape or intelligence sources |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (RA-3, RA-5, SI-5, PM-16) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.RA, DE.CM, ID.IM, GOVERN) · [MITRE ATT&CK](https://attack.mitre.org/) · [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) |
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
9. [Intelligence-Driven Program Reprioritization](#9-intelligence-driven-program-reprioritization)
10. [External Collaboration and Information Sharing](#10-external-collaboration-and-information-sharing)
11. [Metrics](#11-metrics)
12. [Roles and Responsibilities](#12-roles-and-responsibilities)
13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Scope

The README names threat intelligence as a Cyber Risk function. The Operating Model names the Threat Intelligence Analyst as the role that tracks threat actors, advisories, and intelligence-to-detection translation. Existing procedures consume threat intelligence, but no procedure defined how intelligence is sourced, triaged, prioritized, disseminated, or tracked to action. This procedure closes that gap.

Threat intelligence in CERG is operational. Its purpose is not to publish interesting reports. Its purpose is to help the organization make better decisions sooner: patch the right thing faster, change a design before it ships, warn the right owner, tune a detection, reassess a vendor, or record a risk.

This procedure applies to all threat intelligence used by CERG to inform exposure management, threat modeling, architecture review, third-party risk, OT risk, detection priorities, and risk-register decisions.

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

Restricted-source or sensitive intelligence is handled according to its classification under [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md).

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

### 4.4 Analysis Methodology

Raw intelligence is analyzed before dissemination. The following frameworks and standards ensure consistent, defensible analysis.

#### Analysis Frameworks

| **Framework** | **Application** | **Description** |
|---|---|---|
| Diamond Model | Intrusion analysis | Maps adversary, capability, infrastructure, and victim for each intrusion event. Used to identify adversary campaigns and infrastructure patterns. |
| Intelligence Cycle | Production workflow | Planning → Collection → Processing → Analysis → Dissemination → Feedback. Each intelligence product follows this cycle. |
| Kill Chain Analysis | Attack reconstruction | Maps observed activity to Recon → Weaponization → Delivery → Exploitation → Installation → C2 → Actions. Used to identify where defenses failed or succeeded. |

#### Confidence Levels

Every intelligence product includes a confidence assessment:

| **Confidence** | **Definition** | **Criteria** |
|---|---|---|
| Confirmed | Independently corroborated by multiple reliable sources | ≥ 3 corroborating sources; no conflicting information |
| Probable | Supported by reliable sources with minor gaps | 2 corroborating sources or 1 highly reliable source |
| Possible | Plausible but single source or limited corroboration | 1 source of moderate reliability; limited supporting evidence |
| Unlikely | Contradicted by more reliable information | Primary source contradicted; low reliability |
| Doubtful | Highly improbable based on available information | Single low-reliability source; significant contradicting evidence |

#### Source Reliability Assessment

| **Rating** | **Definition** |
|---|---|
| A - Completely Reliable | History of complete reliability; no doubt of authenticity |
| B - Usually Reliable | Minor doubts; history of valid information with occasional errors |
| C - Fairly Reliable | Some doubts; information used but not confirmed through other sources |
| D - Not Usually Reliable | Significant doubts; information used only when corroborated |
| E - Unreliable | History of invalid information; not used |
| F - Cannot Be Judged | No basis for reliability assessment |

The Threat Intelligence Analyst assesses both confidence in the analyzed intelligence and reliability of the source. Products clearly state the confidence level and source reliability rating.

---

### 4.5 IOC Lifecycle Management

Indicators of Compromise (IOCs) have a lifecycle from ingestion through deployment to retirement.

#### IOC Confidence Scoring

| **Score** | **Criteria** |
|---|---|
| High | Confirmed malicious by ≥ 2 independent sources; observed in production attacks |
| Medium | Reported by a trusted source; limited independent confirmation |
| Low | Single report; unverified; or context-dependent (e.g., IP that is also used legitimately) |

#### IOC Expiration

IOCs auto-expire after 90 days unless refreshed. The Threat Intelligence Analyst reviews expiring IOCs and either:
- Refreshes: IOC is still active and confirmed; expiration clock resets
- Retires: IOC is no longer active, has been remediated, or is no longer relevant

Expired IOCs are removed from active detection tooling but retained in the intelligence archive for historical analysis.

#### False Positive Management

| **Step** | **Action** |
|---|---|
| 1 | Detection Engineer identifies a false positive IOC (alert fires on benign activity) |
| 2 | IOC is suppressed in detection tooling with a note and timestamp |
| 3 | Threat Intelligence Analyst reviews within 5 business days |
| 4 | If confirmed false positive: IOC is retired with rationale. If disputed: IOC remains active; detection rule is tuned instead |

False positive rate is tracked as a metric. A sustained false positive rate > 20% on any IOC source triggers a source quality review.

#### Integration with Detection Tooling

IOCs are deployed to detection tooling (SIEM, EDR, NGFW) through an automated or semi-automated pipeline. IOC retirement is synchronized: when an IOC is retired in the intelligence platform, it is automatically removed from detection tooling within 24 hours.

---

## 5. Relevance and Priority

Priority is based on relevance, exposure, exploitation, and potential impact. A dramatic threat report with no relationship to the environment is lower priority than a quiet advisory for a product the organization runs on the internet.

| **Priority** | **Criteria** | **Expected Handling** |
|---|---|---|
| **Critical** | Active exploitation against technology the organization uses, especially internet-facing, identity, OT, or Restricted-data systems. | Same-day owner notification; action or risk entry opened immediately. |
| **High** | Likely exploitation or high-impact technique affecting used technology, a key vendor, or a regulated environment. | Owner notification within one business day; tracked action opened. |
| **Medium** | Plausible relevance, limited exposure, or no known exploitation. | Disseminate to relevant owner; monitor or schedule action. |
| **Low** | General context, weak relevance, or awareness-only item. | Record if useful; no action required. |

Priority does not replace vulnerability severity or risk scoring. It informs them. Vulnerability remediation still follows [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md), and residual risk still follows [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

---

## 6. Products and Dissemination

The Threat Intelligence Analyst produces only products with a clear audience and decision purpose.

| **Product** | **Audience** | **Purpose** |
|---|---|---|
| Flash advisory | Engineering, Risk, Governance, CISO as needed | Time-sensitive item requiring immediate awareness or action. |
| Weekly intelligence digest | Risk and Engineering owners | Relevant trends, exploited vulnerabilities, sector activity, and follow-up reminders. |
| Threat-model input brief | Threat modeling participants | Actor, technique, and abuse-case context for design review. |
| Vulnerability context note | Exposure Management Lead | Exploitation status, weaponization, and prioritization context. |
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
| Patch or mitigate vulnerability | Exposure Management Lead | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md). |
| Change design or control requirement | Engineering Pillar Leader or relevant Engineering role | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) or relevant standard. |
| Add threat-model abuse case | Threat Intelligence Analyst | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md). |
| Reassess supplier | Vendor Risk Analyst | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). |
| Create or tune detection | Detection Engineer | Detection backlog governed by [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md). |
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
| Exposure management | Adds exploitation, weaponization, and environmental relevance to remediation priority. |
| Third-party risk | Identifies supplier compromise, vendor product vulnerabilities, and sector vendor campaigns. |
| Asset management | Helps identify crown-jewel systems and technologies under active targeting. |
| AI security | Tracks prompt-injection, model supply chain, and AI-service data-risk developments. |
| OT risk | Uses ICS-specific intelligence and ATT&CK for ICS where OT is in scope. |
| Risk register | Converts sustained exposure into tracked risk. |
| Metrics and reporting | Provides threat-context narrative for posture reporting. |

---

## 9. Intelligence-Driven Program Reprioritization

Threat intelligence that is collected, triaged, and disseminated but never changes the program is a reporting exercise, not an Adaptive capability. The CERG Framework (FRM-001 Section 6.2) states that "Threat intelligence actively shapes Engineering design decisions and Governance policy priorities." An Adaptive assessor expects to see evidence that intelligence has actually changed the program, not just informed it.

This section defines the quarterly cadence and decision framework by which intelligence drives program-level reprioritization.

### 9.1 Quarterly Threat Landscape Assessment

Once per quarter, aligned with the CERG leadership review cadence (GOV-CAL-001 Section 5), the Risk Pillar Leader presents a Threat Landscape Assessment to the CISO and pillar leaders. The assessment is a structured briefing, not a raw intelligence dump.

The assessment covers:

- **Top 3 threat actors** targeting the organization's sector, with observed TTPs and campaign context
- **TTP changes** observed in the last quarter that differ from the prior assessment
- **Changes in targeting patterns:** are new sectors, technologies, or organization types being targeted?
- **Vulnerabilities actively exploited in the wild** (CISA KEV or vendor-confirmed exploitation), with mapping to CERG assets
- **Intelligence gaps identified:** what should CERG know about the threat landscape that it does not currently know?
- **External incident impact assessment:** any major breach at a peer or in-sector organization, with implications for CERG

### 9.2 Reprioritization Decision Framework

The assessment MUST produce at least one of the following reprioritization decisions, each recorded with rationale in the improvement register (IMPREG-001):

| Decision | Trigger Condition | Example |
|---|---|---|
| **No program change** | Current posture is adequate for the assessed threat landscape. | Must state specifically why : not "we are fine" but "our current network segmentation (STD-NET-001 Section 5) blocks the lateral movement technique observed in the campaign." |
| **Control baseline adjustment** | A new TTP or exploitation pattern is not addressed by the current control baseline. | "Ransomware groups are now exploiting RMM tools for initial access. Proposed: add a CB-001 control requiring RMM tool inventory and approved-tool policy." |
| **Project intake priority shift** | A class of project or technology now carries elevated risk. | "API-first architectures are being targeted. Proposed: elevate API gateway projects to mandatory architecture review." |
| **Detection rule update** | Observed TTPs are not covered by current detection rules. | "The campaign uses a specific LOLBin chain not in our detection set. Proposed: add detection rules for the observed chain." |
| **Tooling or capability gap** | The threat landscape requires a capability CERG does not currently have. | "Adversaries are abusing OAuth token attacks at scale. Proposed: evaluate OAuth threat detection tooling." |
| **Staffing or training recommendation** | A sustained threat pattern requires specialized expertise. | "ICS-targeting activity has increased 300% year-over-year. Proposed: add an OT Threat Analyst position." |
| **External sharing action** | Intelligence is relevant to an ISAC, peer group, or regulator. | "Observed novel ICS technique. Proposed: share sanitized TTP with E-ISAC." |

> **The "No Change" Decision Requires Proof**
>
> "No program change" is a valid output of the quarterly assessment, but it must be a deliberate conclusion with specific rationale, not a default. An assessor reviewing two years of quarterly assessments where every single one concluded "no change needed" will correctly conclude either that the intelligence program is not producing actionable intelligence or that the program is not listening to it. Both conclusions are Adaptive-fatal.

### 9.3 Decision Record

Each reprioritization decision is recorded in the improvement register (IMPREG-001) with:

- Source: "Intelligence-Driven Reprioritization, QN YYYY"
- The intelligence trigger (specific threat actor, TTP, campaign, or vulnerability)
- The decision and accountable role
- A verification checkpoint (reviewed at the next quarterly assessment)

### 9.4 Verification

At each quarterly assessment, the prior quarter's reprioritization decisions are verified:

- Was the control adjusted? Is the new or modified control in CB-001?
- Was the detection rule deployed? Is it producing alerts?
- Was the capability gap funded? Is the tool procured or the hire in progress?
- Incomplete actions are escalated to the CISO.

Verification outcomes (Effective, Partially Effective, Ineffective) are recorded in IMPREG-001 per the improvement lifecycle.

### 9.5 Integration with Lessons Learned

The quarterly Threat Landscape Assessment is an intake source for the Lessons Learned procedure (PRC-LL-001). Intelligence-driven patterns that persist across multiple quarters are analyzed alongside incident, audit, and adversarial validation patterns at the quarterly Lessons Aggregation Review.

---

## 10. External Collaboration and Information Sharing

Adaptive maturity expects bidirectional information sharing : not just consuming threat intelligence, but contributing back, participating in communities, and learning from peers' incidents. This section defines the external collaboration requirements for CERG.

### 10.1 ISAC / ISAO Membership

CERG must maintain membership in at least one sector-appropriate Information Sharing and Analysis Center (ISAC) or Information Sharing and Analysis Organization (ISAO). For organizations with IT and OT footprints, dual membership in the sector IT ISAC and E-ISAC (electricity) or equivalent OT ISAC is recommended.

| Requirement | Detail |
|---|---|
| Minimum participation | Attend quarterly member calls and respond to Requests for Information (RFIs) within the ISAC's published SLA |
| Designated liaison | Threat Intelligence Analyst or Risk Pillar Leader |
| Escalation | Material intelligence received through ISAC channels follows the same triage and prioritization as Section 4-5 |

### 10.2 Peer Benchmarking

At least annually, the Threat Intelligence Analyst collects and analyzes peer benchmarking data where available.

Sources include:
- ISAC member threat reports and statistics
- Industry surveys (DBIR, SANS, sector-specific reports)
- Regulatory aggregate data where published
- Trusted peer exchanges

The benchmarking analysis compares CERG's posture against peer norms:
- Vulnerability closure rates compared to sector peers
- Incident frequency and type compared to sector peers
- Control coverage compared to recommended sector baselines

Significant deviations from peer norms trigger a program review. Example: if peer organizations close Critical vulnerabilities in a mean of 30 days and CERG's mean is 90 days, the gap must be explained and either accepted with rationale or converted to an improvement action.

### 10.3 External Incident Learning

When a major breach at a peer or in-sector organization is publicly reported, CERG conducts a structured External Incident Review within 14 calendar days. The review is led by the Threat Intelligence Analyst with participation from the affected pillar.

The review answers four questions:

1. **Could this happen here?** Does the affected technology, configuration, vendor, or process exist in CERG's environment?
2. **Are the relevant controls present and effective?** Map the attack chain to CERG's control baseline (CB-001). Are all relevant controls Implemented? Have their effectiveness metrics (CEF-001) been measured?
3. **What would our detection and response look like?** If the same attack chain were executed against CERG, would it be detected? Would the response be effective?
4. **What changes, if any, are warranted?** The output is either:
   - "No change needed" with specific rationale (e.g., "the affected technology is not deployed; the attack vector is blocked by STD-NET-001 Section 5")
   - An improvement register entry (IMPREG-001) for each warranted change

### 10.4 Community Contribution

At least annually, CERG contributes back to the ISAC or security community. Minimum contribution: sanitized lessons learned, threat observations, or control effectiveness data. This is both an Adaptive indicator in NIST CSF assessments and a professional obligation.

Acceptable contributions include:
- Sanitized incident lessons (what happened, what worked, what did not : without attribution or sensitive detail)
- Novel threat observations or TTPs
- Control effectiveness insights ("we found that control X was consistently ineffective in Y scenario")
- Tool or technique evaluations

### 10.5 Information Sharing Boundaries

Not everything can be shared. Before any external contribution, the following classification rules apply:

| Classification | Sharing Rule |
|---|---|
| Sanitized, non-attributable observations | Share freely with ISAC / peer groups |
| Specific vulnerabilities before remediation | Do not share externally until remediated |
| Customer, patient, or citizen data | Never share; regulated |
| Attorney-client privileged material | Never share without legal review |
| Competitive or business-strategy information | Never share |
| Incident details during active incident | Share only with official response partners (ISAC, CISA, law enforcement as appropriate) |

When in doubt, the CISO and legal counsel review before sharing.

---

### 10.6 Traffic Light Protocol (TLP) Handling

CERG uses the Traffic Light Protocol (TLP) for all intelligence sharing with external partners, ISACs, and industry groups.

| **TLP Level** | **Definition** | **Handling Requirement** |
|---|---|---|
| TLP:RED | For the eyes and ears of named recipients only; no further distribution | Not shared beyond named recipients. Stored with access restricted to the Threat Intelligence Analyst and named recipients. Not included in any wider-distribution product. |
| TLP:AMBER | Limited distribution within the organization and named partners | May be shared within CERG and with named partner organizations on a need-to-know basis. Not posted on publicly accessible platforms. Products containing TLP:AMBER information are clearly marked. |
| TLP:GREEN | Distribution within the community | May be shared with peer organizations, ISAC members, and trusted partners within the same sector or community. Not released publicly. |
| TLP:CLEAR | Unlimited distribution | May be shared freely. No restrictions on distribution. |

#### TLP Marking

Every intelligence product that contains TLP-classified information is marked with the highest applicable TLP level. The marking appears in the product header. When a product combines intelligence from multiple TLP sources, the most restrictive level applies.

#### Source TLP Compliance

The Threat Intelligence Analyst ensures that intelligence received under a TLP designation is handled per that designation. Intelligence received as TLP:RED is never sourced in a TLP:AMBER or lower product. Intelligence received under Chatham House Rule is paraphrased and not attributed to a specific organization or individual.

---

### 10.7 Consumer Feedback Loop

Intelligence products are assessed by the consumers who use them. This feedback loop drives continuous improvement in intelligence production.

#### Feedback Mechanism

| **Mechanism** | **Description** |
|---|---|
| Product rating | Recipients of intelligence products are invited to rate each product on usefulness (1–5) and accuracy (1–5) |
| Structured feedback | Quarterly, the Threat Intelligence Analyst solicits feedback from the top 5 consumers of intelligence products (e.g., Exposure Management Lead, Vendor Risk Analyst, Detection Engineer, CISO) |
| Ad-hoc feedback | Any consumer may provide feedback at any time through the intelligence intake channel |

#### Feedback Review Process

The Threat Intelligence Analyst reviews all feedback quarterly:
- Products rated < 3 on usefulness are analyzed: was the wrong audience targeted? Was the analysis insufficient? Was the timing poor?
- Products rated < 3 on accuracy are re-examined; if confirmed inaccurate, a correction is issued and the source reliability rating is adjusted
- Patterns in feedback inform source selection, product format changes, and dissemination list adjustments

#### Program Improvements from Feedback

Feedback that identifies a systematic gap in intelligence production (e.g., "we consistently lack context on vulnerabilities affecting our tech stack" or "the weekly digest is too long to read") is routed to the improvement register per [CERG-PRC-LL-001](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md).

---

## 11. Metrics

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

## 12. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Threat Intelligence Responsibility** |
|---|---|
| **Risk Pillar Leader** | Accountable for this procedure and for intelligence quality, prioritization, and escalation. |
| **Threat Intelligence Analyst** | Operates the procedure; maintains sources; triages intelligence; produces intelligence products; tracks intelligence-to-action handoffs. |
| **Exposure Management Lead** | Consumes intelligence for vulnerability prioritization and remediation decisions. |
| **Adversarial Testing Lead** | Uses intelligence to shape adversarial validation scope and scenarios. |
| **Vendor Risk Analyst** | Consumes supplier and vendor intelligence; performs reassessment where needed. |
| **OT Risk Analyst** | Supplies and consumes OT and ICS threat intelligence. |
| **Detection Engineer** | Receives detection leads and maps intelligence to detection backlog where in scope. |
| **Engineering Pillar Leader** | Receives design and architecture-impacting intelligence and assigns relevant Engineering owners. |
| **Governance Pillar Leader** | Receives intelligence with compliance, audit, or executive reporting implications. |
| **Risk Register Owner** | Records sustained exposure or accepted residual risk from intelligence-driven findings. |
| **Chief Information Security Officer (CISO)** | Receives material threat briefings and makes program-level decisions based on intelligence. |

---

## 13. Regulatory and Framework Alignment Summary

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


---

## Appendix A: Intelligence Product Templates

### A.1 Flash Advisory

```
FLASH ADVISORY - TI-YYYY-NNNN
TLP: [AMBER / GREEN]
Date: [date]
Priority: [CRITICAL / HIGH / MEDIUM]

Title:
Summary: [one paragraph - what happened, what to do]

Affected Technology: [vendor, product, version]
Recommended Actions:
  1. [action]
  2. [action]

IOCs (Confidence: [High/Medium/Low]):
  - [type]: [value]

ATT&CK Mapping: [technique IDs]
Source: [source type, reliability rating]
Analyst: [name]
```

### A.2 Weekly Digest

```
WEEKLY THREAT DIGEST - TI-WD-YYYY-WNN
TLP: GREEN
Period: [start] to [end]

Key Developments:
  1. [development]
  2. [development]

New IOCs: [count] - [summary of types]
Upcoming Threats: [what to watch for in the next 7 days]
Recommended Reading: [links to relevant advisories, reports]
Analyst: [name]
```

### A.3 Threat Model Input Brief

```
THREAT MODEL INPUT BRIEF - TI-TM-YYYY-NNNN
TLP: AMBER
System: [system name]
Architecture Review: [AR-YYYY-NNNN]

Threat Actors in Scope:
  | Actor | Capability | Relevance |
  |---|---|---|
  | | | |

Relevant TTPs:
  | TTP | Description | Relevance to System |
  |---|---|---|
  | | | |

Relevant CVEs (last 90 days):
  | CVE | CVSS | Affected Product | Exploit Available? |
  |---|---|---|---|
  | | | | |

Recommended Abuse Cases:
  1. [abuse case]
  2. [abuse case]

Analyst: [name]
```

### A.4 Vulnerability Context Note

```
VULNERABILITY CONTEXT NOTE - TI-VC-YYYY-NNNN
TLP: GREEN
Date: [date]
CVE: [CVE-ID]
CVSS: [score]

Exploit Status:
  [ ] Not observed in wild
  [ ] PoC available
  [ ] Actively exploited

Affected Assets (from CMDB): [list or "None identified"]
Recommended Priority: [Immediate / 72hr / 30-day / Patch-cycle]
Context: [why this matters to the organization]
Analyst: [name]
```

### A.5 Vendor Risk Note

```
VENDOR RISK NOTE - TI-VR-YYYY-NNNN
TLP: AMBER
Date: [date]
Vendor: [name]
Vendor Tier: [T1/T2/T3]

Finding: [description of threat intelligence]
Risk Implication: [what this means for the organization's use of this vendor]
Recommended Action: [specific action for Vendor Risk Analyst]
Related: [CERG-PRC-TPRM-001 reference]
Analyst: [name]
```

### A.6 Executive Threat Brief

```
EXECUTIVE THREAT BRIEF - TI-EX-YYYY-QN
TLP: AMBER
Period: [quarter] [year]

Top Threats:
  1. [threat] - [impact to organization] - [likelihood]
  2. [threat] - [impact] - [likelihood]
  3. [threat] - [impact] - [likelihood]

Program Impact: [how the threat landscape affects CERG program priorities]
Recommended Decisions: [specific decisions for CISO/executive consideration]
Analyst: [name]
Reviewer: [CISO]
```

## 14. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-TI-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Effective Date** | 2026-05-26 |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to threat landscape or intelligence sources |
| **Next Scheduled Review** | 2027-05-26 |
| **Frameworks** | NIST 800-53r5 (RA-3, RA-5, SI-5, PM-16); NIST CSF 2.0 (ID.RA, DE.CM, ID.IM, GOVERN); MITRE ATT&CK; MITRE ATT&CK for ICS |
| **Regulations** | CMMC L2 / 800-171r3; NERC-CIP; SOX ITGC where applicable |
| **Environments** | All CERG-managed environments and risk decisions informed by threat intelligence |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Risk | Initial release. Establishes source management, intake fields, triage outcomes, relevance-based prioritization, tailored intelligence products, action tracking, integration with CERG processes, metrics, and canonical role responsibilities for threat intelligence. |
| 1.1 Draft | 2026-05-26 | Cyber Risk | Added Section 9 (Intelligence-Driven Program Reprioritization): quarterly threat landscape assessment, reprioritization decision framework, decision record, verification, and integration with lessons learned. Added Section 10 (External Collaboration and Information Sharing): ISAC/ISAO membership requirements, peer benchmarking, external incident learning, community contribution, and information sharing boundaries. Renumbered subsequent sections. Updated supporting documents to include PRC-LL-001, IMPREG-001, and GOV-CAL-001. Addresses NIST CSF Adaptive gaps in intelligence-driven program change and bidirectional information sharing. |

### Review Triggers

- Material change to the organization's threat landscape
- Significant change to threat intelligence sources
- Significant incident showing an intelligence gap
- Change to exposure management, threat modeling, third-party risk, or risk-register processes
- Direction from the CISO

Cyber Risk owns this document. The Risk Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines Threat Intelligence Analyst role |
| Exposure Management Procedure | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Consumes vulnerability intelligence |
| Threat Modeling Procedure | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Consumes threat actor and abuse-case context |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Consumes supplier and vendor intelligence |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Tracks residual risk from intelligence-driven findings |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Receives detection leads from intelligence |
| Lessons Learned and Program Improvement Procedure | [`CERG-PRC-LL-001`](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) | Intelligence assessments feed the quarterly aggregation |
| Program Improvement Register | [`CERG-GOV-IMPREG-001`](../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) | Records intelligence-driven program changes |
| Annual Security and Governance Calendar | [`CERG-GOV-CAL-001`](../governance/CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) | Aligns quarterly assessment cadence |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `TI` domain |
