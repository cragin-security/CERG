# CERG Open Source Tool Stack

## Building the CERG Operating Model Without a Software Budget

| | |
|---|---|
| **Document ID** | CERG-OPN-TOOLS-005 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Companion To** | [CERG-OPN-TOOLS-001](CERG-OPN-TOOLS-001_Opinionated_Tool_Matrix.md) |
| **Review Cycle** | Quarterly |
| **Frameworks** | CERG Practitioner Baseline · CIS Controls v8 · NIST 800-53r5 |
| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 |
| **Environments** | IT · Cloud · SaaS · OT (partial) |

---

## 1. Purpose

The companion matrix recommends commercial tools and judges each one on ServiceNow integration, an MSP partner program, and vendor documentation. No open-source project can win those three tests, so this document judges them on different questions — the ones that decide whether you can still run the tool in three years:

1. **Who patches it** when a critical bug lands on a Friday.
2. **Who carries the pager** at 02:00, and whether that number is a contract or a forum.
3. **What the licence permits** when you host it for a client, not just when you use it yourself.
4. **What an upgrade costs** in engineer hours.
5. **What your exit looks like** if the maintainer stops.

Read §4 before any table. The licence question decides more recommendations here than capability does, and it is the reason this document exists at all.

**What an open stack buys you:** no renewal risk, no seat maths at budget time, a configuration you can read and diff, evidence of control that lives in a file rather than a vendor's screenshot, and the ability to run in an environment with no internet path. For a small practice or a regulated utility with a change-board, those are not ideological points. They are the difference between a control you can show an auditor and a control you can only describe.

**What it costs you:** you become the vendor. There is no one to escalate to, no indemnity, and no one else watching for the CVE that affects you. Every recommendation below assumes you accept that and have named a person for it.

---

## 2. What "open source" means in this document

The label is not enough to decide anything, so every table carries a licence column with the actual terms. Four distinctions matter:

| Term | Meaning | What it means for you |
|---|---|---|
| **Permissive** (Apache-2.0, MIT, BSD) | Use, modify, redistribute, keep your changes private | No delivery constraint. Default choice. |
| **Copyleft** (GPL-2.0, GPL-3.0, LGPL) | Derivative works must carry the same licence | Fine to run and host. If you distribute a modified binary to a client, the source obligation travels with it. |
| **Network copyleft** (AGPL-3.0) | The obligation triggers when users reach the software over a network | Fine unmodified. The moment you host a *modified* AGPL tool for clients, you owe those clients the source of your changes. Decide this deliberately. |
| **Source-available** (Elastic-2.0, SSPL, BUSL) | You may read and often use the code; you may not build a competing service | Usable internally. Usually **prohibited** as a hosted offering to third parties. Not open source, whatever the marketing says. |
| **Restricted non-commercial** (CC BY-NC-SA) | No commercial use, including hosting for customers | Blocks client delivery outright. Check this before evaluating the product. |

A licence audit is cheaper than a licence dispute. Record the licence and version of every tool you deploy in the same register you keep for assets, and re-check it at upgrade, because licences change (see §4).

---

## 3. Read this with the commercial matrix, not instead of it

This stack is not a cheaper copy of `CERG-OPN-TOOLS-001`. Three of the twelve categories have no open-source answer that meets a CERG standard, and those categories keep their commercial recommendation:

- **§5.1 GRC** — no open-source platform survives an audit with multiple tenants.
- **§5.3 Endpoint protection** — open source gives you visibility and response, not prevention.
- **§5.12 MSP operations** — no serious open-source PSA or RMM exists.

Where both documents name a tool, take the licence gate first. If the OSS option is blocked by your delivery model, the commercial row from `CERG-OPN-TOOLS-001` still stands.

---

## 4. The licence gate: in-house use versus hosting for clients

This is the decision most practices get wrong, and it is invisible until a client asks for your source code or a lawyer reads the SOW.

