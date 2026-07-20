# CERG Opinionated Tool Matrix

## Practitioner-Grade Tool Recommendations for CERG Adoption

| | |
|---|---|
| **Document ID** | CERG-OPN-TOOLS-001 |
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Quarterly |
| **Frameworks** | CERG 100-Core · CIS Controls v8 · NIST 800-53r5 |
| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 |
| **Environments** | IT · Cloud · SaaS · OT (partial) |

---

## Purpose

This document defines the opinionated tool stack for CERG adopters who work through an MSP, MSSP, or in-house IT generalist. Every recommendation here is based on three criteria:

1. **Integration surface** — Does it talk to ServiceNow GRC and the rest of the stack without custom middleware?
2. **MSP/MSSP multi-tenancy** — Can a single instance or deployment manage multiple client organizations cleanly?
3. **IT generalist usability** — Can someone without a dedicated SOC engineer configure it using vendor documentation alone?

Each category lists a **Primary** (the recommendation), **Acceptable** alternatives (decent but weaker on at least one criterion), and **Avoid** (popular tools that fail hard on the CERG criteria).

---

## Tool Categories

### 1. GRC Platform — The Anchor

The GRC platform is the spine of the CERG program. Every other tool reports into it. Controls are tracked here. Evidence lives here or is linked from here. Audits open here.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary** | **ServiceNow GRC** | Full IT service management + GRC. Controls, evidence, risk register, audit management, compliance dashboards all in one platform. Multi-tenant via domain separation. The only platform that straddles IT operations AND GRC without a messy handoff. |
| **Acceptable** | **Vanta** | Best-in-class for SMB compliance automation (SOC 2, ISO 27001, HIPAA). Agent-based evidence collection. Weak on operational risk and IT service management — you'll need separate tools for incident/change management. Good for startups and small practices. |
| **Acceptable** | **Drata** | Similar to Vanta. Slightly better auditor UX, slightly weaker integrations. For SMB compliance-only use cases. |
| **Avoid** | **Archer** | Legacy architecture, high customization cost, requires dedicated Archer developers. Multi-tenancy is an afterthought. |
| **Avoid** | **OpenGRC / Eramba** | Free but abandonware risk. No MSP multi-tenancy. No API ecosystem. |
| **Avoid** | **Spreadsheets** | You will lose audit credibility immediately. A spreadsheet is not a GRC platform and auditors know it. |

**CERG recommendation:** ServiceNow GRC for any organization with 50+ employees or multi-client MSP/MSSP delivery. Vanta for SMB clients under 50 employees where compliance automation matters more than operational integration.

**CERG standards:** The GRC platform tracks all controls and evidence from the [100-Core Baseline](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md). Implementation guidance is in the [GRC Rollout Guide](grc-rollout-v1.md) and [Engagement Playbook](../engagement-playbook-v1.md).

**Integration note:** ServiceNow GRC has native integrations with most SIEM and endpoint tools. Vanta's integrations are narrower — Wiz, AWS, Azure, GCP, GitHub, Jamf, Intune. Budget for middleware if you need Vanta-to-non-cloud-tool integration.

---

### 2. SIEM / Centralized Logging

The SIEM is the operational brain. It ingests from endpoint, network, cloud, identity, and application sources. Detection rules fire here. Investigations start here.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary: Enterprise** | **Elastic Security** | Full EDR + SIEM in one platform. Open detection engine. Sigma rule support. Agent-based collection. Multi-tenant via Elastic Cloud. The best balance of capability, cost, and MSP-friendliness at scale. |
| **Primary: SMB/Lean** | **Wazuh** | Open-source XDR. Lightweight agent. File integrity monitoring. Good compliance mapping (PCI, HIPAA, GDPR). Free. Multi-tenancy via separate managers or virtual appliances per client. Best for MSPs running on thin margins. |
| **Acceptable** | **Splunk** | Best analytics engine. Best app marketplace. Priced per GB ingested — becomes punitive at scale unless you have an ELA. Multi-tenancy requires Splunk Cloud or heavy engineering. |
| **Acceptable** | **Microsoft Sentinel** | Native Azure integration. Good if clients are already M365 E5. Weak on non-Windows endpoints, OT, and network. Pricing is consumption-based — hard to predict. |
| **Avoid** | **QRadar** | End-of-life migration to SaaS underway. Avoid until the dust settles. |
| **Avoid** | **LogRhythm** | Aging architecture. MSP multi-tenancy is clunky. |
| **Avoid** | **DIY ELK** | Building your own Elasticsearch cluster is a full-time job. Use Elastic Cloud or Wazuh. |

