# Task E01 Output: Evaluate day-in-the-life examples against framework strength

## Scope Reviewed
- Files read:
  - `examples/day-in-the-life/README.md`
  - `examples/day-in-the-life/story-8-cerg-lite-maria.md`
  - `examples/day-in-the-life/story-9-f-01-control-intent.md`
  - `examples/day-in-the-life/story-10-new-ciso-90-days.md`
  - Supporting cross-link scan across `README.md`, `START-HERE.md`, `governance/`, `procedures/`, `standards/`, `plans/`, `templates/`, and `roles/`.
- Sections reviewed:
  - Story index and usage guidance in `examples/day-in-the-life/README.md`.
  - Stories 1-7 embedded in the README.
  - Standalone Stories 8, 9, and 10.
  - FRM-002, IMP-007, START-HERE, SLC-001, CAT-001, and top-level README references to stories.
- Files intentionally not reviewed:
  - Every procedure referenced by every story. Prior C/D workstreams already tested many execution chains; E01 tests example quality.
  - Missing-story candidates in depth. E02 will map narrative coverage gaps and propose new examples.

## Method
- Steps performed:
  1. Inventoried all day-in-the-life stories.
  2. Treated Stories 1-7 as embedded README stories and Stories 8-10 as standalone story files.
  3. Scored each story 0-3 on the ten E01 dimensions: trigger clarity, pillar clarity, handoff clarity, record clarity, evidence clarity, metric closure, improvement loop, human readability, strength of example, and reusability for training.
  4. Compared each story against the strong CERG example definition: realistic trigger, flow, owner, proper pillar work, records, evidence, metrics, decision/improvement closure, non-heroic execution, and business enablement.
  5. Scanned for core-document cross-links to the story set.
- Search terms or scripts used:
  - `find examples/day-in-the-life -maxdepth 1 -type f -name '*.md' | sort`
  - `rg -n "Story [0-9]|story-[0-9]|day-in-the-life|Day in the Life|examples/day-in-the-life" README.md START-HERE.md governance procedures standards plans templates roles examples/day-in-the-life/*.md`
- Assumptions avoided:
  - Did not penalize Story 10 for being a 90-day adoption arc rather than a single event; it is intended for leadership onboarding.
  - Did not require every story to cite metric IDs; however, lack of metric specificity lowers metric-closure score.
  - Did not treat examples as normative source documents. Findings focus on reader comprehension and training value.

## Story Scorecard

Scoring scale: 0 = absent or misleading, 1 = weak, 2 = adequate, 3 = strong.

| Story | Trigger | Pillar clarity | Handoff clarity | Record clarity | Evidence clarity | Metric closure | Improvement loop | Readability | Strength | Training reuse | Total / 30 | Recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1. New SaaS application | 3 | 3 | 2 | 3 | 3 | 2 | 1 | 3 | 3 | 3 | 26 | Keep; expand metric/improvement closure. |
| 2. Critical vulnerability | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 30 | Promote as canonical F-04 story. |
| 3. Audit request | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 3 | 28 | Promote after adding metric IDs / dashboard closure. |
| 4. Major cloud workload launch | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 3 | 3 | 3 | 27 | Rewrite risk-acceptance wording; expand improvement closure. |
| 5. Privileged access review | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 29 | Keep/promote as access-review training story. |
| 6. Third-party security incident notification | 3 | 2 | 2 | 3 | 3 | 1 | 3 | 3 | 2 | 3 | 25 | Rewrite IR boundary and metrics. |
| 7. Enterprise AI assistant rollout | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 28 | Keep; expand final decision and metrics. |
| 8. CERG Lite scanner report | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 3 | 3 | 3 | 27 | Rewrite Critical vendor exception path before promotion. |
| 9. F-01 regulator change | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 30 | Promote as canonical F-01 story. |
| 10. New CISO first 90 days | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 28 | Promote for leadership onboarding; mark as adoption arc, not flow example. |

## Keep / Rewrite / Expand / Cut Recommendations

