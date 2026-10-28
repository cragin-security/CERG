# 2 · Protected-System SCP — `ERP-O2C-01`

**Record type:** System Control Profile (CAT-002) · **Status:** Approved
Local scope only. This profile does not repeat the service interface; it references the service that is expected to cover it, and states what must be covered.

```yaml
system_id: "ERP-O2C-01"
name: "Order-to-Cash ERP"
classification: "SOX-relevant / Confidential — financial"
system_owner: "Controller, Harborline Logistics"
technical_owner: "ERP Platform Lead, IT Operations"
environment: "Cloud"
regulatory_scope:
  - "SOX"
profile_status: "Approved"
last_profile_review: "2026-09-15"
next_profile_review: "2027-09-15"

# The join to the register entry: one stable identifier, no copy of the entry.
crown_jewel_reference:
  asset_id: "ERP-O2C-01"
  scenario_ids: ["SCN-09"]

# Which service is EXPECTED to cover this system. A reference asserts expectation only —
# it does not assert that coverage exists. The service's own evidence and CERG's sampling
# test that claim.
security_service_references:
  - system_id: "SOC-MSP-01"
    covers: ["monitoring", "detection", "alert triage"]
    source_ids_expected:
      - "SRC-MAIL-FLOW"        # mail-flow export, MAIL-TENANT-01
      - "SRC-ERP-AUDIT"        # ERP financial audit trail
      - "SRC-IDP-SIGNIN"       # identity sign-in and MFA events
    required_detections:
      - "DT-SCN09-01 new inbox rule on finance mailbox"
      - "DT-SCN09-02 payment-detail change without dual authorization"
      - "DT-SCN09-03 sign-in from new geography on treasury account"
    asserted_coverage_window: "24x7"

exclusions:
  - statement: "Treasury shared mailbox content is outside CERG's data-handling scope; telemetry only."
    approved_by: "CFO"
    date: "2026-05-02"

controls_applied:
  - control: "CERG-CB-001 AC-04"
    implementation: "Payment release requires two authorizers in ERP-O2C-01."
    evidence: "EIE-2026-011"
    evidence_type: "test result"
    last_validated: "2026-09-28"
    next_review: "2027-09-28"
    owner: "Controller, Harborline Logistics"
    status: "Implemented"
    related_risks: []
    related_exceptions: []
  - control: "CERG-CB-001 AU-02"
    implementation: "ERP audit trail exported to SOC-MSP-01 for monitoring."
    evidence: "EIE-2026-011"
    evidence_type: "export"
    last_validated: "2026-09-28"
    next_review: "2027-03-28"
    owner: "ERP Platform Lead"
    status: "Implemented"
    related_risks: []
    related_exceptions: []
```

## What to notice

**`source_ids_expected` is an expectation written down, not a fact observed.** It is the half of the coverage claim the client owns. Listing `SRC-MAIL-FLOW` here does not mean mail flow is onboarded for the systems that matter — it means "this is what we are paying for." Comparing this list against the service's actual source inventory is the cheapest check a second line can run, and it is the check that produced the finding in this instance.

**The exclusion is recorded, not silently applied.** Treasury mailbox content is out of CERG's data-handling scope by CFO decision. That is a legitimate exclusion — and it is also where the blindness starts, which is why it is written, dated and approved rather than assumed.

**No `service_interface` block here.** Operator, rights, assessor and currency rule are recorded once on `SOC-MSP-01`. Repeating them per protected system is how 500 profiles come to disagree about the same operator.
