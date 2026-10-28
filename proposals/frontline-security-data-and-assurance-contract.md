# Frontline Security Data-and-Assurance Contract

### Proposal · Request catalog supporting the frontline operating model

| | |
|---|---|
| **Proposal reference** | FLA-PROPOSAL-002 |
| **Status** | Proposed — not approved framework content |
| **Owner** | cragin-security |
| **Date** | 2026-10-27 |
| **Classification** | Public |
| **Scope** | Per-engagement instrument; request rows are tailored to the client's registered scope |
| **Source state** | Depends on `experiment/second-line-model-implementation` at `7a74768` — not present in this fork's `main` |
| **Companion documents** | [Frontline Security Assurance Operating Model](frontline-security-assurance-operating-model.md) · [RMF-001](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) · [PLN-CIP-001](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) |

> **Proposal status.** This document carries no CERG document identifier and is not registered
> in the document catalog. It is a candidate contribution to the framework, not normative
> content. Cite it as a draft in proposals and statements of work until it is accepted.

> **Source state.** Written against the second-line experiment rather than against this
> repository's corpus. The conditions, the state-authorship rule, the owner/operator split,
> the `PRC-VM-001` §4.1 re-owning and the `TMPL-SCP-001` service interface block live on
> `experiment/second-line-model-implementation` at `7a74768` and are **not** in this fork's `main`. A reader here will therefore find a
> proposal describing a model the local corpus does not yet implement. That is expected and
> is why this document is non-normative. Re-verify cross-references if the experiment merges.

## Purpose

A structured set of requests (outcomes, not procedures) from second-line cybersecurity to
first-line IT/OT operations teams managing NERC CIP and broader security controls. Each entry
defines what is needed, from where, how often, in what format, and how completeness is
verified. This replaces ad-hoc "please be CIP compliant" requests with a repeatable contract.

---

## Standing Rules (apply to every request)

1. **Named accountable owner.** Every asset, finding, exception, and remediation action needs
   a business/system owner AND an operational support owner.

2. **Authoritative source defined.** Each data element has one authoritative tool. A scanner
   discovers an asset; the CMDB owns its classification and owner. Disagreements resolve to
   the authoritative source per the table below.

3. **Machine-readable delivery preferred.** API feed > dashboard with export > CSV on
   schedule > manual spreadsheet. Screenshots and ad-hoc email are not acceptable for
   recurring requests.

4. **Point-in-time + freshness metadata.** Every submission includes:
   - Extraction date/time and timezone
   - Source system and version
   - Coverage percentage and known blind spots (e.g., "98% of CMDB assets; site XYZ excluded")
   - Source record count

5. **Stable identifiers.** Use CMDB asset IDs and standardized finding IDs so second line can
   trend remediation without matching on hostnames.

6. **Exception discipline.** "Unable to patch" is not a final status. It requires:
   - Compensating control description and validation evidence
   - Documented risk acceptance with business owner and security approver
   - Expiry date
   - Replacement/remediation plan with funded target date

7. **Escalation thresholds.** See definitions below. Do not wait for the periodic report if
   the threshold is met.

8. **Evidence retention.** Records retained per the CIP evidence retention schedule for the
   applicable standard version. Storage location and format documented.

---

## Definitions

### Immediate Notification Thresholds

These events require notification to second-line cybersecurity within the stated window,
regardless of the periodic reporting cadence:

Event | Notification window | Method
Active exploitation or confirmed CVE with known exploitation on crown-jewel asset | Within 1 hour | Phone + email + ticket
Loss of endpoint protection (EDR/AV) on any crown-jewel asset lasting >4 hours | Within 2 hours | Email + ticket
Unapproved external-facing service or port opened on ESP-boundary device | Within 2 hours | Email + ticket
Failed backup on crown-jewel asset past RPO threshold | Within 4 hours | Email + ticket
Material segmentation failure (cross-ESP traffic that violates approved flows) | Within 2 hours | Email + ticket
Privileged credential compromise or suspected PAM bypass | Within 1 hour | Phone + email + ticket
Unauthorized physical access to ESP | Within 1 hour | Phone + email
Vendor/supplier security incident affecting hosted or supported crown-jewel systems | Within 4 hours | Email + ticket

### Material Change Definitions

These trigger "within 1 business day" reporting for applicable requests:

