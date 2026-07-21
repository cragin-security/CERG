# Architecture Decision Records — cragin-security Fork

## Documenting the Rationale Behind Opinionated Framework Choices

| | |
|---|---|
| **Document ID** | CERG-GOV-ADR-001 |
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Annual |
| **Frameworks** | CERG Fork Architecture |
| **Regulations** | Not regulation-specific |
| **Environments** | Consulting practice delivery environments |

---

## Purpose

This document records the architectural decisions made in the cragin-security fork of CERG. Each ADR captures the context, alternatives considered, the decision, and the consequences.

ADRs exist to prevent two failure modes:

1. **Amnesia** — Six months from now, nobody remembers why ServiceNow was chosen over Archer, or why CB-002 has 87 controls instead of 97
2. **Drift** — Without documented rationale, future changes can accidentally reverse a deliberate trade-off

The ADR format follows the well-known [ADR template](https://adr.github.io/) (context → decision → consequences).

---

## ADR-001: OPN Domain Boundary

**Status:** Accepted (2026-07-03)

### Context

The cragin-security fork produces two types of content:
1. Improvements to the upstream CERG framework (bug fixes, doc improvements, framework enhancements)
2. Opinionated consulting delivery materials (tool recommendations, pricing, SOW templates, control implementation instructions)

These two types have different audiences, different quality criteria, and different maintenance cadences. Mixing them in the same documents creates confusion about what is "the framework" vs "the consulting wrapper."

### Decision

A separate `OPN` domain code was created for practice assets. The OPN prefix (short for "Opinionated") marks documents that are fork-specific consulting materials:

- `CERG-OPN-TOOLS-001` — Opinionated Tool Matrix
- `CERG-OPN-TOOLS-002` — GRC Rollout Guide
- `CERG-OPN-TOOLS-003` — Evidence Automation Mapping
- `CERG-OPN-MSP-001` — MSP/MSSP Runbook
- `CERG-OPN-DLV-001` — Engagement Playbook

OPN documents:
- Live in `practice-assets/` directory, not in governance/standards/procedures
- Use the `OPN` prefix in their document ID
- Are registered in CAT-001 §5.10 (Practice Assets) as a separate section
- Carry **Draft** status until the practice stabilizes
- Will never be pushed to the upstream m0dernz/CERG repository

Non-OPN changes (bug fixes, doc improvements, framework enhancements to upstream documents) follow the standard fork-to-upstream contribution workflow.

### Consequences

**Positive:**
- Clear boundary between "the framework" and "the consulting wrapper"
- Upstream-friendly: OPN content never pollutes the upstream PR pipeline
- MSPs and consultants can adopt practice assets independently of framework governance

**Negative:**
- Additional prefix to maintain in CAT-001 and the validator
- Risk of duplication if an upstream document and an OPN document cover adjacent topics
- The validator's `DOC_ID_PATTERN` must be patched locally (this stays fork-only)

---

## ADR-002: Tool Stack Opinionation

**Status:** Accepted (2026-07-03)

### Context

CERG adopters need tool guidance. Upstream CB-001 describes controls at a framework level without prescribing specific products. For MSPs and IT generalists, this is insufficient — they need to know which tool to buy, deploy, and configure.

The fork needed a decision framework for tool recommendations that balances:
- **Integration surface** — does it talk to ServiceNow GRC and the rest of the stack without custom middleware?
- **MSP multi-tenancy** — can a single instance manage multiple client orgs cleanly?
- **IT generalist usability** — can someone without a dedicated security engineer configure it using vendor documentation alone?

### Decision

Each tool category evaluates against the three criteria above and assigns a tier:

| Tier | Meaning |
|------|---------|
| **Primary** | Best on all three criteria. Default recommendation. |
| **Acceptable** | Decent but weaker on at least one criterion. Viable alternative. |
| **Avoid** | Fails on at least one criterion critically. Recommending against. |

Key primary picks and the rationale for rejecting alternatives:

| Category | Primary Pick | Key Alternatives at the Table | Why Primary Won |
|----------|-------------|------------------------------|-----------------|
| GRC Platform | ServiceNow GRC | Archer (legacy), Vanta (SMB-only) | Only platform straddling IT ops AND GRC without a messy handoff. Domain separation for multi-tenancy. |
| SIEM | Wazuh (SMB) / Elastic (Enterprise) | Splunk (cost at scale), Sentinel (Azure lock-in), QRadar (EOL) | Wazuh: free, lightweight, good compliance mapping. Elastic: open detection engine, Sigma support, true multi-tenant. |
| EDR | SentinelOne | CrowdStrike (pricier, overkill for SMB), Defender (weak cross-platform) | Best MSP console, RBAC per client site, solid ServiceNow integration. |
| CSPM | Wiz | Prisma Cloud (needs dedicated engineers), Lacework (agent-based, slower) | Agentless, multi-cloud, graph-based visualization, best multi-tenant. |
| Identity | Okta | Entra ID (M365 lock-in), JumpCloud (weaker enterprise), OneLogin (maintenance mode) | Best integration marketplace, true multi-tenant, independent of cloud provider. |
| Backup | Veeam | Rubrik (pricier), Cohesity (weaker MSP), Commvault (legacy licensing) | Industry standard for on-prem/virtualized backup. Service Provider Console for MSP multi-tenancy. |
| Network Security | Fortinet | Palo Alto (pricier, weaker MSP), Meraki (weaker advanced security), SonicWall (aging) | Best MSP program, broadest feature set per dollar. |
| AppSec | Trivy + Semgrep | Snyk (per-developer pricing), Veracode (slow, requires upload) | Both free, CLI-first, CI/CD-native. No license cost for MSP. |

### Consequences

**Positive:**
- MSPs get a clear "buy this, not that" guide
- Every tool in the stack has a documented API path to ServiceNow GRC
- Integration map shows how the tools fit together

**Negative:**
- Tool recommendations need quarterly review (vendors get acquired, security incidents, EOL)
- "Avoid" recommendations create friction with clients who already own those tools
- Less established vendors may innovate faster than the recommendations track

---

## ADR-003: CB-002 Practitioner Control Baseline

**Status:** Accepted (2026-07-03) — Updated 2026-07-20

### Context

Upstream CB-001 defines ~18 schematic control entries with framework-level parameters. This is appropriate for program architects and auditors but insufficient for MSPs implementing controls.

The fork needs a control baseline that:
- Maps to NIST 800-53r5 families for auditor cross-reference
- Provides copy-paste implementation instructions for IT generalists
- Ties each control to specific tools and evidence artifacts
- Is complete enough to scope an engagement but focused enough to be actionable

### Decision

Create CB-002 as an extended practitioner baseline with the 9-field control format:

| Field | Purpose |
|-------|---------|
| Control ID | NIST-aligned or CERG-native identifier |
| Action Statement | Plain-language requirement, no "shall/should" |
| System Applicability | Hardware, Software, Network, Cloud, Data, Process |
| Owning Pillar | Engineering, Risk, or Governance |
| Named Evidence | Specific artifact that proves the control is operating |
| Minimum Frequency | How often evidence must be collected |
| Subordinate Standard | Link to the relevant CERG standard |
| MSP Implementation Note | Copy-paste instructions for IT generalists |
| Tool Binding | Which tool(s) from the tool matrix satisfy this control |

**Control count:** After initial 97-control release, culled 10 overlapping shorthand controls and expanded 15 to full format. Final: **87 controls** across all 19 NIST families.

**Culling criteria:** A control is culled if it:
1. Exactly duplicates another control's requirement (e.g., SI-002 "Vulnerability Monitoring" = RA-002 "Vulnerability Scanning")
2. Describes an administrative or organizational arrangement that an MSP cannot implement (e.g., PM-002 "Senior Security Officer")
3. Covers a niche NIST scenario irrelevant to the target audience (e.g., SC-005 "VoIP Protection")

### Consequences

**Positive:**
- 87 controls, each earning its place. No filler for a round number.
- Every control has an MSP implementation note with copy-paste commands or API references
- Full cross-walk to NIST 800-53r5, CMMC L2, SOX ITGC, PCI DSS v4

**Negative:**
- 87 controls means the document is large (~90KB, ~1250 lines). Needs a good TOC and search.
- Some pure-manual controls (physical security, personnel screening) feel thin in an MSP context but must remain for framework completeness
- Quarterly review required to keep MSP implementation notes current with tool UI/API changes

---

## ADR-004: Evidence Automation as Separate Practice Asset

**Status:** Accepted (2026-07-20)

### Context

CB-002 defines "Named Evidence" and "Tool Binding" per control, but doesn't detail *how* evidence is collected, *which API endpoint* to call, or *how often* it feeds into the GRC platform. This information is too detailed for the control baseline itself (it would double the document size) but is essential for automated compliance evidence.

### Decision

Create a separate evidence automation mapping (CERG-OPN-TOOLS-003) that covers all 87 controls with:

- Per-tool automation tables: which tool, which controls it auto-evidenced, specific API endpoints, GRC integration path, collection frequency
- Manual evidence table: 31 controls that require human collection, with procedures and schedules
- Quick-reference by priority: deployment order for new client onboarding
- Maturity model: Basic → Intermediate → Advanced → Adaptive

The mapping lives in `practice-assets/tools/` alongside the GRC Rollout Guide and Tool Matrix, not in the governance directory. This is deliberate — evidence automation is a practice delivery tool, not a framework requirement.

### Consequences

**Positive:**
- CB-002 stays focused on the control requirement; the evidence automation document handles the implementation detail
- Separating evidence automation from the control baseline allows different update cadences (tools change more often than controls)
- MSPs have a clear "configure this → collect that → feed into GRC" pipeline

**Negative:**
- Three separate documents now describe the same controls (CB-002, tool matrix, evidence mapping). The user must understand how they relate.
- When CB-002 controls change, the evidence mapping must be updated in lockstep
- API endpoints documented as of July 2026 will drift as vendor APIs evolve

---

## ADR-005: MSP/MSSP Delivery Model Over Enterprise Consulting

**Status:** Accepted (2026-07-03)

### Context

The fork's practice materials could target two different markets:
1. **Enterprise consulting** — Large clients, dedicated security teams, custom engagements, high rates, low volume
2. **MSP/MSSP delivery** — SMB clients, IT generalist implementers, standardized engagements, moderate rates, high volume

The target audience shapes every decision: control depth, tool complexity, pricing model, evidence automation.

### Decision

The fork targets **MSP/MSSP delivery** with the following design choices:

| Dimension | Enterprise Choice | MSP Choice (Selected) |
|-----------|------------------|----------------------|
| Control instructions | Reference to standard | Copy-paste commands |
| Tool selection | Best of breed, any budget | Stack with documented API path to GRC |
| Pricing | Hourly or T&M | Fixed-fee + MRR |
| Evidence | Manual collection by client | Automated via API pipelines |
| Multi-tenancy | Client has own stack | One MSP stack, domain-separated |
| Onboarding | Custom per engagement | Standardized 12-week sprint |
| SOW | Legal review per engagement | Template with client fill-ins |

This choice is reflected in:
- The **MSP Runbook** structure (Phase 1-5 delivery playbook)
- The **Tool Matrix** criteria (multi-tenancy is the #2 criterion)
- The **Pricing Reference Card** (fixed-fee assessment, MRR-based operating)
- The **Engagement Playbook** anti-patterns (all MSP-specific: "The Perpetual Pilot," "The Audit Rescue")

### Consequences

**Positive:**
- Clear target market means every practice asset speaks to the same audience
- MSPs can adopt the entire stack as a turnkey service delivery model
- MRR pricing aligns with how MSPs sell (monthly, not project-based)

**Negative:**
- Excludes the enterprise consulting market (large banks, healthcare systems, government agencies)
- Some controls (physical security, background screening, SoD matrices) feel like compliance checklist items for MSPs, but they must stay for framework completeness
- Risk of "one-size-fits-all" when clients have legitimately different needs (a 5-person startup vs a 200-person mid-market)

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-20 | cragin-security | Initial release: ADR-001 through ADR-005 covering OPN boundary, tool stack, CB-002 structure, evidence automation, and MSP delivery model. |

### Review Triggers

- New architectural decisions that fork from upstream direction
- Tool stack changes (vendor acquisition, EOL, new primary recommendations)
- Evidence automation methodology changes
- Practice maturity level changes (e.g., adding enterprise consulting track)

### Related Documents

- [Opinionated Tool Matrix](../practice-assets/tools/opinionated-tool-matrix-v1.md)
- [100-Core Control Baseline](CERG-GOV-CB-002_100-Core_Control_Baseline.md)
- [Evidence Automation Mapping](../practice-assets/tools/evidence-automation-mapping-v1.md)
- [Engagement Playbook](../practice-assets/engagement-playbook-v1.md)
- [MSP Runbook](../practice-assets/msp-runbook-v1.md)
- [GRC Rollout Guide](../practice-assets/tools/grc-rollout-v1.md)
- [Upstream CERG issuesv1 analysis](https://raw.githubusercontent.com/m0dernz/CERG/refs/heads/feat/issues-fix-pack-v2/issuesv1.md)
