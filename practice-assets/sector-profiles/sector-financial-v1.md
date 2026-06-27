# Sector Profile: Financial Services
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 3 (Compliance-to-Operations) — most financial services organizations have regulatory obligations that drive the engagement tier regardless of team size.

## Default Overlays
SOX ITGC (`CERG-PLN-SOX-001`). PCI DSS if handling CHD. Privacy if handling PII.

## Regulatory Routing

| Trigger | Package |
|---|---|
| US publicly traded company | `CERG-PLN-SOX-001` |
| Handles CHD | `CERG-PLN-PCI-001` |
| EU operations | `CERG-PLN-PRIV-001` |
| US cross-sector holding | Multi-regulator: SOX + PCI + Privacy |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{REGULATORS}}` | List every regulator the client's legal team has confirmed; financial services is the most audit-dense sector |
| `{{EXEC_BODY_NAME}}` | Usually "Audit Committee" (different from "Board of Directors" — confirm with client) |
| `{{CERG_TEAM_SIZE}}` | Typically larger than other sectors for equivalent headcount; FS hires security early |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for FS |
|---|---|---|
| Access recertification completion rate | MTR-001 AC-001 | SOX ITGC AX-03 requires quarterly recert |
| SoD conflict resolution time | MTR-001 AC-001 | Segregation of duties is a regulatory requirement, not a best practice |
| Change management violation rate | MTR-001 CH-001 | Unauthorized production changes are material to financial reporting |
| Vulnerability SLA compliance | MTR-001 VM-001 | OCC / FDIC expectations for timely remediation |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| PLN-SOX-001 | The primary compliance overlay; SOC 1 reuse procedure is particularly valuable |
| STD-AC-001 | Access management is the most-audited control family in FS |
| PRC-AC-002 | JML runbook must be precise; auditors test provisioning/termination samples |
| PRC-VM-001 | FS clients have the tightest patch SLAs (critical within 48 hours at some institutions) |
| STD-RES-001 | BCP/IR is board-level concern; regulators test recovery |

## Common Engagement Mistakes

- Treating SOX as a separate compliance program rather than a scope filter over CERG controls
- Over-engineering access management with tools before the process is defined
- Assuming all FS clients are the same — a credit union's risk profile is very different from an investment bank's
- Neglecting the IR to BCP handoff (FS clients need to show continuity plan integration)