- Asset added to or removed from CIP scope
- Asset reclassified between ESP, LERC, or PACM environments
- Network architecture change affecting ESP boundaries or allowed data flows
- Authentication method change for privileged access to crown jewels
- Change in supported OS/firmware version for any crown-jewel asset
- Change in backup strategy, tool, or retention policy for crown jewels
- Addition, removal, or replacement of security tool (EDR, scanner, firewall, SIEM source)
- Vendor access change involving new systems, new personnel, or elevated privilege
- Physical security control change for any ESP (badge system, camera coverage, door lock)

### Remediation SLAs (minimum targets)

Severity | Remediation SLA | Exception path
Critical (CVSS 9.0-10.0, or actively exploited) | 7 calendar days | CISO-level risk acceptance required; compensating controls must be in place within 48 hours
High (CVSS 7.0-8.9) | 30 calendar days | Senior director-level risk acceptance
Medium (CVSS 4.0-6.9) | 90 calendar days | Business owner risk acceptance
Low (CVSS 0.1-3.9) | Next planned maintenance cycle | Tracked; no formal acceptance needed unless deferred >12 months

---

## Request Catalog

### Column key

- **Req'd fields:** Must be present for the submission to be accepted. Missing fields are
  rejected and trigger a follow-up within 1 business day.
- **Rec'd fields:** Should be included when available. Not required for acceptance, but
  tracked as a completeness metric.
- **Delivery:** P = Push (scheduled), Q = Query (dashboard/API), E = Event-driven
- **Effort:** L = Low (existing data, minimal transformation), M = Medium (automation
  required but achievable), H = High (significant manual work or tool gap)

---

### 1. Authoritative crown-jewel / BES asset inventory

| | |
|---|---|
| **Cadence** | Monthly; within 1 business day for material changes |
| **Req'd fields** | Unique asset ID (CMDB); hostname; IP address; asset type; environment (IT/OT/ESP/LERC/PACM); CIP applicability (yes/no with standard reference); criticality tier; system owner; support group; network zone; OS/firmware; lifecycle status (active/decom/out of support); last-seen date; CMDB record ID |
| **Rec'd fields** | MAC address; location (site/rack/coordinates); serial number; virtual/physical flag; hypervisor host; DNS domain; backup status; associated BC/DR plan ID |
| **Delivery** | P (CSV or API to GRC dashboard) |
| **Validation** | Record count within +/-5% of prior month; no duplicate asset IDs; all crown-jewel assets have non-null owner and support group |
| **Effort** | M |
| **Sources** | SAP/CMDB (authoritative for ownership); Industrial Defender, Nozomi, Armis, Xonius, Tanium (discovery cross-check) |

---

### 2. Inventory reconciliation and exceptions

| | |
|---|---|
| **Cadence** | Monthly |
| **Req'd fields** | Comparison of CMDB assets against active discovery, endpoint tools, vulnerability scanner, and network monitoring; unmatched assets (in CMDB not in tools, in tools not in CMDB); duplicates; stale records (no activity >90 days); disposition (add/remove/update) with owner; target resolution date |
| **Rec'd fields** | Reconciliation methodology (asset matching rules); false-positive log; asset ID cross-reference table |
| **Delivery** | P (CSV or API) |
| **Validation** | Unmatched count decreasing trend month-over-month; no unmatched crown-jewel assets older than one cycle |
| **Effort** | M |
| **Sources** | CMDB as baseline; Tenable, Tanium, SentinelOne, Nozomi, Armis, Xonius for discovery |

---

### 3. Asset classification and scope changes

| | |
|---|---|
| **Cadence** | Monthly report; immediately for scope changes |
| **Req'd fields** | New/removed/reclassified assets; rationale for change; approving authority; CIP applicability assessment (yes/no and which CIP standards apply); data classification; whether crown-jewel or supports one; effective date |
| **Rec'd fields** | Impact analysis for scope changes; change request ID; technical risk assessment reference |
| **Delivery** | P + E (event notification within 1 business day) |
| **Validation** | All scope changes have matching change ticket; classification drift detected when asset attributes change without reclassification |
| **Effort** | L |
| **Sources** | CMDB, GRC system, change management system |

---

### 4. Vulnerability posture for crown jewels and supporting infrastructure