| Story | Recommendation | Rationale |
|---|---|---|
| Story 1 — New SaaS application | Keep / light expand | Strong F-02/TPRM/access/logging example. Add explicit final disposition and metric IDs. |
| Story 2 — Critical vulnerability | Keep / promote | Best compact example of CERG doing operational work under pressure without heroics. It names flow, owners, records, evidence, metrics, and improvement. |
| Story 3 — Audit request | Keep / promote after metric detail | Strong evidence-quality story. Needs named audit/evidence metrics once MTR-001 receives the AE metric family from D02. |
| Story 4 — Major cloud workload launch | Rewrite targeted language | Good multi-flow launch example, but `Risk accepts one low residual risk` conflicts with the business-owner acceptance model. |
| Story 5 — Privileged access review | Keep / promote | Strong example of access review becoming finding, remediation, metric update, and systemic improvement. |
| Story 6 — Third-party security incident notification | Rewrite | Good scenario, but IR boundary and metrics are too soft. Needs Incident Commander / standing IR handoff clarity. |
| Story 7 — Enterprise AI assistant rollout | Keep / expand | Good AI governance example. Add final pilot disposition, named AI records, and stronger metric closure. |
| Story 8 — CERG Lite scanner report | Rewrite before promotion | Excellent small-team story, but the Critical vendor exception path weakens risk-acceptance discipline. |
| Story 9 — F-01 regulator change | Keep / promote | Strongest control-intent story and one of the clearest records/evidence/metrics chains in the example set. |
| Story 10 — New CISO first 90 days | Keep / promote for reader path | Strong leadership/adoption story. It should be labeled as a program arc rather than a single flow exemplar. |

## Top Three Stories Showing CERG Strength

1. **Story 9 — F-01 Control Intent.** Best example of CERG's operating-model strength: external change becomes control change records, conformance scope, implementation design, validation plan, evidence plan, dashboard overlay, and board-visible accountability.
2. **Story 2 — Critical vulnerability.** Best compact operational story. It shows Risk, Engineering, and Governance each doing their proper work, with a clear improvement loop.
3. **Story 10 — New CISO first 90 days.** Best leadership onboarding story. It shows CERG as cadence and decision discipline rather than a documentation project.

Honorable mentions:
- **Story 5** is the strongest access-review / recurring-finding example.
- **Story 8** could become a top-three story after the D03 risk-authority rewrite.

## Findings

### E01-F01 High Story 8 teaches a risky Critical vendor exception pattern
Affected files:
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`

Problem: Story 8 is the canonical CERG Lite story, but its SFTP Critical vendor scenario shows a consolidated Governance/CISO person approving an Exception Record with compensating monitoring and a vendor patch date after both Critical findings are described as having public exploit code. The story does not explicitly show Business Owner approval, CISO/Executive Sponsor escalation where required, or the PPR-tier no-ordinary-acceptance rule.

Why it matters: Story 8 is where small teams learn what to do under pressure. If it shows a Critical public-exploit vendor exposure handled as a routine exception, readers may copy the wrong risk authority model.

Evidence from corpus:
- Story 8: both Critical findings have public exploits.
- Story 8: Priya creates an Exception Record for vendor-owned SFTP; Maria approves it in the weekly meeting.
- PRC-RM §7.3: Business owner approval is required for exceptions carrying residual risk above Low.
- IMP-002 §5: security cannot accept risk on behalf of the business.
- PRC-VM §11: PPR-tier exposures are not eligible for ordinary acceptance except in OT/CIP deviation scenarios.

Recommended action: Rewrite the SFTP branch. Either make it a High/Medium vendor gap suitable for a time-bound exception, or keep it Critical and show full escalation: Business Owner, CISO, Executive Sponsor if Critical, explicit PPR analysis, temporary compensating controls, and an accelerated vendor/alternate-transfer decision.

Owner/workstream: Examples / Small-team risk authority.

### E01-F02 High Story 4 says Risk accepts residual risk, conflicting with RMF authority model
Affected files:
- `examples/day-in-the-life/README.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Problem: Story 4 says `Risk accepts one low residual risk around delayed DDoS exercise completion with a 30-day due date`. Current RMF/PRC-RM language says Risk assesses, documents, and routes; Business Owner accepts business consequence where residual business risk exists. Security roles should not be described as accepting residual risk on behalf of the business.

Why it matters: This exact example may be reused by readers learning go-live risk posture. It can teach the stale authority model that B03/C03/D01 already flagged.