| Licence class | In-house program | Hosting for clients (MSP/MSSP) |
|---|---|---|
| Permissive (Apache-2.0, MIT, BSD) | Use freely | Use freely. Best default for anything inside your delivery platform. |
| Weak copyleft (LGPL-2.1, MPL-2.0) | Use freely | Use freely. Keep your modifications in separate files where the licence asks. |
| Strong copyleft (GPL-2.0/3.0) | Use freely | Fine while you host. If you ship a patched binary to a client, ship the source too. |
| Network copyleft (AGPL-3.0) | Use freely | Fine if you do not modify it. If you do, plan to hand clients your changes or get legal review before you build a service on it. |
| Source-available (Elastic-2.0, SSPL, BUSL) | Usually fine | **Assume prohibited.** Do not build a client-facing service on it without a commercial agreement. |
| Non-commercial (CC BY-NC-SA) | Fine | **Prohibited.** |

Four cases from this stack, each resolved:

- **Vault to OpenBao.** HashiCorp relicensed Vault to the Business Source Licence at version 1.15. The community forked it as OpenBao under MPL-2.0. The exit was executed, so the lesson is not that licences are dangerous — it is that a permissive or weak-copyleft fork is what an exit actually looks like. Prefer projects that already have one.
- **OpenGRC.** A self-hosted GRC platform under the Elastic Licence 2.0. Good software for a single organisation; its terms restrict offering it to third parties as a service. That, not abandonment, is the reason to pause before an MSP adopts it.
- **Security Onion.** A complete open-source-security platform under the Elastic Licence 2.0. Ideal for an in-house sensor estate, and blocked as the product you host for clients.
- **TheHive.** Archived in December 2025 and now commercial-only. This is the one genuine abandonment case in this document, and it is worth reading carefully: the code was open, widely deployed, and the community had no fork ready. If you build a case-management workflow on a single-vendor open project, write down what you would do when it stops.

**The rule:** for any tool that touches client data, the licence is a client-facing fact, not a procurement detail. State it in the SOW, and put it in the asset register.

---

## 5. The in-house stack, by category

Verdicts below assume one organisation, single tenant, one to two people who own security alongside other work. §6 covers what changes when you host for clients.

### 5.1 GRC Platform

No open-source platform passes an audit for a multi-tenant practice, and none of them are close. GRC is mostly workflow, custody, and audit narrative — the parts open projects have not built.

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary** | **None** | — | — | Keep the commercial anchor from [CERG-OPN-TOOLS-001](CERG-OPN-TOOLS-001_Opinionated_Tool_Matrix.md) §1. |
| **Acceptable** | **Eramba Community** | Code is open; not an open-source licence | Community forum | Covers risk, compliance, privacy and incident management — four of seven use cases. Free with no user limit. A defensible answer for a small in-house team. |
| **Acceptable** | **OpenGRC** | Elastic Licence 2.0 | Community issues | Single-tenant, framework-keyed, active development. Fine for one organisation; read §4 before any other use. |
| **Avoid** | **Spreadsheets and shared drives** | — | — | An auditor reads a spreadsheet as a statement of intent, not evidence. |

**CERG standard:** [Practitioner Control Baseline](../../governance/CERG-GOV-CB-002_Practitioner_Control_Baseline.md) defines what must be tracked and evidenced. That requirement does not change with the tool.

### 5.2 SIEM and Centralised Logging

This is where open source genuinely wins, and where most practices should start.

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: SMB/lean** | **Wazuh** | GPL-2.0 core; AGPL-3.0 for the engine bundle and internal tools | You, plus the project | Agent, file integrity monitoring, log analysis, active response, vulnerability detection, compliance mapping. A complete platform at zero licence cost, with one manager per tenant. |
| **Primary: search at scale** | **OpenSearch** | Apache-2.0 | Commercial support available | The permissively licensed fork of Elasticsearch. Use it when you need long retention and dashboards without a licence question. |
| **Acceptable** | **Elastic Security** | AGPLv3 / SSPL / Elastic-2.0 for most of the tree; Apache-2.0 for some parts | Commercial support available | Genuinely capable, and open core rather than open source. Elastic Basic tier is free; the detection engine's free surface is narrower than the paid one. |
| **Acceptable** | **Security Onion** | Elastic Licence 2.0 | Community | Fastest route to a working sensor with Zeek, Suricata and Elasticsearch already wired. In-house use only (§4). |
| **Acceptable** | **Grafana + Loki** | AGPL-3.0 | Community | Good for dashboards and log search on a lean estate. Not a detection platform on its own. |
| **Avoid** | **A hand-built Elasticsearch cluster** | — | You | Running the cluster is a full-time job, and it is not the job you were hired to do. |

