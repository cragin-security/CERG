# Post-Engagement Debrief Protocol v1
## Practice Asset — Not a CERG Corpus Document
## Purpose: Structured knowledge capture within 5 business days of handover

---

## Schedule

Every Tier 2+ engagement produces a structured debrief. The debrief is completed within **5 business days** of handover acceptance. The Engagement Lead owns the debrief; the Practice Principal reviews and archives it.

Tier 1 engagements may produce an abbreviated debrief at the Engagement Lead's discretion.

---

## Debrief Structure

### 1. Engagement Overview

| Field | Value |
|---|---|
| Engagement ID | |
| Client | |
| Tier | |
| Sector | |
| Overlays Applied | |
| Duration (planned → actual) | |
| Handover Date | |
| Client Satisfaction Score (1-5) | |
| Debrief Author | |
| Debrief Date | |

### 2. What Worked

Describe what went well in the engagement design and delivery. Be specific about artifacts, sequencing, and client interactions.

- Which CERG artifacts were most useful to the client?
- Which sequencing decisions (what we did first, what we deferred) were right?
- Which practice assets (intake, checklist, templates, sector profiles) were most effective?
- What client-specific adaptation was the most successful?

Add one bullet per observation. Remove any that do not apply.

### 3. What Didn't Work

Describe friction, confusion, or outright failures in the engagement. These are not failures of the client — they are signals about the engagement design or practice assets.

- Which CERG artifacts caused confusion or required too much explanation?
- Which sequencing decision was wrong? (What should have been done earlier or later?)
- Which practice asset was missing, stale, or misaligned with the client's reality?
- What did the client push back on that the practice assumed would be smooth?
- Where did the validator or tooling fail?

### 4. Sector-Specific Observations

- Did the sector profile (from the threat model catalog) cover the client's actual threat landscape?
- What threat scenario did the client face that was NOT in the sector profile?
- What regulatory overlay required the most tailoring beyond the standard package?
- Did the client's regulator have expectations that the operational package did not anticipate?

### 5. Asset Improvement Recommendations

For each gap identified in §3 and §4, recommend a specific improvement to a practice asset:

| Asset | Improvement | Priority |
|---|---|---|
| [Asset ID/path] | [What to change] | High / Medium / Low |

### 6. Practice Backlog Items

Convert actionable improvement recommendations to practice backlog entries (see `todov1.md` taxonomy):

- Validator gap
- Template omission
- Missing overlay
- Documentation gap
- Training gap

### 7. Client Profile Data (Anonymized)

For the client profile register (§6.2):

| Field | Value |
|---|---|
| Tier | |
| Sector | |
| Overlays | |
| First Risk Review (days from start) | |
| Day-30 Milestone Met | |
| Day-90 Maturity Delta | |
| Referral Likelihood (1-5) | |
| Follow-on Engagement | |

### 8. Raw Observations

Free-text section for anything that does not fit above. This is the archive that future practitioners mine for patterns.

---

## Archive Rules

| Artifact | Retention | Location |
|---|---|---|
| Debrief document | Indefinite | `practice-assets/debriefs/CERG-{ID}-debrief.md` |
| Client profile data (anonymized) | Indefinite | Client profile register |
| Engagement ID in tracker | Indefinite | Engagement status tracker |
| Raw debrief notes | 90 days after debrief | Practitioner's private notes; deleted after archiving |

## Debrief File Naming

```
practice-assets/debriefs/CERG-{TIER}-{YYYY}-{NNN}-debrief.md
```

Example: `practice-assets/debriefs/CERG-2-2026-003-debrief.md`

---

## Abbreviated Template (Tier 1)

```
# Debrief: CERG-{ID}

**Engagement:** {Client}, Tier 1, {Sector}
**Debrief Author:** {Name}
**Date:** {YYYY-MM-DD}

**What Worked:**
- ...
**What Didn't:**
- ...
**Recommendation for Practice:**
- ...
```
