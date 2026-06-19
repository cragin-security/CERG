# Task D01 Output: Reconcile OM canonical roles to RAC and role JDs

## Scope Reviewed
- Files read:
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
  - `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
  - `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
  - `roles/CERG-GOV-JF-001_Job_Families_Overview.md`
  - `roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md`
  - All per-role JD files under `roles/jf-*/*.md`
  - Selected procedure/standard/plan/template references where role names appear, using exact-name scans.
- Sections reviewed:
  - OM-001 §6.1 canonical role roster, §6.2-6.5 typical roles, §8 interfaces, §9 RACI examples.
  - GEN-001 §6 role names.
  - RAC-001 §4 canonical role reference, §5 document ownership RACI, §6 standing process RACI, §7 role descriptions, §8 scaling map.
  - JF-001 §3 job family table and §9 level definitions.
  - JF-002 complete crosswalk table.
  - JD §1 role summaries, §2 NICE mapping, §4 responsibilities, §6 TKS references, §10 success profiles, and document-control sections for sampled anomalies.
- Files intentionally not reviewed:
  - Every line of every JD after the pattern was confirmed. D01 tests alignment, not final JD prose quality.
  - HR-adjacent governance files beyond JF/JD alignment. D03 will test small-team consolidation more deeply.

## Method
- Steps performed:
  1. Extracted the 27 OM-001 canonical roles.
  2. Compared OM, GEN, RAC, JF-001, JF-002, and per-role JD role sets.
  3. Listed per-role JD files and compared each JD's declared canonical role to the expected role.
  4. Scanned standards, procedures, plans, and templates for exact canonical-role mentions to identify roles not connected to operational work.
  5. Scanned known synonym/noncanonical terms for role-name drift.
  6. Compared role descriptions against RAC-001 process assignments and known C01/C02/C03 findings.
- Search terms or scripts used:
  - `find roles -path 'roles/jf-*/*.md'`
  - Python extraction of `**CERG Canonical Role:**` fields from per-role JDs.
  - Exact-name mention counts across `standards/`, `procedures/`, `plans/`, and `templates/`.
  - Targeted scans for `Risk Manager`, `System Owner`, `Technical Lead`, `Project Sponsor`, `Governance Lead`, `Engineering Lead`, `CISO designee`, and role-name variants.
- Assumptions avoided:
  - Did not treat external business/project roles as automatically wrong. Some noncanonical role names may be local project roles, but they should be defined or mapped.
  - Did not count family-index files (`*-000_*.md`) as per-role JDs.
  - Did not assume a role must appear in many procedures to be valid. A role can be valid if it is specialized, but zero operational appearances is still a human-clarity risk.

## Role Reconciliation Matrix

