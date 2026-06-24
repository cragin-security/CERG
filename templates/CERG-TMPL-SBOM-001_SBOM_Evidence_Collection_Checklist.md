## SBOM Evidence Collection Checklist
### Audit-Ready Artifacts for Software Supply Chain

---
| | |
|---|---|
| **Document ID** | CERG-TMPL-SBOM-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Vendor Risk Analyst |
| **Parent Document** | [CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) §11 |
| **Supporting Schema** | `machine-readable/cerg-sbom-schema.yaml` |
| **Review Cycle** | Annual / On SBOM process change |
| **Frameworks** | NIST 800-161r1 · NTIA SBOM · EO 14028 · CSA CCM · NIST 800-53 SR |
| **Regulations** | NERC-CIP CIP-013 · CMMC SR.L2 · SOX ITGC · FedRAMP |
| **Environments** | All vendor software deliveries; internal production builds |

---

## Purpose
Standardizes SBOM evidence collection for vendor-delivered software and internally-built artifacts. Supports CIP-013, CMMC SR.L2, EO 14028, and SOX ITGC evidence requirements.

---

## Evidence by SBOM Source

### Vendor-Delivered SBOM (T1/T2/T3 Software Vendors)
| **Artifact** | **Source** | **Frequency** | **CIP-013** | **CMMC** | **SOX** | **Notes** |
|---|---|---|---|---|---|---|
| SBOM file (CycloneDX/SPDX) | Vendor TPRM portal | Per delivery + material update | ✓ | ✓ | | Validate format on receipt |
| SBOM vulnerability scan report | Scanner (Grype/Trivy/OSV) | On receipt + quarterly (T1/T2) | ✓ | ✓ | | Findings → PRC-VM-001 |
| VEX statements for Critical/High | Vendor | Per finding | ✓ | ✓ | | `vex_status` in registry |
| License scan report | Scanner (FOSSA/Scanner) | Per delivery | | | ✓ | Flag GPL/AGPL in proprietary |
| Embedded secrets scan report | Scanner (TruffleHog/Gitleaks) | Per delivery | ✓ | | | Fail if secrets found |
| Signature verification log | Cosign / vendor key | Per delivery | ✓ | | | Verify SBOM authenticity |

### Internal Build SBOM (CI/CD Generated)
| **Artifact** | **Source** | **Frequency** | **CIP-013** | **CMMC** | **SOX** | **Notes** |
|---|---|---|---|---|---|---|
| CycloneDX SBOM artifact | CI pipeline (Syft) | Every production build | ✓ | ✓ | ✓ | Signed, in artifact registry |
| Pipeline vulnerability scan log | CI pipeline (Grype/Trivy) | Every production build | ✓ | ✓ | ✓ | Gate: fail on Critical/High |
| VEX for accepted findings | Developer / Risk | Per finding | ✓ | ✓ | | Documented risk acceptance |
| License compliance report | CI pipeline (license-checker) | Every production build | | | ✓ | Policy gate |
| Secrets scan log | CI pipeline (TruffleHog) | Every production build | ✓ | | ✓ | Gate: fail on any secret |
| SBOM registry record | `machine-readable/cerg-sbom-schema.yaml` | Auto on pipeline success | ✓ | ✓ | | `approval_status = approved` |

### Registry & Reporting
| **Artifact** | **Source** | **Frequency** | **CIP-013** | **CMMC** | **SOX** | **Notes** |
|---|---|---|---|---|---|---|
| SBOM registry export (all records) | SBOM registry / machine-readable | Quarterly | ✓ | ✓ | ✓ | For auditor review |
| Stale SBOM report (>90 days no scan) | SBOM registry query | Monthly | ✓ | | | Triggers re-scan |
| Critical component inventory (log4j, spring, openssl, etc.) | SBOM registry query | Monthly | ✓ | ✓ | | Rapid response to 0-days |

---

## Collection Workflow
1. **Vendor intake:** TPRM requires SBOM at onboarding (T1/T2/T3 software)
2. **Delivery:** Vendor uploads to TPRM portal → auto-validated for format
3. **Scan:** Risk runs vulnerability + license + secrets scans → findings registered
4. **VEX:** Vendor provides VEX for Critical/High within 10 business days
5. **Approve:** Governance sets `approval_status` → evidence linked in TPRM tool
6. **Internal builds:** CI pipeline auto-generates, scans, signs, publishes SBOM
7. **Quarterly audit:** Governance pulls registry export → evidence library

---

## Document Control
| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-SBOM-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Vendor Risk Analyst |
| **Approved By** | CISO |
| **Effective Date** | 2026-06-17 |
| **Review Cycle** | Annual / On SBOM process change |
| **Next Scheduled Review** | 2027-06-17 |

### Revision History
| Version | Date | Author | Change Summary |
|---|---|---|---|
| 1.0 | 2026-06-17 | Cyber Governance | Initial release - SBOM evidence collection checklist |

### Related Documents
| Document | ID | Relationship |
|---|---|---|
| Third-Party Supply Chain Risk Procedure | CERG-PRC-TPRM-001 | Governing procedure §11 |
| SBOM Record Schema | machine-readable/cerg-sbom-schema.yaml | Machine-readable record format |
| Exposure Management Procedure | CERG-PRC-VM-001 | SBOM findings pipeline |
| Secure Configuration Baseline (DISH) | CERG-STD-CFG-001 | Container image signing gate §7 |
| CI/CD SBOM Generation Script | tools/sbom-generate.sh | Pipeline implementation |
