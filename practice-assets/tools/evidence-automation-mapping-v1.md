# CERG Control-to-Evidence Automation Mapping

## Practitioner Guide for Automated Compliance Evidence

| | |
|---|---|
| **Document ID** | CERG-OPN-TOOLS-003 |
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Quarterly |
| **Frameworks** | CERG 100-Core · NIST 800-53r5 · CIS Controls v8 |
| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 |
| **Environments** | All CERG in-scope environments |

---

## Purpose

Every control in the [CERG 100-Core Control Baseline](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) requires evidence. This document maps each control to the tool that can automatically collect that evidence, what the evidence artifact looks like, and how it feeds into the GRC platform.

Three evidence methods:

| Method | Label | Description | Auditor Acceptance |
|--------|-------|-------------|-------------------|
| **Automated** | E2 | Tool generates evidence continuously without human intervention. Polled from API or pushed from agent. | Full — auditor can request a fresh report anytime |
| **Semi-automated** | E1/E2 | Tool generates a report or snapshot, but a human must review, sign, or upload it. | Full — report timestamped with review date |
| **Manual** | E1 | Human collects, documents, or asserts evidence. No automated pipeline exists. | Partial — subject to sampling. Retain for full audit period |

**How to use this document:**

1. Deploy the recommended tool stack per [CERG Opinionated Tool Matrix](opinionated-tool-matrix-v1.md).
2. Configure evidence automation per the tables below.
3. Wire the evidence artifacts into your GRC platform per the [GRC Rollout Guide](grc-rollout-v1.md).
4. For manual-evidence controls, schedule collection in your ticketing system.

---

## Per-Tool Evidence Automation

### Entra ID / Okta (Identity Provider)

Configure: MFA enforcement, Conditional Access policies, automated provisioning/deprovisioning, PIM/PAM, audit logging.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| AC-001 | JML log (user creation/modification/deletion events) | API: Microsoft Graph `/auditLogs/directoryAudits` or Okta System Log | Automated → ServiceNow via REST | Continuous |
| AC-002 | MFA enrollment report (% enrolled, active vs inactive) | API: Microsoft Graph `/reports/credentialUserRegistrationDetails` or Okta `/api/v1/users?filter=profile.mfa.status` | Automated → ServiceNow or Vanta | Monthly snapshot |
| AC-003 | Authentication policy export (conditional access, SSO config) | PowerShell: `Get-MgConditionalAccessPolicy` or Okta `listAuthorizationServers` | Semi-auto: export → upload to GRC | Quarterly |
| AC-004 | PIM elevation logs (who elevated, when, to which role) | API: Microsoft Graph `/privilegedRoleAssignmentRequests` or Okta PAM API | Automated → ServiceNow | Continuous |
| AC-005 | VPN SAML authentication logs (MFA verification) | IdP sign-in logs filtered by VPN app | Automated → SIEM → ServiceNow | Continuous |
| AC-006 | Access review report (review date, reviewer, systems, actions) | API: Microsoft Graph `/identityGovernance/accessReviews/historyDefinitions` or Okta access certification | Automated → ServiceNow | Quarterly |
| AC-008 | Device compliance policy (screen lock timeout, encryption) | API: Microsoft Graph `/deviceManagement/configurationPolicies` or Intune export | Semi-auto: export → upload to GRC | Quarterly |
| IA-001 | User account list (unique IDs, account type) | API: Microsoft Graph `/users` or Okta `/api/v1/users` | Automated → ServiceNow | Quarterly |
| IA-002 | Password policy + MFA configuration | PowerShell: `Get-MgPolicyAuthorizationPolicy` + MFA report | Semi-auto: export → upload to GRC | Monthly |
| IA-003 | Disabled/deleted accounts report | API: Microsoft Graph `/directory/deletedItems` or Okta deactivated users | Automated → ServiceNow | Quarterly |
| IA-004 | Authenticator policy (password policy, token lifetime) | API: Microsoft Graph `/policies/authenticationMethodsPolicy` | Semi-auto: export → upload to GRC | Quarterly |
| PS-002 | Account deprovisioning log (termination timestamp) | Audit log: Microsoft Graph `/auditLogs/directoryAudits` (Delete user events) | Automated → ServiceNow | Per termination |
| PS-003 | Access change log (role transfer events) | Audit log: Microsoft Graph `/auditLogs` (group membership changes) | Automated → ServiceNow | Per transfer |

