# CERG Sector Threat Model Agent — Specification v1
## Practice Asset — Not a CERP Corpus Document

---

## Capability
Per sector: ingest threat intelligence sources, MITRE ATT&CK data, and sector-specific guidance, then produce or update a CERG-relevant threat scenario library with control and evidence mappings.

## Trigger
- A new sector is identified during intake that is not in the current catalog
- An existing sector profile is flagged for refresh (based on debrief feedback or upstream threat intel changes)
- Quarterly threat landscape review cycle

## Inputs Required
1. Sector name (from sector catalog taxonomy)
2. Threat intelligence sources for the sector (ISAC reports, vendor threat briefs, CISA alerts)
3. MITRE ATT&CK enterprise + ICS matrices
4. Existing sector profile (`practice-assets/sector-profiles/sector-{sector}-v1.md`)
5. CERG CB-001 control baseline (`governance/CERG-GOV-CB-001_Unified_Control_Baseline.md`)

## Knowledge to Load

### CERG Corpus
- `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md` — §6 (control set), §9.1 (evidence catalog)
- `machine-readable/cerg-llm-index.json` — document inventory for cross-references

### Practice Assets
- `practice-assets/sector-profiles/sector-threat-model-catalog-v1.md` — existing catalog structure
- `practice-assets/sector-profiles/sector-{sector}-v1.md` — sector profile to update
- `practice-assets/trackers/debrief-protocol-v1.md` — §4 (sector-specific observations)

### External
- Threat intelligence feeds relevant to the sector (web search, ISAC publications, CISA advisories)

## Instructions

### Step 1: Sector Threat Landscape Assessment
Research the current threat landscape for the sector:
- Top 5-7 threat scenarios currently observed in the sector
- Change from previous period (new threats emerging, old threats declining)
- Most common initial access vectors
- Most impactful incident types (regulatory action, data breach, ransomware, physical impact)
- Regulatory or government guidance specific to the sector

### Step 2: Map Threats to CERG Controls
For each threat scenario, identify:
- Primary CERG controls that prevent or detect the threat
- Specific evidence artifacts that demonstrate control effectiveness
- Minimum evidence cadence that would satisfy a regulator or auditor

Use the format from the existing threat model catalog (one row per scenario with threat, controls, evidence).

### Step 3: Identify Gaps in Current Coverage
Flag any threat scenario that has no adequate CERG control coverage:
- Is this a new threat that requires a new control?
- Can an existing control be tightened to cover it?
- Is this a tooling-specific gap (CERG is process-neutral; tool gaps are practice notes, not corpus changes)?

### Step 4: Update Priority Standards
Review the priority standards listed in the sector profile. Based on the threat landscape update:
- Are the current priority standards still correct?
- Should any standard be promoted or demoted?
- Is there a new regulatory requirement that changes priorities?

### Step 5: Produce Updated Profile
Generate the updated sector profile following the existing format:
- Default tier
- Default overlays
- Regulatory routing table
- Threat scenario table
- Priority standards
- Common engagement mistakes

## Output Format
- Full sector profile written to `practice-assets/sector-profiles/sector-{sector}-v{NEW_VERSION}.md`
- Summary of changes: `practice-assets/sector-profiles/changelog-{sector}-{date}.md`

For existing profiles, produce a diff-only update:

```markdown
# Sector Profile Update: {SECTOR}

## What Changed
- {Threat scenario} added (source: {source})
- {Threat scenario} modified (rationale: {rationale})
- {Control} mapping updated from {old} to {new}
- {Standard} priority changed from {old} to {new}

## New Content
{excerpt}

## Expired Content
{excerpt}
```

## Validation Criteria
- [ ] 5-7 threat scenarios per sector (not fewer, not more — keeps the catalog scannable)
- [ ] Each threat scenario maps to at least one CB-001 control
- [ ] Evidence references use names from CB-001 §9.1 evidence catalog
- [ ] Threat sources are cited (ISAC report, CISA advisory, MITRE technique ID)
- [ ] No tool-specific recommendations (CERG is process-neutral)
- [ ] Profile follows the established template format
