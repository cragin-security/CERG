# CERG Engagement Playbook

## How to Scope, Price, and Deliver CERG Consulting Engagements

| | |
|---|---|
| **Document ID** | CERG-OPN-DLV-001 |
| **Version** | 1.1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Quarterly |
| **Frameworks** | CERG 100-Core · NIST 800-53r5 |
| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 |
| **Environments** | All practice delivery environments |

---

## Purpose

This playbook defines how a consulting practice delivers the CERG cybersecurity operating model to clients. It covers the full engagement lifecycle — from initial conversation to final handoff — with pricing guidance, deliverable templates, and anti-patterns.

It assumes you're working from the [Opinionated Tool Matrix](tools/opinionated-tool-matrix-v1.md), the [100-Core Control Baseline](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md), and the [GRC Rollout Guide](tools/grc-rollout-v1.md), and have read the [MSP Runbook](msp-runbook-v1.md). If you're an MSP/MSSP delivering CERG as a managed service, the runbook is your day-to-day. This playbook is your business wrapper.

---

## The CERG Engagement Lifecycle

```
Discover → Assess → Plan → Deploy → Operate → Handoff
```

### Phase 1: Discover (Free, 60 minutes)

**Goal:** Determine if the client is a fit for CERG and which tier they belong in.

**What happens:** A 60-minute call with the client's IT lead and business owner. You walk through the CERG Intake Questionnaire (30 questions). The output is a one-page summary:

- Client profile (industry, size, regulatory obligations)
- Current state (what tools exist, what's missing)
- CERG tier recommendation (Foundations, Structure, Compliance, or Strategic)
- Rough order-of-magnitude pricing (not a quote — a range)

**Pricing:** This call is free. It's a qualification step, not a billable engagement.

**Anti-pattern:** Skipping this phase and writing a proposal based on what the client *says* they have. Always validate with the questionnaire. Clients consistently overestimate their maturity.

### Phase 2: Assess (Billable, 1-2 weeks)

**Goal:** Produce a data-driven gap analysis that replaces speculation with evidence.

**Deliverables:**
1. **Current State Inventory** — tool-by-tool inventory with version, config status, and coverage gaps
2. **Gap Analysis Report** — [CERG 100-Core controls](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) mapped to current state, each scored as Implemented / Partially Implemented / Not Implemented
3. **Risk Register Bootstrap** — top 10 risks by impact, each with a recommended treatment
4. **Tool Stack Recommendation** — specific products and licenses, priced, per the [Tool Matrix](tools/opinionated-tool-matrix-v1.md)

**Pricing guidance:**
- SMB (< 50 employees): $5,000-8,000 (1 week)
- Mid-market (50-500): $12,000-20,000 (2 weeks)
- Enterprise (500+): $25,000-50,000 (3-4 weeks)

**Approach:** On-site is ideal but not required. Remote assessment with screen-sharing and read-only tool access works for most clients.

**Anti-pattern:** Producing a gap analysis that just lists missing controls. The client needs a *prioritized* roadmap — what to fix first, what can wait, what costs nothing but time.

### Phase 3: Plan (Billable, 1 week after assessment)

**Goal:** Convert the gap analysis into a phased implementation plan the client can fund and execute.

**Deliverables:**
1. **Remediation Roadmap** — phased plan: Quick Wins (0-30 days), Foundation (30-90 days), Maturation (90-180 days), Sustainment (ongoing)
2. **Staffing Plan** — what the client's IT team does vs what the MSP/MSSP does vs what requires a specialist
3. **Budget** — tool licenses, consulting fees, internal labor estimate

**Pricing guidance:** Included in the assessment fee. This is where you demonstrate value and earn the implementation engagement.

### Phase 4: Deploy (Billable, 30-90 days)

**Goal:** Get the tool stack stood up, controls implemented, and evidence collection running.

**Scope:** Defined by the remediation roadmap. Typical SMB deployment (Foundations tier):

| Week | Activity | Output |
|------|----------|--------|
| 1-2 | [SentinelOne deploy](msp-runbook-v1.md#21-sentinelone-deployment) + [Wazuh deploy](msp-runbook-v1.md#22-wazuh-deployment-smb-stack) | All endpoints reporting |
| 3 | MFA enforcement + access review baseline | MFA on all accounts |
| 4 | [Tenable deploy](msp-runbook-v1.md#23-tenable-nessus-deployment) + first scan | Baseline vuln report |
| 5 | [Wiz CSPM onboarding](msp-runbook-v1.md#24-wiz-cspm-onboarding) + first scan | Cloud config baseline |
| 6-7 | [Veeam deploy](msp-runbook-v1.md#25-veeam-backup-configuration) + backup configuration | Immutable backups running |
| 8 | [GRC platform setup](tools/grc-rollout-v1.md) (Vanta or ServiceNow) | Controls tracked, evidence pipeline started |
| 9-10 | Sigma rules deploy + detection testing | Detection running, alerts flowing |
| 11-12 | Evidence collection cadence established | First evidence cycle complete |

**Pricing guidance:**
- Foundations (30-day sprint): $15,000-25,000
- Structure (+compliance prep): $30,000-50,000
- Compliance (full CMMC/SOX readiness): $50,000-100,000

### Phase 5: Operate (Recurring, ongoing)

**Goal:** Keep the program running, evidence current, and the client audit-ready.

Two delivery models:

**Model A: Full MSP/MSSP** — You own the tool stack, the monitoring, and the evidence collection. Monthly recurring revenue (MRR).

| Client Size | Monthly Fee | Includes |
|-------------|-------------|----------|
| SMB (<50) | $2,000-4,000/mo | Tool management, evidence collection, monthly reporting, quarterly review |
| Mid-market | $5,000-10,000/mo | Above + detection monitoring, incident response retainers, compliance support |
| Enterprise | $15,000-30,000/mo | Above + dedicated security engineer, board reporting, CISO advisory |

**Model B: Advisory** — Client owns the tools. You provide oversight, quarterly reviews, and audit support. Hourly or retainer.

- Advisory retainer: $3,000-8,000/mo for 10-20 hours/month
- Audit support: $200-300/hr during audit periods

### Phase 6: Handoff (Optional)

**Goal:** Transition the program to in-house staff or a different provider with zero operational disruption. A clean handoff is the difference between a referral and a cautionary tale.

**When to trigger handoff:** The client hires internal security staff, switches MSPs, brings the program in-house after the deployment phase, or the contract term ends without renewal.

**Deliverables:**

1. **Handover Memo** — A 5-10 page document covering:
   - Program status summary (controls implemented, evidence collected, open findings)
   - Tool inventory with license expiry dates, admin accounts, and renewal contacts
   - Current evidence package (last evidence cycle export from GRC platform)
   - Open POA&M items with remediation owners and target dates
   - Risk register export (open risk acceptances, exceptions, pending reviews)
   - Recurring calendar (evidence collection cadence, review schedules, compliance deadlines)
   - Known gaps and compensating controls not yet remediated

2. **Runbook Package** — A zip or Git repo containing:
   - All deployment scripts (PowerShell, Bash, Terraform) with comments
   - Configuration exports from every tool (firewall rules, SIEM configs, EDR policies, backup jobs)
   - Dashboard definitions and saved SIEM queries for the client's environment
   - Custom detection rules (Sigma files) and any environment-specific modifications
   - GRC platform control mappings and evidence templates
   - Architecture diagrams (network topology, data flows, trust boundaries)

3. **Vendor Transfer Checklist** — Technical transfer steps:
   - Tool license transfers from MSP account to client or new provider
   - Admin account handoff with credential rotation (all shared credentials changed)
   - API key and webhook rotation (old keys revoked, new keys tested)
   - DNS/CNAME/redirect changes if MSP-hosted services are moving
   - Email security SPF/DKIM/DMARC record updates if MSP's email gateway is being removed
   - SIEM log source reconfiguration (forwarding destination changes)
   - RMM agent uninstallation or transfer to new provider

4. **Knowledge Transfer Sessions** — Paid transition support:
   - 2-4 hours of recorded walkthrough sessions covering tool operations, incident response procedures, evidence collection workflows, and monthly review cadence
   - One week of standby support post-handoff for questions and issues

5. **Transition Acceptance Form** — Signed by the client confirming:
   - All deliverables received and reviewed
   - Tool access verified (new admins can log in, old MSP access revoked)
   - Evidence package accepted as current
   - Handoff completion date and final invoice acknowledgment

**Pricing:**

| Component | SMB (<50) | Mid-Market (50-500) | Enterprise (500+) |
|-----------|-----------|---------------------|-------------------|
| Handover Memo + Runbook Package | $3,000 | $5,000 | $8,000 |
| Vendor Transfer (per tool) | $500 | $1,000 | $2,000 |
| Knowledge Transfer (2-4 hrs) | $2,000 | $4,000 | $6,000 |
| Standby Support (1 week) | $2,000 | $3,000 | $5,000 |
| **Typical Total** | **$5,000-7,000** | **$8,000-12,000** | **$12,000-15,000** |

**Duration:** 1-3 weeks depending on tool count and complexity. Typically 2 weeks for a standard 5-tool stack.

**Checklist:** Before declaring handoff complete, verify all of the following:

| # | Item | Owner |
|---|------|-------|
| 1 | Handover Memo delivered and acknowledged | Consulting Lead |
| 2 | Runbook Package delivered (verify client can open/run it) | Consulting Lead |
| 3 | All tool licenses transferred to client/provider | Consulting Lead |
| 4 | MSP admin accounts removed from all client tools | Engineering |
| 5 | API keys rotated and new keys tested | Engineering |
| 6 | SIEM log sources re-pointed to new destination | Engineering |
| 7 | DNS changes propagated (if applicable) | Engineering |
| 8 | Knowledge transfer sessions completed | Consulting Lead |
| 9 | Client confirms they can perform evidence collection independently | Consulting Lead |
| 10 | Risk register and POA&M handed off with current status | Consulting Lead |
| 11 | Contract close-out processed (final invoice, NDA expiry, data retention) | Operations |
| 12 | Client sign-off on Transition Acceptance Form | Operations |

**Anti-pattern:** Delaying handoff because the client isn't "ready." If the contract is ending, deliver the package, get sign-off, and exit cleanly. Holding their data hostage damages your reputation and creates legal exposure. A clean handoff earns referrals. A messy one earns bad reviews.

**Pricing:** Never hold the client hostage — a clean handoff earns referrals. Price it to cover actual effort (the table above), not to discourage transition.

---

## Pricing Reference Card

| Engagement | SMB (<50) | Mid-Market (50-500) | Enterprise (500+) |
|------------|-----------|---------------------|-------------------|
| Assessment | $5-8k | $12-20k | $25-50k |
| Deployment (Foundations) | $15-25k | $30-50k | $50-100k |
| Monthly MRR (full MSP) | $2-4k | $5-10k | $15-30k |
| Monthly Advisory | $3-5k | $5-8k | $8-15k |
| Audit Support (per audit) | $5-10k | $15-25k | $30-50k |
| Handoff | $5-7k | $8-12k | $12-15k |

All prices assume US-based consulting. Adjust for geography, competition, and client complexity.

---

## Anti-Patterns to Avoid

### Anti-Pattern: The Audit Rescue

Client calls three weeks before their CMMC assessment. They need [110 controls](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) evidenced and they have nothing. Tempting revenue — but this engagement always fails. You cannot retroactively create 12 months of evidence.

**Instead:** Offer expedited assessment + a tactical plan for what can be done in 3 weeks (usually: deploy MFA, tighten access, document what exists). Be clear this is triage, not compliance. The full program starts after the audit.

### Anti-Pattern: The Tool-Only Client

Client says "just deploy SentinelOne and Tenable, we'll handle the rest." Six months later they're breached and blaming you because the SIEM wasn't tuned and nobody was triaging alerts.

**Instead:** CERG is an operating model, not a tool bundle. If the client only wants tools, sell them a tool deployment engagement with clear scope: "We deploy and configure. You operate." Make the boundary explicit in the SOW.

### Anti-Pattern: The Free Assessment That Never Ends

You do the Discover call. Then "just a few more questions." Then "can you look at this one server?" Then suddenly you're 20 hours into free work.

**Instead:** The Discover call is 60 minutes. Set a timer. After 60 minutes: "This is a good candidate for a formal assessment. I'll send you a proposal." If you give away the assessment, you've devalued the entire practice.

### Anti-Pattern: The Perpetual Pilot

Month 6 and the client is still "evaluating" whether CERG is right for them. They have half the tools deployed and no evidence collected.

**Instead:** Every engagement has a defined end state. For the Discover-to-Deploy path, that end state is "tools running, controls implemented, first evidence cycle complete." If you haven't reached that in 90 days, the engagement is stalled. Escalate or exit.

---

## SOW Essentials

Every Statement of Work for a CERG engagement must include:

1. **Scope** — exact systems, locations, and controls in scope. Use the [CERG Implementation Tiers](../governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md#5-the-306090-day-rollout) (Foundations, Structure, Compliance, Strategic) and the [100-Core Control Baseline](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) for control scoping
2. **Deliverables** — named artifacts (Gap Analysis Report, Remediation Roadmap, Tool Deployment, Evidence Pipeline)
3. **Client Responsibilities** — tool license costs, staff availability for interviews, admin access to systems, approval turnaround on exceptions
4. **Exclusions** — what you are NOT doing (physical security, OT systems, code review, penetration testing unless scoped separately)
5. **Assumptions** — client has working network, domain/admin access, budget for tool licenses
6. **Payment Terms** — 50% upfront, 25% at midpoint, 25% on completion; MRR billed monthly in advance

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-20 | cragin-security | Expanded Phase 6 Handoff: 5 deliverables, pricing table, 12-item exit checklist, knowledge transfer, vendor transfer steps, transition acceptance form. |
| 1.0.0 | 2026-07-03 | cragin-security | Initial release: 6-phase engagement lifecycle, pricing, anti-patterns, SOW essentials |

### Related Documents

- [100-Core Control Baseline](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — the control set this playbook scopes, prices, and delivers
- [Opinionated Tool Matrix](tools/opinionated-tool-matrix-v1.md) — tool selection criteria, primary/acceptable/avoid tiers
- [MSP Runbook](msp-runbook-v1.md) — copy-paste deployment instructions for every tool in the stack
- [GRC Rollout Guide](tools/grc-rollout-v1.md) — wiring ServiceNow GRC or Vanta to the CERG control framework
- [Implementation Guide](../governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) — adoption paths, MVC sequence, role-based checklists