### SentinelOne Singularity (EDR / XDR)

Configure: agent deployment, application control, USB device control, integrity monitoring, network isolation.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| AC-003 | Agent deployment report (endpoints covered, coverage %) | SentinelOne API: `/web/api/v2.1/agents` (count by site) | Automated → ServiceNow via REST | Continuous |
| CM-005 | Application control policy + blocked execution events | SentinelOne API: `/web/api/v2.1/ranger/application-control` (policy export) | Semi-auto: policy export → GRC | Quarterly |
| CM-006 | Software inventory report | SentinelOne API: `/web/api/v2.1/installed-applications` | Automated → ServiceNow | Monthly |
| SI-003 | FIM alert log (unauthorized file changes) | SentinelOne API: `/web/api/v2.1/threats` filtered by FIM type | Automated → SIEM → ServiceNow | Continuous |
| SI-006 | Web control events (blocked categories) | SentinelOne API: `/web/api/v2.1/events/web` | Automated → SIEM → ServiceNow | Monthly |
| SI-007 | USB device control events (blocked devices) | SentinelOne API: `/web/api/v2.1/events/usb` | Automated → SIEM → ServiceNow | Quarterly |
| IR-003 | Network isolation events (containment actions) | SentinelOne API: `/web/api/v2.1/threats` (isolated threats) | Automated → ServiceNow incident | Continuous |
| IR-005 | Forensic snapshot (agent-initiated) | SentinelOne API: `/web/api/v2.1/forensics` (available per threat) | Semi-auto: fetch on incident | Per incident |

### Wazuh / Elastic Security (SIEM / Log Management)

Configure: agent deployment, log source onboarding, FIM module, SCA module, alert rules, reporting.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| AU-001 | Log source dashboard (source count, ingestion rate, last event) | Wazuh API: `/agents/stats` or Elastic API: `/monitoring` | Automated → ServiceNow dashboard | Continuous |
| AU-002 | SIEM retention configuration (hot/warm/cold/delete policies) | Elastic ILM API: `/_ilm/policy` or Wazuh `ossec.conf` export | Semi-auto: config export → GRC | Quarterly |
| AU-003 | Weekly review log (SIEM audit entry or screenshots) | Elastic API: audit log export | Semi-auto: scripted export → GRC ticket | Weekly |
| AU-005 | Index lifecycle management policy (retention by tier) | Elastic API: `/_ilm/policy` | Semi-auto: config export → GRC | Annual |
| AU-006 | Audit policy configuration (GPO export, cloud logging settings) | Elastic agent policy export or Wazuh agent config | Semi-auto: config export → GRC | Quarterly |
| AU-007 | Sample audit report (SIEM-generated, date-stamped) | Elastic Report API or Wazuh reporting module | Semi-auto: generate + upload to GRC | Quarterly |
| CA-001 | Consolidated monitoring dashboard (endpoint, vuln, cloud, backup, identity) | Composite: S1 + Tenable + Wiz + Veeam + Entra ID → ServiceNow | Automated → ServiceNow dashboard | Continuous |
| CM-003 | SCA scan results (compliance pass/fail per benchmark) | Wazuh API: `/sca/checks/agents` | Automated → ServiceNow compliance | Weekly |
| IR-002 | Alert rule configuration (Sigma rules deployed, alert count) | Elastic API: `/_rules/search` or Wazuh ruleset export | Semi-auto: config export → GRC | Quarterly |
| SI-004 | Sigma rule inventory (rule count, ATT&CK mapping, coverage %) | Elastic API: `/_rules/search` filtered by Sigma metadata | Automated → ServiceNow | Monthly |

