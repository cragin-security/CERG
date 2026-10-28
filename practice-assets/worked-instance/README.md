# Worked Instance: One Bounded Defense Claim, End to End

Six filled records and one decision. This is not a story about how the model works — it is what the model looks like when someone actually fills in the templates for one service and runs one challenge.

**Who this is for:** MSP and MSSP adopters, and the internal security leads who hold them accountable. If you are the person who has to answer "our provider says we're covered — are we?" this shows the paper trail that replaces the assurance report.

**Everything here is fictional.** Harborline Logistics, Atlas Managed Security, all identifiers and dates. Scenario `SCN-09` and every record type are real corpus artifacts; the values are invented so you can copy the shape.

---

## The situation

| | |
|---|---|
| **Adopter** | Harborline Logistics — mid-market freight forwarder, 1,150 staff, exchange-listed so SOX ITGC applies |
| **Business service** | Order-to-cash: freight booking → invoicing → cash application |
| **Security service** | `SOC-MSP-01` — 24x7 SOC run by Atlas Managed Security under a client-owned SIEM tenant |
| **Scenario** | `SCN-09` — business email compromise leading to financial fraud or wire diversion |
| **The question** | If an attacker takes over a finance mailbox, can they redirect a payment, and would we catch it before the money moves? |

## The records, in the order they are assembled

| # | File | Record | What it contributes |
|---|---|---|---|
| 1 | [`01-crown-jewel-entry.md`](01-crown-jewel-entry.md) | Crown Jewel Scenario Record (`ERP-O2C-01`) | Business service, SOX scope, consequence dimensions, owner, sponsor, scenario, expected outcome |
| 2 | [`02-protected-system-scp.md`](02-protected-system-scp.md) | System Control Profile — protected system | Local scope, source IDs, required detections, and a reference to the service that is expected to cover it |
| 3 | [`03-service-scp.md`](03-service-scp.md) | System Control Profile — service | Who operates, who owns the tenant, assurance rights, method authority, independent assessor, currency rule, contract reference |
| 4 | [`04-av-record.md`](04-av-record.md) | Rules of Engagement + Adversarial Validation Record (`AV-2026-011`) | Asserted scope, load-bearing links, techniques, assessor, method, evidence period, exclusions, independence |
| 5 | [`05-evidence-index-entry.md`](05-evidence-index-entry.md) | Evidence Index Entry (`EIE-2026-011`) | References the four records above plus the per-link outcome; copies no consequence fields |
| 6 | [`06-claim-and-decision.md`](06-claim-and-decision.md) | The claim, Path A, and Path B | The decision question, the consequential route, and the capped route for an unregistered system |

## What this instance is built to prove

The test applied to the result is one sentence: **did CERG produce a finding the operator could not have produced?** It produced two.

**The chain-break.** The beneficiary-change control reads as implemented in every document that describes it — because every document accurately describes *a callback to the number on file*. The number on file is editable by the vendor through the portal, without Harborline approval. So the callback authenticates a request against data the requester controls. The control is circular, and circularity is invisible to a record that states it correctly.

**The blind spot.** Atlas reports 100% deployment of the `SCN-09` detection set against onboarded sources. Both halves are true, and the treasury shared mailbox is scoped out of the mail-flow export, so the detections that matter cannot fire on the path that matters. The operator measures what it deployed; it cannot measure its own scoping decision, because that decision is its own. CERG can, because it draws its own sample under the assurance rights instead of reading the provider's summary.

The second finding also removes the obvious holding position: the compensation you would reach for — "monitor the payment path until the fix lands" — is the monitoring that cannot fire, so it cannot support a compensated disposition. That is why the model requires *current* effectiveness evidence rather than described evidence.

Everything else in this instance follows from those two gaps.

## What is deliberately absent

No CMDB project, no BIA, no maturity gate, no source register, no new record type, and no score. The missing join in Path B caps a claim rather than triggering a data-quality programme. If your organization cannot name a business service, you lose the ability to assert a business outcome — you do not lose the ability to test.

## Adapting it

Replace the identifiers and the values, keep the structure. The two files that do most of the work are `03-service-scp.yaml` — because that is where rights, assessor and currency are recorded once per service — and `06-claim-and-decision.md`, because that is where a claim either routes a decision or stops at a technical scope.
