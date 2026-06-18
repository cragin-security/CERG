## EMAIL AND MESSAGING SECURITY STANDARD
### Email Authentication · Anti-Phishing · Inbound and Outbound Protection · Collaboration Tools

---

| | |
|---|---|
| **Document ID** | CERG-STD-MSG-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) · [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Review Cycle** | Annual / On material change to the email or collaboration platform |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (SC, SI, AC families) · [NIST 800-177](https://csrc.nist.gov/pubs/sp/800/177/r1/final) (Trustworthy Email) · [CIS Controls v8](https://www.cisecurity.org/controls) (Control 9) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (PROTECT, DETECT) |
| **Regulations** | CMMC L2 / 800-171r3 (3.13.x, 3.14.x) · SOX ITGC · privacy regimes where applicable |
| **Environments** | All CERG-managed email and messaging: corporate email, business collaboration and messaging platforms |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Email Authentication](#3-email-authentication)
4. [Inbound Email Protection](#4-inbound-email-protection)
5. [Anti-Phishing](#5-anti-phishing)
6. [Outbound Email and Data Protection](#6-outbound-email-and-data-protection)
7. [Mailbox and Account Security](#7-mailbox-and-account-security)
8. [Collaboration and Messaging Platforms](#8-collaboration-and-messaging-platforms)
9. [Monitoring and Detection](#9-monitoring-and-detection)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

Email is the most attacked surface in nearly every organization. It is how most phishing arrives, how most credentials are stolen, how most business email compromise begins, and how a great deal of data quietly leaves. The IT, Access, and Data Governance standards each touch email at the edges; none of them owns it. This standard does.

This standard establishes the requirements for email and messaging security across CERG-managed environments: how email is authenticated so the organization's domain cannot be trivially impersonated, how inbound email is filtered, how the organization defends against phishing, how outbound email is protected against data loss, how mailboxes are secured, and how business collaboration and messaging platforms are governed.

It applies to corporate email and to the business messaging and collaboration platforms CERG-managed teams use. It does not govern incident response to a successful email-borne compromise, which is the standing Incident Response team's, per [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4; CERG provides the detections and the telemetry.

> **Email Security Is Mostly About Two Directions**
>
> Email security comes down to two questions. Inbound: can a hostile message reach an employee, and if it does, can the employee tell? Outbound: can sensitive data leave in an email, and can the organization's own domain be used to attack others? Almost every control in this standard serves one of those two directions. A program that filters inbound well and ignores outbound has done half the job.

---

## 2. Principles

1. **Authenticate the domain.** The organization's email domains are configured so that mail claiming to be from them can be verified, and forgeries can be rejected. An unauthenticated domain is a free tool for every attacker.
2. **Filter before the inbox.** Hostile and unwanted mail is stopped before it reaches a person wherever a machine can judge it. Human vigilance is the last layer, not the first.
3. **Assume some phishing gets through.** No filter is perfect. The program prepares employees to recognize and report what gets through, and prepares to respond when someone clicks.
4. **A reported phish is a gift.** An employee who reports a suspicious message is doing security work. Reporting is made easy, and reporting is never punished, even when the employee also clicked.
5. **Outbound is a data-loss path.** Email is one of the most common ways sensitive data leaves. Outbound email is governed by the data classification scheme.
6. **Messaging platforms are email's equal.** Business chat and collaboration platforms carry the same data and the same attacks as email and are governed with the same seriousness.

---

## 3. Email Authentication

The organization's email domains, including domains that are owned but not used to send mail, are configured with the three standard email authentication mechanisms.

1. **SPF.** A Sender Policy Framework record is published for every sending domain, listing the authorized sources of mail for that domain.
2. **DKIM.** DomainKeys Identified Mail signing is enabled so that outbound mail carries a verifiable cryptographic signature. DKIM keys are managed per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md).
3. **DMARC.** A Domain-based Message Authentication, Reporting and Conformance policy is published. The DMARC policy is moved to an enforcing posture (reject, or at minimum quarantine) once SPF and DKIM are confirmed correct. A DMARC policy left permanently at "none" provides reporting but no protection and is not the end state.
4. **Parked domains are locked down.** Owned domains that send no mail publish records that tell the world they send no mail, so they cannot be impersonated.
5. **Inbound authentication is enforced.** The organization checks SPF, DKIM, and DMARC on inbound mail and acts on the results, so that other organizations' authentication protects the organization's people.

> **DMARC at "none" Is a Smoke Detector With No Battery**
>
> Publishing a DMARC record in monitoring-only mode is a common and reasonable first step. Leaving it there forever is not. A DMARC policy at "none" tells the organization who is forging its domain but tells the receiving world to deliver the forgeries anyway. The protection only exists once the policy enforces. CERG treats reaching an enforcing DMARC policy as the completion of this control, and a domain stuck at "none" for longer than the rollout reasonably needs as a finding.

---

## 4. Inbound Email Protection

1. **Inbound mail is filtered.** Inbound email passes through filtering that screens for malware, malicious links, known-bad senders, and spam before delivery.
2. **Attachments are inspected.** Attachments are scanned for malware. High-risk attachment types are blocked or neutralized by default; exceptions are recorded.
3. **Links are protected.** Links in inbound mail are evaluated, and protection is applied at the time the user clicks, not only at the time the mail is delivered, because a link can be made malicious after delivery.
4. **External mail is marked.** Mail originating outside the organization is visibly marked, so an employee can see at a glance that a message claiming to be from a colleague actually came from outside.
5. **High-risk senders are constrained.** Mail that impersonates internal senders, executive names, or known partners is detected and constrained. Lookalike-domain and display-name impersonation are explicit detection targets.
6. **Quarantine is managed.** Quarantined mail is handled through a defined process. Users can see and request release of their own quarantined mail; release of mail that failed a security check is reviewed.

---

## 5. Anti-Phishing

Filtering reduces phishing. It does not eliminate it. This section covers what the program does about the phishing that reaches a person.

1. **Reporting is one action.** Employees have a single, obvious way to report a suspicious message, and using it takes one action. A reporting mechanism that is hard to find is not used.
2. **Reports are triaged.** Reported messages are triaged on a defined cadence. A confirmed malicious message is removed from any other inbox it reached, and its indicators feed detection per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).
3. **Reporting is never punished.** An employee who reports a message they also interacted with is thanked, not disciplined. Punishing the honest report teaches everyone else to stay silent, which is the opposite of the goal.
4. **Phishing simulation is constructive, not a trap.** Where the organization runs phishing simulations, they are run to measure and improve, not to shame individuals. Results are used in aggregate. An employee who fails a simulation is offered help, not humiliation.
5. **A click triggers response, not blame.** When an employee clicks a real phish or enters credentials, the response is immediate and procedural: contain the account, reset the credential per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md), and hand off to the Incident Response team. The employee who reported their own mistake made the response possible.

> **The Organization That Punishes Clicks Goes Blind**
>
> If clicking a phishing link, or admitting to it, gets an employee in trouble, employees stop admitting it. The credential theft still happened; the organization just does not hear about it until the attacker is well inside. Every hour between the click and the report is the attacker's. CERG makes reporting effortless and consequence-free precisely so that the organization hears about the click in minutes, not weeks. A blame-free reporting culture is a security control, and it is one of the most valuable in this standard.

---

## 6. Outbound Email and Data Protection

1. **Outbound email is a governed data path.** Email is one of the realistic exfiltration paths named in [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) §9, and data loss prevention covers it.
2. **Sensitive data outbound is constrained.** Email carrying Confidential or Restricted data outside the organization is monitored and, where it is unauthorized, blocked or quarantined, per the handling table in [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) §6.
3. **Sensitive mail is encrypted.** Email carrying Confidential or Restricted data to external recipients is encrypted, using the mechanisms approved in [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md).
4. **Auto-forwarding to external addresses is controlled.** Automatic forwarding of mail to external addresses is disabled by default. It is a classic data-exfiltration and account-compromise technique. Exceptions are recorded.
5. **Mass and unusual sending is detected.** A mailbox suddenly sending at volume, or sending to many external recipients, is a signal of a compromised account or an insider exfiltrating data, and is detected (Section 9).

---

## 7. Mailbox and Account Security

1. **Email accounts are protected by strong authentication.** Access to email requires multi-factor authentication per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md). The email account is, for most people, the reset path to every other account, so it is protected accordingly.
2. **Mailbox access is least-privilege.** Delegate and shared-mailbox access is granted on need, recorded, and reviewed on the access-review cadence.
3. **Mailbox rules are monitored.** Inbox rules that hide, delete, or forward mail are a hallmark of business email compromise. The creation of suspicious rules is detected.
4. **Legacy and weak authentication is disabled.** Email protocols that cannot enforce multi-factor authentication are disabled. They are a standing bypass of the account's protection.
5. **Email retention follows data governance.** Mailbox content is retained and disposed of per the retention schedule in [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) §8, and preserved under legal hold when one applies.

---

## 8. Collaboration and Messaging Platforms

Business chat, messaging, and collaboration platforms are governed with the same seriousness as email.

1. **Messaging platforms are sanctioned and assessed.** The collaboration and messaging platforms in use are sanctioned, and assessed as SaaS per [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md). Unsanctioned messaging tools are shadow IT.
2. **Access and authentication apply equally.** Access to messaging platforms requires the same authentication and is governed by the same access controls as email.
3. **Data classification applies in chat.** Confidential and Restricted data shared in messaging platforms is governed by [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md). Data loss prevention covers messaging where the platform supports it.
4. **External participation is controlled.** External guests, federated chat with other organizations, and public channels are controlled and visible. An external party in a channel is as significant as an external recipient on an email.
5. **Phishing happens in chat too.** Malicious links and social engineering arrive through messaging platforms. The reporting mechanism and the no-blame culture of Section 5 extend to messaging.
6. **Messaging is logged and retained.** Business messaging is logged per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) and retained per [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md).

---

## 9. Monitoring and Detection

1. **Email and messaging telemetry reaches detection.** Email security events, authentication results, and messaging-platform logs are delivered to the platform governed by [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).
2. **Detection content covers the known patterns.** Detection use cases include business email compromise indicators: suspicious inbox rules, anomalous send volume, impossible-travel sign-ins to mailboxes, mass external forwarding, and lookalike-domain mail.
3. **Reported phishing feeds detection.** Indicators from triaged user reports (Section 5) become detection content, so the next instance of the same campaign is caught by a machine.
4. **CERG detects; the IR team responds.** Consistent with [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4, CERG owns the detection content and feeds confirmed email-borne incidents to the standing Incident Response team.

---

## 10. Roles and Responsibilities

Roles below are the canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Email and Messaging Responsibility** |
|---|---|
| **Engineering Pillar Leader** | Owns this standard. Accountable for the email and messaging platforms and their security configuration. |
| **Cloud Security Engineer** | Operates the email and messaging platforms where they are SaaS; owns SPF, DKIM, DMARC configuration and the inbound and outbound filtering posture. |
| **Cryptography Engineer** | Owns DKIM key management and the encryption mechanisms for sensitive outbound mail. |
| **Identity Engineer** | Owns multi-factor authentication on email and messaging accounts and the disabling of legacy authentication. |
| **Detection Engineer** | Owns email and messaging detection content; consumes the telemetry and the reported-phish indicators. |
| **Governance Pillar Leader** | Owns the position on phishing simulation and the no-blame reporting culture; tracks email-security metrics; cross-references this standard with the control baseline. |
| **Exposure Management Lead** | Tracks vulnerabilities in email and messaging infrastructure. |
| **Policy & Standards Manager** | Maintains this document, its version, and its review cycle. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Standard** |
|---|---|---|
| NIST 800-177 | Trustworthy Email: SPF, DKIM, DMARC, transport encryption | Sections 3, 4, 6 |
| NIST 800-53r5 | SC-7, SC-8, SI-3, SI-4, SI-8, AC-4 | Sections 3, 4, 6, 9 |
| CIS Controls v8 | Control 9 (email and web browser protections) | Sections 4, 5 |
| NIST CSF 2.0 | PROTECT (PR.DS, PR.PS), DETECT (DE.CM) | Sections 4, 6, 9 |
| NIST 800-171r3 / CMMC L2 | 3.13.x (transmission protection), 3.14.x (system integrity) | Sections 3, 4, 6 |
| SOX ITGC | Email retention and access control | Sections 7, 8 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-MSG-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to the email or collaboration platform |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST 800-53r5 (SC, SI, AC); NIST 800-177; CIS Controls v8 (9); NIST CSF 2.0 (PROTECT, DETECT) |
| **Regulations** | CMMC L2 / 800-171r3; SOX ITGC; privacy regimes where applicable |
| **Environments** | All CERG-managed email and messaging |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-21 | Cyber Engineering | Initial release. Establishes email authentication (SPF, DKIM, DMARC to an enforcing policy), inbound email protection, anti-phishing built on effortless blame-free reporting, outbound email and data protection, mailbox and account security, governance of collaboration and messaging platforms, and email and messaging monitoring feeding the detection platform. |

### Review Triggers

- Material change to the email or collaboration and messaging platform
- Revision of NIST 800-177 or relevant NIST 800-53 controls
- A significant phishing or business email compromise incident
- Internal audit or regulatory finding affecting email security
- Direction from the CISO

Cyber Engineering owns this document. The Engineering Pillar Leader (Platforms) is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| IT / Cloud / SaaS Security Standard | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Email and messaging platforms assessed as SaaS |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Multi-factor authentication; credential reset on a click |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Outbound data loss prevention; retention |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | DKIM keys; sensitive-mail encryption |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Email and messaging detection content and telemetry |
| Operating Model | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | CERG detects; the standing IR team responds |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `MSG` domain |