### Tenable / Nessus (Vulnerability Management)

Configure: authenticated scanning, CIS compliance benchmarks, weekly external scan, monthly internal scan.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| RA-002 | Vulnerability scan results (by severity, by host) | Tenable API: `/scans/{id}/results` | Automated → ServiceNow vuln module | Weekly/Continuous |
| CM-001 | CIS compliance scan results (baseline adherence %) | Tenable API: `/compliance/results` | Automated → ServiceNow compliance | Quarterly |
| CM-003 | Configuration drift scan (new non-compliant findings) | Tenable API: `/compliance/results` (delta from previous) | Automated → ServiceNow | Weekly |
| CM-008 | Patch compliance report (% patched, missing patches by severity) | Tenable API: `/patch/results` | Automated → ServiceNow | Monthly |
| SC-004 | TLS scan report (cipher acceptance, protocol version) | Nessus SSL policy + `nmap --script ssl-enum-ciphers` | Semi-auto: export → upload to GRC | Quarterly |

### Wiz (CSPM / Cloud Security)

Configure: cloud account onboarding, CSPM policies, AI-SPM, network graph.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| CA-004 | Cloud network findings (external connections, exposed services) | Wiz API: `/v1/query` (network exposure queries) | Automated → ServiceNow | Quarterly |
| CM-003 | CSPM configuration drift (new cloud misconfigurations) | Wiz API: `/v1/issues` (filtered by severity change) | Automated → ServiceNow | Continuous |
| SC-003 | Cloud encryption status (EBS, S3, Azure SSE, GCP CSEK) | Wiz API: `/v1/query` (encryption at rest query) | Automated → ServiceNow | Quarterly |
| SC-001 | Cloud network segmentation graph (VPCs, subnets, peerings) | Wiz API: `/v1/query` (network topology) | Semi-auto: export → GRC | Quarterly |

### Veeam (Backup / Resilience)

Configure: backup jobs, immutable repositories, SureBackup, backup copy.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| CP-002 | Backup job configuration (systems covered, schedule, retention) | Veeam API: `/jobs` | Semi-auto: export → upload to GRC | Quarterly |
| CP-003 | SureBackup test results (pass/fail per workload, date) | Veeam API: `/sureBackup/results` | Automated → ServiceNow | Monthly |
| CP-004 | Backup copy job config (offsite repository, region) | Veeam API: `/backupCopyJobs` | Semi-auto: export → GRC | Annual |
| CP-005 | Restore test results (RTO/RPO measured per system) | Veeam API: `/restoreSessions` | Semi-auto: export → GRC | Annual |

### Fortinet (Network Security)

Configure: zone-based segmentation, web filter, DNS filter, wireless controller, VPN, 802.1X.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| SC-001 | Firewall ruleset export (zone security policies) | FortiGate API: `/api/v2/cmdb/firewall/policy` | Semi-auto: export → upload to GRC | Quarterly |
| SC-006 | Wireless configuration (SSIDs, encryption, auth method) | FortiGate API: `/api/v2/cmdb/wireless-controller/wtp-profile` | Semi-auto: export → GRC | Quarterly |
| SC-008 | DNS filter configuration (blocked categories, stats) | FortiGate API: `/api/v2/cmdb/dns-filter/dns-filter` | Semi-auto: export → GRC | Quarterly |
| SI-006 | Web filter configuration (categories, HTTPS inspection) | FortiGate API: `/api/v2/cmdb/webfilter/ftgd-local-ratings` | Semi-auto: export → GRC | Quarterly |
| AC-005 | VPN configuration (SSL-VPN settings, MFA requirement) | FortiGate API: `/api/v2/cmdb/vpn.ssl/settings` | Semi-auto: export → GRC | Quarterly |
| CA-004 | Site-to-site VPN inventory (IPsec phase2 tunnels) | FortiGate API: `/api/v2/cmdb/vpn.ipsec/phase2-interface` | Semi-auto: export → GRC | Quarterly |

