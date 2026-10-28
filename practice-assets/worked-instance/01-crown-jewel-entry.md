# 1 · Crown Jewel Scenario Record — `ERP-O2C-01` / `SCN-09`

**Record type:** Crown Jewel Scenario Record (CAT-002) · **Owner:** Risk Pillar Leader · **Status:** Approved
**Source:** `CERG-GOV-CJ-001` §3.2 field set, §4 scenario library

This record carries the consequence. It never carries control state, and it never carries service-interface terms — those live on the profiles that follow.

## Register entry

```yaml
asset_id: "ERP-O2C-01"
system_id: "ERP-O2C-01"            # same value in the protected-system SCP; the join key
business_service: "Order-to-cash — freight booking, invoicing, cash application"
owner: "Controller, Harborline Logistics"
executive_sponsor: "Chief Financial Officer"
criticality_tier: "Tier 0"
crown_jewel: true
regulated_scope: "SOX ITGC"
data_classification: "Confidential — financial"
operational_impact: >
  Freight bookings cannot be invoiced and cash application stops. Roughly 40% of monthly
  revenue is invoiced through this system; a 48-hour outage delays billing for the entire
  book rather than a segment of it.
safety_impact: "None"
financial_reporting_impact: >
  In-scope for SOX ITGC. Payment diversion and invoice manipulation are both financial
  statement risks, not only fraud risks — they reach the revenue line.
customer_impact: >
  Customers see incorrect invoices and disputed statements; the top 20 accounts are
  contractually entitled to reconciliation within 5 business days.
internet_exposed: true
third_party_dependencies:
  - "Atlas Managed Security — SOC and detection service"
  - "MAIL-TENANT-01 — corporate mail tenant"
  - "Payment gateway (see EDG-001 entry)"
recovery_time_objective: "24 hours"
recovery_point_objective: "4 hours"
minimum_logging_profile: "See protected-system SCP ERP-O2C-01"
minimum_identity_profile: "See protected-system SCP ERP-O2C-01"
minimum_adversarial_validation_profile: "SCN-09 quarterly; see AV-2026-011"
review_date: "2027-04-01"
```

## Scenario

```yaml
scenario_id: "SCN-09"
scenario: "Business email compromise leading to financial fraud or wire diversion"
chain_breaking_controls:
  - "AC/IA — email authentication enforcement on the payment domain"
  - "AC — dual authorization on payment and bank-detail change"
  - "AU — detection of mailbox rule creation and payment-detail change on finance accounts"
attack_techniques: ["T1566", "T1114", "T1656"]
expected_outcome: >
  Prevent: credential phishing against finance staff does not yield a session.
  Detect: mailbox rule creation and bank-detail change produce an alert within the
  treasury approval window.
  Contain: a payment change cannot complete without out-of-band verification.
  Recover: diverted funds are recoverable through the bank recall window.
obligation_clock: "Payment approval window — 4 business hours from invoice approval to release"
```

## Why the consequence is named this precisely

The claim that follows is only worth reading because this entry says what breaks and against what clock. "Critical system" would have supported a technical claim and nothing more. `SOX ITGC`, the revenue line, and the four-hour approval window are what make the gap in file 6 a decision for the CFO rather than a ticket for the SOC.

## What must not appear here

- Whether email authentication is currently enforced, whether detections are deployed, or any other control-state judgement.
- The operator, the assessor, the assurance rights or the evidence currency rule. Those belong to the service profile and are recorded once, there.
- Any maturity score or control coverage percentage.