Evidence from corpus:
- Story 4 narrative: `Risk accepts one low residual risk...`.
- RMF-001 §9.7 and PRC-RM §7.1: business owner accepts residual risk; security assesses and routes.
- D01-F02 and C03 already identified stale risk-acceptance authority language across role/procedure artifacts.

Recommended action: Replace with wording such as: `Risk documents the residual risk and recommends a 30-day treatment plan; the Business Owner accepts the temporary business consequence, and Governance records the decision per PRC-RM.`

Owner/workstream: Examples / Risk authority cleanup.

### E01-F03 Medium Story 6 blurs the IR adjacent-function boundary
Affected files:
- `examples/day-in-the-life/README.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`

Problem: Story 6 is a third-party security incident notification story, but it presents Risk as coordinating whether the event becomes an internal incident and Governance as confirming notification obligations and executive reporting cadence. It references the IR Plan and Playbook Set, but does not explicitly name the Incident Commander or the standing IR team as the decision authority if an incident is declared.

Why it matters: CERG's adjacent-function boundary is already a major audit theme. Story 6 should be the clearest narrative that CERG supports vendor incident triage and hands off active incident command to the standing IR team when activation criteria are met.

Evidence from corpus:
- Story 6 step 4: Risk coordinates vendor questions, exposure analysis, and whether the event becomes an internal incident.
- PLN-IR and PRC-IR banners: the standing IR team and Incident Commander own active incident response.
- RAC-001 §6.4: CERG roles are Consulted for incident response operations, not Accountable.

Recommended action: Rewrite Story 6 to add an explicit decision point: Vendor Risk Analyst triages third-party exposure; if activation criteria are met, the Incident Commander declares/declines incident status. Governance supplies regulatory mapping and evidence; it does not own the IR notification clock unless delegated by the IR process.

Owner/workstream: Examples / Adjacent IR boundary.

### E01-F04 Medium Metric closure is often generic rather than reproducible
Affected files:
- `examples/day-in-the-life/README.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

Problem: Several stories say metrics update, but do not name the metric IDs, source records, or dashboard tile. Story 2 and Story 9 are strongest here. Stories 1, 3, 4, 5, 6, 7, and 8 often use generic phrases such as `Metrics update`, `Reporting Metric Record`, or `monthly metrics refresh`.

Why it matters: One of CERG's strengths is record-to-metric traceability. A story is more reusable for training when a reader can see exactly which metric changes because of the work.

Evidence from corpus:
- Story 1: metrics update for intake throughput, cycle time, and exception volume, but no IDs.
- Story 3: evidence package and improvement are strong, but audit/evidence metrics are not ID-defined in MTR-001.
- Story 6: metrics for third-party incident response are named generically.
- D02-F04 found PRC-AUD metric concepts are not defined in MTR-001.

Recommended action: Add one `Metric closure` line to each story's Operational outputs. Use exact MTR IDs where they exist (e.g., EM, TP, CM, ID, SR, CE). For audit/evidence stories, first add the AE metric family to MTR-001 or mark the metric as planned.

Owner/workstream: Examples / Metrics traceability.

### E01-F05 Medium README and START-HERE story-count guidance is inconsistent with the actual ten-story set
Affected files:
- `examples/day-in-the-life/README.md`
- `START-HERE.md`
- `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`

Problem: The example README now lists ten stories, but `START-HERE.md` still says there are seven narrative walkthroughs. CAT-001 correctly says ten. Some stories are embedded in the README while Stories 8-10 are standalone files, making the inventory harder to understand at a glance.

Why it matters: This is a reader-navigation issue. New adopters are explicitly told to read one story early; stale counts and mixed file layout can make the examples feel less governed than the core corpus.

Evidence from corpus:
- `examples/day-in-the-life/README.md` lists Stories 1-10.
- `START-HERE.md` says `seven narrative walkthroughs`.
- CAT-001 §5 example entry says ten narrative walkthroughs.
- Filesystem contains the README plus standalone files for Stories 8, 9, and 10 only.

Recommended action: Update `START-HERE.md` to say ten stories. Consider splitting Stories 1-7 into standalone files or explicitly label README as containing Stories 1-7 and separate files as Stories 8-10.

Owner/workstream: Examples / Reader navigation.

### E01-F06 Medium Core flow sections do not directly point readers to the best matching examples
Affected files:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`
- `examples/day-in-the-life/README.md`

