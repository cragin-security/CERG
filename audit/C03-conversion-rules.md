# Task C03 Output: Test exception, risk acceptance, and finding conversion rules

## Scope Reviewed
- Files read:
  - `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
  - `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
  - `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
  - `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
  - `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md` where project/pre-production findings are referenced
  - `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md` where audit/evidence findings are referenced
  - `procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md` where incident lessons become improvements
  - `templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md`
  - `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md`
  - `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`
  - `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
  - Relevant findings from `audit/B03-authority-centers.md`, `audit/C01-flow-trace.md`, and `audit/C02-execution-chain.md`
- Sections reviewed:
  - GEN-001 canonical terms, record types, and conversion rules.
  - FLOW-001 F-04 and conversion rules, F-06 incident feedback, and SLA exception logic.
  - RMF-001 risk scoring, risk acceptance authority, acceptance review/expiration triggers, and appetite calibration.
  - PRC-RM risk register workflow, exception workflow, acceptance routing, approval table, and metrics.
  - PRC-VM observation/exposure classification, treatment options, acceptance/exception distinction, and PPR rule.
- Files intentionally not reviewed:
  - Every individual standard that can originate a finding. C03 tests the conversion vocabulary and decision paths, not each source domain.
  - Full day-in-the-life story scoring. Example quality is handled in E01/E03, though known Story 4 wording is carried forward.

## Method
- Steps performed:
  1. Extracted canonical definitions and conversion rules from GEN-001, FLOW-001, PRC-VM, PRC-RM, RMF, and RM templates.
  2. Compared the definitions for contradictory triggers, record names, authority paths, and expiration behavior.
  3. Classified the eight required scenarios into records, decision paths, and approver paths.
  4. Flagged cases where the corpus produces more than one plausible answer.
- Search terms or scripts used: targeted reads and scans for `finding`, `vulnerability`, `risk`, `exception`, `risk acceptance`, `accepted residual`, `control gap`, `incident`, `expires`, `expired`, `monitor`, `PPR`, `Business Owner`, and `CISO`.
- Assumptions avoided:
  - Did not assume `risk acceptance` and `exception` are interchangeable. The corpus explicitly separates them.
  - Did not assume every finding becomes a risk. PRC-VM and GEN both allow direct remediation without risk promotion.
  - Did not treat IR records as CERG-owned where the adjacent-function model says the standing IR team owns incident operations.

## Conversion Decision Table

| Starting condition | Canonical classification | Primary record | Converts / promotes when | Approver / accountable path | Current clarity |
|---|---|---|---|---|---|
| Raw scanner, SAST, CSPM, SBOM, advisory, or intel signal | Observation / vulnerability signal, not yet a finding | Exposure pipeline / source observation | Becomes Finding only after validation/triage confirms in-scope condition requiring disposition | Exposure Management Lead validates; Engineering supports technical confirmation | Mostly clear; GEN says vulnerability becomes finding when triaged, PRC-VM says no SLA until classification. Align wording. |
| Validated observed condition requiring disposition | Finding | Finding Record / Exposure Backlog Item | Promotes to Risk when SLA exceeded, Tier 0/1, active exploitation, business decision required, compensating controls needed, recurring/systemic, or regulatory deviation | Risk owns finding; Engineering treats; Governance routes exception/acceptance if needed | Clear concept; FLOW F-04 closure rules conflict internally. |
| Loss-event scenario with owner/treatment | Risk | Risk Register Entry / Risk Record | May create Exception if a control/standard deviation is involved; may produce Risk Acceptance if residual risk is intentionally accepted | Risk assesses; Business Owner owns consequence; CISO/Exec per RMF/PRC-RM severity | Clear except scoring drift and template drift. |
| Control/standard cannot be met as written or by deadline | Security Exception | Security Exception Record + linked Risk Register Entry | Expiration without renewal auto-creates High Finding; repeated renewal escalates one approval tier | Governance owns workflow; Risk assesses; Engineering validates controls; Business Owner signs if residual risk > Low | Strong in PRC-RM/TMPL-RM-002. |
| Residual risk is intentionally accepted within appetite | Risk Acceptance | Risk Register accepted status + TMPL-RM-004 acceptance form | Expiration/review trigger should either renew, treat, or create High Finding; threat/regulatory/incident changes force re-score | Business Owner at all levels; CISO for High; CISO + Executive Sponsor for Critical | Strong in RMF/TMPL-RM-004, but GEN/TMPL-RM-003 stale. |
| Missing or ineffective control, systemic condition | Control Gap | Finding Record or Risk Register Entry; POA&M where regulated | Usually Risk if systemic; Exception if temporary deviation; Control Change or Improvement if program/control baseline change required | Depends on source: Governance for control baseline/evidence, Engineering for implementation, Risk for exposure scenario | Medium clarity; needs record-choice rule. |
| Declared security event | Incident | Incident Record owned by Incident Commander / standing IR team | Lessons may create Findings, Risks, Control Change Records, or Program Improvement Records | IR owns incident; CERG supports root cause, evidence, reporting, and improvement routing | Conceptually clear; F-06 owner wording conflicts. |
| Monitor-only condition | Monitoring state / no current acceptance, if no control deviation and no business acceptance needed | Finding/Risk notes or exposure pipeline state | Converts to Risk Acceptance if the organization chooses to live with residual business risk; Exception if control deviation exists | Risk documents monitoring criteria; Business Owner accepts if risk is accepted | Weak definition; `Monitor only` needs guardrails. |

## Scenario Classifications

| Scenario | Correct classification | Record path | Approver path | Ambiguity / issue |
|---|---|---|---|---|
| Critical CVE on internet-facing system with public exploit | PRC-VM: observation → validated condition → Confirmed Exposure or Material Risk / PPR if KEV, active exploitation, or crown-jewel context. FLOW: Finding; promote to Risk due active exploitation/Tier 0/1/business urgency. | Exposure pipeline observation; Finding Record; Risk Record if PPR/active exploitation/crown jewel/SLA breach; emergency Change Record if remediation bypasses normal change; Incident Record if exploitation is occurring internally. | Treatment is urgent. PRC-VM says PPR-tier exposures are not eligible for risk acceptance except OT windowing. CISO notified if past SLA or incident invoked. | Needs explicit precedence: PRC-VM PPR no-acceptance rule overrides generic Critical risk acceptance table. |
| OT patch deferred to maintenance window | Confirmed exposure/flaw with OT maintenance-window overlay; may be risk acceptance, security exception, and/or CIP deviation depending BES scope and control deviation. | Finding/Exposure record; Risk Record if SLA/window exceeds tolerance; Exception Record if control/SLA deviation; CIP deviation/mitigation plan for BES; Change Record for maintenance implementation. | Business/Asset Owner owns operational consequence; CISO approves High/Critical acceptance; NERC-CIP Compliance Manager/Governance coordinates BES deviation; Operations leadership signs reliability tradeoff where applicable. | Strong but complex. Needs a single OT scenario note showing when exception vs risk acceptance vs CIP deviation run together. |
| Vendor cannot patch a SaaS control gap | Vendor-responsible control gap and/or inherited-control failure; Finding stays open against provider if Tier 1 SaaS posture drift; Risk Record if business exposure remains; Exception if CERG control requirement cannot be met. | Vendor Risk Assessment Record; Finding Record or Exposure Backlog Item; Risk Register Entry; Security Exception Record if control deviation; Shared Responsibility Matrix / Inheritance Evidence Package; possible SCCT if vendor incident. | Vendor Risk Analyst assesses; Business Owner accepts residual vendor risk; CISO if High/Critical; Governance for exception documentation. | Clear in pieces, but SaaS/SBOM templates are not invoked in PRC-TPRM (C02). |
| Audit evidence missing for an access review | Evidence deficiency/control-test issue. It is a Finding if evidence is missing/stale and control relies on it; Risk if residual control failure remains or pattern is systemic; POA&M if regulated/CUI. | Audit intake/control test record; Finding Record or corrective action; Evidence Index Entry; Risk Record if residual risk remains; POA&M if CUI. | Evidence Librarian/Governance manages evidence issue; control owner fixes; Risk Register Owner creates risk where residual exposure remains; regulated owner signs POA&M path. | Mostly clear. Control deficiency vs evidence deficiency could use a small conversion table in PRC-AUD/CAT-002. |
| Accepted risk expires | Should become invalid acceptance requiring renewal/treatment; GEN/FLOW say auto-create High Finding if not renewed. | Risk Register Entry changes from Accepted to overdue/expired; High Finding Record auto-created; acceptance form renewal or treatment plan opened. | Original acceptance approver notified; Business Owner must re-accept; CISO/Executive Sponsor per severity. | PRC-RM says no acceptance expires automatically and every acceptance requires fresh approval, but is less explicit than GEN/FLOW about auto-creating the High Finding. |
| Exception expires | Invalid exception; High Finding and open control gap. | Exception Record status expired/invalid; Finding Record severity High; linked Risk Register Entry; POA&M/CIP deviation if regulated. | Governance/Risk Register Owner warning chain; renewal requires fresh approval; repeated renewals escalate one approval tier. | Strong. |
| Incident creates lessons learned | Incident remains an IR-owned event; lessons may create CERG findings, risks, control changes, or improvements. | Incident Record; Lesson Artifact; Lessons Aggregation Summary; Program Improvement Record; Finding/Risk/Control Change Record as needed. | Incident Commander owns incident artifact; Governance triages lesson; Risk/Engineering own resulting actions; CISO for Critical lessons. | Strong concept, but F-06 text still conflicts on active incident ownership. |
| Recurring misconfiguration appears across systems | Recurrent Finding; systemic control gap; likely Risk Record and Control Change/Improvement. | Finding Records; root-cause Finding; Risk Register Entry; Control Change Record (F-01); Program Improvement Record if process/standard/tooling change needed. | Risk escalates recurrence; Engineering fixes root cause; Governance routes control/standard change; CISO if systemic High/Critical. | Strong in FLOW/LL/IMPREG, but F-03/F-05 should add explicit feedback paths for recurring coverage/change patterns. |

## Findings

### C03-F01 High Risk Acceptance definition still points to stale template authority
Affected files:
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`
- `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Problem: GEN-001 defines `Risk Acceptance` and cites TMPL-RM-003 as the source. PRC-RM and TMPL-RM-004 now define the stronger canonical model: Business Owner accepts business consequence; approval follows RMF §9.7; TMPL-RM-004 is the required acceptance form. TMPL-RM-003 omits a Business Owner approval row and is therefore stale or incomplete.

Why it matters: The glossary is where readers go when terms are ambiguous. If it points to the stale template, users can bypass the core business-owner accountability rule.

Evidence from corpus:
- GEN-001 §3: Risk Acceptance source is TMPL-RM-003.
- PRC-RM §7.1 and §7.6 route Risk Acceptance to TMPL-RM-004.
- TMPL-RM-004 requires Business Owner acceptance and RMF §9.7 authority.
- TMPL-RM-003 approval table lacks Business Owner.

Recommended action: Make RMF-001 §9.7 + PRC-RM §7.1 + TMPL-RM-004 the canonical acceptance path. Update GEN-001 to point there. Retire TMPL-RM-003 or convert it into a low/medium memo that still requires Business Owner acceptance.

Owner/workstream: Risk / Glossary / Templates.

### C03-F02 High PPR-tier exposure acceptance rule needs explicit precedence over generic Critical acceptance authority
Affected files:
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Problem: PRC-VM states PPR-tier exposures are not eligible for risk acceptance except OT operational windowing scenarios where the CIP deviation path is the sole approved path. PRC-RM/RMF provide generic Critical risk acceptance authority with CISO + Executive Sponsor / board notification. Both can be true, but the precedence is not stated where a reader handling a critical internet-facing active exploit would look.

Why it matters: A reader could incorrectly conclude that a PPR-tier active exploit may be accepted through the generic Critical acceptance table. For active exploitation, that would undermine the exposure-management model.

Evidence from corpus:
- PRC-VM §11.2: PPR-tier exposures are not eligible for risk acceptance except OT windowing.
- PRC-RM §8 allows Critical acceptance through CISO + Executive Sponsor / board notified.
- FLOW F-04 lists formal risk acceptance as an allowed treatment path for findings without carving out PPR-tier exposures.

Recommended action: Add a precedence sentence to PRC-RM, RMF, and FLOW F-04: `PRC-VM PPR-tier no-acceptance rule governs active exploitation / PPR exposures; generic Critical acceptance authority applies only where the source procedure allows acceptance.`

Owner/workstream: Risk / Exposure Management.

### C03-F03 High Risk scoring and acceptance authority are coupled, but RMF and PRC-RM scoring bands still differ
Affected files:
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md`

