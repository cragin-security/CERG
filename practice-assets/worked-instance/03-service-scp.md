# 3 · Service SCP — `SOC-MSP-01`

**Record type:** System Control Profile (CAT-002) · **Status:** Approved
One profile per operated security service. This is the file that makes the provider relationship answerable, and it is the one most adopters do not have.

```yaml
system_id: "SOC-MSP-01"
name: "24x7 SOC and detection service — Atlas Managed Security"
classification: "Confidential"
system_owner: "Head of Information Security, Harborline Logistics"
technical_owner: "Atlas Managed Security — Service Delivery Manager"
environment: "Hybrid"
regulatory_scope:
  - "SOX"
profile_status: "Approved"
last_profile_review: "2026-09-01"
next_profile_review: "2027-03-01"

# Completed once, because this profile represents an operated security service.
service_interface:
  service_model: "provider"
  first_line_service_owner: "Head of Information Security, Harborline Logistics"
  first_line_operator: "Atlas Managed Security (24x7 SOC: monitoring, detection engineering, alert triage)"
  tool_or_tenant_owner: >
    Harborline owns the SIEM tenant, licences and data; Atlas operates it. Tenant
    ownership is what keeps the evidence retrievable on exit and what makes the
    query rights below real rather than theoretical.
  operational_boundaries: >
    Atlas retains the operating obligations: 24x7 monitoring, detection content
    maintenance, triage to the agreed queue, escalation to Harborline on-call, and
    source health of every onboarded feed. Harborline retains payment authorization,
    remediation execution and acceptance of residual risk. Harborline does not triage,
    does not deploy detection content, and does not administer the platform.
  assurance_method_authority: "CERG-PRC-AV-001 §6 and §10; CERG-STD-LM-001 §7 (detection validation)"
  assurance_rights:
    - "read/query — direct query of the tenant, not report-on-request"
    - "sampling — Harborline selects the sample; Atlas supplies the population"
    - "re-test/replay — re-run detection content against historical telemetry with client-chosen inputs"
    - "closure verification — confirm a tuning or content change is live before a finding closes"
  independent_assessor: "Adversarial Testing Lead, CERG (internal, not Atlas, not Harborline IT)"
  evidence_currency_rule: >
    Threat-event driven per CERG-GOV-CJ-001 §5.6 — a technique class entering the scenario
    chain (KEV addition, tradecraft shift, incident in the blast radius), a material change
    to detection content, source onboarding, identity paths or the crown-jewel population,
    or the annual calendar review, whichever comes first. Material change requires
    re-assertion within 30 days.
  provider_contract_reference: "TPRM-2026-014 — MSA Schedule 4 (Assurance) and Schedule 6 (Exit)"

security_service_references: []
```

## What to notice

**`tool_or_tenant_owner` is the field that makes the rest work.** Harborline owns the tenant and the data; Atlas operates it. Had Atlas owned the tenant, the read/query right would still exist on paper but the evidence would leave with the contract. This single line is the difference between an observable service and documented hope.

**The rights are four specific things, not "audit rights."** Read/query, sampling with the client choosing the sample, re-test/replay with client-chosen inputs, and closure verification. The third one is what makes the finding in this instance possible — and it is also what a SOC 2 report cannot substitute for.

**`independent_assessor` names a role outside both parties.** Not Atlas, because a provider cannot assess its own operated scope. Not Harborline IT, because Harborline IT is the state author for the payment workflow. The pairing of this assessor with the asserted scope in `AV-2026-011` is what carries the independence claim.

**`provider_contract_reference` points at schedules, not a PDF.** Schedule 4 is where the four rights are contractually enforceable; Schedule 6 is exit. A reference to "the MSA" would not survive an exit discussion.

**This profile carries no `business_service`, deliberately.** One SOC serves order-to-cash, payroll and treasury. Naming one business service here would make the SOC the business service and would be wrong for the other two — and consequence belongs on each consumer's register entry.
