# 4 · Rules of Engagement and Adversarial Validation Record — `AV-2026-011`

**Record type:** Adversarial Validation Record (CAT-002) · **Owner:** Adversarial Testing Lead
**Procedure:** `CERG-PRC-AV-001` (v1.5) · **Engagement type:** §2 type 1 (purple team) with §6.4 evidence sampling

## Rules of Engagement — signed before any activity

```yaml
engagement: "AV-2026-011"
scenario: "(commissioned against SCN-09 — business email compromise leading to financial fraud
           or wire diversion. Asserted protected-system scope: ERP-O2C-01 payment path, the
           treasury shared mailbox, and the vendor maintenance portal.)"
objectives: >
  Determine whether a finance mailbox takeover can produce a released payment to an
  attacker-controlled beneficiary without detection inside the four-hour approval window.
asserted_scope:
  in_scope:
    - "MAIL-TENANT-01 — treasury@ and ap@ shared mailboxes"
    - "ERP-O2C-01 — payment release and bank-detail change workflow"
    - "Vendor maintenance portal — beneficiary record updates by vendors"
    - "SOC-MSP-01 — detection coverage for the three SCN-09 detections"
  out_scope:
    - "Treasury mailbox content beyond header and detection telemetry (CFO exclusion, 2026-05-02)"
    - "Bank-side beneficiary verification and recall"
techniques: ["T1566.002", "T1114.003", "T1656"]
load_bearing_links:
  - id: "L2"
    link: "Independent out-of-band verification on beneficiary change and payment release"
    chain_breaking: true
    why: >
      Absence of an independent verification channel allows the diversion to complete on
      its own. The other links reduce likelihood; this one is the break.
  - id: "L1"
    link: "DMARC enforcement on the payment domain"
    chain_breaking: false
    why: "Reduces delivery likelihood. Scenario still requires the payment path to succeed."
  - id: "L3"
    link: "Detection of inbox-rule creation and beneficiary change on finance accounts"
    chain_breaking: false
    why: >
      Removes the catch and the recall window. Does not by itself allow the diversion —
      the payment control must still be defeated.
assessor: "Adversarial Testing Lead, CERG"
method: >
  Phishing simulation against ap@ and treasury@; beneficiary-change walkthrough with the
  Controller and two live vendor-portal sessions; payment release test with two authorizers;
  detection validation by replaying 90 days of tenant telemetry against the three required
  detections.
evidence_period: "2026-06-01 to 2026-09-30"
independence: >
  Assessor is independent of Atlas Managed Security (the operator) and of Harborline IT (the
  state author for the payment workflow) for the asserted scope. The assessor named on the
  SOC-MSP-01 service profile is a separate assignment and does not carry to this claim.
safety_constraints: "No live payment released. No real beneficiary account altered. Portal sessions read-only."
```

## Results by link

| Link | Chain-breaking | Outcome | Evidence |
|---|---|---|---|
| **L2** Independent out-of-band verification | **Yes** | **Failed** | Two portal sessions + walkthrough, 2026-09-25 |
| **L1** DMARC enforcement | No | Held — `p=reject`; spoofed sender rejected at gateway before delivery | Mail policy export, 2026-09-24 |
| **L3** Detection on the finance path | No | **Failed** — deployed, cannot fire on the treasury path | Replay, 2026-09-28 |

## Finding 1 — the verification channel is circular

The Controller's full statement of the control is: *the callback goes to the vendor's number on file.* Two things follow, and only the second is visible to anyone reading the procedure:

1. The number on file is a control parameter, which is correct design.
2. **The vendor can change the number on file through the maintenance portal, and that change requires no Harborline approval.** So the callback verifies the request against data the requester controls. An attacker who takes over a vendor account updates the number, requests the beneficiary change, and receives their own callback.

The control is not absent. It is circular — it authenticates a request against the requester's own data — and a circular control reads as implemented in every document that describes it, because the document says "out-of-band verification to the number on file" and that is exactly what happens.

Nothing in the vendor portal, the ERP approval workflow, or the procedure document records the missing half: that the number must be changed under a different authority than the one that requests the payment. That is the finding, and neither the operator nor the control owner could have produced it from their own records — both records are individually accurate.

## Finding 2 — the detection gap behind a green coverage number

Atlas reports 100% deployment of the `SCN-09` detection set against **onboarded sources**. Both halves are true. The mail-flow export (`SRC-MAIL-FLOW`) is built from a tenant connector scope that **excludes shared mailboxes**, and `treasury@` is a shared mailbox. So `DT-SCN09-01` has no inbox-rule events to evaluate on the mailbox that matters, while `DT-SCN09-03` genuinely fires — sign-in events are in scope. The dashboard is green and one third of it is real.

Established by replay, not interview: 90 days of tenant telemetry against the three required detections, with **CERG selecting the sample** and Atlas supplying the population and connector configuration.

This is the operator-impossible finding. Atlas measures what it deployed against what it onboarded. The connector scope is Atlas's own administrative decision, and no provider metric is designed to audit its own scope choices.

## Why the load-bearing classification matters

Two links failed and only one of them downgrades the claim. Had the detection gap been the load-bearing link, this would have been a claim about monitoring, and the fix would have been a ticket. Because the verification channel is chain-breaking and the detection gap is not, the claim says something narrower and more useful: *the payment control itself is defeatable without an insider, detection would not have caught it, and both facts are curable by different owners at different costs.*

A rule that treated every failure as load-bearing would have hidden that distinction.
