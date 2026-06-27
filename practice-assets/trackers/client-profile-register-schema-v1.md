# Client Profile Register — Schema v1
## Practice Asset — Not a CERG Corpus Document
## Purpose: Anonymized register of every CERG engagement for pattern recognition

---

## Why Anonymized

Client profile data drives practice improvements — which sectors are underserved, which overlays need the most tailoring, which tiers produce the best client outcomes. Linking specific data to a named client creates an unnecessary liability and inhibits honest pattern analysis. The register identifies engagements by Engagement ID only; client names are stored only in the engagement tracker (§5.1), which is access-restricted.

---

## Schema

### Per-Client Record Structure

```yaml
record_id: CLT-{YYYY}-{NNN}
engagement_id: CERG-{TIER}-{YYYY}-{NNN}
anonymized: true

profile:
  tier: {1 | 2 | 3 | 4}
  sector: {sector_name}  # from intake
  size_classification: {small | mid | large | enterprise}
  regulatory_burden: {none | single | multiple | critical_infrastructure}
  overlays_selected: [{overlay1}, {overlay2}]
  maturity_initial: {initial | formative | defined | managed | optimized}
  maturity_day90: {initial | formative | defined | managed | optimized}

cadence:
  days_to_first_risk_review: {number}
  day30_milestone_met: {true | false}
  day90_milestone_met: {true | false}
  
outcome:
  maturity_delta: {+N | -N levels}
  handover_satisfaction_score: {1-5}
  follow_on_engagement: {true | false}
  follow_on_tier: {1 | 2 | 3 | 4 | null}
  days_to_follow_on: {number | null}

practice:
  overlays_requiring_tailoring: [{overlay1}, {overlay2}]
  sprint_delivered_on_time: {true | false}
  scope_changes_during: {number}
  practitioner_count: {number}
  practice_assets_used: [{asset_id1}, {asset_id2}]
```

---

## Summary Table (Spreadsheet View)

| ID | Eng ID | Tier | Sector | Size | Burden | Overlays | Mat Init | Mat D90 | Δ | Days to 1st Rev | Day30✓ | Day90✓ | Sat(1-5) | Follow-on |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLT-2026-001 | CERG-2-2026-003 | 2 | HC | Mid | Single | SOX | Defined | Managed | +2 | 22 | ✅ | ✅ | 4 | Tier 3 |
| CLT-2026-002 | CERG-1-2026-001 | 1 | Tech | Small | None | — | Initial | Defined | +3 | 18 | ✅ | ✅ | 5 | — |

---

## Update Cadence

| Event | When | Who |
|---|---|---|
| Record created | On engagement start | Engagement Lead |
| Day-30 milestone updated | Within 2 days of day 30 | Engagement Lead |
| Day-90 milestone updated | Within 2 days of day 90 | Engagement Lead |
| Outcome updated | On handover | Engagement Lead |
| Satisfaction and follow-on | Within 14 days of handover | Practice Principal |

---

## Minimum Viable Target

The practice should maintain at least **10 anonymized records** before drawing conclusions about:
- Per-sector engagement duration benchmarks
- Per-overlay tailoring effort estimates
- Tier assignment accuracy (did the assigned tier match the actual effort needed?)
- Practitioner-to-engagement ratios

The client profile register enables answering "we haven't done a Tier 3 in the Healthcare sector before — what can we learn from the three that are closest to it?" without exposing client identity.
