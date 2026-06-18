# Story 8: CERG Lite - Maria and the Tuesday scanner report

This story is for the CERG Lite team: 2-8 people running the Minimum Viable CERG (MVC) spine. Every other story in this directory assumes a Standard or Regulated team. Read [CERG-GOV-IMP-003](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) and [CERG-GOV-IMP-006](../../governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) before this story.

## Situation

Northwind Logistics is a 60-person regional distribution company. Last quarter the CEO told the IT Lead, Maria, that she "also owns security now" after the previous security contractor walked off mid-engagement. Maria has two people on her team: Devin (help desk and endpoint) and Priya (network and cloud). None of the three has held a dedicated security role before.

Six weeks ago Maria adopted the MVC. The [Cybersecurity Policy](../../governance/CERG-POL-001_Cybersecurity_Policy.md) is signed by the Executive Sponsor (the COO). Maria is CISO + Governance + Risk Register consolidated. Devin is Engineering Lead. Priya is Risk + Exposure Management + Vendor Risk consolidated. The first 10 records exist (per IMP-003 §5): profile, role assignment map, asset extract, top 10 risks, exposure backlog, exception register, evidence index, control snapshot, regulatory applicability, and 30-day improvement backlog. The first weekly 1-hour cadence meeting ran last Friday.

It is Tuesday at 8:07 a.m. The vulnerability scanner has finished its weekly run against the production subnet, the staging cloud tenant, and the four external IPs. Priya opens the export. There are 47 findings. Two are rated Critical.

## CERG flow pattern

