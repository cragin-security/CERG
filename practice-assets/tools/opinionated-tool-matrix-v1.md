1|# CERG Opinionated Tool Matrix
2|
3|## Practitioner-Grade Tool Recommendations for CERG Adoption
4|
5|| | |
6||---|---|
7|| **Document ID** | CERG-OPN-TOOLS-001 |
8|| **Version** | 1.0.0 |
9|| **Status** | Draft |
10|| **Classification** | Public |
11|| **Owner** | Consulting Practice Lead |
12|| **Parent Policy** | CERG-POL-001 |
13|| **Review Cycle** | Quarterly |
14|| **Frameworks** | CERG 100-Core · CIS Controls v8 · NIST 800-53r5 |
15|| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 |
16|| **Environments** | IT · Cloud · SaaS · OT (partial) |
17|
18|---
19|
20|## Purpose
21|
22|This document defines the opinionated tool stack for CERG adopters who work through an MSP, MSSP, or in-house IT generalist. Every recommendation here is based on three criteria:
23|
24|1. **Integration surface** — Does it talk to ServiceNow GRC and the rest of the stack without custom middleware?
25|2. **MSP/MSSP multi-tenancy** — Can a single instance or deployment manage multiple client organizations cleanly?
26|3. **IT generalist usability** — Can someone without a dedicated SOC engineer configure it using vendor documentation alone?
27|
28|Each category lists a **Primary** (the recommendation), **Acceptable** alternatives (decent but weaker on at least one criterion), and **Avoid** (popular tools that fail hard on the CERG criteria).
29|
30|---
31|
32|## Tool Categories
33|
34|### 1. GRC Platform — The Anchor
35|
36|The GRC platform is the spine of the CERG program. Every other tool reports into it. Controls are tracked here. Evidence lives here or is linked from here. Audits open here.
37|
38|| Tier | Product | Rationale |
39||------|---------|-----------|
40|| **Primary** | **ServiceNow GRC** | Full IT service management + GRC. Controls, evidence, risk register, audit management, compliance dashboards all in one platform. Multi-tenant via domain separation. The only platform that straddles IT operations AND GRC without a messy handoff. |
41|| **Acceptable** | **Vanta** | Best-in-class for SMB compliance automation (SOC 2, ISO 27001, HIPAA). Agent-based evidence collection. Weak on operational risk and IT service management — you'll need separate tools for incident/change management. Good for startups and small practices. |
42|| **Acceptable** | **Drata** | Similar to Vanta. Slightly better auditor UX, slightly weaker integrations. For SMB compliance-only use cases. |
43|| **Avoid** | **Archer** | Legacy architecture, high customization cost, requires dedicated Archer developers. Multi-tenancy is an afterthought. |
44|| **Avoid** | **OpenGRC / Eramba** | Free but abandonware risk. No MSP multi-tenancy. No API ecosystem. |
45|| **Avoid** | **Spreadsheets** | You will lose audit credibility immediately. A spreadsheet is not a GRC platform and auditors know it. |
46|
47|**CERG recommendation:** ServiceNow GRC for any organization with 50+ employees or multi-client MSP/MSSP delivery. Vanta for SMB clients under 50 employees where compliance automation matters more than operational integration.
48|
49|**Integration note:** ServiceNow GRC has native integrations with most SIEM and endpoint tools. Vanta's integrations are narrower — Wiz, AWS, Azure, GCP, GitHub, Jamf, Intune. Budget for middleware if you need Vanta-to-non-cloud-tool integration.
50|
51|---
52|
53|### 2. SIEM / Centralized Logging
54|
55|The SIEM is the operational brain. It ingests from endpoint, network, cloud, identity, and application sources. Detection rules fire here. Investigations start here.
56|
57|| Tier | Product | Rationale |
58||------|---------|-----------|
59|| **Primary: Enterprise** | **Elastic Security** | Full EDR + SIEM in one platform. Open detection engine. Sigma rule support. Agent-based collection. Multi-tenant via Elastic Cloud. The best balance of capability, cost, and MSP-friendliness at scale. |
60|| **Primary: SMB/Lean** | **Wazuh** | Open-source XDR. Lightweight agent. File integrity monitoring. Good compliance mapping (PCI, HIPAA, GDPR). Free. Multi-tenancy via separate managers or virtual appliances per client. Best for MSPs running on thin margins. |
61|| **Acceptable** | **Splunk** | Best analytics engine. Best app marketplace. Priced per GB ingested — becomes punitive at scale unless you have an ELA. Multi-tenancy requires Splunk Cloud or heavy engineering. |
62|| **Acceptable** | **Microsoft Sentinel** | Native Azure integration. Good if clients are already M365 E5. Weak on non-Windows endpoints, OT, and network. Pricing is consumption-based — hard to predict. |
63|| **Avoid** | **QRadar** | End-of-life migration to SaaS underway. Avoid until the dust settles. |
64|| **Avoid** | **LogRhythm** | Aging architecture. MSP multi-tenancy is clunky. |
65|| **Avoid** | **DIY ELK** | Building your own Elasticsearch cluster is a full-time job. Use Elastic Cloud or Wazuh. |
66|
67|**CERG recommendation:** Wazuh for SMB clients and lean MSP stacks. Elastic Security when the client has the budget and needs EDR + SIEM convergence.
68|
69|---
70|
71|### 3. Endpoint Protection / EDR
72|
73|Endpoint is the first line of defense and the richest source of detection telemetry. CERG requires EDR, not signature-only antivirus.
74|
75|| Tier | Product | Rationale |
76||------|---------|-----------|
77|| **Primary** | **SentinelOne Singularity** | Strong detection with minimal noise. Multi-tenant console with RBAC per client site. API that talks to ServiceNow. Good offline detection for OT/air-gapped. |
78|| **Acceptable** | **CrowdStrike Falcon** | Best threat intel. Best IR capabilities. Multi-tenant via Falcon Complete for MSSPs. Pricier than SentinelOne. Overkill for SMB. |
79|| **Acceptable** | **Microsoft Defender for Endpoint** | Included in M365 E5. Deep Windows integration. Weaker on Linux/Mac. Multi-tenant via Lighthouse. |
80|| **Avoid** | **Symantec / Broadcom** | Aging detection engine. Multi-tenancy is an afterthought. Integration surface is shrinking. |
81|| **Avoid** | **McAfee / Trellix** | Fragmented product line. MSP program is inconsistent. |
82|| **Avoid** | **Bitdefender GravityZone** | Decent detection, weak API. Does not integrate cleanly with ServiceNow. |
83|
84|**CERG recommendation:** SentinelOne. Good enough detection, excellent MSP console, solid ServiceNow integration. CrowdStrike if the client has breach history or is a high-value target.
85|
86|---
87|
88|### 4. Vulnerability Management
89|
90|Vulnerability scanning is table stakes. CERG requires authenticated scanning, a remediation workflow, and evidence that findings were closed.
91|
92|| Tier | Product | Rationale |
93||------|---------|-----------|
94|| **Primary** | **Tenable (Nessus)** | Industry standard. Largest plugin library. Good API. Multi-tenant via Tenable.io. |
95|| **Alternate Primary** | **Qualys** | Comparable to Tenable. Better cloud/container coverage. Weaker OT. |
96|| **Acceptable** | **Wiz** | Cloud-first vulnerability + CSPM in one. Agentless. Best for cloud-native clients. Weak on on-prem/OT. |
97|| **Acceptable** | **CrowdStrike Falcon Spotlight** | Bundled with Falcon. Good for existing CrowdStrike shops. Not a standalone choice. |
98|| **Avoid** | **Rapid7 InsightVM / Nexpose** | Once competitive. Falling behind on cloud/container scanning. MSP program is weak. |
99|
100|**CERG recommendation:** Tenable for mixed on-prem/cloud environments. Wiz for cloud-native clients.
101|
102|---
103|
104|### 5. Cloud Security Posture Management (CSPM)
105|
106|Every CERG client has cloud footprint — even if it's just M365 and a SaaS stack. CSPM catches misconfigurations before they become incidents.
107|
108|| Tier | Product | Rationale |
109||------|---------|-----------|
110|| **Primary** | **Wiz** | Agentless, multi-cloud, broad coverage. Graph-based risk visualization. Multi-tenant. The best CSPM on the market. |
111|| **Acceptable** | **CrowdStrike Falcon Cloud Security** | Good if you're already in the Falcon ecosystem. Less breadth than Wiz. |
112|| **Acceptable** | **Microsoft Defender for Cloud** | Included with Azure. Good CSPM for Azure-only shops. Weak on AWS/GCP. |
113|| **Avoid** | **Palo Alto Prisma Cloud** | Powerful but complex. Requires dedicated cloud security engineers. MSP-multi-tenancy is an afterthought. |
114|| **Avoid** | **Lacework** | Agent-based. Slower to deploy. Narrower coverage. |
115|
116|**CERG recommendation:** Wiz for multi-cloud. Microsoft Defender for Cloud if Azure-only and budget-constrained.
117|
118|---
119|
120|### 6. Identity / IAM
121|
122|Identity is the new perimeter. CERG requires MFA everywhere, SSO where possible, and a clear source of truth for accounts and access.
123|
124|| Tier | Product | Rationale |
125||------|---------|-----------|
126|| **Primary: IAM Platform** | **Okta** | Best integration marketplace. Good API. Multi-tenant. The standard answer for MSP-delivered IAM. |
127|| **Alternate Primary** | **Entra ID (Azure AD)** | Included with M365. Deep Windows integration. Multi-tenant via Lighthouse. Best for M365-centric clients. |
128|| **Acceptable** | **JumpCloud** | Good for heterogeneous environments (Windows + Mac + Linux). Weaker enterprise features. |
129|| **Avoid** | **OneLogin** | Acquired, in maintenance mode. Integration marketplace is shrinking. |
130|| **Avoid** | **On-prem AD without Entra ID sync** | You're operating a legacy identity store without cloud integration. This is not a CERG-compliant architecture for any client with cloud workloads. 

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
| 1.0.0 | 2026-07-03 | cragin-security | Initial release: 12 categories, integration map, decision guide |

### Review Triggers

- Quarterly review against vendor market changes
- Re-review if a primary vendor is acquired, has a major breach, or sunsets a key product line
- Re-review on CERG 100-Core baseline version changes

### Related Documents

- [CERG 100-Core Control Baseline](CERG-GOV-CB-002_100-Core_Control_Baseline.md) (in development)
- [GRC Rollout Guide](grc-rollout-v1.md)
- [MSP Runbook](msp-runbook-v1.md) (in development)
