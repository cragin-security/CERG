# Sector Profile: Energy / Utilities
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 3 (Compliance-to-Operations). Energy and utility organizations have regulatory obligations (NERC-CIP) that drive minimum Tier 3. Smaller municipal utilities may start at Tier 2 if they have no registered BES Cyber Systems.

## Default Overlays
NERC-CIP (`CERG-PLN-CIP-001`). BES overlay. OT Safety. Privacy for customer billing data.

## Regulatory Routing

| Trigger | Package |
|---|---|
| NERC-CIP registered entity | `CERG-PLN-CIP-001` |
| Operates OT/BES Cyber Systems | `CERG-STD-OT-001` + BES overlay |
| Handles customer PII (billing, usage data) | `CERG-PLN-PRIV-001` |
| State public utility commission oversight | Practice-owned state PUC guidance (not a CERG overlay; regulatory reporting varies by state) |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{REGULATORS}}` | NERC-CIP is the primary; state PUC may add consumer protection requirements |
| `{{IR_TEAM_NAME}}` | Energy sector IR is complicated by NERC-CIP CIP-008 reporting requirements — incident definition differs between cyber and grid operations |
| `{{EXEC_BODY_NAME}}` | Usually "Risk Committee" or "NERC Compliance Committee" — different from typical Cyber Oversight Group |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for Energy |
|---|---|---|
| BES asset inventory completeness | MTR-001 AM-001 | CIP-002 requires accurate categorization; miscategorization is a reportable finding |
| CIP-005 remote access review completion | MTR-001 AC-001 | Electronic access/perimeter review is a quarterly compliance activity |
| CIP-007 vulnerability SLA compliance | MTR-001 VM-001 | BES Cyber System patching has calendar-based deadlines |
| CIP-009 recovery test completion | MTR-001 CP-001 | 15-month test window; missed test is a compliance violation |
| OT device visibility | MTR-001 AM-001 | Passive OT discovery coverage; regulators increasingly ask about unknown devices |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| PLN-CIP-001 | The primary compliance overlay; maps each CIP requirement to CERG controls |
| STD-OT-001 | OT-specific security standard; includes BES vs. non-BES differentiation |
| STD-NET-001 | ESP/EAP boundaries are the core security architecture for BES environments |
| STD-CFG-001 (OT DISH variant) | BES Cyber System hardening baselines per CIP-010 |
| PRC-VM-001 OT annex | Passive scanning method, extended patch SLAs, CIP-007 deviation procedures |
| PRC-CHG-001 | CIP-010 baseline change management is a compliance requirement |

## Common Engagement Mistakes

- Treating all energy organizations as identical (a nuclear facility, a natural gas pipeline, and an electric co-op each have different regulatory regimes, not all NERC-CIP)
- Assuming NERC-CIP maturity means cybersecurity maturity (CIP compliance does not equal security posture; many CIP-compliant organizations have no detection engineering program)
- Over-segmenting the OT network to the point of operational impracticality (ESP/EAP with documented exceptions is better than a perfect design that operations bypasses)
- Forgetting the IT side (energy orgs focus heavily on OT/CIP but often have SOX exposure and billing PII that need separate attention)
