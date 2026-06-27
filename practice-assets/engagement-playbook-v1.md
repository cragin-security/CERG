# CERG Client Engagement Playbook v1

**Purpose:** A single consultant-facing guide that walks through a CERG engagement from intake call to signed handover. Every section references existing practice assets — nothing new to create.

**Target audience:** CERG practice consultants (1-3 person delivery teams)

---

## 1. Engagement Lifecycle Overview

```text
INT/AKE ──> DISCOVERY ──> TIER SELECTION ──> DELIVERY ──> HANDOVER ──> DEBRIEF
  1 day      2-5 days       1 day           2-16 weeks     1-2 days     1 day
```

**Total engagement duration by tier:**
| Tier | Duration | Team Size | Price Band (indicative) |
|------|----------|-----------|------------------------|
| Tier 1: Foundations | 2 weeks | 1 consultant | $10-20k |
| Tier 2: Structure | 4 weeks | 1-2 consultants | $30-50k |
| Tier 3: Compliance | 6-8 weeks | 2 consultants | $60-120k |
| Tier 4: Strategic Partner | 12-16 weeks | 2-3 consultants | $150-300k |

---

## 2. Phase 1: Intake (Day 1)

**Input:** Signed engagement letter (SOW template below)
**Output:** Completed intake questionnaire + qualified scope
**Consultant action:** 1-hour kickoff call + 2 hours prep

### Pre-Call Prep
1. Review [`practice-assets/intake/cerg-intake-questionnaire-v1.md`](../intake/cerg-intake-questionnaire-v1.md)
2. Preview the client's sector profile if known (see `sector-profiles/`)
3. Check if the client has any existing documentation (policies, risk register, org chart)

### Kickoff Call Agenda
1. **Security context** — What keeps the CISO up at night? Recent incidents? (15 min)
2. **Regulatory pressure** — What audits are coming? What keeps the compliance team up? (10 min)
3. **Budget window** — What's the budget range? (5 min)
4. **Stakeholder map** — Who needs to approve? Who needs to be involved? (5 min)
5. **Sector overlay** — Select the relevant sector profile (10 min)

### Sector Profile Selection
Use the sector overlay to tailor the engagement from day one:

| If client is in... | Load this sector profile | Key overlay |
|-------------------|------------------------|-------------|
| Government / Defense | `sector-government-v1.md` | CMMC, FedRAMP |
| Healthcare | `sector-healthcare-v1.md` | HIPAA, HITRUST |
| Financial | `sector-financial-v1.md` | SOX ITGC, PCI |
| Energy / Utilities | `sector-energy-utilities-v1.md` | NERC CIP |
| Manufacturing / OT | `sector-manufacturing-ot-v1.md` | ISA 62443 |
| SaaS / Technology | `sector-saas-v1.md` | SOC 2, ISO 27001 |
| Defense Industrial Base | `sector-dib-v1.md` | CMMC L2+ |
| Cross-holding / Holdings | `sector-cross-holding-v1.md` | Multiple frameworks |

### Regulatory Overlays
If the engagement has an overlay requirement, add these documents:
- Cloud migration: `overlay-cloud-migration-v1.md`
- FedRAMP assessment: `overlay-fedramp-assessment-v1.md`
- HIPAA/HITRUST: `overlay-hipaa-hitrust-assessment-v1.md`
- ISO refinement: `overlay-iso-refinement-v1.md`

---

## 3. Phase 2: Discovery (Days 2-5)

**Input:** Completed intake questionnaire
**Output:** Tier scope document + engagement plan
**Consultant action:** 3-5 days of discovery (remote or on-site)

### Discovery Checklist

| Activity | Tool/Asset | Hours | Output |
|----------|-----------|-------|--------|
| Org structure mapping | Org chart + interview | 2-3 | Stakeholder map |
| Regulatory scope | Regulatory packages (`plans/` folder) | 2-4 | Regulatory register |
| Tool stack audit | CB-001 tool mappings | 3-4 | Current tool inventory |
| Control maturity sample | CB-001 (sample 10 controls) | 4-6 | Baseline maturity assessment |
| Risk register review | TMPL-RM-001 | 2-3 | Risk register gap |
| Architecture review | Network diagram, cloud accounts | 2-4 | Architecture notes |
| Document inventory | CAT-001 catalog | 2-3 | Document gap analysis |

### Org Profile Validation
Use [`practice-assets/checklists/org-profile-checklist-v1.md`](../checklists/org-profile-checklist-v1.md) to validate the organizational profile. This determines which CERG adoption path fits.

### Determine the Right CERG Adoption Path
Use IMP-005 (Adoption Decision Tree) for the formal assessment. Quick reference:

- **CERG Lite** (<15 FTEs, no regulatory pressure): Tier 1
- **CERG Standard** (15-100 FTEs, basic compliance): Tier 2
- **CERG Regulated** (any size, active regulatory scope): Tier 3
- **CERG Strategic** (100+ FTEs, multi-regulator, building program): Tier 4