**CERG recommendation:** Wazuh for SMB clients and lean MSP stacks. Elastic Security when the client has the budget and needs EDR + SIEM convergence.

**CERG standard:** [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) — defines detection coverage requirements, log source minimums, retention periods, and evidence parameters for SI-family controls.

---

### 3. Endpoint Protection / EDR

Endpoint is the first line of defense and the richest source of detection telemetry. CERG requires EDR, not signature-only antivirus.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary** | **SentinelOne Singularity** | Strong detection with minimal noise. Multi-tenant console with RBAC per client site. API that talks to ServiceNow. Good offline detection for OT/air-gapped. |
| **Acceptable** | **CrowdStrike Falcon** | Best threat intel. Best IR capabilities. Multi-tenant via Falcon Complete for MSSPs. Pricier than SentinelOne. Overkill for SMB. |
| **Acceptable** | **Microsoft Defender for Endpoint** | Included in M365 E5. Deep Windows integration. Weaker on Linux/Mac. Multi-tenant via Lighthouse. |
| **Avoid** | **Symantec / Broadcom** | Aging detection engine. Multi-tenancy is an afterthought. Integration surface is shrinking. |
| **Avoid** | **McAfee / Trellix** | Fragmented product line. MSP program is inconsistent. |
| **Avoid** | **Bitdefender GravityZone** | Decent detection, weak API. Does not integrate cleanly with ServiceNow. |

**CERG recommendation:** SentinelOne. Good enough detection, excellent MSP console, solid ServiceNow integration. CrowdStrike if the client has breach history or is a high-value target.

**CERG standards:** [Endpoint and Mobile Security Standard](../../standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) — endpoint hardening, EDR coverage requirements, mobile device management. [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) — detection rule requirements fed by endpoint telemetry.

---

### 4. Vulnerability Management

Vulnerability scanning is table stakes. CERG requires authenticated scanning, a remediation workflow, and evidence that findings were closed.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary** | **Tenable (Nessus)** | Industry standard. Largest plugin library. Good API. Multi-tenant via Tenable.io. |
| **Alternate Primary** | **Qualys** | Comparable to Tenable. Better cloud/container coverage. Weaker OT. |
| **Acceptable** | **Wiz** | Cloud-first vulnerability + CSPM in one. Agentless. Best for cloud-native clients. Weak on on-prem/OT. |
| **Acceptable** | **CrowdStrike Falcon Spotlight** | Bundled with Falcon. Good for existing CrowdStrike shops. Not a standalone choice. |
| **Avoid** | **Rapid7 InsightVM / Nexpose** | Once competitive. Falling behind on cloud/container scanning. MSP program is weak. |

**CERG recommendation:** Tenable for mixed on-prem/cloud environments. Wiz for cloud-native clients.

