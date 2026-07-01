# FedRAMP / DoD SRG Overlay Assessment v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: Gap analysis and build recommendation

---

## Executive Summary

**Recommendation:** DO NOT BUILD a standalone FedRAMP operational package. Instead, provide a FedRAMP overlay pattern within the existing CB-001 framework using the High-Impact baseline + FedRAMP-specific augmentations.

**Rationale:** FedRAMP maps to NIST 800-53 controls. CERG's control baseline (CB-001) is already organized by NIST 800-53 families and carries a High-Impact overlay. FedRAMP is a scope + documentation overlay on top of the High-Impact baseline — it does not introduce new control families that CERG does not address. A standalone FedRAMP package would duplicate the baseline.

---

## FedRAMP Requirements vs. CERG Coverage

### Assessment Criteria

FedRAMP applies to cloud service offerings (CSOs) seeking a FedRAMP authorization (JAB, Agency, or FedRAMP Equivalent). The control baseline is NIST 800-53 Rev 5 (Low / Moderate / High), plus FedRAMP-specific enhancements:

| FedRAMP Requirement | CERG Coverage | Gap |
|---|---|---|
| NIST 800-53 High baseline controls | Covered by CB-001 §6 (core baseline) + §8 High-Impact overlay | No gap — CERG's High-Impact overlay selects the High baseline parameters |
| FedRAMP-specific control enhancements (e.g., AC-2(1), AC-2(2), AC-6(1), AC-6(5)) | CB-001 controls are written at the base level; enhancements are in subordinate standards | Partial — enhancements need documentation in a FedRAMP appendix to relevant standards |
| System Security Plan (SSP) per FedRAMP template | CERG has PLN-CUI-001 SSP template; FedRAMP has its own SSP template with different sections | Significant — FedRAMP SSP template is prescriptive and US government–specific |
| Continuous monitoring program (ConMon) per FedRAMP ISSO requirements | CERG has PM-14, CA-2, CAL-001; FedRAMP ConMon has specific monthly/quarterly/annual evidence submission requirements | Partial — cadence and evidence format differ from CERG baseline |
| Incident reporting to US-CERT within 1 hour (for High) or 4 hours (for Moderate) | CERG IR-4, IR-8 carry standard notification timelines; FedRAMP has specific external reporting requirements | Gap — CERG incident response docs do not reference US-CERT notification SLAs |
| Third-party assessment organization (3PAO) interface | CERG has PRC-AUD-001 for audit management; FedRAMP 3PAO process is more structured with Readiness Assessment Report (RAR) and SAR | Partial — process documentation needs FedRAMP-specific annex |
| Authorization boundary definition | CERG has SC-7 (boundary protection) and assumes well-defined system boundaries | Partial — FedRAMP requires explicit boundary documentation in the SSP with data-flow diagrams |
| FedRAMP Identity and Access Management requirements (PIV / CAC integration) | CERG has IA-2, IA-3, AC-3 with MFA requirements; PIV/CAC is an implementation detail | No gap — CERG is technology-agnostic; PIV/CAC is implementation |

### Gap Classification

| Category | Gaps | Build Decision |
|---|---|---|
| No gap | 2 | No action |
| Partial gap | 5 | FedRAMP overlay annex in existing CERG standards |
| Significant gap | 1 (FedRAMP SSP template) | Practice-owned FedRAMP SSP adapter (not a new CERG document) |

---

## Build vs. Defer Decision

| Option | Effort | Value | Decision |
|---|---|---|---|
| Building a FedRAMP overlay package (e.g., a practice-run set of augmentations for the CB-001 High-Impact baseline) carries... | High — 2+ weeks (FedRAMP SSP template, ConMon schedule, 3PAO interface) | High — FedRAMP is a frequent consulting need (SaaS → FedRAMP path) | Defer — high value but high effort; build only when first FedRAMP client engagement is confirmed |
| Provide FedRAMP overlay annex in CB-001 + practice adapter for SSP | Medium — 1 week | High | RECOMMENDED — captures the gap without over-investing before client demand is confirmed |
| Defer entirely | None | None | Acceptable only if no FedRAMP client pipeline |

**Decision:** RECOMMEND — Prefer FedRAMP overlay annex in CB-001 §8 and a practice-owned SSP adapter (not a new CERG document). Build the full operational package when the first FedRAMP client engagement is signed.

---

## Recommended Action Plan

| Step | Action | Owner | Effort | Trigger |
|---|---|---|---|---|
| 1 | Add FedRAMP row to CB-001 §8 overlay matrix (references NIST 800-53 High baseline + US-CERT notification) | Governance | 2 hours | Next CB-001 review cycle |
| 2 | Create practice-owned FedRAMP SSP adapter: FedRAMP SSP template sections → CERG control evidence mapping | Practice | 1 day | On first FedRAMP client engagement |
| 3 | Add US-CERT notification SLAs to PLN-IR-001 annex or practice IR supplement | Risk / Practice | 4 hours | On first FedRAMP client engagement |
| 4 | Build the FedRAMP package (full overlay in the client repo) | Governance | 2 weeks | On second FedRAMP client engagement or client-funded build |

---

## Related Overlays

| Overlay | Relationship to FedRAMP |
|---|---|
| CUI / CMMC | FedRAMP + CUI is common for FedRAMP High systems handling CUI |
| ISO 27001 | FedRAMP Equivalent pathway can use ISO 27001 certification as baseline |
| PCI DSS | FedRAMP + PCI for cloud payment systems |
