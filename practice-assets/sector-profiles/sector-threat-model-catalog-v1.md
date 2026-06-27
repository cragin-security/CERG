# CERG Sector Threat Model Catalog v1
## Practice Asset — Not a CERG Corpus Document
## Purpose: Per-sector threat model · CERG control mapping · Evidence priorities

---

## How to Use This Catalog

1. When onboarding a client, identify their sector from the intake questionnaire (A4).
2. For each threat scenario in that sector, verify that the mapped CERG controls are:
   - **Implemented** for the relevant scope
   - **Evidenced** at the named cadence
   - **Documented** as accepted risk or on the improvement register if not implemented
3. The evidence column names the specific CERG evidence artifact the auditor or assessor will expect.

Each sector also lists the **default mandatory overlays** — operational packages that are automatically selected when a client in this sector engages.

---

## 1. Technology / SaaS

### Default Overlays
None mandatory at baseline. Voluntary: SOC 2 readiness, PCI DSS if handling CHD.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | Compromise of cloud/SaaS identity provider → lateral movement into customer environments | AC-2, AC-3, AC-6, IA-2, IA-5 | IdP policy export, MFA enforcement report, PAM session logs, service account inventory |
| 2 | SaaS supply chain attack via vendor compromise (e.g., SolarWinds-style) | SR-2, SR-3, SA-9 | TPRM register, vendor assessment reports, SBOM evidence, shared responsibility matrix |
| 3 | AI/ML pipeline poisoning or model extraction from customer-facing AI features | CM-3, CM-8, RA-3, AI overlay | AI intake records, model inventory, prompt injection test evidence, data lineage |
| 4 | Data exfiltration via misconfigured cloud storage (S3 buckets, Firestore, etc.) | SC-7, SC-28, CM-6, CM-8 | Cloud security group export, encryption config, drift report, asset inventory |
| 5 | Insecure CI/CD pipeline with cryptographic key exposure in source control | IA-5, CM-3, AU-2 | Secrets scanner report, change records, SIEM source inventory for pipeline audit events |
| 6 | Customer data breach via compromised API keys or OAuth token theft | AC-3, AC-6, AU-2, AU-12, SI-4 | API gateway logs, key rotation evidence, detection coverage report, anomaly alert sample |
| 7 | SOC 2 Type II finding due to insufficient evidence of control operation | CA-2, PL-1, PM-14 | Maturity scorecard, control test worksheet, annual compliance calendar |

### Priority Standards
STD-IT-001 · STD-AC-001 · STD-LM-001 · STD-CR-001 · PRC-TPRM-001 · PRC-VM-001

---

## 2. Financial Services

### Default Overlays
SOX ITGC (`CERG-PLN-SOX-001`). PCI DSS if handling CHD.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | Wire fraud via compromised privileged access (internal or external) | AC-2, AC-6, IA-2, AU-6, AU-12 | PAM session logs, SoD matrix, access recert report, anomaly detection alerts |
| 2 | SOX ITGC deficiency from change management failure (unauthorized code move to production) | CM-3, CM-5, SI-2, PRC-CHG-001 evidence | CAB minutes, change records, CI/CD pipeline review, emergency change review |
| 3 | BCP/DR test failure exposing financial reporting recovery gaps | CP-2, CP-4, CP-9, CP-10 | Recovery plan, test evidence, RTO/RPO validation, backup restoration test |
| 4 | Third-party processor breach (payment, clearing, or settlement provider) | SR-2, SR-3, SA-9, PLN-SOX-001 SOC 1 reuse | TPSP register, SOC 1 reports, CUEC inventory, compensating control evidence |
| 5 | Insider trade based on unauthorized access to material non-public information | AC-2, AC-6, AU-2, AU-9 | JML log, privilege review, audit log access controls, user activity monitoring |
| 6 | FDIC/OCC/state regulator examination finding — evidence not current | CA-2, PM-14, PL-1, AUD-001 | Evidence library review, compliance calendar, annual policy review |

### Priority Standards
PLN-SOX-001 · STD-AC-001 · STD-LM-001 · STD-RES-001 · STD-CR-001 · PRC-AC-002

---

## 3. Healthcare / Life Sciences

### Default Overlays
Privacy (`CERG-PLN-PRIV-001`). CUI if handling CUI/PHI in clinical trials.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | PHI breach via compromised EHR/EMR access — regulatory (HIPAA/HITRUST) reporting risk | AC-2, AC-3, IA-2, AU-2, AU-12 | Access recertification, MFA enforcement, SIEM CHD/PHI coverage, audit trail evidence |
| 2 | Clinical trial data integrity compromise (CUI impact; regulatory action) | SC-8, SC-28, CM-3, SR-2 | Encryption in transit/at rest, change control for trial systems, vendor assessment for CROs |
| 3 | Ransomware on medical device or diagnostic system causing patient care delay | CP-2, CP-4, CP-9, IR-4, SC-7 | Recovery plan, backup test, segmentation diagram, IR playbook evidence |
| 4 | Vendor/third-party CRO data breach impacting sponsor obligations | SR-2, SR-3, SA-9 | TPSP register, contractual security clauses, right-to-audit evidence |
| 5 | Insider access to health records beyond job role (privacy violation) | AC-2, AC-6, AU-6, AU-12 | Access recert, privilege review, user activity monitoring alerts |
| 6 | Clinical system availability failure during procedure/treatment | CP-2, CP-10, SI-2 | Recovery plan, failover test evidence, patch SLA compliance |