**CERG standard:** [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) sets detection coverage, log-source minimums, retention and evidence parameters. A free SIEM does not reduce those requirements; it moves the work to you.

### 5.3 Endpoint Protection and EDR

Be exact here, because marketing language usually is not. No open-source tool replaces a commercial EDR, and CERG requires prevention, not just observation.

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: visibility and response** | **Wazuh agent** | GPL-2.0 | You | Integrity monitoring, log collection, active response, configuration assessment. |
| **Primary: IR and hunting** | **Velociraptor** | AGPL-3.0 | Maintainer, under Rapid7 stewardship | Query-based endpoint visibility, mass hunting, and an offline collector that is the best available answer for air-gapped and OT evidence collection. Not a prevention tool. |
| **Primary: fleet truth** | **osquery** | Apache-2.0 and GPL-2.0, dual | Community | SQL against the endpoint. Best tool for answering "what is actually installed" during an incident. |
| **Acceptable** | **Falco** | Apache-2.0 | Community | Runtime detection for containers and Kubernetes. |
| **Avoid** | **Calling any of these "EDR"** | — | — | Prevention, blocking and rollback are what the [Endpoint and Mobile Security Standard](../../standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) requires. If the client needs blocking, they need a commercial EDR alongside this stack. Say so in writing. |

**CERG standard:** [Endpoint and Mobile Security Standard](../../standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) defines EDR coverage and hardening requirements.

### 5.4 Vulnerability Management

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: authenticated scanning** | **Greenbone Community Edition** | GPL-2.0 scanner; AGPL-3.0 manager | Community feed, you operate it | Full authenticated network scanning and a real remediation workflow. The community feed lags the commercial feed; account for that in your SLA. |
| **Primary: external and web surface** | **Nuclei** | MIT | Project | Template-driven checks for exposed services and known-issue patterns. Fast enough to run on every deploy. |
| **Primary: containers and images** | **Trivy** and **Grype** | Apache-2.0 | Project | Both scan images and filesystems; Trivy also generates SBOMs (§5.7). |
| **Acceptable** | **Wazuh vulnerability detection** | GPL-2.0 | You | Adequate for a lean estate where agents are already deployed. Not a substitute for authenticated network scanning. |
| **Avoid** | **ScoutSuite** | GPL-2.0 | Nobody, currently | Last substantive release activity September 2025. Do not put it on the critical path. |

**CERG standards:** [Asset Management and Inventory Standard](../../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) defines inventory scope; [Practitioner Baseline RA-005](../../governance/CERG-GOV-CB-002_Practitioner_Control_Baseline.md) sets scanning and remediation parameters.

### 5.5 Cloud Security Posture Management

The strongest open-source upgrade available to the commercial matrix, which has no open entry in this category at all.

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary** | **Prowler** | Apache-2.0 for the CLI and self-hosted server; paid private-cloud tier exists | Project, releasing most weeks | Over 650 AWS checks, plus Azure, GCP, Microsoft 365, Kubernetes, GitHub, Google Workspace and Okta. Ships compliance frameworks and a self-hosted web app. |
| **Acceptable** | **Steampipe** | AGPL-3.0 | Turbot | Query cloud APIs as SQL. Excellent for the checks a scanner does not ship, and a way to build evidence extracts for a control. |
| **Acceptable** | **Kubescape** | Apache-2.0 | Community | Kubernetes posture, NSA/CISA and CIS frameworks, admission control. |
| **Acceptable** | **Checkov** | Apache-2.0 | Community | Infrastructure-as-code scanning, so misconfiguration is caught before the account exists. |
| **Avoid** | **Assuming Prowler replaces a graph-based CSPM** | — | — | It finds misconfigurations per check. It does not aggregate them into attack paths the way Wiz does. Read the findings, do not just count them. |

