## IMPLEMENTATION CARDS
### For Every Security Intent · Minimum Viable to Full Implementation · Who Does What

---

| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-004 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CMX-001](CERG-GOV-CMX-001_Compliance_Matrix.md) · [CERG-PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Review Cycle** | Annual / On material change to control baseline |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 · NIST 800-171r3 |
| **Regulations** | NERC-CIP · CMMC L2 · SOX ITGC |
| **Environments** | All in-scope |

---

## Table of Contents

1. [Intent 1: Know What You Own](#1--know-what-you-own)
2. [Intent 2: Identify and Remediate Vulnerabilities](#2--identify-and-remediate-vulnerabilities)
3. [Intent 3: Enforce Least Privilege](#3--enforce-least-privilege)
4. [Intent 4: Verify Identity Before Granting Access](#4--verify-identity-before-granting-access)
5. [Intent 5: Harden Systems](#5--harden-systems)
6. [Intent 6: Protect Data — Encryption as Baseline](#6--protect-data--encryption-as-baseline)
7. [Intent 7: Segment Networks](#7--segment-networks)
8. [Intent 8: Manage Vendor and Third-Party Risk](#8--manage-vendor-and-third-party-risk)
9. [Intent 9: Control and Log Privileged Access](#9--control-and-log-privileged-access)
10. [Intent 10: Conduct Adversarial Testing](#10--conduct-adversarial-testing)
11. [Intent 11: Train and Background-Check Personnel](#11--train-and-background-check-personnel)
12. [Intent 12: Write and Maintain Policies](#12--write-and-maintain-policies)
13. [Intent 13: Manage Configuration Changes](#13--manage-configuration-changes)
14. [Intent 14: Collect, Protect, and Retain Audit Evidence](#14--collect-protect-and-retain-audit-evidence)
15. [Intent 15: Assess Your Own Security Posture](#15--assess-your-own-security-posture)
16. [Intent 16: Manage Risk Formally](#16--manage-risk-formally)
17. [Intent 17: Protect Physical Access](#17--protect-physical-access)
18. [Intent 18: Monitor Threats Continuously](#18--monitor-threats-continuously)
19. [Intent 19: Plan and Practice Incident Response](#19--plan-and-practice-incident-response)
20. [Intent 20: Manage Recovery and Lessons Learned](#20--manage-recovery-and-lessons-learned)
21. [Intent 21: Manage Accounts Throughout Their Lifecycle](#21--manage-accounts-throughout-their-lifecycle)
22. [Intent 22: Define and Enforce a Compliance Calendar](#22--define-and-enforce-a-compliance-calendar)
23. [Document Control](#23--document-control)

---

> **How to use these cards:** Each card translates a security intent from [CMX-001](CERG-GOV-CMX-001_Compliance_Matrix.md) into actionable implementation guidance. Start with the minimum viable column; layer toward the good column as the program matures. Every card names the pillar responsible, the evidence to produce, the most common failure mode, and the exception path when the standard cannot be met.
>
> **Maturity lens:** Treat each card as a staged adoption path, not a binary checklist. Minimum Viable usually corresponds to an Informed or early Repeatable practice in [MAT-001](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md). Good Implementation corresponds to Repeatable or Adaptive practice when evidence, metrics, and improvement feedback are operating. Do not rename CERG controls or intents locally just to fit another model; preserve CERG IDs and use the card to decide the next maturity move.

---

## 1 — Know What You Own

**Intent:** Maintain an authoritative asset inventory. [CMX-001 §1](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | One authoritative inventory with owner, data class, environment, regulatory flag | Inventory reconciled against cloud, endpoint, IdP, scanner, SaaS, and procurement |
| **Evidence** | CMDB export, owner attestation | Reconciliation report, coverage dashboard, unowned-asset count trending downward |
| **Failure Mode** | Unknown Internet-facing asset; orphaned SaaS tenant; vendor-owned admin path without organizational visibility |
| **Exception Path** | Governance exception if field missing from inventory record; Risk escalation if unknown asset is confirmed exposed |
| **Engineering Role** | Asset onboarding pattern; project-handoff inventory entry |
| **Risk Role** | Coverage validation — scan coverage % vs inventory |
| **Governance Role** | Evidence and control mapping; ownership attestation cadence |

---

## 2 — Identify and Remediate Vulnerabilities

**Intent:** Identify and remediate known vulnerabilities on a defined schedule. [CMX-001 §2](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Authenticated scan of production systems; CVSS-based SLA for Critical/High | Exposure management pipeline: observe → validate → assess reachability → classify → treat → verify (per [VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)) |
| **Evidence** | Scan reports, remediation tickets, SLA tracking | Exposure pipeline state log, KEV triage records, compensating control validation |
| **Failure Mode** | Scanner report treated as the vulnerability program; CVSS 9.9 on a service that isn't running; "false positive" used as catch-all |
| **Exception Path** | Risk acceptance per [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7; compensating controls documented and verified |
| **Engineering Role** | Treatment execution; configuration changes; compensating control implementation |
| **Risk Role** | Pipeline operation; observation triage; exposure confirmation; KEV monitoring |
| **Governance Role** | SLA tracking; exception documentation; POA&M entries for CUI environments |

---

## 3 — Enforce Least Privilege

**Intent:** Control who can access what — enforce least privilege. [CMX-001 §3](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Role-based access groups; quarterly access review of privileged accounts | JIT access for all privileged operations; attribute-based access control; automated de-provisioning on role change |
| **Evidence** | Access review records, privileged group membership | PAM session logs, elevation justification records, access recertification status |
| **Failure Mode** | Standing admin access justified as "operational necessity"; access review becomes rubber-stamp exercise; service accounts with interactive login |
| **Exception Path** | Governance exception with documented compensating control and expiration; no standing global admin without CISO approval |
| **Engineering Role** | PAM deployment; directory structure; access automation |
| **Risk Role** | Privileged access monitoring; anomalous access detection |
| **Governance Role** | Access review cadence; recertification enforcement; exception tracking |

---

## 4 — Verify Identity Before Granting Access

**Intent:** Authenticate users and systems — verify identity before granting access. [CMX-001 §4](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | MFA for all remote access and privileged accounts | Phishing-resistant MFA for all accounts; passwordless where feasible; FIDO2/WebAuthn for privileged |
| **Evidence** | IdP configuration, MFA enrollment reports | Phishing-resistant MFA coverage %, authentication method distribution |
| **Failure Mode** | SMS/phone-call MFA treated as equivalent to phishing-resistant; service accounts bypassing MFA; federation trust not reviewed |
| **Exception Path** | Governance exception for systems that cannot support MFA; compensating controls required (network restriction, session monitoring) |
| **Engineering Role** | IdP architecture; federation trust review; authentication method deployment |
| **Risk Role** | Authentication anomaly detection; credential theft monitoring |
| **Governance Role** | MFA policy enforcement; exception tracking; coverage reporting |

---

## 5 — Harden Systems

**Intent:** Remove what isn't needed, lock down what is. [CMX-001 §5](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | CIS Level 1 baseline deployed; monthly drift scan | CIS Level 2 for High-Impact/CUI; DISH profile per [STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md); automated drift remediation |
| **Evidence** | DISH scan results, baseline coverage report | Drift detection alerts, automated remediation logs, baseline exception register |
| **Failure Mode** | Baseline deployed once and never re-validated; drift accepted as normal; "hardening breaks the application" used to avoid baselines |
| **Exception Path** | Governance exception with compensating controls; baseline deviation documented per asset; re-evaluated quarterly |
| **Engineering Role** | Baseline authoring; drift detection; automated remediation |
| **Risk Role** | Drift monitoring; exposure assessment of unhardened assets |
| **Governance Role** | Baseline policy; exception register; coverage reporting |

---

## 6 — Protect Data — Encryption as Baseline

**Intent:** Protect data in transit and at rest. [CMX-001 §6](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | TLS 1.2+ for all external services; encryption at rest for regulated data | TLS 1.3 only; CMK/BYOK for cloud; FIPS 140-2/3 validated modules for CUI; certificate lifecycle automation |
| **Evidence** | TLS configuration scan, encryption-at-rest configuration | Certificate inventory, cipher suite audit, key management audit log |
| **Failure Mode** | Internal traffic unencrypted because "it's inside the firewall"; expired certificates in production; weak cipher suites accepted |
| **Exception Path** | Governance exception for legacy systems with documented retirement plan; compensating controls per [STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| **Engineering Role** | Cryptography deployment; certificate management; key lifecycle |
| **Risk Role** | Cipher suite validation; certificate expiry monitoring |
| **Governance Role** | Encryption policy; FIPS compliance tracking; exception register |

---

## 7 — Segment Networks

**Intent:** Limit lateral movement and blast radius. [CMX-001 §7](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | IT/OT separation; production/non-production separation; Internet-facing DMZ | Microsegmentation; zero-trust network architecture; identity-aware proxies; OT Purdue-model-aligned segmentation |
| **Evidence** | Network diagram, firewall rule review, segmentation test results | Microsegmentation policy coverage, lateral movement test results, OT zone-boundary monitoring |
| **Failure Mode** | Flat network with "the firewall will catch it"; OT/IT boundary documented but not enforced; "temporary" cross-zone rules become permanent |
| **Exception Path** | Governance exception with compensating controls; cross-zone paths reviewed quarterly; auto-expiring firewall rules |
| **Engineering Role** | Network architecture; segmentation design; firewall/ACL management |
| **Risk Role** | Segmentation validation; lateral movement testing; exposed interface discovery |
| **Governance Role** | Segmentation policy; exception tracking; zone-boundary review cadence |

---

## 8 — Manage Vendor and Third-Party Risk

**Intent:** Extend controls beyond the organizational perimeter. [CMX-001 §8](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Vendor inventory with tier assignment; critical vendors assessed annually | Full TPRM pipeline per [TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md): evidence by tier, shared responsibility matrices, SBOM, kill-switch testing, SCCT activation |
| **Evidence** | Vendor register, assessment records for Tier 1-2 | SOC 2/ISO 27001 evidence, shared responsibility matrix, kill-switch test log, SBOM repository |
| **Failure Mode** | Questionnaire-only assessment; vendor risk accepted because "we've always used them"; MSP with standing global admin |
| **Exception Path** | Risk acceptance per RMF-001 §9.7; compensating monitoring for opaque-dependency vendors per [EDG-001](CERG-GOV-EDG-001_Edge_Register.md) |
| **Engineering Role** | Vendor access architecture; kill-switch implementation; PAM integration |
| **Risk Role** | Vendor assessment; evidence collection; SCCT operation; continuous monitoring |
| **Governance Role** | Contract clause library; Approved Provider Catalog; regulatory evidence package |

---

## 9 — Control and Log Privileged Access

**Intent:** Know who did what, when. [CMX-001 §9](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Privileged session logging; admin action audit trail retained 90 days | Full session recording; just-in-time elevation; real-time anomaly detection on privileged actions; SIEM correlation |
| **Evidence** | Privileged access logs, session records | PAM session video/keystroke logs, elevation justification records, anomalous-access alerts |
| **Failure Mode** | Shared admin accounts; "break-glass" used as routine access path; logs stored where admins can delete them |
| **Exception Path** | Governance exception for emergency access; post-hoc review within 24 hours; break-glass activations reviewed quarterly |
| **Engineering Role** | PAM deployment; session recording; log integrity |
| **Risk Role** | Anomalous access detection; privileged user behavior analytics |
| **Governance Role** | Access logging policy; break-glass register; audit evidence retention |

---

## 10 — Conduct Adversarial Testing

**Intent:** Find what scanners miss. [CMX-001 §10](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Annual external penetration test | Continuous adversarial validation: internal/external pen tests, cloud red-team, application pen tests, OT-specific assessment, purple-team detection validation |
| **Evidence** | Pen test report, finding remediation records | Adversarial validation schedule, finding-to-closure pipeline, detection rule validation results |
| **Failure Mode** | Pen test treated as annual compliance checkbox; findings accepted without remediation; only external surface tested |
| **Exception Path** | Risk acceptance for findings that cannot be remediated within SLA; compensating controls verified before acceptance |
| **Engineering Role** | Remediation of adversarial findings; control improvement |
| **Risk Role** | Engagement scoping and execution; finding triage and tracking |
| **Governance Role** | Schedule enforcement; evidence collection; board reporting |

---

## 11 — Train and Background-Check Personnel

**Intent:** Ensure personnel with access to sensitive systems are vetted and trained. [CMX-001 §11](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Background check for privileged users; annual security awareness training | Role-specific training paths; phishing simulation program; certification tracking per [TRN-001](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) |
| **Evidence** | Training completion records, background check status | Training matrix by role, phishing simulation results, certification register |
| **Failure Mode** | Training treated as annual video-compliance exercise; background checks not re-run; contractors exempted |
| **Exception Path** | Conditional access for pre-cleared individuals awaiting background check; supervision required |
| **Engineering Role** | Training platform integration; access tied to training status |
| **Risk Role** | Phishing simulation; insider threat indicators |
| **Governance Role** | Training policy; background check policy; compliance tracking |

---

## 12 — Write and Maintain Policies

**Intent:** Define what good looks like. [CMX-001 §12](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Cybersecurity policy signed by Executive Sponsor; annual review | Full policy hierarchy: policy → standards → procedures → templates; version-controlled; tokenized adaptation per [VAR-001](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) |
| **Evidence** | Signed policy, review records | Policy repository with version history, review cadence tracker, exception register |
| **Failure Mode** | Policy exists as PDF on intranet, never read; review cycle missed for years; policy contradicts operational reality |
| **Exception Path** | Policy exception process per [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md); exceptions tracked with expiration |
| **Engineering Role** | Technical input to standards; architecture alignment with policy |
| **Risk Role** | Risk input to policy appetite statements |
| **Governance Role** | Policy authorship; review cadence; version control; exception workflow |

---

## 13 — Manage Configuration Changes

**Intent:** Track drift, prevent unauthorized changes. [CMX-001 §13](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Change management process for production systems; CAB for security-significant changes | Automated change detection; drift alerts; pre-approved change patterns; CI/CD-integrated security gates |
| **Evidence** | Change records, CAB minutes, approval evidence | Drift detection alerts, automated compliance checks, change-to-baseline reconciliation |
| **Failure Mode** | Emergency changes bypassing process become routine; drift accumulates silently; change records don't match reality |
| **Exception Path** | Emergency change path with post-hoc review within 24 hours; repeated emergency changes on same system trigger finding |
| **Engineering Role** | Change automation; CI/CD security gates; drift remediation |
| **Risk Role** | Drift impact assessment; unauthorized change detection |
| **Governance Role** | Change policy; CAB operation; evidence collection for audit |

---

## 14 — Collect, Protect, and Retain Audit Evidence

**Intent:** Prove controls are working. [CMX-001 §14](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Evidence collected for each control; stored securely; retained per regulatory requirement | Evidence library with automated collection; evidence linked to control baseline per [CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md); freshness tracking |
| **Evidence** | Evidence library index, sample evidence artifacts | Evidence freshness dashboard, control-to-evidence traceability matrix, auditor access log |
| **Failure Mode** | Evidence scramble before audit; evidence exists but isn't linked to specific controls; evidence stale (collected once, never refreshed) |
| **Exception Path** | Missing evidence documented as control gap; POA&M entry for CUI environments |
| **Engineering Role** | Evidence-producing automation; tooling integration |
| **Risk Role** | Evidence validation; sampling-based quality checks |
| **Governance Role** | Evidence library management; retention policy; audit response coordination |

---

## 15 — Assess Your Own Security Posture

**Intent:** Periodic internal evaluation — don't wait for auditors. [CMX-001 §15](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Annual self-assessment against control baseline | Continuous control monitoring; quarterly maturity assessment per [MAT-001](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md); automated control testing |
| **Evidence** | Self-assessment results, remediation plans | Control effectiveness ratings, maturity scorecard, continuous monitoring dashboard |
| **Failure Mode** | Self-assessment becomes self-congratulation; no independent validation; findings not tracked to closure |
| **Exception Path** | Assessment findings enter risk register per PRC-RM-001; treatment tracked per RMF-001 |
| **Engineering Role** | Control implementation evidence; technical validation |
| **Risk Role** | Independent control testing; adversarial validation of controls |
| **Governance Role** | Assessment methodology; scoring rubric; finding tracking |

---

## 16 — Manage Risk Formally

**Intent:** Document, accept, or treat identified risks. [CMX-001 §16](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Risk register with owner, severity, treatment, and review date per [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Quantitative risk scoring (LEF × LM); risk appetite calibration; board-level risk reporting; business-owner acceptance at every tier per [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 |
| **Evidence** | Risk register, treatment plans, acceptance records | Risk appetite statement, quantitative ALE dashboard, acceptance authority log |
| **Failure Mode** | Risk register as parking lot — risks recorded, never treated; acceptance without compensating controls; renewal without re-evaluation |
| **Exception Path** | Risk acceptance per RMF-001 §9.7; business owner accepts; renewals require fresh approval cycle |
| **Engineering Role** | Treatment implementation; compensating control design |
| **Risk Role** | Risk identification; scoring; treatment recommendation |
| **Governance Role** | Register curation; acceptance workflow; board reporting |

---

## 17 — Protect Physical Access

**Intent:** Cyber starts at the door. [CMX-001 §17](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Badge access for data centers; visitor logging; camera coverage of critical facilities | Multi-factor physical access; zone-based access control; integration with logical access (badge-out = session termination); OT substation physical security |
| **Evidence** | Access logs, visitor register, camera coverage map | Physical access review records, zone-access matrix, integration test results |
| **Failure Mode** | Physical security treated as "facilities problem" not cyber concern; tailgating accepted; contractor physical access not reviewed |
| **Exception Path** | Governance exception for temporary physical access; escort required; time-bound |
| **Engineering Role** | Physical security system integration; badge-to-logical-access correlation |
| **Risk Role** | Physical access anomaly detection; critical facility risk assessment |
| **Governance Role** | Physical access policy; review cadence; evidence collection |

---

## 18 — Monitor Threats Continuously

**Intent:** Detect what vulnerability scans miss. [CMX-001 §18](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | SIEM with critical log sources; alerting for known-bad indicators | Full detection engineering pipeline: log source onboarding per [STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), detection rules, purple-team validation, threat intelligence integration |
| **Evidence** | SIEM coverage report, alert response metrics | Detection coverage by MITRE ATT&CK technique, purple-team pass rate, threat intel feed integration status |
| **Failure Mode** | SIEM as log dump — everything collected, nothing tuned; alert fatigue → alerts ignored; detection rules never validated |
| **Exception Path** | Log source gap documented with compensating monitoring; reviewed quarterly |
| **Engineering Role** | Log source integration; detection rule development |
| **Risk Role** | Threat intelligence; detection validation; alert triage |
| **Governance Role** | Logging policy; coverage reporting; retention compliance |

---

## 19 — Plan and Practice Incident Response

**Intent:** Know what to do before it happens. [CMX-001 §19](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | IR plan with roles, contact list, and escalation path; annual tabletop exercise | Full IR playbooks by incident type; quarterly tabletop; annual live-fire exercise; SCCT activation path per [TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Evidence** | IR plan, tabletop results, after-action reports | Exercise schedule, improvement tracking, playbook version history, SCCT test records |
| **Failure Mode** | IR plan exists as PDF, never exercised; contact list stale; "the IR team will handle it" without defined handoff |
| **Exception Path** | No exception path; incident response capability is mandatory and gaps are treated as Critical findings |
| **Engineering Role** | IR tooling; forensic capability; containment automation |
| **Risk Role** | Detection-to-IR handoff; threat intelligence during incidents |
| **Governance Role** | IR plan maintenance; exercise schedule; after-action improvement tracking |

---

## 20 — Manage Recovery and Lessons Learned

**Intent:** Restore operations and capture what was learned. [CMX-001 §20](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Backup and restore procedures for critical systems; annual restore test | RTO/RPO defined per system tier; automated backup validation; restoration test schedule per [STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md); lessons-learned pipeline to standards feedback |
| **Evidence** | Backup success reports, restore test results, lessons-learned records | RTO/RPO compliance dashboard, automated backup validation, improvement record linkage to standards updates |
| **Failure Mode** | Backups exist but restore never tested; lessons learned documented but never acted on; same incident repeats |
| **Exception Path** | Restoration gap documented as risk; compensating manual procedure defined; tested quarterly |
| **Engineering Role** | Backup architecture; restore automation; resilience engineering |
| **Risk Role** | Recovery risk assessment; single-point-of-failure identification |
| **Governance Role** | BC/DR policy; test schedule enforcement; lessons-learned feedback loop |

---

## 21 — Manage Accounts Throughout Their Lifecycle

**Intent:** Provisioning through termination — no orphaned access. [CMX-001 §21](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Joiner/mover/leaver process; access removed within 24 hours of termination | Automated identity lifecycle; HRIS-integrated provisioning/de-provisioning; access recertification per [STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **Evidence** | Termination tickets, access removal confirmation | Identity lifecycle automation log, recertification status dashboard, orphaned account report |
| **Failure Mode** | Manual de-provisioning — "we'll get to it"; contractor accounts not tracked; service accounts with no owner |
| **Exception Path** | Conditional retention of access for knowledge transfer; time-bound (max 30 days); supervisor approval required |
| **Engineering Role** | Identity lifecycle automation; HRIS integration |
| **Risk Role** | Orphaned account detection; dormant account monitoring |
| **Governance Role** | Access lifecycle policy; recertification schedule; audit evidence |

---

## 22 — Define and Enforce a Compliance Calendar

**Intent:** No surprises at audit time. [CMX-001 §22](CERG-GOV-CMX-001_Compliance_Matrix.md)

| | Minimum Viable | Good Implementation |
|---|---|---|
| **Implementation** | Annual calendar of compliance activities; evidence collected throughout the year | Continuous compliance monitoring; evidence auto-collection; regulatory mapping per framework; pre-audit readiness review 60 days before engagement |
| **Evidence** | Compliance calendar, activity completion records | Evidence freshness dashboard, framework-to-control mapping, pre-audit readiness report |
| **Failure Mode** | Pre-audit scramble; evidence collected once and never refreshed; calendar exists but activities not tracked to completion |
| **Exception Path** | Missed activity documented as finding; compensating evidence identified where possible; entered in improvement register |
| **Engineering Role** | Evidence-producing automation; control implementation |
| **Risk Role** | Continuous control monitoring; independent validation |
| **Governance Role** | Calendar ownership; activity tracking; evidence library; audit liaison |

---

## 23 — Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.1 | 2026-06-18 | Governance Pillar Leader | Reframed cards as security-intent adoption paths and added the maturity lens for agents and adopters. |
| 1.0 | 2026-06 | CERG Governance | Initial release. 22 implementation cards mapping security intents to actionable implementation guidance. |

### Review Triggers

Annual review or upon material change to the control baseline, compliance matrix, or CERG operating model.

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Compliance Matrix | CERG-GOV-CMX-001 | Source of the 22 intents |
| Control Baseline | CERG-GOV-CB-001 | Controls referenced by implementation cards |
| Architecture Review Procedure | CERG-PRC-AR-001 | Pre-approved patterns referenced |
| Exposure Management Procedure | CERG-PRC-VM-001 | Intent 2 operational implementation |
| TPRM Procedure | CERG-PRC-TPRM-001 | Intent 8 operational implementation |
| Risk Management Framework | CERG-GOV-RMF-001 | Risk acceptance authority |
| Edge Register | CERG-GOV-EDG-001 | Edge management for vendor/network intents |

---
>
> _An intent without implementation guidance is governance poetry. These cards make the intents actionable._

---

_CERG-GOV-IMP-004 · Version 1.1 · PUBLIC_
