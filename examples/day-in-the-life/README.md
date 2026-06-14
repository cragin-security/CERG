# CERG Example: Day in the Life Operational Stories

These examples show how CERG flows, roles, records, and evidence come together during normal operations. They are not new requirements. They are narrative walkthroughs that help a reader see how existing CERG artifacts are used in real work.

Use these examples after reading the [Cross-Pillar Operational Flows](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md), [Operating Model](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md), and [Consolidated Roles and RACI Instrument](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md).

---

## Story 1: New SaaS application

### Situation

A business team wants to adopt a customer success SaaS platform. The tool will process customer contact data, integrate with the identity provider, and export activity logs to the enterprise SIEM. The business wants go-live in six weeks.

### CERG flow pattern

Primary flow: [F-02 Project Intake, Architecture Review, and Threat Modeling](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#9-flow-f-02--project-intake-architecture-review-and-threat-modeling)

Supporting procedures and standards:

- [Architecture Review and Project Intake Procedure](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)
- [Third Party and Supply Chain Risk Procedure](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)
- [Data Governance and Classification Standard](../../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md)
- [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md)
- [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
- [Evidence Quality Standard](../../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md)

### Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | The Business Owner submits a project intake for the new SaaS vendor. | Business Owner | Project Intake Record |
| 2 | Governance confirms required intake fields, expected go-live date, business owner, data types, and regulatory scope. | Governance Pillar | Intake completeness check |
| 3 | Engineering applies the tiering model. Because the service is internet-facing SaaS with identity integration and customer data, it is not routed as a low-risk known pattern. | Engineering Pillar | Architecture Review Record |
| 4 | Risk initiates vendor risk assessment and requests security documentation, subprocessors, breach history, data residency, and contract security terms. | Risk Pillar | Vendor assessment file |
| 5 | Data classification is confirmed. The project is tagged for customer data handling requirements and retention expectations. | Governance Pillar | Data classification decision |
| 6 | Access requirements are defined: SSO required, MFA inherited from the IdP, role-based access, least privilege groups, named admin accounts, and periodic access review scope. | Engineering Pillar | Access design evidence |
| 7 | Logging requirements are applied: administrative activity, authentication events, privilege changes, export events, and integration failures must be available for monitoring. | Engineering Pillar | Logging requirement checklist |
| 8 | Open risks are dispositioned. A missing vendor feature becomes either a remediation before go-live, a time-bound exception, or a risk acceptance package. | Risk Pillar | Risk Record or Exception Record |
| 9 | Evidence is stored with the intake package: review notes, vendor questionnaire, contract clauses, data classification, access design, logging validation, and final disposition. | Evidence Librarian | Evidence index entries |
| 10 | Metrics update after closure: intake cycle time, reviews by tier, vendor risk completion, exceptions opened, and pre-go-live issues remediated. | Governance Pillar | Reporting Metric Record |

### Example day-in-the-life narrative

On Monday morning, the business sponsor opens the intake record and identifies the system owner, target go-live date, expected users, data elements, and vendor contact. Governance reviews the intake the same day and sends one clarification: the initial request says "customer data" but does not identify whether regulated data is included.

By Wednesday, Engineering completes the architecture review. The design uses SSO, two privileged admin groups, SCIM provisioning, and a vendor-hosted API. Engineering confirms that the application cannot go live unless admin activity and user authentication logs are exportable. Risk starts the third-party assessment in parallel instead of waiting for architecture review closure.

The vendor returns a SOC report, penetration test summary, subprocessors list, and data processing addendum. Risk identifies one gap: customer data exports are logged in the vendor console but are not available through the standard log API. The Business Owner agrees that exports will be limited to two approved roles until the vendor API feature is available.

At the go-live decision meeting, Engineering confirms SSO, access groups, and log ingestion for authentication and admin events. Risk documents the export-log limitation as a time-bound exception with compensating controls. Governance verifies that evidence is indexed and that the exception expiration date is on the calendar.

### Operational outputs

- Project Intake Record closed with security disposition.
- Architecture Review Record approved with conditions.
- Vendor assessment completed and linked.
- Data classification decision recorded.
- Access model and logging evidence stored.
- Exception Record created if a requirement is deferred.
- Metrics updated for intake throughput, cycle time, and exception volume.

---

## Story 2: Critical vulnerability

### Situation

A vulnerability scanner reports a critical remote-code-execution exposure on an internet-facing application server. Threat intelligence indicates public exploit code is available. The affected application supports a customer portal.

### CERG flow pattern

Primary flow: [F-04 Finding to Remediation, Exception, or Residual Risk](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#11-flow-f-04-finding--remediation-exception-or-residual-risk)

Supporting procedures and standards:

- [Vulnerability Management Procedure](../../procedures/CERG-PRC-VM-001_Vulnerability_Management_Procedure.md)
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
- [Security Change Management Procedure](../../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md)
- [Lessons Learned and Program Improvement Procedure](../../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md)
- [Metrics Dashboard and Reporting](../../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md)

### Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Scanner creates a critical finding for an internet-facing server. | Risk Pillar | Finding Record |
| 2 | Risk validates reachability, asset ownership, exploitability, compensating controls, and whether active exploitation indicators exist. | Risk Pillar | Triage notes and severity decision |
| 3 | Engineering owns remediation planning and coordinates patching, configuration change, WAF rule, or service isolation. | Engineering Pillar | Change Record |
| 4 | Governance checks the applicable SLA, evidence expectations, and whether required records are complete. | Governance Pillar | SLA and evidence review |
| 5 | If remediation will miss SLA, the Technical Owner submits an exception request with rationale, compensating controls, and expiration date. | Technical Owner | Exception Record |
| 6 | If residual risk is material, the Business Owner and CISO review the risk package and approve, reject, or require further treatment. | Business Owner and CISO | Risk acceptance memo |
| 7 | Metrics update for critical findings, SLA performance, exceptions, reopen rate, and time to validate remediation. | Governance Pillar | Reporting Metric Record |
| 8 | Lessons learned determine whether standards, baselines, scanning coverage, or patch windows need updates. | Risk Pillar | Improvement Record |

### Example day-in-the-life narrative

At 8:15 a.m., the scanner imports a critical finding and automatically maps it to the customer portal asset record. Risk confirms the server is internet-facing and that exploit code is available. Because public exploitation is plausible, the finding remains Critical and receives the critical SLA.

By 9:00 a.m., Engineering owns the remediation bridge. The application team reports that the vendor patch requires a minor version upgrade and a brief outage. The Business Owner approves an emergency maintenance window at noon. Engineering also applies a temporary WAF rule while preparing the patch.

Governance does not run the patch. Governance confirms the SLA clock, expected evidence, and required linkage between the Finding Record and Change Record. Risk monitors for indicators of compromise and confirms that no incident declaration is required based on current evidence.

At 12:30 p.m., Engineering completes the emergency change and uploads patch output, service validation, and rollback-not-used confirmation. Risk rescans the asset and validates closure. Governance records that the critical SLA was met and the dashboard updates that evening.

During lessons learned, the team discovers that this application missed a monthly dependency owner review. The action is not just "patch faster." The program improvement is to update the secure configuration baseline and require explicit owner validation for internet-facing dependencies.

### Operational outputs

- Finding Record created, triaged, and closed or promoted.
- Change Record linked to remediation evidence.
- Exception or Risk Record created only if remediation misses SLA or residual risk remains.
- CISO or Business Owner acceptance captured when required.
- Metrics updated for critical vulnerability operations.
- Improvement Record created when the issue reveals a systemic control gap.

---

## Story 3: Audit request

### Situation

An external auditor requests evidence that privileged access reviews were performed for a SOX-relevant financial application during the prior quarter. The auditor asks for the review population, reviewer sign-off, exceptions, and evidence that removals were completed.

### CERG flow pattern

Primary flow: [F-07 Metrics, Oversight, and Improvement Routing](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#14-flow-f-07-metrics-oversight-and-improvement-routing)

Supporting procedures and standards:

- [Audit and Evidence Management Procedure](../../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md)
- [Evidence Quality Standard](../../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md)
- [Access Management Runbook](../../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md)
- [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md)
- [Compliance Matrix](../../governance/CERG-GOV-CMX-001_Compliance_Matrix.md)
- [Program Improvement Register](../../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md)

### Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Auditor requests privileged access review evidence for a defined system and period. | Auditor or Governance Pillar | Audit request ticket |
| 2 | Governance pulls the evidence index and maps the request to control, system, period, and required evidence quality tier. | Governance Pillar | Evidence index extract |
| 3 | Engineering supplies the IdP export, application role export, reviewer attestation, and removal tickets. | Engineering Pillar | IdP and application evidence |
| 4 | Risk explains open exceptions, overdue removals, or residual access risks that existed during the period. | Risk Pillar | Exception or Risk Record summary |
| 5 | Governance applies evidence quality rules and checks completeness, timestamp integrity, reviewer authority, population accuracy, and chain of custody. | Governance Pillar | Evidence quality assessment |
| 6 | If evidence gaps or control failures are found, they become program work rather than ad hoc audit responses. | Governance Pillar | Finding Record or Improvement Record |

### Example day-in-the-life narrative

The auditor sends the request on Tuesday afternoon. Governance translates the request into the control language used internally: quarterly privileged access review for the SOX-relevant finance application. The Evidence Librarian locates the prior quarter evidence package and sees that the reviewer attestation is present but the IdP export file name does not include the extraction timestamp.

Engineering regenerates a current export for comparison and supplies the original system-generated export from the access review tool. The application owner confirms that the review population included all privileged groups and all break-glass accounts. Two removals were requested during the review period, and Engineering links the completed removal tickets.

Risk adds context for one exception. A privileged service account could not be removed because a replacement integration was still being tested. The exception had compensating monitoring, a named owner, and an expiration date. Governance includes that explanation in the audit response package instead of letting the auditor infer that the exception was unmanaged.

Governance applies the evidence quality tier and identifies one improvement: export naming was inconsistent across applications. The audit response is completed, but the work does not stop there. Governance creates a program improvement item to standardize evidence naming and extraction metadata for all access reviews.

### Operational outputs

- Audit request mapped to control, system, period, and evidence requirements.
- Evidence package assembled from the evidence index.
- IdP, application, attestation, and removal evidence linked.
- Exceptions and risks explained with current status.
- Evidence quality tier applied.
- Findings or improvements created for evidence gaps.

---

## Story 4: Major cloud workload launch

### Situation

A product team is moving a customer-facing API from a data center to a cloud platform. The workload will use managed compute, managed database, object storage, secrets management, and centralized logging. The launch is tied to a business commitment, so the team needs clear security gates without creating avoidable delay.

### CERG flow pattern

Primary flows: [F-02 Project Intake, Architecture Review, and Threat Modeling](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#9-flow-f-02--project-intake-architecture-review-and-threat-modeling), [F-03 Asset Registration and Coverage Validation](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#10-flow-f-03--asset-registration-and-coverage-validation), and [F-05 Change and Release Security Routing](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#12-flow-f-05-change--release-security-routing)

Supporting procedures and standards:

- [Architecture Review and Project Intake Procedure](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)
- [Threat Modeling Procedure](../../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md)
- [Asset Management and Inventory Standard](../../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md)
- [IT, Cloud, and SaaS Security Standard](../../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md)
- [Logging, Monitoring, and Detection Standard](../../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)
- [Security Change Management Procedure](../../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md)

### Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Business submits the launch request with go-live date, customer impact, data types, and service owner. | Business Owner | Project Intake Record |
| 2 | Engineering reviews the reference architecture, network paths, identity model, encryption, secrets, and deployment pipeline. | Engineering Pillar | Architecture Review Record |
| 3 | Risk facilitates threat modeling because the workload is internet-facing and handles customer data. | Risk Pillar | Threat Model Record |
| 4 | Governance confirms the applicable cloud, logging, evidence, and change requirements before release approval. | Governance Pillar | Control conformance checklist |
| 5 | Engineering registers cloud assets, owners, criticality, data classification, monitoring coverage, and backup expectations. | Engineering Pillar | Asset Records |
| 6 | Risk validates residual launch risks, such as incomplete rate limiting or delayed DDoS testing, and determines whether an exception is needed. | Risk Pillar | Risk Record or Exception Record |
| 7 | Governance verifies release evidence and updates metrics for architecture reviews, threat models, asset coverage, and launch exceptions. | Governance Pillar | Reporting Metric Record |

### Example day-in-the-life narrative

The project arrives with a firm go-live date, so Engineering immediately routes it as a regulated internet-facing workload rather than a routine infrastructure change. The first architecture review identifies two issues: object storage needs explicit public-access blocking, and secrets must move from pipeline variables to the managed secrets service.

Risk runs a short threat model with the product team. The highest-priority scenario is credential theft leading to API abuse and data export. Engineering adds rate limiting, privileged workflow logging, and alerting for abnormal export volume. Governance confirms that the evidence package must include asset registration, logging validation, threat model decisions, and the final change approval.

Two days before launch, Engineering proves that logs are flowing to the SIEM and that cloud assets have owners and classifications. Risk accepts one low residual risk around delayed DDoS exercise completion with a 30-day due date. Governance confirms the exception is time-bound and visible in reporting. The release proceeds with clear ownership rather than informal verbal approval.

### Operational outputs

- Intake, architecture review, threat model, asset, and change records linked.
- Cloud assets registered with ownership, classification, and monitoring status.
- Logging and alerting evidence captured before go-live.
- Residual launch risks recorded with owners and due dates.
- Metrics updated for review cycle time, asset coverage, and exceptions.

---

## Story 5: Privileged access review finds excessive access

### Situation

A quarterly privileged access review finds that several users retained administrator access after changing roles. One account belongs to a contractor whose engagement ended two weeks earlier. The application supports a sensitive business process.

### CERG flow pattern

Primary flows: [F-04 Finding to Remediation, Exception, or Residual Risk](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#11-flow-f-04-finding--remediation-exception-or-residual-risk) and [F-07 Metrics, Oversight, and Improvement Routing](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#14-flow-f-07-metrics-oversight-and-improvement-routing)

Supporting procedures and standards:

- [Access Management Runbook](../../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md)
- [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md)
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
- [Audit and Evidence Management Procedure](../../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md)

### Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Governance identifies excessive privileged access during the scheduled review. | Governance Pillar | Access review evidence |
| 2 | Engineering removes access, disables stale accounts, and validates group membership after remediation. | Engineering Pillar | Access removal tickets |
| 3 | Risk evaluates whether the access created material exposure, whether activity review is needed, and whether the issue is systemic. | Risk Pillar | Finding Record |
| 4 | Governance checks evidence quality, reviewer sign-off, removal timestamps, and whether review SLA was met. | Governance Pillar | Evidence quality assessment |
| 5 | If access cannot be removed immediately, the owner requests a time-bound exception with monitoring or compensating controls. | Asset Owner | Exception Record |
| 6 | Metrics update for review completion, excessive access rate, removal cycle time, contractor access defects, and recurring findings. | Governance Pillar | Reporting Metric Record |
| 7 | Lessons learned feed standards, joiner-mover-leaver controls, contractor offboarding, or role engineering work. | Risk Pillar | Improvement Record |

### Example day-in-the-life narrative

Governance starts the quarterly review by pulling the privileged group membership and sending it to the approved application owner. The owner flags five users who no longer need administrator access. Engineering removes four immediately but discovers that the contractor account is still active in the IdP.

Risk opens a finding because the contractor access represents exposure after engagement end. Risk asks Engineering to review recent privileged activity and confirms that no suspicious activity is visible. Governance verifies that the reviewer decision, removal ticket, timestamped export, and validation export are all stored in the evidence package.

The team does not treat this as a one-off cleanup. Risk notices the same mover issue appeared in another application last quarter. Governance creates an improvement item to strengthen role-change triggers and contractor offboarding evidence. Engineering agrees to add automated group-owner notification when a privileged user changes department or employment type.

### Operational outputs

- Access review evidence completed and quality-checked.
- Excess access removed and independently validated.
- Finding opened for stale privileged access exposure.
- Exception created only where immediate removal is not possible.
- Metrics and program improvement items updated.

---

## Story 6: Third-party security incident notification

### Situation

A vendor notifies the organization that its file transfer platform was compromised. The organization uses the vendor to exchange operational reports with customers. The vendor cannot yet confirm whether customer files were accessed.

### CERG flow pattern

Primary flows: [F-06 Incident to Recovery to Standards Feedback](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#13-flow-f-06-incident--recovery-to-standards-feedback) and [F-04 Finding to Remediation, Exception, or Residual Risk](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#11-flow-f-04-finding--remediation-exception-or-residual-risk)

Supporting procedures and standards:

- [Incident Response Plan](../../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)
- [Incident Response Playbook Set](../../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md)
- [Third Party and Supply Chain Risk Procedure](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
- [Lessons Learned and Program Improvement Procedure](../../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md)

### Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Vendor notification is received and triaged for affected services, data, dates, and contract obligations. | Risk Pillar | Third-party incident record |
| 2 | Engineering identifies integrations, disables risky transfer paths if needed, rotates credentials, and preserves logs. | Engineering Pillar | Containment and log evidence |
| 3 | Governance confirms notification obligations, evidence requirements, decision logging, and executive reporting cadence. | Governance Pillar | Decision log and evidence index |
| 4 | Risk coordinates vendor questions, exposure analysis, and whether the event becomes an internal incident. | Risk Pillar | Incident Record or Risk Record |
| 5 | Engineering implements technical recovery actions, such as credential rotation, endpoint validation, and alternate transfer process. | Engineering Pillar | Change or recovery records |
| 6 | Governance tracks open actions, customer or regulator evidence needs, and metrics for third-party incident response. | Governance Pillar | Reporting Metric Record |
| 7 | Lessons learned update vendor requirements, contract clauses, monitoring expectations, or exit criteria. | Risk Pillar | Improvement Record |

### Example day-in-the-life narrative

The vendor notice arrives at 4:30 p.m. Risk opens the triage record and asks three questions immediately: what data types were exchanged, what dates are in scope, and what indicators or logs are available. Engineering identifies the integration owner, pauses scheduled transfers, rotates API credentials, and preserves local transfer logs.

Governance starts the decision log and confirms who will approve customer communications if data exposure is confirmed. The CISO receives a short status summary with known facts, unknowns, next decision time, and current containment actions. Risk pushes the vendor for file-level access evidence and maps the scenario to the vendor risk record.

The next morning, the vendor confirms that no organization files were accessed, but the vendor cannot meet the evidence quality the organization normally requires. Risk records residual third-party risk. Governance requires the evidence limitation to be visible in the file, not hidden in email. Engineering implements an alternate encrypted transfer path for the most sensitive reports until the vendor completes remediation.

### Operational outputs

- Third-party incident triage and decision log created.
- Integrations, credentials, and logs preserved or remediated.
- Vendor risk record updated with incident facts and residual risk.
- Governance evidence package prepared for executive, customer, or audit use.
- Vendor standards and contract requirements updated if gaps are found.

---

## Story 7: Enterprise AI assistant rollout

### Situation

A business function wants to deploy an enterprise AI assistant for summarizing documents, drafting communications, and searching internal knowledge. The tool may process confidential information and has browser, email, or document repository integrations.

### CERG flow pattern

Primary flow: [F-02 Project Intake, Architecture Review, and Threat Modeling](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#9-flow-f-02--project-intake-architecture-review-and-threat-modeling)

Supporting procedures and standards:

- [Artificial Intelligence Security Standard](../../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md)
- [Architecture Review and Project Intake Procedure](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)
- [Data Governance and Classification Standard](../../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md)
- [Access Management Standard](../../standards/CERG-STD-AC-001_Access_Management_Standard.md)
- [Third Party and Supply Chain Risk Procedure](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)

### Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Business submits the AI use case, user population, data sources, integrations, and desired productivity outcomes. | Business Owner | Project Intake Record |
| 2 | Governance confirms whether the use case is allowed, restricted, or prohibited under the AI standard and data classification rules. | Governance Pillar | AI use-case disposition |
| 3 | Engineering reviews identity integration, permissions inheritance, connector scope, logging, retention, and administrative controls. | Engineering Pillar | Architecture Review Record |
| 4 | Risk assesses vendor controls, model/data handling, prompt and output risks, sensitive data exposure, and abuse scenarios. | Risk Pillar | Vendor assessment and Threat Model Record |
| 5 | Governance defines required user guidance, evidence, monitoring metrics, and approval conditions for pilot or production rollout. | Governance Pillar | Control conformance checklist |
| 6 | Engineering implements scoped pilot access, connector restrictions, logging, and administrative guardrails. | Engineering Pillar | Implementation evidence |
| 7 | Risk reviews pilot outcomes and open risks before expansion. | Risk Pillar | Risk Record or approval notes |
| 8 | Metrics update for AI use cases reviewed, approved, restricted, exceptions, incidents, and user population. | Governance Pillar | Reporting Metric Record |

### Example day-in-the-life narrative

The business request starts as a simple productivity ask, but the intake reveals that the assistant will index internal documents and email content. Governance checks the AI standard and determines that the use case is allowed only as a controlled pilot because confidential information may be processed.

Engineering reviews the connector model and finds that the assistant inherits user permissions from the document repository. That reduces some risk, but Engineering still restricts the pilot to one business unit, disables unapproved external plugins, and enables admin audit logs. Risk reviews the vendor's data handling terms and threat models accidental oversharing, prompt injection through documents, and unauthorized connector expansion.

The pilot launches with user guidance, logging, and a named Business Owner. After 30 days, Risk reports no material incidents but identifies repeated attempts to use the assistant with restricted data. Governance updates the user guidance and requires a data-handling reminder before expansion. Engineering keeps connector approvals centralized until the control is proven stable.

### Operational outputs

- AI use case intake and disposition recorded.
- Architecture, vendor, data, and access reviews completed.
- Pilot restrictions and administrative controls evidenced.
- Risk review completed before broad rollout.
- Metrics updated for AI governance and adoption oversight.

---

## How to use these stories

- Use them in onboarding to explain how the three pillars interact without requiring every pillar to own every task.
- Use them in tabletop exercises to test whether local records, evidence stores, and dashboards can support the walkthrough.
- Use them during implementation planning to identify missing integrations between intake, ticketing, GRC, evidence storage, identity, vulnerability, and reporting systems.
- Adapt the roles, systems, and timing to your [Organization Adaptation Profile](../../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) without changing the underlying accountability model.
