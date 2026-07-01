# CERG Remediation Roadmap Template v1

**Purpose:** Structured plan for closing control gaps, organized by priority and effort.
**Target audience:** Client IT/Security team — the people doing the work.

---

## 1. Roadmap Overview

| Phase | Timeline | Focus | Controls | Owner |
|-------|----------|-------|----------|-------|
| Quick Wins | Week 1-2 | Policies, MFA, basic logging | 10 controls | Client IT / MSP |
| Foundation | Weeks 3-6 | Access control, backup, patching | 25 controls | Client IT + CERG |
| Structure | Weeks 7-14 | Process definition, SIEM, vulnerability management | 35 controls | CERG-led |
| Compliance | Weeks 15-26 | Regulatory overlays, supply chain, audit readiness | 30 controls | CERG-led |
| Sustain | Ongoing | Evidence automation, QBR cadence, maturity growth | All controls | MSP / Internal |

---

## 2. Quick Wins (Week 1-2)

*Low effort, high impact. Can be done by client IT with CERG guidance.*

| Week | Control | Task | Est. Hours | Verification |
|------|---------|------|------------|--------------|
| 1 | AC-1 | Deploy access control policy template | 2 | Policy signed |
| 1 | IA-1 | Enable MFA for all users | 4 | MFA enrollment >95% |
| 1 | SI-1 | Deploy EDR on all endpoints | 8 | Agent coverage >95% |
| 2 | AC-3 | Block legacy authentication | 2 | Legacy auth blocked |
| 2 | CM-1 | Apply OS security baseline | 4 | Baseline compliance >90% |

---

## 3. Foundation (Weeks 3-6)

*Establishes the basic security program infrastructure.*

| Week | Control | Task | Est. Hours | Dependencies |
|------|---------|------|------------|--------------|
| 3 | AU-1 | Configure log collection + SIEM ingestion | 8 | EDR deployed (SI-1) |
| 3 | CM-8 | Deploy asset inventory tool | 4 | RMM access |
| 4 | AC-4 | Configure PIM / JIT access | 6 | MFA enabled (IA-1) |
| 4 | CP-1 | Deploy backup strategy | 8 | Asset inventory (CM-8) |
| 5 | RA-2 | Configure vulnerability scanning | 4 | Network access |
| 5 | AU-2 | Establish weekly log review cadence | 2 | SIEM configured (AU-1) |
| 6 | AC-2 | Deploy account lifecycle automation | 6 | HR feed / IdP |

---

## 4. Structure (Weeks 7-14)

*Process definition, risk management, and response capability.*

| Week | Control | Task | Est. Hours | Dependencies |
|------|---------|------|------------|--------------|
| 7-8 | IR-1 | Create incident response plan | 16 | Management buy-in |
| 7-8 | RA-1 | Establish risk register | 8 | Asset inventory (CM-8) |
| 9-10 | CM-2 | Implement change control process | 8 | PSA integration |
| 9-10 | CP-2 | Create recovery plan + test | 12 | Backups active (CP-1) |
| 11-12 | SR-1 | Vendor risk assessment process | 8 | Vendor list |
| 11-12 | AT-1 | Deploy security awareness training | 4 | Training budget |
| 13-14 | PL-1 | Create 12-month security roadmap | 4 | All above complete |

---

## 5. Compliance (Weeks 15-26)

*Regulatory overlay implementation (only if applicable).*

| Framework | Controls | Weeks | Est. Hours | Notes |
|-----------|----------|-------|------------|-------|
| PCI DSS | 40 overlay controls | 15-20 | 60-80 | Requires ASV, SAQ |
| CMMC L2 | 60-80 controls with evidence | 15-26 | 80-120 | C3PAO assessment |
| SOX ITGC | ~30 ITGC controls | 15-20 | 40-60 | External auditor |
| NERC-CIP | ~45 CIP controls | 20-26 | 80-160 | OT-specific |
| FedRAMP | ~80 controls | 20-30 | 120-200 | 3PAO required |

---

## 6. Sustain (Ongoing)

| Activity | Cadence | Owner | Automation |
|----------|---------|-------|------------|
| Weekly orphan account check | Weekly | MSP / IT | Automated script |
| Quarterly access review | Quarterly | Client IT | Report generation |
| Vulnerability scan + remediate | Weekly / Monthly | MSP / IT | Qualys / Wiz |
| QBR + roadmap update | Quarterly | CERG + client | Report template |
| Annual tabletop exercise | Annually | CERG-led | After-action report |
| Annual control validation | Annually | CERG / auditor | Evidence package |

---

## 7. Resource Estimate

| Phase | CERG Hours | Client Hours | Total Hours | Duration | |
|-------|-----------|-------------|-------------|----------|--|
| Quick Wins | 8 | 12 | 20 | 2 weeks |
| Foundation | 16 | 24 | 40 | 4 weeks |
| Structure | 32 | 24 | 56 | 8 weeks |
| Compliance | Variable | Variable | 40-200+ | 6-12 weeks |
| Sustain | 4 hrs/mo | 8 hrs/mo | 12 hrs/mo | Ongoing |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | CERG-DELIV-RMEDIT-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Confidential |
| **Owner** | CERG Practice Lead |
| **Effective Date** | YYYY-MM-DD |

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 | 2026-06-30 | CERG Practice Lead | Initial version |