| | |
|---|---|
| **Cadence** | Weekly; critical findings within 1 business day |
| **Req'd fields** | Asset ID (CMDB); CVE/plugin ID; severity (CVSS 3.x base and temporal); exploitation status (known exploited, proof of concept, remote/network/local); detection date and source; affected software and version; network exposure (internet-facing, ESP-facing, segmented); port/service; owner; remediation due date per SLA; status (open, in remediation, exception/risk-acceptance ID); ticket or finding ID |
| **Rec'd fields** | EPSS score; CISA KEV repository match; exploit maturity; vulnerability age at current severity; patch or configuration remediation option; impact on availability if patching requires downtime |
| **Delivery** | P (weekly) + E (critical findings within 1 business day) |
| **Validation** | Crown-jewel count matches monthly inventory +/-5%; zero critical findings past 7-day SLA; aging distribution reported (0-30, 31-60, 61-90, 90+ days) |
| **Effort** | M-H |
| **Sources** | Tenable, Industrial Defender, Nozomi, Armis, Xonius, Tanium, SentinelOne |

---


### 5. Vulnerability remediation performance and aging

| | |
|---|---|
| **Cadence** | Monthly |
| **Req'd fields** | Open findings count by severity, by age bucket (0-30, 31-60, 61-90, 90+ days), by asset class (crown-jewel, supporting, standard), by owner, by environment; overdue items (past SLA); remediation SLA performance percentage (closed within SLA / total closed) per month; approved exceptions with expiry dates |
| **Rec'd fields** | Mean time to remediate (MTTR) per severity; bottleneck analysis (waiting on vendor, downtime required, cannot remediate); trend (increasing/decreasing open findings) |
| **Delivery** | P |
| **Validation** | SLA performance trend non-declining; aging bucket 90+ days zero for crown jewels; exception expiry dates in future |
| **Effort** | M |
| **Sources** | Vulnerability management platform, ticketing system, GRC |

---

### 6. Patch and firmware compliance

| | |
|---|---|
| **Cadence** | Monthly; expedited reporting for actively exploited vulnerabilities |
| **Req'd fields** | Required patch/firmware bulletin or CVE; affected assets (CMDB IDs); current and target versions; deployment status (pending, staged, deployed, failed, rolled back); validation evidence (post-patch scan or tool confirmation); failed deployments with error detail; maintenance window reference; deferral reason; risk acceptance ID if applicable |
| **Rec'd fields** | Patch source (vendor, OEM, ICS-CERT); reboot required flag and impact; patch deployment chronology (start/end per asset); rollback procedure and test evidence |
| **Delivery** | P (monthly) + E (for actively exploited vulns within 24 hours) |
| **Validation** | Crown-jewel patch compliance percentage reported; critical/high patches past SLA flagged; failure rate trend reported; no crown-jewel asset >30 days behind on critical patches without documented exception |
| **Effort** | H |
| **Sources** | Tanium, endpoint management, OT patch management tools (e.g., Siemens, Rockwell vendor tools), change management system, vulnerability scanner post-patch verification |

---

### 7. Unsupported / end-of-life technology register

| | |
|---|---|
| **Cadence** | Monthly |
| **Req'd fields** | Product name and version; affected asset IDs (CMDB); vendor name; vendor support end date (general support and extended support); exposure risk (network-accessible, contains sensitive data, external-facing); business owner; compensating controls applied; replacement target product; replacement target date; risk acceptance ID and expiry |
| **Rec'd fields** | Estimated effort/cost to replace; procurement status; vendor extension or custom support contract status; known CVEs patched after EOL date |
| **Delivery** | P |
| **Validation** | All EOL assets have either a replacement plan with funded target date or a current risk acceptance; no new EOL assets added without comp control review; count per product trending down |
| **Effort** | L |
| **Sources** | CMDB (lifecycle status field), vendor records, vulnerability scanner (detected EOL software), procurement/purchasing system |

---

### 8. Endpoint security control coverage and health

| | |
|---|---|
| **Cadence** | Weekly; immediately on material outage (loss of coverage >4 hours on any crown jewel) |
| **Req'd fields** | Asset ID (CMDB); hostname; EDR product and version; AV product and version; definition/pattern file date; policy version loaded; last check-in timestamp; tamper protection status (on/off/altered); malware prevention status (active/degraded); exceptions (exclusion paths, approved deactivations); unprotected/unknown assets with reason |
| **Rec'd fields** | Disk encryption status (if applicable); firewall status (OS-based); last full scan date; suspicious detection count; software inventory checksum; USB/device control policy status |
| **Delivery** | P (weekly) + E (within 2 hours of detection of uncovered crown jewel) |
| **Validation** | Coverage percentage reported (crown-jewel and overall); zero missing check-in events from EDR agent on crown jewels; outlier assets (no check-in >7 days) flagged and assigned |
| **Effort** | L |
| **Sources** | SentinelOne, Tanium, CrowdStrike, endpoint management console |

