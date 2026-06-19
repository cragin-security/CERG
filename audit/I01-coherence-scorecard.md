# Task I01 Output: CERG Coherence Scorecard

## Overall Verdict

CERG's operating-model logic holds. The three-pillar model is credible, teachable, and generally executable: Engineering builds and remediates, Risk validates exposure and treatment, Governance governs records/evidence/authority/reporting, and Business owns business consequence. The remaining issues are not a failure of the model; they are drift and reader-protection problems around authority, routing, role artifacts, record names, and examples.

Overall coherence score: **4.0 / 5**

Interpretation:
- **Strong core:** three-pillar logic, evidence model, policy/control/procedure trace, and CISO first-hour comprehension.
- **Repair needed before source rewrite/public promotion:** IR adjacent-function authority, risk-acceptance/scoring authority, swapped Detection/Vendor JDs, FLOW record/closure drift, Story 8/10 authority language, and MTR visible defects.
- **Primary improvement theme:** keep CERG complete, but make the high-use reader paths simpler and the authority centers sharper.

## Score Summary

| Area | Score | Short verdict |
|---|---:|---|
| 1. Three-pillar logic | 4 / 5 | Model holds with local repairs. |
| 2. Pillar boundary clarity | 3 / 5 | Strong in most adjacent areas; IR boundary is a stop-the-line contradiction. |
| 3. Handoff clarity | 4 / 5 | Flows work, but FLOW sometimes over-owns procedure detail. |
| 4. Role/RACI clarity | 3 / 5 | Canonical model is good; JD/authority drift is material. |
| 5. Record/evidence closure | 4 / 5 | Evidence spine is strong; record-name authority needs cleanup. |
| 6. Risk/exception/finding vocabulary | 3 / 5 | Conceptual distinction is strong; duplicate scoring/templates create drift. |
| 7. Example strength | 3 / 5 | Examples are valuable but several teach stale authority language. |
| 8. Human first-hour comprehension | 4 / 5 | CISO path is strong; practitioner/business paths need routing. |
| 9. Voice consistency | 4 / 5 | House voice is strong; boilerplate/JDs/generated text drift. |
| 10. Structural elegance | 3 / 5 | Complete and powerful, but adoption/workforce suites feel heavy. |
| 11. Small-team scalability | 3 / 5 | Principle is right; consolidation maps and Story 8 need repair. |
| 12. Regulated-scope clarity | 4 / 5 | Regulated overlays are strong; composite traces need better maps. |

---

## 1. Three-pillar logic — 4 / 5

Rationale: The core decomposition is sound. Tested work fits the three questions: Engineering builds/operates/remediates, Risk assesses exposure/treatment, Governance governs rule/record/evidence/reporting. No audit task found a need for a fourth pillar.

Top evidence:
- `B01` verdict: "Three-pillar model holds with repairs."
- `H01` found a new CISO can understand CERG as an operating model in the first hour.
- `H04` found the policy-to-control-to-procedure-to-record/evidence chain mostly works.

Top issue:
- Some local text blurs Risk into acceptance authority, especially examples and older role language.

Recommended action:
- Treat `FRM-002`'s three-question model as canonical short wording. Rewrite stale examples and role passages that say or imply `Risk accepts` business risk.

## 2. Pillar boundary clarity — 3 / 5

Rationale: Privacy, BCP, OT operations, Legal/ERM/Procurement, and Business Owner boundaries are mostly clear. Incident Response is the major exception: IR metadata and banners say the standing IR team owns IR, while body/footer sections assign notification-clock or exercise ownership to Governance/Risk.

Top evidence:
- `B02` and `B03` identify IR ownership as Critical.
- `OM-001` clearly states CERG does not own IR operations, notification clocks, or exercises.
- IR plan/playbook sections contradict that boundary.

Top issue:
- Competing incident authority centers during the highest-pressure operating condition.

Recommended action:
- Make the standing IR team / Incident Commander canonical owner of incident command, notification-clock process, and exercises. Make CERG Governance support notification evidence/registers and cross-reference hygiene.

## 3. Handoff clarity — 4 / 5

Rationale: The canonical flow idea works. F-02, F-04, F-07, and the day-in-the-life examples show triggers, handoffs, records, and closure. Handoff clarity weakens where FLOW-001 carries procedure-level clocks or closure rules that conflict with procedures.

Top evidence:
- `C01` and `H02` show practitioners can execute common workflows from FRM-002 and procedure paths.
- `G01` finds FLOW-001 should remain a map, not a competing procedure.
- `H04` shows vulnerability remediation trace is clean end to end.

