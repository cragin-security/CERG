# Task G02 Output: Section-level rewrite queue

## Scope Reviewed
- Files read:
  - `/workspace/thebigone.md` G02 instructions.
  - Audit findings from `audit/B01` through `audit/F03`.
  - Structural simplification recommendations from `audit/G01-big-cuts-mergers.md`.
  - Exact section-heading inventories for high-priority affected files.
- Sections reviewed:
  - Findings tables and detailed finding bodies from B, C, D, E, and F workstreams.
  - High-priority sections in FLOW-001, IR plan/playbooks, RMF/PRC-RM/PRC-VM, RAC/OM/JF/JDs, MTR/PRC-AUD, CAT/GEN, adoption guides, and examples.
- Files intentionally not reviewed:
  - Every low-level typo or punctuation issue. Those belong in G03.
  - Full source sections for every planned rewrite. G02 is a queue, not the rewrite pass.
  - Machine-readable regeneration scripts, except where noted as follow-up after governed source edits.

## Method
- Steps performed:
  1. Gathered all B-F findings and grouped them by affected file and conceptual dependency.
  2. Promoted only section-level governed-document rewrites into this queue.
  3. Deferred local wording, malformed tables, punctuation, and safe mechanical fixes to G03.
  4. Ranked rewrite tasks by severity, dependency, and reader impact.
  5. Split multi-document issues into one-file tasks wherever possible, with synchronized bundles identified where ordering matters.
- Search terms or scripts used:
  - `rg` inventory of audit finding headings.
  - Heading extraction across high-priority files to identify exact target sections.
- Assumptions avoided:
  - Did not require every audit finding to become a G02 task. Some findings are polish, generated-artifact, or future comprehension-test inputs.
  - Did not merge unrelated rewrites just because they touch the same file.
  - Did not propose source edits in this artifact.

## Rewrite Dependency Bundles

| Bundle | Purpose | Must be coordinated across | First file to edit | Notes |
|---|---|---|---|---|
| G02-B1 | IR adjacent-function authority cleanup | FLOW-001 F-06, PLN-IR-001, PRC-IR-002, Incident Commander JD, Story 6 | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` | Highest conceptual dependency. Make the flow boundary clear before examples and JD polish. |
| G02-B2 | Risk acceptance / exception / scoring authority cleanup | RMF-001, PRC-RM-001, RM templates, RAC-001, examples | `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md` | RMF remains canonical; dependent docs point back to it. |
| G02-B3 | FLOW-001 execution cleanup | FLOW F-03/F-04/F-05/F-07 plus CAT-002/MTR/PRC-VM/PRC-CHG | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` | Keep FLOW as map, not competing procedure. |
| G02-B4 | Record-name authority cleanup | CAT-002, FLOW-001, GEN-001, FRM-002, examples, templates | `governance/CERG-GOV-CAT-002_Record_Catalog.md` | Decide canonical names and aliases before rewriting examples. |
| G02-B5 | Workforce role architecture cleanup | Detection/Vendor JDs, JF-001, RAC-001, per-role JD readability | Detection and Vendor Risk JD pair | Fix wrong role content before shortening JDs. |
| G02-B6 | Small-team operating model cleanup | IMP-003, RAC-001, OM-001, Story 8, START-HERE | `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md` | Synchronize maps; do not delete roles. |
| G02-B7 | Examples promotion and rewrite | examples README, Story 8, Story 6, Story 9/10, new stories | `examples/day-in-the-life/README.md` | Fix authority errors before promoting as training material. |

## Ranked Rewrite Queue