| Canonical role | OM | GEN | RAC | JF-001 family table | JF-002 | Per-role JD | Procedure / standard support | Result |
|---|---|---|---|---|---|---|---|---|
| Chief Information Security Officer (CISO) | Present | Present | Present | Present as CISO | Present | Present, but JD canonical field omits `(CISO)` | Strong | Minor naming mismatch in JD field. |
| Executive Sponsor | Present | Present | Present | Missing from §3 family-role list | Present | Present | Strong in risk acceptance | JF-001 omission. |
| Engineering Pillar Leader | Present | Present | Present | Missing from §3 family-role list | Present | Present | Strong | JF-001 omission. |
| Cloud Security Engineer | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Identity Engineer | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| OT Security Engineer | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Application Security Engineer | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Endpoint Engineer | Present | Present | Present | Present | Present | Present | Moderate | Aligned; endpoint execution path could be clearer (C02). |
| Cryptography Engineer | Present | Present | Present | Present | Present | Present | Moderate | Aligned; crypto execution path could be clearer (C02). |
| Pre-production Reviewer | Present | Present | Present | Missing from §3 family-role list | Present | Present | Present mainly in AR/SDL | JF-001 omission; otherwise aligned. |
| Risk Pillar Leader | Present | Present | Present | Missing from §3 family-role list | Present | Present | Strong | JF-001 omission; authority language drift. |
| Exposure Management Lead | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Adversarial Testing Lead | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Threat Intelligence Analyst | Present | Present | Present | Present | Present | Present | Strong in TI/LM/LL | Aligned. |
| Vendor Risk Analyst | Present | Present | Present | Present | Present | Present, but body is Detection Engineer content | Strong in TPRM/AI/NET | JD content swapped. |
| OT Risk Analyst | Present | Present | Present | Present | Present | Present | Moderate | Aligned. |
| Identity Risk Analyst | Present | Present | Present | Present | Present | Present | No exact-name hits in standards/procedures/plans/templates | Role exists but operational connection is weak. |
| Detection Engineer | Present | Present | Present | Present | Present | Present, but body is Vendor Risk Analyst content | Strong in LM/AV/MTR references | JD content swapped; DT metrics missing (C02). |
| Governance Pillar Leader | Present | Present | Present | Missing from §3 family-role list | Present | Present | Strong | JF-001 omission; authority language drift. |
| NERC-CIP Compliance Manager | Present | Present | Present | Present | Present | Present | Strong in OT/CIP | Aligned. |
| CMMC / Federal Compliance Manager | Present | Present | Present | Present | Present | Present | Strong in CUI/CMMC | Aligned. |
| SOX ITGC Lead | Present | Present | Present | Present | Present | Present | Strong in SOX/CHG/RES/AUD | Aligned. |
| Policy & Standards Manager | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Risk Register Owner | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Evidence Librarian | Present | Present | Present | Present | Present | Present | Strong | Aligned. |
| Incident Commander | Present as Adjacent | Present | Present as Adjacent | Present | Present | Present | Strong in IR | Concept aligned; source docs still conflict on IR ownership from B02/C01. |
| Lead Investigator | Present as Adjacent | Present | Present as Adjacent | Present | Present | Present | Present in IR | Concept aligned. |

## Synonym and Role-Name Drift Table

| Noncanonical or ambiguous term | Where observed | Recommended canonical treatment |
|---|---|---|
| `Risk Manager` | OM synonym column | Replace with `Risk Pillar Leader` where it means pillar lead; `Risk Register Owner` where it means register operator. |
| `System Owner` | Adoption guidance, AC runbook, threat modeling, CUI package/templates | Map to `Asset Owner`, `Technical Owner`, or `Business Owner` depending accountability. Avoid using as a CERG canonical role. |
| `Project Sponsor` | PRC-AR | Accept as a project/business role if defined, but map to `Business Owner` for residual-risk accountability. |
| `Technical Lead` | PRC-AR | Accept as project delivery role, but map to `Technical Owner` or named Engineering role for CERG accountability. |
| `Business / Asset Owners` | PRC-RM, PRC-TPRM | Split into `Business Owner` and `Asset Owner` where the decision differs. |
| `Vendor / Third-Party Risk Analyst` | OM typical roles | Replace with `Vendor Risk Analyst`. |
| `Application / Application Security Engineer` | OM typical roles | Replace with `Application Security Engineer`. |
| `Endpoint / Endpoint Engineer` | OM typical roles | Replace with `Endpoint Engineer`. |
| `Adversarial Testing Lead (Red Team)` | OM typical roles | Replace with `Adversarial Testing Lead`; use `red team` as activity, not role name. |
| `Governance Lead` / `Engineering Lead` in incident context | OM/RAC/IR docs | If these are incident-activation support roles, define them as incident assignments staffed by CERG roles; do not treat them as canonical CERG roles. |
| `CISO designee` | OM/STY | Accept only as documented delegation pattern per OM; prefer named canonical role where the approver is known. |

## Findings

### D01-F01 Critical Detection Engineer and Vendor Risk Analyst JD bodies are swapped
Affected files:
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md`
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md`