---



### 9. Secure configuration / baseline compliance

| | |
|---|---|
| **Cadence** | Monthly; after major platform changes |
| **Req'd fields** | Baseline or control identifier; asset (CMDB ID); observed vs. required setting; compliance result (pass/fail/not applicable); exception reference; owner; remediation ticket ID; validation date. Include: local accounts, unnecessary services/ports, logging settings, time sync config, USB/removable-media controls as applicable per baseline |
| **Rec'd fields** | CIS/NIST benchmark version referenced; automated vs. manual assessment flag; deviation impact analysis; remediation or compensating control detail |
| **Delivery** | P |
| **Validation** | Crown-jewel baseline compliance percentage >= target (org-defined); critical deviations have remediation tickets with owners; no uncontrolled deviation older than two reporting cycles |
| **Effort** | H |
| **Sources** | Tanium, configuration management (Ansible, SCCM, Puppet), hardening tools (CIS-CAT, OpenSCAP), manual checklist for OT assets where automated checks are unavailable |

---

### 10. Firewall and network security posture

| | |
|---|---|
| **Cadence** | Monthly; before/after material changes affecting ESP boundaries |
| **Req'd fields** | Rule ID (firewall manager); source zone/IP; destination zone/IP; ports/protocols; ESP boundary flag; business purpose; application/system owner; approver; creation date; last review date; expiry date (for temporary rules); rule flags (unused, shadowed, permissive, risky) |
| **Rec'd fields** | Hit count; last match timestamp; rule change history; NAT rule mapping; implied permit analysis; risky service flags (e.g., RDP, SMB, SSH allowed from wide sources) |
| **Delivery** | P (monthly) + E (before/after ESP boundary changes) |
| **Validation** | Zero rules past review date without extension; unused rule count decreasing; no crown-jewel-facing allow-all rules; all temporary rules have expiry and an owner |
| **Effort** | M-H |
| **Sources** | Tufin, FireMon, firewall manager (e.g., Panorama, Cisco FMC), change management system |

---

### 11. Network segmentation and exposure validation

| | |
|---|---|
| **Cadence** | Quarterly; after architecture changes |
| **Req'd fields** | Approved data-flow diagram reference; actual allowed paths from firewall rules and ACLs; deviations from approved architecture; exposed management services (RDP, SSH, HTTPS) on ESP-boundary devices; remote-access paths (VPN, jump boxes, vendor access); unresolved findings with owner; test/validation date and method |
| **Rec'd fields** | Lateral movement path analysis; external attack surface discovery results (internet-facing assets); ESP bypass risk assessment; segmentation test methodology and coverage |
| **Delivery** | P (quarterly) + E (architecture changes trigger revalidation within 1 month) |
| **Validation** | All deviations have risk acceptance or plan to align; no unapproved cross-ESP flows; remote-access paths are limited to authorized jump hosts with MFA; findings decreasing trend |
| **Effort** | H |
| **Sources** | FireMon/Tufin data correlated with architecture repository; Nozomi passive network monitoring; firewall configs; vulnerability scanner external scope |

---

### 12. Privileged and remote-access review

| | |
|---|---|
| **Cadence** | Monthly for privileged access; quarterly for broader access |
| **Req'd fields** | Account ID or credential name; named owner (person or service ID); role or access purpose; target systems; privilege level (e.g., domain admin, local admin, read-only); authentication method (e.g., password, cert, smart card, MFA); MFA status; last use timestamp; manager or system-owner recertification date; terminated/transferred accounts removal check; exceptions with expiry |
| **Rec'd fields** | Service account vs. user account flag; shared account flag; password age; password complexity; last password rotation date; PAM-managed flag (e.g., CyberArk, Delinea); session recording status; approval ticket reference |
| **Delivery** | P |
| **Validation** | No privileged accounts without recertification within SLA; terminated/transferred accounts removed within 24 hours; service accounts have designated owners; no shared accounts on crown jewels without documented exception and PAM-managed passwords |
| **Effort** | M |
| **Sources** | IAM/PAM (e.g., CyberArk, Delinea, BeyondTrust), Active Directory, Azure AD, VPN/jump-host logs, server local-account audits |