| Rank | Task ID | Severity | File | Section heading | Main source findings | Dependency |
|---|---|---|---|---|---|---|
| 1 | G02-R01 | Critical | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` | `## 14. Flow F-06 — Incident to Recovery to Standards Feedback` | B02-F01, B03-F01, C01-F01, F03-F03 | G02-B1 |
| 2 | G02-R02 | Critical | `plans/CERG-PLN-IR-001_Incident_Response_Plan.md` | `## 3. Roles and the Incident Response Team`; `## 6. Notification Obligations`; `## 11. Exercises and Plan Maintenance` | B02-F01, B02-F02, B03-F01, F03-F03 | G02-B1 |
| 3 | G02-R03 | Critical | `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md` | `## 2. Ownership Boundary`; `## 17. Post-Incident CERG Actions`; `## 18. Roles and Responsibilities` | B02-F01, B02-F02, B03-F01, D02-F03 | G02-B1 |
| 4 | G02-R04 | Critical | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md` | `## 1` through `## 12` role body | B01-F03, D01-F01 | G02-B5 |
| 5 | G02-R05 | Critical | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md` | `## 1` through `## 12` role body | B01-F03, D01-F01 | G02-B5 |
| 6 | G02-R06 | High | `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md` | `### 9.5`, `### 9.7`, `### 9.7a`, `### 9.10` | B03-F03, C03-F01, C03-F02, C03-F03, F02-F01 | G02-B2 |
| 7 | G02-R07 | High | `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md` | `## 4`, `## 5`, `## 7`, `## 8`, `## 9` | B03-F02, B03-F03, C03-F01, C03-F03, C03-F06 | G02-B2 |
| 8 | G02-R08 | High | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` | `## 12. Flow F-04 — Finding to Remediation, Exception, or Residual Risk` | C01-F02, C01-F03, C03-F04, C03-F05 | G02-B3 |
| 9 | G02-R09 | High | `governance/CERG-GOV-CAT-002_Record_Catalog.md` | `## 4. Authoritative Record Catalog` | B03-F04, C01-F04, F01-F02, F02-F06, G01-F03 | G02-B4 |
| 10 | G02-R10 | High | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` | `## 4. Authoritative Record Types`; all `### Primary Record` subsections | C01-F04, F02-F06, G01-F03 | G02-B4 |
| 11 | G02-R11 | High | `roles/CERG-GOV-JF-001_Job_Families_Overview.md` | `## 3. The Five CERG Job Families` | D01-F03, G01-F05 | G02-B5 |
| 12 | G02-R12 | High | `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md` | `## 5`, `## 6`, `## 7`, `## 8` | D01-F02, D01-F05, D03-F01, G01-F01 | G02-B5/B6 |
| 13 | G02-R13 | High | `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md` | `## 1`, `## 3`, `## 4`, `## 5`, `## 8` | D03-F01, D03-F02, D03-F04, D03-F05 | G02-B6 |
| 14 | G02-R14 | High | `examples/day-in-the-life/story-8-cerg-lite-maria.md` | `## Walkthrough`; `### Narrative`; `## Operational outputs` | D03-F03, E01-F01, F03-F04 | G02-B6/B7 |
| 15 | G02-R15 | High | `examples/day-in-the-life/README.md` | `## Story 4`; `## Story 6`; story index | B01-F01, E01-F02, E01-F03, E03-F01, E03-F02 | G02-B7 |
| 16 | G02-R16 | High | `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md` | `## 8`, `## 9`, `## 11`, Appendix A | C02-F02, D02-F01, D02-F02, E02-F01 | none |
| 17 | G02-R17 | High | `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md` | `### 3.2b`, `## 4`, relevant audit/evidence metrics | C02-F01, D02-F04, E01-F04, C02-F07 | none |
| 18 | G02-R18 | High | `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md` | `## 9. Metrics`; `## 10. Roles and Responsibilities` | D02-F04, F02-F05, G01-F01 | depends G02-R17 |
| 19 | G02-R19 | Medium | `governance/CERG-GOV-GEN-001_CERG_Glossary.md` | `## 3`, `## 4`, `## 5`, `## 6` | F01-F01, F02-F01, F02-F02, F02-F04, G01-F03 | G02-B4/B2 |
| 20 | G02-R20 | Medium | `governance/CERG-GOV-FRM-002_Framework_System_Map.md` | `## 3`, `## 4`, navigation rows for record/flow/example paths | B01 positive confirmation, E01-F06, F02-F06, G01-F08 | after G02-R09/R10 |
| 21 | G02-R21 | Medium | `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md` | `## 5`, `## 7`, `## 11`, `## 16` | C02-F05, E02-F05, F02-F06 | none |
| 22 | G02-R22 | Medium | `standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md` | `## 4` through `## 10` | C02-F04 | none |
| 23 | G02-R23 | Medium | `START-HERE.md` | Path sections and `After the first 30 days` | E01-F05, F03-F02, G01-F04, G01-F08 | after H01 preferred |
| 24 | G02-R24 | Medium | `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md` | `## 2`, `## 3`, `## 4`, `## 6` | G01-F04, F03-F02 | after H01/H02 preferred |
| 25 | G02-R25 | Medium | Per-role JD template pattern | `## 9`, `## 11.3` across JDs | A02, F03-F05, G01-F05 | after G02-R04/R05 |
| 26 | G02-R26 | Medium | `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md` | sections governing role names, document-control boilerplate, em dash rule | F01-F03, F03-F01, F02-F03 | none |

## Detailed Rewrite Tasks

### G02-R01 Critical — Rewrite FLOW-001 F-06 as an adjacent-function support flow
File path: `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Section heading: `## 14. Flow F-06 — Incident to Recovery to Standards Feedback`

Issue: F-06 currently names CERG/Risk ownership in a way that conflicts with the Incident Commander and standing IR team authority model.

