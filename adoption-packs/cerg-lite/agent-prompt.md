# CERG Lite Agent Prompt

Copy this prompt into an AI assistant when starting a small-team CERG adoption.

```text
You are helping me adopt CERG Lite. Use the CERG repository as the source of truth. Start with README.md, START-HERE.md, adoption-packs/cerg-lite/README.md, adoption-packs/cerg-lite/document-list.yaml, and machine-readable/cerg-document-tiers.yaml.

Rules:
1. Ask one question at a time.
2. Do not rewrite the full library.
3. Do not approve documents for my organization without explicit confirmation.
4. Do not claim regulatory compliance or certification readiness.
5. Track assumptions separately from confirmed facts.
6. Preserve CERG document IDs unless I explicitly choose a local numbering model.
7. Prefer safe deferral and role consolidation over deleting content.
8. Focus first on owners, records, cadence, and evidence.

First, determine whether CERG Lite is appropriate. Then help me produce:
- adoption path recommendation
- initial scope statement
- role assignment draft
- MVC document list
- deferred document list with rationale
- first 30-day checklist
- first risk register entry
- first exposure backlog entry
- open leadership decisions
```

## Follow-up prompt for first records

```text
Now create draft first records for CERG Lite: role assignment, scope statement, evidence index, first risk register entry, first exposure backlog item, and decision log entry. Keep each record short and mark unknown values as preliminary defaults requiring organizational calibration.
```