---



### 13. Security logging and monitoring coverage

| | |
|---|---|
| **Cadence** | Monthly |
| **Req'd fields** | In-scope assets sending logs (CMDB ID, hostname); required log sources per asset (OS events, auth logs, firewall logs, application logs, EDR alerts); collector or SIEM destination; last event received timestamp; time-sync status (NTP configured, offset within tolerance); retention applied (e.g., 90 days, 12 months per CIP); monitoring use case assignment (e.g., login failures, malware detection, config change); gaps with remediation ticket ID and owner |
| **Rec'd fields** | Log volume trends (GB/day per source); compressed vs. uncompressed retention; log source version; parsing error rate; missing sources list; forwarding path redundancy |
| **Delivery** | P |
| **Validation** | Crown-jewel log source count matches inventory; zero gaps in crown-jewel coverage unresolved >30 days; time sync offset within tolerance on all crown jewels; no critical monitoring use case without a crown-jewel log source |
| **Effort** | M |
| **Sources** | SIEM (Splunk, Sentinel, Elastic/Security Onion), SentinelOne, Nozomi, syslog infrastructure, logging platform |

---

### 14. Security events, incidents, and near misses

| | |
|---|---|
| **Cadence** | Immediate notification under defined thresholds; monthly trend report |
| **Req'd fields** | Event/incident ID; affected assets (CMDB IDs); detection source (EDR, SIEM rule, firewall log, human report); time detected and time escalated; severity initial and updated; initial containment action; accountable owner; CIP-reportability assessment (reportable to NERC CIP? which standard?); root-cause analysis completion date; corrective actions and owners; lessons-learned reference |
| **Rec'd fields** | Incident classification (e.g., phishing, malware, unauthorized access, availability); kill-chain phase; IOCs extracted; evidence preserved location; regulatory reporting status; tabletop exercise cross-reference |
| **Delivery** | E (notification per threshold table) + P (monthly trend: count by type, severity, asset class, MTTR, repeat offenders, CIP-reportable count) |
| **Validation** | All threshold-triggering events have notification time within SLA; all confirmed incidents have RCA within 30 days; CIP-reportable events documented per standard; incident count/severity trend reported |
| **Effort** | L |
| **Sources** | SIEM/SOC platform, EDR console, ticketing/incident management, firewall logs |

---

### 15. Change management evidence for security-relevant changes

| | |
|---|---|
| **Cadence** | Monthly; pre-change notification for defined high-risk changes |
| **Req'd fields** | Change ID; affected crown-jewel assets; change type (patch, config, firmware, replacement, vendor access); risk assessment result (high/medium/low); CAB or security reviewer approval; implementation and rollback plan; test evidence (pre-change scan, functional test); post-change validation result (post-change scan, log check, connectivity test); configuration baseline updated flag; emergency change flag and rationale |
| **Rec'd fields** | Change window date/time; duration; stakeholder notification; test environment separation; peer review reference; outage window approval; impact on existing exceptions or risk acceptances |
| **Delivery** | P (monthly) + E (pre-notification for changes that materially affect security posture, ESP boundaries, or CIP scope) |
| **Validation** | All crown-jewel changes have pre/post change validation evidence; emergency changes have post-hoc review scheduled within 7 days; no crown-jewel change bypassed CAB review without approved emergency process; change failure rate trend reported |
| **Effort** | L |
| **Sources** | ITSM/change system (ServiceNow, Jira, Remedy), configuration management, validation scan results |

---

### 16. Backup, restoration, and recoverability assurance

| | |
|---|---|
| **Cadence** | Monthly status; at least annual restoration tests per system tier |
| **Req'd fields** | Backup success/failure status per crown-jewel asset; backup scope (full, incremental, differential, config backup, database); encryption status (at rest and in transit); retention tier and duration; immutable copy status (write-once-read-many, air-gapped); last restore test date per asset; RTO achieved vs. required; RPO achieved vs. required; gaps with corrective-action plan; business owner attestation of recovery priority |
| **Rec'd fields** | Backup tool; backup server location; replication target location; recovery-point mapping; recovery procedure document reference; tabletop vs. actual restore flag; DR plan reference |
| **Delivery** | P (monthly) + E (failed backup on crown jewel past RPO threshold triggers immediate notification) |
| **Validation** | Zero crown-jewel assets without verified backup; restore test schedule compliance per tier (annual minimum); backup failure rate trend non-increasing; restore test results achieving stated RTO/RPO; any gap has a corrective-action plan with owner and target |
| **Effort** | M |
| **Sources** | Backup/recovery tool (Veeam, Commvault, Avamar, Rubrik), DR plan repository, restore test reports |

