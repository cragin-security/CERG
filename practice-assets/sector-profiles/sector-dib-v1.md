# Sector Profile: Defense Industrial Base
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 3 (Compliance-to-Operations). CMMC certification or CUI handling obligation drives the tier. Smaller DIB subcontractors may enter at Tier 2 if they have no CUI scope (rare).

## Default Overlays
CUI/CMMC (`CERG-PLN-CUI-001`). IR adjacent.

## Regulatory Routing

| Trigger | Package |
|---|---|
| Handles CUI per DFARS 252.204-7012 | `CERG-PLN-CUI-001` |
| Pursuing CMMC certification (L2 or L1) | `CERG-PLN-CUI-001` — CMMC L2 = CUI baseline + 110+ practices |
| SPRS score reporting required | `CERG-PLN-CUI-001` §8 (POA&M scoring methodology) |
| ITAR-controlled data | Practice-owned ITAR guidance (supplements STD-CUI-001 with export control requirements) |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{ORG_SECTOR}}` | "Defense Industrial Base" — if the client builds military hardware, software, or provides services to DoD |
| `{{REGULATORS}}` | DoD/CMMC is primary; state PUC if energy DIB; ITAR/DDTC if exporting defense articles |
| `{{PRIMARY_REGULATOR}}` | CMMC (nearing assessment) or DFARS (contractual flow-down) |
| `{{SCALE_TIER}}` | DIB subcontractors are frequently small/mid companies that hold CUI; do not estimate Tier 1 just because team is small |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for DIB |
|---|---|---|
| CUI system scope accuracy | MTR-001 AM-001 | Scope errors cause CMMC assessment failures |
| POA&M closure rate | MTR-001 RM-001 | SPRS score is directly affected by open POA&Ms |
| CUI incident notification timeline | PRC-IR-002 | DFARS requires contractor-to-CO notification within 72 hours of suspected breach |
| Training completion rate (CUI handling) | MTR-001 AT-001 | CMMC AT.L2-3.2.2 requires annual training |
| SSP review cycle currency | MTR-001 CA-001 | SSP must be current per CMMC CA.L2-3.12.1 |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| PLN-CUI-001 | The primary compliance package; covers CMMC POA&M, SSP requirements |
| STD-CUI-001 | Maps to CMMC L2 practice requirements across 14 domains |
| STD-CFG-001 (DISH) | Hardening baselines under CMMC CM domain |
| PRC-AUD-001 | Audit and evidence management for CMMC assessment readiness |
| STD-AC-001 | Access control for CUI enclaves; CMMC AC domain is the largest |
| PRC-TPRM-001 | Subcontractor CUI flow-down and supply chain requirements |

## Common Engagement Mistakes

- Over-preparing for CMMC L2 (the standard is rigorous but achievable; the biggest failure mode is scope creep — defining too many systems as CUI-in-scope and drowning in control implementation)
- Treating CMMC as a checklist rather than an operating model (CMMC assessments test operating effectiveness, not just design — evidence must be current, not assembled the week before)
- Ignoring the SPRS score (many DIB contractors do not know their current SPRS score; assessing it is the first step)
- Not involving legal in CUI scope determination (whether data is CUI is a legal/contractual determination, not a security decision)
