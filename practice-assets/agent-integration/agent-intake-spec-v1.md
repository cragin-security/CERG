# CERG Intake Agent — Specification v1
## Practice Asset — Not a CERP Corpus Document

---

## Capability
Read completed intake questionnaire responses, classify client by tier + sector + regulatory burden, and output an engagement scope draft.

## Trigger
A completed intake questionnaire file is placed at `practice-assets/intake/completed/{CLIENT_NAME}-intake.md` or the raw responses are provided as input text.

## Inputs Required
1. Intake responses for Sections A–E (from `practice-assets/intake/cerg-intake-questionnaire-v1.md`)
2. Current engagement tier definitions (from `CERG-PLN-CON-001 §3`)
3. Sector profile catalog (from `practice-assets/sector-profiles/sector-threat-model-catalog-v1.md`)

## Knowledge to Load

### CERG Corpus (all from fork)
- `plans/CERG-PLN-CON-001_Consulting_Services_Operating_Plan.md` — §3 (tier model), §4 (client routing), §5 (overlay matrix), §6 (deliverables)
- `governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md` — token catalog

### Practice Assets
- `practice-assets/intake/cerg-intake-questionnaire-v1.md` — questionnaire structure and routing logic
- `practice-assets/scope-templates/tier{1,2,3,4}-scope.md` — scope templates
- `practice-assets/sector-profiles/sector-{sector}-v1.md` — relevant sector profile
- `practice-assets/checklists/org-profile-checklist-v1.md` — token validation

## Instructions

### Step 1: Classify Tier
Apply the routing logic from the intake questionnaire §Routing Logic section. The tier is the HIGHEST applicable tier:

- No existing program, team <5, no regulatory pressure → Tier 1
- Existing function, fragmented policies, team 5–15 → Tier 2
- Regulated environment, recurring audit burden → Tier 3
- Multiple regulators, enterprise scale, strategic investment → Tier 4
- Team >100 OR budget >$5M OR multiple concurrent AOC/ROC deadlines → Tier 4

### Step 2: Classify Sector
Map the client's sector (from question A4) to the threat model catalog. Load the corresponding sector profile from `practice-assets/sector-profiles/`.

### Step 3: Select Overlays
For each checked regulator in Section C, select the corresponding operational package:
- NERC-CIP → `CERG-PLN-CIP-001`
- CMMC/CUI → `CERG-PLN-CUI-001`
- SOX ITGC → `CERG-PLN-SOX-001`
- PCI DSS → `CERG-PLN-PCI-001`
- ISO 27001 → `CERG-PLN-ISO-001`
- HIPAA/HITRUST → Practice HIPAA gap kit + `PLN-PRIV-001`
- Privacy → `CERG-PLN-PRIV-001`
- FedRAMP → Practice FedRAMP adapter

### Step 4: Generate Org Profile Stub
Create a stub `cerg-org-profile.yml` with the values from Section A. Missing values are marked as `{{TBD}}` with a note to the practice lead.

### Step 5: Assess Maturity Baseline
Count the "currently operational" items from Section D. Map to maturity level:
- 0–2 items → Initial
- 3–4 items → Formative
- 5–6 items → Defined
- 7–8 items → Managed
- 9 items → Optimized

### Step 6: Produce Engagement Scope Draft
Fill in the tier-appropriate scope template with:
- Client name, sector, tier, overlays
- In-scope and out-of-scope items from the tier template
- Duration from Section E
- Maturity baseline note
- Price anchor from the pricing model

## Output Format
A file named `CERG-{TIER}-{YYYY}-{NNN}-scope-draft.md` containing:
1. Engagement overview table (tier, sector, regulators, overlays, duration)
2. `cerg-org-profile.yml` stub
3. Maturity baseline assessment
4. Deferred decisions log
5. Scope document with in-scope/out-of-scope/deliverables

Write this file to `practice-assets/intake/completed/`.

## Validation Criteria
- [ ] Every Section A–E response is addressed
- [ ] Tier classification is consistent with the routing logic
- [ ] Each regulator maps to an existing overlay
- [ ] Maturity baseline is calculated correctly
- [ ] Scope document uses the correct tier template
- [ ] No client-identifying information leaks beyond the intake/completed/ directory