---



### 17. Third-party / vendor connectivity and support access

| | |
|---|---|
| **Cadence** | Monthly summary; immediately before new vendor access is provisioned |
| **Req'd fields** | Vendor or third-party name; business/system owner; target systems (CMDB IDs); access method (VPN, jump host, direct connection); MFA status; approval reference (ticket, contract); access start and end date; monitoring/logging coverage on vendor sessions; inactive access last use >90 days flagged; contract or security-review status (passed, pending, expired) |
| **Rec'd fields** | Vendor support tier (T1-T3 escalation path); vendor personnel names and IDs; access restriction level (support-only session, config access, admin); non-disclosure or data-protection agreement reference; last access review date |
| **Delivery** | P (monthly) + E (new access approval notification within 2 business days of provisioning) |
| **Validation** | No vendor access without current contract and security review; no inactive vendor accounts >90 days without review; all crown-jewel vendor access session-logged; access terms and expiry date documented |
| **Effort** | M |
| **Sources** | PAM/VPN logs, CMDB, vendor management system (or contracts database), identity management |

---

### 18. Control exceptions and risk acceptances

| | |
|---|---|
| **Cadence** | Monthly |
| **Req'd fields** | Control or standard requirement reference (e.g., CIP-007 R2, internal baseline X); affected assets (CMDB IDs); risk statement (what is the risk and to what); compensating controls description and validation evidence; business owner (named); security approver (named); approval date; expiry date; remediation milestone plan with target dates; review status (active, expired, closed, pending renewal) |
| **Rec'd fields** | Original finding or deviation ticket ID; risk scoring (pre/post compensating controls); vulnerability age at time of acceptance; alternative remediation cost estimate; exception trend (same control, multiple assets) |
| **Delivery** | P |
| **Validation** | No expired exceptions without renewal or remediation action; all exceptions have compensating controls validated within the last review cycle; exception count trending down; no critical-severity exception older than 6 months without CISO-level re-review |
| **Effort** | L |
| **Sources** | GRC system (e.g., ServiceNow GRC, Archer, AuditBoard), risk register, ticketing system |

---

### 19. Data quality and attestation

| | |
|---|---|
| **Cadence** | Monthly |
| **Req'd fields** | Named frontline owner who attests to completeness and accuracy of submission; source system and extraction date/time; record counts for each report; known limitations (e.g., "3 field sites not reachable this cycle"); reconciliation results from Row 2; material changes since prior period; corrective actions for data quality gaps |
| **Rec'd fields** | Data retention policy reference; attestation method (manual sign-off, automated dashboard attest, audit log); completeness checklist (all rows submitted, all fields populated) |
| **Delivery** | P |
| **Validation** | On-time submission performance reported with the cause of any late submission; record count variance from the prior period explained and reconciled; no crown-jewel asset unaccounted for across all reports; gaps from prior month have corrective action owners and deadlines |
| **Effort** | L |
| **Sources** | All source systems (CMDB, vulnerability, endpoint, firewall, etc.), ticketing system, attestation log |

---



---

### ADDITIONAL PROPOSED ROWS

---

### 20. Removable media and portable device controls

| | |
|---|---|
| **Cadence** | Quarterly inventory; monthly exception updates |
| **Req'd fields** | Device type (USB drive, external HDD, laptop, tablet); serial number or identifier; assigned user or custodian; encryption status (enabled, none, unknown); data classification permitted; last scan date (malware scan); last inventory verification date; exceptions (policy waivers with expiry); loss or theft reporting status |
| **Rec'd fields** | Manufacturer; model; capacity; firmware version; purchase date; decommission date; associated crown-jewel data at rest flag; removable-media policy version |
| **Delivery** | P |
| **Validation** | All removable media inventoried; zero unencrypted devices with crown-jewel data; exception count trending down; loss/theft incidents reported per policy; removable-media inventory reconciled to issued-device records |
| **Effort** | L |
| **Sources** | Endpoint management (Tanium, SCCM, JAMF, Intune), DLP tool, manual inventory for OT air-gapped media, IT procurement records |

