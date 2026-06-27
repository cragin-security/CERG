# GRC Tool Rollout · CERG Framework Mapping

**Target tool:** ServiceNow GRC (enterprise) / OneTrust (mid-market) / Vanta (SMB)
**Source:** CERG corpus (99 controls, 15 standards, 12 procedures, risk framework, policy spine)
**Engagement duration:** 2 weeks (SMB) / 4-6 weeks (mid-market) / 12-16 weeks (enterprise)

---

## 1. GRC Tool Selection Guide

Use this decision tree with the client in the first discovery call.

```text
Client has ServiceNow already?
├─ YES → Use ServiceNow GRC (already paying for it)
├─ NO → Client size?
│   ├─ <200 employees → Vanta or Drata
│   ├─ 200-2000 → OneTrust or LogicGate
│   └─ 2000+ → ServiceNow GRC (budget for it)
```

**Vanta** is the default SMB pick: automated evidence collection, SOC 2 / ISO / HIPAA / PCI reports, API integrations with 200+ SaaS tools. Impressive demo for the price.

**OneTrust** is the mid-market sweet spot: dedicated GRC without the ServiceNow platform overhead. Policy management, risk register, vendor risk, and evidence collection in one product. Implementation in 4-6 weeks with 1-2 consultants.

**ServiceNow GRC** is enterprise-grade but requires dedicated platform administration. The CISO dashboard, integrated risk view, and audit management are best-in-class. The downside: you need a ServiceNow implementation partner or internal ServiceNow admin.

---

## 2. Phase 1: Framework Ingestion (Week 1-2)

### Step 1: Create the Control Framework

Every GRC tool needs a control framework mapped to regulations. CERG CB-001 is that framework.

**Output:** Control framework with 99 controls grouped into 18 families.

```
ServiceNow: Policy & Compliance Management → Controls → Create → Import CSV
OneTrust: Framework Manager → Create Framework → Import
Vanta: Policies → Add Framework → Custom
```

*Control CSV import format:*
```csv
Control ID,Family,Control Statement,Implementation Guidance,Regulatory Mapping,Test Procedure
AC-1,Access Control,Access control rules documented and approved,NIST 800-53 AC-1 · PCI 7.1,Verify policy exists with review date
AC-2,Access Control,Every account has approved request and named owner,NIST AC-2 · PCI 7.2.4,Compare IdP to HR roster monthly
[...all 99 controls...]
```

### Step 2: Create the Policy Library

CERG provides the document templates. Import governance spine first.

**Priority order for policy import:**
1. POL-001 Cybersecurity Policy (umbrella policy)
2. OM-001 Operating Model (governance structure)
3. FRM-001 Framework (control framework reference)
4. RMF-001 Risk Management Framework (risk methodology)
5. CB-001 Control Baseline (the control statements)
6. CAT-001 Document Catalog (document registry)
7. Records catalog (evidence retention schedule)

**ServiceNow: Policy & Compliance → Policies → Import from Word/Markdown**
**OneTrust: Policy Manager → Create Policy → Upload**
**Vanta: Policies → Add Policy → Markdown**

### Step 3: Map Regulations to Controls

CERG CB-001 controls already include NIST 800-53, ISO 27001, PCI DSS, CMMC references. Import these mappings.

*Mapping format:*
```csv
Control ID,Framework,Control Ref
AC-1,NIST 800-53,AC-1
AC-1,ISO 27001,A.9.1.1
AC-1,PCI DSS,7.1
AC-1,CMMC,AC.L2-3.1.1
AC-2,NIST 800-53,AC-2
[...etc...]
```

---

## 3. Phase 2: Risk Register Setup (Week 2-3)

### Step 1: Import Risk Taxonomy

CERG GOV-TAX-001 provides the risk taxonomy. Map to GRC tool risk categories.

**Standard risk categories:**
- Strategic (board-level decisions)
- Operational (people, process, technology failure)
- Financial (financial loss, fraud, insurance gaps)
- Compliance (regulatory violation, audit failure)
- Reputational (brand damage, customer trust)
- Third Party (vendor/supplier failure)

### Step 2: Configure Risk Scoring