Problem: Risk acceptance authority depends on Low/Medium/High/Critical residual risk bands. B03 found that RMF and PRC-RM carry different likelihood/impact calibration tables. C03 confirms this affects conversion outcomes: a finding promoted to risk may land in a different approval path depending on which scoring table the operator uses.

Why it matters: Conversion rules are only precise if the scoring model is stable. Approval authority, reporting, and acceptance treatment all depend on severity.

Evidence from corpus:
- RMF says its scoring model is canonical and every scoring document should produce the same severity.
- PRC-RM still has different numeric impact/probability anchors.
- TMPL-RM-001 contains its own examples and approval bands.

Recommended action: Use RMF as canonical. Replace PRC-RM and TMPL-RM-001 scoring tables with exact copies or concise cross-references to RMF; preserve operational examples only if they cannot drift.

Owner/workstream: Risk / Scoring calibration.

### C03-F04 Medium Vulnerability-to-finding wording differs between GEN/FLOW and PRC-VM's observation-state model
Affected files:
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`

Problem: GEN/FLOW use the vocabulary `Vulnerability becomes a Finding when triaged`. PRC-VM uses a more precise exposure model: observations enter the pipeline, are validated, reachability assessed, then classified; no SLA starts until classification. The concepts are compatible, but `triaged` is too loose compared with PRC-VM's states.

Why it matters: C03 scenario 1 depends on knowing when the SLA clock starts. If `triage` means initial intake, the clock starts too early; if it means PRC-VM classification, the flow works.

Evidence from corpus:
- GEN-001 conversion rule: vulnerability becomes Finding when triaged.
- PRC-VM §4.2: no SLA clock starts at observation intake; clock starts at confirmation/classification.
- PRC-VM §2 state model distinguishes Observed, Validated, Reachability Assessed, Exposure Confirmed, Treatment Selected, Closure Verified.

Recommended action: Update GEN/FLOW language to: `A vulnerability or observation becomes a Finding when validation/classification confirms an in-scope condition requiring disposition. PRC-VM governs exposure observations and SLA start.`

Owner/workstream: Glossary / Flow / Exposure Management.

### C03-F05 Medium Monitor-only is an allowed decision class but lacks guardrails
Affected files:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Problem: FLOW lists `Monitor only` as an allowed decision class. PRC-VM has states such as Hygiene Debt and Confirmed Flaw Not Currently Exposed where monitoring can be legitimate. PRC-RM defines acceptance as proceeding without further action beyond monitoring. The corpus does not state the boundary between monitor-only as an operational exposure state and risk acceptance as a business decision.

Why it matters: `Monitor only` can become a loophole for silent acceptance if not constrained. A reader needs to know when monitoring is enough and when Business Owner acceptance is required.

Evidence from corpus:
- FLOW allowed decision classes include `Monitor only`.
- PRC-VM §7 classifies Confirmed Flaw Not Currently Exposed as `Monitor control; plan remediation`.
- PRC-RM §5.1 says Accept means proceed without further action beyond monitoring.

Recommended action: Define `Monitor only` in GEN/FLOW: allowed only where no control deviation exists, no business decision is required, compensating control is verified, review cadence is assigned, and conversion triggers to Finding/Risk are documented. Otherwise use Risk Acceptance.

Owner/workstream: Glossary / Risk.

### C03-F06 Medium Accepted-risk expiration behavior is clear in GEN/FLOW but less explicit in PRC-RM
Affected files:
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`

