# Task B02 Output: Test pillar boundaries against adjacent functions

## Scope Reviewed
- Files read:
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md` §§3.4 and 8
  - `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md` incident and adjacent-role sections
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` F-06 and adjacent references
  - `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
  - `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
  - `plans/CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md`
  - `plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md`
  - day-in-the-life Story 3, Story 6, Story 8, Story 9, and Story 10 material in `examples/day-in-the-life/`
- Sections reviewed: ownership boundary sections, interface tables, incident activation/notification/exercise sections, privacy and BCP boundary tables, incident-support roles, day-in-the-life audit/vendor incident examples.
- Files intentionally not reviewed: full Legal, HR, Procurement, Facilities, Awareness, and Enterprise Risk charters because CERG only contains interfaces to those functions, not their owned program artifacts.

## Method
- Steps performed:
  1. Listed every adjacent function named in the operating model, IR, privacy, BCP, and example material.
  2. For each adjacent function, mapped what CERG provides, consumes, does not own, handoff record, and escalation authority.
  3. Tested whether adjacent functions are accidentally treated as CERG-owned.
  4. Verified IR document lifecycle status and ownership treatment against project rules.
  5. Checked whether Adjunct roles appear only as interfaces unless the artifact is explicitly an IR-family interface artifact.
- Search terms or scripts used: targeted reads and scans for `adjacent`, `Incident Commander`, `notification clock`, `exercise`, `Security Awareness`, `Privacy`, `Business Continuity`, `Legal`, `Enterprise Risk`, `OT Operations`, `Business Owner`, and `External Interface`.
- Assumptions avoided: did not treat all CERG support activity as ownership. The test distinguished support, evidence, and coordination from command authority or program ownership.

## Boundary Map

