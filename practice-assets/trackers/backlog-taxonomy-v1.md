# Practice Backlog Taxonomy v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: Categorize engagement findings by type for pattern analysis

---

## Why a Taxonomy

Every engagement generates improvement feedback — gaps in the CERG corpus, missing practice assets, validator limitations, training needs. Without a taxonomy, this feedback lives in debrief documents and never becomes actionable. The taxonomy ensures every finding is categorized, tracked, and either resolved or escalated.

---

## Categories

### Validator Gap
The CERG corpus validator (`cerg-validate.py`) fails to catch a structural issue or produces a false positive that wastes client time.

| Subtype | Example | Resolution |
|---|---|---|
| Missing check | Validator passes but a broken link exists in a table of contents | Add check to validator |
| False positive | Validator flags a cross-reference that is valid but uses a different format | Adjust regex or exclusion list |
| Performance issue | Validator takes >30 seconds on a client corpus with 150+ docs | Optimize scanning scope |

### Template Omission
A practice or CERG template that should exist for a common client scenario does not exist.

| Subtype | Example | Resolution |
|---|---|---|
| Missing template | No template for collecting FedRAMP SSP evidence | Create template |
| Missing field | Risk register template does not include `risk_treatment_owner` | Add field |
| Incomplete instructions | Template lacks instructions for the client fill-in user | Add instructions section |

### Missing Overlay
A regulatory framework or industry sector lacks CERG coverage.

| Subtype | Example | Resolution |
|---|---|---|
| New regulator | Client needs FedRAMP coverage; no overlay exists | Build overlay (full or practice adapter) |
| New sector | Client is a new sector not in the sector profile catalog | Add sector profile |
| Partial coverage | Existing overlay covers 80% but misses key control | Patch overlay |

### Documentation Gap
An existing CERG document or practice asset is unclear, contradictory, or missing critical content.

| Subtype | Example | Resolution |
|---|---|---|
| Ambiguous language | PRC-VM-001 does not define "critical vulnerability" threshold | Clarify language in next review |
| Missing example | STD-AC-001 defines MFA requirements but gives no configuration example | Add example section |
| Outdated reference | Document references a retired framework version | Update crosswalk |

### Training Gap
A practitioner or client skill gap identified during engagement.

| Subtype | Example | Resolution |
|---|---|---|
| Practitioner knowledge gap | Practitioner cannot explain OT scanning limitations to client | Add module to onboarding |
| Client readiness gap | Client does not understand the difference between an SSP and an SCP | Add client-facing explainer |
| Methodology gap | Practice does not have a standard approach for ISA (Internal Security Assessor) support | Create methodology document |

### Practice Process Gap
A missing or inadequate practice operating procedure.

| Subtype | Example | Resolution |
|---|---|---|
| No intake process | Intake was ad hoc; missing client's regulatory burden until Week 3 | Build intake questionnaire (done: 4.1) |
| No handover standard | Handover was verbal; client confused about what they own | Build handover memo (done: 4.6) |
| No debrief process | Debrief not conducted; lessons lost | Build debrief protocol (done: 6.1) |

---

## Backlog Entry Format

```yaml
entry_id: BL-{YYYY}-{NNN}
date: {YYYY-MM-DD}
source: {engagement_id | practice_review | client_feedback}
category: {validator_gap | template_omission | missing_overlay | documentation_gap | training_gap | practice_process_gap}
subtype: {as_above}
severity: {critical | high | medium | low}
description: "Clear description of the gap"
impact: "What happens if this is not resolved"
resolution: "What needs to be built, fixed, or learned"
owner: {name}
target: {YYYY-MM-DD | TBD}
status: {open | in_progress | resolved | wont_fix}
```

---

## Backlog Review Cadence

| Event | Frequency | Who |
|---|---|---|
| New entries added | On debrief completion or discovery | Engagement Lead |
| Priority review | Monthly | Practice Principal |
| Backlog grooming | Quarterly | Practice team |
| Upstream contribution selection | Quarterly | Practice Principal |