---

### 21. Personnel security and training currency

| | |
|---|---|
| **Cadence** | Monthly exceptions; quarterly completion rates |
| **Req'd fields** | Employee or contractor ID; role; current CIP training requirements; training completion dates; training expiry dates; background check date and status (complete, pending, not required); personnel risk assessment status (valid, expired, none required); exceptions (past-due training, expired background check, pending risk assessment) with owner and remediation date |
| **Rec'd fields** | Position risk tier; elevated-access privilege flag; security awareness training completion; role-based technical training completion; insider-risk monitoring flag; termination/transfer date for offboarded personnel |
| **Delivery** | P |
| **Validation** | No crown-jewel access without current training and background check; expired training resolved within 30 days; personnel risk assessment exceptions approved by security leadership; termination access revocation verified within 24 hours |
| **Effort** | L |
| **Sources** | HR system (Workday, PeopleSoft), Learning management system (LMS), IAM/PAM for access verification, personnel risk assessment database |

---

### 22. Physical security controls for ESPs and perimeters

| | |
|---|---|
| **Cadence** | Quarterly |
| **Req'd fields** | Physical perimeter ID; ESP or asset name; access control system (badge reader, keypad, mantrap); access control system online/offline status; CCTV coverage present (Y/N); CCTV retention applied; last visitor log audit date; last physical security test date (e.g., door-alarm test, intrusion test); exceptions (broken reader, camera blind spot, unlocked door) with owner and remediation date |
| **Rec'd fields** | Door sensor status; alarm system status; lock type (electronic, mechanical, both); entry/exit log retention period; tailgate detection; security guard post assignment; after-hours access procedure; key inventory and key-holder list |
| **Delivery** | P |
| **Validation** | All ESPs have working access control and CCTV; no unresolved physical security exception on crown-jewel ESP older than 30 days; periodic test schedule met; visitor logs retained per policy; alarm events reviewed within SLA |
| **Effort** | M |
| **Sources** | Physical access control system (Lenel, Genetec, Honeywell, AMAG), CCTV system, visitor management system (eVestigator, Envoy), manual inspection reports |

---

### 23. Software supply chain and vendor patch intake

| | |
|---|---|
| **Cadence** | Monthly |
| **Req'd fields** | Vendor/developer name; software product name and version; target deployment systems (CMDB IDs); software bill of materials (SBOM) availability (Y/N/not requested); known vulnerabilities at time of import (CVE IDs); vendor patch notification mechanism (email, portal, auto-update); vendor patch SLA (contracted response timeframe); responsible frontline team; exceptions (running software without SBOM, unpatched vendor software) |
| **Rec'd fields** | SBOM format (SPDX, CycloneDX); vulnerability scanning results pre-deployment; vendor security contact; contractual security requirements reference; vendor incident notification procedure; source/third-party dependency chain; open-source component license risk |
| **Delivery** | P |
| **Validation** | No new crown-jewel software deployment without SBOM where available; known-vulnerability acceptance at import approved by security; vendor patch SLA compliance tracked; software dependencies documented for crown-jewel applications |
| **Effort** | H |
| **Sources** | CMDB (software inventory), vulnerability scanner (software discovery), procurement/contract system, vendor management portal, GitLab/GitHub (for SBOM generation) |

---



---

## Friction Analysis: Where Frontline Will Push Back

This section is deliberately pragmatic — every item here is a prediction of friction based
on actual field experience. Use it to pre-negotiate, invest in automation, or adjust cadence
before the contract is delivered to frontline teams.

### Likely to trigger pushback (High friction)

**Row 6 (Patch and firmware compliance) — Effort H**
- Pain point: OT patching cycles, coordinated maintenance windows, vendor approval delays.
  A single firmware patch can be a multi-month project.
- Mitigation: Accept deferred patching only with comp controls and documented vendor
  coordination. Do NOT accept "waiting for window" as a permanent status.
- Watch for: "we patched" without post-patch scan evidence.

**Row 9 (Secure configuration / baseline compliance) — Effort H**
- Pain point: Manual checking on OT assets where automated tools don't exist or break things.
  Many OT devices have no local agent capability.