Problem: The Detection Engineer file has the correct title and canonical role line, but its role summary, core responsibilities, domain expertise, education/certification profile, and several TKS labels describe a Vendor Risk Analyst. The Vendor Risk Analyst file has the correct title and canonical role line, but its body describes a Detection Engineer. Some NICE rows remain partly correct for the file title, so the files are internally mixed rather than simply renamed.

Why it matters: These are operational roles, not cosmetic descriptions. Detection Engineer owns detection-rule authoring, ATT&CK coverage, and IR handoff. Vendor Risk Analyst owns TPRM, vendor tiering, evidence, and SCCT support. A reader using these JDs for hiring, staffing, or role assignment would assign the wrong work to the wrong person.

Evidence from corpus:
- OM-001 and RAC-001 define Detection Engineer as detection-rule authoring, ATT&CK coverage, tuning, logging/monitoring coverage, and IR handoff.
- OM-001 and RAC-001 define Vendor Risk Analyst as operating TPRM, vendor assessment, supply chain coordination, and SCCT participation.
- JD-RISKOPS-004 `Detection Engineer` §1 begins `The Vendor Risk Analyst operates the Third-Party and Supply Chain Risk Procedure`.
- JD-RISKOPS-007 `Vendor Risk Analyst` §1 begins `The Detection Engineer owns detection-rule authoring`.

Recommended action: Manually repair both files section-by-section, not by blind file swap. Preserve the correct title/metadata/canonical role and move the correct role body content, NICE/TKS labels, qualifications, success profile, and related-doc relevance into the matching JD. Revalidate TKS references after repair.

Owner/workstream: Workforce / Role JDs.

### D01-F02 High Risk-acceptance authority language in OM/RAC/JDs conflicts with the current business-owner acceptance model
Affected files:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-008_Risk_Pillar_Leader.md`
- `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-007_Governance_Pillar_Leader.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Problem: OM, RAC, and pillar-leader JDs still say the Risk Pillar Leader holds Medium risk-acceptance authority and the Governance Pillar Leader holds Low/Informational risk-acceptance authority. RMF-001 §9.7 and PRC-RM now clarify that Business Owner acceptance is required for Low, Medium, High, and Critical risk where business impact exists; security roles assess, route, approve on the cybersecurity side, document, or track. Informational items need no formal acceptance.

Why it matters: This is an authority-center issue expressed through workforce architecture. If a JD says a security leader `holds risk-acceptance authority`, a reader may conclude that security can accept business risk, contradicting the RMF's central rule.

Evidence from corpus:
- RMF-001 §9.7: Business Owner accepts business consequence at Low/Medium/High; Executive Sponsor at Critical; security assesses and CISO/pillar roles approve or document as applicable.
- PRC-RM §7.1: Business Owner explicitly accepts residual risk; security does not accept business consequence.
- OM-001 canonical role roster: Risk Pillar Leader has Medium severity risk-acceptance authority; Governance Pillar Leader has Low/Informational severity risk-acceptance authority.
- RAC-001 role descriptions repeat this language.
- Risk and Governance Pillar Leader JDs repeat this language.

Recommended action: Replace `holds risk-acceptance authority` language with precise phrasing: `reviews/concurs/routes/documents acceptance per RMF-001 §9.7; Business Owner accepts business consequence; CISO approves High/Critical cybersecurity program acceptance`. Update OM, RAC, and affected JDs together.

Owner/workstream: Workforce / Risk authority cleanup.

### D01-F03 High JF-001 family overview omits five canonical roles from its main family table
Affected files:
- `roles/CERG-GOV-JF-001_Job_Families_Overview.md`
- `roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md`
- `roles/jf-*/*.md`

Problem: JF-001 says it groups the 27 canonical CERG roles into five job families. Its §3 family table lists only 22 role names. It omits Executive Sponsor, Engineering Pillar Leader, Risk Pillar Leader, Governance Pillar Leader, and Pre-production Reviewer. JF-002's complete crosswalk and the per-role JD files include them.

