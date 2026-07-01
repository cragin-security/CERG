# CERG Opinionated Tool Stack · v1

**Domain name:** people know this at-a-glance; **tool** our recommendation; followed by the structural decision logic.

---

## 1. Identity & Access Management (IAM)

| Tier | Primary | Acceptable | Avoid | Rationale |
|------|---------|------------|-------|-----------|
| **SMB (<200 users)** | Entra ID P1 | JumpCloud, Google Cloud Identity Free | On-prem AD without sync | M365 is near-universal in this tier; Entra ID P1 includes CA, MFA, SSPR |
| **Mid-market (200–2k)** | Entra ID P2 | Okta | Oracle Identity, ForgeRock | P2 unlocks PIM, Entitlement Mgmt, Identity Protection |
| **Enterprise (2k+)** | Entra ID P2 + Okta (multi-IdP) | — | Homegrown SSO | Both IdPs for acquisition/heterogeneous scenarios; Okta for non-Microsoft apps |

### Privileged Access Management (PAM)

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **SMB** | Entra PIM | LAPS | No PAM at all |
| **Mid-market** | Entra PIM + CyberArk | Delinea (Thycotic) | BeyondTrust for pure on-prem |
| **Enterprise** | CyberArk | BeyondTrust, Delinea | Keepas/Excel for privileged passwords |

---

## 2. Endpoint Detection & Response (EDR / XDR)

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **All tiers** | **SentinelOne** | CrowdStrike Falcon | McAfee, Symantec, Trend Micro legacy AV |
| — | — | Defender for Endpoint (M365 E5 shops) | Cylance, Carbon Black (deprecated models) |

**Why SentinelOne over CrowdStrike:**
- Autonomous rollback of ransomware encryption (not just detection)
- No internet dependency for core detection (CrowdStrike is cloud-required)
- Storyline technology correlates related events without cloud hop
- More aggressive pricing at SMB tier

**Why SentinelOne when CrowdStrike is fine:**
- E5 shops already have Defender for Endpoint bundled — use it
- Regulated clients that insist on FedRAMP-authorised → CrowdStrike

---

## 3. SIEM & Log Management

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **SMB** | Sentinel (M365) / Wazuh (non-M365) | Splunk free (50GB/day) | SumoLogic, LogRhythm |
| **Mid-market** | Sentinel | Splunk Cloud | LogRhythm (maintenance-heavy) |
| **Enterprise** | Splunk Cloud + Sentinel (hybrid) | Panther, Chronicle | Graylog (insufficient for compliance) |

**The split:**
- If the client is on M365 → Sentinel is default. Native M365/Entra/Azure log ingest, KQL, no extra licensing for M365 logs.
- If the client is non-Microsoft or hybrid → Splunk for log parsing breadth.
- If the client has zero budget → Wazuh. It is free and covers FIM, SIEM, and compliance reporting.

---

## 4. Vulnerability Management

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **SMB** | Nessus Professional | OpenVAS, Qualys Free | Nexpose (Rapid7 discontinued focus) |
| **Mid-market** | Qualys VMDR | Tenable.io | InsightVM (Rapid7 — good but expensive for what it does) |
| **Enterprise** | Qualys VMDR + Wiz | Tenable.io, Rapid7 | Outdated scanner-only solutions |
| **Cloud-native** | Wiz | Defender for Cloud, AWS Inspector | Prisma Cloud (Palo Alto — complex licensing) |

**Wiz is in a special category:**
- Agentless cloud scanning (no agents on 50k workloads)
- Exploit path analysis (shows attack path, not just CVSS)
- Graph-based IaC scanning integrated
- Use Wiz for cloud + Qualys for on-prem/OT hybrid

---

## 5. Cloud Security Posture (CSPM / CWPP / CIEM)

| Capability | Primary | Acceptable | Avoid |
|------------|---------|------------|-------|
| CSPM | Wiz | Defender for Cloud, AWS Security Hub | Prisma Cloud |
| CIEM | Entra ID (Azure) / Wiz (multi) | Saviynt | Manual RBAC reviews |
| IaC scanning | Checkov + Trivy | tfsec, Snyk IaC | Palo Alto Prisma IaC |

