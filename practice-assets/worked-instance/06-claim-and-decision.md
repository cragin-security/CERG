# 6 · The Claim, and the Two Decisions It Can Produce

## The bounded defense claim

> **Against the SOX ITGC obligation carried by Order-to-cash, and inside the four-hour payment approval window, Harborline is not fully defensible against `SCN-09` for the period 2026-06-01 to 2026-09-30.**
>
> Email authentication held under direct challenge. Detection is a separate and curable gap. The load-bearing link failed: independent out-of-band verification on beneficiary change is circular — the callback authenticates the request against a phone number the requester can change through the vendor portal without Harborline approval. The control reads as implemented in every record that describes it, because every record accurately describes a callback to the number on file.

The six elements, mapped:

| Element | This instance |
|---|---|
| Business service and obligation at stake | Order-to-cash / SOX ITGC, revenue line, four-hour approval window — referenced from `CJ-2026-ERP-O2C-01-SCN-09` |
| Scenario and expected outcome | `SCN-09`; prevent delivery, detect inside the approval window, contain before release |
| Chain-link state walk | L2 failed (chain-breaking); L1 held; L3 failed, not chain-breaking |
| Independent challenge | `AV-2026-011`, assessor independent of Atlas and of Harborline IT for the asserted scope |
| Decision | Not filed — put to the CFO as a question. See Path A |
| Retest trigger | Threat event per `CJ-001` §5.6; remediation retest per `PRC-AV-001` §10.3 |

## The question the CFO actually receives

> **The beneficiary-change control can be defeated without an insider, and our detection would not have caught it. Do we fund the portal change-control fix now — vendor approval required, callback to a number verified under a different authority — or accept the exposure through the next payment cycle?**

Two things make that a decision rather than a report. It is bounded to a scope and a period. And it is answerable in one meeting.

## Path A — consequential: the full chain

```text
FIND-2026-031  circular verification on beneficiary change       Critical
  -> RISK-2026-031  created or updated per PRC-RM-001            SOX ITGC + financial statement risk
     -> Risk Acceptance Record per RMF-001 §9.7 (TMPL-RM-004)    attaches to RISK-2026-031
ODR-2026-Q4  fund treatment | assign action | route an acceptance request
             — the ODR routes; it never accepts
```

**The acceptance has a subject.** It attaches to `RISK-2026-031`, not to the claim, not to the meeting, and not to the ODR. An acceptance that floats as a minute entry is the failure this chain exists to prevent.

**The remediation clock is separate from the claim clock.** `PRC-AV-001` §10.3 requires the Critical finding to be retested within 30 days of a remediation claim, and the finding closes only when the retest demonstrates the fix. That does not re-open or refresh the scenario claim — the claim re-opens on the threat event or a material change.

### The compensating control that is not available

The obvious holding position is *"we will monitor the payment path closely until the fix lands."* It cannot be used as a compensated disposition, and the reason is the second finding: a compensating control may only support a compensated-exposure decision when its effectiveness evidence is current (`PRC-VM-001` §7.1), and the monitoring that would serve as the compensation is the monitoring that cannot fire on the treasury path.

That is not a coincidence of this instance — it is the general shape. The control you reach for as compensation is often the one the same test has just shown to be hollow, which is why the compensated-disposition evidence requirement is written as *current* evidence rather than *described* evidence.

### The provider finding, routed differently

```text
FIND-2026-032  connector scope excludes shared mailboxes           High
  -> remediation obligation under TPRM-2026-014 Schedule 4         Atlas owns the fix
  -> CERG re-test within 60 days per PRC-AV-001 §10.3              CERG verifies; Atlas does not attest
```

Atlas may produce the corrected configuration and the evidence that the scope now includes the mailbox. Atlas may not close this finding. That is the same rule as the assessment itself, applied to remediation: the party that changed the state does not certify the state.

## Path B — capped: the same service, an unregistered system

`PAYROLL-SAAS-01` is monitored by the same `SOC-MSP-01` and its profile already carries `security_service_references: [SOC-MSP-01]`. Payroll is material to the business. It has **no crown-jewel entry** — the asset was never put through register classification.

The same replay shows the same connector scoping: payroll mailbox detections cannot fire either. The finding is real, testable, and worth fixing.

What changes is only what can be asserted:

```text
claim scope        = the technical service (SOC-MSP-01), not a business service
disposition        = recorded on the Finding Record with decision, date, closure rationale
                     (or the Exposure Backlog Item where PRC-VM-001 governs)
ODR                = not used — there is no consequential claim to route
Risk Acceptance    = unavailable — there is no named consequence to accept
```

**What still happens:** the test ran, the gap is written down, the provider still has to fix it, and the retest still applies.

**What does not happen:** Harborline cannot tell the CFO, the auditor, or a customer what this gap costs, because it has not said which business service depends on the capability and against which obligation. That is the entire cost of the missing join — and it is a cost paid in the assertion, not in a data-cleanup project.

The distance between Path A and Path B is one register entry. Not a BIA. Not a CMDB programme. One entry, with a business service name and an obligation.

## What the two paths together demonstrate

1. **The model produces findings the operator could not have produced.** Circular verification is invisible to both records that describe it; the connector-scope gap is invisible to the metric that reports on it.
2. **It distinguishes severity structurally rather than by rating.** The chain-breaking link downgrades the claim; the non-chain-breaking link does not, and both get fixed on their own clocks.
3. **It caps without blocking.** The unregistered system is still tested and still remediated. Only the assertion is limited.
4. **It cannot be satisfied by paperwork.** Two links held on direct challenge; one failed for a reason no document recorded. A programme that only read the documents would have concluded the path was defended.