```
Likelihood: 1 (Rare) to 5 (Almost Certain)
Impact: 1 (Negligible) to 5 (Catastrophic)
Score = Likelihood × Impact (range 1-25)

Thresholds:
  Low (1-5): Risk owner manages
  Medium (6-11): Risk owner + documented acceptance
  High (12-16): CISO approval required
  Critical (17-25): Board notification required
```

### Step 3: Seed the Risk Register

Initial risk register entries (pre-populate before engaging):
- Missing MFA on remote access (High)
- Incomplete asset inventory (Medium)
- No tabletop exercise in 12+ months (High)
- Vendor risk assessments overdue (Medium)
- Incomplete patch management SLA compliance (Medium-to-High depending on findings)

---

## 4. Phase 3: Evidence Collection Automation (Week 3-6)

### Automated Evidence Sources (by GRC tool)

| Data Source | ServiceNow | OneTrust | Vanta |
|-------------|-----------|----------|-------|
| Entra ID users list | REST API + scheduled import | API connector | Native integration |
| MFA enrollment status | REST API | API connector | Native integration |
| SentinelOne agent health | REST API | API connector | Native integration |
| Vulnerability scan results | Qualys integration | Qualys API | API connector |
| Cloud resources | Azure/GCP/AWS API | API connector | API connector |
| EDR coverage report | REST API | API connector | Native integration |
| DMARC/SPF config | Manual review | Manual review | Native integration |

### Manual Evidence Templates

For controls without automated evidence (policies, procedures, training), use CERG templates:

| Template CERG ID | Purpose |
|-----------------|---------|
| TMPL-AUD-001 | Control evidence worksheet |
| TMPL-SCP-001 | System control profile |
| TMPL-CUI-002 | POA&M |
| TMPL-MTR-001 | Board reporting deck |
| TMPL-SAAS-001 | SaaS evidence checklist |
| TMPL-SBOM-001 | SBOM evidence checklist |

---

## 5. Phase 4: Policy Exception & Acceptance Workflow (Week 4-8)

### Configure the Risk Acceptance Flow

```text
Finding identified → Risk owner assesses → Document compensating control →
→ Submit exception request → CISO reviews → 
→ If approved: Set expiration date (max 12 months)
→ If rejected: Create remediation plan with target date
→ Quarterly review of all outstanding exceptions
```

**CERG templates that map directly:**
- TMPL-RM-002 Security Exception Request Form
- TMPL-RM-004 Risk Acceptance Request Form
- TMPL-RM-003 Risk Acceptance Memo

**In ServiceNow:** Configure as a standard change request pathway with CISO approval step.

**In OneTrust:** Configure as a risk acceptance workflow.

**In Vanta:** Use the built-in Finding → Accept Risk flow.

---

## 6. Phase 5: Vendor Risk Management (Week 6-10)

### Import Vendor Assessment

CERG TPRM-001 vendor questionnaire + SR-1/SR-2 controls provide the assessment template.

**Minimum vendor tiers:**
- **Critical** (data access, authentication provider): Full assessment + SOC 2 + penetration test → Annually
- **High** (data processing, infrastructure): Full questionnaire + SOC 2 → Annually
- **Medium** (data exposure limited): Short questionnaire → Every 2 years
- **Low** (no data access, standard SaaS): Security review → Once

### Vendor Risk SLAs

```text
Critical vendor onboarding: Assessment completed before contract signing
High vendor onboarding: Assessment completed within 30 days of contract
Vendor breach notification: Critical = 24h, High = 72h
Vendor review cadence: Annual for Critical/High
```

---

## 7. Tool-Specific: ServiceNow GRC Deep Dive

### Why ServiceNow for Enterprise GRC

1. **Single platform for ITSM + GRC + SecOps.** No custom integration between change tickets and risk assessments.
2. **Vendor Risk Management** is a native module. No separate tool.
3. **Policy & Compliance** module houses controls, evidence, audits in one place.
4. **Performance Analytics** provides CISO dashboard out of the box.
5. **Common Services Data Model** means CMDB, Incident, Change, and GRC share data.

### Recommended ServiceNow Modules