Top issue:
- FLOW F-04 duplicates/conflicts with PRC-VM closure/SLA logic; F-06 also needs IR boundary repair.

Recommended action:
- Rewrite FLOW-001 to own triggers, handoffs, records, evidence checkpoints, and closure shape. Let procedures/SLC own detailed clocks and treatment mechanics.

## 4. Role/RACI clarity — 3 / 5

Rationale: OM/RAC/JF/JD architecture is a differentiator, but role drift is currently one of the highest-risk coherence defects. The model knows what roles should do, but some role artifacts and local authority statements disagree.

Top evidence:
- `D01` found Detection Engineer and Vendor Risk Analyst JD bodies are swapped.
- `D01` found OM/RAC/JDs still say pillar leaders hold risk-acceptance authority, conflicting with business-owner acceptance model.
- `D02` found role/procedure fit generally works once the reader reaches the procedure.

Top issue:
- Workforce artifacts can teach wrong operational assignments despite correct OM/RAC intent.

Recommended action:
- Repair Detection/Vendor JDs first. Then align OM/RAC/JD risk-acceptance wording to RMF-001 §9.7: Security reviews/routes/documents; Business Owner accepts consequence.

## 5. Record/evidence closure — 4 / 5

Rationale: CERG's record/evidence spine is one of its strongest features. CAT-002, AUD-001, PRC-AUD, CB-001, TRC-001, and MTR-001 create an auditable loop. The main weakness is record-name authority spread across CAT, FLOW, GEN, examples, and templates.

Top evidence:
- `H04` found the auditor trace mostly works.
- `CAT-002` provides canonical record types and required fields.
- `AUD-001` gives strong evidence quality tests and rejects weak evidence patterns.

Top issue:
- Record definitions and aliases compete across CAT-002, FLOW-001, GEN-001, and examples.

Recommended action:
- Make CAT-002 canonical for record names/required fields/evidence value; GEN canonical for definitions; FLOW a flow-to-CAT-record crosswalk with alias column only.

## 6. Risk/exception/finding vocabulary — 3 / 5

Rationale: The conceptual distinction between finding, exception, risk acceptance, treatment, and business consequence is strong in newer RMF/PRC-RM/TMPL-RM-004 material. Drift remains in scoring calibration, older templates, and examples.

Top evidence:
- `C03`, `B03`, `D01`, and `H03` all identify risk-acceptance authority drift.
- `PRC-RM-001` §7.1 and `TMPL-RM-004` clearly distinguish security exception from risk acceptance.
- `B03` found RMF and PRC-RM scoring anchors differ materially.

Top issue:
- RMF/PRC-RM duplicate scoring and TMPL-RM-003 omission of Business Owner can route decisions incorrectly.

Recommended action:
- Keep RMF-001 as scoring/acceptance authority. Make PRC-RM an operational pointer or exact summary. Retire or rewrite TMPL-RM-003 to include Business Owner acceptance.

## 7. Example strength — 3 / 5

Rationale: The examples are first-class teaching assets and often explain CERG better than abstract documents. But several examples currently teach stale authority or boundary language and should not be promoted unmodified.

Top evidence:
- `E01` identifies Story 9, Story 2, and Story 10 as the strongest teaching assets.
- `E01` flags Story 8 Critical vendor exposure and Story 4 `Risk accepts` language.
- `H01` found Story 10 useful but authority language stale.

Top issue:
- Examples can undermine the model precisely because they are memorable.

Recommended action:
- Repair authority language before promotion. Add missing high-value stories for evidence failure, OT patch deferral, and business-owner residual-risk/funding decisions only where existing stories cannot absorb them.

## 8. Human first-hour comprehension — 4 / 5

Rationale: CERG is understandable quickly for a security leader. Practitioners can execute many common workflows. Business owners and auditors can understand the model, but their paths require more routing support and less jargon.

Top evidence:
- `H01`: new CISO comprehension is mostly strong; FRM-002 is the best front-door map.
- `H02`: SaaS intake, vulnerability triage, TPRM, and risk exceptions are executable, but some direct user-need rows are missing.
- `H03`: business accountability principle is strong, but no dedicated business-owner front door exists.
- `H04`: auditor chain exists, but composite traces need curated maps.

Top issue:
- Front-door navigation is optimized for security readers more than Business Owners, auditors, and weekly-task practitioners.

