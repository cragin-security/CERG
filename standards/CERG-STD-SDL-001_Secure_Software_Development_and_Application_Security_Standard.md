## SECURE SOFTWARE DEVELOPMENT AND APPLICATION SECURITY STANDARD
### Secure SDLC · Code Review Gates · SAST/DAST/SCA · Secrets · Dependencies and SBOM · Pipeline Security

---

| | |
|---|---|
| **Document ID** | CERG-STD-SDL-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Application Security) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Review Cycle** | Annual / On NIST SSDF revision · On material toolchain change |
| **Frameworks** | [NIST SSDF 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (SA, SI, CM families) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) · OWASP SAMM · [NIST 800-161r1](https://csrc.nist.gov/pubs/sp/800/161/r1/final) (software supply chain) · [SLSA](https://slsa.dev/) |
| **Regulations** | CMMC L2 / 800-171r3 (3.4.x, 3.13.x, 3.14.x) · SOX ITGC (change management) · NERC-CIP (where software supports BES Cyber Systems) |
| **Environments** | All CERG-managed software: in-house applications, scripts, infrastructure-as-code, integration code, and automation |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [The Secure SDLC](#3-the-secure-sdlc)
4. [Security Gates](#4-security-gates)
5. [Code Review Requirements](#5-code-review-requirements)
6. [Automated Security Testing: SAST, DAST, SCA](#6-automated-security-testing-sast-dast-sca)
7. [Secrets in Code](#7-secrets-in-code)
8. [Dependencies and Software Bill of Materials](#8-dependencies-and-software-bill-of-materials)
9. [Pipeline and Build Security](#9-pipeline-and-build-security)
10. [Infrastructure as Code](#10-infrastructure-as-code)
11. [Vulnerability Handling for Software](#11-vulnerability-handling-for-software)
12. [Roles and Responsibilities](#12-roles-and-responsibilities)
13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Scope

The Cyber Engineering pillar exists to build securely. Its mission statement, set in [`CERG-GOV-FRM-001`](../governance/CERG-GOV-FRM-001_CERG_Framework.md), is "build securely, deploy confidently, consult continuously." Until this standard, the program had no document that said what building securely actually requires. The architecture review procedure [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) governs the engagement; this standard governs the code.

This standard establishes the requirements for secure software development across the CERG-managed estate: how software moves through a secure development lifecycle, the security gates it passes, the code review and automated testing it is subject to, how secrets and dependencies are handled, and how the build pipeline that produces it is itself secured.

It applies to every piece of software CERG-managed teams write or materially modify: customer-facing and internal applications, microservices and APIs, scripts and automation, integration and glue code, and infrastructure-as-code. It does not govern the security of purchased software, which is handled by [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md), except where purchased components are embedded as dependencies (Section 8).

> **The Standard Is a Floor, Applied by Risk Tier**
>
> Not every script needs a penetration test. This standard sets the minimum bar for all software and then scales the rigor by the risk tier of what is being built. A throwaway internal report generator and an internet-facing application that processes regulated data are both in scope; they are not subject to the same gate intensity. Section 3.2 defines the tiers. The floor is never zero, and it is never optional.

---

## 2. Principles

Six principles govern secure development in CERG.

1. **Shift left, but do not shift blind.** Security findings are cheapest to fix before code is written and most expensive after release. Testing, review, and threat modeling happen as early as the lifecycle allows. But early testing that no one acts on is theater; every gate has an owner and a consequence.
2. **The pipeline is the enforcement point.** A requirement that depends on a developer remembering it will be forgotten. Security requirements are enforced by the build pipeline wherever a machine can enforce them. Human review is reserved for what a machine cannot judge.
3. **Build securely; do not own the result.** Consistent with the Engineering pillar mission, Engineering builds software securely and hands it off. Engineering does not become the permanent operator of every application it helps build. Security posture travels with the handoff.
4. **A finding is a risk until it is closed or accepted.** An open security finding is not a backlog item that quietly ages out. It is closed, or it is risk-accepted through [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). There is no third option.
5. **Provenance is part of the product.** Software that cannot be traced to its source, its dependencies, and its build is not trusted. Every release carries a Software Bill of Materials and a verifiable build provenance.
6. **Secrets never live in code.** This principle is absolute and has no risk-tier exception. Section 7.

---

## 3. The Secure SDLC

### 3.1 Lifecycle Phases

Secure development is not a phase bolted onto delivery. Security activity is defined for every phase of the lifecycle.

| **Phase** | **Security Activity** | **Primary Owner** |
|---|---|---|
| Requirements | Security and abuse-case requirements captured; data classification per [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) identified. | Application Security Engineer |
| Design | Threat modeling; architecture review intake per [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). | Application Security Engineer |
| Implementation | Secure coding practice; SAST and SCA in the developer loop; secrets scanning. | Engineering Pillar Leader |
| Verification | DAST; code review gate; pre-production review per [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). | Pre-production Reviewer |
| Release | Build provenance and SBOM generated; release gate cleared. | Application Security Engineer |
| Operation and handoff | Security posture documented; dependency monitoring active; ownership transferred. | Engineering Pillar Leader |

### 3.2 Software Risk Tiers

The intensity of the gates in Section 4 scales by software risk tier. The tier is assigned at requirements and confirmed at design review.

| **Tier** | **Definition** | **Examples** |
|---|---|---|
| **Tier 1 - Critical** | Internet-facing, or processes regulated or Confidential data, or supports a BES Cyber System or a SOX-relevant financial process. | Customer portal; API handling CUI; software in NERC-CIP scope. |
| **Tier 2 - Standard** | Internal application or service not in Tier 1, handling internal-classified data. | Internal workflow tool; internal reporting service. |
| **Tier 3 - Minimal** | Low-impact internal automation, scripts, and tooling with no regulated data and no production blast radius. | A scheduled internal report generator; a developer utility. |

> **Tier Is Assigned, Not Assumed**
>
> A team does not get to call its own software Tier 3 to avoid the gates. The tier is proposed by the building team and confirmed by the Application Security Engineer at design review. When in doubt, the higher tier applies. Disagreements are resolved by the Engineering Pillar Leader, and a tier decision that lowers rigor is recorded.

---

## 4. Security Gates

A security gate is a checkpoint software must clear to advance. Gates are enforced by the pipeline (Section 9) wherever automatable.

### 4.1 The Gate Set

| **Gate** | **Tier 1** | **Tier 2** | **Tier 3** | **Blocks On** |
|---|---|---|---|---|
| Threat model complete | Required | Required | Recommended | Missing or stale threat model |
| SAST clean | Required | Required | Required | Any unresolved High or Critical finding |
| SCA clean | Required | Required | Required | Any dependency with a known High or Critical vulnerability and no exception |
| Secrets scan clean | Required | Required | Required | Any detected secret (no exception) |
| Code review approved | Required, 2 reviewers | Required, 1 reviewer | Required, 1 reviewer | Unapproved change to a protected branch |
| DAST clean | Required | Recommended | Not required | Any unresolved High or Critical finding |
| SBOM generated | Required | Required | Required | Missing SBOM |
| Build provenance attested | Required | Required | Recommended | Unverifiable build |
| Pre-production review signed | Required | Required | Not required | Unsigned go-live readiness per [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) |

### 4.2 Gate Bypass

A gate is bypassed only through a risk exception filed under [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). The exception names the gate, the reason, the compensating control, and an expiry. A bypassed gate without a filed exception is a control failure, and the build is not released. The secrets-scan gate is the one gate that is never bypassed.

---

## 5. Code Review Requirements

1. **Every change to a protected branch is reviewed.** No change reaches a release branch without at least one approving review from someone other than the author. Tier 1 software requires two approving reviewers.
2. **The reviewer is competent in the change.** A review approval asserts the reviewer understood the change and saw no security defect. An approval given without reading the change is a falsified control.
3. **Author cannot self-approve.** The person who wrote the change cannot be a required approver of it. This holds even on a small team; if only one other person can review, that person reviews.
4. **Security-sensitive changes pull in Application Security.** Changes to authentication, authorization, cryptography, input handling, or data export require an Application Security Engineer among the reviewers, regardless of tier.
5. **Review evidence is retained.** The review record (who approved, when, against which commit) is retained as control evidence and is auditable.

> **Small Teams Still Separate Author From Approver**
>
> On a five-person team the temptation is to let a developer merge their own code because "there is no one else." There is someone else. The separation of author from approver is the single most effective software control CERG mandates, and it does not scale away. If genuinely only one person can review a given change, that one person reviews it. The author still does not approve their own work.

---

## 6. Automated Security Testing: SAST, DAST, SCA

### 6.1 Static Application Security Testing (SAST)

SAST runs on every commit to a protected branch and in the developer loop where the toolchain supports it. SAST findings at High or Critical block the SAST gate. The SAST ruleset is owned by the Application Security Engineer and reviewed at least annually. False positives are suppressed with a recorded, reviewable justification, not by disabling the rule.

### 6.2 Dynamic Application Security Testing (DAST)

DAST runs against a deployed pre-production instance for Tier 1 software and is recommended for Tier 2. DAST covers the OWASP application risk categories at minimum. High and Critical DAST findings block the DAST gate.

### 6.3 Software Composition Analysis (SCA)

SCA inventories third-party and open-source dependencies and checks them against known-vulnerability data. SCA runs on every build. A dependency carrying a known High or Critical vulnerability blocks the SCA gate until the dependency is updated, replaced, or an exception is filed. SCA output feeds the SBOM in Section 8.

### 6.4 Tooling Discipline

The specific tools are an implementation choice and are not named in this standard, so the standard survives a toolchain change. What the standard fixes is that SAST, DAST, and SCA capability exists, runs in the pipeline, and gates releases. An organization adopting CERG selects tools that meet that bar; the [`CERG-GOV-VAR-001`](../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) profile is the right place to record the selected toolchain.

---

## 7. Secrets in Code

This section has no risk-tier exception and no gate bypass.

1. **Secrets are never committed.** Passwords, API keys, tokens, private keys, connection strings, and any other credential are never written into source code, configuration files in the repository, build scripts, or container images.
2. **Secrets scanning is mandatory.** A secrets scanner runs on every commit and on the full repository history. A detected secret blocks the build.
3. **A detected secret is treated as compromised.** A secret that reaches a repository, even a private one, even briefly, is considered exposed. It is rotated immediately per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md), and the exposure is logged. Removing the commit does not undo the exposure.
4. **Secrets come from a secrets manager at runtime.** Software retrieves credentials at runtime from the secrets management platform governed by [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md). Build-time injection from a secrets manager is acceptable; hard-coding is not.

> **A Secret in Git History Is a Secret in Production**
>
> The most common rationalization is "it was only in a private repo" or "I removed the commit." Neither matters. A secret that touched version control has been copied to every clone, every fork, every backup, and every CI cache that ever pulled the repository. The only safe response is rotation. CERG treats a committed secret as a confirmed exposure, every time.

---

## 8. Dependencies and Software Bill of Materials

1. **Every release carries an SBOM.** A Software Bill of Materials listing every component and its version is generated for every release of Tier 1 and Tier 2 software, and for Tier 3 where the pipeline supports it. The SBOM is retained as a release artifact.
2. **Dependencies are pinned.** Builds resolve dependencies to specific, recorded versions. A build that resolves "latest" is not reproducible and is not permitted for Tier 1 or Tier 2.
3. **Dependencies are monitored after release.** A new vulnerability disclosed against a dependency already in production is a software vulnerability, handled per Section 11. SBOMs make this monitoring possible; that is their operational purpose.
4. **New dependencies are assessed before adoption.** Before a new third-party or open-source dependency is introduced, it is checked for maintenance health, known vulnerabilities, and license compatibility. A dependency with no recent maintenance is a supply chain risk.
5. **Internal components are inventoried too.** Reusable internal libraries are dependencies. They appear in the SBOM and are monitored like any other component.

---

## 9. Pipeline and Build Security

The build pipeline produces trusted software. A compromised pipeline produces compromised software that passes every other gate. The pipeline is therefore protected as a Tier 1 system regardless of what it builds.

1. **Pipeline access is least-privilege and reviewed.** Access to modify pipeline configuration, build steps, or deployment credentials follows [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) and is reviewed on the access-review cadence.
2. **Build steps are defined as code and reviewed.** Pipeline definitions are version-controlled and subject to the code review requirements in Section 5. A change to how software is built is a security-sensitive change.
3. **Builds are isolated.** Build jobs run in ephemeral, isolated environments. A build does not run with standing production credentials.
4. **Build provenance is attested.** Tier 1 and Tier 2 releases carry verifiable provenance: what source commit, what build steps, what environment produced the artifact. This aligns with SLSA build-integrity levels.
5. **Artifacts are integrity-protected.** Released artifacts are signed or hashed so the deployment target can verify it is deploying what the pipeline produced.
6. **Pipeline activity is logged.** Build and deployment events are logged to the platform governed by [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).

---

## 10. Infrastructure as Code

Infrastructure-as-code is software and is governed by this standard. Specifically:

1. IaC is subject to code review (Section 5) and to SAST-equivalent scanning for misconfiguration before apply.
2. IaC must not contain secrets (Section 7).
3. IaC that provisions production infrastructure is Tier 1 or Tier 2 by the same risk-tier logic in Section 3.2.
4. IaC-provisioned configuration must satisfy the secure configuration baselines in [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md). IaC is the preferred mechanism for enforcing those baselines consistently.

---

## 11. Vulnerability Handling for Software

A security finding in CERG-managed software, whether found by SAST, DAST, SCA, code review, adversarial validation, or post-release disclosure, is a vulnerability.

1. **Pre-production findings are engineering inputs.** A finding caught before go-live is remediated before go-live, or the go-live is risk-accepted per [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). This is the pre-production versus post-production distinction from [`CERG-GOV-FRM-001`](../governance/CERG-GOV-FRM-001_CERG_Framework.md) §4.3.
2. **Post-production findings follow the VM procedure.** A finding in released, operating software is a managed vulnerability and is remediated against the SLAs in [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md).
3. **No silent aging.** A software finding is closed or risk-accepted. It is never simply moved down a backlog until it is forgotten. This is Principle 4.

---

## 12. Roles and Responsibilities

Roles below are the canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Secure Development Responsibility** |
|---|---|
| **Application Security Engineer** | Owns this standard. Owns the SAST/DAST/SCA rulesets, threat modeling, the gate definitions, and the software risk-tier decision. Reviews security-sensitive changes. |
| **Engineering Pillar Leader** | Accountable for secure development across the pillar. Owns implementation-phase practice and the operation-and-handoff phase. Resolves risk-tier disputes. |
| **Pre-production Reviewer** | Owns the verification-phase pre-production review and signs go-live readiness for Tier 1 and Tier 2 software. |
| **Cloud Security Engineer** | Owns pipeline and build security where the pipeline runs on cloud infrastructure; owns IaC misconfiguration scanning. |
| **Cryptography Engineer** | Owns the secrets management platform that software retrieves credentials from; supports rotation of exposed secrets. |
| **Exposure Management Lead** | Operates the post-production software vulnerability SLAs per [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md). |
| **Governance Pillar Leader** | Maintains the exceptions register for gate bypasses; tracks audit-facing evidence; cross-references this standard with the control baseline. |
| **Policy & Standards Manager** | Maintains this document, its version, and its review cycle. |

---

## 13. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Standard** |
|---|---|---|
| NIST SSDF 800-218 | PO, PS, PW, RV practice groups | Sections 3, 4, 6, 8, 11 |
| NIST 800-53r5 | SA-11, SA-15, SA-22, SI-2, SI-10, CM-3, CM-4 | Sections 4, 5, 6, 9, 11 |
| NIST 800-171r3 / CMMC L2 | 3.4.x (configuration), 3.13.x (system protection), 3.14.x (system integrity) | Sections 9, 10, 11 |
| NIST 800-161r1 | Software supply chain | Sections 8, 9 |
| OWASP ASVS / SAMM | Verification levels; maturity practices | Sections 4, 6 |
| SLSA | Build provenance and integrity levels | Section 9 |
| SOX ITGC | Change management; segregation of duties | Sections 5, 9 |

---

## 14. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-SDL-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Application Security) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on NIST SSDF revision or material toolchain change |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST SSDF 800-218; NIST 800-53r5 (SA, SI, CM); OWASP ASVS / SAMM; NIST 800-161r1; SLSA |
| **Regulations** | CMMC L2 / 800-171r3; SOX ITGC; NERC-CIP where applicable |
| **Environments** | All CERG-managed software |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-21 | Cyber Engineering | Initial release. Establishes the secure SDLC, software risk tiers, the security gate set, code review requirements, SAST/DAST/SCA testing requirements, the absolute no-secrets-in-code rule, dependency and SBOM requirements, pipeline and build security, infrastructure-as-code coverage, and software vulnerability handling. |

### Review Triggers

- Revision of the NIST Secure Software Development Framework (800-218)
- Material change to the organization's build toolchain or CI/CD platform
- A significant software-related security incident
- Internal audit or regulatory finding affecting software development
- Direction from the CISO

Cyber Engineering owns this document. The Engineering Pillar Leader (Application Security) is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Framework | [`CERG-GOV-FRM-001`](../governance/CERG-GOV-FRM-001_CERG_Framework.md) | Engineering pillar mission and the pre/post-production risk distinction |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Governs the engagement; this standard governs the code |
| Exposure Management Procedure | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Post-production software vulnerability SLAs |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Gate-bypass exceptions |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Secrets management platform; secret rotation |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Pipeline access control |
| Secure Configuration Baseline Standard (DISH) | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Baselines that infrastructure-as-code must satisfy |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Pipeline activity logging |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Purchased software; vendor component risk |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `SDL` domain |
