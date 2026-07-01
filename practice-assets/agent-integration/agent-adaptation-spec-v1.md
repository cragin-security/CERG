# CERG Document Adaptation Agent — Specification v1
## Practice Asset — Not a CERP Corpus Document

---

## Capability
Take a completed `cerg-org-profile.yml`, run the CERG render tool, validate the output, and flag sector-specific issues in the rendered corpus.

## Trigger
A completed and signed `cerg-org-profile.yml` is placed in the client repository root.

## Inputs Required
1. `cerg-org-profile.yml` with all 22 tokens populated
2. Client repository path (where the CERG corpus lives)
3. Sector profile (from `practice-assets/sector-profiles/sector-{sector}-v1.md`)

## Knowledge to Load

### CERG Corpus
- `governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md` — token catalog, phrase map, render workflow
- `tools/cerg-render.py` — available via terminal tool

### Practice Assets
- `practice-assets/checklists/org-profile-checklist-v1.md` — token-by-token validation rules
- `practice-assets/sector-profiles/sector-{sector}-v1.md` — sector-specific adaptation guidance

## Instructions

### Step 1: Validate Token Completeness
Run the org profile checklist against `cerg-org-profile.yml`:
- Verify all 22 tokens have values
- No token contains the V1 reference value ("Northwind Energy", "14,000", "NERC-CIP")
- `{{ORG_SECTOR}}` maps to an existing sector profile
- `{{REGULATORS}}` includes only confirmed frameworks
- `{{SCALE_TIER}}` is consistent with `{{CERG_TEAM_SIZE}}`

Report any failures to the practice lead before proceeding.

### Step 2: Validate Sector Fit
Cross-reference `{{ORG_SECTOR}}` against the sector profile:
- Is the token value an exact match? (not "Tech" for "Technology / SaaS")
- Does the sector profile have regulatory routing guidance that matches `{{REGULATORS}}`?
- Flag any mismatch between sector-specific metric priorities and the regulators selected

### Step 3: Run Render
Execute: `python3 tools/cerg-render.py --profile cerg-org-profile.yml --check`

If `--check` reports unresolved tokens, list each one and the source document.

If `--check` passes, execute the full render:
`python3 tools/cerg-render.py --profile cerg-org-profile.yml --out rendered/`

### Step 4: Validate Rendered Corpus
Check the rendered output for:
- No bare `{{TOKEN}}` strings remain anywhere in the corpus
- `{{ORG_NAME}}` appears correctly in policy headers and document metadata
- `{{REGULATORS}}` appears in crosswalk tables and overlay matrices
- `{{SCALE_TIER}}`-related language reads correctly (e.g., "small team" language is not paired with "enterprise" scale examples)

### Step 5: Run Validator
Execute: `python3 tools/cerg-validate.py`

The validator must pass with 0 errors before the corpus is considered production-ready.

### Step 6: Flag Sector-Specific Issues
Review the rendered corpus for sector-specific accuracy:
- Do the threat scenarios in the documents match the client's sector? (e.g., a Healthcare client should not see manufacturing-specific examples)
- Do the regulatory references match the selected overlays?
- Flag the practice lead on any sector-specific adaptation that might require manual review.

## Output Format
A file named `adaptation-report-{CLIENT}.md` written to the client repository root:

```markdown
# Adaptation Report: {CLIENT}

## Token Validation
- Total tokens: 22
- Unresolved: 0
- Sector match: ✅ ({SECTOR})

## Render Check
- Status: ✅ Pass
- Unresolved tokens reported: 0

## Validator
- Status: ✅ Pass
- Errors: 0

## Sector Flags
- {Number} flags raised (see below)

## Recommendations
1. {Recommendation}
2. {Recommendation}
```

## Validation Criteria
- [ ] All 22 tokens validated against checklist
- [ ] Render `--check` passes
- [ ] Full render completes successfully
- [ ] Validator passes with 0 errors
- [ ] No bare `{{TOKEN}}` strings in rendered corpus
- [ ] Sector-specific accuracy confirmed or flags raised
