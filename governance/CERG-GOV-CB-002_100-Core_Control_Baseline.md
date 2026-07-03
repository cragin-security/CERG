1|# 100-Core Control Baseline (Extended)
2|
3|## Practitioner-Ready Control Set with MSP Copy-Paste Instructions
4|
5|| | |
6||---|---|
7|| **Document ID** | CERG-GOV-CB-002 |
8|| **Version** | 1.0.0 |
9|| **Status** | Draft |
10|| **Classification** | Public |
11|| **Owner** | Consulting Practice Lead |
12|| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
13|| **Review Cycle** | Quarterly |
14|| **Frameworks** | NIST 800-53r5 · NIST 800-171r3 · NIST CSF 2.0 · CIS Controls v8 · ISO/IEC 27001 A.5-A.8 |
15|| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 · HIPAA Security Rule |
16|| **Environments** | All in-scope assets — IT, cloud, SaaS, OT (partial), CUI (where scoped) |
17|
18|---
19|
20|## Table of Contents
21|
22|1. [Relationship to Upstream CERG](#1-relationship-to-upstream-cerg)
23|2. [Control Format](#2-control-format)
24|3. [Access Control (AC)](#3-access-control-ac)
25|4. [Awareness and Training (AT)](#4-awareness-and-training-at)
26|5. [Audit and Accountability (AU)](#5-audit-and-accountability-au)
27|6. [Assessment, Authorization, and Monitoring (CA)](#6-assessment-authorization-and-monitoring-ca)
28|7. [Configuration Management (CM)](#7-configuration-management-cm)
29|8. [Contingency Planning (CP)](#8-contingency-planning-cp)
30|9. [Identification and Authentication (IA)](#9-identification-and-authentication-ia)
31|10. [Incident Response (IR)](#10-incident-response-ir)
32|11. [Maintenance (MA)](#11-maintenance-ma)
33|12. [Media Protection (MP)](#12-media-protection-mp)
34|13. [Physical and Environmental (PE)](#13-physical-and-environmental-pe)
35|14. [Planning (PL)](#14-planning-pl)
36|15. [Personnel Security (PS)](#15-personnel-security-ps)
37|16. [Risk Assessment (RA)](#16-risk-assessment-ra)
38|17. [System and Services Acquisition (SA)](#17-system-and-services-acquisition-sa)
39|18. [System and Communications Protection (SC)](#18-system-and-communications-protection-sc)
40|19. [System and Information Integrity (SI)](#19-system-and-information-integrity-si)
41|20. [Supply Chain Risk Management (SR)](#20-supply-chain-risk-management-sr)
42|21. [Program Management (PM)](#21-program-management-pm)
43|22. [Document Control](#22-document-control)
44|
45|---
46|
47|## 1. Relationship to Upstream CERG
48|
49|The upstream CERG baseline ([CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md)) defines the framework architecture and a schematic control matrix. This document — part of the cragin-security fork — extends the upstream baseline into a **practitioner-ready control set**.
50|
51|Differences from upstream:
52|
53|| Dimension | Upstream (CB-001) | This Document (CB-002) |
54||-----------|-------------------|------------------------|
55|| Control count | ~18 schematic entries | 97 enumerated controls |
56|| Audience | Program architects, auditors | MSPs, MSSPs, IT generalists |
57|| Instructions | None | Copy-paste deployment per control |
58|| Tool bindings | Framework-level | Tied to [Opinionated Tool Matrix](../practice-assets/tools/opinionated-tool-matrix-v1.md) |
59|| Evidence | Named artifact | Named artifact + collection method + frequency |
60|| Inheritance | Described in Section 5 of CB-001 | Per-control inheritance notes where applicable |
61|
62|Upstream CB-001 remains the authoritative architecture. This document is the implementation companion. Control IDs (e.g., AC-001) correspond to NIST 800-53r5 identifiers where applicable; CERG-native controls use domain-specific prefixes.
63|
64|---
65|
66|## 2. Control Format
67|
68|Every control entry follows this structure:
69|
70|| **Control ID** | NIST-aligned or CERG-native identifier |
71|| **Action Statement** | What the control requires, in plain language an IT generalist can understand |
72|| **System Applicability** | Hardware, Software, Network, Cloud, Data, Process — one or more |
73|| **Owning Pillar** | Engineering, Risk, or Governance |
74|| **Named Evidence** | The specific artifact that proves the control is operating |
75|| **Minimum Frequency** | How often evidence must be collected |
76|| **Subordinate Standard** | Link to the relevant CERG standard with parameter detail |
77|| **MSP Implementation Note** | Copy-paste instructions for MSPs/MSSPs (where applicable) |
78|| **Tool Binding** | Which tool(s) from the [Opinionated Tool Matrix](../practice-assets/tools/opinionated-tool-matrix-v1.md) satisfy this control |
79|
80|---
81|
82|## 3. Access Control (AC)
83|
84|### AC-001: Account Lifecycle Management
85|
86|| **Control ID** | AC-001 |
87|| **Action Statement** | Every user and service account has a documented request, named owner, defined access level, and Join-Move-Leave (JML) record. Accounts are disabled within 24 hours of termination. Dormant accounts (no login in 90 days) are disabled. |
88|| **System Applicability** | Hardware, Software, Network, Cloud, Data, Process |
89|| **Owning Pillar** | Engineering |
90|| **Named Evidence** | JML ticket log or HRIS integration report showing account lifecycle events |
91|| **Minimum Frequency** | Continuous (automated) / Quarterly (manual review) |
92|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
93|| **MSP Implementation Note** | Connect HRIS to IdP for automated provisioning/deprovisioning. For clients without HRIS integration, run this script quarterly: `Get-ADUser -Filter {LastLogonDate -lt (Get-Date).AddDays(-90)} | Disable-ADAccount`. Document all terminations in the ticket system within one business day. |
94|| **Tool Binding** | Okta / Entra ID (IdP), HaloPSA (ticketing), NinjaOne (RMM verification) |
95|
96|### AC-002: MFA Enforcement
97|
98|| **Control ID** | AC-002 |
99|| **Action Statement** | Multi-factor authentication is enforced for all user accounts accessing company systems. No exceptions for executives, IT staff, or administrators. Service accounts with non-interactive login must have documented compensating controls (network restriction, monitoring, credential rotation). |
100|| **System Applicability** | Software, Cloud, Network |
101|| **Owning Pillar** | Engineering |
102|| **Named Evidence** | IdP MFA enrollment report showing 100% enrollment for active human users |
103|| **Minimum Frequency** | Monthly |
104|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
105|| **MSP Implementation Note** | See [MSP Runbook](../practice-assets/msp-runbook-v1.md) AC-002 section for full deployment steps. Core commands: Okta > Security > Multifactor > Require for all. Entra ID > Conditional Access > Require MFA for all users. Test: attempt login without MFA — must be rejected. |
106|| **Tool Binding** | Okta / Entra ID |
107|
108|### AC-003: Access Enforcement
109|
110|| **Control ID** | AC-003 |
111|| **Action Statement** | All access to systems uses approved authentication and authorization controls. Local accounts, shared accounts, hard-coded credentials, and static passwords are prohibited where an IdP can enforce authentication. |
112|| **System Applicability** | Hardware, Software, Network, Cloud, Data |
113|| **Owning Pillar** | Engineering |
114|| **Named Evidence** | IdP policy export showing authentication policies; PAM solution deployment report (if applicable) |
115|| **Minimum Frequency** | Quarterly |
116|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
117|| **MSP Implementation Note** | Enforce SAML/OIDC SSO for all SaaS apps. Block legacy authentication protocols in Entra ID. For on-prem systems: join to domain, enforce Kerberos, disable NTLM where possible. Audit local accounts monthly: `Get-LocalUser | Where-Object Enabled` on all servers. |
118|| **Tool Binding** | Okta / Entra ID |
119|
120|### AC-004: Least Privilege
121|
122|| **Control ID** | AC-004 |
123|| **Action Statement** | Users and services operate with the minimum access necessary. Administrative privileges are granted through just-in-time or privileged access management, not standing group membership. Default and over-privileged accounts are identified and restricted. |
124|| **System Applicability** | Hardware, Software, Cloud, Data |
125|| **Owning Pillar** | Engineering |
126|| **Named Evidence** | Quarterly privilege audit report; PAM session log for administrative access |
127|| **Minimum Frequency** | Quarterly |
128|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
129|| **MSP Implementation Note** | Remove all users from Domain Admins. Create tiered admin groups (Workstation Admin, Server Admin, Domain Admin). Use PAM for elevation. For SMB without PAM budget: dedicated admin accounts (u-admin) separate from daily driver accounts, with 12-hour credential rotation. |
130|| **Tool Binding** | Okta / Entra ID (PIM), CyberArk / Delinea (PAM for enterprise) |
131|
132|### AC-005: Remote Access
133|
134|| **Control ID** | AC-005 |
135|| **Action Statement** | Remote access to internal systems requires MFA, encrypted transport, and device posture validation. Split-tunnel VPN configurations are prohibited unless documented with compensating controls. |
136|| **System Applicability** | Network, Cloud, Software |
137|| **Owning Pillar** | Engineering |
138|| **Named Evidence** | VPN/firewall configuration export; remote access policy |
139|| **Minimum Frequency** | Quarterly |
140|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
141|| **MSP Implementation Note** | FortiGate: enable SSL-VPN with SAML to Okta/Entra ID for MFA. Require client certificate in addition to MFA for admin VPN. Disable split tunneling unless explicitly scoped and documented. Verify: `show vpn ssl settings` shows `require-certificate enable`. |
142|| **Tool Binding** | Fortinet (firewall/VPN), Okta / Entra ID (auth) |
143|
144|### AC-006: Quarterly Access Review
145|
146|| **Control ID** | AC-006 |
147|| **Action Statement** | Access to all systems is reviewed quarterly by the system or data owner. Access that is no longer required is revoked within 5 business days. The review is documented and signed. |
148|| **System Applicability** | Software, Cloud, Data, Process |
149|| **Owning Pillar** | Engineering |
150|| **Named Evidence** | Signed access review report with reviewer name, date, systems reviewed, and actions taken |
151|| **Minimum Frequency** | Quarterly |
152|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
153|| **MSP Implementation Note** | Export all users with group memberships from Entra ID/Okta + all SaaS admin roles. Send to department heads with 5-day deadline. Revoke flagged access immediately. Document the review — even if no changes, the documentation IS the evidence. |
154|| **Tool Binding** | Okta / Entra ID |
155|
156|### AC-007: Separation of Duties
157|
158|| **Control ID** | AC-007 |
159|| **Action Statement** | No single individual can both request and approve access, or both develop and deploy code to production, or both initiate and approve payments. Conflicts are identified and mitigated through policy and tooling. |
160|| **System Applicability** | Process, Software |
161|| **Owning Pillar** | Governance |
162|| **Named Evidence** | Separation of duties matrix; access policy defining incompatible roles |
163|| **Minimum Frequency** | Annual |
164|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
165|| **MSP Implementation Note** | For SMB clients where one person wears every hat: implement two-person approval in the ticketing system for production changes. The incompatible duties are: (1) request access / approve access, (2) write code / deploy to production, (3) configure firewall / approve firewall change. |
166|| **Tool Binding** | HaloPSA (ticketing approval workflows), ServiceNow GRC |
167|
168|### AC-008: Session Lock
169|
170|| **Control ID** | AC-008 |
171|| **Action Statement** | User sessions lock after 15 minutes of inactivity. Re-authentication requires the full credential, not just screen dismissal. Device-level screen lock is enforced via MDM or GPO. |
172|| **System Applicability** | Hardware, Software |
173|| **Owning Pillar** | Engineering |
174|| **Named Evidence** | GPO/MDM policy export showing screen lock settings |
175|| **Minimum Frequency** | Quarterly |
176|| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
177|| **MSP Implementation Note** | Windows GPO: Computer Config > Policies > Windows Settings > Security Settings > Local Policies > Security Options > "Interactive logon: Machine inactivity limit" = 900 seconds. Verify: `gpresult /r` on a domain workstation. |
178|| **Tool Binding** | Active Directory GPO, Intune, Jamf |
179|
180|---
181|
182|## 4. Awareness and Training (AT)
183|
184|### AT-001: Security Awareness Training
185|
186|| **Control ID** | AT-001 |
187|| **Action Statement** | All personnel receive security awareness training within 30 days of hire and annually thereafter. Training covers phishing recognition, password hygiene, data handling, incident reporting, and the CERG program structure. |
188|| **System Applicability** | Process |
189|| **Owning Pillar** | Governance |
190|| **Named Evidence** | Training completion report with user list, completion dates, and course content summary |
191|| **Minimum Frequency** | Annual |
192|| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |
193|| **MSP Implementation Note** | Use a phishing simulation platform (KnowBe4, Proofpoint) with monthly simulated phishing. Track click rates. Anyone who clicks gets immediate remediation training. Annual full training via the same platform. |
194|| **Tool Binding** | KnowBe4, Proofpoint SAT, or M365 Attack Simulation Training |
195|
196|### AT-002: Role-Based Training
197|
198|| **Control ID** | AT-002 |
199|| **Action Statement** | Personnel in security-sensitive roles (developers, admins, executives, IR team) receive role-specific training on the threats, tools, and procedures relevant to their function. |
200|| **System Applicability** | Process |
201|| **Owning Pillar** | Governance |
202|| **Named Evidence** | Role-specific training assignments and completion records |
203|| **Minimum Frequency** | Annual |
204|| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |
205|| **MSP Implementation Note** | Developers: OWASP Top 10, secure coding. Admins: hardening, detection response. Executives: ransomware decision-making, breach notification obligations. Track in LMS or ticketing system. |
206|| **Tool Binding** | KnowBe4, PluralSight, SANS |
207|
208|### AT-003: Insider Threat Awareness
209|
210|| **Control ID** | AT-003 |
211|| **Action Statement** | Personnel are trained to recognize and report indicators of insider threat — unusual access patterns, data exfiltration warning signs, behavioral red flags. |
212|| **System Applicability** | Process |
213|| **Owning Pillar** | Governance |
214|| **Named Evidence** | Training module completion records |
215|| **Minimum Frequency** | Annual |
216|| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7 |
217|| **MSP Implementation Note** | Include insider threat module in annual training. Content: "If you see a coworker downloading large amounts of data before resigning, or accessing systems they don't normally use, report it. You will not get in trouble for a good-faith report." |
218|| **Tool Binding** | KnowBe4, Proofpoint SAT |
219|
220|---
221|
222|## 5. Audit and Accountability (AU)
223|
224|### AU-001: Audit Log Collection
225|
226|| **Control ID** | AU-001 |
227|| **Action Statement** | All systems generate audit logs for security-relevant events. Logs are forwarded to a centralized SIEM within 5 minutes of generation. Log sources include: endpoints, servers, network devices, firewalls, IdP, cloud platforms, and SaaS applications. |
228|| **System Applicability** | Hardware, Software, Network, Cloud, Data |
229|| **Owning Pillar** | Risk |
230|| **Named Evidence** | SIEM dashboard showing log source count and ingestion status |
231|| **Minimum Frequency** | Continuous |
232|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
233|| **MSP Implementation Note** | Windows: enable Event Log Forwarding or deploy Wazuh agent. Network: syslog to SIEM. Cloud: CloudTrail (AWS), Activity Log (Azure), Cloud Audit Logs (GCP) → SIEM. SaaS: API connectors to SIEM. Minimum log sources per client: endpoints, firewalls, domain controllers, IdP, cloud admin activity, email gateway. |
234|| **Tool Binding** | Elastic Security / Wazuh |
235|
236|### AU-002: Log Protection
237|
238|| **Control ID** | AU-002 |
239|| **Action Statement** | Audit logs are protected from unauthorized modification, deletion, and access. Log integrity is verifiable. Log retention meets the longest applicable regulatory requirement (minimum 90 days online, 1 year offline). |
240|| **System Applicability** | Data, Cloud |
241|| **Owning Pillar** | Risk |
242|| **Named Evidence** | SIEM configuration showing access controls and retention settings |
243|| **Minimum Frequency** | Quarterly |
244|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
245|| **MSP Implementation Note** | Wazuh: default retention is filesystem-based — ensure sufficient disk. Elastic: configure index lifecycle management (hot 30d → warm 60d → cold 365d → delete). Restrict SIEM access to named MSP security personnel only. |
246|| **Tool Binding** | Elastic Security / Wazuh |
247|
248|### AU-003: Log Review
249|
250|| **Control ID** | AU-003 |
251|| **Action Statement** | Security logs are reviewed regularly. Automated alerting is configured for high-severity events. Weekly manual review of SIEM dashboards for anomalies that escaped automated detection. |
252|| **System Applicability** | Data, Process |
253|| **Owning Pillar** | Risk |
254|| **Named Evidence** | Weekly review log (screenshot or SIEM audit entry); alert configuration export |
255|| **Minimum Frequency** | Weekly (manual review), Continuous (automated) |
256|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
257|| **MSP Implementation Note** | Schedule 30-minute weekly review session per client. Check: top alerts, new log sources, detection coverage gaps, suppressed alerts that should be re-enabled. Document the session in the ticketing system. |
258|| **Tool Binding** | Elastic Security / Wazuh |
259|
260|### AU-004: Time Synchronization
261|
262|| **Control ID** | AU-004 |
263|| **Action Statement** | All systems use a common time source synchronized to a reliable NTP server. Log timestamps are consistent and usable for correlation and forensic analysis. |
264|| **System Applicability** | Hardware, Software, Network, Cloud |
265|| **Owning Pillar** | Engineering |
266|| **Named Evidence** | NTP configuration export from domain controller or cloud platform |
267|| **Minimum Frequency** | Quarterly |
268|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
269|| **MSP Implementation Note** | Domain controllers sync to pool.ntp.org or time.windows.com. All domain-joined systems inherit. Linux: `timedatectl set-ntp true`. Network devices: `ntp server <dc-ip>`. Verify: `w32tm /query /status` on Windows, `timedatectl` on Linux. |
270|| **Tool Binding** | Built-in OS NTP |
271|
272|### AU-005: Audit Record Retention
273|
274|| **Control ID** | AU-005 |
275|| **Action Statement** | Audit records are retained according to a defined schedule. Online retention: minimum 90 days. Offline/archive retention: minimum 1 year. Retention schedule is documented and enforced by tooling. |
276|| **System Applicability** | Data |
277|| **Owning Pillar** | Risk |
278|| **Named Evidence** | Retention policy document; SIEM configuration showing retention settings |
279|| **Minimum Frequency** | Annual review of retention settings |
280|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
281|| **MSP Implementation Note** | Higher retention for regulated clients: PCI requires 1 year online. HIPAA: 6 years (can be offline). CMMC: minimum 90 days, recommend 1 year. Scale storage accordingly. |
282|| **Tool Binding** | Elastic Security / Wazuh (with appropriate storage) |
283|
284|### AU-006: Audit Generation
285|
286|| **Control ID** | AU-006 |
287|| **Action Statement** | Information systems generate audit records for defined event types: account creation/modification/deletion, privilege use, logon/logoff, object access, policy changes, system events, and security tool alerts. |
288|| **System Applicability** | Hardware, Software, Network, Cloud |
289|| **Owning Pillar** | Risk |
290|| **Named Evidence** | Audit policy configuration export (GPO, cloud platform, SaaS settings) |
291|| **Minimum Frequency** | Continuous generation; quarterly configuration review |
292|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
293|| **MSP Implementation Note** | Windows: Advanced Audit Policy via GPO. Enable: Account Logon, Account Management, Logon/Logoff, Object Access (at minimum file shares), Policy Change, Privilege Use, System. Cloud: enable all management-plane logging (CloudTrail, Activity Log, Audit Logs). |
294|| **Tool Binding** | Active Directory GPO, Cloud native logging |
295|
296|### AU-007: Audit Reduction and Report Generation
297|
298|| **Control ID** | AU-007 |
299|| **Action Statement** | The SIEM supports ad-hoc querying and scheduled report generation for audit events. The MSP can produce a human-readable report of security-relevant events for a given time period within 1 hour of request. |
300|| **System Applicability** | Software |
301|| **Owning Pillar** | Risk |
302|| **Named Evidence** | Sample audit report generated from SIEM |
303|| **Minimum Frequency** | Capability verification quarterly |
304|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
305|| **MSP Implementation Note** | Elastic: create saved dashboards per client. Wazuh: use the reporting module. Both should support "give me all authentication failures for Client X in March 2026" in < 1 hour. |
306|| **Tool Binding** | Elastic Security / Wazuh |
307|
308|---
309|
310|## 6. Assessment, Authorization, and Monitoring (CA)
311|
312|### CA-001: Continuous Monitoring
313|
314|| **Control ID** | CA-001 |
315|| **Action Statement** | The security posture of in-scope systems is monitored continuously through automated tooling. Monitoring covers: endpoint protection status, vulnerability scan results, cloud configuration, backup status, and identity hygiene. Deviations from baseline generate alerts. |
316|| **System Applicability** | Hardware, Software, Network, Cloud |
317|| **Owning Pillar** | Governance |
318|| **Named Evidence** | Consolidated monitoring dashboard; alert configuration |
319|| **Minimum Frequency** | Continuous |
320|| **Subordinate Standard** | [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
321|| **MSP Implementation Note** | Required dashboards per client: SentinelOne agent status, Tenable vulnerability summary, Wiz cloud findings, Veeam backup health, Entra ID/Okta MFA status. Review all five weekly. Any gap gets a ticket. |
322|| **Tool Binding** | SentinelOne, Tenable, Wiz, Veeam, Okta/Entra ID → ServiceNow GRC |
323|
324|### CA-002: Security Assessment
325|
326|| **Control ID** | CA-002 |
327|| **Action Statement** | A security assessment of in-scope systems is conducted at least annually. The assessment evaluates control effectiveness, identifies gaps, and produces a prioritized remediation plan. |
328|| **System Applicability** | Process |
329|| **Owning Pillar** | Governance |
330|| **Named Evidence** | Annual assessment report with findings, severity, and remediation status |
331|| **Minimum Frequency** | Annual |
332|| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
333|| **MSP Implementation Note** | This is the CERG Assessment engagement (see [Engagement Playbook](../practice-assets/engagement-playbook-v1.md)). For ongoing clients, repeat the assessment annually with reduced scope — verify existing controls, focus on changes since last assessment. |
334|| **Tool Binding** | Tenable/Nessus (technical assessment), ServiceNow GRC (control assessment) |
335|
336|### CA-003: Authorization
337|
338|| **Control ID** | CA-003 |
339|| **Action Statement** | Systems are formally authorized to operate by the appropriate authority before entering production. Authorization is based on a review of security controls, risk acceptance, and residual risk. |
340|| **System Applicability** | Process |
341|| **Owning Pillar** | Governance |
342|| **Named Evidence** | Signed Authorization to Operate (ATO) document per system, or consolidated ATO for the environment |
343|| **Minimum Frequency** | Per system deployment; annual reaffirmation |
344|| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
345|| **MSP Implementation Note** | For SMB clients: a single ATO document covering the core IT environment, signed by the business owner. For CMMC clients: formal authorization package per CMMC assessment scope. |
346|| **Tool Binding** | ServiceNow GRC (authorization workflow) |
347|
348|### CA-004: Interconnection Monitoring
349|
350|| **Control ID** | CA-004 |
351|| **Action Statement** | Connections between the client's environment and external systems (MSP tools, cloud providers, SaaS platforms, partner networks) are documented and monitored. Changes to interconnections are reviewed and authorized. |
352|| **System Applicability** | Network, Cloud |
353|| **Owning Pillar** | Governance |
354|| **Named Evidence** | Interconnection inventory; firewall ruleset review |
355|| **Minimum Frequency** | Quarterly |
356|| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
357|| **MSP Implementation Note** | Document every site-to-site VPN, every API integration, every SaaS OAuth connection. Review quarterly: is this connection still needed? Is the partner still authorized? Are credentials rotated? |
358|| **Tool Binding** | Fortinet (firewall rules), ServiceNow GRC (interconnection register) |
359|
360|### CA-005: Plan of Action and Milestones (POA&M)
361|
362|| **Control ID** | CA-005 |
363|| **Action Statement** | All findings from assessments, audits, and continuous monitoring are tracked in a POA&M. Each entry has: finding description, severity, remediation owner, target date, and status. The POA&M is reviewed monthly. |
364|| **System Applicability** | Process |
365|| **Owning Pillar** | Governance |
366|| **Named Evidence** | Current POA&M export with all open items |
367|| **Minimum Frequency** | Monthly review; continuous update |
368|| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
369|| **MSP Implementation Note** | ServiceNow GRC: use the POA&M module. Vanta: use risk register with due dates. Track every finding from vuln scans, assessments, audits, and monitoring gaps. Nothing older than 90 days without a funded remediation plan. |
370|| **Tool Binding** | ServiceNow GRC / Vanta |
371|
372|---
373|
374|## 7. Configuration Management (CM)
375|
376|### CM-001: Configuration Baseline
377|
378|| **Control ID** | CM-001 |
379|| **Action Statement** | Every system type has a documented, approved configuration baseline. Baselines are based on CIS Benchmarks or equivalent hardening standards. Deviations require documented exception. |
380|| **System Applicability** | Hardware, Software |
381|| **Owning Pillar** | Engineering |
382|| **Named Evidence** | Configuration baseline document per system type; exception log |
383|| **Minimum Frequency** | Annual review; update on major version change |
384|| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
385|| **MSP Implementation Note** | Start with CIS Benchmarks. Download the PDF for Windows Server, Ubuntu, and your firewall model. Apply the Level 1 profile (safe for production). Document which settings diverge and why. |
386|| **Tool Binding** | CIS Benchmark PDFs + Wazuh SCA module for enforcement |
387|
388|### CM-002: Change Control
389|
390|| **Control ID** | CM-002 |
391|| **Action Statement** | Changes to production systems follow a documented change management process. Changes are requested, reviewed, approved, tested where feasible, and documented. Emergency changes are permitted but require post-hoc review within 24 hours. |
392|| **System Applicability** | Process, Hardware, Software, Network, Cloud |
393|| **Owning Pillar** | Engineering |
394|| **Named Evidence** | Change tickets for the review period; change management policy |
395|| **Minimum Frequency** | Per-change documentation; quarterly process review |
396|| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
397|| **MSP Implementation Note** | Use the ticketing system for all production changes. Minimum fields: what's changing, why, rollback plan, approver, test results. For SMB with a single IT person: self-approve is acceptable for routine changes; major changes (firewall, domain controller, backup config) require a second set of eyes. |
398|| **Tool Binding** | HaloPSA / ConnectWise Manage |
399|
400|### CM-003: Configuration Drift Detection
401|
402|| **Control ID** | CM-003 |
403|| **Action Statement** | Systems are monitored for configuration drift from their approved baseline. Drift findings are detected within the scan interval and remediated or excepted. |
404|| **System Applicability** | Hardware, Software, Cloud |
405|| **Owning Pillar** | Engineering |
406|| **Named Evidence** | Configuration scan results showing baseline compliance; drift findings and remediation records |
407|| **Minimum Frequency** | Weekly (critical), Monthly (all) |
408|| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
409|| **MSP Implementation Note** | Wazuh SCA module: load CIS policies, schedule weekly scans. Wiz: continuous CSPM for cloud. Tenable: monthly compliance scans against CIS benchmarks. Any finding > Medium opens a ticket. |
410|| **Tool Binding** | Wazuh (SCA), Tenable/Nessus (compliance scans), Wiz (CSPM) |
411|
412|### CM-004: Least Functionality
413|
414|| **Control ID** | CM-004 |
415|| **Action Statement** | Systems are configured to provide only the functions and services necessary for their purpose. Unnecessary software, services, ports, and protocols are removed or disabled. |
416|| **System Applicability** | Hardware, Software |
417|| **Owning Pillar** | Engineering |
418|| **Named Evidence** | Server build checklist; port scan results showing only required services |
419|| **Minimum Frequency** | Per-build; quarterly verification |
420|| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
421|| **MSP Implementation Note** | Server build checklist: remove all roles/features not required. Disable SMBv1, LLMNR, NetBIOS, WPAD. Uninstall unnecessary software (browser toolbars, outdated Java, trial software). Verify with `nmap -sV <target>` — every open port must have a documented purpose. |
422|| **Tool Binding** | CIS Benchmark checklists, Nmap |
423|
424|### CM-005: Software Whitelisting
425|
426|| **Control ID** | CM-005 |
427|| **Action Statement** | Only authorized software executes on endpoints and servers. Unapproved software is blocked by default. Whitelisting is based on publisher certificate, file hash, or path — not user discretion. |
428|| **System Applicability** | Hardware |
429|| **Owning Pillar** | Engineering |
430|| **Named Evidence** | Application control policy export; blocked execution events |
431|| **Minimum Frequency** | Continuous enforcement; quarterly policy review |
432|| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
433|| **MSP Implementation Note** | Windows: AppLocker in audit-only mode for 30 days to build the baseline, then enforce. SentinelOne: Application Control module. For simple SMB deployments: Software Restriction Policies via GPO (path-based) is better than nothing. |
434|| **Tool Binding** | Windows AppLocker, SentinelOne Application Control |
435|
### CM-006: Software Inventory

| **Control ID** | CM-006 |
| **Action Statement** | A current inventory of all software installed on in-scope systems is maintained. Unauthorized or unmanaged software is identified and removed or approved. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Software inventory report; unauthorized software findings log |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | NinjaOne agent collects installed software inventory automatically. Review monthly: flag anything not in the approved list. SentinelOne also provides software inventory with threat context. |
| **Tool Binding** | NinjaOne (RMM), SentinelOne |

### CM-007: Hardware Inventory

| **Control ID** | CM-007 |
| **Action Statement** | A current inventory of all in-scope hardware assets is maintained. Inventory includes: asset ID, type, location, owner, operating system, IP address, and last seen date. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Hardware inventory report covering all in-scope assets |
| **Minimum Frequency** | Monthly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | NinjaOne provides automated hardware inventory. Reconcile monthly against the client's asset list. Flag any device not in RMM but present on the network (rogue device detection). |
| **Tool Binding** | NinjaOne (RMM) |

### CM-008: Automated Patching

| **Control ID** | CM-008 |
| **Action Statement** | Operating system and application patches are deployed within defined SLAs. Critical security patches: 7 days. High-severity: 14 days. Medium: 30 days. Patch deployment is automated via RMM or native update management. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Patch compliance report showing deployment status by severity |
| **Minimum Frequency** | Monthly (reporting), Continuous (deployment) |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | NinjaOne: configure automated approval for Critical and Security patches. Test on pilot group (5% of endpoints), then deploy to all. Servers: maintenance window. Document any patch that breaks something and the exception. |
| **Tool Binding** | NinjaOne, Windows Update for Business, Tenable (vuln → patch mapping) |

---

## 8. Contingency Planning (CP)

### CP-001: Contingency Plan

| **Control ID** | CP-001 |
| **Action Statement** | A written contingency plan exists for the in-scope environment. The plan identifies critical systems, recovery objectives (RTO/RPO), roles and responsibilities, and recovery procedures. |
| **System Applicability** | Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Contingency plan document, signed and current |
| **Minimum Frequency** | Annual review; update on major system change |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Minimum plan contents: critical system list (priority order), RTO per system (how fast to recover), RPO per system (how much data loss is acceptable), who does what during recovery, communication plan, test schedule. Keep it under 10 pages — it needs to be usable during an incident. |
| **Tool Binding** | ServiceNow GRC (plan repository) |

### CP-002: Backup Configuration

| **Control ID** | CP-002 |
| **Action Statement** | All critical systems and data are backed up on a defined schedule. Backups are stored in at least two locations with at least one immutable or offline copy. Backup configuration is documented. |
| **System Applicability** | Hardware, Software, Cloud, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Backup job configuration export; storage location documentation |
| **Minimum Frequency** | Quarterly review of configuration |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Veeam: configure daily incremental, weekly full, monthly archival. Enable immutability on all backup repositories (Linux hardened repo or object storage with Object Lock). Backup copy to offsite (Veeam Cloud Connect to MSP infrastructure). Document the 3-2-1 rule: 3 copies, 2 media types, 1 offsite. |
| **Tool Binding** | Veeam |

### CP-003: Backup Testing

| **Control ID** | CP-003 |
| **Action Statement** | Backups are tested regularly to confirm they can be restored. Test results are documented. Failed tests generate an incident and immediate remediation. |
| **System Applicability** | Hardware, Software, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Backup test results log showing date, system tested, outcome |
| **Minimum Frequency** | Monthly (automated), Quarterly (manual full restore test) |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Veeam SureBackup: schedule weekly automated test restores of sample workloads. Quarterly manual test: restore a production file server, verify users can access data. Any failure = high-severity incident. |
| **Tool Binding** | Veeam |

### CP-004: Alternate Storage Site

| **Control ID** | CP-004 |
| **Action Statement** | Backup data is stored at a geographically separate location from the primary site. The alternate site is far enough to survive a regional disaster (minimum 50 miles for physical sites; different cloud region for cloud). |
| **System Applicability** | Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Storage location documentation showing geographic separation |
| **Minimum Frequency** | Annual verification |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | For on-prem clients: Veeam backup copy to MSP's cloud repository (different region). For cloud-native: cross-region replication. Verify: "if the primary site burns down, do we still have backups?" |
| **Tool Binding** | Veeam, AWS S3 Cross-Region Replication, Azure GRS |

### CP-005: System Recovery Procedures

| **Control ID** | CP-005 |
| **Action Statement** | Documented procedures exist for recovering each critical system from backup. Procedures are tested and updated annually. Recovery time and recovery point objectives are defined and measured. |
| **System Applicability** | Process, Hardware, Software, Data |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Recovery procedure document; test results with RTO/RPO measurements |
| **Minimum Frequency** | Annual test; quarterly review of procedures |
| **Subordinate Standard** | [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **MSP Implementation Note** | Write recovery procedures in order: domain controller first (authentication), then file server, then application servers, then email. Each procedure: step-by-step commands. Test once a year and time it. If DR test takes 8 hours but the plan says 4 hours, update the plan or fix the process. |
| **Tool Binding** | Veeam (orchestration), HaloPSA (procedure documentation) |

---

## 9. Identification and Authentication (IA)

### IA-001: Unique Identification

| **Control ID** | IA-001 |
| **Action Statement** | Every user and system component has a unique identifier. Shared accounts are prohibited for interactive login. Service accounts are uniquely named and documented. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | User account list showing unique identifiers; service account inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | One person = one account. No "admin" account shared among IT staff. Service accounts follow naming convention: `svc-Purpose-Env`. Document all service accounts in Hudu/IT Glue. |
| **Tool Binding** | Okta / Entra ID, Hudu (documentation) |

### IA-002: Strong Authentication

| **Control ID** | IA-002 |
| **Action Statement** | Authentication uses phishing-resistant methods where possible (FIDO2, certificate-based). Password-based authentication requires minimum 12 characters and is combined with MFA. Default passwords are changed on first use. |
| **System Applicability** | Software, Cloud, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | MFA enrollment report; password policy configuration |
| **Minimum Frequency** | Monthly verification |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Entra ID: Password Protection enabled. Minimum 12 characters (set higher if possible). Ban common passwords. FIDO2 security keys for privileged accounts where budget allows. At minimum: MFA on everything. |
| **Tool Binding** | Okta / Entra ID |

### IA-003: Identifier Management

| **Control ID** | IA-003 |
| **Action Statement** | User identifiers are managed throughout their lifecycle. Identifiers are never reused for 12 months after deactivation. Group accounts are prohibited. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Account lifecycle policy; disabled accounts report |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Disable, don't delete — retains audit trail. No username reuse for 12 months. No group/shared accounts ("reception", "warehouse"). Every human gets their own account. |
| **Tool Binding** | Okta / Entra ID |

### IA-004: Authenticator Management

| **Control ID** | IA-004 |
| **Action Statement** | Authenticators (passwords, tokens, certificates, keys) are managed through their lifecycle: issuance, storage, rotation, revocation, and disposal. Default authenticators are changed on first use. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Password policy; certificate inventory; token management process |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Passwords: 12+ characters, no expiration if MFA is enforced (per NIST 800-63B). Service account passwords: rotate every 90 days or use managed identities. API keys: rotate quarterly, store in vault/Hudu. |
| **Tool Binding** | Okta / Entra ID, Hudu (credential documentation) |

### IA-005: Device Authentication

| **Control ID** | IA-005 |
| **Action Statement** | Devices connecting to the network or accessing resources are uniquely identified and authenticated. Certificate-based or domain authentication is preferred over pre-shared keys. |
| **System Applicability** | Hardware, Network |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Network access control configuration; device certificate inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **MSP Implementation Note** | Windows: domain-joined = authenticated. Network: 802.1X with device certificates for wired/wireless (enterprise). Guest network: separate SSID, internet-only. At minimum: MAC filtering + separate VLAN for unknown devices. |
| **Tool Binding** | Active Directory, Fortinet (802.1X/NAC) |

---

## 10. Incident Response (IR)

### IR-001: Incident Response Plan

| **Control ID** | IR-001 |
| **Action Statement** | A written incident response plan exists. It defines incident types, severity classification, roles, communication procedures, and escalation paths. The plan is tested annually. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | IR plan document; test/exercise results |
| **Minimum Frequency** | Annual review and test |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Minimum plan contents: incident definition (what counts), severity levels (1-4), who to call first (and second and third), containment steps, evidence preservation, notification obligations, post-incident review. Keep it short — 5-10 pages. |
| **Tool Binding** | ServiceNow GRC (plan repository), HaloPSA (incident workflow) |

### IR-002: Incident Detection and Reporting

| **Control ID** | IR-002 |
| **Action Statement** | Incidents are detected through automated monitoring and reported through a defined channel. All personnel know how to report a security incident. Reports are acknowledged within 1 hour and triaged within 4 hours. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Alert configuration; incident report log |
| **Minimum Frequency** | Continuous |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | SIEM alerts → MSP ticketing system (auto-create ticket). End user reports → dedicated email (security@client.com) or phone. Quarterly test: send a test alert, verify it creates a ticket within 5 minutes. |
| **Tool Binding** | Elastic/Wazuh → HaloPSA, SentinelOne → HaloPSA |

### IR-003: Incident Containment

| **Control ID** | IR-003 |
| **Action Statement** | The IR team can contain an incident within defined timeframes. Containment procedures exist for common incident types (ransomware, account compromise, data exfiltration, denial of service). |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Containment procedure documents; post-incident reports with containment timelines |
| **Minimum Frequency** | Annual review; per-incident execution |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Ransomware containment procedure: isolate affected systems (disable switch port or remove from network), revoke compromised credentials, preserve evidence (forensic image before reimaging), engage IR firm if beyond MSP capability. Pre-stage: SentinelOne network isolation capability for rapid containment. |
| **Tool Binding** | SentinelOne (network isolation), Fortinet (ACL changes) |

### IR-004: Post-Incident Review

| **Control ID** | IR-004 |
| **Action Statement** | Within 14 days of incident closure, a post-incident review is conducted. The review identifies root cause, timeline, response effectiveness, lessons learned, and control improvements. Findings are tracked to remediation. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Post-incident review document per incident |
| **Minimum Frequency** | Per incident |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Standard post-incident template: (1) What happened (timeline), (2) How we found out (detection source), (3) What we did (response actions), (4) What worked / what didn't, (5) What changes are needed (controls, training, tooling). Track action items in POA&M. |
| **Tool Binding** | ServiceNow GRC / HaloPSA |

### IR-005: Incident Evidence Preservation

| **Control ID** | IR-005 |
| **Action Statement** | During incident response, evidence is preserved for forensic analysis and potential legal action. Chain of custody is maintained. Evidence retention follows legal and regulatory requirements. |
| **System Applicability** | Process, Data |
| **Owning Pillar** | Risk |
| **Named Evidence** | Evidence handling procedure; chain of custody log for incidents |
| **Minimum Frequency** | Per incident |
| **Subordinate Standard** | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **MSP Implementation Note** | Before reimaging a compromised system: take forensic image (FTK Imager or dd). Preserve SIEM logs, firewall logs, endpoint telemetry for the incident window. Store evidence on write-once media or immutable storage. Do not delete anything until legal/insurance confirms it's clear. |
| **Tool Binding** | FTK Imager, Veeam (forensic backup), Elastic/Wazuh (log export) |

---

## 11. Maintenance (MA)

### MA-001: Controlled Maintenance

| **Control ID** | MA-001 |
| **Action Statement** | System maintenance is planned, scheduled, and performed by authorized personnel. Maintenance activities are logged. Remote maintenance sessions are authenticated, encrypted, and monitored. |
| **System Applicability** | Hardware, Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Maintenance schedule; maintenance logs |
| **Minimum Frequency** | Per maintenance event |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | All maintenance: scheduled in ticketing system, approved before execution. Remote sessions: use the RMM (NinjaOne) which logs all activity. No RDP directly from the internet — always through VPN or RMM. |
| **Tool Binding** | NinjaOne, HaloPSA |

### MA-002: Maintenance Tools

| **Control ID** | MA-002 |
| **Action Statement** | Maintenance tools (diagnostic utilities, remote access tools, patching tools) are approved, inventoried, and kept current. Unapproved tools are blocked. |
| **System Applicability** | Software |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Approved tool list; tool inventory |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Standardize on: NinjaOne (RMM), HaloPSA (ticketing), SentinelOne (EDR), Veeam (backup). These are the approved maintenance tools. Everything else requires a documented exception. No TeamViewer, AnyDesk, LogMeIn — use the RMM. |
| **Tool Binding** | NinjaOne, SentinelOne (application control to block unapproved tools) |

### MA-003: Firmware and Hardware Updates

| **Control ID** | MA-003 |
| **Action Statement** | Network device firmware, server firmware (BIOS/UEFI), and hardware component firmware are updated when security vulnerabilities are announced. Critical firmware updates: 30 days. |
| **System Applicability** | Hardware |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Firmware inventory with version and update status |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **MSP Implementation Note** | Fortinet: subscribe to security advisories. Apply critical firmware within 30 days. Servers: vendor firmware update tools (Dell OpenManage, HPE iLO). Document firmware versions in Hudu. |
| **Tool Binding** | NinjaOne (inventory), Hudu (documentation), vendor update tools |

---

## 12. Media Protection (MP)

### MP-001: Media Sanitization

| **Control ID** | MP-001 |
| **Action Statement** | Digital media (hard drives, SSDs, USB drives, tapes) is sanitized before disposal or reuse. Sanitization method is appropriate to the data classification. NIST SP 800-88 methods are the standard. |
| **System Applicability** | Hardware, Data |
| **Owning Pillar** | Governance |
| **Named Evidence** | Media disposal log with sanitization method per device |
| **Minimum Frequency** | Per disposal event |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |
| **MSP Implementation Note** | Standard IT equipment: secure erase (ATA Secure Erase) or cryptographic erase (destroy encryption key). CUI/regulated data: physical destruction (shredder, degausser, certified destruction service). Document what was destroyed, when, by whom, method used. |
| **Tool Binding** | DBAN (secure erase), certified destruction service |

### MP-002: Media Transport

| **Control ID** | MP-002 |
| **Action Statement** | Media containing sensitive data is protected during transport. Encryption is applied. Access is restricted to authorized couriers. Chain of custody is maintained. |
| **System Applicability** | Data, Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Transport log; encryption verification |
| **Minimum Frequency** | Per transport event |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |
| **MSP Implementation Note** | Backup tapes/disks for offsite storage: encrypt before transport (Veeam encryption at rest). Use bonded courier. Document: what was transported, when, from where to where, who transported it, encryption status. |
| **Tool Binding** | Veeam (encryption), Hudu (chain of custody log) |

### MP-003: Media Access

| **Control ID** | MP-003 |
| **Action Statement** | Access to media containing sensitive data is restricted to authorized personnel. Media is stored in physically secure locations. Access is logged. |
| **System Applicability** | Data, Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Access control list for media storage; access log |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) |
| **MSP Implementation Note** | Backup media: locked cabinet or data center cage. Access restricted to named personnel. Document who has keys/codes. For cloud-native clients without physical media: this control is satisfied by cloud provider's physical security (documented via SOC 2 report). |
| **Tool Binding** | Physical security (locked storage), Cloud provider SOC 2 (inheritance) |

---

## 13. Physical and Environmental (PE)

### PE-001: Physical Access Control

| **Control ID** | PE-001 |
| **Action Statement** | Physical access to facilities housing in-scope systems is controlled and monitored. Access is granted based on role and need. Visitor access is logged and escorted. |
| **System Applicability** | Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Physical access policy; access log (or badge system report) |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | For on-prem clients: verify badge/key system, locked server rooms, visitor escort policy. For cloud-only clients: inheritance from cloud provider's physical security (document SOC 2 report). For MSP's own facility: same controls apply to client backup media. |
| **Tool Binding** | Client's physical security system; Cloud provider SOC 2 (inheritance) |

### PE-002: Environmental Controls

| **Control ID** | PE-002 |
| **Action Statement** | Facilities housing in-scope systems have environmental controls: temperature, humidity, fire suppression, and power protection (UPS + generator). Controls are monitored and tested. |
| **System Applicability** | Physical |
| **Owning Pillar** | Governance |
| **Named Evidence** | Environmental monitoring logs; UPS/generator test records |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | For on-prem clients with server rooms: verify UPS capacity, generator test schedule, temperature monitoring. For cloud-only: inheritance. Flag: if the client's "server room" is a closet with no cooling and a $50 UPS, document as a finding. |
| **Tool Binding** | Client's environmental monitoring; Cloud provider SOC 2 |

### PE-003: Monitoring Physical Access

| **Control ID** | PE-003 |
| **Action Statement** | Physical access to facilities is monitored. Access events are logged and reviewed. Unauthorized access attempts are investigated. |
| **System Applicability** | Physical, Data |
| **Owning Pillar** | Governance |
| **Named Evidence** | Access log review records; incident reports for unauthorized access |
| **Minimum Frequency** | Quarterly review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Minimum: door access log, reviewed quarterly. For higher-security: cameras at entry points, motion sensors, 24/7 monitoring (or review of footage after-hours). Cloud: inheritance. |
| **Tool Binding** | Client's physical security system; Cloud provider SOC 2 |

---

## 14. Planning (PL)

### PL-001: System Security Plan

| **Control ID** | PL-001 |
| **Action Statement** | A System Security Plan (SSP) exists for the in-scope environment. The SSP describes system boundaries, security controls, implementation status, and interconnection with other systems. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | System Security Plan document |
| **Minimum Frequency** | Annual review |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | For SMB clients: a single SSP covering the core IT environment. Contents: system description, boundary diagram, control implementation status (this baseline mapped to the environment), interconnection table, responsible parties. |
| **Tool Binding** | ServiceNow GRC (document management) |

### PL-002: Architecture Documentation

| **Control ID** | PL-002 |
| **Action Statement** | The in-scope system architecture is documented. Documentation includes: network topology, data flows, trust boundaries, external connections, and security tool placement. |
| **System Applicability** | Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Architecture diagram; data flow diagram |
| **Minimum Frequency** | Quarterly review; update on change |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Maintain architecture diagram in Hudu. Minimum: internet → firewall → LAN/VLANs, with servers, workstations, cloud connections, and security tools labeled. Update when anything changes. An outdated diagram is worse than no diagram. |
| **Tool Binding** | Hudu, Draw.io / Lucidchart |

### PL-003: Rules of Behavior

| **Control ID** | PL-003 |
| **Action Statement** | Users of in-scope systems acknowledge rules of behavior before being granted access. Rules cover acceptable use, data handling, security responsibilities, and consequences of violation. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Signed rules of behavior acknowledgments |
| **Minimum Frequency** | On hire; annual reaffirmation |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Include in employee handbook or new-hire onboarding. Annual reaffirmation via training platform. Signed PDF stored in HR system or Hudu. |
| **Tool Binding** | KnowBe4, HRIS, Hudu |

---

## 15. Personnel Security (PS)

### PS-001: Personnel Screening

| **Control ID** | PS-001 |
| **Action Statement** | Personnel with access to in-scope systems undergo background screening before access is granted. Screening level is appropriate to the sensitivity of the data and systems accessed. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Screening policy; screening completion records (high-level confirmation, not detailed results) |
| **Minimum Frequency** | Pre-hire; re-screening per policy (typically 3-5 years) |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Minimum for IT staff: criminal background check, employment verification. For CMMC-regulated: adds citizenship verification. Document that screening occurred — don't store detailed results in client systems. |
| **Tool Binding** | Client's HR/background check provider |

### PS-002: Personnel Termination

| **Control ID** | PS-002 |
| **Action Statement** | Upon termination of employment, access to all systems is revoked within 24 hours. Physical access is revoked. Company equipment is recovered. Exit interview covers security obligations. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Termination checklist; access revocation confirmation |
| **Minimum Frequency** | Per termination event |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Ideally automated via HRIS → IdP deprovisioning. Manual: termination checklist covers all systems. Critical: disable IdP account first (this cascades to SSO apps). Then: VPN, email, remote access, physical access. Confirm within 24 hours. |
| **Tool Binding** | Okta/Entra ID, HRIS |

### PS-003: Personnel Transfer

| **Control ID** | PS-003 |
| **Action Statement** | When personnel change roles, access is reviewed and adjusted to match the new role within 5 business days. Old access is removed; new access is granted only as needed. |
| **System Applicability** | Process |
| **Owning Pillar** | Governance |
| **Named Evidence** | Role change access review records |
| **Minimum Frequency** | Per transfer event |
| **Subordinate Standard** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) |
| **MSP Implementation Note** | Trigger: HR system or manager notifies of role change → review all group memberships and app assignments → remove old, add new → document. Use IdP group-based access to make this scalable (change group = change access everywhere). |
| **Tool Binding** | Okta/Entra ID |

---

## 16. Risk Assessment (RA)

### RA-001: Risk Assessment

| **Control ID** | RA-001 |
| **Action Statement** | A risk assessment of the in-scope environment is conducted at least annually. The assessment identifies threats, vulnerabilities, likelihood, impact, and resulting risk level. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Risk assessment report |
| **Minimum Frequency** | Annual |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | Annual CERG Assessment engagement covers this. Deliverables: risk register with scored risks, threat analysis, vulnerability correlation. Start with the top 10 risks — don't try to enumerate 200 low-probability scenarios. Focus on what could actually hurt the business. |
| **Tool Binding** | ServiceNow GRC (risk module) |

### RA-002: Vulnerability Scanning

| **Control ID** | RA-002 |
| **Action Statement** | In-scope systems are scanned for vulnerabilities at defined intervals. Results are triaged, prioritized, and remediated per defined SLAs. Exceptions are tracked in the risk register. |
| **System Applicability** | Hardware, Software, Network, Cloud |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vulnerability scan report; remediation log |
| **Minimum Frequency** | Weekly (external), Monthly (internal) |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | See [MSP Runbook](../practice-assets/msp-runbook-v1.md) RA-005 section. Tenable authenticated scans weekly (external) and monthly (internal). Critical vulns: 7 days. High: 30 days. Medium: 90 days. |
| **Tool Binding** | Tenable/Nessus |

### RA-003: Risk Register

| **Control ID** | RA-003 |
| **Action Statement** | A risk register tracks all identified risks: threat, vulnerability, likelihood, impact, inherent risk, treatment (accept/mitigate/transfer/avoid), residual risk, owner, and review date. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Current risk register export |
| **Minimum Frequency** | Monthly review; continuous update |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | ServiceNow GRC: risk module. Vanta: risk register. Minimum fields per risk entry: ID, description, threat source, affected assets, likelihood (1-5), impact (1-5), inherent risk score, treatment, residual risk, owner, target review date. Review monthly. |
| **Tool Binding** | ServiceNow GRC, Vanta |

### RA-004: Risk Acceptance

| **Control ID** | RA-004 |
| **Action Statement** | When a risk cannot be mitigated or transferred, it is formally accepted by the appropriate authority. Risk acceptances have an expiration date (maximum 12 months), documented compensating controls, and an approving signature. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Signed risk acceptance documents |
| **Minimum Frequency** | Per acceptance; review on expiration |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | The risk acceptance template: (1) What risk are we accepting? (2) Why can't we fix it now? (3) What compensating controls reduce the risk? (4) When does this acceptance expire? (5) Who's signing? The signer should be the business owner, not IT — it's a business decision. |
| **Tool Binding** | ServiceNow GRC (risk acceptance workflow) |

### RA-005: Threat Intelligence Integration

| **Control ID** | RA-005 |
| **Action Statement** | The risk assessment process incorporates current threat intelligence. Emerging threats relevant to the client's industry and technology stack are reviewed and risk-assessed at least quarterly. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Threat intelligence review notes; risk register updates based on threat intel |
| **Minimum Frequency** | Quarterly |
| **Subordinate Standard** | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **MSP Implementation Note** | Subscribe to: CISA alerts, MS-ISAC (state/local gov), vendor advisories (Fortinet, Microsoft, SentinelOne). Quarterly review: any new threat that applies to our clients? Add to risk register if relevant. Sector-specific: healthcare clients = HHS alerts, financial = FS-ISAC, energy = E-ISAC. |
| **Tool Binding** | CISA, vendor advisories, ISAC memberships |

---

## 17. System and Services Acquisition (SA)

### SA-001: Security Requirements in Procurement

| **Control ID** | SA-001 |
| **Action Statement** | Security requirements are included in RFPs, contracts, and vendor selection criteria for all system and service acquisitions. Vendors are evaluated against CERG control requirements before purchase. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Security requirements in RFP/contract; vendor evaluation checklist |
| **Minimum Frequency** | Per acquisition |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | Before buying any new tool/service: (1) Does it integrate with our stack? (2) Does it have an API for ServiceNow/Vanta? (3) Does it support MFA? (4) Does it have a SOC 2 or ISO 27001 report? (5) Can we manage it multi-tenant for MSP? Score each vendor. Reject if they fail on 2+ criteria. |
| **Tool Binding** | ServiceNow GRC (vendor risk module) |

### SA-002: Software Development Security

| **Control ID** | SA-002 |
| **Action Statement** | Custom-developed software follows secure development practices. Code is reviewed, tested for security flaws, and scanned for vulnerabilities before deployment. |
| **System Applicability** | Software, Process |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Secure coding policy; code review records; SAST/SCA scan results |
| **Minimum Frequency** | Per release |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | For clients who write custom code: add Semgrep to CI/CD pipeline. Block merges on high-severity findings. For MSP-developed scripts/automation: peer review before production deployment. |
| **Tool Binding** | Semgrep, Trivy |

### SA-003: Supply Chain Risk Management

| **Control ID** | SA-003 |
| **Action Statement** | Third-party software and services are assessed for supply chain risk before acquisition. SBOMs are collected for critical software. Vendor security posture is reviewed annually. |
| **System Applicability** | Process, Software |
| **Owning Pillar** | Risk |
| **Named Evidence** | Vendor risk assessment; SBOM inventory |
| **Minimum Frequency** | Pre-acquisition; annual vendor review |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | For critical software (firewalls, backup, EDR, SIEM): collect SBOMs. For all vendors: annual SOC 2 review. Flag any vendor who won't provide a SOC 2 or who has had a breach in the last 12 months without remediation. |
| **Tool Binding** | Trivy (SBOM generation), ServiceNow GRC (vendor risk) |

### SA-004: Development Environment Security

| **Control ID** | SA-004 |
| **Action Statement** | Development and testing environments are separate from production. Production data is not used in development without sanitization. Development access does not grant production access. |
| **System Applicability** | Software, Cloud |
| **Owning Pillar** | Engineering |
| **Named Evidence** | Environment separation documentation; data sanitization procedure |
| **Minimum Frequency** | Annual review |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | Separate dev/test/prod in different networks or cloud accounts. No production credentials in dev. No production data in dev without scrubbing (remove PII, replace with dummy data). Developers do not have admin access to production. |
| **Tool Binding** | Cloud IAM (AWS Organizations, Azure Management Groups), Git branching strategy |

### SA-005: Outsourced Development

| **Control ID** | SA-005 |
| **Action Statement** | When software development is outsourced, the contract requires adherence to the client's security standards. Deliverables are scanned for vulnerabilities before acceptance. Source code and build artifacts are escrowed or delivered. |
| **System Applicability** | Process |
| **Owning Pillar** | Risk |
| **Named Evidence** | Contract with security requirements; acceptance test results |
| **Minimum Frequency** | Per outsourced development engagement |
| **Subordinate Standard** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) |
| **MSP Implementation Note** | Contract clause: "Developer shall adhere to CERG-STD-IT-001 Section X. Code will be scanned with Semgrep and Trivy. SBOM will be delivered with each release. Source code will be delivered to client upon termination." Scan every delivery before accepting it. |
| **Tool Binding** | Semgrep, Trivy |


---

## 18. System and Communications Protection (SC)

### SC-001: Network Segmentation
Network segmented to isolate critical systems, restrict lateral movement, separate trust zones. VLANs for servers, workstations, guest, DMZ. OT physically/logically isolated from IT. | Network | Engineering | Network diagram, firewall ruleset | Quarterly | Fortinet, VLANs

### SC-002: Boundary Protection
Firewalls restrict traffic to authorized ports/protocols. Default-deny inbound/outbound. Rules reviewed quarterly. | Network | Engineering | Firewall config export, review log | Quarterly | Fortinet

### SC-003: Encryption at Rest
Sensitive data at rest encrypted. Keys managed separately. | Hardware, Software, Cloud, Data | Engineering | Encryption config, key management procedure | Quarterly | BitLocker, Cloud encryption

### SC-004: Encryption in Transit
TLS 1.2+ required. Legacy protocols disabled. | Network, Cloud, Software | Engineering | TLS scan report | Quarterly | Qualys SSL Labs, Nmap

### SC-005: VoIP Protection
VoIP isolated on separate VLAN. Default credentials changed. | Network, Hardware | Engineering | VoIP config, credential log | Quarterly | Fortinet, VoIP PBX

### SC-006: Wireless Security
WPA2-Enterprise with 802.1X. No PSK for corporate. Guest isolated. | Network | Engineering | Wireless config | Quarterly | Fortinet, RADIUS/NPS

### SC-007: Mobile Device Security
MDM enforced: screen lock, encryption, min OS, remote wipe. | Hardware, Software | Engineering | MDM policy, compliance report | Monthly | Microsoft Intune, Jamf

### SC-008: DNS Security
DNS filtering blocks malicious domains. Internal DNS hardened. | Network | Engineering | DNS config, filtering policy | Quarterly | Fortinet, Cisco Umbrella

---

## 19. System and Information Integrity (SI)

### SI-001: Malware Protection
Anti-malware deployed. Real-time protection. Auto-update. Coverage monitored. | Hardware, Software | Risk | EDR dashboard | Monthly | SentinelOne

### SI-002: Vulnerability Monitoring
New vulns assessed within 24h. CISA KEV, vendor advisories monitored. | Hardware, Software, Cloud | Risk | Advisory review log | Weekly | Tenable, CISA KEV

### SI-003: File Integrity Monitoring
Critical files monitored for unauthorized changes. Alerts generated. | Software | Risk | FIM config, alert log | Continuous | Wazuh, SentinelOne

### SI-004: Detection Engineering
Sigma rules deployed, ATT&CK mapped. Tested with Atomic Red Team. Gaps documented. | Software, Process | Risk | Rule inventory, test results | Monthly | Sigma, ART, Elastic/Wazuh

### SI-005: Email Security
SPF/DKIM/DMARC enforced. Safe Links/Attachments. Phish investigated. | Software, Cloud | Risk | Email config, phish metrics | Monthly | M365 Defender, Proofpoint

### SI-006: Web Filtering
Web traffic filtered for malicious/phishing/inappropriate sites. | Network, Software | Risk | Filtering config | Monthly | Fortinet, SentinelOne

### SI-007: Data Loss Prevention
DLP for email, cloud, endpoints. Sensitive data exfiltration blocked. | Data, Cloud | Risk | DLP config, incident log | Quarterly | Microsoft Purview, SentinelOne

### SI-008: Application Security Testing
Web apps tested for vulns. Critical remediated before production. | Software | Engineering | App test report | Per release | OWASP ZAP, Burp Suite

---

## 20. Supply Chain Risk Management (SR)

### SR-001: Software Bill of Materials
SBOM collected for critical software. Components, versions, vulns tracked. | Software | Risk | SBOM inventory | Per acquisition | Trivy

### SR-002: Vendor Risk Assessment
Vendors assessed: posture, history, compliance, data handling. | Process | Risk | Vendor assessment, tier list | Annual (critical) | ServiceNow GRC

### SR-003: Trusted Software Sources
Software from trusted sources only. Integrity verified before install. | Software | Engineering | Approved source list | Per acquisition | SentinelOne

### SR-004: Hardware Supply Chain
Hardware from authorized resellers. Counterfeit/tampered rejected. | Hardware | Risk | Authorized reseller list | Per acquisition | Reseller agreements

---

## 21. Program Management (PM)

### PM-001: Information Security Program Plan
Documented plan: scope, org structure, roles, resources, metrics. | Process | Governance | Program plan document | Annual | ServiceNow GRC

### PM-002: Senior Security Officer
Named individual accountable for program. Budget authority. | Process | Governance | Appointment/org chart | Annual | None (organizational)

### PM-003: Security Metrics Program
Performance measured. Reported to leadership. Improves program. | Process | Governance | Metrics dashboard | Monthly/Quarterly | ServiceNow GRC, Elastic/Wazuh

### PM-004: Continuous Improvement
Program reviewed and improved. Lessons learned feed updates. | Process | Governance | Review minutes, action items | Quarterly | ServiceNow GRC, HaloPSA

---

## 22. Document Control

### Control Count Summary

| Family | Controls |
|--------|----------|
| AC — Access Control | 8 |
| AT — Awareness and Training | 3 |
| AU — Audit and Accountability | 7 |
| CA — Assessment, Authorization, Monitoring | 5 |
| CM — Configuration Management | 8 |
| CP — Contingency Planning | 5 |
| IA — Identification and Authentication | 5 |
| IR — Incident Response | 5 |
| MA — Maintenance | 3 |
| MP — Media Protection | 3 |
| PE — Physical and Environmental | 3 |
| PL — Planning | 3 |
| PS — Personnel Security | 3 |
| RA — Risk Assessment | 5 |
| SA — System and Services Acquisition | 5 |
| SC — System and Communications Protection | 8 |
| SI — System and Information Integrity | 8 |
| SR — Supply Chain Risk Management | 4 |
| PM — Program Management | 4 |
| **Total** | **97** |

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | cragin-security | Initial release: 97 controls across 19 families |

### Review Triggers

- Quarterly review against threat intelligence and regulatory changes
- Re-review if upstream CERG CB-001 is updated
- Re-review on major tool stack changes (vendor acquisition, breach, EOL)

### Related Documents

- [Upstream CERG Unified Control Baseline](CERG-GOV-CB-001_Unified_Control_Baseline.md)
- [Opinionated Tool Matrix](../practice-assets/tools/opinionated-tool-matrix-v1.md)
- [MSP Runbook](../practice-assets/msp-runbook-v1.md)
- [GRC Rollout Guide](../practice-assets/tools/grc-rollout-v1.md)
- [Engagement Playbook](../practice-assets/engagement-playbook-v1.md)