Desired reader outcome: A reader can tell that the standing IR team owns incident declaration, classification, command, notification clocks, and exercises; CERG supplies evidence, exposure analysis, engineering support, and post-incident improvement routing.

Rewrite constraints:
- Do not make Risk the primary incident owner.
- Do not make Governance the owner of regulatory notification clocks.
- Preserve the value of the flow: incidents must feed standards, metrics, risk records, and improvement work.
- Use explicit handoff language: IR declares/classifies; CERG supports; CERG receives lessons/improvement actions.

Related documents to keep consistent:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md`
- `procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md`

Acceptance criteria:
- No sentence says or implies Risk owns incident command, incident classification, or notification clocks.
- F-06 names `Incident Commander / standing IR team` as incident-operation owner.
- CERG-owned outputs are limited to support records, evidence packages, findings/risks, standards updates, metrics, and improvement records.
- Validator passes.

### G02-R02 Critical — Align IR Plan role and notification sections to the External Interface model
File path: `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`

Section heading: `## 3. Roles and the Incident Response Team`; `## 6. Notification Obligations`; `## 11. Exercises and Plan Maintenance`

Issue: The plan banner says IR is adjacent and standing-IR-owned, but body sections assign notification-clock and exercise ownership to Governance/CERG language.

Desired reader outcome: During an incident, a reader knows the Incident Commander owns decisions and clocks; CERG roles support evidence, SSP/POA&M impact tracking, technical recovery support, and post-incident improvement.

Rewrite constraints:
- Maintain `External Interface` status/ownership pattern.
- Replace `Governance owns notification clock` language with `Governance tracks evidence and supports Legal/IC notification decisioning`.
- Keep Legal/Privacy/Communications boundaries intact.
- Do not weaken regulatory deadline specificity.

Related documents to keep consistent:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`

Acceptance criteria:
- Role table and notification sections do not contradict the banner.
- Exercise/plan maintenance ownership points to standing IR team / Incident Commander, with CERG support only.
- Document Control owner/status remains consistent with External Interface treatment.

### G02-R03 Critical — Align IR playbook ownership, testing, and CERG support sections
File path: `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`

Section heading: `## 2. Ownership Boundary`; `## 17. Post-Incident CERG Actions`; `## 18. Roles and Responsibilities`

Issue: The playbook has a strong adjacent-function banner, but body and footer language still blur CERG-facing maintenance with IR ownership.

Desired reader outcome: A reader sees playbooks as standing IR team procedures stored in CERG for integration, with CERG post-incident support and improvement handoffs clearly named.

Rewrite constraints:
- Keep playbook operational detail if it belongs to IR, but label CERG use as support/input.
- Do not make Governance the owner of active response or playbook exercise management.
- Make post-incident CERG actions point to PRC-LL and FLOW F-06 after F-06 is rewritten.

Related documents to keep consistent:
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md`

Acceptance criteria:
- Ownership boundary, roles, and document-control language agree.
- CERG support roles are Consulted/Responsible for support outputs, not Accountable for incident response.

### G02-R04 Critical — Restore Detection Engineer JD body to detection content
File path: `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md`

Section heading: `## 1. Role Summary` through `## 12. Related CERG Documents`

Issue: The Detection Engineer JD appears to contain Vendor Risk Analyst body content.

Desired reader outcome: A reader sees Detection Engineer as Risk Operations role for detection-rule authoring, ATT&CK coverage, telemetry coverage, tuning, validation, and IR handoff support.

Rewrite constraints:
- Coordinate with G02-R05; do not duplicate two role bodies.
- Preserve metadata, document ID, and links unless source content confirms they are wrong.
- Align with OM-001/RAC-001 Detection Engineer description and STD-LM/PRC-TI responsibilities.
- Re-run any JD population scripts only if needed and understood.

Related documents to keep consistent:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md`
- `procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md`
- `roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md`

Acceptance criteria:
- Role summary, responsibilities, KSAs, KPIs, success profile, and related docs are detection-oriented.
- No vendor-tiering/vendor-assessment body content remains except where detection consumes vendor telemetry context.

### G02-R05 Critical — Restore Vendor Risk Analyst JD body to vendor-risk content
File path: `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md`

Section heading: `## 1. Role Summary` through `## 12. Related CERG Documents`

Issue: The Vendor Risk Analyst JD appears to contain Detection Engineer body content.

Desired reader outcome: A reader sees Vendor Risk Analyst as the role for third-party tiering, evidence review, SaaS/provider assessment, contract/evidence lifecycle input, continuous vendor monitoring, and TPRM metrics.

Rewrite constraints:
- Coordinate with G02-R04.
- Align to PRC-TPRM, TPRM templates, and RAC-001.
- Preserve JD structure and metadata.

