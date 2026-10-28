# 5 · Evidence Index Entry — `EIE-2026-011`

**Record type:** Evidence Index Entry (CAT-002) · **Owner:** Evidence Librarian
**Attributes:** inherited from `CERG-GOV-AUD-001` — attributable, current, retrievable

This record **references**. It is attached to the Crown Jewel Scenario Record for `ERP-O2C-01` / `SCN-09` and copies no consequence fields. If this file were lost, the consequence would still be recoverable from the register entry and the evidence from the sources below. That is the test of an index.

```yaml
evidence_index_id: "EIE-2026-011"
attached_to: "CJ-2026-ERP-O2C-01-SCN-09"     # the Crown Jewel Scenario Record
scenario: "SCN-09"
evidence_period: "2026-06-01 to 2026-09-30"
assembled: "2026-10-06"
assembled_by: "Evidence Librarian"
claim_state: "bounded — not fully defensible for the asserted scope and period"
```

## References

| Reference | Record | Contributes |
|---|---|---|
| `CJ-2026-ERP-O2C-01-SCN-09` | Crown Jewel Scenario Record | Business service, SOX scope, consequence dimensions, owner, sponsor, scenario, expected outcome against the four-hour clock |
| `SCP-ERP-O2C-01` | System Control Profile (protected) | Local scope, expected source IDs, required detections, the treasury-mailbox exclusion |
| `SCP-SOC-MSP-01` | System Control Profile (service) | Operator, tenant ownership, the four assurance rights, method authority, independent assessor, currency rule, contract schedules |
| `AV-2026-011` | Adversarial Validation Record | Asserted scope, load-bearing classification, techniques, assessor, method, evidence period, exclusions, independence |
| `TPRM-2026-014-S4` | Contract schedule | The enforceable assurance rights and the exit schedule |

## Per-link state walk

| Link | Chain-breaking | State | Evidence date |
|---|---|---|---|
| L2 Independent out-of-band verification | **Yes** | **Not effective — circular; verifies against requester-controlled data** | 2026-09-25 |
| L1 DMARC enforcement | No | Effective | 2026-09-24 |
| L3 Detection on the treasury path | No | **Not effective for the asserted scope — deployed, cannot fire** | 2026-09-28 |

## Challenge evidence

- Two live vendor-portal beneficiary-change sessions, read-only, to establish that the number on file is updatable without Harborline approval.
- Payment release test with two authorizers; Controller walkthrough of the callback procedure.
- Replay of 90 days of tenant telemetry against `DT-SCN09-01`, `-02`, `-03`; sample selected by CERG, population supplied by Atlas.
- Connector scope configuration for `SRC-MAIL-FLOW`, retrieved under the read/query right.
- Phishing simulation results against `ap@` and `treasury@` (L1).

## Two findings, two owners, two clocks

| Finding | Owner | Route |
|---|---|---|
| `FIND-2026-031` — circular verification on beneficiary change (Critical) | Harborline — Controller and IT | Risk register, then acceptance or treatment via ODR |
| `FIND-2026-032` — connector scope excludes shared mailboxes (High) | Atlas — provider remediation | Contract Schedule 4 correction; verified by CERG re-test, not by provider attestation |

## Retest triggers recorded with the claim

Threat event, not calendar: a technique class entering the chain (KEV addition on T1566 or T1114, tradecraft shift), a material change to detection content, connector scope, identity paths or the crown-jewel population, or the annual review — whichever arrives first.

Two separate clocks, which must not be confused:

- **Remediation retest** — `PRC-AV-001` §10.3: Critical findings retested within 30 days of a remediation claim, High within 60; the finding closes only when the retest demonstrates remediation.
- **Claim retest** — `CJ-001` §5.6: re-walk and re-challenge when the threat event or a material change arrives. A closed finding does not make the claim current on its own.

## What this entry does not contain

No consequence fields, no risk rating, no decision, no acceptance. The decision lives in the ODR; the acceptance, if taken, attaches to `RISK-2026-031`. An index entry that starts carrying conclusions stops being an index and becomes a parallel record that will drift from the register.
