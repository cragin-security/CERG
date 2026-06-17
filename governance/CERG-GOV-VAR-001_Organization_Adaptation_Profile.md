
# SURGE: Cyber Engineering, Risk & Governance

## ORGANIZATION ADAPTATION PROFILE
### Token Scheme · Values File · Render Tool

---

| | |
|---|---|
| **Document ID** | CERG-GOV-VAR-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) · [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) |
| **Review Cycle** | Annual / On any change to the token scheme |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How Adaptation Works](#2-how-adaptation-works)
3. [The Token Scheme](#3-the-token-scheme)
4. [Token Catalog](#4-token-catalog)
5. [The Organization Profile File](#5-the-organization-profile-file)
6. [The Render Tool](#6-the-render-tool)
7. [The Phrase Map](#7-the-phrase-map)
8. [Adaptation Workflow](#8-adaptation-workflow)
9. [Rules and Discipline](#9-rules-and-discipline)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

The CERG README says: "Drop it in, adapt the names and org structure to fit yours, and you have a functioning program." That sentence hides a problem. There has never been a map of *what* to adapt. An adopter who wants to change "the organization" to their own name, or scale the headcount figures down, or swap the illustrative sector, has had to read all 28 documents and find every occurrence by hand. That is slow, it is error-prone, and it is the kind of work that gets done once and then drifts.

This document removes that problem. It defines a token scheme, ships a single values file an organization fills in once, and ships a render tool that produces an organization-specific copy of the entire corpus in one command.

It applies to every adopter of CERG and to every CERG artifact that contains adaptable text.

> **Adaptation Is Mechanical**
>
> Adapting CERG is not a creative act. It is a substitution. Names, headcounts, sectors, regulators, and illustrative examples are variables; the framework around them is fixed. The moment adaptation becomes hand-editing prose, version discipline is lost. Fill in the profile once. Render. Review the output. That is the whole job.

---

## 2. How Adaptation Works

CERG separates two kinds of content.

**Fixed content** is the framework itself: the three pillars, the canonical role roster, the control baseline, the procedures, the cross-reference rules. This content does not change between adopters. It is the product.

**Variable content** is everything that names a specific organization: the organization's name, its sector, its size, the regulators it answers to, the names of its standing teams, and the illustrative examples chosen to make a point. This content is different for every adopter.

Adaptation is the act of replacing variable content with an organization's own values. CERG does this in two layers:

1. **Tokens.** Explicit variable tokens of the form `{{TOKEN_NAME}}`. Any new CERG content, and any organization-maintained content, uses tokens directly. The render tool substitutes them.
2. **The phrase map.** The V1 corpus was written before the token scheme existed, so it contains hard-coded variable phrases (for example, a specific headcount used as a scaling upper bound). The phrase map is a configurable list of those known phrases and the token each maps to. The render tool applies it so the existing corpus adapts without the source files being rewritten.

The published corpus is left intact and generic. The render tool produces a separate, organization-specific output. The source stays the master; the output is an export, exactly as [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) requires.

> **Why Not Just Edit the 28 Documents**
>
> Tokenizing all 28 published, approved documents in place is a corpus-wide normalization pass that touches every artifact and changes every revision history. That is its own scoped piece of work, not a side effect of adoption. Until it is done, the phrase map carries the load: it adapts the existing corpus at render time without mutating a single approved source file. New documents use tokens natively from day one.

---

## 3. The Token Scheme

A token is an uppercase identifier wrapped in double braces.

```
{{TOKEN_NAME}}
```

Rules for tokens:

- **Uppercase, underscore-separated.** `{{ORG_NAME}}`, not `{{OrgName}}` or `{{org-name}}`.
- **Double braces, no spaces.** `{{ORG_NAME}}`, not `{{ ORG_NAME }}` or `{ORG_NAME}`. The double-brace form is chosen because it does not collide with Markdown syntax and is visually obvious in a draft.
- **Every token appears in the catalog.** Section 4 is the authoritative list. A token used in a document but absent from the catalog is an error the render tool reports.
- **Tokens never appear in fixed content.** Role names stay canonical (see Section 9). The three pillars are never tokenized. Document IDs are never tokenized.
- **A token has exactly one meaning.** `{{REGULATORS}}` is always the full regulator list. It is never reused to mean something else in another document.

> **Tokens Are Not for Roles**
>
> The single most important rule. Canonical role names from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1 are fixed content. They are never tokenized. "Governance Pillar Leader" is written literally, every time, in every document. If an organization renames that seat internally, that mapping lives in the organization's own role-assignment map, not in the CERG corpus. Tokenizing a role would let an adopter silently rename a seat and break every cross-reference that depends on it.

---

## 4. Token Catalog

This is the authoritative list of tokens. New tokens are added only by amendment to this document.

### 4.1 Organization Identity

| **Token** | **Meaning** | **Example Value** |
|---|---|---|
| `{{ORG_NAME}}` | The organization's common name, as used in running prose. | `Northwind Energy` |
| `{{ORG_LEGAL_NAME}}` | The full legal entity name, for cover pages and approvals. | `Northwind Energy Holdings, Inc.` |
| `{{ORG_SHORT_NAME}}` | A short form or abbreviation. | `Northwind` |
| `{{ORG_SECTOR}}` | The industry sector, used in illustrative examples. | `[your sector]` |
| `{{ORG_CONTENT_REPO}}` | Where the authoritative Markdown corpus lives. | `https://git.example.com/security/cerg` |

### 4.2 Program Identity

| **Token** | **Meaning** | **Example Value** |
|---|---|---|
| `{{PROGRAM_NAME}}` | The name the organization gives its security program. Defaults to `CERG`. | `CERG` |
| `{{PROGRAM_ACRONYM}}` | The pronounced acronym for the pillar set. Defaults to `SURGE`. | `SURGE` |

### 4.3 Scale and Structure

| **Token** | **Meaning** | **Example Value** |
|---|---|---|
| `{{TOTAL_EMPLOYEES}}` | Headcount of the organization. | `[your headcount]` |
| `{{PROTECTED_POPULATION}}` | Total population of identities, devices, and access relationships managed. | `[your number]` |
| `{{CERG_TEAM_SIZE}}` | Size of the security team running the program. | `[your team size]` |
| `{{ENG_STAFF}}` | Headcount in the Engineering pillar. | `14` |
| `{{RISK_STAFF}}` | Headcount in the Risk pillar. | `15` |
| `{{GOV_STAFF}}` | Headcount in the Governance pillar. | `13` |
| `{{SCALE_TIER}}` | The reference scale band this adopter sits in: `small`, `mid`, or `large`. | `[small, mid, or large]` |

### 4.4 Oversight and Standing Teams

| **Token** | **Meaning** | **Example Value** |
|---|---|---|
| `{{COG_NAME}}` | The organization's name for the Cyber Oversight Group, the CISO reporting body. | `Cyber Oversight Group` |
| `{{IR_TEAM_NAME}}` | The name of the standing Incident Response team that owns `CERG-PLN-IR-001`. | `Security Incident Response Team` |
| `{{EXEC_BODY_NAME}}` | The executive or board body that endorses the policy. | `Risk and Audit Committee` |

### 4.5 Regulatory Context

| **Token** | **Meaning** | **Example Value** |
|---|---|---|
| `{{REGULATORS}}` | The full list of regulators and frameworks in scope. | `NERC-CIP, CMMC L2, SOX ITGC` |
| `{{PRIMARY_REGULATOR}}` | The single most consequential regulator, used where one example is needed. | `NERC-CIP` |

### 4.6 Contact and Control

| **Token** | **Meaning** | **Example Value** |
|---|---|---|
| `{{SECURITY_CONTACT}}` | The published contact address for security matters. | `security@example.com` |
| `{{DOC_CONTROL_CONTACT}}` | The contact for document-control questions. | `cerg-docs@example.com` |
| `{{ADOPTION_DATE}}` | The date the organization adopted CERG. | `2026-05-21` |

> **The Scale Figures Are an Upper Bound**
>
> The V1 corpus uses a large-enterprise illustration as a deliberate upper bound, so readers can scale down. The scale tokens in §4.3 exist precisely so an adopter can replace that upper bound with their own reality. A five-person team sets `{{CERG_TEAM_SIZE}}` to `5` and `{{SCALE_TIER}}` to `small`, and the rendered corpus stops describing a large-enterprise organization back to them.

---

## 5. The Organization Profile File

An adopter fills in exactly one file: `cerg-org-profile.yml`. It lives at the root of the adopter's content repository. It is the single source of truth for every token value.

The file ships in the repository pre-populated with the V1 reference values (the upper-bound illustration), so an adopter sees a working example and edits it down to their own organization.

The file structure mirrors the catalog in Section 4: one block per category, one key per token (lowercase form of the token name). The render tool reads this file and nothing else for token values.

> **One File, One Source of Truth**
>
> Every token value lives in `cerg-org-profile.yml`. Not in a second file, not in a wiki page, not in someone's head. When a value changes, it changes in one place and the next render propagates it everywhere. An organization that maintains token values in more than one place has recreated the drift problem this scheme exists to remove.

---

## 6. The Render Tool

The render tool is `tools/cerg-render.py`. It is a single Python script with no dependencies outside the standard library, so it runs anywhere Python 3 runs.

### 6.1 What It Does

1. Reads `cerg-org-profile.yml`.
2. Walks the corpus for Markdown files.
3. For each file, applies the phrase map (Section 7), then substitutes every `{{TOKEN}}`.
4. Writes the result to an output directory, leaving the source untouched.
5. Reports any token found in a document that is not in the profile, and any profile key that maps to no catalog token.

### 6.2 Usage

```
# Render the whole corpus into ./rendered using ./cerg-org-profile.yml
python3 tools/cerg-render.py

# Explicit paths
python3 tools/cerg-render.py --profile cerg-org-profile.yml --source . --out rendered

# Check only: report unresolved tokens and exit non-zero if any are found.
# Does not write output. Use this in CI.
python3 tools/cerg-render.py --check
```

### 6.3 Exit Behavior

The tool exits non-zero if it finds an unresolved token (a `{{TOKEN}}` with no value in the profile) or an unknown token (a `{{TOKEN}}` not in the catalog). This makes `--check` usable as a continuous-integration gate: a document that introduces a token without registering it fails the build.

---

## 7. The Phrase Map

The phrase map handles hard-coded variable text in the V1 corpus, text written before tokens existed. It is a list of exact phrases and the rendered replacement each should receive. It is defined inside the render tool and is editable by the adopter.

The V1 phrase map covers the known hard-coded strings, primarily the upper-bound scale figures. As the corpus is progressively tokenized in future work, phrase-map entries are retired and replaced by native tokens. The phrase map is a bridge, not a permanent fixture.

> **The Phrase Map Shrinks Over Time**
>
> Every phrase-map entry is debt. It exists because a document contains a hard-coded value instead of a token. The correct long-term fix is to tokenize the source. Until then the phrase map carries it. A healthy CERG corpus has a phrase map that gets shorter with each release, not longer.

---

## 8. Adaptation Workflow

This is the workflow an adopter follows. It is referenced by [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §5.1, step 2.

| **Step** | **Action** | **Role** |
|---|---|---|
| 1 | Copy `cerg-org-profile.yml` and fill in every token value for the organization. | Policy & Standards Manager |
| 2 | Run `python3 tools/cerg-render.py --check` and resolve every reported unresolved token. | Policy & Standards Manager |
| 3 | Run `python3 tools/cerg-render.py` to produce the rendered corpus. | Policy & Standards Manager |
| 4 | Review the rendered output. Confirm names, scale figures, and examples read correctly. | Governance Pillar Leader |
| 5 | Publish the rendered corpus as the organization's working library. The CERG source remains the upstream master for future updates. | Governance Pillar Leader |

When CERG publishes an update upstream, the adopter pulls the new source, updates the profile if new tokens were added, and re-renders. The organization's values are never lost because they live in one file, separate from the corpus.

---

## 9. Rules and Discipline

1. **Never tokenize a canonical role name.** Roles from [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1 are fixed content. See the callout in Section 3.
2. **Never tokenize a Document ID.** IDs are stable identifiers. `CERG-GOV-VAR-001` is written literally, always.
3. **Never tokenize the pillar names.** Cyber Engineering, Cyber Risk, and Cyber Governance are the framework. They are fixed.
4. **Every token is in the catalog.** A token not in Section 4 is invalid. Add it by amendment before using it.
5. **One profile file.** All values live in `cerg-org-profile.yml`. See the callout in Section 5.
6. **Render; do not hand-edit.** Adaptation is the render tool. Hand-editing the rendered output breaks the ability to re-render on the next upstream update.
7. **The source stays generic.** The CERG corpus in this repository is never rendered in place. Rendering produces a separate output for a separate organization.

---

## 10. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-VAR-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to the token scheme |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-21 | Cyber Governance | Initial release. Establishes the token scheme, the token catalog, the `cerg-org-profile.yml` values file, the `cerg-render.py` render tool, the phrase map bridge for the un-tokenized V1 corpus, the adaptation workflow, and the adaptation discipline rules. |

### Review Triggers

- A new token is required by a new or revised CERG artifact
- The canonical role roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1 changes
- The corpus is tokenized in place, retiring phrase-map entries
- Adopter feedback indicating a missing or ambiguous token
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Document Control) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative artifact inventory; source-versus-export rule |
| Implementation and Adaptation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Consumer of the adaptation workflow defined here |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster; roles are never tokenized |