### Priority Standards
STD-CUI-001 · STD-AC-001 · STD-LM-001 · STD-RES-001 · PLN-PRIV-001 · PRC-TPRM-001

---

## 4. Manufacturing / OT

### Default Overlays
OT Safety (`CERG-STD-OT-001`). BES overlay if systems are grid-connected.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | Production line disruption via ransomware on IT-connected OT systems | SC-7, CP-2, CP-9, IR-4, RA-5 | Segmentation diagram, recovery plan, backup/restore of PLC configs, IR playbook |
| 2 | Unauthorized remote access to plant-floor systems (contractor, vendor) | AC-17, IA-2, AU-2, PE-2 | Remote access gateway logs, MFA evidence, vendor access registry, session recording |
| 3 | OT asset inventory gap (unknown device on the floor) → blind spot | CM-8, SC-7 | CMDB OT asset class, passive OT inventory scan, network traffic baseline |
| 4 | Unpatched OT vulnerability exploited (limited maintenance windows) | RA-5, SI-2, PRC-VM-001 OT deferral procedure | OT-specific vulnerability scan (passive), risk acceptance for deferred patches, compensating controls |
| 5 | Plant-floor change control bypass (operator modifies PLC logic without review) | CM-3, CM-5, PRC-CHG-001 | Change records, change-authority review, OT-specific change advisory board minutes |
| 6 | Safety-system interlock disabled via compromised engineering workstation | SC-7, AC-6, CM-7 | Zone segmentation, least privilege for engineering stations, baseline configuration evidence |

### Priority Standards
STD-OT-001 · STD-NET-001 · STD-AC-001 · STD-CFG-001 (DISH OT variant) · STD-LM-001 · PRC-VM-001 · PRC-CHG-001

---

## 5. Energy / Utilities

### Default Overlays
NERC-CIP (`CERG-PLN-CIP-001`). BES overlay. OT Safety.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | BES Cyber System compromise leading to reportable grid disturbance | AC-2, AC-5, SC-7, AU-2, RA-5, SI-2 | CIP-005 log review, CIP-007 scan report, CIP-010 baseline verification, ESP/EAP diagram |
| 2 | NERC-CIP CIP-008 reportable incident — detection-to-notification gap | IR-4, IR-8, AU-6 | Incident case file, IR plan, regulatory notification timeline evidence |
| 3 | OT cyber recovery exceeding RTO (NERC-CIP CIP-009 failure) | CP-2, CP-4, CP-9, CP-10 | Recovery plan, 15-month test window evidence, backup restoration test, BES-specific RTO/RPO |
| 4 | Third-party grid operations vendor with BES cyber system access goes unmonitored | SR-2, SR-3, AC-17, SA-9 | TPSP register, vendor remote access logs, CIP-013 compliance evidence, contract clauses |
| 5 | Physical security perimeter (PSP) breach at substation or control center | PE-2, PE-3, PLN-CIP-001 PSP controls | Badge logs, visitor logs, PSP inspection record, video access logs (90-day retention) |
| 6 | Supply chain attack on substation automation firmware | SR-2, SR-3, CM-2 | Firmware integrity verification, vendor SBOM, procurement security requirements |

### Priority Standards
PLN-CIP-001 · STD-OT-001 · STD-NET-001 · STD-AC-001 · STD-CFG-001 · STD-RES-001 · PRC-TPRM-001

---

## 6. Defense Industrial Base

### Default Overlays
CUI/CMMC (`CERG-PLN-CUI-001`). IR adjacent.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | CUI exfiltration from unmanaged/unmonitored endpoint within CUI enclave | CM-7, CM-8, SC-7, AU-2, AU-12 | Device inventory, endpoint hardening evidence, SIEM CDE/CUI log coverage |
| 2 | CMMC assessment failure — POA&M with long-term open items exceeds SPRS threshold | CA-2, RA-5, SI-2, PLN-CUI-001 §7 | POA&M register, maturity scorecard, SPRS score evidence, remediation SLAs |
| 3 | Unauthorized foreign national access to CUI or ITAR-controlled data | AC-2, AC-3, AC-6, IA-2, JR 5 (citizenship check) | Access recert, nationality-based access controls, export control training evidence |
| 4 | DFARS clause violation — contractor fails to flow down CUI requirements to subcontractor | SR-2, SR-3, PLN-CUI-001 subcontractor | Flow-down contract clauses, subcontractor compliance evidence, TPSP assessment |
| 5 | Incident involving a CUI system goes unreported to the contracting officer | IR-4, IR-8, PL-1 | Incident case record, CUI incident notification evidence, policy compliance |
| 6 | Incomplete system security plan (SSP) for CUI system coverage | CA-2, PL-1, CM-8, PLN-CUI-001 §3 | SSP, system boundary diagram, asset inventory with CUI designation |

