# Sector Profile: Cross-sector / Holding
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 3 or Tier 4. Holding companies span multiple regulators via subsidiaries. Central security function must support different compliance obligations simultaneously.

## Default Overlays
All that apply per subsidiary. Consolidated GRC evidence model is mandatory.

## Regulatory Routing

| Trigger | Package |
|---|---|
| Any subsidiary with SOX exposure | `CERG-PLN-SOX-001` (central or per-subsidiary register) |
| Any subsidiary with CUI/CMMC | `CERG-PLN-CUI-001` (per subsidiary) |
| Any subsidiary with PCI DSS | `CERG-PLN-PCI-001` |
| Any subsidiary with NERC-CIP | `CERG-PLN-CIP-001` |
| Any subsidiary with PII | `CERG-PLN-PRIV-001` |
| Any subsidiary with ISO 27001 | `CERG-PLN-ISO-001` + ISO refinement assets |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{ORG_NAME}}` | The holding company name, not a subsidiary |
| `{{REGULATORS}}` | Full consolidated list across all subsidiaries — this token may be a paragraph, not a short list |
| `{{SCALE_TIER}}` | Always "large" or "enterprise" — the central function is almost never small |
| `{{COG_NAME}}` | May differ per subsidiary (Sub A calls it "Cyber Council"; Sub B calls it "Security Steering Committee") |

## Operating Model Variants

The CERG operating model (OM-001) assumes a single organization. For holdings, three variants apply:

| Variant | Description | When to Use |
|---|---|---|
| Centralized | One security team serves all subsidiaries from a single CERG corpus | Subsidiaries are similar (e.g., all SaaS), share infrastructure, and accept common risk posture |
| Federated | Central team sets policy and standards; each subsidiary operates independently within guardrails | Subsidiaries have different regulators, risk appetites, or maturity levels |
| Hybrid | Central team handles shared services (SIEM, IdP, SOC, threat intel); subsidiaries own controls within their regulatory scope | Most common for large holdings — variations apply per domain |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| GOV-CMX-001 | Compliance matrix maps all subsidiary regulators to a single evidence library |
| GOV-OM-001 | Operating model variant selection (centralized/federated/hybrid) |
| RAC-001 | RACI must distinguish central from subsidiary accountability |
| TMPL-SCP-001 | Per-subsidiary or per-system profiles with regulatory scope designation |
| PRC-TPRM-001 | Third-party risk must account for shared services and subsidiary-specific vendors |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for Holdings |
|---|---|---|
| Regulatory coverage completeness (% of subsidiaries with documented CERG adoption) | CA-2 | Ensures no subsidiary is a coverage blind spot |
| Shared service control effectiveness | MTR-001 CB-001 | Shared IdP/SIEM failures affect all subsidiaries |
| Per-subsidiary maturity delta from central baseline | MTR-001 MAT-001 | Identifies which subsidiaries need support |
| Consistent evidence quality across subsidiaries | MTR-001 AUD-001 | Auditor review finds weakest evidence first |

## Common Engagement Mistakes

- Assuming one CERG corpus fits all subsidiaries (it can, if carefully tokenized and rendered per subsidiary; more likely each subsidiary needs a rendered variant)
- Centralizing everything (some controls must be subsidiary-owned: local access decisions, local risk acceptance, local regulatory reporting)
- Neglecting M&A integration (holdings acquire subsidiaries with varying maturity; CERG should have an acquisition integration procedure)
- Letting the strongest subsidiary set the policy for the weakest (or vice versa — the weakest subsidiary's control gaps create enterprise risk)