Problem: GEN and FLOW state that an expired risk acceptance auto-creates a High Finding. PRC-RM states no acceptance expires automatically and requires a fresh approval cycle at expiration, but it is less explicit about the post-expiration record behavior for risk acceptances than it is for exceptions.

Why it matters: The scenario `accepted risk expires` should have one deterministic answer. The exception expiration path is excellent; the risk acceptance expiration path should match that clarity.

Evidence from corpus:
- GEN-001 extended rule: Risk Acceptance that expires without renewal auto-creates a High Finding.
- FLOW-001 SLA exception logic: Accepted Risk Expiration auto-creates High Finding.
- PRC-RM §7.4.1 provides detailed exception expiration warnings and post-expiration High Finding, but acceptance expiration is discussed more generally.

Recommended action: Add a risk-acceptance expiration warning chain to PRC-RM or explicitly state that the exception warning chain applies with the same Day 0 High Finding behavior.

Owner/workstream: Risk / PRC-RM.

### C03-F07 Medium Control gap record choice needs a cleaner rule
Affected files:
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`

Problem: GEN says a Control Gap can become a Finding Record or Risk Record and usually becomes a Risk due to systemic impact. PRC-AUD routes evidence deficiency, technical control gap, accepted residual risk, and policy/standard gap through different corrective paths. CAT-002 does not define a Control Gap Record, which is probably correct, but the choice between Finding, Risk, POA&M, Exception, and Improvement is not summarized in one place.

Why it matters: Control gaps are common audit outputs. Without a small decision table, operators may overuse the risk register for local defects or underuse it for systemic weaknesses.

Evidence from corpus:
- GEN control gap conversion rule.
- PRC-AUD §8 finding/corrective action tracking paths.
- PRC-RM risk source categories include governance/compliance and technical control gaps.

Recommended action: Add a compact `Control gap routing` table to GEN or PRC-AUD: local defect → Finding/corrective action; residual risk remains → Risk; deliberate deviation → Exception; regulated gap → POA&M/CIP/SOX path; systemic program weakness → Improvement Record.

Owner/workstream: Governance / Risk / Evidence.

## Positive Confirmations
- The exception versus risk acceptance distinction is now strong in PRC-RM §7.1 and TMPL-RM-004. This is a major improvement over ambiguous `waiver/acceptance` language.
- PRC-VM's exposure-state model is excellent. It prevents scanner output from becoming unfiltered risk noise.
- Exception expiration handling is strong: warning chain, Day 0 High Finding, control gap flag, and renewal escalation are all present.
- Incident-to-learning conversion is conceptually strong through PRC-LL and IMPREG, as long as IR ownership text is corrected elsewhere.
- The scenario tests mostly produce workable answers; the remaining problems are precedence, stale templates, and concise routing tables rather than missing operating-model concepts.

## Open Questions
- Should TMPL-RM-003 be retired outright, or retained only as a low/medium memo variant that still requires Business Owner acceptance?
- Should `Monitor only` be allowed as a final decision class, or only as an interim state under a Finding/Risk with explicit review triggers?
- Should the risk acceptance expiration path exactly mirror the exception expiration warning chain, or should it have a lighter cadence?
- Should PPR-tier no-acceptance be repeated in RMF/PRC-RM authority tables, or stated once as a cross-reference to PRC-VM?

## Proposed Next Tasks
- D01: reconcile role names and JDs, especially Detection Engineer / Vendor Risk Analyst and Risk acceptance accountabilities.
- G02: add rewrite queue entries for GEN risk acceptance source, PRC-VM/PPR precedence, RMF/PRC-RM scoring, vulnerability-to-finding wording, monitor-only guardrails, acceptance expiration, and control-gap routing.
- E01/E03: review examples for wrong language such as Risk `accepting` residual risk instead of Business Owner acceptance.
