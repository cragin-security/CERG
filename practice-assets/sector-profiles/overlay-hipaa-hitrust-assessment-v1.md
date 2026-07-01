# HIPAA / HITRUST Overlay Assessment v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: Gap analysis and build recommendation

---

## Executive Summary

**Recommendation:** DO NOT BUILD a standalone HITRUST or HIPAA operational package. Instead, route through the CUI overlay (for HIPAA Security Rule) or the existing Privacy overlay (for HIPAA Privacy Rule + Breach Notification). For HITRUST, provide a practice-owned crosswalk adapter.

**Rationale:** HIPAA Security Rule maps to NIST 800-53 controls covered by CERG's CUI overlay (STD-CUI-001). HIPAA Privacy Rule and Breach Notification are addressed by the Privacy overlay (PLN-PRIV-001). HITRUST CSF is a meta-framework overlay on NIST/ISO — the practice should maintain a crosswalk adapter rather than a standalone operational package.

---

## HIPAA Requirements vs. CERG Coverage

### HIPAA Security Rule (45 CFR §164.308–312)

| HIPAA Standard | CERG Coverage | Gap |
|---|---|---|
| Security Management Process (164.308(a)(1)) — risk analysis, risk management, sanction policy | RA-3, PM-9, PRC-RM-001 | No gap — CERG risk management framework covers this |
| Assigned Security Responsibility (164.308(a)(2)) | OM-001, RAC-001 | No gap — CERG operating model names security roles |
| Workforce Security (164.308(a)(3)) — authorization, supervision, clearance, termination | AC-2, PS-2, ONB-001 | No gap — CERG access management and onboarding cover this |
| Information Access Management (164.308(a)(4)) — access authorization, establishment, modification | AC-2, AC-3, AC-6, PRC-AC-002 | No gap |
| Security Awareness and Training (164.308(a)(5)) | AT-2, TRN-001 | Partial — CERG training framework exists but HIPAA-specific content (PHI handling, breach reporting obligations) needs inclusion |
| Security Incident Procedures (164.308(a)(6)) — response, reporting, escalation | IR-4, IR-8 | Partial — HIPAA breach notification to HHS (60 days) and affected individuals (without unreasonable delay) needs specific reference |
| Contingency Plan (164.308(a)(7)) — data backup, disaster recovery, emergency mode, testing | CP-2, CP-4, CP-9, CP-10, RES-001 | No gap |
| Evaluation (164.308(a)(8)) — periodic technical and non-technical evaluation | CA-2, MAT-001 | No gap |
| Business Associate Contracts (164.308(b)(1)) | SR-2, SR-3, PRC-TPRM-001 | Partial — CERG TPRM covers vendor risk but HIPAA BA agreements have specific content requirements (breach notification, access, return/destruction of PHI) |
| Access Controls (164.312(a)(1)) — unique user ID, emergency access, automatic logoff, encryption and decryption | AC-2, AC-3, IA-2, IA-5 | No gap |
| Audit Controls (164.312(b)) — hardware, software, and procedural mechanisms | AU-2, AU-12, LM-001 | No gap |
| Integrity Controls (164.312(c)(1)) | SI-7 (covered by STD-LM-001 file integrity monitoring) | No gap |
| Person or Entity Authentication (164.312(d)) | IA-2, IA-3 | No gap |
| Transmission Security (164.312(e)(1)) — integrity controls, encryption | SC-8, CR-001 | No gap |
| Accountability / BA Agreements (164.314) | PRC-TPRM-001 | Partial (see above) |
| Group Health Plan (164.316) — policies and procedures documentation | PL-1 | No gap |

### HIPAA Breach Notification Rule (45 CFR §164.400–414)

| Requirement | CERG Coverage | Gap |
|---|---|---|
| Breach notification to affected individuals without unreasonable delay (max 60 days) | IR-4, IR-8 | Gap — CERG IR docs do not name specific regulatory notification SLAs for HIPAA |
| Breach notification to HHS (60 days for 500+ individuals; annual for smaller) | IR-4 | Gap — same as above |
| Breach notification to media (500+ individuals in same state/jurisdiction) | IR-4 | Gap — CERG does not differentiate media notification triggers |

### HIPAA Privacy Rule (45 CFR §164.500–534)

The Privacy Rule (uses and disclosures of PHI, minimum necessary, patient rights) is largely a policy and procedure matter, not a technical control. CERG's Privacy Operational Package (PLN-PRIV-001) covers these requirements at the policy level. No significant technical control gap.

---

## HITRUST CSF vs. CERG Coverage

HITRUST CSF is a certifiable risk-based framework that overlays multiple standards (NIST, ISO, HIPAA, PCI). Version 11 covers 49 control categories across 19 domains.

| HITRUST Requirement | CERG Coverage | Gap |
|---|---|---|
| NIST 800-53-derived controls | Full — CERG baseline is NIST 800-53 | No gap |
| ISO 27001-derived controls | Partial — CERG has PLN-ISO-001 but HITRUST ISO controls may have different parameters | Minor — can be addressed via crosswalk |
| HITRUST-specific control parameters | CB-001 baseline has some, not all | Moderate — certain HITRUST-specific maturity indicators (M, S, C scores) do not have a direct CERG equivalent |

**HITRUST Recommendation:** Practice-owned crosswalk adapter only. Do not build a dedicated operational package. The crosswalk maps HITRUST CSF control references to CERG controls, HITRUST maturity indicators to CERG's MAT-001 scoring, and HITRUST assessment evidence to CERG's evidence catalog.

---

## Gap Summary

| Gap Area | Severity | Resolution | Effort |
|---|---|---|---|
| HIPAA-specific security awareness content | Low | Add HIPAA content module to TRN-001 / awareness program | 1 day |
| HIPAA breach notification SLAs in IR docs | Medium | Add breach notification appendix to practice IR template (not CERG corpus) | 4 hours |
| Business Associate agreement content in TPRM | Low | Add HIPAA BA template to TPRM template annex | 1 day |
| HITRUST CSF crosswalk | Low | Practice-owned crosswalk spreadsheet | 1 day |

---

## Build vs. Defer Decision

| Option | Effort | Value | Decision |
|---|---|---|---|
| building a standalone HIPAA operational package | High — 2 weeks | Moderate — HIPAA is well-covered by existing CUI + Privacy overlays | DO NOT BUILD — existing overlays cover 90%+ of HIPAA Security Rule |
| Practice-owned HIPAA/HITRUST gap kit | Low — 1-2 days | High — enables consulting engagements without CERG corpus churn | **RECOMMENDED** — contains BA agreement template, breach notification appendix, HITRUST crosswalk, security awareness module |
| Defer entirely | None | None | Acceptable if no healthcare client pipeline |

**Decision:** RECOMMEND — Practice-owned HIPAA/HITRUST gap kit (not a CERG corpus document). Route clients through existing CUI overlay + Privacy overlay + practice gap kit.

---

## Recommended Action Plan

| Step | Action | Owner | Effort | Trigger |
|---|---|---|---|---|
| 1 | Create practice HIPAA gap kit: BA agreement template, breach notification appendix, HITRUST crosswalk | Practice | 1-2 days | On first healthcare client engagement |
| 2 | Update CON-001 sector overlay matrix: add Healthcare → PLN-PRIV-001 + STD-CUI-001 + HIPAA gap kit | Practice | 1 hour | After gap kit created |
| 3 | Add HIPAA-specific notification SLAs to practice incident response supplement | Practice | 4 hours | After gap kit created |
