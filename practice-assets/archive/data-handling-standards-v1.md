# Data Handling and Confidentiality Standards v1
## Practice Asset — Not a CERP Corpus Document

---

## Scope

These standards apply to all client data acquired, stored, processed, or transmitted during a CERG consulting engagement. They apply to every practitioner, contractor, and subcontractor working on the engagement.

---

## Data Classification

### Engagement Data Categories

| Category | Definition | Examples |
|---|---|---|
| **Client Confidential** | Information that identifies the client, their systems, their personnel, or their security posture | Client name, network diagrams, vulnerability reports, risk register entries, org chart, system inventories |
| **Client Rendered Corpus** | The adapted CERG markdown corpus produced for a client | Rendered policy documents, adapted standards, filled-in templates |
| **Practice IP** | Practice-owned tools, templates, methodologies | Practice asset library, intake forms, sector profiles |
| **Practice Operations** | Engagement metadata and anonymized data | Engagement tracker entries, client profile register (anonymized), debrief summaries |

### Handling Requirements

| Category | Storage | Transmission | Retention | Disposal |
|---|---|---|---|---|
| Client Confidential | Encrypted at rest; access-controlled by engagement team | Encrypted in transit (TLS 1.2+); never via unencrypted email | Until 90 days after engagement close; then client may request deletion | Secure deletion (shred files, wipe cloud storage) |
| Client Rendered Corpus | Client repository (client-owned) | Client repository access controls | Client determines | Client determines |
| Practice IP | Practice repository (access-controlled) | Practice repository | Indefinite | N/A |
| Practice Operations | Practice repository | Practice repository | Anonymized records: indefinite. Raw identifiers: deleted within 90 days | Anonymization before retention |

---

## Specific Rules

### Rule 1: No Client Data in Practice Templates

Practice templates (intake forms, scope documents, checklists) are stored in the practice repository with client data fields as `{{PLACEHOLDERS}}`. Completed versions are stored in the engagement file repository, not in the practice repository.

### Rule 2: Rendered Corpus Belongs to the Client

The adapted CERG corpus produced for a client is the client's asset. The practice retains a reference copy until the engagement close for support purposes. After close, the practice copy is deleted unless the client requests otherwise.

### Rule 3: Practice IP Stays with the Practice

Practice-owned templates, scripts, and methodologies are not transferred to the client unless explicitly licensed. Clients receive the rendered CERG corpus (which is open source + their adaptations) and the client-specific artifacts (risk register, improvement register). They do not receive the practice's internal process documentation.

### Rule 4: Anonymization Before Reuse

Any client-specific insight that the practice wants to retain for future engagements (e.g., "Financial Services clients consistently need help with SoD matrices") must be anonymized before entering the client profile register or practice knowledge base. Anonymization removes: client name, individual names, specific system names, and any information that would identify the client.

### Rule 5: Breach Notification

If practice systems containing client confidential data are breached, the Practice Principal notifies affected clients within 72 hours of discovery. Notification includes: what data was affected, what the practice has done to contain the breach, and recommended steps for the client.

---

## Practitioner Responsibilities

| Responsibility | Standard |
|---|---|
| Use practice-approved tools for all client work | No personal cloud storage, personal laptops, or unapproved SaaS |
| Encrypt client data at rest | Full-disk encryption on practice systems; encrypted cloud storage |
| Encrypt client data in transit | TLS 1.2+ for all file transfers; VPN for remote access to client systems |
| Clean up client data after engagement | Delete local copies within 30 days of handover unless client requests retention |
| Report potential breaches | Within 24 hours of discovery, report to Practice Principal |