Related documents to keep consistent:
- `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`
- `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire.md`
- `templates/CERG-TMPL-TPRM-002_Vendor_Edge_Register.md`
- `templates/CERG-TMPL-TPRM-003_SaaS_Security_Intake_Form.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`

Acceptance criteria:
- Role body is vendor-risk-oriented and no detection-platform body content remains except where vendor telemetry or supply-chain incident support is relevant.

### G02-R06 High — Clarify RMF risk scoring, acceptance authority, and PPR precedence
File path: `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`

Section heading: `### 9.5 Likelihood, Impact, and Severity Bands`; `### 9.7 Risk Acceptance Authority (Canonical)`; `### 9.7a Policy Exception vs. Risk Acceptance`; `### 9.10 Event-Driven Re-Assessment Triggers`

Issue: Risk scoring and authority are mostly strong but need precedence rules for PPR-tier exposures, clearer `Risk Owner` language, stale template references removed, and alignment with PRC-RM.

Desired reader outcome: A reader can tell who accepts residual risk, which scoring table is canonical, when PPR exposure cannot be accepted, and what record/template is used.

Rewrite constraints:
- Keep RMF as canonical risk acceptance authority.
- Use `Business Owner accepts residual business risk`; Risk assesses/recommends; Governance records.
- Define or avoid `Risk Owner` to prevent confusion with Risk Register Owner.
- Make PPR-tier exposure precedence explicit over generic Critical acceptance authority.
- Point to `TMPL-RM-004` as request form where appropriate; keep `TMPL-RM-003` only if intentionally retained as memo output.

Related documents to keep consistent:
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
- `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`
- `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`

Acceptance criteria:
- No stale instruction routes acceptance authority to the wrong template or role.
- Scoring bands and acceptance authority align with PRC-RM or PRC-RM explicitly defers to RMF.
- PPR no-acceptance rule is unambiguous.

### G02-R07 High — Align PRC-RM to RMF for scoring, acceptance, expiration, and templates
File path: `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Section heading: `## 4. Risk Assessment and Scoring`; `## 5. Risk Treatment`; `## 7. Exception Process`; `## 8. Approval Authority`; `## 9. Review, Escalation, and Reporting`

Issue: PRC-RM contains materially different scoring guidance, stale template references, less explicit accepted-risk expiration behavior, and local authority wording that should defer to RMF.

Desired reader outcome: A practitioner can execute risk register, exception, and acceptance workflow without seeing competing scoring/authority rules.

Rewrite constraints:
- Do not create a second canonical authority table.
- Summarize RMF and point to RMF for canonical authority.
- Use CAT-002 record names once decided.
- Preserve regulatory deviation distinctions from F02.

Related documents to keep consistent:
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md`
- `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`

Acceptance criteria:
- PRC-RM scoring and authority cannot contradict RMF.
- Exception vs risk acceptance path is clear.
- Expiring accepted risks trigger fresh review/reapproval, not silent continuation.

### G02-R08 High — Rewrite FLOW F-04 to defer detailed exposure clocks to PRC-VM
File path: `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Section heading: `## 12. Flow F-04 — Finding to Remediation, Exception, or Residual Risk`

Issue: F-04 has duplicate mandatory rules and an SLA model that conflicts with PRC-VM.

Desired reader outcome: A reader can follow the finding-to-treatment handoff without seeing competing SLA clocks or closure authority.

Rewrite constraints:
- Remove duplicate/contradictory mandatory rules.
- Retain flow-level treatment paths and conversion rules.
- Defer canonical exposure SLAs to PRC-VM §7.2.
- Add guardrails for `monitor only` if not handled elsewhere.

Related documents to keep consistent:
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Acceptance criteria:
- F-04 no longer publishes a conflicting SLA table.
- Closure authority distinguishes Critical/High validation from lower-risk automated/self-closure with Risk sampling, if retained.
- Every path ends in a named record and evidence requirement.

### G02-R09 High — Establish CAT-002 canonical record names and alias policy
File path: `governance/CERG-GOV-CAT-002_Record_Catalog.md`

Section heading: `## 4. Authoritative Record Catalog`

Issue: CAT-002 is the intended authority but does not fully absorb record names used by FLOW, examples, and templates.

Desired reader outcome: A reader can identify the canonical name, common aliases, required fields, owner, and evidence value for each operational record.

Rewrite constraints:
- Do not delete useful local aliases; capture them as aliases if needed.
- Decide whether `Control Change Record` and `Control Implementation Record` are one record or two.
- Decide whether `Project Intake Record`, `Architecture Review Record`, `Project Security Review Record`, and `Production Handoff Package` are separate records or a record family.
- Include `Vendor Risk Assessment Record` if TPRM uses it.

