# CERG Intake Questionnaire v1
## Practice Asset — Not a CERG Corpus Document
## Purpose: Classify client → tier + sector + overlays in 15 questions

---

### Instructions
Complete this questionnaire before scoping any CERG engagement. Each answer feeds `cerg-org-profile.yml` token values and determines the engagement tier, sector profile, and mandatory overlay packages. Where the client cannot answer, note the gap in the "Deferred / Unknown" column.

---

## Section A: Organization Identity (→ org profile)

**A1. Organization name (common name)**
Field: `{{ORG_NAME}}`

**A2. Legal entity name**
Field: `{{ORG_LEGAL_NAME}}`

**A3. Short name / abbreviation**
Field: `{{ORG_SHORT_NAME}}`

**A4. Industry sector**
Options: Technology/SaaS · Financial Services · Healthcare/Life Sciences · Manufacturing/OT · Energy/Utilities · Defense Industrial Base · Government/Federal · Cross-sector/Holding · Other (specify)
→ Determines sector profile (Section 2 of todov1)

---

## Section B: Size and Scale (→ tier + org profile)

**B1. Total organization headcount**
Options: < 500 · 500–10,000 · 10,000–100,000 · 100,000+
Field: `{{TOTAL_EMPLOYEES}}`

**B2. Security team headcount**
Options: 1–5 · 5–15 · 15–30 · 30–150 · 150+
Fields: `{{CERG_TEAM_SIZE}}`, `{{ENG_STAFF}}`, `{{RISK_STAFF}}`, `{{GOV_STAFF}}`
→ Determines size classification and role consolidation map

**B3. Does a named security leader exist (CISO or equivalent)?**
Yes / No / Shared (e.g., IT Director carries security)
→ Gate: if No, engagement must start with executive alignment before CERG adoption

**B4. Is there an Executive Sponsor who will endorse the security policy?**
Yes / No / To be identified
→ Gate: if No, policy cannot be signed; engagement scope changes

**B5. Does the organization have a written cybersecurity policy today?**
Yes, current · Yes, outdated · No
→ Helps determine Tier 1 vs Tier 2 entry point

---

## Section C: Regulatory Burden (→ tier + overlay packages)

**C1. Which regulatory frameworks apply? (select all)**
☐ NERC-CIP (registered entity)
☐ CMMC / CUI / DFARS
☐ SOX ITGC (publicly traded)
☐ PCI DSS (stores/processes/transmits cardholder data)
☐ ISO 27001 (certified or pursuing)
☐ HIPAA / HITRUST
☐ FedRAMP / FISMA
☐ GDPR / CCPA / Privacy framework
☐ None (internal governance only)

**C2. Rank the single most consequential regulator for your organization (drives scope, audit frequency, penalties)**
→ Determines `{{PRIMARY_REGULATOR}}`

**C3. Full list of regulators (comma-separated)**
→ Determines `{{REGULATORS}}`

**C4. Does the organization have an existing audit or assessment calendar?**
Yes, documented · Yes, informal · No
→ Helps determine maturity baseline

**C5. Has the organization had a material audit finding in the last 12 months?**
Yes / No / Not applicable (no prior audit)
→ If Yes, flag for Tier 3+ and root cause analysis during intake

---

## Section D: Existing Capabilities (→ maturity baseline + gap analysis)

**D1. Which of the following are currently operational?**
☐ Risk register (populated and reviewed)
☐ Vulnerability management program
☐ Access recertification process
☐ Security architecture review / project intake
☐ Incident response plan (tested)
☐ Third-party / vendor risk management
☐ Configuration baseline (hardening standard)
☐ Evidence library for audits
☐ Metrics dashboard / CISO reporting
→ Helps set the maturity baseline (Initial / Formative / Defined / Managed / Optimized)

**D2. What is the primary pain point driving this engagement?**
☐ No existing security program / starting from scratch
☐ Policy exists but is not operational
☐ Audit findings recur / evidence is assembled annually
☐ Regulatory pressure (new or expanded scope)
☐ M&A integration / organizational change
☐ Tooling is in place but processes are ad hoc
☐ Other (specify)
→ Helps determine engagement narrative and "why CERG" value proposition

**D3. What is the approximate annual cybersecurity budget?**
☐ < $250K
☐ $250K–$1M
☐ $1M–$5M
☐ $5M+
→ Guides price anchor, tooling assumptions, and staffing expectations

---

## Section E: Engagement Logistics

**E1. Desired engagement start window**
☐ Immediate (within 2 weeks)
☐ Next quarter
☐ Future (no committed date)

**E2. Engagement duration expectation**
☐ 30–60 days (quick start)
☐ 90 days
☐ 90–180 days
☐ Ongoing retainer
→ Helps select tier and pricing model

---

## Routing Logic

### Tier Assignment
Apply the highest applicable tier:

| Condition | Tier |
|---|---|
| No existing program, team < 5, no regulatory pressure | Tier 1 |
| Existing function, fragmented policies, team 5–15 | Tier 2 |
| Regulated environment, recurring audit burden | Tier 3 |
| Multiple regulators, enterprise scale, strategic investment | Tier 4 |
| Team > 100 OR budget > $5M OR multiple concurrent AOC/ROC deadlines | Tier 4 |

### Overlay Selection
For each checked regulator in C1, the corresponding operational package is mandatory:
- NERC-CIP → `CERG-PLN-CIP-001`
- CMMC/CUI → `CERG-PLN-CUI-001`
- SOX ITGC → `CERG-PLN-SOX-001`
- PCI DSS → `CERG-PLN-PCI-001`
- ISO 27001 → `CERG-PLN-ISO-001`
- HIPAA/HITRUST → `CERG-PLN-PRIV-001` + sector profile
- Privacy → `CERG-PLN-PRIV-001`

### Sector Profile Activation
From A4, the corresponding sector profile is loaded:
→ `practice-assets/sector-profiles/SECTOR_profile.md`

---

## Output

Completed intake produces:
1. `cerg-org-profile.yml` stub with populated token values
2. Engagement tier assignment
3. Sector profile reference
4. Mandatory overlay package list
5. Maturity baseline (from D1)
6. Deferred decisions log (items marked pending or unknown)

**Format:** YAML or structured JSON for automated processing. A completed intake file becomes the input to the engagement scope template (see `practice-assets/scope-templates/`).