Recommended action:
- Add FRM-002/IMP-007 rows for exception/acceptance, access-review evidence, vendor assessment, OT patch deferral, and Business Owner/System Sponsor path.

## 9. Voice consistency — 4 / 5

Rationale: CERG's house voice is a strength: direct, operational, evidence-centered, and skeptical of shelfware. Drift appears in boilerplate, generated/JD content, and vague coordinator language.

Top evidence:
- `F01` defines a strong voice model.
- `F03` finds spine and examples generally sound like CERG.
- `F03` identifies repeated weak boilerplate: `responsible for`, `where applicable`, `as needed`, and `coordinates` at decision points.

Top issue:
- Document-control boilerplate and per-role JD generated sections weaken readability and accountability.

Recommended action:
- Add STY-001 house patterns for document-control ownership, applicability decisions, and role/action verbs. Apply after higher-priority authority repairs.

## 10. Structural elegance — 3 / 5

Rationale: CERG is structurally rich and mostly justified, but it is at risk of feeling complete before it feels simple. The adoption suite and workforce subsystem are powerful but cognitively heavy.

Top evidence:
- `G01` recommends shortening and pointing rather than merging or retiring most major artifacts.
- `H01` finds the CISO can understand the model but wants clearer first decisions and MVC/full-spine distinction.
- `G01` says workforce needs a system map and thinner per-role JDs, not fewer authoritative documents.

Top issue:
- Too many front doors and repeated summaries create reader fatigue and drift risk.

Recommended action:
- Keep the document suite, but clarify each artifact's job: START-HERE front door, IMP-005 adoption authority, IMP-006 checklists, IMP-007 reader paths, CAT/FRM maps, RAC role assignment, OM operating model.

## 11. Small-team scalability without conceptual loss — 3 / 5

Rationale: The core principle is excellent: heads collapse, questions do not. But small-team maps disagree and Story 8 currently weakens guardrails by showing an over-compressed Critical vendor-risk path.

Top evidence:
- `D03` confirms the concept works for two-, five-, and eight-person teams if hats remain explicit.
- `FRM-002` states that questions do not collapse, only heads.
- `E01` and `D03` flag Story 8 and small-team map inconsistencies.

Top issue:
- Small-team examples/adoption maps can accidentally teach that authority also collapses.

Recommended action:
- Synchronize IMP-003, RAC-001, OM-001, and Story 8. Add explicit `hat` labels and state that Business Owner/CISO/Executive Sponsor authority still applies even when one person holds multiple CERG roles.

## 12. Regulated-scope clarity without compliance takeover — 4 / 5

Rationale: CERG generally keeps regulated scope as overlays, not the operating model's center. CUI, CIP, SOX, and evidence packages are strong. The main weakness is that regulated architecture review and OT deferral require composite routing rather than a simple trace.

Top evidence:
- `H04` shows CUI architecture review is operationally strong but a composite trace.
- `H02` shows OT patch deferral content exists but navigation requires inference.
- `TRC-001` overlay traceability is valuable and should be expanded.

Top issue:
- Auditors/practitioners need curated overlay paths for regulated workflows, especially CUI architecture review and OT/BES patch deferral.

Recommended action:
- Add regulated workflow trace rows/cards: CUI architecture review package, BES/OT patch deferral, SOX access/change evidence, and CMMC POA&M trigger path.

---

## Top Cross-Cutting Risks to Coherence

1. **Authority drift:** IR ownership, risk acceptance, scoring, and local role tables repeat authority in too many places.
2. **Record-name drift:** record aliases are useful locally but need CAT-002 authority and alias discipline.
3. **Workforce artifact drift:** swapped JDs and stale authority language can undermine otherwise strong role architecture.
4. **Example authority drift:** stories are powerful enough to teach the wrong thing if not repaired first.
5. **Front-door routing gaps:** the corpus contains the answer, but some personas cannot find it fast enough.

## Top Cross-Cutting Strengths to Preserve

1. The three-pillar question model.
2. The `yes, and` operating philosophy when backed by records and decisions.
3. The definition of done: owner, decision, evidence, residual risk, control/register update, review date.
4. The evidence quality model in `AUD-001`.
5. The day-in-the-life examples as first-class teaching tools.
6. Small-team principle: heads collapse, questions do not.
7. Regulated overlays as overlays, not a replacement for the operating model.

## I01 Acceptance Criteria Check

- Concise enough for executive read: yes.
- Detailed enough to justify scores: yes.
- Scores supported by A-H findings: yes.
- Each area includes score, rationale, top evidence, top issue, and recommended action: yes.