Why it matters: JF-001 is the entry point for workforce architecture. If the family overview omits leadership and rotated roles, a reader can believe these roles are outside the family model even though JDs exist and JF-002 maps them.

Evidence from corpus:
- JF-001 §1 claims 27 roles.
- JF-001 §3 JF-SECENG lists six engineering specialist roles but not Engineering Pillar Leader or Pre-production Reviewer.
- JF-001 §3 JF-RISKOPS lists seven risk specialist roles but not Risk Pillar Leader.
- JF-001 §3 JF-GOVCOMP lists six governance roles but not Governance Pillar Leader.
- JF-001 §3 JF-EXEC lists CISO but not Executive Sponsor.
- JF-002 §8 and JD files include all 27.

Recommended action: Update JF-001 §3 role lists to include all 27 canonical roles, or explicitly distinguish `family members` from `leadership/business sponsor roles` and reconcile the claim in §1.

Owner/workstream: Workforce / Job families.

### D01-F04 Medium Identity Risk Analyst exists in the role architecture but is not connected to operating procedures
Affected files:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-006_Identity_Risk_Analyst.md`
- Relevant identity/detection procedures and standards

Problem: Identity Risk Analyst is present in OM, GEN, RAC, JF-001, JF-002, and has a JD. Exact-name scans across standards, procedures, plans, and templates found zero operational references. RAC gives it a role description but no clearly owned standing process row.

Why it matters: A role without procedure touchpoints is hard to staff, evaluate, or consolidate. The JD says it owns identity-threat detection, UEBA, OAuth, and token risk, but the operating model does not show where that work executes.

Evidence from corpus:
- OM-001: Identity Risk Analyst owns UEBA, identity-threat detection, OAuth and token risk.
- RAC-001 role description repeats this.
- Exact-name scan across standards/procedures/plans/templates: zero hits outside workforce/spine docs.
- STD-AC, PRC-AC, STD-LM, and MTR contain adjacent identity/detection work but do not route work to Identity Risk Analyst.

Recommended action: Either route identity-threat detection work explicitly in STD-LM, PRC-AC, MTR detection/identity metrics, or mark Identity Risk Analyst as an optional specialization under Detection Engineer / Risk Pillar Leader in small and standard implementations.

Owner/workstream: Workforce / Risk procedures.

### D01-F05 Medium RAC-001 document-ownership RACI is missing newer artifacts and likely no longer matches CAT-001 inventory
Affected files:
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`
- Newer standards/procedures/templates/governance instruments

Problem: RAC-001 says every artifact registered in CAT-001 should have a row in the Section 5 RACI. Its current document-ownership RACI covers the core library but appears to stop before newer artifacts such as FLOW, GEN, SLC, TRC, CJ, EDG, IMPREG, CEF, LL, AI templates, SaaS/SBOM templates, and many standalone templates.

Why it matters: RAC-001 claims to be the authoritative answer to `who owns this?` If the artifact list is stale, document ownership becomes split between CAT-001 metadata, local document-control sections, and an incomplete RACI.

Evidence from corpus:
- RAC-001 §9: when an artifact is registered in CAT-001, a row is added to Section 5.
- A01 corpus map shows many artifacts beyond the rows visible in RAC-001 §5.
- C02 found TRC and template-routing staleness; this is the workforce/RACI version of the same drift.

Recommended action: Refresh RAC-001 §5 against CAT-001 or replace the long document-ownership RACI with a rule that CAT-001 metadata is authoritative and RAC-001 owns standing-process RACI. Avoid maintaining two incomplete artifact inventories.

Owner/workstream: Governance / RACI maintenance.

### D01-F06 Medium Canonical-role synonym guidance is noisy and sometimes identical to the canonical role
Affected files:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- Standards/procedures/plans/templates using local role variants

