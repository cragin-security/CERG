# Adopt CERG With an Agent

This guide gives humans and AI assistants a safe way to start CERG adoption without turning the full repository into an overwhelming rewrite project.

## 1. Operating rules for the agent

Use these rules in every adoption session:

1. Ask one question at a time when collecting organization-specific facts.
2. Do not mark documents approved for the organization without explicit human confirmation.
3. Do not claim regulatory compliance or certification readiness.
4. Preserve CERG document IDs unless the user intentionally creates a local numbering system.
5. Prefer tailoring, deferral, and role consolidation over deleting core operating-model content.
6. Record assumptions separately from facts.
7. Produce records and decisions, not just rewritten prose.
8. Keep the first adoption focused on the MVC spine unless a regulated overlay is clearly in scope.

## 2. Recommended agent context

Before helping with adoption, load these files:

1. [README.md](README.md)
2. [START-HERE.md](START-HERE.md)
3. [adoption-packs/cerg-lite/README.md](adoption-packs/cerg-lite/README.md)
4. [machine-readable/cerg-document-tiers.yaml](machine-readable/cerg-document-tiers.yaml)
5. [machine-readable/cerg-llm-index.json](machine-readable/cerg-llm-index.json)

Load additional documents only when the task requires them.

## 3. First prompt for CERG Lite

Copy and paste this into your agent:

```text
You are helping me adopt CERG Lite. Do not rewrite documents yet. First, help me decide whether CERG is appropriate for my organization and whether Lite, Standard, or Regulated applies. Ask one question at a time. Track assumptions separately from confirmed facts. When we are done, produce: adoption path recommendation, initial scope statement, role assignment draft, first 30-day checklist, and list of documents to defer.
```

## 4. Organization profile prompt

```text
Help me complete the CERG Organization Adaptation Profile. Use the CERG source documents as reference. Ask one question at a time for organization name, sector, headcount, systems in scope, data types, regulators, executive sponsor, security owner, risk acceptance authority, record locations, and review cadence. Do not invent answers. If I do not know, write "preliminary default requiring organizational calibration" and explain what decision is needed.
```

## 5. First records prompt

```text
Using CERG Lite, help me create the first operating records. Produce draft records for: role assignment, scope statement, evidence index, first risk register entry, first exposure backlog item, and first decision log entry. Keep each record short. Use fields from the CERG Record Catalog and Risk Register Templates where applicable.
```

## 6. Deferral prompt

```text
Review the CERG document tiers and help me decide what to defer for the first 30 days. For each deferred document or document group, give the reason, dependency risk, trigger for adoption, and whether the deferral is safe, conditional, or unsafe.
```

## 7. Regulated overlay prompt

Use this only if CUI, CMMC, NERC-CIP, SOX, ISO 27001, privacy, OT, or similar obligations are in scope.

```text
Help me identify CERG regulated overlays that may apply. Do not claim compliance. Ask about data types, contracts, systems, business processes, regulators, and assessment goals. Then produce a recommended overlay list, evidence implications, and documents that become required because of the overlay.
```

## 8. Contributor prompt

```text
I want to contribute to CERG. Read CONTRIBUTING.md and the document style guide before suggesting changes. Prefer improving existing documents over adding new ones. For any new artifact proposal, explain the adoption path, dependency, record produced, and why the content cannot fit in an existing document.
```

## 9. Agent deliverables checklist

A good first agent-assisted session should produce:

- Adoption path recommendation
- Initial scope statement
- Role assignment draft
- MVC document list
- Deferred document list with rationale
- First 30-day checklist
- First risk register entry
- First exposure backlog entry
- Questions requiring leadership decision

If the agent only rewrites policy text, it is not helping you adopt CERG. Adoption means owners, decisions, records, cadence, and evidence.