Related documents to keep consistent:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `examples/day-in-the-life/README.md`

Acceptance criteria:
- CAT-002 can serve as record-name source of truth.
- FLOW/examples/templates can be updated from CAT-002 without inventing new labels.

### G02-R10 High — Align FLOW record references to CAT-002
File path: `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Section heading: `## 4. Authoritative Record Types`; all `### Primary Record` sections

Issue: FLOW uses record names that drift from CAT-002 and from examples.

Desired reader outcome: Every flow names the CAT-002 canonical record first and any local alias second.

Rewrite constraints:
- Perform after G02-R09.
- Avoid restating CAT-002 required fields in full.
- Keep flow-level record purpose and handoff value.

Related documents to keep consistent:
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- examples and templates.

Acceptance criteria:
- No primary record in FLOW lacks a CAT-002 mapping.
- Record aliases are consistently marked as aliases.

### G02-R11 High — Add missing canonical roles to JF-001 family table
File path: `roles/CERG-GOV-JF-001_Job_Families_Overview.md`

Section heading: `## 3. The Five CERG Job Families`

Issue: JF-001 omits Executive Sponsor, Engineering Pillar Leader, Risk Pillar Leader, Governance Pillar Leader, and Pre-production Reviewer from the main family table.

Desired reader outcome: A hiring manager or reader can see all 27 canonical roles represented in the job-family view.

Rewrite constraints:
- Do not change OM-001 canonical role roster.
- Preserve distinction between operating pillars and job families.
- Keep adjacent IR role boundary clear.

Related documents to keep consistent:
- `governance/CERG-GOV-JD-001_CERG_Job_Descriptions.md`
- `roles/jf-*/*-000_*.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`

Acceptance criteria:
- All 27 canonical/adjacent roles are represented or explicitly scoped.
- Family counts match JD-001 and role tree.

### G02-R12 High — Refresh RAC-001 authority, document ownership, and scaling map
File path: `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`

Section heading: `## 5. Master RACI: Document Ownership`; `## 6. Master RACI: Standing Processes`; `## 7. Role Descriptions`; `## 8. The Scaling Map`

Issue: RAC-001 is authoritative but appears stale against CAT-001 inventory, risk acceptance model, and small-team maps.

Desired reader outcome: A reader sees a current document/process RACI and role description set that agrees with RMF, OM, JDs, and small-team guidance.

Rewrite constraints:
- Do not make RAC override RMF risk acceptance authority.
- Remove stale statements that pillar leaders `hold` acceptance authority if RMF has moved to Business Owner acceptance with approvals.
- Update document ownership only after comparing to CAT-001.
- Synchronize five-person map with IMP-003 and D03 decisions.

Related documents to keep consistent:
- `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`

Acceptance criteria:
- RAC document ownership rows include current cataloged artifacts.
- Role descriptions do not conflict with RMF business-owner acceptance model.
- Scaling map matches the canonical small-team map.

### G02-R13 High — Rewrite small-team adoption map and two-person operating case
File path: `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`

Section heading: `## 1. Who This Is For`; `## 3. Operating Rhythm for a 5-Person Team`; `## 4. Role Consolidation Map`; `## 5. First 10 Records to Create`; `## 8. Minimum Viable Evidence Library`

Issue: CERG Lite says 2-8 people, but maps focus on five people; maps disagree with RAC/OM/Story 8; role-safety guardrails are detached from the map.

Desired reader outcome: A two-, three-, five-, and eight-person adopter can map roles to people without deleting roles or violating risk/exception guardrails.

Rewrite constraints:
- Do not remove separation-of-duty constraints; name compensating oversight when roles collapse.
- Preserve `questions do not collapse, only heads` principle.
- Define when Executive Sponsor or outside reviewer is required for High/Critical acceptance.
- Use a Decision Log / Role Assignment Map as proof.

Related documents to keep consistent:
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `START-HERE.md`
- Story 8.

Acceptance criteria:
- Two-person case is operationally mapped.
- Five-person map matches RAC.
- Eight-person deconsolidation path is explicit.
- Role safety guardrails appear next to the map, not only elsewhere.

### G02-R14 High — Rewrite Story 8 Critical vendor exposure path
File path: `examples/day-in-the-life/story-8-cerg-lite-maria.md`

Section heading: `## Walkthrough`; `### Narrative`; `## Operational outputs`

Issue: Story 8 teaches a risky pattern by approving an exception for a Critical vendor exposure in a small team without strong business/CISO/regulatory guardrails.

Desired reader outcome: A small-team reader learns how to preserve authority and evidence discipline when one person wears multiple hats.

