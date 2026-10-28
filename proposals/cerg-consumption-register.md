# CERG Consumption Register

### What CERG must receive to make a claim, and from whom

| | |
|---|---|
| **Proposal reference** | FLA-PROPOSAL-003 |
| **Status** | Proposed — not approved framework content |
| **Owner** | cragin-security |
| **Date** | 2026-10-27 |
| **Classification** | Public |
| **Source state** | Depends on `experiment/second-line-model-implementation` at `7a74768` — not present in this fork's `main` |
| **Companion documents** | [Frontline Security Assurance Operating Model](frontline-security-assurance-operating-model.md) · [Data-and-Assurance Contract](frontline-security-data-and-assurance-contract.md) |

> **Purpose.** Most boundary arguments are really disagreements about inputs. This register lists what CERG consumes, from which role or service, in what form, at what cadence, and which claim it supports. If both sides agree on the inputs, the "who operates" question usually answers itself.

> **Source state.** Written against the second-line experiment rather than against this
> repository's corpus. The conditions, the state-authorship rule, the owner/operator split,
> the `PRC-VM-001` §4.1 re-owning and the `TMPL-SCP-001` service interface block live on
> `experiment/second-line-model-implementation` at `7a74768` and are **not** in this fork's `main`. A reader here will therefore find a
> proposal describing a model the local corpus does not yet implement. That is expected and
> is why this document is non-normative. Re-verify cross-references if the experiment merges.

## How to read this

Three things are fused in the current corpus and need separating before any conflict can be resolved:

| Layer | Question | Owner |
|---|---|---|
| **Operation** | Who runs the source and keeps it producing? | First line, internal or contracted |
| **Custody and health** | Who keeps the data complete, current, and retrievable? | First line — the operating party |
| **Consumption** | Who reads it to make an assurance claim? | CERG |

The fusion is visible in two places:

- `PRC-VM-001` §4.1 lists twelve observation sources and names **Risk** as owner or co-owner of all twelve — nine as sole owner. Read as an operation table, that says CERG runs scanners, CSPM, SSPM, and OT passive monitoring. Read as a consumption table, it says CERG owns the *claims* those sources support. The corpus never says which.
- `MTR-001` §4 mixes CERG pillar roles (Exposure Management Lead, Cyber Risk – Detection, Adversarial Testing Lead) with operational titles such as "IAM Operator" in a single **Owning Role** column, for systems of record that first line operates — the exposure pipeline, the SIEM source inventory, the detection registry.

Splitting the columns is a smaller change than moving any responsibility.

## Register — by supplier

Form abbreviations: **R** = raw read/query access · **E** = export or report · **A** = attestation · **T** = test or sample.

### First-line security operations (SOC / provider)

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 1 | Raw telemetry access, not dashboards | R | Continuous | Detection effectiveness (condition 2 capability) | `MTR-001` §4 DT-003; `STD-LM-001` |
| 2 | Source inventory and health, including failed connectors | E | Daily | Coverage claims; red/amber source state | `MTR-001` §4 DT-001/003 |
| 3 | Detection registry: what is deployed, where | E | On change + nightly | Coverage vs requirement | `MTR-001` §4 DT-001 |
| 4 | Alert dispositions, closed-case sample | T | Quarterly | Operating evidence of triage | `service_interface.assurance_rights[]` — sampling |
| 5 | Escalation timeliness against agreed clocks | E | Monthly | Service performance | `PRC-TPRM-001` §9 |
| 6 | Tuning backlog and change records | E | Per change | Retest trigger after validation | *unspecified* |

### Exposure and vulnerability operations

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 7 | Observation output with source provenance | E | Per cycle | Exposure classification | `PRC-VM-001` §4.1 |
| 8 | Coverage statement: what was in scope, what was excluded, why | A | Per cycle | Non-blindness claim | *partially — §4.1 lists sources, not exclusions* |
| 9 | Scanner/tool configuration as deployed | E | On change | Implementation evidence | *unspecified* |
| 10 | Remediation completion with verification artifact | T | Per closure | Closure, not ticket closure | *unspecified* |
| 11 | Independent re-scan or query rights | T | On demand | Effectiveness, not report acceptance | `service_interface.assurance_rights[]` — re-test |

### Identity operations

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 12 | IdP / PAM audit logs, direct query | R | Continuous | Identity control effectiveness | `MTR-001` §4 ID-001–010 |
| 13 | Recertification and joiner-mover-leaver evidence | E | Quarterly | Access review completion | `MTR-001` §4; `PRC-AC-002` |
| 14 | Non-human identity inventory | E | Monthly | NHI exposure population | `MTR-001` §4 (NHI registry) |

### Resilience and backup operations

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 15 | Backup job history and failure logs | E | Nightly | Backup coverage | `MTR-001` §4 CM-001–005 |
| 16 | Scheduled restore-test results | E | Per test | Recovery capability | `STD-RES-001` |
| 17 | Adversarial restore execution window and outcome | T | Per exercise | Recoverability under attack, not schedule | `service_interface.assurance_rights[]` — re-test, with the AVR |
| 18 | Immutability and retention configuration | E | On change | Ransomware-recovery precondition | *unspecified* |