Problem: OM-001's synonym column includes repeated identical strings such as `Identity Engineer`, `Detection Engineer`, `Vendor Risk Analyst`, and `Governance Pillar Leader` as synonyms for themselves. Other local variants such as `System Owner`, `Project Sponsor`, `Technical Lead`, `Governance Lead`, and `Engineering Lead` appear in operational documents without a clear canonical mapping.

Why it matters: The canonical roster is supposed to reduce ambiguity. A synonym column that repeats canonical names and misses real drift terms makes it harder for contributors to know which terms to replace.

Evidence from corpus:
- OM-001 §6.1 synonym column repeats exact canonical role names for multiple roles.
- Exact scans found noncanonical or local terms across PRC-AR, PRC-RM, PRC-TPRM, CUI, AC, TM, IR, and adoption guidance.

Recommended action: Clean the synonym column to include only true noncanonical variants, and add a short local-role mapping note for project/business roles (`Project Sponsor`, `Technical Lead`, `System Owner`) versus CERG canonical roles.

Owner/workstream: Workforce / Vocabulary.

### D01-F07 Low CISO JD canonical role field omits the `(CISO)` canonical suffix
Affected files:
- `roles/jf-exec/CERG-GOV-JD-EXEC-001_Chief_Information_Security_Officer.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`

Problem: OM/GEN/RAC list the canonical role as `Chief Information Security Officer (CISO)`. The per-role JD canonical role field says `Chief Information Security Officer` without `(CISO)`.

Why it matters: This is low severity because the meaning is obvious, but D01 is testing exact role-set consistency. Exact-match scripts see this as a missing/extra role.

Evidence from corpus:
- JD extraction found 27 per-role JD files, but exact role-set comparison reported missing `Chief Information Security Officer (CISO)` and extra `Chief Information Security Officer`.

Recommended action: Update the JD canonical-role line to match OM exactly: `Chief Information Security Officer (CISO)`.

Owner/workstream: Workforce / Polish.

## Positive Confirmations
- The per-role JD file set is complete in count: 27 per-role JD files exist for the 27 OM canonical roles, excluding family-index files.
- OM, GEN, RAC, and JF-002 are broadly aligned on the role roster and pillar/family placement.
- RAC-001 has the right precedence model: OM owns role names; RAC owns assignments; local tables conform.
- Adjacent IR roles are correctly marked as non-CERG in the workforce architecture; the remaining IR problem is in plan/procedure body text, not the role roster itself.
- Most specialist JDs align with their OM/RAC summaries. The severe issue is concentrated in the Detection/Vendor pair rather than widespread JD swaps.
- The small-team scaling principle in RAC-001 is strong: roles consolidate onto fewer people; accountabilities do not disappear.

## Open Questions
- Should JF-001 §3 include pillar leaders and Executive Sponsor in the family table, or should it explicitly separate `operating roles` from `leadership/business roles`?
- Should Identity Risk Analyst remain a standalone canonical role, or be treated as a specialization of Detection Engineer until procedures explicitly route identity-threat detection work to it?
- Should RAC-001 continue to maintain document-ownership RACI for every artifact, or should CAT-001 become the sole source for document owner/approval metadata while RAC focuses on process RACI?
- When incident documents use `Engineering Lead` and `Governance Lead`, should those become formal incident-assignment labels staffed by canonical roles, or should they be replaced with canonical role names throughout?

## Proposed Next Tasks
- D02: test selected roles against actual procedure work, using Detection Engineer, Vendor Risk Analyst, Evidence Librarian, Pre-production Reviewer, and Incident Commander as high-value cases.
- D03: test whether role consolidation guidance preserves these distinctions in small teams.
- G02: add rewrite queue items for Detection/Vendor JD repair, OM/RAC/JD risk-acceptance authority wording, JF-001 role list completion, Identity Risk Analyst procedure routing, RAC artifact-RACI refresh, and synonym cleanup.
- G03: carry CISO exact-name mismatch and identical synonym entries into polish queue.