| Adjacent function | What CERG provides | What CERG consumes | What CERG does not own | Handoff record | Escalation authority |
|---|---|---|---|---|---|
| Incident Response / standing IR team | Asset context, data classification, control evidence, logging posture, recovery dependencies, risk history, vendor context, post-incident findings, control changes, evidence preservation. | Incident declaration, severity, affected scope, status updates, lessons learned, post-incident corrective-action triggers. | Incident command, active response decisions, IR plan, notification decisions, regulatory notification clocks, exercise management. | Incident Record, incident timeline, Post-Incident Summary, Improvement Record, risk-register entry. | Incident Commander during active response; CISO for material escalation; Legal for privileged/legal decisions. |
| Security Awareness | Policy content, procedure content, threat intelligence themes, examples from project work, phishing/themed risk context. | Training completion, phishing simulation metrics, user-reporting trends, awareness campaign outputs. | Awareness program ownership, training delivery strategy, culture campaign ownership. | Training completion report, phishing simulation result, awareness metrics feed. | Awareness program owner under CISO oversight; CISO for program-level gaps. |
| Privacy / DPO / Legal privacy process | Data inventory, data classification, asset and vendor facts, DPIA support, DSR technical support, breach facts, evidence, privacy-related risk entries. | Privacy-law interpretation, lawful basis/notice/consent decisions, DSR validity decisions, privacy regulator decisions. | Legal interpretation of privacy law, privacy notices, consent, lawful basis, data subject request decisioning, privacy regulator communications. | Privacy data inventory, DPIA record, DSR support evidence, breach support evidence, privacy risk/exception record. | Enterprise legal/privacy process; Incident Commander and Legal during breach events; CISO for material privacy-security risk acceptance. |
| Business Continuity / Enterprise BCP | Cyber recovery controls, backup and restore evidence, asset dependencies, data classification, residual risk, degraded-operation evidence. | Business impact analysis priorities, crisis declaration, process criticality, manual workaround decisions, business recovery sequencing. | Enterprise business-continuity program, business process priority decisions, enterprise crisis communications, manual/degraded process ownership. | BIA record, recovery runbook, activation record, recovery decision log, DR exercise package, risk acceptance or exception. | Enterprise BCP/crisis process; CISO when cyber-led; Business Owner for process criticality. |
| Legal | Facts, evidence, data classification, incident timeline support, contractual/security control facts, risk context. | Privilege decisions, legal interpretation, statutory and contractual notification advice, law enforcement strategy. | Legal advice, privilege determinations, statutory interpretation, legal notices. | Legal decision log, privileged work-product labels, regulatory/customer notification package. | General Counsel or delegated legal lead. |
| Enterprise Risk Management | Cyber risk feed, COG materials, register summaries, material risk escalation, treatment status. | Enterprise risk appetite, cross-functional treatment decisions, business risk context. | Enterprise risk framework and non-cyber risk ownership. | COG agenda/materials, risk register report, board/cross-functional action item. | Cyber Oversight Group, Enterprise Risk lead, CISO. |
| Internal Audit / external auditors / assessors | Evidence index, audit packages, control testing results, findings and corrective-action tracking. | Audit requests, testing criteria, evidence sufficiency feedback, findings. | Auditor independence, audit conclusions, external assessment decisions. | Audit request ticket, evidence package, control test worksheet, POA&M/finding record. | Governance Pillar Leader for response coordination; auditor/assessor for assessment outcome. |
| Procurement / Vendor Management | Vendor security tiering, control evidence, contract security clauses, third-party risk findings. | Business criticality, procurement workflow, contract process, vendor contacts. | Commercial procurement process, final vendor business selection, non-security contract ownership. | Vendor assessment record, shared responsibility matrix, contract clause review, vendor risk record. | Vendor Risk Analyst for cyber assessment; Procurement lead for sourcing; CISO for material security exception. |
| IT Operations | Secure designs, standards, baselines, change security routing, vulnerability/remediation guidance, evidence requirements. | Implementation capacity, system administration facts, operational constraints, change windows. | Day-to-day IT service ownership outside CERG-owned security platforms. | Change Record, remediation evidence, asset record, configuration baseline. | Engineering Pillar Leader for security architecture; IT operations leadership for operational execution. |
| OT Operations / reliability operations | OT security design, CIP evidence, risk context, OT-safe vulnerability methods, recovery control support. | Grid-impact judgments, maintenance windows, operational safety constraints, reliability decisions. | Grid operations, safety/running-state decisions, operational reliability authority. | OT maintenance window record, CIP evidence record, asset/coverage record, risk/exception record. | OT operations supervisor/lead for operational impact; CISO/Governance for regulatory/security escalation. |
| Physical Security / Facilities | Cyber requirements where CIP-006/PE-family or cyber-physical controls apply, evidence mapping, risk entries. | Facility access facts, physical control operation, facilities incident inputs. | Non-cyber physical security program and facilities controls outside cyber scope. | Physical access evidence, CIP-006 evidence, risk or finding record for cyber-relevant gap. | Facilities/Physical Security leadership; NERC-CIP Compliance Manager for regulated evidence. |
| Human Resources | Personnel security requirements, JML control evidence, contractor integration requirements, disciplinary referral facts for willful non-compliance. | HRIS events, employment status, role changes, training assignment data, HR process decisions. | Employment decisions, HR investigations, disciplinary process, corporate training operations outside cyber awareness. | JML record, personnel risk assessment, contractor role map, access removal evidence. | HR leadership; CISO for security-risk escalation. |
| Internal Communications / PR | Technical facts, approved incident-status facts, security program updates. | Communication timing, messaging channels, public/internal communication strategy. | Public relations, workforce broadcast content ownership, media handling. | Incident communication approval record, workforce broadcast, public statement record. | Incident Commander and Legal during incidents; Communications/PR lead for messaging. |
| Business Owners / Executive Sponsors | Risk analysis, treatment options, evidence, exception/risk-acceptance packages, decision records. | Business impact, funding decisions, criticality, risk acceptance/concurrence, process ownership. | Business consequence ownership and acceptance decisions. | Risk Acceptance Memo, Exception Record, Decision Log, COG action item. | Business Owner/Executive Sponsor; CISO for high/material risk per RMF. |
| Board / executive leadership | Posture metrics, material risk reporting, regulatory overlays, decision options, budget/risk tradeoffs. | Risk appetite, funding decisions, governance expectations, oversight challenge. | Day-to-day control implementation, operational triage, evidence curation. | Board cyber brief, COG package, metrics dashboard, authorizing decision. | CISO to board/executive forum. |