### Microsoft 365 Defender (Email Security)

Configure: Safe Links, Safe Attachments, Anti-Phish, SPF/DKIM/DMARC, DLP.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| SI-005 | Email security configuration (Safe Links, Safe Attachments, DMARC) | Exchange Online PowerShell: `Get-SafeLinksPolicy`, `Get-SafeAttachmentPolicy`, `Get-DmarcPolicy` | Semi-auto: export → upload to GRC | Monthly |
| SI-005 | Phishing investigation log (reported phish, disposition, timestamps) | M365 Defender API: `/api/incidents` (email-based) | Automated → SIEM → ServiceNow | Continuous |
| SI-007 | DLP policy matches (blocked email containing sensitive data) | Microsoft Purview API: `/api/dlp/incidents` | Automated → ServiceNow | Continuous |

### Trivy / Semgrep (AppSec / Supply Chain)

Configure: CI/CD pipeline integration, SBOM generation, SAST scanning.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| SA-002 | SAST/DAST scan results (findings by severity, pass/fail gate) | Semgrep API: `/api/v1/deployments/{dep}/findings` | Automated → ServiceNow via API | Per release |
| SR-001 | SBOM inventory (component list, CVE matches) | Trivy SBOM output: `trivy sbom /tmp/sbom.json` | Semi-auto: store in Hudu → GRC | Per acquisition |

### ServiceNow GRC / Vanta (Governance Platform)

Configure: policy and compliance module, risk register, vendor risk, POA&M, Performance Analytics.

| Control | Evidence Artifact | Collection Method | GRC Feed | Frequency |
|---------|-------------------|-------------------|----------|-----------|
| CA-005 | POA&M entries (open items by age, finding owner, status) | ServiceNow GRC: `sn_compliance_finding` table | Native — ServiceNow IS the evidence | Continuous |
| PM-003 | Metrics dashboard (SLA adherence, trend, score) | ServiceNow GRC: Performance Analytics dashboard | Native — ServiceNow IS the evidence | Monthly |
| PM-004 | Program review records (quarterly review minutes, action items) | ServiceNow GRC: Task or HaloPSA ticket | Native — system of record | Quarterly |
| RA-003 | Risk register (risk entries, scores, treatments, owner) | ServiceNow GRC: `sn_grc_risk` or Vanta risk register | Native — GRC IS the evidence | Continuous |
| RA-004 | Risk acceptance records (accepted risks, approvals, expiry) | ServiceNow GRC risk acceptance workflow | Native — GRC IS the evidence | Per acceptance |
| CA-003 | Authorization workflow (ATO records, sign-off trail) | ServiceNow GRC authorization module | Native — GRC IS the evidence | Annual |
| SR-002 | Vendor assessment records (assessments by tier, due dates) | ServiceNow GRC vendor risk module | Native — GRC IS the evidence | Annual |

---

## Manual Evidence Controls

These controls cannot be fully automated. Evidence is collected by a human and uploaded to the GRC platform. Schedule collection in your ticketing system.

