## CERG Style Compliance Tracker

| | |
|---|---|
| **Document ID** | CERG-GOV-STY-002 |
| **Version** | 1.02 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

---

## 1. Purpose and Scope

This tracker records the current style and document-governance exceptions against [`CERG-GOV-STY-001`](CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md). It is a review record, not a second document catalog. [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) remains the authoritative inventory, and the Markdown corpus remains authoritative over generated artifacts.

The snapshot below covers cataloged CERG artifacts only. Repository guides, examples, issue templates, and other uncataloged supporting Markdown are not counted as governed artifacts.

## 2. Current Corpus Snapshot

**Review date:** 2026-10-27

| Measure | Current count | Basis |
|---|---:|---|
| Cataloged CERG artifacts | 129 | CAT-001 §5 as parsed by `tools/cerg-integrity-check.py` |
| Indexed source Markdown documents | 149 | `machine-readable/cerg-llm-index.json` and integrity-check file inventory |
| Cataloged artifacts with a lifecycle-control section | 128 (99%) | Review of cataloged source for Document Control, Procedure Control, or Plan Control sections |
| Cataloged artifacts with the current STY-001 metadata field set | 127 (98%) | Review of Document ID, version, status, classification, owner, parent, review cycle, frameworks, regulations, and environments |

Counts are deliberately derived during each review rather than copied into CAT-001. A catalog add, retirement, rename, or material metadata change triggers this tracker for reassessment.

## 3. Open Compliance Items

### 3.1 Operating Model Document Control

| Item | Affected artifact | Current state | Required action |
|---|---|---|---|
| Lifecycle-control section and complete metadata | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | The cataloged Operating Model lacks a recognized Document Control, Procedure Control, or Plan Control section and lacks explicit Regulations and Environments metadata fields. | Add a Document Control section and complete the metadata set at the next Operating Model review. Preserve OM-001 as the authoritative source for canonical role names and operating boundaries. |

### 3.2 Risk Register Template Parent Reference

| Item | Affected artifact | Current state | Required action |
|---|---|---|---|
| Parent artifact field | [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | The template has complete ownership and lifecycle metadata but lacks an explicit Parent Policy, Parent Document, or Parent Plan field. | Add the governing parent reference at the next template review without creating a competing source of truth for risk acceptance or record definitions. |

### 3.3 Review-Date Detection Coverage

The integrity checker validates dated `Next Scheduled Review` fields. This review identified that a fill-in example in a document can precede the actual lifecycle date and mask an overdue date. The checker is updated with this review to select the authoritative dated value rather than the first fill-in value it encounters.

## 4. Resolved or Confirmed Items

| Item | Current determination |
|---|---|
| Formerly reported missing Document Control sections | The current source review finds lifecycle-control sections for every cataloged artifact except OM-001. Earlier entries for PRC-VM-001 and PRC-RM-001 are no longer open. |
| Metadata-format exceptions | The current STY-001 field set is complete for 127 of 129 cataloged artifacts. The two remaining field-set gaps are tracked in Section 3. |
| Four-part workforce IDs | Four-part workforce IDs remain an approved compatibility form for the job-description family and are supported by the validator. |
| Incident Response ownership boundary | The Incident Response documents retain External Interface status and remain adjacent to CERG rather than CERG-owned operational incident-command artifacts. |
| Catalog count management | CAT-001 intentionally does not carry a hard-coded artifact total. The catalog parser and generated LLM index provide the review-time counts in Section 2. |

## 5. Review Method

Each quarterly review performs the following checks:

1. Run `python3 tools/cerg-validate.py` and require zero errors.
2. Run `python3 tools/cerg-integrity-check.py`; investigate P0 and P1 findings before closing the review and record any accepted P2 items.
3. Reconcile the CAT-001 parser count, LLM-index document count, and governed-source lifecycle-control review.
4. Confirm that each open tracker item names its authoritative source and does not create duplicate role, record, control, or risk-acceptance authority.
5. Update this tracker only when the recorded counts, exceptions, or review method change.

---

## 6. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-STY-002 |
| **Version** | 1.02 |
| **Status** | Approved |
| **Effective Date** | 2026-10-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly |
| **Next Scheduled Review** | 2027-01-27 |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.02 | 2026-10-27 | Governance Pillar Leader | Quarterly review completed. Rebuilt the tracker from the current corpus: recorded 129 cataloged artifacts, 149 indexed source documents, 128 lifecycle-control sections, and two remaining metadata or lifecycle exceptions. Removed stale duplicate history and corrected review-date detection coverage. |
| 1.01 | 2026-06-17 | Governance Pillar Leader | Added Document Control section. |

### Review Triggers

- Quarterly review cycle
- Any artifact added to, retired from, or renamed in the CERG library
- Material change to CAT-001, STY-001, validator behavior, or metadata conventions

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Document Authoring and Style Guide | [`CERG-GOV-STY-001`](CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) | Governs the style and lifecycle conventions tracked here |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative inventory and lifecycle status source |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Open lifecycle-control and metadata exception |
| Risk Register Templates and Reporting | [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Open parent-reference metadata exception |