## IR External Interface Verification

| Artifact | Header status | Header owner | Boundary banner | Body consistency | Result |
|---|---|---|---|---|---|
| `CERG-PLN-IR-001` | External Interface | Standing IR Team / Incident Commander | Strong: not CERG-owned, IC authority supersedes CERG workflows, CERG supports only. | Mixed: several body/footer statements assign Governance ownership of notification clocks, exercises, and document ownership. | Fails consistency check. |
| `CERG-PRC-IR-002` | External Interface | Standing IR Team / Incident Commander | Strong: not CERG-owned, CERG support and handoff only. | Mixed: footer says Cyber Governance owns the playbook set; exercise design is assigned to Governance. | Fails consistency check. |

## Findings

### B02-F01 Critical IR documents contradict the Operating Model on notification-clock and exercise ownership
Affected files:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`

Problem: OM-001 §3.4 and both IR banners state that CERG does not own Incident Response operations, the IR plan, regulatory notification clocks, or exercise management. But the IR plan body assigns the Governance Pillar Leader or Governance Lead ownership of the regulatory notification clock, and §11 assigns tabletop/exercise activities to Governance and Risk. PRC-IR-002 §2.2 assigns exercise design to the Governance Pillar Leader in coordination with the Incident Commander.

Why it matters: This is the exact adjacent-function failure the plan warned about. During an incident, a reader could conclude that CERG Governance owns notification-clock management or IR exercise management, while the operating model says the standing IR team owns those responsibilities. That could cause the wrong role to be accountable during a regulatory deadline.

Evidence from corpus:
- OM-001 §3.4: CERG does not own regulatory notification clocks or exercise management.
- IR plan banner: CERG's role is supporting, not directing; changes to notification timelines or exercise schedules are the IR team's responsibility.
- IR plan §3.1: `Governance Pillar Leader` owns the regulatory notification clock.
- IR plan §6: `Governance Lead owns the notification clock for each in-flight incident`.
- IR plan §11: tabletop exercises and contact roster/retainer tests are owned by Governance and/or Risk.
- PRC-IR-002 §2.2: exercises are designed by the Governance Pillar Leader in coordination with the Incident Commander.

Recommended action: Rewrite IR body language to distinguish support from ownership. Suggested rule: the Incident Commander/standing IR team owns the notification-clock process and exercise program; CERG Governance maintains the notification register/evidence package at IC and Legal direction. Exercise rows should show `Standing IR Team / Incident Commander` as owner, with Governance/Risk as support where appropriate.

Owner/workstream: Adjacent Functions / IR boundary.

### B02-F02 High IR document-control footers conflict with External Interface ownership treatment
Affected files:
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`

Problem: Both IR artifacts have External Interface metadata and Standing IR Team / Incident Commander ownership at the top. Later control/footer language reassigns document ownership or maintenance to Cyber Governance/Governance Pillar Leader. The IR plan says, `Cyber Governance owns the plan as a document. The CISO owns the operational capability the plan describes.` PRC-IR-002 says, `Cyber Governance owns this CERG-facing playbook set.`

Why it matters: Project rules require IR documents to be External Interface, owned by Standing IR Team / Incident Commander. Footer ownership drift weakens that model and creates two apparent owners for the same artifact.

Evidence from corpus:
- IR plan metadata: Status `External Interface`; Owner `Standing IR Team / Incident Commander`.
- IR plan banner: maintained by the standing IR team; CERG Governance reviews cross-reference accuracy only.
- IR plan Plan Control: Cyber Governance owns the plan as a document.
- PRC-IR-002 metadata: Status `External Interface`; Owner `Standing IR Team / Incident Commander`.
- PRC-IR-002 Document Control: Cyber Governance owns the playbook set.

Recommended action: Align footer/control sections to the header and banner. Use language such as: `The Standing IR Team / Incident Commander owns this External Interface artifact. CERG Governance may maintain repository links and cross-reference hygiene on behalf of the owner, but IR procedure content changes require Standing IR Team owner concurrence.`

Owner/workstream: Adjacent Functions / Document Control.

