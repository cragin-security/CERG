
# SURGE: Cyber Engineering, Risk & Governance

## DOCUMENT AUTHORING AND STYLE GUIDE
### House Voice · Metadata · Structure · Cross-References · Skeleton · Quality Gates

---

| | |
|---|---|
| **Document ID** | CERG-GOV-STY-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) · [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) |
| **Review Cycle** | Annual / On material change to catalog, naming, role, or rendering conventions |
| **Frameworks** | NIST CSF 2.0 GOVERN · ISO/IEC 27001 A.5 · NIST 800-53r5 PM |
| **Regulations** | Cross-cutting |
| **Environments** | CERG documentation library |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [CERG House Voice](#2-cerg-house-voice)
3. [Document Anatomy](#3-document-anatomy)
4. [Metadata Rules](#4-metadata-rules)
5. [ID, File Name, and Status Rules](#5-id-file-name-and-status-rules)
6. [Role and RACI Rules](#6-role-and-raci-rules)
7. [Cross-Reference Rules](#7-cross-reference-rules)
8. [Callouts, Tables, and Lists](#8-callouts-tables-and-lists)
9. [Language and Style Rules](#9-language-and-style-rules)
10. [Org-Adaptation and Token Rules](#10-org-adaptation-and-token-rules)
11. [Blank Document Skeleton](#11-blank-document-skeleton)
12. [Quality Gates Before Commit](#12-quality-gates-before-commit)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

This guide defines how CERG documents are authored, reviewed, and kept consistent. It is the companion to the catalog. The catalog governs IDs, registration, status, and cross-reference discipline. This guide governs the writing pattern, metadata pattern, document skeleton, role discipline, quality gates, and house voice.

It applies to every new or revised CERG policy, governance instrument, standard, procedure, plan, template, and operational package.

> **Consistency Is a Control**
>
> A framework that looks like 60 unrelated documents is not a framework. Consistent structure, vocabulary, role names, metadata, and cross-references make the library operational. A reader should be able to open any artifact and know where to find scope, roles, evidence, approvals, and revision history without hunting.

---

## 2. CERG House Voice

CERG writing is:

- direct;
- practical;
- declarative;
- evidence-oriented;
- opinionated where ambiguity would create risk;
- clear about ownership and handoffs;
- usable by a small team without weakening the role model.

CERG writing is not:

- vendor marketing copy;
- legal boilerplate without operational direction;
- generic security advice;
- a list of controls without owners or evidence;
- a maturity fantasy that assumes a large staff;
- a compliance checklist with no operating model.

A CERG artifact should answer five questions quickly:

1. What does this document govern?
2. Who owns it?
3. What must happen?
4. What proves it happened?
5. Where does a reader go next?

---

## 3. Document Anatomy

Every full CERG artifact follows this structure unless the document type requires a narrow exception.

| **Section** | **Purpose** | **Required** |
|---|---|---|
| Title block | Names the artifact and subtitle. | Yes |
| Metadata table | Identifies ID, status, owner, parent, supporting documents, review cycle, frameworks, regulations, environments. | Yes |
| Table of Contents | Gives predictable navigation. | Yes for substantive artifacts |
| Purpose and Scope | Defines why the artifact exists and what it covers. | Yes |
| Operating content | Requirements, process, template, plan, or instrument body. | Yes |
| Roles and Responsibilities | Shows canonical role accountability. | Yes when the body assigns work |
| Evidence, metrics, or outputs | Shows what proves the process or control worked. | Yes where applicable |
| Document Control | Records version, approval, review, revision history, and triggers. | Yes |
| Related Documents | Lists authoritative links to related artifacts. | Yes |

---

## 4. Metadata Rules

Use this field set unless a sibling document of the same type uses a clearly established variant.

| **Field** | **Rule** |
|---|---|
| Document ID | Must match catalog ID and file name stem. |
| Version | New artifacts start at `1.0`. Catalog amendments increment the catalog version. |
| Status | New artifacts start as `Draft` unless the human owner has explicitly approved. |
| Classification | Use `Public` unless the artifact contains sensitive operational detail. |
| Owner | Use a canonical role from `CERG-GOV-OM-001` or an already established artifact owner. |
| Parent Policy / Parent Document / Parent Plan | Link to the governing artifact. |
| Supporting Documents | Link only to cataloged or roadmap-reserved artifacts. |
| Review Cycle | Use concrete cadence and trigger conditions. |
| Frameworks | Cite major frameworks that shape the artifact. |
| Regulations | List applicable regulatory drivers or `Cross-cutting`. |
| Environments | State the scope clearly. |

Metadata is not decorative. It is how the document participates in governance, audit, evidence, and lifecycle management.

---

## 5. ID, File Name, and Status Rules

### 5.1 ID Pattern

CERG IDs follow:

`CERG-<TYPE>-<DOMAIN>-<NNN>`

Examples:

| **Type** | **Example** | **Meaning** |
|---|---|---|
| `GOV` | `CERG-GOV-CAT-001` | Governance instrument |
| `STD` | `CERG-STD-AC-001` | Standard |
| `PRC` | `CERG-PRC-RM-001` | Procedure |
| `PLN` | `CERG-PLN-ISO-001` | Plan or operational package |
| `TMPL` | `CERG-TMPL-RM-002` | Standalone template |

New domain codes require a catalog amendment before the batch is complete.

### 5.2 File Name Pattern

Use:

`CERG-<TYPE>-<DOMAIN>-<NNN>_Readable_Title_With_Underscores.md`

Do not rename existing files casually. Links, catalog rows, and references depend on stable paths.

### 5.3 Status Pattern

| **Status** | **Use** |
|---|---|
| Draft | New artifact awaiting formal approval. |
| Approved | Human owner has approved the artifact for use. |
| Published | Catalog or public-facing instrument formally maintained as active. |
| Retired | Artifact no longer authoritative but retained for history. |

Do not self-approve new artifacts. If approval is pending, write `CISO (pending)` or the appropriate pending approver.

---

## 6. Role and RACI Rules

Use only canonical role names from `CERG-GOV-OM-001` and assignments from `CERG-GOV-RAC-001`.

Rules:

1. Do not invent role names.
2. Do not use synonyms if the canonical role exists.
3. A local roles table may explain responsibilities for the reader, but it must conform to `CERG-GOV-RAC-001`.
4. Scaling down is done by role consolidation onto fewer people, not by deleting roles.
5. Exactly one role is accountable for each activity where a RACI is used.
6. External teams may own adjacent programs; preserve those boundaries.

Examples of role discipline:

| **Avoid** | **Use Instead** |
|---|---|
| Security team | Governance Pillar Leader, Risk Pillar Leader, or Engineering Pillar Leader, as appropriate |
| AppSec owner | Application Security Engineer |
| Audit person | Evidence Librarian or Governance Pillar Leader |
| Vendor owner | Vendor Risk Analyst or Business Owner, depending on context |
| Executive security lead | Chief Information Security Officer (CISO) |

---

## 7. Cross-Reference Rules

The catalog's rules govern. This guide repeats the operational version for authors:

1. Link only to artifacts in the catalog or roadmap.
2. Prefer Document ID over title in prose.
3. Use relative Markdown links to repo files.
4. Mark planned artifacts as `(Planned, V1.x)` or `(Planned, V2)`.
5. Do not cite a file that does not exist unless it is in the roadmap.
6. If an artifact is newly created, amend the catalog in the same batch.
7. If a related document is out of scope, state the boundary instead of inventing a fake artifact.

Good cross-reference:

`See [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) for risk treatment workflow.`

Weak cross-reference:

`See the risk procedure.`

---

## 8. Callouts, Tables, and Lists

### 8.1 Callouts

Use callouts to sharpen important guidance.

Pattern:

```markdown
> **Short Title**
>
> Practical explanation. Make the point directly. Avoid generic warnings.
```

Callouts should state a principle, pitfall, or operating rule. They should not repeat the paragraph above them.

### 8.2 Tables

Use tables when a reader must compare fields, owners, statuses, evidence, cadence, or approvals.

Rules:

- keep column names short;
- use canonical role names;
- make required fields obvious;
- avoid sprawling tables when a short list is clearer;
- include evidence or output columns when the table describes activity.

### 8.3 Lists

Use numbered lists for sequence. Use bullets for sets.

---

## 9. Language and Style Rules

### 9.1 Required Style

- Use active voice.
- Use direct verbs: owns, approves, records, reviews, escalates.
- Define thresholds, cadences, outputs, and evidence.
- Name the role that owns an activity.
- Prefer concrete nouns over vague terms.
- Use short paragraphs.

### 9.2 Prohibited or Discouraged Style

- No em dashes.
- Avoid passive constructions that hide ownership.
- Avoid `should` when the document creates a requirement. Use `must`, `shall`, or direct imperative language where appropriate.
- Avoid generic phrases such as `best practice`, `robust security`, or `industry standard` unless immediately defined.
- Do not cite regulations as decoration. Cite them when the artifact operationalizes a requirement.
- Do not add AI-tool attribution in commits, comments, or document text.

### 9.3 Terminology

| **Use** | **Avoid** |
|---|---|
| artifact | document thing, policy item |
| evidence | proof, support, backup material |
| accountable role | owner in vague contexts |
| residual risk | remaining risk when controls are considered |
| exception | waiver, unless the parent process uses waiver as a synonym |
| review cycle | cadence, unless speaking informally |

---

## 10. Org-Adaptation and Token Rules

`CERG-GOV-VAR-001` governs organization adaptation. Authors must not scatter hard-coded organization facts when a token should be used.

Rules:

1. Tokenize organization identity, scale, and example values when they are meant to vary by adopting organization.
2. Do not tokenize framework IDs, role names, core CERG terms, or control IDs.
3. Keep literal token examples intact in documents that teach the token scheme.
4. Run `python3 tools/cerg-render.py --check` before committing.
5. Do not edit rendered output back into source files unless the change is deliberate.

---

## 11. Blank Document Skeleton

Copy this skeleton for new substantive artifacts.

```markdown
# SURGE: Cyber Engineering, Risk & Governance

## [DOCUMENT TITLE]
### [Subtitle: Topic · Topic · Topic]

---

| | |
|---|---|
| **Document ID** | CERG-[TYPE]-[DOMAIN]-[NNN] |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | [Canonical role] |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [Document links] |
| **Review Cycle** | Annual / [trigger] |
| **Frameworks** | [Frameworks] |
| **Regulations** | [Regulations] |
| **Environments** | [Scope] |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Operating Requirements](#2-operating-requirements)
3. [Roles and Responsibilities](#3-roles-and-responsibilities)
4. [Evidence and Metrics](#4-evidence-and-metrics)
5. [Document Control](#5-document-control)

---

## 1. Purpose and Scope

[Explain what this artifact governs and what is out of scope.]

> **[Callout Title]**
>
> [Sharp operating principle or pitfall.]

---

## 2. Operating Requirements

[Requirements, process, plan, or template content.]

---

## 3. Roles and Responsibilities

| **Role** | **Responsibility** |
|---|---|
| [Canonical role] | [Responsibility] |

---

## 4. Evidence and Metrics

| **Evidence / Metric** | **Owner** | **Cadence** | **Location** |
|---|---|---|---|
| [Evidence] | [Role] | [Cadence] | [Location] |

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-[TYPE]-[DOMAIN]-[NNN] |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [YYYY-MM-DD] |
| **Classification** | Public |
| **Owner** | [Canonical role] |
| **Approved By** | CISO (pending) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on [trigger] |
| **Next Scheduled Review** | [YYYY-MM-DD] |
| **Frameworks** | [Frameworks] |
| **Regulations** | [Regulations] |
| **Environments** | [Scope] |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | [YYYY-MM-DD] | Cyber Governance | Initial release. |

### Review Triggers

- [Trigger]

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| [Title] | [ID](path.md) | [Relationship] |
```

---

## 12. Quality Gates Before Commit

Every contribution must pass these gates before commit:

| **Gate** | **Command / Check** | **Pass Condition** |
|---|---|---|
| No em dash characters | Search files for the prohibited em dash character | No output |
| Render check | `python3 tools/cerg-render.py --check` | Passes |
| Catalog registration | Inspect `CERG-GOV-CAT-001` | New artifact listed or planned entry updated |
| Role discipline | Compare against `CERG-GOV-OM-001` and `CERG-GOV-RAC-001` | No invented roles |
| Cross-reference discipline | Follow internal links or use a link checker when available | No dead links |
| Status discipline | Inspect metadata and Document Control | New artifact is Draft unless approved |
| Commit message hygiene | Review commit text | No AI-tool attribution |

A document is not complete until the catalog is amended where required.

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-STY-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to catalog, naming, role, or rendering conventions |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST CSF 2.0 GOVERN; ISO/IEC 27001 A.5; NIST 800-53r5 PM |
| **Regulations** | Cross-cutting |
| **Environments** | CERG documentation library |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes the CERG house style, metadata and skeleton rules, role and cross-reference discipline, language rules, org-adaptation guidance, and pre-commit quality gates. |

### Review Triggers

- Catalog structure or cross-reference rule change
- Role roster or RACI change
- Org-adaptation token scheme change
- Quality gate or render tool change
- New artifact type introduced
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative ID, catalog, status, roadmap, and cross-reference rule source |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster source |
| Consolidated Roles and RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | RACI and role assignment source |
| Organization Adaptation Profile | [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Org-token and rendering guidance |
