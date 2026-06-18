# CERG Machine-Readable Artifacts

This directory contains machine-readable YAML specifications generated from the CERG corpus. These files are designed for consumption by LLMs, automation tools, and programmatic validation.

> **⚠ These are DERIVED ARTIFACTS.** The CERG markdown corpus is authoritative. If a YAML file and its source disagree, the source wins. YAML files are regenerated when source documents change; manual edits are overwritten. See `METADATA.yaml` for per-file governance information.

## Maturity Status

| File | Status | Notes |
|------|--------|-------|
| `cerg-llm-index.json` | Production | Full local Markdown corpus index (131 docs, including README/meta/example files) |
| `cerg-manifest.yaml` | Production | Governed source artifact inventory (118 artifacts) with hashes, canonical paths, and LLM flags |
| `cerg-publication-manifest.yaml` | Production | Publication eligibility per governed artifact |
| `cerg-content-tags.yaml` | Production | Section-level content tags |
| `cerg-document-tiers.yaml` | Stable | Agent-friendly adoption tiers, loading order, and deferral guidance |
| `cerg-flows.yaml` | Production | 7 cross-pillar flow specifications |
| `cerg-record-schemas.yaml` | Production | Core operational record schemas |
| `cerg-runtime-model.yaml` | Stable | Core operational objects |
| `cerg-requirements.yaml` | **Pilot** | 85 atomic requirements extracted from 8 normative source documents. `owner_role` and `evidence_required` fields require population during adoption — see file header for instructions. |
| `cerg-vulnerability-priority-model.yaml` | Stable | Priority formula references CVSS-weighting — adopters should calibrate weights to their environment |
| All other schemas | Stable | Single-purpose companion schema files — adopt as-is or adapt |

## Adoption Checklist

For each machine-readable artifact:

1. **Verify source alignment.** Confirm the YAML matches the current state of its source CERG document(s).
2. **Populate adoption fields.** For `cerg-requirements.yaml`, assign `owner_role` and `evidence_required` for every mandatory requirement.
3. **Calibrate models.** For `cerg-vulnerability-priority-model.yaml`, validate that weights and SLAs match organizational policy.
4. **Test consumption.** Load the artifacts into your target system (GRC tool, SIEM, automation pipeline) and verify schema compatibility.
5. **Set regeneration triggers.** Define what source-document changes trigger artifact regeneration in your CI/CD pipeline.

## File Inventory

| File | Purpose | Source |
|------|---------|--------|
| `cerg-llm-index.json` | Full local Markdown corpus index for LLM/agent consumption | Repo-local Markdown corpus |
| `cerg-manifest.yaml` | Canonical manifest of all 118 governed CERG source artifacts with metadata, hashes, canonical paths, and LLM consumption flags | Governed Markdown artifact metadata |
| `cerg-publication-manifest.yaml` | Publication eligibility for each governed artifact — separates lifecycle approval from "safe to publish" | Document metadata |
| `cerg-content-tags.yaml` | Content type tags for every section heading in the corpus | All CERG documents |
| `cerg-document-tiers.yaml` | Adoption tiers, loading order, safe deferrals, and agent task mapping | README, START-HERE, IMP-005, MVC spine, adoption aids |
| `cerg-requirements.yaml` | Atomic requirements extracted from 8 normative source documents (pilot; not the MVC spine) | POL-001, STD-AC/IT/LM/RES/CR, CB-001, RMF-001 |
| `cerg-flows.yaml` | Cross-pillar operational flow specifications (7 flows) | FLOW-001 |
| `cerg-record-schemas.yaml` | Record template schemas (5 record types) | FLOW-001 §16 |
| `cerg-runtime-model.yaml` | Core operational objects and their relationships | CERG-ACT-006 |
| `cerg-control-evidence-map.yaml` | Control-to-evidence traceability | CB-001 |
| `cerg-evidence-schema.yaml` | Evidence lifecycle and object schema | CERG-ACT-008 |
| `cerg-metrics-model.yaml` | Decision-grade metrics model and CISO dashboard sections | MTR-001, CERG-ACT-009 |
| `cerg-crown-jewel-schema.yaml` | Crown Jewel register schema and criticality tiers | CERG-ACT-010 |
| `cerg-vulnerability-priority-model.yaml` | Risk-weighted vulnerability prioritization model | CERG-ACT-011 |
| `cerg-control-test-plan.yaml` | Control efficacy test plan schema | CERG-ACT-012 |
| `cerg-ir-interface.yaml` | CERG-to-IR interface contract | CERG-ACT-013 |
| `cerg-vendor-kill-switch.yaml` | Vendor access disablement procedure schema | CERG-ACT-014 |
| `cerg-tier-0-identity-profile.yaml` | Tier 0 identity controls for Crown Jewel systems | CERG-ACT-015 |
| `cerg-segmentation-schema.yaml` | Network segmentation verification schema | CERG-ACT-016 |
| `cerg-ai-system-intake.yaml` | AI/ML system security intake schema | CERG-ACT-017 |
| `cerg-workforce-capacity-model.yaml` | Workforce capacity model schema | CERG-ACT-018 |
| `cerg-decision-log.yaml` | Governance decision log schema | CERG-ACT-019 |

## How These Are Generated

Core indexes and manifests are generated from the repo-local CERG Markdown corpus during the build process. `cerg-manifest.yaml` and `cerg-publication-manifest.yaml` are regenerated with `python3 tools/regenerate-machine-readable.py`. `cerg-llm-index.json` is regenerated with `python3 tools/regenerate-llm-index.py`. The requirement register is regenerated when its normative source documents change. Single-purpose schema files are maintained alongside the documents they describe.

## For LLM Consumers

Start with `cerg-document-tiers.yaml` when choosing what to load for an adoption task, then use `cerg-llm-index.json` for the complete Markdown corpus map. Use `cerg-manifest.yaml` for governed source artifacts and canonical paths, then load `cerg-content-tags.yaml` to understand what each section contains. Use `cerg-requirements.yaml` for traceable obligations after populating adoption-specific fields. Use the individual schema files for structured field definitions.
