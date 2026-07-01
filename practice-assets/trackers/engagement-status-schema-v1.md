# CERG Engagement Status Tracker — Schema v1
## Practice Asset — Not a CERG Corpus Document
## Purpose: Single source of truth for all active and completed engagements

---

## Implementation

This schema can be stored as:
- A YAML file per engagement (for git-based tracking)
- A spreadsheet with one row per engagement (for shared admin access)
- A Notion/Airtable database (for team collaboration)

The canonical fields are the same regardless of implementation. The YAML form is the practice's reference schema.

---

## YAML Schema

```yaml
engagement:
  id: CERG-{TIER}-{YYYY}-{NNN}
  client: {CLIENT_NAME}
  tier: {TIER}  # 1 | 2 | 3 | 4
  sector: {SECTOR}  # from sector profile catalog
  regulators: [{REGULATOR_LIST}]

intake:
  date: {YYYY-MM-DD}
  source: {REFERRAL_SOURCE}  # webinar | referral | conference | inbound | partner
  intake_completed_by: {PRACTITIONER_NAME}

scoping:
  scope_document: {PATH_TO_SCOPE_DOC}
  overlays_selected: [{overlay1}, {overlay2}]
  price_anchor: {PRICE_ANCHOR}
  signed_sow_date: {YYYY-MM-DD}

execution:
  start_date: {YYYY-MM-DD}
  policy_signed_date: {YYYY-MM-DD}
  first_risk_review_date: {YYYY-MM-DD}
  maturity_baseline_date: {YYYY-MM-DD}
  maturity_baseline_score: {SCORE}
  day_30_milestone_met: {true | false}
  day_60_milestone_met: {true | false}
  day_90_milestone_met: {true | false}
  maturity_delta_score: {SCORE}  # day 90 delta

handover:
  handover_date: {YYYY-MM-DD}
  handover_memo: {PATH_TO_MEMO}
  improvement_register: {PATH_TO_REGISTER}
  handover_accepted_by: {CLIENT_NAME}
  handover_signed_date: {YYYY-MM-DD}

post_engagement:
  debrief_date: {YYYY-MM-DD}
  debrief_document: {PATH_TO_DEBRIEF}
  client_satisfaction_score: {1-5}
  referral_received: {true | false}
  follow_on_engagement_id: {NEXT_ENGAGEMENT_ID | null}
```

---

## Summary View (Spreadsheet Columns)

For the shared admin tracker, these columns are the minimum viable set:

| Field | Example |
|---|---|
| Engagement ID | CERG-2-2026-003 |
| Client Name | Northwind Health |
| Tier | 2 |
| Sector | Healthcare |
| Overlays | SOX, PCI |
| Start Date | 2026-02-01 |
| Policy Signed | 2026-03-01 |
| First Risk Review | 2026-03-15 |
| Day-30 Milestone | ✅ |
| Day-90 Milestone | ✅ |
| Handover Date | 2026-05-01 |
| Day-90 Maturity Delta | +2 levels |
| Client Satisfaction | 4/5 |
| Referral | Yes |
| Follow-on | CERG-3-2026-004 |

---

## Tracking Cadence

| Event | Who Updates | When |
|---|---|---|
| Intake complete | Practice Principal | Day 1 |
| Scope document sent | Engagement Lead | Day 1 |
| Policy signed | Engagement Lead | On sign-off |
| First risk review | Engagement Lead | On completion |
| Milestone check (day 30/60/90) | Engagement Lead | Within 2 business days of milestone date |
| Handover | Engagement Lead | On handover acceptance |
| Debrief | Engagement Lead | Within 5 business days of handover |
| Satisfaction + referral | Practice Principal | Within 14 days of handover |