| Module | Required? | Purpose | Implementation Time |
|--------|-----------|---------|-------------------|
| Policy & Compliance Management | Yes | Controls, policies, evidence collection | 4-6 weeks |
| Risk Management | Yes | Risk register, scoring, risk acceptance | 2-3 weeks |
| Vendor Risk Management | Yes | Vendor assessments, questionnaires | 3-4 weeks |
| Audit Management | Yes | Audit planning, evidence requests, findings | 2-3 weeks |
| Performance Analytics | No (nice to have) | CISO dashboard, executive reporting | 1-2 weeks |
| SecOps Response | No | Integrates SIEM alerts with IR playbooks | 4-8 weeks |

### Implementation Team

```text
ServiceNow Platform Admin: Full-time (internal or partner)
Security Consultant (CERG): 2 days/week for control framework
Subject Matter Experts: 2 hours/week per domain
Project Manager: 4 hours/week
```

### Estimated Timeline

```text
Week 1-2:  Framework ingestion (controls, policies, regulations)
Week 3-4:  Risk register + risk taxonomy
Week 5-8:  Evidence collection automation + API integrations
Week 9-10: Vendor risk management configuration
Week 11-12: Reporting + dashboard + CISO summary
Week 13-16: Testing, refinement, user acceptance
```

---

## 8. GRC Rollout — What CERG Docs Map Where

| GRC Tool Module | CERG Documents to Import | Notes |
|----------------|-------------------------|-------|
| **Policy Library** | POL-001, OM-001, 15x STD docs, 12x PRC docs | Import as markdown/HTML, not PDF. Version control enabled. |
| **Control Framework** | CB-001 (99 controls, 18 families) | Map all 99 controls. Each control gets a test procedure from the CB-001 Verification section. |
| **Risk Register** | TAX-001 (risk taxonomy), RMF-001 (methodology), FRM-001 (framework) | Risk categories from TAX-001 map to GRC risk taxonomy. |
| **Vendor Assessments** | TPRM-001 (questionnaire), SR-1, SR-2 (controls) | Build as vendor risk questionnaire in GRC tool. |
| **Evidence Collection** | TMPL-AUD-001 (evidence worksheet), TMPL-SCP-001 (system profile) | Configure auto-evidence for technical controls, manual upload for policy controls. |
| **Audit Management** | TMPL-CUI-002 (POA&M), Improvement Register | Create annual audit plan from CAL-001 calendar. |
| **Training Tracking** | TRN-001 (training framework), CMP-001 (competencies) | Import training matrix, track completion. |
| **Metrics Dashboard** | MTR-001 (metrics), CAL-001 (calendar) | Configure 5 top metrics from CB-001: vuln SLA, phishing click rate, access review %, MTTD, MTTR. |

---

## 9. GRC Rollout — Sizing by Client Size

| Activity | SMB (Vanta) | Mid-Market (OneTrust) | Enterprise (ServiceNow) |
|----------|-------------|----------------------|------------------------|
| Framework import | 1 day (API-native) | 3 days (import wizard) | 2 weeks (data model config) |
| Policy import | 1 day (native editor) | 3 days (bulk import) | 1 week (Policy & Compliance module) |
| Risk register | 1 day (spreadsheet import) | 3 days (risk taxonomy config) | 2 weeks (risk model design) |
| Evidence automation | 2 days (API connectors) | 2 weeks (API integrations) | 4 weeks (automation engine + scripting) |
| Vendor risk | 2 days (built-in) | 1 week (questionnaire templates) | 3 weeks (Vendor Risk module setup) |
| User training | 1 hour (video + email) | 4 hours (workshop) | 2 days (admin + user training) |
| **Total engagement** | **2 weeks** | **4-6 weeks** | **12-16 weeks** |

---

## 10. GRC Tool Pricing (2026 Estimated)

| Tool | Annual License | Implementation | Ongoing Support |
|------|---------------|----------------|-----------------|
| Vanta | $12k (starter) - $36k (business) | Included | Included |
| Drata | $15k (starter) - $48k (scale) | Included | Included |
| OneTrust | $60k - $200k | $30k (partner) | $15-30k (annual) |
| LogicGate | $50k - $150k | $25k (partner) | $12-25k (annual) |
| ServiceNow GRC | $150k - $500k+ | $100k - $300k (partner) | $30k - $100k (annual) |

**What the practice can charge:**
- Vanta setup: $5k - $10k (2 weeks)
- OneTrust setup: $20k - $50k (4-6 weeks)
- ServiceNow GRC: $100k - $250k (12-16 weeks, typically with implementation partner)