Rewrite constraints:
- Do not show Risk or Governance accepting business consequence.
- If Critical vendor exposure is accepted, show Business Owner and CISO/Executive Sponsor authority, compensating controls, expiration, and escalation.
- Prefer treatment/escalation over exception if acceptance would violate PPR/regulatory rules.
- Replace vague `coordinates` wording with record/action language.

Related documents to keep consistent:
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`

Acceptance criteria:
- Story preserves small-team consolidation logic without weakening risk authority.
- Outputs include named record, evidence, owner, expiration/review date, and metric/update.

### G02-R15 High — Repair Story 4/6 authority language and example index guidance
File path: `examples/day-in-the-life/README.md`

Section heading: `## Story 4: Major cloud workload launch`; `## Story 6: Third-party security incident notification`; `## Stories at a glance`

Issue: Story 4 says Risk accepts residual risk; Story 6 blurs IR boundary; index/count guidance has drift and examples need better flow links.

Desired reader outcome: Examples teach the correct model: Risk recommends/records, Business Owner accepts, IR owns incident command, CERG supports and records evidence/improvement.

Rewrite constraints:
- Do not duplicate full procedures.
- Use CAT-002 record names after G02-R09/R10 if possible.
- Add direct links from stories to FLOW IDs and best matching procedures.
- Keep Stories 2, 9, and 10 as promotion candidates with minimal changes.

Related documents to keep consistent:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `START-HERE.md`

Acceptance criteria:
- No `Risk accepts` residual-risk wording remains.
- IR story uses Incident Commander authority.
- Story count and links are accurate.

### G02-R16 High — Tighten architecture review Phase 4/5, template state, and pre-production role scope
File path: `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`

Section heading: `## 8. Phase 4: Pre-Production Security Review`; `## 9. Phase 5: Production Handoff and Go-Live`; `## 11. Templates`; `Appendix A`

Issue: PRC-AR says standalone AR templates are planned/internal even though TMPL-AR exists and is Approved; Phase 4 extension authority points to Risk; Pre-production Reviewer role scope appears broader than the title/JD.

Desired reader outcome: A project team knows which template to use, who owns pre-production review, who can extend/approve/reject, and what evidence closes the handoff.

Rewrite constraints:
- Align with Engineering ownership of architecture/pre-production review.
- Keep Risk involved for exposure validation, not review-timeline ownership.
- Use approved TMPL-AR if it is the authoritative form.
- Do not bury Phase 5 handoff evidence in appendix only.

Related documents to keep consistent:
- `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`
- `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Acceptance criteria:
- Template state matches catalog/approved template.
- Phase 4 extension authority is Engineering-owned or explicitly escalated per SLC.
- Handoff package fields and evidence are clear.

### G02-R17 High — Add missing detection and audit/evidence metric IDs to MTR-001
File path: `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

Section heading: `### 3.2b Detection Metrics (Owner: Cyber Risk)`; `## 4. KRI / KPI Data Source Map`; relevant audit/evidence metric sections

Issue: Detection metrics DT-001 through DT-003 and audit/evidence metrics referenced elsewhere are not defined or mapped cleanly.

Desired reader outcome: Standards and procedures can cite metric IDs that exist, have owners, source records, thresholds, and action paths.

Rewrite constraints:
- Do not add vanity metrics without source records.
- Every metric must map to a source of record and owner.
- Align detection metrics with STD-LM and Detection Engineer role.
- Align audit/evidence metrics with PRC-AUD.

Related documents to keep consistent:
- `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md`
- `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Acceptance criteria:
- Referenced DT/audit/evidence metric IDs exist and have source records.
- MTR source map is complete enough for F-07 board-reporting evidence.

### G02-R18 High — Align PRC-AUD metrics and role section to MTR/RAC
File path: `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`

Section heading: `## 9. Metrics`; `## 10. Roles and Responsibilities`

Issue: PRC-AUD names metrics not defined in MTR and carries local role-accountability detail that should defer to RAC.

Desired reader outcome: Evidence/audit operators know which metrics to update and which role owns audit intake, evidence quality, finding routing, and corrective action tracking.

Rewrite constraints:
- Perform after or with G02-R17.
- Use RAC as authority for RACI.
- Use ticket wording only as tool/container, not authoritative record.

Related documents to keep consistent:
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`
- `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`

Acceptance criteria:
- All PRC-AUD metrics exist in MTR or are explicitly local/non-dashboard measures.
- Role section points to RAC and names only procedure-specific actions.

### G02-R19 Medium — Tighten glossary role, record, and conversion vocabulary
File path: `governance/CERG-GOV-GEN-001_CERG_Glossary.md`

Section heading: `## 3. Canonical Terms`; `## 4. Record Types and Their Terms`; `## 5. Conversion Rules (extended)`; `## 6. Role Names`