| Control | Why Manual | Collection Procedure | Minimum Schedule | Suggested Trigger |
|---------|-----------|---------------------|------------------|-------------------|
| AT-001 | Awareness training is people-process, not tool-generated | Export training platform completion report | Annual | Employee hire + annual cycle |
| AT-002 | Role-based assignments vary per org | Map roles to training assignments, export completions | Annual | Role change + annual cycle |
| AT-003 | Insider threat awareness is training content, not a tool metric | Training completion report for insider threat module | Annual | Included with AT-001 cycle |
| CA-002 | Security assessment requires human analysis | Conduct CERG Assessment per engagement playbook, upload report | Annual | Engagement calendar |
| CP-001 | Contingency plan is a written document | Review plan, update if needed, upload signed PDF | Annual | Planned DR test cycle |
| IR-001 | IR plan is a written document | Review plan, conduct tabletop, upload signed PDF | Annual | Q1 program review |
| IR-004 | Post-incident review requires human analysis | Write PIR template, upload to GRC within 14 days | Per incident | Incident closure |
| MA-001 | Maintenance is an operational process | Export ticketing system maintenance tickets | Per event | Maintenance window |
| MA-002 | Tool inventory requires human reconciliation | Audit tool list against RMM inventory | Quarterly | Q1/Q2/Q3/Q4 review |
| MA-003 | Firmware versions require manual check | Export firmware inventory from vendor tools | Quarterly | Patch Tuesday cycle |
| MP-001 | Media disposal is event-driven | Complete disposal log form per event | Per event | Hardware retirement |
| MP-002 | Media transport is event-driven | Complete transport log form per shipment | Per event | Offsite media shipment |
| MP-003 | Physical media access requires physical controls | Review access log, document any exceptions | Quarterly | Facility access review |
| PE-001 | Physical access is a facility control | Export badge system report, review exceptions | Quarterly | Facility access review |
| PE-002 | Environmental controls are facility management | Verify UPS test log, generator test, temperature logs | Quarterly | Facility inspection |
| PE-003 | Physical monitoring review requires human check | Review security footage / door access log anomalies | Quarterly | Facility inspection |
| PL-001 | SSP is a written document | Update SSP, upload signed PDF | Annual | Significant system change |
| PL-002 | Architecture diagram is maintained by humans | Update diagram in Hudu, upload to GRC | Quarterly | Network or cloud change |
| PL-003 | Rules of behavior are signed by humans | Upload signed AUP from onboarding/HR system | On hire + annual | Employment onboarding |
| PM-001 | Program plan is a written document | Review and update program plan, upload signed PDF | Annual | Q1 program review |
| PS-001 | Background screening is an HR process | Confirm screening was completed (store confirmation, not results) | Pre-hire | Before access grant |
| RA-001 | Risk assessment requires human analysis | Conduct annual risk assessment, upload report | Annual | Q4 planning cycle |
| RA-005 | Threat intel review requires analyst judgment | Document threat intel review notes, update risk register | Quarterly | CISA KEV + ISAC bulletin cycle |
| SA-001 | Procurement security review is per-event | Complete vendor evaluation checklist per procurement | Per acquisition | Before purchase order |
| SA-003 | Vendor risk assessment requires analyst review | Review vendor SOC 2, breach history, complete assessment | Annual (critical) | Contract renewal |
| SA-004 | Dev environment separation is architecture review | Document dev/test/prod separation per system | Per system | Architecture review |
| SA-005 | Outsourced dev contract review requires analysis | Review contract for security requirements, upload to GRC | Per engagement | Before outsourcing |
| IA-005 | Device auth config is a one-time setup with quarterly check | Export NAC/802.1X config, verify device cert enrollment | Quarterly | Network config review |
| AU-004 | Time sync config is a one-time setup with quarterly verification | Run `w32tm /query /status` on DCs, verify sync | Quarterly | Q1/Q2/Q3/Q4 review |
| AC-007 | SoD matrix is an organizational design document | Review SoD policy, update per role changes | Annual | Role definition change |
| CM-001 | Config baseline document requires human authoring | Update baseline doc per CIS benchmark version changes | Annual | Major OS version release |
| CM-002 | Change tickets are created per change | Ticketing system is the evidence for change control | Per change | Any production change |
| CM-004 | Least functionality checklist is per-build | Document server build checklist per new deployment | Per build | New server deployment |
| CM-007 | Hardware inventory requires monthly reconciliation | Reconcile RMM inventory against purchase records | Monthly | Month-end reconciliation |
| CP-003 | Full restore test requires human execution | Perform manual file-level restore, document outcome | Quarterly | Q1/Q2/Q3/Q4 DR test |

