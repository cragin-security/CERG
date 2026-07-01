# CERG Client Artifact Assembly Agent — Specification v1
## Practice Asset — Not a CERP Corpus Document

---

## Capability
Assemble the complete client deployment package from individual components: rendered corpus, org profile, scope document, risk register bootstrap, handover memo, and improvement register.

## Trigger
- Engagement handover is 5 business days away
- All component artifacts are in their expected locations

## Inputs Required
1. Client repository path (containing rendered CERG corpus)
2. Completed `cerg-org-profile.yml`
3. Risk register bootstrap (`practice-assets/templates/risk-register-bootstrap-v1.md` or equivalent client-specific file)
4. Engagement scope template (completed per intake agent output)
5. Handover memo template (`practice-assets/templates/handover-memo-v1.md`)
6. Client improvement register template (`practice-assets/templates/client-improvement-register-v1.md`)
7. Signed adoption record (`practice-assets/templates/signed-adoption-record-v1.md`)
8. Engagement tracker record (`practice-assets/trackers/engagement-status-schema-v1.md`)

## Knowledge to Load

### CERG Corpus
- `plans/CERG-PLN-CON-001_Consulting_Services_Operating_Plan.md` — §6 (standardized deliverables table, artifact ownership conventions)

### Practice Assets
- `practice-assets/templates/signed-adoption-record-v1.md`
- `practice-assets/templates/risk-register-bootstrap-v1.md`
- `practice-assets/templates/handover-memo-v1.md`
- `practice-assets/templates/client-improvement-register-v1.md`
- `practice-assets/templates/practice-case-study-v1.md`
- `practice-assets/checklists/org-profile-checklist-v1.md`
- `practice-assets/scope-templates/tier{1,2,3,4}-{scope}.md`

## Instructions

### Step 1: Inventory Artifacts
Check which deliverables are present in the client repository. The CERG-PLN-CON-001 §6.1 table defines the required deliverables per tier.

| Artifact | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Org profile | Required | Required | Required | Required |
| Rendered corpus | Required | Required | Required | Required |
| Catalog with status | Required | Required | Required | Required |
| Signed policy | Required | Required | Required | Required |
| Maturity baseline | Required | Required | Required | Required |
| Risk register | Required (guided) | Required (guided) | Required (supported) | Required (supported) |
| First cadence cycle | Required (guided) | Required | Required | Required |
| Handover memo | Optional | Required | Required | Required |

### Step 2: Complete Adoption Record
Fill the signed adoption record template with:
- Client organization info from `cerg-org-profile.yml`
- Adoption date
- CERG version from rendered corpus metadata
- Signature blocks for CISO, Executive Sponsor, and Practice Lead
- Artifact inventory table listing MVC documents and their adoption status

### Step 3: Complete Handover Memo
Fill the handover memo template with:
- Engagement summary from the engagement scope document
- Deliverables status (what was delivered, what is in progress, what was deferred)
- Current state: which cadences are running independently
- Deferred decisions from the improvement register
- Handover checklist (review with client)
- Next 90 days recommendation

### Step 4: Seed Improvement Register
Populate the improvement register with:
- All deferred standards and procedures from the catalog adoption log
- All scope items marked "out of scope" that the client may revisit
- All maturity baseline findings that were not remediated during the engagement
- Each entry must have a type (from the 8 types), a named owner, and a target date

### Step 5: Update Engagement Tracker
Create the engagement tracker record with:
- Engagement ID, client, tier, sector, overlays
- Key milestone dates (intake, start, policy signed, first risk review, handover)
- Maturity baseline and delta

### Step 6: Verify Completion
Run the handover checklist:

- [ ] Rendered corpus in client repository
- [ ] Policy signed and scanned
- [ ] Risk register populated
- [ ] Improvement register seeded
- [ ] Handover memo completed
- [ ] Engagement tracker updated
- [ ] Case study skeleton created (optional, if approval for external use)

## Output Format
All artifacts written to the client repository. A summary file named `deployment-package-checklist-{CLIENT}-{DATE}.md` written to the practice engagement directory documenting what was assembled, what was deferred, and any issues encountered.

## Validation Criteria
- [ ] All tier-required deliverables from CON-001 §6.1 are present
- [ ] Adoption record has all required signature blocks
- [ ] Handover memo has all required fields completed
- [ ] Improvement register has at minimum: one entry per deferred standard, one entry per open maturity finding, named owners, target dates
- [ ] Engagement tracker record has all required timestamps
- [ ] No `{{PLACEHOLDER}}` strings remain in completed templates