Issue: GEN has strong vocabulary, but term drift remains around `Policy & Standards Manager`, `Risk Owner`, `System Owner`, waiver/deviation/exception, and records.

Desired reader outcome: A reader can find the controlled term and know which terms are aliases, forbidden, or context-specific.

Rewrite constraints:
- Do not turn GEN into CAT-002; record names should point to CAT-002 after G02-R09.
- Include exact role spelling from OM/RAC/JDs.
- Define `System Owner` only as regulatory/local alias and map it to Business/Asset/Technical Owner.
- Clarify waiver/deviation/exception boundaries.

Related documents to keep consistent:
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`

Acceptance criteria:
- GEN gives unambiguous preferred terms and forbidden/alias terms.
- Role spelling matches workforce docs.

### G02-R20 Medium — Update FRM-002 navigation to canonical records, examples, and pillar wording
File path: `governance/CERG-GOV-FRM-002_Framework_System_Map.md`

Section heading: `## 3`; `## 4`; navigation rows for record/flow/example paths

Issue: FRM-002 is the strongest navigation artifact, but record names and example links should reflect the cleaned-up CAT/FLOW/examples model.

Desired reader outcome: A first-hour reader can navigate from a need to the right authoritative document, record, and best example.

Rewrite constraints:
- Use FRM-002's three-question model as canonical short pillar wording.
- Do not duplicate detailed procedures.
- Update after CAT/FLOW/example record names are stable.

Related documents to keep consistent:
- `README.md`
- `START-HERE.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `examples/day-in-the-life/README.md`

Acceptance criteria:
- Navigation rows point to current authoritative files.
- Example links map to best matching flow stories.

### G02-R21 Medium — Make TPRM templates and evidence lifecycle explicit
File path: `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`

Section heading: `## 5. Evidence by Tier`; `## 7. Approved Provider and SaaS Catalog`; `## 11. SBOM and Software Integrity`; `## 16. Continuous Monitoring and Re-Assessment`

Issue: TPRM/SaaS/SBOM templates exist but are not clearly invoked by the procedure; TPRM lifecycle is underrepresented in examples.

Desired reader outcome: Vendor Risk Analyst and procurement-adjacent readers know which template/record to use at intake, tiering, evidence review, continuous monitoring, SBOM review, reassessment, and offboarding.

Rewrite constraints:
- Keep Procurement/ERM/Business Relationship boundaries intact.
- Use canonical record names after CAT-002 cleanup.
- Do not turn every vendor into full assessment; preserve tiering.

Related documents to keep consistent:
- `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire.md`
- `templates/CERG-TMPL-TPRM-002_Vendor_Edge_Register.md`
- `templates/CERG-TMPL-TPRM-003_SaaS_Security_Intake_Form.md`
- SBOM templates if present.

Acceptance criteria:
- Each TPRM template has an invocation point and output record.
- Continuous monitoring and reassessment have clear triggers and metrics.

### G02-R22 Medium — Add execution-chain summary to data governance standard
File path: `standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md`

Section heading: `## 4. Classifying Data` through `## 10. Roles and Responsibilities`

Issue: Data governance requirements are strong but lack a local execution-chain summary for classification, retention, disposal, and DLP.

Desired reader outcome: A data owner/project team can tell which procedure/template/record turns classification and lifecycle requirements into work.

Rewrite constraints:
- Do not invent a new full procedure unless the author decides one is required.
- Add a compact `Execution Path` table mapping requirement to procedure/template/record/owner.
- Preserve privacy/legal boundaries.

Related documents to keep consistent:
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`
- `plans/CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md`

Acceptance criteria:
- Classification/retention/disposal/DLP each name an owner, record, and evidence source or explicitly point to adjacent function.

### G02-R23 Medium — Tighten START-HERE adoption scope and story guidance
File path: `START-HERE.md`

Section heading: Path sections and `## After the first 30 days`

Issue: START-HERE has story-count drift and uses `where applicable` in adoption-scope decisions without naming the decision record.

Desired reader outcome: A new adopter knows which path to choose, what to record in the first 48 hours, and where to go next without guessing applicability.

Rewrite constraints:
- Keep START-HERE short.
- Use IMP-005 for detailed adoption scope/dependency rules.
- Use IMP-003 for CERG Lite details.
- Fix story count after example set is finalized.

Related documents to keep consistent:
- `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `examples/day-in-the-life/README.md`

Acceptance criteria:
- `Where applicable` path decisions name who decides and what record captures it.
- Story count and links are accurate.

### G02-R24 Medium — Clarify IMP-005 as adoption-scope authority
File path: `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md`

Section heading: `## 2. Adoption Decision Tree`; `## 3. Safe Tailoring Rules`; `## 4. Dependency Matrix`; `## 6. Adoption Gates`