---

## 4. Phase 3: Tier & Scope Selection (Day 5-6)

**Input:** Discovery findings
**Output:** Signed scope document
**Consultant action:** 1-day scoping session + proposal submission

### Scope Templates
Use the tier-specific scope templates from [`practice-assets/scope-templates/`](../scope-templates/):

| Template | Best for | Contains |
|----------|---------|----------|
| `tier1-foundations-scope.md` | New security function, 1-15 FTEs | MVC spine (8 docs), risk register bootstrap, 40 Core controls |
| `tier2-structure-scope.md` | Existing function, 5-30 FTEs | MVC + standards gap analysis + architecture review |
| `tier3-compliance-scope.md` | Regulated environment | Tier 2 + regulatory packages + evidence automation |
| `tier4-strategic-scope.md` | Enterprise, multi-regulator | Tier 3 + co-designed roadmap + GRC tool integration |

### Guardrails and Gates
- Tier 1-2 transition gate: MVC spine adopted + first risk register completed + one tabletop executed
- Tier 2-3 transition gate: Standards gap closed + evidence automation running + access reviews quarterly
- Tier 3-4 transition gate: GRC tool loaded + continuous monitoring active + annual test program running

Reference: [`tier1-guardrails-v1.md`](../scope-templates/tier1-guardrails-v1.md), [`tier2-to-3-gates-v1.md`](../scope-templates/tier2-to-3-gates-v1.md)

### Deliverable Confirmation
For each engagement, the consultant and client confirm:
1. **Core deliverables** — fixed per tier (use the scope template)
2. **Regulatory packages** — add from `plans/` folder as needed
3. **Sector overlays** — add from `sector-profiles/` as needed
4. **Tool integrations** — GRC tool, SIEM, EDR alignment per tool matrix
5. **Evidence automation** — which controls get automated evidence collection

---

## 5. Phase 4: Delivery (2-16 weeks)

**Input:** Signed scope
**Output:** All agreed deliverables
**Consultant action:** Per the delivery plan

### Week 1-2: MVC Spine
Deliver the 8-document MVC spine from CERG:
1. POL-001 Cybersecurity Policy
2. OM-001 Operating Model
3. FRM-001 Framework
4. CAT-001 Document Catalog
5. RMF-001 Risk Management Framework
6. PRC-RM-001 Risk Register Procedure
7. TMPL-RM-001 Risk Register Templates
8. PRC-VM-001 Exposure Management Procedure

**Templates to use:** [`TMPL-SCP-001`](../../templates/CERG-TMPL-SCP-001_System_Control_Profile_Template.md) for system profiles, [`TMPL-AUD-001`](../../templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md) for evidence collection

### Week 3-4: Control Baseline
Use CB-001 for the control baseline. Per control, the consultant:
1. Reviews the **Statement** with the client
2. Provides **IT Generalist** commands/steps for the system owner
3. Maps **MSP guidance** if a managed services provider is involved
4. Applies **Tool Mappings** based on the client's actual tool stack
5. Runs **Verification** steps to confirm the control is operating
6. Documents **findings** for the improvement register

### Week 5-8: Standards and Procedures (Tier 2+)
Import 15 standards from the `standards/` directory. For each standard:
1. Review with the relevant technical team
2. Confirm current state vs. standard requirement
3. Document gaps as POA&M entries
4. Implement compensating controls for gaps

### Week 8-12: Regulatory Packages (Tier 3+)
For each regulatory package in `plans/`:
1. Identify applicable controls from CB-001
2. Tailor implementation guidance to the regulation
3. Create evidence collection procedures
4. Prepare for assessment or audit

### Week 12-16: Strategic Integration (Tier 4+)
1. **GRC tool deployment**: Use the ServiceNow GRC Accelerator (see `tools/`)
2. **Tool stack optimization**: Align to the opinionated tool matrix
3. **Detection framework**: Implement from `detection/detection-engineering-framework-v1.md`
4. **Vendor risk program**: Deploy TPRM-001 questionnaire and process
5. **M&A integration**: If applicable, use `ma-security-framework-v1.md`

---

## 6. Phase 5: Handover (Days 1-2 before close)

**Input:** Completed deliverables
**Output:** Signed handover memo + improvement register + client archive
**Consultant action:** 1-2 handover days

### Handover Package
1. [`handover-memo-v1.md`](../templates/handover-memo-v1.md) — signed by client and consultant
2. [`client-improvement-register-v1.md`](../templates/client-improvement-register-v1.md) — all open findings
3. [`risk-register-bootstrap-v1.md`](../templates/risk-register-bootstrap-v1.md) — current risk state
4. All CERG documents in client format (markdown or GRC tool)
5. Evidence repository (organized by control ID)

### Knowledge Transfer
- 2-hour walkthrough of the completed deliverables
- Identification of internal owner for each pillar (Engineering, Risk, Governance)
- Training on CERG document maintenance process
- Access to the practice update channel

