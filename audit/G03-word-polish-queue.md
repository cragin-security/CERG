# Task G03 Output: Word-level polish queue

## Scope Reviewed
- Files read:
  - `/workspace/thebigone.md` G03 instructions.
  - Audit outputs: `audit/A02-validation-baseline.md`, `audit/C01-flow-trace.md`, `audit/C02-execution-chain.md`, `audit/D01-role-reconciliation.md`, `audit/D02-role-procedure-fit.md`, `audit/D03-role-consolidation.md`, `audit/E01-example-quality.md`, `audit/E02-missing-stories.md`, `audit/E03-example-rewrite-plan.md`, `audit/F01-voice-vocab-inventory.md`, `audit/F02-term-drift.md`, `audit/F03-house-voice-findings.md`, and `audit/G02-section-rewrite-queue.md`.
  - Source snippets from affected files for safe exact old/new text.
- Sections reviewed:
  - Low-severity findings and explicit `G03` handoff notes.
  - A02 mechanical scan findings.
  - Known local polish defects in FLOW, SLC, FRM, PRC-IR, TRC, TMPL-AR, START-HERE/examples, GEN, STY, and role JDs.
- Files intentionally not reviewed:
  - Full source documents line by line. G03 is a queue derived from prior audits, not a new proofread of the full corpus.
  - High-severity conceptual rewrites already queued in G02.
  - Generated machine-readable files except where source edits may later require regeneration.

## Method
- Steps performed:
  1. Collected Low findings and explicit polish handoff notes from A through G02.
  2. Grouped polish candidates by file.
  3. Separated safe mechanical fixes from context-sensitive wording/structure fixes.
  4. For safe fixes, captured exact old text and new text.
  5. For context-sensitive fixes, wrote instructions rather than replacement strings.
- Search terms or scripts used:
  - `rg` for `NERC-CIP,,`, `800-171,,`, leading `||`, `Section 11`, `1.0 Draft`, story-count references, CISO canonical role, `Policy and Standards Manager`, and STY em-dash guidance.
  - Python scan for long role JD bullet/table lines over 350 characters.
- Assumptions avoided:
  - Did not recommend global role/term replacements from F02.
  - Did not reflow JD content blindly because some sections are generated and some role bodies are currently wrong.
  - Did not treat historical revision-history `1.0 Draft` strings as automatically safe to change without owner decision.

## Safe Mechanical Fixes

These can be done with exact replacement and validation. They should still be committed one file at a time per repository practice.

| File | Priority | Old text | New text | Source findings | Notes |
|---|---|---|---|---|---|
| `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md` | Low | `|| Request type | Tier / trigger | CERG commitment (preliminary default) | Escalation if missed | Metric |` | `| Request type | Tier / trigger | CERG commitment (preliminary default) | Escalation if missed | Metric |` | A02-F02 | Exact table-row pipe fix. |
| `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md` | Low | `|| Exception / risk-acceptance request intake | All | Acknowledge and route to the correct approver within 3 business days | Risk Register Owner | SR-004 |` | `| Exception / risk-acceptance request intake | All | Acknowledge and route to the correct approver within 3 business days | Risk Register Owner | SR-004 |` | A02-F02 | Exact table-row pipe fix. |
| `governance/CERG-GOV-FRM-001_CERG_Framework.md` | Low | `NERC-CIP,,` | `NERC-CIP,` | A02-F03 | Safe punctuation fix; verify only one intended replacement. |
| `governance/CERG-GOV-FRM-001_CERG_Framework.md` | Low | `800-171,,` | `800-171,` | A02-F03 | Safe punctuation fix; verify only one intended replacement. |
| `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md` | Low | `5. **Stand-down**: The Incident Commander declares stand-down; CERG returns to normal operations and begins post-incident actions per Section 11.` | `5. **Stand-down**: The Incident Commander declares stand-down; CERG returns to normal operations and begins post-incident actions per Section 17.` | D03-F06 | Safe local reference correction unless Section 17 is renamed during G02 IR rewrite. If G02-R03 happens first, re-check section number. |
| `governance/CERG-GOV-GEN-001_CERG_Glossary.md` | Medium | `- **Policy and Standards Manager**` | `- **Policy & Standards Manager**` | F01-F01 | Safe if OM/RAC/JD remain canonical with ampersand spelling. |