Issue: Adoption guidance is spread across many IMP documents; IMP-005 should be the scope/dependency authority.

Desired reader outcome: A reader can use IMP-005 to decide required, conditional, recommended, and deferred artifacts with documented rationale.

Rewrite constraints:
- Do not absorb checklists from IMP-006 or detailed CERG Lite operations from IMP-003.
- Add explicit output record: adoption scope decision / decision log / organization adaptation profile.
- Preserve one-person/two-person guardrails from IMP-003 once rewritten.

Related documents to keep consistent:
- `START-HERE.md`
- `governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`

Acceptance criteria:
- IMP-005 is clearly the canonical dependency/scope selection artifact.
- Tailoring choices produce named records and review dates.

### G02-R25 Medium — Shorten copied competency and management-track sections in per-role JDs
File path: Per-role JD files under `roles/jf-*/*.md`

Section heading: `## 9. Competency Expectations by Grade`; `### 11.3 Management Track Option`

Issue: JD competency rows are dense and duplicated from CMP/JA, making role files harder to scan.

Desired reader outcome: A hiring manager or practitioner can read role-specific duties quickly and follow links for full competency/grade detail.

Rewrite constraints:
- Do only after G02-R04/R05 role swap is repaired.
- Prefer a template/scripted rewrite after one approved sample.
- Do not remove role-specific KPIs or responsibilities.
- Keep NICE TKS sections if required by workforce model.

Related documents to keep consistent:
- `governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md`
- `governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md`
- `tools/populate-jd-sections.py` if used.

Acceptance criteria:
- JD body is materially shorter and easier to scan.
- CMP/JA remain authoritative for detailed behavioral anchors and grade rules.
- No JD loses role-specific accountability.

### G02-R26 Medium — Update STY-001 with house-voice and document-control patterns
File path: `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`

Section heading: sections governing role names, vocabulary, document control, and punctuation/style rules

Issue: STY-001 already has strong guidance, but F findings show the corpus needs a standard document-control sentence pattern, clearer canonical-role replacement rules, and a decision on the no-em-dash rule.

Desired reader outcome: Future authors can avoid repeating the term/voice drift found in F01-F03.

Rewrite constraints:
- Do not overfit STY-001 to current defects.
- Clarify whether em dash is prohibited or allowed in signature/narrative voice.
- Add a document-control boilerplate pattern that uses active verbs.
- Strengthen `security team`, `GRC`, `system owner`, and `risk owner` guidance without implying blind replacement.

Related documents to keep consistent:
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `audit/F01-voice-vocab-inventory.md`
- `audit/F02-term-drift.md`
- `audit/F03-house-voice-findings.md`

Acceptance criteria:
- STY-001 can be used to prevent known F01-F03 drift in new content.
- Guidance distinguishes operational ambiguity from style preference.

## Items Deferred to G03 or Other Workstreams

- Low-level punctuation/formatting defects from A02: FLOW TOC numbering, SLC malformed table pipes, FRM duplicate punctuation, local line-level wording.
- Machine-readable pillar classification in `cerg-llm-index.json`: should be handled as a tooling/index-generation task after source authority is settled.
- Bulk document-control boilerplate replacement: defer until STY-001 pattern is approved, then handle as G03 safe/context-sensitive batch.
- New example drafting from E02: belongs in an implementation task after existing example authority errors are fixed.
- Full adoption comprehension validation: H01/H02 should run before merging or retiring adoption guidance.

## Positive Confirmations

- The rewrite queue is dominated by authority, record, and handoff clarity rather than style-only edits.
- Most issues can be fixed section-by-section without renaming or moving files.
- The highest-risk dependencies are clear: IR boundary first; RMF risk authority before PRC-RM/templates/examples; CAT-002 record names before FLOW/example record cleanup; JD role-swap repair before JD readability cleanup.
- G01's conclusion holds: the right move is authority consolidation and targeted section rewrites, not broad deletion.

## Open Questions

- Should the author approve a CAT-002 alias strategy before any FLOW/example record-name edits start?
- Should STY-001 be updated before or after the first governed-document rewrite pass?
- Should H01/H02 be run before START-HERE/IMP rewrites, or is the current audit evidence enough to start those changes?
- Should JD readability cleanup be scripted from `tools/populate-jd-sections.py` or performed manually from an approved sample JD?

## Proposed Next Tasks

- G03: build the word-level polish queue for low-risk local fixes.
- H01/H02: run reader comprehension tests before adoption-suite restructuring.
- Implementation phase: start with G02-R01 through G02-R03 as synchronized IR boundary cleanup, one governed source commit at a time.
