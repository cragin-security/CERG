# ISO 27001 / ISMS Overlay Refinement v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: Consulting delivery refinement for upstream CERG-PLN-ISO-001

---

## Executive Summary

**Recommendation:** REFINE upstream PLN-ISO-001 for consulting delivery. Upstream has the operational package skeleton but it needs: ISMS scope definition framework, Statement of Applicability (SOA) production workflow, internal audit program interface, and certification body interaction model.

**Rationale:** ISO 27001 is a certification audit, not a self-assessment. The consulting value is helping clients prepare for certification body (CB) audits with the right evidence structure, internal audit cadence, and SOA completeness. Upstream PLN-ISO-001 covers the controls but not the certification pathway.

---

## Current State Assessment

### What Upstream Already Provides

| Asset | Status | Consulting Readiness |
|---|---|---|
| PLN-ISO-001 operational package | Exists | Needs refinement for CB readiness |
| CB-001 control baseline (ISO 27001 A.5–A.8 mapped) | Exists | ISO Annex A controls are mapped to CERG controls |
| Evidence catalog per CB-001 §9 | Exists | ISO wants specific evidence naming (SOA control → evidence reference) |
| Internal audit procedure (PRC-AUD-001) | Exists | Generic audit procedure, not ISO-specific |
| Maturity assessment (MAT-001) | Exists | Not aligned to ISO 27001 maturity scoring (does not map to "Not Implemented → Partially → Largely → Fully → Continuous") |

### Gaps for Consulting Delivery

| Gap | Impact | Effort to Close |
|---|---|---|
| No ISMS scope definition framework | Client cannot articulate ISMS boundary for Stage 1 audit | 1 day |
| No SOA production workflow | SOA is the core ISO deliverable; client must map assets → threats → Annex A controls → applicability → implementation → evidence | 2-3 days |
| Internal audit program not ISO-aligned | Stage 2 audit requires 12 months of internal audit records with specific finding taxonomy | 1 day |
| Certification body interaction model unclear | Client does not know what to expect in Stage 1, Stage 2, and surveillance visits | 4 hours |
| Evidence naming convention not ISO-compatible | ISO auditors expect evidence to reference the Annex A control, not the CERG control ID | 4 hours |
| No surveillance cycle management | After certification, client needs annual surveillance visit planning | 2 hours |

---

## Refinement Plan

### What Gets Built

| Asset | Type | Location |
|---|---|---|
| ISMS Scope Definition Framework | Practice-owned | `practice-assets/templates/iso-scope-framework-v1.md` |
| SOA Production Workflow + Template | Practice-owned | `practice-assets/templates/iso-soa-v1.md` |
| ISO Internal Audit Program Template | Practice-owned | `practice-assets/templates/iso-internal-audit-program-v1.md` |
| Certification Body Interaction Guide | Practice-owned | `practice-assets/sector-profiles/iso-cert-body-guide-v1.md` |
| CB-001 Annex A Crosswalk Refinement | CERG corpus update | CB-001 §10.6 (ISO 27001:2022 Annex A crosswalk) |

### What Gets Refined (Upstream CERG Changes)

| Change | Document | Effort |
|---|---|---|
| Add ISO 27001 crosswalk to CB-001 §10 | CB-001 | 2 hours |
| Add ISO surveillance cycle to CAL-001 (optional) | CAL-001 | 30 min |
| Update TRC-001 to include ISO Annex A control-to-evidence mapping | TRC-001 | 4 hours (significant) |

### What Gets Deferred

| Item | Reason |
|---|---|
| Full ISO 27001:2022 rewrite of CB-001 | CB-001 is NIST-organized by design; ISO mapping belongs in crosswalks, not baseline restructuring |
| Standalone ISO internal audit procedure | PRC-AUD-001 exists; ISO-aligned annex is sufficient |
| ISO-specific evidence library | CERG evidence catalog is framework-agnostic; ISO evidence naming is a label, not a structural change |

---

## Recommended Action Plan

| Step | Action | Owner | Effort | Trigger |
|---|---|---|---|---|
| 1 | Create ISMS scope definition framework | Practice | 1 day | Before first ISO consulting engagement |
| 2 | Create ISO SOA production workflow + template | Practice | 2-3 days | Before first ISO consulting engagement |
| 3 | Create ISO-aligned internal audit program template | Practice | 1 day | Before first ISO consulting engagement |
| 4 | Create certification body interaction guide | Practice | 4 hours | Before first ISO consulting engagement |
| 5 | Add ISO 27001 Annex A crosswalk to CB-001 §10 | Governance | 2 hours | Next CB-001 update cycle |
| 6 | Update CON-001 overlay selection for ISO | Governance | 30 min | After CB-001 crosswalk added |

**Decision:** REFINE — Build the four practice-owned assets first, then update CB-001 crosswalk. Defer full corpus restructure.

---

## ISO 27001:2022 vs. CERG Overlay Pattern

| ISO Annex A Control | CERG CB-001 Control | Status |
|---|---|---|
| A.5 Information Security Policies | PL-1, PM-1 | ✓ Covered |
| A.6 Organization of Information Security | OM-001, RAC-001, FLOW-001 | ✓ Covered |
| A.7 Human Resource Security | PS-2, AT-2, ONB-001, TRN-001 | ✓ Covered |
| A.8 Asset Management | CM-8, AM-001, DG-001 | ✓ Covered |
| A.9 Access Control | AC-2 through AC-19, IA-2, IA-5 | ✓ Covered |
| A.10 Cryptography | SC-8, SC-28, CR-001 | ✓ Covered |
| A.11 Physical and Environmental Security | PE-2, PE-3 | ✓ Covered |
| A.12 Operations Security | CM-3, CM-6, AU-2, SI-2, SI-4, PRC-CHG-001 | ✓ Covered |
| A.13 Communications Security | SC-7, SC-8, NET-001 | ✓ Covered |
| A.14 System Acquisition, Development and Maintenance | SA-9, SDL-001, TM-001 | ✓ Covered |
| A.15 Supplier Relationships | SR-2, SR-3, PRC-TPRM-001 | ✓ Covered |
| A.16 Incident Management | IR-4, IR-8, PRC-IR-002 | ✓ Covered |
| A.17 Information Security Aspects of Business Continuity | CP-2, CP-4, CP-9, CP-10, RES-001 | ✓ Covered |
| A.18 Compliance | CA-2, PL-1, CMX-001, AUD-001 | ✓ Covered |

All 14 ISO 27001:2022 Annex A control clauses are covered by existing CERG controls. The gap is not control coverage — it is certification readiness: SOA, ISMS scope, internal audit program, and CB interaction.