**CERG standards:** [Configuration Baseline Standard](../../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) covers baselines and drift; [IT, Cloud, and SaaS Security Standard](../../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) covers cloud posture requirements.

### 5.6 Identity and IAM

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: platform** | **Keycloak** | Apache-2.0 | Commercial support available | SSO, MFA, identity brokering, fine-grained authorisation. Realms are the multi-tenancy primitive — one realm per client is the cleanest isolation in this entire stack. |
| **Primary: lighter deployment** | **Authentik** | MIT for the core; some directories separately licensed | Community | Cleaner UI and faster to stand up than Keycloak. Check the licence of every component you enable. |
| **Primary: secrets** | **OpenBao** | MPL-2.0 | Community | The permissively licensed fork of Vault, after Vault moved to the Business Source Licence. Choose this over Vault when you need to host for clients (§4). |
| **Acceptable** | **MISP** | AGPL-3.0 | Community | Threat-intel sharing, and usable as an indicator store feeding identity and network detections. |
| **Avoid** | **On-premises directory with no federation** | — | You | No MFA path, no conditional access, no reviewable group model. Not a CERG-compliant architecture. |

**CERG standard:** [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md) sets MFA enforcement, SSO, lifecycle and access-review cadence.

### 5.7 AppSec and Supply Chain

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: dependencies and containers** | **Trivy** | Apache-2.0 | Aqua, plus community | Filesystem, repo, container and Kubernetes scanning; SBOM generation in CycloneDX and SPDX. |
| **Primary: SBOM** | **Syft** | Apache-2.0 | Anchore | Generate the SBOM once and feed both the scanner and the evidence store. |
| **Primary: SAST** | **Semgrep OSS** | LGPL-2.1 | Commercial support available | Rules as code, broad language coverage, runs in CI. The paid platform adds cross-file analysis; the OSS engine covers the standard's gate. |
| **Primary: secrets** | **Gitleaks** | MIT | Community | Pre-commit and CI secret detection. |
| **Primary: finding of record** | **DefectDojo** | BSD-3-Clause | Community | This is the piece most lean stacks skip, and the one the standard actually needs: findings with an owner, a status and a closure date you can show an auditor. |
| **Acceptable** | **TruffleHog** | AGPL-3.0 | Community | Broader verification of found credentials. Mind the licence if you build a service on it (§4). |
| **Avoid** | **Scanner output as evidence** | — | — | A JSON file from a CLI is a finding, not closure. Without a system of record the standard cannot be evidenced. |

**CERG standard:** [Secure Software Development Standard](../../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) sets SDLC gates and SAST/SCA requirements; [Practitioner Baseline SR family](../../governance/CERG-GOV-CB-002_Practitioner_Control_Baseline.md) covers supply-chain risk.

### 5.8 Detection Engineering

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: rule format** | **Sigma** | Rules under the Detection Rule Licence 1.1; specification open | SigmaHQ | Portable rules. Write once, translate to the SIEM you happen to run. Note that the rule licence is not OSI-approved — read it before redistributing rules commercially. |
| **Primary: translation** | **pySigma** | LGPL-2.1 | SigmaHQ | Backends for the major SIEMs. This is what makes the rules portable in practice. |
| **Primary: testing** | **Atomic Red Team** | MIT | Red Canary | Small, executable technique tests. Run one, confirm your SIEM saw it, record the result. |
| **Acceptable** | **Caldera** | Apache-2.0 | MITRE | Automated adversary emulation. Use it once ART has proven individual detections. |
| **Acceptable** | **Chainsaw** | GPL-3.0 | WithSecure | Rapid Sigma matching against raw event logs and forensic artefacts. Excellent for validating a rule before it goes live. |
| **Acceptable** | **Hayabusa** | AGPL-3.0 | Community | Fast Windows event-log hunting with Sigma. |
| **Avoid** | **Rules written only in a proprietary query language** | — | You | SPL, KQL and EQL rules do not travel. Keep the canonical rule in Sigma and treat the translated artefact as build output. |