---

## 6. Network Security

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **ZTNA / SASE** | Cloudflare Zero Trust | Zscaler, Netskope | Legacy VPN-only |
| **SMB Firewall** | pfSense/OPNsense | Ubiquiti Dream Machine | Consumer routers (Linksys, Netgear) |
| **Mid-market Firewall** | Fortinet / Meraki MX | Palo Alto (pricey) | SonicWall (EOL) |
| **Enterprise Firewall** | Palo Alto | Fortinet | Check Point (legacy) |
| **SD-WAN** | Meraki | VeloCloud, FortiGate SD-WAN | MPLS-only, no SD-WAN |

**Why Cloudflare Zero Trust is the default:**
- Free tier for small teams (up to 50 users)
- No open inbound ports (eliminates RDP/SSH exposure entirely)
- MFA built in, device posture checks, browser isolation
- Application-layer access — user reaches the app, not the network

---

## 7. Backup & Resilience

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **SMB** | Veeam (free edition) | Acronis, Windows Backup | Tape-only |
| **Mid-market** | Veeam (paid) | Rubrik | Cohesity (complex) |
| **Enterprise** | Rubrik or Veeam + Azure Backup | Cohesity, Commvault (legacy) | — |

**Veeam is the default** because:
- Immutable storage (S3 Object Lock / Azure Blob immutability)
- Image-level backups, instant VM recovery
- Free edition covers 10 workloads
- Broad platform support (VMware, Hyper-V, physical, cloud)

---

## 8. Asset Management / CMDB

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **SMB** | Snipe-IT (free) | GLPI, Excel (🚨) | — |
| **Mid-market** | Device42 | ServiceNow CMDB | Spreadsheets |
| **Enterprise** | ServiceNow CMDB | Device42, BMC Helix | Homegrown databases |

---

## 9. Penetration Testing & Adversarial Validation

| Type | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **Automated pentest** | Pentera | Cymulate, AttackIQ | Open-source scanners only |
| **Human-led (app)** | Cobalt | Synack, HackerOne Bug Bounty | Bug bounty without prior pentest |
| **Human-led (network)** | HackTheBox Enterprise | Cobalt, pentest firm | Self-reported (coverage gaps) |
| **Purple team** | Pentera + human | Cymulate + human | Automated-only without human validation |

---

## 10. GRC (Governance, Risk, Compliance)

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **SMB (<200)** | Vanta / Drata | SharePoint list + CERG template | OneTrust (too expensive, overengineered) |
| **Mid-market (200–2k)** | OneTrust / LogicGate | ServiceNow GRC (if SN already) | Spreadsheet-only (becomes unmanageable) |
| **Enterprise (2k+)** | **ServiceNow GRC** | OneTrust, AuditBoard | Homegrown GRC |

**Why ServiceNow GRC is the enterprise pick:**
The "Swiss Army knife" argument is correct — ServiceNow already does ITSM, ITOM, HR, CSM, and SecOps for most enterprises. Adding GRC means:
- Controls live in the same platform as change tickets and incidents
- Evidence collection is automated via integrations to the SN platform
- Policy management, risk register, vendor risk, and audit management in one UI
- The CISO lives in the same dashboard as the IT team

**But ServiceNow is wrong for SMB/mid-market** because:
- $150k+/year minimum before implementation
- Requires dedicated platform administrator
- Takes 6+ months to configure properly
- For a consulting startup, you cannot ServiceNow-enable every client

**Practice recommendation:**
- **Internally for the practice**: Vanta or Drata (automated evidence collection, SOC 2 roadmap, costs $5-15k/year). This gives you a GRC tool to dogfood and demonstrate.
- **For SMB clients**: Vanta/Drata (sell the GRC setup as a 2-week engagement)
- **For mid-market clients**: OneTrust or LogicGate (sell as 4-6 week engagement)
- **For enterprise clients**: ServiceNow GRC (sell as 12-16 week engagement with implementation partner)

