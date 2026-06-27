# Sector Profile: Healthcare / Life Sciences
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 3 (Compliance-to-Operations) — HIPAA/HITRUST obligations plus clinical trial CUI drive regulatory scope.

## Default Overlays
Privacy (`CERG-PLN-PRIV-001`). CUI if handling clinical trial data or working with federal research partners.

## Regulatory Routing

| Trigger | Package |
|---|---|
| Handles PHI (HIPAA covered entity or business associate) | Practice HIPAA gap kit + `PLN-PRIV-001` |
| Pursuing HITRUST certification | Practice HITRUST crosswalk adapter |
| Clinical trial data (CUI) | `CERG-PLN-CUI-001` |
| EU patient data (GDPR + HIPAA) | `CERG-PLN-PRIV-001` + GDPR-specific controls in HIPAA gap kit |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{ORG_SECTOR}}` | Differentiate: Healthcare (patient care delivery) vs. Life Sciences (research, pharma, devices) |
| `{{REGULATORS}}` | HIPAA is not a single regulator — OCR enforces; Medicare/Medicaid conditions of participation add another layer |
| `{{IR_TEAM_NAME}}` | Healthcare IR is adjacent to patient safety incident reporting — clarify boundaries |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for HC |
|---|---|---|
| PHI access recertification completion | MTR-001 AC-001 | HIPAA Security Rule requires periodic access review for ePHI |
| Breach notification timeline | PRC-IR-002 | 60-day HHS notification clock; OCR tracks timeliness |
| Vendor risk assessment completion | MTR-001 TPRM-001 | Business associate agreements are a compliance requirement |
| Encryption coverage (data at rest + in transit) | MTR-001 CR-001 | HIPAA encryption addressable; auditors expect it |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| PLN-PRIV-001 | Privacy overlay covers PHI handling requirements at the policy level |
| STD-CUI-001 | Maps directly to HIPAA Security Rule for clinical research environments |
| PRC-TPRM-001 | Business Associate agreements flow through TPRM; HIPAA BA requirements are stricter than standard CERG TPRM |
| STD-AC-001 | Access controls for EHR/EMR systems are the most-tested control in HIPAA assessments |
| PRC-AUD-001 | HITRUSH assessments and internal audit programs need structured evidence |

## Common Engagement Mistakes

- Confusing HIPAA Security Rule (technical controls) with HIPAA Privacy Rule (policy/process) — CERG covers the former well; the latter requires legal input
- Treating all PHI as the same sensitivity level — patient treatment data ≠ clinical trial data ≠ de-identified data; different controls apply
- Underestimating vendor risk — healthcare clients typically have 3-5x more vendors than equivalent-sized tech companies (CROs, EMR vendors, labs, billing, telehealth)
- Not differentiating between a hospital system (IT + OT + clinical engineering) and a health tech startup (cloud only)