## Context-Sensitive Polish Queue by File

### `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| TOC and section-number drift | After G02 conceptual FLOW rewrites, regenerate or manually repair the TOC and heading numbering. Renumber from highest to lowest; fix `Shared State Models` subsections currently numbered `7.x` under section 8 and minimum record templates currently numbered `16.x` under section 19. | A02-F01, C01-F08 | No | After G02-R01, R08, R10 |
| Duplicate `### Mandatory Rules` heading in F-04 | Do not merely rename one heading. Resolve in G02-R08 because the duplicate blocks conflict conceptually. | C01-F02 | No | G02-R08 |
| Missing F-07 `Evidence Required` block | Add as section-level rewrite, not word polish, because it affects metric/reporting authority. | C01-F07 | No | G02-B3 |

### `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Two malformed leading table pipes | Apply the two exact replacements listed in Safe Mechanical Fixes. | A02-F02 | Yes | None |

### `governance/CERG-GOV-FRM-001_CERG_Framework.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Duplicate commas in front-door text | Apply exact punctuation replacements listed in Safe Mechanical Fixes. | A02-F03 | Yes | None |
| Marketing/slogan-adjacent lines should remain operationalized | Do not remove slogans wholesale. During G02/G03 front-door harmonization, keep memorable lines only where nearby prose names roles, records, evidence, or next steps. | F03-F06, G01-F08 | No | H01 preferred |

### `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Incorrect `Section 11` cross-reference in §18.1 | Apply exact replacement to `Section 17` only if G02-R03 has not renumbered sections. | D03-F06 | Yes, conditional | Before or after G02-R03 with re-check |
| Revision history contains `1.0 Draft` | Review after IR ownership/status cleanup. If historical Draft label is not intentional, change revision-history version cell to `1.0`. | C02 G03 handoff pattern | No | G02-R03 |
| Document-control boilerplate voice | Replace only after STY-001 document-control pattern is approved. | F03-F01 | No | G02-R26 |

### `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Revision history contains `1.0 Draft` in an Approved document | Human-review whether revision history should preserve draft provenance or normalize version cell to `1.0`. Do not change blindly. | C02 G03 handoff | No | TRC refresh from C02-F03 |
| Stale traceability content | Not a G03 polish fix. Queue as G02/implementation refresh if TRC remains authoritative or semi-authoritative. | C02-F03 | No | G02 if pursued |

### `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Revision history contains `1.0 Draft` in an Approved template | Human-review whether to normalize to `1.0`. Do not change blindly until PRC-AR/TMPL-AR authority state is resolved. | C02 G03 handoff | No | G02-R16 |
| Template state conflicts with PRC-AR text | Not word polish; fix in PRC-AR section rewrite. | C02-F02 | No | G02-R16 |

### `roles/jf-exec/CERG-GOV-JD-EXEC-001_Chief_Information_Security_Officer.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| CISO JD exact-name mismatch was reported, but current source already shows `Chief Information Security Officer (CISO)` in the canonical role field | No action unless D01 was based on older source or another CISO field is found. Re-check before opening an edit. | D01-F07 | No | None |
| Long responsibility and KSA bullets | Do not reflow until G02-R25 JD pattern is approved. | A02-F04, F03-F05 | No | G02-R25 |
| Role summary says CISO leads IR and Awareness functions | Review with IR adjacent-function cleanup. This may be conceptually correct as CISO oversight, but wording should not imply CERG owns IR operations. | B02/B03/D02 | No | G02-B1 |

