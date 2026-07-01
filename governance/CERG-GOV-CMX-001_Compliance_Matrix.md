### Cyber Engineering, Risk & Governance: CERG Framework

> **How to read this matrix:** Each row represents a security _intent_, the underlying goal that multiple frameworks are all trying to achieve. The regulatory and NIST columns show where each framework addresses that intent. Where multiple frameworks align to one row, a single control effort satisfies all of them. Items marked **⚠ Unique** have requirements that don't fully overlap with the other frameworks and warrant dedicated attention.

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CMX-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on framework version change |
| **Frameworks** | NIST 800-53r5; NIST 800-171r3; NIST CSF 2.0; NIST RMF |
| **Regulations** | NERC-CIP; CMMC L2; SOX ITGC |
| **Environments** | All in-scope environments |

---

## Table of Contents

1. [Know what you own: maintain an authoritative asset inventory](#1-know-what-you-own-maintain-an-authoritative-asset-inventory)
2. [Identify and remediate known vulnerabilities on a defined schedule](#2-identify-and-remediate-known-vulnerabilities-on-a-defined-schedule)
3. [Control who can access what: enforce least privilege](#3-control-who-can-access-what-enforce-least-privilege)
4. [Authenticate users and systems: verify identity before granting access](#4-authenticate-users-and-systems-verify-identity-before-granting-access)
5. [Harden systems: remove what isn't needed, lock down what is](#5-harden-systems-remove-what-isnt-needed-lock-down-what-is)
6. [Protect data in transit and at rest: encryption as a baseline control](#6-protect-data-in-transit-and-at-rest-encryption-as-a-baseline-control)
7. [Segment networks: limit lateral movement and blast radius](#7-segment-networks-limit-lateral-movement-and-blast-radius)
8. [Manage vendor and third-party risk: extend controls beyond the perimeter](#8-manage-vendor-and-third-party-risk-extend-controls-beyond-the-perimeter)
9. [Control and log privileged/remote access: know who did what, when](#9-control-and-log-privilegedremote-access-know-who-did-what-when)
10. [Conduct adversarial testing: find what scanners miss](#10-conduct-adversarial-testing-find-what-scanners-miss)
11. [Train and background-check personnel with access to sensitive systems](#11-train-and-background-check-personnel-with-access-to-sensitive-systems)
12. [Write and maintain policies: define what good looks like](#12-write-and-maintain-policies-define-what-good-looks-like)
13. [Manage configuration changes: track drift, prevent unauthorized changes](#13-manage-configuration-changes-track-drift-prevent-unauthorized-changes)
14. [Collect, protect, and retain audit evidence: prove controls are working](#14-collect-protect-and-retain-audit-evidence-prove-controls-are-working)
15. [Assess your own security posture: periodic internal evaluation](#15-assess-your-own-security-posture-periodic-internal-evaluation)
16. [Manage risk formally: document, accept, or treat identified risks](#16-manage-risk-formally-document-accept-or-treat-identified-risks)
17. [Protect physical access to critical systems: cyber starts at the door](#17-protect-physical-access-to-critical-systems-cyber-starts-at-the-door)
18. [Monitor threats continuously: detect what vulnerability scans miss](#18-monitor-threats-continuously-detect-what-vulnerability-scans-miss)
19. [Plan and practice incident response: know what to do before it happens](#19-plan-and-practice-incident-response-know-what-to-do-before-it-happens)
20. [Manage recovery: restore operations and capture lessons learned](#20-manage-recovery-restore-operations-and-capture-lessons-learned)
21. [Manage accounts throughout their lifecycle: provisioning through termination](#21-manage-accounts-throughout-their-lifecycle-provisioning-through-termination)
22. [Define and enforce a compliance calendar: no surprises at audit time](#22-define-and-enforce-a-compliance-calendar-no-surprises-at-audit-time)
23. [Quick Reference: Pillar Summary](#quick-reference-pillar-summary)
24. [Key Consolidation Opportunities](#key-consolidation-opportunities)
23. [Document Control](#document-control)

## 1. Know what you own: maintain an authoritative asset inventory

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) IDENTIFY · 800-53 CM-8 · 800-171 3.4.1 · RMF Step 1|
|NERC-CIP|CIP-002 (BES asset categorization)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|CM.2.061|

**What "done" looks like:** Living asset register with classification, owner, and regulatory designation (BES/CUI). Engineering produces at project handoff; Risk validates via scan coverage.

---

## 2. Identify and remediate known vulnerabilities on a defined schedule

**Primary Pillar:** Risk **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) IDENTIFY · 800-53 SI-2, RA-5 · 800-171 3.11.2 · RMF Step 6|
|NERC-CIP|CIP-007-6 R2 (patch management), CIP-010 R3 (vuln assessment)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|RM.2.141, SI.2.214|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC patch/change risk|

**What "done" looks like:** Continuous scan coverage across IT and OT; prioritized finding register with SLA tracking; deviation/exception process for OT-constrained systems.

---

## 3. Control who can access what: enforce least privilege

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 AC-2, AC-6 · 800-171 3.1.1–3.1.3 · RMF Step 3|
|NERC-CIP|CIP-004 R4 (access management), CIP-005 R2 (interactive remote access)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|AC.1.001, AC.1.002, AC.2.006|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC access control (segregation of duties)|

**What "done" looks like:** Role-based access model implemented; privileged access managed separately; access reviews on defined cycle; MFA enforced for remote and privileged access.

---

## 4. Authenticate users and systems: verify identity before granting access

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 IA-2, IA-5 · 800-171 3.5.1–3.5.3 · RMF Step 3|
|NERC-CIP|CIP-005 R2 (EACMS authentication), CIP-007 R5 (account management)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|IA.1.076, IA.3.083|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC authentication controls|

**What "done" looks like:** MFA deployed for all remote and privileged access; default/shared credentials eliminated; password policy enforced by technical control, not just policy.

---

## 5. Harden systems: remove what isn't needed, lock down what is

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 CM-6, CM-7 · 800-171 3.4.6, 3.4.7 · RMF Step 3|
|NERC-CIP|CIP-007 R1 (ports and services), CIP-010 R1 (config baseline)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|CM.2.061, CM.2.064|

**What "done" looks like:** Secure configuration baselines (CIS benchmarks or equivalent) documented and enforced for each platform class; deviation from baseline requires documented exception.

---

## 6. Protect data in transit and at rest: encryption as a baseline control

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 SC-8, SC-28 · 800-171 3.13.8, 3.13.10 · RMF Step 3|
|NERC-CIP|CIP-011 (BES Cyber System Information protection)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|SC.3.177, SC.3.187|

**What "done" looks like:** Encryption standards defined and applied to all CUI/BCSI environments; key management process documented; TLS enforced on all external-facing interfaces.

---

## 7. Segment networks: limit lateral movement and blast radius

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 SC-7 · 800-171 3.13.1 · RMF Step 3|
|NERC-CIP|CIP-005 (Electronic Security Perimeters and EAPs)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|SC.1.175|

**What "done" looks like:** Documented network zones with access control lists; OT/ICS and CUI environments isolated; ESP/EAP documented for all BES Cyber Systems.

---

## 8. Manage vendor and third-party risk: extend controls beyond the perimeter

**Primary Pillar:** Risk **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) GOVERN · 800-53 SA-9, SR-3 · 800-171 3.1.20 · RMF Step 2|
|NERC-CIP|CIP-013 (supply chain risk management)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|SR.3.169|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC third-party SOC 2 review|

**What "done" looks like:** Vendor risk assessment program with tiered review depth; contract security requirements (right-to-audit, incident notification, data handling); supply chain risk management plan.

---

## 9. Control and log privileged/remote access: know who did what, when

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 AU-2, AU-12, AC-17 · 800-171 3.3.1 · RMF Step 3|
|NERC-CIP|CIP-005 R2 (interactive remote access), CIP-007 R4 (security event logging)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|AU.2.041, AU.2.042|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC access logging and review|

**What "done" looks like:** All privileged and remote sessions logged; session recordings for high-risk access; log retention per regulatory requirement; log review process defined and tracked.

---

## 10. Conduct adversarial testing: find what scanners miss

**Primary Pillar:** Risk **Regulations:** [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST **⚠ Unique:** No direct NERC-CIP analog

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) IDENTIFY · 800-53 CA-8 · 800-171 3.11.1 · RMF Step 4|
|[CMMC](https://dodcio.defense.gov/CMMC/)|CA.2.157 (pen test as part of assessment)|

**What "done" looks like:** Annual minimum pen test schedule; scope includes internal, external, and (where applicable) OT/ICS targets; findings tracked to closure with Engineering review of architectural impacts.

---

## 11. Train and background-check personnel with access to sensitive systems

**Primary Pillar:** Governance **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) GOVERN · 800-53 PS-2, AT-2 · 800-171 3.9.1 · RMF Step 1|
|NERC-CIP|CIP-004 (personnel training and risk assessment)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|PS.2.127, AT.2.056|

**What "done" looks like:** Role-based training program with completion tracking; background check process for privileged users; CIP-004 training records maintained per regulatory retention requirement.

---

## 12. Write and maintain policies: define what good looks like

**Primary Pillar:** Governance **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) GOVERN · 800-53 PL-1, PM-1 · 800-171 3.12.4 · RMF Step 1|
|NERC-CIP|CIP-003 (security management controls, senior manager approval)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|All 14 domains require policy documentation|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC policy requirements|

**What "done" looks like:** Policy library version-controlled and reviewed on defined cycle; each policy mapped to regulatory citation; senior leader approval documented; implementation guidance published for each policy.

---

## 13. Manage configuration changes: track drift, prevent unauthorized changes

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 CM-3, CM-5 · 800-171 3.4.3 · RMF Step 3|
|NERC-CIP|CIP-010 R1 (configuration change management)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|CM.2.062|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC change management (key [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC control)|

**What "done" looks like:** All changes to in-scope systems go through documented change process; baseline comparison before/after; unauthorized change detection via config monitoring; [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) change tickets retained as audit evidence.

---

## 14. Collect, protect, and retain audit evidence: prove controls are working

**Primary Pillar:** Governance **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) GOVERN · 800-53 AU-9, AU-11 · 800-171 3.3.2 · RMF Step 6|
|NERC-CIP|CIP-007 R4 (log retention), all CIP standards require evidence retention|
|[CMMC](https://dodcio.defense.gov/CMMC/)|AU.2.042, all domain documentation|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|Audit trail retention for ITGC and financial system access|

**What "done" looks like:** Evidence library organized by control and regulatory citation; retention periods enforced per framework (NERC-CIP: per standard, [CMMC](https://dodcio.defense.gov/CMMC/): available for assessment, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204): per audit retention requirements); pre-audit evidence review process.

---

## 15. Assess your own security posture: periodic internal evaluation

**Primary Pillar:** Risk **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) IDENTIFY · 800-53 CA-2 · 800-171 3.12.1 · RMF Step 4|
|NERC-CIP|CIP-010 R3 (annual vuln assessment)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|CA.2.157 (assessment of security requirements)|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC control self-assessment|

**What "done" looks like:** Annual security assessment cycle with documented scope, findings, and remediation plan; self-assessment results feed risk register and POA&M; Governance tracks findings to closure.

---

## 16. Manage risk formally: document, accept, or treat identified risks

**Primary Pillar:** Governance **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) GOVERN · 800-53 RA-3, PM-9 · 800-171 3.11.1 · RMF Step 4–5|
|NERC-CIP|CIP-003 (risk management), deviation/mitigation plan process|
|[CMMC](https://dodcio.defense.gov/CMMC/)|RM.2.141, RM.3.144 (POA&M management)|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|Enterprise risk management (ERM) interface|

**What "done" looks like:** Risk register maintained with owner, severity, treatment status, and target closure date; POA&M current and leadership-reviewed quarterly; risk acceptance documented with CISO or VP sign-off per policy.

---

## 17. Protect physical access to critical systems: cyber starts at the door

**Primary Pillar:** Governance **Regulations:** NERC-CIP · · NIST **⚠ Unique:** NERC-CIP most prescriptive, CIP-006/CIP-014 unique to BES environments

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 PE-2, PE-3 · RMF Step 3|
|NERC-CIP|CIP-006 (physical security of BES Cyber Systems), CIP-014 (transmission physical security)|

**What "done" looks like:** Physical access controls documented for all in-scope locations; access lists maintained and reviewed; visitor logs retained; NERC-CIP deviation process invoked when physical security controls are temporarily impaired.

---

## 18. Monitor threats continuously: detect what vulnerability scans miss

**Primary Pillar:** Risk **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) DETECT · 800-53 SI-4, IR-4 · 800-171 3.14.6 · RMF Step 6|
|NERC-CIP|CIP-007 R4 (security event monitoring)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|SI.2.216, IR.2.092|

**What "done" looks like:** SIEM or equivalent collecting logs from in-scope systems; defined alert thresholds; analyst review cadence; threat intelligence feeds integrated; OT monitoring via passive methods where active scanning would introduce operational risk.

---

## 19. Plan and practice incident response: know what to do before it happens

**Primary Pillar:** Governance **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) RESPOND · 800-53 IR-2, IR-4, IR-8 · 800-171 3.6.1–3.6.3 · RMF Step 6|
|NERC-CIP|CIP-008 (incident reporting and response planning)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|IR.2.092, IR.2.093|

**What "done" looks like:** Documented IR plan with roles, escalation paths, and regulatory notification requirements; tabletop exercise at least annually; CIP-008 reporting timelines documented and practiced; lessons learned feed risk register.

---

## 20. Manage recovery: restore operations and capture lessons learned

**Primary Pillar:** Governance **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · NIST **⚠ Unique:** CIP-009 unique to BES, highly prescriptive on testing cadence

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) RECOVER · 800-53 CP-2, CP-9 · 800-171 3.6.2 · RMF Step 6|
|NERC-CIP|CIP-009 (recovery plans for BES Cyber Systems)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|RE.2.137|

**What "done" looks like:** Recovery plans documented, tested, and updated annually; backup and restoration tested; post-incident review drives updates to Engineering architecture, Risk assessments, and Governance playbooks.

---

## 21. Manage accounts throughout their lifecycle: provisioning through termination

**Primary Pillar:** Engineering **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) PROTECT · 800-53 AC-2 · 800-171 3.1.1 · RMF Step 3|
|NERC-CIP|CIP-004 R4 (access management), CIP-007 R5 (account management)|
|[CMMC](https://dodcio.defense.gov/CMMC/)|AC.2.005, AC.2.006|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|ITGC joiner/mover/leaver process|

**What "done" looks like:** Automated provisioning/deprovisioning tied to HR system; access reviews on defined cycle; privileged account inventory; shared/service account governance documented.

---

## 22. Define and enforce a compliance calendar: no surprises at audit time

**Primary Pillar:** Governance **Regulations:** NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) · NIST **⚠ Unique:** Governance operational discipline, no direct technical control analog

|Framework|Requirement|
|---|---|
|NIST|[CSF](https://www.nist.gov/cyberframework) GOVERN · 800-53 PM-14 · RMF Step 6|
|NERC-CIP|All CIP standards have annual and periodic review requirements|
|[CMMC](https://dodcio.defense.gov/CMMC/)|Annual self-assessment or C3PAO assessment cycle|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)|Annual ITGC audit cycle|

**What "done" looks like:** Master compliance calendar covering all frameworks; activities assigned to owners in CERG; upcoming deadlines visible to CISO; evidence collection treated as ongoing, not pre-audit scramble.

---

## Quick Reference: Pillar Summary

|Pillar|Control Areas Owned|Key Frameworks Satisfied|
|---|---|---|
|**Engineering**|Asset inventory · Least privilege · Authentication · System hardening · Encryption · Network segmentation · Logging · Config change management · Account lifecycle|NERC-CIP CIP-005/007/010/011 · [CMMC](https://dodcio.defense.gov/CMMC/) AC/IA/SC/CM domains · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC|
|**Risk**|Exposure management · Vendor risk · Adversarial testing · Self-assessment · Threat monitoring|NERC-CIP CIP-007/010/013 · [CMMC](https://dodcio.defense.gov/CMMC/) RM/CA/SI domains · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) third-party|
|**Governance**|Policy & standards · Personnel training · Evidence management · Risk register · Physical security · IR planning · Recovery · Compliance calendar|NERC-CIP CIP-003/004/006/008/009/014 · [CMMC](https://dodcio.defense.gov/CMMC/) all documentation · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · [CMMC](https://dodcio.defense.gov/CMMC/) SSP/POA&M|

---

## Key Consolidation Opportunities

These control areas produce evidence satisfying four or more frameworks simultaneously. One team effort, multiple checkboxes.

1. **Asset inventory**, CIP-002 + [CMMC](https://dodcio.defense.gov/CMMC/) CM + NIST CM-8
2. **Access management**, CIP-004/005/007 + [CMMC](https://dodcio.defense.gov/CMMC/) AC + [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC
3. **Configuration change management**, CIP-010 + [CMMC](https://dodcio.defense.gov/CMMC/) CM + [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC
4. **Audit evidence and log retention**, all CIP standards + [CMMC](https://dodcio.defense.gov/CMMC/) AU + [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)
5. **Exposure management**, CIP-007/010 + [CMMC](https://dodcio.defense.gov/CMMC/) RM/SI + [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) patch risk
6. **Policy and standards**, CIP-003 + [CMMC](https://dodcio.defense.gov/CMMC/) (all 14 domains) + [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC

---


---

## 23. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CMX-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on framework version change |
| **Next Scheduled Review** | 2027-05-01 |
| **Frameworks** | NIST 800-53r5; NIST 800-171r3; NIST CSF 2.0; NIST RMF |
| **Regulations** | NERC-CIP; CMMC L2; SOX ITGC |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-01 | Cyber Governance | Initial release. Compliance matrix mapping security intents to NIST, CMMC, NERC-CIP, and SOX frameworks. |
| 1.21 | 2026-05-22 | Cyber Governance | Updated framework references and pillar alignments. |

### Review Triggers

- Framework version change (NIST 800-53, NIST 800-171, CMMC, NERC-CIP)
- New regulatory requirement
- Material change to organizational scope
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Unified Control Baseline | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control spine, overlays, evidence mapping |
| CERG Framework | [CERG-GOV-FRM-001](CERG-GOV-FRM-001_CERG_Framework.md) | Narrative framework |
| Document Catalog | [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Master document inventory |