### B02-F03 Medium Security Awareness boundary is stated but not operationalized
Affected files:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-FRM-001_CERG_Framework.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`

Problem: Security Awareness is named as adjacent and separate, but its boundary is less executable than IR, Privacy, and BCP. OM-001 says Awareness program ownership is separate, while OM-001 §8 says Risk provides phishing simulation operations and threat-actor context. There is no equivalent boundary table defining what CERG provides, consumes, does not own, the handoff record, or escalation authority.

Why it matters: Awareness is one of the functions explicitly excluded from CERG's three-pillar scope. Without an operational boundary, CERG could drift into owning awareness operations or readers could treat phishing simulation results as Risk-owned program operations rather than an Awareness-owned program feed.

Evidence from corpus:
- FRM-001 §2.1 names Security Awareness as adjacent.
- OM-001 §3.4 excludes Security Awareness program ownership.
- OM-001 §8 says Risk provides phishing simulation operations and threat-actor context for targeted campaigns.
- No `PLN-AWARE` or boundary table equivalent appears in the loaded corpus.

Recommended action: Add a short Awareness interface table to OM-001 §8 or a future adjacent-interface appendix: CERG provides policy content, threat themes, metrics interpretation, and evidence requirements; Awareness owns campaign/training execution and phishing simulation operations; handoff records are training completion reports, phishing simulation result feeds, and awareness improvement items.

Owner/workstream: Adjacent Functions / Awareness.

### B02-F04 Medium Incident-support severity labels drift between Sev and P notation
Affected files:
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Problem: The IR plan uses `Sev 1` through `Sev 4`. FLOW-001 uses `P1` through `P4`. PRC-IR-002 maps P1-P4 to Sev 1-4, which helps, but the corpus mixes the notation across adjacent and CERG flow documents.

Why it matters: This is not a conceptual contradiction because PRC-IR-002 provides a mapping. It is a usability issue during incidents, when readers need severity labels to be instantly unambiguous.

Evidence from corpus:
- IR plan §5 uses `Sev 1 - Critical` through `Sev 4 - Minor`.
- FLOW-001 F-06 uses `P1 - Critical` through `P4 - Low`.
- PRC-IR-002 §3.2 states `P1 = Sev 1`, `P2 = Sev 2`, and so on.

Recommended action: Pick one label as canonical for incident severity, or require every incident-facing document to show the paired label in headings and tables, e.g., `P1 / Sev 1 - Critical`.

Owner/workstream: Adjacent Functions / IR usability.

## Positive Confirmations
- Privacy boundary is strong. `PLN-PRIV-001` clearly says CERG does not replace legal, privacy, or records-management programs and limits CERG to cyber/data/vendor/evidence machinery.
- Business continuity boundary is strong. `PLN-BC-001` clearly separates Enterprise BCP/business process decisions from CERG cyber recovery controls, risk, and evidence.
- Business ownership is conceptually strong. CERG supplies risk facts and evidence; the business owns consequence, criticality, funding, and residual-risk decisions.
- OT operations are treated as an authority boundary, not just a technical environment. IR and BCP materials defer to operations on operational/safety impact.
- PRC-IR-002 has a strong opening boundary statement: `CERG does not command the incident. CERG makes the incident runnable.` That sentence should be preserved.
- Adjunct IR roles, Incident Commander and Lead Investigator, are used mainly in IR-facing contexts and RAC/GEN cross-references, which is appropriate.

## Open Questions
- Should IR notification-clock ownership be phrased as `IC/Legal own the notification decision; Governance maintains the notification register and evidence package` across all documents?
- Should Security Awareness receive a small External Interface package, or is an OM-001 interface table sufficient?
- Should incident severity labels standardize on `P` or `Sev`, or should every incident-facing artifact carry paired notation?
- Should the IR plan remain in the repository as an External Interface artifact if the standing IR team is external to CERG, or should it be represented as a reference stub with links/expected interfaces only?

## Proposed Next Tasks
- B03: authority register, with IR ownership and risk acceptance as high-priority authority concepts.
- C01: flow trace, with F-06 tested carefully after the IR boundary repair decision.
- G02/G03: create exact rewrite tasks for the IR plan and IR playbook document-control/notification/exercise sections.