### `roles/jf-*/*.md` per-role JD corpus

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| 51 long lines across 25 role files | Do not line-wrap mechanically. Convert long compound bullets into sub-bullets or shorter one-duty bullets from an approved template. | A02-F04, D02-F05, F03-F05 | No | After G02-R04/R05 and G02-R25 sample |
| Dense competency tables duplicated from CMP-001 | Shorten or replace with summary/link after approved JD pattern. | F03-F05, G01-F05 | No | G02-R25 |
| Document-control boilerplate repeats weak `responsible for` pattern | Replace only after STY-001 approves a standard pattern. | F03-F01 | No | G02-R26 |

### `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Long bullet contains vendor-risk duties | Do not polish locally; repair whole role body as critical rewrite. | A02-F05, D01-F01 | No | G02-R04 |

### `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Long bullet contains detection duties | Do not polish locally; repair whole role body as critical rewrite. | A02-F05, D01-F01 | No | G02-R05 |

### `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| No-em-dash rule conflicts with established spine voice | Owner decision required: either enforce as hard rule with automated check or revise guidance to discourage overuse rather than prohibit. Do not batch-replace em dashes until decision is made. | F01-F03 | No | G02-R26 |
| `Security team` replacement guidance says `as appropriate` | Refine guidance to say name the acting pillar/role when assigning work; generic audience/team-size use is allowed. | F02-F03, F03-F07 | No | G02-R26 |
| Document-control boilerplate pattern missing | Add approved active-voice pattern before bulk boilerplate cleanup. | F03-F01 | No | G02-R26 |

### `governance/CERG-GOV-GEN-001_CERG_Glossary.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| `Policy and Standards Manager` spelling | Apply exact ampersand replacement listed in Safe Mechanical Fixes. | F01-F01 | Yes | None |
| `System Owner`, `Risk Owner`, waiver/deviation/exception boundaries | Not a word-level global fix. Clarify in glossary rewrite. | F02-F01, F02-F02, F02-F04 | No | G02-R19 |

### `START-HERE.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Story count guidance may be stale against ten-story set | Re-check after example restructuring. Update count/links in the same change as example index cleanup. | E01-F05, E03 handoff | No | G02-R15/R23 |
| `Where applicable` in adoption path | Do not search/replace. Rewrite sentences to name the scope decision owner and record. | F03-F02 | No | G02-R23 |
| `future pain` phrase | Keep if nearby prose explains late findings, vendor surprises, and production exceptions. | F03-F06 | No | G02-R23/H01 |

### `examples/day-in-the-life/README.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Stories 1-7 embedded in README while Stories 8-10 are standalone | Consider one-story-per-file split after content stabilizes. Do not split before authority rewrites unless needed for onboarding usability. | E01-F07 | No | After G02-R15 |
| Story count/index drift | Re-check after final story set and new story decisions. | E01-F05, E03 handoff | No | G02-R15 |
| Vague `coordinates` language in walkthrough tables | Replace locally with action/record verbs during story rewrite. Do not global replace. | F03-F04 | No | G02-R15 |

### `examples/day-in-the-life/story-8-cerg-lite-maria.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Heading says `5-person rhythm` while story uses three people | If Story 8 keeps three-person cast, change heading to `Operating under the small-team rhythm` or similar. | E03 rewrite plan | No | G02-R14 |
| Operational outputs need authority-safe wording | Rewrite after Critical vendor path decision. | E01-F01, D03-F03 | No | G02-R14 |

### `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Subtitle/body uses `Waiver Request` / `waiver` language | Do not remove blindly if adopters need local synonym support. Preferred cleanup: make `Security Exception Record` primary and mention `waiver` only as local synonym if intentionally supported. | F02-F04 | No | G02-B2/G02-R19 |

### `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| May conflict with newer RMF/TMPL-RM-004 acceptance request authority | Do not word-polish until RMF/PRC-RM decide whether TMPL-RM-003 remains an output memo, legacy template, or retired/reclassified artifact. | B03-F02, C03-F01 | No | G02-R06/R07 |