**CERG standards:** [Asset Management and Inventory Standard](../../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) — asset inventory requirements that feed vulnerability scoping. [100-Core Baseline RA-005](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — vulnerability scanning and remediation parameters.

---

### 5. Cloud Security Posture Management (CSPM)

Every CERG client has cloud footprint — even if it's just M365 and a SaaS stack. CSPM catches misconfigurations before they become incidents.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary** | **Wiz** | Agentless, multi-cloud, broad coverage. Graph-based risk visualization. Multi-tenant. The best CSPM on the market. |
| **Acceptable** | **CrowdStrike Falcon Cloud Security** | Good if you're already in the Falcon ecosystem. Less breadth than Wiz. |
| **Acceptable** | **Microsoft Defender for Cloud** | Included with Azure. Good CSPM for Azure-only shops. Weak on AWS/GCP. |
| **Avoid** | **Palo Alto Prisma Cloud** | Powerful but complex. Requires dedicated cloud security engineers. MSP-multi-tenancy is an afterthought. |
| **Avoid** | **Lacework** | Agent-based. Slower to deploy. Narrower coverage. |

**CERG recommendation:** Wiz for multi-cloud. Microsoft Defender for Cloud if Azure-only and budget-constrained.

**CERG standards:** [Configuration Baseline Standard](../../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) — cloud configuration baselines and drift detection. [IT, Cloud, and SaaS Security Standard](../../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) — cloud security posture requirements.

---

### 6. Identity / IAM

Identity is the new perimeter. CERG requires MFA everywhere, SSO where possible, and a clear source of truth for accounts and access.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary: IAM Platform** | **Okta** | Best integration marketplace. Good API. Multi-tenant. The standard answer for MSP-delivered IAM. |
| **Alternate Primary** | **Entra ID (Azure AD)** | Included with M365. Deep Windows integration. Multi-tenant via Lighthouse. Best for M365-centric clients. |
| **Acceptable** | **JumpCloud** | Good for heterogeneous environments (Windows + Mac + Linux). Weaker enterprise features. |
| **Avoid** | **OneLogin** | Acquired, in maintenance mode. Integration marketplace is shrinking. |
|| **Avoid** | **On-prem AD without Entra ID sync** | You're operating a legacy identity store without cloud integration. This is not a CERG-compliant architecture for any client with cloud workloads. |

**CERG standard:** [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md) — MFA enforcement, SSO integration, account lifecycle management, access review cadence, and IA/AC family control parameters.

### 7. AppSec / Supply Chain

Software supply chain security is mandatory under CMMC L2 and increasingly required by cyber insurance. CERG requires SBOMs, dependency scanning, and secret detection in CI/CD.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary: Dependency** | **Trivy** | Open-source. Scans containers, filesystems, git repos, K8s. SBOM generation (CycloneDX/SPDX). Fast. CLI-first. Free. The standard answer for CERG supply chain. |
| **Primary: SAST** | **Semgrep** | Open-source. Rules-as-code. Broad language support. CI/CD integration. Multi-tenant via Semgrep Cloud or self-hosted. |
| **Acceptable** | **Snyk** | Good UI. Good integrations. Priced per developer — expensive at scale. |
| **Acceptable** | **GitHub Advanced Security** | Great if your clients are on GitHub Enterprise. CodeQL is powerful. Lock-in risk. |
| **Avoid** | **Veracode** | Slow scan times. Requires uploading code to their cloud. Weak CLI. Not MSP-friendly. |
| **Avoid** | **Checkmarx** | Enterprise pricing. Complex deployment. Overkill for SMB. |

**CERG recommendation:** Trivy for dependency/container/supply-chain scanning. Semgrep for SAST. Both are free, CLI-first, and work in CI/CD without vendor lock-in.

**CERG standards:** [Secure Software Development Standard](../../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) — SDLC security requirements, CI/CD pipeline gates, SAST/SCA integration. [100-Core Baseline SR family](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — supply chain risk management controls.

---

### 8. Detection Engineering

CERG's detection strategy is threat-intel-validated. Rules are written in Sigma format and deployed to the SIEM. The tool stack here is about rule development, testing, and validation.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary: Rule Format** | **Sigma** | Open standard. Portable across Elastic, Splunk, Wazuh, Sentinel. Write once, deploy anywhere. CERG ships Sigma rules. |
| **Primary: Testing** | **Atomic Red Team** | MITRE ATT&CK test framework. Run atomic tests, verify your SIEM catches them. Free. |
| **Acceptable** | **Chainsaw** | Fast Sigma rule testing against raw logs. Good for rule validation without a full SIEM. |
| **Acceptable** | **APT-Hunter** | Threat hunting framework. Good for purple team exercises. |
| **Avoid** | **Custom/proprietary detection languages** | Splunk SPL, Elastic EQL, KQL. Write rules in Sigma, let the converter handle translation. Proprietary rules are non-portable. |

**CERG recommendation:** Sigma for rules. Atomic Red Team for testing. Chainsaw for validation.

**CERG standard:** [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) — detection coverage tiers, Sigma rule requirements, testing cadence, and evidence parameters.

---

### 9. Backup & Cyber Resilience

Ransomware recovery starts with backups that work. CERG requires immutable, tested, offline-capable backups.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary** | **Veeam** | Industry standard for on-prem/virtualized backup. Immutable backups. Good API. Multi-tenant via Veeam Service Provider Console. |
| **Acceptable** | **Rubrik** | Cloud-native. Good ransomware detection. Pricier. Weaker on physical/OT. |
| **Acceptable** | **Cohesity** | Comparable to Rubrik. Good API. Weaker MSP multi-tenancy. |
| **Avoid** | **Commvault** | Aging architecture. Complex licensing. MSP program is inconsistent. |
| **Avoid** | **Veritas / Backup Exec** | Legacy product. Does not support modern immutable backup workflows. |
| **Avoid** | **"We use cloud snapshots"** | Snapshots are not backups. They live in the same control plane as the data they protect and can be deleted by the same compromised credentials. CERG requires offline or immutable copies. |

**CERG recommendation:** Veeam for mixed environments. Rubrik for cloud-native. Never snapshots alone.

**CERG standard:** [Cyber Resilience and Backup Standard](../../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) — immutable backup requirements, recovery testing cadence, RTO/RPO parameters, and evidence collection for CP-family controls.

---

### 10. Network Security

Firewalls, segmentation, and network monitoring. CERG requires network segmentation between IT, OT, CUI, and guest networks.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary** | **Fortinet (FortiGate)** | Broadest feature set per dollar. Good MSP program. Centralized management. SD-WAN built in. |
| **Acceptable** | **Palo Alto** | Best application-layer inspection. Pricier. MSP program is weaker. |
| **Acceptable** | **Cisco Meraki** | Easiest to manage for IT generalists. Cloud-managed. Weaker advanced security features. |
| **Avoid** | **SonicWall** | Aging platform. MSP program is good but the product is falling behind. |
| **Avoid** | **Sophos XG** | Good enough for SMB. Enterprise features are thin. |

**CERG recommendation:** Fortinet. Best MSP program, best value, broadest feature set.

**CERG standard:** [Network Security and Segmentation Standard](../../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) — segmentation requirements, firewall rule management, network monitoring, and SC-family control parameters.

---

### 11. AI Security

AI systems introduce new risks: model poisoning, prompt injection, data leakage, shadow AI. CERG treats AI as a new attack surface requiring tooling.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary: Discovery** | **Wiz AI-SPM** | Discovers AI services (OpenAI, Azure AI, GCP AI, SageMaker), maps data flows, identifies misconfigurations. Integrated with Wiz CSPM. |
| **Acceptable** | **Lasso Security** | Browser extension for shadow AI detection. Lightweight. Good for initial discovery. |
| **Acceptable** | **HiddenLayer** | AI-specific detection and response. Good for orgs with significant AI deployments. |
| **Avoid** | **Manual AI inventory via surveys** | Shadow AI moves too fast. You need automated discovery. |

**CERG recommendation:** Wiz AI-SPM for cloud AI discovery. Lasso for browser-based shadow AI detection. Both should be part of the CSPM deployment.

**CERG standard:** [Artificial Intelligence Security Standard](../../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) — AI system risk assessment, model security controls, data provenance requirements, and AI-specific evidence collection.

---

### 12. MSP/MSSP Operations Stack

Beyond the security tools, MSPs need operational tooling to deliver CERG at scale. This stack handles client onboarding, monitoring, ticketing, and reporting.

| Tier | Product | Rationale |
|------|---------|-----------|
| **Primary: RMM** | **NinjaOne** | Modern RMM. Good API. Patch management. Multi-tenant. Lightweight agent. Best balance for CERG-aligned MSPs. |
| **Acceptable** | **Datto RMM** | Good if you're in the Datto/Kaseya ecosystem. Heavier agent. |
| **Acceptable** | **ConnectWise Automate** | Powerful but complex. Requires dedicated automation engineers. |
| **Primary: Ticketing/PSA** | **HaloPSA** | Modern PSA. Good API. Multi-tenant. Integrates with ServiceNow. Best for CERG-aligned MSPs. |
| **Acceptable** | **ConnectWise Manage** | Industry standard. Aging UI. Good integrations. |
| **Primary: Documentation** | **Hudu** | IT documentation platform. Good API. Multi-tenant. Integrates with RMM and PSA. |
| **Acceptable** | **IT Glue** | More mature than Hudu. Owned by Kaseya. Pricing is opaque. |
| **Avoid** | **SolarWinds RMM** | Supply chain compromise history (2020). Ecosystem is fragmented. |
| **Avoid** | **Spreadsheets and shared drives** | You cannot run a multi-client CERG practice on spreadsheets. You need a documentation platform, a ticketing system, and an RMM. |

**CERG recommendation:** NinjaOne + HaloPSA + Hudu. Modern, API-first, multi-tenant. ServiceNow GRC ties them together at the governance layer.

**CERG practice assets:** [Engagement Playbook](../engagement-playbook-v1.md) — scoping, pricing, and delivery lifecycle. [MSP Runbook](../msp-runbook-v1.md) — tool deployment commands and per-control implementation. [GRC Rollout Guide](grc-rollout-v1.md) — wiring controls and evidence into the governance layer.

---

## Tool Integration Map

```
                    ┌──────────────────────────────┐
                    │     ServiceNow GRC (Anchor)   │
                    │  Controls · Evidence · Audit  │
                    └──────────┬───────────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌─────────────────┐    ┌────────────────┐
│   SIEM/XDR    │    │  Endpoint / EDR  │    │  Vuln Mgmt     │
│ Elastic/Wazuh │    │  SentinelOne     │    │  Tenable/Wiz   │
└───────┬───────┘    └────────┬────────┘    └───────┬────────┘
        │                     │                     │
        └──────────┬──────────┘                     │
                   │                                │
                   ▼                                ▼
        ┌─────────────────┐              ┌──────────────────┐
        │  Detection Rules │              │  CSPM / AI-SPM   │
        │  Sigma + ART     │              │  Wiz             │
        └─────────────────┘              └──────────────────┘
                   │                                │
                   ▼                                ▼
        ┌─────────────────┐              ┌──────────────────┐
        │  AppSec Pipeline │              │  Identity / IAM  │
        │  Trivy + Semgrep │              │  Okta / Entra ID │
        └─────────────────┘              └──────────────────┘
                   │                                │
                   ▼                                ▼
        ┌─────────────────────────────────────────────────────┐
        │                   MSP Operations                     │
        │  NinjaOne (RMM) · HaloPSA (Ticketing) · Hudu (Docs) │
        └─────────────────────────────────────────────────────┘
```

Every tool in this diagram has a documented API and a supported integration path to ServiceNow GRC. No custom middleware required.

---

## Decision Guide: Which Stack for Which Client?

| Client Profile | GRC | SIEM | EDR | CSPM | IAM | Backup |
|----------------|-----|------|-----|------|-----|--------|
| **SMB (<50 employees)** | Vanta | Wazuh | SentinelOne | Wiz (if cloud) | Entra ID / Okta | Veeam |
| **Mid-market (50-500)** | ServiceNow GRC | Elastic | SentinelOne | Wiz | Okta | Veeam |
| **Enterprise (500+)** | ServiceNow GRC | Elastic | CrowdStrike | Wiz | Okta | Rubrik |
| **Cloud-native** | Vanta/ServiceNow | Elastic | SentinelOne | Wiz | Okta | Cloud-native backup |
| **OT-heavy** | ServiceNow GRC | Elastic | SentinelOne | N/A (on-prem) | Entra ID (IT side) | Veeam |
| **CMMC L2** | ServiceNow GRC | Elastic | SentinelOne | Wiz (IT enclave) | Entra ID (GCC High) | Veeam |
| **Lean MSP practice** | Vanta (per-client) | Wazuh | SentinelOne | Wiz (if cloud) | Entra ID | Veeam |

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | cragin-security | Initial release: 12 categories, integration map, decision guide. Cross-references to upstream CERG standards added per category. |

### Review Triggers

- Quarterly review against vendor market changes
- Re-review if a primary vendor is acquired, has a major breach, or sunsets a key product line
- Re-review on CERG 100-Core baseline version changes

### Related Documents

- [CERG 100-Core Control Baseline](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — the full control set with MSP implementation notes for all 19 families
- [GRC Rollout Guide](grc-rollout-v1.md) — wiring ServiceNow GRC or Vanta to the CERG control framework
- [MSP Runbook](../msp-runbook-v1.md) — tool deployment commands and per-control implementation
- [Engagement Playbook](../engagement-playbook-v1.md) — scoping, pricing, SOW essentials, engagement lifecycle
- [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md) — MFA, SSO, account lifecycle, access review parameters
- [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) — detection coverage, log retention, SIEM requirements
- [Configuration Baseline Standard](../../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) — DISH baseline, hardening benchmarks, drift detection
- [Network Security and Segmentation Standard](../../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) — segmentation, firewall management, network monitoring
- [Cyber Resilience and Backup Standard](../../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) — immutable backup, recovery testing, RTO/RPO
- [Endpoint and Mobile Security Standard](../../standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) — endpoint hardening, EDR coverage, MDM
- [Secure Software Development Standard](../../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) — SDLC security, CI/CD gates, SAST/SCA
- [Artificial Intelligence Security Standard](../../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) — AI risk assessment, model security, data provenance