**CERG standard:** [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) sets coverage tiers, rule requirements and testing cadence; [Threat Intel Validation](CERG-OPN-TOOLS-004_Threat_Intel_Validation.md) covers feeding exploits-in-the-wild evidence into rule priority.

### 5.9 Backup and Cyber Resilience

The standard asks for immutable, tested, offline-capable copies. It does not name a product, and open source satisfies it.

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: object storage** | **restic** | BSD-2-Clause | Community | Encrypted, deduplicated, append-only repositories in S3-compatible storage with object lock enabled. Object lock is what makes the copy immutable — the tool does not do it for you. |
| **Primary: alternate** | **Kopia** | Apache-2.0 | Community | Comparable feature set with a policy model that suits many endpoints. |
| **Primary: virtualised estates** | **Proxmox Backup Server** | AGPL-3.0 | Community | Image-level backup with verification, for a Proxmox estate or as a target for other hypervisors. |
| **Primary: Kubernetes** | **Velero** | Apache-2.0 | Community | Cluster and volume backup with restore testing. |
| **Acceptable** | **Borg** | BSD-3-Clause | Community | Mature and well understood. Weaker object-storage story than restic. |
| **Avoid** | **Snapshots and sync-only mirrors** | — | — | A snapshot lives in the same control plane as the data it protects. A mirror faithfully replicates the ransomware. |
| **Avoid** | **Backups with no tested restore** | — | You | The requirement is a restore you have performed, with a date next to it. Nothing in this stack performs that test for you. |

**CERG standard:** [Cyber Resilience and Backup Standard](../../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) sets immutability, recovery-testing cadence and RTO/RPO parameters.

### 5.10 Network Security and Monitoring

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: firewall and segmentation** | **OPNsense** | BSD-2-Clause | Community | Full-featured firewall, VLANs, IDS integration, frequent releases. The better-maintained of the two open firewall platforms. |
| **Acceptable** | **pfSense CE** | Apache-2.0 | Netgate | Proven, and the community edition trails the commercial Plus edition. Check the feature gap before standardising on it. |
| **Primary: network security monitoring** | **Suricata** | GPL-2.0 | OISF | Signature IDS/IPS, broad rule ecosystem, high throughput. |
| **Primary: protocol analysis** | **Zeek** | BSD-style, University of California | Community | Connection logs and protocol analysis that turn network traffic into evidence. Pair with Suricata rather than choosing between them. |
| **Acceptable** | **CrowdSec** | MIT | Community | Behaviour-based blocking with a shared reputation network. Good value where you have no dedicated analyst. |
| **Avoid** | **Monitoring a segment you have not defined** | — | — | [Network Security and Segmentation Standard](../../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) requires defined segments first. Sensors on an undefined estate produce noise, not coverage. |
| **Avoid** | **Expecting open routing and switching** | — | — | Firewalls and monitoring are solved. Data-centre switching silicon is not. Budget for hardware. |

**CERG standard:** [Network Security and Segmentation Standard](../../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) sets segmentation, firewall rule management and monitoring requirements.

### 5.11 AI Security

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: model testing** | **garak** | Apache-2.0 | NVIDIA, plus community | Probes LLMs for prompt injection, jailbreaks, data leakage and hallucination. Run it against any model you deploy. |
| **Primary: evaluation and red team** | **promptfoo** | MIT | Community | Test suites for prompts and agents, in CI, with results you can diff between releases. |
| **Acceptable** | **Prowler LLM checks** | Apache-2.0 | Project | Cloud-side AI service discovery and configuration checks, shipped inside the CSPM you already run (§5.5). |
| **Avoid** | **Manual AI inventory through surveys** | — | — | Shadow AI outruns a survey. |
| **Avoid** | **Expecting this to find shadow AI in SaaS** | — | — | Nothing here sees browser extensions and unsanctioned SaaS the way a CASB does. That gap is real and must be stated as residual risk. |

**CERG standard:** [Artificial Intelligence Security Standard](../../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) sets AI risk assessment, model security and provenance requirements.

### 5.12 MSP and Service Operations

No open-source PSA or RMM reaches delivery grade. In-house service management is a different question and is well served.

