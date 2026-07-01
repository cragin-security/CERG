# Practitioner Onboarding Guide v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: Getting a new practice engineer productive within 2 weeks

---

## Week 1: CERG Corpus Orientation

### Day 1–2: Read the Spine

| Order | Document | Expected Time | Why It Matters |
|---|---|---|---|
| 1 | `START-HERE.md` | 30 min | Adoption narrative and path selection |
| 2 | `governance/CERG-POL-001_Cybersecurity_Policy.md` | 45 min | The 10 principles — everything derives from this |
| 3 | `governance/CERG-GOV-FRM-001_CERG_Framework.md` | 30 min | Three-pillar model narrative |
| 4 | `governance/CERG-GOV-OM-001_CERG_Operating_Model.md` | 45 min | Canonical role roster, RACI, decision rights |
| 5 | `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md` | 60 min | The map of all documents — refer back constantly |
| 6 | `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md` | 60 min | The control set — most-cited document in audits |
| 7 | `governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md` | 45 min | How clients actually adopt CERG |

**Check:** Can you explain to a client why POL-001 is the spine and CAT-001 is the index?

### Day 3: Understand the Consulting Model

| Asset | What to Learn |
|---|---|
| `CERG-PLN-CON-001_Consulting_Services_Operating_Plan.md` | The four tiers, client routing, standardized deliverables |
| `practice-assets/intake/cerg-intake-questionnaire-v1.md` | How we classify clients |
| `practice-assets/scope-templates/tier*.md` | What is in and out of scope per tier |
| `practice-assets/sector-profiles/sector-threat-model-catalog-v1.md` | The 8 sectors and their threat models |

**Check:** Given a hypothetical client (sector: Financial Services, team: 12 FTEs, regulators: SOX), what tier do you recommend and why?

### Day 4: Practice Asset Library Tour

Walk through every file in `practice-assets/`:

| Directory | Purpose |
|---|---|
| `intake/` | Client classification |
| `scope-templates/` | Engagement scoping |
| `sector-profiles/` | Sector-specific guidance + overlay assessments |
| `templates/` | Reusable client artifacts |
| `scripts/` | Automation (CI check, render-and-diff, provisioning) |
| `trackers/` | Engagement management, debrief, backlog |

**Check:** What is the difference between `sector-threat-model-catalog-v1.md` and `sector-FINANCIAL-v1.md`? (Answer: catalog is cross-sector; financial profile is sector-specific depth.)

### Day 5: Tooling Exercise

```
# Clone the practice fork
git clone https://github.com/cragin-sec/CERG.git
cd CERG

# Run the validator
python3 tools/cerg-validate.py

# Review the LLM index
cat machine-readable/cerg-llm-index.json | python3 -m json.tool | head -40

# Run the render check
python3 tools/cerg-render.py --check

# Run the upstream drift check
python3 practice-assets/scripts/check-upstream-drift.py \
  --client-repo . \
  --out /tmp/drift-report.md
```

**Check:** Validator passes; drift report shows no discrepancies.

---

## Week 2: Client Delivery Simulation

### Day 6: Simulate Intake

Take the intake questionnaire and fill it out for a hypothetical client:

```
Client: Acme Health Systems
Sector: Healthcare
Headcount: 3,000
Security team: 8 FTEs
Regulators: HIPAA, PCI (handles CHD in patient payments)
Pain point: Audit findings recur
```

1. Determine tier, sector, overlays
2. Complete `cerg-org-profile.yml` stub
3. Run through the org profile checklist

### Day 7: Simulate Rendering

```
# Copy the default profile
cp cerg-org-profile.yml cerg-org-profile-acme.yml

# Edit tokens to match Acme Health Systems
# Run render check
python3 tools/cerg-render.py --profile cerg-org-profile-acme.yml --check
```

### Day 8: Simulate Risk Register Bootstrap

Open `practice-assets/templates/risk-register-bootstrap-v1.md`.

1. Customize all 10 entries for Acme Health Systems
2. Add 3 entries specific to healthcare (PHI, BA agreements, clinical trial data if applicable)
3. Run through the first risk review format

### Day 9: Simulate Handover

1. Complete the handover memo for Acme Health Systems
2. Seed the improvement register with deferred standards
3. Write the handover summary

### Day 10: Shadow an Active Engagement (If Available)

If no active engagement, pair with a senior practitioner on backlog review.

---

## Competency Checklist

After 2 weeks, the practitioner should be able to:

- [ ] Run `cerg-validate.py` and interpret the output
- [ ] Run `cerg-render.py --check` and resolve token issues
- [ ] Explain the difference between Tier 1–4 to a client
- [ ] Classify a client by sector, size, and regulatory burden
- [ ] Identify which operational package applies to which regulator
- [ ] Locate any CERG document by ID
- [ ] Explain the three-pillar model
- [ ] Explain why NIST 800-53 is the CB-001 spine
- [ ] Navigate the practice asset library without guidance
- [ ] Complete a debrief document after a mock engagement

## Ongoing Development

| Month | Focus |
|---|---|
| 1 | Shadow a Tier 2 engagement as observer |
| 2 | Lead a Tier 1 engagement with senior review |
| 3 | Independently run a Tier 1 engagement |
| 6 | Lead or co-lead a Tier 2 engagement |
| 12 | Lead a Tier 3 engagement with overlay package |