### `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Generally strong business-owner wording; may need cross-reference updates after RMF/PRC-RM cleanup | Re-check related-document and approval wording after G02-R06/R07. | C03-F01, F02 | No | G02-R06/R07 |

### `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Local role label cleanup around Pre-production Reviewer and Phase 4 extension authority | Do not polish in isolation; rewrite Phase 4/5 sections in G02. | D02-F01, D02-F02 | No | G02-R16 |
| Appendix worked example may need template-state wording | Align after TMPL-AR/PRC-AR authority is resolved. | C02-F02 | No | G02-R16 |

### `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

| Issue | Instruction | Source findings | Mechanical? | Dependency |
|---|---|---|---|---|
| Missing DT metric definitions and audit/evidence metric IDs | Not polish. Add metrics through G02-R17. | C02-F01, D02-F04 | No | G02-R17 |
| Malformed/source-map table drift noted in C01 summary | Re-check after metrics rewrite; then queue exact table fixes if any remain. | C01 | No | G02-R17 |

## Safe Mechanical Batch Candidates

These are candidates for a small scripted batch only after a human confirms scope:

| Candidate | Scope | Why not immediate global replacement? |
|---|---|---|
| Replace exact `NERC-CIP,,` and `800-171,,` in FRM-001 | Single file, exact strings | Safe but still commit per file. |
| Replace leading `||` in SLC-001 table rows | Single file, exact strings | Safe but verify rendered table afterward. |
| Normalize `Policy and Standards Manager` to `Policy & Standards Manager` | GEN-001 exact role line | Safe in glossary line; broader corpus should be scanned and reviewed. |
| Convert `Section 11` to `Section 17` in PRC-IR §18.1 | Single exact sentence | Safe only before section renumbering; re-check after G02 IR rewrite. |

## Context-Sensitive Batch Candidates

These should use a reviewed sample and then a scripted or semi-scripted pass:

| Candidate | Scope | Required precondition |
|---|---|---|
| Document-control boilerplate active-voice rewrite | Many governed Markdown files | STY-001 approved pattern from G02-R26. |
| JD long-bullet reflow | 25 per-role JDs | Role swap fixed; one sample JD approved; generator impact understood. |
| JD competency section shortening | All per-role JDs | CMP/JA cross-reference pattern approved. |
| Record-name normalization | FLOW, CAT, GEN, examples, templates | CAT-002 alias strategy approved. |
| `security team`/`GRC`/`system owner`/`risk owner` wording | Corpus-wide | Use F02 table; context review required. |
| Em dash replacement/enforcement | Potentially many docs | Author decision on STY no-em-dash rule. |

## Positive Confirmations

- Only a handful of defects are safe exact mechanical edits today.
- The largest apparent polish classes, JD readability and record-name normalization, are correctly dependent on G02 authority decisions.
- Existing validation remains clean; these polish items are about human readability and presentation, not CI failures.
- F02 already prevents unsafe global term replacement by classifying context-specific uses.

## Open Questions

- Should revision-history `1.0 Draft` values be preserved as historical state or normalized in Approved documents?
- Should STY-001's no-em-dash rule be enforced mechanically or softened?
- Should story file splitting happen before or after example authority rewrites?
- Should document-control boilerplate be standardized in source before or after high-priority conceptual rewrites?

## Proposed Next Tasks

- If the owner wants quick wins before H workstream, apply the safe mechanical fixes one file at a time: SLC-001, FRM-001, GEN-001, PRC-IR reference.
- Otherwise continue to H01/H02 comprehension tests and reserve source edits for the implementation phase.
- After any governed source edits, run `python3 tools/cerg-validate.py` and `python3 tools/cerg-integrity-check.py`; regenerate machine-readable artifacts only when governed metadata, paths, inventory, or classifications change.