---

## 11. Security Awareness Training

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **All tiers** | KnowBe4 | M365 Defender for Office 365 Training | Generic annual slide deck |
| **SMB** | KnowBe4 (starter) | GoPhish (free, self-hosted) | "Just the annual HR video" |

---

## 12. Detection Engineering

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **Sigma rules** | Sigma (open format) | Splunk ES, Sentinel Analytics | Vendor-locked rules only |
| **Detection-as-code** | Panther (detection-as-code platform) | Splunk ES | Manual rule writing |

---

## 13. Supply Chain & Vendor Risk

| Tier | Primary | Acceptable | Avoid |
|------|---------|------------|-------|
| **SMB** | Questionnaire + Spreadsheet | UpGuard Free | No assessment |
| **Mid-market** | Whistic / OneTrust | UpGuard, SecurityScorecard | — |
| **Enterprise** | ServiceNow Vendor Risk | OneTrust TPRM | — |

---

## 14. Framework Alignment: Mapping CERG Pillars to Tools

| CERG Pillar | Capability | Tool (Primary) | Tool (Acceptable) |
|-------------|------------|----------------|-------------------|
| **Engineering** | Identity | Entra ID + PIM | Okta + CyberArk |
| **Engineering** | Endpoints | SentinelOne | CrowdStrike, Defender |
| **Engineering** | Cloud | Wiz | Defender for Cloud |
| **Engineering** | Network | Cloudflare ZT | Meraki, Palo Alto |
| **Engineering** | SIEM | Sentinel | Splunk, Wazuh |
| **Risk** | Vuln Mgmt | Qualys + Wiz | Tenable, Wazuh |
| **Risk** | Adversarial | Pentera + Cobalt | Cymulate, HTB |
| **Risk** | Supply Chain | Whistic | OneTrust TPRM |
| **Risk** | Risk Register | ServiceNow GRC / OneTrust | Vanta, Drata |
| **Governance** | Policy Mgmt | ServiceNow GRC | SharePoint, OneTrust |
| **Governance** | Training | KnowBe4 | M365, GoPhish |
| **Governance** | Backup | Veeam | Rubrik, Azure Backup |

---

## 15. Pricing Guide (Approximate Annual, SaaS)

| Tool | SMB (50 users) | Mid-market (500 users) | Enterprise (5k+ users) |
|------|---------------|-----------------------|----------------------|
| Entra ID P1/P2 | $1,500 | $54,000 | $540,000 |
| SentinelOne | $2,500 | $37,500 | $375,000 |
| Sentinel SIEM | $0 (included M365) | $37,500 | $375,000 |
| Splunk Cloud | — | $100,000 | $1M+ |
| Wiz | $10,000 | $75,000 | $500,000+ |
| Cloudflare ZT | Free | $15,000 | $100,000+ |
| Veeam | Free | $1,500 | $15,000+ |
| Vanta/Drata | $12,000 | $36,000 | — |
| OneTrust | — | $60,000 | $150,000+ |
| ServiceNow GRC | — | — | $150,000+ |
| KnowBe4 | $2,500 | $12,000 | $60,000+ |
| **Total estimated** | **$30k–50k** | **$400k–600k** | **$2M–4M+** |

---

## 16. Opinionation Rationale

Every tool above was selected because:

1. **It works for a clear tier range.** No tool is recommended for all sizes. Vanta is wrong for enterprises. ServiceNow GRC is wrong for SMBs.

2. **It integrates with the rest of the stack.** SentinelOne feeds Sentinel, which feeds ServiceNow GRC, which uses Entra ID for identity. Toolchain integration > best-in-class individual tools.

3. **The practice can deliver it.** If I recommend a tool that takes a 6-person team to implement, the practice cannot sell that engagement. Every recommendation above can be deployed by 1-3 consultants within the engagement tier timeframe.

4. **It avoids vendor lock-in risk.** Where possible, tools support open standards (Sigma for detections, STIX/TAXII for intel, OWASP CRS for WAF).
