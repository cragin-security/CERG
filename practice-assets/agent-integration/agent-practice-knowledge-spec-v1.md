# CERG Practice Knowledge Agent — Specification v1
## Practice Asset — Not a CERP Corpus Document

---

## Capability
Mine debrief documents, case studies, and the client profile register to surface patterns, recommend practice asset updates, and draft upstream contributions.

## Trigger
- Quarterly practice review cycle
- New debrief added to the debrief archive
- Client profile register reaches a new milestone count (10, 25, 50 records)

## Inputs Required
1. All debrief documents from `practice-assets/debriefs/`
2. Client profile register (`practice-assets/trackers/client-profile-register-schema-v1.md` populated records)
3. Practice backlog (`practice-assets/trackers/backlog-taxonomy-v1.md`)
4. Current practice asset directory structure

## Knowledge to Load

### Practice Assets
- `practice-assets/trackers/debrief-protocol-v1.md` — debrief structure
- `practice-assets/trackers/client-profile-register-schema-v1.md` — register schema
- `practice-assets/trackers/backlog-taxonomy-v1.md` — backlog categories
- `practice-assets/trackers/README.md (contributing section)` — contribution decision tree
- All sector profiles — to compare against observed patterns
- All overlay assessments — to check if findings validate or contradict the assessment

## Instructions

### Step 1: Aggregate Debrief Findings
Read all debrief documents in the archive. Extract:

**What Worked (repeated patterns):**
- Which CERG artifacts were most frequently cited as useful across engagements?
- Which sequencing decisions were consistently called out as correct?
- Which practice assets were most effective?

**What Didn't Work (repeated failures):**
- Which CERG artifacts caused the most confusion?
- Which sequencing decisions were consistently called out as wrong?
- Which practice assets were missing or stale?
- Which overlay packages needed the most tailoring?

**Sector-Specific Patterns:**
- For each sector with 3+ debriefs: what patterns emerge?
- Which threats from the threat model catalog were validated? Which were missing?

### Step 2: Analyze Client Profile Register
Read the client profile register. Calculate:

- Average days-to-first-risk-review per tier
- Per-sector maturity delta distribution
- Tier assignment accuracy: what percentage of engagements stayed at the assigned tier vs. upgraded?
- Overlay selection frequency: which packages are most commonly selected? Which require the most tailoring?
- Satisfaction score distribution: which sectors/tiers/overlays correlate with highest/lowest satisfaction?
- Follow-on engagement rate: what percentage of clients upgrade tiers?

### Step 3: Cross-Reference Debriefs with Backlog
For each backlog item, check if debrief evidence supports or contradicts the entry:
- If 3+ debriefs independently raise the same issue, promote to High priority
- If no debrief evidence supports a backlog item, demote or remove
- If debrief evidence reveals a new pattern not in the backlog, create a new backlog entry

### Step 4: Generate Recommendations

#### Practice Asset Updates
For each practice asset, recommend:
- Update: specific section to change and why
- Retire: asset that is no longer used or relevant
- Create: new asset needed based on pattern

Format:
```markdown
| Asset | Recommendation | Evidence | Priority |
|---|---|---|---|
| sector-healthcare-v1.md | Add clinical trial data flow scenario | 2 of 3 healthcare debriefs cited this | High |
| tier2-scope.md | Reduce architecture review activation from required to recommended | 2 Tier 2 engagements deferred this step | Medium |
```

#### Upstream Contribution Candidates
For each candidate, evaluate against the contribution workflow criteria:
- Benefits multiple client profiles?
- Reduces practice maintenance burden?
- Consistent with upstream CERG design principles?

Format:
```markdown
| Candidate | Criteria Score | Contribution Type | Practice Backlog Ref |
|---|---|---|---|
| CB-001 PCI crosswalk §10.5 | 3/3 | Issue/PR | BL-2026-003 |
| New STD template: ASV scan evidence | 2/3 (narrow, but high value) | Issue with draft | BL-2026-008 |
```

### Step 5: Produce Quarterly Practice Review Report

```markdown
# Practice Review: Q{1-4} {YEAR}

## Engagement Summary
- Active engagements: {N}
- Completed handovers: {N}
- Average satisfaction: {X.X}/5
- Follow-on rate: {X%}

## Pattern Highlights
- What's working: {summary}
- What needs attention: {summary}

## Asset Recommendations
{asset table}

## Upstream Contribution Candidates
{candidate table}

## Backlog Status
- Open items: {N}
- Resolved this period: {N}
- Priority distribution: {High/M/L}
```

## Output Format
Report written to `practice-assets/reports/practice-review-Q{1-4}-{YEAR}.md`.

Backlog updates written to `practice-assets/trackers/backlog-taxonomy-v1.md`.

Upstream contribution candidates queued in `practice-assets/trackers/upstream-contribution-candidates-{YEAR}-Q{1-4}.md`.

## Validation Criteria
- [ ] All debrief documents in the archive are read (not a sample)
- [ ] Client profile register analysis uses all available records
- [ ] Each recommendation is backed by at least one debrief reference
- [ ] Upstream contribution candidates include rationale for each criterion
- [ ] Report follows the prescribed format
- [ ] No client-identifying information in the report or candidate documents