| Tier | Product | Licence | Who carries the pager | Note |
|---|---|---|---|---|
| **Primary: ticketing** | **Zammad** | AGPL-3.0 | Community, paid hosting available | Solid helpdesk, SLA handling, API. Enough for an in-house service desk. |
| **Primary: assets and CMDB** | **GLPI** | GPL-3.0 | Community | Asset inventory, tickets, contracts, licence management. Pairs well with the inventory the [Asset Management and Inventory Standard](../../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) requires. |
| **Acceptable** | **Shuffle** | AGPL-3.0 | Community | SOAR playbooks for enrichment and case routing. Read §4 before hosting it for clients. |
| **Avoid for MSP delivery** | **This category, collectively** | — | — | Multi-tenant billing, per-client reporting and dispatch are what a PSA sells. There is no open equivalent. Keep the commercial PSA and RMM from [CERG-OPN-TOOLS-001](CERG-OPN-TOOLS-001_Opinionated_Tool_Matrix.md) §12. |

**CERG practice assets:** [MSP Runbook](../CERG-OPN-MSP-001_MSP_MSSP_Runbook.md) and [Engagement Playbook](../CERG-OPN-DLV-001_Engagement_Playbook.md) describe delivery workflow. Adopting this stack does not change the workflow, only the tools underneath it.

---

## 6. What changes when you host for clients

Only the categories whose verdict actually moves are listed. Anything not named here reads the same as §5.

**Hard blocks.** Do not put these into a client-facing service without a commercial agreement: Security Onion, OpenGRC, and the non-Apache parts of Elastic. All are source-available, not open source. Their terms are about exactly the thing you would be doing.

**AGPL tools need a written policy.** Velociraptor, Greenbone's manager, Steampipe, TruffleHog, Zammad, Shuffle, MISP and Grafana are all AGPL-3.0. Run unmodified, they are fine. If you patch one and serve it to clients, you owe those clients the source of your patch. Decide once, write it in the delivery standard, and either keep them unmodified or route modifications upstream.

**Tenancy patterns that work:**

| Category | Pattern | Why |
|---|---|---|
| Identity | **One Keycloak realm per client** | Strongest isolation in the stack, and it makes offboarding a delete rather than an archaeology project. |
| SIEM | **One Wazuh manager per client** | Avoids cross-tenant log exposure and keeps ingestion failures contained. Costs a VM per client. |
| CSPM | **One Prowler role per client account, one scan target each** | Findings stay attributable without extra engineering. |
| Backup | **One restic repository and key per client** | Key separation is the whole protection. Shared repos fail the isolation test. |
| Findings | **One DefectDojo product per client** | Closure evidence stays per-client and exportable at offboarding. |

**What you must add that the tools do not give you:** an upgrade calendar with a named owner per tool, a per-client data-separation statement in the SOW, a documented exit (where does the data go, in what format, and who deletes it), and a support position for each tool that a client can read — including the honest version, which for several of these is "community forum, best effort, we hold the SLA".

---

## 7. Where open source loses

Say these out loud to a client rather than letting them discover it.

- **GRC.** Not close. Workflow, custody and audit narrative are the product, and the open projects are single-tenant and thin on both.
- **Endpoint prevention.** Open source observes and responds. It does not block and roll back.
- **Shadow-AI discovery.** No open tool watches browsers and unsanctioned SaaS.
- **Orchestrated recovery testing.** Restic restores a file. Proving an RTO is a rehearsal you run and document.
- **Curated detection content and threat intel.** Community content is good and uneven. Budget analyst time to filter it.
- **Indemnity.** Nobody to sue, nobody to call at 02:00. Price the pager time into the engagement.

---

## 8. Three reference builds

**A. Lean in-house, one to two security people.** Wazuh, Prowler, Trivy with Semgrep and Gitleaks, DefectDojo as the finding of record, Sigma with Atomic Red Team, restic into object-locked storage, OPNsense with Suricata and Zeek, Keycloak, GLPI with Zammad, garak and promptfoo. Licence cost is zero. The real cost is the FTE and the hardware, and the honest constraint is that one person now owns nine upgrade paths.

