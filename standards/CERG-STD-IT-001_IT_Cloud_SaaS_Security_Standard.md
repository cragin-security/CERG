## IT (HOSTED, CLOUD, AND SaaS) SECURITY STANDARD
### Owned Data Center · Leased Facility · IaaS · PaaS · SaaS

---

| | |
|---|---|
| **Document ID** | CERG-STD-IT-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Significant Change / Material Cloud Service Adoption |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r2/final) · [NIST 800-144](https://csrc.nist.gov/pubs/sp/800/144/final) · NIST RMF · CSA CCM v4 |
| **Regulations** | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [CMMC L2](https://dodcio.defense.gov/CMMC/) (where applicable) · HIPAA (where applicable) |
| **Environments** | Owned Data Center · Leased / Colocation · IaaS · PaaS · SaaS · Hybrid |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [CERG Roles in Hosted and Cloud Environments](#2-cerg-roles-in-hosted-and-cloud-environments)
3. [GOVERN, Cloud Program Foundation and Shared Responsibility](#3-govern--cloud-program-foundation-and-shared-responsibility)
4. [IDENTIFY, Visibility Across Estates](#4-identify--visibility-across-estates)
5. [PROTECT, Architecture, Identity, and Data](#5-protect--architecture-identity-and-data)
6. [DETECT, Cloud-Native and Cross-Estate Monitoring](#6-detect--cloud-native-and-cross-estate-monitoring)
7. [RESPOND, Containment Without Crossing Tenant Boundaries](#7-respond--containment-without-crossing-tenant-boundaries)
8. [RECOVER, Resilience in Multi-Tenant Environments](#8-recover--resilience-in-multi-tenant-environments)
9. [Training and Personnel](#9-training-and-personnel)
10. [Regulatory and Framework Alignment Summary](#10-regulatory-and-framework-alignment-summary)
11. [Exceptions and Escalation](#11-exceptions-and-escalation)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

This standard implements the foundational principles established in **[CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md)** for information technology assets hosted in owned data centers, leased / colocation facilities, infrastructure-as-a-service (IaaS), platform-as-a-service (PaaS), and software-as-a-service (SaaS) environments. It defines specific, measurable security requirements that apply regardless of whether the underlying infrastructure is owned, leased, rented, or consumed as a service.

The intent is durable: as the organization continues to shift workloads between owned, hybrid, and fully cloud-native models, the security obligations do not change, only the implementation specifics do. This standard makes those implementation differences explicit while keeping the underlying control intent constant.

### 1.1 Scope

This standard applies to:

- All applications, services, and data hosted in **organization-owned data centers**
- All systems housed in **leased / colocation** facilities, regardless of who provides the physical security
- All **IaaS** workloads (e.g., AWS EC2, Azure VMs, GCP Compute, private cloud)
- All **PaaS** services consumed by the organization (e.g., managed databases, container platforms, serverless functions)
- All **SaaS** applications used to process organizational data, including productivity, collaboration, HR, finance, ITSM, and security tooling
- All **hybrid** integrations between the above, including identity federation, VPN, ExpressRoute / Direct Connect, and API integrations
- All personnel and third parties with administrative or privileged access to in-scope systems

> **Note on OT and BES Cyber Systems**
>
> Grid and control system environments are governed by **[CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)**. Where an enterprise IT system has direct or indirect connectivity to an OT environment, both standards apply, and the more stringent requirement controls.

### 1.2 The Shared Responsibility Reality

Cloud and SaaS providers operate under a shared responsibility model. The provider is accountable for security *of* the cloud, physical facilities, hypervisor, base platform, and the organization remains accountable for security *in* the cloud, data, identity, configuration, application logic, and access. Outsourcing the workload does not outsource the accountability.

> **The Shared Responsibility Trap**
>
> The single most common cause of cloud-related incidents is not a provider failure, it is a customer misunderstanding of which side of the line a given control sits on. Every cloud or SaaS service in use must have a documented shared responsibility mapping. Where the mapping is ambiguous, the organization assumes the obligation until the provider documents otherwise in writing.

### 1.3 Relationship to Parent Policy

This standard is subordinate to **[CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md)**. It implements specific requirements; it does not limit any principle established in that policy. Where this standard is silent, the policy governs. Exceptions follow the process defined in [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) Section 7.

---

## 2. CERG Roles in Hosted and Cloud Environments

The three CERG pillars operate across all hosted and cloud estates with the same structure as on-premises IT, with adaptations that reflect the operating model of each environment.

| **CERG Pillar** | **Hosted / Cloud / SaaS-Specific Responsibilities** |
|---|---|
| **Engineering** | Reviews and approves architecture for all cloud and SaaS adoptions before production. Defines and maintains secure landing zones, reference architectures, and configuration baselines for each cloud platform in use. Embeds security guardrails into infrastructure-as-code (IaC) pipelines. Conducts pre-production reviews of all new SaaS integrations and IaaS workloads. Owns the organization's shared responsibility matrix. |
| **Risk** | Operates continuous configuration assessment (CSPM/SSPM) and exposure management across cloud and SaaS estates. Maintains the SaaS inventory and integration risk register. Conducts third-party risk assessments for all SaaS and cloud providers and tracks SOC 2 / ISO 27001 / FedRAMP attestation currency. Runs adversarial testing against cloud workloads and SaaS configurations on a defined cadence. |
| **Governance** | Maintains this standard and all subordinate cloud and SaaS procedures. Owns the cloud governance framework - including approved provider list, data residency rules, and tenancy approval workflow. Tracks compliance posture against SOC 2 / ISO 27001 / [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) / [CMMC](https://dodcio.defense.gov/CMMC/) obligations for cloud and SaaS estates. Coordinates [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC evidence collection from cloud and SaaS systems supporting financial reporting. |

> **The "Cloud Is Just Someone Else's Computer" Fallacy**
>
> Cloud and SaaS are not a free pass on security obligations, but they also are not equivalent to on-premises systems. Treating a SaaS app as "out of scope because the vendor handles security" produces real, exploitable gaps. Treating an IaaS workload as just a virtual machine ignores the cloud control plane, often the most attractive attack surface. CERG treats each environment on its own terms, with controls calibrated to the actual operating model.

---

## 3. GOVERN: Cloud Program Foundation and Shared Responsibility

### 3.1 Approved Provider and Service Catalog

The organization shall not consume cloud or SaaS services that have not been assessed and approved through CERG. Shadow IT, services procured outside this process, is one of the most material sources of unmanaged risk in modern enterprises.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain an authoritative catalog of approved cloud platforms (IaaS/PaaS) and SaaS applications. New services may not enter production use without being added to the catalog. | All Cloud / SaaS | Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SA-9 · CSA CCM GRC-04 |
| Assess every cloud or SaaS provider before onboarding. Assessment scope is tiered: Tier 1 (regulated data, broad access, financial reporting impact), Tier 2 (general business data), Tier 3 (low-sensitivity, narrow access). | All Cloud / SaaS | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SA-9 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC vendor |
| Validate provider attestations - SOC 2 Type II, ISO 27001, FedRAMP, HITRUST, or equivalent - before onboarding and annually thereafter. Track expiration and re-attestation in the vendor risk register. | All Cloud / SaaS | Risk / Governance | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.12.4 |
| Document data residency, sub-processor disclosure, and right-to-audit clauses in every cloud and SaaS contract. Contracts without these provisions require CISO sign-off and documented compensating controls. | All Cloud / SaaS | Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SR-3 · GDPR Art 28 |
| Maintain a written shared responsibility matrix for every approved cloud platform and SaaS application. Map each in-scope control to: provider, customer, or shared. Update upon any change in service model. | All Cloud / SaaS | Engineering / Governance | [NIST 800-144](https://csrc.nist.gov/pubs/sp/800/144/final) · CSA CCM |

### 3.2 Data Classification and Placement

Where data lives determines what controls apply. Every workload and SaaS tenant shall be mapped to a documented data classification.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Classify all data processed in cloud and SaaS environments per the organization's data classification scheme: Public, Internal, Confidential, Restricted (CUI / PCI / PHI / financial). | All Cloud / SaaS | Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) RA-2 |
| Prohibit storage or processing of Restricted-tier data in any cloud or SaaS service not explicitly approved for that classification. | All Cloud / SaaS | Governance / Engineering | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.3 · [CMMC](https://dodcio.defense.gov/CMMC/) AC.L2-3.1.3 |
| Maintain a data flow inventory for each in-scope cloud workload and SaaS tenant documenting: data classes processed, ingress / egress endpoints, integration partners, and sub-processors. | All Cloud / SaaS | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SA-8 · GDPR Art 30 |
| Where data residency restrictions apply (regulatory, contractual, customer commitment), configure provider region constraints and document the enforcement mechanism. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SA-9(5) |

### 3.3 Tenancy, Account, and Subscription Governance

Cloud accounts and SaaS tenants are control boundaries. They are governed, not arbitrarily provisioned.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| All cloud accounts (AWS accounts, Azure subscriptions, GCP projects) shall be provisioned through the organization-approved landing zone with embedded guardrails, logging, and identity federation. Manual root account creation is prohibited. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2 · CSA CCM IAM-09 |
| Root, global administrator, and tenant owner accounts shall be protected by phishing-resistant MFA, vaulted credentials, break-glass procedures, and continuous monitoring. Use of these accounts shall trigger an alert. | All Cloud / SaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-2(11) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| SaaS tenants procured for production use shall be registered to organizational identity (SSO/SCIM), placed under contract with the central procurement process, and inventoried in the SaaS catalog. Free-tier or personal-account use of SaaS for organizational work is prohibited. | All SaaS | Governance / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| Decommission unused accounts, subscriptions, projects, and SaaS tenants on a documented schedule. Idle resources are an unmonitored attack surface and a cost liability. | All Cloud / SaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-8(3) |

---

## 4. IDENTIFY: Visibility Across Estates

### 4.1 Inventory and Configuration Visibility

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain a real-time inventory of all cloud resources across all approved cloud platforms, populated via provider APIs (e.g., AWS Config, Azure Resource Graph, GCP Asset Inventory). Static spreadsheets are not acceptable. | IaaS / PaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-8 · [NIST CSF 2.0](https://www.nist.gov/cyberframework) ID.AM |
| Maintain a SaaS inventory populated from at minimum: SSO/IdP logs, expense data, and SaaS discovery tooling. Reconcile monthly. | All SaaS | Risk / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-8 · CSA CCM AIS-04 |
| Deploy continuous cloud security posture management (CSPM) covering all production cloud accounts and subscriptions. Posture findings flow to the centralized vulnerability program. | IaaS / PaaS | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CA-7 · CSA CCM IVS-09 |
| Deploy SaaS security posture management (SSPM) for all Tier 1 SaaS applications and for any SaaS storing Restricted-tier data. | All SaaS (Tier 1) | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CA-7 |
| Tag every cloud resource with: owner, environment (prod/non-prod), data classification, cost center, and application identifier. Untagged resources are flagged for owner identification and remediation. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-8 |

### 4.2 Vulnerability and Configuration Drift Identification

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Scan all IaaS workloads (VMs, containers, serverless functions) for OS, library, and runtime vulnerabilities on a defined cadence. Container images shall be scanned in the build pipeline and before promotion to production. | IaaS / PaaS | Risk / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) RA-5 · CIS Top 18 |
| Detect drift from approved configuration baselines for cloud control-plane resources (e.g., security groups, IAM policies, storage bucket ACLs, encryption settings) within 24 hours. | IaaS / PaaS | Risk / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-2(7), CM-6(1) |
| Exposure treatment and patch hygiene follow the canonical classification and SLA table in [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md). This standard does not restate SLA values; PRC-VM-001 governs PPR, confirmed exposure, compensated flaw, and hygiene debt timing. | IaaS / PaaS | Risk / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-2 · CISA KEV |
| Where a vulnerability cannot be remediated within SLA, document compensating controls and obtain risk acceptance per [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) Section 7. | All Cloud | Risk / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-2(6) |

---

## 5. PROTECT: Architecture, Identity, and Data

### 5.1 Identity and Access

> **Identity Is the New Perimeter**
>
> In cloud and SaaS, traditional network boundaries are advisory at best. Identity, who is making this API call, from where, on what device, is the actual enforcement point. Identity controls in cloud environments must be treated with the same operational priority as firewall rules were in the data-center era.

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| All workforce access to cloud and SaaS shall be brokered through the central identity provider (IdP) using SSO. Direct local accounts on cloud platforms or SaaS apps are prohibited except for documented break-glass and emergency cases. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-2, IA-8 · [NIST 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) |
| Enforce phishing-resistant MFA (FIDO2, platform authenticators, or equivalent) for all administrative access to cloud and SaaS. Standard MFA (TOTP, push) is the minimum for general user access. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-2(11) · [NIST 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) AAL2/AAL3 |
| Apply just-in-time (JIT) elevation for cloud and SaaS privileged roles. Standing administrative access is prohibited except for documented exceptions reviewed quarterly. | IaaS / PaaS / Tier 1 SaaS | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-6(2), AC-6(5) |
| Conditional access policies shall evaluate at minimum: device compliance, location / network risk, user risk signals, and session sensitivity. Sensitive admin paths require compliant managed devices. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(12), AC-17 |
| Automate identity lifecycle (joiner / mover / leaver) via SCIM, IdP groups, or equivalent. Manual deprovisioning is not an acceptable primary control for Tier 1 systems. | All Cloud / SaaS | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(1) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| Conduct quarterly access reviews for Tier 1 SaaS, cloud control-plane access, and any system supporting financial reporting. Reviews shall be evidenced and retained per [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC requirements. | Tier 1 SaaS / IaaS / PaaS | Governance | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-2(7) |

### 5.2 Network and Architecture

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| All production IaaS workloads shall be deployed into a documented landing zone with: hub-and-spoke or equivalent network architecture, egress filtering, default-deny security groups, and centralized DNS / logging. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SC-7 · CSA CCM IVS-06 |
| Public exposure of resources (cloud storage, databases, management endpoints) is prohibited unless explicitly justified, documented, and protected by compensating controls. CSPM shall continuously detect and alert on public exposure of in-scope resource types. | IaaS / PaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SC-7 · CIS Benchmarks |
| All administrative access to cloud control planes and SaaS admin consoles shall traverse the organization's secure access path (e.g., conditional access + privileged access workstation, or equivalent). | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-17 · [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) 3.1.12 |
| Where a cloud environment must interconnect with on-premises systems, the connection (VPN, ExpressRoute, Direct Connect, Cloud Interconnect) shall be terminated in a documented transit network with egress / ingress filtering and traffic logging. | Hybrid | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SC-7(3), SC-8 |
| IT systems shall not establish direct routed connectivity to OT environments. All IT/OT data flows transit the OT DMZ per [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) and require Engineering approval. | Hybrid | Engineering | [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) §5.1 |

### 5.3 Data Protection

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Encrypt data in transit using TLS 1.2 or higher with approved cipher suites for all in-scope cloud and SaaS communications. Disable legacy protocols (SSLv3, TLS 1.0/1.1) on customer-managed endpoints. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SC-8 · [NIST 800-52r2](https://csrc.nist.gov/pubs/sp/800/52/r2/final) |
| Encrypt data at rest for Confidential and Restricted classifications using provider-native encryption or customer-managed keys. Customer-managed keys (CMK) are required for Restricted data. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SC-28 · [CMMC](https://dodcio.defense.gov/CMMC/) SC.L2-3.13.8 |
| Manage encryption keys in a dedicated key management service (KMS / HSM-backed). Key rotation, separation of duties, and key access logging are required. Key custody for Restricted data shall reside with the customer, not the provider. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SC-12 · FIPS 140-2/3 |
| Apply DLP controls to Tier 1 SaaS and to outbound cloud data flows where Restricted-tier data is present. DLP policies shall block, alert, or quarantine per the data classification scheme. | All Cloud / SaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AC-23, SI-4(4) |
| Backups of Restricted-tier and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant data shall be encrypted, isolated (separate trust boundary or immutable storage), and tested for restoration per Section 8.2. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-9 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |

### 5.4 Hardening and Secure Build

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain documented secure configuration baselines for: each cloud platform's control plane, each VM OS image, each container base image, and each major PaaS service in use. Baselines align to CIS Benchmarks where available. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-6 · CIS Benchmarks |
| Production cloud workloads shall be deployed via infrastructure-as-code (IaC) with mandatory pre-merge security checks (static analysis, policy-as-code). Manual production changes are exception cases. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-3 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC change |
| Container images shall be built from approved base images, scanned for vulnerabilities, and signed. Production clusters shall enforce admission policies that reject unsigned or unscanned images. | PaaS (containers) | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-7, SI-2 · [NIST 800-190](https://csrc.nist.gov/pubs/sp/800/190/final) |
| Secrets (API keys, database credentials, signing keys) shall be stored in a dedicated secrets manager and consumed at runtime. Plaintext secrets in source repositories, configuration files, or IaC are prohibited and shall be detected by automated scanning. | IaaS / PaaS / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IA-5 · OWASP ASVS |
| Tier 1 SaaS applications shall be configured against documented hardening baselines (e.g., M365 Secure Score, Salesforce Health Check, Google Workspace baseline). Baseline drift is detected by SSPM and remediated within SLA. | Tier 1 SaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CM-6 · CIS Benchmarks |

---

## 6. DETECT: Cloud-Native and Cross-Estate Monitoring

### 6.1 Logging

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Enable cloud control-plane audit logging (CloudTrail, Azure Activity Logs, GCP Audit Logs) in all accounts / subscriptions / projects. Logs route to a centralized, tamper-resistant log archive separate from the originating account. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-2, AU-9 · CIS Cloud |
| Capture admin and authentication logs from all Tier 1 SaaS via provider APIs or SIEM connectors. Where the provider does not expose required event types, raise a risk-accepted gap with quarterly review. | Tier 1 SaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-2 |
| Retain audit logs for in-scope cloud and SaaS environments for a minimum of 12 months, with at least 90 days hot / immediately searchable. Longer retention applies where regulation requires (e.g., [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), HIPAA). | All Cloud / SaaS | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-11 · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) |
| Protect log archives with write-once / immutable storage controls and dedicated access roles. Log deletion or modification requires CISO approval and shall trigger an alert. | All Cloud / SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU-9(2), AU-9(3) |

### 6.2 Detection Engineering

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Operate a centralized SIEM (or equivalent) that ingests cloud audit logs, SaaS audit logs, EDR telemetry, IdP / SSO events, and network telemetry. Detection rules cover cloud-specific TTPs (e.g., MITRE ATT&CK for Cloud). | All Cloud / SaaS | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-4 · MITRE ATT&CK |
| Deploy CSPM and SSPM continuous detection rules covering at minimum: public exposure, disabled logging, weakened encryption, privilege escalation paths, anomalous admin behavior, and identity-provider tampering. | All Cloud / SaaS | Risk / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SI-4(5), CA-7 |
| Subscribe to and integrate cloud-relevant threat intelligence (CISA advisories, provider security bulletins, ISAC feeds). Translate relevant intelligence into detection rules and posture checks. | All Cloud / SaaS | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PM-16, SI-5 |
| Test detections quarterly through purple-team exercises or automated adversary emulation (e.g., Stratus Red Team, AWS / Azure attack simulation tooling) in non-production accounts. | IaaS / PaaS | Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CA-8 · MITRE ATT&CK |

---

## 7. RESPOND: Containment Without Crossing Tenant Boundaries

> **Cloud Response Has Different Rules**
>
> Response actions in cloud environments operate inside a multi-tenant control plane owned by the provider. Containment that would be straightforward on-premises, pulling a cable, isolating a VLAN, must be executed through provider APIs and with awareness of shared responsibility limits. Forensic acquisition in cloud and SaaS depends on what the provider exposes. Plans must be built around those realities, not against them.

### 7.1 Cloud and SaaS Incident Response

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain documented response playbooks for cloud and SaaS incident classes including, at minimum: compromised cloud credential, malicious IaC change, exposed storage / database, SaaS account takeover, OAuth grant abuse, and supply chain compromise of a SaaS dependency. | All Cloud / SaaS | Governance / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4, IR-8 |
| Pre-stage cloud-native isolation actions (e.g., quarantine IAM policies, account-suspend automation, network ACL templates) in approved IaC and validate quarterly. Improvisation during an incident is not acceptable for Tier 1 systems. | IaaS / PaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4(1), IR-4(2) |
| Document forensic acquisition procedures per provider, including which artifacts are obtainable, retention windows, and the formal request channels for provider-side data. Validate annually with each Tier 1 provider. | All Cloud / SaaS | Risk / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4(6), AU-12 |
| Confirm and document provider incident notification SLAs. Where a provider's SLA is insufficient for organizational regulatory obligations, compensating monitoring controls shall be implemented. | All Cloud / SaaS | Governance / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-6 · GDPR Art 33 |
| Integrate cloud and SaaS response into the master Incident Response Plan (**[CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)**). Notification timelines for [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), breach laws, contractual customer commitments, and regulator obligations shall be documented per data class. | All Cloud / SaaS | Governance | [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |

---

## 8. RECOVER: Resilience in Multi-Tenant Environments

### 8.1 Recovery Planning

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Maintain documented recovery plans for all Tier 1 cloud workloads and SaaS applications, including: RTO, RPO, dependencies, restoration procedures, and provider escalation contacts. | All Cloud / SaaS | Governance / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-2 · ISO 22301 |
| Define a tiered availability strategy per workload (e.g., multi-AZ, multi-region, multi-cloud) commensurate with business criticality. The chosen strategy shall be tested, not assumed. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-7 · CSA CCM BCR |
| For SaaS systems with no provider-side restore option, the organization shall operate independent backups (e.g., third-party SaaS backup for M365, Google Workspace, Salesforce). Provider replication is not equivalent to a backup. | Tier 1 SaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-9 · CSA CCM BCR-08 |
| For [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems, document backup integrity, retention, and restoration testing as ITGC evidence. Restoration testing shall occur at least annually with results retained. | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant | Engineering / Governance | [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-9(1) |

### 8.2 Backup Testing and Restoration

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| Test restoration of Tier 1 cloud workloads at least annually from production-equivalent backups. Test results shall be documented as audit evidence. | IaaS / PaaS | Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-9(1), CP-10 |
| Validate that recovery procedures account for cloud-specific failure modes: region outage, provider account compromise, IAM lockout, and dependency-chain SaaS unavailability. | All Cloud / SaaS | Engineering / Risk | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) CP-2(2), CP-2(5) |
| Conduct post-incident reviews within 30 days of any significant availability or security event affecting an in-scope system. Lessons learned feed Engineering, Risk, and Governance backlog items. | All Cloud / SaaS | Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) IR-4(4) |

---

## 9. Training and Personnel

| **Requirement** | **Applies To** | **CERG Owner** | **Regulatory Reference** |
|---|---|---|---|
| All personnel with cloud administrative roles shall complete role-appropriate cloud security training within 60 days of assignment and annually thereafter. | IaaS / PaaS | Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AT-2, AT-3 |
| SaaS administrators for Tier 1 applications shall complete platform-specific security configuration training and stay current with provider security release notes. | Tier 1 SaaS | Governance / Engineering | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AT-3 |
| All workforce members shall complete annual security awareness training that includes SaaS-specific risks: phishing, OAuth grants, third-party app authorization, and shadow IT. | All Cloud / SaaS | Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AT-2 · [CMMC](https://dodcio.defense.gov/CMMC/) AT.L2-3.2.1 |
| Engineering personnel responsible for IaC and pipeline security shall maintain current knowledge of cloud-native attack patterns and provider security advisories. | IaaS / PaaS | Engineering / Governance | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AT-3 |

---

## 10. Regulatory and Framework Alignment Summary

| **Requirement Area** | **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | **[NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r2/final)** | **CSA CCM v4** | **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC** |
|---|---|---|---|---|---|
| Approved Provider / Vendor Mgmt | GV.SC | SA-9, SR-3 | 3.1.20 | STA-01 to STA-09 | Vendor mgmt |
| Data Classification & Residency | GV.OC | RA-2, SA-9(5) | 3.1.3, 3.8.x | DSP-01 to DSP-19 | - |
| Identity / SSO / MFA | PR.AA | IA-2, IA-5, AC-2 | 3.5.1–3.5.11 | IAM-01 to IAM-16 | Access |
| Privileged Access (JIT, PIM) | PR.AA | AC-6, AC-2(7) | 3.1.5 | IAM-04, IAM-09 | Access |
| Network & Landing Zone | PR.IR | SC-7, SC-8 | 3.13.1, 3.13.5 | IVS-06, IVS-09 | - |
| Encryption & Key Mgmt | PR.DS | SC-12, SC-28 | 3.13.10, 3.13.11 | CEK-01 to CEK-21 | - |
| Hardening / IaC / Pipelines | PR.PS | CM-3, CM-6 | 3.4.x | CCC-01 to CCC-09 | Change mgmt |
| CSPM / SSPM / Vulnerability | ID.RA, DE.CM | CA-7, RA-5, SI-2 | 3.11.2, 3.14.1 | TVM-01 to TVM-10 | - |
| Logging & SIEM | DE.AE | AU-2, AU-9, SI-4 | 3.3.1, 3.14.6 | LOG-01 to LOG-13 | Logging |
| Cloud Incident Response | RS | IR-4, IR-6, IR-8 | 3.6.1–3.6.3 | SEF-01 to SEF-08 | - |
| Recovery & Resilience | RC | CP-2, CP-9, CP-10 | 3.6.x | BCR-01 to BCR-11 | Availability |
| Personnel Training | GV.RR | AT-2, AT-3 | 3.2.1–3.2.3 | HRS-01 to HRS-13 | - |

---

## 11. Exceptions and Escalation

No control in this standard may be waived without a documented exception. Exceptions to controls supporting [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC, [CMMC](https://dodcio.defense.gov/CMMC/), or Restricted-data handling carry additional obligations.

| **Exception Type** | **Approval Required** | **Process** | **Review Cycle** |
|---|---|---|---|
| Standard exception (Internal-data SaaS / non-prod IaaS) | Engineering Pillar Leader + Governance | Submit risk acceptance via risk register with compensating control documentation. | Annual |
| Tier 1 SaaS / production IaaS | CISO | Risk register entry with compensating controls. Governance reviews shared-responsibility implications. | Annual |
| Restricted-data placement exception | CISO + Data Owner | Risk register + data classification review. CUI placements additionally subject to [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md). | Annual |
| [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant system control gap | CISO + CFO designee | Risk register + ITGC compensating control documentation. External audit notification as required. | Quarterly until closed |
| Emergency exception (operational necessity) | CISO (post-hoc within 24 hours) | Engineering may take emergency action; document immediately, formal exception within 24 hours. | 30 days maximum |

---

## 12. Document Control

| | |
|---|---|
| **Document ID** | CERG-STD-IT-001 |
| **Version** | 1.21 |
| **Approved By** | CISO |
| **Next Review** | Annual / Upon Significant Change / Material Cloud Service Adoption |
| **Change Log** | 1.0 - Initial publication. Owned data center, leased, IaaS, PaaS, SaaS. |


### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 DRAFT | 2026 | CERG Governance | Initial release - owned data center, leased, IaaS, PaaS, SaaS |

### Review Triggers

This standard shall be reviewed annually and upon any of the following triggering events:

- Material change to the organization's cloud or SaaS estate, new platform adoption, major migration, or significant provider consolidation
- Release of materially updated provider shared-responsibility documentation
- Significant cybersecurity incident affecting any in-scope cloud or SaaS system
- Changes to [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), 800-171, CSA CCM, or [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC guidance that materially affect requirements herein
- Direction from the CISO, internal audit findings, or external regulatory examination

Governance owns this document. The Governance Pillar Leader (Enterprise IT/Cloud) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - this standard is subordinate |
| Grid and Control System Standard | [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | Peer standard - governs OT estates and IT/OT boundary |
| CUI Handling Standard | [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) | Peer standard - applies in addition where CUI is present |
| Access Management Standard | [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) | Peer standard - identity and access requirements apply across IT, cloud, and SaaS environments |
| Third-Party and Supply Chain Risk Procedure | [CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | SaaS onboarding, vendor evidence, and shared responsibility interface |