### Priority Standards
PLN-CUI-001 · STD-CUI-001 · STD-AC-001 · STD-CFG-001 · STD-LM-001 · PRC-TPRM-001 · PRC-AUD-001

---

## 7. Government / Federal

### Default Overlays
CUI if handling CUI. ISO or FedRAMP equivalent. Privacy.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | FISMA control deficiency identified by OIG audit — recurring finding | CA-2, PM-14, PRC-AUD-001 | Control test worksheet, findings register, POA&M with closure evidence |
| 2 | Foreign state threat actor — persistent access via compromised vendor/supplier network | SR-2, SR-3, SI-4, SC-7 | TPSP register, country-risk register, threat intelligence feed evidence, segmentation test |
| 3 | CUI spillage or improper handling in unclassified environment | CM-6, SC-8, SC-28, STD-CUI-001 | DLP alert evidence, encryption config, data classification labels, handling policy |
| 4 | Insider threat — cleared employee exfiltrates classified material | AC-6, AU-2, AU-9, PE-3 | PAM session logs, user activity monitoring, removable media controls, badge access policies |
| 5 | FedRAMP or ATO renewal delay due to evidence package gap | CA-2, PL-1, PM-14, AUD-001 evidence library | Evidence library review, annual security assessment plan, compliance calendar |
| 6 | Identity federation compromise between federal partner agencies | IA-2, IA-3, AC-3, AU-12 | IdP federation config, cross-certificate validation, MFA evidence |

### Priority Standards
STD-CUI-001 · STD-AC-001 · STD-LM-001 · STD-CR-001 · PRC-AUD-001 · PRC-TPRM-001 · PLN-PRIV-001

---

## 8. Cross-sector / Holding

### Default Overlays
All that apply per subsidiary. Consolidated GRC evidence model.

### Threat Scenarios

| # | Threat Scenario | CERG Controls | Evidence Required |
|---|---|---|---|
| 1 | Regulatory gap where one subsidiary is in PCI scope and another is in CMMC — no shared evidence model | CMX-001, CAT-002, GOV-OM-001 | Compliance matrix per subsidiary, regulatory overlay map, control baseline shared scope |
| 2 | Central security team cannot enforce policies on autonomous subsidiary | GOV-OM-001, RAC-001, IMP-002 | Operating model variant, RACI per subsidiary, escalation path and authority boundaries |
| 3 | M&A target with unknown security posture becomes liability post-close | PRC-TPRM-001, CM-8, RA-3, IMP-005 | Pre-acquisition assessment, 90-day integration plan, risk register entries for acquired entity |
| 4 | Duplicate tool and vendor contracts across subsidiaries (cost inefficiency) | TMPL-TPRM-001, PRC-TPRM-001 | Vendor inventory, contract overlap analysis, procurement consolidation plan |
| 5 | Shared service (IdP, SIEM, NOC) does not meet the strictest regulatory requirement of any subsidiary | AC-2, AU-2, SD-7, CB-001 overlay stacking | Shared service control testing per strictest overlay, SLAs with subsidiary-specific evidence |

### Priority Standards
GOV-CMX-001 · GOV-OM-001 · RAC-001 · STD-IT-001 · PRC-TPRM-001 · TMPL-SCP-001

---

## Reference: All Sectors Crosswalk

| Sector | Default Overlays | Spine Standards |
|---|---|---|
| Technology / SaaS | None (voluntary: SOC 2, PCI) | STD-IT-001 · STD-AC-001 · STD-LM-001 |
| Financial Services | SOX ITGC, PCI (if CHD) | STD-AC-001 · STD-LM-001 · PLN-SOX-001 |
| Healthcare / Life Sciences | Privacy, CUI (if clinical trials) | STD-CUI-001 · STD-AC-001 · PLN-PRIV-001 |
| Manufacturing / OT | OT Safety, BES (if grid-connected) | STD-OT-001 · STD-NET-001 · STD-CFG-001 |
| Energy / Utilities | NERC-CIP, BES, OT Safety | PLN-CIP-001 · STD-OT-001 · STD-RES-001 |
| Defense Industrial Base | CUI/CMMC | PLN-CUI-001 · STD-CUI-001 · STD-CFG-001 |
| Government / Federal | CUI (if applicable), ISO/FedRAMP, Privacy | STD-CUI-001 · STD-AC-001 · PRC-AUD-001 |
| Cross-sector / Holding | All applicable per subsidiary | GOV-CMX-001 · GOV-OM-001 · RAC-001 |