**B. Multi-tenant MSP delivery.** Keep the commercial GRC, PSA and RMM from the companion matrix. Add Wazuh per tenant, Prowler per client account, Keycloak realms, per-client restic repositories, per-client DefectDojo products, and a one-page AGPL policy in the delivery standard. The commercial licence cost falls; the engineering cost rises; the SOW grows a section.

**C. Air-gapped or OT estate.** Wazuh manager with a local rule set and no external feed, Velociraptor offline collector for endpoint evidence, Trivy with a mirrored database, Sigma rules run through Chainsaw against collected artefacts, restic to removable media with a documented rotation, and OPNsense for the boundary between IT and OT. This build is where open source has no commercial equal: every component runs with no internet path.

---

## 9. Integration map

```
                    ┌──────────────────────────────┐
                    │   Commercial GRC (anchor)    │
                    │  Controls · Evidence · Audit │
                    └──────────┬───────────────────┘
                               │  API + export
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌─────────────────┐    ┌────────────────┐
│  Wazuh (SIEM) │    │  osquery        │    │  Prowler       │
│  OpenSearch   │    │  Velociraptor   │    │  Trivy         │
└───────┬───────┘    └────────┬────────┘    └───────┬────────┘
        │                     │                     │
        └──────────┬──────────┘                     │
                   ▼                                ▼
        ┌─────────────────┐              ┌──────────────────┐
        │  Sigma + pySigma│              │  DefectDojo      │
        │  Chainsaw · ART │              │  finding of record│
        └────────┬────────┘              └────────┬─────────┘
                 │                                │
                 ▼                                ▼
        ┌─────────────────┐              ┌──────────────────┐
        │  Keycloak       │              │  restic / Kopia  │
        │  OpenBao        │              │  object lock     │
        └─────────────────┘              └──────────────────┘
```

The arrows that matter are the ones into the GRC platform. Most of these tools export JSON, CSV or an API; the work is not the integration, it is deciding which field becomes the evidence artefact and who signs it.

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-11-16 | cragin-security | Initial release: licence gate across five licence classes, twelve categories with licence and support ownership, multi-tenant delivery section, three reference builds, integration map. Companion to CERG-OPN-TOOLS-001. |

### Review Triggers

- Quarterly, together with the commercial matrix
- Re-review whenever a named project changes licence, changes maintainer, or archives
- Re-review when a client delivery model changes from in-house to hosted, or the reverse
- Re-review on CERG Practitioner Baseline version changes

### Related Documents

- [CERG-OPN-TOOLS-001](CERG-OPN-TOOLS-001_Opinionated_Tool_Matrix.md) — the commercial matrix this document pairs with
- [CERG-OPN-TOOLS-003](CERG-OPN-TOOLS-003_Evidence_Automation_Mapping.md) — control-to-tool evidence pipelines
- [CERG-OPN-TOOLS-004](CERG-OPN-TOOLS-004_Threat_Intel_Validation.md) — exploit-in-the-wild evidence for rule priority
- [MSP/MSSP Runbook](../CERG-OPN-MSP-001_MSP_MSSP_Runbook.md) — deployment commands and per-control implementation
- [Engagement Playbook](../CERG-OPN-DLV-001_Engagement_Playbook.md) — scoping, pricing, delivery lifecycle
- [Practitioner Control Baseline](../../governance/CERG-GOV-CB-002_Practitioner_Control_Baseline.md) — the control set these tools must evidence
- [Document Catalog and Naming Convention](../../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) — registration rules and domain codes
- [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) — detection coverage, retention, SIEM requirements
- [Endpoint and Mobile Security Standard](../../standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) — EDR coverage, hardening, MDM
- [Cyber Resilience and Backup Standard](../../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) — immutability, recovery testing, RTO/RPO
- [Network Security and Segmentation Standard](../../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) — segmentation, firewall management, monitoring
- [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md) — MFA, SSO, lifecycle, access review
- [Secure Software Development Standard](../../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) — SDLC gates, SAST/SCA, SBOM
- [Configuration Baseline Standard](../../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) — baselines, hardening benchmarks, drift
- [Artificial Intelligence Security Standard](../../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) — AI risk assessment, model security, provenance
