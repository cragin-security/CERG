
# SURGE: Cyber Engineering, Risk & Governance

## ACCESS MANAGEMENT STANDARD
### Identity · Authentication · Authorization · Lifecycle

---

| | |
|---|---|
| **Document ID** | CERG-STD-AC-001 |
| **Version** | 1.21 |
| **Status** | Published |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Identity & Access) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Significant Change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-63](https://pages.nist.gov/800-63-3/)-3 (B/C) · [NIST 800-171r2](https://csrc.nist.gov/pubs/sp/800/171/r2/final) · NIST RMF |
| **Regulations** | NERC-CIP · [CMMC L2](https://dodcio.defense.gov/CMMC/) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · HIPAA (where applicable) |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [CERG Roles in Access Management](#2-cerg-roles-in-access-management)
3. [Identity Foundation](#3-identity-foundation)
4. [Authentication](#4-authentication)
5. [Authorization](#5-authorization)
6. [Privileged Access Management](#6-privileged-access-management)
7. [Remote, Vendor, and Third-Party Access](#7-remote-vendor-and-third-party-access)
8. [Identity Lifecycle (Joiner / Mover / Leaver)](#8-identity-lifecycle-joiner--mover--leaver)
9. [Access Review and Recertification](#9-access-review-and-recertification)
10. [Monitoring, Logging, and Detection](#10-monitoring-logging-and-detection)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Exceptions and Escalation](#12-exceptions-and-escalation)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

This standard implements the foundational principles established in **[CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md)** for identity, authentication, authorization, and the full access lifecycle. It defines specific, measurable requirements that apply to every in-scope asset, regardless of system class, environment, or trust level.

Access management is the connective tissue between every other security control. A perfectly hardened system is no more secure than the worst credential authorized to log into it. A perfectly classified data store is no more protected than the weakest authorization rule that permits read access. This standard treats identity as the primary enforcement layer it has become.

### 1.1 Scope

This standard applies to:

- All workforce identities (employees, contractors, consultants) accessing organizational systems
- All system, service, and application identities (machine identities, workload identities, API credentials)
- All third-party identities (vendors, integrators, customers, partners) with access to organizational systems
- All authentication and authorization decisions across owned, hybrid, cloud, SaaS, and OT environments
- All credentials, secrets, keys, tokens, and certificates used to authenticate or authorize access

### 1.2 Standard Versus Subordinate Detail

This standard establishes the requirements. Specific implementation details, IdP configuration baselines, MFA enrollment procedures, PAM workflows, access review run-books, are maintained as procedures and platform guides linked from this document. Where a subordinate procedure conflicts with this standard, this standard governs.

### 1.3 Relationship to Parent Policy and Peer Standards

This standard is subordinate to **[CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md)** and operates alongside the IT ([CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md)), OT ([CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)), and CUI ([CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md)) standards. Where any peer standard imposes more stringent access requirements for a specific environment or data class (e.g., NERC-CIP CIP-004 for BES Cyber Systems, 800-171 3.5 for CUI), the more stringent requirement controls.

---

## 2. CERG Roles in Access Management

| **CERG Pillar** | **Access Management Responsibilities** |
|---|---|
| **Engineering** | Designs, implements, and maintains identity platforms - IdP, directory, MFA, SSO, federation, PAM, secrets management, and certificate authorities. Builds joiner / mover / leaver automations. Maintains identity-related infrastructure-as-code, conditional access policies, and platform-level access controls. |
| **Risk** | Operates continuous identity threat detection (UEBA, identity provider risk signals, privileged session monitoring). Conducts identity-focused adversarial testing. Maintains the identity-risk view in the risk register: stale accounts, excessive privileges, MFA bypass paths, dormant service accounts. |
| **Governance** | Owns this standard and all access management procedures. Operates the access review and recertification program. Maintains role definitions, segregation-of-duties (SoD) policies, and approval matrices. Produces access-control evidence for [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), and other regulatory regimes. Coordinates access-related findings during audits. |

> **The "Every Door, Every Time" Standard**
>
> Strong access control is not selective. An MFA prompt that can be bypassed once, through legacy protocols, an unmanaged endpoint, or an exception with no expiration, is not a strong control; it is a control with a documented bypass. CERG measures access maturity by the absence of exceptions, not by the strength of the primary path.

---

## 3. Identity Foundation

### 3.1 Authoritative Identity Sources

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Maintain an authoritative source for each identity class: HRIS for employees, a contractor management system for contractors, an asset / configuration system for machine identities, and a vendor management record for third-party identities. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-4, AC-2 |
| Provision and deprovision workforce accounts only from authoritative sources via automated workflows. Manual account creation is an exception case requiring documented justification. | Engineering | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(1) |
| Reconcile downstream systems (IdP, directory, applications) with authoritative sources on at least a daily cadence. Discrepancies are flagged and resolved within defined SLAs. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(4), CA-7 |

### 3.2 Identity Federation and SSO

| **Requirement**                                                                                                                                                                                                                         | **CERG Owner**           | **Regulatory Reference**               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | -------------------------------------- |
| All in-scope applications shall integrate with the central identity provider via SSO (SAML, OIDC, or equivalent) where technically supported. Local-account-only applications require a documented exception and compensating controls. | Engineering              | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-2, IA-8 · [NIST 800-63](https://pages.nist.gov/800-63-3/)-3 |
| Identity federation to third parties (partners, customers, vendors) shall be approved by Engineering and Governance, scoped to the minimum necessary, and reviewed annually.                                                            | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-8, CA-3                 |
| Where SSO is not technically feasible, local accounts shall be uniquely identified, MFA-enforced, and included in the access review program.                                                                                            | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(7), IA-2              |

### 3.3 Identity Classes

The organization recognizes the following identity classes. Controls in this standard apply to all classes; specific provisions are noted where they differ.

| **Class** | **Definition** | **Primary Controls** |
|---|---|---|
| **Workforce - Employee** | Permanent or fixed-term employees of the organization. | HR-driven lifecycle, full MFA, conditional access, role-based authorization. |
| **Workforce - Contractor / Consultant** | Non-employee individuals performing work on the organization's behalf. | Contractor-system lifecycle, sponsor accountability, fixed end-dates, MFA, narrower authorization scope. |
| **Privileged Administrator** | Workforce identities with elevated rights to platforms, systems, or data classes. | All workforce controls, plus PAM-managed credentials, JIT elevation, session recording, dedicated privileged workstation where required. |
| **Service / Machine Identity** | Non-human identities (service accounts, managed identities, workload identities) authenticating to systems and APIs. | Secrets manager custody, no interactive login, scoped permissions, rotation policy, ownership, expiration. |
| **Vendor / Third-Party** | Identities belonging to external organizations with access to organizational systems. | Federation or sponsored accounts, scope-limited, time-bound, monitored, contractually obligated. |
| **Break-Glass / Emergency** | Highly privileged identities reserved for emergency access when normal mechanisms are unavailable. | Vaulted credentials, dual control, alarmed use, post-use review, documented procedure. |

---

## 4. Authentication

### 4.1 Multi-Factor Authentication

> **Phishing-Resistant by Default for Anything That Matters**
>
> SMS and voice MFA are no longer sufficient for privileged access or for anything that holds Restricted-tier data. [NIST 800-63](https://pages.nist.gov/800-63-3/)-3 retired SMS as a restricted authenticator. The standard for administrative paths is phishing-resistant authentication, FIDO2/WebAuthn, platform authenticators, or smart cards. TOTP and push remain acceptable for general workforce access where conditional access policies provide compensating signals.

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Enforce MFA for all remote access, all access to privileged functions, and all access to systems classified Confidential or Restricted, regardless of network location. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-2(1), IA-2(2), IA-2(11) |
| Use phishing-resistant authenticators (FIDO2, platform authenticators, PIV / CAC, or equivalent) for: privileged roles in any environment, root / global-admin accounts, all CUI-system access ([CMMC L2](https://dodcio.defense.gov/CMMC/) expectation), and all break-glass paths. | Engineering | [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B AAL3 · [CMMC](https://dodcio.defense.gov/CMMC/) IA.L2-3.5.3 |
| For non-privileged workforce access, MFA shall be enforced via methods that meet [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B AAL2 or higher. SMS / voice methods are not acceptable as the sole second factor for new enrollments. | Engineering | [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B AAL2 |
| Service-to-service and workload-to-service authentication shall use platform-issued credentials (managed identities, workload identities, mTLS) where technically available; long-lived static API keys are an exception case. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-9 · [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B |
| Authentication failures, lockouts, and MFA bypass events shall be logged and alerted on. Account-lockout thresholds and durations are defined in the IdP baseline. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-7, AU-2 |

### 4.2 Credential Management

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| All credentials (passwords, keys, tokens, certificates) shall meet the cryptographic strength requirements defined in the IdP / cryptographic standard. Legacy algorithms (e.g., MD5, SHA-1, weak cipher suites) shall be disabled wherever technically possible. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-5 · [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B |
| Default and vendor-supplied credentials shall be changed before deployment or first connection of any system to organizational networks. Detection of unchanged defaults is a Critical finding. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-5(1) · NERC-CIP CIP-007 R5.5 |
| Workforce passwords shall meet the organization's password policy aligned with [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B. Periodic forced rotation is not required unless a compromise is suspected; passwords shall be screened against known-compromised lists at set / reset. | Engineering | [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B §5.1.1 |
| Shared accounts are prohibited. Where a vendor or vendor product requires a shared credential, document the exception, vault the credential under PAM, and apply session-attribution monitoring. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-2, AC-2 · NERC-CIP CIP-007 R5.1 |
| Secrets, API keys, and certificates shall be stored in an approved secrets management platform with rotation, access logging, and least-privilege retrieval. Plaintext secrets in source repositories, configuration files, IaC, container images, or chat tools are prohibited. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-5(7) · OWASP ASVS |

### 4.3 Session Management

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Enforce session inactivity timeouts and absolute session lifetimes appropriate to the sensitivity of the system. Privileged sessions and Restricted-data systems use shorter limits than general workforce systems. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-11, AC-12 |
| Bind sessions to device posture where supported. Sessions established on noncompliant devices for sensitive paths shall be terminated automatically. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-12(1), IA-2(12) |
| Provide session revocation capability for the IdP and for Tier 1 SaaS / cloud control planes. Compromise response shall be able to invalidate sessions globally within minutes. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-12, IR-4 |

---

## 5. Authorization

### 5.1 Least Privilege

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Grant access strictly on the basis of least privilege - the minimum required to perform an authorized function. New roles and entitlements shall be reviewed for least-privilege adherence before approval. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.5 |
| Default to deny. Network, application, and platform authorization defaults shall be deny-by-default with explicitly authorized exceptions. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-3 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.3 |
| Authorization shall reference role, attribute, or policy - not user identity alone. Identity-only authorization (entitlements assigned directly to a user without role/group/policy abstraction) is restricted to documented exceptions. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-3 · [NIST CSF](https://www.nist.gov/cyberframework) PR.AA |

### 5.2 Role and Group Design

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Maintain documented role definitions for in-scope applications and platforms. Each role specifies entitlements, intended use, and owner. Roles are reviewed annually and upon material application change. | Governance / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| Segregation of duties (SoD) policies shall be defined for systems supporting financial reporting, payment processing, regulated operational activities, and security-control configuration. SoD violations are detected and remediated as part of the access review program. | Governance / Engineering | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-5 |
| Role and group assignments shall be made through a documented request and approval workflow with line-manager and resource-owner approvals as appropriate. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(1) |

### 5.3 Authorization for Sensitive Data and Functions

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Access to Restricted-tier data (CUI, PCI, PHI, financially material data) requires explicit authorization by the data owner. Inherited group access is permitted only where the inheriting group has an authorized purpose. | Governance / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.3 · HIPAA 164.308 |
| Highly destructive functions (mass delete, configuration baseline modification, identity-platform changes) shall require additional authorization controls: dual approval, JIT elevation, or compensating session monitoring. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6 · [NIST CSF](https://www.nist.gov/cyberframework) PR.AA |
| Cross-organizational data sharing (federation, OAuth grants to third-party apps, API integrations) shall be authorized by Engineering and Governance and documented in the third-party integration register. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-21 · CSA CCM IAM-13 |

---

## 6. Privileged Access Management

### 6.1 Privileged Access Definition

The following access types shall be treated as privileged and subject to the controls in this section:

- Administrative access to operating systems, hypervisors, and container platforms
- Administrative access to identity platforms (IdP, directory, MFA, PAM, KMS, CA)
- Administrative access to cloud control planes (account / subscription / project admin, IAM-policy authoring)
- Administrative access to Tier 1 SaaS applications (M365 GA, Salesforce SysAdmin, etc.)
- Administrative access to security infrastructure (SIEM, EDR, firewall, DLP, CSPM, network appliances)
- Administrative access to BES Cyber Systems and OT control systems
- Access to break-glass / emergency accounts
- Administrative access to backup, snapshot, and restoration systems

### 6.2 Privileged Access Controls

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| All privileged access shall be brokered through an approved Privileged Access Management (PAM) platform. Direct administrative access bypassing PAM is an exception case with documented compensating controls. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6, IA-2 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.5 |
| Implement just-in-time (JIT) privileged access - standing administrative entitlements are eliminated in favor of time-bound, request-approved elevation. Where JIT is not technically feasible, document the technical limit and apply enhanced session monitoring. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6(2), AC-6(5) |
| Privileged sessions shall be logged and, for designated high-risk roles, recorded in a tamper-resistant format. Recordings are retained per regulatory and contractual requirements. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-2, AU-12, AC-17(1) |
| Phishing-resistant MFA is mandatory for all privileged authentication. Privileged authentication shall traverse a dedicated path (e.g., privileged access workstation or compliant device + conditional access for high-sensitivity targets). | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-2(11) · [NIST 800-63](https://pages.nist.gov/800-63-3/)-3B AAL3 |
| Separate privileged credentials from standard user credentials. Administrative work shall not be performed from the user's daily-driver account. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6(5) · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.5 |

### 6.3 Break-Glass / Emergency Access

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Maintain documented break-glass procedures for critical platforms (IdP, cloud control plane, OT control systems). Procedures define when break-glass is permitted, how to invoke it, who is notified, and the post-use review. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6, IR-4 |
| Break-glass credentials shall be vaulted, dual-controlled, alarmed on use, and rotated after each use. The credential check-out and check-in shall be logged. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-5 · [NIST CSF](https://www.nist.gov/cyberframework) PR.AA |
| Test break-glass procedures at least annually. Document the test, validate the credential is usable, and confirm alerting fires. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-4 |

---

## 7. Remote, Vendor, and Third-Party Access

### 7.1 Remote Access

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| All remote access to organizational assets shall be authorized, MFA-enforced, logged, and routed through a documented secure path (VPN, zero-trust access broker, SSE, or equivalent). | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-17 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.12 |
| Remote administrative access shall require additional controls: phishing-resistant MFA, compliant or managed endpoint, and where applicable, session recording. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-17(2)(3) · CIP-005-6 R2 |
| Remote access to BES Cyber Systems shall traverse an Intermediate System per [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) and NERC-CIP CIP-005 R2 requirements. | Engineering / Governance | NERC-CIP CIP-005 R2 · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) |
| Split-tunnel VPN configurations are prohibited for sessions accessing Restricted-tier data or privileged functions, unless a documented exception with compensating controls is approved. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-17(3) |

### 7.2 Vendor and Third-Party Access

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Vendor and third-party accounts shall be sponsored by an internal accountable manager, scope-limited, time-bound, and reviewed at least quarterly. Vendor accounts without an active engagement shall be disabled. | Governance / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PS-7, AC-2 · CIP-004-6 |
| Vendor remote access to in-scope systems shall use phishing-resistant MFA, traverse the secure remote access path, and be logged with session attribution. Persistent vendor connections require Engineering and CISO approval. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-17 · CIP-005-6 R2 |
| Vendor access to BES Cyber Systems, CUI environments, or [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems requires contractual security obligations matching this standard and is subject to additional approval per the applicable peer standard. | Governance / Risk | DFARS 252.204-7012 · CIP-013-2 |
| Detect and alert on use of vendor credentials outside contracted maintenance windows or from anomalous source locations. | Risk / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-4(2) · CIP-007-6 R4 |

---

## 8. Identity Lifecycle (Joiner / Mover / Leaver)

### 8.1 Joiner

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| New workforce identities shall be provisioned only after the authoritative source (HRIS / contractor system) records the relationship. Pre-start provisioning is permitted only where the workflow logs the future effective date. | Engineering / Governance | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(1) |
| Baseline access shall be limited to role-defined entitlements. Additional access requires the workflow-based request and approval process. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.5 |
| Personnel screening required by contract or regulation (e.g., NERC-CIP CIP-004 PRA, CUI personnel screening) shall be completed and documented before access is granted. | Governance / HR | CIP-004-6 R3 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.9.1 |

### 8.2 Mover (Role Change)

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Role-change events from the authoritative source shall trigger an authorization review. Entitlements no longer required by the new role shall be revoked, not retained. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(2) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| Movers into privileged roles trigger PAM enrollment, additional training, and SoD review. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-5, AC-6 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| Long-duration accumulation of entitlements ("entitlement creep") is detected through the access review program and remediated. | Governance / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(7) |

### 8.3 Leaver

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Workforce access shall be disabled on or before the documented separation date. For BES Cyber Systems, access revocation timelines comply with CIP-004 (24 hours for terminations). | Engineering | CIP-004-6 R4 · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(3) |
| Service accounts and tokens owned by the leaver shall be reassigned or decommissioned. Personally created automation, scripts, and API keys are inventoried and transitioned. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(3), IA-5 |
| Federated and external system access (SaaS local accounts not behind SSO, third-party portals) shall be deprovisioned through documented run-books. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| Termination involving suspected wrongdoing or hostile separation invokes the enhanced offboarding procedure (immediate revocation, session termination, evidence preservation). | Risk / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4, PS-4(2) |

### 8.4 Service Account Lifecycle

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Every service account shall have a documented owner, purpose, scope, and expiration / review date. Ownerless service accounts are remediated within the cycle defined in the access review program. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2, IA-2 |
| Service-account credentials shall be vaulted in the secrets manager and rotated on a defined cadence appropriate to risk. Static, never-rotated credentials are an exception case. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-5 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.5.10 |
| Service accounts shall not be used for interactive logins. Where vendor software requires interactive use of a service account, document the exception and apply session monitoring. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2, AU-2 |

---

## 9. Access Review and Recertification

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Conduct access reviews on a defined cadence per system tier: privileged roles (quarterly), Tier 1 systems / [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant (quarterly), Tier 2 systems (semi-annual), Tier 3 systems (annual). | Governance | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(7) · CIP-004-6 R4.2 |
| Reviews require evidence of an active, attributable decision by the accountable manager or resource owner. "Rubber-stamp" approvals (single-click bulk approve without review) are non-compliant. | Governance | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(7) |
| Review findings - terminated users with active access, role mismatches, SoD violations, dormant accounts - shall be remediated within the SLA defined in the access review procedure. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(3), AC-2(13) |
| Recertify external (vendor / contractor) identities at least quarterly. Inactive external identities (no successful authentication in 60 days) are disabled pending sponsor confirmation. | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PS-7, AC-2 |
| Maintain access-review evidence in the audit evidence library per regulatory retention requirements. | Governance | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [CMMC](https://dodcio.defense.gov/CMMC/) CA.L2-3.12.4 |

---

## 10. Monitoring, Logging, and Detection

| **Requirement** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|
| Centralize identity-related logs from: IdP, MFA, PAM, directory services, conditional access, OAuth grant events, and Tier 1 SaaS authentication. Retain per regulatory requirement (minimum 12 months). | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-2, AU-11 |
| Detect and alert on identity attack indicators: impossible travel, atypical sign-in, MFA fatigue patterns, legacy auth attempts, OAuth grant anomalies, password spray, token theft / replay, and privileged role assignments outside change windows. | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-4(5), AU-6 · MITRE ATT&CK T1078 |
| Detect and respond to dormant account use. Accounts inactive beyond a defined threshold shall be disabled automatically. | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(3) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| Privileged role assignments, role-permission changes, and changes to MFA or conditional access policy shall generate alerts and be reconciled to an approved change ticket. | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-6, CM-3 |
| Integrate identity telemetry with the SIEM and the centralized incident response process. Identity-detected events have defined containment playbooks (force sign-out, revoke session, disable account, reset credentials). | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4, SI-4 |

---

## 11. Regulatory and Framework Alignment Summary

| **Requirement Area** | **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | **[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)** | **NERC-CIP** | **[CMMC L2](https://dodcio.defense.gov/CMMC/)** | **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC** |
|---|---|---|---|---|---|---|
| Identity Foundation / SSO | PR.AA | IA-2, IA-8, AC-2 | 3.5.1, 3.5.2 | CIP-004 R4 | IA.L2-3.5.1 | Access |
| MFA & Authenticator Strength | PR.AA | IA-2(1)(2)(11) | 3.5.3 | CIP-005 R2 | IA.L2-3.5.3 | Access |
| Credential & Secrets Mgmt | PR.AA | IA-5, IA-5(1)(7) | 3.5.7–3.5.10 | CIP-007 R5 | IA.L2-3.5.7 | Access |
| Least Privilege & Authorization | PR.AA | AC-3, AC-6 | 3.1.5 | CIP-004 R4 | AC.L2-3.1.5 | Access / SoD |
| Privileged Access (PAM, JIT) | PR.AA | AC-6(2)(5), AU-12 | 3.1.5 | CIP-007 R5 | AC.L2-3.1.5 | Access |
| Remote & Vendor Access | PR.AA | AC-17, PS-7 | 3.1.12 | CIP-005 R2 | AC.L2-3.1.12 | Access |
| Joiner / Mover / Leaver | PR.AA | AC-2(1)(2)(3) | 3.5.6 | CIP-004 R4 | AC.L2-3.5.6 | Access |
| Access Review / Recert | GV.RR | AC-2(7) | 3.1.5 | CIP-004 R4.2 | AC.L2-3.1.5 | Access |
| Monitoring & Detection | DE.CM | AU-6, SI-4 | 3.3.5 | CIP-007 R4 | AU.L2-3.3.5 | Logging |

---

## 12. Exceptions and Escalation

| **Exception Type** | **Approval Required** | **Process** | **Review Cycle** |
|---|---|---|---|
| Standard exception (non-privileged, non-regulated) | Manager + Governance | Risk register entry with compensating control documentation. | Annual |
| Privileged access exception | CISO | PAM-bypass exceptions require enhanced session monitoring and quarterly review. | Quarterly |
| Shared / vendor-required credential | Engineering Manager + Governance | Vault under PAM, document attribution model, monitor session use. | Annual |
| MFA exception (workforce identity) | CISO | Permitted only for documented technical limitations; compensating controls required (e.g., source-IP restrictions, enhanced monitoring). | Quarterly |
| Standing privileged access (no JIT) | CISO | Risk register entry; session recording required where technically feasible. | Quarterly |
| BES Cyber System access exception | CISO + NERC-CIP deviation as applicable | Follow [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) §11 escalation. | Per CIP-mitigation milestones |
| CUI-environment access exception | CISO; POA&M entry | Follow [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) §11. | Per POA&M plan |
| Emergency / break-glass use | CISO post-hoc within 24 hours | Alerted at time of use; post-use review and credential rotation. | Per use |

---

## 13. Document Control

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 DRAFT | 2026 | CERG Governance | Initial release - identity, authentication, authorization, lifecycle |

### Review Triggers

- Material change to the organization's IdP, MFA, PAM, or secrets management platforms
- Revisions to [NIST 800-63](https://pages.nist.gov/800-63-3/), 800-53, 800-171, NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), or [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC guidance that materially affect requirements
- Significant identity-related incident
- Internal audit or regulatory finding affecting access control
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Identity & Access) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - this standard is subordinate |
| Grid and Control System Standard | [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | Peer standard - BES Cyber System access provisions apply in addition |
| IT (Hosted/Cloud/SaaS) Security Standard | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Peer standard - cloud/SaaS-specific provisions apply in addition |
| CUI Handling Standard | [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handli