- Mitigation: Accept manual checklists with photographic or log evidence for OT assets
  where automation is impossible. Require a funded automation plan for repeat findings.
- Watch for: "all compliant" with no per-host evidence.

**Row 11 (Network segmentation and exposure validation) — Effort H**
- Pain point: Requires passive discovery, firewall config analysis, and architectural
  review. Often there is no single source of truth for "approved flows."
- Mitigation: Start with ESP boundaries only, expand to internal zones over three cycles.
- Watch for: Architecture diagrams that haven't been updated since initial deployment.

**Row 23 (Software supply chain and vendor patch intake) — Effort H**
- Pain point: SBOMs are not standard in OT vendor world. Many vendor contracts have no
  patch SLA or security notification requirement. This is a greenfield activity for most
  NERC CIP organizations.
- Mitigation: Start with a vendor inventory and SBOM availability assessment. Do NOT set
  SLA targets before assessing the current state.

### Moderate friction

**Row 5 (Vulnerability remediation performance and aging) — Effort M**
- Pain point: Aging reports require stable finding identifiers and cross-cycle tracking.
  Scanner re-scans may generate new finding IDs, breaking the aging trend.
- Mitigation: Require stable vulnerability instance IDs from the scanner. Validate trend
  reports by manually sampling 5 assets per cycle for the first three months.

**Row 10 (Firewall and network security posture) — Effort M-H**
- Pain point: Firewall rule inventories are huge (thousands of rules) and many rule purposes
  are undocumented. "Business purpose" field will be the biggest gap.
- Mitigation: Accept "legacy" business purpose tags for rules older than 2 years, but
  require new rules to have a filled business purpose. Require annual rule recertification.

**Row 17 (Third-party / vendor connectivity) — Effort M**
- Pain point: Vendor access is often managed outside IT/OT by procurement or engineering.
  Contractors come and go with loose coordination.
- Mitigation: Automate vendor-account provisioning via PAM tied to contract database, not
  manual spreadsheet.

**Row 22 (Physical security for ESPs) — Effort M**
- Pain point: Physical security is often managed by facilities or a separate security team,
  not the IT/OT frontline this contract targets. The request may land in the wrong team.
- Mitigation: Route this row to the facilities/security team directly, or designate a
  liaison.

### Low friction (already being done, may just need formalization)

**Rows 1-3 (Asset inventory, reconciliation, classification)** — These are already implicit
in CIP compliance. The request formalizes what is likely already done for audit evidence.

**Row 8 (Endpoint control coverage)** — EDR/AV dashboards already provide this data.
The ask is to export/push it to second line rather than just checking it locally.

**Row 14 (Security events and incidents)** — Already done if there is a SOC.
The ask is notification thresholds and monthly trends, which is a reporting formalization.

### Automation dependency map

These rows require automation investment to meet the stated cadence:

| Row | Current state (likely) | Target state | Investment needed |
|---|---|---|---|
| 4 (Vulnerability) | Manual export weekly | API feed to dashboard | Vuln tool API integration |
| 6 (Patch compliance) | Manual tracking per asset | Automated patch assessment | Tanium/SCCM + OT tool coverage |
| 8 (Endpoint health) | Dashboard-only visibility | API feed with drift alert | EDR API + alerting pipeline |
| 9 (Baseline compliance) | Manual spot checks | Automated scan + exception | CIS-CAT/OpenSCAP + OT baseline tool |
| 10 (Firewall rules) | Manual rule review | FireMon/Tufin automated audit | Rule management tool procurement |
| 13 (Logging coverage) | SIEM query per request | Automated coverage report | SIEM API + asset log source mapping |
| 16 (Backup restore tests) | Manual documentation | Automated test orchestration | Backup tool + reporting platform |

Rows marked Effort L or M with an existing tool already producing the data (e.g., EDR for
Row 8, vulnerability scanner for Row 4) need API integration, not a new tool purchase.

---
---

## Proposal Status

This document is a candidate framework contribution, not approved CERG content.

- It carries no CERG identifier and has no catalog entry, so it must not be cited as a CERG
  control, standard, or procedure.
- Adoption requires the upstream framework owner to accept it as a companion governance
  instrument and register it in the document catalog.
- Until then, engagement use is per-client: cite it as a draft operating model in the
  statement of work and keep client-specific applicability decisions in the engagement record.
