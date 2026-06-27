# Sector Profile: Technology / SaaS
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 2 (Structure) — most SaaS companies have some existing security function but fragmented processes.

## Default Overlays
None mandatory at baseline. Voluntary: SOC 2 Type II, PCI DSS (if handling CHD), FedRAMP (if targeting US government).

## Regulatory Routing

| Trigger | Package |
|---|---|
| Handles CHD | `CERG-PLN-PCI-001` |
| Sells to US government | FedRAMP equivalent (practice-owned overlay) |
| Public company | `CERG-PLN-SOX-001` |
| EU customers with PII | `CERG-PLN-PRIV-001` |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{ORG_SECTOR}}` | "Technology / SaaS" |
| `{{REGULATORS}}` | SOC 2 alone does not count as a regulator; list only frameworks with external audit or assessment obligations |
| `{{SCALE_TIER}}` | Most SaaS security teams are `small` to `mid` regardless of total headcount; the security team-to-total-employee ratio is typically 1:50-1:100 |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for SaaS |
|---|---|---|
| MTTI (Mean Time to Identify) | MTR-001 DT-001 | SOC 2 Type II looks for timely detection indicators |
| Vulnerability SLA compliance | MTR-001 VM-001, VM-002 | Cloud attack surface changes daily; SLA compliance demonstrates control |
| Access recertification completion rate | MTR-001 AC-001 | Customer data protection is the product |
| Detection coverage (ATT&CK %) | MTR-001 DT-001 | Demonstrates proactive security posture to prospects |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| STD-IT-001 | Primary standard — cloud and SaaS environment is the entire infrastructure |
| STD-AC-001 | Identity is the new perimeter; MFA, SSO, SCIM are table stakes |
| PRC-TPRM-001 | SaaS clients have the most supply chain scrutiny from their own customers |
| PRC-VM-001 | Continuous scanning in ephemeral cloud environments |
| TMPL-SCP-001 | Per-system profiles help demonstrate security to enterprise prospects |

## Common Engagement Mistakes

- Over-investing in standards before the risk register is running (SaaS companies love frameworks; they need a running program first)
- Deferring access management because "we use SSO" — SSO is not access management (JML, recertification, privilege review still apply)
- Treating SOC 2 as a regulator rather than a output of a running program