Problem: FRM-002 and IMP-007 point to day-in-the-life stories, but FLOW-001's individual flow sections do not appear to include direct `See Story X` links. That means a reader studying F-01 through F-07 from the authoritative flow document may not discover the strongest narrative example for that exact flow.

Why it matters: E01 asks for missing cross-links from core documents to the strongest stories. FLOW-001 is the natural place to link each flow to a worked example because each story declares its primary flow.

Evidence from corpus:
- FRM-002 §4.1/§4.2 and navigation sections link to story groups.
- IMP-007 links CISO/Risk/Engineering readers to Story 10, Story 2, and Story 1.
- Search found no direct story links in FLOW-001.

Recommended action: Add a short `Worked example` line at the end of each FLOW-001 flow: F-01 → Story 9; F-02 → Story 1 or 7; F-03/F-05 → Story 4; F-04 → Story 2 or 5/8; F-06 → rewritten Story 6; F-07 → Story 3 or 10.

Owner/workstream: Examples / Cross-linking.

### E01-F07 Low Stories 1-7 are strong but less reusable because they are embedded in one long README
Affected files:
- `examples/day-in-the-life/README.md`
- `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`

Problem: Stories 1-7 are embedded in the README, while Stories 8-10 are standalone files. Links to Story 1/2/3 use README anchors; links to Story 8/9/10 use direct files. The content works, but training and onboarding reuse would be easier if each story had a stable file path.

Why it matters: Low severity because anchors work today and validation passes. But examples are meant for onboarding and tabletop reuse; a one-story-per-file pattern would make them easier to assign, revise, and cite.

Evidence from corpus:
- Filesystem contains only `story-8`, `story-9`, and `story-10` standalone files.
- IMP-007 links Story 1 and Story 2 through README anchors, while Story 10 is linked directly.

Recommended action: Consider splitting Stories 1-7 into `story-1-new-saas-application.md` through `story-7-enterprise-ai-assistant-rollout.md`, leaving the README as an index. If that is too much churn, add a note that Stories 1-7 live inline in the README.

Owner/workstream: Examples / Structure polish.

## Positive Confirmations
- The example set is much stronger than a generic case-study appendix. Every story has a realistic trigger, a named flow, a walkthrough table, narrative, and operational outputs.
- Stories 2, 5, and 9 are especially good at showing that CERG is an operating model: work creates records, evidence, metrics, and improvement rather than merely approvals.
- Story 10 is highly useful for new CISO comprehension. It shows cadence, first records, decision log, metrics, board update, resourcing, and improvement without pretending adoption is a one-time project.
- Story 7 makes the AI standard practical and avoids turning AI governance into a purely prohibitive control story.
- The examples generally show the business being enabled: SaaS goes live with conditions, cloud launch proceeds with evidence, AI pilot runs with guardrails, and the new CISO gets audits under control.
- FRM-002 and IMP-007 already use the examples as reader-path assets, which is exactly the right pattern.

## Open Questions
- Should Stories 1-7 become standalone files, or should the README intentionally remain the container for shorter examples?
- Should examples cite exact metric IDs even when MTR-001 does not yet define the needed metric family, or should those be marked as planned until G02 source cleanup?
- Should Story 8 keep the Critical vendor SFTP scenario and show the full escalation path, or use a less severe vendor finding to teach ordinary small-team exception handling?
- Should Story 6 be the canonical IR-adjacent story after rewrite, or should E02 propose a separate incident handoff story that focuses only on CERG-to-IR boundaries?
- Should Story 10 remain in day-in-the-life examples or move/copy into onboarding/adoption examples because it is a 90-day program arc?

## Proposed Next Tasks
- E02: map story coverage to F-01 through F-07 and identify missing stories only where the existing set does not teach a major handoff.
- E03: produce rewrite plans for Story 4, Story 6, Story 8, and metric-closure expansions across Stories 1, 3, 5, and 7.
- G02: add rewrite queue items for Story 8 risk-authority correction, Story 4 risk-acceptance wording, Story 6 IR boundary, FLOW-001 worked-example links, and MTR audit/evidence metrics.
- G03: add polish queue items for START-HERE story count and potential story file split.