### Ongoing Support Options
- **Monthly check-in**: 1-hour review of POA&M progress (Tier 1-2)
- **Quarterly health check**: 4-hour review + metrics dashboard update (Tier 2-3)
- **Retainer**: 4 hours/week for ongoing support, evidence collection, audit prep (Tier 3-4)

---

## 7. Phase 6: Debrief (After engagement close)

**Input:** Engagement experience + client feedback
**Output:** Debrief record + practice improvement items
**Consultant action:** 1-hour debrief per consultant

### Debrief Protocol
Use [`debrief-protocol-v1.md`](../trackers/debrief-protocol-v1.md) — the full debrief process.

### Key Debrief Questions
1. Was the scope accurate? Over-scoped? Under-scoped?
2. What sector-specific or tool-specific knowledge was missing?
3. What deliverables took longer than estimated?
4. What client resistance was encountered? (Staffing, budget, org politics)
5. What evidence collection was hardest? (Opportunity for automation)
6. What would you do differently next time?

### Practice Improvement
- Update the scope template for the tier delivered
- Add any new patterns to the anti-pattern catalog
- Save client-specific adaptations to the adaptation profile for re-engagement

---

## 8. Templates and Forms Reference

| When to use | Template | Location |
|------------|----------|----------|
| Engagement start | Engagement letter / SOW | `templates/engagement-letter-sow-v1.md` |
| Throughout | Risk register | `templates/risk-register-bootstrap-v1.md` |
| Throughout | System control profiles | `templates/CERG-TMPL-SCP-001.md` |
| Throughout | Control evidence | `templates/CERG-TMPL-AUD-001.md` |
| Throughout | Security exception | `templates/CERG-TMPL-RM-002.md` |
| Throughout | Risk acceptance | `templates/CERG-TMPL-RM-003.md` |
| Monthly | POA&M tracking | `templates/CERG-TMPL-CUI-002.md` |
| Quarterly | Metrics reporting | `templates/CERG-TMPL-MTR-001.md` |
| Quarterly | Vendor assessment | `templates/CERG-TMPL-TPRM-001.md` |
| Engagement close | Handover memo | `templates/handover-memo-v1.md` |
| Engagement close | Improvement register | `templates/client-improvement-register-v1.md` |
| Post-engagement | Debrief | `trackers/debrief-protocol-v1.md` |
| Proposal | Case study | `templates/practice-case-study-v1.md` |

---

## 9. Tools Integration Guide

For the recommended tool stack, see the full opinionated tool matrix at [`tools/opinionated-tool-matrix-v1.md`](../tools/opinionated-tool-matrix-v1.md).

### Quick Tool Decisions During Discovery

| If client has... | Recommend |
|-----------------|-----------|
| Microsoft 365 | Entra ID P1/P2, Sentinel SIEM, Intune MDM, Defender (if E5) |
| Google Workspace | Okta, Google Cloud Identity, CrowdStrike |
| Hybrid on-prem + cloud | CyberArk PAM, Splunk SIEM, Veeam backup |
| Zero budget | Wazuh SIEM, OpenVAS vuln scanner, pfSense firewall, Snipe-IT asset mgmt |
| Heavy regulation | CyberArk PAM, ServiceNow GRC, Qualys vuln, KnowBe4 training |
| Cloud-first (multi-cloud) | Wiz CSPM, Cloudflare ZTNA, Trivy IaC scanning |

### GRC Tool Integration

| Tool | Setup Time | Integration with CERG | Reference |
|------|-----------|----------------------|-----------|
| Vanta | 2 weeks | API-based evidence collection | `tools/grc-rollout-v1.md` |
| OneTrust | 4-6 weeks | Framework import + policy mgmt | `tools/grc-rollout-v1.md` |
| ServiceNow GRC | 12-16 weeks | CSV import accelerator | `tools/servicenow-accelerator/` |
| Spreadsheet | 1 day | Not recommended beyond 20 controls | — |

---

## 10. Common Engagement Anti-Patterns

From the CERG Anti-Pattern Catalog (`CERG-GOV-ANTI-001`):

| Anti-Pattern | Symptom | Correction |
|-------------|---------|------------|
| Scope creep | Client adds "one more thing" every week | Reference signed scope. Any addition triggers a change order. |
| No executive sponsor | Security team is engaged but director/VPs are not | Pause delivery until executive sponsor is identified. |
| Evidence procrastination | "We'll collect evidence at the end" | Evidence collected during delivery, not after. Every control verified before the next is started. |
| Tooling as a substitute | Client buys SentinelOne and expects compliance | Tools enable controls. Controls are processes, not products. |
| Compliance checkboxes | "Just tell me what to check to pass the audit" | CERG is an operating model, not a checklist. If that's all they want, refer them to a compliance-only firm. |

---

## Document Control

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07 | CERG Practice | Initial playbook |

*End of playbook*