Primary flow: [F-04 Finding to Remediation, Exception, or Residual Risk](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#12-flow-f-04-finding-to-remediation-exception-or-residual-risk)

Supporting procedures and standards:

- [Small Team Adoption Path](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) - the operating rhythm and role consolidation map for a 3-person team.
- [Role-Based Implementation Checklists](../../governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) - what each consolidated role does in week 1 through month 6.
- [Exposure Management Procedure](../../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) - the observe, validate, classify, treat, verify flow Priya runs.
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - how the two Critical findings move from Finding to Risk if SLA is missed.
- [Adoption Safety Guide](../../governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md) - role safety and decision log requirements for consolidated roles.
- [Risk Management Framework](../../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) - the severity-tiered SLA table and exception logic.
- [Evidence Quality Standard](../../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md) - what "evidence" means on a spreadsheet in a small team.

### How the three pillars collapse onto three people

| Pillar | Consolidated role at Northwind | Primary responsibilities today |
|---|---|---|
| Governance | Maria (also CISO) | Decision log, exception routing, evidence index, executive sponsor liaison |
| Risk | Priya | Triage the 47 findings, severity calls, SLA tracking, risk register updates |
| Engineering | Devin | Patch planning, change windows, asset ownership confirmation |

The collapse is intentional and recorded in the [Decision Log](../../governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md#4-the-decision-log) per IMP-002 §4. Maria is the only person who signs exceptions. Priya owns the scanner schedule and the risk register. Devin owns the change record. There is no fourth person to delegate to.

## Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Priya imports the 47 findings into the exposure backlog spreadsheet and tags each row with asset, severity, and SLA clock start. | Priya (Risk) | Exposure backlog (EVD rows) |
| 2 | Priya validates reachability and asset ownership for the two Critical findings. One is on the customer portal web server; the other is on a legacy SFTP endpoint that hosts a vendor integration. | Priya (Risk) | Triage notes in Finding Record |
| 3 | Priya checks whether public exploit code exists for either Critical CVE. Both have public exploits. Severity stays Critical. KEV-style override is unnecessary because the CVSS already classifies Critical, but Priya notes the active exploitation risk in the Finding Record. | Priya (Risk) | Triage notes |
| 4 | Devin confirms the customer portal web server is in his asset inventory and that the application owner (Operations Director) is named. The SFTP endpoint is owned by a vendor, not Devin - he routes that one back to Priya for vendor-side coordination. | Devin (Engineering) | Asset Record update; vendor question logged |
| 5 | Devin opens a Change Record for the customer portal patch. He coordinates a same-day maintenance window with the Operations Director. The Critical SLA is 48 hours per [RMF-001](../../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md); he has time, but only if the change goes today. | Devin (Engineering) | Change Record |
| 6 | For the SFTP endpoint, Priya opens a Third-Party Finding and sends the vendor the CVE details, asks for patch timeline, and references the contract SLA (vendor must patch Critical within 30 days). Priya creates an Exception Record with compensating monitoring (alerting on anomalous SFTP traffic) and the vendor patch date as the expiration. | Priya (Risk) | Third-Party Finding; Exception Record |
| 7 | Maria reviews both Criticals in the 20-minute risk slot during the next weekly meeting. She confirms the Critical SLA will be met on the portal (Devin's path) and approves Priya's Exception Record with the monitoring requirement. Maria logs the decision in the Decision Log per IMP-002 §4. | Maria (Governance / CISO) | Decision Log entry; approved Exception Record |
| 8 | After the maintenance window, Devin uploads patch output, the change ticket closure, and a service-validation screenshot. Priya rescans the asset and confirms closure. The Finding Record moves to Closed. | Devin (Engineering) + Priya (Risk) | Closed Finding Record |
| 9 | Priya leaves the remaining 45 findings in the exposure backlog with SLA clocks running. She flags the 11 High findings for the biweekly vulnerability SLA review. | Priya (Risk) | Updated exposure backlog |
| 10 | Maria updates the evidence index with two new rows: the Closed Finding for the portal, and the Exception Record for the SFTP endpoint. The monthly metrics refresh will pull these automatically next week. | Maria (Governance) | Evidence index entries |

### Narrative

At 8:07 a.m. Priya's email pings with the scanner export. She has been doing this every Tuesday for six weeks and has the spreadsheet template down. By 8:30 a.m. the two Critical findings are tagged, validated against the asset inventory, and routed. The portal finding goes to Devin. The SFTP finding goes back to Priya because the asset is vendor-owned.

Devin sees the portal Change Record in his queue at 8:45 a.m. He calls the Operations Director directly - the CERG escalation rule says a Critical SLA bypasses the normal change review queue. The Director approves a 2 p.m. maintenance window and reschedules a customer email blast so users hit the maintenance banner, not a blank page. Devin also applies a temporary WAF rule on the vulnerable path while the patch is prepared.

Maria joins for the weekly 1-hour meeting at 10 a.m. Priya walks through the two Criticals in her 20-minute slot. Maria approves the SFTP exception because the compensating monitoring is already in place and the vendor contract requires patch within 30 days. Maria adds one Decision Log entry: "Vendor-side Critical CVE accepted with monitoring until vendor patch date; expires 30 days from today." That single entry satisfies IMP-002 §4.

At 2:15 p.m. the maintenance window opens. Devin deploys the patch, validates the service, captures the validation screenshot, and closes the change ticket. Priya rescans at 3 p.m. The Critical is closed. The remaining exposure backlog carries the 45 other findings into the biweekly SLA review.

By the end of Tuesday, the team has produced:

- 1 closed Finding Record (portal Critical)
- 1 open Exception Record (SFTP Critical, with expiration date)
- 1 closed Change Record (portal patch)
- 1 Decision Log entry (Maria)
- 2 evidence index rows (one per Critical outcome)
- 11 High findings flagged for biweekly review

No one worked more than their usual hours. The scanner run took 23 minutes of Priya's time. Devin's engineering work was bounded by the 4-hour change window. Maria's governance overhead was 15 minutes in the weekly meeting plus the Decision Log entry.

### Operating under the 5-person rhythm

The MVC spine did not break under pressure. The weekly 1-hour cadence absorbed the Critical triage in Maria's 20-minute risk slot. The Decision Log made Maria's exception approval auditable without a separate meeting. The exposure backlog spreadsheet gave Priya a place to capture every finding without opening a ticket for each one.

The collapse of the three pillars onto three people is the central design constraint of CERG Lite, not a workaround. Maria is doing CISO, Governance, and Risk Register work in one head. Devin is doing Engineering and Identity work in one head. Priya is doing Risk, Exposure Management, Threat Intel (read-only), and Vendor Risk in one head. The MVC spine fits because the consolidated roles each get one seat at the weekly meeting, and the records are designed to be one-row-per-event in a spreadsheet.

If Northwind grows to 8 people in the next year, the team will deconsolidate. Maria will keep CISO and Governance. Priya will keep Risk and Exposure Management. They will add a dedicated Identity Engineer, a dedicated Compliance person, and two more Engineering roles. The records do not change. The RACI in [OM-001](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) does not change. The cadence expands from weekly 1-hour to weekly 2-hour with sub-pillar owners. That deconsolidation is the documented growth path in IMP-003 §4.

## Operational outputs

- 1 closed Finding Record for the customer portal Critical CVE.
- 1 open Exception Record for the SFTP Critical CVE, with compensating monitoring and expiration date.
- 1 closed Change Record linked to the portal patch.
- 1 Decision Log entry recording Maria's exception approval.
- 2 evidence index rows added (one per Critical outcome).
- 11 High findings flagged for the biweekly SLA review; remaining 34 findings left in the backlog with SLA clocks running.

## What this story does not cover

- **Internal IR declaration.** Northwind's IR owner is a contracted MSSP. The story does not walk through a real internal IR event because the MVC spine deliberately defers incident ownership to the standing IR team. See Story 6 for that.
- **Audit response.** Northwind is not yet regulated. When their largest customer requests a SOC 2 attestation in six months, Story 3 will be the right reference.
- **AI tooling.** Northwind is not yet piloting AI. When the Operations Director asks about an AI assistant for the customer service team, Story 7 will be the right reference.

For the 5-person operating rhythm used in this story, see [CERG-GOV-IMP-003 §3](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md#3-operating-rhythm-for-a-5-person-team). For the role consolidation map, see [CERG-GOV-IMP-003 §4](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md#4-role-consolidation-map).