---

## Quick-Reference by Tool

For MSP onboarding a new client, configure these evidence pipelines in order:

| Priority | Tool | Controls Auto-Evidenced |
|----------|------|------------------------|
| 1 | **Entra ID / Okta** | AC-001, AC-002, AC-003, AC-004, AC-005, AC-006, AC-008, IA-001, IA-002, IA-003, IA-004, PS-002, PS-003 |
| 2 | **SentinelOne** | AC-003, CM-005, CM-006, SI-003, SI-006, SI-007, IR-003, IR-005 |
| 3 | **Wazuh / Elastic** | AU-001, AU-002, AU-003, AU-005, AU-006, CA-001, CM-003, IR-002, SI-004 |
| 4 | **Tenable / Nessus** | RA-002, CM-001, CM-003, CM-008, SC-004 |
| 5 | **Wiz** | CA-004, CM-003, SC-003, SC-001 |
| 6 | **Veeam** | CP-002, CP-003, CP-004, CP-005 |
| 7 | **Fortinet** | SC-001, SC-006, SC-008, SI-006, AC-005, CA-004 |
| 8 | **M365 Defender** | SI-005, SI-007 |
| 9 | **Trivy / Semgrep** | SA-002, SR-001 |
| — | **ServiceNow GRC / Vanta** | CA-005, PM-003, PM-004, RA-003, RA-004, CA-003, SR-002 |

**Manual-only controls (no tool pipeline):** 31 controls requiring human collection (AT-001 through AC-007 in the manual table above). Schedule these in your PSA with quarterly reminders.

---

## Evidence Automation Maturity

| Level | Description | Controls Achieved | Recommended For |
|-------|-------------|-------------------|-----------------|
| **Basic** | Manual collection only. MSP generates reports on request. | ~31 manual controls | SMB clients < 25 employees |
| **Intermediate** | All tool-generated evidence collected via API. Manual controls scheduled. | ~87 controls, ~56 auto-evidenced | Mid-market 50-500 employees, CMMC L2 prep |
| **Advanced** | Real-time evidence pipeline into GRC. Continuous monitoring dashboards. Exception alerts on evidence lapse. | 87 controls, continuous evidence refresh | Enterprise, SOX/CMMC L2 mature |
| **Adaptive** | Evidence feeds automated compliance scoring. Control effectiveness measured programmatically. | 87 controls + effectiveness metrics | Multi-client MSP with ServiceNow GRC |

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-20 | cragin-security | Initial release: 87 controls mapped to evidence tools, collection methods, GRC integration, and manual evidence procedures. |

### Review Triggers

- CB-002 100-Core Control Baseline updates (new/modified controls, tool binding changes)
- Tool stack changes (vendor acquisition, EOL, new integration capabilities)
- Regulatory evidence requirement changes (CMMC, SOX, PCI)

### Related Documents

- [CERG 100-Core Control Baseline](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — the control set this mapping covers
- [Opinionated Tool Matrix](opinionated-tool-matrix-v1.md) — tool selection criteria, primary/acceptable/avoid tiers
- [GRC Rollout Guide](grc-rollout-v1.md) — wiring ServiceNow GRC or Vanta to the CERG control framework
- [MSP Runbook](../msp-runbook-v1.md) — tool deployment commands and per-control implementation
- [Engagement Playbook](../engagement-playbook-v1.md) — scoping, pricing, SOW essentials, engagement lifecycle
- [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) — detection coverage and SIEM evidence parameters
- [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md) — identity and access evidence requirements
- [Cyber Resilience and Backup Standard](../../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) — backup and recovery evidence parameters