### Incident response and forensics

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 19 | Operational incident record and case intel | E | Per incident | Detection and response effectiveness | `OM-001` §8 IR interface; `PLN-IR-001` |
| 20 | Post-incident findings and near misses | E | Per incident | Improvement and exposure inputs | `PRC-LL-001` |
| 21 | Evidence-quality confirmation at collection time | A | Per incident | Assurability of the record | `AUD-001` (currency, retrieval) |

### OT operations

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 22 | Passive monitoring output and blind spots | E | Continuous | OT coverage claim | `STD-OT-001` |
| 23 | Safety, reliability, and maintenance-window constraints | A | Per change | Feasibility of treatment | `PRC-VM-001`; `STD-OT-001` |
| 24 | ESP / EAP architecture facts | E | On change | Segmentation validation | `STD-OT-001`; `STD-NET-001` |

### Architecture and platform teams

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 25 | Reference designs and supported patterns | E | On change | Feasibility and compensating-control viability | `OM-001` §8; `PRC-AR-001` |
| 26 | Integration and data-flow facts for review gates | E | Per project | Architecture risk determination | `FLOW-001` F-02 |
| 27 | Platform limits and integration capacity | A | Per request | Whether a control is achievable | *unspecified* |

### System, service, and business owners

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 28 | Criticality and crown-jewel designation | A | On change | Risk tiering and scope | `CJ-001`; `FLOW-001` F-03 |
| 29 | Residual-risk acceptance decisions | A | Per decision | Whether a gap is owned | `RMF-001` §9.7 (authority) |
| 30 | Treatment funding and priority decisions | A | Per decision | Feasibility vs. risk trade | `RMF-001` |

### Third line and external

| # | CERG consumes | Form | Cadence | Claim it supports | Corpus home |
|---|---|---|---|---|---|
| 31 | Internal audit findings | E | Per audit | Assurance of CERG's own claims | `OM-001` §8 |
| 32 | External assessor and regulator findings | E | Per assessment | Conformance boundary | `OM-001` §8 |

## The reverse view — every claim needs a supplier

| CERG claim | Inputs required | Fails without |
|---|---|---|
| "Detection covers the priority attack paths" | 1, 2, 3, 6 + threat prioritization | Raw telemetry access (capability) |
| "Exposures are classified and treated" | 7, 8, 10, 11 | Provenance and a closure artifact (currency) |
| "Identity controls operate as designed" | 12, 13, 14 | Direct log query (capability) |
| "Recovery is demonstrable" | 15, 16, 17, 18 | Adversarial restore, not scheduled (currency) |
| "Incidents are detected and handled" | 19, 20, 21 | Pre-agreed evidence quality (currency) |
| "OT is covered and safe to test" | 22, 23, 24 | Safety authority and stop rights (independence) |
| "Architecture risk is controlled" | 25, 26, 27 | Design facts at review time (capability) |
| "Residual risk is owned" | 28, 29, 30 | A named decision-maker (independence) |

## Where the corpus needs work — status as at the experiment merge

1. **`PRC-VM-001` §4.1** — *addressed upstream.* PR #225 re-owned the seven operational source rows to first line, keeping validation, classification and SLA measurement with Risk. The split this register asked for is now expressed as row ownership rather than a split column; either form resolves the ambiguity, and the row-ownership form is stronger because it cannot be read as a consumption table.
2. **`MTR-001` §4** — *open.* Split **Owning Role** into *system-of-record custodian* and *metric owner*. The failure-mode column is already right; it just does not say who owns the failure.
3. **`OM-001` §8** — *open.* Add the operational service interfaces: SOC or provider, exposure operations, identity operations, resilience operations. Seventeen organizational interfaces, none of these.
4. **Service interface fields** — *partly addressed upstream.* The `TMPL-SCP-001` `service_interface:` block and schema now carry the interface once per service. What remains open is the contract side: `PRC-TPRM-001` §9 still describes only technology providers, and the assurance-rights clauses do not exist yet.

## What to ask each stakeholder

| Supplier | Questions |
|---|---|
| SOC / MSSP operator | Can you give raw telemetry access, or only dashboards? What is your alert-disposition export, and how far back? How do you report source health and blind spots? |
| Exposure operations | Who signs the coverage and exclusion statement, and what makes it true? Can CERG re-scan a sample independently? What artifact proves a finding was fixed rather than closed? |
| Identity operations | What is the direct query path to IdP and PAM logs? How is NHI inventory produced? Who attests recertification? |
| Resilience operations | Which restores are scheduled and which are adversarial? Who authorizes an adversarial restore, and who can stop it? |
| IR team | What in the incident record is assurable, and when is evidence quality confirmed — at collection or after? |
| OT operations | Who holds stop authority in a test? What constitutes a blind spot you already know about? |
| Architecture / platform | Which controls are not achievable on current platforms, and what is the supported alternative? |
| Business and system owners | Who accepts residual risk when a supplier cannot meet the input requirement? |

## Relationship to the boundary RFC

This register supplies the inputs the boundary RFC's conditions depend on. Independence, service-appropriate capability, and evidence currency are properties of a claim; each one is satisfied or lost at a specific row above. It introduces no CERG role, record type, or control — every row either cites an existing home or is marked unspecified.
