# Sector Profile: Manufacturing / OT
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 2 or Tier 3 depending on OT regulatory burden. Pure manufacturing IT (no OT connection to safety systems) is Tier 2. OT-connected to industrial control systems is Tier 3.

## Default Overlays
OT Safety (carried by `CERG-STD-OT-001`). BES overlay if grid-connected. Privacy if handling PII in HR/ERP.

## Regulatory Routing

| Trigger | Package |
|---|---|
| OT systems connected to IT network | `CERG-STD-OT-001` (OT Safety overlay) |
| Grid-connected (BES Cyber System) | `CERG-PLN-CIP-001` |
| ISO 9001 / TS 16949 | Not a direct CERG overlay; refer to ISO refinement |
| Export controls (ITAR/EAR) | Practice-owned export control guidance + STD-CUI-001 for CUI scope |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{ORG_SECTOR}}` | Be specific: Aerospace, Automotive, Chemical, Pharma mfg, Food processing, etc. — each has different safety implications |
| `{{PROTECTED_POPULATION}}` | Must include OT device count (PLCs, RTUs, HMIs, historians, engineering workstations) |
| `{{ENG_STAFF}}` | OT security engineers are distinct from IT security engineers; if the client has neither, note the gap |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for Mfg |
|---|---|---|
| OT device inventory completeness | MTR-001 AM-001 | Most OT environments have 40-60% visibility; blind spots are safety risk |
| Segmentation violation count | MTR-001 NM-001 | IT → OT traffic is the primary attack path for ransomware |
| OT vulnerability SLA compliance | MTR-001 VM-001 | Patching window constraints mean SLAs must be risk-based, not CVSS-based |
| Change management compliance (OT) | MTR-001 CH-001 | Unauthorized PLC logic changes can cause physical damage |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| STD-OT-001 | The primary standard for OT environments; includes the visibility decision matrix |
| STD-NET-001 | Network segmentation between IT/OT and between OT zones is the most important control |
| PRC-CHG-001 | OT change control is stricter than IT — plant-floor changes have safety implications |
| PRC-VM-001 | OT vulnerability management uses passive scanning; SLAs differ from IT |
| STD-CFG-001 (OT DISH variant) | OT hardening baselines are platform-specific; standard IT baselines can break OT |

## Common Engagement Mistakes

- Applying IT scanning to OT networks (active scanning can disrupt PLCs; use passive or supervised methods)
- Treating the plant floor as one zone (Purdue model: Level 0-4 should be segregated)
- Ignoring engineering workstations as an attack path (ransomware starts at the engineer's desk, not the PLC)
- Assuming OT devices have the same logging capabilities as IT (many do not; compensate with network-level monitoring)
